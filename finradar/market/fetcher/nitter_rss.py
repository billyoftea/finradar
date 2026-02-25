"""
Nitter RSS 推文抓取器

Nitter 是一个开源的 Twitter 前端替代品，提供 RSS 订阅功能

使用方式:
    仅使用自建 Nitter 实例（需要 Twitter 账号 tokens）

自建实例部署:
    参考 finradar/nitter/README.md

使用方法:
    # 方式1: 使用自建实例 (推荐)
    from finradar.market.fetcher.nitter_rss import NitterRSSFetcher
    
    fetcher = NitterRSSFetcher(config={
        "nitter_instance": "http://localhost:8080",  # 自建实例地址
        "accounts": ["VitalikButerin", "elonmusk"]
    })
    data = await fetcher.fetch()
    
    # 方式2: 使用环境变量配置
    # export NITTER_INSTANCE="http://localhost:8080"
    fetcher = NitterRSSFetcher(config={
        "accounts": ["VitalikButerin"]
    })
"""

import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, List
import logging
import re
import html
import os
import json
from email.utils import parsedate_to_datetime
from urllib.parse import urljoin
from pathlib import Path

from . import BaseFetcher

logger = logging.getLogger(__name__)


class NitterRSSFetcher(BaseFetcher):
    """
    Nitter RSS 推文抓取器
    
    通过 Nitter 实例的 RSS 订阅源获取推文
    完全免费，无需 Twitter API
    """
    
    # 自建实例地址 (优先使用，最稳定)
    # 可通过环境变量 NITTER_INSTANCE 或 config 参数配置
    LOCAL_INSTANCE = os.environ.get("NITTER_INSTANCE", "")
    # 仅使用自建实例
    
    # 推荐关注的账号
    RECOMMENDED_ACCOUNTS = {
        "crypto": [
            "VitalikButerin",   # 以太坊创始人
            "cz_binance",       # Binance CEO
            "WatcherGuru",      # 加密新闻
            "whale_alert",      # 大额转账监控
            "DefiLlama",        # DeFi 数据
            "coinaborek",       # Coinbase
        ],
        "tech": [
            "elonmusk",         # Elon Musk
            "sama",             # Sam Altman
            "ylecun",           # Yann LeCun
            "OpenAI",           # OpenAI 官方
        ],
        "finance": [
            "MacroAlf",         # 宏观分析
            "unusual_whales",   # 期权异动
            "zerohedge",        # 金融新闻
        ],
    }
    
    def __init__(self, config: Optional[Dict] = None):
        super().__init__(config)
        self.project_root = Path(__file__).resolve().parents[3]
        
        # 尝试从全局配置文件读取配置
        self._load_from_global_config()
        
        # 配置要关注的账号（优先使用传入的 config，其次使用全局配置）
        self.accounts = self.config.get("accounts", [])
        if not self.accounts:
            # 如果 config 中没有指定，尝试从全局配置获取
            self.accounts = self._get_accounts_from_global()
        if not self.accounts:
            # 最后使用默认 crypto 账号
            self.accounts = self.RECOMMENDED_ACCOUNTS.get("crypto", [])[:5]
        
        # 每个账号获取的推文数量（0=不限制）
        raw_max_tweets_per_user = self.config.get("max_tweets_per_user", 10)
        try:
            self.max_tweets_per_user = int(raw_max_tweets_per_user)
        except (TypeError, ValueError):
            self.max_tweets_per_user = 10
        
        # 确定 Nitter 实例 (优先级: config > 全局配置 > 环境变量 > 默认本地实例)
        self.current_instance = self._determine_instance()
        
        # 是否使用自建实例
        self.using_local_instance = self._is_local_instance(self.current_instance)
        
        # 请求超时时间
        self.timeout = self.config.get("timeout", 15)
        self.trending_engagement_threshold = int(self.config.get("trending_engagement_threshold", 10) or 10)
        self.trending_mode = str(self.config.get("trending_mode", "keyword") or "keyword").strip().lower()
        if self.trending_mode not in {"keyword", "global", "hybrid"}:
            self.trending_mode = "keyword"
        self.trending_min_retweets = int(self.config.get("trending_min_retweets", 0) or 0)
        self.trending_pages_per_query = max(1, int(self.config.get("trending_pages_per_query", 3) or 3))
        self.trending_realtime_sampling = bool(self.config.get("trending_realtime_sampling", False))
        self.trending_queries_per_run = max(0, int(self.config.get("trending_queries_per_run", 0) or 0))
        self.trending_cache_hours = max(1, int(self.config.get("trending_cache_hours", 24) or 24))
        self.trending_cache_max_items = max(100, int(self.config.get("trending_cache_max_items", 2000) or 2000))
        self.trending_cache_file = str(self.config.get("trending_cache_file", "output/twitter/trending_cache.json") or "output/twitter/trending_cache.json")
        self.trending_state_file = str(self.config.get("trending_state_file", "output/twitter/trending_state.json") or "output/twitter/trending_state.json")
        self.keyword_trending_min_results = max(0, int(self.config.get("keyword_trending_min_results", 0) or 0))
        self.trending_global_queries = [
            str(q).strip() for q in (self.config.get("trending_global_queries", []) or [])
            if str(q).strip()
        ]
        
        # 是否启用
        self.enabled = self.config.get("enabled", True)
        
        instance_type = "本地/自建" if self.using_local_instance else "自定义远程"
        logger.info(f"NitterRSSFetcher initialized with {len(self.accounts)} accounts, using {instance_type} instance: {self.current_instance}")
    
    def _load_from_global_config(self):
        """从全局配置文件加载 Twitter 配置"""
        try:
            from .social_config import SocialSourceConfig
            global_config = SocialSourceConfig()
            
            if global_config.twitter.enabled:
                # 合并全局配置（不覆盖已有配置）
                if "nitter_instance" not in self.config:
                    self.config["nitter_instance"] = global_config.twitter.nitter_instance
                if "max_tweets_per_user" not in self.config:
                    self.config["max_tweets_per_user"] = global_config.twitter.max_tweets_per_user
                if "timeout" not in self.config:
                    self.config["timeout"] = global_config.twitter.timeout
                if "enabled" not in self.config:
                    self.config["enabled"] = global_config.twitter.enabled
                if "trending_mode" not in self.config:
                    self.config["trending_mode"] = global_config.twitter.trending_mode
                if "trending_global_queries" not in self.config:
                    self.config["trending_global_queries"] = global_config.twitter.trending_global_queries
                if "trending_realtime_sampling" not in self.config:
                    self.config["trending_realtime_sampling"] = global_config.twitter.trending_realtime_sampling
                if "trending_queries_per_run" not in self.config:
                    self.config["trending_queries_per_run"] = global_config.twitter.trending_queries_per_run
                if "trending_min_retweets" not in self.config:
                    self.config["trending_min_retweets"] = global_config.twitter.trending_min_retweets
                if "trending_pages_per_query" not in self.config:
                    self.config["trending_pages_per_query"] = global_config.twitter.trending_pages_per_query
                if "search_delay" not in self.config:
                    self.config["search_delay"] = global_config.twitter.search_delay
                if "search_page_delay" not in self.config:
                    self.config["search_page_delay"] = global_config.twitter.search_page_delay
                if "trending_cache_hours" not in self.config:
                    self.config["trending_cache_hours"] = global_config.twitter.trending_cache_hours
                if "trending_cache_max_items" not in self.config:
                    self.config["trending_cache_max_items"] = global_config.twitter.trending_cache_max_items
                if "trending_cache_file" not in self.config:
                    self.config["trending_cache_file"] = global_config.twitter.trending_cache_file
                if "trending_state_file" not in self.config:
                    self.config["trending_state_file"] = global_config.twitter.trending_state_file
                if "trending_engagement_threshold" not in self.config:
                    self.config["trending_engagement_threshold"] = global_config.twitter.trending_engagement_threshold
                if "keyword_trending_min_results" not in self.config:
                    self.config["keyword_trending_min_results"] = global_config.twitter.keyword_trending_min_results

                # 存储全局账号配置
                self._global_accounts = global_config.twitter.accounts
            else:
                self._global_accounts = {}
                
        except Exception as e:
            logger.debug(f"Could not load global config: {e}")
            self._global_accounts = {}
    
    def _get_accounts_from_global(self) -> List[str]:
        """从全局配置获取所有账号"""
        all_accounts = []
        for category, accounts in self._global_accounts.items():
            all_accounts.extend(accounts)
        return all_accounts
    
    def _determine_instance(self) -> str:
        """
        确定要使用的 Nitter 实例
        优先级: config 参数 > 环境变量 > 默认本地实例
        """
        config_instance = str(self.config.get("nitter_instance", "") or "").strip()
        if config_instance:
            return config_instance.rstrip("/")

        env_instance = str(os.environ.get("NITTER_INSTANCE", "") or "").strip()
        if env_instance:
            return env_instance.rstrip("/")

        default_instance = "http://localhost:8080"
        logger.warning("NITTER_INSTANCE 未配置，使用默认自建实例: %s", default_instance)
        return default_instance

    def _is_local_instance(self, url: str) -> bool:
        """检查是否为本地/自建实例"""
        # 包含所有私有 IP 地址段: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
        local_patterns = ["localhost", "127.0.0.1", "0.0.0.0", "192.168.", "10.", "172."]
        return any(pattern in url for pattern in local_patterns)
    
    async def fetch(self) -> Dict[str, Any]:
        """
        抓取所有关注账号的推文
        
        Returns:
            包含推文列表的字典
        """
        all_tweets = []
        errors = []
        
        # 请求间隔（秒），避免触发速率限制
        request_delay = float(self.config.get("request_delay", 0.1) or 0.1)
        try:
            concurrency = max(1, int(self.config.get("concurrency", 5) or 5))
        except (TypeError, ValueError):
            concurrency = 5

        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={"User-Agent": "Mozilla/5.0 (compatible; finradar/1.0)"}
        ) as session:
            if concurrency > 1:
                sem = asyncio.Semaphore(concurrency)

                async def _fetch_one(username):
                    async with sem:
                        try:
                            result = await self._fetch_user_rss(session, username)
                            if result:
                                return ("ok", username, result)
                        except Exception as e:
                            return ("err", username, str(e))
                        return ("ok", username, [])

                tasks = [_fetch_one(u) for u in self.accounts]
                results = await asyncio.gather(*tasks, return_exceptions=True)

                for r in results:
                    if isinstance(r, Exception):
                        errors.append(str(r))
                    elif r[0] == "ok" and r[2]:
                        all_tweets.extend(r[2])
                    elif r[0] == "err":
                        errors.append(f"@{r[1]}: {r[2]}")
                        logger.warning(f"Failed to fetch @{r[1]}: {r[2]}")
            else:
                for i, username in enumerate(self.accounts):
                    try:
                        result = await self._fetch_user_rss(session, username)
                        if result:
                            all_tweets.extend(result)
                    except Exception as e:
                        errors.append(f"@{username}: {str(e)}")
                        logger.warning(f"Failed to fetch @{username}: {e}")

                    if i < len(self.accounts) - 1:
                        await asyncio.sleep(request_delay)
        
        # 按时间排序（最新在前）
        all_tweets.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        
        return {
            "tweets": all_tweets,
            "errors": errors,
            "instance_used": self.current_instance,
            "timestamp": datetime.now()
        }
    
    async def fetch_trending(self, keywords: List[str] = None, max_results: int = 30) -> Dict[str, Any]:
        """
        抓取热门推文（基于关键词搜索 + 按互动数据排序）
        
        Args:
            keywords: 搜索关键词列表，默认使用热门金融/科技关键词
            max_results: 返回的最大推文数量
            
        Returns:
            包含热门推文列表的字典
        """
        # 默认关键词模式（金融、加密、AI、科技相关）
        default_keywords = [
            "bitcoin", "crypto", "AI", "AI artificial intelligence",
            "stock market", "nasdaq", "SPY"
        ]
        # 默认全网模式（按语言采样全局热议）
        default_global_queries = [
            "lang:en",
            "lang:es",
            "lang:ja",
            "lang:zh",
            "lang:fr",
            "lang:de",
            "lang:pt",
            "lang:ar",
            "lang:hi",
            "lang:ko",
        ]

        keyword_queries = [str(q).strip() for q in (keywords or []) if str(q).strip()]
        if not keyword_queries:
            keyword_queries = list(default_keywords)
        global_queries = self.trending_global_queries or default_global_queries

        if self.trending_mode == "global":
            all_queries = list(global_queries)
        elif self.trending_mode == "hybrid":
            all_queries = keyword_queries + list(global_queries)
        else:
            all_queries = keyword_queries

        # 去重并保序
        seen_queries = set()
        dedup_queries = []
        for q in all_queries:
            key = q.lower()
            if key in seen_queries:
                continue
            seen_queries.add(key)
            dedup_queries.append(q)
        all_queries = dedup_queries

        sampled = False
        cursor_before = 0
        cursor_after = 0
        if self.trending_realtime_sampling and self.trending_queries_per_run > 0 and len(all_queries) > self.trending_queries_per_run:
            sampled = True
            queries, cursor_before, cursor_after = self._select_queries_for_run(all_queries)
        else:
            queries = list(all_queries)

        all_trending_tweets = []
        errors = []
        if self.using_local_instance:
            search_delay = float(self.config.get("search_delay", 0.2) or 0.2)
        else:
            search_delay = float(self.config.get("search_delay", 2.0) or 2.0)
        min_retweets = max(0, int(self.trending_min_retweets or 0))
        
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={"User-Agent": "Mozilla/5.0 (compatible; finradar/1.0)"}
        ) as session:
            # 对每个关键词进行搜索
            for i, keyword in enumerate(queries):
                try:
                    tweets = await self._search_tweets(
                        session,
                        keyword,
                        min_retweets=min_retweets,
                        max_pages=self.trending_pages_per_query,
                    )
                    if tweets:
                        all_trending_tweets.extend(tweets)
                        logger.info(f"Found {len(tweets)} tweets for keyword '{keyword}'")
                except Exception as e:
                    errors.append(f"Search '{keyword}': {str(e)}")
                    logger.warning(f"Failed to search for '{keyword}': {e}")
                
                # 搜索请求间隔
                if i < len(queries) - 1:
                    await asyncio.sleep(search_delay)

        # 按互动数据排序（点赞+转推数）
        all_trending_tweets.sort(
            key=lambda x: (x.get("likes", 0) + x.get("retweets", 0)),
            reverse=True
        )

        # 去重（根据推文ID）
        seen_ids = set()
        unique_tweets = []
        for tweet in all_trending_tweets:
            dedup_key = self._tweet_dedup_key(tweet)
            if dedup_key in seen_ids:
                continue
            seen_ids.add(dedup_key)
            unique_tweets.append(tweet)

        rolled_tweets = unique_tweets
        cache_stats = {"cache_size": len(unique_tweets), "rolled_count": len(unique_tweets)}
        if sampled:
            rolled_tweets, cache_stats = self._merge_trending_cache(unique_tweets)

        selected_tweets, keyword_available, keyword_selected = self._apply_keyword_mix_quota(
            rolled_tweets,
            max_results=max_results,
        )

        return {
            "trending_tweets": selected_tweets,
            "total_found": len(all_trending_tweets),
            "unique_count": len(unique_tweets),
            "rolled_count": len(rolled_tweets),
            "keyword_query_available_count": keyword_available,
            "keyword_query_selected_count": keyword_selected,
            "query_mode": self.trending_mode,
            "queries_used": queries,
            "queries_all": all_queries,
            "sampling_enabled": sampled,
            "query_cursor_before": cursor_before,
            "query_cursor_after": cursor_after,
            "cache_size": cache_stats.get("cache_size", len(rolled_tweets)),
            "cache_window_hours": self.trending_cache_hours,
            "errors": errors,
            "instance_used": self.current_instance,
            "timestamp": datetime.now()
        }

    def _resolve_data_path(self, path_text: str) -> Path:
        """解析配置路径，支持相对仓库根目录。"""
        p = Path(str(path_text or "").strip())
        if not p.is_absolute():
            p = self.project_root / p
        return p

    def _load_json_dict(self, path: Path) -> Dict[str, Any]:
        """读取 JSON 对象，失败时返回空字典。"""
        try:
            if not path.exists():
                return {}
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, dict) else {}
        except Exception as e:
            logger.debug(f"Failed to load json {path}: {e}")
            return {}

    def _save_json_dict(self, path: Path, data: Dict[str, Any]):
        """写入 JSON 对象。"""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.warning(f"Failed to save json {path}: {e}")

    def _select_queries_for_run(self, all_queries: List[str]) -> tuple[List[str], int, int]:
        """
        轮询选择本轮查询（小批量），并持久化 cursor。
        """
        total = len(all_queries)
        if total <= 0:
            return [], 0, 0

        state_path = self._resolve_data_path(self.trending_state_file)
        state = self._load_json_dict(state_path)
        try:
            cursor = int(state.get("cursor", 0) or 0)
        except Exception:
            cursor = 0
        cursor = cursor % total

        batch_size = max(1, min(total, self.trending_queries_per_run))
        selected = [all_queries[(cursor + i) % total] for i in range(batch_size)]
        next_cursor = (cursor + batch_size) % total

        self._save_json_dict(
            state_path,
            {
                "cursor": next_cursor,
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "batch_size": batch_size,
                "total_queries": total,
            },
        )

        return selected, cursor, next_cursor

    def _parse_datetime_utc(self, value: Any) -> Optional[datetime]:
        """解析时间字符串为 UTC aware datetime。"""
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

    def _tweet_dedup_key(self, tweet: Dict[str, Any]) -> str:
        """生成推文去重键。"""
        tweet_id = str(tweet.get("id", "") or "").strip()
        if tweet_id:
            return f"id:{tweet_id}"
        url = str(tweet.get("url", "") or tweet.get("nitter_url", "") or "").strip()
        if url:
            return f"url:{url}"
        username = str(tweet.get("username", "") or "").strip().lower()
        text = str(tweet.get("text", "") or "").strip()[:160]
        return f"txt:{username}:{text}"

    def _tweet_score(self, tweet: Dict[str, Any]) -> int:
        """互动评分，用于缓存合并时择优。"""
        try:
            likes = int(tweet.get("likes", 0) or 0)
            retweets = int(tweet.get("retweets", 0) or 0)
            replies = int(tweet.get("replies", 0) or 0)
        except Exception:
            return 0
        return likes + retweets + replies

    
    def _is_global_query_text(self, query: str) -> bool:
        q = str(query or "").strip().lower()
        return bool(q) and q.startswith("lang:")

    def _is_keyword_query_tweet(self, tweet: Dict[str, Any]) -> bool:
        query = str((tweet or {}).get("keyword", "") or "").strip()
        if not query:
            return False
        return not self._is_global_query_text(query)

    def _apply_keyword_mix_quota(self, tweets: List[Dict[str, Any]], max_results: int) -> tuple[List[Dict[str, Any]], int, int]:
        ranked = list(tweets or [])
        keyword_ranked = [t for t in ranked if self._is_keyword_query_tweet(t)]
        keyword_available = len(keyword_ranked)

        # max_results<=0 视为不限制（全量返回）
        if max_results <= 0:
            return ranked, keyword_available, keyword_available

        keyword_target = min(max_results, max(0, int(self.keyword_trending_min_results or 0)))
        if keyword_target <= 0 or not keyword_ranked:
            keyword_selected = sum(1 for t in ranked[:max_results] if self._is_keyword_query_tweet(t))
            return ranked[:max_results], keyword_available, keyword_selected

        selected: List[Dict[str, Any]] = []
        selected_keys = set()

        def _key(item: Dict[str, Any]) -> str:
            return self._tweet_dedup_key(item)

        for tweet in keyword_ranked:
            if len(selected) >= keyword_target or len(selected) >= max_results:
                break
            key = _key(tweet)
            if key in selected_keys:
                continue
            selected.append(tweet)
            selected_keys.add(key)

        for tweet in ranked:
            if len(selected) >= max_results:
                break
            key = _key(tweet)
            if key in selected_keys:
                continue
            selected.append(tweet)
            selected_keys.add(key)

        keyword_selected = sum(1 for t in selected if self._is_keyword_query_tweet(t))
        return selected, keyword_available, keyword_selected

    def _merge_trending_cache(self, fresh_tweets: List[Dict[str, Any]]) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        将本轮热门推文合并到滚动缓存，返回窗口期内聚合结果。
        """
        now_utc = datetime.now(timezone.utc)
        cutoff = now_utc - timedelta(hours=self.trending_cache_hours)
        cache_path = self._resolve_data_path(self.trending_cache_file)
        raw_cache = self._load_json_dict(cache_path)
        cached_items = raw_cache.get("tweets", []) if isinstance(raw_cache.get("tweets"), list) else []

        merged: Dict[str, Dict[str, Any]] = {}
        merged_meta: Dict[str, datetime] = {}

        def _upsert(item: Dict[str, Any], default_fetched_at: datetime):
            if not isinstance(item, dict):
                return
            key = self._tweet_dedup_key(item)
            if not key:
                return

            fetched_at = self._parse_datetime_utc(item.get("fetched_at")) or default_fetched_at
            if fetched_at < cutoff:
                return

            normalized = dict(item)
            normalized["fetched_at"] = fetched_at.isoformat()

            current = merged.get(key)
            if current is None:
                merged[key] = normalized
                merged_meta[key] = fetched_at
                return

            # 优先保留互动更高的推文；相同互动时保留最近抓到的版本
            current_score = self._tweet_score(current)
            next_score = self._tweet_score(normalized)
            current_fetched = merged_meta.get(key) or default_fetched_at
            should_replace = (next_score > current_score) or (
                next_score == current_score and fetched_at > current_fetched
            )
            if should_replace:
                merged[key] = normalized
                merged_meta[key] = fetched_at

        for item in cached_items:
            _upsert(item, now_utc)

        for item in fresh_tweets:
            normalized = dict(item) if isinstance(item, dict) else {}
            normalized["fetched_at"] = now_utc.isoformat()
            _upsert(normalized, now_utc)

        merged_list = list(merged.values())
        merged_list.sort(
            key=lambda x: (
                self._tweet_score(x),
                self._parse_datetime_utc(x.get("fetched_at")) or now_utc,
            ),
            reverse=True,
        )
        if len(merged_list) > self.trending_cache_max_items:
            merged_list = merged_list[:self.trending_cache_max_items]

        self._save_json_dict(
            cache_path,
            {
                "updated_at": now_utc.isoformat(),
                "cache_hours": self.trending_cache_hours,
                "tweets": merged_list,
            },
        )

        return merged_list, {"cache_size": len(merged_list), "rolled_count": len(merged_list)}
    
    async def _search_tweets(
        self,
        session: aiohttp.ClientSession,
        keyword: str,
        min_retweets: int = 0,
        max_pages: int = 1,
    ) -> List[Dict]:
        """
        搜索热门推文（仅使用当前自建实例）
        """
        params = {
            "q": keyword,
            "f": "tweets",
            "include": "nativeretweets",
        }
        if min_retweets > 0:
            params["min_retweets"] = str(min_retweets)

        max_pages = max(1, int(max_pages or 1))
        page_delay = float(
            self.config.get(
                "search_page_delay",
                0.3 if self.using_local_instance else 1.0,
            ) or (0.3 if self.using_local_instance else 1.0)
        )

        instance = self.current_instance
        search_url = f"{instance}/search"
        all_tweets: List[Dict[str, Any]] = []
        seen_ids = set()
        next_page_url = ""

        for page_idx in range(max_pages):
            request_url = search_url if page_idx == 0 else next_page_url
            request_params = params if page_idx == 0 else None
            if not request_url:
                break

            try:
                async with session.get(
                    request_url,
                    params=request_params,
                    timeout=aiohttp.ClientTimeout(total=self.timeout),
                ) as response:
                    if response.status != 200:
                        logger.warning(
                            f"Search failed on {instance} for '{keyword}' page {page_idx + 1}: HTTP {response.status}"
                        )
                        break

                    html_doc = await response.text()
                    page_tweets = self._parse_search_results(html_doc, keyword)
                    for tweet in page_tweets:
                        dedup_key = (
                            tweet.get("id")
                            or tweet.get("url")
                            or f"{tweet.get('username', '')}::{tweet.get('text', '')[:120]}"
                        )
                        if dedup_key in seen_ids:
                            continue
                        seen_ids.add(dedup_key)
                        all_tweets.append(tweet)

                    next_href = self._extract_next_page_href(html_doc)
                    if next_href:
                        next_page_url = urljoin(f"{instance}/search", next_href)
                    else:
                        next_page_url = ""

            except asyncio.TimeoutError:
                logger.warning(f"Search timeout on {instance} for '{keyword}' page {page_idx + 1}")
                break
            except Exception as e:
                logger.error(f"Error searching tweets on {instance} for '{keyword}' page {page_idx + 1}: {e}")
                break

            if page_idx < max_pages - 1 and next_page_url:
                await asyncio.sleep(page_delay)

        return all_tweets

    def _extract_next_page_href(self, html_doc: str) -> str:
        """从搜索结果页面提取下一页链接（cursor）。"""
        try:
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html_doc, "html.parser")
            link = soup.select_one("div.show-more a[href]")
            if link and link.get("href"):
                return str(link.get("href")).strip()
            return ""
        except Exception:
            return ""
    
    def _parse_search_results(self, html: str, keyword: str) -> List[Dict]:
        """
        解析搜索结果HTML
        
        Args:
            html: 搜索结果HTML
            keyword: 搜索关键词
            
        Returns:
            推文列表
        """
        tweets = []
        
        try:
            # 使用BeautifulSoup解析HTML
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            
            # 查找所有推文元素
            tweet_items = soup.find_all("div", class_="timeline-item")
            
            for item in tweet_items:
                try:
                    # 提取用户名
                    username = item.get("data-username", "")
                    if not username:
                        continue
                    
                    # 提取推文内容
                    tweet_content = item.find("div", class_="tweet-content")
                    if not tweet_content:
                        continue
                    
                    text = tweet_content.get_text(" ", strip=True)
                    if not text:
                        continue
                    
                    # 提取链接和推文ID
                    tweet_link = item.find("a", class_="tweet-link")
                    tweet_url = ""
                    tweet_id = ""
                    if tweet_link and tweet_link.get("href"):
                        tweet_url = tweet_link["href"]
                        # 从URL提取ID: /username/status/123456
                        match = re.search(r"/status/(\d+)", tweet_url)
                        if match:
                            tweet_id = match.group(1)
                    
                    # 提取时间（Nitter 页面显示 UTC 时间）
                    created_at = datetime.now(timezone.utc).isoformat()
                    date_link = item.select_one("span.tweet-date a[title]")
                    if date_link:
                        raw_time = str(date_link.get("title", "")).strip()
                        if raw_time:
                            parsed_time = None
                            for fmt in ("%b %d, %Y · %I:%M %p UTC", "%b %d, %Y · %H:%M UTC"):
                                try:
                                    parsed_time = datetime.strptime(raw_time, fmt).replace(tzinfo=timezone.utc)
                                    break
                                except Exception:
                                    continue
                            if parsed_time:
                                created_at = parsed_time.isoformat()

                    # 提取互动数据（点赞、转推等）
                    stats_item = item.find("div", class_="tweet-stats")
                    likes = 0
                    retweets = 0
                    replies = 0
                    
                    if stats_item:
                        # 查找互动图标和数值
                        tweet_stat_elements = stats_item.find_all("span", class_="tweet-stat")
                        for stat in tweet_stat_elements:
                            icon_class = ""
                            value_text = ""
                            
                            icon_elem = stat.find("span", class_=re.compile(r"icon-"))
                            if icon_elem:
                                icon_class = " ".join(icon_elem.get("class", []))
                            
                            # 提取数值
                            value_div = stat.find("div")
                            if value_div:
                                value_text = value_div.get_text(strip=True)
                            
                            # 解析数值
                            value = 0
                            try:
                                normalized = value_text.replace(",", "").strip().upper()
                                if normalized.endswith("K"):
                                    value = int(float(normalized[:-1]) * 1_000)
                                elif normalized.endswith("M"):
                                    value = int(float(normalized[:-1]) * 1_000_000)
                                else:
                                    value = int(normalized or "0")
                            except:
                                pass
                            
                            # 根据图标类型分配数值
                            if "icon-heart" in icon_class:
                                likes = value
                            elif "icon-retweet" in icon_class:
                                retweets = value
                            elif "icon-comment" in icon_class:
                                replies = value
                    
                    # 构造Twitter原始链接
                    twitter_url = f"https://twitter.com/{username}/status/{tweet_id}" if tweet_id else ""
                    
                    # 只添加有一定互动量的推文（过滤低质量内容）
                    total_engagement = likes + retweets + replies
                    if total_engagement < self.trending_engagement_threshold:
                        continue
                    
                    tweets.append({
                        "id": tweet_id,
                        "text": text,
                        "username": username,
                        "user_name": username,  # Nitter搜索结果不提供显示名称
                        "created_at": created_at,
                        "likes": likes,
                        "retweets": retweets,
                        "replies": replies,
                        "url": twitter_url,
                        "nitter_url": f"{self.current_instance}/status/{tweet_id}" if tweet_id else "",
                        "source": "nitter_search",
                        "keyword": keyword
                    })
                    
                except Exception as e:
                    logger.debug(f"Error parsing tweet item: {e}")
                    continue
            
            logger.info(f"Parsed {len(tweets)} tweets from keyword '{keyword}'")
            return tweets
            
        except ImportError:
            logger.error("BeautifulSoup not installed. Run: pip install beautifulsoup4")
            return []
        except Exception as e:
            logger.error(f"Error parsing search results: {e}")
            return []
    
    async def _fetch_user_rss(self, session: aiohttp.ClientSession, username: str) -> List[Dict]:
        """
        获取单个用户的 RSS 订阅（仅使用当前自建实例）
        """
        instance = self.current_instance
        rss_url = f"{instance}/{username}/rss"

        try:
            async with session.get(rss_url) as response:
                if response.status == 200:
                    content = await response.text()

                    if not content.strip().startswith("<"):
                        logger.warning(f"Invalid RSS response from {instance}: not XML")
                        return []

                    tweets = self._parse_rss(content, username)
                    if self.max_tweets_per_user > 0:
                        return tweets[:self.max_tweets_per_user]
                    return tweets

                if response.status == 404:
                    logger.warning(f"User @{username} not found on {instance}")
                    return []

                if response.status == 403:
                    raise Exception(f"403 Forbidden from {instance} - instance may require tokens")

                if response.status == 429:
                    raise Exception(f"429 Too Many Requests from {instance}")

                raise Exception(f"HTTP {response.status} from {instance}")

        except asyncio.TimeoutError:
            raise Exception(f"Timeout fetching {rss_url}")
        except Exception as e:
            raise Exception(f"Failed fetching {rss_url}: {e}")

    def _parse_rss(self, rss_content: str, username: str) -> List[Dict]:
        """
        解析 RSS XML 内容
        
        Args:
            rss_content: RSS XML 字符串
            username: 用户名
        
        Returns:
            推文列表
        """
        tweets = []
        
        try:
            root = ET.fromstring(rss_content)
            channel = root.find("channel")
            
            if channel is None:
                return []
            
            # 获取用户显示名称
            user_name = username
            title_elem = channel.find("title")
            if title_elem is not None and title_elem.text:
                # 格式: "User Name / @username"
                user_name = title_elem.text.split(" /")[0].strip()
            
            # 解析每条推文
            for item in channel.findall("item"):
                tweet = self._parse_item(item, username, user_name)
                if tweet:
                    tweets.append(tweet)
        
        except ET.ParseError as e:
            logger.error(f"RSS parse error: {e}")
        
        return tweets
    
    def _parse_item(self, item: ET.Element, username: str, user_name: str) -> Optional[Dict]:
        """
        解析单条 RSS item
        
        Args:
            item: XML item 元素
            username: 用户名
            user_name: 显示名称
        
        Returns:
            推文字典或 None
        """
        try:
            # 获取推文链接
            link_elem = item.find("link")
            link = link_elem.text if link_elem is not None else ""
            
            # 从链接提取推文 ID
            tweet_id = ""
            if link:
                # 格式: https://nitter.xxx/user/status/123456
                match = re.search(r"/status/(\d+)", link)
                if match:
                    tweet_id = match.group(1)
            
            # 获取发布时间
            pub_date_elem = item.find("pubDate")
            created_at = ""
            if pub_date_elem is not None and pub_date_elem.text:
                try:
                    dt = parsedate_to_datetime(pub_date_elem.text)
                    created_at = dt.isoformat()
                except:
                    created_at = pub_date_elem.text
            
            # 获取推文内容
            description_elem = item.find("description")
            raw_text = description_elem.text if description_elem is not None else ""
            
            # 清理 HTML 标签
            text = self._clean_html(raw_text)
            
            # 构造 Twitter 原始链接
            twitter_url = f"https://twitter.com/{username}/status/{tweet_id}" if tweet_id else ""
            
            return {
                "id": tweet_id,
                "text": text,
                "username": username,
                "user_name": user_name,
                "created_at": created_at,
                "url": twitter_url,
                "nitter_url": link,
                # RSS 不提供互动数据
                "likes": 0,
                "retweets": 0,
                "replies": 0,
                "source": "nitter_rss"
            }
        
        except Exception as e:
            logger.error(f"Error parsing RSS item: {e}")
            return None
    
    def _clean_html(self, html_text: str) -> str:
        """
        清理 HTML 标签，保留纯文本
        
        Args:
            html_text: 包含 HTML 的文本
        
        Returns:
            清理后的纯文本
        """
        if not html_text:
            return ""
        
        # 解码 HTML 实体
        text = html.unescape(html_text)
        
        # 将 <br> 转换为换行
        text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
        
        # 将链接转换为 URL
        text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>.*?</a>', r'\1', text)
        
        # 移除所有其他 HTML 标签
        text = re.sub(r'<[^>]+>', '', text)
        
        # 清理多余空白
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = text.strip()
        
        return text
    
    def parse(self, raw_data: Dict[str, Any]) -> List[Dict]:
        """
        解析原始数据（已经是标准格式，直接返回）
        """
        return raw_data.get("tweets", [])
    
    # ==================== 便捷方法 ====================
    
    async def get_single_user(self, username: str, max_tweets: int = 10) -> List[Dict]:
        """
        获取单个用户的推文
        
        Args:
            username: Twitter 用户名
            max_tweets: 最大推文数
        
        Returns:
            推文列表
        """
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={"User-Agent": "Mozilla/5.0 (compatible; finradar/1.0)"}
        ) as session:
            try:
                tweets = await self._fetch_user_rss(session, username)
                return tweets[:max_tweets]
            except Exception as e:
                logger.error(f"Error fetching @{username}: {e}")
                return []
    
    def get_all_recommended_accounts(self) -> Dict[str, List[str]]:
        """获取所有推荐账号"""
        return self.RECOMMENDED_ACCOUNTS
    
    async def check_instance_health(self) -> Dict[str, Any]:
        """
        检查当前自建 Nitter 实例健康状态
        """
        results = {
            "local_instance": None,
        }

        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=5)
        ) as session:
            try:
                async with session.get(f"{self.current_instance}/VitalikButerin/rss") as response:
                    results["local_instance"] = {
                        "url": self.current_instance,
                        "status": response.status,
                        "healthy": response.status == 200,
                    }
            except Exception as e:
                results["local_instance"] = {
                    "url": self.current_instance,
                    "status": "error",
                    "healthy": False,
                    "error": str(e),
                }

        return results

    def get_instance_info(self) -> Dict[str, Any]:
        """
        获取当前实例配置信息
        
        Returns:
            当前实例的配置信息
        """
        return {
            "current_instance": self.current_instance,
            "is_local": self.using_local_instance,
            "accounts": self.accounts,
            "max_tweets_per_user": self.max_tweets_per_user,
            "timeout": self.timeout,
            "env_instance": os.environ.get("NITTER_INSTANCE", "(not set)"),
            "setup_guide": "See finradar/nitter/README.md for self-hosted setup"
        }


# ==================== 便捷函数 ====================

async def quick_fetch_tweets(usernames: List[str]) -> List[Dict]:
    """
    快速获取指定用户的推文
    
    Args:
        usernames: 用户名列表
    
    Returns:
        推文列表
    
    示例:
        tweets = await quick_fetch_tweets(["VitalikButerin", "elonmusk"])
    """
    fetcher = NitterRSSFetcher(config={"accounts": usernames})
    result = await fetcher.fetch()
    return result.get("tweets", [])
