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
import json
import os
import sqlite3
import sys
import logging
import re
import time
from datetime import datetime, timedelta
from pathlib import Path
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
#  2. 数据格式化（给 AI 的全量版）
# ══════════════════════════════════════════════════════

def format_market_for_ai(market: dict) -> str:
    """格式化市场数据给 AI 分析（含板块指数）"""
    data = market.get("data", {})
    lines = []
    
    # A股主要指数
    stock = data.get("stock_cn", {})
    if stock and stock.get("market_closed"):
        lines.append(f"【A股】{stock.get('market_status', 'A股休市')}")
    if stock and stock.get("indices"):
        lines.append("【A股主要指数】")
        for idx in stock["indices"]:
            if isinstance(idx, dict):
                lines.append(f"  {idx.get('name','')}: {idx.get('price',0):.2f} ({idx.get('change_pct',0):+.2f}%)")
    
    # A股板块指数
    sectors = stock.get("sectors", []) if stock else []
    if sectors:
        # 按涨跌幅排序
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
    
    # 北向资金
    north = stock.get("north_flow", {}) if stock else {}
    if north:
        lines.append("【北向资金】")
        for k, v in north.items():
            if isinstance(v, (int, float)):
                lines.append(f"  {k}: {v:.2f}亿")
    
    # 市场统计
    mstats = stock.get("market_stats", {}) if stock else {}
    if mstats:
        lines.append("【市场统计】")
        for k, v in mstats.items():
            lines.append(f"  {k}: {v}")
    
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
        cat_names = {"commodity": "国内商品期货", "index_futures": "股指期货", "international": "国际期货"}
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
            return content
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
                    date_str: str, iso_date: str, report_label: str, time_range: str) -> str:
    """
    分批调用 DeepSeek，每个数据源独立分析，最后综合汇总。
    
    步骤:
      1. 市场+板块数据 → 市场分析
      2. Twitter 分片并行(默认20路) → 分片摘要 → 汇总
      3. 微信分片并行(默认20路) → 分片摘要 → 汇总
      4. 热榜全量      → 热榜分析
      5. 汇总以上4份分析 → 最终综合报告
    """
    date_context = f"{iso_date} {report_label}（覆盖时段: {time_range}）"
    section_summaries = {}
    parallelism = get_deepseek_parallelism()
    logger.info(f"⚙️ DeepSeek 分片并发: {parallelism} 路")
    
    # ─── 第1步: 市场数据分析 ────────────────────────
    logger.info("🔍 [1/5] 分析市场数据...")
    market_text = format_market_for_ai(market)
    if market_text != "暂无市场数据":
        summary = call_deepseek(
            system_prompt=(
                "你是资深金融市场分析师。请对以下市场数据进行专业分析，包括：\n"
                "1. 主要指数走势判断\n"
                "2. 板块轮动分析：哪些板块在领涨/领跌，反映什么资金偏好\n"
                "3. 加密货币和商品期货的关键变化\n"
                "4. 北向资金流向暗示\n"
                "5. 涨跌驱动链条：请明确“事件/政策/情绪 -> 资金行为 -> 价格表现”的因果路径，并标注证据强弱\n\n"
                "用中文，Markdown格式，重要数据**加粗**，600-900字。"
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
                "输出中文 Markdown，180-350字，避免重复。"
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
                "中文 Markdown，150-280字。"
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
                    "按重要性排序，去重，中文 Markdown，500-800字。"
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
                "输出中文 Markdown，220-420字，尽量保留具体信息。"
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
                "中文 Markdown，180-320字。"
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
                    "中文 Markdown，800-1200字，按重要性排序。"
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
    
    # ─── 第4步: 热榜分析 ────────────────────────
    logger.info("🔍 [4/5] 分析热榜新闻...")
    news_text = format_news_for_ai(news)
    if news_text != "暂无热榜数据":
        summary = call_deepseek(
            system_prompt=(
                "你是资深新闻分析师。请对以下各平台热榜进行分析，提取：\n"
                "1. 跨平台共同关注的3-5个热点事件\n"
                "2. 与金融市场相关的重要新闻\n"
                "3. 科技/AI 相关热点\n"
                "4. 社会舆论焦点\n\n"
                "用中文，Markdown格式，300-500字。"
            ),
            user_prompt=f"以下是 {date_context} 各平台热榜新闻：\n\n{news_text}",
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=1500
        )
        section_summaries["news"] = summary
    
    # ─── 第5步: 综合汇总 ────────────────────────
    logger.info("🔍 [5/5] 生成综合分析报告...")
    
    # 检查是否为周末
    is_weekend_flag, _ = is_weekend(date_str)
    weekend_note = "【注意：今日为周末，A股休市，部分市场数据可能缺失】" if is_weekend_flag else ""
    
    synthesis_input = f"以下是 {date_context} 各数据源的分析结果，请进行最终综合汇总：{weekend_note}\n\n"
    
    if "market" in section_summaries:
        synthesis_input += f"## 市场数据分析\n{section_summaries['market']}\n\n"
    if "twitter" in section_summaries:
        synthesis_input += f"## Twitter 推文分析\n{section_summaries['twitter']}\n\n"
    if "wechat" in section_summaries:
        synthesis_input += f"## 微信公众号分析\n{section_summaries['wechat']}\n\n"
    if "news" in section_summaries:
        synthesis_input += f"## 热榜新闻分析\n{section_summaries['news']}\n\n"
    
    final_summary = call_deepseek(
        system_prompt=(
            "你是资深金融市场首席分析师，正在编写今日市场综合研报。\n"
            "用户会提供来自市场数据、Twitter、微信公众号、新闻热榜的分析结果。\n"
            "请将它们融合为一份结构清晰的综合报告，包括：\n\n"
            "## 📊 市场总览\n"
            "综合A股（含板块轮动）、加密货币、贵金属、期货的走势判断\n\n"
            "## 🔥 热点事件\n"
            "当天最重要的3-5个事件，结合多个信息源交叉验证\n\n"
            "## 🧠 涨跌驱动（为什么）\n"
            "明确解释主要市场与板块为什么涨/跌，给出驱动链条与证据强弱（高/中/低）\n\n"
            "## 🤖 科技动态\n"
            "AI、科技行业重要进展\n\n"
            "## 🌍 地缘政治\n"
            "影响市场的国际事件\n\n"
            "## 📚 重要微信文章\n"
            "从微信公众号分析中提取最重要、最值得关注的3-5篇文章，包括原文标题、公众号、简要分析（100字内）和推荐理由\n\n"
            "## 💡 投资启示\n"
            "基于以上信息的前瞻性投资建议\n\n"
            "要求：\n"
            "- 用中文，语言精炼专业\n"
            "- Markdown 格式，每个版块用 ## 标题\n"
            "- 重要数据用 **加粗**，关键判断要明确\n"
            "- 去除重复信息，交叉引用不同来源\n"
            "- 总字数 1500-3000 字"
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
            "## 📊 市场总览\n"
            "综合分析调用失败，已保留下方各板块详细分析与原始数据。\n\n"
            "## 🔥 热点事件\n"
            "请优先阅读下方 Twitter / 微信 / 热榜详细分析中的高优先级条目。\n\n"
            "## 💡 投资启示\n"
            "结合市场与社媒信息，重点关注高景气板块与政策敏感事件，控制仓位与节奏。"
        )
    
    # 组装完整 AI 分析输出
    result_parts = [final_summary]
    
    # 附上各板块详细分析（折叠展示）
    result_parts.append("\n\n---\n")
    result_parts.append("<details><summary>📑 点击展开各板块详细分析</summary>\n")
    
    if "market" in section_summaries:
        result_parts.append(f"### 📊 市场数据详细分析\n\n{section_summaries['market']}\n")
    if "twitter" in section_summaries:
        result_parts.append(f"### 🐦 Twitter 详细分析\n\n{section_summaries['twitter']}\n")
    if "wechat" in section_summaries:
        result_parts.append(f"### 📱 微信公众号详细分析\n\n{section_summaries['wechat']}\n")
    if "news" in section_summaries:
        result_parts.append(f"### 📰 热榜详细分析\n\n{section_summaries['news']}\n")
    
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
                lines.append(f"- ⭐ **{repo.get('name','')}** ({repo.get('stars',0)} stars)")
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
                time_range=time_range
            )
    else:
        ai_summary = "> ℹ️ 本次使用 `--no-ai` 参数，已跳过 DeepSeek 分析。\n"
    
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
    report_parts.append("\n---\n")
    
    # 原始数据
    report_parts.append("# 📋 原始数据\n")
    report_parts.append(generate_raw_market_section(market))
    report_parts.append(generate_raw_twitter_section(social))
    report_parts.append(generate_raw_wechat_section(social))
    report_parts.append(generate_raw_news_section(news))
    
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
