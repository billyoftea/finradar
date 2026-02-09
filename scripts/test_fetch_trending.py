#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试热门内容获取功能（Twitter和微信）
"""

import asyncio
import sys
from datetime import datetime
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


async def test_twitter_trending():
    """测试Twitter热门推文获取"""
    print("\n" + "="*70)
    print("🐦 测试 Twitter 热门推文获取")
    print("="*70)
    
    from fin_module.fetcher.nitter_rss import NitterRSSFetcher
    from fin_module.fetcher.social_config import SocialSourceConfig
    
    # 加载配置
    config = SocialSourceConfig()
    
    if not config.twitter.enabled:
        print("⚠️ Twitter 功能未启用")
        return []
    
    print(f"📌 使用 Nitter 实例: {config.twitter.nitter_instance}")
    print(f"🔑 热门关键词: {config.twitter.trending_keywords[:3]}...")
    print(f"🎯 最大结果数: {config.twitter.trending_max_results}")
    
    # 初始化 fetcher
    fetcher = NitterRSSFetcher({
        "nitter_instance": config.twitter.nitter_instance,
        "timeout": config.twitter.timeout,
        "max_tweets_per_user": config.twitter.max_tweets_per_user
    })
    
    # 获取热门推文
    print(f"\n📊 开始抓取热门推文...")
    result = await fetcher.fetch_trending(
        keywords=config.twitter.trending_keywords,
        max_results=config.twitter.trending_max_results
    )
    
    trending_tweets = result.get("trending_tweets", [])
    print(f"✅ 成功获取 {len(trending_tweets)} 条热门推文")
    print(f"   总共找到: {result.get('total_found', 0)}")
    print(f"   去重后: {result.get('unique_count', 0)}")
    
    if result.get("errors"):
        print(f"\n⚠️ 错误信息:")
        for error in result['errors'][:3]:
            print(f"   - {error}")
    
    # 显示前10条
    print(f"\n🔥 热门推文 TOP 10:")
    print("-"*70)
    
    for i, tweet in enumerate(trending_tweets[:10], 1):
        likes = tweet.get("likes", 0)
        retweets = tweet.get("retweets", 0)
        replies = tweet.get("replies", 0)
        total = likes + retweets + replies
        username = tweet.get("username", "")
        text = tweet.get("text", "")[:80]
        keyword = tweet.get("keyword", "")
        
        print(f"\n{i}. @{username} [{keyword}]")
        print(f"   互动: 👍{likes} 🔄{retweets} 💬{replies} (总计:{total})")
        print(f"   内容: {text}...")
        if tweet.get("url"):
            print(f"   链接: {tweet['url']}")
    
    return trending_tweets


async def test_wechat_hot():
    """测试微信热门文章获取"""
    print("\n" + "="*70)
    print("📱 测试微信热门文章获取")
    print("="*70)
    
    from fin_module.fetcher.wechat_article import WechatArticleFetcher
    from fin_module.fetcher.social_config import SocialSourceConfig
    
    # 加载配置
    config = SocialSourceConfig()
    
    if not config.wechat.enabled:
        print("⚠️ 微信功能未启用")
        return []
    
    print(f"📌 微信服务地址: {config.wechat.service_url}")
    print(f"🔑 扫描分类: {config.wechat.hot_categories}")
    print(f"🎯 最大结果数: {config.wechat.hot_max_results}")
    print(f"⏰ 时间范围: 最近 {config.wechat.hot_hours_ago} 小时")
    
    # 初始化 fetcher
    fetcher = WechatArticleFetcher(
        base_url=config.wechat.service_url,
        timeout=config.wechat.timeout,
        auth_key=config.wechat.auth_key
    )
    
    # 检查服务可用性
    print(f"\n🔍 检查微信服务状态...")
    is_available = await fetcher.check_service()
    
    if not is_available:
        print("❌ 微信服务不可用")
        print("\n请先确保微信服务已启动:")
        print("  cd fin_module/wechat-article")
        print("  docker-compose up -d")
        return []
    
    print("✅ 服务可用")
    
    # 获取热门文章
    print(f"\n📊 开始抓取热门文章...")
    result = await fetcher.fetch_hot_articles(
        max_results=config.wechat.hot_max_results,
        hours_ago=config.wechat.hot_hours_ago,
        categories=config.wechat.hot_categories
    )
    
    hot_articles = result.get("hot_articles", [])
    print(f"✅ 成功获取 {len(hot_articles)} 条热门高质量文章")
    print(f"   总共扫描: {result.get('total_found', 0)} 篇文章")
    
    if result.get("errors"):
        print(f"\n⚠️ 错误信息:")
        for error in result['errors'][:5]:
            print(f"   - {error}")
    
    # 显示前10条
    print(f"\n🔥 热门文章 TOP 10:")
    print("-"*70)
    
    for i, article in enumerate(hot_articles[:10], 1):
        account = article.account_name
        title = article.title[:70]
        read = article.read_count
        like = article.like_count
        comment = article.comment_count
        score = read * 1.0 + like * 10.0 + comment * 20.0
        
        print(f"\n{i}. 【{account}】{title}")
        print(f"   热度: 📖{read:,} 👍{like} 💬{comment} (-score:{score:.0f})")
        if article.publish_time:
            print(f"   时间: {article.publish_time.strftime('%Y-%m-%d %H:%M')}")
        if article.digest:
            digest = article.digest[:100]
            print(f"   摘要: {digest}...")
    
    return hot_articles


async def main():
    """主函数"""
    print("\n" + "="*70)
    print("🚀 FinRadar 热门内容获取测试")
    print(f"⏰ 测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # 测试Twitter热门
    trending_tweets = []
    try:
        trending_tweets = await test_twitter_trending()
    except Exception as e:
        print(f"\n❌ Twitter 测试失败: {e}")
        import traceback
        traceback.print_exc()
    
    # 测试微信热门
    hot_articles = []
    try:
        hot_articles = await test_wechat_hot()
    except Exception as e:
        print(f"\n❌ 微信测试失败: {e}")
        import traceback
        traceback.print_exc()
    
    # 总结
    print("\n" + "="*70)
    print("📊 测试总结")
    print("="*70)
    print(f"✅ Twitter 热门推文: {len(trending_tweets)} 条")
    print(f"✅ 微信热门文章: {len(hot_articles)} 篇")
    print(f"\n🎉 所有测试完成!")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())
