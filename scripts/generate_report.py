#!/usr/bin/env python3
# coding=utf-8
"""
finradar 每日综合报告生成器

汇总市场数据、Twitter、微信公众号、NewsNow热榜，
调用 DeepSeek API 生成 AI 分析摘要，输出为 Markdown 格式。

用法:
    python scripts/generate_report.py                    # 今天
    python scripts/generate_report.py --date 20260207    # 指定日期
    python scripts/generate_report.py --type morning     # 只生成早报
    python scripts/generate_report.py --type evening     # 只生成晚报
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from email.utils import parsedate_to_datetime
from html import unescape
import json
import math
import os
import sqlite3
import sys
import logging
import re
import time
from datetime import datetime, timedelta
from pathlib import Path
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

import requests
import yaml

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ── 路径 ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = PROJECT_ROOT / "config" / "config.yaml"
OUTPUT_MARKET = PROJECT_ROOT / "output" / "market"
OUTPUT_NEWS = PROJECT_ROOT / "output" / "news"
OUTPUT_REPORT = PROJECT_ROOT / "output" / "report"

DEFAULT_DEEPSEEK_BASE = "https://api.deepseek.com"
DEFAULT_DEEPSEEK_MODEL = "deepseek-chat"
DEFAULT_WEB_SEARCH_ENDPOINT = "https://news.google.com/rss/search"
BEIJING_TZ = ZoneInfo("Asia/Shanghai")


def now_beijing() -> datetime:
    """返回北京时间（带时区）。"""
    return datetime.now(BEIJING_TZ)


def get_social_section(social: dict, section_name: str) -> dict:
    """兼容 social 数据两种结构：{data:{twitter/wechat}} 或平铺结构。"""
    if not isinstance(social, dict):
        return {}
    data = social.get("data")
    if isinstance(data, dict):
        section = data.get(section_name, {})
        if isinstance(section, dict):
            return section
    section = social.get(section_name, {})
    return section if isinstance(section, dict) else {}


def normalize_deepseek_model(model_name: str) -> str:
    """将配置模型名标准化为 DeepSeek API 需要的 model 字段。"""
    if not model_name:
        return DEFAULT_DEEPSEEK_MODEL
    model_name = str(model_name).strip()
    if "/" in model_name:
        model_name = model_name.split("/", 1)[1]
    return model_name or DEFAULT_DEEPSEEK_MODEL


def resolve_deepseek_runtime(args_api_key: str | None) -> dict:
    """解析 DeepSeek 运行参数（key/base/model）。"""
    cfg = load_config()
    ai_cfg = cfg.get("ai", {}) if isinstance(cfg, dict) else {}
    api_key = args_api_key or os.environ.get("DEEPSEEK_API_KEY") or ai_cfg.get("api_key", "")
    api_base = os.environ.get("DEEPSEEK_API_BASE") or ai_cfg.get("api_base", "") or DEFAULT_DEEPSEEK_BASE
    model = normalize_deepseek_model(
        os.environ.get("DEEPSEEK_MODEL") or ai_cfg.get("model", DEFAULT_DEEPSEEK_MODEL)
    )
    return {
        "api_key": str(api_key).strip(),
        "api_base": str(api_base).rstrip("/"),
        "model": model,
        "config": cfg,
    }


def parse_datetime_flex(raw_value: str, day_hint: datetime | None = None) -> datetime | None:
    """解析多种时间格式。"""
    if raw_value is None:
        return None

    text = str(raw_value).strip()
    if not text:
        return None

    # 仅小时分钟，样例: "17-37" / "17:37"
    if re.match(r"^\d{2}[-:]\d{2}$", text):
        if day_hint is None:
            return None
        hour, minute = text.replace("-", ":").split(":")
        return day_hint.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)

    candidates = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
    ]
    for fmt in candidates:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue

    try:
        # 兼容 ISO 格式和带 Z 时区
        return datetime.fromisoformat(text.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        return None


def get_report_window(date_str: str, report_type: str) -> tuple[datetime, datetime]:
    """返回报告覆盖窗口（本地时间，左闭右开）。"""
    report_day = datetime.strptime(date_str, "%Y%m%d")
    if report_type == "morning":
        start_dt = (report_day - timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0)
        end_dt = report_day.replace(hour=8, minute=0, second=0, microsecond=0)
    else:
        start_dt = report_day.replace(hour=8, minute=0, second=0, microsecond=0)
        end_dt = report_day.replace(hour=20, minute=0, second=0, microsecond=0)
    return start_dt, end_dt


def parse_iso_datetime(raw_value) -> datetime | None:
    """解析 ISO 时间并统一为北京时间。"""
    if raw_value is None:
        return None
    text = str(raw_value).strip()
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=BEIJING_TZ)
    return dt.astimezone(BEIJING_TZ)


def report_anchor_datetime(date_str: str, report_type: str) -> datetime:
    """报告时效锚点：早报取当日08:00，晚报取当日20:00（北京时间）。"""
    day = datetime.strptime(date_str, "%Y%m%d").replace(tzinfo=BEIJING_TZ)
    hour = 8 if report_type == "morning" else 20
    return day.replace(hour=hour, minute=0, second=0, microsecond=0)


def hours_ago(anchor: datetime, ref: datetime | None) -> float:
    """计算 ref 相对 anchor 的小时差，缺失返回极大值。"""
    if ref is None:
        return 10_000.0
    return (anchor - ref).total_seconds() / 3600.0


def is_trading_day(date_str: str) -> bool:
    """简单交易日判断（周一到周五）。"""
    day = datetime.strptime(date_str, "%Y%m%d")
    return day.weekday() < 5


def market_snapshot_filter(market: dict, date_str: str, report_type: str) -> tuple[dict, list[str]]:
    """
    过滤市场快照，避免 AI 使用过时数据。
    返回: (filtered_market, notes)
    """
    filtered = deepcopy(market) if isinstance(market, dict) else {}
    data = filtered.get("data", {}) if isinstance(filtered, dict) else {}
    if not isinstance(data, dict):
        return filtered, ["市场数据结构异常，已跳过时效过滤"]

    notes: list[str] = []
    anchor = report_anchor_datetime(date_str, report_type)
    trade_day = is_trading_day(date_str)
    is_morning = report_type == "morning"

    def _drop(key: str, reason: str) -> None:
        if key in data:
            data.pop(key, None)
            notes.append(reason)

    stock = data.get("stock_cn")
    stock_ts = parse_iso_datetime(stock.get("timestamp")) if isinstance(stock, dict) else None
    stock_age = hours_ago(anchor, stock_ts)
    if is_morning:
        _drop("stock_cn", "早报阶段不纳入 A 股盘面，避免使用非交易时段快照")
    elif not trade_day:
        _drop("stock_cn", "非交易日，不纳入 A 股盘面")
    else:
        stock_day_ok = bool(stock_ts and stock_ts.date() == anchor.date())
        stock_time_ok = bool(stock_ts and stock_ts.hour >= 14)
        if not stock_day_ok or not stock_time_ok or stock_age > 12:
            _drop(
                "stock_cn",
                f"A 股快照时效不足（timestamp={stock_ts or 'N/A'}，距锚点约 {stock_age:.1f}h）",
            )

    futures = data.get("futures")
    if isinstance(futures, dict):
        futures_ts = parse_iso_datetime(futures.get("timestamp"))
        futures_age = hours_ago(anchor, futures_ts)
        if is_morning:
            # 早报仅保留国际期货，移除日盘主导的国内/股指期货
            futures.pop("commodity", None)
            futures.pop("index_futures", None)
            if not futures.get("international"):
                futures.pop("international", None)
            if not futures.get("international"):
                _drop("futures", "早报时段无可用国际期货快照")
            elif futures_age > 16:
                _drop("futures", f"国际期货快照过旧（timestamp={futures_ts or 'N/A'}，{futures_age:.1f}h）")
        else:
            if futures_age > 14:
                _drop("futures", f"期货快照过旧（timestamp={futures_ts or 'N/A'}，{futures_age:.1f}h）")

    pm = data.get("precious_metal")
    if isinstance(pm, dict):
        pm_ts = parse_iso_datetime(pm.get("timestamp"))
        pm_age = hours_ago(anchor, pm_ts)
        if pm_age > 16:
            _drop("precious_metal", f"贵金属快照过旧（timestamp={pm_ts or 'N/A'}，{pm_age:.1f}h）")

    crypto = data.get("crypto")
    if isinstance(crypto, dict):
        crypto_ts = parse_iso_datetime(crypto.get("timestamp"))
        crypto_age = hours_ago(anchor, crypto_ts)
        if crypto_age > 10:
            _drop("crypto", f"加密市场快照过旧（timestamp={crypto_ts or 'N/A'}，{crypto_age:.1f}h）")

    github = data.get("github")
    if isinstance(github, dict):
        gh_ts = parse_iso_datetime(github.get("timestamp"))
        gh_age = hours_ago(anchor, gh_ts)
        if gh_age > 72:
            _drop("github", f"GitHub 趋势快照过旧（timestamp={gh_ts or 'N/A'}，{gh_age:.1f}h）")

    yahoo_stock = data.get("yahoo_stock")
    if isinstance(yahoo_stock, dict):
        ys_ts = parse_iso_datetime(yahoo_stock.get("timestamp"))
        ys_age = hours_ago(anchor, ys_ts)
        max_age = 22 if is_morning else 36
        if ys_age > max_age:
            _drop("yahoo_stock", f"Yahoo Finance 股票快照过旧（timestamp={ys_ts or 'N/A'}，{ys_age:.1f}h）")
        elif not yahoo_stock.get("markets"):
            _drop("yahoo_stock", "Yahoo Finance 股票快照为空")

    if "us_stock" not in data and "yahoo_stock" not in data:
        notes.append("当前无可用美股直连行情源；美股解读仅来自 Twitter/热榜/联网检索文本证据")

    # 清理空壳字段
    for key in list(data.keys()):
        value = data.get(key)
        if isinstance(value, dict) and not value:
            data.pop(key, None)

    filtered["data"] = data
    return filtered, notes


def format_market_filter_notes(notes: list[str]) -> str:
    """格式化市场时效过滤说明。"""
    if not notes:
        return "市场时效过滤：未发现需要剔除的数据。"
    lines = ["市场时效过滤结果："]
    for idx, note in enumerate(notes, start=1):
        lines.append(f"{idx}. {note}")
    return "\n".join(lines)


# ══════════════════════════════════════════════════════
#  1. 数据读取
# ══════════════════════════════════════════════════════

def load_config():
    """读取 config.yaml"""
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_market_data(date_str: str) -> dict:
    """读取最新市场数据 (每30分钟更新的那个)"""
    path = OUTPUT_MARKET / f"market_data_{date_str}.json"
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def load_social_data(date_str: str, report_type: str = None) -> dict:
    """
    读取社交媒体数据 (早报/晚报)
    report_type: "morning" / "evening" / None(自动选最新)
    """
    if report_type:
        path = OUTPUT_MARKET / f"market_data_{date_str}_{report_type}.json"
        if path.exists():
            with open(path, encoding="utf-8") as f:
                return json.load(f)

    # 回退策略：
    # 1) 同日同类型 social 文件（按修改时间）
    # 2) 同日任意 social 文件（按修改时间）
    candidates = sorted(
        OUTPUT_MARKET.glob(f"market_data_{date_str}_*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if report_type:
        typed_candidates = []
        for c in candidates:
            try:
                with open(c, encoding="utf-8") as f:
                    d = json.load(f)
                if d.get("mode") == "social" and d.get("report_type") == report_type:
                    typed_candidates.append(d)
            except Exception:
                continue
        if typed_candidates:
            return typed_candidates[0]

    for c in candidates:
        with open(c, encoding="utf-8") as f:
            d = json.load(f)
        if d.get("mode") == "social":
            return d
    return {}


def is_weekend(date_str: str) -> tuple:
    """检测是否为周末及休市情况
    
    Returns:
        (is_weekend: bool, market_status: str)
        market_status 可能是: '正常交易', 'A股休市', '全市场休市'
    """
    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    dt = datetime.strptime(iso_date, "%Y-%m-%d")
    weekday = dt.weekday()  # 0=周一, 6=周日
    
    if weekday >= 5:  # 周六(5)或周日(6)
        return True, 'A股休市'
    return False, '正常交易'


def load_news_data(date_str: str, report_type: str) -> list:
    """按早报/晚报时间窗口读取 NewsNow 热榜数据。"""
    start_dt, end_dt = get_report_window(date_str, report_type)

    # 早报需跨天读取
    report_day = datetime.strptime(date_str, "%Y%m%d")
    days_to_scan = [report_day]
    if report_type == "morning":
        days_to_scan.insert(0, report_day - timedelta(days=1))

    dedup = {}
    for day in days_to_scan:
        db_path = OUTPUT_NEWS / f"{day.strftime('%Y-%m-%d')}.db"
        if not db_path.exists():
            continue

        conn = sqlite3.connect(str(db_path))
        rows = conn.execute(
            """
            SELECT n.title, p.name as platform, n.rank, n.url, n.first_crawl_time, n.last_crawl_time
            FROM news_items n
            JOIN platforms p ON n.platform_id = p.id
            WHERE n.rank <= 30
            ORDER BY n.last_crawl_time DESC, n.rank ASC
            """
        ).fetchall()
        conn.close()

        for title, platform, rank, url, first_time, last_time in rows:
            day_hint = day.replace(hour=0, minute=0, second=0, microsecond=0)
            first_dt = parse_datetime_flex(first_time, day_hint=day_hint)
            last_dt = parse_datetime_flex(last_time, day_hint=day_hint) or first_dt
            if last_dt is None:
                continue
            if not (start_dt <= last_dt < end_dt):
                continue

            key = title.strip()
            row_data = {
                "title": title,
                "platform": platform,
                "rank": rank,
                "url": url,
                "first_time": first_time,
                "last_time": last_time,
                "_last_dt": last_dt,
            }
            # 同标题保留窗口内更靠后的数据，若时间相同保留排名更高者
            if key not in dedup:
                dedup[key] = row_data
                continue

            old = dedup[key]
            if row_data["_last_dt"] > old["_last_dt"]:
                dedup[key] = row_data
            elif row_data["_last_dt"] == old["_last_dt"] and row_data["rank"] < old["rank"]:
                dedup[key] = row_data

    result = sorted(
        dedup.values(),
        key=lambda x: (x["_last_dt"], -int(x["rank"]) if str(x["rank"]).isdigit() else 0),
        reverse=True,
    )
    for item in result:
        item.pop("_last_dt", None)
    return result[:120]


# ══════════════════════════════════════════════════════
#  1.5 联网检索上下文
# ══════════════════════════════════════════════════════

def parse_bool(value, default: bool = False) -> bool:
    """将常见布尔文本安全转换为 bool。"""
    if value is None:
        return default
    text = str(value).strip().lower()
    if text in {"1", "true", "yes", "on", "y"}:
        return True
    if text in {"0", "false", "no", "off", "n"}:
        return False
    return default


def parse_keywords_arg(raw_keywords: str | None) -> list[str]:
    """解析关键词参数，支持中英文逗号/分号/换行。"""
    if not raw_keywords:
        return []
    parts = re.split(r"[,\n，;；]+", str(raw_keywords))
    keywords = []
    for part in parts:
        text = normalize_plain_text(part)
        if not text:
            continue
        text = text[:80]
        if text not in keywords:
            keywords.append(text)
    return keywords


def parse_rfc822_datetime(raw: str) -> datetime | None:
    """解析 RSS pubDate。"""
    if not raw:
        return None
    try:
        dt = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return None
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=BEIJING_TZ)
    return dt.astimezone(BEIJING_TZ)


def strip_html_tags(text: str) -> str:
    """去除 HTML 标签并压缩空白。"""
    plain = re.sub(r"<[^>]+>", " ", str(text or ""))
    plain = unescape(plain)
    return normalize_plain_text(plain)


def choose_market_queries(market: dict, iso_date: str, include_a_share: bool = True) -> list[str]:
    """从市场数据中提取较有解释价值的检索词。"""
    data = market.get("data", {}) if isinstance(market, dict) else {}
    queries: list[str] = [
        f"{iso_date} 全球市场 盘面 复盘 原因",
        f"{iso_date} 中国 宏观 经济 政策 市场 影响",
        f"{iso_date} AI 科技 行业 动态 影响",
    ]

    stock = data.get("stock_cn", {}) if isinstance(data, dict) else {}
    if include_a_share and isinstance(stock, dict):
        indices = [i for i in stock.get("indices", []) if isinstance(i, dict)]
        if indices:
            top_index = sorted(indices, key=lambda x: abs(float(x.get("change_pct", 0) or 0)), reverse=True)[0]
            idx_name = normalize_plain_text(top_index.get("name", "A股主要指数"))
            idx_change = float(top_index.get("change_pct", 0) or 0)
            direction = "上涨" if idx_change >= 0 else "下跌"
            queries.append(f"{idx_name} {direction} 原因")

    yahoo_stock = data.get("yahoo_stock", {}) if isinstance(data, dict) else {}
    if isinstance(yahoo_stock, dict):
        markets = [m for m in yahoo_stock.get("markets", []) if isinstance(m, dict)]
        if markets:
            top_market = sorted(markets, key=lambda x: abs(float(x.get("change_pct", 0) or 0)), reverse=True)[0]
            market_name = normalize_plain_text(top_market.get("name", top_market.get("symbol", "美股指数")))
            market_change = float(top_market.get("change_pct", 0) or 0)
            direction = "上涨" if market_change >= 0 else "下跌"
            queries.append(f"{market_name} {direction} 原因")

    crypto = data.get("crypto", {}) if isinstance(data, dict) else {}
    if isinstance(crypto, dict):
        coins = [c for c in crypto.get("coins", []) if isinstance(c, dict)]
        if coins:
            top_coin = sorted(coins, key=lambda x: abs(float(x.get("change_24h", 0) or 0)), reverse=True)[0]
            symbol = str(top_coin.get("symbol", "BTC")).upper()
            change = float(top_coin.get("change_24h", 0) or 0)
            direction = "上涨" if change >= 0 else "下跌"
            queries.append(f"{symbol} {direction} 原因")

    pm = data.get("precious_metal", {}) if isinstance(data, dict) else {}
    if isinstance(pm, dict):
        metals = [m for m in pm.get("metals", []) if isinstance(m, dict)]
        if metals:
            top_metal = sorted(metals, key=lambda x: abs(float(x.get("change_pct", 0) or 0)), reverse=True)[0]
            name = normalize_plain_text(top_metal.get("name", "黄金"))
            direction = "上涨" if float(top_metal.get("change_pct", 0) or 0) >= 0 else "下跌"
            queries.append(f"{name} {direction} 原因")

    return list(dict.fromkeys([q for q in queries if normalize_plain_text(q)]))


def choose_news_queries(news: list) -> list[str]:
    """从热榜中抽取标题作为检索提示。"""
    if not news:
        return []
    valid_items = [n for n in news if isinstance(n, dict)]
    if not valid_items:
        return []
    valid_items.sort(key=lambda x: news_rank_value(x.get("rank")))
    queries = []
    for item in valid_items[:4]:
        title = normalize_plain_text(item.get("title", ""))
        if not title:
            continue
        title = title[:36]
        queries.append(f"{title} 事件 背景")
    return list(dict.fromkeys(queries))


def build_web_search_queries(
    market: dict,
    news: list,
    iso_date: str,
    report_type: str,
    custom_keywords: list[str] | None = None,
) -> list[str]:
    """构建联网检索查询词（用户关键词优先）。"""
    if custom_keywords:
        return list(dict.fromkeys(custom_keywords))

    is_morning_report = report_type == "morning"
    queries = choose_market_queries(market, iso_date, include_a_share=not is_morning_report)
    queries.extend(choose_news_queries(news))
    return list(dict.fromkeys([q for q in queries if q]))[:8]


def fetch_google_news_rss(
    query: str,
    lookback: str = "1d",
    max_items: int = 8,
    timeout: int = 15,
    language: str = "zh-CN",
    country: str = "CN",
) -> list[dict]:
    """使用 Google News RSS 做轻量联网检索。"""
    query = normalize_plain_text(query)
    if not query:
        return []

    query_with_range = query
    if lookback and "when:" not in query.lower():
        query_with_range = f"{query} when:{lookback}"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    params = {
        "q": query_with_range,
        "hl": language,
        "gl": country,
        "ceid": f"{country}:{language}",
    }
    response = requests.get(DEFAULT_WEB_SEARCH_ENDPOINT, params=params, headers=headers, timeout=timeout)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    items: list[dict] = []
    for item in root.findall("./channel/item"):
        title = normalize_plain_text(item.findtext("title", ""))
        if not title:
            continue
        link = clean_external_url(item.findtext("link", ""))
        source_node = item.find("source")
        source = normalize_plain_text(source_node.text if source_node is not None else "") or "Google News"
        pub_raw = normalize_plain_text(item.findtext("pubDate", ""))
        pub_dt = parse_rfc822_datetime(pub_raw)
        pub_display = pub_dt.strftime("%Y-%m-%d %H:%M") if pub_dt else ""

        desc_html = item.findtext("description", "")
        snippet = strip_html_tags(desc_html)
        if snippet and title in snippet:
            snippet = normalize_plain_text(snippet.replace(title, "", 1))
        snippet = snippet[:220]

        items.append(
            {
                "query": query,
                "title": title,
                "source": source,
                "published_at": pub_display,
                "published_ts": pub_dt.timestamp() if pub_dt else 0,
                "snippet": snippet,
                "link": link,
            }
        )
        if len(items) >= max_items:
            break
    return items


def resolve_previous_report_path(date_str: str, report_type: str) -> Path | None:
    """定位上一期早晚报文件。"""
    report_day = datetime.strptime(date_str, "%Y%m%d")
    if report_type == "morning":
        prev_day = report_day - timedelta(days=1)
        candidate = OUTPUT_REPORT / f"daily_{prev_day.strftime('%Y%m%d')}_evening.md"
    else:
        candidate = OUTPUT_REPORT / f"daily_{date_str}_morning.md"
    return candidate if candidate.exists() else None


def load_previous_report_context(date_str: str, report_type: str, max_chars: int = 2200) -> str:
    """读取上一期 AI 摘要，补足上下文。"""
    prev_path = resolve_previous_report_path(date_str, report_type)
    if prev_path is None:
        return ""

    try:
        content = prev_path.read_text(encoding="utf-8")
    except OSError:
        return ""

    match = re.search(r"#\s+🤖\s+AI 分析摘要\s*(.*?)\n#\s+📋\s+原始数据", content, flags=re.S)
    excerpt = match.group(1).strip() if match else content
    excerpt = re.sub(r"<details>.*?</details>", "", excerpt, flags=re.S)
    excerpt = normalize_plain_text(excerpt)
    if len(excerpt) > max_chars:
        excerpt = excerpt[:max_chars] + "..."

    if not excerpt:
        return ""
    return f"上一期报告：{prev_path.name}\n{excerpt}"


def run_web_context_search(
    iso_date: str,
    report_type: str,
    market: dict,
    news: list,
    keywords: list[str] | None = None,
) -> dict:
    """执行联网检索并返回结构化上下文。"""
    keywords = keywords or []
    lookback_default = "2d" if report_type == "morning" else "1d"
    lookback = os.environ.get("WEB_CONTEXT_LOOKBACK", lookback_default).strip() or lookback_default
    max_queries = int(os.environ.get("WEB_CONTEXT_MAX_QUERIES", "8"))
    max_items_per_query = int(os.environ.get("WEB_CONTEXT_PER_QUERY", "6"))
    max_items_total = int(os.environ.get("WEB_CONTEXT_MAX_ITEMS", "24"))
    max_age_hours = int(os.environ.get("WEB_CONTEXT_MAX_AGE_HOURS", "72"))
    timeout = int(os.environ.get("WEB_CONTEXT_TIMEOUT", "18"))
    language = os.environ.get("WEB_CONTEXT_LANGUAGE", "zh-CN")
    country = os.environ.get("WEB_CONTEXT_COUNTRY", "CN")

    queries = build_web_search_queries(
        market=market,
        news=news,
        iso_date=iso_date,
        report_type=report_type,
        custom_keywords=keywords or None,
    )[:max_queries]
    if not queries:
        return {"queries": [], "items": [], "errors": []}

    results: list[dict] = []
    errors: list[str] = []
    workers = min(max(1, len(queries)), 4)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {
            executor.submit(
                fetch_google_news_rss,
                query,
                lookback,
                max_items_per_query,
                timeout,
                language,
                country,
            ): query
            for query in queries
        }
        for future in as_completed(future_map):
            query = future_map[future]
            try:
                rows = future.result()
                logger.info(f"🌐 联网检索 [{query}] 命中 {len(rows)} 条")
                results.extend(rows)
            except Exception as e:  # pragma: no cover - network dependent
                err = f"{query}: {e}"
                logger.warning(f"⚠️ 联网检索失败: {err}")
                errors.append(err)

    now_ts = now_beijing().timestamp()
    dedup_map: dict[tuple[str, str], dict] = {}
    for item in results:
        title = normalize_plain_text(item.get("title", "")).lower()
        source = normalize_plain_text(item.get("source", "")).lower()
        if not title:
            continue
        ts = float(item.get("published_ts", 0) or 0)
        if ts and (now_ts - ts) > max_age_hours * 3600:
            continue
        key = (title, source)
        old = dedup_map.get(key)
        if old is None or ts > float(old.get("published_ts", 0) or 0):
            dedup_map[key] = item

    dedup_items = sorted(dedup_map.values(), key=lambda x: float(x.get("published_ts", 0) or 0), reverse=True)
    for item in dedup_items:
        item.pop("published_ts", None)

    return {
        "queries": queries,
        "items": dedup_items[:max_items_total],
        "errors": errors,
    }


def format_web_context_for_ai(web_context: dict) -> str:
    """将联网检索结果压缩为 AI 可读文本。"""
    if not isinstance(web_context, dict):
        return "暂无联网检索补充"

    items = [i for i in web_context.get("items", []) if isinstance(i, dict)]
    if not items:
        return "暂无联网检索补充"

    queries = [q for q in web_context.get("queries", []) if isinstance(q, str)]
    lines = [
        f"联网检索共 {len(items)} 条（关键词: {', '.join(queries) if queries else '自动提取'}）"
    ]
    for idx, item in enumerate(items, start=1):
        published = item.get("published_at", "") or "-"
        source = item.get("source", "unknown")
        title = normalize_plain_text(item.get("title", ""))
        snippet = normalize_plain_text(item.get("snippet", ""))
        link = clean_external_url(item.get("link"))
        lines.append(f"{idx}. [{published}] {source} | {title}")
        if snippet:
            lines.append(f"   摘要: {snippet}")
        if link:
            lines.append(f"   链接: {link}")
    return "\n".join(lines)


def generate_web_context_section(web_context: dict) -> str:
    """生成报告中的联网检索来源区。"""
    if not isinstance(web_context, dict):
        return "## 🌐 联网检索补充\n\n暂无数据\n"

    queries = [q for q in web_context.get("queries", []) if isinstance(q, str)]
    items = [i for i in web_context.get("items", []) if isinstance(i, dict)]
    errors = [e for e in web_context.get("errors", []) if isinstance(e, str)]

    lines = ["## 🌐 联网检索补充\n"]
    if queries:
        lines.append(f"- 关键词：{', '.join(queries)}")
    if not items:
        lines.append("- 暂无可用检索结果（可能网络受限或关键词未命中）\n")
        if errors:
            lines.append("> 检索错误：")
            for err in errors[:3]:
                lines.append(f"> - {err}")
            lines.append("")
        return "\n".join(lines)

    lines.append(f"- 命中结果：{len(items)} 条（按发布时间倒序）\n")
    grouped: dict[str, list[dict]] = {}
    for item in items:
        query = normalize_plain_text(item.get("query", "")) or "自动查询"
        grouped.setdefault(query, []).append(item)

    for query, rows in grouped.items():
        lines.append(f"### 🔎 {query}\n")
        for row in rows[:6]:
            title = normalize_plain_text(row.get("title", ""))
            source = normalize_plain_text(row.get("source", "unknown"))
            published = row.get("published_at", "") or "-"
            link = clean_external_url(row.get("link"))
            snippet = normalize_plain_text(row.get("snippet", ""))
            if link:
                lines.append(f"- [{title}]({link})")
            else:
                lines.append(f"- {title}")
            lines.append(f"  - 来源: {source} | 时间: {published}")
            if snippet:
                lines.append(f"  - 摘要: {snippet}")
        lines.append("")

    if errors:
        lines.append("> 部分关键词检索失败（已自动跳过）：")
        for err in errors[:5]:
            lines.append(f"> - {err}")
        lines.append("")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════
#  2. 数据格式化（给 AI 的全量版）
# ══════════════════════════════════════════════════════

def format_market_for_ai(market: dict, include_a_share: bool = True) -> str:
    """格式化市场数据给 AI 分析（含板块指数，可按需排除 A 股盘面）。"""
    data = market.get("data", {})
    lines = []
    
    # A股主要指数/板块（早报可按需跳过）
    stock = data.get("stock_cn", {})
    if include_a_share:
        if stock and stock.get("market_closed"):
            lines.append(f"【A股】{stock.get('market_status', 'A股休市')}")
        if stock and stock.get("indices"):
            lines.append("【A股主要指数】")
            for idx in stock["indices"]:
                if isinstance(idx, dict):
                    lines.append(f"  {idx.get('name','')}: {idx.get('price',0):.2f} ({idx.get('change_pct',0):+.2f}%)")

        sectors = stock.get("sectors", []) if stock else []
        if sectors:
            sorted_sectors = sorted(
                [s for s in sectors if isinstance(s, dict) and s.get("change_pct") is not None],
                key=lambda x: x.get("change_pct", 0),
                reverse=True
            )
            if sorted_sectors:
                lines.append("【A股板块涨幅前15】")
                for s in sorted_sectors[:15]:
                    leader = f" (领涨: {s['leading_stock']})" if s.get("leading_stock") else ""
                    lines.append(f"  {s.get('name','')}: {s.get('change_pct',0):+.2f}%{leader}")
                lines.append("【A股板块跌幅前15】")
                for s in sorted_sectors[-15:]:
                    leader = f" (领跌: {s['leading_stock']})" if s.get("leading_stock") else ""
                    lines.append(f"  {s.get('name','')}: {s.get('change_pct',0):+.2f}%{leader}")

        north = stock.get("north_flow", {}) if stock else {}
        if north:
            lines.append("【北向资金】")
            for k, v in north.items():
                if isinstance(v, (int, float)):
                    lines.append(f"  {k}: {v:.2f}亿")

        mstats = stock.get("market_stats", {}) if stock else {}
        if mstats:
            lines.append("【市场统计】")
            for k, v in mstats.items():
                lines.append(f"  {k}: {v}")

    # Yahoo Finance 全球股票总览
    yahoo_stock = data.get("yahoo_stock", {})
    if isinstance(yahoo_stock, dict):
        markets = [m for m in yahoo_stock.get("markets", []) if isinstance(m, dict)]
        if markets:
            lines.append("【全球股票总览（Yahoo Finance）】")
            for item in markets:
                region = item.get("region", "全球")
                name = item.get("name", item.get("symbol", "未知"))
                symbol = item.get("symbol", "")
                currency = item.get("currency", "")
                try:
                    price = float(item.get("price", 0) or 0)
                except (TypeError, ValueError):
                    price = 0.0
                try:
                    change_pct = float(item.get("change_pct", 0) or 0)
                except (TypeError, ValueError):
                    change_pct = 0.0
                lines.append(
                    f"  [{region}] {name}({symbol}): {price} {currency} ({change_pct:+.2f}%)"
                )
            overview = yahoo_stock.get("overview", {})
            if isinstance(overview, dict):
                lines.append(
                    f"  统计: 上涨{overview.get('up', 0)} / 下跌{overview.get('down', 0)} / "
                    f"平盘{overview.get('flat', 0)} (总计{overview.get('total', len(markets))})"
                )
    
    # 贵金属
    pm = data.get("precious_metal", {})
    if pm and pm.get("metals"):
        lines.append("【贵金属】")
        for metal in pm["metals"]:
            if isinstance(metal, dict):
                lines.append(f"  {metal.get('name','')}: ${metal.get('price',0):.2f} ({metal.get('change_pct',0):+.2f}%)")
    
    # 加密货币
    crypto = data.get("crypto", {})
    if crypto and crypto.get("coins"):
        lines.append("【加密货币】")
        for coin in crypto["coins"]:
            if isinstance(coin, dict):
                lines.append(f"  {coin.get('symbol','').upper()}: ${coin.get('price',0):,.2f} ({coin.get('change_24h',0):+.2f}%)")
    
    # 期货
    futures = data.get("futures", {})
    if futures:
        cat_names = {"commodity": "国内商品期货", "international": "国际期货"}
        if include_a_share:
            cat_names["index_futures"] = "股指期货"
        for cat_key, cat_name in cat_names.items():
            items = futures.get(cat_key, [])
            if items:
                lines.append(f"【{cat_name}】")
                for item in items:
                    if isinstance(item, dict):
                        lines.append(f"  {item.get('name','')}: {item.get('price',0)} ({item.get('change_pct',0):+.2f}%)")
    
    return "\n".join(lines) if lines else "暂无市场数据"


def format_twitter_for_ai(social: dict) -> str:
    """格式化 Twitter 推文给 AI 分析（全量）"""
    twitter_data = get_social_section(social, "twitter")
    tweets = twitter_data.get("tweets", [])
    if not tweets:
        return "暂无 Twitter 数据"

    trending_count = sum(1 for t in tweets if isinstance(t, dict) and t.get("is_trending"))
    lines = [
        f"共 {len(tweets)} 条推文（热门讨论 {trending_count} 条，关注账号 {len(tweets) - trending_count} 条），内容如下："
    ]
    for t in tweets:
        if not isinstance(t, dict):
            continue
        username = t.get("username", "")
        text = t.get("text", "").replace("\n", " ").strip()
        created = t.get("created_at", "")[:16]
        tag = "热门" if t.get("is_trending") else "关注"
        engagement = f"❤️{t.get('likes', 0)} 🔁{t.get('retweets', 0)} 💬{t.get('replies', 0)}"
        lines.append(f"  [{tag}] @{username} [{created}] {engagement}: {text}")

    return "\n".join(lines)


def format_twitter_for_ai_compact(social: dict) -> str:
    """精简版 Twitter 文本（优先热门，控制长度），用于 AI 失败回退。"""
    twitter_data = get_social_section(social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict)]
    if not tweets:
        return "暂无 Twitter 数据"

    trending = [t for t in tweets if t.get("is_trending")]
    follow = [t for t in tweets if not t.get("is_trending")]

    trending_sorted = sorted(
        trending,
        key=lambda x: x.get("likes", 0) + x.get("retweets", 0) + x.get("replies", 0),
        reverse=True
    )[:40]
    follow_sorted = sorted(
        follow,
        key=lambda x: x.get("likes", 0) + x.get("retweets", 0) + x.get("replies", 0),
        reverse=True
    )[:30]

    selected = trending_sorted + follow_sorted
    lines = [f"精选 {len(selected)} 条推文（热门优先）:"]
    for t in selected:
        username = t.get("username", "")
        text = (t.get("text", "") or "").replace("\n", " ").strip()
        text = text[:280] + ("..." if len(text) > 280 else "")
        created = t.get("created_at", "")[:16]
        tag = "热门" if t.get("is_trending") else "关注"
        engagement = f"❤️{t.get('likes', 0)} 🔁{t.get('retweets', 0)} 💬{t.get('replies', 0)}"
        lines.append(f"  [{tag}] @{username} [{created}] {engagement}: {text}")
    return "\n".join(lines)


def format_wechat_for_ai(social: dict) -> str:
    """格式化微信公众号文章给 AI 分析（全量含正文）"""
    wechat_data = get_social_section(social, "wechat")
    articles = wechat_data.get("articles", [])
    if not articles:
        return "暂无微信公众号文章"

    hot_count = sum(1 for a in articles if isinstance(a, dict) and a.get("is_hot"))
    max_article_chars = int(os.environ.get("WECHAT_AI_MAX_ARTICLE_CHARS", "4000"))
    max_total_chars = int(os.environ.get("WECHAT_AI_MAX_TOTAL_CHARS", "180000"))
    current_chars = 0

    lines = [f"共 {len(articles)} 篇公众号文章（热门文章 {hot_count} 篇），内容如下："]
    for a in articles:
        if not isinstance(a, dict):
            continue
        account = a.get("account_name", "")
        title = a.get("title", "")
        digest = a.get("digest", "")
        content = a.get("content", "") or ""
        read_count = a.get("read_count", 0)
        like_count = a.get("like_count", 0)
        comment_count = a.get("comment_count", 0)
        is_hot = bool(a.get("is_hot", False))

        # 清理正文，优先使用正文，其次摘要
        content_text = re.sub(r"<[^>]+>", " ", content)
        content_text = re.sub(r"\s+", " ", content_text).strip()
        digest_text = re.sub(r"\s+", " ", str(digest or "")).strip()
        article_body = content_text or digest_text
        if len(article_body) > max_article_chars:
            article_body = article_body[:max_article_chars] + " ...(已截断)"

        block_lines = [
            f"\n  [{'热门' if is_hot else '关注'}] 【{account}】{title}",
            f"  数据: 阅读={read_count} 点赞={like_count} 评论={comment_count}",
        ]
        if digest_text:
            block_lines.append(f"  摘要: {digest_text}")
        if article_body:
            block_lines.append(f"  正文: {article_body}")

        block_text = "\n".join(block_lines)
        if current_chars + len(block_text) > max_total_chars:
            lines.append("\n  ...（为控制 token，后续文章省略）")
            break
        lines.append(block_text)
        current_chars += len(block_text)

    return "\n".join(lines)


def format_wechat_for_ai_compact(social: dict) -> str:
    """精简版微信公众号文本（标题+摘要+互动），用于风控回退。"""
    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict)]
    if not articles:
        return "暂无微信公众号文章"

    def score(a: dict) -> float:
        return (
            float(a.get("is_hot", False)) * 10000
            + float(a.get("read_count", 0))
            + float(a.get("like_count", 0)) * 10
            + float(a.get("comment_count", 0)) * 20
        )

    selected = sorted(articles, key=score, reverse=True)[:40]
    lines = [f"精选 {len(selected)} 篇公众号文章（按热度排序）:"]
    for a in selected:
        account = a.get("account_name", "")
        title = a.get("title", "")
        digest = re.sub(r"\s+", " ", str(a.get("digest", "") or "")).strip()
        digest = digest[:320] + ("..." if len(digest) > 320 else "")
        lines.append(
            f"  [{'热门' if a.get('is_hot') else '关注'}] 【{account}】{title} | "
            f"阅读={a.get('read_count',0)} 点赞={a.get('like_count',0)} 评论={a.get('comment_count',0)}"
        )
        if digest:
            lines.append(f"    摘要: {digest}")
    return "\n".join(lines)


def is_ai_failure(text: str) -> bool:
    """判断 AI 返回是否可用。"""
    if text is None:
        return True
    normalized = str(text).strip()
    if not normalized:
        return True
    return normalized.startswith("AI 分析失败")


def format_news_for_ai(news: list) -> str:
    """格式化 NewsNow 热榜给 AI 分析（全量）"""
    if not news:
        return "暂无热榜数据"
    
    lines = [f"共 {len(news)} 条热榜新闻，全部内容如下："]
    for n in news:
        lines.append(f"  [{n['platform']}] #{n['rank']} {n['title']}")
    
    return "\n".join(lines)


SUPERSCRIPT_DIGITS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def to_superscript(num: int) -> str:
    """将数字转为 Unicode 角标。"""
    return str(num).translate(SUPERSCRIPT_DIGITS)


def clean_external_url(value) -> str:
    """仅保留 http/https 链接。"""
    url = str(value or "").strip()
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return ""


def build_ai_citation_link_pools(market: dict, social: dict, news: list, web_context: dict | None = None) -> dict:
    """构建 AI 引用来源链接池。"""
    def _short(value: str, max_len: int = 72) -> str:
        text = normalize_plain_text(value)
        if len(text) <= max_len:
            return text
        return text[:max_len] + "..."

    pools = {
        "twitter": [],
        "wechat": [],
        "news": [],
        "github": [],
        "market": [],
        "web": [],
    }

    twitter_data = get_social_section(social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict) and clean_external_url(t.get("url"))]
    tweets_follow = [t for t in tweets if not t.get("is_trending")]
    tweets_hot = [t for t in tweets if t.get("is_trending")]
    tweets_follow_sorted = sorted(
        tweets_follow,
        key=lambda t: (tweet_engagement(t), str(t.get("created_at", ""))),
        reverse=True,
    )
    tweets_hot_sorted = sorted(
        tweets_hot,
        key=lambda t: (tweet_engagement(t), str(t.get("created_at", ""))),
        reverse=True,
    )
    tweets_sorted = tweets_follow_sorted + tweets_hot_sorted
    pools["twitter"] = [
        (
            f"{str(t.get('created_at', ''))[:16]} @{t.get('username', 'unknown')}",
            clean_external_url(t.get("url")),
        )
        for t in tweets_sorted
    ]

    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict) and clean_external_url(a.get("url"))]
    articles_follow = [a for a in articles if not a.get("is_hot")]
    articles_hot = [a for a in articles if a.get("is_hot")]
    articles_follow_sorted = sorted(
        articles_follow,
        key=lambda a: (wechat_article_score(a), str(a.get("publish_time", ""))),
        reverse=True,
    )
    articles_hot_sorted = sorted(
        articles_hot,
        key=lambda a: (wechat_article_score(a), str(a.get("publish_time", ""))),
        reverse=True,
    )
    articles_sorted = articles_follow_sorted + articles_hot_sorted
    pools["wechat"] = [
        (
            f"{str(a.get('publish_time', ''))[:16]} 【{a.get('account_name', '未知公众号')}】{_short(a.get('title', ''), 72)}",
            clean_external_url(a.get("url")),
        )
        for a in articles_sorted
    ]

    news_with_url = [n for n in news if isinstance(n, dict) and clean_external_url(n.get("url"))]
    pools["news"] = [
        (
            f"{n.get('platform', 'unknown')} #{n.get('rank', '-')} | {_short(n.get('title', ''), 72)}",
            clean_external_url(n.get("url")),
        )
        for n in news_with_url
    ]

    github_trending = (market.get("data", {}).get("github", {}) or {}).get("trending", []) or []
    github_with_url = [r for r in github_trending if isinstance(r, dict) and clean_external_url(r.get("url"))]
    pools["github"] = [
        (
            f"{(r.get('full_name') or r.get('name') or 'unknown')} | ⭐ {r.get('stars', 0)}",
            clean_external_url(r.get("url")),
        )
        for r in github_with_url
    ]

    # 市场数据来源尽量给出可点击外链，确保 Notion 中也可点击
    market_data = market.get("data", {}) if isinstance(market, dict) else {}
    market_sources: list[tuple[str, str]] = []
    if isinstance(market_data, dict):
        yahoo_stock = market_data.get("yahoo_stock", {}) if isinstance(market_data.get("yahoo_stock"), dict) else {}
        yahoo_markets = [
            m for m in yahoo_stock.get("markets", [])
            if isinstance(m, dict) and clean_external_url(m.get("url"))
        ]
        for row in yahoo_markets[:8]:
            name = row.get("name") or row.get("symbol") or "Yahoo 股票"
            symbol = row.get("symbol", "")
            market_sources.append((f"Yahoo Finance {name} ({symbol})", clean_external_url(row.get("url"))))
        if market_data.get("crypto"):
            market_sources.append(("CoinGecko API 文档", "https://www.coingecko.com/en/api/documentation"))
        if market_data.get("precious_metal") or (
            isinstance(market_data.get("futures"), dict) and market_data.get("futures", {}).get("international")
        ):
            market_sources.append(("Yahoo Finance 行情", "https://finance.yahoo.com"))
        if market_data.get("stock_cn") or market_data.get("futures"):
            market_sources.append(("AkShare 数据接口文档", "https://akshare.akfamily.xyz"))
    if not market_sources:
        market_sources.append(("AkShare 数据接口文档", "https://akshare.akfamily.xyz"))
    pools["market"] = market_sources

    web_items = []
    if isinstance(web_context, dict):
        web_items = [
            item for item in web_context.get("items", [])
            if isinstance(item, dict) and clean_external_url(item.get("link"))
        ]
    pools["web"] = [
        (
            f"{(item.get('published_at') or '-')[:16]} {item.get('source', 'Web')} | {_short(item.get('title', ''), 72)}",
            clean_external_url(item.get("link")),
        )
        for item in web_items
    ]

    return pools


def normalize_source_label_to_key(label: str) -> str | None:
    """将来源标签映射到统一 key。"""
    text = str(label or "").strip().lower()
    if not text:
        return None
    if "twitter" in text or "推特" in text:
        return "twitter"
    if "微信" in text:
        return "wechat"
    if "热榜" in text or "news" in text or "newsnow" in text:
        return "news"
    if "github" in text:
        return "github"
    if "联网" in text or "搜索" in text or "web" in text:
        return "web"
    if "市场" in text:
        return "market"
    return None


def convert_ai_source_tags_to_clickable_refs(
    ai_text: str,
    market: dict,
    social: dict,
    news: list,
    web_context: dict | None = None,
) -> tuple[str, str]:
    """
    将 AI 输出中的 [来源: xxx] 转成可点击角标链接，如 [¹](url)。
    并返回“引用脚注”区块。
    """
    if not ai_text:
        return ai_text, ""

    source_tag_pattern = re.compile(r"\[来源:\s*([^\]]+)\]")
    pools = build_ai_citation_link_pools(market, social, news, web_context=web_context)
    pointers = {k: 0 for k in pools.keys()}

    ref_records: list[tuple[int, str, str, str]] = []  # idx, source_key, title, url
    url_to_idx: dict[str, int] = {}

    def alloc_ref(source_key: str) -> tuple[int, str, str] | None:
        candidates = pools.get(source_key, [])
        if not candidates:
            return None

        ptr = pointers.get(source_key, 0)
        if ptr >= len(candidates):
            ptr = len(candidates) - 1  # 用最后一条兜底
        title, url = candidates[ptr]
        pointers[source_key] = min(ptr + 1, len(candidates))

        if not url:
            return None
        if url in url_to_idx:
            idx = url_to_idx[url]
            return idx, title, url

        idx = len(ref_records) + 1
        url_to_idx[url] = idx
        ref_records.append((idx, source_key, title, url))
        return idx, title, url

    def repl(match: re.Match) -> str:
        raw = match.group(1)
        parts = [p.strip() for p in re.split(r"[，,、/]+", raw) if p.strip()]
        tokens: list[str] = []
        for part in parts:
            key = normalize_source_label_to_key(part)
            if not key:
                continue
            ref = alloc_ref(key)
            if not ref:
                continue
            idx, _, url = ref
            sup = to_superscript(idx)
            tokens.append(f"[{sup}]({url})")
        if not tokens:
            return match.group(0)
        return "".join(tokens)

    converted = source_tag_pattern.sub(repl, ai_text)
    if not ref_records:
        return converted, ""

    lines = ["\n### 📎 引用脚注\n"]
    source_label = {
        "twitter": "Twitter",
        "wechat": "微信公众号",
        "news": "NewsNow热榜",
        "github": "GitHub",
        "market": "市场原始数据",
        "web": "联网检索",
    }
    for idx, source_key, title, url in ref_records:
        lines.append(f"{idx}. [{title}]({url})（{source_label.get(source_key, source_key)}）")

    return converted, "\n".join(lines) + "\n"


def get_deepseek_parallelism() -> int:
    """获取 DeepSeek 并发路数，默认 20 路。"""
    raw = os.environ.get("DEEPSEEK_PARALLELISM", "20")
    try:
        value = int(raw)
    except ValueError:
        logger.warning(f"⚠️ DEEPSEEK_PARALLELISM={raw} 非法，回退到 20")
        value = 20
    return max(1, min(20, value))


def split_evenly(items: list, parts: int) -> list[list]:
    """将列表尽量均匀拆成多份。"""
    if not items:
        return []
    parts = max(1, min(parts, len(items)))
    buckets = [[] for _ in range(parts)]
    for idx, item in enumerate(items):
        buckets[idx % parts].append(item)
    return [bucket for bucket in buckets if bucket]


NEWS_FINANCE_KEYWORDS = (
    "a股", "港股", "美股", "股市", "股票", "指数", "期货", "债", "债券", "收益率",
    "人民币", "美元", "汇率", "利率", "cpi", "pmi", "非农", "通胀", "降息", "加息",
    "黄金", "白银", "原油", "天然气", "铜", "煤", "比特币", "btc", "eth", "sol",
    "ai", "算力", "芯片", "科技", "再融资", "证监", "交易所", "财联社", "wind"
)
NEWS_PLATFORM_BONUS = ("财联社", "华尔街", "wind", "证券", "财经")
NEWS_RISK_TERMS = (
    "爱泼斯坦", "epstein", "强奸", "性侵", "猥亵", "恋童", "血", "死亡", "谋杀", "自杀", "恐怖"
)


def news_rank_value(raw_rank) -> int:
    """将热榜排名转为整数，失败时给较低优先级。"""
    try:
        return int(raw_rank)
    except Exception:
        return 99


def sanitize_news_title_for_ai(title: str) -> str:
    """对少量高风险词做脱敏，降低模型风控触发概率。"""
    text = normalize_plain_text(title)
    for term in NEWS_RISK_TERMS:
        text = re.sub(re.escape(term), "敏感事件", text, flags=re.IGNORECASE)
    return text


def news_item_score(item: dict) -> float:
    """热榜条目评分：金融/科技相关优先、高排名优先。"""
    title = normalize_plain_text(item.get("title", "")).lower()
    platform = normalize_plain_text(item.get("platform", "")).lower()
    rank = news_rank_value(item.get("rank"))
    score = max(0, 31 - rank) * 3
    if any(k in title for k in NEWS_FINANCE_KEYWORDS):
        score += 100
    if any(p in platform for p in NEWS_PLATFORM_BONUS):
        score += 30
    return score


def build_news_chunks(news: list, parts: int) -> list[list]:
    """按相关度切分热榜，供并行分析。"""
    items = [n for n in news if isinstance(n, dict)]
    if not items:
        return []
    items_sorted = sorted(
        items,
        key=lambda x: (news_item_score(x), -news_rank_value(x.get("rank"))),
        reverse=True,
    )
    chunk_size = max(8, int(os.environ.get("NEWS_AI_CHUNK_SIZE", "18")))
    chunk_count = max(1, (len(items_sorted) + chunk_size - 1) // chunk_size)
    chunk_count = max(1, min(parts, chunk_count))
    return split_evenly(items_sorted, chunk_count)


def format_news_chunk_for_ai(chunk: list, idx: int, total: int) -> str:
    """格式化热榜分片文本。"""
    lines = [f"热榜分片 {idx}/{total}，共 {len(chunk)} 条："]
    for n in chunk:
        platform = n.get("platform", "unknown")
        rank = n.get("rank", "-")
        title = sanitize_news_title_for_ai(str(n.get("title", "")))
        lines.append(f"  [{platform}] #{rank} {title}")
    return "\n".join(lines)


def format_news_chunk_for_ai_compact(chunk: list, idx: int, total: int) -> str:
    """格式化热榜精简分片文本（分片重试用）。"""
    selected = sorted(chunk, key=news_item_score, reverse=True)[:10]
    lines = [f"热榜精简分片 {idx}/{total}，共 {len(selected)} 条："]
    for n in selected:
        platform = n.get("platform", "unknown")
        rank = n.get("rank", "-")
        title = sanitize_news_title_for_ai(str(n.get("title", "")))
        if len(title) > 80:
            title = title[:80] + "..."
        lines.append(f"  [{platform}] #{rank} {title}")
    return "\n".join(lines)


def generate_news_rule_based_summary(news: list) -> str:
    """热榜 AI 全部失败时的规则化降级摘要。"""
    items = [n for n in news if isinstance(n, dict)]
    if not items:
        return "暂无热榜数据"

    items_sorted = sorted(items, key=news_item_score, reverse=True)
    top_common = items_sorted[:8]
    finance_items = [n for n in items_sorted if any(k in normalize_plain_text(n.get("title", "")).lower() for k in NEWS_FINANCE_KEYWORDS)][:8]
    ai_items = [n for n in items_sorted if any(k in normalize_plain_text(n.get("title", "")).lower() for k in ("ai", "人工智能", "算力", "芯片", "科技"))][:6]

    def _fmt(item: dict) -> str:
        return f"- [{item.get('platform', 'unknown')} #{item.get('rank', '-')}] {normalize_plain_text(item.get('title', ''))}"

    lines = [
        "⚠️ 热榜 AI 分析触发风控，已自动回退为规则化摘要（基于原始热榜排序与关键词提取）。",
        "",
        "#### 跨平台高频热点（Top 8）",
    ]
    lines.extend(_fmt(x) for x in top_common)

    lines.append("")
    lines.append("#### 金融市场相关")
    if finance_items:
        lines.extend(_fmt(x) for x in finance_items[:6])
    else:
        lines.append("- 未识别到明显金融关键词（数据不足/未提供）。")

    lines.append("")
    lines.append("#### 科技/AI 相关")
    if ai_items:
        lines.extend(_fmt(x) for x in ai_items[:6])
    else:
        lines.append("- 未识别到明显 AI 关键词（数据不足/未提供）。")

    lines.append("")
    lines.append("#### 社会舆论焦点")
    lines.extend(_fmt(x) for x in top_common[:5])
    return "\n".join(lines)


def tweet_engagement(tweet: dict) -> int:
    """计算推文互动分。"""
    return int(tweet.get("likes", 0)) + int(tweet.get("retweets", 0)) + int(tweet.get("replies", 0))


def build_twitter_chunks(social: dict, parts: int) -> list[list]:
    """按互动热度切分 Twitter 推文，供并行分析。"""
    twitter_data = get_social_section(social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict)]
    if not tweets:
        return []
    tweets_sorted = sorted(tweets, key=tweet_engagement, reverse=True)
    return split_evenly(tweets_sorted, parts)


def format_twitter_chunk_for_ai(chunk: list, idx: int, total: int) -> str:
    """格式化 Twitter 分片文本。"""
    lines = [f"Twitter 分片 {idx}/{total}，共 {len(chunk)} 条推文："]
    for t in chunk:
        username = t.get("username", "")
        text = (t.get("text", "") or "").replace("\n", " ").strip()
        text = text[:360] + ("..." if len(text) > 360 else "")
        created = t.get("created_at", "")[:16]
        tag = "热门" if t.get("is_trending") else "关注"
        engagement = f"❤️{t.get('likes', 0)} 🔁{t.get('retweets', 0)} 💬{t.get('replies', 0)}"
        lines.append(f"  [{tag}] @{username} [{created}] {engagement}: {text}")
    return "\n".join(lines)


def format_twitter_chunk_for_ai_compact(chunk: list, idx: int, total: int) -> str:
    """格式化 Twitter 精简分片文本（分片重试用）。"""
    selected = sorted(chunk, key=tweet_engagement, reverse=True)[:8]
    lines = [f"Twitter 精简分片 {idx}/{total}，共 {len(selected)} 条推文："]
    for t in selected:
        username = t.get("username", "")
        text = (t.get("text", "") or "").replace("\n", " ").strip()
        text = text[:220] + ("..." if len(text) > 220 else "")
        tag = "热门" if t.get("is_trending") else "关注"
        engagement = f"❤️{t.get('likes', 0)} 🔁{t.get('retweets', 0)} 💬{t.get('replies', 0)}"
        lines.append(f"  [{tag}] @{username} {engagement}: {text}")
    return "\n".join(lines)


def wechat_article_score(article: dict) -> float:
    """微信公众号文章评分：热门优先，其次互动量。"""
    return (
        float(article.get("is_hot", False)) * 10000
        + float(article.get("read_count", 0))
        + float(article.get("like_count", 0)) * 10
        + float(article.get("comment_count", 0)) * 20
    )


def normalize_plain_text(text: str) -> str:
    """清理空白，压缩为单行文本。"""
    return re.sub(r"\s+", " ", str(text or "")).strip()


AI_PREFACE_LINE_RE = re.compile(
    r"^(好的|当然|明白|收到|以下|下面|作为|根据您|基于您|我将|我会|很高兴|感谢|可以|没问题)"
)


def sanitize_ai_response_text(text: str) -> str:
    """
    清洗模型输出中的对话式前缀，保留结构化正文。
    例如去掉“好的，作为……我将……”，直接从标题/要点开始。
    """
    cleaned = str(text or "").replace("\r\n", "\n").strip()
    if not cleaned:
        return ""

    # 若存在结构化标题且前缀是客套句，直接裁切到标题起点
    heading_positions = []
    for marker in ("## 一、摘要", "## 摘要", "## 二、分板块汇报", "### 2.1"):
        pos = cleaned.find(marker)
        if pos >= 0:
            heading_positions.append(pos)
    if heading_positions:
        first_heading_pos = min(heading_positions)
        if first_heading_pos > 0:
            preface_text = cleaned[:first_heading_pos]
            if re.search(r"(好的|作为|我将|我会|根据您|基于您|以下|下面)", preface_text):
                cleaned = cleaned[first_heading_pos:].lstrip()

    lines = cleaned.splitlines()
    while lines:
        first = lines[0].strip()
        if not first:
            lines.pop(0)
            continue
        if first.startswith("#"):
            break
        if AI_PREFACE_LINE_RE.match(first) and len(lines) > 1:
            lines.pop(0)
            while lines and not lines[0].strip():
                lines.pop(0)
            continue
        break

    return "\n".join(lines).strip()


WECHAT_TOPIC_STOPWORDS = {
    "今天", "今日", "最新", "重磅", "市场", "行业", "公司", "中国", "美国", "我们", "你们",
    "已经", "继续", "相关", "进行", "发布", "报道", "观点", "影响", "数据", "分析", "财经",
    "金融", "投资", "风险", "关注", "什么", "如何", "这个", "那个", "一次", "本次", "以及",
}


def text_tokens_for_topic(text: str) -> list[str]:
    """提取中英文主题词（轻量规则）。"""
    plain = normalize_plain_text(text).lower()
    tokens: list[str] = []
    for zh in re.findall(r"[\u4e00-\u9fff]{2,8}", plain):
        if zh in WECHAT_TOPIC_STOPWORDS:
            continue
        tokens.append(zh)
    for en in re.findall(r"[a-z][a-z0-9\\-]{2,24}", plain):
        if en in {"the", "and", "for", "with", "from", "that", "this", "are", "was", "were", "can"}:
            continue
        tokens.append(en)
    return tokens


def build_wechat_consensus_and_signal_text(social: dict) -> str:
    """提取“跨公众号共识议题 + 弱信号”。"""
    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict)]
    if not articles:
        return "暂无微信公众号数据"

    token_map: dict[str, dict] = {}
    for article in articles:
        account = normalize_plain_text(article.get("account_name", "") or "未知公众号")
        title = normalize_plain_text(article.get("title", ""))
        digest = normalize_plain_text(article.get("digest", ""))
        if not title:
            continue

        text = f"{title} {digest}"
        uniq_tokens = set(text_tokens_for_topic(text))
        for token in uniq_tokens:
            bucket = token_map.setdefault(token, {"accounts": set(), "count": 0, "samples": []})
            bucket["accounts"].add(account)
            bucket["count"] += 1
            if len(bucket["samples"]) < 3:
                bucket["samples"].append((account, title))

    topic_rows = []
    for token, meta in token_map.items():
        account_count = len(meta["accounts"])
        if account_count < 2:
            continue
        score = account_count * 10 + int(meta["count"])
        topic_rows.append((score, token, meta))
    topic_rows.sort(reverse=True)

    lines = []
    if topic_rows:
        lines.append("跨公众号共识议题（出现于 2 个及以上公众号）：")
        for idx, (_, token, meta) in enumerate(topic_rows[:8], start=1):
            accounts = sorted(meta["accounts"])[:4]
            sample_titles = [f"《{title}》" for _, title in meta["samples"][:2]]
            lines.append(
                f"{idx}. 议题={token} | 覆盖={len(meta['accounts'])}个公众号 | "
                f"样例={ ' / '.join(sample_titles) if sample_titles else '无' } | "
                f"账号={ '、'.join(accounts) }"
            )
    else:
        lines.append("跨公众号共识议题：暂无明显重合")

    scored_articles = sorted(articles, key=wechat_article_score, reverse=True)
    weak_rows = []
    for article in scored_articles:
        title = normalize_plain_text(article.get("title", ""))
        if not title:
            continue
        account = normalize_plain_text(article.get("account_name", "") or "未知公众号")
        read_count = int(article.get("read_count", 0) or 0)
        like_count = int(article.get("like_count", 0) or 0)
        comment_count = int(article.get("comment_count", 0) or 0)
        signal_score = read_count + like_count * 15 + comment_count * 25
        if signal_score < 150:
            continue
        weak_rows.append((signal_score, account, title, read_count, like_count, comment_count))
    weak_rows.sort(reverse=True)

    lines.append("")
    lines.append("弱信号候选（单篇互动较高、可能提前反映资金/产业关注）：")
    if weak_rows:
        for idx, (score, account, title, read_count, like_count, comment_count) in enumerate(weak_rows[:6], start=1):
            lines.append(
                f"{idx}. 【{account}】《{title}》 | 互动分={score} "
                f"(阅读{read_count}/点赞{like_count}/评论{comment_count})"
            )
    else:
        lines.append("1. 暂无明显弱信号候选")

    return "\n".join(lines)


def is_mostly_english(text: str) -> bool:
    """粗略判断是否英文为主。"""
    raw = str(text or "")
    if not raw:
        return False
    en = len(re.findall(r"[A-Za-z]", raw))
    zh = len(re.findall(r"[\u4e00-\u9fff]", raw))
    return en >= max(24, zh * 2)


def format_twitter_focus_for_ai(social: dict) -> str:
    """提取 Twitter 英文/中文重点推文，供结构化汇报。"""
    twitter_data = get_social_section(social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict)]
    if not tweets:
        return "暂无 Twitter 数据"

    tweets = sorted(tweets, key=tweet_engagement, reverse=True)
    en_tweets = [t for t in tweets if is_mostly_english(t.get("text", ""))]
    zh_tweets = [t for t in tweets if not is_mostly_english(t.get("text", ""))]

    lines = [
        f"Twitter 高互动样本：英文 {len(en_tweets)} 条，非英文 {len(zh_tweets)} 条（按互动排序）"
    ]

    lines.append("\n英文重点（请在最终报告中翻译成中文并保留关键信号）：")
    for idx, t in enumerate(en_tweets[:20], start=1):
        text = normalize_plain_text(t.get("text", ""))[:280]
        lines.append(
            f"{idx}. @{t.get('username','unknown')} | {tweet_engagement(t)} 互动 | "
            f"{str(t.get('created_at',''))[:16]} | {text}"
        )

    lines.append("\n中文/其他语种补充：")
    for idx, t in enumerate(zh_tweets[:12], start=1):
        text = normalize_plain_text(t.get("text", ""))[:220]
        lines.append(
            f"{idx}. @{t.get('username','unknown')} | {tweet_engagement(t)} 互动 | "
            f"{str(t.get('created_at',''))[:16]} | {text}"
        )

    return "\n".join(lines)


REPO_THEME_KEYWORDS = {
    "fintech": ("quant", "trading", "finance", "fintech", "risk", "portfolio", "payment", "broker", "bank"),
    "web3": ("web3", "blockchain", "defi", "wallet", "ethereum", "bitcoin", "solidity", "token", "nft", "zk"),
    "ai": ("ai", "llm", "agent", "gpt", "rag", "diffusion", "model", "inference", "prompt"),
}


def github_repo_theme(repo: dict) -> str:
    """识别 GitHub 项目主题（金融科技/AI/Web3/通用）。"""
    text = normalize_plain_text(
        f"{repo.get('name','')} {repo.get('full_name','')} {repo.get('description','')} {repo.get('language','')}"
    ).lower()
    scores = {k: 0 for k in REPO_THEME_KEYWORDS}
    for theme, words in REPO_THEME_KEYWORDS.items():
        for word in words:
            if word in text:
                scores[theme] += 1
    theme, score = max(scores.items(), key=lambda x: x[1])
    if score == 0:
        return "general"
    return theme


def github_repo_score(repo: dict) -> float:
    """GitHub 项目排序分，兼顾热度与主题相关性。"""
    stars = float(repo.get("stars", 0) or 0)
    theme = github_repo_theme(repo)
    bonus = {"fintech": 40.0, "ai": 28.0, "web3": 24.0, "general": 0.0}.get(theme, 0.0)
    return math.log1p(max(stars, 0.0)) * 12.0 + bonus


def build_github_focus_snapshot(market: dict, top_n: int = 18) -> list[dict]:
    """抽取 GitHub 重点项目（融合 trending + ai_trending）。"""
    github_data = (market.get("data", {}) or {}).get("github", {}) if isinstance(market, dict) else {}
    if not isinstance(github_data, dict):
        return []

    merged: list[dict] = []
    seen = set()
    for key in ("trending", "ai_trending"):
        rows = github_data.get(key, []) or []
        for repo in rows:
            if not isinstance(repo, dict):
                continue
            repo_key = repo.get("full_name") or repo.get("url") or repo.get("name")
            if not repo_key or repo_key in seen:
                continue
            seen.add(repo_key)
            copied = dict(repo)
            copied["theme"] = github_repo_theme(repo)
            copied["score"] = github_repo_score(repo)
            merged.append(copied)

    merged.sort(key=lambda x: (x.get("score", 0), float(x.get("stars", 0) or 0)), reverse=True)
    return merged[:top_n]


def format_github_focus_for_ai(market: dict) -> str:
    """格式化 GitHub 热门项目重点，强调金融科技/AI/Web3。"""
    repos = build_github_focus_snapshot(market)
    if not repos:
        return "暂无 GitHub 趋势数据"

    lines = [f"GitHub 重点项目 {len(repos)} 个（按热度+主题相关性排序）："]
    grouped: dict[str, list[dict]] = {"fintech": [], "ai": [], "web3": [], "general": []}
    for repo in repos:
        grouped.setdefault(repo.get("theme", "general"), []).append(repo)

    label_map = {"fintech": "金融科技", "ai": "AI", "web3": "Web3", "general": "通用开发"}
    for theme in ("fintech", "ai", "web3", "general"):
        rows = grouped.get(theme, [])
        if not rows:
            continue
        lines.append(f"\n[{label_map.get(theme, theme)}] {len(rows)} 个：")
        for idx, repo in enumerate(rows[:8], start=1):
            name = repo.get("full_name") or repo.get("name") or "unknown"
            desc = normalize_plain_text(repo.get("description", ""))[:180]
            lang = repo.get("language", "Unknown")
            stars = int(float(repo.get("stars", 0) or 0))
            lines.append(f"{idx}. {name} | ⭐{stars} | {lang} | {desc}")
    return "\n".join(lines)


def extract_wechat_article_body(article: dict, max_chars: int) -> tuple[str, str]:
    """提取并截断公众号文章正文。"""
    digest = normalize_plain_text(article.get("digest", "") or "")
    content = normalize_plain_text(re.sub(r"<[^>]+>", " ", str(article.get("content", "") or "")))
    body = content or digest
    if len(body) > max_chars:
        body = body[:max_chars] + " ...(已截断)"
    return digest, body


def build_wechat_chunks(social: dict, parts: int) -> list[list]:
    """按热度切分微信公众号文章，供并行分析。"""
    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict)]
    if not articles:
        return []
    articles_sorted = sorted(articles, key=wechat_article_score, reverse=True)
    return split_evenly(articles_sorted, parts)


def format_wechat_chunk_for_ai(chunk: list, idx: int, total: int) -> str:
    """格式化微信公众号分片文本（含正文片段）。"""
    max_article_chars = int(os.environ.get("WECHAT_AI_CHUNK_ARTICLE_CHARS", "1200"))
    lines = [f"微信公众号分片 {idx}/{total}，共 {len(chunk)} 篇："]
    for a in chunk:
        account = a.get("account_name", "")
        title = a.get("title", "")
        pub_time = str(a.get("publish_time", ""))[:16]
        digest, body = extract_wechat_article_body(a, max_article_chars)
        lines.append(
            f"\n  [{'热门' if a.get('is_hot') else '关注'}] 【{account}】{title} [{pub_time}]"
        )
        lines.append(
            f"  数据: 阅读={a.get('read_count',0)} 点赞={a.get('like_count',0)} 评论={a.get('comment_count',0)}"
        )
        if digest:
            lines.append(f"  摘要: {digest}")
        if body:
            lines.append(f"  正文片段: {body}")
    return "\n".join(lines)


def format_wechat_chunk_for_ai_compact(chunk: list, idx: int, total: int) -> str:
    """格式化微信公众号精简分片文本（分片重试用）。"""
    lines = [f"微信公众号精简分片 {idx}/{total}，共 {len(chunk)} 篇："]
    for a in chunk:
        account = a.get("account_name", "")
        title = a.get("title", "")
        pub_time = str(a.get("publish_time", ""))[:16]
        digest = normalize_plain_text(a.get("digest", "") or "")
        digest = digest[:320] + ("..." if len(digest) > 320 else "")
        lines.append(
            f"  [{'热门' if a.get('is_hot') else '关注'}] 【{account}】{title} [{pub_time}] | "
            f"阅读={a.get('read_count',0)} 点赞={a.get('like_count',0)} 评论={a.get('comment_count',0)}"
        )
        if digest:
            lines.append(f"    摘要: {digest}")
    return "\n".join(lines)


def parallel_chunk_analysis(section_name: str,
                            chunks: list[list],
                            system_prompt: str,
                            user_prompt_builder,
                            api_key: str,
                            api_base: str,
                            model: str,
                            max_tokens: int = 1400,
                            temperature: float = 0.6,
                            fallback_system_prompt: str | None = None,
                            fallback_user_prompt_builder=None) -> list[str]:
    """并行执行分片分析，返回按分片顺序排列的摘要列表。"""
    if not chunks:
        return []

    workers = min(get_deepseek_parallelism(), len(chunks))
    logger.info(f"🚀 [{section_name}] 分片并行分析：{len(chunks)} 块，{workers} 路并发")
    results = {}
    chunk_map = {idx: chunk for idx, chunk in enumerate(chunks, start=1)}

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {}
        for idx, chunk in enumerate(chunks, start=1):
            prompt = user_prompt_builder(chunk, idx, len(chunks))
            future = executor.submit(
                call_deepseek,
                system_prompt,
                prompt,
                api_key,
                api_base,
                model,
                max_tokens,
                temperature
            )
            future_map[future] = idx

        for future in as_completed(future_map):
            idx = future_map[future]
            try:
                results[idx] = future.result()
            except Exception as e:
                logger.error(f"❌ [{section_name}] 分片 {idx} 异常: {e}")
                results[idx] = f"AI 分析失败: chunk {idx} exception: {e}"
            if is_ai_failure(results[idx]) and fallback_user_prompt_builder is not None:
                logger.warning(f"⚠️ [{section_name}] 分片 {idx} 进入精简重试")
                fallback_prompt = fallback_user_prompt_builder(chunk_map[idx], idx, len(chunks))
                retry_result = call_deepseek(
                    fallback_system_prompt or system_prompt,
                    fallback_prompt,
                    api_key,
                    api_base,
                    model,
                    max_tokens,
                    temperature
                )
                if not is_ai_failure(retry_result):
                    results[idx] = "⚠️ 分片正文模式失败，已自动回退到分片精简模式。\n\n" + retry_result
            if is_ai_failure(results[idx]):
                logger.warning(f"⚠️ [{section_name}] 分片 {idx} 分析失败")
            else:
                logger.info(f"✅ [{section_name}] 分片 {idx} 分析完成")

    return [results[i] for i in sorted(results.keys())]


# ══════════════════════════════════════════════════════
#  3. DeepSeek AI 分析（分批调用）
# ══════════════════════════════════════════════════════

def call_deepseek(system_prompt: str, user_prompt: str, api_key: str,
                  api_base: str, model: str,
                  max_tokens: int = 4000, temperature: float = 0.7) -> str:
    """调用 DeepSeek API"""
    url = f"{api_base.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    
    logger.info(f"📤 DeepSeek API (prompt: {len(user_prompt)} 字符)...")

    retries = int(os.environ.get("DEEPSEEK_API_RETRIES", "2"))
    retry_sleep = float(os.environ.get("DEEPSEEK_API_RETRY_SLEEP", "1.5"))
    retries = max(1, retries)

    for attempt in range(1, retries + 1):
        resp = None
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=180)
            resp.raise_for_status()
            result = resp.json()
            content = result["choices"][0]["message"].get("content", "")
            if not str(content or "").strip():
                logger.error("❌ DeepSeek 返回空内容")
                if attempt < retries:
                    sleep_seconds = retry_sleep * attempt
                    logger.warning(f"⏳ DeepSeek 空响应重试 ({attempt}/{retries})，{sleep_seconds:.1f}s 后继续")
                    time.sleep(sleep_seconds)
                    continue
                return "AI 分析失败: empty response"
            usage = result.get("usage", {})
            logger.info(f"✅ 完成 (prompt_tokens={usage.get('prompt_tokens',0)}, completion_tokens={usage.get('completion_tokens',0)})")
            cleaned_content = sanitize_ai_response_text(content)
            if cleaned_content != content:
                logger.info("🧹 已清洗 AI 输出前缀")
            return cleaned_content
        except requests.exceptions.HTTPError as e:
            status_code = resp.status_code if resp is not None else None
            logger.error(f"❌ DeepSeek API 错误: {e}")
            try:
                logger.error(f"   响应: {resp.text[:500]}")
            except Exception:
                pass
            can_retry = status_code in (429, 500, 502, 503, 504) and attempt < retries
            if can_retry:
                sleep_seconds = retry_sleep * attempt
                logger.warning(f"⏳ DeepSeek 将重试 ({attempt}/{retries})，{sleep_seconds:.1f}s 后继续")
                time.sleep(sleep_seconds)
                continue
            return f"AI 分析失败: {e}"
        except Exception as e:
            logger.error(f"❌ DeepSeek API 调用异常: {e}")
            if attempt < retries:
                sleep_seconds = retry_sleep * attempt
                logger.warning(f"⏳ DeepSeek 调用异常重试 ({attempt}/{retries})，{sleep_seconds:.1f}s 后继续")
                time.sleep(sleep_seconds)
                continue
            return f"AI 分析失败: {e}"
    return "AI 分析失败: exhausted retries"


def run_ai_analysis(market: dict, social: dict, news: list,
                    api_key: str, api_base: str, model: str,
                    date_str: str, iso_date: str, report_label: str,
                    time_range: str, report_type: str,
                    web_context: dict | None = None,
                    previous_context: str = "") -> str:
    """
    分批调用 DeepSeek，每个数据源独立分析，最后综合汇总。
    
    步骤:
      1. 市场+板块数据 → 市场分析
      2. Twitter 分片并行(默认20路) → 分片摘要 → 汇总
      3. 微信分片并行(默认20路) → 分片摘要 → 汇总
      4. 热榜全量      → 热榜分析
      5. 注入联网检索+上期上下文 → 综合结构化报告
    """
    date_context = f"{iso_date} {report_label}（覆盖时段: {time_range}）"
    section_summaries = {}
    parallelism = get_deepseek_parallelism()
    grounding_rules = (
        "严格约束：\n"
        "1) 只能使用输入文本中的事实，禁止引入外部新闻、历史记忆、常识补全或虚构数字/事件；\n"
        "2) 输入里没有的信息必须明确写“数据不足/未提供”；\n"
        "3) 禁止把猜测写成事实，禁止杜撰“交叉验证”；\n"
        "4) 结论必须可追溯到输入内容。"
    )
    is_morning_report = report_type == "morning"
    a_share_rule = (
        "早报特殊规则：不要分析 A 股盘面数据（指数、板块、北向资金），仅可分析非 A 股市场。"
        if is_morning_report else
        "可正常分析 A 股与其他市场。"
    )
    logger.info(f"⚙️ DeepSeek 分片并发: {parallelism} 路")

    filtered_market, market_filter_notes = market_snapshot_filter(market, date_str, report_type)
    market_filter_note_text = format_market_filter_notes(market_filter_notes)
    wechat_consensus_text = build_wechat_consensus_and_signal_text(social)
    twitter_focus_text = format_twitter_focus_for_ai(social)
    github_focus_text = format_github_focus_for_ai(filtered_market)
    logger.info("🧪 市场时效过滤后可用模块: %s", ",".join((filtered_market.get("data", {}) or {}).keys()))

    # ─── 第1步: 市场数据分析 ────────────────────────
    logger.info("🔍 [1/5] 分析市场数据...")
    market_text = format_market_for_ai(filtered_market, include_a_share=not is_morning_report)
    if market_text != "暂无市场数据":
        summary = call_deepseek(
            system_prompt=(
                "你是资深金融市场分析师。请对以下市场数据进行专业分析，包括：\n"
                "1. 主要市场走势判断\n"
                "2. 关键资产轮动分析：哪些方向在领涨/领跌，反映什么资金偏好\n"
                "3. 加密货币和商品期货的关键变化\n"
                "5. 涨跌驱动链条：请明确“事件/政策/情绪 -> 资金行为 -> 价格表现”的因果路径，并标注证据强弱\n\n"
                "用中文，Markdown格式，重要数据**加粗**，600-900字。\n\n"
                f"{grounding_rules}\n"
                f"5) {a_share_rule}"
            ),
            user_prompt=f"以下是 {date_context} 的金融市场数据：\n\n{market_text}",
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=2000
        )
        section_summaries["market"] = summary
    
    # ─── 第2步: Twitter 分析 ────────────────────────
    logger.info("🔍 [2/5] 分析 Twitter 推文（20 路分片并行）...")
    twitter_chunks = build_twitter_chunks(social, parallelism)
    if twitter_chunks:
        twitter_chunk_summaries = parallel_chunk_analysis(
            section_name="Twitter",
            chunks=twitter_chunks,
            system_prompt=(
                "你是资深金融科技分析师。请只分析当前这一个 Twitter 分片，提取：\n"
                "1. 分片内最重要的3-5条事件\n"
                "2. 分片情绪（乐观/中性/谨慎）\n"
                "3. 可执行关注点（交易信号/政策信号/行业动向）\n"
                "输出中文 Markdown，180-350字，避免重复。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt_builder=lambda chunk, idx, total: (
                f"以下是 {date_context} 的 Twitter 分片数据，请只总结当前分片：\n\n"
                f"{format_twitter_chunk_for_ai(chunk, idx, total)}"
            ),
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=1200,
            temperature=0.5,
            fallback_system_prompt=(
                "你是资深金融科技分析师。请基于精简推文分片，提炼：\n"
                "1) 分片关键事件 2) 情绪判断 3) 可执行关注点。\n"
                "中文 Markdown，150-280字。\n\n"
                f"{grounding_rules}"
            ),
            fallback_user_prompt_builder=lambda chunk, idx, total: (
                f"以下是 {date_context} 的 Twitter 精简分片，请只总结当前分片：\n\n"
                f"{format_twitter_chunk_for_ai_compact(chunk, idx, total)}"
            )
        )
        valid_summaries = [s for s in twitter_chunk_summaries if not is_ai_failure(s)]
        failed_count = len(twitter_chunk_summaries) - len(valid_summaries)
        if valid_summaries:
            merged_prompt = "以下是 Twitter 各分片摘要，请去重后输出最终结论：\n\n"
            for idx, text in enumerate(valid_summaries, start=1):
                merged_prompt += f"### 分片{idx}\n{text}\n\n"
            summary = call_deepseek(
                system_prompt=(
                    "你是资深金融科技分析师。请融合多个 Twitter 分片摘要，输出：\n"
                    "1. 最重要的5-8条信息/事件\n"
                    "2. 市场情绪判断（恐慌/乐观/中性）\n"
                    "3. 值得关注的交易信号或行业动向\n"
                    "4. 地缘政治相关推文要点\n\n"
                    "按重要性排序，去重，中文 Markdown，500-800字。\n\n"
                    f"{grounding_rules}"
                ),
                user_prompt=merged_prompt,
                api_key=api_key,
                api_base=api_base,
                model=model,
                max_tokens=2200,
                temperature=0.5
            )
            if is_ai_failure(summary):
                logger.warning("⚠️ Twitter 分片汇总失败，使用分片结果拼接降级输出")
                summary = "⚠️ Twitter 分片汇总失败，以下是已完成分片摘要：\n\n" + "\n\n".join(valid_summaries)
            elif failed_count > 0:
                summary = f"⚠️ Twitter 分片有 {failed_count}/{len(twitter_chunk_summaries)} 路失败，以下为可用分片汇总。\n\n{summary}"
        else:
            summary = "AI 分析失败: Twitter 全部分片调用失败"
        section_summaries["twitter"] = summary

    # ─── 2.5: Twitter 海外英文信号补充 ─────────────────
    if twitter_focus_text != "暂无 Twitter 数据":
        logger.info("🔍 [2.5/5] 汇总 Twitter 英文信号...")
        twitter_focus_summary = call_deepseek(
            system_prompt=(
                "你是跨市场情报分析师。请基于给定的 Twitter 高互动样本，输出中文汇报：\n"
                "1) 海外英文信号主线（不要直译整段，提炼观点）；\n"
                "2) 与金融科技/AI/Web3 相关的具体线索；\n"
                "3) 可执行关注点与潜在误导噪音。\n\n"
                "输出 Markdown，300-500字，引用关键结论时加 [来源: Twitter]。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt=f"{date_context} 的 Twitter 英文信号样本：\n\n{twitter_focus_text}",
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=1500,
            temperature=0.4,
        )
        if not is_ai_failure(twitter_focus_summary):
            section_summaries["twitter_focus"] = twitter_focus_summary
        else:
            section_summaries["twitter_focus"] = "暂无可用 Twitter 英文信号总结"
    
    # ─── 第3步: 微信公众号分析 ────────────────────────
    logger.info("🔍 [3/5] 分析微信公众号文章（20 路分片并行）...")
    wechat_chunks = build_wechat_chunks(social, parallelism)
    if wechat_chunks:
        wechat_chunk_summaries = parallel_chunk_analysis(
            section_name="WeChat",
            chunks=wechat_chunks,
            system_prompt=(
                "你是资深财经媒体分析师。请只分析当前公众号分片：\n"
                "1. 挑出最值得读的2-4篇（标题+公众号+理由）\n"
                "2. 提炼核心观点与潜在市场影响\n"
                "3. 标记风险提示或噪音信息\n"
                "输出中文 Markdown，220-420字，尽量保留具体信息。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt_builder=lambda chunk, idx, total: (
                f"以下是 {date_context} 的微信公众号分片数据，请只总结当前分片：\n\n"
                f"{format_wechat_chunk_for_ai(chunk, idx, total)}"
            ),
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=1500,
            temperature=0.5,
            fallback_system_prompt=(
                "你是资深财经媒体分析师。请基于公众号精简分片（标题+摘要+互动）输出：\n"
                "1) 值得读的文章 2) 核心观点 3) 风险提示。\n"
                "中文 Markdown，180-320字。\n\n"
                f"{grounding_rules}"
            ),
            fallback_user_prompt_builder=lambda chunk, idx, total: (
                f"以下是 {date_context} 的微信公众号精简分片，请只总结当前分片：\n\n"
                f"{format_wechat_chunk_for_ai_compact(chunk, idx, total)}"
            )
        )
        valid_summaries = [s for s in wechat_chunk_summaries if not is_ai_failure(s)]
        failed_count = len(wechat_chunk_summaries) - len(valid_summaries)
        if valid_summaries:
            merged_prompt = "以下是微信公众号各分片摘要，请去重并汇总为最终阅读建议：\n\n"
            for idx, text in enumerate(valid_summaries, start=1):
                merged_prompt += f"### 分片{idx}\n{text}\n\n"
            summary = call_deepseek(
                system_prompt=(
                    "你是资深财经媒体分析师。请融合多个公众号分片摘要，输出：\n"
                    "第一部分：最值得读的5-8篇文章（标题+公众号+推荐理由）\n"
                    "第二部分：核心观点与市场影响\n"
                    "第三部分：政策监管动向与风险提示\n\n"
                    "中文 Markdown，800-1200字，按重要性排序。\n\n"
                    f"{grounding_rules}"
                ),
                user_prompt=merged_prompt,
                api_key=api_key,
                api_base=api_base,
                model=model,
                max_tokens=2600,
                temperature=0.5
            )
            if is_ai_failure(summary):
                logger.warning("⚠️ 微信分片汇总失败，使用分片结果拼接降级输出")
                summary = "⚠️ 微信分片汇总失败，以下是已完成分片摘要：\n\n" + "\n\n".join(valid_summaries)
            elif failed_count > 0:
                summary = f"⚠️ 微信分片有 {failed_count}/{len(wechat_chunk_summaries)} 路失败，以下为可用分片汇总。\n\n{summary}"
        else:
            summary = "AI 分析失败: 微信公众号全部分片调用失败"
        section_summaries["wechat"] = summary

    # ─── 3.5: 微信共识与弱信号 ────────────────────────
    if wechat_consensus_text != "暂无微信公众号数据":
        logger.info("🔍 [3.5/5] 提炼微信共识与弱信号...")
        wechat_consensus_summary = call_deepseek(
            system_prompt=(
                "你是中文财经信息架构师。请基于输入的“跨公众号共识议题+弱信号候选”输出简洁汇报：\n"
                "1) 先写跨公众号共识（最多4点，强调哪些公众号反复提及）；\n"
                "2) 再写弱信号（最多3点，强调为什么值得提前关注）；\n"
                "3) 全文禁止空话，保持可执行。\n\n"
                "输出 Markdown，280-480字。关键句末加 [来源: 微信]。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt=f"{date_context} 微信共识与弱信号原始抽取：\n\n{wechat_consensus_text}",
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=1400,
            temperature=0.4,
        )
        if is_ai_failure(wechat_consensus_summary):
            section_summaries["wechat_consensus"] = wechat_consensus_text
        else:
            section_summaries["wechat_consensus"] = wechat_consensus_summary
    
    # ─── 第4步: 热榜分析 ────────────────────────
    logger.info("🔍 [4/5] 分析热榜新闻（分片并行）...")
    news_chunks = build_news_chunks(news, min(parallelism, 8))
    if news_chunks:
        news_chunk_summaries = parallel_chunk_analysis(
            section_name="NewsNow",
            chunks=news_chunks,
            system_prompt=(
                "你是资深新闻分析师。请只分析当前热榜分片，输出：\n"
                "1. 分片内最重要的3-5个事件\n"
                "2. 与金融市场相关的新闻线索\n"
                "3. 科技/AI 相关线索\n"
                "4. 社会舆论焦点\n\n"
                "中文 Markdown，180-320字，禁止编造。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt_builder=lambda chunk, idx, total: (
                f"以下是 {date_context} 的 NewsNow 热榜分片，请只总结当前分片：\n\n"
                f"{format_news_chunk_for_ai(chunk, idx, total)}"
            ),
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=900,
            temperature=0.4,
            fallback_system_prompt=(
                "你是资深新闻分析师。请基于精简热榜分片，提炼：\n"
                "1) 关键事件 2) 金融相关线索 3) 科技/AI 线索。\n"
                "中文 Markdown，120-220字。\n\n"
                f"{grounding_rules}"
            ),
            fallback_user_prompt_builder=lambda chunk, idx, total: (
                f"以下是 {date_context} 的 NewsNow 精简分片，请只总结当前分片：\n\n"
                f"{format_news_chunk_for_ai_compact(chunk, idx, total)}"
            )
        )
        valid_summaries = [s for s in news_chunk_summaries if not is_ai_failure(s)]
        failed_count = len(news_chunk_summaries) - len(valid_summaries)

        if valid_summaries:
            merged_prompt = "以下是 NewsNow 各分片摘要，请去重并输出最终热榜分析：\n\n"
            for idx, text in enumerate(valid_summaries, start=1):
                merged_prompt += f"### 分片{idx}\n{text}\n\n"
            summary = call_deepseek(
                system_prompt=(
                    "你是资深新闻分析师。请融合多个热榜分片摘要，输出：\n"
                    "1. 跨平台共同关注的3-5个热点事件\n"
                    "2. 与金融市场相关的重要新闻\n"
                    "3. 科技/AI 相关热点\n"
                    "4. 社会舆论焦点\n\n"
                    "中文 Markdown，300-500字。\n\n"
                    f"{grounding_rules}"
                ),
                user_prompt=merged_prompt,
                api_key=api_key,
                api_base=api_base,
                model=model,
                max_tokens=1500,
                temperature=0.4
            )
            if is_ai_failure(summary):
                logger.warning("⚠️ 热榜分片汇总失败，回退到分片摘要拼接")
                summary = "⚠️ 热榜汇总失败，以下为可用分片摘要：\n\n" + "\n\n".join(valid_summaries[:8])
            elif failed_count > 0:
                summary = f"⚠️ 热榜分片有 {failed_count}/{len(news_chunk_summaries)} 路失败，以下为可用分片汇总。\n\n{summary}"
        else:
            logger.warning("⚠️ 热榜分片全部失败，回退规则化摘要。")
            summary = generate_news_rule_based_summary(news)

        if is_ai_failure(summary):
            logger.warning("⚠️ 热榜分析最终失败，回退规则化摘要。")
            summary = generate_news_rule_based_summary(news)

        section_summaries["news"] = summary

    # ─── 第4.5步: GitHub 趋势（金融科技/AI/Web3） ───────────
    if github_focus_text != "暂无 GitHub 趋势数据":
        logger.info("🔍 [4.5/5] 分析 GitHub 项目雷达...")
        github_summary = call_deepseek(
            system_prompt=(
                "你是技术趋势分析师。请把 GitHub 热门项目按“金融科技 / AI / Web3 / 通用”做中文汇报：\n"
                "1) 先挑出最值得关注的5-8个项目；\n"
                "2) 说明它们可能对应的应用场景和落地价值；\n"
                "3) 标注可能的泡沫噪音或重复概念。\n\n"
                "输出 Markdown，450-700字；结论句加 [来源: GitHub]。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt=f"{date_context} GitHub 项目样本：\n\n{github_focus_text}",
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=2200,
            temperature=0.45,
        )
        if is_ai_failure(github_summary):
            section_summaries["github"] = github_focus_text
        else:
            section_summaries["github"] = github_summary

    # ─── 第5步: 综合汇总 ────────────────────────
    logger.info("🔍 [5/5] 生成综合分析报告（含上下文增强）...")

    # 检查是否为周末
    is_weekend_flag, _ = is_weekend(date_str)
    weekend_note = "【注意：今日为周末，A股休市，部分市场数据可能缺失】" if is_weekend_flag else ""
    web_context_text = format_web_context_for_ai(web_context or {})

    synthesis_input = f"以下是 {date_context} 各数据源的分析结果，请进行最终综合汇总：{weekend_note}\n\n"
    synthesis_input += f"## 市场时效过滤说明\n{market_filter_note_text}\n\n"

    if previous_context:
        synthesis_input += f"## 上一期报告上下文\n{previous_context}\n\n"

    if "market" in section_summaries:
        synthesis_input += f"## 市场数据分析\n{section_summaries['market']}\n\n"
    if "wechat_consensus" in section_summaries:
        synthesis_input += f"## 微信共识与弱信号\n{section_summaries['wechat_consensus']}\n\n"
    if "twitter" in section_summaries:
        synthesis_input += f"## Twitter 推文分析\n{section_summaries['twitter']}\n\n"
    if "twitter_focus" in section_summaries:
        synthesis_input += f"## Twitter 英文信号补充\n{section_summaries['twitter_focus']}\n\n"
    if "wechat" in section_summaries:
        synthesis_input += f"## 微信公众号分析\n{section_summaries['wechat']}\n\n"
    if "news" in section_summaries:
        synthesis_input += f"## 热榜新闻分析\n{section_summaries['news']}\n\n"
    if "github" in section_summaries:
        synthesis_input += f"## GitHub 项目雷达\n{section_summaries['github']}\n\n"
    if web_context_text != "暂无联网检索补充":
        synthesis_input += f"## 联网检索补充\n{web_context_text}\n\n"
    else:
        synthesis_input += "## 联网检索补充\n暂无联网检索补充\n\n"

    if not section_summaries:
        logger.warning("⚠️ 各数据源均无可用原始数据，跳过综合 AI 生成。")
        return (
            "## 一、摘要\n"
            "- 社会：暂无可用数据。\n"
            "- 经济：暂无可用数据。\n"
            "- 市场：暂无可用数据。\n"
            "- 科技：暂无可用数据。\n\n"
            "## 二、分板块汇报\n"
            "### 2.1 市场概况（仅有效交易时段数据）\n"
            "暂无可用市场数据，无法形成有效盘面结论。\n\n"
            "### 2.2 微信公众号共识与弱信号\n"
            "暂无可用微信公众号数据。\n\n"
            "### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）\n"
            "暂无可用 GitHub 趋势数据。\n\n"
            "### 2.4 Twitter 海外信号（英文内容中文汇报）\n"
            "暂无可用 Twitter 数据。\n\n"
            "### 2.5 国内新闻与政策脉络\n"
            "暂无可用热榜数据。\n\n"
            "## 三、明日跟踪清单\n"
            "1. 检查定时任务触发时间。\n"
            "2. 检查抓取服务状态（Nitter / 微信服务 / NewsNow）。\n"
            "3. 补齐数据后重新生成报告。"
        )
    
    final_summary = call_deepseek(
        system_prompt=(
            "你是资深金融市场首席分析师，正在编写今日市场综合研报。\n"
            "你将获得来自市场数据、Twitter、微信公众号、NewsNow、GitHub、联网检索的材料。\n"
            "请产出“摘要 + 分板块汇报”，并优先覆盖金融科技、AI、Web3线索。\n\n"
            "请严格按以下固定结构输出，不允许改一级/二级标题名称：\n\n"
            "## 一、摘要\n"
            "- 社会：\n"
            "- 经济：\n"
            "- 市场：\n"
            "- 科技：\n\n"
            "## 二、分板块汇报\n"
            "### 2.1 市场概况（仅有效交易时段数据）\n"
            + (
                "早报阶段不得分析 A 股盘面；仅分析非 A 股市场与可验证数据。\n"
                if is_morning_report else
                "仅基于“市场时效过滤说明”里保留的数据，禁止使用被过滤掉的旧快照。\n"
            ) +
            "必须包含“发生了什么”“为什么会这样（证据强弱：高/中/低）”“下一步观察”。\n\n"
            "### 2.2 微信公众号共识与弱信号\n"
            "先写跨公众号重复提及的共识议题，再写弱信号候选，并给出判断依据。\n\n"
            "### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）\n"
            "挑出最值得关注的项目，说明应用场景、可落地价值、噪音风险。\n\n"
            "### 2.4 Twitter 海外信号（英文内容中文汇报）\n"
            "把英文高互动内容翻译并提炼成中文结论，不要整段直译。\n\n"
            "### 2.5 国内新闻与政策脉络\n"
            "聚焦国内社会/经济/监管动态，并说明对市场和产业链的影响。\n\n"
            "## 三、明日跟踪清单\n"
            "1. ...\n2. ...\n3. ...\n\n"
            "要求：\n"
            "- 用中文，语言精炼专业\n"
            "- Markdown 格式，每个版块用 ## 标题\n"
            "- 重要数据用 **加粗**，关键判断要明确\n"
            "- 去除重复信息，交叉引用不同来源，优先回答“为什么会这样”\n"
            "- 在关键结论句末标注来源标签，如 [来源: 市场数据] / [来源: Twitter] / [来源: 微信] / [来源: 热榜] / [来源: GitHub] / [来源: 联网搜索]\n"
            "- 单节避免空话，尽量给出可验证事实；输入缺失时明确写“数据不足”\n"
            "- 字数控制：摘要 180-260 字；2.1~2.5 每节 220-380 字；跟踪清单每条 25-50 字\n"
            "- 当 2.1 缺少有效交易时段数据时，只写“数据不足 + 需补充信息”，禁止方向性推断\n"
            "- 不要输出任何关于读者身份背景的信息\n"
            "- 总字数 1500-2600 字\n\n"
            f"{grounding_rules}\n"
            f"5) {a_share_rule}"
        ),
        user_prompt=synthesis_input,
        api_key=api_key,
        api_base=api_base,
        model=model,
        max_tokens=6000,
        temperature=0.5
    )
    if is_ai_failure(final_summary):
        logger.warning("⚠️ 综合分析失败，使用降级模板输出。")
        final_summary = (
            "## 一、摘要\n"
            "- 社会：综合分析调用失败，请参考下方分板块内容。\n"
            "- 经济：自动综合暂不可用。\n"
            "- 市场：请优先查看市场与热榜详细分析。\n"
            "- 科技：请优先查看 GitHub 与 Twitter 详细分析。\n\n"
            "## 二、分板块汇报\n"
            "### 2.1 市场概况（仅有效交易时段数据）\n"
            "综合模型失败，已保留原始市场明细与分板块分析。\n\n"
            "### 2.2 微信公众号共识与弱信号\n"
            "请参考下方“微信公众号详细分析”。\n\n"
            "### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）\n"
            "请参考下方“GitHub 项目详细分析”。\n\n"
            "### 2.4 Twitter 海外信号（英文内容中文汇报）\n"
            "请参考下方“Twitter 英文信号详细分析”。\n\n"
            "### 2.5 国内新闻与政策脉络\n"
            "请参考下方“热榜详细分析”。\n\n"
            "## 三、明日跟踪清单\n"
            "1. 核查数据抓取任务是否完整。\n"
            "2. 对照联网检索补充核验关键事件。\n"
            "3. 重新生成报告并比对结论差异。"
        )
    
    # 组装完整 AI 分析输出
    result_parts = [final_summary]
    
    # 附上各板块详细分析（折叠展示）
    result_parts.append("\n\n---\n")
    result_parts.append("<details><summary>📑 点击展开各板块详细分析</summary>\n")
    
    if "market" in section_summaries:
        result_parts.append(f"### 📊 市场数据详细分析\n\n{section_summaries['market']}\n")
    result_parts.append(f"### ⏱ 市场时效过滤说明\n\n{market_filter_note_text}\n")
    if "twitter" in section_summaries:
        result_parts.append(f"### 🐦 Twitter 详细分析\n\n{section_summaries['twitter']}\n")
    if "twitter_focus" in section_summaries:
        result_parts.append(f"### 🌐 Twitter 英文信号详细分析\n\n{section_summaries['twitter_focus']}\n")
    if "wechat" in section_summaries:
        result_parts.append(f"### 📱 微信公众号详细分析\n\n{section_summaries['wechat']}\n")
    if "wechat_consensus" in section_summaries:
        result_parts.append(f"### 🛰 微信共识与弱信号\n\n{section_summaries['wechat_consensus']}\n")
    if "news" in section_summaries:
        result_parts.append(f"### 📰 热榜详细分析\n\n{section_summaries['news']}\n")
    if "github" in section_summaries:
        result_parts.append(f"### 💻 GitHub 项目详细分析\n\n{section_summaries['github']}\n")
    if isinstance(web_context, dict) and web_context.get("items"):
        result_parts.append(f"### 🌐 联网检索摘要\n\n{format_web_context_for_ai(web_context)}\n")

    result_parts.append("</details>\n")
    
    return "\n".join(result_parts)


# ══════════════════════════════════════════════════════
#  4. Markdown 报告生成
# ══════════════════════════════════════════════════════

def generate_raw_market_section(market: dict) -> str:
    """生成市场数据原文 Markdown（含板块指数）"""
    data = market.get("data", {})
    lines = ["## 📊 金融市场数据\n"]
    
    # A股主要指数
    stock = data.get("stock_cn", {})
    if stock and stock.get("market_closed"):
        lines.append(f"> ⏸ {stock.get('market_status', 'A股休市')}\n")
    if stock and stock.get("indices"):
        lines.append("### 🇨🇳 A股主要指数\n")
        lines.append("| 指数 | 价格 | 涨跌幅 |")
        lines.append("|------|------|--------|")
        for idx in stock["indices"]:
            if isinstance(idx, dict):
                icon = "🟢" if idx.get("change_pct", 0) >= 0 else "🔴"
                lines.append(f"| {idx.get('name','')} | {idx.get('price',0):.2f} | {icon} {idx.get('change_pct',0):+.2f}% |")
        lines.append("")
    
    # A股板块指数
    sectors = stock.get("sectors", []) if stock else []
    if sectors:
        sorted_sectors = sorted(
            [s for s in sectors if isinstance(s, dict) and s.get("change_pct") is not None],
            key=lambda x: x.get("change_pct", 0),
            reverse=True
        )
        if sorted_sectors:
            lines.append("### 📈 A股板块涨幅 TOP 15\n")
            lines.append("| 板块 | 涨跌幅 | 换手率 | 领涨股 |")
            lines.append("|------|--------|--------|--------|")
            for s in sorted_sectors[:15]:
                icon = "🟢" if s.get("change_pct", 0) >= 0 else "🔴"
                turnover = f"{s.get('turnover', 0):.2f}%" if s.get('turnover') else "-"
                lines.append(f"| {s.get('name','')} | {icon} {s.get('change_pct',0):+.2f}% | {turnover} | {s.get('leading_stock','')} |")
            lines.append("")
            
            lines.append("### 📉 A股板块跌幅 TOP 15\n")
            lines.append("| 板块 | 涨跌幅 | 换手率 | 领跌股 |")
            lines.append("|------|--------|--------|--------|")
            for s in sorted_sectors[-15:]:
                icon = "🟢" if s.get("change_pct", 0) >= 0 else "🔴"
                turnover = f"{s.get('turnover', 0):.2f}%" if s.get('turnover') else "-"
                lines.append(f"| {s.get('name','')} | {icon} {s.get('change_pct',0):+.2f}% | {turnover} | {s.get('leading_stock','')} |")
            lines.append("")
    
    # 北向资金
    north = stock.get("north_flow", {}) if stock else {}
    if north:
        lines.append("### 💰 北向资金\n")
        lines.append("| 项目 | 金额(亿元) |")
        lines.append("|------|------------|")
        for k, v in north.items():
            if isinstance(v, (int, float)):
                icon = "🟢" if v >= 0 else "🔴"
                lines.append(f"| {k} | {icon} {v:.2f} |")
        lines.append("")

    # Yahoo Finance 全球股票概览
    yahoo_stock = data.get("yahoo_stock", {})
    yahoo_markets = yahoo_stock.get("markets", []) if isinstance(yahoo_stock, dict) else []
    if yahoo_markets:
        lines.append("### 🌍 全球股票概览（Yahoo Finance）\n")
        lines.append("| 区域 | 指标 | 最新价 | 涨跌幅 | 币种 |")
        lines.append("|------|------|--------|--------|------|")
        for item in yahoo_markets:
            if not isinstance(item, dict):
                continue
            region = item.get("region", "全球")
            name = item.get("name", item.get("symbol", "未知"))
            try:
                price = float(item.get("price", 0) or 0)
            except (TypeError, ValueError):
                price = 0.0
            try:
                change_pct = float(item.get("change_pct", 0) or 0)
            except (TypeError, ValueError):
                change_pct = 0.0
            icon = "🟢" if change_pct >= 0 else "🔴"
            currency = item.get("currency", "")
            url = clean_external_url(item.get("url", ""))
            label = f"[{name}]({url})" if url else name
            lines.append(f"| {region} | {label} | {price:,.2f} | {icon} {change_pct:+.2f}% | {currency} |")
        overview = yahoo_stock.get("overview", {})
        if isinstance(overview, dict):
            lines.append("")
            lines.append(
                f"> 概览：上涨 {overview.get('up', 0)} | 下跌 {overview.get('down', 0)} | "
                f"平盘 {overview.get('flat', 0)} | 总计 {overview.get('total', len(yahoo_markets))}"
            )
        lines.append("")

    # 贵金属
    pm = data.get("precious_metal", {})
    if pm and pm.get("metals"):
        lines.append("### 🥇 贵金属\n")
        lines.append("| 品种 | 价格 | 涨跌幅 |")
        lines.append("|------|------|--------|")
        for metal in pm["metals"]:
            if isinstance(metal, dict):
                icon = "🟢" if metal.get("change_pct", 0) >= 0 else "🔴"
                lines.append(f"| {metal.get('name','')} | ${metal.get('price',0):.2f} | {icon} {metal.get('change_pct',0):+.2f}% |")
        lines.append("")
    
    # 加密货币
    crypto = data.get("crypto", {})
    if crypto and crypto.get("coins"):
        lines.append("### ₿ 加密货币\n")
        lines.append("| 币种 | 价格 | 24h涨跌 |")
        lines.append("|------|------|---------|")
        for coin in crypto["coins"]:
            if isinstance(coin, dict):
                icon = "🟢" if coin.get("change_24h", 0) >= 0 else "🔴"
                lines.append(f"| {coin.get('symbol','').upper()} | ${coin.get('price',0):,.2f} | {icon} {coin.get('change_24h',0):+.2f}% |")
        lines.append("")
    
    # 期货
    futures = data.get("futures", {})
    if futures:
        cat_names = {"commodity": "商品期货", "index_futures": "股指期货", "international": "国际期货"}
        for cat_key, cat_name in cat_names.items():
            items = futures.get(cat_key, [])
            if items:
                lines.append(f"### 📈 {cat_name}\n")
                lines.append("| 品种 | 价格 | 涨跌幅 |")
                lines.append("|------|------|--------|")
                for item in items[:10]:
                    if isinstance(item, dict):
                        icon = "🟢" if item.get("change_pct", 0) >= 0 else "🔴"
                        lines.append(f"| {item.get('name','')} | {item.get('price','')} | {icon} {item.get('change_pct',0):+.2f}% |")
                lines.append("")
    
    # GitHub
    github = data.get("github", {})
    if github and github.get("trending"):
        lines.append("### 💻 GitHub 趋势\n")
        for repo in github["trending"][:5]:
            if isinstance(repo, dict):
                repo_name = repo.get("name", "")
                repo_url = str(repo.get("url", "") or "").strip()
                if repo_url.startswith("http://") or repo_url.startswith("https://"):
                    lines.append(f"- ⭐ [**{repo_name}**]({repo_url}) ({repo.get('stars',0)} stars)")
                else:
                    lines.append(f"- ⭐ **{repo_name}** ({repo.get('stars',0)} stars)")
                desc = repo.get("description", "")[:80]
                if desc:
                    lines.append(f"  - {desc}")
        lines.append("")
    
    return "\n".join(lines)


def generate_raw_twitter_section(social: dict) -> str:
    """生成 Twitter 原文 Markdown"""
    twitter_data = get_social_section(social, "twitter")
    tweets = twitter_data.get("tweets", [])
    if not tweets:
        return "## 🐦 Twitter 热点\n\n暂无数据\n"
    trending = [t for t in tweets if isinstance(t, dict) and t.get("is_trending")]
    follow = [t for t in tweets if isinstance(t, dict) and not t.get("is_trending")]
    lines = [f"## 🐦 Twitter 热点 ({len(tweets)} 条)\n"]
    lines.append(
        f"- 来源统计: 关注账号 {twitter_data.get('follow_tweets_count', len(follow))} 条 | "
        f"热门讨论 {twitter_data.get('trending_tweets_count', len(trending))} 条\n"
    )

    if trending:
        lines.append("### 🔥 热门讨论推文\n")
        trending = sorted(
            trending,
            key=lambda x: (x.get("likes", 0) + x.get("retweets", 0) + x.get("replies", 0)),
            reverse=True,
        )
        for t in trending[:20]:
            text = t.get("text", "")[:500].replace("\n", " ").replace("|", "\\|")
            created = t.get("created_at", "")[:16]
            url = t.get("url", "")
            engagement = f"❤️{t.get('likes', 0)} 🔁{t.get('retweets', 0)} 💬{t.get('replies', 0)}"
            lines.append(f"- `{created}` @{t.get('username', 'unknown')} {engagement}")
            lines.append(f"  - {text}")
            if url:
                lines.append(f"  - [原文链接]({url})")
        lines.append("")

    # 按账号分组展示关注账号推文
    by_user = {}
    for t in follow:
        u = t.get("username", "unknown")
        by_user.setdefault(u, []).append(t)

    for username, user_tweets in by_user.items():
        lines.append(f"### @{username} ({len(user_tweets)} 条)\n")
        for t in user_tweets[:5]:
            text = t.get("text", "")[:300].replace("\n", " ").replace("|", "\\|")
            created = t.get("created_at", "")[:16]
            url = t.get("url", "")
            lines.append(f"- `{created}` {text}")
            if url:
                lines.append(f"  - [原文链接]({url})")
        if len(user_tweets) > 5:
            lines.append(f"- *... 及其他 {len(user_tweets) - 5} 条*")
        lines.append("")

    return "\n".join(lines)


def generate_raw_wechat_section(social: dict) -> str:
    """生成微信公众号原文 Markdown"""
    wechat_data = get_social_section(social, "wechat")
    articles = wechat_data.get("articles", [])
    if not articles:
        return "## 📱 微信公众号\n\n暂无数据\n"
    
    lines = [f"## 📱 微信公众号 ({len(articles)} 篇)\n"]
    hot_articles = [a for a in articles if isinstance(a, dict) and a.get("is_hot")]
    normal_articles = [a for a in articles if isinstance(a, dict) and not a.get("is_hot")]
    lines.append(
        f"- 来源统计: 关注公众号 {wechat_data.get('follow_articles_count', len(normal_articles))} 篇 | "
        f"热门文章 {wechat_data.get('hot_articles_count', len(hot_articles))} 篇\n"
    )

    if hot_articles:
        lines.append("### 🔥 热门文章\n")
        for a in hot_articles[:20]:
            title = a.get("title", "")
            account = a.get("account_name", "")
            url = a.get("url", "")
            digest = a.get("digest", "")[:200]
            pub_time = a.get("publish_time", "")[:16]
            stats = f"阅读 {a.get('read_count', 0)} | 点赞 {a.get('like_count', 0)} | 评论 {a.get('comment_count', 0)}"
            if url:
                lines.append(f"- [{title}]({url})")
            else:
                lines.append(f"- {title}")
            lines.append(f"  - **{account}** | {pub_time} | {stats}")
            if digest:
                lines.append(f"  - {digest}")
        lines.append("")

    for a in normal_articles:
        title = a.get("title", "")
        account = a.get("account_name", "")
        url = a.get("url", "")
        digest = a.get("digest", "")[:150]
        pub_time = a.get("publish_time", "")[:16]
        
        if url:
            lines.append(f"### [{title}]({url})")
        else:
            lines.append(f"### {title}")
        lines.append(f"**{account}** | {pub_time}\n")
        if digest:
            lines.append(f"> {digest}\n")
    
    return "\n".join(lines)


def generate_raw_news_section(news: list) -> str:
    """生成 NewsNow 热榜原文 Markdown"""
    if not news:
        return "## 🔥 NewsNow 热榜\n\n暂无数据\n"
    
    lines = [f"## 🔥 NewsNow 热榜 ({len(news)} 条)\n"]
    
    # 按平台分组
    by_platform = {}
    for n in news:
        p = n["platform"]
        by_platform.setdefault(p, []).append(n)
    
    for platform, items in by_platform.items():
        lines.append(f"### {platform}\n")
        lines.append("| 排名 | 标题 |")
        lines.append("|------|------|")
        for item in items[:10]:
            title = item["title"].replace("|", "\\|")
            url = item.get("url", "")
            if url:
                lines.append(f"| #{item['rank']} | [{title}]({url}) |")
            else:
                lines.append(f"| #{item['rank']} | {title} |")
        lines.append("")
    
    return "\n".join(lines)


def generate_ai_reference_section(
    market: dict,
    social: dict,
    news: list,
    report_type: str,
    web_context: dict | None = None,
) -> str:
    """生成 AI 分析区引用来源（可点击链接）。"""
    max_twitter = int(os.environ.get("AI_REF_MAX_TWITTER", "20"))
    max_wechat = int(os.environ.get("AI_REF_MAX_WECHAT", "20"))
    max_news = int(os.environ.get("AI_REF_MAX_NEWS", "30"))
    max_github = int(os.environ.get("AI_REF_MAX_GITHUB", "10"))
    max_yahoo = int(os.environ.get("AI_REF_MAX_YAHOO_STOCK", "12"))
    max_web = int(os.environ.get("AI_REF_MAX_WEB", "24"))

    def clean_url(value) -> str:
        url = str(value or "").strip()
        if url.startswith("http://") or url.startswith("https://"):
            return url
        return ""

    def short_text(value: str, max_len: int = 90) -> str:
        text = normalize_plain_text(value)
        if len(text) <= max_len:
            return text
        return text[:max_len] + "..."

    lines = ["## 🔗 AI 分析引用来源\n", "> 以下为本次 AI 摘要直接使用的原始材料链接（节选）。\n"]
    has_any_link = False

    twitter_data = get_social_section(social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict) and clean_url(t.get("url"))]
    tweets_sorted = sorted(
        tweets,
        key=lambda t: (tweet_engagement(t), str(t.get("created_at", ""))),
        reverse=True,
    )
    selected_tweets = tweets_sorted[:max_twitter]
    lines.append(f"### 🐦 Twitter ({len(selected_tweets)}/{len(tweets)} 条)\n")
    if selected_tweets:
        has_any_link = True
        for t in selected_tweets:
            lines.append(
                f"- [{str(t.get('created_at', ''))[:16]} @{t.get('username', 'unknown')} | "
                f"{short_text(t.get('text', ''))}]({clean_url(t.get('url'))})"
            )
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict) and clean_url(a.get("url"))]
    articles_sorted = sorted(
        articles,
        key=lambda a: (wechat_article_score(a), str(a.get("publish_time", ""))),
        reverse=True,
    )
    selected_articles = articles_sorted[:max_wechat]
    lines.append(f"### 📱 微信公众号 ({len(selected_articles)}/{len(articles)} 条)\n")
    if selected_articles:
        has_any_link = True
        for a in selected_articles:
            lines.append(
                f"- [{str(a.get('publish_time', ''))[:16]} 【{a.get('account_name', '未知公众号')}】"
                f"{short_text(a.get('title', ''), 100)}]({clean_url(a.get('url'))})"
            )
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    news_with_url = [n for n in news if isinstance(n, dict) and clean_url(n.get("url"))]
    selected_news = news_with_url[:max_news]
    lines.append(f"### 🔥 NewsNow ({len(selected_news)}/{len(news_with_url)} 条)\n")
    if selected_news:
        has_any_link = True
        for n in selected_news:
            lines.append(
                f"- [{n.get('platform', 'unknown')} #{n.get('rank', '-')} | "
                f"{short_text(n.get('title', ''), 100)}]({clean_url(n.get('url'))})"
            )
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    github_trending = (market.get("data", {}).get("github", {}) or {}).get("trending", []) or []
    github_with_url = [r for r in github_trending if isinstance(r, dict) and clean_url(r.get("url"))]
    selected_github = github_with_url[:max_github]
    lines.append(f"### 💻 GitHub ({len(selected_github)}/{len(github_with_url)} 条)\n")
    if selected_github:
        has_any_link = True
        for repo in selected_github:
            name = repo.get("full_name") or repo.get("name") or "unknown"
            stars = repo.get("stars", 0)
            lines.append(f"- [{name} | ⭐ {stars}]({clean_url(repo.get('url'))})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    yahoo_stock = (market.get("data", {}).get("yahoo_stock", {}) or {})
    yahoo_markets = yahoo_stock.get("markets", []) if isinstance(yahoo_stock, dict) else []
    yahoo_with_url = [m for m in yahoo_markets if isinstance(m, dict) and clean_url(m.get("url"))]
    selected_yahoo = yahoo_with_url[:max_yahoo]
    lines.append(f"### 🌍 Yahoo Finance 股票 ({len(selected_yahoo)}/{len(yahoo_with_url)} 条)\n")
    if selected_yahoo:
        has_any_link = True
        for item in selected_yahoo:
            name = item.get("name", item.get("symbol", "未知"))
            symbol = item.get("symbol", "")
            region = item.get("region", "全球")
            change = item.get("change_pct", 0)
            try:
                change = float(change or 0)
            except (TypeError, ValueError):
                change = 0.0
            lines.append(
                f"- [{region} | {name} ({symbol}) | {change:+.2f}%]({clean_url(item.get('url'))})"
            )
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    web_items = []
    if isinstance(web_context, dict):
        web_items = [
            item for item in web_context.get("items", [])
            if isinstance(item, dict) and clean_url(item.get("link"))
        ]
    selected_web = web_items[:max_web]
    lines.append(f"### 🌐 联网检索 ({len(selected_web)}/{len(web_items)} 条)\n")
    if selected_web:
        has_any_link = True
        for item in selected_web:
            published = (item.get("published_at") or "-")[:16]
            source = item.get("source", "Web")
            title = short_text(item.get("title", ""), 100)
            lines.append(f"- [{published} {source} | {title}]({clean_url(item.get('link'))})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    if report_type == "morning":
        lines.append("> 注：早报 AI 已按规则跳过 A 股盘面数据分析。\n")

    if not has_any_link:
        lines.append("> 当前未提取到可用引用来源链接。\n")

    return "\n".join(lines)


def generate_source_link_index_section(
    market: dict,
    social: dict,
    news: list,
    web_context: dict | None = None,
) -> str:
    """生成统一原始链接索引，便于跳转查阅。"""
    max_twitter = int(os.environ.get("LINK_INDEX_MAX_TWITTER", "80"))
    max_wechat = int(os.environ.get("LINK_INDEX_MAX_WECHAT", "80"))
    max_news = int(os.environ.get("LINK_INDEX_MAX_NEWS", "120"))
    max_github = int(os.environ.get("LINK_INDEX_MAX_GITHUB", "20"))
    max_yahoo = int(os.environ.get("LINK_INDEX_MAX_YAHOO_STOCK", "40"))
    max_web = int(os.environ.get("LINK_INDEX_MAX_WEB", "120"))

    def clean_url(value) -> str:
        url = str(value or "").strip()
        if url.startswith("http://") or url.startswith("https://"):
            return url
        return ""

    def short_text(value: str, max_len: int = 80) -> str:
        text = normalize_plain_text(value)
        if len(text) <= max_len:
            return text
        return text[:max_len] + "..."

    lines = ["## 🔗 原始链接索引\n"]
    has_any_link = False

    # Twitter links
    twitter_data = get_social_section(social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict)]
    tweets_with_url = [t for t in tweets if clean_url(t.get("url"))]
    tweets_sorted = sorted(
        tweets_with_url,
        key=lambda t: (tweet_engagement(t), str(t.get("created_at", ""))),
        reverse=True,
    )
    selected_tweets = tweets_sorted[:max_twitter]
    lines.append(f"### 🐦 Twitter 原文 ({len(selected_tweets)}/{len(tweets_with_url)} 条)\n")
    if selected_tweets:
        has_any_link = True
        for t in selected_tweets:
            url = clean_url(t.get("url"))
            username = t.get("username", "unknown")
            created = str(t.get("created_at", ""))[:16]
            text = short_text(t.get("text", ""), 90) or "(无正文)"
            tag = "热门" if t.get("is_trending") else "关注"
            lines.append(f"- [{created} @{username} [{tag}] | {text}]({url})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    # WeChat links
    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict)]
    articles_with_url = [a for a in articles if clean_url(a.get("url"))]
    articles_sorted = sorted(
        articles_with_url,
        key=lambda a: (wechat_article_score(a), str(a.get("publish_time", ""))),
        reverse=True,
    )
    selected_articles = articles_sorted[:max_wechat]
    lines.append(f"### 📱 微信公众号原文 ({len(selected_articles)}/{len(articles_with_url)} 条)\n")
    if selected_articles:
        has_any_link = True
        for a in selected_articles:
            url = clean_url(a.get("url"))
            account = a.get("account_name", "未知公众号")
            title = short_text(a.get("title", ""), 100) or "(无标题)"
            pub_time = str(a.get("publish_time", ""))[:16]
            lines.append(f"- [{pub_time} 【{account}】{title}]({url})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    # NewsNow links
    news_with_url = [n for n in news if isinstance(n, dict) and clean_url(n.get("url"))]
    selected_news = news_with_url[:max_news]
    lines.append(f"### 🔥 NewsNow 原文 ({len(selected_news)}/{len(news_with_url)} 条)\n")
    if selected_news:
        has_any_link = True
        for n in selected_news:
            url = clean_url(n.get("url"))
            platform = n.get("platform", "unknown")
            rank = n.get("rank", "-")
            title = short_text(n.get("title", ""), 100) or "(无标题)"
            lines.append(f"- [{platform} #{rank} | {title}]({url})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    # GitHub links
    github_trending = (market.get("data", {}).get("github", {}) or {}).get("trending", []) or []
    github_with_url = [r for r in github_trending if isinstance(r, dict) and clean_url(r.get("url"))]
    selected_github = github_with_url[:max_github]
    lines.append(f"### 💻 GitHub 原文 ({len(selected_github)}/{len(github_with_url)} 条)\n")
    if selected_github:
        has_any_link = True
        for repo in selected_github:
            url = clean_url(repo.get("url"))
            name = repo.get("full_name") or repo.get("name") or "unknown"
            desc = short_text(repo.get("description", ""), 90)
            stars = repo.get("stars", 0)
            if desc:
                lines.append(f"- [{name} | ⭐ {stars} | {desc}]({url})")
            else:
                lines.append(f"- [{name} | ⭐ {stars}]({url})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    # Yahoo Finance links
    yahoo_stock = (market.get("data", {}).get("yahoo_stock", {}) or {})
    yahoo_markets = yahoo_stock.get("markets", []) if isinstance(yahoo_stock, dict) else []
    yahoo_with_url = [m for m in yahoo_markets if isinstance(m, dict) and clean_url(m.get("url"))]
    selected_yahoo = yahoo_with_url[:max_yahoo]
    lines.append(f"### 🌍 Yahoo Finance 原文 ({len(selected_yahoo)}/{len(yahoo_with_url)} 条)\n")
    if selected_yahoo:
        has_any_link = True
        for item in selected_yahoo:
            url = clean_url(item.get("url"))
            name = short_text(item.get("name", item.get("symbol", "未知")), 60)
            symbol = item.get("symbol", "")
            region = item.get("region", "全球")
            change = item.get("change_pct", 0)
            try:
                change = float(change or 0)
            except (TypeError, ValueError):
                change = 0.0
            lines.append(f"- [{region} | {name} ({symbol}) | {change:+.2f}%]({url})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    # Web links
    web_items = []
    if isinstance(web_context, dict):
        web_items = [item for item in web_context.get("items", []) if isinstance(item, dict) and clean_url(item.get("link"))]
    selected_web = web_items[:max_web]
    lines.append(f"### 🌐 联网检索原文 ({len(selected_web)}/{len(web_items)} 条)\n")
    if selected_web:
        has_any_link = True
        for item in selected_web:
            url = clean_url(item.get("link"))
            source = short_text(item.get("source", "Web"), 30)
            title = short_text(item.get("title", ""), 100) or "(无标题)"
            published = str(item.get("published_at", ""))[:16] or "-"
            lines.append(f"- [{published} {source} | {title}]({url})")
    else:
        lines.append("- 暂无可用链接")
    lines.append("")

    if not has_any_link:
        lines.append("> 当前报告未提取到可用原始链接。\n")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════
#  5. 主流程
# ══════════════════════════════════════════════════════

def main():
    now_bj = now_beijing()
    parser = argparse.ArgumentParser(description="finradar 每日综合报告")
    parser.add_argument("--date", default=now_bj.strftime("%Y%m%d"),
                        help="日期 YYYYMMDD (默认今天)")
    parser.add_argument("--type", choices=["morning", "evening", "auto"], default="auto",
                        help="报告类型: morning/evening/auto")
    parser.add_argument("--api-key", default=None,
                        help="DeepSeek API Key (也可通过环境变量 DEEPSEEK_API_KEY)")
    parser.add_argument("--no-ai", action="store_true",
                        help="跳过 AI 分析，只汇总原始数据")
    parser.add_argument("--keywords", default="",
                        help="联网检索关键词（逗号分隔，留空则自动提取）")
    parser.add_argument("--no-web-context", action="store_true",
                        help="禁用联网检索补充")
    parser.add_argument("--output", default=None,
                        help="输出文件路径 (默认 output/report/daily_YYYYMMDD.md)")
    args = parser.parse_args()
    
    date_str = args.date
    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    
    # 获取 DeepSeek 运行配置
    deepseek_runtime = resolve_deepseek_runtime(args.api_key)
    api_key = deepseek_runtime["api_key"]
    api_base = deepseek_runtime["api_base"]
    model = deepseek_runtime["model"]
    runtime_config = deepseek_runtime.get("config", {}) if isinstance(deepseek_runtime, dict) else {}
    report_cfg = runtime_config.get("report", {}) if isinstance(runtime_config, dict) else {}
    web_cfg = report_cfg.get("web_context", {}) if isinstance(report_cfg, dict) else {}
    
    # ── 判断早报/晚报 ──────────────────────────────
    if args.type == "auto":
        hour = now_bj.hour
        if 5 <= hour < 14:
            report_type = "morning"
        elif 14 <= hour < 24:
            report_type = "evening"
        else:
            report_type = "morning"
    else:
        report_type = args.type
    
    report_label = "🌅 早报" if report_type == "morning" else "🌇 晚报"
    time_range = "昨日20:00 → 今日08:00" if report_type == "morning" else "今日08:00 → 20:00"
    
    logger.info(f"📅 生成 {iso_date} {report_label}")
    logger.info(f"🤖 DeepSeek 配置: model={model}, base={api_base}")
    
    # ── 读取数据 ──────────────────────────────────
    logger.info("📥 读取市场数据...")
    market = load_market_data(date_str)
    
    logger.info(f"📥 读取社交媒体数据 ({report_type})...")
    social = load_social_data(date_str, report_type)
    
    logger.info("📥 读取热榜数据...")
    news = load_news_data(date_str, report_type)
    
    logger.info(f"   市场: {'✅' if market else '❌'}")
    logger.info(f"   社交: {'✅' if social else '❌'} (mode={social.get('mode','N/A')}, type={social.get('report_type','N/A')})")
    logger.info(f"   热榜: {'✅' if news else '❌'} ({len(news)} 条)")
    if social and report_type in ("morning", "evening"):
        loaded_type = social.get("report_type")
        if loaded_type and loaded_type != report_type:
            logger.warning(f"⚠️ 社交数据类型不匹配: 期望 {report_type}，实际读取到 {loaded_type}")

    # ── 上下文增强（上期 + 联网检索）────────────────────
    previous_context = load_previous_report_context(date_str, report_type)
    if previous_context:
        logger.info("🧩 已加载上一期报告上下文")
    else:
        logger.info("🧩 未找到上一期报告，跳过上下文衔接")

    config_keywords = web_cfg.get("keywords", []) if isinstance(web_cfg, dict) else []
    if not isinstance(config_keywords, list):
        config_keywords = []
    raw_keywords = (
        args.keywords
        or os.environ.get("REPORT_WEB_KEYWORDS", "")
        or ",".join(config_keywords)
    )
    custom_keywords = parse_keywords_arg(raw_keywords)

    web_context_enabled = not args.no_web_context
    if "enabled" in web_cfg:
        web_context_enabled = bool(web_cfg.get("enabled")) and web_context_enabled
    env_web_flag = os.environ.get("WEB_CONTEXT_ENABLED")
    if env_web_flag is not None:
        web_context_enabled = parse_bool(env_web_flag, web_context_enabled)

    web_context = {"queries": [], "items": [], "errors": []}
    if web_context_enabled:
        logger.info("🌐 开始联网检索补充上下文...")
        web_context = run_web_context_search(
            iso_date=iso_date,
            report_type=report_type,
            market=market,
            news=news,
            keywords=custom_keywords,
        )
        logger.info(
            "🌐 联网检索完成: %s 条，关键词 %s 个",
            len(web_context.get("items", []) or []),
            len(web_context.get("queries", []) or []),
        )
    else:
        logger.info("🌐 已禁用联网检索补充")

    # ── AI 分析 ──────────────────────────────────
    ai_summary = ""
    if not args.no_ai:
        if not api_key:
            logger.warning("⚠️ 未配置 DeepSeek API Key，跳过 AI 分析")
            ai_summary = "> ⚠️ AI 分析未启用（未配置 API Key）\n"
        else:
            ai_summary = run_ai_analysis(
                market=market,
                social=social,
                news=news,
                api_key=api_key,
                api_base=api_base,
                model=model,
                date_str=date_str,
                iso_date=iso_date,
                report_label=report_label,
                time_range=time_range,
                report_type=report_type,
                web_context=web_context,
                previous_context=previous_context,
            )
    else:
        ai_summary = "> ℹ️ 本次使用 `--no-ai` 参数，已跳过 DeepSeek 分析。\n"
    ai_summary, ai_footnote_section = convert_ai_source_tags_to_clickable_refs(
        ai_summary,
        market=market,
        social=social,
        news=news,
        web_context=web_context,
    )
    
    # ── 生成完整 Markdown ──────────────────────
    report_parts = []
    
    # 检查休市状态
    is_weekend_flag, market_status = is_weekend(date_str)
    market_status_badge = "⚠️ A股休市" if is_weekend_flag else "✅ 正常交易"
    
    # 标题
    generated_at_bj = now_beijing()
    report_parts.append(f"# 📰 finradar {report_label}")
    report_parts.append(f"**{iso_date}** | {report_label} | 覆盖时段: {time_range} | 市场状态: {market_status_badge}")
    report_parts.append(f"生成时间: {generated_at_bj.strftime('%Y-%m-%d %H:%M')}（北京时间）\n")
    if is_weekend_flag:
        report_parts.append(f"**⚠️ 注意：今日为周末，A股休市，部分市场数据可能缺失或未更新**\n")
    report_parts.append("---\n")
    
    # AI 分析摘要
    report_parts.append("# 🤖 AI 分析摘要\n")
    report_parts.append(ai_summary)
    if ai_footnote_section:
        report_parts.append(ai_footnote_section)
    report_parts.append(generate_web_context_section(web_context))
    report_parts.append(generate_ai_reference_section(market, social, news, report_type, web_context=web_context))
    report_parts.append("\n---\n")
    
    # 原始数据
    report_parts.append("# 📋 原始数据\n")
    report_parts.append("<a id=\"raw-market-data\"></a>")
    report_parts.append(generate_raw_market_section(market))
    report_parts.append(generate_raw_twitter_section(social))
    report_parts.append(generate_raw_wechat_section(social))
    report_parts.append(generate_raw_news_section(news))
    report_parts.append(generate_source_link_index_section(market, social, news, web_context=web_context))
    
    # 页脚
    report_parts.append("---\n")
    report_parts.append(f"*报告由 finradar 自动生成 | {generated_at_bj.strftime('%Y-%m-%d %H:%M:%S')}（北京时间）*\n")
    
    full_report = "\n".join(report_parts)
    
    # ── 保存 ──────────────────────────────────
    OUTPUT_REPORT.mkdir(parents=True, exist_ok=True)
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = OUTPUT_REPORT / f"daily_{date_str}_{report_type}.md"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_report)
    
    logger.info(f"✅ 报告已保存: {output_path}")
    logger.info(f"   文件大小: {output_path.stat().st_size / 1024:.1f} KB")
    
    return str(output_path)


if __name__ == "__main__":
    main()
