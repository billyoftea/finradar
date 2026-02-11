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
from datetime import datetime
from typing import Dict, Any, List, Optional
from zoneinfo import ZoneInfo

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
        self.config = config or {}
        self.results: Dict[str, Any] = {}
        self.errors: List[str] = []
        self.fetch_timeout = float(
            os.environ.get("MARKET_FETCH_TIMEOUT", self.config.get("fetch_timeout", 120))
        )
        self.module_timeouts = self.config.get("module_timeouts", {}) or {}
        # 微信全文抓取较慢，单独给更长默认超时，避免“看起来失败但其实还在正常抓取”。
        self.module_timeouts.setdefault("wechat", float(os.environ.get("WECHAT_FETCH_TIMEOUT", 1800)))

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
                "trending_engagement_threshold": twitter_conf.trending_engagement_threshold,
            }
            
            fetcher = NitterRSSFetcher(config)
            if fetcher.enabled:
                max_age_hours = twitter_conf.max_age_hours
                logger.info(f"🐦 正在抓取 Twitter 热点 (实例: {twitter_conf.nitter_instance}, 时间范围: {max_age_hours}小时)...")
                logger.info(f"   关注账号: {len(config['accounts'])} 个")
                follow_result = await fetcher.fetch()
                follow_tweets = follow_result.get("tweets", []) or []
                for item in follow_tweets:
                    if isinstance(item, dict):
                        item.setdefault("is_trending", False)

                trending_tweets = []
                trending_errors = []
                if twitter_conf.fetch_trending:
                    keywords = twitter_conf.trending_keywords or None
                    logger.info(f"   热门关键词: {len(keywords or [])} 个")
                    trending_result = await fetcher.fetch_trending(
                        keywords=keywords,
                        max_results=twitter_conf.trending_max_results
                    )
                    trending_errors = trending_result.get("errors", []) or []
                    for item in trending_result.get("trending_tweets", []) or []:
                        if not isinstance(item, dict):
                            continue
                        engagement = item.get("likes", 0) + item.get("retweets", 0) + item.get("replies", 0)
                        if engagement < twitter_conf.trending_engagement_threshold:
                            continue
                        item["is_trending"] = True
                        trending_tweets.append(item)
                else:
                    logger.info("   热门推文抓取已禁用")

                # 合并去重：热门优先，随后是关注账号
                merged = []
                seen = set()
                for tweet in trending_tweets + follow_tweets:
                    if not isinstance(tweet, dict):
                        continue
                    dedup_key = tweet.get("id") or tweet.get("url") or f"{tweet.get('username','')}::{tweet.get('text','')[:120]}"
                    if dedup_key in seen:
                        continue
                    seen.add(dedup_key)
                    merged.append(tweet)

                # 按时间过滤推文（与微信一致的 12 小时窗口）
                if max_age_hours > 0 and merged:
                    from datetime import timedelta, timezone
                    cutoff_time = datetime.now().astimezone() - timedelta(hours=max_age_hours)

                    before_count = len(merged)
                    filtered_tweets = []
                    for tweet in merged:
                        created_at = tweet.get("created_at", "")
                        if not created_at:
                            filtered_tweets.append(tweet)
                            continue

                        try:
                            dt_text = str(created_at).replace("Z", "+00:00")
                            tweet_time = datetime.fromisoformat(dt_text)
                            if tweet_time.tzinfo is None:
                                tweet_time = tweet_time.replace(tzinfo=timezone.utc)
                            if tweet_time.astimezone(cutoff_time.tzinfo) >= cutoff_time:
                                filtered_tweets.append(tweet)
                        except (ValueError, TypeError):
                            filtered_tweets.append(tweet)

                    merged = filtered_tweets
                    logger.info(f"   时间过滤: {before_count}条 → {len(merged)}条 (过去{max_age_hours}小时内)")

                # 按创建时间排序（热门搜索结果没有原始时间，保留其当前位置）
                merged.sort(key=lambda x: x.get("created_at", ""), reverse=True)

                logger.info(
                    "✅ Twitter 数据抓取完成，共 %s 条 (关注: %s, 热门: %s)",
                    len(merged), len(follow_tweets), len(trending_tweets)
                )
                return {
                    "tweets": merged,
                    "follow_tweets_count": len(follow_tweets),
                    "trending_tweets_count": len(trending_tweets),
                    "trending_errors": trending_errors,
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
            
            # 检查服务是否可用
            if not await fetcher.check_service():
                logger.warning("⚠️ 微信公众号服务不可用")
                self.errors.append("微信公众号服务不可用 (请检查 wechat-article-exporter 服务)")
                await fetcher.close()
                return None
            
            fetch_content = wechat_conf.fetch_content
            max_age_hours = wechat_conf.max_age_hours
            logger.info(f"📱 正在抓取微信公众号文章 (服务: {wechat_conf.service_url}, 时间范围: {max_age_hours}小时, 抓取全文: {'是' if fetch_content else '否'})...")
            
            # 计算时间截止点
            from datetime import timedelta
            cutoff_time = datetime.now() - timedelta(hours=max_age_hours) if max_age_hours > 0 else None
            
            # 获取所有配置的公众号
            all_accounts = wechat_conf.get_all_accounts()
            logger.info(f"   配置的公众号: {len(all_accounts)} 个")
            
            all_articles = []
            for account_name in all_accounts[:10]:  # 限制数量避免太慢
                try:
                    # 先搜索公众号获取 fakeid
                    accounts = await fetcher.search_accounts(account_name, limit=1)
                    if accounts:
                        # 先获取文章列表（不含全文）
                        articles = await fetcher.get_articles(
                            accounts[0].fakeid, 
                            count=wechat_conf.max_articles_per_account
                        )
                        # 添加公众号名称
                        for art in articles:
                            art.account_name = account_name
                        
                        # ⚠️ 关键：先时间过滤，再抓取全文
                        if cutoff_time:
                            before_filter = len(articles)
                            articles = [a for a in articles if a.publish_time and a.publish_time >= cutoff_time]
                            logger.info(f"   {account_name}: {before_filter}篇 → 过滤后{len(articles)}篇({max_age_hours}h内)")
                        
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

            # 微信热门文章（跨账号维度）
            hot_articles = []
            hot_errors = []
            if wechat_conf.fetch_hot_articles:
                logger.info("🔥 正在抓取微信公众号热门文章...")
                hot_result = await fetcher.fetch_hot_articles(
                    max_results=wechat_conf.hot_max_results,
                    hours_ago=wechat_conf.hot_hours_ago,
                    categories=wechat_conf.hot_categories or None
                )
                hot_errors = hot_result.get("errors", []) or []
                hot_articles = hot_result.get("hot_articles", []) or []

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
            await fetcher.close()
            
            return {
                "articles": merged_articles[:80],
                "follow_articles_count": len(all_articles),
                "hot_articles_count": len(hot_articles),
                "hot_errors": hot_errors,
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
          - "market": 仅金融市场 (A股/贵金属/加密货币/期货/GitHub)
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
        
        return self.results
    
    def generate_report(self) -> str:
        """生成市场日报"""
        report_lines = []
        now = datetime.now(BEIJING_TZ)
        
        report_lines.append("=" * 50)
        report_lines.append(f"📊 每日市场追踪报告")
        report_lines.append(f"📅 {now.strftime('%Y年%m月%d日 %H:%M')}")
        report_lines.append("=" * 50)
        
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
            if pm_data.get("gold"):
                gold = pm_data["gold"]
                report_lines.append(f"  🪙 黄金: ${gold.get('price', 0):.2f} ({gold.get('change_pct', 0):+.2f}%)")
            if pm_data.get("silver"):
                silver = pm_data["silver"]
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
            if futures_data.get("commodities"):
                for item in futures_data["commodities"][:5]:
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
