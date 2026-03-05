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
import threading
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
OUTPUT_DEBUG = PROJECT_ROOT / "output" / "debug"
OUTPUT_TWITTER_USED = PROJECT_ROOT / "output" / "twitter" / "report_used_tweets.jsonl"
OUTPUT_STATE = PROJECT_ROOT / "output" / "state"
REPORT_DEDUP_DB = OUTPUT_STATE / "report_dedup.sqlite3"
REPORT_NEXT_TRACK_FILE = OUTPUT_REPORT / "next_track_state.json"
REPORT_NEXT_TRACK_LOG = OUTPUT_REPORT / "next_track_history.jsonl"

DEFAULT_DEEPSEEK_BASE = "https://api.deepseek.com"
DEFAULT_DEEPSEEK_MODEL = "deepseek-chat"
DEFAULT_WEB_SEARCH_ENDPOINT = "https://news.google.com/rss/search"
BEIJING_TZ = ZoneInfo("Asia/Shanghai")

FLOW_TRACE_LOCK = threading.Lock()
FLOW_TRACE_STATE = {
    "enabled": False,
    "run_id": "",
    "date_str": "",
    "report_type": "",
    "args": {},
    "timeline": [],
    "raw_material": {},
    "deepseek_calls": [],
    "outputs": {},
    "deepseek_call_seq": 0,
}


def _json_safe(value):
    """尽量将对象转换为可 JSON 序列化结构。"""
    try:
        return json.loads(json.dumps(value, ensure_ascii=False, default=str))
    except Exception:
        return str(value)


def init_flow_trace(enabled: bool, date_str: str, report_type: str, args_payload: dict | None = None) -> None:
    """初始化单次报告的链路追踪状态。"""
    run_id = now_beijing().strftime("%Y%m%d_%H%M%S")
    payload = {
        "enabled": bool(enabled),
        "run_id": run_id,
        "date_str": date_str,
        "report_type": report_type,
        "args": _json_safe(args_payload or {}),
        "timeline": [],
        "raw_material": {},
        "deepseek_calls": [],
        "outputs": {},
        "deepseek_call_seq": 0,
    }
    with FLOW_TRACE_LOCK:
        FLOW_TRACE_STATE.clear()
        FLOW_TRACE_STATE.update(payload)
    if enabled:
        flow_trace_event(
            "trace_initialized",
            {
                "run_id": run_id,
                "date_str": date_str,
                "report_type": report_type,
            },
        )


def flow_trace_enabled() -> bool:
    with FLOW_TRACE_LOCK:
        return bool(FLOW_TRACE_STATE.get("enabled"))


def flow_trace_event(stage: str, payload: dict | None = None) -> None:
    """记录流程时间线。"""
    if not flow_trace_enabled():
        return
    event = {
        "timestamp": now_beijing().isoformat(),
        "stage": str(stage).strip(),
        "payload": _json_safe(payload or {}),
    }
    with FLOW_TRACE_LOCK:
        FLOW_TRACE_STATE.setdefault("timeline", []).append(event)


def flow_trace_set_raw_material(key: str, payload) -> None:
    """记录原始素材快照。"""
    if not flow_trace_enabled():
        return
    key = str(key or "").strip()
    if not key:
        return
    with FLOW_TRACE_LOCK:
        raw = FLOW_TRACE_STATE.setdefault("raw_material", {})
        raw[key] = _json_safe(payload)


def flow_trace_set_output(key: str, payload) -> None:
    """记录最终产物相关信息。"""
    if not flow_trace_enabled():
        return
    key = str(key or "").strip()
    if not key:
        return
    with FLOW_TRACE_LOCK:
        outputs = FLOW_TRACE_STATE.setdefault("outputs", {})
        outputs[key] = _json_safe(payload)


def flow_trace_next_call_id() -> int:
    if not flow_trace_enabled():
        return 0
    with FLOW_TRACE_LOCK:
        seq = int(FLOW_TRACE_STATE.get("deepseek_call_seq", 0) or 0) + 1
        FLOW_TRACE_STATE["deepseek_call_seq"] = seq
    return seq


def flow_trace_append_deepseek_call(payload: dict) -> None:
    """追加一条 DeepSeek 调用 I/O 记录。"""
    if not flow_trace_enabled():
        return
    with FLOW_TRACE_LOCK:
        FLOW_TRACE_STATE.setdefault("deepseek_calls", []).append(_json_safe(payload))


def dump_flow_trace(output_path: Path | None = None) -> Path | None:
    """将本次 trace 写入 output/debug。"""
    if not flow_trace_enabled():
        return None

    with FLOW_TRACE_LOCK:
        payload = deepcopy(FLOW_TRACE_STATE)

    calls = payload.get("deepseek_calls", [])
    payload["summary"] = {
        "deepseek_call_count": len(calls),
        "timeline_events": len(payload.get("timeline", [])),
        "raw_material_keys": sorted((payload.get("raw_material", {}) or {}).keys()),
        "output_keys": sorted((payload.get("outputs", {}) or {}).keys()),
    }
    if calls:
        first_call = calls[0]
        payload["sample_prompt"] = {
            "call_id": first_call.get("call_id"),
            "system_prompt": first_call.get("system_prompt", ""),
            "user_prompt": first_call.get("user_prompt", ""),
        }

    if output_path is None:
        run_id = payload.get("run_id", now_beijing().strftime("%Y%m%d_%H%M%S"))
        date_str = payload.get("date_str", now_beijing().strftime("%Y%m%d"))
        report_type = payload.get("report_type", "auto")
        output_path = OUTPUT_DEBUG / f"flow_{date_str}_{report_type}_{run_id}.json"

    output_path = Path(output_path).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


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
    strict_market_age_hours = max(1, int(os.environ.get("REPORT_STRICT_MARKET_MAX_AGE_HOURS", "12") or 12))
    future_skew_hours = max(
        0.1,
        float(os.environ.get("REPORT_MARKET_FUTURE_SKEW_MINUTES", "30") or 30) / 60.0,
    )
    max_change_pct_abs = max(5.0, float(os.environ.get("REPORT_MAX_CHANGE_PCT_ABS", "40") or 40))
    had_yahoo_stock = isinstance(data.get("yahoo_stock"), dict) and bool(data.get("yahoo_stock"))
    had_us_stock = isinstance(data.get("us_stock"), dict) and bool(data.get("us_stock"))

    def _drop(key: str, reason: str) -> None:
        if key in data:
            data.pop(key, None)
            notes.append(reason)

    def _as_float(raw) -> float | None:
        try:
            num = float(raw)
        except (TypeError, ValueError):
            return None
        if math.isnan(num) or math.isinf(num):
            return None
        return num

    def _sanitize_rows(rows: list[dict], *, price_key: str, change_key: str, label: str) -> tuple[list[dict], int]:
        cleaned: list[dict] = []
        removed = 0
        for row in rows:
            if not isinstance(row, dict):
                removed += 1
                continue
            price = _as_float(row.get(price_key))
            change_pct = _as_float(row.get(change_key))
            # 数值异常：缺价格、价格<=0、涨跌幅绝对值异常过大
            if price is None or price <= 0:
                removed += 1
                continue
            if change_pct is None or abs(change_pct) > max_change_pct_abs:
                removed += 1
                continue
            cleaned.append(row)
        if removed > 0:
            notes.append(f"{label}存在 {removed} 条数值异常记录，已从 AI 输入中剔除")
        return cleaned, removed

    def _is_stale_or_future(raw_ts: datetime | None, max_age_hours: int) -> tuple[bool, str]:
        age = hours_ago(anchor, raw_ts)
        if age < -future_skew_hours:
            return True, f"快照晚于报告锚点（timestamp={raw_ts or 'N/A'}，疑似未来数据）"
        if age > max_age_hours:
            return True, f"快照超过 {max_age_hours}h 时效窗口（timestamp={raw_ts or 'N/A'}，{age:.1f}h）"
        return False, ""

    def _is_future_snapshot(raw_ts: datetime | None) -> tuple[bool, str]:
        age = hours_ago(anchor, raw_ts)
        if age < -future_skew_hours:
            return True, f"快照晚于报告锚点（timestamp={raw_ts or 'N/A'}，疑似未来数据）"
        return False, ""

    stock = data.get("stock_cn")
    stock_ts = parse_iso_datetime(stock.get("timestamp")) if isinstance(stock, dict) else None
    if isinstance(stock, dict):
        invalid, reason = _is_stale_or_future(stock_ts, strict_market_age_hours)
        if invalid:
            _drop("stock_cn", f"A 股{reason}")
        else:
            indices = [i for i in stock.get("indices", []) if isinstance(i, dict)]
            indices, _ = _sanitize_rows(indices, price_key="price", change_key="change_pct", label="A股指数")
            stock["indices"] = indices
            sectors = [s for s in stock.get("sectors", []) if isinstance(s, dict)]
            # 板块涨跌幅采用同一异常阈值
            sectors_cleaned: list[dict] = []
            removed_sector = 0
            for row in sectors:
                pct = _as_float(row.get("change_pct"))
                if pct is None or abs(pct) > max_change_pct_abs:
                    removed_sector += 1
                    continue
                sectors_cleaned.append(row)
            if removed_sector:
                notes.append(f"A股板块存在 {removed_sector} 条数值异常记录，已从 AI 输入中剔除")
            stock["sectors"] = sectors_cleaned
            north_flow = stock.get("north_flow")
            if is_north_flow_zero_snapshot(north_flow if isinstance(north_flow, dict) else {}):
                stock.pop("north_flow", None)
                notes.append("北向资金快照三项全0（疑似未更新），已从 AI 输入中剔除")
            if not stock.get("indices") and not stock.get("sectors"):
                _drop("stock_cn", "A 股快照缺少有效指数/板块数据")

    futures = data.get("futures")
    if isinstance(futures, dict):
        futures_ts = parse_iso_datetime(futures.get("timestamp"))
        invalid, reason = _is_stale_or_future(futures_ts, strict_market_age_hours)
        if invalid:
            _drop("futures", f"期货{reason}")
        else:
            has_items = False
            for cat in ("commodity", "international", "index_futures"):
                rows = [r for r in futures.get(cat, []) if isinstance(r, dict)]
                rows, _ = _sanitize_rows(rows, price_key="price", change_key="change_pct", label=f"期货({cat})")
                futures[cat] = rows
                if rows:
                    has_items = True
            if not has_items:
                _drop("futures", "期货快照缺少有效合约数据")

    pm = data.get("precious_metal")
    if isinstance(pm, dict):
        pm_ts = parse_iso_datetime(pm.get("timestamp"))
        invalid, reason = _is_stale_or_future(pm_ts, strict_market_age_hours)
        if invalid:
            _drop("precious_metal", f"贵金属{reason}")
        else:
            rows = pm.get("metals")
            metal_rows = []
            if isinstance(rows, list):
                metal_rows = [r for r in rows if isinstance(r, dict)]
            elif isinstance(rows, dict):
                metal_rows = [r for r in rows.values() if isinstance(r, dict)]
            metal_rows, _ = _sanitize_rows(metal_rows, price_key="price", change_key="change_pct", label="贵金属")
            if isinstance(rows, list):
                pm["metals"] = metal_rows
            elif isinstance(rows, dict):
                pm["metals"] = {str(i): row for i, row in enumerate(metal_rows, start=1)}
            if not metal_rows:
                _drop("precious_metal", "贵金属快照缺少有效品种数据")

    crypto = data.get("crypto")
    if isinstance(crypto, dict):
        crypto_ts = parse_iso_datetime(crypto.get("timestamp"))
        invalid, reason = _is_future_snapshot(crypto_ts)
        if invalid:
            _drop("crypto", f"加密市场{reason}")
        else:
            coins = [c for c in crypto.get("coins", []) if isinstance(c, dict)]
            cleaned: list[dict] = []
            removed = 0
            for coin in coins:
                price = _as_float(coin.get("price"))
                pct = _as_float(coin.get("change_24h"))
                if price is None or price <= 0 or pct is None or abs(pct) > 80:
                    removed += 1
                    continue
                cleaned.append(coin)
            if removed:
                notes.append(f"加密货币存在 {removed} 条数值异常记录，已从 AI 输入中剔除")
            crypto["coins"] = cleaned
            if not cleaned:
                _drop("crypto", "加密快照缺少有效币种数据")

    github = data.get("github")
    if isinstance(github, dict):
        gh_ts = parse_iso_datetime(github.get("timestamp"))
        gh_age = hours_ago(anchor, gh_ts)
        if gh_age < -1:
            _drop("github", f"GitHub 快照晚于报告锚点（timestamp={gh_ts or 'N/A'}，疑似未来数据）")
        elif gh_age > 72:
            _drop("github", f"GitHub 趋势快照过旧（timestamp={gh_ts or 'N/A'}，{gh_age:.1f}h）")

    yahoo_stock = data.get("yahoo_stock")
    if isinstance(yahoo_stock, dict):
        ys_ts = parse_iso_datetime(yahoo_stock.get("timestamp"))
        invalid, reason = _is_stale_or_future(ys_ts, strict_market_age_hours)
        if invalid:
            _drop("yahoo_stock", f"Yahoo Finance 股票{reason}")
        else:
            markets = [m for m in yahoo_stock.get("markets", []) if isinstance(m, dict)]
            markets, _ = _sanitize_rows(markets, price_key="price", change_key="change_pct", label="Yahoo 股票")
            yahoo_stock["markets"] = markets
            if not markets:
                _drop("yahoo_stock", "Yahoo Finance 股票快照为空")

    stock_overview = data.get("stock_overview")
    if isinstance(stock_overview, dict):
        ov_ts = parse_iso_datetime(stock_overview.get("timestamp"))
        invalid, reason = _is_stale_or_future(ov_ts, strict_market_age_hours)
        if invalid:
            _drop("stock_overview", f"股票总览{reason}")
        else:
            # 若底层 A 股和 Yahoo 都不可用，总览也不应进入 AI 输入，避免语义不一致
            if "stock_cn" not in data and "yahoo_stock" not in data:
                _drop("stock_overview", "股票总览缺少底层行情支撑（A股/Yahoo 已被过滤）")

    if "us_stock" not in data and "yahoo_stock" not in data:
        if had_yahoo_stock or had_us_stock:
            notes.append("美股直连行情源存在但已因时效/可用性过滤被移除；当前美股解读仅来自文本证据")
        else:
            notes.append("当前无可用美股直连行情源；美股解读仅来自 Twitter/热榜/联网检索文本证据")

    notes.insert(
        0,
        (
            f"严格时效模式：非加密市场仅保留过去 {strict_market_age_hours}h 数据；"
            "加密市场不做过旧时效过滤，仅剔除未来时间异常与数值异常数据。"
        ),
    )

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


def load_market_data(date_str: str, report_type: str = "morning") -> dict:
    """读取市场数据，并在重跑时避免误用锚点之后的“未来快照”造成前视偏差。"""

    def _read_json(path: Path) -> dict:
        if not path.exists():
            return {}
        try:
            with open(path, encoding="utf-8") as f:
                payload = json.load(f)
            return payload if isinstance(payload, dict) else {}
        except Exception:
            return {}

    def _previous_trading_day(day_str: str) -> str:
        day = datetime.strptime(day_str, "%Y%m%d") - timedelta(days=1)
        while day.weekday() >= 5:
            day -= timedelta(days=1)
        return day.strftime("%Y%m%d")

    def _previous_calendar_day(day_str: str) -> str:
        day = datetime.strptime(day_str, "%Y%m%d") - timedelta(days=1)
        return day.strftime("%Y%m%d")

    path = OUTPUT_MARKET / f"market_data_{date_str}.json"
    payload = _read_json(path)
    # 早报固定采用“前一交易日 A 股收盘快照”，避免误用当日盘中/未来快照。
    if report_type == "morning":
        prev_day = _previous_trading_day(date_str)
        prev_path = OUTPUT_MARKET / f"market_data_{prev_day}.json"
        prev_payload = _read_json(prev_path)
        prev_stock = (
            (((prev_payload.get("data") or {}).get("stock_cn")) if isinstance(prev_payload, dict) else None)
            if prev_payload else None
        )
        if not payload and prev_payload:
            payload = prev_payload
            logger.info("🌅 早报未找到当日市场快照，改用前一交易日文件: %s", prev_path.name)
        elif payload and isinstance(prev_stock, dict) and prev_stock:
            data = payload.get("data", {})
            if not isinstance(data, dict):
                data = {}
                payload["data"] = data
            data["stock_cn"] = deepcopy(prev_stock)
            logger.info(
                "🌅 早报A股固定使用前一交易日收盘快照: %s (stock_ts=%s)",
                prev_path.name,
                prev_stock.get("timestamp", "N/A"),
            )
        elif payload:
            logger.warning("⚠️ 早报未找到可替换的前一交易日A股快照: %s", prev_path.name)

    if not payload:
        return {}

    anchor = report_anchor_datetime(date_str, report_type)
    ts_candidates = [
        parse_iso_datetime(payload.get("timestamp")),
        parse_iso_datetime(((payload.get("data") or {}).get("stock_cn") or {}).get("timestamp")),
        parse_iso_datetime(((payload.get("data") or {}).get("yahoo_stock") or {}).get("timestamp")),
    ]
    ts_candidates = [dt for dt in ts_candidates if dt is not None]
    newest_ts = max(ts_candidates) if ts_candidates else None

    # 若快照明显晚于报告锚点（例如重跑早报时拿到10:30快照），回退到前一日收盘文件
    if newest_ts and newest_ts > anchor + timedelta(minutes=30):
        if report_type == "morning":
            # 早报优先回退到“前一自然日”以保留更近的海外/加密快照，
            # 但 A 股指数仍固定使用前一交易日收盘快照，避免前视偏差。
            prev_calendar = _previous_calendar_day(date_str)
            prev_calendar_path = OUTPUT_MARKET / f"market_data_{prev_calendar}.json"
            prev_calendar_payload = _read_json(prev_calendar_path)
            if prev_calendar_payload:
                prev_trade_day = _previous_trading_day(date_str)
                prev_trade_path = OUTPUT_MARKET / f"market_data_{prev_trade_day}.json"
                prev_trade_payload = _read_json(prev_trade_path)
                prev_stock = (
                    (((prev_trade_payload.get("data") or {}).get("stock_cn")) if isinstance(prev_trade_payload, dict) else None)
                    if prev_trade_payload else None
                )
                if isinstance(prev_stock, dict) and prev_stock:
                    data = prev_calendar_payload.get("data", {})
                    if not isinstance(data, dict):
                        data = {}
                        prev_calendar_payload["data"] = data
                    data["stock_cn"] = deepcopy(prev_stock)
                logger.info(
                    "⏪ 检测到未来市场快照(%s > anchor %s)，早报回退使用 %s（A股沿用 %s）",
                    newest_ts.isoformat(),
                    anchor.isoformat(),
                    prev_calendar_path.name,
                    prev_trade_path.name,
                )
                return prev_calendar_payload

        prev_day = _previous_calendar_day(date_str)
        prev_path = OUTPUT_MARKET / f"market_data_{prev_day}.json"
        prev_payload = _read_json(prev_path)
        if prev_payload:
            logger.info(
                "⏪ 检测到未来市场快照(%s > anchor %s)，回退使用 %s",
                newest_ts.isoformat(),
                anchor.isoformat(),
                prev_path.name,
            )
            return prev_payload

    return payload


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
        metals = get_precious_metal_rows(pm)
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

    queries = choose_market_queries(market, iso_date, include_a_share=True)
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
    lookback_days: int = 3,
    max_reports: int = 6,
) -> list[Path]:
    """定位历史报告路径，覆盖最近 3 天最多 6 期上下文（按时间由近到远）。"""
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


def get_precious_metal_rows(pm_data: dict) -> list[dict]:
    """统一贵金属结构为列表，兼容 list/dict 两种存储形态。"""
    if not isinstance(pm_data, dict):
        return []
    metals = pm_data.get("metals")
    if isinstance(metals, list):
        return [m for m in metals if isinstance(m, dict)]
    if isinstance(metals, dict):
        return [m for m in metals.values() if isinstance(m, dict)]
    return []


def is_north_flow_zero_snapshot(north_flow: dict) -> bool:
    """判断北向资金是否为“全0快照”（兼容历史快照缺少标记字段）。"""
    if not isinstance(north_flow, dict) or not north_flow:
        return False
    if bool(north_flow.get("is_zero_snapshot")):
        return True
    values = [
        safe_float(north_flow.get("net_flow"), 0.0),
        safe_float(north_flow.get("hu_net_flow"), 0.0),
        safe_float(north_flow.get("shen_net_flow"), 0.0),
    ]
    return all(abs(v) < 1e-9 for v in values)


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
    """读取最近 3 天多期报告的“摘要 + 跟踪/增量认知”上下文。"""
    paths = list_previous_report_paths(
        date_str=date_str,
        report_type=report_type,
        lookback_days=int(os.environ.get("REPORT_CONTEXT_LOOKBACK_DAYS", "3")),
        max_reports=int(os.environ.get("REPORT_CONTEXT_MAX_REPORTS", "6")),
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

        match = re.search(
            r"#\s+🤖\s+(?:AI 分析摘要|详细 AI 分析)\s*(.*?)\n#\s+📋\s+原始数据",
            content,
            flags=re.S,
        )
        excerpt = match.group(1).strip() if match else content
        excerpt = re.sub(r"<details>.*?</details>", "", excerpt, flags=re.S).strip()

        summary_section = extract_markdown_section(excerpt, "## 一、摘要")
        tracking_section = (
            extract_markdown_section(excerpt, "## 六、增量认知与下期博弈锚点")
            or extract_markdown_section(excerpt, "## 三、明日跟踪清单")
        )
        report_block = [f"历史报告 {idx}: {path.name}"]
        if summary_section:
            report_block.append(
                "【摘要】\n"
                + truncate_text_preserve_lines(summary_section, max_chars=max_chars_each)
            )
        if tracking_section:
            report_block.append(
                "【增量认知/跟踪】\n"
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


def init_report_dedup_db() -> sqlite3.Connection:
    """初始化跨次推送去重库（SQLite）。"""
    OUTPUT_STATE.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(REPORT_DEDUP_DB))
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS report_used_items (
            source TEXT NOT NULL,
            dedup_key TEXT NOT NULL,
            anchor_at TEXT,
            report_date TEXT,
            report_type TEXT,
            title TEXT,
            url TEXT,
            payload TEXT,
            created_at TEXT NOT NULL,
            PRIMARY KEY (source, dedup_key)
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_report_used_items_source ON report_used_items(source)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_report_used_items_created ON report_used_items(created_at)")
    conn.commit()
    return conn


def cleanup_report_dedup(conn: sqlite3.Connection, retention_days: int) -> None:
    """清理过期去重记录。"""
    if retention_days <= 0:
        return
    cutoff = now_beijing() - timedelta(days=retention_days)
    conn.execute("DELETE FROM report_used_items WHERE created_at < ?", (cutoff.isoformat(),))
    conn.commit()


def load_recent_report_dedup_keys(
    conn: sqlite3.Connection,
    source: str,
    anchor: datetime,
    lookback_hours: int,
) -> set[str]:
    """加载回看窗口内的已使用 key。"""
    if lookback_hours <= 0:
        return set()
    cutoff = anchor - timedelta(hours=lookback_hours)
    rows = conn.execute(
        "SELECT dedup_key, created_at FROM report_used_items WHERE source = ?",
        (source,),
    ).fetchall()
    keys: set[str] = set()
    for dedup_key, created_at in rows:
        dt = _parse_report_used_dt(created_at)
        if dt and dt < cutoff:
            continue
        key = str(dedup_key or "").strip()
        if key:
            keys.add(key)
    return keys


def build_news_dedup_key(item: dict) -> str:
    """News 去重 key。"""
    title = normalize_plain_text(item.get("title", "")).lower()
    platform = normalize_plain_text(item.get("platform", "")).lower()
    if title or platform:
        return f"{platform}::{title}"
    return ""


def build_wechat_dedup_key(item: dict) -> str:
    """公众号文章去重 key。"""
    url = clean_external_url(item.get("url"))
    if url:
        return f"url:{url}"
    account = normalize_plain_text(item.get("account_name", "")).lower()
    title = normalize_plain_text(item.get("title", "")).lower()
    pub = str(item.get("publish_time", "") or "").strip()
    key = f"{account}::{title}::{pub}"
    return key.strip(":")


def build_github_dedup_key(item: dict) -> str:
    """GitHub 项目去重 key。"""
    full_name = normalize_plain_text(item.get("full_name", "")).lower()
    if full_name:
        return f"repo:{full_name}"
    url = clean_external_url(item.get("url"))
    if url:
        return f"url:{url}"
    name = normalize_plain_text(item.get("name", "")).lower()
    return f"name:{name}" if name else ""


def build_web_dedup_key(item: dict) -> str:
    """联网检索条目去重 key。"""
    url = clean_external_url(item.get("link"))
    if url:
        return f"url:{url}"
    title = normalize_plain_text(item.get("title", "")).lower()
    source = normalize_plain_text(item.get("source", "")).lower()
    if title or source:
        return f"{source}::{title}"
    return ""


def dedup_incremental_items(
    conn: sqlite3.Connection,
    source: str,
    items: list[dict],
    anchor: datetime,
    lookback_hours: int,
    key_builder,
) -> tuple[list[dict], int, list[dict]]:
    """基于 SQLite 去重，返回（增量条目、命中过滤数量、待记录条目）。"""
    recent_keys = load_recent_report_dedup_keys(conn, source, anchor, lookback_hours)
    selected: list[dict] = []
    removed = 0
    to_record: list[dict] = []

    for item in items:
        if not isinstance(item, dict):
            continue
        dedup_key = str(key_builder(item) or "").strip()
        if dedup_key and dedup_key in recent_keys:
            removed += 1
            continue
        selected.append(item)
        if dedup_key:
            recent_keys.add(dedup_key)
            to_record.append(
                {
                    "source": source,
                    "dedup_key": dedup_key,
                    "title": normalize_plain_text(
                        item.get("title")
                        or item.get("text")
                        or item.get("full_name")
                        or item.get("name")
                        or ""
                    ),
                    "url": clean_external_url(
                        item.get("url")
                        or item.get("link")
                        or item.get("nitter_url")
                    ),
                    "payload": item,
                }
            )
    return selected, removed, to_record


def persist_report_used_records(
    records: list[dict],
    date_str: str,
    report_type: str,
    anchor: datetime,
) -> None:
    """落盘本次已推送条目，供下次 12H 增量去重。"""
    if not records:
        return
    conn = init_report_dedup_db()
    retention_days = max(1, int(os.environ.get("REPORT_DEDUP_RETENTION_DAYS", "14") or 14))
    cleanup_report_dedup(conn, retention_days=retention_days)
    now_iso = now_beijing().isoformat()
    unique_records: dict[tuple[str, str], dict] = {}
    for row in records:
        source = str(row.get("source", "") or "").strip()
        key = str(row.get("dedup_key", "") or "").strip()
        if not source or not key:
            continue
        unique_records[(source, key)] = row

    for (source, key), row in unique_records.items():
        conn.execute(
            """
            INSERT INTO report_used_items
            (source, dedup_key, anchor_at, report_date, report_type, title, url, payload, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(source, dedup_key) DO UPDATE SET
                anchor_at=excluded.anchor_at,
                report_date=excluded.report_date,
                report_type=excluded.report_type,
                title=excluded.title,
                url=excluded.url,
                payload=excluded.payload,
                created_at=excluded.created_at
            """,
            (
                source,
                key,
                anchor.isoformat(),
                date_str,
                report_type,
                normalize_plain_text(row.get("title", "")),
                clean_external_url(row.get("url")),
                json.dumps(row.get("payload", {}), ensure_ascii=False),
                now_iso,
            ),
        )
    conn.commit()
    conn.close()


def apply_cross_source_incremental_dedup(
    market: dict,
    social: dict,
    news: list,
    web_context: dict,
    date_str: str,
    report_type: str,
) -> tuple[dict, dict, list[dict], dict, dict, list[dict]]:
    """
    12H 跨次增量去重：
    - 晚报默认不重复早报已推送内容（可配置）。
    - 返回去重后的数据、统计信息和待持久化记录。
    """
    lookback_hours = max(1, int(os.environ.get("REPORT_DEDUP_LOOKBACK_HOURS", "12") or 12))
    strict_delta = parse_bool(os.environ.get("REPORT_STRICT_DELTA", "1"), True)
    github_floor_count = max(0, int(os.environ.get("REPORT_GITHUB_FLOOR_COUNT", "5") or 5))
    dedup_twitter_enabled = parse_bool(os.environ.get("REPORT_DEDUP_TWITTER_ENABLED", "0"), False)
    dedup_wechat_enabled = parse_bool(os.environ.get("REPORT_DEDUP_WECHAT_ENABLED", "0"), False)
    dedup_news_enabled = parse_bool(os.environ.get("REPORT_DEDUP_NEWS_ENABLED", "0"), False)
    dedup_github_enabled = parse_bool(os.environ.get("REPORT_DEDUP_GITHUB_ENABLED", "1"), True)
    dedup_web_enabled = parse_bool(os.environ.get("REPORT_DEDUP_WEB_ENABLED", "1"), True)
    anchor = report_anchor_datetime(date_str, report_type)

    filtered_market = deepcopy(market) if isinstance(market, dict) else {}
    filtered_social = deepcopy(social) if isinstance(social, dict) else {}
    filtered_news = [n for n in (news or []) if isinstance(n, dict)]
    filtered_web = deepcopy(web_context) if isinstance(web_context, dict) else {"queries": [], "items": [], "errors": []}

    conn = init_report_dedup_db()
    cleanup_report_dedup(conn, retention_days=max(1, int(os.environ.get("REPORT_DEDUP_RETENTION_DAYS", "14") or 14)))

    dedup_records: list[dict] = []
    stats = {
        "mode": "strict" if strict_delta else "fallback",
        "lookback_hours": lookback_hours,
        "twitter_removed": 0,
        "wechat_removed": 0,
        "news_removed": 0,
        "github_removed": 0,
        "github_floor_added": 0,
        "web_removed": 0,
        "twitter_dedup_enabled": bool(dedup_twitter_enabled),
        "wechat_dedup_enabled": bool(dedup_wechat_enabled),
        "news_dedup_enabled": bool(dedup_news_enabled),
        "github_dedup_enabled": bool(dedup_github_enabled),
        "web_dedup_enabled": bool(dedup_web_enabled),
    }

    twitter_data = get_social_section(filtered_social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict)]
    if dedup_twitter_enabled:
        tw_selected, tw_removed, tw_records = dedup_incremental_items(
            conn=conn,
            source="twitter",
            items=tweets,
            anchor=anchor,
            lookback_hours=lookback_hours,
            key_builder=twitter_item_dedup_key,
        )
        if tweets and not tw_selected and not strict_delta:
            tw_selected = tweets[:]
            tw_removed = 0
            tw_records = []
    else:
        tw_selected, tw_removed, tw_records = tweets[:], 0, []
    twitter_data["tweets"] = tw_selected
    stats["twitter_removed"] = tw_removed
    dedup_records.extend(tw_records)

    if isinstance(filtered_social.get("data"), dict):
        filtered_social["data"]["twitter"] = twitter_data
    elif isinstance(filtered_social, dict):
        filtered_social["twitter"] = twitter_data

    wechat_data = get_social_section(filtered_social, "wechat")
    articles = [a for a in wechat_data.get("articles", []) if isinstance(a, dict)]
    if dedup_wechat_enabled:
        wc_selected, wc_removed, wc_records = dedup_incremental_items(
            conn=conn,
            source="wechat",
            items=articles,
            anchor=anchor,
            lookback_hours=lookback_hours,
            key_builder=build_wechat_dedup_key,
        )
        if articles and not wc_selected and not strict_delta:
            wc_selected = articles[:]
            wc_removed = 0
            wc_records = []
    else:
        wc_selected, wc_removed, wc_records = articles[:], 0, []
    wechat_data["articles"] = wc_selected
    stats["wechat_removed"] = wc_removed
    dedup_records.extend(wc_records)

    if isinstance(filtered_social.get("data"), dict):
        filtered_social["data"]["wechat"] = wechat_data
    elif isinstance(filtered_social, dict):
        filtered_social["wechat"] = wechat_data

    if dedup_news_enabled:
        ns_selected, ns_removed, ns_records = dedup_incremental_items(
            conn=conn,
            source="news",
            items=filtered_news,
            anchor=anchor,
            lookback_hours=lookback_hours,
            key_builder=build_news_dedup_key,
        )
        if filtered_news and not ns_selected and not strict_delta:
            ns_selected = filtered_news[:]
            ns_removed = 0
            ns_records = []
    else:
        ns_selected, ns_removed, ns_records = filtered_news[:], 0, []
    filtered_news = ns_selected
    stats["news_removed"] = ns_removed
    dedup_records.extend(ns_records)

    github_data = ((filtered_market.get("data", {}) or {}).get("github", {}) if isinstance(filtered_market, dict) else {})
    if isinstance(github_data, dict):
        gh_removed = 0
        gh_floor_added = 0
        gh_records_all: list[dict] = []

        def _repo_rank_key(repo: dict) -> tuple[float, str]:
            try:
                stars = float(repo.get("stars", 0) or 0)
            except (TypeError, ValueError):
                stars = 0.0
            updated_at = str(repo.get("updated_at", "") or "")
            return stars, updated_at

        for key in ("trending", "ai_trending", "fintech_trending", "quant_trending", "web3_trending", "interesting_trending"):
            repos = [r for r in github_data.get(key, []) if isinstance(r, dict)]
            if dedup_github_enabled:
                selected, removed, records = dedup_incremental_items(
                    conn=conn,
                    source="github",
                    items=repos,
                    anchor=anchor,
                    lookback_hours=lookback_hours,
                    key_builder=build_github_dedup_key,
                )
            else:
                selected, removed, records = repos[:], 0, []
            if repos and not selected and not strict_delta:
                selected = repos[:]
                removed = 0
                records = []
            # 增量+保底：严格增量下也保持最少项目数，避免 GitHub 只剩 0/1 条
            if repos and strict_delta and github_floor_count > 0:
                floor_target = min(github_floor_count, len(repos))
                if len(selected) < floor_target:
                    selected_keys = {
                        build_github_dedup_key(r)
                        for r in selected
                        if isinstance(r, dict) and build_github_dedup_key(r)
                    }
                    supplement: list[dict] = []
                    for repo in sorted(repos, key=_repo_rank_key, reverse=True):
                        repo_key = build_github_dedup_key(repo)
                        if repo_key and repo_key in selected_keys:
                            continue
                        supplement.append(repo)
                        if repo_key:
                            selected_keys.add(repo_key)
                        if len(selected) + len(supplement) >= floor_target:
                            break
                    if supplement:
                        selected = selected + supplement
                        removed = max(0, removed - len(supplement))
                        gh_floor_added += len(supplement)
            github_data[key] = selected
            gh_removed += removed
            gh_records_all.extend(records)
        stats["github_removed"] = gh_removed
        stats["github_floor_added"] = gh_floor_added
        dedup_records.extend(gh_records_all)

    web_items = [w for w in (filtered_web.get("items", []) if isinstance(filtered_web, dict) else []) if isinstance(w, dict)]
    if dedup_web_enabled:
        wb_selected, wb_removed, wb_records = dedup_incremental_items(
            conn=conn,
            source="web",
            items=web_items,
            anchor=anchor,
            lookback_hours=lookback_hours,
            key_builder=build_web_dedup_key,
        )
        if web_items and not wb_selected and not strict_delta:
            wb_selected = web_items[:]
            wb_removed = 0
            wb_records = []
    else:
        wb_selected, wb_removed, wb_records = web_items[:], 0, []
    if isinstance(filtered_web, dict):
        filtered_web["items"] = wb_selected
    stats["web_removed"] = wb_removed
    dedup_records.extend(wb_records)

    conn.close()
    return filtered_market, filtered_social, filtered_news, filtered_web, stats, dedup_records


def parse_next_track_items(text: str, max_items: int = 6) -> list[str]:
    """从报告文本中提取“下一次建议跟踪/明日跟踪清单”条目。"""
    content = str(text or "")
    section = ""
    for heading in (
        "## 🧭 下一次建议跟踪",
        "## 六、增量认知与下期博弈锚点",
        "## 三、明日跟踪清单",
        "## 6. 下一次建议跟踪",
    ):
        section = extract_markdown_section(content, heading)
        if section:
            break
    if not section:
        return []

    items: list[str] = []
    for raw in section.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line in {"---", "***"}:
            break
        if line.startswith("<details") or line.startswith("</details"):
            break
        if line.startswith("#"):
            break
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\d+[.)]\s+", "", line)
        line = normalize_plain_text(line)
        if not line:
            continue
        if line not in items:
            items.append(line)
        if len(items) >= max_items:
            break
    return items


def save_next_track_state(date_str: str, report_type: str, items: list[str]) -> None:
    """保存本期建议跟踪，供下期注入。"""
    if not items:
        return
    payload = {
        "date_str": date_str,
        "report_type": report_type,
        "anchor_at": report_anchor_datetime(date_str, report_type).isoformat(),
        "recorded_at": now_beijing().isoformat(),
        "items": items,
    }
    OUTPUT_REPORT.mkdir(parents=True, exist_ok=True)
    REPORT_NEXT_TRACK_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(REPORT_NEXT_TRACK_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def load_previous_next_track_context(date_str: str, report_type: str, max_chars: int = 1200) -> str:
    """读取上一轮建议跟踪（优先独立状态文件，不再依赖整篇历史报告）。"""
    anchor = report_anchor_datetime(date_str, report_type)
    rows: list[dict] = []

    if REPORT_NEXT_TRACK_LOG.exists():
        try:
            with open(REPORT_NEXT_TRACK_LOG, encoding="utf-8") as f:
                for raw in f:
                    line = raw.strip()
                    if not line:
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    row_anchor = _parse_report_used_dt(row.get("anchor_at") or row.get("recorded_at"))
                    if not row_anchor or row_anchor >= anchor:
                        continue
                    items = row.get("items", [])
                    if isinstance(items, list) and items:
                        rows.append(
                            {
                                "anchor_at": row_anchor,
                                "date_str": row.get("date_str", ""),
                                "report_type": row.get("report_type", ""),
                                "items": [normalize_plain_text(x) for x in items if normalize_plain_text(x)],
                            }
                        )
        except Exception as e:
            logger.warning("⚠️ 读取 next_track_history 失败: %s", e)

    if not rows and REPORT_NEXT_TRACK_FILE.exists():
        try:
            row = json.loads(REPORT_NEXT_TRACK_FILE.read_text(encoding="utf-8"))
            items = row.get("items", [])
            row_anchor = _parse_report_used_dt(row.get("anchor_at") or row.get("recorded_at"))
            if row_anchor and row_anchor < anchor and isinstance(items, list) and items:
                rows.append(
                    {
                        "anchor_at": row_anchor,
                        "date_str": row.get("date_str", ""),
                        "report_type": row.get("report_type", ""),
                        "items": [normalize_plain_text(x) for x in items if normalize_plain_text(x)],
                    }
                )
        except Exception as e:
            logger.warning("⚠️ 读取 next_track_state 失败: %s", e)

    if not rows:
        return ""

    rows_sorted = sorted(rows, key=lambda x: x["anchor_at"], reverse=True)[:2]
    parts: list[str] = []
    for idx, row in enumerate(rows_sorted, start=1):
        header = f"上一轮跟踪 {idx}: {row.get('date_str','')} {row.get('report_type','')}"
        lines = [header]
        for j, item in enumerate(row.get("items", [])[:5], start=1):
            lines.append(f"{j}. {item}")
        parts.append("\n".join(lines))
    return truncate_text_preserve_lines("\n\n".join(parts), max_chars=max_chars)


def safe_float(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def format_pct(value) -> str:
    pct = safe_float(value, 0.0)
    return f"{pct:+.2f}%"


def format_price(value, decimals: int = 2) -> str:
    num = safe_float(value, 0.0)
    return f"{num:,.{decimals}f}"


def load_rss_deep_reads(date_str: str, report_type: str, max_items: int = 2) -> list[dict]:
    """读取 12H 窗口内阮一峰 RSS。"""
    start_dt, end_dt = get_report_window(date_str, report_type)
    report_day = datetime.strptime(date_str, "%Y%m%d")
    days_to_scan = [report_day]
    if report_type == "morning":
        days_to_scan.insert(0, report_day - timedelta(days=1))

    selected: list[dict] = []
    for day in days_to_scan:
        db_path = PROJECT_ROOT / "output" / "rss" / f"{day.strftime('%Y-%m-%d')}.db"
        if not db_path.exists():
            continue
        conn = sqlite3.connect(str(db_path))
        rows = conn.execute(
            """
            SELECT i.feed_id, i.title, i.url, i.summary, i.published_at, i.last_crawl_time
            FROM rss_items i
            WHERE i.feed_id = 'ruanyifeng'
            ORDER BY i.last_crawl_time DESC
            LIMIT 40
            """
        ).fetchall()
        conn.close()

        for feed_id, title, url, summary, published_at, last_crawl_time in rows:
            pub_dt = parse_datetime_flex(published_at) or parse_datetime_flex(last_crawl_time)
            if pub_dt is None:
                continue
            if not (start_dt <= pub_dt < end_dt):
                continue
            selected.append(
                {
                    "feed_id": feed_id,
                    "title": normalize_plain_text(title),
                    "url": clean_external_url(url),
                    "summary": normalize_plain_text(summary),
                    "published_at": pub_dt.strftime("%Y-%m-%d %H:%M"),
                }
            )
            if len(selected) >= max_items:
                return selected
    return selected


def generate_tldr_3_sentences(
    ai_summary: str,
    api_key: str,
    api_base: str,
    model: str,
    iso_date: str,
    report_label: str,
) -> str:
    """生成三句 TL;DR。"""
    fallback = (
        f"{iso_date}{report_label}主要变化集中在市场波动、政策新闻与科技信号三条主线。"
        "本期内容已按12小时窗口做增量筛选，优先保留新出现的重要事件。"
        "建议先读宏观要闻和科技前沿，再结合跟踪清单执行下一轮观察。"
    )
    if not api_key or is_ai_failure(ai_summary):
        return fallback

    try:
        prompt = truncate_text_preserve_lines(ai_summary, max_chars=2800)
        text = call_deepseek(
            system_prompt=(
                "你是宏观科技日报编辑。请将输入内容压缩为严格3句话中文 TL;DR：\n"
                "1) 第一句写最关键的市场/政策变化；\n"
                "2) 第二句写科技/产业前沿信号；\n"
                "3) 第三句写可执行的跟踪重点。\n"
                "禁止编号、禁止空话、禁止超过3句。"
            ),
            user_prompt=f"{iso_date} {report_label} 详细分析：\n\n{prompt}",
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=320,
            temperature=0.3,
        )
        cleaned = normalize_plain_text(text)
        if cleaned:
            return cleaned
    except Exception:
        pass
    return fallback


def generate_panorama_brief_section(
    iso_date: str,
    report_label: str,
    time_range: str,
    generated_at: datetime,
    market: dict,
    social: dict,
    news: list,
    web_context: dict,
    tldr: str,
    next_track_items: list[str],
    dedup_stats: dict,
    report_type: str,
) -> str:
    """生成 12H 全景简报头部（你指定的固定模板）。"""
    data = market.get("data", {}) if isinstance(market, dict) else {}
    stock_cn = data.get("stock_cn", {}) if isinstance(data, dict) else {}
    yahoo = data.get("yahoo_stock", {}) if isinstance(data, dict) else {}
    crypto = data.get("crypto", {}) if isinstance(data, dict) else {}
    metals = data.get("precious_metal", {}) if isinstance(data, dict) else {}
    futures = data.get("futures", {}) if isinstance(data, dict) else {}
    github = data.get("github", {}) if isinstance(data, dict) else {}
    twitter = get_social_section(social, "twitter")
    wechat = get_social_section(social, "wechat")

    def _pick_price(row: dict) -> float:
        for key in ("price", "current", "close", "last", "value"):
            if key not in row:
                continue
            try:
                value = float(row.get(key, 0) or 0)
            except (TypeError, ValueError):
                continue
            if value != 0:
                return value
        return 0.0

    a_indices = [i for i in stock_cn.get("indices", []) if isinstance(i, dict)]
    a_indices = sorted(a_indices, key=lambda x: abs(safe_float(x.get("change_pct"), 0.0)), reverse=True)[:2]
    a_line = " | ".join(
        f"{normalize_plain_text(i.get('name','A股指数'))} {format_price(_pick_price(i))} ({format_pct(i.get('change_pct', 0))})"
        for i in a_indices
    ) if a_indices else "数据不足"

    y_indices = [i for i in yahoo.get("markets", []) if isinstance(i, dict)]
    y_indices = sorted(y_indices, key=lambda x: abs(safe_float(x.get("change_pct"), 0.0)), reverse=True)[:3]
    y_line = " | ".join(
        f"{normalize_plain_text(i.get('name', i.get('symbol', 'Global')))} {format_pct(i.get('change_pct', 0))}"
        for i in y_indices
    ) if y_indices else "数据不足"

    coins = [c for c in crypto.get("coins", []) if isinstance(c, dict)]
    btc = next((c for c in coins if str(c.get("symbol", "")).upper() == "BTC"), {})
    eth = next((c for c in coins if str(c.get("symbol", "")).upper() == "ETH"), {})
    high_beta = sorted(
        [c for c in coins if str(c.get("symbol", "")).upper() not in {"BTC", "ETH"}],
        key=lambda x: abs(safe_float(x.get("change_24h"), 0.0)),
        reverse=True,
    )[:2]
    high_beta_line = "、".join(
        f"{str(c.get('symbol', '?')).upper()} {format_pct(c.get('change_24h', 0))}" for c in high_beta
    ) if high_beta else "暂无明显高波币种"

    metals_rows = get_precious_metal_rows(metals if isinstance(metals, dict) else {})
    gold = next(
        (
            m for m in metals_rows
            if any(
                key in str(m.get("symbol", "")).lower() or key in str(m.get("name", "")).lower()
                for key in ("gold", "黄金", "xau")
            )
        ),
        {},
    )
    futures_rows: list[dict] = []
    for key in ("international", "commodity", "index_futures"):
        futures_rows.extend([x for x in futures.get(key, []) if isinstance(x, dict)])
    futures_top = sorted(futures_rows, key=lambda x: abs(safe_float(x.get("change_pct"), 0.0)), reverse=True)[:2]
    futures_line = " | ".join(
        f"{normalize_plain_text(x.get('name', x.get('symbol', '期货')))} {format_pct(x.get('change_pct', 0))}"
        for x in futures_top
    ) if futures_top else "数据不足"

    finance_news = [n for n in news if isinstance(n, dict)]
    finance_news = sorted(finance_news, key=lambda x: int(x.get("rank", 999) or 999))
    top_news = finance_news[:2]

    web_items = [w for w in web_context.get("items", []) if isinstance(w, dict)] if isinstance(web_context, dict) else []
    world_view = web_items[0] if web_items else {}

    tech_news = [
        n for n in finance_news
        if any(k in normalize_plain_text(n.get("title", "")).lower() for k in ("ai", "芯片", "模型", "算力", "机器人", "openai", "gpt"))
    ]
    wechat_articles = [a for a in wechat.get("articles", []) if isinstance(a, dict)]
    wechat_sorted = sorted(wechat_articles, key=wechat_article_score, reverse=True)
    tech_focus = tech_news[0] if tech_news else ({"title": wechat_sorted[0].get("title", ""), "platform": wechat_sorted[0].get("account_name", "")} if wechat_sorted else {})

    gh_repos = collect_github_source_repos(market)
    gh_top = sorted(gh_repos, key=lambda x: safe_float(x.get("stars"), 0.0), reverse=True)[:1]
    gh_item = gh_top[0] if gh_top else {}

    tweets = [t for t in twitter.get("tweets", []) if isinstance(t, dict)]
    tweets_sorted = sorted(tweets, key=lambda t: (tweet_engagement(t), str(t.get("created_at", ""))), reverse=True)
    top_tweets = tweets_sorted[:30]
    top_tweet_text = " ".join(normalize_plain_text(t.get("text", "")) for t in top_tweets)
    crypto_signal = "未识别明显链上叙事"
    if any(k in top_tweet_text.lower() for k in ("bitcoin", "btc", "ethereum", "eth", "defi", "stablecoin", "etf", "token")):
        crypto_signal = "高互动推文集中在 BTC/ETH、ETF 与链上流动性叙事"
    elif top_tweet_text:
        crypto_signal = "本窗口链上叙事热度一般，以宏观/政策讨论为主"

    topic_tokens = []
    for token in ("AI", "Fed/利率", "关税/贸易", "地缘政治", "芯片算力", "加密资产"):
        key_map = {
            "AI": ("ai", "openai", "model", "agent", "llm"),
            "Fed/利率": ("fed", "rate", "yield", "inflation"),
            "关税/贸易": ("tariff", "trade", "关税"),
            "地缘政治": ("ukraine", "iran", "russia", "israel"),
            "芯片算力": ("nvidia", "amd", "chip", "semiconductor", "算力", "芯片"),
            "加密资产": ("btc", "bitcoin", "eth", "crypto", "defi"),
        }
        if any(k.lower() in top_tweet_text.lower() for k in key_map[token]):
            topic_tokens.append(token)
    topic_line = "、".join(topic_tokens[:2]) if topic_tokens else "宏观与市场情绪分化"

    social_platforms = {"今日头条", "百度热搜", "澎湃新闻", "bilibili 热搜", "凤凰网", "贴吧", "微博", "抖音", "知乎"}
    social_news = [n for n in finance_news if normalize_plain_text(n.get("platform", "")) in social_platforms]
    social_top = social_news[0] if social_news else {}
    zhihu_bili = [n for n in social_news if normalize_plain_text(n.get("platform", "")) in {"知乎", "bilibili 热搜"}]
    deep_topic = zhihu_bili[0] if zhihu_bili else {}
    fun_news = [n for n in social_news if normalize_plain_text(n.get("platform", "")) in {"贴吧", "抖音", "微博"}]
    fun_topic = fun_news[0] if fun_news else {}

    rss_reads = load_rss_deep_reads(iso_date.replace("-", ""), report_type, max_items=1)
    deep_reads: list[dict] = []
    if wechat_sorted:
        deep_reads.extend(wechat_sorted[:2])
    if rss_reads:
        deep_reads.append(rss_reads[0])

    delta_note = ""
    if isinstance(dedup_stats, dict):
        github_note = f"-{dedup_stats.get('github_removed',0)}"
        github_floor = int(dedup_stats.get("github_floor_added", 0) or 0)
        if github_floor > 0:
            github_note += f"（保底+{github_floor}）"
        delta_note = (
            f"增量去重：Twitter -{dedup_stats.get('twitter_removed',0)} | "
            f"微信 -{dedup_stats.get('wechat_removed',0)} | "
            f"热榜 -{dedup_stats.get('news_removed',0)} | "
            f"GitHub {github_note} | "
            f"联网 -{dedup_stats.get('web_removed',0)}"
        )

    lines = [
        f"# 🌍 {iso_date} 12H 个人全景简报 ({'早报' if report_type == 'morning' else '晚报'})",
        f"**生成时间:** {generated_at.strftime('%Y-%m-%d %H:%M')}  |  **时间窗口:** 过去 12 小时（{time_range}）",
    ]
    if delta_note:
        lines.append(f"**Δ 增量过滤:** {delta_note}")
    lines.extend(
        [
            "",
            f"**💡 AI 导读 (TL;DR):** {tldr}",
            "",
            "---",
            "",
            "### 📊 1. 市场行情雷达 (Market Monitor)",
            f"* **股市盘点:** A股 {a_line} | 全球核心异动 {y_line}",
            f"* **加密货币:** BTC {format_price(btc.get('price', 0))} ({format_pct(btc.get('change_24h', 0))}) | ETH {format_price(eth.get('price', 0))} ({format_pct(eth.get('change_24h', 0))}) | 其他高波币种: {high_beta_line}",
            f"* **大宗贵金属:** 黄金 {format_price(_pick_price(gold))} | 核心期货异动 {futures_line}",
            "",
            "### 📰 2. 宏观财经与全网要闻 (Macro & Top News)",
            f"* **🔴 财经焦点:** {normalize_plain_text(top_news[0].get('title', '数据不足'))} - *{normalize_plain_text(top_news[0].get('platform', '来源待补'))}* （12小时内高频传播）" if top_news else "* **🔴 财经焦点:** 数据不足",
            f"* **🔴 财经焦点:** {normalize_plain_text(top_news[1].get('title', '数据不足'))} - *{normalize_plain_text(top_news[1].get('platform', '来源待补'))}*" if len(top_news) > 1 else "* **🔴 财经焦点:** 数据不足",
            f"* **🌍 国际视点:** {normalize_plain_text(world_view.get('title', '暂无联网检索国际事件'))}",
            "",
            "### 🚀 3. 科技、加密与开源前沿 (Tech & Crypto Pulse)",
            f"* **🔥 科技热点:** {normalize_plain_text(tech_focus.get('title', '暂无科技热点样本'))}",
            f"* **💻 开发者:** {normalize_plain_text(gh_item.get('full_name', '暂无 GitHub 项目'))} - {normalize_plain_text(gh_item.get('description', ''))}",
            f"* **⛓️ 链上风向:** {crypto_signal}",
            f"* **🐦 推特大V:** 过去12小时高频讨论主题：{topic_line}",
            "",
            "### 🗣️ 4. 国内社交与舆情吃瓜 (Social Chatter)",
            f"* **🔥 热搜第一:** {normalize_plain_text(social_top.get('title', '暂无'))}",
            f"* **💡 深度热议:** {normalize_plain_text(deep_topic.get('title', '暂无'))} - *当前讨论以观点分歧与政策影响评估为主*",
            f"* **🎮 娱乐/次文化:** {normalize_plain_text(fun_topic.get('title', '暂无'))}",
            "",
            "### 📚 5. 深度精读推荐 (Deep Reads)",
        ]
    )

    if deep_reads:
        for item in deep_reads[:3]:
            if item.get("feed_id") == "ruanyifeng":
                title = normalize_plain_text(item.get("title", ""))
                source = "阮一峰"
                summary = normalize_plain_text(item.get("summary", ""))[:90] or "可用于补充技术与行业趋势背景。"
                lines.append(f"* 📖 [{title}]({clean_external_url(item.get('url'))}) - *{source}* （{summary}）")
            else:
                title = normalize_plain_text(item.get("title", ""))
                source = normalize_plain_text(item.get("account_name", "公众号"))
                digest = normalize_plain_text(item.get("digest", ""))[:90] or "建议关注其对资产定价与策略框架的启发。"
                lines.append(f"* 📖 [{title}]({clean_external_url(item.get('url'))}) - *{source}* （{digest}）")
    else:
        lines.append("* 📖 暂无可用深度精读样本")

    lines.extend(["", "## 🧭 下一次建议跟踪"])
    if next_track_items:
        for idx, item in enumerate(next_track_items[:5], start=1):
            lines.append(f"{idx}. {item}")
    else:
        lines.append("1. 跟踪本窗口内最强政策变量在下一交易时段的落地进展。")
        lines.append("2. 跟踪高波动资产（加密/期货）是否出现方向反转。")
        lines.append("3. 跟踪 AI 与开源项目从话题热度到真实采用的转化。")

    lines.append("")
    return "\n".join(lines)


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
        return {"queries": [], "items": [], "errors": [], "raw_material_downloads": []}

    results: list[dict] = []
    errors: list[str] = []
    raw_material_downloads: list[dict] = []
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
                raw_material_downloads.append(
                    {
                        "query": query,
                        "fetched_count": len(rows),
                        "items": rows,
                    }
                )
                results.extend(rows)
            except Exception as e:  # pragma: no cover - network dependent
                err = f"{query}: {e}"
                logger.warning(f"⚠️ 联网检索失败: {err}")
                errors.append(err)
                raw_material_downloads.append(
                    {
                        "query": query,
                        "fetched_count": 0,
                        "items": [],
                        "error": str(e),
                    }
                )

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
        "raw_material_downloads": raw_material_downloads,
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
            for key in ("net_flow", "hu_net_flow", "shen_net_flow"):
                if key in north:
                    lines.append(f"  {key}: {safe_float(north.get(key), 0.0):+.2f}亿")
            if is_north_flow_zero_snapshot(north):
                lines.append("  提示: 当前快照三项全为0，可能为数据源未更新，避免直接推断资金方向。")

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
    metals_rows = get_precious_metal_rows(pm if isinstance(pm, dict) else {})
    if metals_rows:
        lines.append("【贵金属】")
        for metal in metals_rows:
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


def format_market_indices_watch_for_ai(market: dict) -> str:
    """提取摘要可直接引用的关键指数与异动指数。"""
    data = market.get("data", {}) if isinstance(market, dict) else {}
    lines: list[str] = []
    has_a_share_index_block = False

    stock = data.get("stock_cn", {}) if isinstance(data, dict) else {}
    if isinstance(stock, dict):
        indices = [i for i in stock.get("indices", []) if isinstance(i, dict)]
        if indices:
            watch_order = ["上证指数", "深证成指", "沪深300", "创业板指", "科创50", "中证500"]
            name_map = {normalize_plain_text(i.get("name", "")): i for i in indices}
            picked = [name_map[n] for n in watch_order if n in name_map]
            if picked:
                lines.append("【A股关键指数】")
                has_a_share_index_block = True
                for idx in picked:
                    lines.append(
                        f"  {idx.get('name','')}: {safe_float(idx.get('price'), 0.0):,.2f} ({safe_float(idx.get('change_pct'), 0.0):+.2f}%)"
                    )
            outlier = sorted(indices, key=lambda x: abs(safe_float(x.get("change_pct"), 0.0)), reverse=True)[0]
            lines.append(
                f"【A股异动指数】{outlier.get('name','未知')}: {safe_float(outlier.get('change_pct'), 0.0):+.2f}%"
            )

        north_flow = stock.get("north_flow", {})
        if isinstance(north_flow, dict) and north_flow:
            net_flow = safe_float(north_flow.get("net_flow"), 0.0)
            hu_flow = safe_float(north_flow.get("hu_net_flow"), 0.0)
            shen_flow = safe_float(north_flow.get("shen_net_flow"), 0.0)
            lines.append(
                f"【北向资金】净流入={net_flow:+.2f}亿 | 沪股通={hu_flow:+.2f}亿 | 深股通={shen_flow:+.2f}亿"
            )
            if is_north_flow_zero_snapshot(north_flow):
                lines.append("【北向资金提示】数据源当期返回全0，可能尚未更新，避免过度解读方向。")

    yahoo_stock = data.get("yahoo_stock", {}) if isinstance(data, dict) else {}
    if isinstance(yahoo_stock, dict):
        markets = [m for m in yahoo_stock.get("markets", []) if isinstance(m, dict)]
        if markets:
            if not has_a_share_index_block:
                shanghai = next(
                    (
                        item for item in markets
                        if str(item.get("symbol", "")).upper() == "000001.SS"
                        or "上证" in normalize_plain_text(item.get("name", ""))
                    ),
                    None,
                )
                if isinstance(shanghai, dict):
                    lines.append("【A股关键指数（Yahoo兜底）】")
                    lines.append(
                        f"  上证指数: {safe_float(shanghai.get('price'), 0.0):,.2f} ({safe_float(shanghai.get('change_pct'), 0.0):+.2f}%)"
                    )
            major = sorted(markets, key=lambda x: abs(safe_float(x.get("change_pct"), 0.0)), reverse=True)[:8]
            lines.append("【全球关键指数】")
            for item in major:
                name = normalize_plain_text(item.get("name", item.get("symbol", "Global")))
                lines.append(f"  {name}: {safe_float(item.get('change_pct'), 0.0):+.2f}%")
            outlier = major[0]
            lines.append(
                f"【全球异动指数】{normalize_plain_text(outlier.get('name', outlier.get('symbol', 'Global')))}: {safe_float(outlier.get('change_pct'), 0.0):+.2f}%"
            )

    return "\n".join(lines) if lines else "关键指数样本不足。"


def format_sector_structure_for_ai(market: dict) -> str:
    """提取 A 股板块强弱结构，便于盘面段落展开。"""
    data = market.get("data", {}) if isinstance(market, dict) else {}
    stock = data.get("stock_cn", {}) if isinstance(data, dict) else {}
    if not isinstance(stock, dict):
        return "A股行业板块数据：未提供。"
    sectors = [s for s in stock.get("sectors", []) if isinstance(s, dict) and s.get("change_pct") is not None]
    if not sectors:
        return "A股行业板块数据：当前窗口未抓取到有效板块涨跌（数据不足/抓取失败），请在正文显式标注。"

    sorted_rows = sorted(sectors, key=lambda x: safe_float(x.get("change_pct"), 0.0), reverse=True)
    gainers = sorted_rows[:10]
    losers = sorted_rows[-10:]

    lines = ["【A股板块结构】"]
    lines.append("板块涨幅前10：")
    for row in gainers:
        turnover = safe_float(row.get("turnover"), 0.0)
        leader = normalize_plain_text(row.get("leading_stock", ""))
        suffix = f" | 换手{turnover:.2f}%" if turnover else ""
        if leader:
            suffix += f" | 领涨{leader}"
        lines.append(f"  - {normalize_plain_text(row.get('name', '未知板块'))}: {safe_float(row.get('change_pct'), 0.0):+.2f}%{suffix}")

    lines.append("板块跌幅前10：")
    for row in losers:
        turnover = safe_float(row.get("turnover"), 0.0)
        leader = normalize_plain_text(row.get("leading_stock", ""))
        suffix = f" | 换手{turnover:.2f}%" if turnover else ""
        if leader:
            suffix += f" | 领跌{leader}"
        lines.append(f"  - {normalize_plain_text(row.get('name', '未知板块'))}: {safe_float(row.get('change_pct'), 0.0):+.2f}%{suffix}")

    return "\n".join(lines)


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
    for key in ("trending", "ai_trending", "fintech_trending", "quant_trending", "web3_trending", "interesting_trending"):
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
    if "联网" in text or "搜索" in text:
        return "web"
    if text in {"web", "websearch", "web-search", "web_search"}:
        return "web"
    if "市场" in text:
        return "market"
    return None


def normalize_inline_source_id_links(ai_text: str) -> str:
    """
    将模型直接输出的 [MK01](url) / [GH2](url) 标准化为 [来源ID: MK01]。
    这样后续统一走来源ID映射，减少格式漂移和错链风险。
    """
    text = str(ai_text or "")
    if not text:
        return text

    pattern = re.compile(
        r"\[(TW|WC|NW|GH|MK|WB)\s*[-_]?(\d{1,3})\]\((https?://[^)\s]+)\)",
        flags=re.IGNORECASE,
    )

    def _repl(match: re.Match) -> str:
        token = normalize_source_id_token(f"{match.group(1)}{match.group(2)}")
        if not token:
            return match.group(0)
        return f"[来源ID: {token}]"

    return pattern.sub(_repl, text)


def sanitize_source_id_tags(ai_text: str) -> str:
    """
    清洗 [来源ID: ...] 中的非法占位内容（如“未提供”），仅保留合法来源ID。
    """
    text = str(ai_text or "")
    if not text:
        return text

    pattern = re.compile(r"\[来源ID:\s*([^\]]+)\]", flags=re.IGNORECASE)
    valid_id_pattern = re.compile(r"^(TW|WC|NW|GH|MK|WB)\d{2,3}$")

    def _repl(match: re.Match) -> str:
        raw = str(match.group(1) or "")
        parts = [p for p in re.split(r"[，,、/|;+；\s]+", raw) if p.strip()]
        valid_tokens: list[str] = []
        for part in parts:
            token = normalize_source_id_token(part)
            if token and valid_id_pattern.match(token):
                valid_tokens.append(token)
        if not valid_tokens:
            return ""
        uniq = list(dict.fromkeys(valid_tokens))
        return f"[来源ID: {', '.join(uniq)}]"

    cleaned = pattern.sub(_repl, text)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def canonicalize_source_id_markdown_links(ai_text: str, ref_records: list[dict]) -> str:
    """
    将残留的 [MK01](url) / [GH02](url) 统一替换为角标链接，确保正文引用风格一致。
    """
    text = str(ai_text or "")
    if not text or not ref_records:
        return text

    source_to_ref: dict[str, dict] = {}
    for row in ref_records:
        if not isinstance(row, dict):
            continue
        source_id = normalize_source_id_token(row.get("source_id", ""))
        url = clean_external_url(row.get("url", ""))
        idx = int(row.get("idx", 0) or 0)
        if not source_id or not url or idx <= 0:
            continue
        source_to_ref[source_id] = {"idx": idx, "url": url}

    if not source_to_ref:
        return text

    pattern = re.compile(
        r"\[(TW|WC|NW|GH|MK|WB)\s*[-_]?(\d{1,3})\]\((https?://[^)\s]+)\)",
        flags=re.IGNORECASE,
    )

    def _repl(match: re.Match) -> str:
        token = normalize_source_id_token(f"{match.group(1)}{match.group(2)}")
        ref = source_to_ref.get(token)
        if not ref:
            return match.group(0)
        return f"[{to_superscript(int(ref['idx']))}]({ref['url']})"

    return pattern.sub(_repl, text)


def convert_ai_source_tags_to_clickable_refs(
    ai_text: str,
    market: dict,
    social: dict,
    news: list,
    web_context: dict | None = None,
) -> tuple[str, str, list[dict]]:
    """
    将 AI 输出中的 [来源: xxx] / [来源ID: xx] 转成可点击引用链接（优先显示来源ID）。
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
    url_to_source_id_map: dict[str, str] = {}
    first_source_row_map: dict[str, dict] = {}
    for row in catalog:
        if not isinstance(row, dict):
            continue
        source_id = normalize_source_id_token(row.get("source_id", ""))
        if source_id:
            source_id_map[source_id] = row
            url = clean_external_url(row.get("url", ""))
            if url:
                url_to_source_id_map[url] = source_id
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
        safe_source_id = normalize_source_id_token(source_id) or normalize_source_id_token(url_to_source_id_map.get(safe_url, ""))
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

    def _render_inline_ref(ref: dict) -> str:
        """正文内引用渲染：优先显示来源ID，保证“来源明确可点开”。"""
        if not isinstance(ref, dict):
            return ""
        url = clean_external_url(ref.get("url", ""))
        if not url:
            return ""
        source_id = normalize_source_id_token(ref.get("source_id", ""))
        if source_id:
            return f"[{source_id}]({url})"
        idx = int(ref.get("idx", 0) or 0)
        if idx <= 0:
            return ""
        return f"[{to_superscript(idx)}]({url})"

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
            token_text = _render_inline_ref(ref)
            if token_text:
                refs.append(token_text)
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
            if idx in seen_token:
                continue
            seen_token.add(idx)
            token_text = _render_inline_ref(ref)
            if token_text:
                tokens.append(token_text)
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
            token_text = _render_inline_ref(ref)
            if token_text:
                refs.append(token_text)

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
    max_en = int(os.environ.get("TWITTER_FOCUS_MAX_EN", "0") or 0)
    max_other = int(os.environ.get("TWITTER_FOCUS_MAX_OTHER", "0") or 0)
    selected_en = en_tweets if max_en <= 0 else en_tweets[:max_en]
    selected_other = zh_tweets if max_other <= 0 else zh_tweets[:max_other]

    lines = [
        f"Twitter 高互动样本：英文 {len(en_tweets)} 条，非英文 {len(zh_tweets)} 条（按互动排序）"
    ]

    lines.append("\n英文重点（请在最终报告中翻译成中文并保留关键信号）：")
    for idx, t in enumerate(selected_en, start=1):
        text = normalize_plain_text(t.get("text", ""))[:280]
        lines.append(
            f"{idx}. @{t.get('username','unknown')} | {tweet_engagement(t)} 互动 | "
            f"{str(t.get('created_at',''))[:16]} | {text}"
        )

    lines.append("\n中文/其他语种补充：")
    for idx, t in enumerate(selected_other, start=1):
        text = normalize_plain_text(t.get("text", ""))[:220]
        lines.append(
            f"{idx}. @{t.get('username','unknown')} | {tweet_engagement(t)} 互动 | "
            f"{str(t.get('created_at',''))[:16]} | {text}"
        )

    return "\n".join(lines)


DEFAULT_TWITTER_RELEVANCE_POSITIVE_KEYWORDS = (
    "fed", "fomc", "powell", "rate", "rates", "yield", "treasury", "bond", "inflation",
    "cpi", "pmi", "gdp", "recession", "liquidity", "usd", "dollar", "fx", "carry",
    "stock", "stocks", "equity", "earnings", "guidance", "ipo", "valuation", "etf",
    "option", "gamma", "volatility", "vix", "sector", "market", "macro", "policy",
    "bitcoin", "btc", "ethereum", "eth", "sol", "crypto", "defi", "stablecoin", "onchain",
    "ai", "llm", "agent", "model", "openai", "anthropic", "nvidia", "chip", "semiconductor",
    "fintech", "payment", "lending", "credit", "risk", "saas", "medtech", "biotech",
    "关税", "降息", "加息", "通胀", "利率", "收益率", "汇率", "就业", "非农", "政策",
    "财报", "估值", "资金流", "期权", "波动率", "比特币", "以太坊", "加密", "芯片", "算力",
)

DEFAULT_TWITTER_RELEVANCE_NEGATIVE_KEYWORDS = (
    "giveaway", "airdrop", "nsfw", "porn", "nude", "escort", "dating", "idol", "fan cam",
    "meme", "lol", "lmao", "hahaha", "suicidar", "kill", "sex", "gossip", "celebrity",
    "中奖", "抽奖", "福利视频", "裸照", "八卦", "追星", "饭圈", "搞笑", "段子", "娱乐圈",
)


def build_twitter_relevance_runtime() -> dict:
    """构建 Twitter 相关性过滤配置（配置文件 + 环境变量）。"""
    twitter_cfg = {}
    try:
        cfg = load_config()
        if isinstance(cfg, dict):
            twitter_cfg = cfg.get("twitter", {}) if isinstance(cfg.get("twitter"), dict) else {}
    except Exception:
        twitter_cfg = {}

    enabled_default = bool(twitter_cfg.get("relevance_filter_enabled", True))
    enabled = parse_bool(os.environ.get("TWITTER_RELEVANCE_FILTER_ENABLED"), enabled_default)

    min_score_default = int(twitter_cfg.get("relevance_min_score", 2) or 2)
    try:
        min_score = int(os.environ.get("TWITTER_RELEVANCE_MIN_SCORE", str(min_score_default)) or min_score_default)
    except ValueError:
        min_score = min_score_default

    floor_default = int(os.environ.get("TWITTER_RELEVANCE_FLOOR_COUNT", "20") or 20)
    floor_count = max(0, floor_default)

    cfg_positive = twitter_cfg.get("relevance_positive_keywords", [])
    cfg_negative = twitter_cfg.get("relevance_negative_keywords", [])
    if not isinstance(cfg_positive, list):
        cfg_positive = []
    if not isinstance(cfg_negative, list):
        cfg_negative = []

    env_positive = parse_keywords_arg(os.environ.get("TWITTER_RELEVANCE_POSITIVE_KEYWORDS", ""))
    env_negative = parse_keywords_arg(os.environ.get("TWITTER_RELEVANCE_NEGATIVE_KEYWORDS", ""))

    positive_keywords = [normalize_plain_text(x).lower() for x in (cfg_positive or []) if normalize_plain_text(x)]
    negative_keywords = [normalize_plain_text(x).lower() for x in (cfg_negative or []) if normalize_plain_text(x)]
    if not positive_keywords:
        positive_keywords = list(DEFAULT_TWITTER_RELEVANCE_POSITIVE_KEYWORDS)
    if not negative_keywords:
        negative_keywords = list(DEFAULT_TWITTER_RELEVANCE_NEGATIVE_KEYWORDS)
    if env_positive:
        positive_keywords = [normalize_plain_text(x).lower() for x in env_positive if normalize_plain_text(x)]
    if env_negative:
        negative_keywords = [normalize_plain_text(x).lower() for x in env_negative if normalize_plain_text(x)]

    return {
        "enabled": bool(enabled),
        "min_score": max(-20, min(50, int(min_score))),
        "floor_count": floor_count,
        "positive_keywords": list(dict.fromkeys([x for x in positive_keywords if x])),
        "negative_keywords": list(dict.fromkeys([x for x in negative_keywords if x])),
    }


def twitter_relevance_score(tweet: dict, runtime: dict) -> int:
    """计算推文相关性评分（财经/科技导向）。"""
    text = normalize_plain_text(tweet.get("text", "") or "")
    username = normalize_plain_text(tweet.get("username", "") or "")
    keyword = normalize_plain_text(tweet.get("keyword", "") or "")
    source = normalize_plain_text(tweet.get("source", "") or "")
    joined = f"{text} {username} {keyword} {source}".lower()

    positive_keywords = runtime.get("positive_keywords", []) if isinstance(runtime, dict) else []
    negative_keywords = runtime.get("negative_keywords", []) if isinstance(runtime, dict) else []
    min_score = int(runtime.get("min_score", 2) or 2) if isinstance(runtime, dict) else 2
    _ = min_score

    pos_hits = 0
    for kw in positive_keywords:
        if kw and kw in joined:
            pos_hits += 1

    neg_hits = 0
    for kw in negative_keywords:
        if kw and kw in joined:
            neg_hits += 1

    signal_bonus = 0
    if re.search(r"(\$[A-Za-z]{1,6}|\b\d+(\.\d+)?%|\b\d+bp\b)", joined):
        signal_bonus += 1
    if re.search(r"\b(qoq|yoy|guidance|earnings|etf|cpi|pmi|fomc|yield|inflation)\b", joined):
        signal_bonus += 1
    if tweet.get("is_trending"):
        signal_bonus += 1
    else:
        signal_bonus += 2
    if tweet_engagement(tweet) >= 500:
        signal_bonus += 1

    score = pos_hits * 2 + signal_bonus - neg_hits * 3
    return int(score)


def filter_social_twitter_for_report(social: dict) -> tuple[dict, dict]:
    """
    对社交数据中的 Twitter 推文做相关性过滤。
    返回: (filtered_social, stats)
    """
    filtered_social = deepcopy(social) if isinstance(social, dict) else {}
    twitter_data = get_social_section(filtered_social, "twitter")
    tweets = [t for t in twitter_data.get("tweets", []) if isinstance(t, dict)]
    runtime = build_twitter_relevance_runtime()

    stats = {
        "enabled": bool(runtime.get("enabled", True)),
        "before": len(tweets),
        "after": len(tweets),
        "removed": 0,
        "min_score": int(runtime.get("min_score", 2) or 2),
        "floor_count": int(runtime.get("floor_count", 0) or 0),
        "floor_applied": 0,
    }
    if not tweets or not runtime.get("enabled", True):
        return filtered_social, stats

    scored_rows = []
    for tweet in tweets:
        row = dict(tweet)
        score = twitter_relevance_score(row, runtime)
        row["_relevance_score"] = score
        scored_rows.append(row)

    scored_rows.sort(
        key=lambda x: (
            int(x.get("_relevance_score", 0) or 0),
            tweet_engagement(x),
            str(x.get("created_at", "")),
        ),
        reverse=True,
    )

    min_score = int(runtime.get("min_score", 2) or 2)
    selected = [row for row in scored_rows if int(row.get("_relevance_score", 0) or 0) >= min_score]

    floor_count = max(0, int(runtime.get("floor_count", 0) or 0))
    if floor_count > 0 and len(selected) < floor_count and scored_rows:
        selected_map = {twitter_item_dedup_key(x): x for x in selected}
        for row in scored_rows:
            key = twitter_item_dedup_key(row)
            if key in selected_map:
                continue
            selected.append(row)
            selected_map[key] = row
            if len(selected) >= floor_count:
                break
        stats["floor_applied"] = max(0, len(selected) - len([r for r in scored_rows if int(r.get("_relevance_score", 0) or 0) >= min_score]))

    selected.sort(
        key=lambda x: (
            int(x.get("_relevance_score", 0) or 0),
            tweet_engagement(x),
            str(x.get("created_at", "")),
        ),
        reverse=True,
    )

    twitter_data["tweets"] = selected
    twitter_data["relevance_filter_enabled"] = True
    twitter_data["relevance_min_score"] = min_score
    twitter_data["relevance_removed_count"] = max(0, len(tweets) - len(selected))
    twitter_data["follow_tweets_count"] = sum(1 for t in selected if not t.get("is_trending"))
    twitter_data["trending_tweets_count"] = sum(1 for t in selected if t.get("is_trending"))

    if isinstance(filtered_social.get("data"), dict):
        filtered_social["data"]["twitter"] = twitter_data
    else:
        filtered_social["twitter"] = twitter_data

    stats["after"] = len(selected)
    stats["removed"] = max(0, len(tweets) - len(selected))
    return filtered_social, stats


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
    unlimited = int(max_items or 0) <= 0

    lookback_hours = max(0, int(os.environ.get("TWITTER_REPORT_DEDUP_LOOKBACK_HOURS", "36") or 36))
    strict_mode = parse_bool(os.environ.get("TWITTER_REPORT_DEDUP_STRICT", "1"), True)
    recent_used_keys = _load_recent_report_used_twitter_keys(date_str, report_type, lookback_hours)
    if not recent_used_keys:
        return tweets_sorted[:] if unlimited else tweets_sorted[:max_items]

    selected: list[dict] = []
    skipped: list[dict] = []
    for tweet in tweets_sorted:
        dedup_key = twitter_item_dedup_key(tweet)
        if dedup_key in recent_used_keys:
            skipped.append(tweet)
            continue
        selected.append(tweet)
        if (not unlimited) and len(selected) >= max_items:
            break

    if (not strict_mode) and skipped:
        if unlimited:
            selected.extend(skipped)
        elif len(selected) < max_items:
            selected.extend(skipped[: max_items - len(selected)])

    logger.info(
        "🐦 Twitter 日报去重: 回看%s小时，已用key=%s，命中过滤=%s，最终=%s",
        lookback_hours,
        len(recent_used_keys),
        len(skipped),
        len(selected if unlimited else selected[:max_items]),
    )
    return selected if unlimited else selected[:max_items]


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
    if int(max_items or 0) <= 0:
        return articles_sorted
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
    try:
        max_items = int(os.environ.get("TWITTER_AI_ITEM_MAX", "0") or 0)
    except ValueError:
        max_items = 0
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
    try:
        max_items = int(os.environ.get("WECHAT_AI_ITEM_MAX", "0") or 0)
    except ValueError:
        max_items = 0
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
    call_id = flow_trace_next_call_id()
    call_started_at = now_beijing().isoformat()
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
    attempt_logs: list[dict] = []

    def _finalize(status: str, output_text: str) -> str:
        flow_trace_append_deepseek_call(
            {
                "call_id": call_id,
                "started_at": call_started_at,
                "finished_at": now_beijing().isoformat(),
                "status": status,
                "api_base": api_base,
                "model": model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "system_prompt_len": len(str(system_prompt or "")),
                "user_prompt_len": len(str(user_prompt or "")),
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "attempts": attempt_logs,
                "output": output_text,
            }
        )
        return output_text

    for attempt in range(1, retries + 1):
        resp = None
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=180)
            resp.raise_for_status()
            result = resp.json()
            content = result["choices"][0]["message"].get("content", "")
            usage = result.get("usage", {})
            attempt_info = {
                "attempt": attempt,
                "status": "ok",
                "http_status": resp.status_code if resp is not None else None,
                "usage": usage,
                "raw_output": content,
            }
            if not str(content or "").strip():
                logger.error("❌ DeepSeek 返回空内容")
                attempt_info["status"] = "empty_response"
                attempt_logs.append(attempt_info)
                if attempt < retries:
                    sleep_seconds = retry_sleep * attempt
                    logger.warning(f"⏳ DeepSeek 空响应重试 ({attempt}/{retries})，{sleep_seconds:.1f}s 后继续")
                    time.sleep(sleep_seconds)
                    continue
                return _finalize("failed", "AI 分析失败: empty response")
            logger.info(f"✅ 完成 (prompt_tokens={usage.get('prompt_tokens',0)}, completion_tokens={usage.get('completion_tokens',0)})")
            cleaned_content = sanitize_ai_response_text(content)
            attempt_info["cleaned_output"] = cleaned_content
            attempt_logs.append(attempt_info)
            if cleaned_content != content:
                logger.info("🧹 已清洗 AI 输出前缀")
            return _finalize("ok", cleaned_content)
        except requests.exceptions.HTTPError as e:
            status_code = resp.status_code if resp is not None else None
            logger.error(f"❌ DeepSeek API 错误: {e}")
            try:
                logger.error(f"   响应: {resp.text[:500]}")
            except Exception:
                pass
            attempt_logs.append(
                {
                    "attempt": attempt,
                    "status": "http_error",
                    "http_status": status_code,
                    "error": str(e),
                    "response_text": (resp.text[:2000] if resp is not None and resp.text else ""),
                }
            )
            can_retry = status_code in (429, 500, 502, 503, 504) and attempt < retries
            if can_retry:
                sleep_seconds = retry_sleep * attempt
                logger.warning(f"⏳ DeepSeek 将重试 ({attempt}/{retries})，{sleep_seconds:.1f}s 后继续")
                time.sleep(sleep_seconds)
                continue
            return _finalize("failed", f"AI 分析失败: {e}")
        except Exception as e:
            logger.error(f"❌ DeepSeek API 调用异常: {e}")
            attempt_logs.append(
                {
                    "attempt": attempt,
                    "status": "exception",
                    "error": str(e),
                }
            )
            if attempt < retries:
                sleep_seconds = retry_sleep * attempt
                logger.warning(f"⏳ DeepSeek 调用异常重试 ({attempt}/{retries})，{sleep_seconds:.1f}s 后继续")
                time.sleep(sleep_seconds)
                continue
            return _finalize("failed", f"AI 分析失败: {e}")
    return _finalize("failed", "AI 分析失败: exhausted retries")


def summarize_twitter_detailed(
    social: dict,
    date_context: str,
    api_key: str,
    api_base: str,
    model: str,
    grounding_rules: str,
    parallelism: int,
) -> str:
    """Twitter 单次详细汇总（分片并行 + 汇总合并）。"""
    try:
        max_parts = int(os.environ.get("TWITTER_AI_CHUNK_PARTS", "6") or 6)
    except ValueError:
        max_parts = 6
    max_parts = max(1, max_parts)

    chunks = build_twitter_chunks(social, min(parallelism, max_parts))
    if not chunks:
        return "暂无 Twitter 数据"

    chunk_summaries = parallel_chunk_analysis(
        section_name="Twitter-Summary",
        chunks=chunks,
        system_prompt=(
            "你是跨市场信号分析师。请只分析当前 Twitter 分片，输出 4-6 条中文要点。\n"
            "每条必须包含：发生了什么 + 为什么重要 + [来源ID: TWxx]。\n"
            "格式固定为无序列表，禁止编造输入外信息。\n\n"
            f"{grounding_rules}"
        ),
        user_prompt_builder=lambda chunk, idx, total: (
            f"以下是 {date_context} 的 Twitter 分片，请只总结当前分片：\n\n"
            f"{format_twitter_chunk_for_ai(chunk, idx, total)}"
        ),
        api_key=api_key,
        api_base=api_base,
        model=model,
        max_tokens=1100,
        temperature=0.35,
        fallback_system_prompt=(
            "你是跨市场信号分析师。请基于精简 Twitter 分片输出 3-4 条要点，"
            "每条末尾附 [来源ID: TWxx]。\n\n"
            f"{grounding_rules}"
        ),
        fallback_user_prompt_builder=lambda chunk, idx, total: (
            f"以下是 {date_context} 的 Twitter 精简分片，请只总结当前分片：\n\n"
            f"{format_twitter_chunk_for_ai_compact(chunk, idx, total)}"
        ),
    )
    valid_summaries = [s for s in chunk_summaries if not is_ai_failure(s)]

    if valid_summaries:
        merged_prompt = "以下是 Twitter 各分片摘要，请去重并合并为详细汇总：\n\n"
        for idx, text in enumerate(valid_summaries, start=1):
            merged_prompt += f"### 分片{idx}\n{text}\n\n"

        summary = call_deepseek(
            system_prompt=(
                "你是跨市场情报分析师。请输出“Twitter 详细汇总”，结构如下：\n"
                "1) 主线与情绪（3-4条）\n"
                "2) 金融市场线索（3-5条）\n"
                "3) 科技/AI/Web3 线索（3-5条）\n"
                "4) 噪音与误导风险（2-3条）\n"
                "每条都要附 [来源ID: TWxx]，不要输出额外客套话。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt=merged_prompt,
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=1800,
            temperature=0.35,
        )
        if not is_ai_failure(summary):
            return summary

    fallback_text = format_twitter_for_ai_compact(social)
    if fallback_text == "暂无 Twitter 数据":
        return fallback_text
    fallback_summary = call_deepseek(
        system_prompt=(
            "你是跨市场情报分析师。请把输入的 Twitter 样本整理为详细汇总，"
            "每条要点附 [来源ID: TWxx]。\n\n"
            f"{grounding_rules}"
        ),
        user_prompt=f"{date_context} Twitter 样本：\n\n{fallback_text}",
        api_key=api_key,
        api_base=api_base,
        model=model,
        max_tokens=1500,
        temperature=0.35,
    )
    if is_ai_failure(fallback_summary):
        return "暂无可用 Twitter 汇总"
    return fallback_summary


def summarize_wechat_detailed(
    social: dict,
    date_context: str,
    api_key: str,
    api_base: str,
    model: str,
    grounding_rules: str,
    parallelism: int,
) -> str:
    """微信公众号单次详细汇总（分片并行 + 汇总合并）。"""
    try:
        max_parts = int(os.environ.get("WECHAT_AI_CHUNK_PARTS", "6") or 6)
    except ValueError:
        max_parts = 6
    max_parts = max(1, max_parts)

    chunks = build_wechat_chunks(social, min(parallelism, max_parts))
    if not chunks:
        return "暂无微信公众号文章"

    chunk_summaries = parallel_chunk_analysis(
        section_name="WeChat-Summary",
        chunks=chunks,
        system_prompt=(
            "你是中文财经编辑。请只分析当前微信公众号分片，输出 4-6 条中文要点。\n"
            "每条必须包含：文章在讲什么 + 市场/产业信号 + [来源ID: WCxx]。\n"
            "格式固定为无序列表，禁止编造输入外信息。\n\n"
            f"{grounding_rules}"
        ),
        user_prompt_builder=lambda chunk, idx, total: (
            f"以下是 {date_context} 的微信公众号分片，请只总结当前分片：\n\n"
            f"{format_wechat_chunk_for_ai(chunk, idx, total)}"
        ),
        api_key=api_key,
        api_base=api_base,
        model=model,
        max_tokens=1200,
        temperature=0.35,
        fallback_system_prompt=(
            "你是中文财经编辑。请基于精简微信公众号分片输出 3-4 条要点，"
            "每条末尾附 [来源ID: WCxx]。\n\n"
            f"{grounding_rules}"
        ),
        fallback_user_prompt_builder=lambda chunk, idx, total: (
            f"以下是 {date_context} 的微信公众号精简分片，请只总结当前分片：\n\n"
            f"{format_wechat_chunk_for_ai_compact(chunk, idx, total)}"
        ),
    )
    valid_summaries = [s for s in chunk_summaries if not is_ai_failure(s)]

    if valid_summaries:
        merged_prompt = "以下是微信公众号各分片摘要，请去重并合并为详细汇总：\n\n"
        for idx, text in enumerate(valid_summaries, start=1):
            merged_prompt += f"### 分片{idx}\n{text}\n\n"

        summary = call_deepseek(
            system_prompt=(
                "你是中文财经总编。请输出“微信公众号详细汇总”，结构如下：\n"
                "1) 高频共识主线（3-4条）\n"
                "2) 市场/行业增量线索（4-6条）\n"
                "3) 可能的弱信号与待验证点（2-3条）\n"
                "每条都要附 [来源ID: WCxx]，不要输出额外客套话。\n\n"
                f"{grounding_rules}"
            ),
            user_prompt=merged_prompt,
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=1900,
            temperature=0.35,
        )
        if not is_ai_failure(summary):
            return summary

    fallback_text = format_wechat_for_ai_compact(social)
    if fallback_text == "暂无微信公众号文章":
        return fallback_text
    fallback_summary = call_deepseek(
        system_prompt=(
            "你是中文财经总编。请把输入的公众号样本整理为详细汇总，"
            "每条要点附 [来源ID: WCxx]。\n\n"
            f"{grounding_rules}"
        ),
        user_prompt=f"{date_context} 微信公众号样本：\n\n{fallback_text}",
        api_key=api_key,
        api_base=api_base,
        model=model,
        max_tokens=1600,
        temperature=0.35,
    )
    if is_ai_failure(fallback_summary):
        return "暂无可用微信公众号汇总"
    return fallback_summary


def run_ai_analysis(market: dict, social: dict, news: list,
                    api_key: str, api_base: str, model: str,
                    date_str: str, iso_date: str, report_label: str,
                    time_range: str, report_type: str,
                    web_context: dict | None = None,
                    previous_context: str = "") -> str:
    """
    分批调用 DeepSeek，每个数据源独立分析，最后综合汇总。

    步骤:
      1. 市场+板块数据 → 市场分析（早报/晚报均纳入 A 股）
      2. Twitter 详细汇总（分片并行 + 合并）
      3. 微信公众号详细汇总（分片并行 + 合并）
      4. 热榜全量 → 热榜分析
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
    a_share_rule = "早报与晚报都要纳入 A 股盘面（指数、板块、北向资金）及其他市场。"
    logger.info(f"⚙️ DeepSeek 并发上限: {parallelism} 路")

    filtered_market, market_filter_notes = market_snapshot_filter(market, date_str, report_type)
    market_filter_note_text = format_market_filter_notes(market_filter_notes)
    github_focus_text = format_github_focus_for_ai(filtered_market, previous_context=previous_context)
    filtered_market_data = filtered_market.get("data", {}) if isinstance(filtered_market, dict) else {}
    logger.info("🧪 市场时效过滤后可用模块: %s", ",".join((filtered_market_data or {}).keys()))
    has_non_crypto_market_data = any(
        key in filtered_market_data
        for key in ("stock_cn", "yahoo_stock", "futures", "precious_metal", "stock_overview")
    )
    has_crypto_market_data = bool(
        isinstance(filtered_market_data.get("crypto"), dict)
        and (filtered_market_data.get("crypto", {}) or {}).get("coins")
    )

    # ─── 第1步: 市场数据分析 ────────────────────────
    logger.info("🔍 [1/5] 分析市场数据（含 A 股）...")
    market_text = format_market_for_ai(filtered_market, include_a_share=True)
    if market_text != "暂无市场数据" and has_non_crypto_market_data:
        summary = call_deepseek(
            system_prompt=(
                "你是资深金融市场分析师。请对以下市场数据进行专业分析，包括：\n"
                "1. 主要市场走势判断\n"
                "2. 关键资产轮动分析：哪些方向在领涨/领跌，反映什么资金偏好\n"
                "3. 加密货币和商品期货的关键变化\n"
                "4. A 股指数、板块与北向资金传导关系\n"
                "5. 涨跌驱动链条：请明确“事件/政策/情绪 -> 资金行为 -> 价格表现”的因果路径，并标注证据强弱\n\n"
                "用中文，Markdown 格式，重要数据**加粗**，650-950字。\n\n"
                f"{grounding_rules}\n"
                f"5) {a_share_rule}"
            ),
            user_prompt=f"以下是 {date_context} 的金融市场数据：\n\n{market_text}",
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=2200,
        )
        section_summaries["market"] = summary
    else:
        logger.info("ℹ️ 严格时效窗口下非加密市场数据不足，跳过市场盘面分析。")
        section_summaries["market"] = (
            "当前窗口非加密市场快照未通过严格时效校验（仅允许过去12小时内数据），"
            "本期不输出市场盘面结论，转由资讯与社交叙事补充判断。"
        )

    # ─── 第2步: Twitter 详细汇总 ────────────────────────
    logger.info("🔍 [2/5] 生成 Twitter 详细汇总（分片并行）...")
    twitter_summary = summarize_twitter_detailed(
        social=social,
        date_context=date_context,
        api_key=api_key,
        api_base=api_base,
        model=model,
        grounding_rules=grounding_rules,
        parallelism=parallelism,
    )
    if twitter_summary != "暂无 Twitter 数据":
        section_summaries["twitter"] = twitter_summary

    # ─── 第3步: 微信公众号详细汇总 ────────────────────────
    logger.info("🔍 [3/5] 生成微信公众号详细汇总（分片并行）...")
    wechat_summary = summarize_wechat_detailed(
        social=social,
        date_context=date_context,
        api_key=api_key,
        api_base=api_base,
        model=model,
        grounding_rules=grounding_rules,
        parallelism=parallelism,
    )
    if wechat_summary != "暂无微信公众号文章":
        section_summaries["wechat"] = wechat_summary

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
                "4. 社会议题焦点\n\n"
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
            ),
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
                    "4. 社会议题焦点\n\n"
                    "中文 Markdown，300-500字。\n\n"
                    f"{grounding_rules}"
                ),
                user_prompt=merged_prompt,
                api_key=api_key,
                api_base=api_base,
                model=model,
                max_tokens=1500,
                temperature=0.4,
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

    # ─── 第5步: 综合汇总（分板块拼接，降低长上下文漂移） ───────────
    logger.info("🔍 [5/5] 生成综合分析报告（分板块拼接）...")

    is_weekend_flag, _ = is_weekend(date_str)
    weekend_note = "【注意：今日为周末，A股休市，部分市场数据可能缺失】" if is_weekend_flag else ""
    web_context_text = format_web_context_for_ai(web_context or {})
    citation_catalog_text = format_ai_citation_catalog_for_prompt(
        market=filtered_market,
        social=social,
        news=news,
        web_context=web_context,
    )

    if not section_summaries:
        logger.warning("⚠️ 各数据源均无可用原始数据，跳过综合 AI 生成。")
        return (
            "## 一、摘要\n"
            "- 社会：暂无可用数据。\n"
            "- 经济：暂无可用数据。\n"
            "- 市场：暂无可用数据。\n"
            "- 科技：暂无可用数据。\n\n"
            "## 📈 二、市场异动与定价逻辑 (Market Pricing)\n"
            "### 2.1 权益与宏观市场\n"
            "暂无可用市场数据，无法形成有效盘面结论。\n\n"
            "### 2.2 加密与预测市场 (Crypto & Prediction Markets)\n"
            "暂无可用加密与预测市场数据。\n\n"
            "## 🛰️ 三、产业前沿与跨域叙事 (Industry & Tech Alpha)\n"
            "### 3.1 叙事对撞：海外 Twitter vs 国内微信公号\n"
            "暂无可用社交媒体数据。\n\n"
            "### 3.2 极客雷达：GitHub 趋势与底层技术\n"
            "暂无可用 GitHub 趋势数据。\n\n"
            "## 四、政策动向与社会核心议题 (Policy & Social Sentiment)\n"
            "暂无可用热榜数据。\n\n"
            "## 📖 五、硬核研报与长文拆解 (Deep Paper Breakdown)\n"
            "### 5.1 推荐清单与重点拆解（10篇）\n"
            "暂无可用长文样本。\n\n"
            "## 🧭 六、增量认知与下期博弈锚点 (Next Watch)\n"
            "本期认知增量：数据源缺失，暂无法形成可靠增量结论。\n"
            "下期跟踪清单：\n"
            "1. 检查抓取任务是否按预期执行。\n"
            "2. 检查社交与热榜数据源可用性（Nitter / 微信 / NewsNow）。\n"
            "3. 补齐数据后重新生成报告。"
        )

    target_read_minutes = max(
        8,
        min(30, int(os.environ.get("REPORT_TARGET_READING_MINUTES", "15") or 15)),
    )
    long_form = target_read_minutes >= 15
    default_section_input_chars = "6200" if long_form else "4200"
    section_input_limit = max(
        1600,
        int(os.environ.get("REPORT_SECTION_INPUT_MAX_CHARS", default_section_input_chars) or default_section_input_chars),
    )

    def _section_input(section_name: str, blocks: list[tuple[str, str]]) -> str:
        lines = [
            f"报告上下文: {date_context}",
            f"当前板块: {section_name}",
            f"周末提示: {weekend_note or '无'}",
            f"市场时效过滤说明:\n{market_filter_note_text}",
            f"可引用来源ID索引:\n{citation_catalog_text}",
        ]
        if previous_context:
            lines.append(
                "上一轮建议跟踪事项:\n"
                + truncate_text_preserve_lines(previous_context, max_chars=1600)
            )
        for title, text in blocks:
            if not text:
                continue
            lines.append(
                f"## {title}\n"
                + truncate_text_preserve_lines(str(text), max_chars=section_input_limit)
            )
        return "\n\n".join(lines)

    def _strip_section_headings(text: str) -> str:
        cleaned = sanitize_ai_response_text(text)
        lines = cleaned.splitlines()
        # 仅剥离最前面的总标题，保留小标题用于可读性分段
        while lines and lines[0].strip().startswith("#"):
            lines.pop(0)
            while lines and not lines[0].strip():
                lines.pop(0)
        cleaned = "\n".join(lines)
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
        return cleaned

    def _polish_section_markdown(text: str) -> str:
        """提升可读性：修复强调样式并拆分过长段落。"""
        cleaned = str(text or "").replace("\r\n", "\n").strip()
        if not cleaned:
            return ""

        def _italic_to_bold(match: re.Match) -> str:
            inner = match.group(1)
            if not inner or inner != inner.strip():
                return match.group(0)
            token = inner.strip()
            if len(token) < 2:
                return match.group(0)
            return f"**{token}**"

        # 统一单星号强调为双星号，降低“看起来像漏写粗体”的情况
        cleaned = re.sub(r"(?<!\*)\*([^*\n]{2,80})\*(?!\*)", _italic_to_bold, cleaned)

        out_lines: list[str] = []
        for raw in cleaned.splitlines():
            line = raw.rstrip()
            stripped = line.strip()
            if not stripped:
                if out_lines and out_lines[-1] != "":
                    out_lines.append("")
                continue

            is_structured_line = bool(
                re.match(r"^(#{1,6}\s+|[-*]\s+|\d+[.)、]\s+|>\s+|\|)", stripped)
            ) or stripped.startswith("```")
            if is_structured_line:
                out_lines.append(stripped if stripped.startswith("|") else line.strip())
                continue

            plain = normalize_plain_text(stripped)
            if len(plain) < 180 or ("。" not in plain and "；" not in plain):
                out_lines.append(plain)
                continue

            segments = re.split(r"(?<=[。！？；])", plain)
            bucket: list[str] = []
            sentence_count = 0
            for seg in segments:
                piece = seg.strip()
                if not piece:
                    continue
                bucket.append(piece)
                sentence_count += 1
                if sentence_count >= 3:
                    out_lines.append("".join(bucket))
                    out_lines.append("")
                    bucket = []
                    sentence_count = 0
            if bucket:
                out_lines.append("".join(bucket))

        normalized: list[str] = []
        for line in out_lines:
            if line == "" and (not normalized or normalized[-1] == ""):
                continue
            normalized.append(line)
        return "\n".join(normalized).strip()

    def _call_section(
        section_name: str,
        system_prompt: str,
        blocks: list[tuple[str, str]],
        max_tokens: int | None = None,
        temperature: float = 0.4,
        fallback: str = "数据不足",
    ) -> str:
        if max_tokens is None:
            max_tokens = 1800 if long_form else 1400
        user_prompt = _section_input(section_name, blocks)
        output = call_deepseek(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            api_key=api_key,
            api_base=api_base,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        if is_ai_failure(output):
            logger.warning("⚠️ 板块生成失败: %s", section_name)
            return fallback
        body = _neutralize_north_flow_zero_inference(
            _polish_section_markdown(_strip_section_headings(output))
        )
        return body or fallback

    def _tok(long_value: int, short_value: int) -> int:
        return long_value if long_form else short_value

    def _normalize_summary_block(text: str) -> str:
        def _strip_summary_links(raw: str) -> str:
            val = str(raw or "")
            # 摘要不保留任何来源标注，便于快速阅读
            val = re.sub(r"\[来源ID:\s*[^\]]+\]", "", val, flags=re.IGNORECASE)
            val = re.sub(r"\[[^\]]+\]\(https?://[^)]+\)", "", val)
            val = re.sub(r"\s{2,}", " ", val)
            return normalize_plain_text(val)

        values = {"社会": "", "经济": "", "市场": "", "科技": ""}
        for raw in str(text or "").splitlines():
            line = normalize_plain_text(raw)
            if not line:
                continue
            m = re.match(r"^[-*]?\s*(社会|经济|市场|科技)\s*[：:]\s*(.+)$", line)
            if not m:
                continue
            key, value = m.group(1), _strip_summary_links(m.group(2))
            if value:
                values[key] = value
        defaults = {
            "社会": "暂无显著新增社会叙事，需继续观察舆情扩散链条。",
            "经济": "宏观增量信息不足，需结合下一窗口政策与数据确认方向。",
            "市场": "盘面新增信号有限，先以风险控制与增量验证为主。",
            "科技": "科技主线以延续为主，需跟踪是否出现真实落地催化。",
        }

        def _find_cn_index_change(index_name: str) -> float | None:
            data = filtered_market.get("data", {}) if isinstance(filtered_market, dict) else {}
            stock = data.get("stock_cn", {}) if isinstance(data, dict) else {}
            indices = stock.get("indices", []) if isinstance(stock, dict) else []
            for item in indices:
                if not isinstance(item, dict):
                    continue
                name = str(item.get("name", "") or "").strip()
                if index_name in name:
                    try:
                        return float(item.get("change_pct", 0) or 0)
                    except (TypeError, ValueError):
                        return None
            return None

        market_line = values["市场"] or defaults["市场"]
        market_appendix: list[str] = []
        sh_change = _find_cn_index_change("上证")
        if sh_change is not None and ("上证指数" not in market_line and "上证综指" not in market_line):
            market_appendix.append(f"上证指数{sh_change:+.2f}%")
        hs300_change = _find_cn_index_change("沪深300")
        if hs300_change is not None and "沪深300" not in market_line:
            market_appendix.append(f"沪深300{hs300_change:+.2f}%")
        if market_appendix:
            market_line = market_line.rstrip("。") + "；A股跟踪：" + "、".join(market_appendix) + "。"
        values["市场"] = market_line

        lines = []
        for key in ("社会", "经济", "市场", "科技"):
            lines.append(f"- {key}：{values[key] or defaults[key]}")
        return "\n".join(lines)

    def _normalize_next_watch_block(text: str) -> str:
        increment = ""
        items: list[str] = []
        for raw in str(text or "").splitlines():
            line = normalize_plain_text(raw)
            if not line:
                continue
            if not increment:
                m_inc = re.match(r"^本期认知增量\s*[：:]\s*(.+)$", line)
                if m_inc and normalize_plain_text(m_inc.group(1)):
                    increment = normalize_plain_text(m_inc.group(1))
                    continue
            m_item = re.match(r"^\d+[.)、]\s*(.+)$", line)
            if m_item:
                item = normalize_plain_text(m_item.group(1))
                if item and item not in items:
                    items.append(item)
                continue
            if line.startswith("下期跟踪清单"):
                continue
            if (not increment) and len(line) >= 10:
                increment = line

        if not increment:
            increment = "市场交易主线从事件脉冲转向“兑现强度验证”，需要用跨市场联动来确认趋势真伪。"
        defaults = [
            "延续跟进：盯住政策/监管变量是否从“表态”进入“落地执行”。",
            "收口复盘：复核高波动资产是否出现量价背离或趋势再确认。",
            "新增观察：跟踪 GitHub 高热项目在真实采用场景中的验证信号。",
        ]
        while len(items) < 3:
            items.append(defaults[len(items)])
        return "\n".join(
            [
                f"本期认知增量：{increment}",
                "下期跟踪清单：",
                *(f"{idx}. {item}" for idx, item in enumerate(items[:3], start=1)),
            ]
        )

    def _north_flow_zero_snapshot() -> bool:
        data = filtered_market.get("data", {}) if isinstance(filtered_market, dict) else {}
        stock = data.get("stock_cn", {}) if isinstance(data, dict) else {}
        north = stock.get("north_flow", {}) if isinstance(stock, dict) else {}
        return is_north_flow_zero_snapshot(north if isinstance(north, dict) else {})

    north_flow_zero_snapshot = _north_flow_zero_snapshot()

    def _neutralize_north_flow_zero_inference(text: str) -> str:
        if not north_flow_zero_snapshot:
            return text
        cleaned = str(text or "")
        rules = [
            (
                r"北向资金[^。\n；]{0,120}(?:\*{0,2}\+?0(?:\.0+)?亿元\*{0,2}|零流入)"
                r"[^。\n；]{0,120}(?:绝对观望|观望状态|观望态度|中性观望|中性态度|外资观望)[^。\n；]{0,40}",
                "北向资金净流入显示为+0.00亿元（全0快照），可能是源端未更新，暂不据此判断外资态度",
            ),
            (
                r"北向资金[^。\n；]{0,120}(?:绝对观望|观望状态|观望态度|中性观望|中性态度|外资观望)",
                "北向资金快照可能未更新，暂不据此判断外资态度",
            ),
        ]
        for pattern, repl in rules:
            cleaned = re.sub(pattern, repl, cleaned)
        return cleaned

    index_watch_text = format_market_indices_watch_for_ai(filtered_market)
    sector_structure_text = format_sector_structure_for_ai(filtered_market)

    summary_raw = _call_section(
        section_name="一、摘要",
        system_prompt=(
            "你是金融研究总编。请只输出4行要点，不要标题、不要解释：\n"
            "- 社会：...\n- 经济：...\n- 市场：...\n- 科技：...\n"
            "每行80-160字，必须体现“新增/延续/反转”之一；"
            "其中“市场”这一行必须同时覆盖：\n"
            "1) 至少2个关键指数（优先上证指数/沪深300/纳斯达克/标普/恒生）；\n"
            "2) 至少1个异动最明显指数（按绝对涨跌幅）；\n"
            "3) 若北向资金存在全0快照，要显式提示“可能未更新”。\n"
            "只有当该行有明确事实时才在句末标注 [来源ID: ...]，"
            "数据不足行禁止写 [来源ID: 未提供]。\n\n"
            f"目标阅读时长约 {target_read_minutes} 分钟，请给出有信息密度的提要。\n\n"
            f"{grounding_rules}"
        ),
        blocks=[
            ("市场关键指数与异动快照", index_watch_text),
            ("市场数据分析", section_summaries.get("market", "")),
            ("Twitter 详细汇总", section_summaries.get("twitter", "")),
            ("微信公众号详细汇总", section_summaries.get("wechat", "")),
            ("热榜新闻分析", section_summaries.get("news", "")),
            ("GitHub 项目雷达", section_summaries.get("github", "")),
            ("联网检索补充", web_context_text),
        ],
        max_tokens=_tok(1500, 1100),
        temperature=0.35,
        fallback=(
            "- 社会：社会层面暂无显著新增变量。\n"
            "- 经济：宏观经济增量信息有限，需等待下一窗口确认。\n"
            "- 市场：市场主线以存量博弈为主，关注风险偏好再定价。\n"
            "- 科技：科技与开源信号延续，关注落地节奏。"
        ),
    )
    summary_block = _normalize_summary_block(summary_raw)

    if has_non_crypto_market_data:
        section_21 = _call_section(
            section_name="2.1 全球大类资产与风险水位",
            system_prompt=(
                "你是全球宏观与资产配置分析师。仅输出该板块正文，不要标题。\n"
                "内容结构固定两段，并使用三级小标题分段：\n"
                "### 风险偏好图谱\n"
                "横向对比中美权益、港股、加密货币、贵金属与大宗商品的相对强弱，"
                "提炼资金在风险资产与避险资产间的迁移方向（Risk-On / Risk-Off）。\n"
                "### 宏观定价锚点\n"
                "从宏观热榜与社交信号中提取当前被定价权重最高的宏观因子，并解释其与资产轮动的对应关系。\n"
                "写作要求：每段2-4句，段间空行；尽量使用 **加粗**，不要使用单星号斜体。\n"
                "关键判断附 [来源ID: ...]。\n\n"
                f"目标阅读时长约 {target_read_minutes} 分钟，本板块写成中长文（约650-1000字）。\n\n"
                f"{grounding_rules}"
            ),
            blocks=[
                ("市场关键指数与异动快照", index_watch_text),
                ("市场数据分析", section_summaries.get("market", "")),
                ("Twitter 详细汇总", section_summaries.get("twitter", "")),
                ("热榜新闻分析", section_summaries.get("news", "")),
                ("联网检索补充", web_context_text),
            ],
            max_tokens=_tok(2400, 1400),
            temperature=0.35,
            fallback="全球大类资产仍呈结构分化，风险偏好方向待后续宏观变量验证。",
        )

        section_22 = _call_section(
            section_name="2.2 中美权益结构与主线验证",
            system_prompt=(
                "你是中美权益策略研究员。仅输出该板块正文，不要标题。\n"
                "内容结构固定两段，并使用三级小标题分段：\n"
                "### A/H股盘面与逻辑映射\n"
                "提炼A/H股最强与最弱板块（若缺板块数据须明确“板块数据不足/未提供”），"
                "并强制关联国内财经热榜或微信投研共识进行验证。\n"
                "### 美股科技与海外映射\n"
                "提炼美股核心指数与科技主线波动特征，结合海外社交/外媒叙事提取驱动逻辑。\n"
                "必须覆盖A股结构与跨市场映射；对北向资金“全0”快照禁止直接当作方向结论。\n"
                "写作要求：每段2-4句，段间空行；关键判断附 [来源ID: ...]。\n\n"
                f"目标阅读时长约 {target_read_minutes} 分钟，本板块写成中长文（约650-1000字）。\n\n"
                f"{grounding_rules}\n"
                f"{a_share_rule}"
            ),
            blocks=[
                ("市场关键指数与异动快照", index_watch_text),
                ("A股板块结构快照", sector_structure_text),
                ("市场数据分析", section_summaries.get("market", "")),
                ("微信公众号详细汇总", section_summaries.get("wechat", "")),
                ("Twitter 详细汇总", section_summaries.get("twitter", "")),
                ("热榜新闻分析", section_summaries.get("news", "")),
                ("联网检索补充", web_context_text),
            ],
            max_tokens=_tok(2500, 1450),
            temperature=0.35,
            fallback="中美权益主线仍以结构分化为主，关键叙事的价格验证强度偏弱。",
        )
    else:
        section_21 = "当前窗口非加密市场数据不足（严格12小时时效校验未通过），本期不输出大类资产盘面结论。"
        section_22 = "当前窗口非加密市场数据不足（严格12小时时效校验未通过），本期不输出中美权益结构结论。"

    if has_crypto_market_data:
        section_23 = _call_section(
            section_name="2.3 另类资产与博弈前沿",
            system_prompt=(
                "你是加密与另类资产研究员。仅输出该板块正文，不要标题。\n"
                "内容结构固定两段，并使用三级小标题分段：\n"
                "### 主流加密与链上叙事\n"
                "提炼BTC/ETH及异动币种的涨跌态势，并给出社交文本中最强解释链条。\n"
                "### 焦点事件与预测博弈\n"
                "提炼讨论热度最高且分歧最大的待落地事件，说明多空双方押注逻辑与潜在影响。\n"
                "若样本不足必须明确“数据不足/未提供”。关键判断附 [来源ID: ...]。\n\n"
                f"目标阅读时长约 {target_read_minutes} 分钟，本板块写成中长文（约500-900字）。\n\n"
                f"{grounding_rules}"
            ),
            blocks=[
                ("市场数据分析", section_summaries.get("market", "")),
                ("Twitter 详细汇总", section_summaries.get("twitter", "")),
                ("热榜新闻分析", section_summaries.get("news", "")),
                ("微信公众号详细汇总", section_summaries.get("wechat", "")),
                ("联网检索补充", web_context_text),
            ],
            max_tokens=_tok(2200, 1300),
            temperature=0.35,
            fallback="加密与另类资产仍处于事件驱动博弈阶段，待新增链上与资金面数据确认。",
        )
    else:
        section_23 = "当前窗口加密市场数据不足（时间异常或数值校验未通过），本期不输出加密盘面结论。"

    section_31 = _call_section(
        section_name="3.1 叙事对撞：海外 Twitter vs 国内微信公号",
        system_prompt=(
            "你是产业研究负责人。仅输出该板块正文，不要标题。\n"
            "必须先写“海外焦点叙事（Bull/Bear）”，再写“国内投研共识”，最后写“预期差评估”。\n"
            "重点比较同一主题在海外与国内信息源的分歧与共识，结论尽量附 [来源ID: ...]。\n\n"
            f"目标阅读时长约 {target_read_minutes} 分钟，本板块写成中长文（约650-1100字）。\n\n"
            f"{grounding_rules}"
        ),
        blocks=[
            ("Twitter 详细汇总", section_summaries.get("twitter", "")),
            ("微信公众号详细汇总", section_summaries.get("wechat", "")),
            ("联网检索补充", web_context_text),
        ],
        max_tokens=_tok(2400, 1300),
        temperature=0.35,
        fallback="海外与国内叙事暂无明确反转，当前更像“共识延续 + 局部分歧”，需后续催化验证。",
    )

    section_32 = _call_section(
        section_name="3.2 极客雷达：GitHub 趋势与底层技术",
        system_prompt=(
            "你是技术趋势研究员。仅输出该板块正文，不要标题。\n"
            "围绕 GitHub trending 做项目雷达：\n"
            "1) 挑出最值得关注的项目并说明“为何值得看”；\n"
            "2) 解释底层技术痛点与可能落地路径；\n"
            "3) 提醒重复叙事/泡沫噪音；\n"
            "4) 避免每次都写成同一批项目，优先强调本期增量。\n"
            "关键判断尽量附 [来源ID: ...]。\n\n"
            f"目标阅读时长约 {target_read_minutes} 分钟，本板块写成中长文（约600-1000字）。\n\n"
            f"{grounding_rules}"
        ),
        blocks=[
            ("GitHub 项目雷达", section_summaries.get("github", "")),
            ("Twitter 详细汇总", section_summaries.get("twitter", "")),
            ("微信公众号详细汇总", section_summaries.get("wechat", "")),
            ("联网检索补充", web_context_text),
        ],
        max_tokens=_tok(2200, 1300),
        temperature=0.35,
        fallback="GitHub 热门项目以延续性主题为主，短期内需观察是否出现真实采用与二次扩散。",
    )

    section_4 = _call_section(
        section_name="四、政策动向与社会核心议题",
        system_prompt=(
            "你是政策与社会舆情研究员。仅输出该板块正文，不要标题。\n"
            "内容必须拆成两段：\n"
            "1) 政策灰线与产业映射（监管/补贴/贸易规则及产业传导）；\n"
            "2) 值得关注的社会议题（跨平台共鸣议题及其经济含义）。\n"
            "需要明确“事件 -> 产业/预期 -> 价格/行为”链条，尽量附 [来源ID: ...]。\n\n"
            f"目标阅读时长约 {target_read_minutes} 分钟，本板块写成中长文（约600-1000字）。\n\n"
            f"{grounding_rules}"
        ),
        blocks=[
            ("热榜新闻分析", section_summaries.get("news", "")),
            ("微信公众号详细汇总", section_summaries.get("wechat", "")),
            ("联网检索补充", web_context_text),
        ],
        max_tokens=_tok(2200, 1300),
        temperature=0.35,
        fallback="政策与社会议题暂无确定性反转，建议继续跟踪“监管落地节奏 + 社会情绪扩散链条”。",
    )

    section_51 = _call_section(
        section_name="5.1 硬核研报与长文拆解",
        system_prompt=(
            "你是投研方法论编辑。仅输出该板块正文，不要标题。\n"
            "输出结构固定为两部分，并使用对应小标题：\n"
            "### 推荐阅读清单（10篇）\n"
            "必须列出10篇，格式为“1. [标题](链接) | 来源 | 主题标签 | 推荐理由（1句）”。\n"
            "主题覆盖要求：\n"
            "- 投资/宏观/产业研究 >= 4篇\n"
            "- 科技/AI/开源技术 >= 3篇\n"
            "- 社会高关注议题、公共政策或深度调查 >= 3篇\n"
            "### 重点拆解（2-3篇）\n"
            "每篇按“研究假设与立论点 / 数据基础与方法论 / 推演结论与实操启示”三段展开。\n"
            "不要复述口号，结论尽量附 [来源ID: ...]。\n"
            "写作要求：段间空行，优先 **加粗**，不要使用单星号斜体。\n\n"
            f"目标阅读时长约 {target_read_minutes} 分钟，本板块写成中长文（约500-900字）。\n\n"
            f"{grounding_rules}"
        ),
        blocks=[
            ("微信公众号详细汇总", section_summaries.get("wechat", "")),
            ("Twitter 详细汇总", section_summaries.get("twitter", "")),
            ("热榜新闻分析", section_summaries.get("news", "")),
            ("联网检索补充", web_context_text),
        ],
        max_tokens=_tok(3000, 1700),
        temperature=0.35,
        fallback=(
            "### 推荐阅读清单（10篇）\n"
            "1. 暂无足够长文样本（数据不足/未提供）\n"
            "2. 暂无足够长文样本（数据不足/未提供）\n"
            "3. 暂无足够长文样本（数据不足/未提供）\n"
            "4. 暂无足够长文样本（数据不足/未提供）\n"
            "5. 暂无足够长文样本（数据不足/未提供）\n"
            "6. 暂无足够长文样本（数据不足/未提供）\n"
            "7. 暂无足够长文样本（数据不足/未提供）\n"
            "8. 暂无足够长文样本（数据不足/未提供）\n"
            "9. 暂无足够长文样本（数据不足/未提供）\n"
            "10. 暂无足够长文样本（数据不足/未提供）\n\n"
            "### 重点拆解（2-3篇）\n"
            "当前窗口长文样本不足，建议下期补充高质量研报与社会调查后再进行深拆。"
        ),
    )

    next_watch_raw = _call_section(
        section_name="六、增量认知与下期博弈锚点",
        system_prompt=(
            "你是策略研究总编。仅输出该板块正文，不要标题，格式必须严格为：\n"
            "本期认知增量：...\n"
            "下期跟踪清单：\n"
            "1. ...\n2. ...\n3. ...\n"
            "要求：\n"
            "- “本期认知增量”必须是一句话总结本期底层逻辑变化；\n"
            "- 跟踪清单的前两条尽量承接最近三天六期的历史跟踪（延续或收口），第三条写本期新增变量；\n"
            "- 每条25-70字，可附 [来源ID: ...]。\n\n"
            f"目标阅读时长约 {target_read_minutes} 分钟。\n\n"
            f"{grounding_rules}"
        ),
        blocks=[
            ("最近三天六期摘要与跟踪", previous_context),
            ("2.1 全球大类资产与风险水位", section_21),
            ("2.2 中美权益结构与主线验证", section_22),
            ("2.3 另类资产与博弈前沿", section_23),
            ("3.1 叙事对撞", section_31),
            ("3.2 极客雷达", section_32),
            ("四、政策动向与社会核心议题", section_4),
            ("5.1 硬核研报与长文拆解", section_51),
        ],
        max_tokens=_tok(1600, 900),
        temperature=0.35,
        fallback=(
            "本期认知增量：市场主线从“事件驱动冲击”转向“兑现强度验证”，需看跨市场联动是否确认。\n"
            "下期跟踪清单：\n"
            "1. 延续跟进：核查政策变量在下一窗口是否出现落地验证。\n"
            "2. 收口复盘：复核高波动资产是否出现趋势确认或反转。\n"
            "3. 新增观察：跟踪科技主线从讨论热度到实际采用的转化。"
        ),
    )
    next_watch_block = _normalize_next_watch_block(next_watch_raw)

    final_summary = "\n".join(
        [
            "## 一、摘要",
            summary_block,
            "",
            "## 📈 二、市场异动与定价逻辑 (Market Pricing)",
            "### 2.1 全球大类资产与风险水位 (Global Risk Sentiment)",
            section_21,
            "",
            "### 2.2 中美权益结构与主线验证 (Equity Narratives Validation)",
            section_22,
            "",
            "### 2.3 另类资产与博弈前沿 (Crypto & Alternative Bets)",
            section_23,
            "",
            "## 🛰️ 三、产业前沿与跨域叙事 (Industry & Tech Alpha)",
            "### 3.1 叙事对撞：海外 Twitter vs 国内微信公号",
            section_31,
            "",
            "### 3.2 极客雷达：GitHub 趋势与底层技术",
            section_32,
            "",
            "## 四、政策动向与社会核心议题 (Policy & Social Sentiment)",
            section_4,
            "",
            "## 📖 五、硬核研报与长文拆解 (Deep Paper Breakdown)",
            "### 5.1 推荐清单与重点拆解（10篇）",
            section_51,
            "",
            "## 🧭 六、增量认知与下期博弈锚点 (Next Watch)",
            next_watch_block,
        ]
    )

    result_parts = [final_summary]
    result_parts.append("\n\n---\n")
    result_parts.append("<details><summary>📑 点击展开各板块详细分析</summary>\n")

    if "market" in section_summaries:
        result_parts.append(f"### 📊 市场数据详细分析\n\n{section_summaries['market']}\n")
    result_parts.append(f"### ⏱ 市场时效过滤说明\n\n{market_filter_note_text}\n")
    if "twitter" in section_summaries:
        result_parts.append(f"### 🐦 Twitter 详细汇总\n\n{section_summaries['twitter']}\n")
    if "wechat" in section_summaries:
        result_parts.append(f"### 📱 微信公众号详细汇总\n\n{section_summaries['wechat']}\n")
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
        for key in ("net_flow", "hu_net_flow", "shen_net_flow"):
            value = safe_float(north.get(key), 0.0)
            icon = "🟢" if value >= 0 else "🔴"
            lines.append(f"| {key} | {icon} {value:.2f} |")
        if is_north_flow_zero_snapshot(north):
            lines.append("")
            lines.append("> 注：北向资金当期快照为全0，可能是源端未更新，不宜过度解读。")
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
    metals_rows = get_precious_metal_rows(pm if isinstance(pm, dict) else {})
    if metals_rows:
        lines.append("### 🥇 贵金属\n")
        lines.append("| 品种 | 价格 | 涨跌幅 |")
        lines.append("|------|------|--------|")
        for metal in metals_rows:
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
    parser.add_argument("--trace-flow", action="store_true",
                        help="记录 sys/user prompt、模型输出和 raw_material 全链路")
    parser.add_argument("--trace-output", default=None,
                        help="链路追踪输出文件路径 (默认 output/debug/flow_*.json)")
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

    trace_enabled = bool(args.trace_flow)
    env_trace_flag = os.environ.get("REPORT_TRACE_FLOW")
    if env_trace_flag is not None:
        trace_enabled = parse_bool(env_trace_flag, trace_enabled)
    trace_output_arg = args.trace_output or os.environ.get("REPORT_TRACE_OUTPUT", "")
    trace_output_path = Path(trace_output_arg).expanduser().resolve() if trace_output_arg else None
    init_flow_trace(
        enabled=trace_enabled,
        date_str=date_str,
        report_type=report_type,
        args_payload={
            "date": date_str,
            "type": report_type,
            "no_ai": bool(args.no_ai),
            "keywords": args.keywords,
            "no_web_context": bool(args.no_web_context),
            "output": args.output or "",
            "trace_output": str(trace_output_path) if trace_output_path else "",
            "model": model,
            "api_base": api_base,
        },
    )
    flow_trace_event(
        "report_parameters_resolved",
        {
            "iso_date": iso_date,
            "report_label": report_label,
            "time_range": time_range,
            "trace_enabled": trace_enabled,
        },
    )
    
    logger.info(f"📅 生成 {iso_date} {report_label}")
    logger.info(f"🤖 DeepSeek 配置: model={model}, base={api_base}")
    
    # ── 读取数据 ──────────────────────────────────
    logger.info("📥 读取市场数据...")
    market = load_market_data(date_str, report_type=report_type)
    
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
    flow_trace_set_raw_material(
        "loaded_sources",
        {
            "market": market,
            "social": social,
            "news": news,
        },
    )
    flow_trace_event(
        "base_data_loaded",
        {
            "market_loaded": bool(market),
            "social_loaded": bool(social),
            "news_count": len(news) if isinstance(news, list) else 0,
        },
    )

    # ── 联网检索补充 ─────────────────────
    config_keywords = web_cfg.get("keywords", []) if isinstance(web_cfg, dict) else []
    if not isinstance(config_keywords, list):
        config_keywords = []
    raw_keywords = (
        args.keywords
        or os.environ.get("REPORT_WEB_KEYWORDS", "")
        or ",".join(config_keywords)
    )
    custom_keywords = parse_keywords_arg(raw_keywords)

    force_web_context = parse_bool(os.environ.get("REPORT_FORCE_WEB_CONTEXT", "1"), True)
    web_context_enabled = not args.no_web_context
    if not force_web_context:
        if "enabled" in web_cfg:
            web_context_enabled = bool(web_cfg.get("enabled")) and web_context_enabled
    elif isinstance(web_cfg, dict) and (web_cfg.get("enabled") is False) and web_context_enabled:
        logger.info("🌐 已忽略 report.web_context.enabled=false，按 REPORT_FORCE_WEB_CONTEXT=1 强制联网检索")
    env_web_flag = os.environ.get("WEB_CONTEXT_ENABLED")
    if env_web_flag is not None:
        web_context_enabled = parse_bool(env_web_flag, web_context_enabled)

    web_context = {"queries": [], "items": [], "errors": [], "raw_material_downloads": []}
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
    flow_trace_set_raw_material(
        "web_raw_material_downloads",
        web_context.get("raw_material_downloads", []),
    )
    flow_trace_set_raw_material(
        "web_context_filtered",
        {
            "queries": web_context.get("queries", []),
            "items": web_context.get("items", []),
            "errors": web_context.get("errors", []),
        },
    )
    flow_trace_event(
        "web_context_ready",
        {
            "enabled": web_context_enabled,
            "query_count": len(web_context.get("queries", []) or []),
            "item_count": len(web_context.get("items", []) or []),
            "error_count": len(web_context.get("errors", []) or []),
        },
    )

    # ── 12H 增量去重（跨次）─────────────────────
    market, social, news, web_context, dedup_stats, dedup_records = apply_cross_source_incremental_dedup(
        market=market,
        social=social,
        news=news,
        web_context=web_context,
        date_str=date_str,
        report_type=report_type,
    )
    logger.info(
        "🧹 增量去重完成: Twitter -%s | 微信 -%s | 热榜 -%s | GitHub -%s（保底+%s） | 联网 -%s",
        dedup_stats.get("twitter_removed", 0),
        dedup_stats.get("wechat_removed", 0),
        dedup_stats.get("news_removed", 0),
        dedup_stats.get("github_removed", 0),
        dedup_stats.get("github_floor_added", 0),
        dedup_stats.get("web_removed", 0),
    )
    flow_trace_set_output("dedup_stats", dedup_stats)
    flow_trace_event("dedup_completed", dedup_stats)

    # ── Twitter 相关性过滤已关闭：直接使用抓取阶段（12h窗口）结果────────────
    social_for_summary = social
    logger.info("🎯 Twitter 相关性过滤: 已禁用（使用抓取阶段时间窗口过滤结果）")

    # ── 上下文增强（最近三天六期：摘要+跟踪 + 上轮跟踪事项）────────────────────
    previous_report_context = load_previous_report_context(
        date_str,
        report_type,
        max_chars=max(2400, int(os.environ.get("REPORT_PREVIOUS_CONTEXT_MAX_CHARS", "5600") or 5600)),
    )
    previous_track_context = load_previous_next_track_context(
        date_str,
        report_type,
        max_chars=max(1200, int(os.environ.get("REPORT_PREVIOUS_TRACK_MAX_CHARS", "2200") or 2200)),
    )
    previous_context = "\n\n".join(
        [chunk for chunk in (previous_report_context, previous_track_context) if str(chunk or "").strip()]
    ).strip()
    if previous_context:
        logger.info("🧩 已加载历史上下文（最近三天六期摘要/跟踪 + 上轮跟踪事项）")
    else:
        logger.info("🧩 未找到可用历史上下文")
    flow_trace_set_raw_material("previous_context", previous_context)
    flow_trace_event(
        "previous_context_ready",
        {
            "has_previous_context": bool(previous_context),
            "length": len(previous_context),
        },
    )

    # ── AI 分析 ──────────────────────────────────
    ai_summary = ""
    if not args.no_ai:
        if not api_key:
            logger.warning("⚠️ 未配置 DeepSeek API Key，跳过 AI 分析")
            ai_summary = "> ⚠️ AI 分析未启用（未配置 API Key）\n"
        else:
            ai_summary = run_ai_analysis(
                market=market,
                social=social_for_summary,
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
    ai_summary = sanitize_source_id_tags(ai_summary)
    ai_summary = normalize_inline_source_id_links(ai_summary)
    ai_summary, _, ai_ref_records = convert_ai_source_tags_to_clickable_refs(
        ai_summary,
        market=market,
        social=social_for_summary,
        news=news,
        web_context=web_context,
    )
    ai_summary = canonicalize_source_id_markdown_links(ai_summary, ai_ref_records)
    flow_trace_set_output("ai_summary", ai_summary)
    flow_trace_set_output("ai_ref_records", ai_ref_records)
    flow_trace_event(
        "ai_summary_ready",
        {
            "ai_enabled": bool(not args.no_ai and api_key),
            "ai_summary_length": len(ai_summary),
            "deepseek_calls": len(FLOW_TRACE_STATE.get("deepseek_calls", []) or []),
        },
    )
    
    # ── 生成完整 Markdown ──────────────────────
    report_parts = []
    generated_at_bj = now_beijing()
    next_track_items = parse_next_track_items(ai_summary, max_items=5)

    # 顶部仅保留详细 AI 分析（不再插入前置简报）
    report_parts.append("# 🤖 详细 AI 分析\n")
    report_parts.append(ai_summary)
    if spec_enabled:
        report_parts.append(
            generate_speculation_brief_section(
                market,
                report_type=report_type,
                max_points=spec_max_points,
            )
        )
    report_parts.append(generate_web_context_section(web_context))

    health_alert_section = generate_source_health_alert_section(
        social=social,
        report_type=report_type,
        date_str=date_str,
    )
    if health_alert_section:
        report_parts.append(health_alert_section)

    report_parts.append("\n---\n")

    # 原始数据
    report_parts.append("# 📋 原始数据\n")
    report_parts.append("<a id=\"raw-market-data\"></a>")
    report_parts.append(generate_raw_market_section(market))
    report_parts.append(generate_raw_twitter_section(social))
    report_parts.append(generate_raw_wechat_section(social))
    report_parts.append(generate_raw_news_section(news))

    # 页脚
    report_parts.append("---\n")
    report_parts.append(f"*报告由 finradar 自动生成 | {generated_at_bj.strftime('%Y-%m-%d %H:%M:%S')}（北京时间）*\n")
    
    full_report = "\n".join(report_parts)
    flow_trace_set_output("final_report_markdown", full_report)
    
    # ── 保存 ──────────────────────────────────
    OUTPUT_REPORT.mkdir(parents=True, exist_ok=True)
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = OUTPUT_REPORT / f"daily_{date_str}_{report_type}.md"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_report)
    flow_trace_set_output("report_path", str(output_path))
    flow_trace_set_output("report_size_bytes", output_path.stat().st_size)

    # 记录本次已使用条目（跨次去重）与下一轮跟踪事项
    try:
        persist_report_used_records(
            records=dedup_records,
            date_str=date_str,
            report_type=report_type,
            anchor=report_anchor_datetime(date_str, report_type),
        )
    except Exception as e:
        logger.warning("⚠️ 写入跨次去重记录失败: %s", e)

    try:
        save_next_track_state(date_str=date_str, report_type=report_type, items=next_track_items)
    except Exception as e:
        logger.warning("⚠️ 写入下一轮跟踪状态失败: %s", e)
    
    logger.info(f"✅ 报告已保存: {output_path}")
    logger.info(f"   文件大小: {output_path.stat().st_size / 1024:.1f} KB")

    try:
        saved_trace_path = dump_flow_trace(trace_output_path)
        if saved_trace_path is not None:
            logger.info("🧪 链路追踪已保存: %s", saved_trace_path)
    except Exception as e:
        logger.warning("⚠️ 写入链路追踪失败: %s", e)
    
    return str(output_path)


if __name__ == "__main__":
    main()
