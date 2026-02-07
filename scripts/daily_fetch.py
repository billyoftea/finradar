#!/usr/bin/env python
# coding=utf-8
"""
FinRadar 每日数据抓取脚本

一键抓取所有数据源：
- 📊 金融市场数据（A股、贵金属、加密货币、期货）
- 🐦 Twitter/X 动态
- 📱 微信公众号文章
- 🔥 TrendRadar 热榜新闻

使用方法:
    # 抓取所有数据
    python scripts/daily_fetch.py
    
    # 或指定模块
    python scripts/daily_fetch.py --market      # 仅金融市场
    python scripts/daily_fetch.py --twitter     # 仅 Twitter
    python scripts/daily_fetch.py --wechat      # 仅微信公众号
    python scripts/daily_fetch.py --trendradar  # 仅热榜新闻
    
    # 组合使用
    python scripts/daily_fetch.py --twitter --wechat  # Twitter + 微信
"""

import asyncio
import argparse
import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path

# 添加项目根目录到 path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DailyFetcher:
    """每日数据抓取器"""
    
    def __init__(self):
        self.results = {}
        self.errors = []
        self.output_dir = PROJECT_ROOT / "output"
        self.output_dir.mkdir(exist_ok=True)
        
    async def fetch_market_data(self) -> dict:
        """抓取金融市场数据（A股、贵金属、加密货币、期货、GitHub）"""
        print("\n" + "=" * 60)
        print("📊 开始抓取金融市场数据...")
        print("=" * 60)
        
        try:
            from fin_module import MarketTracker
            
            tracker = MarketTracker()
            await tracker.fetch_all()
            
            # 保存报告
            market_dir = self.output_dir / "market"
            market_dir.mkdir(exist_ok=True)
            tracker.save_report(str(market_dir))
            
            self.results["market"] = {
                "success": True,
                "data": tracker.results,
                "errors": tracker.errors
            }
            
            print(f"✅ 金融市场数据抓取完成")
            return tracker.results
            
        except Exception as e:
            logger.error(f"❌ 金融市场数据抓取失败: {e}")
            self.errors.append(f"market: {e}")
            self.results["market"] = {"success": False, "error": str(e)}
            return {}
    
    async def fetch_twitter(self) -> dict:
        """抓取 Twitter 数据"""
        print("\n" + "=" * 60)
        print("🐦 开始抓取 Twitter 数据...")
        print("=" * 60)
        
        try:
            from fin_module.fetcher.nitter_rss import NitterRSSFetcher
            
            fetcher = NitterRSSFetcher()
            print(f"   使用实例: {fetcher.current_instance}")
            print(f"   账号数量: {len(fetcher.accounts)}")
            
            data = await fetcher.fetch()
            
            # 保存数据
            twitter_file = self.output_dir / "twitter" / f"tweets_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            twitter_file.parent.mkdir(exist_ok=True)
            
            with open(twitter_file, "w", encoding="utf-8") as f:
                json.dump({
                    "timestamp": datetime.now().isoformat(),
                    "instance": data.get("instance_used", ""),
                    "tweets": data.get("tweets", []),
                    "errors": data.get("errors", [])
                }, f, ensure_ascii=False, indent=2, default=str)
            
            tweet_count = len(data.get("tweets", []))
            error_count = len(data.get("errors", []))
            
            self.results["twitter"] = {
                "success": True,
                "tweet_count": tweet_count,
                "error_count": error_count,
                "file": str(twitter_file)
            }
            
            print(f"✅ Twitter 抓取完成: {tweet_count} 条推文, {error_count} 个错误")
            print(f"   保存到: {twitter_file}")
            
            # 显示最新几条推文
            if data.get("tweets"):
                print("\n   📌 最新推文预览:")
                for tweet in data["tweets"][:3]:
                    text = tweet.get("text", "")[:50]
                    print(f"      @{tweet.get('username', '?')}: {text}...")
            
            return data
            
        except Exception as e:
            logger.error(f"❌ Twitter 抓取失败: {e}")
            self.errors.append(f"twitter: {e}")
            self.results["twitter"] = {"success": False, "error": str(e)}
            return {}
    
    async def fetch_wechat(self) -> dict:
        """抓取微信公众号文章"""
        print("\n" + "=" * 60)
        print("📱 开始抓取微信公众号文章...")
        print("=" * 60)
        
        try:
            from fin_module.fetcher.wechat_article import WechatArticleFetcher
            from fin_module.fetcher.social_config import SocialSourceConfig
            
            # 加载配置
            config = SocialSourceConfig()
            wechat_conf = config.wechat
            
            if not wechat_conf.enabled:
                print("⚠️ 微信公众号抓取已禁用")
                self.results["wechat"] = {"success": False, "error": "disabled"}
                return {}
            
            print(f"   服务地址: {wechat_conf.service_url}")
            print(f"   时间范围: 过去 {wechat_conf.max_age_hours} 小时")
            print(f"   抓取全文: {'是' if wechat_conf.fetch_content else '否'}")
            
            fetcher = WechatArticleFetcher(
                base_url=wechat_conf.service_url,
                auth_key=wechat_conf.auth_key,
                timeout=wechat_conf.timeout
            )
            
            # 获取所有配置的公众号
            all_accounts = wechat_conf.get_all_accounts()
            print(f"   公众号数量: {len(all_accounts)}")
            
            from datetime import timedelta
            cutoff_time = datetime.now() - timedelta(hours=wechat_conf.max_age_hours) if wechat_conf.max_age_hours > 0 else None
            
            all_articles = []
            success_count = 0
            
            for account_name in all_accounts[:15]:  # 限制数量
                try:
                    print(f"   正在抓取: {account_name}...", end=" ")
                    accounts = await fetcher.search_accounts(account_name, limit=1)
                    if accounts:
                        # 先获取文章列表（不含全文）
                        articles = await fetcher.get_articles(
                            accounts[0].fakeid,
                            count=wechat_conf.max_articles_per_account
                        )
                        for art in articles:
                            art.account_name = account_name
                        
                        # ⚠️ 关键：先时间过滤，再抓取全文
                        if cutoff_time:
                            articles = [a for a in articles if a.publish_time and a.publish_time >= cutoff_time]
                        
                        # 如果启用全文抓取，对过滤后的文章抓取全文
                        if wechat_conf.fetch_content and articles:
                            print(f"过滤后 {len(articles)} 篇，", end="")
                            for i, art in enumerate(articles, 1):
                                try:
                                    content = await fetcher.get_article_content(art.url)
                                    art.content = content
                                    print(f"\r   正在抓取: {account_name}... 过滤后 {len(articles)} 篇，抓取全文 [{i}/{len(articles)}]", end="", flush=True)
                                    if i < len(articles):
                                        await asyncio.sleep(wechat_conf.content_delay)
                                except Exception as e:
                                    logger.debug(f"获取文章全文失败 {art.title}: {e}")
                        
                        all_articles.extend(articles)
                        success_count += 1
                        print(f"\r   正在抓取: {account_name}... ✓ {len(articles)} 篇（24h内）")
                    else:
                        print("✗ 未找到")
                except Exception as e:
                    print(f"✗ {e}")
                    
                # 添加延迟避免限流
                await asyncio.sleep(0.5)
            
            await fetcher.close()
            
            # 按时间排序
            all_articles.sort(key=lambda x: x.publish_time if x.publish_time else datetime.min, reverse=True)
            
            # 保存数据
            wechat_file = self.output_dir / "wechat" / f"articles_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            wechat_file.parent.mkdir(exist_ok=True)
            
            with open(wechat_file, "w", encoding="utf-8") as f:
                json.dump({
                    "timestamp": datetime.now().isoformat(),
                    "articles": [
                        {
                            "title": a.title,
                            "author": a.author,
                            "account_name": a.account_name,
                            "publish_time": a.publish_time.isoformat() if a.publish_time else "",
                            "url": a.url,
                            "digest": a.digest,
                            "content": a.content if hasattr(a, 'content') and a.content else ""
                        } for a in all_articles[:100]
                    ]
                }, f, ensure_ascii=False, indent=2)
            
            self.results["wechat"] = {
                "success": True,
                "article_count": len(all_articles),
                "account_success": success_count,
                "file": str(wechat_file)
            }
            
            print(f"\n✅ 微信公众号抓取完成: {len(all_articles)} 篇文章")
            print(f"   保存到: {wechat_file}")
            
            # 显示最新文章
            if all_articles:
                print("\n   📌 最新文章预览:")
                for art in all_articles[:3]:
                    print(f"      [{art.account_name}] {art.title[:40]}...")
            
            return {"articles": all_articles}
            
        except Exception as e:
            logger.error(f"❌ 微信公众号抓取失败: {e}")
            self.errors.append(f"wechat: {e}")
            self.results["wechat"] = {"success": False, "error": str(e)}
            return {}
    
    async def fetch_trendradar(self) -> dict:
        """运行 TrendRadar 热榜抓取"""
        print("\n" + "=" * 60)
        print("🔥 开始运行 TrendRadar 热榜抓取...")
        print("=" * 60)
        
        try:
            # TrendRadar 使用同步代码，在线程中运行
            import subprocess
            
            result = subprocess.run(
                [sys.executable, "-m", "trendradar"],
                cwd=str(PROJECT_ROOT),
                capture_output=True,
                text=True,
                timeout=300  # 5分钟超时
            )
            
            if result.returncode == 0:
                self.results["trendradar"] = {"success": True}
                print("✅ TrendRadar 热榜抓取完成")
                # 显示部分输出
                if result.stdout:
                    lines = result.stdout.strip().split('\n')
                    for line in lines[-10:]:  # 显示最后10行
                        print(f"   {line}")
            else:
                self.results["trendradar"] = {"success": False, "error": result.stderr}
                print(f"❌ TrendRadar 运行失败")
                if result.stderr:
                    print(f"   错误: {result.stderr[:200]}")
                    
            return self.results.get("trendradar", {})
            
        except subprocess.TimeoutExpired:
            logger.error("❌ TrendRadar 运行超时")
            self.errors.append("trendradar: timeout")
            self.results["trendradar"] = {"success": False, "error": "timeout"}
            return {}
        except Exception as e:
            logger.error(f"❌ TrendRadar 运行失败: {e}")
            self.errors.append(f"trendradar: {e}")
            self.results["trendradar"] = {"success": False, "error": str(e)}
            return {}
    
    def print_summary(self):
        """打印抓取摘要"""
        print("\n" + "=" * 60)
        print("📋 抓取摘要")
        print("=" * 60)
        
        for module, result in self.results.items():
            if result.get("success"):
                status = "✅"
                details = []
                if "tweet_count" in result:
                    details.append(f"{result['tweet_count']} 条推文")
                if "article_count" in result:
                    details.append(f"{result['article_count']} 篇文章")
                if "file" in result:
                    details.append(f"→ {Path(result['file']).name}")
                detail_str = ", ".join(details) if details else "完成"
                print(f"  {status} {module}: {detail_str}")
            else:
                error = result.get("error", "unknown error")
                print(f"  ❌ {module}: {error[:50]}")
        
        print("=" * 60)
        print(f"📅 完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)


async def main():
    parser = argparse.ArgumentParser(
        description="FinRadar 每日数据抓取",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python scripts/daily_fetch.py                 # 抓取所有数据
  python scripts/daily_fetch.py --twitter       # 仅 Twitter
  python scripts/daily_fetch.py --wechat        # 仅微信公众号
  python scripts/daily_fetch.py --market        # 仅金融市场
  python scripts/daily_fetch.py --trendradar    # 仅热榜新闻
  python scripts/daily_fetch.py -t -w           # Twitter + 微信
        """
    )
    
    parser.add_argument("-m", "--market", action="store_true", help="抓取金融市场数据")
    parser.add_argument("-t", "--twitter", action="store_true", help="抓取 Twitter 数据")
    parser.add_argument("-w", "--wechat", action="store_true", help="抓取微信公众号文章")
    parser.add_argument("-r", "--trendradar", action="store_true", help="运行 TrendRadar 热榜抓取")
    parser.add_argument("-a", "--all", action="store_true", help="抓取所有数据（默认）")
    
    args = parser.parse_args()
    
    # 如果没有指定任何模块，则抓取所有
    fetch_all = args.all or not (args.market or args.twitter or args.wechat or args.trendradar)
    
    print("=" * 60)
    print("🚀 FinRadar 每日数据抓取")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    fetcher = DailyFetcher()
    
    # 按顺序执行抓取
    if fetch_all or args.market:
        await fetcher.fetch_market_data()
    
    if fetch_all or args.twitter:
        await fetcher.fetch_twitter()
    
    if fetch_all or args.wechat:
        await fetcher.fetch_wechat()
    
    if fetch_all or args.trendradar:
        await fetcher.fetch_trendradar()
    
    # 打印摘要
    fetcher.print_summary()
    
    # 返回是否全部成功
    all_success = all(r.get("success", False) for r in fetcher.results.values())
    return 0 if all_success else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
