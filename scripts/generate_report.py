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
OUTPUT_TWITTER_USED = PROJECT_ROOT / "output" / "twitter" / "report_used_tweets.jsonl"

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
            try:
                with open(path, encoding="utf-8") as f:
                    direct_data = json.load(f)
                if direct_data.get("mode") == "social":
                    return direct_data
                logger.warning(
                    "⚠️ 忽略非社交数据文件: %s (mode=%s)",
                    path.name,
                    direct_data.get("mode", "N/A"),
                )
            except Exception as e:
                logger.warning("⚠️ 读取社交数据文件失败 %s: %s", path.name, e)

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


def list_previous_report_paths(
    date_str: str,
    report_type: str,
    lookback_days: int = 2,
    max_reports: int = 3,
) -> list[Path]:
    """定位历史报告路径，覆盖前 1-2 天上下文（按时间由近到远）。"""
    report_day = datetime.strptime(date_str, "%Y%m%d")
    candidates: list[Path] = []

    if report_type == "evening":
        candidates.append(OUTPUT_REPORT / f"daily_{date_str}_morning.md")

    for offset in range(1, max(1, lookback_days) + 1):
        day = report_day - timedelta(days=offset)
        day_str = day.strftime("%Y%m%d")
        candidates.append(OUTPUT_REPORT / f"daily_{day_str}_evening.md")
        candidates.append(OUTPUT_REPORT / f"daily_{day_str}_morning.md")

    existed: list[Path] = []
    seen = set()
    for path in candidates:
        key = str(path.resolve()) if path.exists() else str(path)
        if key in seen:
            continue
        seen.add(key)
        if path.exists():
            existed.append(path)
        if len(existed) >= max_reports:
            break
    return existed


def extract_markdown_section(content: str, heading: str) -> str:
    """提取 Markdown 二级标题下的正文。"""
    pattern = rf"{re.escape(heading)}\s*(.*?)(?=\n##\s+|\Z)"
    match = re.search(pattern, content, flags=re.S)
    if not match:
        return ""
    return match.group(1).strip()


def truncate_text_preserve_lines(text: str, max_chars: int) -> str:
    """按字符上限截断文本，尽量保留换行结构。"""
    block = str(text or "").strip()
    if len(block) <= max_chars:
        return block
    return block[:max_chars].rstrip() + "..."


def load_previous_report_context(date_str: str, report_type: str, max_chars: int = 3600) -> str:
    """读取前 1-2 天多期摘要，增强连续性并减少重复。"""
    paths = list_previous_report_paths(
        date_str=date_str,
        report_type=report_type,
        lookback_days=int(os.environ.get("REPORT_CONTEXT_LOOKBACK_DAYS", "2")),
        max_reports=int(os.environ.get("REPORT_CONTEXT_MAX_REPORTS", "3")),
    )
    if not paths:
        return ""

    total_reports = len(paths)
    max_chars_each = max(700, max_chars // max(1, total_reports))
    parts: list[str] = []
    for idx, path in enumerate(paths, start=1):
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue

        match = re.search(r"#\s+🤖\s+AI 分析摘要\s*(.*?)\n#\s+📋\s+原始数据", content, flags=re.S)
        excerpt = match.group(1).strip() if match else content
        excerpt = re.sub(r"<details>.*?</details>", "", excerpt, flags=re.S).strip()

        summary_section = extract_markdown_section(excerpt, "## 一、摘要")
        tracking_section = extract_markdown_section(excerpt, "## 三、明日跟踪清单")
        report_block = [f"历史报告 {idx}: {path.name}"]
        if summary_section:
            report_block.append(
                "【摘要】\n"
                + truncate_text_preserve_lines(summary_section, max_chars=max_chars_each)
            )
        if tracking_section:
            report_block.append(
                "【跟踪清单】\n"
                + truncate_text_preserve_lines(tracking_section, max_chars=max_chars_each)
            )
        if len(report_block) == 1:
            plain_excerpt = normalize_plain_text(excerpt)
            if plain_excerpt:
                report_block.append(truncate_text_preserve_lines(plain_excerpt, max_chars=max_chars_each))
        parts.append("\n".join(report_block))

    if not parts:
        return ""
    merged = "\n\n".join(parts).strip()
    return truncate_text_preserve_lines(merged, max_chars=max_chars)


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

    # 股票总览（A股 + Yahoo）
    stock_overview = data.get("stock_overview", {}) if isinstance(data, dict) else {}
    if isinstance(stock_overview, dict):
        summary = stock_overview.get("summary", {}) if isinstance(stock_overview.get("summary"), dict) else {}
        tracked = int(summary.get("tracked", 0) or 0)
        if tracked > 0:
            lines.append("【股票总览】")
            lines.append(
                f"  跟踪{tracked}个标的：上涨{int(summary.get('up', 0) or 0)} / "
                f"下跌{int(summary.get('down', 0) or 0)} / 平盘{int(summary.get('flat', 0) or 0)}"
            )
            by_region = stock_overview.get("by_region", [])
            if isinstance(by_region, list) and by_region:
                region_bits = []
                for item in by_region[:6]:
                    if not isinstance(item, dict):
                        continue
                    region_bits.append(
                        f"{item.get('region', '全球')} {float(item.get('avg_change_pct', 0) or 0):+.2f}%"
                    )
                if region_bits:
                    lines.append(f"  区域强弱: {' | '.join(region_bits)}")
            key_indices = stock_overview.get("key_indices", [])
            if isinstance(key_indices, list) and key_indices:
                key_bits = []
                for item in key_indices[:6]:
                    if not isinstance(item, dict):
                        continue
                    key_bits.append(
                        f"{item.get('name', item.get('symbol', '未知'))} "
                        f"{float(item.get('change_pct', 0) or 0):+.2f}%"
                    )
                if key_bits:
                    lines.append(f"  关键指数: {' | '.join(key_bits)}")
    
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


def split_match_tokens(text: str) -> set[str]:
    """用于来源匹配的简易分词（中英混合）。"""
    content = normalize_plain_text(text).lower()
    if not content:
        return set()
    ascii_tokens = re.findall(r"[a-z0-9][a-z0-9_\-/.]{1,40}", content)
    zh_tokens = re.findall(r"[\u4e00-\u9fff]{2,8}", content)
    stop_words = {
        "来源", "数据", "报告", "分析", "市场", "今天", "昨日", "今日",
        "的", "了", "和", "以及", "进行", "相关", "信息", "显示",
    }
    tokens = set()
    for tok in ascii_tokens + zh_tokens:
        token = tok.strip(" .,:;!?()[]{}\"'`")
        if len(token) < 2:
            continue
        if token in stop_words:
            continue
        tokens.add(token)
    return tokens


def collect_github_source_repos(market: dict) -> list[dict]:
    """收集 GitHub 全部可引用项目（含 AI/FinTech/Web3 扩展池）。"""
    github_data = (market.get("data", {}) or {}).get("github", {}) if isinstance(market, dict) else {}
    if not isinstance(github_data, dict):
        return []
    merged = []
    seen = set()
    for key in ("trending", "ai_trending", "fintech_trending", "web3_trending"):
        rows = github_data.get(key, []) or []
        for repo in rows:
            if not isinstance(repo, dict):
                continue
            repo_key = repo.get("full_name") or repo.get("url") or repo.get("name")
            if not repo_key or repo_key in seen:
                continue
            seen.add(repo_key)
            merged.append(repo)
    return merged


def build_ai_citation_link_pools(market: dict, social: dict, news: list, web_context: dict | None = None) -> dict:
    """构建 AI 引用来源链接池（包含匹配文本，用于减少错配）。"""
    def _short(value: str, max_len: int = 72) -> str:
        text = normalize_plain_text(value)
        if len(text) <= max_len:
            return text
        return text[:max_len] + "..."

    def _candidate(title: str, url: str, match_text: str) -> dict:
        return {
            "title": normalize_plain_text(title),
            "url": clean_external_url(url),
            "match_text": normalize_plain_text(match_text),
            "tokens": split_match_tokens(match_text),
        }

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
    tweets_sorted = sorted(
        tweets,
        key=lambda t: (tweet_engagement(t), str(t.get("created_at", ""))),
        reverse=True,
    )
    for t in tweets_sorted:
        username = str(t.get("username", "unknown")).strip()
        created = str(t.get("created_at", ""))[:16]
        text = normalize_plain_text(t.get("text", ""))
        title = f"{created} @{username} | {_short(text, 88)}"
        match_text = f"@{username} {created} {text}"
        pools["twitter"].append(_candidate(title, t.get("url", ""), match_text))

    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict) and clean_external_url(a.get("url"))]
    articles_sorted = sorted(
        articles,
        key=lambda a: (wechat_article_score(a), str(a.get("publish_time", ""))),
        reverse=True,
    )
    for a in articles_sorted:
        account = str(a.get("account_name", "未知公众号")).strip()
        title_text = normalize_plain_text(a.get("title", "") or "")
        digest = normalize_plain_text(a.get("digest", "") or "")
        pub_time = str(a.get("publish_time", ""))[:16]
        title = f"{pub_time} 【{account}】{_short(title_text, 88)}"
        match_text = f"{account} {title_text} {digest} {pub_time}"
        pools["wechat"].append(_candidate(title, a.get("url", ""), match_text))

    news_with_url = [n for n in news if isinstance(n, dict) and clean_external_url(n.get("url"))]
    for n in news_with_url:
        platform = n.get("platform", "unknown")
        rank = n.get("rank", "-")
        title_text = normalize_plain_text(n.get("title", ""))
        title = f"{platform} #{rank} | {_short(title_text, 88)}"
        match_text = f"{platform} {title_text} {rank}"
        pools["news"].append(_candidate(title, n.get("url", ""), match_text))

    github_repos = collect_github_source_repos(market)
    github_with_url = [r for r in github_repos if isinstance(r, dict) and clean_external_url(r.get("url"))]
    github_with_url = sorted(
        github_with_url,
        key=lambda r: (
            github_repo_score(r),
            float(r.get("stars", 0) or 0),
            str(r.get("updated_at", "")),
        ),
        reverse=True,
    )
    for r in github_with_url:
        full_name = r.get("full_name") or r.get("name") or "unknown"
        stars = int(float(r.get("stars", 0) or 0))
        desc = normalize_plain_text(r.get("description", "") or "")
        language = normalize_plain_text(r.get("language", "") or "")
        topics = " ".join([normalize_plain_text(x) for x in (r.get("topics", []) or []) if str(x).strip()])
        title = f"{full_name} | ⭐ {stars}"
        match_text = f"{full_name} {desc} {language} {topics}"
        pools["github"].append(_candidate(title, r.get("url", ""), match_text))

    # 市场数据来源尽量给出可点击外链，确保 Notion 中可点击
    market_data = market.get("data", {}) if isinstance(market, dict) else {}
    market_sources: list[dict] = []
    if isinstance(market_data, dict):
        yahoo_stock = market_data.get("yahoo_stock", {}) if isinstance(market_data.get("yahoo_stock"), dict) else {}
        yahoo_markets = [
            m for m in yahoo_stock.get("markets", [])
            if isinstance(m, dict) and clean_external_url(m.get("url"))
        ]
        for row in yahoo_markets[:10]:
            name = row.get("name") or row.get("symbol") or "Yahoo 股票"
            symbol = row.get("symbol", "")
            region = row.get("region", "")
            title = f"Yahoo Finance {name} ({symbol})"
            match_text = f"{name} {symbol} {region} {row.get('change_pct', '')}"
            market_sources.append(_candidate(title, row.get("url", ""), match_text))
        if market_data.get("crypto"):
            market_sources.append(_candidate(
                "CoinGecko API 文档",
                "https://www.coingecko.com/en/api/documentation",
                "CoinGecko crypto api documentation",
            ))
        if market_data.get("precious_metal") or (
            isinstance(market_data.get("futures"), dict) and market_data.get("futures", {}).get("international")
        ):
            market_sources.append(_candidate(
                "Yahoo Finance 行情",
                "https://finance.yahoo.com",
                "yahoo finance quote commodity futures index",
            ))
        if market_data.get("stock_cn") or market_data.get("futures"):
            market_sources.append(_candidate(
                "AkShare 数据接口文档",
                "https://akshare.akfamily.xyz",
                "akshare stock futures china api",
            ))
    if not market_sources:
        market_sources.append(_candidate(
            "AkShare 数据接口文档",
            "https://akshare.akfamily.xyz",
            "akshare stock futures china api",
        ))
    pools["market"] = market_sources

    web_items = []
    if isinstance(web_context, dict):
        web_items = [
            item for item in web_context.get("items", [])
            if isinstance(item, dict) and clean_external_url(item.get("link"))
        ]
    web_items = sorted(
        web_items,
        key=lambda item: (
            float(item.get("published_ts", 0) or 0),
            normalize_plain_text(item.get("title", "")),
        ),
        reverse=True,
    )
    for item in web_items:
        published = (item.get("published_at") or "-")[:16]
        source = item.get("source", "Web")
        title_text = normalize_plain_text(item.get("title", ""))
        title = f"{published} {source} | {_short(title_text, 88)}"
        match_text = f"{source} {title_text} {item.get('snippet', '')}"
        pools["web"].append(_candidate(title, item.get("link", ""), match_text))

    return pools


AI_SOURCE_ORDER = ("twitter", "wechat", "news", "github", "market", "web")
AI_SOURCE_LABEL = {
    "twitter": "Twitter",
    "wechat": "微信公众号",
    "news": "NewsNow热榜",
    "github": "GitHub",
    "market": "市场原始数据",
    "web": "联网检索",
}
AI_SOURCE_PREFIX = {
    "twitter": "TW",
    "wechat": "WC",
    "news": "NW",
    "github": "GH",
    "market": "MK",
    "web": "WB",
}
AI_SOURCE_PREFIX_TO_KEY = {v: k for k, v in AI_SOURCE_PREFIX.items()}


def build_ai_citation_catalog(
    market: dict,
    social: dict,
    news: list,
    web_context: dict | None = None,
    pools: dict | None = None,
) -> list[dict]:
    """构建可被 AI 直接引用的来源 ID 目录，避免链接错配。"""
    pools = pools or build_ai_citation_link_pools(market, social, news, web_context=web_context)
    if not isinstance(pools, dict):
        return []

    limits = {
        "twitter": int(os.environ.get("AI_CITATION_CATALOG_MAX_TWITTER", "16")),
        "wechat": int(os.environ.get("AI_CITATION_CATALOG_MAX_WECHAT", "16")),
        "news": int(os.environ.get("AI_CITATION_CATALOG_MAX_NEWS", "14")),
        "github": int(os.environ.get("AI_CITATION_CATALOG_MAX_GITHUB", "14")),
        "market": int(os.environ.get("AI_CITATION_CATALOG_MAX_MARKET", "10")),
        "web": int(os.environ.get("AI_CITATION_CATALOG_MAX_WEB", "14")),
    }
    catalog: list[dict] = []
    url_seen = set()
    for source_key in AI_SOURCE_ORDER:
        prefix = AI_SOURCE_PREFIX.get(source_key, "SRC")
        rows = [r for r in (pools.get(source_key, []) or []) if isinstance(r, dict)]
        max_count = max(0, limits.get(source_key, 12))
        rank = 0
        for row in rows:
            url = clean_external_url(row.get("url", ""))
            if not url or url in url_seen:
                continue
            url_seen.add(url)
            rank += 1
            if rank > max_count:
                break
            source_id = f"{prefix}{rank:02d}"
            catalog.append(
                {
                    "source_id": source_id,
                    "source_key": source_key,
                    "title": normalize_plain_text(row.get("title", "")),
                    "match_text": normalize_plain_text(row.get("match_text", "")),
                    "url": url,
                }
            )
    return catalog


def format_ai_citation_catalog_for_prompt(
    market: dict,
    social: dict,
    news: list,
    web_context: dict | None = None,
) -> str:
    """将可引用来源目录格式化给综合提示词使用。"""
    pools = build_ai_citation_link_pools(market, social, news, web_context=web_context)
    catalog = build_ai_citation_catalog(
        market=market,
        social=social,
        news=news,
        web_context=web_context,
        pools=pools,
    )
    if not catalog:
        return "暂无可引用来源ID索引"

    lines = [
        f"可引用来源ID索引（共 {len(catalog)} 条）：",
        "引用格式必须为 [来源ID: TW01] 或 [来源ID: TW01, GH02]，禁止使用泛化 [来源: Twitter]。",
    ]
    for row in catalog:
        source_id = row.get("source_id", "")
        source_key = row.get("source_key", "")
        title = normalize_plain_text(row.get("title", ""))
        title = title[:110] + ("..." if len(title) > 110 else "")
        url = clean_external_url(row.get("url", ""))
        lines.append(f"- {source_id} | {AI_SOURCE_LABEL.get(source_key, source_key)} | {title} | {url}")
    return "\n".join(lines)


def normalize_source_id_token(token: str) -> str:
    """标准化来源 ID（兼容 TW1/TW-01 等写法）。"""
    raw = re.sub(r"[^A-Za-z0-9]", "", str(token or "").upper())
    if not raw:
        return ""
    m = re.match(r"^([A-Z]{2,3})(\d{1,3})$", raw)
    if not m:
        return raw
    prefix = m.group(1)
    number = int(m.group(2))
    return f"{prefix}{number:02d}"


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
) -> tuple[str, str, list[dict]]:
    """
    将 AI 输出中的 [来源: xxx] 转成可点击角标链接，如 [¹](url)。
    并返回“引用脚注”区块。
    """
    if not ai_text:
        return ai_text, "", []

    source_id_pattern = re.compile(r"\[来源ID:\s*([^\]]+)\]", flags=re.IGNORECASE)
    source_tag_pattern = re.compile(r"\[来源:\s*([^\]]+)\]")
    legacy_source_pattern = re.compile(r"\[([^\[\]\n]{1,80})\](?!\()")
    pools = build_ai_citation_link_pools(market, social, news, web_context=web_context)
    catalog = build_ai_citation_catalog(
        market=market,
        social=social,
        news=news,
        web_context=web_context,
        pools=pools,
    )
    source_id_map = {}
    first_source_row_map: dict[str, dict] = {}
    for row in catalog:
        if not isinstance(row, dict):
            continue
        source_id = normalize_source_id_token(row.get("source_id", ""))
        if source_id:
            source_id_map[source_id] = row
        source_key = str(row.get("source_key", "")).strip()
        if source_key and source_key not in first_source_row_map:
            first_source_row_map[source_key] = row

    used_candidate_indexes: dict[str, set[int]] = {k: set() for k in pools.keys()}
    min_score = int(os.environ.get("AI_CITATION_MIN_SCORE", "8"))

    ref_records: list[dict] = []
    url_to_idx: dict[str, int] = {}

    def register_ref(source_key: str, title: str, url: str, score: int, source_id: str = "") -> dict | None:
        safe_url = clean_external_url(url)
        if not safe_url:
            return None
        safe_source_id = normalize_source_id_token(source_id)
        if safe_url in url_to_idx:
            idx = url_to_idx[safe_url]
            record = ref_records[idx - 1]
            if safe_source_id and not record.get("source_id"):
                record["source_id"] = safe_source_id
            if score > int(record.get("score", 0) or 0):
                record["score"] = int(score)
            return {
                "idx": idx,
                "source_key": source_key,
                "title": record.get("title", title),
                "url": safe_url,
                "score": int(record.get("score", score) or score),
                "source_id": record.get("source_id", safe_source_id),
            }

        idx = len(ref_records) + 1
        url_to_idx[safe_url] = idx
        record = {
            "idx": idx,
            "source_key": source_key,
            "title": normalize_plain_text(title),
            "url": safe_url,
            "score": int(score),
            "source_id": safe_source_id,
        }
        ref_records.append(record)
        return record

    def register_default_source_ref(source_key: str) -> dict | None:
        row = first_source_row_map.get(source_key)
        if not row:
            return None
        source_id = normalize_source_id_token(row.get("source_id", ""))
        return register_ref(
            source_key=source_key,
            title=str(row.get("title", "")),
            url=str(row.get("url", "")),
            score=60,
            source_id=source_id,
        )

    def score_candidate(context_text: str, candidate: dict) -> int:
        context_norm = normalize_plain_text(context_text).lower()
        match_text = normalize_plain_text(candidate.get("match_text", "")).lower()
        if not context_norm or not match_text:
            return 0

        context_tokens = split_match_tokens(context_norm)
        cand_tokens = candidate.get("tokens", set())
        if not isinstance(cand_tokens, set):
            cand_tokens = split_match_tokens(match_text)

        overlap = context_tokens & cand_tokens
        token_score = 0
        for token in overlap:
            if len(token) >= 8:
                token_score += 5
            elif len(token) >= 4:
                token_score += 3
            else:
                token_score += 1

        exact_bonus = 0
        if match_text and match_text in context_norm:
            exact_bonus += 20
        title_norm = normalize_plain_text(candidate.get("title", "")).lower()
        if title_norm and title_norm in context_norm:
            exact_bonus += 12

        for token in re.findall(r"@[a-z0-9_]{2,32}", match_text):
            if token in context_norm:
                exact_bonus += 8
        for token in re.findall(r"[a-z0-9][a-z0-9_\-/.]{2,36}", match_text):
            if token in context_norm:
                exact_bonus += 2
        for token in re.findall(r"[\u4e00-\u9fff]{2,10}", match_text):
            if token in context_norm:
                exact_bonus += 1
        return token_score + exact_bonus

    def alloc_ref(source_key: str, context_text: str, allow_rank_fallback: bool = False) -> dict | None:
        candidates = pools.get(source_key, [])
        if not candidates:
            return None

        best_idx = -1
        best_score = -1
        for idx, candidate in enumerate(candidates):
            if not candidate.get("url"):
                continue
            score = score_candidate(context_text, candidate)
            if idx in used_candidate_indexes[source_key]:
                score -= 2
            if score > best_score:
                best_score = score
                best_idx = idx

        if best_idx < 0:
            return None
        chosen = candidates[best_idx]
        url = chosen.get("url", "")
        title = chosen.get("title", "")
        if not url:
            return None
        if best_score < min_score and len(candidates) > 1:
            if not allow_rank_fallback:
                return None
            fallback_idx = None
            for idx, candidate in enumerate(candidates):
                if not candidate.get("url"):
                    continue
                if idx not in used_candidate_indexes[source_key]:
                    fallback_idx = idx
                    break
            if fallback_idx is None:
                fallback_idx = 0
            chosen = candidates[fallback_idx]
            best_idx = fallback_idx
            url = chosen.get("url", "")
            title = chosen.get("title", "")
            best_score = 0
            if not url:
                return None

        used_candidate_indexes[source_key].add(best_idx)
        return register_ref(
            source_key=source_key,
            title=title,
            url=url,
            score=best_score,
            source_id="",
        )

    def repl_source_id(match: re.Match) -> str:
        raw = match.group(1)
        context_left = ai_text[max(0, match.start() - 220): match.start()]
        context_right = ai_text[match.end(): min(len(ai_text), match.end() + 120)]
        context_text = f"{context_left} {context_right}"
        parts = [p.strip() for p in re.split(r"[，,、/|;+；\s]+", raw) if p.strip()]
        refs: list[str] = []
        seen_idx = set()
        for part in parts:
            token = normalize_source_id_token(part)
            row = source_id_map.get(token)
            ref = None
            if row:
                ref = register_ref(
                    source_key=str(row.get("source_key", "")),
                    title=str(row.get("title", "")),
                    url=str(row.get("url", "")),
                    score=100,
                    source_id=token,
                )
            else:
                source_key = None
                # 兼容超目录上限的来源ID（如 WB23），按来源前缀与序号直取池内条目。
                m = re.match(r"^([A-Z]{2,3})(\d{2,3})$", token)
                if m:
                    prefix = m.group(1)
                    source_key = AI_SOURCE_PREFIX_TO_KEY.get(prefix)
                    if source_key:
                        rank = int(m.group(2))
                        candidates = [c for c in (pools.get(source_key, []) or []) if isinstance(c, dict)]
                        if 1 <= rank <= len(candidates):
                            chosen = candidates[rank - 1]
                            ref = register_ref(
                                source_key=source_key,
                                title=str(chosen.get("title", "")),
                                url=str(chosen.get("url", "")),
                                score=100,
                                source_id=f"{prefix}{rank:02d}",
                            )

                if ref:
                    pass
                else:
                    source_key = normalize_source_label_to_key(part)
                if source_key:
                    # 兼容模型误写“来源ID: 市场数据分析”等非标准ID标签。
                    ref = alloc_ref(
                        source_key=source_key,
                        context_text=context_text,
                        allow_rank_fallback=True,
                    )
                    if ref and int(ref.get("score", 0) or 0) < 40:
                        fallback_ref = register_default_source_ref(source_key)
                        if fallback_ref:
                            ref = fallback_ref
                        idx = int(ref.get("idx", 0) or 0)
                        if 1 <= idx <= len(ref_records):
                            ref_records[idx - 1]["score"] = max(int(ref_records[idx - 1].get("score", 0) or 0), 40)
                        ref["score"] = max(int(ref.get("score", 0) or 0), 40)
            if not ref:
                continue
            idx = int(ref["idx"])
            if idx in seen_idx:
                continue
            seen_idx.add(idx)
            refs.append(f"[{to_superscript(idx)}]({ref['url']})")
        if not refs:
            return match.group(0)
        return "".join(refs)

    def repl(match: re.Match) -> str:
        raw = match.group(1)
        context_left = ai_text[max(0, match.start() - 220): match.start()]
        context_right = ai_text[match.end(): min(len(ai_text), match.end() + 120)]
        context_text = f"{context_left} {context_right}"
        parts = [p.strip() for p in re.split(r"[，,、/|;+；]+", raw) if p.strip()]
        tokens: list[str] = []
        seen_token = set()
        for part in parts:
            key = normalize_source_label_to_key(part)
            if not key:
                continue
            part_norm = normalize_plain_text(part).lower()
            generic_tokens = {
                "twitter": {"twitter", "推特", "x"},
                "wechat": {"微信", "公众号"},
                "news": {"热榜", "news", "newsnow"},
                "github": {"github"},
                "market": {"市场", "市场数据", "本期市场数据"},
                "web": {"联网", "搜索", "web", "联网搜索"},
            }
            allow_rank_fallback = False
            for token in generic_tokens.get(key, set()):
                if token and token in part_norm:
                    allow_rank_fallback = True
                    break
            ref = alloc_ref(key, context_text=context_text, allow_rank_fallback=allow_rank_fallback)
            if not ref:
                continue
            if int(ref.get("score", 0) or 0) < 40:
                fallback_ref = register_default_source_ref(key)
                if fallback_ref:
                    ref = fallback_ref
                idx = int(ref.get("idx", 0) or 0)
                if 1 <= idx <= len(ref_records):
                    ref_records[idx - 1]["score"] = max(int(ref_records[idx - 1].get("score", 0) or 0), 40)
                ref["score"] = max(int(ref.get("score", 0) or 0), 40)
            idx = int(ref["idx"])
            url = str(ref["url"])
            if idx in seen_token:
                continue
            seen_token.add(idx)
            sup = to_superscript(idx)
            tokens.append(f"[{sup}]({url})")
        if not tokens:
            return match.group(0)
        return "".join(tokens)

    converted = source_id_pattern.sub(repl_source_id, ai_text)
    converted = source_tag_pattern.sub(repl, converted)

    def repl_legacy_source(match: re.Match) -> str:
        raw = normalize_plain_text(match.group(1))
        if not raw:
            return match.group(0)

        raw_lower = raw.lower()
        if raw_lower.startswith("来源id") or raw_lower.startswith("来源"):
            return match.group(0)
        if re.fullmatch(r"[0-9\s,，.;；:：\-⁰¹²³⁴⁵⁶⁷⁸⁹]+", raw):
            return match.group(0)

        context_left = converted[max(0, match.start() - 220): match.start()]
        context_right = converted[match.end(): min(len(converted), match.end() + 120)]
        context_text = f"{context_left} {context_right}"

        parts = [p.strip() for p in re.split(r"[，,、/|;+；]+|\s+", raw) if p.strip()]
        if not parts:
            return match.group(0)

        refs: list[str] = []
        seen_idx = set()
        recognized_any = False

        for part in parts:
            token = normalize_source_id_token(part)
            ref = None
            if token:
                m = re.match(r"^([A-Z]{2,3})(\d{2,3})$", token)
                if m and AI_SOURCE_PREFIX_TO_KEY.get(m.group(1)):
                    recognized_any = True
                    row = source_id_map.get(token)
                    if row:
                        ref = register_ref(
                            source_key=str(row.get("source_key", "")),
                            title=str(row.get("title", "")),
                            url=str(row.get("url", "")),
                            score=100,
                            source_id=token,
                        )
                    else:
                        prefix = m.group(1)
                        source_key = AI_SOURCE_PREFIX_TO_KEY.get(prefix)
                        rank = int(m.group(2))
                        candidates = [c for c in (pools.get(source_key, []) or []) if isinstance(c, dict)]
                        if 1 <= rank <= len(candidates):
                            chosen = candidates[rank - 1]
                            ref = register_ref(
                                source_key=source_key,
                                title=str(chosen.get("title", "")),
                                url=str(chosen.get("url", "")),
                                score=100,
                                source_id=f"{prefix}{rank:02d}",
                            )

            if not ref:
                source_key = normalize_source_label_to_key(part)
                if source_key:
                    recognized_any = True
                    ref = alloc_ref(
                        source_key=source_key,
                        context_text=context_text,
                        allow_rank_fallback=True,
                    )
                    if ref and int(ref.get("score", 0) or 0) < 40:
                        fallback_ref = register_default_source_ref(source_key)
                        if fallback_ref:
                            ref = fallback_ref
                        idx = int(ref.get("idx", 0) or 0)
                        if 1 <= idx <= len(ref_records):
                            ref_records[idx - 1]["score"] = max(int(ref_records[idx - 1].get("score", 0) or 0), 40)
                        ref["score"] = max(int(ref.get("score", 0) or 0), 40)

            if not ref:
                continue
            idx = int(ref["idx"])
            if idx in seen_idx:
                continue
            seen_idx.add(idx)
            refs.append(f"[{to_superscript(idx)}]({ref['url']})")

        if not recognized_any or not refs:
            return match.group(0)
        return "".join(refs)

    converted = legacy_source_pattern.sub(repl_legacy_source, converted)
    if not ref_records:
        return converted, "", []

    lines = ["\n### 📎 引用脚注\n"]
    for record in ref_records:
        idx = int(record.get("idx", 0))
        source_key = str(record.get("source_key", ""))
        title = str(record.get("title", "")).strip()
        url = str(record.get("url", "")).strip()
        score = int(record.get("score", 0) or 0)
        source_id = normalize_source_id_token(record.get("source_id", ""))
        score_text = f"匹配分={score}"
        source_id_text = f"，来源ID={source_id}" if source_id else ""
        lines.append(
            f"{idx}. [{title}]({url})（{AI_SOURCE_LABEL.get(source_key, source_key)}，{score_text}{source_id_text}）"
        )

    return converted, "\n".join(lines) + "\n", ref_records


def generate_citation_verification_section(ai_text: str, ref_records: list[dict]) -> str:
    """生成引用匹配校验结果，便于持续核验链接对齐质量。"""
    unresolved_id_tags = re.findall(r"\[来源ID:\s*([^\]]+)\]", ai_text or "", flags=re.IGNORECASE)
    unresolved_tags = re.findall(r"\[来源:\s*([^\]]+)\]", ai_text or "")
    unresolved_legacy_tags: list[str] = []
    for raw in re.findall(r"\[([^\[\]\n]{1,80})\](?!\()", ai_text or ""):
        text = normalize_plain_text(raw)
        text_lower = text.lower()
        if not text:
            continue
        if text_lower.startswith("来源id") or text_lower.startswith("来源"):
            continue
        if re.fullmatch(r"[0-9\s,，.;；:：\-⁰¹²³⁴⁵⁶⁷⁸⁹]+", text):
            continue

        parts = [p.strip() for p in re.split(r"[，,、/|;+；]+|\s+", text) if p.strip()]
        has_source_hint = False
        for part in parts:
            token = normalize_source_id_token(part)
            m = re.match(r"^([A-Z]{2,3})(\d{2,3})$", token)
            if m and AI_SOURCE_PREFIX_TO_KEY.get(m.group(1)):
                has_source_hint = True
                break
            if normalize_source_label_to_key(part):
                has_source_hint = True
                break
        if has_source_hint:
            unresolved_legacy_tags.append(text)

    low_score_refs = [
        r for r in ref_records
        if isinstance(r, dict) and int(r.get("score", 0) or 0) < int(os.environ.get("AI_CITATION_WARN_SCORE", "7"))
    ]
    unresolved_total = len(unresolved_id_tags) + len(unresolved_tags) + len(unresolved_legacy_tags)
    if unresolved_total:
        logger.warning("⚠️ 引用匹配未完全覆盖，未匹配标签数: %s", unresolved_total)
    if low_score_refs:
        logger.warning("⚠️ 存在低置信引用，建议人工复核，数量: %s", len(low_score_refs))

    lines = ["## 🧪 引用匹配校验\n"]
    lines.append(f"- 已匹配引用条数: {len(ref_records)}")
    lines.append(f"- 未完成匹配标签: {unresolved_total}")
    if unresolved_total:
        sample_rows = unresolved_id_tags[:3] + unresolved_tags[:3] + unresolved_legacy_tags[:3]
        sample = "；".join(sample_rows[:5])
        lines.append(f"- 未匹配示例: {sample}")
    lines.append(f"- 低置信引用条数: {len(low_score_refs)}")
    if low_score_refs:
        lines.append("- 处理建议: 检查上述低分脚注；必要时以“原始链接索引”人工复核。")
    else:
        lines.append("- 处理建议: 本次未发现低置信引用。")
    return "\n".join(lines) + "\n"


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
    "quant": ("quant", "backtest", "backtesting", "factor", "alpha", "timeseries", "orderbook", "risk-model"),
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
    bonus = {"fintech": 40.0, "quant": 34.0, "ai": 28.0, "web3": 24.0, "general": 0.0}.get(theme, 0.0)
    return math.log1p(max(stars, 0.0)) * 12.0 + bonus


def build_github_focus_snapshot(market: dict, top_n: int = 18, previous_context: str = "") -> list[dict]:
    """抽取 GitHub 重点项目（融合多池数据 + 主题去重 + 历史降重）。"""
    github_data = (market.get("data", {}) or {}).get("github", {}) if isinstance(market, dict) else {}
    if not isinstance(github_data, dict):
        return []

    previous_repo_names = {
        x.lower() for x in re.findall(r"\b[a-z0-9_.-]+/[a-z0-9_.-]+\b", normalize_plain_text(previous_context).lower())
    }

    merged: list[dict] = []
    seen = set()
    for key in ("trending", "ai_trending", "fintech_trending", "quant_trending", "web3_trending", "interesting_trending"):
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
            full_name = normalize_plain_text(copied.get("full_name", "")).lower()
            if full_name and full_name in previous_repo_names:
                copied["score"] = float(copied["score"]) * 0.62
                copied["is_recent_repeat"] = True
            else:
                copied["is_recent_repeat"] = False
            merged.append(copied)

    merged.sort(key=lambda x: (x.get("score", 0), float(x.get("stars", 0) or 0)), reverse=True)
    theme_caps = {"fintech": 5, "quant": 5, "ai": 8, "web3": 4, "general": 5}
    selected: list[dict] = []
    theme_counts = {k: 0 for k in theme_caps}
    for repo in merged:
        theme = str(repo.get("theme", "general"))
        cap = int(theme_caps.get(theme, 4))
        if theme_counts.get(theme, 0) >= cap:
            continue
        selected.append(repo)
        theme_counts[theme] = theme_counts.get(theme, 0) + 1
        if len(selected) >= top_n:
            break
    if len(selected) < top_n:
        used = {r.get("full_name") or r.get("url") or r.get("name") for r in selected}
        for repo in merged:
            key = repo.get("full_name") or repo.get("url") or repo.get("name")
            if key in used:
                continue
            selected.append(repo)
            if len(selected) >= top_n:
                break
    return selected[:top_n]


def format_github_focus_for_ai(market: dict, previous_context: str = "") -> str:
    """格式化 GitHub 热门项目重点，强调金融科技/AI/Web3。"""
    repos = build_github_focus_snapshot(market, previous_context=previous_context)
    if not repos:
        return "暂无 GitHub 趋势数据"

    lines = [f"GitHub 重点项目 {len(repos)} 个（按热度+主题相关性排序）："]
    grouped: dict[str, list[dict]] = {"fintech": [], "quant": [], "ai": [], "web3": [], "general": []}
    for repo in repos:
        grouped.setdefault(repo.get("theme", "general"), []).append(repo)

    label_map = {"fintech": "金融科技", "quant": "量化", "ai": "AI", "web3": "Web3", "general": "有意思项目/通用开发"}
    for theme in ("fintech", "quant", "ai", "web3", "general"):
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


def twitter_item_dedup_key(tweet: dict) -> str:
    """生成推文去重键（优先 id / url）。"""
    tweet_id = str(tweet.get("id", "") or "").strip()
    if tweet_id:
        return f"id:{tweet_id}"
    url = clean_external_url(tweet.get("url")) or clean_external_url(tweet.get("nitter_url"))
    if url:
        return f"url:{url}"
    username = normalize_plain_text(tweet.get("username", "") or "").lower()
    text = normalize_plain_text(tweet.get("text", "") or "").lower()[:180]
    return f"user:{username}|text:{text}"


def _parse_report_used_dt(raw_value: str) -> datetime | None:
    """解析日报已用推文记录时间。"""
    text = str(raw_value or "").strip()
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=BEIJING_TZ)
    return dt.astimezone(BEIJING_TZ)


def _load_recent_report_used_twitter_keys(date_str: str, report_type: str, lookback_hours: int) -> set[str]:
    """读取回看窗口内“日报已使用推文”的去重键。"""
    if lookback_hours <= 0 or not OUTPUT_TWITTER_USED.exists() or not date_str or not report_type:
        return set()

    anchor = report_anchor_datetime(date_str, report_type)
    cutoff = anchor - timedelta(hours=lookback_hours)
    used_keys: set[str] = set()

    try:
        with open(OUTPUT_TWITTER_USED, encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                row_dt = _parse_report_used_dt(row.get("anchor_at") or row.get("recorded_at"))
                if row_dt and row_dt < cutoff:
                    continue
                tweets = row.get("tweets", [])
                if not isinstance(tweets, list):
                    continue
                for item in tweets:
                    if not isinstance(item, dict):
                        continue
                    key = str(item.get("dedup_key", "") or "").strip()
                    if key:
                        used_keys.add(key)
    except Exception as e:
        logger.warning("⚠️ 读取推文去重记录失败: %s", e)

    return used_keys


def record_twitter_items_used_by_report(selected: list[dict], date_str: str, report_type: str):
    """记录本次日报使用的推文，供后续去重。"""
    if not selected or not date_str or not report_type:
        return

    payload = {
        "date_str": date_str,
        "report_type": report_type,
        "anchor_at": report_anchor_datetime(date_str, report_type).isoformat(),
        "recorded_at": now_beijing().isoformat(),
        "count": len(selected),
        "tweets": [
            {
                "dedup_key": twitter_item_dedup_key(tweet),
                "id": str(tweet.get("id", "") or ""),
                "username": normalize_plain_text(tweet.get("username", "") or "unknown"),
                "url": clean_external_url(tweet.get("url")) or clean_external_url(tweet.get("nitter_url")),
                "engagement": tweet_engagement(tweet),
            }
            for tweet in selected
            if isinstance(tweet, dict)
        ],
    }

    try:
        OUTPUT_TWITTER_USED.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_TWITTER_USED, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception as e:
        logger.warning("⚠️ 写入推文去重记录失败: %s", e)


def build_twitter_items_for_individual_summary(
    social: dict,
    max_items: int,
    date_str: str = "",
    report_type: str = "",
) -> list[dict]:
    """选择用于逐条简介的推文样本（含日报去重）。"""
    twitter_data = get_social_section(social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict)]
    if not tweets:
        return []

    tweets_sorted = sorted(
        tweets,
        key=lambda t: (tweet_engagement(t), str(t.get("created_at", ""))),
        reverse=True,
    )

    lookback_hours = max(0, int(os.environ.get("TWITTER_REPORT_DEDUP_LOOKBACK_HOURS", "36") or 36))
    recent_used_keys = _load_recent_report_used_twitter_keys(date_str, report_type, lookback_hours)
    if not recent_used_keys:
        return tweets_sorted[:max_items]

    selected: list[dict] = []
    skipped: list[dict] = []
    for tweet in tweets_sorted:
        dedup_key = twitter_item_dedup_key(tweet)
        if dedup_key in recent_used_keys:
            skipped.append(tweet)
            continue
        selected.append(tweet)
        if len(selected) >= max_items:
            break

    if len(selected) < max_items and skipped:
        selected.extend(skipped[: max_items - len(selected)])

    logger.info(
        "🐦 Twitter 日报去重: 回看%s小时，已用key=%s，命中过滤=%s，最终=%s",
        lookback_hours,
        len(recent_used_keys),
        len(skipped),
        len(selected[:max_items]),
    )
    return selected[:max_items]


def build_wechat_items_for_individual_summary(social: dict, max_items: int) -> list[dict]:
    """选择用于逐篇简介的公众号文章样本。"""
    wechat_data = get_social_section(social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict)]
    if not articles:
        return []
    articles_sorted = sorted(
        articles,
        key=lambda a: (wechat_article_score(a), str(a.get("publish_time", ""))),
        reverse=True,
    )
    return articles_sorted[:max_items]


def build_twitter_item_prompt(tweet: dict, idx: int, total: int, date_context: str) -> str:
    """构建单条推文简介提示词。"""
    username = normalize_plain_text(tweet.get("username", "") or "unknown")
    created = str(tweet.get("created_at", ""))[:16] or "-"
    tag = "热门讨论" if tweet.get("is_trending") else "关注账号"
    text = normalize_plain_text(tweet.get("text", ""))[:720]
    likes = int(tweet.get("likes", 0) or 0)
    retweets = int(tweet.get("retweets", 0) or 0)
    replies = int(tweet.get("replies", 0) or 0)
    return (
        f"{date_context} Twitter 逐条简介（{idx}/{total}）\n"
        f"- 账号: @{username}\n"
        f"- 类型: {tag}\n"
        f"- 时间: {created}\n"
        f"- 互动: ❤️{likes} / 🔁{retweets} / 💬{replies}\n"
        f"- 原文: {text or '无正文'}\n"
    )


def build_wechat_item_prompt(article: dict, idx: int, total: int, date_context: str) -> str:
    """构建单篇公众号文章简介提示词。"""
    account = normalize_plain_text(article.get("account_name", "") or "未知公众号")
    title = normalize_plain_text(article.get("title", "") or "无标题")
    publish_time = str(article.get("publish_time", ""))[:16] or "-"
    digest, body = extract_wechat_article_body(article, max_chars=800)
    read_count = int(article.get("read_count", 0) or 0)
    like_count = int(article.get("like_count", 0) or 0)
    comment_count = int(article.get("comment_count", 0) or 0)
    hot_tag = "热门文章" if article.get("is_hot") else "关注文章"

    return (
        f"{date_context} 微信公众号逐篇简介（{idx}/{total}）\n"
        f"- 公众号: {account}\n"
        f"- 标题: {title}\n"
        f"- 属性: {hot_tag}\n"
        f"- 发布时间: {publish_time}\n"
        f"- 互动: 阅读={read_count} 点赞={like_count} 评论={comment_count}\n"
        f"- 摘要: {digest or '无摘要'}\n"
        f"- 正文片段: {body or '无正文'}\n"
    )


def fallback_twitter_item_brief(tweet: dict) -> str:
    """单条推文简介失败时的规则化回退。"""
    text = normalize_plain_text(tweet.get("text", ""))[:120]
    engagement = tweet_engagement(tweet)
    recommendation = "精读" if tweet.get("is_trending") or engagement >= 800 else "略读"
    return (
        f"讲了什么：{text or '正文不足'}\n"
        f"关键信号：互动={engagement}，账号={tweet.get('username', 'unknown')}\n"
        f"阅读建议：{recommendation}（建议结合原推文链接核对上下文）"
    )


def fallback_wechat_item_brief(article: dict) -> str:
    """单篇公众号简介失败时的规则化回退。"""
    title = normalize_plain_text(article.get("title", ""))[:80]
    digest = normalize_plain_text(article.get("digest", ""))[:120]
    score = int(wechat_article_score(article))
    recommendation = "精读" if score >= 9000 or article.get("is_hot") else "略读"
    return (
        f"讲了什么：{title or '标题缺失'}；{digest or '摘要不足'}\n"
        f"关键信号：互动分={score}（阅读/点赞/评论综合）\n"
        f"阅读建议：{recommendation}（先看摘要再决定是否通读）"
    )


ITEM_BRIEF_LABEL_MAP = {
    "讲了什么": "summary",
    "关键信号": "signal",
    "阅读建议": "advice",
}


def parse_item_brief_fields(brief_text: str) -> dict[str, str]:
    """解析单条简介文本，统一为三段字段并去除编号前缀。"""
    fields = {"summary": "", "signal": "", "advice": ""}
    fallback_lines: list[str] = []

    for raw_line in str(brief_text or "").splitlines():
        line = normalize_plain_text(raw_line)
        if not line:
            continue
        line = re.sub(r"^\s*(?:[-*•]+\s*)?", "", line)
        line = re.sub(r"^\s*\d+\s*[).、:：-]?\s*", "", line)
        line = re.sub(r"^\s*[（(]\d+[）)]\s*", "", line)

        matched = re.match(r"^(讲了什么|关键信号|阅读建议)\s*[：:]\s*(.+)$", line)
        if matched:
            key = ITEM_BRIEF_LABEL_MAP.get(matched.group(1))
            value = normalize_plain_text(matched.group(2))
            if key and value and not fields[key]:
                fields[key] = value
            continue

        fallback_lines.append(line)

    fallback_iter = iter(fallback_lines)
    for key in ("summary", "signal", "advice"):
        if fields[key]:
            continue
        for candidate in fallback_iter:
            candidate = normalize_plain_text(candidate)
            if candidate:
                fields[key] = candidate
                break

    if not fields["summary"]:
        fields["summary"] = "信息不足"
    if not fields["signal"]:
        fields["signal"] = "信息不足"
    if not fields["advice"]:
        fields["advice"] = "略读（信息不足）"
    return fields


def parallel_item_brief_analysis(
    section_name: str,
    items: list[dict],
    system_prompt: str,
    user_prompt_builder,
    api_key: str,
    api_base: str,
    model: str,
    fallback_text_builder,
    max_tokens: int = 520,
    temperature: float = 0.3,
) -> list[str]:
    """并行执行“逐条/逐篇”AI 简介，保持输入顺序返回。"""
    if not items:
        return []

    max_parallel = int(os.environ.get("SOCIAL_ITEM_PARALLELISM", "6"))
    workers = min(get_deepseek_parallelism(), len(items), max(1, max_parallel))
    logger.info(f"🚀 [{section_name}] 逐条并行简介：{len(items)} 条，{workers} 路并发")

    results: dict[int, str] = {}
    item_map = {idx: item for idx, item in enumerate(items, start=1)}

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {}
        for idx, item in enumerate(items, start=1):
            prompt = user_prompt_builder(item, idx, len(items))
            future = executor.submit(
                call_deepseek,
                system_prompt,
                prompt,
                api_key,
                api_base,
                model,
                max_tokens,
                temperature,
            )
            future_map[future] = idx

        for future in as_completed(future_map):
            idx = future_map[future]
            item = item_map[idx]
            try:
                brief = future.result()
            except Exception as e:
                logger.error(f"❌ [{section_name}] 单条简介 {idx} 异常: {e}")
                brief = f"AI 分析失败: item {idx} exception: {e}"

            if is_ai_failure(brief):
                logger.warning(f"⚠️ [{section_name}] 单条简介 {idx} 失败，回退规则摘要")
                brief = fallback_text_builder(item)
            else:
                logger.info(f"✅ [{section_name}] 单条简介 {idx} 完成")
            results[idx] = brief

    return [results[i] for i in range(1, len(items) + 1)]


def format_twitter_individual_briefs(
    social: dict,
    date_context: str,
    api_key: str,
    api_base: str,
    model: str,
    grounding_rules: str,
    date_str: str = "",
    report_type: str = "",
) -> str:
    """生成 Twitter 逐条简介（每条独立调用 AI）。"""
    max_items = int(os.environ.get("TWITTER_AI_ITEM_MAX", "12"))
    selected = build_twitter_items_for_individual_summary(
        social,
        max_items=max_items,
        date_str=date_str,
        report_type=report_type,
    )
    if not selected:
        return "暂无 Twitter 数据"

    briefs = parallel_item_brief_analysis(
        section_name="Twitter-Item",
        items=selected,
        system_prompt=(
            "你是金融科技导读编辑。只针对输入的这一条推文，给出可快速筛读的简介。\n"
            "固定输出三行（不要编号）：\n"
            "讲了什么：\n"
            "关键信号：\n"
            "阅读建议：精读/略读 + 原因\n"
            "要求：每行尽量不超过45字，禁止引用输入外信息。\n\n"
            f"{grounding_rules}"
        ),
        user_prompt_builder=lambda item, idx, total: build_twitter_item_prompt(item, idx, total, date_context),
        api_key=api_key,
        api_base=api_base,
        model=model,
        fallback_text_builder=fallback_twitter_item_brief,
        max_tokens=420,
        temperature=0.25,
    )

    lines = [f"Twitter 逐条简介（共 {len(selected)} 条，按互动热度排序）："]
    for idx, (tweet, brief) in enumerate(zip(selected, briefs), start=1):
        username = normalize_plain_text(tweet.get("username", "") or "unknown")
        created = str(tweet.get("created_at", ""))[:16] or "-"
        engagement = tweet_engagement(tweet)
        tag = "热门" if tweet.get("is_trending") else "关注"
        text = normalize_plain_text(tweet.get("text", ""))[:160]
        link = clean_external_url(tweet.get("url"))
        brief_fields = parse_item_brief_fields(brief)
        lines.append(f"{idx}. [{tag}] @{username}")
        lines.append("   基本信息:")
        lines.append(f"   - 时间: {created}")
        lines.append(f"   - 互动: {engagement}")
        lines.append(f"   - 原文摘录: {text or '无正文'}")
        lines.append(f"   - 原文链接: [点击查看原文]({link})" if link else "   - 原文链接: 无")
        lines.append("   内容导读:")
        lines.append(f"   - 讲了什么: {brief_fields['summary']}")
        lines.append(f"   - 关键信号: {brief_fields['signal']}")
        lines.append(f"   - 阅读建议: {brief_fields['advice']}")
        lines.append("")
    record_twitter_items_used_by_report(selected, date_str=date_str, report_type=report_type)
    return "\n".join(lines)


def format_wechat_individual_briefs(
    social: dict,
    date_context: str,
    api_key: str,
    api_base: str,
    model: str,
    grounding_rules: str,
) -> str:
    """生成公众号逐篇简介（每篇独立调用 AI）。"""
    max_items = int(os.environ.get("WECHAT_AI_ITEM_MAX", "12"))
    selected = build_wechat_items_for_individual_summary(social, max_items=max_items)
    if not selected:
        return "暂无微信公众号文章"

    briefs = parallel_item_brief_analysis(
        section_name="WeChat-Item",
        items=selected,
        system_prompt=(
            "你是财经公众号导读编辑。只针对输入的这一篇文章，给出可快速筛读的简介。\n"
            "固定输出三行（不要编号）：\n"
            "讲了什么：\n"
            "关键信号：\n"
            "阅读建议：精读/略读 + 原因\n"
            "要求：每行尽量不超过55字，禁止引用输入外信息。\n\n"
            f"{grounding_rules}"
        ),
        user_prompt_builder=lambda item, idx, total: build_wechat_item_prompt(item, idx, total, date_context),
        api_key=api_key,
        api_base=api_base,
        model=model,
        fallback_text_builder=fallback_wechat_item_brief,
        max_tokens=500,
        temperature=0.25,
    )

    lines = [f"微信公众号逐篇简介（共 {len(selected)} 篇，按热度排序）："]
    for idx, (article, brief) in enumerate(zip(selected, briefs), start=1):
        account = normalize_plain_text(article.get("account_name", "") or "未知公众号")
        title = normalize_plain_text(article.get("title", "") or "无标题")
        publish_time = str(article.get("publish_time", ""))[:16] or "-"
        read_count = int(article.get("read_count", 0) or 0)
        like_count = int(article.get("like_count", 0) or 0)
        comment_count = int(article.get("comment_count", 0) or 0)
        link = clean_external_url(article.get("url"))
        brief_fields = parse_item_brief_fields(brief)
        lines.append(f"{idx}. 【{account}】{title}")
        lines.append("   基本信息:")
        lines.append(f"   - 时间: {publish_time}")
        lines.append(f"   - 互动: 阅读={read_count} 点赞={like_count} 评论={comment_count}")
        lines.append(f"   - 原文链接: [点击查看原文]({link})" if link else "   - 原文链接: 无")
        lines.append("   内容导读:")
        lines.append(f"   - 讲了什么: {brief_fields['summary']}")
        lines.append(f"   - 关键信号: {brief_fields['signal']}")
        lines.append(f"   - 阅读建议: {brief_fields['advice']}")
        lines.append("")
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
      2. Twitter 逐条独立分析 → 逐条简介
      3. 微信公众号逐篇独立分析 → 逐篇简介
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
    logger.info(f"⚙️ DeepSeek 并发上限: {parallelism} 路")

    filtered_market, market_filter_notes = market_snapshot_filter(market, date_str, report_type)
    market_filter_note_text = format_market_filter_notes(market_filter_notes)
    wechat_consensus_text = build_wechat_consensus_and_signal_text(social)
    twitter_focus_text = format_twitter_focus_for_ai(social)
    github_focus_text = format_github_focus_for_ai(filtered_market, previous_context=previous_context)
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
    
    # ─── 第2步: Twitter 逐条简介 ────────────────────────
    logger.info("🔍 [2/5] 生成 Twitter 逐条简介（逐条独立调用）...")
    twitter_summary = format_twitter_individual_briefs(
        social=social,
        date_context=date_context,
        api_key=api_key,
        api_base=api_base,
        model=model,
        grounding_rules=grounding_rules,
        date_str=date_str,
        report_type=report_type,
    )
    if twitter_summary != "暂无 Twitter 数据":
        section_summaries["twitter"] = twitter_summary

    # ─── 2.5: Twitter 海外英文信号补充 ─────────────────
    if twitter_focus_text != "暂无 Twitter 数据":
        logger.info("🔍 [2.5/5] 汇总 Twitter 英文信号...")
        twitter_focus_summary = call_deepseek(
            system_prompt=(
                "你是跨市场情报分析师。请基于给定的 Twitter 高互动样本，输出中文汇报：\n"
                "1) 海外英文信号主线（不要直译整段，提炼观点）；\n"
                "2) 与金融科技/AI/Web3 相关的具体线索；\n"
                "3) 可执行关注点与潜在误导噪音。\n\n"
                "输出 Markdown，300-500字，不要添加来源标签（最终综合层统一引用）。\n\n"
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
    
    # ─── 第3步: 微信公众号逐篇简介 ────────────────────────
    logger.info("🔍 [3/5] 生成微信公众号逐篇简介（逐篇独立调用）...")
    wechat_summary = format_wechat_individual_briefs(
        social=social,
        date_context=date_context,
        api_key=api_key,
        api_base=api_base,
        model=model,
        grounding_rules=grounding_rules,
    )
    if wechat_summary != "暂无微信公众号文章":
        section_summaries["wechat"] = wechat_summary

    # ─── 3.5: 微信共识与弱信号 ────────────────────────
    if wechat_consensus_text != "暂无微信公众号数据":
        logger.info("🔍 [3.5/5] 提炼微信共识与弱信号...")
        wechat_consensus_summary = call_deepseek(
            system_prompt=(
                "你是中文财经信息架构师。请基于输入的“跨公众号共识议题+弱信号候选”输出简洁汇报：\n"
                "1) 先写跨公众号共识（最多4点，强调哪些公众号反复提及）；\n"
                "2) 再写弱信号（最多3点，强调为什么值得提前关注）；\n"
                "3) 全文禁止空话，保持可执行。\n\n"
                "输出 Markdown，280-480字，不要添加来源标签（最终综合层统一引用）。\n\n"
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
                "输出 Markdown，450-700字，不要添加来源标签（最终综合层统一引用）。\n\n"
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
    citation_catalog_text = format_ai_citation_catalog_for_prompt(
        market=filtered_market,
        social=social,
        news=news,
        web_context=web_context,
    )

    synthesis_input = f"以下是 {date_context} 各数据源的分析结果，请进行最终综合汇总：{weekend_note}\n\n"
    synthesis_input += f"## 市场时效过滤说明\n{market_filter_note_text}\n\n"
    synthesis_input += f"## 可引用来源ID索引\n{citation_catalog_text}\n\n"

    if previous_context:
        synthesis_input += f"## 历史报告上下文（近1-2天）\n{previous_context}\n\n"

    if "market" in section_summaries:
        synthesis_input += f"## 市场数据分析\n{section_summaries['market']}\n\n"
    if "wechat_consensus" in section_summaries:
        synthesis_input += f"## 微信共识与弱信号\n{section_summaries['wechat_consensus']}\n\n"
    if "twitter" in section_summaries:
        synthesis_input += f"## Twitter 逐条简介\n{section_summaries['twitter']}\n\n"
    if "twitter_focus" in section_summaries:
        synthesis_input += f"## Twitter 英文信号补充\n{section_summaries['twitter_focus']}\n\n"
    if "wechat" in section_summaries:
        synthesis_input += f"## 微信公众号逐篇简介\n{section_summaries['wechat']}\n\n"
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
            "必须包含“发生了什么”“为什么会这样（证据强弱：高/中/低）”“下一步观察”。\n"
            "首句必须写“较上期：...”，仅写增量变化；无变化写“较上期无显著新增”。\n\n"
            "### 2.2 微信公众号共识与弱信号\n"
            "先写跨公众号重复提及的共识议题，再写弱信号候选，并给出判断依据。\n"
            "输入里含有“微信公众号逐篇简介”时，请优先引用逐篇信息，不要把多篇文章混成一句泛化结论。\n\n"
            "### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）\n"
            "挑出最值得关注的项目，说明应用场景、可落地价值、噪音风险。\n"
            "首句必须写“较上期：...”。\n\n"
            "### 2.4 Twitter 海外信号（英文内容中文汇报）\n"
            "把英文高互动内容翻译并提炼成中文结论，不要整段直译。\n"
            "输入里含有“Twitter 逐条简介”时，请基于逐条信息提炼，不要把多条推文混成一个笼统段落。\n"
            "首句必须写“较上期：...”。\n\n"
            "### 2.5 国内新闻与政策脉络\n"
            "聚焦国内社会/经济/监管动态，并说明对市场和产业链的影响。\n"
            "首句必须写“较上期：...”。\n\n"
            "## 三、明日跟踪清单\n"
            "1. ...\n2. ...\n3. ...\n\n"
            "要求：\n"
            "- 用中文，语言精炼专业\n"
            "- Markdown 格式，每个版块用 ## 标题\n"
            "- 重要数据用 **加粗**，关键判断要明确\n"
            "- 去除重复信息，交叉引用不同来源，优先回答“为什么会这样”；同一事实不要在多个版块重复表述\n"
            "- 若历史上下文已出现同一事实，除非有新增数据/反转，否则不要重复复述，改写为“延续无新增”\n"
            "- 在关键结论句末必须标注来源ID，格式仅允许 [来源ID: TW01] 或 [来源ID: TW01, GH02]\n"
            "- 只能使用“可引用来源ID索引”里给出的 ID；禁止输出 [来源: Twitter] 这类泛标签\n"
            "- 若同一结论由多个来源支撑，必须把多个来源ID写进同一个标签\n"
            "- 单节避免空话，尽量给出可验证事实；输入缺失时明确写“数据不足”\n"
            "- 字数控制：摘要 180-260 字；2.1~2.5 每节 220-380 字；跟踪清单每条 25-50 字\n"
            "- 当 2.1 缺少有效交易时段数据时，只写“数据不足 + 需补充信息”，禁止方向性推断\n"
            "- 不要输出任何关于读者身份背景的信息\n"
            "- 若提供“历史报告上下文”：先判断每节是“延续/新增/反转”；跟踪清单第1-2条必须承接历史事项（标注“延续跟进”或“收口复盘”），第3条写本期新增观察\n"
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
            "请参考下方“微信公众号逐篇简介”。\n\n"
            "### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）\n"
            "请参考下方“GitHub 项目详细分析”。\n\n"
            "### 2.4 Twitter 海外信号（英文内容中文汇报）\n"
            "请参考下方“Twitter 逐条简介”和“Twitter 英文信号详细分析”。\n\n"
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
        result_parts.append(f"### 🐦 Twitter 逐条简介\n\n{section_summaries['twitter']}\n")
    if "twitter_focus" in section_summaries:
        result_parts.append(f"### 🌐 Twitter 英文信号详细分析\n\n{section_summaries['twitter_focus']}\n")
    if "wechat" in section_summaries:
        result_parts.append(f"### 📱 微信公众号逐篇简介\n\n{section_summaries['wechat']}\n")
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

    # 股票总览（A股 + Yahoo）
    stock_overview = data.get("stock_overview", {}) if isinstance(data, dict) else {}
    if isinstance(stock_overview, dict):
        summary = stock_overview.get("summary", {}) if isinstance(stock_overview.get("summary"), dict) else {}
        tracked = int(summary.get("tracked", 0) or 0)
        if tracked > 0:
            lines.append("### 🧭 股票总览\n")
            lines.append(
                f"> 跟踪 **{tracked}** 个标的：上涨 **{int(summary.get('up', 0) or 0)}** | "
                f"下跌 **{int(summary.get('down', 0) or 0)}** | 平盘 **{int(summary.get('flat', 0) or 0)}** | "
                f"上涨占比 **{float(summary.get('up_ratio_pct', 0) or 0):.1f}%**"
            )
            by_region = stock_overview.get("by_region", [])
            if isinstance(by_region, list) and by_region:
                region_items = []
                for item in by_region[:6]:
                    if not isinstance(item, dict):
                        continue
                    region_items.append(
                        f"{item.get('region', '全球')} {float(item.get('avg_change_pct', 0) or 0):+.2f}% "
                        f"({int(item.get('up', 0) or 0)}/{int(item.get('count', 0) or 0)})"
                    )
                if region_items:
                    lines.append(f"> 区域强弱：{' | '.join(region_items)}")
            lines.append("")
    
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
    if twitter_data.get("trending_sampling_enabled"):
        used = len(twitter_data.get("trending_queries_used", []) or [])
        total = len(twitter_data.get("trending_queries_all", []) or [])
        cache_size = int(twitter_data.get("trending_cache_size", len(trending)) or 0)
        lines.append(f"- 实时采样: 本轮 query {used}/{total} | 汇总缓存 {cache_size} 条\n")

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
    used_refs: list[dict] | None = None,
) -> str:
    """生成 AI 分析区引用来源（严格与正文角标一致）。"""
    lines = ["## 🔗 AI 分析引用来源\n"]
    lines.append("> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。\n")

    if not used_refs:
        lines.append("- 当前正文未成功匹配到可点击来源标签（已保留 [来源ID: ...] 或 [来源: ...] 原标签）。")
        if report_type == "morning":
            lines.append("- 早报规则：已按策略跳过 A 股盘面分析。")
        return "\n".join(lines) + "\n"

    by_source: dict[str, list[dict]] = {}
    for ref in used_refs:
        if not isinstance(ref, dict):
            continue
        key = str(ref.get("source_key", "")).strip() or "unknown"
        by_source.setdefault(key, []).append(ref)

    for key in AI_SOURCE_ORDER:
        rows = by_source.get(key, [])
        if not rows:
            continue
        lines.append(f"### {AI_SOURCE_LABEL.get(key, key)} ({len(rows)} 条)\n")
        rows_sorted = sorted(rows, key=lambda x: int(x.get("idx", 0) or 0))
        for ref in rows_sorted:
            idx = int(ref.get("idx", 0) or 0)
            title = normalize_plain_text(ref.get("title", "")) or "未命名来源"
            url = clean_external_url(ref.get("url", ""))
            score = int(ref.get("score", 0) or 0)
            source_id = normalize_source_id_token(ref.get("source_id", ""))
            id_text = f"，来源ID={source_id}" if source_id else ""
            if url:
                lines.append(f"- [{to_superscript(idx)}] [{title}]({url})（匹配分={score}{id_text}）")
            else:
                lines.append(f"- [{to_superscript(idx)}] {title}（无可用链接）")
        lines.append("")

    if report_type == "morning":
        lines.append("> 注：早报 AI 已按规则跳过 A 股盘面数据分析。\n")

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
    github_repos = collect_github_source_repos(market)
    github_with_url = [r for r in github_repos if isinstance(r, dict) and clean_url(r.get("url"))]
    github_with_url = sorted(
        github_with_url,
        key=lambda r: (
            github_repo_score(r),
            float(r.get("stars", 0) or 0),
            str(r.get("updated_at", "")),
        ),
        reverse=True,
    )
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


def generate_speculation_brief_section(
    market: dict,
    report_type: str,
    max_points: int = 2,
) -> str:
    """
    生成小资金投机方向提示（超短版）。

    只给“观察方向”，不输出具体买卖指令。
    """
    max_points = max(1, min(int(max_points or 2), 3))
    data = market.get("data", {}) if isinstance(market, dict) else {}
    if not isinstance(data, dict):
        data = {}

    def to_float(value, default: float = 0.0) -> float:
        try:
            num = float(value)
        except (TypeError, ValueError):
            return default
        if math.isnan(num) or math.isinf(num):
            return default
        return num

    candidates: list[tuple[float, str]] = []

    # 1) A股强势板块（早报仅做观察提示，不做盘中判断）
    stock = data.get("stock_cn", {})
    sectors = stock.get("sectors", []) if isinstance(stock, dict) else []
    valid_sectors = [s for s in sectors if isinstance(s, dict)]
    if valid_sectors:
        top_sector = max(valid_sectors, key=lambda x: to_float(x.get("change_pct", 0)))
        sec_change = to_float(top_sector.get("change_pct", 0))
        if sec_change > 0:
            sec_name = str(top_sector.get("name", "A股板块")).strip() or "A股板块"
            leader = str(top_sector.get("leading_stock", "")).strip()
            leader_text = f"，龙头 {leader}" if leader else ""
            time_tag = "（次日观察）" if report_type == "evening" else ""
            candidates.append(
                (
                    abs(sec_change),
                    f"A股强势方向：{sec_name} {sec_change:+.2f}%{leader_text}{time_tag}",
                )
            )

    # 2) 全球指数高波动方向
    stock_overview = data.get("stock_overview", {})
    top_gainers = stock_overview.get("top_gainers", []) if isinstance(stock_overview, dict) else []
    top_losers = stock_overview.get("top_losers", []) if isinstance(stock_overview, dict) else []
    mover_pool = [m for m in (top_gainers[:2] + top_losers[:2]) if isinstance(m, dict)]
    if mover_pool:
        top_mover = max(mover_pool, key=lambda x: abs(to_float(x.get("change_pct", 0))))
        move = to_float(top_mover.get("change_pct", 0))
        name = str(top_mover.get("name", top_mover.get("symbol", "全球指数"))).strip() or "全球指数"
        region = str(top_mover.get("region", "全球")).strip() or "全球"
        direction = "强动量延续" if move > 0 else "高波动回撤"
        candidates.append((abs(move), f"海外指数方向：{region} {name} {move:+.2f}%（{direction}）"))

    # 3) 加密高波动方向
    crypto = data.get("crypto", {})
    coins = crypto.get("coins", []) if isinstance(crypto, dict) else []
    valid_coins = [c for c in coins if isinstance(c, dict)]
    if valid_coins:
        top_coin = max(valid_coins, key=lambda x: abs(to_float(x.get("change_24h", 0))))
        coin_change = to_float(top_coin.get("change_24h", 0))
        if abs(coin_change) >= 2.0:
            symbol = str(top_coin.get("symbol", "crypto")).upper()
            candidates.append((abs(coin_change), f"高波动资产：{symbol} 24h {coin_change:+.2f}%（轻仓快进快出）"))

    # 4) 国际商品波动方向
    futures = data.get("futures", {})
    intl = futures.get("international", []) if isinstance(futures, dict) else []
    valid_intl = [f for f in intl if isinstance(f, dict)]
    if valid_intl:
        top_future = max(valid_intl, key=lambda x: abs(to_float(x.get("change_pct", 0))))
        f_change = to_float(top_future.get("change_pct", 0))
        if abs(f_change) >= 0.8:
            fname = str(top_future.get("name", top_future.get("code", "国际商品"))).strip() or "国际商品"
            candidates.append((abs(f_change), f"商品波段方向：{fname} {f_change:+.2f}%"))

    lines = ["## 🎯 投机方向（超短）\n"]
    if not candidates:
        lines.append("- 当前无清晰高波动主线，先观察不追单。")
        lines.append("- 纪律：只做最熟悉方向，单笔止损不超过本金 1%-2%。\n")
        return "\n".join(lines)

    candidates.sort(key=lambda x: x[0], reverse=True)
    seen = set()
    picked = []
    for _, text in candidates:
        key = normalize_plain_text(text)
        if not key or key in seen:
            continue
        seen.add(key)
        picked.append(text)
        if len(picked) >= max_points:
            break

    for item in picked:
        lines.append(f"- {item}")
    lines.append("- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。\n")
    return "\n".join(lines)


def extract_wechat_health_alerts(social: dict) -> list[str]:
    """提取微信公众号登录/抓取健康提醒。"""
    wechat_data = get_social_section(social, "wechat")
    if not isinstance(wechat_data, dict) or not wechat_data:
        return []

    alerts: list[str] = []
    health_alerts = [str(x).strip() for x in wechat_data.get("health_alerts", []) if str(x).strip()]
    alerts.extend(health_alerts)

    def has_similar_alert(*keywords: str) -> bool:
        terms = [str(k).strip().lower() for k in keywords if str(k).strip()]
        if not terms:
            return False
        for item in alerts:
            text = normalize_plain_text(item).lower()
            if all(term in text for term in terms):
                return True
        return False

    if wechat_data.get("login_required"):
        auth_error = normalize_plain_text(wechat_data.get("auth_error", "")) or "检测到微信认证异常"
        if not (
            has_similar_alert("登录异常")
            or has_similar_alert("登录态", "失效")
            or has_similar_alert("invalid session")
        ):
            alerts.append(f"检测到微信公众号登录态失效风险：{auth_error}")

    follow_count = int(wechat_data.get("follow_articles_count", 0) or 0)
    hot_count = int(wechat_data.get("hot_articles_count", 0) or 0)
    if follow_count == 0 and hot_count == 0:
        if not (
            has_similar_alert("抓取", "0 篇")
            or has_similar_alert("0 篇")
            or has_similar_alert("账号搜索失败占比")
        ):
            alerts.append("本次微信公众号抓取结果为 0 篇，请检查登录态或服务状态。")

    hot_errors = [normalize_plain_text(e) for e in wechat_data.get("hot_errors", []) if normalize_plain_text(e)]
    auth_hot_errors = [e for e in hot_errors if ("认证信息无效" in e or "登录" in e and ("失效" in e or "过期" in e))]
    if auth_hot_errors:
        alerts.append(f"热门抓取接口返回认证异常（示例：{auth_hot_errors[0]}）。")

    # 去重并保序
    dedup = []
    seen = set()
    for item in alerts:
        key = normalize_plain_text(item)
        if not key or key in seen:
            continue
        seen.add(key)
        dedup.append(str(item).strip())
    return dedup


def generate_source_health_alert_section(social: dict, report_type: str, date_str: str) -> str:
    """生成报告顶部的数据源健康提醒（用于 Notion/邮件同步提醒）。"""
    wechat_alerts = extract_wechat_health_alerts(social)
    if not wechat_alerts:
        return ""

    lines = ["## 🚨 数据源健康提醒\n"]
    for idx, alert in enumerate(wechat_alerts, start=1):
        lines.append(f"{idx}. {alert}")
    lines.append("")
    lines.append("处理建议：")
    lines.append("1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。")
    lines.append("2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。")
    lines.append(
        f"3. 然后执行 `./scripts/local.sh report {report_type} {date_str}` 与 "
        f"`./scripts/local.sh notion-push {report_type} {date_str}` 覆盖 Notion 页面。"
    )
    return "\n".join(lines) + "\n"


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
    spec_cfg = report_cfg.get("speculation", {}) if isinstance(report_cfg, dict) else {}
    if not isinstance(spec_cfg, dict):
        spec_cfg = {}
    spec_enabled = bool(spec_cfg.get("enabled", True))
    env_spec_flag = os.environ.get("REPORT_SPECULATION_ENABLED")
    if env_spec_flag is not None:
        spec_enabled = parse_bool(env_spec_flag, spec_enabled)
    try:
        spec_max_points = int(spec_cfg.get("max_points", 2) or 2)
    except (TypeError, ValueError):
        spec_max_points = 2
    env_spec_points = os.environ.get("REPORT_SPECULATION_MAX_POINTS")
    if env_spec_points is not None:
        try:
            spec_max_points = int(env_spec_points)
        except (TypeError, ValueError):
            pass
    spec_max_points = max(1, min(spec_max_points, 3))
    
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
        logger.info("🧩 已加载前 1-2 天历史报告上下文")
    else:
        logger.info("🧩 未找到可用历史报告，跳过上下文衔接")

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
    ai_summary, ai_footnote_section, ai_ref_records = convert_ai_source_tags_to_clickable_refs(
        ai_summary,
        market=market,
        social=social,
        news=news,
        web_context=web_context,
    )
    citation_check_section = generate_citation_verification_section(ai_summary, ai_ref_records)
    
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

    health_alert_section = generate_source_health_alert_section(
        social=social,
        report_type=report_type,
        date_str=date_str,
    )
    if health_alert_section:
        report_parts.append(health_alert_section)
    
    # AI 分析摘要
    report_parts.append("# 🤖 AI 分析摘要\n")
    report_parts.append(ai_summary)
    if ai_footnote_section:
        report_parts.append(ai_footnote_section)
    report_parts.append(citation_check_section)
    if spec_enabled:
        report_parts.append(
            generate_speculation_brief_section(
                market,
                report_type=report_type,
                max_points=spec_max_points,
            )
        )
    report_parts.append(generate_web_context_section(web_context))
    report_parts.append(
        generate_ai_reference_section(
            market,
            social,
            news,
            report_type,
            web_context=web_context,
            used_refs=ai_ref_records,
        )
    )
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
