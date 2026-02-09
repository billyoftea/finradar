#!/bin/bash
# 快速测试热门内容功能
# 用法: bash scripts/quick_test_trending.sh

echo "============================================================"
echo "🚀 finradar 快速测试热门内容功能"
echo "⏰ 时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================================"

# 1. 测试Twitter热门
echo ""
echo "📦 1️⃣  测试 Twitter 热门推文（10秒）"
echo "------------------------------------------------------------"
timeout 20 python3 -c "
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

async def test():
    from finradar.market.fetcher.nitter_rss import NitterRSSFetcher
    fetcher = NitterRSSFetcher()
    result = await fetcher.fetch_trending(keywords=['bitcoin'], max_results=5)
    tweets = result.get('trending_tweets', [])
    print(f'✅ 成功获取 {len(tweets)} 条热门推文')
    for i, t in enumerate(tweets[:3], 1):
        total = t.get('likes', 0) + t.get('retweets', 0)
        print(f'  {i}. @{t.get(\"username\")} - 互动:{total} - {t.get(\"text\")[:40]}...')

asyncio.run(test())
" 2>&1 | grep -v "INFO\|WARNING"

# 2. 测试微信热门（15秒）
echo ""
echo "📱 2️⃣  测试微信热门文章（快速模式）"
echo "------------------------------------------------------------"
timeout 30 python3 -c "
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

async def test():
    from finradar.market.fetcher.wechat_article import WechatArticleFetcher
    fetcher = WechatArticleFetcher()
    
    ok = await fetcher.check_service()
    if not ok:
        print('❌ 微信服务不可用')
        return
    
    print('✅ 微信服务可用')
    
    # 只扫描1个财经公众号测试
    hot_result = await fetcher.fetch_hot_articles(
        max_results=3,
        hours_ago=72,
        categories=['finance']
    )
    hot_articles = hot_result.get('hot_articles', [])
    print(f'✅ 成功获取 {len(hot_articles)} 条热门文章')
    for i, art in enumerate(hot_articles[:3], 1):
        score = art.read_count * 1.0 + art.like_count * 10.0 + art.comment_count * 20.0
        print(f'  {i}. 【{art.account_name}】- 热度:{score:.0f} - {art.title[:40]}...')

asyncio.run(test())
" 2>&1 | grep -E "(✅|❌|📊|1\.|2\.|3\.)" | head -10

# 总结
echo ""
echo "============================================================"
echo "✅ 快速测试完成"
echo "============================================================"
echo ""
echo "如需完整测试，请运行："
echo "  python3 scripts/test_fetch_trending.py"
echo ""
echo "如需获取完整数据，请运行："
echo "  python3 scripts/fetch_social_with_trending.py"
echo ""
