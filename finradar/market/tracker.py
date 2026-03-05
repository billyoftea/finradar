#!/usr/bin/env python
# coding=utf-8
"""
每日市场追踪主程序

功能：
- A股大盘与板块动态
- Yahoo Finance 全球股票总览
- 贵金属（黄金/白银）走势
- 加密货币市场行情
- 期货市场变化
- GitHub 技术趋势
- Twitter/X 热点动态
- 微信公众号文章

支持: python -m finradar --mode market
"""

import asyncio
import os
import sys
import json
import logging
import math
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional
from zoneinfo import ZoneInfo

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:  # pragma: no cover - 环境缺少依赖时走降级
    yaml = None
    YAML_AVAILABLE = False

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
BEIJING_TZ = ZoneInfo("Asia/Shanghai")


class MarketTracker:
    """每日市场追踪器"""
    
    def __init__(self, config: Optional[Dict] = None):
        loaded_config = config if isinstance(config, dict) else self._load_market_config_from_yaml()
        self.config = loaded_config or {}
        self.results: Dict[str, Any] = {}
        self.errors: List[str] = []
        tracker_config = self.config.get("market_tracker", {}) if isinstance(self.config, dict) else {}
        if not isinstance(tracker_config, dict):
            tracker_config = {}
        self.fetch_timeout = float(
            os.environ.get(
                "MARKET_FETCH_TIMEOUT",
                tracker_config.get("fetch_timeout", self.config.get("fetch_timeout", 120))
            )
        )
        self.module_timeouts = (
            tracker_config.get("module_timeouts", {})
            or self.config.get("module_timeouts", {})
            or {}
        )
        # 社交抓取较慢，给更长默认超时，避免“看起来失败但其实还在正常抓取”。
        self.module_timeouts.setdefault("twitter", float(os.environ.get("TWITTER_FETCH_TIMEOUT", 900)))
        self.module_timeouts.setdefault("wechat", float(os.environ.get("WECHAT_FETCH_TIMEOUT", 1800)))

    @staticmethod
    def _safe_float(value: Any) -> float | None:
        """安全转 float，过滤 NaN/Inf。"""
        try:
            num = float(value)
        except (TypeError, ValueError):
            return None
        if math.isnan(num) or math.isinf(num):
            return None
        return num

    @staticmethod
    def _parse_datetime_utc(value: Any) -> Optional[datetime]:
        """解析任意时间值为 UTC aware datetime。"""
        if not value:
            return None
        text = str(value).strip()
        if not text:
            return None
        text = text.replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(text)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            return None

    @staticmethod
    def _twitter_tweet_dedup_key(tweet: Dict[str, Any]) -> str:
        """Twitter 推文去重键。"""
        tweet_id = str((tweet or {}).get("id", "") or "").strip()
        if tweet_id:
            return f"id:{tweet_id}"
        url = str((tweet or {}).get("url", "") or (tweet or {}).get("nitter_url", "") or "").strip()
        if url:
            return f"url:{url}"
        username = str((tweet or {}).get("username", "") or "").strip().lower()
        text = str((tweet or {}).get("text", "") or "").strip()[:160]
        return f"txt:{username}:{text}"

    @staticmethod
    def _twitter_tweet_score(tweet: Dict[str, Any]) -> int:
        """互动评分，用于缓存更新时择优。"""
        try:
            likes = int((tweet or {}).get("likes", 0) or 0)
            retweets = int((tweet or {}).get("retweets", 0) or 0)
            replies = int((tweet or {}).get("replies", 0) or 0)
        except Exception:
            return 0
        return likes + retweets + replies

    @staticmethod
    def _resolve_data_path(path_text: str) -> Path:
        """解析输出路径，支持相对项目根目录。"""
        path = Path(str(path_text or "").strip())
        if not path.is_absolute():
            project_root = Path(__file__).resolve().parents[2]
            path = project_root / path
        return path

    @staticmethod
    def _load_json_dict(path: Path) -> Dict[str, Any]:
        """读取 JSON 对象，异常时返回空字典。"""
        try:
            if not path.exists():
                return {}
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    @staticmethod
    def _save_json_dict(path: Path, data: Dict[str, Any]):
        """写入 JSON 对象。"""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.warning("写入缓存失败 %s: %s", path, e)

    def _merge_follow_timeline_cache(
        self,
        fresh_tweets: List[Dict[str, Any]],
        cache_file: str,
        retention_hours: int = 48,
        max_items: int = 30000,
    ) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """合并关注账号推文到本地滚动缓存，并按保留窗口裁剪。"""
        now_utc = datetime.now(timezone.utc)
        retention_hours = max(1, int(retention_hours or 48))
        max_items = max(100, int(max_items or 30000))
        cutoff = now_utc - timedelta(hours=retention_hours)

        cache_path = self._resolve_data_path(cache_file)
        raw_cache = self._load_json_dict(cache_path)
        cached_items = raw_cache.get("tweets", []) if isinstance(raw_cache.get("tweets"), list) else []

        merged: Dict[str, Dict[str, Any]] = {}
        dropped_old = 0

        def _effective_time(item: Dict[str, Any], default_dt: datetime) -> tuple[datetime, datetime]:
            created = self._parse_datetime_utc(item.get("created_at"))
            fetched = self._parse_datetime_utc(item.get("fetched_at")) or default_dt
            return created or fetched, fetched

        def _upsert(item: Dict[str, Any], default_fetched_at: datetime):
            nonlocal dropped_old
            if not isinstance(item, dict):
                return

            key = self._twitter_tweet_dedup_key(item)
            if not key:
                return

            normalized = dict(item)
            item_time, fetched_time = _effective_time(normalized, default_fetched_at)
            if item_time < cutoff:
                dropped_old += 1
                return

            normalized["fetched_at"] = fetched_time.isoformat()
            current = merged.get(key)
            if current is None:
                merged[key] = normalized
                return

            current_time, current_fetched = _effective_time(current, default_fetched_at)
            current_score = self._twitter_tweet_score(current)
            next_score = self._twitter_tweet_score(normalized)
            should_replace = (
                item_time > current_time
                or (item_time == current_time and next_score > current_score)
                or (
                    item_time == current_time
                    and next_score == current_score
                    and fetched_time > current_fetched
                )
            )
            if should_replace:
                merged[key] = normalized

        for item in cached_items:
            _upsert(item, now_utc)

        for item in fresh_tweets or []:
            normalized = dict(item) if isinstance(item, dict) else {}
            normalized["fetched_at"] = now_utc.isoformat()
            _upsert(normalized, now_utc)

        merged_list = list(merged.values())
        merged_list.sort(
            key=lambda x: (
                self._parse_datetime_utc(x.get("created_at"))
                or self._parse_datetime_utc(x.get("fetched_at"))
                or now_utc,
                self._twitter_tweet_score(x),
            ),
            reverse=True,
        )

        if len(merged_list) > max_items:
            merged_list = merged_list[:max_items]

        self._save_json_dict(
            cache_path,
            {
                "updated_at": now_utc.isoformat(),
                "retention_hours": retention_hours,
                "max_items": max_items,
                "tweets": merged_list,
            },
        )

        return merged_list, {
            "cache_file": str(cache_path),
            "cache_before_count": len(cached_items),
            "cache_after_count": len(merged_list),
            "fresh_count": len([t for t in (fresh_tweets or []) if isinstance(t, dict)]),
            "dropped_old_count": dropped_old,
            "retention_hours": retention_hours,
        }

    def _load_market_config_from_yaml(self) -> Dict[str, Any]:
        """
        从 config.yaml 读取市场模块配置。

        仅提取市场追踪需要的配置，避免引入新闻/推送等无关字段。
        """
        if not YAML_AVAILABLE:
            logger.warning("PyYAML 未安装，无法读取 config.yaml，市场模块将使用默认配置")
            return {}

        config_path_text = os.environ.get("CONFIG_PATH", "config/config.yaml")
        config_path = Path(config_path_text)
        if not config_path.is_absolute():
            project_root = Path(__file__).resolve().parents[2]
            config_path = project_root / config_path

        if not config_path.exists():
            logger.warning("未找到配置文件 %s，市场模块将使用默认配置", config_path)
            return {}

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                raw = yaml.safe_load(f) or {}
        except Exception as e:
            logger.warning("读取市场配置失败: %s", e)
            return {}

        if not isinstance(raw, dict):
            return {}

        section_keys = (
            "market_tracker",
            "stock_cn",
            "yahoo_stock",
            "precious_metal",
            "crypto",
            "futures",
            "github",
        )
        parsed: Dict[str, Any] = {}
        for key in section_keys:
            value = raw.get(key)
            if isinstance(value, dict):
                parsed[key] = value
        return parsed

    def _build_stock_overview(self) -> Optional[Dict[str, Any]]:
        """
        构建股票总览（A股 + Yahoo 全球指数），提供统一市场 breadth 视角。
        """
        entries: List[Dict[str, Any]] = []
        seen: set[tuple[str, str]] = set()

        stock_cn = self.results.get("stock_cn")
        if isinstance(stock_cn, dict):
            for item in stock_cn.get("indices", []) or []:
                if not isinstance(item, dict):
                    continue
                symbol = str(item.get("code", "")).strip()
                if not symbol:
                    continue
                key = ("stock_cn", symbol)
                if key in seen:
                    continue
                seen.add(key)

                change_pct = self._safe_float(item.get("change_pct"))
                if change_pct is None:
                    continue

                price = self._safe_float(item.get("price"))
                entries.append(
                    {
                        "source": "stock_cn",
                        "region": "A股",
                        "name": str(item.get("name", symbol)),
                        "symbol": symbol,
                        "price": round(price, 2) if price is not None else None,
                        "change_pct": round(change_pct, 2),
                        "currency": "CNY",
                    }
                )

        yahoo_stock = self.results.get("yahoo_stock")
        if isinstance(yahoo_stock, dict):
            for item in yahoo_stock.get("markets", []) or []:
                if not isinstance(item, dict):
                    continue
                symbol = str(item.get("symbol", "")).strip()
                if not symbol:
                    continue
                key = ("yahoo_finance", symbol)
                if key in seen:
                    continue
                seen.add(key)

                change_pct = self._safe_float(item.get("change_pct"))
                if change_pct is None:
                    continue

                price = self._safe_float(item.get("price"))
                region = str(item.get("region", "全球")).strip() or "全球"
                entries.append(
                    {
                        "source": "yahoo_finance",
                        "region": region,
                        "name": str(item.get("name", symbol)),
                        "symbol": symbol,
                        "price": round(price, 2) if price is not None else None,
                        "change_pct": round(change_pct, 2),
                        "currency": str(item.get("currency", "")).strip(),
                    }
                )

        if not entries:
            return None

        up = sum(1 for item in entries if item.get("change_pct", 0) > 0)
        down = sum(1 for item in entries if item.get("change_pct", 0) < 0)
        flat = len(entries) - up - down

        by_region_map: Dict[str, Dict[str, Any]] = {}
        for item in entries:
            region = str(item.get("region", "全球")) or "全球"
            bucket = by_region_map.setdefault(
                region,
                {"region": region, "count": 0, "up": 0, "down": 0, "sum_change_pct": 0.0},
            )
            change_pct = float(item.get("change_pct", 0) or 0.0)
            bucket["count"] += 1
            bucket["sum_change_pct"] += change_pct
            if change_pct > 0:
                bucket["up"] += 1
            elif change_pct < 0:
                bucket["down"] += 1

        by_region: List[Dict[str, Any]] = []
        for region, bucket in by_region_map.items():
            count = int(bucket.get("count", 0))
            avg = (bucket.get("sum_change_pct", 0.0) / count) if count else 0.0
            by_region.append(
                {
                    "region": region,
                    "count": count,
                    "up": int(bucket.get("up", 0)),
                    "down": int(bucket.get("down", 0)),
                    "avg_change_pct": round(avg, 2),
                }
            )
        by_region.sort(key=lambda x: x.get("avg_change_pct", 0), reverse=True)

        top_gainers = sorted(entries, key=lambda x: float(x.get("change_pct", 0) or 0), reverse=True)[:5]
        top_losers = sorted(entries, key=lambda x: float(x.get("change_pct", 0) or 0))[:5]

        key_name_candidates = {
            "上证指数", "深证成指", "沪深300", "创业板指",
            "标普500", "纳斯达克综合", "道琼斯工业指数",
            "恒生指数", "日经225", "德国DAX", "法国CAC40",
        }
        key_symbol_candidates = {
            "^GSPC", "^IXIC", "^DJI", "^HSI", "^N225", "^GDAXI", "^FCHI",
            "000001", "399001", "000300", "399006", "000001.SS",
        }

        key_indices = []
        key_seen: set[tuple[str, str]] = set()
        for item in entries:
            name = str(item.get("name", ""))
            symbol = str(item.get("symbol", ""))
            if name not in key_name_candidates and symbol not in key_symbol_candidates:
                continue
            marker = (name, symbol)
            if marker in key_seen:
                continue
            key_seen.add(marker)
            key_indices.append(item)
        key_indices = sorted(key_indices, key=lambda x: abs(float(x.get("change_pct", 0) or 0)), reverse=True)[:8]

        return {
            "summary": {
                "tracked": len(entries),
                "up": up,
                "down": down,
                "flat": flat,
                "up_ratio_pct": round((up / len(entries) * 100) if entries else 0.0, 2),
                "sources": {
                    "stock_cn": sum(1 for item in entries if item.get("source") == "stock_cn"),
                    "yahoo_finance": sum(1 for item in entries if item.get("source") == "yahoo_finance"),
                },
            },
            "by_region": by_region,
            "key_indices": key_indices,
            "top_gainers": top_gainers,
            "top_losers": top_losers,
            "timestamp": datetime.now(BEIJING_TZ).isoformat(),
        }

    def _build_speculation_brief_lines(self, max_points: int = 2) -> List[str]:
        """生成超短投机方向提示（仅方向，不含买卖建议）。"""
        points: List[tuple[float, str]] = []
        max_points = max(1, min(int(max_points or 2), 3))
        as_float = lambda v: float(self._safe_float(v) or 0.0)

        stock_overview = self.results.get("stock_overview")
        if isinstance(stock_overview, dict):
            top_gainers = stock_overview.get("top_gainers", [])
            top_losers = stock_overview.get("top_losers", [])
            mover_pool = [m for m in (top_gainers[:2] + top_losers[:2]) if isinstance(m, dict)]
            if mover_pool:
                mover = max(mover_pool, key=lambda x: abs(as_float(x.get("change_pct", 0))))
                move = as_float(mover.get("change_pct", 0))
                name = mover.get("name", mover.get("symbol", "指数"))
                region = mover.get("region", "全球")
                direction = "动量延续" if move > 0 else "高波动回撤"
                points.append((abs(move), f"海外波动：{region} {name} {move:+.2f}%（{direction}）"))

        stock_cn = self.results.get("stock_cn")
        if isinstance(stock_cn, dict):
            sectors = [s for s in stock_cn.get("sectors", []) or [] if isinstance(s, dict)]
            if sectors:
                top_sector = max(sectors, key=lambda x: as_float(x.get("change_pct", 0)))
                sec_move = as_float(top_sector.get("change_pct", 0))
                if sec_move > 0:
                    sec_name = top_sector.get("name", "A股板块")
                    leader = top_sector.get("leading_stock", "")
                    leader_text = f"，龙头 {leader}" if leader else ""
                    points.append((abs(sec_move), f"A股方向：{sec_name} {sec_move:+.2f}%{leader_text}"))

        crypto = self.results.get("crypto")
        if isinstance(crypto, dict):
            coins = [c for c in crypto.get("coins", []) or [] if isinstance(c, dict)]
            if coins:
                top_coin = max(coins, key=lambda x: abs(as_float(x.get("change_24h", 0))))
                coin_move = as_float(top_coin.get("change_24h", 0))
                if abs(coin_move) >= 2:
                    symbol = str(top_coin.get("symbol", "crypto")).upper()
                    points.append((abs(coin_move), f"高波动资产：{symbol} 24h {coin_move:+.2f}%（轻仓）"))

        if not points:
            return [
                "  - 当前无清晰高波动主线，先观察不追单。",
                "  - 纪律：单笔风险不超过本金 1%-2%。",
            ]

        points.sort(key=lambda x: x[0], reverse=True)
        selected = []
        seen = set()
        for _, text in points:
            if text in seen:
                continue
            seen.add(text)
            selected.append(text)
            if len(selected) >= max_points:
                break

        lines = [f"  - {text}" for text in selected]
        lines.append("  - 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。")
        return lines

    async def _run_with_timeout(self, key: str, coro):
        """给单个模块抓取加超时保护，避免某个数据源阻塞整个流程。"""
        timeout = self.module_timeouts.get(key, self.fetch_timeout)
        if not timeout or float(timeout) <= 0:
            return await coro
        try:
            return await asyncio.wait_for(coro, timeout=float(timeout))
        except asyncio.TimeoutError:
            msg = f"{key} 抓取超时 ({int(float(timeout))}s)"
            logger.error(f"❌ {msg}")
            self.errors.append(msg)
            return None
        
    async def fetch_stock_cn(self) -> Optional[Dict]:
        """抓取A股数据"""
        try:
            from .fetcher.stock_cn import StockCNFetcher
            fetcher = StockCNFetcher(self.config.get("stock_cn", {}))
            if fetcher.enabled:
                logger.info("📊 正在抓取 A股市场数据...")
                data = await fetcher.fetch()
                logger.info("✅ A股数据抓取完成")
                return data
        except ImportError as e:
            logger.warning(f"⚠️ A股模块未安装: {e}")
            self.errors.append(f"A股模块: {e}")
        except Exception as e:
            logger.error(f"❌ A股数据抓取失败: {e}")
            self.errors.append(f"A股数据: {e}")
        return None
    
    async def fetch_precious_metal(self) -> Optional[Dict]:
        """抓取贵金属数据"""
        try:
            from .fetcher.precious_metal import PreciousMetalFetcher
            fetcher = PreciousMetalFetcher(self.config.get("precious_metal", {}))
            if fetcher.enabled:
                logger.info("🥇 正在抓取贵金属数据...")
                data = await fetcher.fetch()
                logger.info("✅ 贵金属数据抓取完成")
                return data
        except ImportError as e:
            logger.warning(f"⚠️ 贵金属模块未安装: {e}")
            self.errors.append(f"贵金属模块: {e}")
        except Exception as e:
            logger.error(f"❌ 贵金属数据抓取失败: {e}")
            self.errors.append(f"贵金属数据: {e}")
        return None
    
    async def fetch_crypto(self) -> Optional[Dict]:
        """抓取加密货币数据"""
        try:
            from .fetcher.crypto import CryptoFetcher
            fetcher = CryptoFetcher(self.config.get("crypto", {
                "coins": ["bitcoin", "ethereum", "solana", "bnb", "xrp"],
                "vs_currency": "usd"
            }))
            if fetcher.enabled:
                logger.info("₿ 正在抓取加密货币数据...")
                data = await fetcher.fetch()
                logger.info("✅ 加密货币数据抓取完成")
                return data
        except ImportError as e:
            logger.warning(f"⚠️ 加密货币模块未安装: {e}")
            self.errors.append(f"加密货币模块: {e}")
        except Exception as e:
            logger.error(f"❌ 加密货币数据抓取失败: {e}")
            self.errors.append(f"加密货币数据: {e}")
        return None
    
    async def fetch_futures(self) -> Optional[Dict]:
        """抓取期货数据"""
        try:
            from .fetcher.futures import FuturesFetcher
            fetcher = FuturesFetcher(self.config.get("futures", {}))
            if fetcher.enabled:
                logger.info("📈 正在抓取期货数据...")
                data = await fetcher.fetch()
                logger.info("✅ 期货数据抓取完成")
                return data
        except ImportError as e:
            logger.warning(f"⚠️ 期货模块未安装: {e}")
            self.errors.append(f"期货模块: {e}")
        except Exception as e:
            logger.error(f"❌ 期货数据抓取失败: {e}")
            self.errors.append(f"期货数据: {e}")
        return None

    async def fetch_yahoo_stock(self) -> Optional[Dict]:
        """抓取 Yahoo Finance 全球股票概览"""
        try:
            from .fetcher.yahoo_stock import YahooStockFetcher
            fetcher = YahooStockFetcher(self.config.get("yahoo_stock", {}))
            if fetcher.enabled:
                logger.info("🌍 正在抓取 Yahoo Finance 全球股票概览...")
                data = await fetcher.fetch()
                logger.info("✅ Yahoo Finance 股票概览抓取完成")
                return data
        except ImportError as e:
            logger.warning(f"⚠️ Yahoo Finance 模块未安装: {e}")
            self.errors.append(f"Yahoo Finance模块: {e}")
        except Exception as e:
            logger.error(f"❌ Yahoo Finance 数据抓取失败: {e}")
            self.errors.append(f"Yahoo Finance数据: {e}")
        return None
    
    async def fetch_github(self) -> Optional[Dict]:
        """抓取GitHub趋势数据"""
        try:
            from .fetcher.github import GitHubFetcher
            fetcher = GitHubFetcher(self.config.get("github", {}))
            if fetcher.enabled:
                logger.info("💻 正在抓取 GitHub 趋势...")
                data = await fetcher.fetch()
                logger.info("✅ GitHub 数据抓取完成")
                return data
        except ImportError as e:
            logger.warning(f"⚠️ GitHub模块未安装: {e}")
            self.errors.append(f"GitHub模块: {e}")
        except Exception as e:
            logger.error(f"❌ GitHub数据抓取失败: {e}")
            self.errors.append(f"GitHub数据: {e}")
        return None
    
    async def fetch_twitter(self) -> Optional[Dict]:
        """抓取Twitter热点数据（通过Nitter RSS，从config.yaml读取配置）"""
        try:
            from .fetcher.nitter_rss import NitterRSSFetcher
            from .fetcher.social_config import SocialSourceConfig
            
            # 从全局配置读取
            global_config = SocialSourceConfig()
            twitter_conf = global_config.twitter
            
            if not twitter_conf.enabled:
                logger.info("🐦 Twitter 已在配置中禁用")
                return None
            
            # 构建 fetcher 配置
            config = {
                "enabled": twitter_conf.enabled,
                "nitter_instance": twitter_conf.nitter_instance,
                "accounts": twitter_conf.get_all_accounts(),
                "max_tweets_per_user": twitter_conf.max_tweets_per_user,
                "timeout": twitter_conf.timeout,
                "concurrency": int(getattr(twitter_conf, "follow_concurrency", 1) or 1),
                "request_delay": float(getattr(twitter_conf, "follow_request_delay", 1.0) or 1.0),
                "follow_cache_enabled": bool(getattr(twitter_conf, "follow_cache_enabled", True)),
                "follow_cache_file": str(getattr(twitter_conf, "follow_cache_file", "output/twitter/follow_cache.json") or "output/twitter/follow_cache.json"),
                "follow_cache_retention_hours": int(getattr(twitter_conf, "follow_cache_retention_hours", 48) or 48),
                "follow_cache_max_items": int(getattr(twitter_conf, "follow_cache_max_items", 30000) or 30000),
                "trending_mode": twitter_conf.trending_mode,
                "trending_global_queries": twitter_conf.trending_global_queries,
                "trending_realtime_sampling": twitter_conf.trending_realtime_sampling,
                "trending_queries_per_run": twitter_conf.trending_queries_per_run,
                "trending_min_retweets": twitter_conf.trending_min_retweets,
                "trending_pages_per_query": twitter_conf.trending_pages_per_query,
                "search_delay": twitter_conf.search_delay,
                "search_page_delay": twitter_conf.search_page_delay,
                "trending_cache_hours": twitter_conf.trending_cache_hours,
                "trending_cache_max_items": twitter_conf.trending_cache_max_items,
                "trending_cache_file": twitter_conf.trending_cache_file,
                "trending_state_file": twitter_conf.trending_state_file,
                "trending_engagement_threshold": twitter_conf.trending_engagement_threshold,
                "keyword_trending_min_results": int(getattr(twitter_conf, "keyword_trending_min_results", 0) or 0),
            }
            
            fetcher = NitterRSSFetcher(config)
            if fetcher.enabled:
                configured_max_age_hours = int(getattr(twitter_conf, "max_age_hours", 12) or 12)
                try:
                    hot_window_hours = int(os.environ.get("SOCIAL_HOT_WINDOW_HOURS", "12") or 12)
                except (TypeError, ValueError):
                    hot_window_hours = 12
                effective_window_hours = max(1, hot_window_hours)
                logger.info(
                    "🐦 正在抓取 Twitter 热点 (实例: %s, 抓取时间窗口: %sh, 配置max_age_hours=%sh)...",
                    twitter_conf.nitter_instance,
                    effective_window_hours,
                    configured_max_age_hours,
                )
                logger.info(f"   关注账号: {len(config['accounts'])} 个")

                follow_only_scan = str(os.environ.get("TWITTER_FOLLOW_ONLY_SCAN", "")).strip().lower() in {"1", "true", "yes", "on"}
                follow_cache_enabled = bool(getattr(twitter_conf, "follow_cache_enabled", True))
                follow_cache_file = str(getattr(twitter_conf, "follow_cache_file", "output/twitter/follow_cache.json") or "output/twitter/follow_cache.json")
                follow_cache_retention_hours = int(getattr(twitter_conf, "follow_cache_retention_hours", 48) or 48)
                follow_cache_max_items = int(getattr(twitter_conf, "follow_cache_max_items", 30000) or 30000)

                if follow_only_scan:
                    logger.info("   TWITTER_FOLLOW_ONLY_SCAN=1：仅抓关注账号并更新本地缓存，跳过热门搜索")

                # 先抓关注账号（可落地滚动缓存）
                follow_result = {"tweets": [], "errors": [], "instance_used": fetcher.current_instance}
                fresh_follow_tweets: List[Dict[str, Any]] = []
                follow_tweets: List[Dict[str, Any]] = []
                if twitter_conf.fetch_follow_accounts:
                    follow_result = await fetcher.fetch()
                    fresh_follow_tweets = [item for item in (follow_result.get("tweets", []) or []) if isinstance(item, dict)]
                    for item in fresh_follow_tweets:
                        item.setdefault("is_trending", False)
                else:
                    logger.info("   关注账号抓取已禁用（fetch_follow_accounts=false）")

                follow_cache_stats: Dict[str, Any] = {}
                if follow_cache_enabled:
                    follow_tweets, follow_cache_stats = self._merge_follow_timeline_cache(
                        fresh_tweets=fresh_follow_tweets,
                        cache_file=follow_cache_file,
                        retention_hours=follow_cache_retention_hours,
                        max_items=follow_cache_max_items,
                    )
                    for item in follow_tweets:
                        item.setdefault("is_trending", False)
                    logger.info(
                        "   关注缓存: fresh=%s | cache=%s | dropped_old=%s | file=%s",
                        int(follow_cache_stats.get("fresh_count", 0) or 0),
                        int(follow_cache_stats.get("cache_after_count", 0) or 0),
                        int(follow_cache_stats.get("dropped_old_count", 0) or 0),
                        str(follow_cache_stats.get("cache_file", follow_cache_file)),
                    )
                else:
                    follow_tweets = fresh_follow_tweets

                # 再抓搜索补充（仅后续做时间过滤）
                trending_tweets = []
                trending_errors = []
                trending_result: Dict[str, Any] = {}
                fetch_trending_enabled = bool(twitter_conf.fetch_trending) and (not follow_only_scan)
                if fetch_trending_enabled:
                    keywords = twitter_conf.trending_keywords or None
                    logger.info(
                        "   热门模式: %s | 关键词: %s 个 | 全局查询: %s 个 | 实时采样: %s | KOL保底: %s",
                        str(twitter_conf.trending_mode or "keyword"),
                        len(keywords or []),
                        len(twitter_conf.trending_global_queries or []),
                        "是" if twitter_conf.trending_realtime_sampling else "否",
                        int(getattr(twitter_conf, "kol_min_results", 0) or 0),
                    )
                    trending_result = await fetcher.fetch_trending(
                        keywords=keywords,
                        max_results=0,  # 0=不限制
                    )
                    logger.info(
                        "   热门抓取: 本轮query %s/%s | 原始唯一 %s | 汇总后 %s",
                        len(trending_result.get("queries_used", []) or []),
                        len(trending_result.get("queries_all", []) or trending_result.get("queries_used", []) or []),
                        int(trending_result.get("unique_count", 0) or 0),
                        int(trending_result.get("rolled_count", trending_result.get("unique_count", 0)) or 0),
                    )
                    trending_errors = trending_result.get("errors", []) or []
                    for item in trending_result.get("trending_tweets", []) or []:
                        if not isinstance(item, dict):
                            continue
                        item["is_trending"] = True
                        trending_tweets.append(item)
                else:
                    logger.info("   热门推文抓取已禁用")

                # 合并去重：关注账号优先，搜索补充随后
                merged = []
                seen = set()
                for tweet in follow_tweets + trending_tweets:
                    if not isinstance(tweet, dict):
                        continue
                    dedup_key = tweet.get("id") or tweet.get("url") or f"{tweet.get('username','')}::{tweet.get('text','')[:120]}"
                    if dedup_key in seen:
                        continue
                    seen.add(dedup_key)
                    merged.append(tweet)

                # 仅按时间过滤
                pre_time_filter_count = len(merged)
                post_time_filter_count = len(merged)
                if effective_window_hours > 0 and merged:
                    cutoff_time = datetime.now().astimezone() - timedelta(hours=effective_window_hours)

                    filtered_tweets = []
                    for tweet in merged:
                        candidate_time = tweet.get("created_at", "") or tweet.get("fetched_at", "")
                        if not candidate_time:
                            filtered_tweets.append(tweet)
                            continue

                        try:
                            dt_text = str(candidate_time).replace("Z", "+00:00")
                            tweet_time = datetime.fromisoformat(dt_text)
                            if tweet_time.tzinfo is None:
                                tweet_time = tweet_time.replace(tzinfo=timezone.utc)
                            if tweet_time.astimezone(cutoff_time.tzinfo) >= cutoff_time:
                                filtered_tweets.append(tweet)
                        except (ValueError, TypeError):
                            filtered_tweets.append(tweet)

                    merged = filtered_tweets
                    post_time_filter_count = len(merged)
                    logger.info(
                        "   时间过滤: %s条 → %s条 (过去%s小时内)",
                        pre_time_filter_count,
                        post_time_filter_count,
                        effective_window_hours,
                    )
                time_filter_removed_count = max(0, pre_time_filter_count - post_time_filter_count)

                def _is_keyword_query(item: Dict[str, Any]) -> bool:
                    query = str(item.get("keyword", "") or "").strip().lower()
                    return bool(query) and (not query.startswith("lang:"))

                actual_kol = sum(1 for t in merged if isinstance(t, dict) and not t.get("is_trending"))
                trending_selected_count = sum(1 for t in merged if isinstance(t, dict) and t.get("is_trending"))
                keyword_selected_count = sum(
                    1 for t in merged if isinstance(t, dict) and t.get("is_trending") and _is_keyword_query(t)
                )

                priority_raw = getattr(twitter_conf, "priority_accounts", []) or []
                alias_map = {
                    "samaltman": "sama",
                    "haigao1": "haigao",
                    "marcoslopezdeprado": "lopezdeprado",
                    "shaynecoplan": "shayne_coplan",
                    "nassimtaleb": "nntaleb",
                    "tradethenews": "trade_the_news",
                    "alexwang_": "alexandr_wang",
                    "emad_mostaque": "emostaque",
                }
                priority_set = {
                    alias_map.get(str(name).strip().lstrip("@").lower(), str(name).strip().lstrip("@").lower())
                    for name in priority_raw
                    if str(name).strip()
                }
                priority_selected = int(sum(
                    1 for t in merged if isinstance(t, dict) and (not t.get("is_trending")) and (
                        str(t.get("username", "") or "").strip().lstrip("@").lower() in priority_set
                    )
                ))

                logger.info(
                    "   结果策略: 仅时间过滤，关注保留=%s，搜索补充=%s（关键词命中=%s）",
                    actual_kol,
                    trending_selected_count,
                    keyword_selected_count,
                )

                logger.info(
                    "✅ Twitter 数据抓取完成，共 %s 条 (关注: %s, 热门: %s)",
                    len(merged), len(follow_tweets), len(trending_tweets)
                )

                return {
                    "tweets": merged,
                    "follow_tweets_count": len(follow_tweets),
                    "follow_fresh_tweets_count": len(fresh_follow_tweets),
                    "follow_cache_enabled": bool(follow_cache_enabled),
                    "follow_cache_file": str(follow_cache_stats.get("cache_file", follow_cache_file)) if follow_cache_enabled else "",
                    "follow_cache_retention_hours": int(follow_cache_stats.get("retention_hours", follow_cache_retention_hours) or follow_cache_retention_hours),
                    "follow_cache_size": int(follow_cache_stats.get("cache_after_count", len(follow_tweets)) or len(follow_tweets)),
                    "follow_cache_dropped_old_count": int(follow_cache_stats.get("dropped_old_count", 0) or 0),
                    "trending_tweets_count": len(trending_tweets),
                    "time_filter_window_hours": int(effective_window_hours),
                    "pre_time_filter_count": int(pre_time_filter_count),
                    "post_time_filter_count": int(post_time_filter_count),
                    "time_filter_removed_count": int(time_filter_removed_count),
                    "trending_errors": trending_errors,
                    "trending_query_mode": trending_result.get("query_mode") if fetch_trending_enabled else "",
                    "trending_queries_used": trending_result.get("queries_used", []) if fetch_trending_enabled else [],
                    "trending_queries_all": trending_result.get("queries_all", []) if fetch_trending_enabled else [],
                    "trending_sampling_enabled": bool(trending_result.get("sampling_enabled")) if fetch_trending_enabled else False,
                    "trending_cache_size": int(trending_result.get("cache_size", 0) or 0) if fetch_trending_enabled else 0,
                    "kol_min_results": int(getattr(twitter_conf, "kol_min_results", 0) or 0),
                    "keyword_trending_min_results": int(getattr(twitter_conf, "keyword_trending_min_results", 0) or 0),
                    "kol_selected_count": int(sum(1 for t in merged if isinstance(t, dict) and not t.get("is_trending"))),
                    "keyword_trending_available_count": int(trending_result.get("keyword_query_available_count", 0) or 0),
                    "keyword_trending_selected_count": int(keyword_selected_count),
                    "priority_selected_count": int(sum(1 for t in merged if isinstance(t, dict) and (not t.get("is_trending")) and (str(t.get("username", "") or "").strip().lstrip("@").lower() in priority_set))),
                    "instance_used": follow_result.get("instance_used", fetcher.current_instance),
                    "timestamp": datetime.now(BEIJING_TZ).isoformat(),
                }
        except ImportError as e:
            logger.warning(f"⚠️ Twitter模块未安装: {e}")
            self.errors.append(f"Twitter模块: {e}")
        except Exception as e:
            logger.error(f"❌ Twitter数据抓取失败: {e}")
            self.errors.append(f"Twitter数据: {e}")
        return None
    
    async def fetch_wechat(self) -> Optional[Dict]:
        """抓取微信公众号文章（从config.yaml读取配置）"""
        try:
            from .fetcher.wechat_article import WechatArticleFetcher
            from .fetcher.social_config import SocialSourceConfig
            
            # 从全局配置读取
            global_config = SocialSourceConfig()
            wechat_conf = global_config.wechat
            
            if not wechat_conf.enabled:
                logger.info("📱 微信公众号已在配置中禁用")
                return None
            
            fetcher = WechatArticleFetcher(
                base_url=wechat_conf.service_url,
                timeout=wechat_conf.timeout
            )
            login_reminder_days = max(1, int(getattr(wechat_conf, "login_reminder_days", 4) or 4))
            
            # 检查服务是否可用
            if not await fetcher.check_service():
                logger.warning("⚠️ 微信公众号服务不可用")
                self.errors.append("微信公众号服务不可用 (请检查 wechat-article-exporter 服务)")
                await fetcher.close()
                return None
            
            fetch_content = wechat_conf.fetch_content
            configured_max_age_hours = int(getattr(wechat_conf, "max_age_hours", 12) or 12)
            try:
                hot_window_hours = int(os.environ.get("SOCIAL_HOT_WINDOW_HOURS", "12") or 12)
            except (TypeError, ValueError):
                hot_window_hours = 12
            effective_window_hours = max(1, hot_window_hours)
            auth_key_health = fetcher.get_auth_key_health()
            logger.info(
                "📱 正在抓取微信公众号文章 (服务: %s, 抓取时间窗口: %sh, 配置max_age_hours=%sh, 抓取全文: %s)...",
                wechat_conf.service_url,
                effective_window_hours,
                configured_max_age_hours,
                '是' if fetch_content else '否',
            )
            
            # 计算时间截止点
            cutoff_time = datetime.now() - timedelta(hours=effective_window_hours) if effective_window_hours > 0 else None
            
            # 获取所有配置的公众号
            all_accounts = wechat_conf.get_all_accounts()
            logger.info(f"   配置的公众号: {len(all_accounts)} 个")
            per_account_limit = int(getattr(wechat_conf, "max_articles_per_account", 0) or 0)
            if per_account_limit <= 0:
                logger.info("   普通公众号抓取: 不限篇数（按时间窗口分页抓取）")
            else:
                logger.info("   普通公众号抓取: 每号上限 %s 篇", per_account_limit)

            async def _fetch_account_articles_paginated(fakeid: str, account_name: str) -> List[Any]:
                """分页抓取单个公众号文章；count<=0 视为不限篇数，仅受时间窗口约束。"""
                page_size = 20  # wechat-article-exporter 单页最大 20
                articles_acc: List[Any] = []
                offset = 0

                while True:
                    if per_account_limit > 0:
                        remaining = per_account_limit - len(articles_acc)
                        if remaining <= 0:
                            break
                        request_size = max(1, min(page_size, remaining))
                    else:
                        request_size = page_size

                    page_articles = await fetcher.get_articles(
                        fakeid,
                        offset=offset,
                        count=request_size,
                        account_name=account_name,
                    )
                    if not page_articles:
                        break

                    for art in page_articles:
                        art.account_name = account_name
                    articles_acc.extend(page_articles)

                    # 触达时间窗口下界后停止翻页，避免无意义全量回溯。
                    oldest_time = min(
                        (art.publish_time for art in page_articles if getattr(art, "publish_time", None)),
                        default=None,
                    )
                    if cutoff_time and oldest_time and oldest_time < cutoff_time:
                        break

                    if len(page_articles) < request_size:
                        break
                    offset += len(page_articles)

                return articles_acc
            
            all_articles = []
            follow_before_time_filter_count = 0
            follow_after_time_filter_count = 0
            account_lookup_failures = []
            for account_name in all_accounts:
                try:
                    # 先搜索公众号获取 fakeid
                    accounts = await fetcher.search_accounts(account_name, limit=1)
                    if not accounts:
                        reason = fetcher.last_error_message or "未搜索到公众号"
                        account_lookup_failures.append(f"{account_name}: {reason}")
                        continue

                    # 分页获取文章列表（不含全文）
                    articles = await _fetch_account_articles_paginated(accounts[0].fakeid, account_name)
                    
                    # ⚠️ 关键：先时间过滤，再抓取全文
                    if cutoff_time:
                        before_filter = len(articles)
                        follow_before_time_filter_count += before_filter
                        articles = [a for a in articles if a.publish_time and a.publish_time >= cutoff_time]
                        follow_after_time_filter_count += len(articles)
                        logger.info(
                            "   %s: %s篇 → 过滤后%s篇(%sh内)",
                            account_name,
                            before_filter,
                            len(articles),
                            effective_window_hours,
                        )
                    else:
                        follow_before_time_filter_count += len(articles)
                        follow_after_time_filter_count += len(articles)
                    
                    # 如果启用全文抓取，对过滤后的文章抓取全文
                    if fetch_content and articles:
                        logger.info(f"   正在抓取 {account_name} 的{len(articles)}篇文章全文...")
                        for i, art in enumerate(articles, 1):
                            try:
                                content = await fetcher.get_article_content(art.url)
                                art.content = content
                                if i < len(articles):
                                    await asyncio.sleep(wechat_conf.content_delay)
                            except Exception as e:
                                logger.debug(f"获取文章全文失败 {art.title}: {e}")
                    
                    all_articles.extend(articles)
                except Exception as e:
                    logger.warning(f"获取 {account_name} 文章失败: {e}")
                    account_lookup_failures.append(f"{account_name}: {e}")

            # 微信热门文章（跨账号维度）
            hot_articles = []
            hot_errors = []
            if wechat_conf.fetch_hot_articles:
                logger.info("🔥 正在抓取微信公众号热门文章...")
                hot_result = await fetcher.fetch_hot_articles(
                    max_results=wechat_conf.hot_max_results,
                    hours_ago=effective_window_hours,
                    categories=wechat_conf.hot_categories or None
                )
                hot_errors = hot_result.get("errors", []) or []
                hot_articles = hot_result.get("hot_articles", []) or []
                hot_total_found = int(hot_result.get("total_found", len(hot_articles)) or 0)
                hot_high_quality_count = int(hot_result.get("high_quality_count", len(hot_articles)) or 0)

                # 可选：为热门文章补抓全文，便于后续 AI 深度总结
                if fetch_content and hot_articles:
                    for i, article in enumerate(hot_articles, 1):
                        if getattr(article, "content", "") or not getattr(article, "url", ""):
                            continue
                        try:
                            article.content = await fetcher.get_article_content(article.url)
                        except Exception as e:
                            logger.debug(f"获取热门文章全文失败 {getattr(article, 'title', '')}: {e}")
                        if i < len(hot_articles):
                            await asyncio.sleep(wechat_conf.content_delay)
            else:
                hot_total_found = 0
                hot_high_quality_count = 0
            
            # 按发布时间排序（最新的在前）
            all_articles.sort(key=lambda x: x.publish_time if x.publish_time else datetime.min, reverse=True)

            # 合并普通文章 + 热门文章，热门优先并去重
            merged_articles = []
            seen_articles = {}

            def _article_to_dict(article, is_hot=False):
                return {
                    "title": article.title,
                    "author": article.author,
                    "account_name": article.account_name,
                    "publish_time": article.publish_time.isoformat() if article.publish_time else "",
                    "url": article.url,
                    "digest": article.digest,
                    "content": article.content if hasattr(article, "content") and article.content else "",
                    "read_count": getattr(article, "read_count", 0),
                    "like_count": getattr(article, "like_count", 0),
                    "comment_count": getattr(article, "comment_count", 0),
                    "is_hot": bool(is_hot),
                }

            for article in hot_articles:
                if not article:
                    continue
                data = _article_to_dict(article, is_hot=True)
                key = data["url"] or f"{data['account_name']}::{data['title']}"
                seen_articles[key] = data
                merged_articles.append(data)

            for article in all_articles:
                data = _article_to_dict(article, is_hot=False)
                key = data["url"] or f"{data['account_name']}::{data['title']}"
                if key in seen_articles:
                    # 已有热门版本，补全正文/摘要字段
                    current = seen_articles[key]
                    if not current.get("content") and data.get("content"):
                        current["content"] = data["content"]
                    if not current.get("digest") and data.get("digest"):
                        current["digest"] = data["digest"]
                    continue
                seen_articles[key] = data
                merged_articles.append(data)

            logger.info(
                "✅ 微信公众号文章抓取完成，共 %s 篇 (普通: %s, 热门: %s)",
                len(merged_articles), len(all_articles), len(hot_articles)
            )

            def _is_auth_related_message(text: str) -> bool:
                msg = str(text or "").strip().lower()
                if not msg:
                    return False
                auth_keywords = (
                    "invalid session",
                    "session expired",
                    "session invalid",
                    "login required",
                    "not logged",
                    "auth",
                    "token",
                    "cookie",
                    "401",
                    "403",
                    "未登录",
                    "登录",
                    "认证",
                    "凭据",
                    "会话",
                )
                return any(k in msg for k in auth_keywords)

            health_alerts = []
            login_required = False
            auth_error = fetcher.auth_error_message or ""
            auth_key_age_days = auth_key_health.get("age_days") if isinstance(auth_key_health, dict) else None
            auth_key_updated_at = auth_key_health.get("updated_at", "") if isinstance(auth_key_health, dict) else ""

            if fetcher.auth_invalid:
                login_required = True
                msg = auth_error or fetcher.last_error_message or "公众号登录态可能已失效"
                health_alerts.append(f"检测到微信登录异常：{msg}。请重新扫码登录 wechat-exporter。")

            auth_related_failures = [
                str(msg).strip() for msg in (account_lookup_failures + hot_errors)
                if _is_auth_related_message(msg)
            ]
            if auth_related_failures:
                login_required = True
                if not auth_error:
                    auth_error = auth_related_failures[0]
                if not fetcher.auth_invalid:
                    health_alerts.append(
                        f"检测到微信登录异常：{auth_error}。请重新扫码登录 wechat-exporter。"
                    )

            if isinstance(auth_key_age_days, (int, float)) and auth_key_age_days >= float(login_reminder_days):
                health_alerts.append(
                    f"微信登录凭据最近更新已 {auth_key_age_days:.1f} 天（阈值 {login_reminder_days} 天），建议尽快重新扫码登录。"
                )

            checked_accounts = min(10, len(all_accounts))
            if checked_accounts > 0 and not merged_articles:
                fail_ratio = len(account_lookup_failures) / checked_accounts
                if fail_ratio >= 0.6:
                    health_alerts.append(
                        f"本次抓取公众号文章为 0 篇，账号搜索失败占比 {fail_ratio:.0%}，请检查登录态或服务状态。"
                    )

            # 去重并保序
            dedup_health_alerts = []
            seen_alert = set()
            for alert in health_alerts:
                normalized = str(alert).strip()
                if not normalized or normalized in seen_alert:
                    continue
                seen_alert.add(normalized)
                dedup_health_alerts.append(normalized)
            await fetcher.close()
            
            return {
                "articles": merged_articles[:80],
                "follow_articles_count": len(all_articles),
                "hot_articles_count": len(hot_articles),
                "time_filter_window_hours": int(effective_window_hours),
                "follow_before_time_filter_count": int(follow_before_time_filter_count),
                "follow_after_time_filter_count": int(follow_after_time_filter_count),
                "follow_time_filter_removed_count": int(max(0, follow_before_time_filter_count - follow_after_time_filter_count)),
                "hot_fetch_hours_ago": int(effective_window_hours),
                "hot_total_found_count": int(hot_total_found),
                "hot_high_quality_count": int(hot_high_quality_count),
                "hot_errors": hot_errors,
                "account_lookup_failures": account_lookup_failures[:80],
                "login_required": login_required,
                "fetch_status": "login_required" if login_required else ("warning" if dedup_health_alerts else "ok"),
                "auth_error": auth_error,
                "auth_key_age_days": round(float(auth_key_age_days), 2) if isinstance(auth_key_age_days, (int, float)) else None,
                "auth_key_updated_at": auth_key_updated_at,
                "login_reminder_days": login_reminder_days,
                "health_alerts": dedup_health_alerts,
                "timestamp": datetime.now(BEIJING_TZ).isoformat(),
            }
        except ImportError as e:
            logger.warning(f"⚠️ 微信公众号模块未安装: {e}")
            self.errors.append(f"微信公众号模块: {e}")
        except Exception as e:
            logger.error(f"❌ 微信公众号数据抓取失败: {e}")
            self.errors.append(f"微信公众号数据: {e}")
        return None
    
    async def fetch_all(self, mode: str = "all") -> Dict[str, Any]:
        """
        抓取数据源
        
        mode:
          - "all":    抓取所有 (默认)
          - "market": 仅金融市场 (A股/Yahoo全球股票/贵金属/加密货币/期货/GitHub)
          - "social": 仅社交媒体 (Twitter + 微信公众号)
        """
        logger.info("=" * 60)
        logger.info(f"🚀 开始市场追踪... [模式: {mode}]")
        logger.info(f"📅 时间: {datetime.now(BEIJING_TZ).strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 60)
        
        tasks = []
        keys = []
        
        if mode in ("all", "market"):
            tasks += [
                self._run_with_timeout("stock_cn", self.fetch_stock_cn()),
                self._run_with_timeout("yahoo_stock", self.fetch_yahoo_stock()),
                self._run_with_timeout("precious_metal", self.fetch_precious_metal()),
                self._run_with_timeout("crypto", self.fetch_crypto()),
                self._run_with_timeout("futures", self.fetch_futures()),
                self._run_with_timeout("github", self.fetch_github()),
            ]
            keys += ["stock_cn", "yahoo_stock", "precious_metal", "crypto", "futures", "github"]
        
        if mode in ("all", "social"):
            tasks += [
                self._run_with_timeout("twitter", self.fetch_twitter()),
                self._run_with_timeout("wechat", self.fetch_wechat()),
            ]
            keys += ["twitter", "wechat"]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for key, result in zip(keys, results):
            if isinstance(result, Exception):
                logger.error(f"❌ {key} 抓取异常: {result}")
                self.errors.append(f"{key}: {result}")
            else:
                self.results[key] = result

        stock_overview = self._build_stock_overview()
        if stock_overview:
            self.results["stock_overview"] = stock_overview
        
        return self.results
    
    def generate_report(self) -> str:
        """生成市场日报"""
        report_lines = []
        now = datetime.now(BEIJING_TZ)
        
        report_lines.append("=" * 50)
        report_lines.append(f"📊 每日市场追踪报告")
        report_lines.append(f"📅 {now.strftime('%Y年%m月%d日 %H:%M')}")
        report_lines.append("=" * 50)

        # 股票总览（A股 + Yahoo Finance）
        stock_overview = self.results.get("stock_overview")
        if isinstance(stock_overview, dict):
            report_lines.append("\n🧭 【股票总览】")
            report_lines.append("-" * 40)
            summary = stock_overview.get("summary", {}) if isinstance(stock_overview.get("summary"), dict) else {}
            report_lines.append(
                "  跟踪标的: {tracked} | 上涨: {up} | 下跌: {down} | 平盘: {flat} | 上涨占比: {ratio:.1f}%".format(
                    tracked=int(summary.get("tracked", 0) or 0),
                    up=int(summary.get("up", 0) or 0),
                    down=int(summary.get("down", 0) or 0),
                    flat=int(summary.get("flat", 0) or 0),
                    ratio=float(summary.get("up_ratio_pct", 0.0) or 0.0),
                )
            )

            by_region = stock_overview.get("by_region", [])
            if isinstance(by_region, list) and by_region:
                region_text = []
                for item in by_region[:6]:
                    if not isinstance(item, dict):
                        continue
                    region_text.append(
                        f"{item.get('region', '全球')} {float(item.get('avg_change_pct', 0) or 0):+.2f}% "
                        f"({int(item.get('up', 0) or 0)}/{int(item.get('count', 0) or 0)})"
                    )
                if region_text:
                    report_lines.append(f"  区域强弱: {' | '.join(region_text)}")

            key_indices = stock_overview.get("key_indices", [])
            if isinstance(key_indices, list) and key_indices:
                key_text = []
                for item in key_indices[:6]:
                    if not isinstance(item, dict):
                        continue
                    name = item.get("name", item.get("symbol", "未知"))
                    change_pct = float(item.get("change_pct", 0) or 0.0)
                    icon = "📈" if change_pct >= 0 else "📉"
                    key_text.append(f"{icon}{name} {change_pct:+.2f}%")
                if key_text:
                    report_lines.append(f"  关键指数: {' | '.join(key_text)}")

            top_gainers = stock_overview.get("top_gainers", [])
            if isinstance(top_gainers, list) and top_gainers:
                gainers_text = []
                for item in top_gainers[:3]:
                    if not isinstance(item, dict):
                        continue
                    gainers_text.append(
                        f"{item.get('name', item.get('symbol', '未知'))} {float(item.get('change_pct', 0) or 0):+.2f}%"
                    )
                if gainers_text:
                    report_lines.append(f"  领涨: {', '.join(gainers_text)}")

            top_losers = stock_overview.get("top_losers", [])
            if isinstance(top_losers, list) and top_losers:
                losers_text = []
                for item in top_losers[:3]:
                    if not isinstance(item, dict):
                        continue
                    losers_text.append(
                        f"{item.get('name', item.get('symbol', '未知'))} {float(item.get('change_pct', 0) or 0):+.2f}%"
                    )
                if losers_text:
                    report_lines.append(f"  领跌: {', '.join(losers_text)}")

        # 投机方向（超短）
        report_lines.append("\n🎯 【投机方向（超短）】")
        report_lines.append("-" * 40)
        report_lines.extend(self._build_speculation_brief_lines(max_points=2))
        
        # A股市场
        if self.results.get("stock_cn"):
            report_lines.append("\n🇨🇳 【A股市场】")
            report_lines.append("-" * 40)
            stock_data = self.results["stock_cn"]
            if isinstance(stock_data, dict) and stock_data.get("market_closed"):
                report_lines.append(f"  ⏸ {stock_data.get('market_status', 'A股休市')}")
            elif stock_data.get("indices"):
                for idx in stock_data["indices"][:5]:
                    if isinstance(idx, dict):
                        name = idx.get("name", "未知")
                        price = idx.get("price", 0)
                        change_pct = idx.get("change_pct", 0)
                        icon = "📈" if change_pct >= 0 else "📉"
                        report_lines.append(f"  {icon} {name}: {price:.2f} ({change_pct:+.2f}%)")
            else:
                report_lines.append("  ⚠️ 暂无可用A股行情数据")
        
        # 贵金属
        if self.results.get("precious_metal"):
            report_lines.append("\n🥇 【贵金属】")
            report_lines.append("-" * 40)
            pm_data = self.results["precious_metal"]
            metals = pm_data.get("metals", {}) if isinstance(pm_data, dict) else {}
            if not metals and isinstance(pm_data, dict):
                # 兼容旧结构
                metals = {
                    "gold": pm_data.get("gold"),
                    "silver": pm_data.get("silver"),
                }
            gold = metals.get("gold") if isinstance(metals, dict) else None
            silver = metals.get("silver") if isinstance(metals, dict) else None
            if isinstance(gold, dict):
                report_lines.append(f"  🪙 黄金: ${gold.get('price', 0):.2f} ({gold.get('change_pct', 0):+.2f}%)")
            if isinstance(silver, dict):
                report_lines.append(f"  🥈 白银: ${silver.get('price', 0):.2f} ({silver.get('change_pct', 0):+.2f}%)")

        # Yahoo Finance 全球股票概览
        if self.results.get("yahoo_stock"):
            report_lines.append("\n🌍 【Yahoo Finance 全球股票总览】")
            report_lines.append("-" * 40)
            yahoo_data = self.results["yahoo_stock"]
            markets = yahoo_data.get("markets", []) if isinstance(yahoo_data, dict) else []
            if markets:
                for item in markets[:10]:
                    if not isinstance(item, dict):
                        continue
                    name = item.get("name", item.get("symbol", "未知"))
                    region = item.get("region", "全球")
                    try:
                        price = float(item.get("price", 0) or 0)
                    except (TypeError, ValueError):
                        price = 0.0
                    try:
                        change = float(item.get("change_pct", 0) or 0)
                    except (TypeError, ValueError):
                        change = 0.0
                    icon = "📈" if change >= 0 else "📉"
                    report_lines.append(f"  {icon} [{region}] {name}: {price:.2f} ({change:+.2f}%)")
            else:
                report_lines.append("  ⚠️ 暂无可用 Yahoo Finance 股票概览数据")
        
        # 加密货币
        if self.results.get("crypto"):
            report_lines.append("\n₿ 【加密货币】")
            report_lines.append("-" * 40)
            crypto_data = self.results["crypto"]
            if crypto_data.get("coins"):
                for coin in crypto_data["coins"][:5]:
                    if isinstance(coin, dict):
                        symbol = coin.get("symbol", "???").upper()
                        price = coin.get("price", 0)
                        change = coin.get("change_24h", 0)
                        icon = "📈" if change >= 0 else "📉"
                        report_lines.append(f"  {icon} {symbol}: ${price:,.2f} ({change:+.2f}%)")
        
        # 期货
        if self.results.get("futures"):
            report_lines.append("\n📈 【期货市场】")
            report_lines.append("-" * 40)
            futures_data = self.results["futures"]
            commodities = []
            if isinstance(futures_data, dict):
                commodities = futures_data.get("commodity", []) or futures_data.get("commodities", [])
            if commodities:
                for item in commodities[:5]:
                    if isinstance(item, dict):
                        name = item.get("name", "未知")
                        price = item.get("price", 0)
                        change = item.get("change_pct", 0)
                        icon = "📈" if change >= 0 else "📉"
                        report_lines.append(f"  {icon} {name}: {price:.2f} ({change:+.2f}%)")
        
        # GitHub
        if self.results.get("github"):
            report_lines.append("\n💻 【GitHub 趋势】")
            report_lines.append("-" * 40)
            github_data = self.results["github"]
            if github_data.get("trending"):
                for repo in github_data["trending"][:5]:
                    if isinstance(repo, dict):
                        name = repo.get("name", "未知")
                        stars = repo.get("stars", 0)
                        desc = repo.get("description", "")[:50]
                        report_lines.append(f"  ⭐ {name} ({stars} stars)")
                        if desc:
                            report_lines.append(f"     {desc}...")
        
        # Twitter
        if self.results.get("twitter"):
            report_lines.append("\n🐦 【Twitter 热点】")
            report_lines.append("-" * 40)
            twitter_data = self.results["twitter"]
            tweets = twitter_data.get("tweets", [])
            if twitter_data.get("trending_tweets_count") is not None:
                report_lines.append(
                    f"  来源统计: 关注账号 {twitter_data.get('follow_tweets_count', 0)} 条 | "
                    f"热门讨论 {twitter_data.get('trending_tweets_count', 0)} 条"
                )
            if tweets:
                for tweet in tweets[:5]:
                    if isinstance(tweet, dict):
                        username = tweet.get("username", "未知")
                        text = tweet.get("text", "")[:80].replace("\n", " ")
                        likes = tweet.get("likes", 0)
                        hot_tag = "🔥" if tweet.get("is_trending") else "  "
                        report_lines.append(f"  {hot_tag} @{username}: {text}...")
                        report_lines.append(f"     ❤️ {likes}")
            else:
                report_lines.append("  暂无推文数据")
        
        # 微信公众号
        if self.results.get("wechat"):
            report_lines.append("\n📱 【微信公众号】")
            report_lines.append("-" * 40)
            wechat_data = self.results["wechat"]
            articles = wechat_data.get("articles", [])
            if wechat_data.get("hot_articles_count") is not None:
                report_lines.append(
                    f"  来源统计: 关注公众号 {wechat_data.get('follow_articles_count', 0)} 篇 | "
                    f"热门文章 {wechat_data.get('hot_articles_count', 0)} 篇"
                )
            if articles:
                for article in articles[:5]:
                    if isinstance(article, dict):
                        title = article.get("title", "未知")[:40]
                        account = article.get("account_name", "未知")
                        hot_tag = "🔥" if article.get("is_hot") else "📄"
                        report_lines.append(f"  {hot_tag} [{account}] {title}")
            else:
                report_lines.append("  暂无公众号文章")
        
        # 错误汇总
        if self.errors:
            report_lines.append("\n⚠️ 【抓取警告】")
            report_lines.append("-" * 40)
            for error in self.errors:
                report_lines.append(f"  - {error}")
        
        report_lines.append("\n" + "=" * 50)
        report_lines.append("📌 报告生成完毕")
        report_lines.append("=" * 50)
        
        return "\n".join(report_lines)
    
    def save_report(self, output_dir: str = None, mode: str = "all"):
        if output_dir is None:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            output_dir = os.path.join(project_root, "output", "market")
        """
        保存报告到文件
        
        mode:
          - "social": 根据时间判断早报/晚报标签，避免覆盖
          - "market" / "all": 直接覆盖（市场数据每30分钟更新）
        """
        os.makedirs(output_dir, exist_ok=True)
        
        now = datetime.now(BEIJING_TZ)
        date_str = now.strftime("%Y%m%d")
        
        # 如果是社交媒体模式（早报/晚报），添加时间标签避免覆盖
        suffix = ""
        if mode == "social":
            hour = now.hour
            # 05:00-14:00 算早报，14:00-24:00 算晚报
            if 5 <= hour < 14:
                suffix = "_morning"
                label = "早报"
            elif 14 <= hour < 24:
                suffix = "_evening"
                label = "晚报"
            else:
                suffix = f"_{now.strftime('%H%M')}"  # 其他时间用小时分钟
                label = "临时报告"
            logger.info(f"📅 社交媒体数据标签: {label}")
        
        # 保存文本报告
        report_file = os.path.join(output_dir, f"market_report_{date_str}{suffix}.txt")
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(self.generate_report())
        logger.info(f"📄 报告已保存: {report_file}")
        
        # 保存 JSON 数据
        json_file = os.path.join(output_dir, f"market_data_{date_str}{suffix}.json")
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump({
                "timestamp": now.isoformat(),
                "mode": mode,
                "report_type": suffix.lstrip("_") if suffix else "latest",
                "data": self.results,
                "errors": self.errors
            }, f, ensure_ascii=False, indent=2, default=str)
        logger.info(f"📊 数据已保存: {json_file}")
        
        return report_file, json_file


async def main(mode_override=None):
    """主函数 - 支持 --mode market|social|all 参数

    Args:
        mode_override: 如果从 finradar.__main__ 调用，直接传入模式，跳过 argparse
    """
    if mode_override:
        mode = mode_override
    else:
        import argparse
        parser = argparse.ArgumentParser(description="finradar 市场追踪")
        parser.add_argument("--mode", choices=["all", "market", "social"],
                            default="all", help="运行模式: all=全部, market=仅市场数据, social=仅Twitter+微信")
        args = parser.parse_args()
        mode = args.mode
    
    # 创建追踪器并执行
    tracker = MarketTracker()
    
    try:
        await tracker.fetch_all(mode=mode)
        
        # 生成并打印报告
        report = tracker.generate_report()
        print(report)
        
        # 保存报告（传入 mode 以便添加早报/晚报标签）
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        output_dir = os.getenv("OUTPUT_DIR", os.path.join(project_root, "output", "market"))
        tracker.save_report(output_dir, mode=mode)
        
        logger.info(f"🎉 追踪完成! [模式: {mode}]")
        
    except Exception as e:
        logger.error(f"❌ 执行失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
