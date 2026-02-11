"""
Yahoo Finance 全球股票总览抓取器

基于 yfinance 获取主要指数/ETF 的日线快照，用于补充全球市场 overview。
"""

import asyncio
from datetime import datetime
import logging
import math
from typing import Any, Dict, List, Optional
from urllib.parse import quote

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False
    yf = None

from . import BaseFetcher

logger = logging.getLogger(__name__)


def _safe_float(value: Any) -> float | None:
    """安全转 float，过滤 NaN/Inf。"""
    try:
        num = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(num) or math.isinf(num):
        return None
    return num


def _safe_int(value: Any) -> int:
    """安全转 int。"""
    num = _safe_float(value)
    if num is None:
        return 0
    return int(num)


class YahooStockFetcher(BaseFetcher):
    """Yahoo Finance 全球股票概览抓取器。"""

    DEFAULT_WATCHLIST = [
        {"symbol": "^GSPC", "name": "标普500", "region": "美股", "market": "index", "currency": "USD"},
        {"symbol": "^IXIC", "name": "纳斯达克综合", "region": "美股", "market": "index", "currency": "USD"},
        {"symbol": "^DJI", "name": "道琼斯工业指数", "region": "美股", "market": "index", "currency": "USD"},
        {"symbol": "^RUT", "name": "罗素2000", "region": "美股", "market": "index", "currency": "USD"},
        {"symbol": "^VIX", "name": "VIX波动率指数", "region": "美股", "market": "index", "currency": "USD"},
        {"symbol": "^HSI", "name": "恒生指数", "region": "港股", "market": "index", "currency": "HKD"},
        {"symbol": "^N225", "name": "日经225", "region": "日股", "market": "index", "currency": "JPY"},
        {"symbol": "^KS11", "name": "韩国综合指数", "region": "韩股", "market": "index", "currency": "KRW"},
        {"symbol": "^FTSE", "name": "英国富时100", "region": "欧股", "market": "index", "currency": "GBP"},
        {"symbol": "^GDAXI", "name": "德国DAX", "region": "欧股", "market": "index", "currency": "EUR"},
        {"symbol": "^FCHI", "name": "法国CAC40", "region": "欧股", "market": "index", "currency": "EUR"},
        {"symbol": "000001.SS", "name": "上证综指", "region": "A股", "market": "index", "currency": "CNY"},
    ]

    def __init__(self, config: Optional[Dict] = None):
        super().__init__(config)

        if not YFINANCE_AVAILABLE:
            logger.warning("yfinance not installed. Run: pip install yfinance")
            self.enabled = False

        self.watchlist = self._normalize_watchlist(self.config.get("watchlist"))
        self.history_period = str(self.config.get("history_period", "5d"))
        self.request_timeout = float(self.config.get("request_timeout", 12))

    def _normalize_watchlist(self, raw_watchlist: Any) -> List[Dict[str, Any]]:
        """规范化 watchlist，支持 list[str] / list[dict]。"""
        if not isinstance(raw_watchlist, list) or not raw_watchlist:
            return list(self.DEFAULT_WATCHLIST)

        results: List[Dict[str, Any]] = []
        for item in raw_watchlist:
            if isinstance(item, str):
                symbol = item.strip()
                if not symbol:
                    continue
                results.append(
                    {
                        "symbol": symbol,
                        "name": symbol,
                        "region": "全球",
                        "market": "index",
                        "currency": "USD",
                    }
                )
                continue

            if not isinstance(item, dict):
                continue

            symbol = str(item.get("symbol", "")).strip()
            if not symbol:
                continue

            results.append(
                {
                    "symbol": symbol,
                    "name": str(item.get("name", symbol)).strip() or symbol,
                    "region": str(item.get("region", "全球")).strip() or "全球",
                    "market": str(item.get("market", "index")).strip() or "index",
                    "currency": str(item.get("currency", "USD")).strip() or "USD",
                }
            )

        return results or list(self.DEFAULT_WATCHLIST)

    async def fetch(self) -> Dict[str, Any]:
        """抓取 Yahoo Finance 股票概览。"""
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(None, self._fetch_single_symbol, item)
            for item in self.watchlist
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        markets: List[Dict[str, Any]] = []
        for item, result in zip(self.watchlist, results):
            if isinstance(result, Exception):
                logger.error("Error fetching Yahoo symbol %s: %s", item.get("symbol"), result)
                continue
            if isinstance(result, dict) and result:
                markets.append(result)

        return {
            "markets": markets,
            "overview": self._build_overview(markets),
            "timestamp": datetime.now().isoformat(),
            "source": "yahoo_finance",
        }

    def _fetch_single_symbol(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """抓取单个代码行情。"""
        symbol = str(item.get("symbol", "")).strip()
        if not symbol:
            return {}

        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=self.history_period, timeout=self.request_timeout)
            if hist is None or hist.empty:
                return {}

            latest = hist.iloc[-1]
            prev = hist.iloc[-2] if len(hist) > 1 else latest

            price = _safe_float(latest.get("Close"))
            prev_close = _safe_float(prev.get("Close"))
            if price is None or prev_close is None:
                return {}

            change = price - prev_close
            change_pct = (change / prev_close * 100) if prev_close else 0.0

            open_price = _safe_float(latest.get("Open"))
            high_price = _safe_float(latest.get("High"))
            low_price = _safe_float(latest.get("Low"))
            volume = _safe_int(latest.get("Volume"))

            return {
                "symbol": symbol,
                "name": item.get("name", symbol),
                "region": item.get("region", "全球"),
                "market": item.get("market", "index"),
                "currency": item.get("currency", "USD"),
                "price": round(price, 2),
                "change": round(change, 2),
                "change_pct": round(change_pct, 2),
                "prev_close": round(prev_close, 2),
                "open": round(open_price, 2) if open_price is not None else None,
                "high": round(high_price, 2) if high_price is not None else None,
                "low": round(low_price, 2) if low_price is not None else None,
                "volume": volume,
                "url": f"https://finance.yahoo.com/quote/{quote(symbol, safe='')}",
            }
        except Exception as e:
            logger.error("Error fetching Yahoo symbol %s: %s", symbol, e)
            return {}

    def _build_overview(self, markets: List[Dict[str, Any]]) -> Dict[str, Any]:
        """构建轻量总览统计。"""
        up = 0
        down = 0
        flat = 0
        region_stats: Dict[str, Dict[str, Any]] = {}

        for item in markets:
            change_pct = _safe_float(item.get("change_pct"))
            if change_pct is None:
                continue
            if change_pct > 0:
                up += 1
            elif change_pct < 0:
                down += 1
            else:
                flat += 1

            region = str(item.get("region", "全球"))
            bucket = region_stats.setdefault(region, {"count": 0, "sum_change_pct": 0.0, "up": 0, "down": 0})
            bucket["count"] += 1
            bucket["sum_change_pct"] += change_pct
            if change_pct > 0:
                bucket["up"] += 1
            elif change_pct < 0:
                bucket["down"] += 1

        by_region = []
        for region, stat in region_stats.items():
            count = int(stat.get("count", 0))
            avg_change_pct = (stat.get("sum_change_pct", 0.0) / count) if count else 0.0
            by_region.append(
                {
                    "region": region,
                    "count": count,
                    "avg_change_pct": round(avg_change_pct, 2),
                    "up": int(stat.get("up", 0)),
                    "down": int(stat.get("down", 0)),
                }
            )

        by_region.sort(key=lambda x: x.get("region", ""))

        top_movers = sorted(
            [m for m in markets if _safe_float(m.get("change_pct")) is not None],
            key=lambda x: abs(float(x.get("change_pct", 0) or 0)),
            reverse=True,
        )[:5]

        return {
            "total": len(markets),
            "up": up,
            "down": down,
            "flat": flat,
            "by_region": by_region,
            "top_movers": top_movers,
        }

    def parse(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """parse 保持透传。"""
        return raw_data or {}

