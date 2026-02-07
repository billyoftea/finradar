# 📊 FinRadar 每日数据抓取指南

## 快速开始

### 一键抓取所有数据（推荐）

```bash
./fetch-all.sh
```

这将抓取：
- 📊 金融市场数据（A股、贵金属、加密货币、期货、GitHub）
- 🐦 Twitter 动态
- 📱 微信公众号文章
- 🔥 TrendRadar 热榜新闻

---

## 分模块抓取

### 仅抓取 Twitter

```bash
./fetch-all.sh -t
# 或
./fetch-all.sh --twitter
```

### 仅抓取微信公众号

```bash
./fetch-all.sh -w
# 或
./fetch-all.sh --wechat
```

### 仅抓取金融市场

```bash
./fetch-all.sh -m
# 或
./fetch-all.sh --market
```

### 仅抓取热榜新闻

```bash
./fetch-all.sh -r
# 或
./fetch-all.sh --trendradar
```

### 组合抓取

```bash
# Twitter + 微信公众号
./fetch-all.sh -t -w

# 金融市场 + Twitter
./fetch-all.sh -m -t

# Twitter + 微信 + 市场
./fetch-all.sh -t -w -m
```

---

## 输出文件位置

所有抓取的数据都保存在 `output/` 目录下：

```
output/
├── market/                              # 金融市场数据
│   ├── market_report_20260204.txt       # 文本报告
│   └── market_data_20260204.json        # JSON 数据
├── twitter/                             # Twitter 数据
│   └── tweets_20260204_0643.json        # 推文数据
├── wechat/                              # 微信公众号数据
│   └── articles_20260204_0645.json      # 文章数据
└── news/                                # TrendRadar 数据
    └── 2026-02-04.db                    # SQLite 数据库
```

---

## 定时任务配置

### 使用 crontab 设置定时抓取

```bash
# 编辑 crontab
crontab -e

# 添加以下行（每天早上 8:00 抓取所有数据）
0 8 * * * cd /home/ubuntu/finradar && ./fetch-all.sh >> /tmp/finradar-cron.log 2>&1

# 或者每小时抓取一次
0 * * * * cd /home/ubuntu/finradar && ./fetch-all.sh >> /tmp/finradar-cron.log 2>&1

# 仅在工作日的工作时间抓取（周一到周五，9:00-18:00 每小时）
0 9-18 * * 1-5 cd /home/ubuntu/finradar && ./fetch-all.sh >> /tmp/finradar-cron.log 2>&1
```

### 查看定时任务日志

```bash
tail -f /tmp/finradar-cron.log
```

---

## Python 直接调用

如果你想在 Python 代码中调用：

```python
import asyncio
from scripts.daily_fetch import DailyFetcher

async def main():
    fetcher = DailyFetcher()
    
    # 抓取所有数据
    await fetcher.fetch_market_data()
    await fetcher.fetch_twitter()
    await fetcher.fetch_wechat()
    await fetcher.fetch_trendradar()
    
    # 打印摘要
    fetcher.print_summary()

asyncio.run(main())
```

### 仅抓取 Twitter

```python
import asyncio
from fin_module.fetcher.nitter_rss import NitterRSSFetcher

async def main():
    fetcher = NitterRSSFetcher()
    data = await fetcher.fetch()
    
    print(f"抓取到 {len(data['tweets'])} 条推文")
    for tweet in data['tweets'][:5]:
        print(f"@{tweet['username']}: {tweet['text'][:50]}...")

asyncio.run(main())
```

### 仅抓取微信公众号

```python
import asyncio
from fin_module.fetcher.wechat_article import WechatArticleFetcher

async def main():
    fetcher = WechatArticleFetcher(config={
        "service_url": "http://172.31.42.175:3001",
        "auth_key": "你的auth_key"
    })
    
    # 搜索公众号
    accounts = await fetcher.search_accounts("财联社", limit=1)
    
    if accounts:
        # 获取文章
        articles = await fetcher.get_articles(accounts[0].fakeid, count=10)
        print(f"抓取到 {len(articles)} 篇文章")
        
        for art in articles:
            print(f"[{art.author}] {art.title}")
    
    await fetcher.close()

asyncio.run(main())
```

---

## 故障排查

### Twitter 抓取失败 (HTTP 429)

**原因**：速率限制

**解决方案**：
1. 更新 Twitter Token：`./scripts/update-twitter-token.sh`
2. 减少配置的账号数量
3. 增加请求延迟（编辑 `config/config.yaml`，添加 `request_delay: 2.0`）

### 微信公众号抓取失败

**原因**：Auth Key 过期（约 4 天有效期）

**解决方案**：
1. 访问 `http://你的服务器IP:3001` 重新登录
2. 更新 Auth Key：`./scripts/update-wechat-key.sh`

### TrendRadar 运行失败

**原因**：可能是配置问题或依赖问题

**解决方案**：
1. 检查 `config/config.yaml` 配置
2. 单独运行测试：`python -m trendradar`
3. 查看详细错误日志

---

## 配置文件

主配置文件位于 `config/config.yaml`，可以修改：

- Twitter 账号列表：`twitter.accounts`
- 微信公众号列表：`wechat.accounts`
- 时间过滤设置：`wechat.max_age_hours`（默认 24 小时）
- 是否抓取全文：`wechat.fetch_content`

---

## 高级用法

### 仅抓取最近 12 小时的微信文章

编辑 `config/config.yaml`：

```yaml
wechat:
  max_age_hours: 12  # 改为 12 小时
```

### 禁用某个数据源

编辑 `config/config.yaml`：

```yaml
twitter:
  enabled: false  # 禁用 Twitter 抓取

wechat:
  enabled: false  # 禁用微信抓取
```

### 调整请求延迟（避免限流）

编辑 `config/config.yaml`：

```yaml
twitter:
  request_delay: 2.0  # 每个账号之间间隔 2 秒

wechat:
  content_delay: 1.0  # 每篇文章之间间隔 1 秒
```

---

## 数据格式说明

### Twitter 数据格式

```json
{
  "timestamp": "2026-02-04T06:43:05.123456",
  "instance": "http://172.31.42.175:8080",
  "tweets": [
    {
      "id": "1234567890",
      "username": "elonmusk",
      "user_name": "Elon Musk",
      "text": "推文内容...",
      "created_at": "2026-02-04T06:30:00+00:00",
      "url": "https://twitter.com/elonmusk/status/1234567890"
    }
  ],
  "errors": []
}
```

### 微信公众号数据格式

```json
{
  "timestamp": "2026-02-04T06:45:00.123456",
  "articles": [
    {
      "title": "文章标题",
      "author": "作者",
      "account_name": "公众号名称",
      "publish_time": "2026-02-04T06:00:00",
      "url": "https://mp.weixin.qq.com/s/xxxxx",
      "digest": "文章摘要",
      "content": "文章全文（如果启用了全文抓取）"
    }
  ]
}
```

---

## 获取帮助

```bash
./fetch-all.sh --help
```

或查看源代码：
- Shell 脚本：`fetch-all.sh`
- Python 脚本：`scripts/daily_fetch.py`
- Twitter 抓取器：`fin_module/fetcher/nitter_rss.py`
- 微信抓取器：`fin_module/fetcher/wechat_article.py`
