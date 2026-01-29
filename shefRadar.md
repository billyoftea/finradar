我现在想基于SHEFerRadar项目，写一个每日追踪最新大盘和板块的agent，计划包括以下几个板块：
1.大盘情况：
    上证指数的涨跌，沪深300的涨跌
    成交量、国家队情况、北上资金、主力流向
    上涨的股票/下跌股票的比例

2.分版块情况，按照统一的板块标准的涨跌情况。此外，我特别关注科技股、周期股、农业股，需要重点说明这三个大类的情况

3.黄金、白银的涨跌

4.比特币、以太坊的涨跌，以及一些最近比较火的meme币

5.期货市场

6.twitter比较火的项目解析

7.github上热门项目解析


在除了目前的newsnow外，还要增加一些其他的信息源：

信息源：
新闻：财联社
金融数据：ths，金价、银价，yahoo finance
twitter：补充国外政要和web3的最新动态

• 大盘/板块：ifind。。。、东方财富API（北上/主力流）、AkShare库。​
• 黄金/白银：Yahoo Finance API或Investing.com。
• 比特币/meme币：CoinGecko免费API（ETH、SOL、DOGE等日涨跌）。
• 期货：Wind API或CFFEX官网。
Twitter火项目：Twitter API v2（trends endpoint）或LunarCrush（crypto社交热度）。


让我再查看一下项目的整体架构和相关文件，以便制定更详细的推进计划。 

读取 [](file:///c%3A/Users/Lenovo/Desktop/SHEFerRadar/SHEFerRadar/core/data.py#1-1)，行 1 到 150

读取 [](file:///c%3A/Users/Lenovo/Desktop/SHEFerRadar/SHEFerRadar/storage/base.py#1-1)，行 1 到 100

基于您的 shefAgent.md 和 SHEFerRadar 的现有架构，我为您制定了一个分阶段的推进计划：

---

## 📋 **项目推进计划：Financial SHEFerRadar Agent**

### 🎯 **项目定位**
基于 SHEFerRadar 的成熟架构，构建一个**金融市场数据追踪和智能分析 Agent**，覆盖股票、加密货币、大宗商品、期货等多维度金融数据，并提供 AI 深度分析报告。

---

## 📅 **分阶段实施计划**

---

### **阶段 1：基础设施搭建（1-2 周）**

#### 目标
建立新模块的基础架构，复用 SHEFerRadar 的存储、通知、AI 分析能力。

#### 任务清单

**1.1 创建新模块目录结构**
```
SHEFerRadar/finance/
├── __init__.py
├── market/                    # 市场数据爬取
│   ├── __init__.py
│   ├── stock.py              # 股票市场（大盘/板块）
│   ├── crypto.py             # 加密货币
│   ├── futures.py            # 期货
│   └── commodities.py        # 大宗商品（黄金白银）
├── social/                    # 社交媒体数据
│   ├── __init__.py
│   ├── twitter.py            # Twitter 热门项目
│   └── github.py             # GitHub 热门项目
└── analysis/                  # 金融数据分析
    ├── __init__.py
    ├── analyzer.py           # 市场数据分析器
    └── formatter.py          # 数据格式化
```

**1.2 扩展数据模型**
在 base.py 中添加新数据模型：
```python
@dataclass
class MarketItem:
    """市场行情数据"""
    symbol: str               # 代码
    name: str                  # 名称
    price: float               # 价格
    change: float              # 涨跌额
    change_percent: float      # 涨跌幅 (%)
    volume: float              # 成交量
    time: str                  # 数据时间
    
@dataclass
class CryptoItem:
    """加密货币数据"""
    symbol: str
    name: str
    price: float
    change_24h: float
    market_cap: float
    volume_24h: float
```

**1.3 创建配置文件**
```
config/finance.yaml          # 金融数据配置
config/finance_prompt.txt    # AI 分析提示词
```

**1.4 安装依赖库**
在 requirements.txt 中添加：
```
akshare>=1.12.0             # A股数据
yfinance>=0.2.0             # Yahoo Finance
pycoingecko>=3.1.0          # CoinGecko API
tweepy>=4.14.0              # Twitter API
```

**验收标准**
- ✅ 目录结构创建完成
- ✅ 新数据模型定义完成
- ✅ 配置文件骨架创建完成
- ✅ 依赖包可以正常安装

---

### **阶段 2：A股数据模块（2-3 周）**

#### 目标
实现 A 股大盘、板块的实时数据获取和存储。

#### 任务清单

**2.1 大盘数据获取** (`market/stock.py`)
```python
功能点：
- 上证指数、沪深300实时数据
- 成交量统计
- 北向资金净流入
- 主力资金流向
- 涨停家数 / 跌停家数比例

数据源：
- AkShare: ak.stock_zh_index_spot()
- 东方财富 API
```

**2.2 板块数据获取**
```python
功能点：
- 统一板块标准（申万/中信行业）
- 科技股板块追踪（电子、计算机、通信）
- 周期股板块追踪（钢铁、煤炭、有色金属）
- 农业股板块追踪

数据源：
- AkShare: ak.stock_board_industry_name_em()
```

**2.3 数据存储扩展**
扩展现有 base.py，支持市场数据 CRUD：
- 添加 `save_market_data()` 方法
- 添加 `get_market_today()` 方法
- 添加 `get_market_history()` 方法

**2.4 数据可视化配置**
在 HTML 报告中添加：
- 涨跌分布饼图
- 板块涨跌幅柱状图
- 大盘走势折线图

**验收标准**
- ✅ 能正确获取上证指数、沪深300实时数据
- ✅ 能正确获取板块涨跌数据
- ✅ 数据能存入 SQLite 数据库
- ✅ HTML 报告能正确展示图表

---

### **阶段 3：加密货币模块（1-2 周）**

#### 目标
实现主流加密货币和热门 meme 币数据的追踪。

#### 任务清单

**3.1 主流币种数据** (`market/crypto.py`)
```python
功能点：
- 比特币 (BTC)
- 以太坊 (ETH)
- Solana (SOL)

数据源：
- CoinGecko API: /coins/markets
- yfinance (备选)
```

**3.2 Meme 币热榜**
```python
功能点：
- DOGE, SHIB, PEPE 等热门 meme 币价格
- 24小时涨跌幅排名
- 社交热度综合评分

数据来源：
- CoinGecko: /coins/markets vs_currency=usd category=meme
- LunarCrush API (社交热度)
```

**3.3 数据推送格式化**
设计推送模板：
```
🚀 #加密货币今日观察

💰 主流币种
BTC: $xxx (+x.xx%)
ETH: $xxx (+x.xx%)

🔥 Meme 币热榜
1. DOGE: +x.xx%
2. SHIB: +x.xx%
```

**验收标准**
- ✅ 能获取 BTC/ETH 实时价格
- ✅ 能获取 Meme 币排名
- ✅ 数据能纳入现有推送体系

---

### **阶段 4：大宗商品与期货（1 周）**

#### 目标
实现黄金、白银及期货市场数据追踪。

#### 任务清单

**4.1 大宗商品数据** (`market/commodities.py`)
```python
功能点：
- 黄金实时价格（美元/盎司）
- 白银实时价格
- 人民币金价换算

数据来源：
- Yahoo Finance: GC=F (黄金), SI=F (白银)
- Investing.com API
```

**4.2 期货数据** (`market/futures.py`)
```python
功能点：
- 主要期货品种行情
- 螺纹钢、铁矿石等黑色系
- 原油、橡胶等能化系

数据来源：
- AkShare 期货接口
- Wind API (如有权限)
```

**验收标准**
- ✅ 黄金白银价格实时更新
- ✅ 期货数据能正常获取
- ✅ 数据展示格式统一

---

### **阶段 5：社交媒体数据（2 周）**

#### 目标
集成 Twitter 和 GitHub 的热点数据，捕捉市场情绪和新兴趋势。

#### 任务清单

**5.1 Twitter 热门项目** (`social/twitter.py`)
```python
功能点：
- 政治/经济要人动态
- Web3 项目热度趋势
- Crypto 社区情绪指标

数据来源：
- Twitter API v2: /2/trends
- LunarCrush (社交媒体热度分析)
```

**5.2 GitHub 热门项目** (`social/github.py`)
```python
功能点：
- Trending Repositories
- 区块链/AI 相关项目
- Web3 开发者活跃度指标

数据来源：
- GitHub API: /search/repositories (按 stars 排序)
```

**5.3 数据筛选逻辑**
- 关键词匹配（`web3`, `crypto`, `blockchain`, `ai`, `llm`）
- 星标数过滤（如 stars > 1000）
- 时间范围过滤（最近一周）

**验收标准**
- ✅ Twitter API 能正常调用
- ✅ GitHub Trending 能正常获取
- ✅ 能按关键词筛选相关项目

---

### **阶段 6：AI 分析能力扩展（2 周）**

#### 目标
基于金融数据特点，定制 AI 分析模型和提示词。

#### 任务清单

**6.1 金融专用提示词**
创建 `config/finance_prompt.txt`，包含：
```python
核心板块：
1. 大盘走势分析
   - 综合判断牛熊趋势
   - 识别关键技术位
   - 预测短中期走势

2. 板块轮动分析
   - 识别领涨/领跌板块
   - 发现资金流向规律
   - 预测下一轮热点

3. 风险预警
   - 识别异常波动
   - 提醒重大事件影响
   - 给出仓位建议
```

**6.2 数据模型扩展**
在 analyzer.py 中添加：
```python
@dataclass
class FinanceAIAnalysisResult:
    """金融AI分析结果"""
    market_overview: str           # 大盘概览
    sector_rotation: str           # 板块轮动
    crypto_insights: str           # 加密货币洞察
    risk_alerts: List[str]         # 风险预警列表
    trading_signals: str           # 交易信号
```

**6.3 结合历史数据**
实现趋势分析：
- 大盘历史走势对比
- 板块涨跌周期分析
- 北向资金流入趋势

**验收标准**
- ✅ AI 能生成专业的市场分析报告
- ✅ 报告包含风险预警和操作建议
- ✅ 分析逻辑符合金融领域规范

---

### **阶段 7：集成与测试（1-2 周）**

#### 目标
将所有模块集成到现有推送体系，并进行全面测试。

#### 任务清单

**7.1 主流程集成**
修改 __main__.py：
```python
# 在现有爬虫流程后添加金融数据流程
def run_financedaily():
    1. 获取大盘数据
    2. 获取板块数据
    3. 获取加密货币数据
    4. 获取Twitter/GitHub数据
    5. AI分析
    6. 生成推送
```

**7.2 推送格式设计**
```
━━━━━━━━━━━━━━━━━━━━
📈 #金融日报 2026-01-27
━━━━━━━━━━━━━━━━━━━━

【大盘】上证 +0.5% 沪深300 +0.3%
【资金】北向 +20亿 主力 +15亿

【板块轮动】
🔥 科技股领涨 (+2.5%)
❄️ 周期股调整 (-1.2%)

【加密货币】
BTC $42,500 (+1.2%)
ETH $2,300 (+0.8%)

【AI 智能分析】
...
```

**7.3 错误处理与降级**
- API 失败时的备用数据源
- 数据异常时的容错处理
- 推送失败的重试机制

**7.4 性能优化**
- 多线程并发请求
- 数据缓存策略
- API 限流保护

**验收标准**
- ✅ 完整流程能正常运行
- ✅ 推送内容格式正确
- ✅ 异常情况能妥善处理

---

### **阶段 8：部署与文档（1 周）**

#### 目标
实现自动化部署和完善文档。

#### 任务清单

**8.1 GitHub Actions 集成**
添加 `.github/workflows/finance_daily.yml`：
```yaml
cron: "0 16 * * 1-5"  # 每周一到周五16:00（市场收盘后）
```

**8.2 配置文档**
创建 `docs/FINANCE_GUIDE.md`：
- API 密钥配置说明
- 各数据源配置方法
- 自定义板块/币种配置
- AI 分析参数调整

**8.3 示例配置文件**
```
config/finance_config.example.yaml
  - 大盘指标开关
  - 板块关注列表
  - 加密货币关注列表
  - Twitter 关键词过滤
```

**验收标准**
- ✅ 自动化任务能按时执行
- ✅ 文档清晰易懂
- ✅ 配置文件有完整示例

---

## 🚀 **优先级建议**

| 阶段 | 优先级 | 预估工时 | 核心价值 |
|------|--------|----------|----------|
| 阶段1 | ⭐⭐⭐⭐⭐ | 6天 | 基础设施，必须先做 |
| 阶段2 | ⭐⭐⭐⭐⭐ | 12天 | 核心功能，用户最关注 |
| 阶段3 | ⭐⭐⭐⭐ | 7天 | 加密货币，热门需求 |
| 阶段5 | ⭐⭐⭐⭐ | 10天 | 社交媒体，捕捉情绪 |
| 阶段6 | ⭐⭐⭐⭐ | 10天 | AI分析，差异化功能 |
| 阶段4 | ⭐⭐⭐ | 5天 | 大宗商品，辅助指标 |
| 阶段7 | ⭐⭐⭐⭐⭐ | 8天 | 集成测试，确保质量 |
| 阶段8 | ⭐⭐⭐ | 5天 | 部署文档，完善体验 |

**总计：约 2-3 个月**

---

## 💡 **关键技术点提醒**

### 1. 数据时效性
- 股票市场：15:00 盘后获取当日数据
- 加密货币：24小时实时，适合多次查询
- Twitter/GitHub：定时任务批量获取

### 2. API 限流
- AkShare 免费，但有一定限制
- CoinGecko 免费配额：每分钟 10-30 次
- Twitter API: 免费版有次数限制

### 3. 数据准确性
- 多数据源交叉验证
- 异常数据自动过滤
- 数据缺失时的降级策略

### 4. 成本控制
- 尽量使用免费 API
- 合理设置查询频率
- 本地缓存减少重复请求

---

## 🎯 **MVP（最小可行产品）建议**

如果时间有限，可以先实现一个精简版：

**MVP 包含：**
1. ✅ 大盘数据（上证、沪深300）
2. ✅ 板块数据（科技/周期/农业）
3. ✅ BTC/ETH 价格
4. ✅ 基础 AI 分析

**MVP 工期：约 3-4 周**
