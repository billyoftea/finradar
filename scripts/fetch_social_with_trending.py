#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取社交媒体数据（包含关注账号 + 热门内容）
用于集成到finradar主流程
"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


async def fetch_twitter_data(config, report_type: str = "evening") -> Dict[str, Any]:
    """
    获取Twitter数据（关注账号 + 热门推文）
    
    Returns:
        包含普通推文和热门推文的字典
    """
    from finradar.market.fetcher.nitter_rss import NitterRSSFetcher
    
    print(f"\n🐦 获取 Twitter 数据...")
    print(f"   使用实例: {config.twitter.nitter_instance}")
    
    # 初始化fetcher
    fetcher = NitterRSSFetcher({
        "nitter_instance": config.twitter.nitter_instance,
        "timeout": config.twitter.timeout,
        "max_tweets_per_user": config.twitter.max_tweets_per_user
    })
    
    # 1. 获取关注账号的推文
    follow_accounts = config.twitter.get_all_accounts()
    print(f"   关注账号数: {len(follow_accounts)}")
    
    if follow_accounts:
        fetcher.accounts = follow_accounts[:30]  # 限制最多30个账号
        result = await fetcher.fetch()
        follow_tweets = result.get("tweets", [])
        print(f"   ✅ 关注推文: {len(follow_tweets)} 条")
    else:
        follow_tweets = []
        print(f"   ⚠️ 未配置关注账号")
    
    # 2. 获取热门推文（如果启用）
    trending_tweets = []
    if config.twitter.fetch_trending:
        print(f"   抓取热门推文...")
        trending_keywords = config.twitter.trending_keywords
        print(f"   热门关键词数: {len(trending_keywords)}")
        
        trending_result = await fetcher.fetch_trending(
            keywords=trending_keywords,
            max_results=config.twitter.trending_max_results
        )
        trending_tweets = trending_result.get("trending_tweets", [])
        print(f"   🔥 热门推文: {len(trending_tweets)} 条")
    else:
        print(f"   ⚠️ 热门推文获取未启用")
    
    # 合并数据：热门在前
    all_tweets = trending_tweets + follow_tweets
    
    return {
        "tweets": all_tweets,
        "trending_count": len(trending_tweets),
        "follow_count": len(follow_tweets),
        "timestamp": datetime.now().isoformat()
    }


async def fetch_wechat_data(config, report_type: str = "evening") -> Dict[str, Any]:
    """
    获取微信数据（关注公众号 + 热门文章）
    
    Returns:
        包含普通文章和热门文章的字典
    """
    from finradar.market.fetcher.wechat_article import WechatArticleFetcher
    
    print(f"\n📱 获取微信文章数据...")
    print(f"   服务地址: {config.wechat.service_url}")
    
    # 初始化fetcher
    fetcher = WechatArticleFetcher()
    
    # 检查服务可用性
    service_ok = await fetcher.check_service()
    if not service_ok:
        print(f"   ❌ 微信服务不可用")
        return {
            "articles": [],
            "trending_count": 0,
            "follow_count": 0,
            "error": "service_unavailable",
            "timestamp": datetime.now().isoformat()
        }
    
    print(f"   ✅ 服务可用")
    
    # 1. 获取关注公众号的文章
    follow_accounts = config.wechat.get_all_accounts()
    print(f"   关注公众号数: {len(follow_accounts)}")
    
    follow_articles = []
    if follow_accounts:
        # 限制取前20个公众号
        for i, account_name in enumerate(follow_accounts[:20]):
            try:
                accounts = await fetcher.search_accounts(account_name)
                if accounts:
                    fakeid = accounts[0].fakeid
                    articles = await fetcher.get_articles(fakeid, account_name=account_name)
                    follow_articles.extend(articles)
                    print(f"   [{i+1}/{len(follow_accounts[:20])}] {account_name}: {len(articles)} 篇")
                
                # 请求延迟
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"   ⚠️ {account_name} 获取失败: {e}")
        
        # 按时间排序，取最新的
        follow_articles.sort(key=lambda x: x.publish_time or datetime.min, reverse=True)
        follow_articles = follow_articles[:100]  # 限制最多100篇
        print(f"   ✅ 关注文章: {len(follow_articles)} 篇")
    else:
        print(f"   ⚠️ 未配置关注公众号")
    
    # 2. 获取热门文章（如果启用）
    hot_articles = []
    if config.wechat.fetch_hot_articles:
        print(f"   抓取热门文章...")
        try:
            hot_result = await fetcher.fetch_hot_articles(
                max_results=config.wechat.hot_max_results,
                hours_ago=config.wechat.hot_hours_ago,
                categories=config.wechat.hot_categories
            )
            hot_articles = hot_result.get("hot_articles", [])
            print(f"   🔥 热门文章: {len(hot_articles)} 篇")
        except Exception as e:
            print(f"   ⚠️ 热门文章获取失败: {e}")
    else:
        print(f"   ⚠️ 热门文章获取未启用")
    
    # 合并数据：热门在前
    all_articles = []
    
    # 转换热门文章为字典格式
    for art in hot_articles:
        all_articles.append({
            "title": art.title,
            "author": art.author,
            "account_name": art.account_name,
            "publish_time": art.publish_time.isoformat() if art.publish_time else "",
            "url": art.url,
            "digest": art.digest,
            "cover_url": art.cover_url,
            "read_count": art.read_count,
            "like_count": art.like_count,
            "comment_count": art.comment_count,
            "is_original": art.is_original,
            "content": art.content,
            "is_hot": True  # 标记为热门
        })
    
    # 转换普通文章为字典格式
    for art in follow_articles:
        all_articles.append({
            "title": art.title,
            "author": art.author,
            "account_name": art.account_name,
            "publish_time": art.publish_time.isoformat() if art.publish_time else "",
            "url": art.url,
            "digest": art.digest,
            "cover_url": art.cover_url,
            "read_count": art.read_count,
            "like_count": art.like_count,
            "comment_count": art.comment_count,
            "is_original": art.is_original,
            "content": art.content,
            "is_hot": False
        })
    
    return {
        "articles": all_articles,
        "trending_count": len(hot_articles),
        "follow_count": len(follow_articles),
        "timestamp": datetime.now().isoformat()
    }


async def main():
    """
    主函数：获取所有社交媒体数据
    """
    from finradar.market.fetcher.social_config import SocialSourceConfig
    
    print("\n" + "="*70)
    print("🚀 finradar 社交媒体数据获取（含热门内容）")
    print(f"⏰ 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # 加载配置
    config = SocialSourceConfig()
    
    # 确定报告类型
    report_type = "evening"
    
    # 获取Twitter数据
    twitter_data = {}
    if config.twitter.enabled:
        try:
            twitter_data = await fetch_twitter_data(config, report_type)
        except Exception as e:
            print(f"\n❌ Twitter 数据获取失败: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"\n⚠️ Twitter 功能未启用")
    
    # 获取微信数据
    wechat_data = {}
    if config.wechat.enabled:
        try:
            wechat_data = await fetch_wechat_data(config, report_type)
        except Exception as e:
            print(f"\n❌ 微信数据获取失败: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"\n⚠️ 微信功能未启用")
    
    # 组合数据
    social_data = {
        "mode": "social",
        "report_type": report_type,
        "timestamp": datetime.now().isoformat(),
        "twitter": twitter_data,
        "wechat": wechat_data
    }
    
    # 保存数据
    output_dir = Path(__file__).parent.parent / "output" / "market"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    date_str = datetime.now().strftime("%Y%m%d")
    output_path = output_dir / f"market_data_{date_str}_{report_type}.json"
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(social_data, f, ensure_ascii=False, indent=2)
    
    # 打印总结
    print("\n" + "="*70)
    print("📊 数据获取完成")
    print("="*70)
    print(f"Twitter:")
    print(f"   关注推文: {twitter_data.get('follow_count', 0)} 条")
    print(f"   热门推文: {twitter_data.get('trending_count', 0)} 条")
    print(f"   总计: {len(twitter_data.get('tweets', []))} 条")
    print(f"微信:")
    print(f"   关注文章: {wechat_data.get('follow_count', 0)} 篇")
    print(f"   热门文章: {wechat_data.get('trending_count', 0)} 篇")
    print(f"   总计: {len(wechat_data.get('articles', []))} 篇")
    print(f"\n✅ 数据已保存: {output_path}")
    print("="*70)
    
    return social_data


if __name__ == "__main__":
    asyncio.run(main())
