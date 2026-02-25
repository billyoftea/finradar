# 📰 finradar 🌅 早报
**2026-02-13** | 🌅 早报 | 覆盖时段: 昨日20:00 → 今日08:00 | 市场状态: ✅ 正常交易
生成时间: 2026-02-14 11:44（北京时间）

---

## 🚨 数据源健康提醒

1. 检测到微信登录异常：财联社: invalid session。请重新扫码登录 wechat-exporter。
2. 本次抓取公众号文章为 0 篇，账号搜索失败占比 100%，请检查登录态或服务状态。

处理建议：
1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。
2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。
3. 然后执行 `./scripts/local.sh report morning 20260213` 与 `./scripts/local.sh notion-push morning 20260213` 覆盖 Notion 页面。

# 🤖 AI 分析摘要

## 一、摘要
- **社会**：美国司法部长帕姆·邦迪在国会听证会上以“股市上涨”为由，为不追查爱泼斯坦案等儿童贩卖罪行辩护，引发美国社会强烈不满与政治争议，凸显经济叙事与社会正义的严重割裂 [¹](https://twitter.com/TVietor08/status/2021705825216278670)[²](https://twitter.com/AdameMedia/status/2021639407984656769)[³](https://twitter.com/MikeNellis/status/2021742758956826875)[⁴](https://twitter.com/notthreadguy/status/2022018683586195484)。国内社会关注点分散，包括体育赛事、青少年权益事件及民生话题。
- **经济**：全球市场呈现“美股韧、亚太弱”的分化格局。美国强劲的非农数据持续压制降息预期，而市场对“AI替代”的担忧情绪正从科技股蔓延至房地产服务等传统行业 [⁵](https://wallstreetcn.com/articles/3765486)[⁶](https://wallstreetcn.com/articles/3765544)[⁷](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)。中国央行节前释放流动性，社融数据公布，显示政策维稳意图。
- **市场**：报告时段内，美股三大指数微涨，**罗素2000小盘股（+0.91%）** 表现突出，但道指标普录得三个月最差单周表现 [⁸](https://finance.yahoo.com/quote/%5ERUT)[⁹](https://news.google.com/rss/articles/CBMibkFVX3lxTE5taUw3Uzd4aWVRcF9hR3B6NWpuQ2NiYmJvMkViZVVHLVpmb0JFSDd3c1Itb0xmbnk5NzRndEFGeXRmbERaOVdNX3k2V0U3OEViVGhYZ1pQREdXU1B0Q1AzNHJaQjhkaDgtMHpZUWZn?oc=5)。亚太市场普遍承压，恒指、日经跌幅居前。加密货币（ETH +3.17%）强势，与股市分化形成对比 [¹⁰](https://finance.yahoo.com/quote/%5EIXIC)[¹¹](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5)。
- **科技**：AI对就业和产业的冲击成为市场核心焦虑，房地产服务股因“AI替代”担忧遭抛售 [⁶](https://wallstreetcn.com/articles/3765544)[⁷](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)。GitHub趋势完全聚焦于**AI技能库、成本优化与开发工具**，生态围绕Claude Code等核心工具高度集中 [¹²](https://github.com/coreyhaines31/marketingskills)[¹³](https://github.com/Leey21/awesome-ai-research-writing)[¹⁴](https://github.com/blader/humanizer)。国内“AI除幻第一股”海致科技港股上市首日暴涨242%，显示市场对AI细分赛道的高度热情 [¹⁵](https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5)。

## 二、分板块汇报
### 2.1 市场概况（仅有效交易时段数据）
较上期：美股大盘指数由跌转微涨，但亚太市场（除A股外）普遍下跌，市场分化加剧，VIX指数小幅上升。

**发生了什么**：在报告覆盖的有效交易时段，**美股三大指数（标普500、纳斯达克、道琼斯）均录得0.11%至0.24%的小幅上涨**，其中**罗素2000小盘股指数上涨0.91%**，表现突出 [¹⁶](https://finance.yahoo.com/quote/%5EGSPC)[¹⁰](https://finance.yahoo.com/quote/%5EIXIC)[¹⁷](https://finance.yahoo.com/quote/%5EDJI)[⁸](https://finance.yahoo.com/quote/%5ERUT)。然而，亚太市场普遍走弱，**恒生指数下跌1.72%，日经225指数下跌1.21%，韩国综合指数下跌0.28%** [¹⁸](https://finance.yahoo.com/quote/%5EHSI)[¹⁹](https://finance.yahoo.com/quote/%5EN225)[²⁰](https://finance.yahoo.com/quote/%5EKS11)。欧洲市场涨跌互现。**VIX波动率指数上涨2.69%至21.38**，显示市场不确定性小幅升温 [²¹](https://finance.yahoo.com/quote/%5EVIX)。加密货币表现强势，ETH领涨3.17% [¹¹](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5)。

**为什么会这样（证据强弱：中）**：市场分化主要源于区域风险情绪与资金轮动。1) **美股韧性**：可能部分受益于资金从动荡的亚太市场流出后，寻求美元资产的避险或再平衡，小盘股领涨或反映对美国内需经济的局部乐观 [⁸](https://finance.yahoo.com/quote/%5ERUT)。2) **亚太市场疲软**：输入文本未提供具体原因，但结合VIX上升及区域普跌，可能受区域特定的风险因素或全球流动性收紧预期影响。3) **加密货币强势**：可能与**以太坊超过30%的供应被锁定质押**创纪录有关，显示了强劲的链上基本面与持有者信心 [¹¹](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5)。4) **AI担忧蔓延**：尽管大盘指数上涨，但“AI替代”恐慌情绪被指从科技股蔓延至物流、地产服务等板块，造成结构性压力 [⁶](https://wallstreetcn.com/articles/3765544)[⁷](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)。

**下一步观察**：1) 观察美股小盘股（罗素2000）的强势能否持续，以及是否扩散至其他周期板块。2) 监测亚太市场（尤其是港股）下跌是短期情绪宣泄还是趋势性资金流出。3) 跟踪VIX指数是否继续攀升，以及市场对“AI替代”叙事敏感度的变化。

### 2.2 微信公众号共识与弱信号
数据不足。输入文本中未提供“微信公众号逐篇简介”或具体的公众号文章内容，无法提炼跨公众号共识或弱信号。

### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）
较上期：热度持续高度集中于AI领域，特别是围绕Claude Code等AI编程工具的技能扩展与成本优化，金融科技与Web3领域无显著项目。

本期GitHub趋势呈现 **“AI工具链深化”与“生态内卷化”** 并存的局面。最值得关注的项目均围绕AI，尤其是提升AI应用效率与降低使用门槛：
1.  **AI技能垂直化**：`coreyhaines31/marketingskills` (⭐7525) 和 `Leey21/awesome-ai-research-writing` (⭐5697) 分别针对营销和科研写作，表明AI正从通用能力向**专业化技能包**演进，落地价值在于直接赋能特定职业场景 [¹²](https://github.com/coreyhaines31/marketingskills)[¹³](https://github.com/Leey21/awesome-ai-research-writing)。
2.  **AI内容“人性化”处理**：`blader/humanizer` (⭐4751) 及其汉化版热度高企，直击AI生成内容（AIGC）在实际应用中的“机器痕迹”痛点，应用场景广泛，但潜在风险与内容合规及隐蔽使用相关 [¹⁴](https://github.com/blader/humanizer)[²²](https://github.com/op7418/Humanizer-zh)。
3.  **开发与成本基础设施**：`BlockRunAI/ClawRouter` (⭐2337) 宣称通过智能LLM路由节省推理成本，`mindfold-ai/Trellis` (⭐2187) 提供一体化AI框架。这些项目瞄准AI开发中的**工程效率与运营成本**核心痛点，若其宣称的效能属实，具有较高工具价值，但需验证 [²³](https://github.com/BlockRunAI/ClawRouter)[²⁴](https://github.com/mindfold-ai/Trellis)。

**噪音风险**：1) **生态过度集中**：大量项目围绕“Claude Code”单一生态，存在功能同质化与内卷风险。2) **价值宣称待考**：如`ClawRouter`所称“节省78%成本”缺乏输入文本中的第三方验证。3) **赛道缺失**：**金融科技与Web3领域项目完全缺席**，显示当前开发者热度与资本关注存在显著偏差 [²³](https://github.com/BlockRunAI/ClawRouter)。

### 2.4 Twitter 海外信号（英文内容中文汇报）
较上期：关于美国司法官员将股市表现与司法追责不当关联的争议持续发酵并成为绝对焦点，AI与加密信号零星出现。

Twitter高互动内容几乎被单一政治社会事件主导：**美国司法部长帕姆·邦迪在关于掩盖儿童贩卖的听证会上，以“股市上涨”为由，为不调查恋童癖者辩护**。此举被广泛批评为“反乌托邦”、“荒谬”和“不称职”，引发了民众对官员将金融市场表现置于社会正义之上的强烈愤怒 [¹](https://twitter.com/TVietor08/status/2021705825216278670)[²](https://twitter.com/AdameMedia/status/2021639407984656769)[³](https://twitter.com/MikeNellis/status/2021742758956826875)[⁴](https://twitter.com/notthreadguy/status/2022018683586195484)[²⁵](https://twitter.com/StoneJAlex/status/2021829082862784790)。这显示美国社会情绪中对“经济叙事”掩盖深层社会问题的极度不满，可能加剧政治不确定性。

在科技与金融线索方面：1) **AI工具链**：有推文列举包括ChatGPT、Perplexity（研究）、Suno（作曲）、Runway（视频编辑）在内的11个AI生产力工具，展示了AI应用生态的成熟度 [²⁶](https://twitter.com/Lush_Beauty1/status/2021891789267890190)。2) **AI争议**：有观点提醒，AI的“不可避免性”叙事可能是一种恐吓策略，强调“如果我们不允许，AI就不会接管” [²⁷](https://twitter.com/jzux/status/2022037403062743284)。3) **加密货币**：出现了“为何2012年没买比特币”的经典后悔叙事，以及关于央行购金背景下“链上黄金”重要性的讨论 [²⁸](https://twitter.com/moonshot/status/2021960073602638045)。

### 2.5 国内新闻与政策脉络
较上期：央行流动性操作与社融数据发布成为节前关键经济信号，AI领域出现标志性资本市场事件。

国内政策与市场动态聚焦于节前维稳与AI产业：1) **货币政策**：央行预告并开展**1万亿元买断式逆回购操作**，分析师认为此举降低了近期降准的必要性，旨在平滑节前流动性 [²⁹](https://news.google.com/rss/articles/CBMiwglBVV95cUxPZVdwT09vSjFMeVViSGhldTJjMG9Qd0VrTHM4RnRlRVFuNzdhaUV4T0VIVGE2djdwOVdXWk5nMXJDR2pmZm1UbkY0R0JueGZibkVpOTZoMG5HX1luUUNLbFBrcnJHMTFkYXdZTFlqQVRFRmlhTDR6TGQ1UnJZNERjclN2ZmJiUmhhTzd4cngwQXB5QmVqdFVncHJaaUpwR2JVci0zZEVOM3NnejU4bWNDc3drQjF6ZXNQdUhxbTNKaUtPMEQyY2tNWVhSYmxWZWZXcUN6TTZqeE1SYmhtUEVyNHE2Q1FCRUk3YkNTVlhhR2QycmowNHVUQ2FNcnY4WHRfUzljMm9tQUhKMklnZkl2TDJQWDY3anVWVm9tMldxMFVzTGFSTjU5eWNGbEV5Yk41V3lteUtQb1dqeTBvdDhKeDhTeWxJUmVySkNDOEJSZ0k5WlJRcl90RlVtMFhkbFYwSG80aVMtN3BNalRyOUxycXpPeVFnWktPdkdGQ05wOEI4UGFJenAzSF9aLTYxbk9JNDVGaGZhZDdkNkRFa0hXaUVadDJsM0t6TGZIWS1ySm5DczNPYVVlNUhfS0VjUjFlTXlRdWo0cElocUw4d3U4bEkxaTFTRURUQmRTVlNQb1libENZTFVwbkpiWUFnaDU4S3pSLVA5aGxaWUpGRU9ReTRKQzJyUDM3em40Rk1mQ1Y1bkJaM1dNZjVCeGJtNmNtY3RnMDJsM0k1YWZQQ0phR1Faa1E1ZDNPTzNITHBrdzR3aE1GSHE4dXMwdGI1LV9WYktJbE5uSXB1anB3WWdoNE9Ma2JMazFrVExNd2NET1NFR2ZiZ3FodjM4OWh2amplb1RvOXZkOWFmekN3Sm1JOVgxd3JHSEZzeVFqMDkycW41bVFHZ2NqNXdNWmk2TnFlczBubVlvTXVubHkwTFZzdG5TaGg1Z1c0ZWE2LUE1MEZlTWozZE5nQkMxTzhmNDVpaVo5aHppOElWMzdrMDV6c2g4RGhLZzA2UTBoSUowaWxhVmJmVy0zRUdrRGVZN0J4VzZqaTdiWjI5a0wwUHdNeUdqTHd4X004YWUxbVoyOVBhd280NkRIaUJfTzlZQ3l1ajlDbmtKQmlFbFEzQ0V0NG5JeEhGMldIbm5ydlhXYkFGMTVUZHVIdnpWNnJCNzJUZ0libGQwZGxjQ0VISTdtejFDSWstclBRcVl1WGRteHlBRElfdFFHVFZrZzdjMDd3Nkx2UkVrMDlHRWplVTVxcDAybEEybkNxdk5WTWowY1R4MzB0Y0g4czN4RU9JaWVKaHJjM1B2QzFudC1GM3AtMUppVXUxbURfcndwUWxUNmF3dkhaTEZRellGcVZLa3ZBb2RLRFoxX3M3SWZHYmxmX25oM0pDV1FTVWxSMkloMjBndVR0Xy1zdlY0Q0RybURYdDVWcE0zY0tsYXI4TDdqdU9BcVlxbUh0RmRZc0cta1ZmdUNtS1o0UXJ2SVVVaTNTUWx6Qm96ZlBKdkZSSDN2WTMtQkNqY1NLQ0hHdFROT3plXzBOalJ0bUxjbmlOdlRyYXR2Y0VZQ3hrTDNmZ1JITEk3MmpjelVqXzc4b1Q3djhYZVFLWTNtdC1PNFRpZFl6VXc?oc=5)[¹⁵](https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5)。同时，央行发布数据显示**1月社会融资规模增量为7.22万亿元**，为市场提供了重要的信用扩张观察窗口 [³¹](https://news.google.com/rss/articles/CBMigAFBVV95cUxQXy1BaHYxdktCYXBkSmUzT3J1MnBxQ0JGTFFoNVFDdDRSa0toM0tIM21RVGZ3YUxXQmN1TDhEZXh0dWZXY0ljcnlscHJBR05zYjFmeHdLcndmcldFN2tVQkY3a0kzOVNIOG9jaFZfWDlVanduR0o0elFfUElZRFpYbg?oc=5)。2) **资本市场热点**：**“AI除幻第一股”海致科技集团在港股上市首日暴涨超242%**，成为年内最强新股，显示资本市场对AI细分技术（此处指消除AI幻觉）抱有极高热情和估值预期 [¹⁵](https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5)。3) **产业动态**：AI视频领域竞争激烈，被描述为“双雄并起”，且技术已达到能生成“导演级镜头”的水平 [³²](https://wallstreetcn.com/articles/3765542)。同时，OpenAI指控DeepSeek侵权的事件引发关注，可能影响国内大模型的国际合作与竞争环境 [³³](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVhxamF5ajMyYmdxLXhhc2ZHYkJkTlJhLURpZk1xQXpOY1BQZTJKdE5vcTFxX1dNZXdueS1XLTlIOVZOcWNvTFhfb0dtWXQ2ajl6QUJOb2NVLWI5YjZyNmR4SGRpT043UHpiOUJKUEhiRDQxdzdFckVuRUptdS1kdHQ4RkptQk5vUl82SnA0dXN3bUxYbkhrbg?oc=5)。

## 三、明日跟踪清单
1.  **延续跟进：亚太市场资金流出性质判断**：紧密跟踪港股、日股等亚太市场主要指数的资金流向（如ETF申购赎回、外资持股数据），结合美元指数与区域政策新闻，判断当前下跌是短期技术调整还是趋势性资本外流 [¹⁸](https://finance.yahoo.com/quote/%5EHSI)[¹⁹](https://finance.yahoo.com/quote/%5EN225)[²⁰](https://finance.yahoo.com/quote/%5EKS11)。
2.  **收口复盘：美国司法争议的市场影响评估**：观察帕姆·邦迪听证会争议是否会进一步发酵，并评估其对美国政治风险溢价及投资者情绪（特别是对政府治理信心）的实质性影响，监测相关舆情指数或政治不确定性指数 [¹](https://twitter.com/TVietor08/status/2021705825216278670)[²](https://twitter.com/AdameMedia/status/2021639407984656769)[³](https://twitter.com/MikeNellis/status/2021742758956826875)。
3.  **新增观察：AI恐慌情绪的扩散路径**：重点关注“AI替代”叙事是否从房地产服务板块进一步蔓延至金融、法律、医疗等其它白领密集型行业，并观察相关行业ETF或个股的异常波动 [⁶](https://wallstreetcn.com/articles/3765544)[⁷](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)。


---

<details><summary>📑 点击展开各板块详细分析</summary>

### 📊 市场数据详细分析

### 1. 主要市场走势判断
在报告覆盖的时段内，全球主要股票市场呈现**分化**格局，整体风险偏好有所降温，但未出现恐慌性抛售。
*   **美股表现相对坚韧**：三大股指（标普500、纳斯达克、道琼斯）均录得小幅上涨（+0.11% 至 +0.24%），**罗素2000小盘股指数表现突出，上涨0.91%**，显示市场内部存在结构性机会。
*   **亚太及欧洲市场普遍承压**：日股（-1.21%）、韩股（-0.28%）、港股（-1.72%）均下跌。欧股表现不一，英国富时100（+0.20%）和德国DAX（+0.14%）微涨，法国CAC40（-0.40%）下跌。
*   **A股市场**：根据指令，本报告不分析A股盘面数据。
*   **市场情绪指标**：**VIX波动率指数上涨2.69%至21.38**，表明市场不确定性或避险情绪小幅升温，但绝对水平未显示极度恐慌。

### 2. 关键资产轮动分析
*   **领涨方向**：
    1.  **美股小盘股（罗素2000）**：其涨幅（+0.91%）显著跑赢美股大盘指数，这可能反映了资金在寻找更具增长潜力的内部标的，或是对美国经济韧性的一种押注。数据未提供具体板块信息，无法判断行业轮动。
    2.  **加密货币**：BTC（+1.35%）、ETH（+3.17%）、SOL（+2.20%）全线收涨，成为该时段内表现最亮眼的资产类别之一，显示高风险偏好资金仍在积极活动。
*   **领跌方向**：
    1.  **港股与日股**：恒生指数（-1.72%）和日经225（-1.21%）跌幅居前，显示**亚太市场资金流出压力较大**，可能与区域特定的风险因素或美元流动性环境有关。数据未提供具体原因。
    2.  **部分大宗商品**：天然气（-1.24%）、COMEX铜（-0.30%）和WTI原油（-0.22%）小幅下跌，反映对工业需求和能源前景的短期谨慎情绪。

**资金偏好总结**：资金呈现**两极分化**特征。一方面，风险偏好较高的资金流向加密货币和美股小盘股；另一方面，避险情绪导致资金从部分亚太股市和工业商品中流出。美股大盘成为资金的“稳定器”或“避风港”。

### 3. 加密货币和商品期货的关键变化
*   **加密货币**：整体强势上行，**ETH领涨（+3.17%）**，表现优于BTC和SOL。这表明市场可能不仅关注比特币的基准作用，也在积极交易其他主流加密资产。驱动原因数据不足。
*   **商品期货**：
    *   **能源**：油价涨跌互现，**布伦特原油收平**，WTI微跌，天然气下跌。市场对原油供需前景看法分歧，缺乏明确方向。
    *   **工业金属**：**COMEX铜价下跌0.30%**，结合亚太股市疲软，可能暗示市场对全球制造业活动短期前景的担忧。数据未提供库存或需求端信息。
    *   **贵金属**：数据未提供，无法分析。

### 4. 涨跌驱动链条分析
基于现有数据，可推断以下部分驱动链条：

*   **链条一：区域风险情绪传导 -> 资金从亚太流向相对安全的美元资产 -> 亚太股市下跌，美股相对抗跌**
    *   **事件/政策/情绪（证据弱）**：数据未提供具体事件。但港股、日股显著下跌，且VIX指数上升，表明存在负面情绪或不确定性，可能源自区域内部。
    *   **资金行为（证据中）**：亚太股市普跌与美股（尤其罗素2000）上涨形成对比，显示资金在区域间进行再配置。
    *   **价格表现（证据强）**：恒指 **-1.72%**，日经 **-1.21%**；标普500 **+0.24%**，罗素2000 **+0.91%**。

*   **链条二：高风险偏好资金持续活跃 -> 涌入加密货币市场 -> 加密资产普涨**
    *   **事件/政策/情绪（证据弱）**：数据未提供驱动加密市场的具体消息。
    *   **资金行为（证据中）**：在股票市场分化、商品疲软的背景下，加密货币独立走强，是明确的资金流入信号。
    *   **价格表现（证据强）**：ETH **+3.17%**，BTC **+1.35%**，SOL **+2.20%**。

*   **链条三：对经济增长的疑虑 -> 削减工业商品多头仓位 -> 铜、天然气价格下跌**
    *   **事件/政策/情绪（证据弱）**：数据未提供直接的经济数据或事件。
    *   **资金行为（证据中）**：与亚太股市下跌、美股小盘股领涨（可能反映内需故事）的复杂图景相结合，部分资金选择撤离与经济周期紧密相关的工业商品。
    *   **价格表现（证据强）**：COMEX铜 **-0.30%**，天然气 **-1.24%**。

**结论**：报告时段内市场处于**多空拉锯状态**。美股凭借其深度和流动性吸收了部分避险资金，而加密货币则成为激进资金的突破口。亚太市场成为主要的情绪宣泄地。缺乏明确的宏观主题驱动，市场更多由资金在不同资产类别和区域间的**结构性轮动**所主导。后续需关注这种分化格局是否会收敛，以及VIX指数的变化趋势。

### ⏱ 市场时效过滤说明

市场时效过滤结果：
1. 早报阶段不纳入 A 股盘面，避免使用非交易时段快照

### 🐦 Twitter 逐条简介

Twitter 逐条简介（共 12 条，按互动热度排序）：
1. [热门] @TVietor08 | 2026-02-13T05:57 | 互动=191282
   原文摘录: The stock market is up so we don’t have to prosecute pedophiles is one of the worst political messages i have ever heard.
   原文链接: [点击查看原文](https://twitter.com/TVietor08/status/2021705825216278670)
   1) 讲了什么：用户批评某政治言论，认为股市上涨不应成为不追责犯罪者的理由。
   2) 关键信号：未提供具体事件或数据，仅为个人观点表达。
   3) 阅读建议：略读，因内容属主观评论，无具体金融科技信息。
2. [热门] @AdameMedia | 2026-02-13T05:57 | 互动=169009
   原文摘录: BREAKING: 🇺🇸 🇮🇱 Pam Bondi starts talking about stock market gains during her testimony on her COVER UP of child trafficking. This is fucking dystopian man. Lock
   原文链接: [点击查看原文](https://twitter.com/AdameMedia/status/2021639407984656769)
   1) 讲了什么：Pam Bondi在掩盖儿童贩卖的听证会上谈及股市收益，推文称其行为反乌托邦。
   2) 关键信号：未提供具体市场数据或政策信号，仅为个人评论。
   3) 阅读建议：略读，内容属个人情绪化评论，无具体金融科技信息。
3. [热门] @NotHoodlum | 2026-02-13T05:57 | 互动=154891
   原文摘录: I didn’t realize we don’t pursue pedophiles if the stock market is doing well. Thank you, Pam Bondi, for that clarification.
   原文链接: [点击查看原文](https://twitter.com/NotHoodlum/status/2021618127570866444)
   1) 讲了什么：用户讽刺地评论股市表现好时就不追捕恋童癖者，并提及帕姆·邦迪的澄清。
   2) 关键信号：股市表现与执法关联的讽刺性观点，提及帕姆·邦迪。
   3) 阅读建议：略读 + 原因：内容为讽刺性个人评论，无具体金融科技信息。
4. [热门] @hashjenni | 2026-02-13T05:57 | 互动=116909
   原文摘录: Imagine a little girl tells you an old man was sexually abusing her and your response is “yeah but the stock market.”
   原文链接: [点击查看原文](https://twitter.com/hashjenni/status/2021852693514658217)
   1) 讲了什么：有人转述小女孩指控老人性侵，对方却回应“但股市呢”。
   2) 关键信号：未提供具体事件背景或数据。
   3) 阅读建议：略读 + 原因：仅为一句引述，无金融科技相关信息。
5. [热门] @Rep_Stansbury | 2026-02-13T05:57 | 互动=104692
   原文摘录: Admin Officials in the Epstein Files: Donald J. Trump (President) Melania Trump (1st Lady) Howard Lutnick (Sec. Commerce) John Phelan (Sec. Navy) Paolo Zampolli
   原文链接: [点击查看原文](https://twitter.com/Rep_Stansbury/status/2021796092879184037)
   1) 讲了什么：推文列出爱泼斯坦文件中提及的美国政府官员与知名人士名单。
   2) 关键信号：名单包含特朗普、马斯克等多位现任、前任官员及公众人物。
   3) 阅读建议：略读 + 原因：仅为名单罗列，未提供事件背景或分析。
6. [热门] @moonshot | 2026-02-13T05:57 | 互动=38161
   原文摘录: “why didn’t you buy bitcoin in 2012” me in 2012:
   原文链接: [点击查看原文](https://twitter.com/moonshot/status/2021960073602638045)
   1) 讲了什么：一条推文引用“2012年为何不买比特币”的常见问题。
   2) 关键信号：推文互动数据高，但未提供具体讨论内容。
   3) 阅读建议：略读 + 原因：内容仅为引用常见问题，无新信息或分析。
7. [热门] @MikeNellis | 2026-02-13T05:57 | 互动=34312
   原文摘录: “The stock market is up, so I don’t have to investigate pedophiles and sex traffickers” is an insane defense by Pam Bondi. She’s just as bad as every monster in
   原文链接: [点击查看原文](https://twitter.com/MikeNellis/status/2021742758956826875)
   1) 讲了什么：Pam Bondi用股市上涨为不调查恋童癖和性贩子辩护，被批荒谬。
   2) 关键信号：股市上涨与不调查犯罪被关联；发言者被比作档案中的怪物。
   3) 阅读建议：略读。仅个人观点，无具体金融科技信息或数据。
8. [热门] @ScottJenningsKY | 2026-02-13T05:57 | 互动=33349
   原文摘录: The government is shrinking. The private sector is growing. Wages are finally outpacing inflation. And President Trump has only been in office for a year. Let h
   原文链接: [点击查看原文](https://twitter.com/ScottJenningsKY/status/2022063985647137241)
   1) 讲了什么：推文称政府缩小、私营部门增长、工资增速超通胀，特朗普执政一年。
   2) 关键信号：数据不足/未提供。
   3) 阅读建议：略读 + 原因：仅为个人观点陈述，未提供具体数据或事件支撑。
9. [热门] @notthreadguy | 2026-02-13T05:57 | 互动=31134
   原文摘录: does nobody care that the attorney general said under oath on national television the biggest scandal in american history doesn't matter because the stock marke
   原文链接: [点击查看原文](https://twitter.com/notthreadguy/status/2022018683586195484)
   1) 讲了什么：司法部长在电视上宣誓称美国史上最大丑闻不重要，因股市上涨。
   2) 关键信号：司法部长表态、股市表现与丑闻关联。
   3) 阅读建议：略读 + 原因：仅为个人观点讨论，未提供具体丑闻或数据。
10. [热门] @StoneJAlex | 2026-02-13T05:57 | 互动=30904
   原文摘录: Why in the world is this woman talking about the stock market? She’s the Attorney General of the United States of America. She’s totally unfit and should be fir
   原文链接: [点击查看原文](https://twitter.com/StoneJAlex/status/2021829082862784790)
   1) 讲了什么：用户质疑美国司法部长谈论股市，认为其不称职应被解雇。
   2) 关键信号：司法部长谈论股市引发批评，互动数据高。
   3) 阅读建议：略读 + 原因：仅为个人观点表达，无具体金融科技事件或分析。
11. [热门] @Lush_Beauty1 | 2026-02-13T05:57 | 互动=30826
   原文摘录: 1. ChatGPT = solve any problem 2. PicWish = remove backgrounds 3. Descript = edit podcasts 4. Perplexity = research anything 5. ElevenLabs = clone voices 6. Gam
   原文链接: [点击查看原文](https://twitter.com/Lush_Beauty1/status/2021891789267890190)
   1) 讲了什么：列举了11个AI工具及其功能，建议保存以备不时之需。
   2) 关键信号：未提供。
   3) 阅读建议：略读 + 原因：内容为工具列表，信息密度低，无分析或深度信号。
12. [热门] @Uncommonsince76 | 2026-02-13T05:57 | 互动=30569
   原文摘录: Wow! 🤯. This Irish media company found Jeffrey Epstein’s Fed Ex Account password, then logged as has him and saw packages have been shipped as recent as 2024… R
   原文链接: [点击查看原文](https://twitter.com/Uncommonsince76/status/2021656795694121334)
   1) 讲了什么：爱尔兰媒体公司发现爱泼斯坦联邦快递账户密码，登录后看到包裹发货至2024年。
   2) 关键信号：账户密码被获取，包裹发货时间数据未提供。
   3) 阅读建议：略读 + 原因：仅提供事件概述，无具体证据或数据支持。

### 🌐 Twitter 英文信号详细分析

### 海外英文信号主线
1.  **政治与市场关联争议**：美国总检察长帕姆·邦迪在关于掩盖儿童贩卖的证词中，以股市上涨为由，为不追查恋童癖者辩护，引发广泛愤怒与批评。舆论认为这是将金融市场表现与司法追责不当关联的“反乌托邦”行为。
2.  **爱泼斯坦案持续发酵**：爱泼斯坦文件中提及多名美国政府前/现任官员及知名人士（包括特朗普、马斯克等），同时有线索称其联邦快递账户在2024年仍有活动，显示案件关注度未减。
3.  **经济与政策叙事**：有观点认为，在特朗普政府执政一年后，政府规模缩小、私营部门增长、工资增速超过通胀，呈现积极经济信号。
4.  **社会不满情绪**：民众对当选官员感到愤怒和厌倦，认为1月6日事件是深层政府针对MAGA运动的构陷，但该运动反而变得更强大。

### 与金融科技/AI/Web3相关的具体线索
1.  **AI工具应用**：提及一系列AI生产力工具，包括ChatGPT（解决问题）、Perplexity（研究）、ElevenLabs（语音克隆）、Suno（作曲）、Runway（视频编辑）等，展示了AI在日常工作中的具体应用场景。
2.  **AI发展与争议**：
    *   **技术进步**：AI被用于在乳腺癌发病前5年进行检测。
    *   **警惕观点**：有声音提醒，AI的“不可避免性”叙事可能是一种恐吓营销，强调“如果我们不允许，AI就不会接管”。
3.  **加密货币与数字资产**：
    *   **比特币**：出现“为什么2012年没买比特币”的经典后悔叙事。
    *   **链上黄金**：提出央行以1960年代以来未见的速度购金、通胀持续、主权债务高企的背景下，链上黄金为何重要的问题。
4.  **技术故障**：Windows 11更新程序导致游戏FPS大幅下降，NVIDIA工作人员建议卸载该更新作为解决方案。

### 可执行关注点与潜在误导噪音
**可执行关注点：**
1.  **市场情绪风险**：政治丑闻与金融市场表现的强行关联，可能加剧市场对政策不确定性及司法独立性的担忧，影响风险偏好。
2.  **AI工具链**：所列的AI工具清单（如Perplexity、Suno、Runway）代表了当前高关注度的AI应用方向，可作为观察AI落地和投资趋势的切入点。
3.  **数字资产叙事**：央行购金与主权债务背景下的“链上黄金”讨论，可能预示着将传统避险资产逻辑引入加密世界的叙事尝试。

**潜在误导噪音：**
1.  **情绪化指控**：关于爱泼斯坦文件涉及人员的名单及账户活动的指控，未经司法证实，属于高度情绪化和猜测性的内容，需警惕其真实性。
2.  **阴谋论叙事**：将1月6日事件完全归因于政治构陷的指控，缺乏输入文本提供的证据支持，属于典型的政治阴谋论，信息可信度低。
3.  **片面经济描述**：“政府缩小、私营增长、工资跑赢通胀”是单一正面描述，未提供任何具体数据或对比基准，可能掩盖了经济全貌。
4.  **技术问题归因**：Windows更新导致FPS下降仅为个案报告，未提供普遍性证据或官方全面确认，可能夸大问题影响范围。

### 📰 热榜详细分析

# 热榜综合分析报告

基于提供的各分片摘要，以下是融合分析后的关键发现：

## 1. 跨平台共同关注的3-5个热点事件
*   **冬奥/体育赛事**：多个分片提及，是共同的社会关注焦点。具体事件包括：意大利老将在速度滑冰女子5000米项目上绝杀夺金；米兰冬奥会中国雪橇队创造历史；短道速滑赛事（孙龙、范可新等运动员表现）及冰壶女队战胜英国等。
*   **社会法治与青少年权益事件**：“浙江13岁体操女运动员坠楼案”及其关联的“体罚索财”事件在多个分片出现，引发对校园安全、师德及青少年权益保护的广泛关注。
*   **AI技术的社会应用与讨论**：AI技术的影响是贯穿多个分片的线索，具体表现为：市场对“AI担忧”拖累股指的讨论；房地产服务股被视为“下一个AI受害者”；以及公众对AI生成视频、AI替班等具体应用的关注与讨论。
*   **国际关系与摩擦**：多个分片涉及，包括：中方回应荷兰启动对安世半导体的调查；中方回应关于“特朗普将于4月初访华”的消息；以及“欧盟加大对华限制，六国联名警告”。

## 2. 与金融市场相关的重要新闻
*   **美国货币政策与市场反应**：强劲的非农就业数据打击了市场对美联储降息的预期。“新美联储通讯社”预计首次降息可能延至7月。这些预期影响了美国股指（尤其受AI担忧拖累）、美债、金银及原油价格。
*   **特定行业板块波动**：房地产服务股遭遇抛售，创下“疫情以来最大单日跌幅”，并被市场与AI影响关联。
*   **资本市场动态**：机器人公司“灵心巧手”完成近15亿元人民币B轮融资；民营火箭领域诞生“最大单笔融资”。
*   **国内经济信号**：一线城市房地产市场出现回暖信号。
*   **其他**：关于“欧盟加大对华限制”对金融市场的具体影响，输入文本未提供细节。

## 3. 科技/AI 相关热点
*   **AI对产业与市场的影响**：市场存在“AI担忧”，并将其视为拖累美股和影响房地产服务板块的因素。AI技术对传统行业的潜在颠覆性影响传导至资本市场。
*   **AI视频与内容生成**：中国AI视频领域出现“双雄并起”现象。AI视频工具已达到能生成“导演级镜头”的水平，引发关于其在影视领域应用与商业化的公众讨论。
*   **AI的具体应用案例**：出现“用AI解锁吴克群将军令”、“哈尔滨小哥为早回家过年找AI替班”等热搜，反映AI在娱乐互动和日常工作场景中的渗透。
*   **机器人技术**：“灵心巧手”公司售出超过一万只机器人“手”，是AI与机器人技术商业化的案例。
*   **前沿科技议题**：“建立太空数据中心有多难”涉及航天与数字基础设施结合的议题。

## 4. 社会舆论焦点
*   **体育赛事与运动员**：冬奥会及相关冰雪赛事（短道速滑、雪橇、U型池等）的比赛结果、运动员表现（如孙龙、范可新、武绍桐等）及动态（如孙龙落泪）是主要的社会关注点。
*   **社会民生与公共事件**：除前述青少年运动员坠楼案外，“河南邓州错领骨灰盒”、“钱氏家训受关注”、“酒桌文化讨论”、“六户村民合建楼房”、“第三方火车票‘加速包’被约谈”以及“换新费上万的假肢被修鞋大爷免费修好”等事件，分别引发对公共管理、传统文化、消费权益、社会互助等话题的讨论。
*   **娱乐与社会话题**：涵盖广泛，包括霍启刚郭晶晶合体拜年、蒋欣相关话题、艺人蔡徐坤动态、电视剧《太平年》角色讨论、游戏资讯（王者荣耀、喵喵的结合）、以及“过年第一批烫发的人”、“连续五年都没有年三十”等生活化内容。
*   **企业家动态**：于东来宣布退休引发对企业传承的关注。
*   **国际事件**：加拿大校园枪击案、美国司法部长与议员激烈争论、立陶宛可能转向与中国恢复关系等吸引了一定舆论关注。

### 💻 GitHub 项目详细分析

# GitHub热门项目技术趋势分析报告

## 一、最值得关注的项目（5-8个）

基于提供的项目列表，以下项目在热度（Star数）和主题相关性上最为突出：

1.  **coreyhaines31/marketingskills** (AI，⭐7525)：专注于为AI智能体（Claude Code）提供营销技能集。
2.  **Leey21/awesome-ai-research-writing** (AI，⭐5697)：旨在提升AI辅助的科研写作效率。
3.  **blader/humanizer** (AI，⭐4751)：用于消除文本中AI生成痕迹的Claude Code技能。
4.  **BlockRunAI/ClawRouter** (AI，⭐2337)：智能LLM路由，宣称可节省推理成本。
5.  **mindfold-ai/Trellis** (AI，⭐2187)：面向Claude Code和Cursor的一体化AI框架与工具包。
6.  **hesamsheikh/awesome-openclaw-usecases** (通用开发，⭐1933)：OpenClaw应用场景的社区集合。
7.  **op7418/CodePilot** (通用开发，⭐1815)：Claude Code的本地桌面图形用户界面。

## 二、应用场景与落地价值分析

*   **AI内容生成与优化**：`marketingskills`、`awesome-ai-research-writing`、`PaperBanana`等项目表明，AI正深度融入营销文案、学术写作、科研绘图等具体生产环节，旨在直接提升内容产出的效率与质量。其落地价值在于将通用大模型能力转化为垂直领域的生产力工具。
*   **AI痕迹消除与“人化”处理**：`humanizer`及其汉化版本`Humanizer-zh`热度很高，直接对应了当前AI生成内容（AIGC）在实际应用中面临的可识别性问题。其应用场景包括需要使文本更自然、避免被检测为AI生成的各类写作任务，潜在价值与AIGC的合规及隐蔽使用需求相关。
*   **AI开发与成本优化基础设施**：`ClawRouter`提出了通过智能路由在多模型间分配请求以降低推理成本的方案，`Trellis`提供一体化开发框架，`agentation`提供智能体视觉反馈工具。这些项目瞄准的是AI应用开发中的工程效率与运营成本痛点，具有成为开发者工具链中关键组件的潜力。
*   **AI编程助手生态扩展**：多个项目（如`CodePilot`、`companion`、`peon-ping`）围绕“Claude Code”和“Cursor”等AI编程工具构建增强功能，包括图形界面、移动端支持、通知系统等。这反映出一个围绕核心AI编程工具形成的活跃外围生态，旨在改善开发者体验，其价值在于丰富和巩固主流AI编程工具的使用场景。

## 三、可能的泡沫噪音或重复概念

*   **概念集中与同质化风险**：输入样本中超过三分之二的项目属于**AI**类别，且大量项目（如`marketingskills`、`humanizer`、`Trellis`、`CodePilot`、`companion`等）明确围绕“Claude Code”这一特定AI编程工具或其生态构建。这显示出当前热度的**高度集中性**，可能存在生态内卷和功能重复的风险。例如，`humanizer`与`Humanizer-zh`是同一核心功能的不同语言版本。
*   **价值宣称需谨慎验证**：`ClawRouter`项目宣称“节省78%推理成本”，此类具体的效能数据在输入文本中**未提供**可追溯的验证依据或基准测试详情，应视为项目方的单方面宣称，存在夸大或依赖特定条件的可能性。
*   **应用场景的务实性差异**：`awesome-openclaw-usecases`作为用例集合，其长期价值取决于社区持续贡献的质量与多样性，目前**数据不足**以判断其内容深度。`peon-ping`等项目提供了趣味性增强功能，但其解决的是相对边缘的体验问题，核心价值有限。
*   **金融科技与Web3领域项目缺失**：在本次提供的项目样本中，**未出现**明确归类于金融科技或Web3领域的项目。所有高热度项目均集中于AI及其应用生态（特别是AI编程）以及通用开发工具。

### 🌐 联网检索摘要

联网检索共 20 条（关键词: 2026-02-13 全球市场 盘面 复盘 原因, 2026-02-13 中国 宏观 经济 政策 市场 影响, 2026-02-13 AI 科技 行业 动态 影响, VIX波动率指数 上涨 原因, ETH 上涨 原因, 华尔街见闻早餐FM-Radio | 2026年2月12日 事件 背景, 圆脸谈加拿大校园枪击致10死 事件 背景, 强劲非农打击降息预期，AI担忧拖累美股指，美债承压，金银涨，原油冲高回落 事件 背景）
1. [2026-02-14 07:16] 新浪财经 | 道指标普录得3个月最差单周，亚马逊九连阴，英伟达苹果跌超2%，黄金夺回5000美元 - 新浪财经
   摘要: 道指标普录得3个月最差单周，亚马逊九连阴，英伟达苹果跌超2%，黄金夺回5000美元 新浪财经
   链接: https://news.google.com/rss/articles/CBMibkFVX3lxTE5taUw3Uzd4aWVRcF9hR3B6NWpuQ2NiYmJvMkViZVVHLVpmb0JFSDd3c1Itb0xmbnk5NzRndEFGeXRmbERaOVdNX3k2V0U3OEViVGhYZ1pQREdXU1B0Q1AzNHJaQjhkaDgtMHpZUWZn?oc=5
2. [2026-02-14 06:06] SOHU | 金融股市场动态：建设银行美股表现如何？ - SOHU
   摘要: 金融股市场动态：建设银行美股表现如何？ SOHU
   链接: https://news.google.com/rss/articles/CBMiiwFBVV95cUxOUFFYUzlxbkZteWE1TE5jZzl3S3BpcUY5TDU2Z20yeHl2a20tLW1RQWlwSXBMSU9WcnRmNnpWVWFNS2RlenItYlg5VTNqS3RpeG95S0VVS1l3LWtxclQ5eTJnVV9LTXFsVWN0U2JqN2pPTUFKWGNTcF9pUTdGeUdrd1N1Z3BTOW10LUNV?oc=5
3. [2026-02-14 05:31] 英为财情 Investing.com | 美国股市涨跌不一；截至收盘道琼斯工业平均指数上涨0.10% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 美国股市涨跌不一；截至收盘道琼斯工业平均指数上涨0.10% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMigAFBVV95cUxQXy1BaHYxdktCYXBkSmUzT3J1MnBxQ0JGTFFoNVFDdDRSa0toM0tIM21RVGZ3YUxXQmN1TDhEZXh0dWZXY0ljcnlscHJBR05zYjFmeHdLcndmcldFN2tVQkY3a0kzOVNIOG9jaFZfWDlVanduR0o0elFfUElZRFpYbg?oc=5
4. [2026-02-14 04:01] Cryptopolitan | Ethereum 价格预测（2026、2027、2028-2032 年） - Cryptopolitan
   摘要: Ethereum 价格预测（2026、2027、2028-2032 年） Cryptopolitan
   链接: https://news.google.com/rss/articles/CBMib0FVX3lxTE1sSGFYRTBCTFNocFJzZ0JiZFo3MlRNUXQ5VUFSdkkzY05yY1pFVmlsclE3bEhWSVk4Mm5oaWNEVHhtX1N5SlREczNJaS01M0VqaEhoYXNnU3NfeEdNOFBfQXQ3OVlwX0ZWMlJHTTFRbw?oc=5
5. [2026-02-13 23:39] Binance | 超过30%的供应被锁定：以太坊质押潮在价格触底周期中创下纪录| Htp96发布于币安广场 - Binance
   摘要: 超过30%的供应被锁定：以太坊质押潮在价格触底周期中创下纪录| Htp96发布于币安广场 Binance
   链接: https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5
6. [2026-02-13 22:48] 新浪新闻_手机新浪网 | 财经资讯AI速递：昨夜今晨财经热点一览 丨2026年2月13日 - 新浪新闻_手机新浪网
   摘要: 财经资讯AI速递：昨夜今晨财经热点一览 丨2026年2月13日 新浪新闻_手机新浪网
   链接: https://news.google.com/rss/articles/CBMidEFVX3lxTFBlVDM4dDBnOVdjMW90TkZBZTVBR3BjSXF3V3JOUWtKTjBmR2tMWHo4d09nMTR0ZmpxTXNnbTVpdC16ZXJTb0t5bm9qODd6WjdnTDBNdjRqY0FoN0JzUDl0amRzUVowbkdTYW50Rmo4dnkyTEw5?oc=5
7. [2026-02-13 22:26] 新浪新闻_手机新浪网 | 科技资讯AI速递：昨夜今晨科技热点一览 丨2026年2月13日 - 新浪新闻_手机新浪网
   摘要: 科技资讯AI速递：昨夜今晨科技热点一览 丨2026年2月13日 新浪新闻_手机新浪网
   链接: https://news.google.com/rss/articles/CBMidEFVX3lxTE5iTFRnUEc1MTZXQ2ptend5TEh0Y0FmWDcyZTA1MWFBWTlNNTEwMExJXy0ySVREUl9DUEI0MDUwY3JMd0FfVUtNWTB0SURkZXlnRzNWX18wa3ZnUFJPTWlET1hPQ2EyRVFOMW42YWV4cXE1NlVn?oc=5
8. [2026-02-13 22:13] 财新 | 美股三连跌 “AI替代”恐慌情绪从科技蔓延至物流、地产等板块 - 财新
   摘要: 美股三连跌 “AI替代”恐慌情绪从科技蔓延至物流、地产等板块 财新
   链接: https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5
9. [2026-02-13 20:11] 新浪网 | 央行节前发布重要数据：社融增量7.22万亿元 - 新浪网
   摘要: 央行节前发布重要数据：社融增量7.22万亿元 新浪网
   链接: https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVhxamF5ajMyYmdxLXhhc2ZHYkJkTlJhLURpZk1xQXpOY1BQZTJKdE5vcTFxX1dNZXdueS1XLTlIOVZOcWNvTFhfb0dtWXQ2ajl6QUJOb2NVLWI5YjZyNmR4SGRpT043UHpiOUJKUEhiRDQxdzdFckVuRUptdS1kdHQ4RkptQk5vUl82SnA0dXN3bUxYbkhrbg?oc=5
10. [2026-02-13 18:30] 英为财情 Investing.com | 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.30% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.30% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMigAFBVV95cUxOOFVwdXJrMWltM20zd3ZoUjgxRC1OTE1jZlZvVGJkcnlGRzhEenJPemVMQk9SamctR3R6bHVOOUFqM2RpbU96Wk9pWS02SlVybGtPWlQ0bzV5al8xbkRRUjdLSkRaemRnZVRMWFFyaFNyZ0pwZEhuZ3YxMEREa3lrSw?oc=5
11. [2026-02-13 17:50] 新浪财经 | 港股复盘 | 年内最强新股诞生 “AI除幻第一股”海致科技集团港股上市首日涨超242% - 新浪财经
   摘要: 港股复盘 | 年内最强新股诞生 “AI除幻第一股”海致科技集团港股上市首日涨超242% 新浪财经
   链接: https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5
12. [2026-02-13 13:10] 手机新浪网 | OpenAI指控DeepSeek侵权_新浪新闻 - 手机新浪网
   摘要: OpenAI指控DeepSeek侵权_新浪新闻 手机新浪网
   链接: https://news.google.com/rss/articles/CBMiY0FVX3lxTE1GSmZxeUNvbFBvMF9vMU8zUFRFQXZzb21NbU5kNzlQaFhvcmh1dGlBcEpiaTNhYVluVDhURUlMUXBzYmltQ3hSVW1Ta2FxYmlmWVUxSFlkRXdUN1o2Y05SN1ltMA?oc=5
13. [2026-02-13 09:35] 同花顺财经 | 金银巨震，美股重挫 - 同花顺财经
   摘要: 金银巨震，美股重挫 同花顺财经
   链接: https://news.google.com/rss/articles/CBMiXkFVX3lxTFBaNUR1OE9kekMzNUxHSm41MHl5MU5Ybk1KUzAwNGFqTXl2RE03d3JoT0lxSmhTWkVWYk9XSWswX3dwZjkycFRvZDhQYUJYZUEtOEI3LUlHcHhEYTB1T2c?oc=5
14. [2026-02-13 07:43] 证券之星 | 人民币延续升值趋势，中国资产受益链条明晰 - 证券之星
   摘要: 人民币延续升值趋势，中国资产受益链条明晰 证券之星
   链接: https://news.google.com/rss/articles/CBMiZEFVX3lxTFBPR0ZDSlctc0lTVGRacGV1dnRPQ0k0QUpTU25iR1daVlBLOUtwMmNoQjNSNngydHJ2b285M0VweVpLdjZoNlpUUFZLd3pJcy14S0E2bjY1VVZQaFVUc1ZBejZNUDE?oc=5
15. [2026-02-13 06:34] 富途牛牛 | 金银、股集体下挫，恐慌指数VIX飙升，三倍做空纳指ETF涨超6% - 富途牛牛
   摘要: 金银、股集体下挫，恐慌指数VIX飙升，三倍做空纳指ETF涨超6% 富途牛牛
   链接: https://news.google.com/rss/articles/CBMipwFBVV95cUxQMkx2ZjF0WHJPVjNoQm5hNXhpVjZEMnF3ODRuWm5UOFhKWnlObTlWR25qQUpfZ1dYQk1rUmt2OFcxZWwyYjFBaTh2UDBBdDJnYXVZUW9PTTRqcGluV1VWRnJ2dWhEQUpobTZ4S3FFdHBvWmtJS3NMUWJ1SW5Xb1poWmhfUjhjVkJsNGtFUkNxbnVBQ014YU41aEw0ZHpvNHJsbl9aczk4dw?oc=5
16. [2026-02-13 05:11] 新浪财经 | 2月13日收盘：美股收跌纳指下跌2% AI发展令多个行业承压 - 新浪财经
   摘要: 2月13日收盘：美股收跌纳指下跌2% AI发展令多个行业承压 新浪财经
   链接: https://news.google.com/rss/articles/CBMihwFBVV95cUxOVEhzbFF0bFphZ3pvTDJ6bXBHWlVDTDA2QzdId2VDZWdSY1VnMmFadmROVnplT1Z5b0oyNW1xdXB4RG5hc2RmRU4tM1FRNUxsR0tfYjRudkY5Wk9kYmxnYkQxU19IdVhYRHVwZGFud1dkZjI2eHdWTTNxdlJ3ZGpsd3Jia3RxQzg?oc=5
17. [2026-02-13 00:17] 新浪财经 | 10000亿元！央行最新预告 - 新浪财经
   摘要: 10000亿元！央行最新预告 新浪财经
   链接: https://news.google.com/rss/articles/CBMieEFVX3lxTE9YdzVUY0d1Ymk5SlZiWkJBMDN3OHktb3d4UFl4WWpuTE5rLWxJcGEybG5HRUItb1R6YnBEV2FicDZpV3g2Y0xKdC0xWU5MVm8tb3RyWmRQTnVqSFZUZXdSM0ZHSFFBMUJ1QWlJc09MU25kSzltbmJDeA?oc=5
18. [2026-02-12 21:35] 新浪网 | 央行明日开展1万亿买断式逆回购操作，分析师：降准必要性降低 - 新浪网
   摘要: 央行明日开展1万亿买断式逆回购操作，分析师：降准必要性降低 新浪网
   链接: https://news.google.com/rss/articles/CBMiwglBVV95cUxPZVdwT09vSjFMeVViSGhldTJjMG9Qd0VrTHM4RnRlRVFuNzdhaUV4T0VIVGE2djdwOVdXWk5nMXJDR2pmZm1UbkY0R0JueGZibkVpOTZoMG5HX1luUUNLbFBrcnJHMTFkYXdZTFlqQVRFRmlhTDR6TGQ1UnJZNERjclN2ZmJiUmhhTzd4cngwQXB5QmVqdFVncHJaaUpwR2JVci0zZEVOM3NnejU4bWNDc3drQjF6ZXNQdUhxbTNKaUtPMEQyY2tNWVhSYmxWZWZXcUN6TTZqeE1SYmhtUEVyNHE2Q1FCRUk3YkNTVlhhR2QycmowNHVUQ2FNcnY4WHRfUzljMm9tQUhKMklnZkl2TDJQWDY3anVWVm9tMldxMFVzTGFSTjU5eWNGbEV5Yk41V3lteUtQb1dqeTBvdDhKeDhTeWxJUmVySkNDOEJSZ0k5WlJRcl90RlVtMFhkbFYwSG80aVMtN3BNalRyOUxycXpPeVFnWktPdkdGQ05wOEI4UGFJenAzSF9aLTYxbk9JNDVGaGZhZDdkNkRFa0hXaUVadDJsM0t6TGZIWS1ySm5DczNPYVVlNUhfS0VjUjFlTXlRdWo0cElocUw4d3U4bEkxaTFTRURUQmRTVlNQb1libENZTFVwbkpiWUFnaDU4S3pSLVA5aGxaWUpGRU9ReTRKQzJyUDM3em40Rk1mQ1Y1bkJaM1dNZjVCeGJtNmNtY3RnMDJsM0k1YWZQQ0phR1Faa1E1ZDNPTzNITHBrdzR3aE1GSHE4dXMwdGI1LV9WYktJbE5uSXB1anB3WWdoNE9Ma2JMazFrVExNd2NET1NFR2ZiZ3FodjM4OWh2amplb1RvOXZkOWFmekN3Sm1JOVgxd3JHSEZzeVFqMDkycW41bVFHZ2NqNXdNWmk2TnFlczBubVlvTXVubHkwTFZzdG5TaGg1Z1c0ZWE2LUE1MEZlTWozZE5nQkMxTzhmNDVpaVo5aHppOElWMzdrMDV6c2g4RGhLZzA2UTBoSUowaWxhVmJmVy0zRUdrRGVZN0J4VzZqaTdiWjI5a0wwUHdNeUdqTHd4X004YWUxbVoyOVBhd280NkRIaUJfTzlZQ3l1ajlDbmtKQmlFbFEzQ0V0NG5JeEhGMldIbm5ydlhXYkFGMTVUZHVIdnpWNnJCNzJUZ0libGQwZGxjQ0VISTdtejFDSWstclBRcVl1WGRteHlBRElfdFFHVFZrZzdjMDd3Nkx2UkVrMDlHRWplVTVxcDAybEEybkNxdk5WTWowY1R4MzB0Y0g4czN4RU9JaWVKaHJjM1B2QzFudC1GM3AtMUppVXUxbURfcndwUWxUNmF3dkhaTEZRellGcVZLa3ZBb2RLRFoxX3M3SWZHYmxmX25oM0pDV1FTVWxSMkloMjBndVR0Xy1zdlY0Q0RybURYdDVWcE0zY0tsYXI4TDdqdU9BcVlxbUh0RmRZc0cta1ZmdUNtS1o0UXJ2SVVVaTNTUWx6Qm96ZlBKdkZSSDN2WTMtQkNqY1NLQ0hHdFROT3plXzBOalJ0bUxjbmlOdlRyYXR2Y0VZQ3hrTDNmZ1JITEk3MmpjelVqXzc4b1Q3djhYZVFLWTNtdC1PNFRpZFl6VXc?oc=5
19. [2026-02-12 15:50] Yellow.com | Uniswap 巨鲸在由 BlackRock 推动的 42% 暴涨中抛售 2700 万美元 - Yellow.com
   摘要: Uniswap 巨鲸在由 BlackRock 推动的 42% 暴涨中抛售 2700 万美元 Yellow.com
   链接: https://news.google.com/rss/articles/CBMimwJBVV95cUxPdmZhXzBOZ3pITDdiTHhoQXFIeEMtS2Y2dmkzYjBnMnJSS1NxalRMTy1TR3ZwaGJIWmgwdTBmVnlEWG40OGZoNTJhREhYd0JBM2ppQkdlU3RZNmdGdmVYR0JsVXQ3RVZSVHFuRjBzMjUzVEt5VzZhaGtUZEVzdjZxRnUteUh4b21zTDZEajhKT2tRUnJrSmU0NFFOeVNPcmhmOE5QLWJhYTUzdWRBSHhzVG1iUFY4SE1na25UTk5HR2FyR0JRTnQwVF80VkFoUTcyWGRhTFM1SXZhVWZXSEkzRDlDWGJFMGVEdklhYWdLUVV1cVdUNmtvcnFfTDhWcXIwaU5ldkdwc0FHN0cwV3pLRUd2X204WmpxbVhR?oc=5
20. [2026-02-12 12:09] NAI500 | 美股走势分化凸显AI焦虑，就业利好难掩科技板块抛压 - NAI500
   摘要: 美股走势分化凸显AI焦虑，就业利好难掩科技板块抛压 NAI500
   链接: https://news.google.com/rss/articles/CBMi1AJBVV95cUxQQmNzbEdYQnRCZlhrSzFORDdoOUNBNjNOb3NGakhqdElUVVMxT0h3cndSQ2ZldUtadVdmVk5CcHFSdmtsR3FsdkNwOG9QVUhPSDlvem1ZUElZaVFrbXItemRPN3FPSmltbXBiaVVJSXZPSFY5Z0ZqS3pHZF9KaGZLZk9YMVVReGdtaWRRQzFPTmJDRUJIT2FjbGR1bzJrN0RQSGRoSXJobHo2LTRod1pWTHZhcEdEZWZwamRLSWxyVmhwRXhIYVB3Mnd4V2pYSURQeWtyZFBmWEJUd2REMV9RT1B3MklNY3hlekNWRW9Mc3FTdTN0SDVrZ0tsalZ2TDlhS1hfeW9VVGd4MS13Wi1WMWcteDMyUUFVaWR2dENSZElOcXBZS1pReU9sVkNDaF9sY3NwX1AxclNYTnk0U3FGQXc4LXp6MXQ0RVQwQktqVTdQUlc5?oc=5

</details>


### 📎 引用脚注

1. [2026-02-13T05:57 @TVietor08 | The stock market is up so we don’t have to prosecute pedophiles is one of the worst poli...](https://twitter.com/TVietor08/status/2021705825216278670)（Twitter，匹配分=100，来源ID=TW01）
2. [2026-02-13T05:57 @AdameMedia | BREAKING: 🇺🇸 🇮🇱 Pam Bondi starts talking about stock market gains during her testimony o...](https://twitter.com/AdameMedia/status/2021639407984656769)（Twitter，匹配分=100，来源ID=TW02）
3. [2026-02-13T05:57 @MikeNellis | “The stock market is up, so I don’t have to investigate pedophiles and sex traffickers” ...](https://twitter.com/MikeNellis/status/2021742758956826875)（Twitter，匹配分=100，来源ID=TW07）
4. [2026-02-13T05:57 @notthreadguy | does nobody care that the attorney general said under oath on national television the bi...](https://twitter.com/notthreadguy/status/2022018683586195484)（Twitter，匹配分=100，来源ID=TW09）
5. [华尔街见闻 #4 | 强劲非农打击降息预期，AI担忧拖累美股指，美债承压，金银涨，原油冲高回落](https://wallstreetcn.com/articles/3765486)（NewsNow热榜，匹配分=100，来源ID=NW03）
6. [华尔街见闻 #5 | “下一个AI受害者”出现了，房地产服务股遭抛售，创疫情以来最大单日跌幅](https://wallstreetcn.com/articles/3765544)（NewsNow热榜，匹配分=100，来源ID=NW04）
7. [2026-02-13 22:13 财新 | 美股三连跌 “AI替代”恐慌情绪从科技蔓延至物流、地产等板块 - 财新](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)（联网检索，匹配分=100，来源ID=WB08）
8. [Yahoo Finance 罗素2000 (^RUT)](https://finance.yahoo.com/quote/%5ERUT)（市场原始数据，匹配分=100，来源ID=MK04）
9. [2026-02-14 07:16 新浪财经 | 道指标普录得3个月最差单周，亚马逊九连阴，英伟达苹果跌超2%，黄金夺回5000美元 - 新浪财经](https://news.google.com/rss/articles/CBMibkFVX3lxTE5taUw3Uzd4aWVRcF9hR3B6NWpuQ2NiYmJvMkViZVVHLVpmb0JFSDd3c1Itb0xmbnk5NzRndEFGeXRmbERaOVdNX3k2V0U3OEViVGhYZ1pQREdXU1B0Q1AzNHJaQjhkaDgtMHpZUWZn?oc=5)（联网检索，匹配分=100，来源ID=WB04）
10. [Yahoo Finance 纳斯达克综合 (^IXIC)](https://finance.yahoo.com/quote/%5EIXIC)（市场原始数据，匹配分=100，来源ID=MK02）
11. [2026-02-13 23:39 Binance | 超过30%的供应被锁定：以太坊质押潮在价格触底周期中创下纪录| Htp96发布于币安广场 - Binance](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5)（联网检索，匹配分=100，来源ID=WB05）
12. [coreyhaines31/marketingskills | ⭐ 7525](https://github.com/coreyhaines31/marketingskills)（GitHub，匹配分=100，来源ID=GH01）
13. [Leey21/awesome-ai-research-writing | ⭐ 5697](https://github.com/Leey21/awesome-ai-research-writing)（GitHub，匹配分=100，来源ID=GH02）
14. [blader/humanizer | ⭐ 4751](https://github.com/blader/humanizer)（GitHub，匹配分=100，来源ID=GH03）
15. [2026-02-13 17:50 新浪财经 | 港股复盘 | 年内最强新股诞生 “AI除幻第一股”海致科技集团港股上市首日涨超242% - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5)（联网检索，匹配分=100，来源ID=WB11）
16. [Yahoo Finance 标普500 (^GSPC)](https://finance.yahoo.com/quote/%5EGSPC)（市场原始数据，匹配分=100，来源ID=MK01）
17. [Yahoo Finance 道琼斯工业指数 (^DJI)](https://finance.yahoo.com/quote/%5EDJI)（市场原始数据，匹配分=100，来源ID=MK03）
18. [Yahoo Finance 恒生指数 (^HSI)](https://finance.yahoo.com/quote/%5EHSI)（市场原始数据，匹配分=100，来源ID=MK06）
19. [Yahoo Finance 日经225 (^N225)](https://finance.yahoo.com/quote/%5EN225)（市场原始数据，匹配分=100，来源ID=MK07）
20. [Yahoo Finance 韩国综合指数 (^KS11)](https://finance.yahoo.com/quote/%5EKS11)（市场原始数据，匹配分=100，来源ID=MK08）
21. [Yahoo Finance VIX波动率指数 (^VIX)](https://finance.yahoo.com/quote/%5EVIX)（市场原始数据，匹配分=100，来源ID=MK05）
22. [op7418/Humanizer-zh | ⭐ 2932](https://github.com/op7418/Humanizer-zh)（GitHub，匹配分=100，来源ID=GH05）
23. [BlockRunAI/ClawRouter | ⭐ 2337](https://github.com/BlockRunAI/ClawRouter)（GitHub，匹配分=100，来源ID=GH06）
24. [mindfold-ai/Trellis | ⭐ 2187](https://github.com/mindfold-ai/Trellis)（GitHub，匹配分=100，来源ID=GH07）
25. [2026-02-13T05:57 @StoneJAlex | Why in the world is this woman talking about the stock market? She’s the Attorney Genera...](https://twitter.com/StoneJAlex/status/2021829082862784790)（Twitter，匹配分=100，来源ID=TW10）
26. [2026-02-13T05:57 @Lush_Beauty1 | 1. ChatGPT = solve any problem 2. PicWish = remove backgrounds 3. Descript = edit podcas...](https://twitter.com/Lush_Beauty1/status/2021891789267890190)（Twitter，匹配分=100，来源ID=TW11）
27. [2026-02-13T05:57 @jzux | remember: they want you to think AI is inevitable so they scare you into using it. AI do...](https://twitter.com/jzux/status/2022037403062743284)（Twitter，匹配分=100，来源ID=TW13）
28. [2026-02-13T05:57 @moonshot | “why didn’t you buy bitcoin in 2012” me in 2012:](https://twitter.com/moonshot/status/2021960073602638045)（Twitter，匹配分=100，来源ID=TW06）
29. [2026-02-12 21:35 新浪网 | 央行明日开展1万亿买断式逆回购操作，分析师：降准必要性降低 - 新浪网](https://news.google.com/rss/articles/CBMiwglBVV95cUxPZVdwT09vSjFMeVViSGhldTJjMG9Qd0VrTHM4RnRlRVFuNzdhaUV4T0VIVGE2djdwOVdXWk5nMXJDR2pmZm1UbkY0R0JueGZibkVpOTZoMG5HX1luUUNLbFBrcnJHMTFkYXdZTFlqQVRFRmlhTDR6TGQ1UnJZNERjclN2ZmJiUmhhTzd4cngwQXB5QmVqdFVncHJaaUpwR2JVci0zZEVOM3NnejU4bWNDc3drQjF6ZXNQdUhxbTNKaUtPMEQyY2tNWVhSYmxWZWZXcUN6TTZqeE1SYmhtUEVyNHE2Q1FCRUk3YkNTVlhhR2QycmowNHVUQ2FNcnY4WHRfUzljMm9tQUhKMklnZkl2TDJQWDY3anVWVm9tMldxMFVzTGFSTjU5eWNGbEV5Yk41V3lteUtQb1dqeTBvdDhKeDhTeWxJUmVySkNDOEJSZ0k5WlJRcl90RlVtMFhkbFYwSG80aVMtN3BNalRyOUxycXpPeVFnWktPdkdGQ05wOEI4UGFJenAzSF9aLTYxbk9JNDVGaGZhZDdkNkRFa0hXaUVadDJsM0t6TGZIWS1ySm5DczNPYVVlNUhfS0VjUjFlTXlRdWo0cElocUw4d3U4bEkxaTFTRURUQmRTVlNQb1libENZTFVwbkpiWUFnaDU4S3pSLVA5aGxaWUpGRU9ReTRKQzJyUDM3em40Rk1mQ1Y1bkJaM1dNZjVCeGJtNmNtY3RnMDJsM0k1YWZQQ0phR1Faa1E1ZDNPTzNITHBrdzR3aE1GSHE4dXMwdGI1LV9WYktJbE5uSXB1anB3WWdoNE9Ma2JMazFrVExNd2NET1NFR2ZiZ3FodjM4OWh2amplb1RvOXZkOWFmekN3Sm1JOVgxd3JHSEZzeVFqMDkycW41bVFHZ2NqNXdNWmk2TnFlczBubVlvTXVubHkwTFZzdG5TaGg1Z1c0ZWE2LUE1MEZlTWozZE5nQkMxTzhmNDVpaVo5aHppOElWMzdrMDV6c2g4RGhLZzA2UTBoSUowaWxhVmJmVy0zRUdrRGVZN0J4VzZqaTdiWjI5a0wwUHdNeUdqTHd4X004YWUxbVoyOVBhd280NkRIaUJfTzlZQ3l1ajlDbmtKQmlFbFEzQ0V0NG5JeEhGMldIbm5ydlhXYkFGMTVUZHVIdnpWNnJCNzJUZ0libGQwZGxjQ0VISTdtejFDSWstclBRcVl1WGRteHlBRElfdFFHVFZrZzdjMDd3Nkx2UkVrMDlHRWplVTVxcDAybEEybkNxdk5WTWowY1R4MzB0Y0g4czN4RU9JaWVKaHJjM1B2QzFudC1GM3AtMUppVXUxbURfcndwUWxUNmF3dkhaTEZRellGcVZLa3ZBb2RLRFoxX3M3SWZHYmxmX25oM0pDV1FTVWxSMkloMjBndVR0Xy1zdlY0Q0RybURYdDVWcE0zY0tsYXI4TDdqdU9BcVlxbUh0RmRZc0cta1ZmdUNtS1o0UXJ2SVVVaTNTUWx6Qm96ZlBKdkZSSDN2WTMtQkNqY1NLQ0hHdFROT3plXzBOalJ0bUxjbmlOdlRyYXR2Y0VZQ3hrTDNmZ1JITEk3MmpjelVqXzc4b1Q3djhYZVFLWTNtdC1PNFRpZFl6VXc?oc=5)（联网检索，匹配分=100，来源ID=WB13）
30. [2026-02-13 13:10 手机新浪网 | OpenAI指控DeepSeek侵权_新浪新闻 - 手机新浪网](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1GSmZxeUNvbFBvMF9vMU8zUFRFQXZzb21NbU5kNzlQaFhvcmh1dGlBcEpiaTNhYVluVDhURUlMUXBzYmltQ3hSVW1Ta2FxYmlmWVUxSFlkRXdUN1o2Y05SN1ltMA?oc=5)（联网检索，匹配分=100，来源ID=WB17）
31. [2026-02-14 05:31 英为财情 Investing.com | 美国股市涨跌不一；截至收盘道琼斯工业平均指数上涨0.10% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxQXy1BaHYxdktCYXBkSmUzT3J1MnBxQ0JGTFFoNVFDdDRSa0toM0tIM21RVGZ3YUxXQmN1TDhEZXh0dWZXY0ljcnlscHJBR05zYjFmeHdLcndmcldFN2tVQkY3a0kzOVNIOG9jaFZfWDlVanduR0o0elFfUElZRFpYbg?oc=5)（联网检索，匹配分=100，来源ID=WB09）
32. [华尔街见闻 #3 | 华尔街见闻早餐FM-Radio | 2026年2月12日](https://wallstreetcn.com/articles/3765542)（NewsNow热榜，匹配分=40）
33. [2026-02-13 20:11 新浪网 | 央行节前发布重要数据：社融增量7.22万亿元 - 新浪网](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVhxamF5ajMyYmdxLXhhc2ZHYkJkTlJhLURpZk1xQXpOY1BQZTJKdE5vcTFxX1dNZXdueS1XLTlIOVZOcWNvTFhfb0dtWXQ2ajl6QUJOb2NVLWI5YjZyNmR4SGRpT043UHpiOUJKUEhiRDQxdzdFckVuRUptdS1kdHQ4RkptQk5vUl82SnA0dXN3bUxYbkhrbg?oc=5)（联网检索，匹配分=100，来源ID=WB12）

## 🧪 引用匹配校验

- 已匹配引用条数: 33
- 未完成匹配标签: 0
- 低置信引用条数: 0
- 处理建议: 本次未发现低置信引用。

## 🎯 投机方向（超短）

- A股强势方向：船舶制造 +3.66%，龙头 亚星锚链
- 高波动资产：ETH 24h +3.17%（轻仓快进快出）
- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。

## 🌐 联网检索补充

- 关键词：2026-02-13 全球市场 盘面 复盘 原因, 2026-02-13 中国 宏观 经济 政策 市场 影响, 2026-02-13 AI 科技 行业 动态 影响, VIX波动率指数 上涨 原因, ETH 上涨 原因, 华尔街见闻早餐FM-Radio | 2026年2月12日 事件 背景, 圆脸谈加拿大校园枪击致10死 事件 背景, 强劲非农打击降息预期，AI担忧拖累美股指，美债承压，金银涨，原油冲高回落 事件 背景
- 命中结果：20 条（按发布时间倒序）

### 🔎 VIX波动率指数 上涨 原因

- [道指标普录得3个月最差单周，亚马逊九连阴，英伟达苹果跌超2%，黄金夺回5000美元 - 新浪财经](https://news.google.com/rss/articles/CBMibkFVX3lxTE5taUw3Uzd4aWVRcF9hR3B6NWpuQ2NiYmJvMkViZVVHLVpmb0JFSDd3c1Itb0xmbnk5NzRndEFGeXRmbERaOVdNX3k2V0U3OEViVGhYZ1pQREdXU1B0Q1AzNHJaQjhkaDgtMHpZUWZn?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-14 07:16
  - 摘要: 道指标普录得3个月最差单周，亚马逊九连阴，英伟达苹果跌超2%，黄金夺回5000美元 新浪财经
- [美国股市涨跌不一；截至收盘道琼斯工业平均指数上涨0.10% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxQXy1BaHYxdktCYXBkSmUzT3J1MnBxQ0JGTFFoNVFDdDRSa0toM0tIM21RVGZ3YUxXQmN1TDhEZXh0dWZXY0ljcnlscHJBR05zYjFmeHdLcndmcldFN2tVQkY3a0kzOVNIOG9jaFZfWDlVanduR0o0elFfUElZRFpYbg?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-14 05:31
  - 摘要: 美国股市涨跌不一；截至收盘道琼斯工业平均指数上涨0.10% 提供者 Investing.com 英为财情 Investing.com
- [印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.30% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxOOFVwdXJrMWltM20zd3ZoUjgxRC1OTE1jZlZvVGJkcnlGRzhEenJPemVMQk9SamctR3R6bHVOOUFqM2RpbU96Wk9pWS02SlVybGtPWlQ0bzV5al8xbkRRUjdLSkRaemRnZVRMWFFyaFNyZ0pwZEhuZ3YxMEREa3lrSw?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-13 18:30
  - 摘要: 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.30% 提供者 Investing.com 英为财情 Investing.com
- [金银巨震，美股重挫 - 同花顺财经](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBaNUR1OE9kekMzNUxHSm41MHl5MU5Ybk1KUzAwNGFqTXl2RE03d3JoT0lxSmhTWkVWYk9XSWswX3dwZjkycFRvZDhQYUJYZUEtOEI3LUlHcHhEYTB1T2c?oc=5)
  - 来源: 同花顺财经 | 时间: 2026-02-13 09:35
  - 摘要: 金银巨震，美股重挫 同花顺财经
- [金银、股集体下挫，恐慌指数VIX飙升，三倍做空纳指ETF涨超6% - 富途牛牛](https://news.google.com/rss/articles/CBMipwFBVV95cUxQMkx2ZjF0WHJPVjNoQm5hNXhpVjZEMnF3ODRuWm5UOFhKWnlObTlWR25qQUpfZ1dYQk1rUmt2OFcxZWwyYjFBaTh2UDBBdDJnYXVZUW9PTTRqcGluV1VWRnJ2dWhEQUpobTZ4S3FFdHBvWmtJS3NMUWJ1SW5Xb1poWmhfUjhjVkJsNGtFUkNxbnVBQ014YU41aEw0ZHpvNHJsbl9aczk4dw?oc=5)
  - 来源: 富途牛牛 | 时间: 2026-02-13 06:34
  - 摘要: 金银、股集体下挫，恐慌指数VIX飙升，三倍做空纳指ETF涨超6% 富途牛牛
- [美股走势分化凸显AI焦虑，就业利好难掩科技板块抛压 - NAI500](https://news.google.com/rss/articles/CBMi1AJBVV95cUxQQmNzbEdYQnRCZlhrSzFORDdoOUNBNjNOb3NGakhqdElUVVMxT0h3cndSQ2ZldUtadVdmVk5CcHFSdmtsR3FsdkNwOG9QVUhPSDlvem1ZUElZaVFrbXItemRPN3FPSmltbXBiaVVJSXZPSFY5Z0ZqS3pHZF9KaGZLZk9YMVVReGdtaWRRQzFPTmJDRUJIT2FjbGR1bzJrN0RQSGRoSXJobHo2LTRod1pWTHZhcEdEZWZwamRLSWxyVmhwRXhIYVB3Mnd4V2pYSURQeWtyZFBmWEJUd2REMV9RT1B3MklNY3hlekNWRW9Mc3FTdTN0SDVrZ0tsalZ2TDlhS1hfeW9VVGd4MS13Wi1WMWcteDMyUUFVaWR2dENSZElOcXBZS1pReU9sVkNDaF9sY3NwX1AxclNYTnk0U3FGQXc4LXp6MXQ0RVQwQktqVTdQUlc5?oc=5)
  - 来源: NAI500 | 时间: 2026-02-12 12:09
  - 摘要: 美股走势分化凸显AI焦虑，就业利好难掩科技板块抛压 NAI500

### 🔎 2026-02-13 中国 宏观 经济 政策 市场 影响

- [金融股市场动态：建设银行美股表现如何？ - SOHU](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOUFFYUzlxbkZteWE1TE5jZzl3S3BpcUY5TDU2Z20yeHl2a20tLW1RQWlwSXBMSU9WcnRmNnpWVWFNS2RlenItYlg5VTNqS3RpeG95S0VVS1l3LWtxclQ5eTJnVV9LTXFsVWN0U2JqN2pPTUFKWGNTcF9pUTdGeUdrd1N1Z3BTOW10LUNV?oc=5)
  - 来源: SOHU | 时间: 2026-02-14 06:06
  - 摘要: 金融股市场动态：建设银行美股表现如何？ SOHU
- [央行节前发布重要数据：社融增量7.22万亿元 - 新浪网](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVhxamF5ajMyYmdxLXhhc2ZHYkJkTlJhLURpZk1xQXpOY1BQZTJKdE5vcTFxX1dNZXdueS1XLTlIOVZOcWNvTFhfb0dtWXQ2ajl6QUJOb2NVLWI5YjZyNmR4SGRpT043UHpiOUJKUEhiRDQxdzdFckVuRUptdS1kdHQ4RkptQk5vUl82SnA0dXN3bUxYbkhrbg?oc=5)
  - 来源: 新浪网 | 时间: 2026-02-13 20:11
  - 摘要: 央行节前发布重要数据：社融增量7.22万亿元 新浪网
- [人民币延续升值趋势，中国资产受益链条明晰 - 证券之星](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBPR0ZDSlctc0lTVGRacGV1dnRPQ0k0QUpTU25iR1daVlBLOUtwMmNoQjNSNngydHJ2b285M0VweVpLdjZoNlpUUFZLd3pJcy14S0E2bjY1VVZQaFVUc1ZBejZNUDE?oc=5)
  - 来源: 证券之星 | 时间: 2026-02-13 07:43
  - 摘要: 人民币延续升值趋势，中国资产受益链条明晰 证券之星
- [10000亿元！央行最新预告 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE9YdzVUY0d1Ymk5SlZiWkJBMDN3OHktb3d4UFl4WWpuTE5rLWxJcGEybG5HRUItb1R6YnBEV2FicDZpV3g2Y0xKdC0xWU5MVm8tb3RyWmRQTnVqSFZUZXdSM0ZHSFFBMUJ1QWlJc09MU25kSzltbmJDeA?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-13 00:17
  - 摘要: 10000亿元！央行最新预告 新浪财经
- [央行明日开展1万亿买断式逆回购操作，分析师：降准必要性降低 - 新浪网](https://news.google.com/rss/articles/CBMiwglBVV95cUxPZVdwT09vSjFMeVViSGhldTJjMG9Qd0VrTHM4RnRlRVFuNzdhaUV4T0VIVGE2djdwOVdXWk5nMXJDR2pmZm1UbkY0R0JueGZibkVpOTZoMG5HX1luUUNLbFBrcnJHMTFkYXdZTFlqQVRFRmlhTDR6TGQ1UnJZNERjclN2ZmJiUmhhTzd4cngwQXB5QmVqdFVncHJaaUpwR2JVci0zZEVOM3NnejU4bWNDc3drQjF6ZXNQdUhxbTNKaUtPMEQyY2tNWVhSYmxWZWZXcUN6TTZqeE1SYmhtUEVyNHE2Q1FCRUk3YkNTVlhhR2QycmowNHVUQ2FNcnY4WHRfUzljMm9tQUhKMklnZkl2TDJQWDY3anVWVm9tMldxMFVzTGFSTjU5eWNGbEV5Yk41V3lteUtQb1dqeTBvdDhKeDhTeWxJUmVySkNDOEJSZ0k5WlJRcl90RlVtMFhkbFYwSG80aVMtN3BNalRyOUxycXpPeVFnWktPdkdGQ05wOEI4UGFJenAzSF9aLTYxbk9JNDVGaGZhZDdkNkRFa0hXaUVadDJsM0t6TGZIWS1ySm5DczNPYVVlNUhfS0VjUjFlTXlRdWo0cElocUw4d3U4bEkxaTFTRURUQmRTVlNQb1libENZTFVwbkpiWUFnaDU4S3pSLVA5aGxaWUpGRU9ReTRKQzJyUDM3em40Rk1mQ1Y1bkJaM1dNZjVCeGJtNmNtY3RnMDJsM0k1YWZQQ0phR1Faa1E1ZDNPTzNITHBrdzR3aE1GSHE4dXMwdGI1LV9WYktJbE5uSXB1anB3WWdoNE9Ma2JMazFrVExNd2NET1NFR2ZiZ3FodjM4OWh2amplb1RvOXZkOWFmekN3Sm1JOVgxd3JHSEZzeVFqMDkycW41bVFHZ2NqNXdNWmk2TnFlczBubVlvTXVubHkwTFZzdG5TaGg1Z1c0ZWE2LUE1MEZlTWozZE5nQkMxTzhmNDVpaVo5aHppOElWMzdrMDV6c2g4RGhLZzA2UTBoSUowaWxhVmJmVy0zRUdrRGVZN0J4VzZqaTdiWjI5a0wwUHdNeUdqTHd4X004YWUxbVoyOVBhd280NkRIaUJfTzlZQ3l1ajlDbmtKQmlFbFEzQ0V0NG5JeEhGMldIbm5ydlhXYkFGMTVUZHVIdnpWNnJCNzJUZ0libGQwZGxjQ0VISTdtejFDSWstclBRcVl1WGRteHlBRElfdFFHVFZrZzdjMDd3Nkx2UkVrMDlHRWplVTVxcDAybEEybkNxdk5WTWowY1R4MzB0Y0g4czN4RU9JaWVKaHJjM1B2QzFudC1GM3AtMUppVXUxbURfcndwUWxUNmF3dkhaTEZRellGcVZLa3ZBb2RLRFoxX3M3SWZHYmxmX25oM0pDV1FTVWxSMkloMjBndVR0Xy1zdlY0Q0RybURYdDVWcE0zY0tsYXI4TDdqdU9BcVlxbUh0RmRZc0cta1ZmdUNtS1o0UXJ2SVVVaTNTUWx6Qm96ZlBKdkZSSDN2WTMtQkNqY1NLQ0hHdFROT3plXzBOalJ0bUxjbmlOdlRyYXR2Y0VZQ3hrTDNmZ1JITEk3MmpjelVqXzc4b1Q3djhYZVFLWTNtdC1PNFRpZFl6VXc?oc=5)
  - 来源: 新浪网 | 时间: 2026-02-12 21:35
  - 摘要: 央行明日开展1万亿买断式逆回购操作，分析师：降准必要性降低 新浪网

### 🔎 ETH 上涨 原因

- [Ethereum 价格预测（2026、2027、2028-2032 年） - Cryptopolitan](https://news.google.com/rss/articles/CBMib0FVX3lxTE1sSGFYRTBCTFNocFJzZ0JiZFo3MlRNUXQ5VUFSdkkzY05yY1pFVmlsclE3bEhWSVk4Mm5oaWNEVHhtX1N5SlREczNJaS01M0VqaEhoYXNnU3NfeEdNOFBfQXQ3OVlwX0ZWMlJHTTFRbw?oc=5)
  - 来源: Cryptopolitan | 时间: 2026-02-14 04:01
  - 摘要: Ethereum 价格预测（2026、2027、2028-2032 年） Cryptopolitan
- [超过30%的供应被锁定：以太坊质押潮在价格触底周期中创下纪录| Htp96发布于币安广场 - Binance](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5)
  - 来源: Binance | 时间: 2026-02-13 23:39
  - 摘要: 超过30%的供应被锁定：以太坊质押潮在价格触底周期中创下纪录| Htp96发布于币安广场 Binance
- [Uniswap 巨鲸在由 BlackRock 推动的 42% 暴涨中抛售 2700 万美元 - Yellow.com](https://news.google.com/rss/articles/CBMimwJBVV95cUxPdmZhXzBOZ3pITDdiTHhoQXFIeEMtS2Y2dmkzYjBnMnJSS1NxalRMTy1TR3ZwaGJIWmgwdTBmVnlEWG40OGZoNTJhREhYd0JBM2ppQkdlU3RZNmdGdmVYR0JsVXQ3RVZSVHFuRjBzMjUzVEt5VzZhaGtUZEVzdjZxRnUteUh4b21zTDZEajhKT2tRUnJrSmU0NFFOeVNPcmhmOE5QLWJhYTUzdWRBSHhzVG1iUFY4SE1na25UTk5HR2FyR0JRTnQwVF80VkFoUTcyWGRhTFM1SXZhVWZXSEkzRDlDWGJFMGVEdklhYWdLUVV1cVdUNmtvcnFfTDhWcXIwaU5ldkdwc0FHN0cwV3pLRUd2X204WmpxbVhR?oc=5)
  - 来源: Yellow.com | 时间: 2026-02-12 15:50
  - 摘要: Uniswap 巨鲸在由 BlackRock 推动的 42% 暴涨中抛售 2700 万美元 Yellow.com

### 🔎 2026-02-13 AI 科技 行业 动态 影响

- [财经资讯AI速递：昨夜今晨财经热点一览 丨2026年2月13日 - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMidEFVX3lxTFBlVDM4dDBnOVdjMW90TkZBZTVBR3BjSXF3V3JOUWtKTjBmR2tMWHo4d09nMTR0ZmpxTXNnbTVpdC16ZXJTb0t5bm9qODd6WjdnTDBNdjRqY0FoN0JzUDl0amRzUVowbkdTYW50Rmo4dnkyTEw5?oc=5)
  - 来源: 新浪新闻_手机新浪网 | 时间: 2026-02-13 22:48
  - 摘要: 财经资讯AI速递：昨夜今晨财经热点一览 丨2026年2月13日 新浪新闻_手机新浪网
- [科技资讯AI速递：昨夜今晨科技热点一览 丨2026年2月13日 - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMidEFVX3lxTE5iTFRnUEc1MTZXQ2ptend5TEh0Y0FmWDcyZTA1MWFBWTlNNTEwMExJXy0ySVREUl9DUEI0MDUwY3JMd0FfVUtNWTB0SURkZXlnRzNWX18wa3ZnUFJPTWlET1hPQ2EyRVFOMW42YWV4cXE1NlVn?oc=5)
  - 来源: 新浪新闻_手机新浪网 | 时间: 2026-02-13 22:26
  - 摘要: 科技资讯AI速递：昨夜今晨科技热点一览 丨2026年2月13日 新浪新闻_手机新浪网
- [美股三连跌 “AI替代”恐慌情绪从科技蔓延至物流、地产等板块 - 财新](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)
  - 来源: 财新 | 时间: 2026-02-13 22:13
  - 摘要: 美股三连跌 “AI替代”恐慌情绪从科技蔓延至物流、地产等板块 财新
- [OpenAI指控DeepSeek侵权_新浪新闻 - 手机新浪网](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1GSmZxeUNvbFBvMF9vMU8zUFRFQXZzb21NbU5kNzlQaFhvcmh1dGlBcEpiaTNhYVluVDhURUlMUXBzYmltQ3hSVW1Ta2FxYmlmWVUxSFlkRXdUN1o2Y05SN1ltMA?oc=5)
  - 来源: 手机新浪网 | 时间: 2026-02-13 13:10
  - 摘要: OpenAI指控DeepSeek侵权_新浪新闻 手机新浪网
- [2月13日收盘：美股收跌纳指下跌2% AI发展令多个行业承压 - 新浪财经](https://news.google.com/rss/articles/CBMihwFBVV95cUxOVEhzbFF0bFphZ3pvTDJ6bXBHWlVDTDA2QzdId2VDZWdSY1VnMmFadmROVnplT1Z5b0oyNW1xdXB4RG5hc2RmRU4tM1FRNUxsR0tfYjRudkY5Wk9kYmxnYkQxU19IdVhYRHVwZGFud1dkZjI2eHdWTTNxdlJ3ZGpsd3Jia3RxQzg?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-13 05:11
  - 摘要: 2月13日收盘：美股收跌纳指下跌2% AI发展令多个行业承压 新浪财经

### 🔎 2026-02-13 全球市场 盘面 复盘 原因

- [港股复盘 | 年内最强新股诞生 “AI除幻第一股”海致科技集团港股上市首日涨超242% - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-13 17:50
  - 摘要: 港股复盘 | 年内最强新股诞生 “AI除幻第一股”海致科技集团港股上市首日涨超242% 新浪财经

## 🔗 AI 分析引用来源

> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。

### Twitter (8 条)

- [¹] [2026-02-13T05:57 @TVietor08 | The stock market is up so we don’t have to prosecute pedophiles is one of the worst poli...](https://twitter.com/TVietor08/status/2021705825216278670)（匹配分=100，来源ID=TW01）
- [²] [2026-02-13T05:57 @AdameMedia | BREAKING: 🇺🇸 🇮🇱 Pam Bondi starts talking about stock market gains during her testimony o...](https://twitter.com/AdameMedia/status/2021639407984656769)（匹配分=100，来源ID=TW02）
- [³] [2026-02-13T05:57 @MikeNellis | “The stock market is up, so I don’t have to investigate pedophiles and sex traffickers” ...](https://twitter.com/MikeNellis/status/2021742758956826875)（匹配分=100，来源ID=TW07）
- [⁴] [2026-02-13T05:57 @notthreadguy | does nobody care that the attorney general said under oath on national television the bi...](https://twitter.com/notthreadguy/status/2022018683586195484)（匹配分=100，来源ID=TW09）
- [²⁵] [2026-02-13T05:57 @StoneJAlex | Why in the world is this woman talking about the stock market? She’s the Attorney Genera...](https://twitter.com/StoneJAlex/status/2021829082862784790)（匹配分=100，来源ID=TW10）
- [²⁶] [2026-02-13T05:57 @Lush_Beauty1 | 1. ChatGPT = solve any problem 2. PicWish = remove backgrounds 3. Descript = edit podcas...](https://twitter.com/Lush_Beauty1/status/2021891789267890190)（匹配分=100，来源ID=TW11）
- [²⁷] [2026-02-13T05:57 @jzux | remember: they want you to think AI is inevitable so they scare you into using it. AI do...](https://twitter.com/jzux/status/2022037403062743284)（匹配分=100，来源ID=TW13）
- [²⁸] [2026-02-13T05:57 @moonshot | “why didn’t you buy bitcoin in 2012” me in 2012:](https://twitter.com/moonshot/status/2021960073602638045)（匹配分=100，来源ID=TW06）

### NewsNow热榜 (3 条)

- [⁵] [华尔街见闻 #4 | 强劲非农打击降息预期，AI担忧拖累美股指，美债承压，金银涨，原油冲高回落](https://wallstreetcn.com/articles/3765486)（匹配分=100，来源ID=NW03）
- [⁶] [华尔街见闻 #5 | “下一个AI受害者”出现了，房地产服务股遭抛售，创疫情以来最大单日跌幅](https://wallstreetcn.com/articles/3765544)（匹配分=100，来源ID=NW04）
- [³²] [华尔街见闻 #3 | 华尔街见闻早餐FM-Radio | 2026年2月12日](https://wallstreetcn.com/articles/3765542)（匹配分=40）

### GitHub (6 条)

- [¹²] [coreyhaines31/marketingskills | ⭐ 7525](https://github.com/coreyhaines31/marketingskills)（匹配分=100，来源ID=GH01）
- [¹³] [Leey21/awesome-ai-research-writing | ⭐ 5697](https://github.com/Leey21/awesome-ai-research-writing)（匹配分=100，来源ID=GH02）
- [¹⁴] [blader/humanizer | ⭐ 4751](https://github.com/blader/humanizer)（匹配分=100，来源ID=GH03）
- [²²] [op7418/Humanizer-zh | ⭐ 2932](https://github.com/op7418/Humanizer-zh)（匹配分=100，来源ID=GH05）
- [²³] [BlockRunAI/ClawRouter | ⭐ 2337](https://github.com/BlockRunAI/ClawRouter)（匹配分=100，来源ID=GH06）
- [²⁴] [mindfold-ai/Trellis | ⭐ 2187](https://github.com/mindfold-ai/Trellis)（匹配分=100，来源ID=GH07）

### 市场原始数据 (8 条)

- [⁸] [Yahoo Finance 罗素2000 (^RUT)](https://finance.yahoo.com/quote/%5ERUT)（匹配分=100，来源ID=MK04）
- [¹⁰] [Yahoo Finance 纳斯达克综合 (^IXIC)](https://finance.yahoo.com/quote/%5EIXIC)（匹配分=100，来源ID=MK02）
- [¹⁶] [Yahoo Finance 标普500 (^GSPC)](https://finance.yahoo.com/quote/%5EGSPC)（匹配分=100，来源ID=MK01）
- [¹⁷] [Yahoo Finance 道琼斯工业指数 (^DJI)](https://finance.yahoo.com/quote/%5EDJI)（匹配分=100，来源ID=MK03）
- [¹⁸] [Yahoo Finance 恒生指数 (^HSI)](https://finance.yahoo.com/quote/%5EHSI)（匹配分=100，来源ID=MK06）
- [¹⁹] [Yahoo Finance 日经225 (^N225)](https://finance.yahoo.com/quote/%5EN225)（匹配分=100，来源ID=MK07）
- [²⁰] [Yahoo Finance 韩国综合指数 (^KS11)](https://finance.yahoo.com/quote/%5EKS11)（匹配分=100，来源ID=MK08）
- [²¹] [Yahoo Finance VIX波动率指数 (^VIX)](https://finance.yahoo.com/quote/%5EVIX)（匹配分=100，来源ID=MK05）

### 联网检索 (8 条)

- [⁷] [2026-02-13 22:13 财新 | 美股三连跌 “AI替代”恐慌情绪从科技蔓延至物流、地产等板块 - 财新](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)（匹配分=100，来源ID=WB08）
- [⁹] [2026-02-14 07:16 新浪财经 | 道指标普录得3个月最差单周，亚马逊九连阴，英伟达苹果跌超2%，黄金夺回5000美元 - 新浪财经](https://news.google.com/rss/articles/CBMibkFVX3lxTE5taUw3Uzd4aWVRcF9hR3B6NWpuQ2NiYmJvMkViZVVHLVpmb0JFSDd3c1Itb0xmbnk5NzRndEFGeXRmbERaOVdNX3k2V0U3OEViVGhYZ1pQREdXU1B0Q1AzNHJaQjhkaDgtMHpZUWZn?oc=5)（匹配分=100，来源ID=WB04）
- [¹¹] [2026-02-13 23:39 Binance | 超过30%的供应被锁定：以太坊质押潮在价格触底周期中创下纪录| Htp96发布于币安广场 - Binance](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5)（匹配分=100，来源ID=WB05）
- [¹⁵] [2026-02-13 17:50 新浪财经 | 港股复盘 | 年内最强新股诞生 “AI除幻第一股”海致科技集团港股上市首日涨超242% - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5)（匹配分=100，来源ID=WB11）
- [²⁹] [2026-02-12 21:35 新浪网 | 央行明日开展1万亿买断式逆回购操作，分析师：降准必要性降低 - 新浪网](https://news.google.com/rss/articles/CBMiwglBVV95cUxPZVdwT09vSjFMeVViSGhldTJjMG9Qd0VrTHM4RnRlRVFuNzdhaUV4T0VIVGE2djdwOVdXWk5nMXJDR2pmZm1UbkY0R0JueGZibkVpOTZoMG5HX1luUUNLbFBrcnJHMTFkYXdZTFlqQVRFRmlhTDR6TGQ1UnJZNERjclN2ZmJiUmhhTzd4cngwQXB5QmVqdFVncHJaaUpwR2JVci0zZEVOM3NnejU4bWNDc3drQjF6ZXNQdUhxbTNKaUtPMEQyY2tNWVhSYmxWZWZXcUN6TTZqeE1SYmhtUEVyNHE2Q1FCRUk3YkNTVlhhR2QycmowNHVUQ2FNcnY4WHRfUzljMm9tQUhKMklnZkl2TDJQWDY3anVWVm9tMldxMFVzTGFSTjU5eWNGbEV5Yk41V3lteUtQb1dqeTBvdDhKeDhTeWxJUmVySkNDOEJSZ0k5WlJRcl90RlVtMFhkbFYwSG80aVMtN3BNalRyOUxycXpPeVFnWktPdkdGQ05wOEI4UGFJenAzSF9aLTYxbk9JNDVGaGZhZDdkNkRFa0hXaUVadDJsM0t6TGZIWS1ySm5DczNPYVVlNUhfS0VjUjFlTXlRdWo0cElocUw4d3U4bEkxaTFTRURUQmRTVlNQb1libENZTFVwbkpiWUFnaDU4S3pSLVA5aGxaWUpGRU9ReTRKQzJyUDM3em40Rk1mQ1Y1bkJaM1dNZjVCeGJtNmNtY3RnMDJsM0k1YWZQQ0phR1Faa1E1ZDNPTzNITHBrdzR3aE1GSHE4dXMwdGI1LV9WYktJbE5uSXB1anB3WWdoNE9Ma2JMazFrVExNd2NET1NFR2ZiZ3FodjM4OWh2amplb1RvOXZkOWFmekN3Sm1JOVgxd3JHSEZzeVFqMDkycW41bVFHZ2NqNXdNWmk2TnFlczBubVlvTXVubHkwTFZzdG5TaGg1Z1c0ZWE2LUE1MEZlTWozZE5nQkMxTzhmNDVpaVo5aHppOElWMzdrMDV6c2g4RGhLZzA2UTBoSUowaWxhVmJmVy0zRUdrRGVZN0J4VzZqaTdiWjI5a0wwUHdNeUdqTHd4X004YWUxbVoyOVBhd280NkRIaUJfTzlZQ3l1ajlDbmtKQmlFbFEzQ0V0NG5JeEhGMldIbm5ydlhXYkFGMTVUZHVIdnpWNnJCNzJUZ0libGQwZGxjQ0VISTdtejFDSWstclBRcVl1WGRteHlBRElfdFFHVFZrZzdjMDd3Nkx2UkVrMDlHRWplVTVxcDAybEEybkNxdk5WTWowY1R4MzB0Y0g4czN4RU9JaWVKaHJjM1B2QzFudC1GM3AtMUppVXUxbURfcndwUWxUNmF3dkhaTEZRellGcVZLa3ZBb2RLRFoxX3M3SWZHYmxmX25oM0pDV1FTVWxSMkloMjBndVR0Xy1zdlY0Q0RybURYdDVWcE0zY0tsYXI4TDdqdU9BcVlxbUh0RmRZc0cta1ZmdUNtS1o0UXJ2SVVVaTNTUWx6Qm96ZlBKdkZSSDN2WTMtQkNqY1NLQ0hHdFROT3plXzBOalJ0bUxjbmlOdlRyYXR2Y0VZQ3hrTDNmZ1JITEk3MmpjelVqXzc4b1Q3djhYZVFLWTNtdC1PNFRpZFl6VXc?oc=5)（匹配分=100，来源ID=WB13）
- [³⁰] [2026-02-13 13:10 手机新浪网 | OpenAI指控DeepSeek侵权_新浪新闻 - 手机新浪网](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1GSmZxeUNvbFBvMF9vMU8zUFRFQXZzb21NbU5kNzlQaFhvcmh1dGlBcEpiaTNhYVluVDhURUlMUXBzYmltQ3hSVW1Ta2FxYmlmWVUxSFlkRXdUN1o2Y05SN1ltMA?oc=5)（匹配分=100，来源ID=WB17）
- [³¹] [2026-02-14 05:31 英为财情 Investing.com | 美国股市涨跌不一；截至收盘道琼斯工业平均指数上涨0.10% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxQXy1BaHYxdktCYXBkSmUzT3J1MnBxQ0JGTFFoNVFDdDRSa0toM0tIM21RVGZ3YUxXQmN1TDhEZXh0dWZXY0ljcnlscHJBR05zYjFmeHdLcndmcldFN2tVQkY3a0kzOVNIOG9jaFZfWDlVanduR0o0elFfUElZRFpYbg?oc=5)（匹配分=100，来源ID=WB09）
- [³³] [2026-02-13 20:11 新浪网 | 央行节前发布重要数据：社融增量7.22万亿元 - 新浪网](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVhxamF5ajMyYmdxLXhhc2ZHYkJkTlJhLURpZk1xQXpOY1BQZTJKdE5vcTFxX1dNZXdueS1XLTlIOVZOcWNvTFhfb0dtWXQ2ajl6QUJOb2NVLWI5YjZyNmR4SGRpT043UHpiOUJKUEhiRDQxdzdFckVuRUptdS1kdHQ4RkptQk5vUl82SnA0dXN3bUxYbkhrbg?oc=5)（匹配分=100，来源ID=WB12）

> 注：早报 AI 已按规则跳过 A 股盘面数据分析。


---

# 📋 原始数据

<a id="raw-market-data"></a>
## 📊 金融市场数据

### 🧭 股票总览

> 跟踪 **19** 个标的：上涨 **7** | 下跌 **12** | 平盘 **0** | 上涨占比 **36.8%**
> 区域强弱：美股 +0.82% (5/5) | 欧股 -0.02% (2/3) | 韩股 -0.28% (0/1) | 日股 -1.21% (0/1) | A股 -1.26% (0/8) | 港股 -1.72% (0/1)

### 🇨🇳 A股主要指数

| 指数 | 价格 | 涨跌幅 |
|------|------|--------|
| 上证指数 | 4082.07 | 🔴 -1.26% |
| 深证成指 | 14100.19 | 🔴 -1.28% |
| 沪深300 | 4660.41 | 🔴 -1.25% |
| 创业板指 | 3275.96 | 🔴 -1.57% |
| 科创50 | 1470.33 | 🔴 -0.72% |
| 中证500 | 8299.58 | 🔴 -1.47% |

### 📈 A股板块涨幅 TOP 15

| 板块 | 涨跌幅 | 换手率 | 领涨股 |
|------|--------|--------|--------|
| 船舶制造 | 🟢 +3.66% | 5.84% | 亚星锚链 |
| 航天航空 | 🟢 +2.21% | 3.31% | 安达维尔 |
| 综合行业 | 🟢 +0.63% | 2.38% | 国安股份 |
| 电机 | 🟢 +0.44% | 2.98% | 方正电机 |
| 计算机设备 | 🟢 +0.42% | 2.38% | 汉邦高科 |
| 造纸印刷 | 🟢 +0.39% | 2.42% | 五洲特纸 |
| 汽车零部件 | 🟢 +0.29% | 2.72% | 浙江世宝 |
| 旅游酒店 | 🟢 +0.22% | 2.05% | 金陵饭店 |
| 仪器仪表 | 🟢 +0.19% | 2.67% | 精测电子 |
| 半导体 | 🟢 +0.14% | 2.97% | 微导纳米 |
| 消费电子 | 🟢 +0.10% | 2.15% | 泰嘉股份 |
| 电子化学品 | 🟢 +0.04% | 3.73% | 中巨芯-U |
| 工程咨询服务 | 🟢 +0.03% | 2.43% | 华建集团 |
| 汽车服务 | 🔴 -0.07% | 1.15% | ST东时 |
| 塑料制品 | 🔴 -0.10% | 3.39% | 国风新材 |

### 📉 A股板块跌幅 TOP 15

| 板块 | 涨跌幅 | 换手率 | 领跌股 |
|------|--------|--------|--------|
| 非金属材料 | 🔴 -1.61% | 3.29% | 珂玛科技 |
| 游戏 | 🔴 -1.63% | 3.46% | 电魂网络 |
| 石油行业 | 🔴 -1.67% | 0.41% | *ST新潮 |
| 电力行业 | 🔴 -1.70% | 1.13% | 豫能控股 |
| 化肥行业 | 🔴 -1.79% | 1.95% | 农大科技 |
| 化纤行业 | 🔴 -1.93% | 1.29% | 南京化纤 |
| 能源金属 | 🔴 -1.94% | 3.78% | 盛新锂能 |
| 有色金属 | 🔴 -1.95% | 2.42% | 豪美新材 |
| 贵金属 | 🔴 -2.00% | 3.45% | 晓程科技 |
| 采掘行业 | 🔴 -2.10% | 1.98% | 仁智股份 |
| 钢铁行业 | 🔴 -2.36% | 1.66% | 大中矿业 |
| 航运港口 | 🔴 -2.55% | 1.03% | 海峡股份 |
| 玻璃玻纤 | 🔴 -2.62% | 5.03% | 海南发展 |
| 小金属 | 🔴 -2.97% | 3.08% | 天工股份 |
| 光伏设备 | 🔴 -3.06% | 4.72% | *ST天龙 |

### 💰 北向资金

| 项目 | 金额(亿元) |
|------|------------|
| net_flow | 🟢 0.00 |
| hu_net_flow | 🟢 0.00 |
| shen_net_flow | 🟢 0.00 |

### 🌍 全球股票概览（Yahoo Finance）

| 区域 | 指标 | 最新价 | 涨跌幅 | 币种 |
|------|------|--------|--------|------|
| 美股 | [标普500](https://finance.yahoo.com/quote/%5EGSPC) | 6,848.90 | 🟢 +0.24% | USD |
| 美股 | [纳斯达克综合](https://finance.yahoo.com/quote/%5EIXIC) | 22,634.21 | 🟢 +0.16% | USD |
| 美股 | [道琼斯工业指数](https://finance.yahoo.com/quote/%5EDJI) | 49,508.44 | 🟢 +0.11% | USD |
| 美股 | [罗素2000](https://finance.yahoo.com/quote/%5ERUT) | 2,639.62 | 🟢 +0.91% | USD |
| 美股 | [VIX波动率指数](https://finance.yahoo.com/quote/%5EVIX) | 21.38 | 🟢 +2.69% | USD |
| 港股 | [恒生指数](https://finance.yahoo.com/quote/%5EHSI) | 26,567.12 | 🔴 -1.72% | HKD |
| 日股 | [日经225](https://finance.yahoo.com/quote/%5EN225) | 56,941.97 | 🔴 -1.21% | JPY |
| 韩股 | [韩国综合指数](https://finance.yahoo.com/quote/%5EKS11) | 5,507.01 | 🔴 -0.28% | KRW |
| 欧股 | [英国富时100](https://finance.yahoo.com/quote/%5EFTSE) | 10,423.39 | 🟢 +0.20% | GBP |
| 欧股 | [德国DAX](https://finance.yahoo.com/quote/%5EGDAXI) | 24,887.93 | 🟢 +0.14% | EUR |
| 欧股 | [法国CAC40](https://finance.yahoo.com/quote/%5EFCHI) | 8,307.44 | 🔴 -0.40% | EUR |
| A股 | [上证综指](https://finance.yahoo.com/quote/000001.SS) | 4,082.07 | 🔴 -1.26% | CNY |
| A股 | [深证成指](https://finance.yahoo.com/quote/399001.SZ) | 14,100.19 | 🔴 -1.28% | CNY |

> 概览：上涨 7 | 下跌 6 | 平盘 0 | 总计 13

### 🥇 贵金属

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|

### ₿ 加密货币

| 币种 | 价格 | 24h涨跌 |
|------|------|---------|
| BTC | $68,736.00 | 🟢 +1.35% |
| ETH | $2,035.81 | 🟢 +3.17% |
| SOL | $82.90 | 🟢 +2.20% |

### 📈 股指期货

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|
| 沪深300期货 | 4627.0 | 🔴 -1.92% |
| 中证500期货 | 8274.8 | 🔴 -2.02% |
| 上证50期货 | 3020.0 | 🔴 -2.06% |
| 中证1000期货 | 8189.0 | 🔴 -1.75% |

### 📈 国际期货

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|
| WTI原油 | 62.7 | 🔴 -0.22% |
| 布伦特原油 | 67.52 | 🟢 +0.00% |
| 天然气 | 3.18 | 🔴 -1.24% |
| COMEX铜 | 5.75 | 🔴 -0.30% |

### 💻 GitHub 趋势

- ⭐ [**awesome-openclaw-usecases**](https://github.com/hesamsheikh/awesome-openclaw-usecases) (1933 stars)
  - A community collection of OpenClaw use cases for making life easier.
- ⭐ [**companion**](https://github.com/The-Vibe-Company/companion) (1798 stars)
  - Web & Mobile UI for Claude Code & Codex . Launch sessions, stream responses, app
- ⭐ [**peon-ping**](https://github.com/PeonPing/peon-ping) (1738 stars)
  - Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, and othe
- ⭐ [**secure-openclaw**](https://github.com/ComposioHQ/secure-openclaw) (1482 stars)
  - A personal 24x7 AI assistant like OpenClaw that runs on your messaging platforms
- ⭐ [**k-id-age-verifier**](https://github.com/xyzeva/k-id-age-verifier) (1276 stars)
  - automatically verify your age on discord, twitch, kick, quora and more (k-id)

## 🐦 Twitter 热点 (110 条)

- 来源统计: 关注账号 190 条 | 热门讨论 30 条

### 🔥 热门讨论推文

- `2026-02-13T05:57` @TVietor08 ❤️163913 🔁26545 💬824
  - The stock market is up so we don’t have to prosecute pedophiles is one of the worst political messages i have ever heard.
  - [原文链接](https://twitter.com/TVietor08/status/2021705825216278670)
- `2026-02-13T05:57` @AdameMedia ❤️137158 🔁27972 💬3879
  - BREAKING: 🇺🇸 🇮🇱 Pam Bondi starts talking about stock market gains during her testimony on her COVER UP of child trafficking.   This is fucking dystopian man.   Lock this demon up in a deep dark hole with Kash and Lutnick.
  - [原文链接](https://twitter.com/AdameMedia/status/2021639407984656769)
- `2026-02-13T05:57` @NotHoodlum ❤️137683 🔁16627 💬581
  - I didn’t realize we don’t pursue pedophiles if the stock market is doing well. Thank you, Pam Bondi, for that clarification.
  - [原文链接](https://twitter.com/NotHoodlum/status/2021618127570866444)
- `2026-02-13T05:57` @hashjenni ❤️105125 🔁11485 💬299
  - Imagine a little girl tells you an old man was sexually abusing her and your response is “yeah but the stock market.”
  - [原文链接](https://twitter.com/hashjenni/status/2021852693514658217)
- `2026-02-13T05:57` @Rep_Stansbury ❤️75073 🔁25191 💬4428
  - Admin Officials in the Epstein Files:  Donald J. Trump (President)  Melania Trump (1st Lady) Howard Lutnick (Sec. Commerce)  John Phelan (Sec. Navy) Paolo Zampolli (Kennedy Center) RFK Jr. (Sec. HHS)  Kevin Warsh (Fed Nominee) Mehmet Oz (Admin. for CMS) Elon Musk (Fmr DOGE Appointee) Steve Bannon (Fmr Senior Advisor) Alex Acosta (Fmr Sec. Labor) Bill Barr (Fmr AG) Brett Ratner (Film Director “Melania”) …
  - [原文链接](https://twitter.com/Rep_Stansbury/status/2021796092879184037)
- `2026-02-13T05:57` @moonshot ❤️31620 🔁6033 💬508
  - “why didn’t you buy bitcoin in 2012”  me in 2012:
  - [原文链接](https://twitter.com/moonshot/status/2021960073602638045)
- `2026-02-13T05:57` @MikeNellis ❤️28857 🔁4728 💬727
  - “The stock market is up, so I don’t have to investigate pedophiles and sex traffickers” is an insane defense by Pam Bondi.  She’s just as bad as every monster in the files.
  - [原文链接](https://twitter.com/MikeNellis/status/2021742758956826875)
- `2026-02-13T05:57` @ScottJenningsKY ❤️28566 🔁3716 💬1067
  - The government is shrinking. The private sector is growing. Wages are finally outpacing inflation.  And President Trump has only been in office for a year.  Let him cook.
  - [原文链接](https://twitter.com/ScottJenningsKY/status/2022063985647137241)
- `2026-02-13T05:57` @notthreadguy ❤️28268 🔁2682 💬184
  - does nobody care that the attorney general said under oath on national television the biggest scandal in american history doesn't matter because the stock market is green
  - [原文链接](https://twitter.com/notthreadguy/status/2022018683586195484)
- `2026-02-13T05:57` @StoneJAlex ❤️27077 🔁2895 💬932
  - Why in the world is this woman talking about the stock market? She’s the Attorney General of the United States of America. She’s totally unfit and should be fired.
  - [原文链接](https://twitter.com/StoneJAlex/status/2021829082862784790)
- `2026-02-13T05:57` @Lush_Beauty1 ❤️24626 🔁6101 💬99
  - 1. ChatGPT = solve any problem 2. PicWish = remove backgrounds 3. Descript = edit podcasts 4. Perplexity = research anything 5. ElevenLabs = clone voices 6. Gamma = design documents 7. Suno = compose music 8. Runway = edit videos 9. Canva = design graphics 10. RecCloud = summarize YouTube 11. Grammarly = perfect writing  Save this, it might come in handy.￼
  - [原文链接](https://twitter.com/Lush_Beauty1/status/2021891789267890190)
- `2026-02-13T05:57` @Uncommonsince76 ❤️24876 🔁5611 💬82
  - Wow! 🤯. This Irish media company found Jeffrey Epstein’s Fed Ex Account password, then logged as has him and saw packages have been shipped as recent as 2024…  Read this article. 👇
  - [原文链接](https://twitter.com/Uncommonsince76/status/2021656795694121334)
- `2026-02-13T05:57` @jzux ❤️15856 🔁3067 💬37
  - remember: they want you to think AI is inevitable so they scare you into using it. AI doesn't take over if we don't let it
  - [原文链接](https://twitter.com/jzux/status/2022037403062743284)
- `2026-02-13T05:57` @MAstronomers ❤️15335 🔁828 💬271
  - 🚨 AI detects breast cancer 5 years before it develops
  - [原文链接](https://twitter.com/MAstronomers/status/2021976195630305280)
- `2026-02-13T05:57` @VALOJPNews ❤️11108 🔁1825 💬17
  - Windows 11の更新プログラム「KB5074109」でFPSが大幅低下。NVIDIAスタッフも「更新プログラムのアンインストール」を解決策として言及valorantjp.com/News/3883
  - [原文链接](https://twitter.com/VALOJPNews/status/2021338610583339391)
- `2026-02-13T05:57` @isaiahrmartin ❤️10550 🔁1409 💬68
  - Do you realize how absurd it is the United States Attorney General started talking about the mf STOCK MARKET when she was asked about CHILD ABUSE?!?? THE STOCK MARKET?!?? Nothing shocks me anymore but that was insane!!!!
  - [原文链接](https://twitter.com/isaiahrmartin/status/2022041041067729140)
- `2026-02-13T05:57` @SidneyPowell1 ❤️6223 🔁3243 💬299
  - They seem to have no idea how fed up and angry the people who elected them are 🤬🤬@LeaderJohnThune@SenateGOP
  - [原文链接](https://twitter.com/SidneyPowell1/status/2022115221033410787)
- `2026-02-13T05:57` @goldfishggbr ❤️3281 🔁817 💬2626
  - Central banks are buying gold at rates not seen since the 1960s.   Inflation is persistent. Sovereign debt is at historic highs.  Why does this matter for on-chain gold?
  - [原文链接](https://twitter.com/goldfishggbr/status/2021972909074657656)
- `2026-02-13T05:57` @DC_Draino ❤️4490 🔁1701 💬167
  - Oh we know J6 was a Fed setup by Democrats, RINOs, and the Deep State to squash the MAGA movement.  Unfortunately for them, we only got bigger and stronger.
  - [原文链接](https://twitter.com/DC_Draino/status/2022089047087411499)
- `2026-02-13T05:57` @Manifest_Lord ❤️4994 🔁1064 💬118
  - A queen bee and a worker bee have identical DNA.  Literally the same genes.  But one lives 45 days. The other lives 7 years and rules 80,000 bees.  The difference? What they're fed for 5 days.  Here's the process that will blow your mind (and why it's relevant to humans): 🧵
  - [原文链接](https://twitter.com/Manifest_Lord/status/2021941471570801060)

### @CGTNOfficial (10 条)

- `2026-02-13T05:55` Live: As east China's Zhejiang prepares to host a sub-venue for the http://localhost/search?q=%23SpringFestival2026 Gala, Nanxun ancient town stands out as a luminous symbol of Jiangnan's timeless cultural allure and its spirit of cultural integration. http://localhost/search?q=%23ChineseNewYear htt
  - [原文链接](https://twitter.com/CGTNOfficial/status/2022187758773842430)
- `2026-02-13T05:30` http://localhost/search?q=%23Trump sets one-month window for http://localhost/search?q=%23Iran deal as Netanyahu voices skepticism https://news.cgtn.com/news/2026-02-13/Trump-sets-one-month-window-for-Iran-deal-as-Israel-voices-skepticism-1KIMTS5g59K/p.html
  - [原文链接](https://twitter.com/CGTNOfficial/status/2022181439656042998)
- `2026-02-13T05:29` A second U.S. aircraft carrier will sail from the Caribbean to the Middle East as President Trump weighs possible military action against Iran, AP reports.
  - [原文链接](https://twitter.com/CGTNOfficial/status/2022181370404253971)
- `2026-02-13T05:00` http://localhost/search?q=%23EpsteinFiles Britain's most senior government official, Chris Wormald, agreed with Prime Minister Keir Starmer to stand down, the third member of his team to go in recent days after the appointment of Peter Mandelson as U.S. ambassador threw the government into crisis. h
  - [原文链接](https://twitter.com/CGTNOfficial/status/2022173894090928515)
- `2026-02-13T04:30` U.S. judge: http://localhost/search?q=%23Trump's lawsuit against BBC to go to trial in February 2027  https://news.cgtn.com/news/2026-02-12/news-1KI3HWEHtTi/p.html
  - [原文链接](https://twitter.com/CGTNOfficial/status/2022166340199755995)
- *... 及其他 5 条*

### @CNBC (10 条)

- `2026-02-13T04:42` India approves Rafale jet purchase in $40 billion defense package ahead of Macron visit https://www.cnbc.com/2026/02/13/india-rafale-jets-dassault-39-billion-defense-package-macron-visit-france.html?taid=698eabc64fe0d800012acbf8&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=t
  - [原文链接](https://twitter.com/CNBC/status/2022169552952394138)
- `2026-02-13T03:03` CK Hutchison threatens legal action against Maersk as Panama Canal ports dispute escalates https://www.cnbc.com/2026/02/13/panama-ports-us-china-ck-hutchison-trump.html?taid=698e946891e5920001b9e714&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2022144465939451921)
- `2026-02-13T02:33` Xiaomi's electric SUV tops China sales in January, sells twice as many as Tesla's Model Y https://www.cnbc.com/2026/02/13/xiaomis-electric-suv-tops-china-sales-in-january-sells-twice-as-many-as-teslas-model-y.html?taid=698e8d6191e5920001b9e6d8&utm_campaign=trueanthem&utm_content=main&utm_medium=soci
  - [原文链接](https://twitter.com/CNBC/status/2022136918872367281)
- `2026-02-13T02:22` Waymo is paying DoorDash gig workers to close its robotaxi doors https://www.cnbc.com/2026/02/12/waymo-is-paying-doordash-gig-workers-to-close-its-robotaxi-doors.html?taid=698e8af392bc7f000143a423&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2022134309147013436)
- `2026-02-13T02:04` Epstein files: Goldman Sachs top lawyer Kathy Ruemmler to step down after email fallout https://www.cnbc.com/2026/02/12/epstein-files-goldman-sachs-kathy-ruemmler.html?taid=698e869492bc7f000143a415&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2022129617461486047)
- *... 及其他 5 条*

### @TechCrunch (10 条)

- `2026-02-13T04:42` Waymo is asking DoorDash drivers to shut the doors of its self-driving cars https://techcrunch.com/2026/02/12/waymo-is-asking-doordash-drivers-to-shut-the-doors-of-its-self-driving-cars/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2022169415538905449)
- `2026-02-12T23:45` For $1 million, you can pay Bryan Johnson (or BryanAI?) to teach you how to live longer https://techcrunch.com/2026/02/12/for-1-million-you-can-pay-bryan-johnson-or-bryanai-to-teach-you-how-to-live-longer/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2022094671905009692)
- `2026-02-12T23:31` Amid disappointing earnings, Pinterest claims it sees more searches than ChatGPT https://techcrunch.com/2026/02/12/amid-disappointing-earnings-pinterest-claims-it-sees-more-searches-than-chatgpt/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2022091242507796903)
- `2026-02-12T23:27` IBM will hire your entry-level talent in the age of AI https://techcrunch.com/2026/02/12/ibm-will-hire-your-entry-level-talent-in-the-age-of-ai/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2022090135400264014)
- `2026-02-12T23:23` Build Mode is back on February 19!   This season, we’re diving into what it takes to build a world-class founding team that will stick around to IPO and beyond. We’ve got a line-up of some exceptional guests from companies like http://localhost/Taskrabbit, http://localhost/Generalcatalyst, and http:
  - [原文链接](https://twitter.com/TechCrunch/status/2022089232286711973)
- *... 及其他 5 条*

### @zerohedge (10 条)

- `2026-02-13T04:25` Biggest Shorting Of Software Stocks Since 2010, As Goldman Cries "Nowhere To Hide Today" https://www.zerohedge.com/markets/biggest-shorting-software-stocks-2010-goldman-cries-nowhere-hide-today
  - [原文链接](https://twitter.com/zerohedge/status/2022165107946496239)
- `2026-02-13T04:00` Member Of Trump's 'Religious Liberty Commission' Fired After Heated Israel Debate https://www.zerohedge.com/geopolitical/battle-over-anti-semitism-definition-erupts-white-house-religious-liberty-hearing
  - [原文链接](https://twitter.com/zerohedge/status/2022158820923863237)
- `2026-02-13T03:47` After Hours:  AMAT +10%...big revs guide above on March qtr and “expect to grow our semiconductor equipment business over 20 percent this calendar year”  ABNB +1%...Solid beat and C26 " year-over-year revenue growth to accelerate to at least low double digits”  ANET +8%...Solid 1Q guide (4Q Revs +29
  - [原文链接](https://twitter.com/zerohedge/status/2022155724009132457)
- `2026-02-13T03:35` A Warning To Seattle: Don't Become The Next Cleveland https://www.zerohedge.com/political/warning-seattle-dont-become-next-cleveland
  - [原文链接](https://twitter.com/zerohedge/status/2022152530424172544)
- `2026-02-13T03:16` Golden shower parachutes  zerohedge (@zerohedge)  16 years of waiting for this kodak moment  — http://localhost/zerohedge/status/2022131748948353181#m
  - [原文链接](https://twitter.com/zerohedge/status/2022147734724288941)
- *... 及其他 5 条*

### @Sino_Market (10 条)

- `2026-02-13T03:28` 🇨🇳CHINEXT INDEX DOWN OVER 1%   http://localhost/search?q=%23CHINA http://localhost/search?q=%23SHCOMP http://localhost/search?q=%23SSEC http://localhost/search?q=%23ASHR http://localhost/search?q=%23HSI http://localhost/search?q=%23KWEB http://localhost/search?q=%23FXI http://localhost/search?q=%23H
  - [原文链接](https://twitter.com/Sino_Market/status/2022150741805478116)
- `2026-02-13T02:37` 🇭🇰HK AI STOCKS SHOW MIXED MOVES: HAIZHI TECH UP 224% ON DEBUT, MINIMAX-WP +10% (WEEK +42%), ABOVE HK$210 BN MARKET CAP. MEDBOT +9%. TENCENT MUSIC -9.5%, MOBVISTA -5%, MEITU -4%, BAIDU, MEITUAN, KINGSOFT CLOUD -3%   (https://mktnews.com/flashDetail.html?id=019c54d2-046c-7993-a1bf-1b298d92d262)
  - [原文链接](https://twitter.com/Sino_Market/status/2022138050428690619)
- `2026-02-13T02:20` 🇨🇳SHENZHEN FINANCIAL REGULATOR ISSUES PUBLIC NOTICE TO FURTHER STANDARDIZE GOLD MARKET OPERATIONS   SHENZHEN BANS ILLEGAL GOLD ACTIVITIES, INCLUDING PRE-SET PRICING, LEVERAGED, AND DEFERRED TRADING   http://localhost/search?q=%23CHINA http://localhost/search?q=%23GOLD http://localhost/search?q=%23SI
  - [原文链接](https://twitter.com/Sino_Market/status/2022133650922553520)
- `2026-02-13T01:43` ZHIPU, OR KNOWLEDGE ATLAS JUMPS OVER 13% TO FRESH POST-IPO HIGH; UP 123% THIS WEEK AFTER CODING PLAN SUBSCRIPTIONS SELL OUT.  http://localhost/search?q=%23CHINA http://localhost/search?q=%23ZHIPU http://localhost/search?q=%23GLM5 http://localhost/search?q=%23AI http://localhost/search?q=%23AICODING 
  - [原文链接](https://twitter.com/Sino_Market/status/2022124396119568641)
- `2026-02-13T01:42` CHINA JAN HOME PRICES IN 70 CITIES FALL M/M AT A SLOWER PACE, DOWN Y/Y – NBS  ALL CHINA JAN NEW HOME PRICES -0.4% M/M (DEC -0.4%) ,-3.1% Y/Y (DEC -2.7%)    (https://mktnews.com/flashDetail.html?id=019c549f-f599-7993-a1be-25e547880502)
  - [原文链接](https://twitter.com/Sino_Market/status/2022124171820683639)
- *... 及其他 5 条*

### @LynAldenContact (4 条)

- `2026-02-13T01:13` Cultures have many differing views of morality, but all around the world and for thousands of years, being truthful is arguably the most common one.  A culture cannot long persist on falsities. On open lying.  This cycle ends only when truth becomes principal currency again.
  - [原文链接](https://twitter.com/LynAldenContact/status/2022116819365245237)
- `2026-02-13T00:35` Three companies make nearly all of the RAM in the world and two of them are in Korea.  It's Korea's turn to be like:
  - [原文链接](https://twitter.com/LynAldenContact/status/2022107417946075284)
- `2026-02-12T19:35` It's pretty incredible that we have rolling catastrophes in sectors and single names and the index is sitting right below the highs.
  - [原文链接](https://twitter.com/LynAldenContact/status/2022031802370839012)
- `2026-02-12T19:20` Wild market. We haven't seen anything like this since the dotcom bubble burst.   Over the last 8 sessions, 115 stocks in the S&P 500 have decline 7% or more in a single day.   The average drawdown when that happens is 34%. Right now we're 1.5% below the all-time high.
  - [原文链接](https://twitter.com/LynAldenContact/status/2022028142630801786)

### @DefiLlama (1 条)

- `2026-02-13T00:05` Track token rights, utility, and alignment for dozens of protocols including Aave on our protocol Token Rights pages.  Aave (@aave)  Today we are proposing the Aave Will Win Framework, a new alignment framework that directs 100% of product revenue to the Aave DAO treasury under a token-centric model
  - [原文链接](https://twitter.com/DefiLlama/status/2022099781213131220)

### @elonmusk (7 条)

- `2026-02-13T00:01` From Day One, http://localhost/xai has been upgrading grid infrastructure and ensuring ratepayers don’t pick up our tab.   Today, we are continuing our commitment by installing our own power lines to power our MACROHARD facilities.
  - [原文链接](https://twitter.com/elonmusk/status/2022098797829210250)
- `2026-02-12T19:46` The most beautiful theorems    https://nitter.net/i/grok/share/958f49e427ce425381705784997881a7
  - [原文链接](https://twitter.com/elonmusk/status/2022034584536555592)
- `2026-02-12T19:40` Expansion of consciousness to understand the universe is the reason
  - [原文链接](https://twitter.com/elonmusk/status/2022032974070657289)
- `2026-02-12T19:38` 6 years ago  LilHumansBigImpact (@BigImpactHumans)  Elon was talking about a Moon base and Moon City back in 2020  — http://localhost/BigImpactHumans/status/2021950221090271665#m
  - [原文链接](https://twitter.com/elonmusk/status/2022032630221590983)
- `2026-02-12T19:34` Beauty in the subtle imperfections
  - [原文链接](https://twitter.com/elonmusk/status/2022031611387425234)
- *... 及其他 2 条*

### @PeterSchiff (4 条)

- `2026-02-12T23:10` Silver is trading back down at $74, almost 40% below its recent record high. It's a good time to buy some. http://www.schiffgold.com
  - [原文链接](https://twitter.com/PeterSchiff/status/2022085907684397065)
- `2026-02-12T19:41` Trump Revokes Obama-Era Greenhouse Gas Finding In "Largest Deregulatory Action" In U.S. History https://www.zerohedge.com/technology/largest-act-deregulation-us-history-trump-admin-repeal-obama-era-greenhouse-gas-finding
  - [原文链接](https://twitter.com/PeterSchiff/status/2022033264161042911)
- `2026-02-12T18:55` Existing home sales collapsed 8.4% in January, and 4.4% YoY. Sales are down in large part because prices are still much too high for buyers to afford. If the government does nothing, the crisis will be resolved with a major decline in home prices, causing a very different crisis.
  - [原文链接](https://twitter.com/PeterSchiff/status/2022021864496017441)
- `2026-02-12T18:18` Gold and silver got hit by a wave of selling. Gold is down $150 (3%) and silver is down $9, that’s over 11%. The Dow is also down over 1.3% and the NASDAQ over 1.6%. What's really amazing is that Bitcoin is barely down 1.5%. Sell Bitcoin now and buy silver.http://www.schiffgold.com
  - [原文链接](https://twitter.com/PeterSchiff/status/2022012372429443367)

### @dampedspring (7 条)

- `2026-02-12T22:50` H/t http://localhost/GRoditiD for the idea
  - [原文链接](https://twitter.com/dampedspring/status/2022080967784141108)
- `2026-02-12T22:48` On Jan 8th Trump ordered the GSE's to begin buying 200BN in MBS.  The impact was immediate as MBS spreads collapsed.  What was not known and probably not expected was whether the GSE's would hedge the accumulated duration which make the purchases neutral to the treasury market and which would be con
  - [原文链接](https://twitter.com/dampedspring/status/2022080343944114407)
- `2026-02-12T21:51` YTD ROW DM assets in common currency have crushed US assets  VEA up 9.65% SPY down 10bp  IGOV up 2.93% TLT up 2.37%  WIP up 4.11% TIP up 1.22%.
  - [原文链接](https://twitter.com/dampedspring/status/2022065968131059717)
- `2026-02-12T21:38` This thing works with dollar down but even works with dollar up
  - [原文链接](https://twitter.com/dampedspring/status/2022062890464006538)
- `2026-02-12T21:36` Today was a particularly good case and same with bonds
  - [原文链接](https://twitter.com/dampedspring/status/2022062391442518533)
- *... 及其他 2 条*

### @IanBremmer (3 条)

- `2026-02-12T21:21` macron says europe needs autonomy.  rutte says europe has no choice but america.  the truth is in between.  http://localhost/gzeromedia  Video
  - [原文链接](https://twitter.com/IanBremmer/status/2022058402428624930)
- `2026-02-12T19:30` i’ll take the over. but the fact that this is even remotely plausible should be the top issue on most everyone’s agenda…  Financial Times (@FT)  CEO of Microsoft AI Mustafa Suleyman joins FT editor Roula Khalaf to explain why most of the tasks accountants, lawyers and other professionals currently u
  - [原文链接](https://twitter.com/IanBremmer/status/2022030512756601251)
- `2026-02-12T18:13` 2026 munich security conference theme: “under destruction.”  many europeans believe the destruction is coming from the united states.  recognition is step one.  acting on it is another matter.  http://localhost/gzeromedia  Video
  - [原文链接](https://twitter.com/IanBremmer/status/2022011229561377110)

### @QuantaMagazine (2 条)

- `2026-02-12T20:24` You’ve heard the old real estate adage: Location, location, location! Bosilikja Tasic, a “biological cartographer,” says this is true for the brain too. Tasic used AI to build amazingly detailed maps of the mouse brain. “Location is everything,” she said. http://quantamagazine.org/fed-on-reams-of-ce
  - [原文链接](https://twitter.com/QuantaMagazine/status/2022044058764333368)
- `2026-02-12T20:09` Physicists sent a stream of electrons down a “de Laval" nozzle — a sleek shape that rocket engines use to accelerate their exhaust. A shock wave appeared — a surefire sign that electrons were flowing like a fluid. https://www.quantamagazine.org/physicists-make-electrons-flow-like-water-20260211/
  - [原文链接](https://twitter.com/QuantaMagazine/status/2022040285300113425)

### @karpathy (1 条)

- `2026-02-12T20:12` Congrats on the launch http://localhost/simile_ai ! (and I am excited to be involved as a small angel.)  Simile is working on a really interesting, imo under-explored dimension of LLMs. Usually, the LLMs you talk to have a single, specific, crafted personality. But in principle, the native, primordi
  - [原文链接](https://twitter.com/karpathy/status/2022041235188580788)

### @sama (1 条)

- `2026-02-12T18:15` GPT-5.3-Codex-Spark is launching today as a research preview for Pro.  More than 1000 tokens per second!  There are limitations at launch; we will rapidly improve.  Sam Altman (@sama)  We have a special thing launching to Codex users on the Pro plan later today. It sparks joy for me. I think you are
  - [原文链接](https://twitter.com/sama/status/2022011797524582726)

## 📱 微信公众号

暂无数据

## 🔥 NewsNow 热榜 (120 条)

### 华尔街见闻

| 排名 | 标题 |
|------|------|
| #3 | [华尔街见闻早餐FM-Radio \| 2026年2月12日](https://wallstreetcn.com/articles/3765542) |
| #4 | [强劲非农打击降息预期，AI担忧拖累美股指，美债承压，金银涨，原油冲高回落](https://wallstreetcn.com/articles/3765486) |
| #5 | [“下一个AI受害者”出现了，房地产服务股遭抛售，创疫情以来最大单日跌幅](https://wallstreetcn.com/articles/3765544) |
| #7 | [华尔街怎么看1月非农就业？首次降息延至7月，“新美联储通讯社”预计降息暂停期更久](https://wallstreetcn.com/articles/3765533) |

### bilibili 热搜

| 排名 | 标题 |
|------|------|
| #4 | [圆脸谈加拿大校园枪击致10死](https://search.bilibili.com/all?keyword=%E5%9C%86%E8%84%B8%E8%B0%88%E5%8A%A0%E6%8B%BF%E5%A4%A7%E6%A0%A1%E5%9B%AD%E6%9E%AA%E5%87%BB%E8%87%B410%E6%AD%BB) |
| #13 | [U17亚洲杯抽签出炉](https://search.bilibili.com/all?keyword=U17%E4%BA%9A%E6%B4%B2%E6%9D%AF%E6%8A%BD%E7%AD%BE%E5%87%BA%E7%82%89) |
| #24 | [王者新春版本内容速览](https://search.bilibili.com/all?keyword=%E7%8E%8B%E8%80%85%E6%96%B0%E6%98%A5%E7%89%88%E6%9C%AC%E5%86%85%E5%AE%B9%E9%80%9F%E8%A7%88) |
| #26 | [COS星铁阿哈开业发厕纸](https://search.bilibili.com/all?keyword=COS%E6%98%9F%E9%93%81%E9%98%BF%E5%93%88%E5%BC%80%E4%B8%9A%E5%8F%91%E5%8E%95%E7%BA%B8) |
| #22 | [用AI解锁吴克群将军令](https://search.bilibili.com/all?keyword=%E7%94%A8AI%E8%A7%A3%E9%94%81%E5%90%B4%E5%85%8B%E7%BE%A4%E5%B0%86%E5%86%9B%E4%BB%A4) |
| #8 | [建立太空数据中心有多难](https://search.bilibili.com/all?keyword=%E5%BB%BA%E7%AB%8B%E5%A4%AA%E7%A9%BA%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E6%9C%89%E5%A4%9A%E9%9A%BE) |
| #29 | [带放假的侄子旅游哀牢山](https://search.bilibili.com/all?keyword=%E5%B8%A6%E6%94%BE%E5%81%87%E7%9A%84%E4%BE%84%E5%AD%90%E6%97%85%E6%B8%B8%E5%93%80%E7%89%A2%E5%B1%B1) |
| #24 | [IEM克拉科夫集锦](https://search.bilibili.com/all?keyword=IEM%E5%85%8B%E6%8B%89%E7%A7%91%E5%A4%AB%E9%9B%86%E9%94%A6) |
| #26 | [喵喵的结合获IGN9分](https://search.bilibili.com/all?keyword=%E5%96%B5%E5%96%B5%E7%9A%84%E7%BB%93%E5%90%88%E8%8E%B7IGN9%E5%88%86) |
| #30 | [江寻千马年冰雕神兽龙马](https://search.bilibili.com/all?keyword=%E6%B1%9F%E5%AF%BB%E5%8D%83%E9%A9%AC%E5%B9%B4%E5%86%B0%E9%9B%95%E7%A5%9E%E5%85%BD%E9%BE%99%E9%A9%AC) |

### 澎湃新闻

| 排名 | 标题 |
|------|------|
| #8 | [家长反映“女儿遭教练体罚索财后坠楼”，校方：涉事两教练被警方立案调查](https://www.thepaper.cn/newsDetail_forward_32589244) |
| #19 | [岚目镜观｜从执政美国到选举美国：2026中期选举与“两个美国”的另一面相](https://www.thepaper.cn/newsDetail_forward_32584344) |

### 微博

| 排名 | 标题 |
|------|------|
| #10 | [孙龙](https://s.weibo.com/weibo?q=%E5%AD%99%E9%BE%99) |
| #19 | [短道速滑](https://s.weibo.com/weibo?q=%E7%9F%AD%E9%81%93%E9%80%9F%E6%BB%91) |
| #20 | [任子威说女子500米成绩夸张](https://s.weibo.com/weibo?q=%23%E4%BB%BB%E5%AD%90%E5%A8%81%E8%AF%B4%E5%A5%B3%E5%AD%90500%E7%B1%B3%E6%88%90%E7%BB%A9%E5%A4%B8%E5%BC%A0%23) |
| #24 | [摄影师曝檀健次拍摄几乎一条过](https://s.weibo.com/weibo?q=%23%E6%91%84%E5%BD%B1%E5%B8%88%E6%9B%9D%E6%AA%80%E5%81%A5%E6%AC%A1%E6%8B%8D%E6%91%84%E5%87%A0%E4%B9%8E%E4%B8%80%E6%9D%A1%E8%BF%87%23) |
| #25 | [刘少昂1000米无缘决赛](https://s.weibo.com/weibo?q=%23%E5%88%98%E5%B0%91%E6%98%821000%E7%B1%B3%E6%97%A0%E7%BC%98%E5%86%B3%E8%B5%9B%23) |
| #27 | [冬奥短道速滑女子500米](https://s.weibo.com/weibo?q=%23%E5%86%AC%E5%A5%A5%E7%9F%AD%E9%81%93%E9%80%9F%E6%BB%91%E5%A5%B3%E5%AD%90500%E7%B1%B3%23) |
| #28 | [连续五年都没有年三十](https://s.weibo.com/weibo?q=%23%E8%BF%9E%E7%BB%AD%E4%BA%94%E5%B9%B4%E9%83%BD%E6%B2%A1%E6%9C%89%E5%B9%B4%E4%B8%89%E5%8D%81%23) |
| #29 | [33岁男子开特斯拉跑货拉拉](https://s.weibo.com/weibo?q=%2333%E5%B2%81%E7%94%B7%E5%AD%90%E5%BC%80%E7%89%B9%E6%96%AF%E6%8B%89%E8%B7%91%E8%B4%A7%E6%8B%89%E6%8B%89%23) |
| #15 | [孙龙回应1000米摘银](https://s.weibo.com/weibo?q=%E5%AD%99%E9%BE%99%E5%9B%9E%E5%BA%941000%E7%B1%B3%E6%91%98%E9%93%B6) |
| #25 | [心疼范可新](https://s.weibo.com/weibo?q=%23%E5%BF%83%E7%96%BC%E8%8C%83%E5%8F%AF%E6%96%B0%23) |

### 百度热搜

| 排名 | 标题 |
|------|------|
| #12 | [换新费上万的假肢被修鞋大爷免费修好](https://www.baidu.com/s?wd=%E6%8D%A2%E6%96%B0%E8%B4%B9%E4%B8%8A%E4%B8%87%E7%9A%84%E5%81%87%E8%82%A2%E8%A2%AB%E4%BF%AE%E9%9E%8B%E5%A4%A7%E7%88%B7%E5%85%8D%E8%B4%B9%E4%BF%AE%E5%A5%BD) |
| #27 | [爱泼斯坦偷拍潜在受害者视频曝光](https://www.baidu.com/s?wd=%E7%88%B1%E6%B3%BC%E6%96%AF%E5%9D%A6%E5%81%B7%E6%8B%8D%E6%BD%9C%E5%9C%A8%E5%8F%97%E5%AE%B3%E8%80%85%E8%A7%86%E9%A2%91%E6%9B%9D%E5%85%89) |
| #29 | [美司法部长与国会议员对喷5小时](https://www.baidu.com/s?wd=%E7%BE%8E%E5%8F%B8%E6%B3%95%E9%83%A8%E9%95%BF%E4%B8%8E%E5%9B%BD%E4%BC%9A%E8%AE%AE%E5%91%98%E5%AF%B9%E5%96%B75%E5%B0%8F%E6%97%B6) |
| #30 | [2000元一晚 小城酒店涨疯了](https://www.baidu.com/s?wd=2000%E5%85%83%E4%B8%80%E6%99%9A+%E5%B0%8F%E5%9F%8E%E9%85%92%E5%BA%97%E6%B6%A8%E7%96%AF%E4%BA%86) |
| #18 | [中国科学家在3D打印领域有新突破](https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E5%AE%B6%E5%9C%A83D%E6%89%93%E5%8D%B0%E9%A2%86%E5%9F%9F%E6%9C%89%E6%96%B0%E7%AA%81%E7%A0%B4) |
| #29 | [丁俊晖无缘世界公开赛正赛](https://www.baidu.com/s?wd=%E4%B8%81%E4%BF%8A%E6%99%96%E6%97%A0%E7%BC%98%E4%B8%96%E7%95%8C%E5%85%AC%E5%BC%80%E8%B5%9B%E6%AD%A3%E8%B5%9B) |
| #24 | [霍启刚郭晶晶合体拜年](https://www.baidu.com/s?wd=%E9%9C%8D%E5%90%AF%E5%88%9A%E9%83%AD%E6%99%B6%E6%99%B6%E5%90%88%E4%BD%93%E6%8B%9C%E5%B9%B4) |
| #27 | [中方回应“特朗普将于4月初访华”](https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94%E2%80%9C%E7%89%B9%E6%9C%97%E6%99%AE%E5%B0%86%E4%BA%8E4%E6%9C%88%E5%88%9D%E8%AE%BF%E5%8D%8E%E2%80%9D) |
| #19 | [中方回应荷兰启动调查安世半导体](https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94%E8%8D%B7%E5%85%B0%E5%90%AF%E5%8A%A8%E8%B0%83%E6%9F%A5%E5%AE%89%E4%B8%96%E5%8D%8A%E5%AF%BC%E4%BD%93) |
| #27 | [河南邓州通报错领骨灰盒问题](https://www.baidu.com/s?wd=%E6%B2%B3%E5%8D%97%E9%82%93%E5%B7%9E%E9%80%9A%E6%8A%A5%E9%94%99%E9%A2%86%E9%AA%A8%E7%81%B0%E7%9B%92%E9%97%AE%E9%A2%98) |

### 知乎

| 排名 | 标题 |
|------|------|
| #16 | [饭局上，领导拿着虾对底下人说，虾不错，但就是壳太硬，有什么好的办法应对呢？](https://www.zhihu.com/question/1991135188739179917) |
| #17 | [为什么人会惯用右手？](https://www.zhihu.com/question/362401431) |
| #18 | [《太平年》你喜欢朱亚文饰演的赵匡胤吗？](https://www.zhihu.com/question/2000261338878980792) |
| #19 | [为什么心理学上一直让父母少控制孩子呢？](https://www.zhihu.com/question/1998359905988544296) |
| #20 | [AI 视频工具已经能生成导演级镜头，作为观众，你能接受 AI 生成的影视剧或动画吗？愿意买单吗？](https://www.zhihu.com/question/2004603319558042744) |
| #19 | [于东来宣布年后退休，自己将转为顾问，如何看待他的决定？对胖东来的经营会有何影响？](https://www.zhihu.com/question/2004964321906614929) |
| #15 | [浙江 13 岁体操女运动员坠楼案涉事教练被立案调查，此案目前公开的消息中有什么关键信息？](https://www.zhihu.com/question/2005225348132988533) |
| #17 | [假如我突然成为了中世纪的乡绅，我的一天会怎么度过？](https://www.zhihu.com/question/929339990) |
| #18 | [有哪些关于美食的文学描写，让你印象深刻？](https://www.zhihu.com/question/424366363) |
| #19 | [如何评价蒋恺在《太平年》中饰演的郭威？](https://www.zhihu.com/question/2003434178662928556) |

### 今日头条

| 排名 | 标题 |
|------|------|
| #17 | [六户村民合建楼房 网友直呼像学校](https://www.toutiao.com/trending/7605864603070775334/) |
| #23 | [13年前的奔驰车设计有多炸裂](https://www.toutiao.com/trending/7605594992413638707/) |
| #22 | [全网都在祝李婷新婚快乐](https://www.toutiao.com/trending/7605512746754523174/) |
| #27 | [欧盟加大对华限制 六国联名警告](https://www.toutiao.com/trending/7605848940092591622/) |
| #23 | [钱氏家训“利在天下者必谋之”火了](https://www.toutiao.com/trending/7605888197574475814/) |
| #28 | [男子被劝酒 女儿站身后霸气挡酒](https://www.toutiao.com/trending/7605262291923157046/) |
| #19 | [中国AI视频双雄并起](https://www.toutiao.com/trending/7605961413458136639/) |
| #22 | [一线城市房地产市场回暖态势明显](https://www.toutiao.com/trending/7605942302191652379/) |
| #29 | [中戏表演系原主任陈刚主动投案](https://www.toutiao.com/trending/7605875704760110630/) |
| #27 | [女主播一天喷两次定妆喷雾患肺炎](https://www.toutiao.com/trending/7605858425268633663/) |

### 抖音

| 排名 | 标题 |
|------|------|
| #30 | [吴克群田间红毯大片致敬农民](https://www.douyin.com/hot/2398571) |
| #27 | [你只管走幸福随处可见](https://www.douyin.com/hot/2396978) |
| #29 | [郭晶晶霍启刚粤语送新春祝福](https://www.douyin.com/hot/2397708) |
| #30 | [把第五人格搬进现实](https://www.douyin.com/hot/2397731) |
| #28 | [廉子文与文内马斯碰撞](https://www.douyin.com/hot/2397677) |
| #29 | [蔡雪桐武绍桐无缘前三](https://www.douyin.com/hot/2397820) |
| #22 | [过年第一批烫发的人已安全下车](https://www.douyin.com/hot/2396805) |

### 财联社热门

| 排名 | 标题 |
|------|------|
| #13 | [独家\|灵心巧手完成近15亿元B轮融资！已卖出超万只“手”](https://www.cls.cn/detail/2288571) |
| #13 | [宝马将在全球召回数十万辆汽车](https://www.cls.cn/detail/2288479) |

## 🔗 原始链接索引

### 🐦 Twitter 原文 (80/110 条)

- [2026-02-13T05:57 @TVietor08 [热门] | The stock market is up so we don’t have to prosecute pedophiles is one of the worst politi...](https://twitter.com/TVietor08/status/2021705825216278670)
- [2026-02-13T05:57 @AdameMedia [热门] | BREAKING: 🇺🇸 🇮🇱 Pam Bondi starts talking about stock market gains during her testimony on ...](https://twitter.com/AdameMedia/status/2021639407984656769)
- [2026-02-13T05:57 @NotHoodlum [热门] | I didn’t realize we don’t pursue pedophiles if the stock market is doing well. Thank you, ...](https://twitter.com/NotHoodlum/status/2021618127570866444)
- [2026-02-13T05:57 @hashjenni [热门] | Imagine a little girl tells you an old man was sexually abusing her and your response is “...](https://twitter.com/hashjenni/status/2021852693514658217)
- [2026-02-13T05:57 @Rep_Stansbury [热门] | Admin Officials in the Epstein Files: Donald J. Trump (President) Melania Trump (1st Lady)...](https://twitter.com/Rep_Stansbury/status/2021796092879184037)
- [2026-02-13T05:57 @moonshot [热门] | “why didn’t you buy bitcoin in 2012” me in 2012:](https://twitter.com/moonshot/status/2021960073602638045)
- [2026-02-13T05:57 @MikeNellis [热门] | “The stock market is up, so I don’t have to investigate pedophiles and sex traffickers” is...](https://twitter.com/MikeNellis/status/2021742758956826875)
- [2026-02-13T05:57 @ScottJenningsKY [热门] | The government is shrinking. The private sector is growing. Wages are finally outpacing in...](https://twitter.com/ScottJenningsKY/status/2022063985647137241)
- [2026-02-13T05:57 @notthreadguy [热门] | does nobody care that the attorney general said under oath on national television the bigg...](https://twitter.com/notthreadguy/status/2022018683586195484)
- [2026-02-13T05:57 @StoneJAlex [热门] | Why in the world is this woman talking about the stock market? She’s the Attorney General ...](https://twitter.com/StoneJAlex/status/2021829082862784790)
- [2026-02-13T05:57 @Lush_Beauty1 [热门] | 1. ChatGPT = solve any problem 2. PicWish = remove backgrounds 3. Descript = edit podcasts...](https://twitter.com/Lush_Beauty1/status/2021891789267890190)
- [2026-02-13T05:57 @Uncommonsince76 [热门] | Wow! 🤯. This Irish media company found Jeffrey Epstein’s Fed Ex Account password, then log...](https://twitter.com/Uncommonsince76/status/2021656795694121334)
- [2026-02-13T05:57 @jzux [热门] | remember: they want you to think AI is inevitable so they scare you into using it. AI does...](https://twitter.com/jzux/status/2022037403062743284)
- [2026-02-13T05:57 @MAstronomers [热门] | 🚨 AI detects breast cancer 5 years before it develops](https://twitter.com/MAstronomers/status/2021976195630305280)
- [2026-02-13T05:57 @VALOJPNews [热门] | Windows 11の更新プログラム「KB5074109」でFPSが大幅低下。NVIDIAスタッフも「更新プログラムのアンインストール」を解決策として言及valorantjp.co...](https://twitter.com/VALOJPNews/status/2021338610583339391)
- [2026-02-13T05:57 @isaiahrmartin [热门] | Do you realize how absurd it is the United States Attorney General started talking about t...](https://twitter.com/isaiahrmartin/status/2022041041067729140)
- [2026-02-13T05:57 @SidneyPowell1 [热门] | They seem to have no idea how fed up and angry the people who elected them are 🤬🤬@LeaderJo...](https://twitter.com/SidneyPowell1/status/2022115221033410787)
- [2026-02-13T05:57 @goldfishggbr [热门] | Central banks are buying gold at rates not seen since the 1960s. Inflation is persistent. ...](https://twitter.com/goldfishggbr/status/2021972909074657656)
- [2026-02-13T05:57 @DC_Draino [热门] | Oh we know J6 was a Fed setup by Democrats, RINOs, and the Deep State to squash the MAGA m...](https://twitter.com/DC_Draino/status/2022089047087411499)
- [2026-02-13T05:57 @Manifest_Lord [热门] | A queen bee and a worker bee have identical DNA. Literally the same genes. But one lives 4...](https://twitter.com/Manifest_Lord/status/2021941471570801060)
- [2026-02-13T05:57 @AJEnglish [热门] | Palantir founder Peter Thiel is named over 2,200 times in the Epstein files. Al Jazeera’s ...](https://twitter.com/AJEnglish/status/2022016603878305794)
- [2026-02-13T05:57 @WallStreetMav [热门] | The Netherlands is about to commit financial self-destruction. Their parliament just passe...](https://twitter.com/WallStreetMav/status/2022096868595872196)
- [2026-02-13T05:57 @ShannonJoyRadio [热门] | Pam Bondi is unhinged. Here she attacks Americans who want to prosecute CHILD RAPISTS, lec...](https://twitter.com/ShannonJoyRadio/status/2021639145982988756)
- [2026-02-13T05:57 @GuntherEagleman [热门] | 🚨 BREAKING: Fed-up New Yorkers are FED UP and threatening a full-on PROPERTY TAX REVOLT ag...](https://twitter.com/GuntherEagleman/status/2022131070209274033)
- [2026-02-13T05:57 @chatcutapp [热门] | IT FUCKING HAPPENED. Seedance 2.0 now works with the@openclawagent inside@chatcutapp. This...](https://twitter.com/chatcutapp/status/2021967628387139989)
- [2026-02-13T05:57 @PPpasy [热门] | RT@miss_kimpetit: อีป้าแก่แรงมากกกก ข่าวชนะคดีออกปุ๊บ, เจน AI รูปไดโนเสาร์ใส่ชุดตอนแถลงข่า...](https://twitter.com/PPpasy/status/2022188380159979539)
- [2026-02-13T05:57 @seanmdav [热门] | Nixon was bullied, by his persecutors, into keeping it all secret for fear that the truth ...](https://twitter.com/seanmdav/status/2022000673584242935)
- [2026-02-13T05:57 @Eng_china5 [热门] | Chinese company ByteDance released its latest AI model, “Seedance 2.0,” just 48 hours ago....](https://twitter.com/Eng_china5/status/2021949493374259431)
- [2026-02-13T05:57 @dospara_niigata [热门] | ＼全国のドスパラ店舗紹介キャンペーン🎉／ 第21弾👉ドスパラ新潟店 INTEL Core Ultra 7 265KF 抽選で1名様にプレゼント🎁 ▼応募条件 1⃣@dospara_...](https://twitter.com/dospara_niigata/status/2022128593074368771)
- [2026-02-13T05:57 @Angry_Staffer [热门] | Bondi has spent this entire hearing crashing out, talking about the stock market, and tryi...](https://twitter.com/Angry_Staffer/status/2021646339491475608)
- [2026-02-13T05:55 @CGTNOfficial [关注] | Live: As east China's Zhejiang prepares to host a sub-venue for the http://localhost/searc...](https://twitter.com/CGTNOfficial/status/2022187758773842430)
- [2026-02-13T05:30 @CGTNOfficial [关注] | http://localhost/search?q=%23Trump sets one-month window for http://localhost/search?q=%23...](https://twitter.com/CGTNOfficial/status/2022181439656042998)
- [2026-02-13T05:29 @CGTNOfficial [关注] | A second U.S. aircraft carrier will sail from the Caribbean to the Middle East as Presiden...](https://twitter.com/CGTNOfficial/status/2022181370404253971)
- [2026-02-13T05:00 @CGTNOfficial [关注] | http://localhost/search?q=%23EpsteinFiles Britain's most senior government official, Chris...](https://twitter.com/CGTNOfficial/status/2022173894090928515)
- [2026-02-13T04:42 @CNBC [关注] | India approves Rafale jet purchase in $40 billion defense package ahead of Macron visit ht...](https://twitter.com/CNBC/status/2022169552952394138)
- [2026-02-13T04:42 @TechCrunch [关注] | Waymo is asking DoorDash drivers to shut the doors of its self-driving cars https://techcr...](https://twitter.com/TechCrunch/status/2022169415538905449)
- [2026-02-13T04:30 @CGTNOfficial [关注] | U.S. judge: http://localhost/search?q=%23Trump's lawsuit against BBC to go to trial in Feb...](https://twitter.com/CGTNOfficial/status/2022166340199755995)
- [2026-02-13T04:25 @zerohedge [关注] | Biggest Shorting Of Software Stocks Since 2010, As Goldman Cries "Nowhere To Hide Today" h...](https://twitter.com/zerohedge/status/2022165107946496239)
- [2026-02-13T04:00 @zerohedge [关注] | Member Of Trump's 'Religious Liberty Commission' Fired After Heated Israel Debate https://...](https://twitter.com/zerohedge/status/2022158820923863237)
- [2026-02-13T04:00 @CGTNOfficial [关注] | Why is there a train outside the station that never departs? http://localhost/search?q=%23...](https://twitter.com/CGTNOfficial/status/2022158790439973353)
- [2026-02-13T03:47 @zerohedge [关注] | After Hours: AMAT +10%...big revs guide above on March qtr and “expect to grow our semicon...](https://twitter.com/zerohedge/status/2022155724009132457)
- [2026-02-13T03:35 @zerohedge [关注] | A Warning To Seattle: Don't Become The Next Cleveland https://www.zerohedge.com/political/...](https://twitter.com/zerohedge/status/2022152530424172544)
- [2026-02-13T03:30 @CGTNOfficial [关注] | U.S. Senate fails to advance DHS funding bill, partial government shutdown looms https://n...](https://twitter.com/CGTNOfficial/status/2022151243020341731)
- [2026-02-13T03:28 @Sino_Market [关注] | 🇨🇳CHINEXT INDEX DOWN OVER 1% http://localhost/search?q=%23CHINA http://localhost/search?q=...](https://twitter.com/Sino_Market/status/2022150741805478116)
- [2026-02-13T03:16 @zerohedge [关注] | Golden shower parachutes zerohedge (@zerohedge) 16 years of waiting for this kodak moment ...](https://twitter.com/zerohedge/status/2022147734724288941)
- [2026-02-13T03:10 @zerohedge [关注] | E. Coli At 'Incredibly Dangerous Levels' As DC Raw Sewage Spill Into Potomac May Be Larges...](https://twitter.com/zerohedge/status/2022146237982519649)
- [2026-02-13T03:05 @zerohedge [关注] | hey http://localhost/washingtonpost http://localhost/eilperin can you update this Hall of ...](https://twitter.com/zerohedge/status/2022145025694740601)
- [2026-02-13T03:03 @CNBC [关注] | CK Hutchison threatens legal action against Maersk as Panama Canal ports dispute escalates...](https://twitter.com/CNBC/status/2022144465939451921)
- [2026-02-13T03:00 @CGTNOfficial [关注] | Northeast China's Heilongjiang Province boasts a distinctive self-driving loop route. This...](https://twitter.com/CGTNOfficial/status/2022143696779837487)
- [2026-02-13T02:45 @zerohedge [关注] | Judge Boasberg Orders Government To Facilitate Return Of Deported Venezuelans https://www....](https://twitter.com/zerohedge/status/2022139945469558938)
- [2026-02-13T02:37 @Sino_Market [关注] | 🇭🇰HK AI STOCKS SHOW MIXED MOVES: HAIZHI TECH UP 224% ON DEBUT, MINIMAX-WP +10% (WEEK +42%)...](https://twitter.com/Sino_Market/status/2022138050428690619)
- [2026-02-13T02:33 @CNBC [关注] | Xiaomi's electric SUV tops China sales in January, sells twice as many as Tesla's Model Y ...](https://twitter.com/CNBC/status/2022136918872367281)
- [2026-02-13T02:22 @CNBC [关注] | Waymo is paying DoorDash gig workers to close its robotaxi doors https://www.cnbc.com/2026...](https://twitter.com/CNBC/status/2022134309147013436)
- [2026-02-13T02:20 @zerohedge [关注] | CPI Preview: "Hawkish Print More Likely Than Dovish Print" https://www.zerohedge.com/marke...](https://twitter.com/zerohedge/status/2022133649693442085)
- [2026-02-13T02:20 @Sino_Market [关注] | 🇨🇳SHENZHEN FINANCIAL REGULATOR ISSUES PUBLIC NOTICE TO FURTHER STANDARDIZE GOLD MARKET OPE...](https://twitter.com/Sino_Market/status/2022133650922553520)
- [2026-02-13T02:20 @CGTNOfficial [关注] | Another medal for Team China at http://localhost/search?q=%23MilanoCortina2026! China's Su...](https://twitter.com/CGTNOfficial/status/2022133624964014348)
- [2026-02-13T02:04 @CNBC [关注] | Epstein files: Goldman Sachs top lawyer Kathy Ruemmler to step down after email fallout ht...](https://twitter.com/CNBC/status/2022129617461486047)
- [2026-02-13T02:02 @CNBC [关注] | U.S. signs trade deal with Taiwan, lowering tariffs to 15%, while Taipei to boost American...](https://twitter.com/CNBC/status/2022129334203338959)
- [2026-02-13T01:59 @CGTNOfficial [关注] | Live: As China welcomes the 2026 Year of the Horse, Gubei Water Town, located at the foot ...](https://twitter.com/CGTNOfficial/status/2022128574791397474)
- [2026-02-13T01:43 @Sino_Market [关注] | ZHIPU, OR KNOWLEDGE ATLAS JUMPS OVER 13% TO FRESH POST-IPO HIGH; UP 123% THIS WEEK AFTER C...](https://twitter.com/Sino_Market/status/2022124396119568641)
- [2026-02-13T01:42 @Sino_Market [关注] | CHINA JAN HOME PRICES IN 70 CITIES FALL M/M AT A SLOWER PACE, DOWN Y/Y – NBS ALL CHINA JAN...](https://twitter.com/Sino_Market/status/2022124171820683639)
- [2026-02-13T01:41 @Sino_Market [关注] | SHARES OF BEIJING HAIZHI TECHNOLOGY RISE TO HK$99 EACH IN HONG KONG DEBUT VERSUS OFFER PRI...](https://twitter.com/Sino_Market/status/2022123980019446272)
- [2026-02-13T01:24 @Sino_Market [关注] | 🇭🇰AT OPEN, HANG SENG DOWN 1.45%; TECH INDEX -1.59% http://localhost/search?q=%23CHINA http...](https://twitter.com/Sino_Market/status/2022119574997807305)
- [2026-02-13T01:23 @Sino_Market [关注] | XIAOMI AUTO DELIVERIES SURPASS 600,000 UNITS – LEI JUN (https://mktnews.com/flashDetail.ht...](https://twitter.com/Sino_Market/status/2022119503866544160)
- [2026-02-13T01:22 @CNBC [关注] | CNBC Daily Open: AI is coming after more sectors, and its pace isn't slowing https://www.c...](https://twitter.com/CNBC/status/2022119074222739882)
- [2026-02-13T01:20 @Sino_Market [关注] | Key Global and China News – Past 24 Hours Foreign Exchange & Commodities - Offshore yuan s...](https://twitter.com/Sino_Market/status/2022118707007574392)
- [2026-02-13T01:20 @Sino_Market [关注] | FTSE CHINA A50 INDEX FUTURES DOWN 0.69% AT OPEN (https://mktnews.com/flashDetail.html?id=0...](https://twitter.com/Sino_Market/status/2022118602443493669)
- [2026-02-13T01:14 @zerohedge [关注] | "2/12/26 Market Summary: Dram/Software Fears Spread to Hardware, CTA's to Sell $20bln More...](https://twitter.com/zerohedge/status/2022117249612648703)
- [2026-02-13T01:13 @LynAldenContact [关注] | Cultures have many differing views of morality, but all around the world and for thousands...](https://twitter.com/LynAldenContact/status/2022116819365245237)
- [2026-02-13T00:52 @CNBC [关注] | Amazon's Ring cancels Flock partnership amid Super Bowl ad backlash https://www.cnbc.com/2...](https://twitter.com/CNBC/status/2022111679006277693)
- [2026-02-13T00:35 @LynAldenContact [关注] | Three companies make nearly all of the RAM in the world and two of them are in Korea. It's...](https://twitter.com/LynAldenContact/status/2022107417946075284)
- [2026-02-13T00:22 @CNBC [关注] | Friday's big stock stories: What’s likely to move the market in the next trading session h...](https://twitter.com/CNBC/status/2022104139371544680)
- [2026-02-13T00:05 @DefiLlama [关注] | Track token rights, utility, and alignment for dozens of protocols including Aave on our p...](https://twitter.com/DefiLlama/status/2022099781213131220)
- [2026-02-13T00:03 @CNBC [关注] | Asia-Pacific markets set to fall, tracking AI-fuelled losses on Wall Street https://www.cn...](https://twitter.com/CNBC/status/2022099274549367229)
- [2026-02-13T00:01 @elonmusk [关注] | From Day One, http://localhost/xai has been upgrading grid infrastructure and ensuring rat...](https://twitter.com/elonmusk/status/2022098797829210250)
- [2026-02-12T23:45 @TechCrunch [关注] | For $1 million, you can pay Bryan Johnson (or BryanAI?) to teach you how to live longer ht...](https://twitter.com/TechCrunch/status/2022094671905009692)
- [2026-02-12T23:31 @TechCrunch [关注] | Amid disappointing earnings, Pinterest claims it sees more searches than ChatGPT https://t...](https://twitter.com/TechCrunch/status/2022091242507796903)
- [2026-02-12T23:27 @TechCrunch [关注] | IBM will hire your entry-level talent in the age of AI https://techcrunch.com/2026/02/12/i...](https://twitter.com/TechCrunch/status/2022090135400264014)
- [2026-02-12T23:23 @TechCrunch [关注] | Build Mode is back on February 19! This season, we’re diving into what it takes to build a...](https://twitter.com/TechCrunch/status/2022089232286711973)
- [2026-02-12T23:18 @TechCrunch [关注] | Rivian was saved by software in 2025 https://techcrunch.com/2026/02/12/rivian-was-saved-by...](https://twitter.com/TechCrunch/status/2022087881913975198)

### 📱 微信公众号原文 (0/0 条)

- 暂无可用链接

### 🔥 NewsNow 原文 (120/120 条)

- [华尔街见闻 #3 | 华尔街见闻早餐FM-Radio | 2026年2月12日](https://wallstreetcn.com/articles/3765542)
- [bilibili 热搜 #4 | 圆脸谈加拿大校园枪击致10死](https://search.bilibili.com/all?keyword=%E5%9C%86%E8%84%B8%E8%B0%88%E5%8A%A0%E6%8B%BF%E5%A4%A7%E6%A0%A1%E5%9B%AD%E6%9E%AA%E5%87%BB%E8%87%B410%E6%AD%BB)
- [华尔街见闻 #4 | 强劲非农打击降息预期，AI担忧拖累美股指，美债承压，金银涨，原油冲高回落](https://wallstreetcn.com/articles/3765486)
- [华尔街见闻 #5 | “下一个AI受害者”出现了，房地产服务股遭抛售，创疫情以来最大单日跌幅](https://wallstreetcn.com/articles/3765544)
- [澎湃新闻 #8 | 家长反映“女儿遭教练体罚索财后坠楼”，校方：涉事两教练被警方立案调查](https://www.thepaper.cn/newsDetail_forward_32589244)
- [微博 #10 | 孙龙](https://s.weibo.com/weibo?q=%E5%AD%99%E9%BE%99)
- [百度热搜 #12 | 换新费上万的假肢被修鞋大爷免费修好](https://www.baidu.com/s?wd=%E6%8D%A2%E6%96%B0%E8%B4%B9%E4%B8%8A%E4%B8%87%E7%9A%84%E5%81%87%E8%82%A2%E8%A2%AB%E4%BF%AE%E9%9E%8B%E5%A4%A7%E7%88%B7%E5%85%8D%E8%B4%B9%E4%BF%AE%E5%A5%BD)
- [bilibili 热搜 #13 | U17亚洲杯抽签出炉](https://search.bilibili.com/all?keyword=U17%E4%BA%9A%E6%B4%B2%E6%9D%AF%E6%8A%BD%E7%AD%BE%E5%87%BA%E7%82%89)
- [知乎 #16 | 饭局上，领导拿着虾对底下人说，虾不错，但就是壳太硬，有什么好的办法应对呢？](https://www.zhihu.com/question/1991135188739179917)
- [知乎 #17 | 为什么人会惯用右手？](https://www.zhihu.com/question/362401431)
- [今日头条 #17 | 六户村民合建楼房 网友直呼像学校](https://www.toutiao.com/trending/7605864603070775334/)
- [知乎 #18 | 《太平年》你喜欢朱亚文饰演的赵匡胤吗？](https://www.zhihu.com/question/2000261338878980792)
- [微博 #19 | 短道速滑](https://s.weibo.com/weibo?q=%E7%9F%AD%E9%81%93%E9%80%9F%E6%BB%91)
- [知乎 #19 | 为什么心理学上一直让父母少控制孩子呢？](https://www.zhihu.com/question/1998359905988544296)
- [知乎 #20 | AI 视频工具已经能生成导演级镜头，作为观众，你能接受 AI 生成的影视剧或动画吗？愿意买单吗？](https://www.zhihu.com/question/2004603319558042744)
- [微博 #20 | 任子威说女子500米成绩夸张](https://s.weibo.com/weibo?q=%23%E4%BB%BB%E5%AD%90%E5%A8%81%E8%AF%B4%E5%A5%B3%E5%AD%90500%E7%B1%B3%E6%88%90%E7%BB%A9%E5%A4%B8%E5%BC%A0%23)
- [今日头条 #23 | 13年前的奔驰车设计有多炸裂](https://www.toutiao.com/trending/7605594992413638707/)
- [微博 #24 | 摄影师曝檀健次拍摄几乎一条过](https://s.weibo.com/weibo?q=%23%E6%91%84%E5%BD%B1%E5%B8%88%E6%9B%9D%E6%AA%80%E5%81%A5%E6%AC%A1%E6%8B%8D%E6%91%84%E5%87%A0%E4%B9%8E%E4%B8%80%E6%9D%A1%E8%BF%87%23)
- [微博 #25 | 刘少昂1000米无缘决赛](https://s.weibo.com/weibo?q=%23%E5%88%98%E5%B0%91%E6%98%821000%E7%B1%B3%E6%97%A0%E7%BC%98%E5%86%B3%E8%B5%9B%23)
- [百度热搜 #27 | 爱泼斯坦偷拍潜在受害者视频曝光](https://www.baidu.com/s?wd=%E7%88%B1%E6%B3%BC%E6%96%AF%E5%9D%A6%E5%81%B7%E6%8B%8D%E6%BD%9C%E5%9C%A8%E5%8F%97%E5%AE%B3%E8%80%85%E8%A7%86%E9%A2%91%E6%9B%9D%E5%85%89)
- [微博 #27 | 冬奥短道速滑女子500米](https://s.weibo.com/weibo?q=%23%E5%86%AC%E5%A5%A5%E7%9F%AD%E9%81%93%E9%80%9F%E6%BB%91%E5%A5%B3%E5%AD%90500%E7%B1%B3%23)
- [微博 #28 | 连续五年都没有年三十](https://s.weibo.com/weibo?q=%23%E8%BF%9E%E7%BB%AD%E4%BA%94%E5%B9%B4%E9%83%BD%E6%B2%A1%E6%9C%89%E5%B9%B4%E4%B8%89%E5%8D%81%23)
- [百度热搜 #29 | 美司法部长与国会议员对喷5小时](https://www.baidu.com/s?wd=%E7%BE%8E%E5%8F%B8%E6%B3%95%E9%83%A8%E9%95%BF%E4%B8%8E%E5%9B%BD%E4%BC%9A%E8%AE%AE%E5%91%98%E5%AF%B9%E5%96%B75%E5%B0%8F%E6%97%B6)
- [微博 #29 | 33岁男子开特斯拉跑货拉拉](https://s.weibo.com/weibo?q=%2333%E5%B2%81%E7%94%B7%E5%AD%90%E5%BC%80%E7%89%B9%E6%96%AF%E6%8B%89%E8%B7%91%E8%B4%A7%E6%8B%89%E6%8B%89%23)
- [百度热搜 #30 | 2000元一晚 小城酒店涨疯了](https://www.baidu.com/s?wd=2000%E5%85%83%E4%B8%80%E6%99%9A+%E5%B0%8F%E5%9F%8E%E9%85%92%E5%BA%97%E6%B6%A8%E7%96%AF%E4%BA%86)
- [抖音 #30 | 吴克群田间红毯大片致敬农民](https://www.douyin.com/hot/2398571)
- [财联社热门 #13 | 独家|灵心巧手完成近15亿元B轮融资！已卖出超万只“手”](https://www.cls.cn/detail/2288571)
- [微博 #15 | 孙龙回应1000米摘银](https://s.weibo.com/weibo?q=%E5%AD%99%E9%BE%99%E5%9B%9E%E5%BA%941000%E7%B1%B3%E6%91%98%E9%93%B6)
- [百度热搜 #18 | 中国科学家在3D打印领域有新突破](https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E5%AE%B6%E5%9C%A83D%E6%89%93%E5%8D%B0%E9%A2%86%E5%9F%9F%E6%9C%89%E6%96%B0%E7%AA%81%E7%A0%B4)
- [知乎 #19 | 于东来宣布年后退休，自己将转为顾问，如何看待他的决定？对胖东来的经营会有何影响？](https://www.zhihu.com/question/2004964321906614929)
- [今日头条 #22 | 全网都在祝李婷新婚快乐](https://www.toutiao.com/trending/7605512746754523174/)
- [bilibili 热搜 #24 | 王者新春版本内容速览](https://search.bilibili.com/all?keyword=%E7%8E%8B%E8%80%85%E6%96%B0%E6%98%A5%E7%89%88%E6%9C%AC%E5%86%85%E5%AE%B9%E9%80%9F%E8%A7%88)
- [微博 #25 | 心疼范可新](https://s.weibo.com/weibo?q=%23%E5%BF%83%E7%96%BC%E8%8C%83%E5%8F%AF%E6%96%B0%23)
- [bilibili 热搜 #26 | COS星铁阿哈开业发厕纸](https://search.bilibili.com/all?keyword=COS%E6%98%9F%E9%93%81%E9%98%BF%E5%93%88%E5%BC%80%E4%B8%9A%E5%8F%91%E5%8E%95%E7%BA%B8)
- [抖音 #27 | 你只管走幸福随处可见](https://www.douyin.com/hot/2396978)
- [今日头条 #27 | 欧盟加大对华限制 六国联名警告](https://www.toutiao.com/trending/7605848940092591622/)
- [抖音 #29 | 郭晶晶霍启刚粤语送新春祝福](https://www.douyin.com/hot/2397708)
- [百度热搜 #29 | 丁俊晖无缘世界公开赛正赛](https://www.baidu.com/s?wd=%E4%B8%81%E4%BF%8A%E6%99%96%E6%97%A0%E7%BC%98%E4%B8%96%E7%95%8C%E5%85%AC%E5%BC%80%E8%B5%9B%E6%AD%A3%E8%B5%9B)
- [微博 #30 | 孙龙激动落泪](https://s.weibo.com/weibo?q=%23%E5%AD%99%E9%BE%99%E6%BF%80%E5%8A%A8%E8%90%BD%E6%B3%AA%23)
- [财联社热门 #13 | 宝马将在全球召回数十万辆汽车](https://www.cls.cn/detail/2288479)
- [知乎 #15 | 浙江 13 岁体操女运动员坠楼案涉事教练被立案调查，此案目前公开的消息中有什么关键信息？](https://www.zhihu.com/question/2005225348132988533)
- [知乎 #17 | 假如我突然成为了中世纪的乡绅，我的一天会怎么度过？](https://www.zhihu.com/question/929339990)
- [知乎 #18 | 有哪些关于美食的文学描写，让你印象深刻？](https://www.zhihu.com/question/424366363)
- [微博 #18 | 刘少昂好稳](https://s.weibo.com/weibo?q=%E5%88%98%E5%B0%91%E6%98%82%E5%A5%BD%E7%A8%B3)
- [知乎 #19 | 如何评价蒋恺在《太平年》中饰演的郭威？](https://www.zhihu.com/question/2003434178662928556)
- [百度热搜 #24 | 霍启刚郭晶晶合体拜年](https://www.baidu.com/s?wd=%E9%9C%8D%E5%90%AF%E5%88%9A%E9%83%AD%E6%99%B6%E6%99%B6%E5%90%88%E4%BD%93%E6%8B%9C%E5%B9%B4)
- [微博 #27 | 36岁何穗状态](https://s.weibo.com/weibo?q=%2336%E5%B2%81%E4%BD%95%E7%A9%97%E7%8A%B6%E6%80%81%23)
- [百度热搜 #27 | 中方回应“特朗普将于4月初访华”](https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94%E2%80%9C%E7%89%B9%E6%9C%97%E6%99%AE%E5%B0%86%E4%BA%8E4%E6%9C%88%E5%88%9D%E8%AE%BF%E5%8D%8E%E2%80%9D)
- [微博 #29 | 蒋欣 当年真的错怪你了](https://s.weibo.com/weibo?q=%E8%92%8B%E6%AC%A3+%E5%BD%93%E5%B9%B4%E7%9C%9F%E7%9A%84%E9%94%99%E6%80%AA%E4%BD%A0%E4%BA%86)
- [抖音 #30 | 把第五人格搬进现实](https://www.douyin.com/hot/2397731)
- [微博 #14 | 孙龙短道1000米银牌](https://s.weibo.com/weibo?q=%23%E5%AD%99%E9%BE%99%E7%9F%AD%E9%81%931000%E7%B1%B3%E9%93%B6%E7%89%8C%23)
- [微博 #16 | 孙龙1000米进决赛](https://s.weibo.com/weibo?q=%23%E5%AD%99%E9%BE%991000%E7%B1%B3%E8%BF%9B%E5%86%B3%E8%B5%9B%23)
- [微博 #18 | 孙龙进1000米半决赛](https://s.weibo.com/weibo?q=%23%E5%AD%99%E9%BE%99%E8%BF%9B1000%E7%B1%B3%E5%8D%8A%E5%86%B3%E8%B5%9B%23)
- [百度热搜 #19 | 中方回应荷兰启动调查安世半导体](https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%B9%E5%9B%9E%E5%BA%94%E8%8D%B7%E5%85%B0%E5%90%AF%E5%8A%A8%E8%B0%83%E6%9F%A5%E5%AE%89%E4%B8%96%E5%8D%8A%E5%AF%BC%E4%BD%93)
- [微博 #20 | 中国冰壶女队7比4英国](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E5%86%B0%E5%A3%B6%E5%A5%B3%E9%98%9F7%E6%AF%944%E8%8B%B1%E5%9B%BD%23)
- [bilibili 热搜 #22 | 用AI解锁吴克群将军令](https://search.bilibili.com/all?keyword=%E7%94%A8AI%E8%A7%A3%E9%94%81%E5%90%B4%E5%85%8B%E7%BE%A4%E5%B0%86%E5%86%9B%E4%BB%A4)
- [今日头条 #23 | 钱氏家训“利在天下者必谋之”火了](https://www.toutiao.com/trending/7605888197574475814/)
- [百度热搜 #27 | 河南邓州通报错领骨灰盒问题](https://www.baidu.com/s?wd=%E6%B2%B3%E5%8D%97%E9%82%93%E5%B7%9E%E9%80%9A%E6%8A%A5%E9%94%99%E9%A2%86%E9%AA%A8%E7%81%B0%E7%9B%92%E9%97%AE%E9%A2%98)
- [微博 #27 | 崔佳恩 感情分](https://s.weibo.com/weibo?q=%E5%B4%94%E4%BD%B3%E6%81%A9+%E6%84%9F%E6%83%85%E5%88%86)
- [今日头条 #28 | 男子被劝酒 女儿站身后霸气挡酒](https://www.toutiao.com/trending/7605262291923157046/)
- [百度热搜 #29 | 远洋渔船船长公海遇害细节曝光](https://www.baidu.com/s?wd=%E8%BF%9C%E6%B4%8B%E6%B8%94%E8%88%B9%E8%88%B9%E9%95%BF%E5%85%AC%E6%B5%B7%E9%81%87%E5%AE%B3%E7%BB%86%E8%8A%82%E6%9B%9D%E5%85%89)
- [百度热搜 #30 | 过年最怕别人问你什么](https://www.baidu.com/s?wd=%E8%BF%87%E5%B9%B4%E6%9C%80%E6%80%95%E5%88%AB%E4%BA%BA%E9%97%AE%E4%BD%A0%E4%BB%80%E4%B9%88)
- [微博 #30 | 女子单板U池决赛](https://s.weibo.com/weibo?q=%E5%A5%B3%E5%AD%90%E5%8D%95%E6%9D%BFU%E6%B1%A0%E5%86%B3%E8%B5%9B)
- [华尔街见闻 #7 | 华尔街怎么看1月非农就业？首次降息延至7月，“新美联储通讯社”预计降息暂停期更久](https://wallstreetcn.com/articles/3765533)
- [微博 #10 | 贝尔塞伯短道500米金牌](https://s.weibo.com/weibo?q=%23%E8%B4%9D%E5%B0%94%E5%A1%9E%E4%BC%AF%E7%9F%AD%E9%81%93500%E7%B1%B3%E9%87%91%E7%89%8C%23)
- [今日头条 #19 | 中国AI视频双雄并起](https://www.toutiao.com/trending/7605961413458136639/)
- [今日头条 #22 | 一线城市房地产市场回暖态势明显](https://www.toutiao.com/trending/7605942302191652379/)
- [微博 #27 | 范可新无缘500米决赛](https://s.weibo.com/weibo?q=%23%E8%8C%83%E5%8F%AF%E6%96%B0%E6%97%A0%E7%BC%98500%E7%B1%B3%E5%86%B3%E8%B5%9B%23)
- [抖音 #28 | 廉子文与文内马斯碰撞](https://www.douyin.com/hot/2397677)
- [百度热搜 #28 | 男子结婚“摇”来约200台小米汽车](https://www.baidu.com/s?wd=%E7%94%B7%E5%AD%90%E7%BB%93%E5%A9%9A%E2%80%9C%E6%91%87%E2%80%9D%E6%9D%A5%E7%BA%A6200%E5%8F%B0%E5%B0%8F%E7%B1%B3%E6%B1%BD%E8%BD%A6)
- [今日头条 #29 | 中戏表演系原主任陈刚主动投案](https://www.toutiao.com/trending/7605875704760110630/)
- [百度热搜 #29 | 捷龙三号遥九一箭七星发射成功](https://www.baidu.com/s?wd=%E6%8D%B7%E9%BE%99%E4%B8%89%E5%8F%B7%E9%81%A5%E4%B9%9D%E4%B8%80%E7%AE%AD%E4%B8%83%E6%98%9F%E5%8F%91%E5%B0%84%E6%88%90%E5%8A%9F)
- [抖音 #29 | 蔡雪桐武绍桐无缘前三](https://www.douyin.com/hot/2397820)
- [百度热搜 #30 | 立陶宛释放信号 转向与中国恢复关系](https://www.baidu.com/s?wd=%E7%AB%8B%E9%99%B6%E5%AE%9B%E9%87%8A%E6%94%BE%E4%BF%A1%E5%8F%B7+%E8%BD%AC%E5%90%91%E4%B8%8E%E4%B8%AD%E5%9B%BD%E6%81%A2%E5%A4%8D%E5%85%B3%E7%B3%BB)
- [bilibili 热搜 #8 | 建立太空数据中心有多难](https://search.bilibili.com/all?keyword=%E5%BB%BA%E7%AB%8B%E5%A4%AA%E7%A9%BA%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E6%9C%89%E5%A4%9A%E9%9A%BE)
- [微博 #17 | 张楚桐犯规](https://s.weibo.com/weibo?q=%23%E5%BC%A0%E6%A5%9A%E6%A1%90%E7%8A%AF%E8%A7%84%23)
- [微博 #18 | 黄大宪犯规无缘晋级](https://s.weibo.com/weibo?q=%23%E9%BB%84%E5%A4%A7%E5%AE%AA%E7%8A%AF%E8%A7%84%E6%97%A0%E7%BC%98%E6%99%8B%E7%BA%A7%23)
- [微博 #20 | 虞书欣直播](https://s.weibo.com/weibo?q=%E8%99%9E%E4%B9%A6%E6%AC%A3%E7%9B%B4%E6%92%AD)
- [百度热搜 #24 | 两艘美国海军舰船相撞致2伤](https://www.baidu.com/s?wd=%E4%B8%A4%E8%89%98%E7%BE%8E%E5%9B%BD%E6%B5%B7%E5%86%9B%E8%88%B0%E8%88%B9%E7%9B%B8%E6%92%9E%E8%87%B42%E4%BC%A4)
- [今日头条 #27 | 女主播一天喷两次定妆喷雾患肺炎](https://www.toutiao.com/trending/7605858425268633663/)
- [微博 #28 | 王欣然犯规无缘晋级](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E6%AC%A3%E7%84%B6%E7%8A%AF%E8%A7%84%E6%97%A0%E7%BC%98%E6%99%8B%E7%BA%A7%23)
- [微博 #29 | 王者荣耀超话爆了](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80%E8%B6%85%E8%AF%9D%E7%88%86%E4%BA%86%23)
- [bilibili 热搜 #29 | 带放假的侄子旅游哀牢山](https://search.bilibili.com/all?keyword=%E5%B8%A6%E6%94%BE%E5%81%87%E7%9A%84%E4%BE%84%E5%AD%90%E6%97%85%E6%B8%B8%E5%93%80%E7%89%A2%E5%B1%B1)
- [今日头条 #29 | 谷爱凌冬奥赛服灵感来自青花瓷](https://www.toutiao.com/trending/7605058017667432511/)
- [微博 #10 | 韩国崔佳恩U池夺冠](https://s.weibo.com/weibo?q=%E9%9F%A9%E5%9B%BD%E5%B4%94%E4%BD%B3%E6%81%A9U%E6%B1%A0%E5%A4%BA%E5%86%A0)
- [微博 #13 | 刘少昂进1000米半决赛](https://s.weibo.com/weibo?q=%23%E5%88%98%E5%B0%91%E6%98%82%E8%BF%9B1000%E7%B1%B3%E5%8D%8A%E5%86%B3%E8%B5%9B%23)
- [微博 #14 | 武绍桐第三滑78.00分](https://s.weibo.com/weibo?q=%23%E6%AD%A6%E7%BB%8D%E6%A1%90%E7%AC%AC%E4%B8%89%E6%BB%9178.00%E5%88%86%23)
- [今日头条 #18 | 日本彻底右转有多危险](https://www.toutiao.com/trending/7605377609426190355/)
- [bilibili 热搜 #24 | IEM克拉科夫集锦](https://search.bilibili.com/all?keyword=IEM%E5%85%8B%E6%8B%89%E7%A7%91%E5%A4%AB%E9%9B%86%E9%94%A6)
- [微博 #27 | 王者荣耀马年全明星表演赛](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80%E9%A9%AC%E5%B9%B4%E5%85%A8%E6%98%8E%E6%98%9F%E8%A1%A8%E6%BC%94%E8%B5%9B%23)
- [今日头条 #29 | 医生分享3个常见服药误区](https://www.toutiao.com/trending/7605169819470364726/)
- [百度热搜 #30 | 爱马仕CEO回应被爱泼斯坦案牵连](https://www.baidu.com/s?wd=%E7%88%B1%E9%A9%AC%E4%BB%95CEO%E5%9B%9E%E5%BA%94%E8%A2%AB%E7%88%B1%E6%B3%BC%E6%96%AF%E5%9D%A6%E6%A1%88%E7%89%B5%E8%BF%9E)
- [微博 #8 | 范可新晋级500米半决赛](https://s.weibo.com/weibo?q=%23%E8%8C%83%E5%8F%AF%E6%96%B0%E6%99%8B%E7%BA%A7500%E7%B1%B3%E5%8D%8A%E5%86%B3%E8%B5%9B%23)
- [微博 #9 | 武绍桐第二滑70.25分](https://s.weibo.com/weibo?q=%23%E6%AD%A6%E7%BB%8D%E6%A1%90%E7%AC%AC%E4%BA%8C%E6%BB%9170.25%E5%88%86%23)
- [知乎 #13 | 北京约谈携程、去哪儿等十二家第三方火车票销售平台，要求整改「加速包」等误导性宣传，哪些信息值得关注？](https://www.zhihu.com/question/2005212548996301221)
- [微博 #15 | 任子威说要当心韩国选手](https://s.weibo.com/weibo?q=%23%E4%BB%BB%E5%AD%90%E5%A8%81%E8%AF%B4%E8%A6%81%E5%BD%93%E5%BF%83%E9%9F%A9%E5%9B%BD%E9%80%89%E6%89%8B%23)
- [微博 #20 | 蔡雪桐的冬奥松弛感](https://s.weibo.com/weibo?q=%E8%94%A1%E9%9B%AA%E6%A1%90%E7%9A%84%E5%86%AC%E5%A5%A5%E6%9D%BE%E5%BC%9B%E6%84%9F)
- [抖音 #22 | 过年第一批烫发的人已安全下车](https://www.douyin.com/hot/2396805)
- [百度热搜 #26 | 想在丈母娘家表现 劈柴失误致骨折](https://www.baidu.com/s?wd=%E6%83%B3%E5%9C%A8%E4%B8%88%E6%AF%8D%E5%A8%98%E5%AE%B6%E8%A1%A8%E7%8E%B0+%E5%8A%88%E6%9F%B4%E5%A4%B1%E8%AF%AF%E8%87%B4%E9%AA%A8%E6%8A%98)
- [微博 #27 | 意大利老将5000米0.1秒绝杀夺金](https://s.weibo.com/weibo?q=%23%E6%84%8F%E5%A4%A7%E5%88%A9%E8%80%81%E5%B0%865000%E7%B1%B30.1%E7%A7%92%E7%BB%9D%E6%9D%80%E5%A4%BA%E9%87%91%23)
- [微博 #28 | 速度滑冰女子5000米](https://s.weibo.com/weibo?q=%E9%80%9F%E5%BA%A6%E6%BB%91%E5%86%B0%E5%A5%B3%E5%AD%905000%E7%B1%B3)
- [微博 #8 | 武绍桐U池首轮67.75分](https://s.weibo.com/weibo?q=%23%E6%AD%A6%E7%BB%8D%E6%A1%90U%E6%B1%A0%E9%A6%96%E8%BD%AE67.75%E5%88%86%23)
- [澎湃新闻 #19 | 岚目镜观｜从执政美国到选举美国：2026中期选举与“两个美国”的另一面相](https://www.thepaper.cn/newsDetail_forward_32584344)
- [微博 #23 | 年少有为](https://s.weibo.com/weibo?q=%E5%B9%B4%E5%B0%91%E6%9C%89%E4%B8%BA)
- [百度热搜 #24 | 哈尔滨小哥为早回家过年找AI替班](https://www.baidu.com/s?wd=%E5%93%88%E5%B0%94%E6%BB%A8%E5%B0%8F%E5%93%A5%E4%B8%BA%E6%97%A9%E5%9B%9E%E5%AE%B6%E8%BF%87%E5%B9%B4%E6%89%BEAI%E6%9B%BF%E7%8F%AD)
- [微博 #25 | 武绍桐U池首轮顺利完成](https://s.weibo.com/weibo?q=%23%E6%AD%A6%E7%BB%8D%E6%A1%90U%E6%B1%A0%E9%A6%96%E8%BD%AE%E9%A1%BA%E5%88%A9%E5%AE%8C%E6%88%90%23)
- [bilibili 热搜 #26 | 喵喵的结合获IGN9分](https://search.bilibili.com/all?keyword=%E5%96%B5%E5%96%B5%E7%9A%84%E7%BB%93%E5%90%88%E8%8E%B7IGN9%E5%88%86)
- [微博 #27 | 唐宫奇案](https://s.weibo.com/weibo?q=%E5%94%90%E5%AE%AB%E5%A5%87%E6%A1%88)
- [微博 #28 | 微博之夜 绝美打光](https://s.weibo.com/weibo?q=%E5%BE%AE%E5%8D%9A%E4%B9%8B%E5%A4%9C+%E7%BB%9D%E7%BE%8E%E6%89%93%E5%85%89)
- [微博 #29 | 张凌赫粉丝爬半天山拍了三遍林允](https://s.weibo.com/weibo?q=%E5%BC%A0%E5%87%8C%E8%B5%AB%E7%B2%89%E4%B8%9D%E7%88%AC%E5%8D%8A%E5%A4%A9%E5%B1%B1%E6%8B%8D%E4%BA%86%E4%B8%89%E9%81%8D%E6%9E%97%E5%85%81)
- [bilibili 热搜 #30 | 江寻千马年冰雕神兽龙马](https://search.bilibili.com/all?keyword=%E6%B1%9F%E5%AF%BB%E5%8D%83%E9%A9%AC%E5%B9%B4%E5%86%B0%E9%9B%95%E7%A5%9E%E5%85%BD%E9%BE%99%E9%A9%AC)
- [bilibili 热搜 #5 | 外网热议黑神话春节PV](https://search.bilibili.com/all?keyword=%E5%A4%96%E7%BD%91%E7%83%AD%E8%AE%AE%E9%BB%91%E7%A5%9E%E8%AF%9D%E6%98%A5%E8%8A%82PV)
- [微博 #9 | 中国雪橇队米兰冬奥书写新历史](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E9%9B%AA%E6%A9%87%E9%98%9F%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E4%B9%A6%E5%86%99%E6%96%B0%E5%8E%86%E5%8F%B2%23)
- [知乎 #17 | 主播「斯奎奇大王」直播玩《DOTA2》的表现能看出他是什么水平的玩家吗？](https://www.zhihu.com/question/2005032137506718791)
- [微博 #28 | 太平年大结局](https://s.weibo.com/weibo?q=%E5%A4%AA%E5%B9%B3%E5%B9%B4%E5%A4%A7%E7%BB%93%E5%B1%80)
- [微博 #29 | 蔡徐坤回复无畏](https://s.weibo.com/weibo?q=%23%E8%94%A1%E5%BE%90%E5%9D%A4%E5%9B%9E%E5%A4%8D%E6%97%A0%E7%95%8F%23)
- [百度热搜 #30 | 民营火箭最大单笔融资诞生](https://www.baidu.com/s?wd=%E6%B0%91%E8%90%A5%E7%81%AB%E7%AE%AD%E6%9C%80%E5%A4%A7%E5%8D%95%E7%AC%94%E8%9E%8D%E8%B5%84%E8%AF%9E%E7%94%9F)
- [微博 #10 | 中国队雪橇团体接力顺利完赛](https://s.weibo.com/weibo?q=%E4%B8%AD%E5%9B%BD%E9%98%9F%E9%9B%AA%E6%A9%87%E5%9B%A2%E4%BD%93%E6%8E%A5%E5%8A%9B%E9%A1%BA%E5%88%A9%E5%AE%8C%E8%B5%9B)
- [微博 #26 | 35年前乳汁救武警今患癌红嫂回应](https://s.weibo.com/weibo?q=%2335%E5%B9%B4%E5%89%8D%E4%B9%B3%E6%B1%81%E6%95%91%E6%AD%A6%E8%AD%A6%E4%BB%8A%E6%82%A3%E7%99%8C%E7%BA%A2%E5%AB%82%E5%9B%9E%E5%BA%94%23)
- [百度热搜 #30 | 马年爆火宠物小矮马最高售价超10万](https://www.baidu.com/s?wd=%E9%A9%AC%E5%B9%B4%E7%88%86%E7%81%AB%E5%AE%A0%E7%89%A9%E5%B0%8F%E7%9F%AE%E9%A9%AC%E6%9C%80%E9%AB%98%E5%94%AE%E4%BB%B7%E8%B6%8510%E4%B8%87)

### 💻 GitHub 原文 (19/19 条)

- [coreyhaines31/marketingskills | ⭐ 7525 | Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and grow...](https://github.com/coreyhaines31/marketingskills)
- [Leey21/awesome-ai-research-writing | ⭐ 5697 | Elevate your AI research writing, no more tedious polishing ✨](https://github.com/Leey21/awesome-ai-research-writing)
- [blader/humanizer | ⭐ 4751 | Claude Code skill that removes signs of AI-generated writing from text](https://github.com/blader/humanizer)
- [dwzhu-pku/PaperBanana | ⭐ 3458 | PaperBanana: Automating Academic Illustration For AI Scientists](https://github.com/dwzhu-pku/PaperBanana)
- [op7418/Humanizer-zh | ⭐ 2932 | Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。](https://github.com/op7418/Humanizer-zh)
- [BlockRunAI/ClawRouter | ⭐ 2337 | Smart LLM router — save 78% on inference costs. 30+ models, one wallet, x402 micropayments...](https://github.com/BlockRunAI/ClawRouter)
- [mindfold-ai/Trellis | ⭐ 2187 | All-in-one AI framework & toolkit for Claude Code & Cursor](https://github.com/mindfold-ai/Trellis)
- [benjitaylor/agentation | ⭐ 2141 | The visual feedback tool for agents.](https://github.com/benjitaylor/agentation)
- [ComposioHQ/secure-openclaw | ⭐ 1482 | A personal 24x7 AI assistant like OpenClaw that runs on your messaging platforms. Send a m...](https://github.com/ComposioHQ/secure-openclaw)
- [f/textream | ⭐ 1173 | Textream is a free macOS teleprompter app for streamers, interviewers, and presenters. It ...](https://github.com/f/textream)
- [jlia0/tinyclaw | ⭐ 1086 | TinyClaw is a team of personal agents that collaborate with each other](https://github.com/jlia0/tinyclaw)
- [promptpirate-x/discord-id-bypass-tool | ⭐ 988 | A verified tool that works on any potato computer that will let you bypass discord verific...](https://github.com/promptpirate-x/discord-id-bypass-tool)
- [tw93/Kaku | ⭐ 970 | 🎃 A fast, out-of-the-box terminal built for AI coding.](https://github.com/tw93/Kaku)
- [hesamsheikh/awesome-openclaw-usecases | ⭐ 1933 | A community collection of OpenClaw use cases for making life easier.](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- [op7418/CodePilot | ⭐ 1815 | A native desktop GUI for Claude Code — chat, code, and manage projects visually. Built wit...](https://github.com/op7418/CodePilot)
- [The-Vibe-Company/companion | ⭐ 1798 | Web & Mobile UI for Claude Code & Codex . Launch sessions, stream responses, approve tools...](https://github.com/The-Vibe-Company/companion)
- [PeonPing/peon-ping | ⭐ 1738 | Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, and other IDEs. St...](https://github.com/PeonPing/peon-ping)
- [xyzeva/k-id-age-verifier | ⭐ 1276 | automatically verify your age on discord, twitch, kick, quora and more (k-id)](https://github.com/xyzeva/k-id-age-verifier)
- [SumeLabs/clawra | ⭐ 1270 | Clawra - Openclaw as your girlfriend](https://github.com/SumeLabs/clawra)

### 🌍 Yahoo Finance 原文 (13/13 条)

- [美股 | 标普500 (^GSPC) | +0.24%](https://finance.yahoo.com/quote/%5EGSPC)
- [美股 | 纳斯达克综合 (^IXIC) | +0.16%](https://finance.yahoo.com/quote/%5EIXIC)
- [美股 | 道琼斯工业指数 (^DJI) | +0.11%](https://finance.yahoo.com/quote/%5EDJI)
- [美股 | 罗素2000 (^RUT) | +0.91%](https://finance.yahoo.com/quote/%5ERUT)
- [美股 | VIX波动率指数 (^VIX) | +2.69%](https://finance.yahoo.com/quote/%5EVIX)
- [港股 | 恒生指数 (^HSI) | -1.72%](https://finance.yahoo.com/quote/%5EHSI)
- [日股 | 日经225 (^N225) | -1.21%](https://finance.yahoo.com/quote/%5EN225)
- [韩股 | 韩国综合指数 (^KS11) | -0.28%](https://finance.yahoo.com/quote/%5EKS11)
- [欧股 | 英国富时100 (^FTSE) | +0.20%](https://finance.yahoo.com/quote/%5EFTSE)
- [欧股 | 德国DAX (^GDAXI) | +0.14%](https://finance.yahoo.com/quote/%5EGDAXI)
- [欧股 | 法国CAC40 (^FCHI) | -0.40%](https://finance.yahoo.com/quote/%5EFCHI)
- [A股 | 上证综指 (000001.SS) | -1.26%](https://finance.yahoo.com/quote/000001.SS)
- [A股 | 深证成指 (399001.SZ) | -1.28%](https://finance.yahoo.com/quote/399001.SZ)

### 🌐 联网检索原文 (20/20 条)

- [2026-02-14 07:16 新浪财经 | 道指标普录得3个月最差单周，亚马逊九连阴，英伟达苹果跌超2%，黄金夺回5000美元 - 新浪财经](https://news.google.com/rss/articles/CBMibkFVX3lxTE5taUw3Uzd4aWVRcF9hR3B6NWpuQ2NiYmJvMkViZVVHLVpmb0JFSDd3c1Itb0xmbnk5NzRndEFGeXRmbERaOVdNX3k2V0U3OEViVGhYZ1pQREdXU1B0Q1AzNHJaQjhkaDgtMHpZUWZn?oc=5)
- [2026-02-14 06:06 SOHU | 金融股市场动态：建设银行美股表现如何？ - SOHU](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOUFFYUzlxbkZteWE1TE5jZzl3S3BpcUY5TDU2Z20yeHl2a20tLW1RQWlwSXBMSU9WcnRmNnpWVWFNS2RlenItYlg5VTNqS3RpeG95S0VVS1l3LWtxclQ5eTJnVV9LTXFsVWN0U2JqN2pPTUFKWGNTcF9pUTdGeUdrd1N1Z3BTOW10LUNV?oc=5)
- [2026-02-14 05:31 英为财情 Investing.com | 美国股市涨跌不一；截至收盘道琼斯工业平均指数上涨0.10% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxQXy1BaHYxdktCYXBkSmUzT3J1MnBxQ0JGTFFoNVFDdDRSa0toM0tIM21RVGZ3YUxXQmN1TDhEZXh0dWZXY0ljcnlscHJBR05zYjFmeHdLcndmcldFN2tVQkY3a0kzOVNIOG9jaFZfWDlVanduR0o0elFfUElZRFpYbg?oc=5)
- [2026-02-14 04:01 Cryptopolitan | Ethereum 价格预测（2026、2027、2028-2032 年） - Cryptopolitan](https://news.google.com/rss/articles/CBMib0FVX3lxTE1sSGFYRTBCTFNocFJzZ0JiZFo3MlRNUXQ5VUFSdkkzY05yY1pFVmlsclE3bEhWSVk4Mm5oaWNEVHhtX1N5SlREczNJaS01M0VqaEhoYXNnU3NfeEdNOFBfQXQ3OVlwX0ZWMlJHTTFRbw?oc=5)
- [2026-02-13 23:39 Binance | 超过30%的供应被锁定：以太坊质押潮在价格触底周期中创下纪录| Htp96发布于币安广场 - Binance](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrZ2poRWt6eWdVakVlR0YyQmNRUlJ0aVZZcWs1SjFJdVpmeEw2N0NUc2xfUmRzb3FORWRLR2o5R0E2VU45ZmVSUWFQTXRmbEVuOHhRUmJBTWlQODNlNzdDQ1I0d054RXdu?oc=5)
- [2026-02-13 22:48 新浪新闻_手机新浪网 | 财经资讯AI速递：昨夜今晨财经热点一览 丨2026年2月13日 - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMidEFVX3lxTFBlVDM4dDBnOVdjMW90TkZBZTVBR3BjSXF3V3JOUWtKTjBmR2tMWHo4d09nMTR0ZmpxTXNnbTVpdC16ZXJTb0t5bm9qODd6WjdnTDBNdjRqY0FoN0JzUDl0amRzUVowbkdTYW50Rmo4dnkyTEw5?oc=5)
- [2026-02-13 22:26 新浪新闻_手机新浪网 | 科技资讯AI速递：昨夜今晨科技热点一览 丨2026年2月13日 - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMidEFVX3lxTE5iTFRnUEc1MTZXQ2ptend5TEh0Y0FmWDcyZTA1MWFBWTlNNTEwMExJXy0ySVREUl9DUEI0MDUwY3JMd0FfVUtNWTB0SURkZXlnRzNWX18wa3ZnUFJPTWlET1hPQ2EyRVFOMW42YWV4cXE1NlVn?oc=5)
- [2026-02-13 22:13 财新 | 美股三连跌 “AI替代”恐慌情绪从科技蔓延至物流、地产等板块 - 财新](https://news.google.com/rss/articles/CBMiZEFVX3lxTE4wZlllYXhaX1NEX3A1bXljUDdnTFNhYVU0bi1WbnZVNzZtWGl0TEdwMkdHcGxva1hjZGppNkxVQVFIM3FuR0ZtT29kWWRYRzdYWG9zekdpOV9mUlYtNUdRLTZQWG4?oc=5)
- [2026-02-13 20:11 新浪网 | 央行节前发布重要数据：社融增量7.22万亿元 - 新浪网](https://news.google.com/rss/articles/CBMimAFBVV95cUxNTVhxamF5ajMyYmdxLXhhc2ZHYkJkTlJhLURpZk1xQXpOY1BQZTJKdE5vcTFxX1dNZXdueS1XLTlIOVZOcWNvTFhfb0dtWXQ2ajl6QUJOb2NVLWI5YjZyNmR4SGRpT043UHpiOUJKUEhiRDQxdzdFckVuRUptdS1kdHQ4RkptQk5vUl82SnA0dXN3bUxYbkhrbg?oc=5)
- [2026-02-13 18:30 英为财情 Investing.com | 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.30% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMigAFBVV95cUxOOFVwdXJrMWltM20zd3ZoUjgxRC1OTE1jZlZvVGJkcnlGRzhEenJPemVMQk9SamctR3R6bHVOOUFqM2RpbU96Wk9pWS02SlVybGtPWlQ0bzV5al8xbkRRUjdLSkRaemRnZVRMWFFyaFNyZ0pwZEhuZ3YxMEREa3lrSw?oc=5)
- [2026-02-13 17:50 新浪财经 | 港股复盘 | 年内最强新股诞生 “AI除幻第一股”海致科技集团港股上市首日涨超242% - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE52X29JZnl3Z2o0YTVZWkVSQWNGdjFrYTNvTGk0LVlCTkl6UGliTkNIdE43VlY2ZFpLb0taZWh6cFBSWGpHVjdGdDFXekw2aUJlZlE4TUNYVDUxa3FheEpoNXBFdWowUDdiN1hrNWlMVEdjRE01V3ByVg?oc=5)
- [2026-02-13 13:10 手机新浪网 | OpenAI指控DeepSeek侵权_新浪新闻 - 手机新浪网](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1GSmZxeUNvbFBvMF9vMU8zUFRFQXZzb21NbU5kNzlQaFhvcmh1dGlBcEpiaTNhYVluVDhURUlMUXBzYmltQ3hSVW1Ta2FxYmlmWVUxSFlkRXdUN1o2Y05SN1ltMA?oc=5)
- [2026-02-13 09:35 同花顺财经 | 金银巨震，美股重挫 - 同花顺财经](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBaNUR1OE9kekMzNUxHSm41MHl5MU5Ybk1KUzAwNGFqTXl2RE03d3JoT0lxSmhTWkVWYk9XSWswX3dwZjkycFRvZDhQYUJYZUEtOEI3LUlHcHhEYTB1T2c?oc=5)
- [2026-02-13 07:43 证券之星 | 人民币延续升值趋势，中国资产受益链条明晰 - 证券之星](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBPR0ZDSlctc0lTVGRacGV1dnRPQ0k0QUpTU25iR1daVlBLOUtwMmNoQjNSNngydHJ2b285M0VweVpLdjZoNlpUUFZLd3pJcy14S0E2bjY1VVZQaFVUc1ZBejZNUDE?oc=5)
- [2026-02-13 06:34 富途牛牛 | 金银、股集体下挫，恐慌指数VIX飙升，三倍做空纳指ETF涨超6% - 富途牛牛](https://news.google.com/rss/articles/CBMipwFBVV95cUxQMkx2ZjF0WHJPVjNoQm5hNXhpVjZEMnF3ODRuWm5UOFhKWnlObTlWR25qQUpfZ1dYQk1rUmt2OFcxZWwyYjFBaTh2UDBBdDJnYXVZUW9PTTRqcGluV1VWRnJ2dWhEQUpobTZ4S3FFdHBvWmtJS3NMUWJ1SW5Xb1poWmhfUjhjVkJsNGtFUkNxbnVBQ014YU41aEw0ZHpvNHJsbl9aczk4dw?oc=5)
- [2026-02-13 05:11 新浪财经 | 2月13日收盘：美股收跌纳指下跌2% AI发展令多个行业承压 - 新浪财经](https://news.google.com/rss/articles/CBMihwFBVV95cUxOVEhzbFF0bFphZ3pvTDJ6bXBHWlVDTDA2QzdId2VDZWdSY1VnMmFadmROVnplT1Z5b0oyNW1xdXB4RG5hc2RmRU4tM1FRNUxsR0tfYjRudkY5Wk9kYmxnYkQxU19IdVhYRHVwZGFud1dkZjI2eHdWTTNxdlJ3ZGpsd3Jia3RxQzg?oc=5)
- [2026-02-13 00:17 新浪财经 | 10000亿元！央行最新预告 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE9YdzVUY0d1Ymk5SlZiWkJBMDN3OHktb3d4UFl4WWpuTE5rLWxJcGEybG5HRUItb1R6YnBEV2FicDZpV3g2Y0xKdC0xWU5MVm8tb3RyWmRQTnVqSFZUZXdSM0ZHSFFBMUJ1QWlJc09MU25kSzltbmJDeA?oc=5)
- [2026-02-12 21:35 新浪网 | 央行明日开展1万亿买断式逆回购操作，分析师：降准必要性降低 - 新浪网](https://news.google.com/rss/articles/CBMiwglBVV95cUxPZVdwT09vSjFMeVViSGhldTJjMG9Qd0VrTHM4RnRlRVFuNzdhaUV4T0VIVGE2djdwOVdXWk5nMXJDR2pmZm1UbkY0R0JueGZibkVpOTZoMG5HX1luUUNLbFBrcnJHMTFkYXdZTFlqQVRFRmlhTDR6TGQ1UnJZNERjclN2ZmJiUmhhTzd4cngwQXB5QmVqdFVncHJaaUpwR2JVci0zZEVOM3NnejU4bWNDc3drQjF6ZXNQdUhxbTNKaUtPMEQyY2tNWVhSYmxWZWZXcUN6TTZqeE1SYmhtUEVyNHE2Q1FCRUk3YkNTVlhhR2QycmowNHVUQ2FNcnY4WHRfUzljMm9tQUhKMklnZkl2TDJQWDY3anVWVm9tMldxMFVzTGFSTjU5eWNGbEV5Yk41V3lteUtQb1dqeTBvdDhKeDhTeWxJUmVySkNDOEJSZ0k5WlJRcl90RlVtMFhkbFYwSG80aVMtN3BNalRyOUxycXpPeVFnWktPdkdGQ05wOEI4UGFJenAzSF9aLTYxbk9JNDVGaGZhZDdkNkRFa0hXaUVadDJsM0t6TGZIWS1ySm5DczNPYVVlNUhfS0VjUjFlTXlRdWo0cElocUw4d3U4bEkxaTFTRURUQmRTVlNQb1libENZTFVwbkpiWUFnaDU4S3pSLVA5aGxaWUpGRU9ReTRKQzJyUDM3em40Rk1mQ1Y1bkJaM1dNZjVCeGJtNmNtY3RnMDJsM0k1YWZQQ0phR1Faa1E1ZDNPTzNITHBrdzR3aE1GSHE4dXMwdGI1LV9WYktJbE5uSXB1anB3WWdoNE9Ma2JMazFrVExNd2NET1NFR2ZiZ3FodjM4OWh2amplb1RvOXZkOWFmekN3Sm1JOVgxd3JHSEZzeVFqMDkycW41bVFHZ2NqNXdNWmk2TnFlczBubVlvTXVubHkwTFZzdG5TaGg1Z1c0ZWE2LUE1MEZlTWozZE5nQkMxTzhmNDVpaVo5aHppOElWMzdrMDV6c2g4RGhLZzA2UTBoSUowaWxhVmJmVy0zRUdrRGVZN0J4VzZqaTdiWjI5a0wwUHdNeUdqTHd4X004YWUxbVoyOVBhd280NkRIaUJfTzlZQ3l1ajlDbmtKQmlFbFEzQ0V0NG5JeEhGMldIbm5ydlhXYkFGMTVUZHVIdnpWNnJCNzJUZ0libGQwZGxjQ0VISTdtejFDSWstclBRcVl1WGRteHlBRElfdFFHVFZrZzdjMDd3Nkx2UkVrMDlHRWplVTVxcDAybEEybkNxdk5WTWowY1R4MzB0Y0g4czN4RU9JaWVKaHJjM1B2QzFudC1GM3AtMUppVXUxbURfcndwUWxUNmF3dkhaTEZRellGcVZLa3ZBb2RLRFoxX3M3SWZHYmxmX25oM0pDV1FTVWxSMkloMjBndVR0Xy1zdlY0Q0RybURYdDVWcE0zY0tsYXI4TDdqdU9BcVlxbUh0RmRZc0cta1ZmdUNtS1o0UXJ2SVVVaTNTUWx6Qm96ZlBKdkZSSDN2WTMtQkNqY1NLQ0hHdFROT3plXzBOalJ0bUxjbmlOdlRyYXR2Y0VZQ3hrTDNmZ1JITEk3MmpjelVqXzc4b1Q3djhYZVFLWTNtdC1PNFRpZFl6VXc?oc=5)
- [2026-02-12 15:50 Yellow.com | Uniswap 巨鲸在由 BlackRock 推动的 42% 暴涨中抛售 2700 万美元 - Yellow.com](https://news.google.com/rss/articles/CBMimwJBVV95cUxPdmZhXzBOZ3pITDdiTHhoQXFIeEMtS2Y2dmkzYjBnMnJSS1NxalRMTy1TR3ZwaGJIWmgwdTBmVnlEWG40OGZoNTJhREhYd0JBM2ppQkdlU3RZNmdGdmVYR0JsVXQ3RVZSVHFuRjBzMjUzVEt5VzZhaGtUZEVzdjZxRnUteUh4b21zTDZEajhKT2tRUnJrSmU0NFFOeVNPcmhmOE5QLWJhYTUzdWRBSHhzVG1iUFY4SE1na25UTk5HR2FyR0JRTnQwVF80VkFoUTcyWGRhTFM1SXZhVWZXSEkzRDlDWGJFMGVEdklhYWdLUVV1cVdUNmtvcnFfTDhWcXIwaU5ldkdwc0FHN0cwV3pLRUd2X204WmpxbVhR?oc=5)
- [2026-02-12 12:09 NAI500 | 美股走势分化凸显AI焦虑，就业利好难掩科技板块抛压 - NAI500](https://news.google.com/rss/articles/CBMi1AJBVV95cUxQQmNzbEdYQnRCZlhrSzFORDdoOUNBNjNOb3NGakhqdElUVVMxT0h3cndSQ2ZldUtadVdmVk5CcHFSdmtsR3FsdkNwOG9QVUhPSDlvem1ZUElZaVFrbXItemRPN3FPSmltbXBiaVVJSXZPSFY5Z0ZqS3pHZF9KaGZLZk9YMVVReGdtaWRRQzFPTmJDRUJIT2FjbGR1bzJrN0RQSGRoSXJobHo2LTRod1pWTHZhcEdEZWZwamRLSWxyVmhwRXhIYVB3Mnd4V2pYSURQeWtyZFBmWEJUd2REMV9RT1B3MklNY3hlekNWRW9Mc3FTdTN0SDVrZ0tsalZ2TDlhS1hfeW9VVGd4MS13Wi1WMWcteDMyUUFVaWR2dENSZElOcXBZS1pReU9sVkNDaF9sY3NwX1AxclNYTnk0U3FGQXc4LXp6MXQ0RVQwQktqVTdQUlc5?oc=5)

---

*报告由 finradar 自动生成 | 2026-02-14 11:44:10（北京时间）*
