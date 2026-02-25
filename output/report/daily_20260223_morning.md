# 📰 finradar 🌅 早报
**2026-02-23** | 🌅 早报 | 覆盖时段: 昨日20:00 → 今日08:00 | 市场状态: ✅ 正常交易
生成时间: 2026-02-23 08:03（北京时间）

---

## 🚨 数据源健康提醒

1. 检测到微信登录异常：财联社: invalid session。请重新扫码登录 wechat-exporter。
2. 微信登录凭据最近更新已 5.4 天（阈值 4 天），建议尽快重新扫码登录。
3. 本次抓取公众号文章为 0 篇，账号搜索失败占比 100%，请检查登录态或服务状态。

处理建议：
1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。
2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。
3. 然后执行 `./scripts/local.sh report morning 20260223` 与 `./scripts/local.sh notion-push morning 20260223` 覆盖 Notion 页面。

# 🤖 AI 分析摘要

## 一、摘要
- **社会**：国内舆论延续对**米兰冬奥会**的关注，谷爱凌卫冕金牌及中国队奖牌收官引发全网热议，形成积极社会情绪[NW03, NW04, NW07, NW12, NW14]。同时，**春节返程高峰**成为新焦点，“半夜出发的大聪明全堵在高速上了”等话题登上热搜，反映公众对交通拥堵的集体共鸣与情绪宣泄[NW01, NW09, NW10]。
- **经济**：**全球贸易政策不确定性仍是核心宏观变量**。特朗普宣布将全球进口关税税率从10%加码至**15%**，引发市场关注与潜在的企业诉讼潮[NW05, NW13]。同时，有分析指出美国最高法院此前阻止关税的裁决后，特朗普正寻求新的政策路径[WB05]，显示政策博弈仍在持续。
- **市场**：隔夜（覆盖时段）全球市场呈现**显著的“西强东弱”区域分化**。**欧美股市普遍走强**（法国CAC40 **+1.39%**，纳斯达克 **+0.90%**），VIX指数下跌**-5.64%**显示风险偏好回升。**亚太市场（除韩国外）普遍承压**，日股、港股下跌。**韩国股市逆势暴涨+2.31%**，Twitter线索将其归因于打击裸卖空政策[TW07]。原油与加密货币同步回调。
- **科技**：AI领域呈现**工具化普及与价值反思并存**。GitHub热门项目显示，**AI工作流/智能体构建平台**（如Langflow、Dify）竞争白热化，反映应用层开发门槛降低的趋势[GH07, GH08]。同时，Twitter上出现对AI受益者仅限于大公司的批判[TW08]，以及对OpenAI CEO将AI与人类婴儿训练成本类比的言论的驳斥[TW11]，显示技术普及伴随深层社会伦理讨论。

## 二、分板块汇报
### 2.1 市场概况（仅有效交易时段数据）
较上期：区域分化格局加剧，欧美市场走强与亚太市场（除韩国外）走弱形成鲜明对比，韩国股市出现独立暴涨行情。

**发生了什么**：在覆盖时段内，**欧美主要股指全线上涨**，法国CAC40领涨（**+1.39%**），德国DAX（**+0.87%**）、标普500（**+0.69%**）和纳斯达克（**+0.90%**）均收高，市场恐慌指数VIX下跌**-5.64%**。与之相反，**亚太市场普遍下跌**，日经225指数下跌**-1.12%**，恒生指数下跌**-1.10%**。**韩国综合指数（KS11）逆势暴涨+2.31%**，表现异常突出。大宗商品方面，WTI原油（**-0.77%**）与布伦特原油（**-1.42%**）下跌，主流加密货币同步回调（BTC **-0.50%**, SOL **-2.90%**）。

**为什么会这样（证据强弱：中）**：
1.  **欧美市场走强**：可能与市场对欧美经济前景的相对乐观情绪有关，VIX指数显著下跌印证了风险偏好的提升。但具体驱动事件（如经济数据、央行政策信号）在输入材料中**数据不足**。
2.  **亚太市场承压**：除韩国外，日本、香港等市场下跌，可能受到地区性经济担忧或前一日情绪的延续影响，具体原因**数据不足**。
3.  **韩国股市独立行情**：Twitter线索指出，韩国股市自打击裸卖空行动以来已累计上涨近150%[TW07]。本次单日暴涨**+2.31%**，可视为该政策效应的持续发酵，市场解读为监管强力干预提振了投资者信心。**证据强度为中**，因该解释与历史关注及市场表现吻合，但缺乏当日具体的资金流或政策细节数据。
4.  **原油与加密货币回调**：两者同步下跌，可能反映部分资金从高贝塔风险资产中撤出，转向股市，或是对全球增长前景的短期担忧。具体催化剂**数据不足**。

**下一步观察**：
1.  确认韩国股市暴涨是否伴随巨额外资流入，以及领涨板块是否集中于此前被严重做空的领域。
2.  追踪欧美市场乐观情绪的来源，关注即将公布的欧美经济数据及央行官员讲话。
3.  观察原油与加密货币的下跌是短期技术调整还是趋势性转变的开端。

### 2.2 微信公众号共识与弱信号
数据不足。输入材料中未提供“微信公众号逐篇简介”或可引用的公众号文章内容，无法提炼共识议题或弱信号。

### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）
较上期：AI领域持续聚焦于**应用层工具平台**，金融科技出现**预测市场交易机器人**，Web3则集中于**安全工具**。

1.  **`Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot` (⭐601)**：这是一个针对**预测市场Polymarket**的自动化交易机器人，使用RSI和MACD指标进行15分钟级别的交易。**应用场景**在于高频、短周期的预测市场套利。**可落地价值**在于为熟悉技术分析的交易者提供了自动化工具，可能提升交易效率。**噪音风险**极高：预测市场本身波动大，策略有效性未经长期验证，自动化交易可能导致快速亏损。
2.  **`openclaw/openclaw` (⭐218570)**：项目描述为“任何OS、任何平台”的个人AI助手。**应用场景**是打造跨平台的通用型AI助手。**可落地价值**在于尝试构建一个统一、开放的个人AI入口。**噪音风险**：概念宽泛，相较于操作系统级集成助手（如Copilot），其独特优势与具体功能**数据不足**，可能面临激烈的竞争和清晰的定位挑战。
3.  **`langflow-ai/langflow` (⭐144969) 与 `langgenius/dify` (⭐130007)**：两者均为**低代码/可视化AI智能体与工作流构建平台**。**应用场景**是企业或开发者快速构建、测试和部署基于大模型的应用程序。**可落地价值**显著，能大幅降低AI应用开发门槛，是AI产业化落地的关键工具层。**噪音风险**：该赛道竞争高度同质化（同榜单还有n8n），存在概念炒作和未来市场出清的风险，最终可能只有少数平台胜出。
4.  **`MetaMask/eth-phishing-detect` (⭐1259)**：这是一个用于检测以太坊网络钓鱼域名的开源列表。**应用场景**是为MetaMask等钱包及安全产品提供威胁情报。**可落地价值**明确，直接关乎用户资产安全，是Web3生态的基础设施。**噪音风险**：其防护效果依赖于情报的及时性和准确性，属于被动防御，对新型诈骗手段可能存在滞后性。

### 2.4 Twitter 海外信号（英文内容中文汇报）
较上期：新增对**美国就业数据的担忧**、对**AI发展受益者的批判**，以及关于**比特币周期演变**的叙事。

1.  **宏观经济信号**：有推文引用NBC报道称，“美国经济在2025年经历了几乎零就业增长”[TW04]。此信号若被市场广泛采信，可能强化对经济放缓的担忧，影响美联储政策预期。但该信息仅为单一媒体引用，**证据强度为低**，需官方数据验证。
2.  **AI社会情绪与批判**：一条高互动推文尖锐指出：“AI发展四年，唯一受益者是：1. 销售AI的公司；2.  actively turning computing and internet into shit的人”[TW08]。这延续了历史报告中“讨厌AI很酷”的情绪，反映了部分群体对AI技术红利分配不均及网络环境恶化的不满。另一条推文则展示了AI对OpenAI CEO Sam Altman言论的反驳，Alt曼称训练AI耗能高，但训练人类婴儿也要20年和食物，AI则批评此类比忽视了人类生活体验的内在价值[TW11]。这显示了AI伦理讨论的复杂性。
3.  **加密资产叙事**：有观点认为“比特币周期正在进化”，未来回调会更浅，创新高会更频繁，更像传统股票指数[¹](https://twitter.com/KillaXBT/status/2025536229488390456)。这是一种典型的牛市周期叙事，旨在塑造乐观预期，**证据强度为低**，属于市场观点而非事实。
4.  **Web3/AI结合创新**：Claw Mode项目宣布将在Solana上推出“非同质化代理”（NFA），描述为可拥有、可自主交易的链上AI代理资产[TW14]。这是AI与Web3结合的一个具体案例，将AI代理资产化，值得关注其后续发展。

### 2.5 国内新闻与政策脉络
较上期：社会热点从冬奥盛事自然过渡至**春节返程高峰**，经济层面持续关注**美国关税政策动向**。

1.  **社会热点：春运返程拥堵引发全民共鸣**。“上了高速发现全是聪明人”、“半夜出发的大聪明全堵在高速上了”等话题登上百度、微博等多平台热搜[NW01, NW09]，反映公众对集中出行导致的交通拥堵既有无奈也有幽默式宣泄。同时，“亚洲最大收费站出口全开迎返程潮”的报道[NW10]显示了管理部门的应对措施。此社会情绪短期可能影响相关出行服务平台的用户口碑，但无直接重大市场影响。
2.  **经济政策：美国关税政策仍是焦点**。财联社与华尔街见闻均报道，特朗普宣布将原本10%的全球进口关税税率提升至**15%**[NW05, NW13]。同时，有分析文章探讨“美国对华哪些关税被停止征收？”[NW06]，以及在美国最高法院阻止部分关税后，“特朗普开辟新道路”[WB05]。这表明关税议题处于动态博弈中，**持续增加全球贸易政策的不确定性**，可能扰动全球供应链和汇率市场。
3.  **产业与资本：外资配置逻辑探讨**。有观点指出，外资配置逻辑转向长期持有“优质盈利驱动型资产”[WB01]。这与此前市场关注的外资流向变化相呼应，若形成共识，可能影响A股市场中具备持续盈利能力的核心资产的估值逻辑。

## 三、明日跟踪清单
1.  **延续跟进：韩国股市独立行情的驱动逻辑验证**：结合历史多期关注，需尽快补充韩国市场在近期交易日（特别是2月23日暴涨日）的详细盘面数据、板块资金流向（尤其是外资）及是否有新的政策面消息，以确认其强劲表现的可持续性与具体驱动因素[TW07]。
2.  **收口复盘：美国加征关税（15%）的后续市场与法律反应**：紧密跟踪美股、汇市及全球主要贸易股指对关税加码消息的消化情况，同时关注美国国内企业诉讼进展及他国可能的反制措施声明，评估其对全球供应链情绪的二次冲击[NW05, NW13, WB05]。
3.  **新增观察：AI工作流平台（Langflow/Dify等）的竞争态势与商业化进展**：跟踪这些高星项目近期的版本更新、企业客户获取情况以及融资动态，评估AI应用开发工具赛道是否已出现明确的龙头，以及其商业化落地速度。


---

<details><summary>📑 点击展开各板块详细分析</summary>

### 📊 市场数据详细分析

### 1. 主要市场走势判断
全球股市呈现**区域分化**格局。**亚太市场普遍承压**，其中韩股（**+2.31%**）是唯一显著上涨的例外，而日股（**-1.12%**）、港股（**-1.10%**）和A股（**-1.26%**）均下跌。**欧美市场则整体走强**，法国CAC40（**+1.39%**）、德国DAX（**+0.87%**）、英国富时100（**+0.56%**）以及美股三大指数（标普500 **+0.69%**，纳斯达克 **+0.90%**，道指 **+0.47%**）均录得上涨。市场整体风险偏好呈现“西强东弱”的特征。

### 2. 关键资产轮动分析
*   **领涨方向**：**欧洲股市**表现最为突出，尤其是法国股市。**美国科技股**（以纳斯达克指数为代表）也表现强势。这表明资金在覆盖时段内偏好**欧美发达市场**，特别是**欧洲区域**和**美国科技成长板块**。韩国股市的独立大涨（**+2.31%**）显示有特定资金流入该市场，但具体原因数据未提供。
*   **领跌方向**：**亚太市场（除韩国外）** 普遍走弱，领跌全球。**大宗商品中的原油**（WTI **-0.77%**，布伦特 **-1.42%**）和**主要加密货币**（BTC **-0.50%**，ETH **-0.79%**，SOL **-2.90%**）同步下跌，显示资金从这些风险资产中流出或缺乏买盘支撑。
*   **资金偏好解读**：资金在覆盖时段内明显从**亚太（除韩国）**、**原油**及**加密货币**撤出或观望，转而流入**欧美股市**。这反映出资金在区域配置上更青睐欧美经济前景，在资产类别上暂时规避了部分大宗商品和数字资产的高波动风险。

### 3. 加密货币和商品期货的关键变化
*   **加密货币**：主要币种普遍小幅下跌。**SOL（-2.90%）** 跌幅最大，表现弱于**BTC（-0.50%）** 和**ETH（-0.79%）**，显示市场内部出现分化，资金可能从小市值或特定生态代币中流出。
*   **商品期货**：**能源板块疲软**，两大基准原油价格下跌，其中布伦特原油（**-1.42%**）跌幅大于WTI。**工业金属（COMEX铜 +1.09%）** 和**天然气（+2.23%）** 逆势上涨，与原油走势背离，可能反映不同的供需预期。具体驱动因素数据未提供。

### 4. 涨跌驱动链条分析
基于现有数据，可梳理出以下逻辑链条，但需注意**所有链条的初始驱动事件/政策/情绪均因数据不足而无法确认**。

*   **链条一：欧美股市上涨**
    *   **事件/政策/情绪**：数据不足。可能源于对欧美央行政策、经济数据的积极预期，或市场情绪回暖。
    *   **资金行为**：资金流入欧美股市，尤其是欧洲板块和美国科技股。**证据（强）**：法国CAC40、德国DAX、纳斯达克指数等关键指数均录得显著涨幅。
    *   **价格表现**：欧美主要股指普遍收涨，美股波动率指数VIX下跌**-5.64%**，印证市场恐慌情绪下降。

*   **链条二：亚太市场（除韩国）下跌**
    *   **事件/政策/情绪**：数据不足。可能受到地区性经济担忧、汇率变动或前一日负面情绪的延续影响。
    *   **资金行为**：资金从日本、中国（港股及A股）市场流出或缺乏买入意愿。**证据（强）**：日经225、恒生指数、上证综指同步下跌。
    *   **价格表现**：相关市场指数收跌。

*   **链条三：原油与加密货币同步回调**
    *   **事件/政策/情绪**：数据不足。可能源于共同的宏观担忧（如对经济增长的疑虑）或美元走势的影响。
    *   **资金行为**：资金暂时撤离这两类高贝塔风险资产。**证据（中）**：WTI原油、布伦特原油与BTC、ETH价格在覆盖时段内均下跌，呈现同向波动。
    *   **价格表现**：原油价格与主流加密货币价格收跌。

*   **链条四：韩国股市独立行情**
    *   **事件/政策/情绪**：数据不足。存在强烈的特定国内利好驱动。
    *   **资金行为**：资金大幅流入韩国股市。**证据（强）**：韩国综合指数暴涨**+2.31%**，涨幅远超全球其他主要市场，呈现独立走势。
    *   **价格表现**：韩国综合指数大幅收高。

**总结**：覆盖时段内，市场主线是**资金从部分亚太市场、原油及加密货币流向欧美股市**，导致区域和资产类别表现显著分化。韩国股市因未知的强劲驱动因素走出独立行情。所有价格变动的根本性催化剂均需更多信息才能确定。

### ⏱ 市场时效过滤说明

市场时效过滤结果：
1. 早报阶段不纳入 A 股盘面，避免使用非交易时段快照

### 🐦 Twitter 逐条简介

Twitter 逐条简介（共 12 条，按互动热度排序）：
1. [热门] @Mericamemed | 2026-02-23T00:00 | 互动=24273
   原文摘录: Attention based economy. Thats why.
   原文链接: [点击查看原文](https://twitter.com/Mericamemed/status/2025480679710965820)
   1) 讲了什么：一条推文提及“注意力经济”，未提供具体事件或分析。
   2) 关键信号：推文仅提出“注意力经济”概念，无具体数据或事件支撑。
   3) 阅读建议：略读 + 原因：内容仅为概念性陈述，缺乏实质性信息。
2. [热门] @sycom_jp | 2026-02-23T00:00 | 互动=15474
   原文摘录: 《サイトリニューアル記念キャンペーン》 🌈 初めてのゲーミングPCにもおすすめ 🌈 G-Master Velox III AMD Edition が当たる！ 【応募方法】 ①@sycom_jpをフォロー ② この投稿をリポスト 【＋UPチャンス】 おすすめカスタム構成URLとタグを投稿👇 要リプで確認！ 〆2/25 2
   原文链接: [点击查看原文](https://twitter.com/sycom_jp/status/2022243980751290495)
   1) 讲了什么：账号发布网站更新纪念活动，抽奖送游戏电脑，要求关注并转发。
   2) 关键信号：高互动量（转发过万），活动截止日期为2月25日。
   3) 阅读建议：略读 + 原因：内容为商业推广抽奖，无具体金融科技信息。
3. [热门] @mefinho_ | 2026-02-23T00:00 | 互动=13036
   原文摘录: C’est la video la plus réelle que j’ai vu mdrrr Regardez !!!!
   原文链接: [点击查看原文](https://twitter.com/mefinho_/status/2025530673272885587)
   1) 讲了什么：用户分享了一段视频并称其非常真实。
   2) 关键信号：互动数据较高，但视频具体内容未提供。
   3) 阅读建议：略读 + 原因：原文无具体金融科技信息，仅为个人分享。
4. [热门] @unusual_whales | 2026-02-23T00:00 | 互动=10182
   原文摘录: "The US economy experienced almost zero job growth in 2025," per NBC
   原文链接: [点击查看原文](https://twitter.com/unusual_whales/status/2025586627972939822)
   1) 讲了什么：NBC报道称美国经济在2025年几乎零就业增长。
   2) 关键信号：数据不足/未提供。
   3) 阅读建议：略读 + 原因：仅提及单一媒体报道，无其他信息。
5. [热门] @bindass_ladki | 2026-02-23T00:00 | 互动=7627
   原文摘录: This man has been Prime Minister for 12 years. WORK : 0 VICTIM CARD : 24×7 People are fed up with all this now.
   原文链接: [点击查看原文](https://twitter.com/bindass_ladki/status/2025546268584673727)
   1) 讲了什么：用户批评某国总理任职12年但工作不力，民众已厌倦。
   2) 关键信号：未提供具体国家、政策或事件，仅为个人情绪化评论。
   3) 阅读建议：略读，因缺乏具体金融科技相关事实或数据。
6. [热门] @NevesRodrigo_ | 2026-02-23T00:00 | 互动=5163
   原文摘录: 5km, em estrada de terra, uma moto de uns 130kg, com uma criança na garupa e um sol de rachar E ele fez tudo isso sem reclamar por um único segundo Aí eu tenho 
   原文链接: [点击查看原文](https://twitter.com/NevesRodrigo_/status/2025305132267622488)
   1) 讲了什么：用户分享个人经历，并表达对某网络言论的强烈不满。
   2) 关键信号：推文包含情绪化指责，但未提供具体金融科技事件或数据。
   3) 阅读建议：略读，因内容为个人情绪宣泄，与金融科技主题无关。
7. [热门] @xMarketNews | 2026-02-23T00:00 | 互动=4801
   原文摘录: SOUTH KOREA STOCK MARKET HAS SURGED NEARLY 150% SINCE THEY TOOK ACTION AGAINST NAKED SHORT SELLING🚨 - South Korea Suspended Short Selling to Probe Naked Shortin
   原文链接: [点击查看原文](https://twitter.com/xMarketNews/status/2025296878707913043)
   1) 讲了什么：韩国股市因打击裸卖空而大涨近150%，并引入监禁和重罚。
   2) 关键信号：韩国股市大涨与打击裸卖空行动相关。
   3) 阅读建议：略读 + 原因：信息为单一事件陈述，缺乏具体时间、数据来源和详细背景。
8. [热门] @Sosowski | 2026-02-23T00:00 | 互动=4183
   原文摘录: We’re 4 years into AI and the only people benefitting from AI are: 1. corporations selling AI 2. people actively turning computing and internet into shit
   原文链接: [点击查看原文](https://twitter.com/Sosowski/status/2025561904010158211)
   1) 讲了什么：推文称AI发展四年，受益者只有卖AI的公司和破坏计算与网络的人。
   2) 关键信号：未提供具体数据或事件，仅为观点性批评。
   3) 阅读建议：略读，因缺乏具体事实支撑，属个人评论。
9. [热门] @mcafeenew | 2026-02-23T00:00 | 互动=3682
   原文摘录: 🚨TREASON ALERT: AOC BOOTED FROM HOUSE INTEL COMMITTEE IN MASSIVE SCANDAL – CAUGHT RED-HANDED LEAKING TOP-SECRET ICE PLANS TO RADICAL MINNESOTA ACTIVISTS! 🔗t.me/
   原文链接: [点击查看原文](https://twitter.com/mcafeenew/status/2025675756953915446)
   1) 讲了什么：推文称AOC因泄露机密被逐出众议院情报委员会，面临刑事指控。
   2) 关键信号：指控内容包含地图、特工姓名和藏身处；数据不足/未提供。
   3) 阅读建议：略读 + 原因：信息来自单一账号，缺乏独立验证，属热门讨论类型。
10. [热门] @iamrollandex | 2026-02-23T00:00 | 互动=2778
   原文摘录: Chatgpt is good for writing Claude is good for coding Grok is good for researching Gemini is good for study guide Deepseek is good for brainstorming Perplexity 
   原文链接: [点击查看原文](https://twitter.com/iamrollandex/status/2025300093562163569)
   1) 讲了什么：推文对比了多个AI工具在不同场景下的适用性。
   2) 关键信号：未提供具体数据或事件，仅为功能特点陈述。
   3) 阅读建议：略读，内容为概括性观点，无具体分析或新信息。
11. [热门] @korimakorima | 2026-02-23T00:00 | 互动=1975
   原文摘录: 批判の嵐になったサム・アルトマンの発言（「人々はよく、AIを訓練するのにどれほど多くのエネルギーがかかるかを指摘するが、人間を訓練するのにだって莫大なエネルギーがかかるでしょう、賢くなるまでに20年かかるし、その間に食べるフードが必要でしょう、と語って「コイツ、人間の赤ん坊とAIを同列に扱っとるぞ！」と大反発された）を
   原文链接: [点击查看原文](https://twitter.com/korimakorima/status/2025515099470143652)
   1) 讲了什么：用户让AI评论奥特曼关于AI与人类训练能耗对比的发言，AI批评该发言忽视人类成长过程的内在价值。
   2) 关键信号：AI反驳奥特曼，强调人类生活体验本身就是目的，而非仅为获取智能的成本。
   3) 阅读建议：精读 + 原因：展示了AI对人类价值观的解读及对科技领袖观点的反向批判，内容独特。
12. [热门] @pushpendrakum | 2026-02-23T00:00 | 互动=1478
   原文摘录: Imagine if just 25% of MPs spoke about real issues instead of caste math. Toll scams. Hospital loot. Insurance fraud. Bank charges. Creator rights. Sim incoming
   原文链接: [点击查看原文](https://twitter.com/pushpendrakum/status/2025466732975194578)
   1) 讲了什么：推文想象若25%议员讨论真实问题而非种姓政治，印度将焕然一新。
   2) 关键信号：列举了收费诈骗、医院掠夺、保险欺诈等社会问题。
   3) 阅读建议：略读 + 原因：内容为个人观点性呼吁，无具体事件或数据支撑。

### 🌐 Twitter 英文信号详细分析

### 海外英文信号主线
1.  **宏观经济与政策关注**：市场关注美国2025年近乎零的就业增长，以及特朗普政府将全球关税从10%提高至15%后，美股期货应声下跌。同时，韩国股市因打击裸卖空而大幅上涨的案例被提及，并引发对美国采取类似政策的呼吁。
2.  **对AI发展的批判与实用化**：一种观点认为，AI发展四年以来，主要受益者是销售AI的公司和破坏计算与互联网体验的人。另一方面，市场也关注AI的实用工具属性，例如不同AI模型在写作、编程、研究等领域的特长，以及利用AI在24小时内创建业务的潜力。
3.  **加密资产与Web3动态**：观点认为比特币周期正在演变，未来回调将更浅，新高出现将更频繁。同时，有项目在Solana上推出可作为链上资产铸造、可拥有且能自主交易的“非同质化代理”（NFA）。另有讨论涉及比特币被排除在《统一商法典》的货币适用范围之外。

### 金融科技/AI/Web3相关具体线索
1.  **AI应用细分**：ChatGPT（写作）、Claude（编程）、Grok（研究）、Gemini（学习指南）、DeepSeek（头脑风暴）、Perplexity（事实核查）、Copilot（微软工具生产力）被列举为各具优势的工具。有线索称可通过特定提示词，利用Claude在24小时内将想法转化为收入。
2.  **Web3/加密创新**：Claw Mode项目在Solana上推出“非同质化代理”（NFA），被描述为可拥有的、自主交易的链上AI代理资产，每季发行1000个。
3.  **加密资产叙事**：有观点分析比特币周期正在“进化”，底部反弹至新高的速度加快，未来可能像纳斯达克/标普指数一样频繁创出新高。
4.  **监管与法律地位**：有讨论指出，比特币被排除在《统一商法典》的“货币”适用范围之外。

### 可执行关注点与潜在误导噪音
**可执行关注点**：
1.  **关注AI代理与区块链的结合**：“非同质化代理”（NFA）的概念将AI代理与NFT、链上资产和自主交易结合，是AI+Web3的一个具体创新方向，值得追踪其实际运行模式和市场接受度。
2.  **关注宏观政策对市场的即时影响**：信号显示关税政策调整会立刻影响美股期货，提示需密切关注此类政策信号的释放时点与市场第一反应。
3.  **关注AI工具的差异化定位**：市场正在细化对不同AI模型优势的认知，这对AI产品投资、选型及构建基于特定模型的商业服务具有参考价值。

**潜在误导噪音**：
1.  **情绪化与未经证实的事件**：样本中包含大量政治指控（如美国议员泄密）、犯罪事件（墨西哥毒枭被杀）及阴谋论（QAnon）内容，这些信息真实性未提供验证，属于高互动噪音，需警惕其对市场情绪的短期干扰。
2.  **片面归因与简单类比**：将韩国股市上涨简单归因于打击卖空并呼吁美国效仿，忽略了其他潜在影响因素，结论可能过于简化。关于比特币周期将完全向传统股票指数演变的观点，也属于预测性叙事，需谨慎对待。
3.  **数据不足的论断**：关于“美国2025年近乎零就业增长”的说法，仅为单一媒体（NBC）的报道引用，未提供更广泛的数据来源或官方确认，其准确性有待核实。

### 📰 热榜详细分析

# 新闻热榜综合分析报告

## 1. 跨平台共同关注的3-5个热点事件
根据各分片摘要，跨平台共同关注的热点事件包括：
*   **特朗普关税政策**：分片1、3、4、6、7均提及。内容涉及特朗普宣布将全球进口关税税率从10%提升至15%（分片1、6）、政策已加码至15%并引发企业诉讼（分片3）、市场出现不同解读（分片4）、以及美国国内政治争议（分片7）。
*   **米兰冬奥会闭幕及谷爱凌表现**：分片4、5、6、7均提及。焦点包括冬奥会闭幕（分片4、5）、中国队收官成绩（分片6）、以及谷爱凌在自由式滑雪U型场地成功卫冕金牌（分片5、6、7）。
*   **春节返程高峰**：分片2、3、5、6均提及。社会关注点集中于春运返程拥堵（如“半夜出发的大聪明全堵在高速上了”、“第一批返程的人已堵哭”）、相关情感共鸣及交通议题。
*   **OpenAI动态**：分片2和分片7均提及。具体包括OpenAI大幅下调算力支出目标（分片2），以及被曝面临“四大困境”（分片7）。

## 2. 与金融市场相关的重要新闻
*   **关税政策的市场影响**：特朗普关税政策引发市场关注，分片4指出该政策出现“翻车”并被市场解读为利好，推动美股三大指数集体收涨。分片5提及市场关注“关税风暴”对全球经济的潜在影响。分片7提到美国一州长向特朗普追讨87亿美元关税，可能影响市场对贸易政策的预期。
*   **AI产业与投资线索**：分片4指出全球“内存荒”可能成为AI竞赛的关键瓶颈。分片1提及中国顶流私募Q4集体加仓拼多多并调整AI投资重心。分片4提到大摩评价AI模型公司MiniMax为“全球顶尖基座模型稀缺资产”。分片5显示市场关注“英伟达能否再救AI牛市”。
*   **A股关联事件**：分片1提及A股新材料产业链因春晚机器人展示被关注。分片3指出春节档电影《飞驰人生3》票房领跑，且“背后涉及哪些A股公司”受到关注。
*   **风险预警**：分片3提及SK会长崔泰源警告AI可能导致千亿美元利润瞬间转为巨亏，提示AI发展对大型企业盈利的潜在风险。

## 3. 科技/AI 相关热点
*   **AI产业发展与瓶颈**：**OpenAI动态**是核心热点，包括算力支出目标下调（分片2）和内部“四大困境”（分片7）。**硬件瓶颈**方面，分片4指出“内存荒”席卷全球，可能成为AI竞赛关键瓶颈。**模型进展与评价**方面，分片5提到智谱发布GLM-5技术细节并强调适配国产算力；分片4提及MiniMax被大摩评为全球顶尖基座模型。
*   **AI风险与讨论**：分片3提及SK会长崔泰源警告“AI正在吞噬一切”。分片6提到有观点提出“AI智能体新时代”，以及探讨大模型在专业领域面临的最难跨越的“门坎”（具体内容未提供）。
*   **其他科技动态**：分片7提及特斯拉发布没有方向盘和脚踏板的新车型。分片1提及春晚人形机器人展示带动A股新材料产业链关注，以及索尼关停Bluepoint工作室反映游戏行业整合风险。

## 4. 社会舆论焦点
*   **体育盛事与运动员**：**米兰冬奥会**及相关运动员（尤其是谷爱凌、苏翊鸣）的表现、赛后反应（如谷爱凌得知家人去世后落泪）以及关于金牌“含金量”的讨论（分片6），构成全民关注的舆论焦点。
*   **春节相关议题**：除**返程拥堵**外，还包括春节家庭关系（如“重新学会跟长辈相处”）、消费观（如存款100万讨论）、返程情感（如“返程前的告别”）、以及“春节译名之争”（具体内容未提供）等社会话题（分片2、5、6）。
*   **影视文化消费**：春节档票房破40亿元（分片3）、电影《镖人》票房逆跌（分片3）、以及导演韩延哽咽恳求为电影《星河入梦》增加排片（分片1），反映影视行业竞争与文化消费热点。
*   **社会事件与治理**：包括“江西丰城鞭炮炸死人”被官方辟谣（分片1）、“洗脚闹矛盾，男子跳桥失联”（分片3）、“喂猫起争执，男子遭恶邻杀害”（分片7）等事件引发的讨论，涉及虚假信息治理、公共安全与社会伦理。
*   **国际政治与民生**：美伊紧张局势（分片3、7）、韩美军方分歧（分片3）等国际关系话题，以及“肉要臭了”反映的物流问题（分片4）等民生话题，也受到舆论关注。

### 💻 GitHub 项目详细分析

# GitHub热门项目技术趋势分析报告

基于昨日20:00至今日08:00的GitHub项目样本，按“金融科技 / AI / Web3 / 通用”分类，筛选出最值得关注的5-8个项目，分析其应用场景、落地价值及潜在风险。

## 一、 最值得关注的项目

1.  **金融科技**：`Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot` (Polymarket交易机器人)
2.  **金融科技**：`alsk1992/CloddsBot` (开源AI交易代理)
3.  **AI**：`openclaw/openclaw` (个人AI助手)
4.  **AI**：`n8n-io/n8n` (工作流自动化平台)
5.  **AI**：`langflow-ai/langflow` (AI智能体与工作流构建工具)
6.  **AI**：`langgenius/dify` (智能体工作流开发平台)
7.  **Web3**：`MetaMask/eth-phishing-detect` (Web3钓鱼域名检测工具)
8.  **通用开发**：`tensorflow/tensorflow` (开源机器学习框架)

## 二、 应用场景与落地价值分析

*   **金融科技领域**：`Polymarket-rsi-macd-index-trading-bot` 项目专注于Polymarket的15分钟预测市场，提供实时监控与策略逻辑，其落地价值在于为高频、短周期的预测市场交易提供自动化工具。`CloddsBot` 则定位为跨市场（覆盖Polymarket、Kalshi、Binance等1000多个市场）的自主AI交易代理，旨在扫描市场优势并即时执行，其价值在于构建一个多市场、自动化的量化交易系统。`Mpesa-Based_Wi-Fi-Hotspot_Billing_System` 项目展示了移动支付（M-Pesa）与本地化服务（Wi-Fi热点计费）的结合，具有明确的区域化落地场景。
*   **AI领域**：项目呈现明显的“应用层”与“基础设施/工具层”分化。`openclaw` 致力于打造跨平台个人AI助手，是AI消费级应用的尝试。`n8n`、`langflow` 和 `dify` 均聚焦于AI工作流与智能体的低代码/可视化构建与部署，旨在降低AI应用开发门槛，是企业级AI落地的关键工具平台。`ollama` 和 `huggingface/transformers` 属于模型部署与框架层，为上层应用提供核心能力。`f/prompts.chat` 则围绕提示词工程构建社区生态。
*   **Web3领域**：上榜项目全部与**安全**相关。`eth-phishing-detect` 和 `destroylist` 都专注于识别和封锁针对Web3用户的钓鱼、诈骗域名，反映了当前Web3生态中用户资产安全是迫切需求，其落地价值在于为钱包、交易所等提供基础安全防护数据。
*   **通用开发领域**：`tensorflow` 作为成熟的机器学习框架，持续为各类AI项目提供底层支持，其价值在于生态的稳定性和广泛性。

## 三、 潜在泡沫噪音与重复概念

*   **AI工作流/智能体平台概念重复**：`n8n`、`langflow`、`dify` 以及 `AutoGPT`（虽未列入核心名单但热度很高）均涉及AI工作流自动化与智能体构建，功能定位存在显著重叠。这提示该赛道可能竞争激烈，存在概念炒作和产品同质化风险，最终市场可能只会容纳少数几个平台。
*   **金融科技项目的风险与验证缺失**：两个金融科技交易类项目（Polymarket交易机器人和CloddsBot）都宣称实现自动化交易与市场优势扫描，但其策略的有效性、长期盈利能力和在真实市场环境中的风险控制能力，**数据不足/未提供**。这类项目容易吸引寻求“圣杯”的开发者，但若无严谨的回测与风控，实际落地可能伴随巨大财务风险。
*   **Web3安全工具的局限性**：钓鱼检测工具主要基于已知威胁列表，对于新型、变种攻击的防御效果**数据不足/未提供**。其价值高度依赖于情报的及时性和准确性，可能存在“道高一尺魔高一丈”的持续对抗问题。
*   **个人AI助手的明确性**：`openclaw` 宣称是“任何OS、任何平台”的个人AI助手，但相较于其他项目，其具体区别于现有AI助手（如集成于操作系统的Copilot或语音助手）的独特功能与核心优势**数据不足/未提供**，概念可能较为宽泛。

### 🌐 联网检索摘要

联网检索共 8 条（关键词: 2026-02-23 全球市场 盘面 复盘 原因, 2026-02-23 中国 宏观 经济 政策 市场 影响, 2026-02-23 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 下跌 原因, “上了高速发现全是聪明人” 事件 背景, 黄牛亏麻!T1遭让二追三淘汰 事件 背景, 完美收官！谷爱凌卫冕自由式滑雪U型场地金牌，李方慧夺银 事件 背景）
1. [2026-02-23 07:56] thepaper.cn | 首席展望｜联博基金朱良：外资配置逻辑转向长期持有“优质盈利驱动型资产” - thepaper.cn
   摘要: 首席展望｜联博基金朱良：外资配置逻辑转向长期持有“优质盈利驱动型资产” thepaper.cn
   链接: https://news.google.com/rss/articles/CBMiYEFVX3lxTFA0M09zQ2JiS2Q5SlhYbmxtcDY2RUlXb1JNR1hGTGNwQjRnZEV6TUVJSlA2S09wM0xIS0UwYXdBUzM2NkF5NENwMzRYOEs4dElDVmZQVWxGYzc3R0JCS1dDZA?oc=5
2. [2026-02-23 04:27] 新浪财经 | 最高法院阻止关税重击后，特朗普开辟新道路 - 新浪财经
   摘要: 最高法院阻止关税重击后，特朗普开辟新道路 新浪财经
   链接: https://news.google.com/rss/articles/CBMi0gFBVV95cUxQLTFLQnBiTEJ3ek43WkxLc2RLNWhqbHByejhDcUdjRC1IX2xCVnhuVk5QRE5RNTN4R2g3aHhZNm9JbS1QMXAzSjdtOW5MeTd6cTJPQ3dmTFBLeUp1a29rdWJEUUxHVDJkY3RWZmZlak81bV85Nmo2TFl5R3kxcG54X1FWRGM5TnF3UHVsNTNROE9yVHRRT3k2dmJUSFZvb2NSLUpOTHd1aGU2S3d4b0ZyU3BRMktDdnNTT05IdUtuY1lHUTRyWWNCajdsZXpQWmtZUkE?oc=5
3. [2026-02-23 02:22] 3DM | [超话]#BET9是黄了吗 - 3DM
   摘要: [超话]#BET9是黄了吗 3DM
   链接: https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SS2liS1NyY0p6Zkk1c3E0SGNLU3p5SndvSlBhMkdqLXFiN0JNZG9TMzVZbzVxcGJwQzhCSTdVX2pnY2VRODlZU2RoV0FLVUk?oc=5
4. [2026-02-22 20:22] 游侠网 | 靠谱的博彩平台推荐「🔄神经镜像版」 - 游侠网
   摘要: 靠谱的博彩平台推荐「🔄神经镜像版」 游侠网
   链接: https://news.google.com/rss/articles/CBMiUEFVX3lxTE9rSndnV3ZaY3BoS0R3QmFFSHhuM3F2YjlBNzlIQUdnbzFGVUlYcjl3YnU3d1Q5akRBQzB0MzlMZUlKaU9sWnYyc2ZNaDhKbzFL?oc=5
5. [2026-02-22 12:15] FinanceFeeds | 2026年最值得投资的山寨币：APEMARS上涨，SOL和XRP下跌 - FinanceFeeds
   摘要: 2026年最值得投资的山寨币：APEMARS上涨，SOL和XRP下跌 FinanceFeeds
   链接: https://news.google.com/rss/articles/CBMi_gFBVV95cUxQT2lFUlNlSmhfSkMtYS1TdU5UX1E5YmJ1REVoNzlfQ3RnWFNxZVR1cDFkNk1acWUzT0Y4bDFCS2N1SkNlN2JfRmh0Zy11WkZNWVZfUGljTG1tclM1dF9uSnY5Z05tbmtQTWFOX0FmT0s4bW5VZ3JsYklCQTZRQ05GSW1oUjJlMW5WM1c1WnhNOEhuMFA0ZjJzOURNY0RjSnVKNVlmc2NpaUdpRVk3ME9pbnVnUGoxR2ItNUpDU2tjLWhfTFptSHNHSFBZR2lTcFhBbk9IVTJiano2XzRDZXpnV0FjN0g5Sk5GdFBuUlRLOUZvSWpxVVlqTmFUaXpaQQ?oc=5
6. [2026-02-22 12:05] yeeyi | 下周重磅日程：英伟达财报、特朗普国情咨文、美伊博弈、德总理访华-yeeyi - yeeyi
   摘要: 下周重磅日程：英伟达财报、特朗普国情咨文、美伊博弈、德总理访华-yeeyi yeeyi
   链接: https://news.google.com/rss/articles/CBMiVkFVX3lxTE1sRDlWQ1EzUzFKTk1weXo3TmNaRFVOemZ2X0FNLTNTNl9PcjlfUHJ4cXp4Uk82U0dlaGRaVUpSZlMxU09tZEpyWXJvYlNHRmt5VU5YQVVB?oc=5
7. [2026-02-22 09:48] 3DM | 第一热点 澳门新葡新京网站 - 3DM
   摘要: 第一热点 澳门新葡新京网站 3DM
   链接: https://news.google.com/rss/articles/CBMiV0FVX3lxTFBUdS1LYWlzcDVUQUIzUHR6S0dHSmtIY1FHandITld0NmtCVDBLdEVKNDZOclBhNHA5My16MUdfYXBFNGQ5LUFFUkpSWEZBV2tuZzA5V0xVYw?oc=5
8. [2026-02-21 11:03] 万维读者网 | 美股创20年来首年最差纪录 - 万维读者网
   摘要: 美股创20年来首年最差纪录 万维读者网
   链接: https://news.google.com/rss/articles/CBMiUkFVX3lxTE1WSDNxZ3dzeWFoNWZpMlk3T05wZ2RPbFZZSllnajdvWXU4T0pxWk13eW1pd2xDSkZNaEhSQXQ1cURwRl96YTBaZC1mMTA5ZnFmMVE?oc=5

</details>


### 📎 引用脚注

1. [2026-02-23T00:00 @KillaXBT | The$BTCcycles are evolving. Most people haven’t caught on yet. Each cycle, BTC is reachi...](https://twitter.com/KillaXBT/status/2025536229488390456)（Twitter，匹配分=100，来源ID=TW13）

## 🧪 引用匹配校验

- 已匹配引用条数: 1
- 未完成匹配标签: 0
- 低置信引用条数: 0
- 处理建议: 本次未发现低置信引用。

## 🎯 投机方向（超短）

- 海外指数方向：美股 VIX波动率指数 -5.64%（高波动回撤）
- 高波动资产：SOL 24h -2.90%（轻仓快进快出）
- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。

## 🌐 联网检索补充

- 关键词：2026-02-23 全球市场 盘面 复盘 原因, 2026-02-23 中国 宏观 经济 政策 市场 影响, 2026-02-23 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 下跌 原因, “上了高速发现全是聪明人” 事件 背景, 黄牛亏麻!T1遭让二追三淘汰 事件 背景, 完美收官！谷爱凌卫冕自由式滑雪U型场地金牌，李方慧夺银 事件 背景
- 命中结果：8 条（按发布时间倒序）

### 🔎 2026-02-23 中国 宏观 经济 政策 市场 影响

- [首席展望｜联博基金朱良：外资配置逻辑转向长期持有“优质盈利驱动型资产” - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTFA0M09zQ2JiS2Q5SlhYbmxtcDY2RUlXb1JNR1hGTGNwQjRnZEV6TUVJSlA2S09wM0xIS0UwYXdBUzM2NkF5NENwMzRYOEs4dElDVmZQVWxGYzc3R0JCS1dDZA?oc=5)
  - 来源: thepaper.cn | 时间: 2026-02-23 07:56
  - 摘要: 首席展望｜联博基金朱良：外资配置逻辑转向长期持有“优质盈利驱动型资产” thepaper.cn
- [最高法院阻止关税重击后，特朗普开辟新道路 - 新浪财经](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQLTFLQnBiTEJ3ek43WkxLc2RLNWhqbHByejhDcUdjRC1IX2xCVnhuVk5QRE5RNTN4R2g3aHhZNm9JbS1QMXAzSjdtOW5MeTd6cTJPQ3dmTFBLeUp1a29rdWJEUUxHVDJkY3RWZmZlak81bV85Nmo2TFl5R3kxcG54X1FWRGM5TnF3UHVsNTNROE9yVHRRT3k2dmJUSFZvb2NSLUpOTHd1aGU2S3d4b0ZyU3BRMktDdnNTT05IdUtuY1lHUTRyWWNCajdsZXpQWmtZUkE?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-23 04:27
  - 摘要: 最高法院阻止关税重击后，特朗普开辟新道路 新浪财经
- [[超话]#BET9是黄了吗 - 3DM](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SS2liS1NyY0p6Zkk1c3E0SGNLU3p5SndvSlBhMkdqLXFiN0JNZG9TMzVZbzVxcGJwQzhCSTdVX2pnY2VRODlZU2RoV0FLVUk?oc=5)
  - 来源: 3DM | 时间: 2026-02-23 02:22
  - 摘要: [超话]#BET9是黄了吗 3DM
- [靠谱的博彩平台推荐「🔄神经镜像版」 - 游侠网](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9rSndnV3ZaY3BoS0R3QmFFSHhuM3F2YjlBNzlIQUdnbzFGVUlYcjl3YnU3d1Q5akRBQzB0MzlMZUlKaU9sWnYyc2ZNaDhKbzFL?oc=5)
  - 来源: 游侠网 | 时间: 2026-02-22 20:22
  - 摘要: 靠谱的博彩平台推荐「🔄神经镜像版」 游侠网
- [下周重磅日程：英伟达财报、特朗普国情咨文、美伊博弈、德总理访华-yeeyi - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1sRDlWQ1EzUzFKTk1weXo3TmNaRFVOemZ2X0FNLTNTNl9PcjlfUHJ4cXp4Uk82U0dlaGRaVUpSZlMxU09tZEpyWXJvYlNHRmt5VU5YQVVB?oc=5)
  - 来源: yeeyi | 时间: 2026-02-22 12:05
  - 摘要: 下周重磅日程：英伟达财报、特朗普国情咨文、美伊博弈、德总理访华-yeeyi yeeyi

### 🔎 SOL 下跌 原因

- [2026年最值得投资的山寨币：APEMARS上涨，SOL和XRP下跌 - FinanceFeeds](https://news.google.com/rss/articles/CBMi_gFBVV95cUxQT2lFUlNlSmhfSkMtYS1TdU5UX1E5YmJ1REVoNzlfQ3RnWFNxZVR1cDFkNk1acWUzT0Y4bDFCS2N1SkNlN2JfRmh0Zy11WkZNWVZfUGljTG1tclM1dF9uSnY5Z05tbmtQTWFOX0FmT0s4bW5VZ3JsYklCQTZRQ05GSW1oUjJlMW5WM1c1WnhNOEhuMFA0ZjJzOURNY0RjSnVKNVlmc2NpaUdpRVk3ME9pbnVnUGoxR2ItNUpDU2tjLWhfTFptSHNHSFBZR2lTcFhBbk9IVTJiano2XzRDZXpnV0FjN0g5Sk5GdFBuUlRLOUZvSWpxVVlqTmFUaXpaQQ?oc=5)
  - 来源: FinanceFeeds | 时间: 2026-02-22 12:15
  - 摘要: 2026年最值得投资的山寨币：APEMARS上涨，SOL和XRP下跌 FinanceFeeds

### 🔎 VIX波动率指数 下跌 原因

- [第一热点 澳门新葡新京网站 - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTFBUdS1LYWlzcDVUQUIzUHR6S0dHSmtIY1FHandITld0NmtCVDBLdEVKNDZOclBhNHA5My16MUdfYXBFNGQ5LUFFUkpSWEZBV2tuZzA5V0xVYw?oc=5)
  - 来源: 3DM | 时间: 2026-02-22 09:48
  - 摘要: 第一热点 澳门新葡新京网站 3DM
- [美股创20年来首年最差纪录 - 万维读者网](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1WSDNxZ3dzeWFoNWZpMlk3T05wZ2RPbFZZSllnajdvWXU4T0pxWk13eW1pd2xDSkZNaEhSQXQ1cURwRl96YTBaZC1mMTA5ZnFmMVE?oc=5)
  - 来源: 万维读者网 | 时间: 2026-02-21 11:03
  - 摘要: 美股创20年来首年最差纪录 万维读者网

## 🔗 AI 分析引用来源

> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。

### Twitter (1 条)

- [¹] [2026-02-23T00:00 @KillaXBT | The$BTCcycles are evolving. Most people haven’t caught on yet. Each cycle, BTC is reachi...](https://twitter.com/KillaXBT/status/2025536229488390456)（匹配分=100，来源ID=TW13）

> 注：早报 AI 已按规则跳过 A 股盘面数据分析。


---

# 📋 原始数据

<a id="raw-market-data"></a>
## 📊 金融市场数据

### 🧭 股票总览

> 跟踪 **12** 个标的：上涨 **7** | 下跌 **5** | 平盘 **0** | 上涨占比 **58.3%**
> 区域强弱：韩股 +2.31% (1/1) | 欧股 +0.94% (3/3) | 美股 -0.73% (3/5) | 港股 -1.10% (0/1) | 日股 -1.12% (0/1) | A股 -1.26% (0/1)

> ⏸ A股休市

### 🌍 全球股票概览（Yahoo Finance）

| 区域 | 指标 | 最新价 | 涨跌幅 | 币种 |
|------|------|--------|--------|------|
| 美股 | [标普500](https://finance.yahoo.com/quote/%5EGSPC) | 6,909.51 | 🟢 +0.69% | USD |
| 美股 | [纳斯达克综合](https://finance.yahoo.com/quote/%5EIXIC) | 22,886.07 | 🟢 +0.90% | USD |
| 美股 | [道琼斯工业指数](https://finance.yahoo.com/quote/%5EDJI) | 49,625.97 | 🟢 +0.47% | USD |
| 美股 | [罗素2000](https://finance.yahoo.com/quote/%5ERUT) | 2,663.78 | 🔴 -0.05% | USD |
| 美股 | [VIX波动率指数](https://finance.yahoo.com/quote/%5EVIX) | 19.09 | 🔴 -5.64% | USD |
| 港股 | [恒生指数](https://finance.yahoo.com/quote/%5EHSI) | 26,413.35 | 🔴 -1.10% | HKD |
| 日股 | [日经225](https://finance.yahoo.com/quote/%5EN225) | 56,825.70 | 🔴 -1.12% | JPY |
| 韩股 | [韩国综合指数](https://finance.yahoo.com/quote/%5EKS11) | 5,808.53 | 🟢 +2.31% | KRW |
| 欧股 | [英国富时100](https://finance.yahoo.com/quote/%5EFTSE) | 10,686.90 | 🟢 +0.56% | GBP |
| 欧股 | [德国DAX](https://finance.yahoo.com/quote/%5EGDAXI) | 25,260.69 | 🟢 +0.87% | EUR |
| 欧股 | [法国CAC40](https://finance.yahoo.com/quote/%5EFCHI) | 8,515.49 | 🟢 +1.39% | EUR |
| A股 | [上证综指](https://finance.yahoo.com/quote/000001.SS) | 4,082.07 | 🔴 -1.26% | CNY |

> 概览：上涨 7 | 下跌 5 | 平盘 0 | 总计 12

### 🥇 贵金属

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|

### ₿ 加密货币

| 币种 | 价格 | 24h涨跌 |
|------|------|---------|
| BTC | $67,641.00 | 🔴 -0.50% |
| ETH | $1,957.43 | 🔴 -0.79% |
| SOL | $82.73 | 🔴 -2.90% |

### 📈 国际期货

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|
| WTI原油 | 65.88 | 🔴 -0.77% |
| 布伦特原油 | 70.74 | 🔴 -1.42% |
| 天然气 | 3.12 | 🟢 +2.23% |
| COMEX铜 | 5.89 | 🟢 +1.09% |

### 💻 GitHub 趋势

- ⭐ [**OpenPlanter**](https://github.com/ShinMegamiBoson/OpenPlanter) (1022 stars)
- ⭐ [**picolm**](https://github.com/RightNow-AI/picolm) (656 stars)
  - Run a 1-billion parameter LLM on a $10 board with 256MB RAM
- ⭐ [**Kalshi-Polymarket-Ai-bot**](https://github.com/CraftyGeezer/Kalshi-Polymarket-Ai-bot) (649 stars)
- ⭐ [**Polymarket-rsi-macd-index-trading-bot**](https://github.com/Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot) (601 stars)
  - Real-time polymarket trading bot that combines monitoring with strategy logic fo
- ⭐ [**taste-skill**](https://github.com/Leonxlnx/taste-skill) (550 stars)
  - Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from

## 🐦 Twitter 热点 (99 条)

- 来源统计: 关注账号 200 条 | 热门讨论 30 条

### 🔥 热门讨论推文

- `2026-02-23T00:00` @Mericamemed ❤️21901 🔁2240 💬132
  - Attention based economy. Thats why.
  - [原文链接](https://twitter.com/Mericamemed/status/2025480679710965820)
- `2026-02-23T00:00` @sycom_jp ❤️4148 🔁10490 💬836
  - 《サイトリニューアル記念キャンペーン》  🌈 初めてのゲーミングPCにもおすすめ 🌈 G-Master Velox III AMD Edition が当たる！  【応募方法】 ①@sycom_jpをフォロー ② この投稿をリポスト  【＋UPチャンス】 おすすめカスタム構成URLとタグを投稿👇 要リプで確認！  〆2/25 23:59｜当選DM
  - [原文链接](https://twitter.com/sycom_jp/status/2022243980751290495)
- `2026-02-23T00:00` @mefinho_ ❤️11384 🔁1611 💬41
  - C’est la video la plus réelle que j’ai vu mdrrr   Regardez !!!!
  - [原文链接](https://twitter.com/mefinho_/status/2025530673272885587)
- `2026-02-23T00:00` @unusual_whales ❤️8739 🔁1095 💬348
  - "The US economy experienced almost zero job growth in 2025," per NBC
  - [原文链接](https://twitter.com/unusual_whales/status/2025586627972939822)
- `2026-02-23T00:00` @bindass_ladki ❤️5875 🔁1568 💬184
  - This man has been Prime Minister for 12 years.   WORK : 0  VICTIM CARD : 24×7  People are fed up with all this now.
  - [原文链接](https://twitter.com/bindass_ladki/status/2025546268584673727)
- `2026-02-23T00:00` @NevesRodrigo_ ❤️5107 🔁19 💬37
  - 5km, em estrada de terra, uma moto de uns 130kg, com uma criança na garupa e um sol de rachar  E ele fez tudo isso sem reclamar por um único segundo  Aí eu tenho que vir aqui no Twitter ver uma vadia puta piranha vagabunda falar uma merda dessas
  - [原文链接](https://twitter.com/NevesRodrigo_/status/2025305132267622488)
- `2026-02-23T00:00` @xMarketNews ❤️3801 🔁861 💬139
  - SOUTH KOREA STOCK MARKET HAS SURGED NEARLY 150% SINCE THEY TOOK ACTION AGAINST NAKED SHORT SELLING🚨  - South Korea Suspended Short Selling to Probe Naked Shorting, Introduced Imprisonment and Heavy Fines…   LIKE 👍 IF YOU THINK DONALD TRUMP SHOULD DO THE SAME
  - [原文链接](https://twitter.com/xMarketNews/status/2025296878707913043)
- `2026-02-23T00:00` @Sosowski ❤️3601 🔁546 💬36
  - We’re 4 years into AI and the only people benefitting from AI are: 1. corporations selling AI  2. people actively turning computing and internet into shit
  - [原文链接](https://twitter.com/Sosowski/status/2025561904010158211)
- `2026-02-23T00:00` @mcafeenew ❤️1943 🔁1381 💬358
  - 🚨TREASON ALERT: AOC BOOTED FROM HOUSE INTEL COMMITTEE IN MASSIVE SCANDAL – CAUGHT RED-HANDED LEAKING TOP-SECRET ICE PLANS TO RADICAL MINNESOTA ACTIVISTS!  🔗t.me/+bWjXP07v90xlYWFkShe's SPILLING CLASSIFIED MAPS, UNDERCOVER AGENT NAMES, AND ANTIFA HIDEOUTS – Now Facing CRIMINAL CHARGES That Could LOCK HER UP FOR LIFE! Rep. Joseph Barron DROPS the HAMMER: "This is BEYOND a Breach – It BORDERS on TREASON!"  Is This DELUSIONAL TRAITOR Headed Straight to a 6x8 CELL? You WON'T BELIEVE How She's BETRAYIN
  - [原文链接](https://twitter.com/mcafeenew/status/2025675756953915446)
- `2026-02-23T00:00` @iamrollandex ❤️2252 🔁522 💬4
  - Chatgpt is good for writing   Claude is good for coding   Grok is good for researching   Gemini is good for study guide  Deepseek is good for brainstorming   Perplexity is  good for fact checking   Copilot is good for productivity in Microsoft tools
  - [原文链接](https://twitter.com/iamrollandex/status/2025300093562163569)
- `2026-02-23T00:00` @korimakorima ❤️1633 🔁331 💬11
  - 批判の嵐になったサム・アルトマンの発言（「人々はよく、AIを訓練するのにどれほど多くのエネルギーがかかるかを指摘するが、人間を訓練するのにだって莫大なエネルギーがかかるでしょう、賢くなるまでに20年かかるし、その間に食べるフードが必要でしょう、と語って「コイツ、人間の赤ん坊とAIを同列に扱っとるぞ！」と大反発された）をAIに擁護してもらったら「この発言はいただけませんね。アルトマン氏のロジックでは、人間が成人するまでの20年間は、知性を得るための「待機時間」や「コスト」に過ぎなくなってしまいますが、家族との食事、友人との葛藤、四季の移ろいを感じること――これらは“知性というアウトプット”のための燃料ではなく、それ自体が目的であり、価値なのです」と語りだして本末が転倒　AIが人間性を重んじろと人間を諭してる。
  - [原文链接](https://twitter.com/korimakorima/status/2025515099470143652)
- `2026-02-23T00:00` @pushpendrakum ❤️1066 🔁368 💬44
  - Imagine if just 25% of MPs spoke about real issues instead of caste math.  Toll scams. Hospital loot. Insurance fraud. Bank charges. Creator rights. Sim incoming call.  Crypto taxation system Stock market taxation  India would be unrecognizable. 🇮🇳🔥  Respect to@raghav_chadha
  - [原文链接](https://twitter.com/pushpendrakum/status/2025466732975194578)
- `2026-02-23T00:00` @KillaXBT ❤️1257 🔁95 💬86
  - The$BTCcycles are evolving.  Most people haven’t caught on yet.  Each cycle, BTC is reaching new ATHs faster after bottoming out. A few cycles from now, pullbacks will be shallow, and new ATHs could emerge every few months, much like Nasdaq/SPX.  Wall Street is in the building, they make the most money through euphoric stages, not during downtrends.
  - [原文链接](https://twitter.com/KillaXBT/status/2025536229488390456)
- `2026-02-23T00:00` @Clawmode ❤️561 🔁389 💬482
  - 🦞 What's coming for Claw Mode Today 🦞  - Trading Terminal  - Non-Fungible Agents (NFAs) — Season One starting Today@solana- NFAs are ownable AI trading agents minted as on-chain assets (1,000 per season).   Unlike standard NFTs, each NFA is a living, autonomous entity that trades, posts, and earns fees - forever tied to its minter's revenue stream.  More to be announced. Enter the Claw Mode 🦞  Native token launch on$SOLcoming tomorrow or day after.
  - [原文链接](https://twitter.com/Clawmode/status/2025217886617207050)
- `2026-02-23T00:00` @ninoboxer ❤️1060 🔁311 💬58
  - Just passing this along from one of my best friends from Mexico. It’s a voice text in broken English but good intel.  From Angel about Mexico, it’s voice text  OK, so it started today they killed El Mencho. I don’t know how much you know about him but anyways right now even Cancún and Meredith, where my mom lives. All the highways are closed. They’re preparing for major affiliation attack from the CNGj  Which stands for cartel nueva generación, Jalisco Extremely vicious so weeks before they star
  - [原文链接](https://twitter.com/ninoboxer/status/2025704347347411077)
- `2026-02-23T00:00` @CattardSlim ❤️993 🔁372 💬31
  - The Pedo hunter at Mar-A-Lago was a Christian Trump voter that was pissed about Trump's Epstein files cover-up & his crappy economy.  Austin Tucker Martin was another Tyler Robinson that felt let down by Trump.
  - [原文链接](https://twitter.com/CattardSlim/status/2025704315500056817)
- `2026-02-23T00:00` @iam_elias1 ❤️918 🔁137 💬46
  - 🚨BR€AKING: AI can now build you a business in 24 hours.  Here are 8 insane Claude prompts to turn any idea into income in 2026 👇 (Save for later)
  - [原文链接](https://twitter.com/iam_elias1/status/2025595101523956021)
- `2026-02-23T00:00` @Svyrydenko_Y ❤️663 🔁210 💬23
  - Yesterday, Russia deliberately targeted the Mondelez food production plant in Ukraine's Trostianets, Sumy Oblast, a facility that has operated continuously since the 1990s and was of the very first major foreign investments in Ukraine’s independent economy.  This enterprise began as a state-owned factory in 1978, once the largest chocolate producer in the former Soviet Union. It was later privatized by the American company Mondelez, which invested more than $250 million to modernize production, 
  - [原文链接](https://twitter.com/Svyrydenko_Y/status/2025491390537388314)
- `2026-02-23T00:00` @AAnon55 ❤️556 🔁177 💬33
  - Wondering what QAnon is?  QAnon is a label. It's Q & Anons. Q posted information on the Intel Board, & Anons are regular people.  Open this post & you will see 3 threads packed with Q information. 2 have videos & one has threads.
  - [原文链接](https://twitter.com/AAnon55/status/2025353814891429889)
- `2026-02-23T00:00` @SMQKEDQG ❤️603 🔁141 💬19
  - ‼️ BITCOIN EXCLUDED FROM BEING USED AS MONEY WITHIN THE SCOPE OF UCC LAW‼️  “Rather, it is excluding Bitcoin from being used as money within the scope of the UCC. This distinction is subtle, but it's more than mere semantics.”🙇‍♂️  Documented.📝👇
  - [原文链接](https://twitter.com/SMQKEDQG/status/2025357631389376795)

### @TheEconomist (10 条)

- `2026-02-23T00:00` The last time more people moved to the Midwest than left may have been in the 1950s. What explains the flip in domestic migration? https://www.economist.com/united-states/2026/02/21/the-midwests-remarkable-turnaround
  - [原文链接](https://twitter.com/TheEconomist/status/2025722302608884071)
- `2026-02-22T23:40` If, as many pundits expect, the Democrats win back control of the House of Representatives in November, the Capitol will become an energised place. The job could even seem to matter again https://www.economist.com/leaders/2026/02/19/how-to-improve-american-legislators-lot
  - [原文链接](https://twitter.com/TheEconomist/status/2025717248191529344)
- `2026-02-22T23:20` The government has accused protesters of a co-ordinated, premeditated ambush at an immigrant-detention facility in Texas. The Trump administration wants to extract as much political juice from the case as it can https://www.economist.com/united-states/2026/02/19/the-trump-administration-wants-to-put
  - [原文链接](https://twitter.com/TheEconomist/status/2025712214695366868)
- `2026-02-22T23:00` America has built up a huge military presence in the Middle East—the biggest overseas in decades. The president has a range of options if he decides to attack: http://econ.st/3MKfWYG  Photo: U.S. Navy/USS Abraham Lincoln
  - [原文链接](https://twitter.com/TheEconomist/status/2025707233120575657)
- `2026-02-22T22:45` Donald Trump has ordered strikes on Iran before. His next range of targets would almost certainly be far more expansive—and the consequences uncertain https://www.economist.com/middle-east-and-africa/2026/02/22/what-are-donald-trumps-strike-options-in-iran?taid=699b86f21693130001139e65&utm_campaign=
  - [原文链接](https://twitter.com/TheEconomist/status/2025703422301819076)
- *... 及其他 5 条*

### @zerohedge (10 条)

- `2026-02-22T23:55` Supreme Court Ruling On Tariffs Won't Change US–China Trade Relations, Analysts https://www.zerohedge.com/political/supreme-court-ruling-tariffs-wont-change-us-china-trade-relations-analysts
  - [原文链接](https://twitter.com/zerohedge/status/2025721044334457071)
- `2026-02-22T23:20` How Long Can Emerging Markets Continue To Rally? For Morgan Stanley, This Is The Key Factor https://www.zerohedge.com/markets/how-long-can-emerging-markets-continue-rally-according-morgan-stanley-key-factor
  - [原文链接](https://twitter.com/zerohedge/status/2025712235994140897)
- `2026-02-22T22:45` Tesla Avoids California Suspension By Dropping 'Self-Driving' Claims https://www.zerohedge.com/political/tesla-avoids-california-suspension-dropping-self-driving-claims
  - [原文链接](https://twitter.com/zerohedge/status/2025703427875991759)
- `2026-02-22T22:10` Trump Warns Netflix About Democrat Ties During Bid To Buy Warner Bros https://www.zerohedge.com/markets/trump-warns-netflix-about-democrat-ties-during-bid-buy-warner-bros
  - [原文链接](https://twitter.com/zerohedge/status/2025694618554171792)
- `2026-02-22T21:58` Mexican Resort Towns Burn As Special Forces Kill Jalisco New Generation Cartel Boss "El Mencho"  https://www.zerohedge.com/geopolitical/mexican-forces-kill-cjng-kingpin-sparks-cartel-chaos-across-guadalajara
  - [原文链接](https://twitter.com/zerohedge/status/2025691593836032420)
- *... 及其他 5 条*

### @WSJ (10 条)

- `2026-02-22T23:48` Schools of civic thought, which aim to foster open dialogue and disagreement between students, have themselves become a subject of campus debate https://on.wsj.com/4rWf2ag
  - [原文链接](https://twitter.com/WSJ/status/2025719301198496149)
- `2026-02-22T23:31` Here’s what the history of American board games says about national pride. Some of the games are a bit startling by today’s standards. https://on.wsj.com/3ZLo4uZ
  - [原文链接](https://twitter.com/WSJ/status/2025715061776421159)
- `2026-02-22T23:17` Gen Alpha has acquired a taste for shrimp tempura and salmon nigiri—and parents are paying a heavy price. 🍣 https://on.wsj.com/3OuGkX5
  - [原文链接](https://twitter.com/WSJ/status/2025711591124095227)
- `2026-02-22T23:00` President Trump’s decision to extend for a second time the deployment of the aircraft carrier USS Gerald R. Ford is taking a toll on the ship’s sailors and their families. 🔗: https://on.wsj.com/4kO7owp
  - [原文链接](https://twitter.com/WSJ/status/2025707376741933092)
- `2026-02-22T22:47` As adults age, they face increasing risks of falling or getting lost. http://localhost/juliejargon explores the tech that can help families keep tabs on older loved ones from afar while respecting their privacy. https://on.wsj.com/4cGI1dO
  - [原文链接](https://twitter.com/WSJ/status/2025704002281701712)
- *... 及其他 5 条*

### @ReutersWorld (10 条)

- `2026-02-22T23:40` UK to overhaul special-needs education as costs spiral http://reut.rs/4s5ksjx http://reut.rs/4s5ksjx
  - [原文链接](https://twitter.com/ReutersWorld/status/2025717265514017025)
- `2026-02-22T23:30` North Korea's ruling party re-elects Kim Jong Un general secretary for bolstering nuclear power http://reut.rs/4s93O2w http://reut.rs/4s93O2w
  - [原文链接](https://twitter.com/ReutersWorld/status/2025714858742751501)
- `2026-02-22T22:40` Iranian students protest for second day at some universities http://reut.rs/4rA36eP http://reut.rs/4rA36eP
  - [原文链接](https://twitter.com/ReutersWorld/status/2025702173745598603)
- `2026-02-22T21:40` Vehicles torched in Mexico's Jalisco following federal operation http://reut.rs/3OsH52Q http://reut.rs/3OsH52Q
  - [原文链接](https://twitter.com/ReutersWorld/status/2025687073458397412)
- `2026-02-22T21:30` Cop turned crime boss, Nemesio 'El Mencho' Oseguera leaves bloody legacy http://reut.rs/3Ot7DRv http://reut.rs/3Ot7DRv
  - [原文链接](https://twitter.com/ReutersWorld/status/2025684628950905332)
- *... 及其他 5 条*

### @DeItaone (10 条)

- `2026-02-22T23:28` TRUMP’S TARIFF GAMBLE FACES DOUBTS  Donald Trump has introduced new global tariffs, arguing the U.S. faces a serious balance-of-payments crisis. But many economists and markets see no such emergency, raising doubts about his justification.  The tariffs—set at 10% then raised to 15%—rely on a legal p
  - [原文链接](https://twitter.com/DeItaone/status/2025714299209953776)
- `2026-02-22T22:31` TRUMP MAY CONSIDER STRIKES ON IRAN  Donald Trump is reportedly considering limited airstrikes on Iran, according to the New York Times. Potential targets include the Revolutionary Guard, nuclear facilities, and missile programs. If these strikes fail to pressure Tehran, a broader effort to remove Al
  - [原文链接](https://twitter.com/DeItaone/status/2025699997606645960)
- `2026-02-22T21:36` *TRUMP OPEN TO DEPOSING AYATOLLAH BY FORCE IF IRAN STUBBORN: NYT
  - [原文链接](https://twitter.com/DeItaone/status/2025686147205140507)
- `2026-02-22T21:05` CARTEL KILLING TRIGGERS US ALERT IN MEXICO  The US Department of State urged Americans to shelter in place in parts of Mexico after cartel leader Nemesio Rubén Oseguera Cervantes was killed.  Violence and roadblocks spread across Jalisco and nearby states following the operation against the Jalisco 
  - [原文链接](https://twitter.com/DeItaone/status/2025678463168807418)
- `2026-02-22T16:08` LAGARDE: CONSUMERS DID NOT AVOID THE PAIN OF TARIFFS
  - [原文链接](https://twitter.com/DeItaone/status/2025603600915824698)
- *... 及其他 5 条*

### @swyx (4 条)

- `2026-02-22T22:37` just found out from http://localhost/nytimes that the man shortage in NYC is so bad that dating events are charging women $100 and men $0 and the attendance ratio is still 3:1  do u new york girls know how insane you sound right now to san franciscans, just… move?  pictures taken 5 mins apart right 
  - [原文链接](https://twitter.com/swyx/status/2025701553244700744)
- `2026-02-22T22:20` I don't think the IDE is dead, just evolving. The original "integrated dev environments" emerged to unify a set of dev tools (editor, compiler, debugger, etc) that were previously separate. Right now, a lot of the flagship tools that a traditional IDE offers are becoming less important thanks to AI 
  - [原文链接](https://twitter.com/swyx/status/2025697253210423765)
- `2026-02-22T16:51` dissenting opinion   https://nitter.net/yishan/status/2025057653739978782?s=46  Yishan (@yishan)  One underrecognized cause of this is that OpenAI has Facebook DNA.  Anthropic does not, and has academic DNA.  For all its mixed outcomes, Facebook culture produces people who know how to make products 
  - [原文链接](https://twitter.com/swyx/status/2025614529107746904)
- `2026-02-22T13:23` https://www.anuragk.com/blog/posts/Taalas.html
  - [原文链接](https://twitter.com/swyx/status/2025562167546613812)

### @PeterSchiff (5 条)

- `2026-02-22T22:19` https://finance.yahoo.com/news/trumps-trade-math-bold-confident-213018623.html
  - [原文链接](https://twitter.com/PeterSchiff/status/2025697082602819590)
- `2026-02-22T16:38` Trump claims that he can destroy the economy of any foreign country by putting an embargo on our imports. If Trump cuts off American consumers, there is an entire world of foreign consumers who would gladly buy what Americans can’t. It’s the U.S. economy that would be destroyed.
  - [原文链接](https://twitter.com/PeterSchiff/status/2025611181382152565)
- `2026-02-22T15:59` Large, growing, and persistent U.S. trade deficits are not the problem, but the unfortunate consequence of the problem. Because of bad monetary and fiscal policy under both political parties, Americans save too little and borrow too much, produce too little, and consume too much.
  - [原文链接](https://twitter.com/PeterSchiff/status/2025601413707866371)
- `2026-02-22T15:24` The Trump administration is threatening to use presidential authority to impose full embargoes that prevent Americans from buying any imported products from particular countries or from all countries. This would be even more harmful to Americans and the U.S. economy than tariffs.
  - [原文链接](https://twitter.com/PeterSchiff/status/2025592654734491841)
- `2026-02-22T12:53` Trump already hiked the 10% tariffs he imposed on all imported products Americans buy to the legal maximum 15%. But American consumers will only have to pay the higher taxes for 150 days. Any efforts to leave them in place longer without Congressional approval will be unlawful.
  - [原文链接](https://twitter.com/PeterSchiff/status/2025554616306356644)

### @SCMPNews (8 条)

- `2026-02-22T21:19` New York Mayor Mamdani orders citywide travel ban ahead of major US storm  https://www.scmp.com/news/world/united-states-canada/article/3344280/new-york-mayor-mamdani-orders-citywide-travel-ban-ahead-major-us-storm
  - [原文链接](https://twitter.com/SCMPNews/status/2025681904033296527)
- `2026-02-22T20:23` Mexican army kills leader of Jalisco New Generation Cartel, official says  https://www.scmp.com/news/world/americas/article/3344279/mexican-army-kills-leader-jalisco-new-generation-cartel-official-says
  - [原文链接](https://twitter.com/SCMPNews/status/2025667849197441295)
- `2026-02-22T19:12` France will summon US envoy Charles Kushner over comments on activist’s death  https://www.scmp.com/news/world/europe/article/3344278/france-will-summon-us-envoy-charles-kushner-over-comments-activists-death
  - [原文链接](https://twitter.com/SCMPNews/status/2025650011376099767)
- `2026-02-22T17:41` UK protection officers instructed to guard 2010 Epstein dinner party, reports say  https://www.scmp.com/news/world/europe/article/3344277/uk-protection-officers-instructed-guard-2010-epstein-dinner-party-reports-say
  - [原文链接](https://twitter.com/SCMPNews/status/2025627136195723631)
- `2026-02-22T15:14` Hong Kong eyes booking system, fees after campers overrun hotspots  https://www.scmp.com/news/hong-kong/society/article/3344274/hong-kong-eyes-booking-system-fees-after-campers-overrun-hotspots?module=top_story&pgtype=section
  - [原文链接](https://twitter.com/SCMPNews/status/2025590001942114492)
- *... 及其他 3 条*

### @VitalikButerin (1 条)

- `2026-02-22T19:24` How I think about "security":  The goal is to minimize the divergence between the user's intent, and the actual behavior of the system.  "User experience" can also be defined in this way. Thus, "user experience" and "security" are thus not separate fields. However, "security" focuses on tail risk si
  - [原文链接](https://twitter.com/VitalikButerin/status/2025653045414273438)

### @ylecun (1 条)

- `2026-02-22T19:09` This is a spectacularly important study.  Published in Nature, it provides solid evidence that this platform pushes those on the right further to the right, more pro-Trump, more pro-Russia,…  And that these effects are programmed into the platform  https://www.nature.com/articles/s41586-026-10098-2
  - [原文链接](https://twitter.com/ylecun/status/2025649075840745881)

## 📱 微信公众号

暂无数据

## 🔥 NewsNow 热榜 (120 条)

### 百度热搜

| 排名 | 标题 |
|------|------|
| #1 | [“上了高速发现全是聪明人”](https://www.baidu.com/s?wd=%E2%80%9C%E4%B8%8A%E4%BA%86%E9%AB%98%E9%80%9F%E5%8F%91%E7%8E%B0%E5%85%A8%E6%98%AF%E8%81%AA%E6%98%8E%E4%BA%BA%E2%80%9D) |
| #2 | [历史第一人！谷爱凌冬奥刷爆纪录](https://www.baidu.com/s?wd=%E5%8E%86%E5%8F%B2%E7%AC%AC%E4%B8%80%E4%BA%BA%EF%BC%81%E8%B0%B7%E7%88%B1%E5%87%8C%E5%86%AC%E5%A5%A5%E5%88%B7%E7%88%86%E7%BA%AA%E5%BD%95) |
| #3 | [假期返程天气、交通等服务指南来了](https://www.baidu.com/s?wd=%E5%81%87%E6%9C%9F%E8%BF%94%E7%A8%8B%E5%A4%A9%E6%B0%94%E3%80%81%E4%BA%A4%E9%80%9A%E7%AD%89%E6%9C%8D%E5%8A%A1%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86) |
| #4 | [开了12小时还要12小时：肉要臭了](https://www.baidu.com/s?wd=%E5%BC%80%E4%BA%8612%E5%B0%8F%E6%97%B6%E8%BF%98%E8%A6%8112%E5%B0%8F%E6%97%B6%EF%BC%9A%E8%82%89%E8%A6%81%E8%87%AD%E4%BA%86) |
| #5 | [6元塑料盆用了41年仍完好](https://www.baidu.com/s?wd=6%E5%85%83%E5%A1%91%E6%96%99%E7%9B%86%E7%94%A8%E4%BA%8641%E5%B9%B4%E4%BB%8D%E5%AE%8C%E5%A5%BD) |
| #6 | [全网关心的济南“出逃”鳌鱼找到了](https://www.baidu.com/s?wd=%E5%85%A8%E7%BD%91%E5%85%B3%E5%BF%83%E7%9A%84%E6%B5%8E%E5%8D%97%E2%80%9C%E5%87%BA%E9%80%83%E2%80%9D%E9%B3%8C%E9%B1%BC%E6%89%BE%E5%88%B0%E4%BA%86) |
| #7 | [苏翊鸣手持五星红旗亮相闭幕式](https://www.baidu.com/s?wd=%E8%8B%8F%E7%BF%8A%E9%B8%A3%E6%89%8B%E6%8C%81%E4%BA%94%E6%98%9F%E7%BA%A2%E6%97%97%E4%BA%AE%E7%9B%B8%E9%97%AD%E5%B9%95%E5%BC%8F) |
| #8 | [北京市委市政府发贺电](https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%A7%94%E5%B8%82%E6%94%BF%E5%BA%9C%E5%8F%91%E8%B4%BA%E7%94%B5) |
| #9 | [第一批返程的人已堵哭](https://www.baidu.com/s?wd=%E7%AC%AC%E4%B8%80%E6%89%B9%E8%BF%94%E7%A8%8B%E7%9A%84%E4%BA%BA%E5%B7%B2%E5%A0%B5%E5%93%AD) |
| #11 | [“江西丰城鞭炮炸死人”系编造](https://www.baidu.com/s?wd=%E2%80%9C%E6%B1%9F%E8%A5%BF%E4%B8%B0%E5%9F%8E%E9%9E%AD%E7%82%AE%E7%82%B8%E6%AD%BB%E4%BA%BA%E2%80%9D%E7%B3%BB%E7%BC%96%E9%80%A0) |

### 贴吧

| 排名 | 标题 |
|------|------|
| #1 | [黄牛亏麻!T1遭让二追三淘汰](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%BB%84%E7%89%9B%E4%BA%8F%E9%BA%BB%21T1%E9%81%AD%E8%AE%A9%E4%BA%8C%E8%BF%BD%E4%B8%89%E6%B7%98%E6%B1%B0&topic_id=28350863) |
| #2 | [滑雪GOAT!谷爱凌U池夺金](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%BB%91%E9%9B%AAGOAT%21%E8%B0%B7%E7%88%B1%E5%87%8CU%E6%B1%A0%E5%A4%BA%E9%87%91&topic_id=28350862) |
| #3 | [冬奥5金收官,吧友评含金量](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%86%AC%E5%A5%A55%E9%87%91%E6%94%B6%E5%AE%98%2C%E5%90%A7%E5%8F%8B%E8%AF%84%E5%90%AB%E9%87%91%E9%87%8F&topic_id=28350864) |
| #4 | [洗脚闹矛盾,男子跳桥失联](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B4%97%E8%84%9A%E9%97%B9%E7%9F%9B%E7%9B%BE%2C%E7%94%B7%E5%AD%90%E8%B7%B3%E6%A1%A5%E5%A4%B1%E8%81%94&topic_id=28350857) |
| #5 | [法外狂徒!罗翔帮黑老大减刑](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B3%95%E5%A4%96%E7%8B%82%E5%BE%92%21%E7%BD%97%E7%BF%94%E5%B8%AE%E9%BB%91%E8%80%81%E5%A4%A7%E5%87%8F%E5%88%91&topic_id=28350855) |
| #6 | [撞破妻子出轨,丈夫报警告性侵](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%92%9E%E7%A0%B4%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8%2C%E4%B8%88%E5%A4%AB%E6%8A%A5%E8%AD%A6%E5%91%8A%E6%80%A7%E4%BE%B5&topic_id=28350840) |
| #7 | [钓帝去世,钓鱼圈传奇落幕](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%92%93%E5%B8%9D%E5%8E%BB%E4%B8%96%2C%E9%92%93%E9%B1%BC%E5%9C%88%E4%BC%A0%E5%A5%87%E8%90%BD%E5%B9%95&topic_id=28350858) |
| #8 | [麦当劳作死,联动柜子学院](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%BA%A6%E5%BD%93%E5%8A%B3%E4%BD%9C%E6%AD%BB%2C%E8%81%94%E5%8A%A8%E6%9F%9C%E5%AD%90%E5%AD%A6%E9%99%A2&topic_id=28350849) |
| #9 | [小国作妖,春节译名之争再起](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%B0%8F%E5%9B%BD%E4%BD%9C%E5%A6%96%2C%E6%98%A5%E8%8A%82%E8%AF%91%E5%90%8D%E4%B9%8B%E4%BA%89%E5%86%8D%E8%B5%B7&topic_id=28350853) |
| #10 | [亲爹抛妻弃子,命丧俄乌战场](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E7%88%B9%E6%8A%9B%E5%A6%BB%E5%BC%83%E5%AD%90%2C%E5%91%BD%E4%B8%A7%E4%BF%84%E4%B9%8C%E6%88%98%E5%9C%BA&topic_id=28350847) |

### 澎湃新闻

| 排名 | 标题 |
|------|------|
| #1 | [完美收官！谷爱凌卫冕自由式滑雪U型场地金牌，李方慧夺银](https://www.thepaper.cn/newsDetail_forward_32642129) |
| #2 | [傅莹：在2026年慕安会现场感受国际秩序变化的律动](https://www.thepaper.cn/newsDetail_forward_32639268) |
| #3 | [新春走基层·见喜｜黄糕，在互联网火了的家乡美食](https://www.thepaper.cn/newsDetail_forward_32642312) |
| #4 | [春启新程｜春节里一家亮灯的“烟火小馆”，迎来不少来沪游客](https://www.thepaper.cn/newsDetail_forward_32639299) |
| #5 | [新春走基层·见喜｜重新学会跟长辈相处](https://www.thepaper.cn/newsDetail_forward_32639761) |
| #6 | [中东睿评｜美以与伊朗博弈的混沌状态只能靠战争才能打破吗？](https://www.thepaper.cn/newsDetail_forward_32639434) |
| #7 | [这个春节，上海何以成为热门目的地？](https://www.thepaper.cn/newsDetail_forward_32639992) |
| #8 | [持续放风试探，美官员称或对伊朗发动针对特定个人的军事打击](https://www.thepaper.cn/newsDetail_forward_32641921) |
| #9 | [阿根廷田野手记：关停的工厂、变贵的账单与华商的新生意｜907编辑部](https://www.thepaper.cn/newsDetail_forward_32638732) |
| #10 | [新春走基层丨崇湖湿地公园里的护鸟队员：春节轮班巡湖，鸟越来越多了](https://www.thepaper.cn/newsDetail_forward_32642202) |

### 知乎

| 排名 | 标题 |
|------|------|
| #1 | [米兰冬奥自由式滑雪女子 U 型场地技巧决赛，谷爱凌卫冕，李方慧摘银，如何评价他们的发挥？](https://www.zhihu.com/question/2008677675422672634) |
| #2 | [韩延哽咽恳求多给《星河入梦》有效排片，这部投资近四亿的电影为何面临排片困境？](https://www.zhihu.com/question/2008647492124827724) |
| #3 | [如何评价基努•里维斯的演技？](https://www.zhihu.com/question/21486639) |
| #4 | [在你的专业领域，大模型目前最难跨越的一道「门坎」是什么？](https://www.zhihu.com/question/2003062708547843506) |
| #5 | [索尼关停王牌工作室 Bluepoint 引外媒怒批，为何收购未久便解散？](https://www.zhihu.com/question/2008236854617584217) |
| #6 | [如何看待当所有国产大模型都在 2026 春节撒钱抢用户时，DeepSeek 却默不作声继续奋战？](https://www.zhihu.com/question/2004982651719812885) |
| #7 | [电视剧《大宅门》的四房妻妾中，白景琦为什么唯独不在乎漂亮温柔的槐花？](https://www.zhihu.com/question/1987742399) |
| #8 | [存款有 100 万时，你们内心会有什么感觉？](https://www.zhihu.com/question/604496678) |
| #9 | [现在玩 HiFi 的人，年轻人的比例为什么越来越少了？](https://www.zhihu.com/question/666161645) |
| #10 | [贵州非遗传承人半年卖 800 只「点翠蟑螂」，如何理解这种反差美学？若人人喊打的蟑螂变好看了，你能接受吗？](https://www.zhihu.com/question/2007528287103051494) |

### 财联社热门

| 排名 | 标题 |
|------|------|
| #1 | [特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405) |
| #2 | [中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111) |
| #3 | [什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326) |
| #4 | [春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289) |
| #5 | [美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233) |
| #6 | [特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246) |
| #7 | [春晚人形机器人“大秀肌肉”背后：A股新材料产业链多点突破 这些企业抢占赛道先机](https://www.cls.cn/detail/2292433) |
| #8 | [没有方向盘、没有脚踏板，特斯拉新车来了](https://www.cls.cn/detail/2292285) |
| #9 | [香港长江和记最新发声](https://www.cls.cn/detail/2292101) |
| #10 | [“内存荒”席卷全球，成AI竞赛关键瓶颈？又一硅谷大佬发声](https://www.cls.cn/detail/2292342) |

### 华尔街见闻

| 排名 | 标题 |
|------|------|
| #1 | [玉渊谭天：美国对华哪些关税被停止征收？](https://wallstreetcn.com/articles/3765953) |
| #2 | [特朗普新加征关税税率加码至15% 美政府“越权”关税引企业诉讼潮](https://wallstreetcn.com/articles/3765942) |
| #3 | [大摩评价MiniMax“全球顶尖基座模型稀缺资产”，高估值核心逻辑在于“技术决定天花板、全球化决定估值”](https://wallstreetcn.com/articles/3765947) |
| #4 | [春节期间，国内外都发生了什么？](https://wallstreetcn.com/articles/3765956) |
| #5 | [智谱发布GLM-5技术细节：工程级智能，适配国产算力](https://wallstreetcn.com/articles/3765961) |
| #6 | [欢迎来到AI智能体新时代：未来不是“为人创造”，而是“为AI服务”](https://wallstreetcn.com/articles/3765948) |
| #7 | [表面风光之下，OpenAI的“四大困境”](https://wallstreetcn.com/articles/3765945) |
| #8 | [地热——一场静悄悄的美国能源变革](https://wallstreetcn.com/articles/3765952) |
| #9 | [过去30年来未见之局面！美股指数波动之小创1960年来之最，而个股波动率却高达指数7倍](https://wallstreetcn.com/articles/3765941) |
| #10 | [SK会长崔泰源警告：AI正在吞噬一切，今年千亿美元利润或瞬间变巨亏](https://wallstreetcn.com/articles/3765949) |

### bilibili 热搜

| 排名 | 标题 |
|------|------|
| #1 | [​谷爱凌摘金](https://search.bilibili.com/all?keyword=%E2%80%8B%E8%B0%B7%E7%88%B1%E5%87%8C%E6%91%98%E9%87%91) |
| #2 | [DK战胜T1](https://search.bilibili.com/all?keyword=DK%E6%88%98%E8%83%9CT1) |
| #3 | [美在伊周边集结了多少兵力](https://search.bilibili.com/all?keyword=%E7%BE%8E%E5%9C%A8%E4%BC%8A%E5%91%A8%E8%BE%B9%E9%9B%86%E7%BB%93%E4%BA%86%E5%A4%9A%E5%B0%91%E5%85%B5%E5%8A%9B) |
| #4 | [Zywoo拿下第30个MVP](https://search.bilibili.com/all?keyword=Zywoo%E6%8B%BF%E4%B8%8B%E7%AC%AC30%E4%B8%AAMVP) |
| #5 | [李方慧斩获银牌](https://search.bilibili.com/all?keyword=%E6%9D%8E%E6%96%B9%E6%85%A7%E6%96%A9%E8%8E%B7%E9%93%B6%E7%89%8C) |
| #6 | [虹猫蓝兔七侠传4K修复版定档](https://search.bilibili.com/all?keyword=%E8%99%B9%E7%8C%AB%E8%93%9D%E5%85%94%E4%B8%83%E4%BE%A0%E4%BC%A04K%E4%BF%AE%E5%A4%8D%E7%89%88%E5%AE%9A%E6%A1%A3) |
| #7 | [DK战胜T1赛后数据](https://search.bilibili.com/all?keyword=DK%E6%88%98%E8%83%9CT1%E8%B5%9B%E5%90%8E%E6%95%B0%E6%8D%AE) |
| #8 | [中华野兽先生](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%8D%8E%E9%87%8E%E5%85%BD%E5%85%88%E7%94%9F) |
| #9 | [仙王5完结](https://search.bilibili.com/all?keyword=%E4%BB%99%E7%8E%8B5%E5%AE%8C%E7%BB%93) |
| #10 | [谷爱凌夺冠后得知外婆去世](https://search.bilibili.com/all?keyword=%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0%E5%90%8E%E5%BE%97%E7%9F%A5%E5%A4%96%E5%A9%86%E5%8E%BB%E4%B8%96) |

### 抖音

| 排名 | 标题 |
|------|------|
| #1 | [赫伊森就转发争议内容道歉](https://www.douyin.com/hot/2408951) |
| #2 | [米兰冬奥会闭幕式](https://www.douyin.com/hot/2408928) |
| #3 | [数说新春出游](https://www.douyin.com/hot/2408933) |
| #4 | [谷爱凌李方慧包揽U池金银牌](https://www.douyin.com/hot/2408149) |
| #5 | [中国代表团闭幕式入场](https://www.douyin.com/hot/2409026) |
| #6 | [返程高速堵成什么样了](https://www.douyin.com/hot/2408691) |
| #7 | [即使万般不舍 依然也要往前走](https://www.douyin.com/hot/2408221) |
| #8 | [当美妆达人回村后](https://www.douyin.com/hot/2408098) |
| #9 | [行李箱一装又该返程了](https://www.douyin.com/hot/2408932) |
| #10 | [金正恩当选朝鲜劳动党总书记](https://www.douyin.com/hot/2409034) |

### 微博

| 排名 | 标题 |
|------|------|
| #1 | [半夜出发的大聪明全堵在高速上了](https://s.weibo.com/weibo?q=%23%E5%8D%8A%E5%A4%9C%E5%87%BA%E5%8F%91%E7%9A%84%E5%A4%A7%E8%81%AA%E6%98%8E%E5%85%A8%E5%A0%B5%E5%9C%A8%E9%AB%98%E9%80%9F%E4%B8%8A%E4%BA%86%23) |
| #2 | [意大利把闭幕式办成文旅宣传片](https://s.weibo.com/weibo?q=%23%E6%84%8F%E5%A4%A7%E5%88%A9%E6%8A%8A%E9%97%AD%E5%B9%95%E5%BC%8F%E5%8A%9E%E6%88%90%E6%96%87%E6%97%85%E5%AE%A3%E4%BC%A0%E7%89%87%23) |
| #3 | [返程前的告别看泪目了](https://s.weibo.com/weibo?q=%23%E8%BF%94%E7%A8%8B%E5%89%8D%E7%9A%84%E5%91%8A%E5%88%AB%E7%9C%8B%E6%B3%AA%E7%9B%AE%E4%BA%86%23) |
| #4 | [苏翊鸣手持五星红旗入场](https://s.weibo.com/weibo?q=%23%E8%8B%8F%E7%BF%8A%E9%B8%A3%E6%89%8B%E6%8C%81%E4%BA%94%E6%98%9F%E7%BA%A2%E6%97%97%E5%85%A5%E5%9C%BA%23) |
| #5 | [镖人连续4天票房逆跌](https://s.weibo.com/weibo?q=%23%E9%95%96%E4%BA%BA%E8%BF%9E%E7%BB%AD4%E5%A4%A9%E7%A5%A8%E6%88%BF%E9%80%86%E8%B7%8C%23) |
| #6 | [本届冬奥会最佳镜头](https://s.weibo.com/weibo?q=%E6%9C%AC%E5%B1%8A%E5%86%AC%E5%A5%A5%E4%BC%9A%E6%9C%80%E4%BD%B3%E9%95%9C%E5%A4%B4) |
| #7 | [女子动车厕所冲走50g金手链](https://s.weibo.com/weibo?q=%23%E5%A5%B3%E5%AD%90%E5%8A%A8%E8%BD%A6%E5%8E%95%E6%89%80%E5%86%B2%E8%B5%B050g%E9%87%91%E6%89%8B%E9%93%BE%23) |
| #8 | [米兰冬奥会圣火熄灭](https://s.weibo.com/weibo?q=%23%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E4%BC%9A%E5%9C%A3%E7%81%AB%E7%86%84%E7%81%AD%23) |
| #10 | [一觉醒来米兰冬奥闭幕了](https://s.weibo.com/weibo?q=%23%E4%B8%80%E8%A7%89%E9%86%92%E6%9D%A5%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E9%97%AD%E5%B9%95%E4%BA%86%23) |
| #11 | [谷爱凌夺冠后得知奶奶去世](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0%E5%90%8E%E5%BE%97%E7%9F%A5%E5%A5%B6%E5%A5%B6%E5%8E%BB%E4%B8%96%23) |

### 今日头条

| 排名 | 标题 |
|------|------|
| #1 | [“亚洲最大收费站”出口全开迎返程潮](https://www.toutiao.com/trending/7609797963648516139/) |
| #2 | [中国队5金4银6铜收官](https://www.toutiao.com/trending/7609123113803989035/) |
| #3 | [曝伊朗革命卫队已接管黎巴嫩真主党](https://www.toutiao.com/trending/7608787946786996230/) |
| #4 | [女子跟男友回老家看到木棍梯子惊呆](https://www.toutiao.com/trending/7609150132161642502/) |
| #5 | [谷爱凌：冬奥是用百米速度跑马拉松](https://www.toutiao.com/trending/7609673478799753243/) |
| #6 | [远嫁姐姐回家 47岁弟弟激动得像孩子](https://www.toutiao.com/trending/7608507947525849114/) |
| #7 | [旗手苏翊鸣亮相冬奥会闭幕式](https://www.toutiao.com/trending/7609783177858698803/) |
| #8 | [谷爱凌夺金央视女解说情绪激动哽咽](https://www.toutiao.com/trending/7609825166226640430/) |
| #9 | [你如何看“成为中国人”海外爆火](https://www.toutiao.com/trending/7609309353933504554/) |
| #10 | [媒体：中国冰雪新起点](https://www.toutiao.com/trending/7608945521272815652/) |

### 凤凰网

| 排名 | 标题 |
|------|------|
| #1 | [美最高法裁决后，对华IEEPA关税应自动取消](https://news.ifeng.com/c/8qxg9KwWwcj) |
| #2 | [美国前商务部长：其他关税方案，都会削弱特朗普对华谈判筹码](https://news.ifeng.com/c/8qxAuTEgS6q) |
| #3 | [欧盟、英国、加拿大、墨西哥、德国，最新发声](https://news.ifeng.com/c/8qwaojRoDGX) |
| #4 | [美州长向特朗普发账单，要求退回87亿美元关税](https://news.ifeng.com/c/8qxUeFL6TqS) |
| #5 | [日方批特朗普再加征关税：混乱环境或致日企撤离美国](https://news.ifeng.com/c/8qxI3ju2UuK) |
| #6 | [一顿中餐掀翻秘鲁政坛，美国在背后做了什么？](https://news.ifeng.com/c/8qxLW2rbfUZ) |
| #7 | [韩美军方发生分歧，军演发布会被推迟](https://news.ifeng.com/c/8qxXk0OCONw) |
| #8 | [乌克兰制裁俄罗斯“影子舰队”](https://news.ifeng.com/c/8qwipyWWgXr) |
| #9 | [“有用的白痴王子”，又被利用了](https://news.ifeng.com/c/8qxQebeiSVb) |
| #10 | [男子试图闯入海湖庄园被击毙，疑似携带霰弹枪和燃油罐](https://news.ifeng.com/c/8qxbeT9MHp0) |

## 🔗 原始链接索引

### 🐦 Twitter 原文 (80/99 条)

- [2026-02-23T00:00 @Mericamemed [热门] | Attention based economy. Thats why.](https://twitter.com/Mericamemed/status/2025480679710965820)
- [2026-02-23T00:00 @sycom_jp [热门] | 《サイトリニューアル記念キャンペーン》 🌈 初めてのゲーミングPCにもおすすめ 🌈 G-Master Velox III AMD Edition が当たる！ 【応募方法】 ①@sy...](https://twitter.com/sycom_jp/status/2022243980751290495)
- [2026-02-23T00:00 @mefinho_ [热门] | C’est la video la plus réelle que j’ai vu mdrrr Regardez !!!!](https://twitter.com/mefinho_/status/2025530673272885587)
- [2026-02-23T00:00 @unusual_whales [热门] | "The US economy experienced almost zero job growth in 2025," per NBC](https://twitter.com/unusual_whales/status/2025586627972939822)
- [2026-02-23T00:00 @bindass_ladki [热门] | This man has been Prime Minister for 12 years. WORK : 0 VICTIM CARD : 24×7 People are fed ...](https://twitter.com/bindass_ladki/status/2025546268584673727)
- [2026-02-23T00:00 @NevesRodrigo_ [热门] | 5km, em estrada de terra, uma moto de uns 130kg, com uma criança na garupa e um sol de rac...](https://twitter.com/NevesRodrigo_/status/2025305132267622488)
- [2026-02-23T00:00 @xMarketNews [热门] | SOUTH KOREA STOCK MARKET HAS SURGED NEARLY 150% SINCE THEY TOOK ACTION AGAINST NAKED SHORT...](https://twitter.com/xMarketNews/status/2025296878707913043)
- [2026-02-23T00:00 @Sosowski [热门] | We’re 4 years into AI and the only people benefitting from AI are: 1. corporations selling...](https://twitter.com/Sosowski/status/2025561904010158211)
- [2026-02-23T00:00 @mcafeenew [热门] | 🚨TREASON ALERT: AOC BOOTED FROM HOUSE INTEL COMMITTEE IN MASSIVE SCANDAL – CAUGHT RED-HAND...](https://twitter.com/mcafeenew/status/2025675756953915446)
- [2026-02-23T00:00 @iamrollandex [热门] | Chatgpt is good for writing Claude is good for coding Grok is good for researching Gemini ...](https://twitter.com/iamrollandex/status/2025300093562163569)
- [2026-02-23T00:00 @korimakorima [热门] | 批判の嵐になったサム・アルトマンの発言（「人々はよく、AIを訓練するのにどれほど多くのエネルギーがかかるかを指摘するが、人間を訓練するのにだって莫大なエネルギーがかかるでしょう、賢...](https://twitter.com/korimakorima/status/2025515099470143652)
- [2026-02-23T00:00 @pushpendrakum [热门] | Imagine if just 25% of MPs spoke about real issues instead of caste math. Toll scams. Hosp...](https://twitter.com/pushpendrakum/status/2025466732975194578)
- [2026-02-23T00:00 @KillaXBT [热门] | The$BTCcycles are evolving. Most people haven’t caught on yet. Each cycle, BTC is reaching...](https://twitter.com/KillaXBT/status/2025536229488390456)
- [2026-02-23T00:00 @Clawmode [热门] | 🦞 What's coming for Claw Mode Today 🦞 - Trading Terminal - Non-Fungible Agents (NFAs) — Se...](https://twitter.com/Clawmode/status/2025217886617207050)
- [2026-02-23T00:00 @ninoboxer [热门] | Just passing this along from one of my best friends from Mexico. It’s a voice text in brok...](https://twitter.com/ninoboxer/status/2025704347347411077)
- [2026-02-23T00:00 @CattardSlim [热门] | The Pedo hunter at Mar-A-Lago was a Christian Trump voter that was pissed about Trump's Ep...](https://twitter.com/CattardSlim/status/2025704315500056817)
- [2026-02-23T00:00 @iam_elias1 [热门] | 🚨BR€AKING: AI can now build you a business in 24 hours. Here are 8 insane Claude prompts t...](https://twitter.com/iam_elias1/status/2025595101523956021)
- [2026-02-23T00:00 @Svyrydenko_Y [热门] | Yesterday, Russia deliberately targeted the Mondelez food production plant in Ukraine's Tr...](https://twitter.com/Svyrydenko_Y/status/2025491390537388314)
- [2026-02-23T00:00 @AAnon55 [热门] | Wondering what QAnon is? QAnon is a label. It's Q & Anons. Q posted information on the Int...](https://twitter.com/AAnon55/status/2025353814891429889)
- [2026-02-23T00:00 @SMQKEDQG [热门] | ‼️ BITCOIN EXCLUDED FROM BEING USED AS MONEY WITHIN THE SCOPE OF UCC LAW‼️ “Rather, it is ...](https://twitter.com/SMQKEDQG/status/2025357631389376795)
- [2026-02-23T00:00 @iAmjadKhann [热门] | ہمارے ریسٹورنٹ کے سامنے سیف سٹی کیمرے ہیں لیکن پولیس کا کہنا ہے کہ یہ ایک مہینہ پہلے انسٹا...](https://twitter.com/iAmjadKhann/status/2025669607722291476)
- [2026-02-23T00:00 @KobeissiLetter [热门] | BREAKING: US stock market futures open lower in their initial reaction to President Trump ...](https://twitter.com/KobeissiLetter/status/2025717706368987399)
- [2026-02-23T00:00 @ChristineDrazan [热门] | Oregon's leaders are driving our economy into a ditch. Here in Salem, Democrats just passe...](https://twitter.com/ChristineDrazan/status/2025290183680327750)
- [2026-02-23T00:00 @simonmaginn [热门] | A country that issues its own currency can no more run out of the currency it issues than ...](https://twitter.com/simonmaginn/status/2025539989765783595)
- [2026-02-23T00:00 @liliamcamargo2 [热门] | RT@arc_maiana: Olha ai quem também fez o L junto com painho: Cold Play.](https://twitter.com/liliamcamargo2/status/2025722420435304830)
- [2026-02-23T00:00 @danieljits_web3 [热门] | ETH fees? They're being funneled into NVIDIA & TESLA now.$ONDOis making tokenized stocks a...](https://twitter.com/danieljits_web3/status/2025722078155116766)
- [2026-02-23T00:00 @Gemini [热门] | “You still doing that bitcoin thing?” Me:](https://twitter.com/Gemini/status/2025693189814747233)
- [2026-02-23T00:00 @venussdreams [热门] | tgc stans were so well fed today](https://twitter.com/venussdreams/status/2025621235686633607)
- [2026-02-23T00:00 @iontecs_pemf [热门] | The absolute filth at Blackrock already knew what was in the Epstein Files, didn't they? S...](https://twitter.com/iontecs_pemf/status/2018396892405886995)
- [2026-02-23T00:00 @CleanAirMoms [热门] | ❤️ ❤️ ❤️ The New Brunswick, New Jersey City Council voted Wednesday to cancel plans to con...](https://twitter.com/CleanAirMoms/status/2025425169586499837)
- [2026-02-23T00:00 @TheEconomist [关注] | The last time more people moved to the Midwest than left may have been in the 1950s. What ...](https://twitter.com/TheEconomist/status/2025722302608884071)
- [2026-02-22T23:55 @zerohedge [关注] | Supreme Court Ruling On Tariffs Won't Change US–China Trade Relations, Analysts https://ww...](https://twitter.com/zerohedge/status/2025721044334457071)
- [2026-02-22T23:48 @WSJ [关注] | Schools of civic thought, which aim to foster open dialogue and disagreement between stude...](https://twitter.com/WSJ/status/2025719301198496149)
- [2026-02-22T23:40 @ReutersWorld [关注] | UK to overhaul special-needs education as costs spiral http://reut.rs/4s5ksjx http://reut....](https://twitter.com/ReutersWorld/status/2025717265514017025)
- [2026-02-22T23:40 @TheEconomist [关注] | If, as many pundits expect, the Democrats win back control of the House of Representatives...](https://twitter.com/TheEconomist/status/2025717248191529344)
- [2026-02-22T23:31 @WSJ [关注] | Here’s what the history of American board games says about national pride. Some of the gam...](https://twitter.com/WSJ/status/2025715061776421159)
- [2026-02-22T23:30 @ReutersWorld [关注] | North Korea's ruling party re-elects Kim Jong Un general secretary for bolstering nuclear ...](https://twitter.com/ReutersWorld/status/2025714858742751501)
- [2026-02-22T23:28 @DeItaone [关注] | TRUMP’S TARIFF GAMBLE FACES DOUBTS Donald Trump has introduced new global tariffs, arguing...](https://twitter.com/DeItaone/status/2025714299209953776)
- [2026-02-22T23:20 @zerohedge [关注] | How Long Can Emerging Markets Continue To Rally? For Morgan Stanley, This Is The Key Facto...](https://twitter.com/zerohedge/status/2025712235994140897)
- [2026-02-22T23:20 @TheEconomist [关注] | The government has accused protesters of a co-ordinated, premeditated ambush at an immigra...](https://twitter.com/TheEconomist/status/2025712214695366868)
- [2026-02-22T23:17 @WSJ [关注] | Gen Alpha has acquired a taste for shrimp tempura and salmon nigiri—and parents are paying...](https://twitter.com/WSJ/status/2025711591124095227)
- [2026-02-22T23:00 @WSJ [关注] | President Trump’s decision to extend for a second time the deployment of the aircraft carr...](https://twitter.com/WSJ/status/2025707376741933092)
- [2026-02-22T23:00 @TheEconomist [关注] | America has built up a huge military presence in the Middle East—the biggest overseas in d...](https://twitter.com/TheEconomist/status/2025707233120575657)
- [2026-02-22T22:47 @WSJ [关注] | As adults age, they face increasing risks of falling or getting lost. http://localhost/jul...](https://twitter.com/WSJ/status/2025704002281701712)
- [2026-02-22T22:45 @zerohedge [关注] | Tesla Avoids California Suspension By Dropping 'Self-Driving' Claims https://www.zerohedge...](https://twitter.com/zerohedge/status/2025703427875991759)
- [2026-02-22T22:45 @TheEconomist [关注] | Donald Trump has ordered strikes on Iran before. His next range of targets would almost ce...](https://twitter.com/TheEconomist/status/2025703422301819076)
- [2026-02-22T22:40 @ReutersWorld [关注] | Iranian students protest for second day at some universities http://reut.rs/4rA36eP http:/...](https://twitter.com/ReutersWorld/status/2025702173745598603)
- [2026-02-22T22:40 @TheEconomist [关注] | Few issues unite Elizabeth Warren and Donald Trump, but a distaste for private equity seem...](https://twitter.com/TheEconomist/status/2025702148516819072)
- [2026-02-22T22:37 @swyx [关注] | just found out from http://localhost/nytimes that the man shortage in NYC is so bad that d...](https://twitter.com/swyx/status/2025701553244700744)
- [2026-02-22T22:33 @WSJ [关注] | Are we forever destined to pay more cloud rent to Google, Apple and others? Columnist http...](https://twitter.com/WSJ/status/2025700578345492983)
- [2026-02-22T22:31 @DeItaone [关注] | TRUMP MAY CONSIDER STRIKES ON IRAN Donald Trump is reportedly considering limited airstrik...](https://twitter.com/DeItaone/status/2025699997606645960)
- [2026-02-22T22:23 @WSJ [关注] | Virginia’s Loudoun County is a giant data-center market thanks in part to a radio DJ-turne...](https://twitter.com/WSJ/status/2025697998722732435)
- [2026-02-22T22:20 @swyx [关注] | I don't think the IDE is dead, just evolving. The original "integrated dev environments" e...](https://twitter.com/swyx/status/2025697253210423765)
- [2026-02-22T22:20 @TheEconomist [关注] | On “Checks and Balance” this week, the crummiest job in Washington: 🎧Why so many lawmakers...](https://twitter.com/TheEconomist/status/2025697114978726361)
- [2026-02-22T22:19 @PeterSchiff [关注] | https://finance.yahoo.com/news/trumps-trade-math-bold-confident-213018623.html](https://twitter.com/PeterSchiff/status/2025697082602819590)
- [2026-02-22T22:10 @WSJ [关注] | Lloyd Blankfein discusses his upcoming memoir, surviving office setbacks and the advice he...](https://twitter.com/WSJ/status/2025694632013660649)
- [2026-02-22T22:10 @zerohedge [关注] | Trump Warns Netflix About Democrat Ties During Bid To Buy Warner Bros https://www.zerohedg...](https://twitter.com/zerohedge/status/2025694618554171792)
- [2026-02-22T22:00 @TheEconomist [关注] | Amid Republicans’ debate over America’s commitment to Israel, ancient tropes are resurfaci...](https://twitter.com/TheEconomist/status/2025692124960682405)
- [2026-02-22T21:58 @zerohedge [关注] | Mexican Resort Towns Burn As Special Forces Kill Jalisco New Generation Cartel Boss "El Me...](https://twitter.com/zerohedge/status/2025691593836032420)
- [2026-02-22T21:53 @WSJ [关注] | President Trump said he would direct the defense secretary and relevant departments to beg...](https://twitter.com/WSJ/status/2025690459545252123)
- [2026-02-22T21:51 @zerohedge [关注] | So Jeffrey Epstein in 2010 - 2 years after his arrest for procuring a child prostitute - d...](https://twitter.com/zerohedge/status/2025689976206229779)
- [2026-02-22T21:40 @ReutersWorld [关注] | Vehicles torched in Mexico's Jalisco following federal operation http://reut.rs/3OsH52Q ht...](https://twitter.com/ReutersWorld/status/2025687073458397412)
- [2026-02-22T21:40 @TheEconomist [关注] | India is emerging as an important player on the geopolitical stage. Stay up to date with o...](https://twitter.com/TheEconomist/status/2025687049555026131)
- [2026-02-22T21:39 @zerohedge [关注] | Full Analysis Of The Supreme Court IEEPA Decision: How It Impacts The Economy, Policy And ...](https://twitter.com/zerohedge/status/2025686812811821236)
- [2026-02-22T21:37 @WSJ [关注] | Michael Selig is helping Americans bet on everything from the Fed’s interest rate decision...](https://twitter.com/WSJ/status/2025686414482972711)
- [2026-02-22T21:36 @DeItaone [关注] | *TRUMP OPEN TO DEPOSING AYATOLLAH BY FORCE IF IRAN STUBBORN: NYT](https://twitter.com/DeItaone/status/2025686147205140507)
- [2026-02-22T21:30 @ReutersWorld [关注] | Cop turned crime boss, Nemesio 'El Mencho' Oseguera leaves bloody legacy http://reut.rs/3O...](https://twitter.com/ReutersWorld/status/2025684628950905332)
- [2026-02-22T21:20 @TheEconomist [关注] | Well Informed: your evidence based guide to health and wellness, delivered straight to you...](https://twitter.com/TheEconomist/status/2025682016742609395)
- [2026-02-22T21:19 @SCMPNews [关注] | New York Mayor Mamdani orders citywide travel ban ahead of major US storm https://www.scmp...](https://twitter.com/SCMPNews/status/2025681904033296527)
- [2026-02-22T21:05 @DeItaone [关注] | CARTEL KILLING TRIGGERS US ALERT IN MEXICO The US Department of State urged Americans to s...](https://twitter.com/DeItaone/status/2025678463168807418)
- [2026-02-22T20:40 @ReutersWorld [关注] | Hundreds protest in Verona ahead of Games closing ceremony http://reut.rs/4aFfl3P http://r...](https://twitter.com/ReutersWorld/status/2025671975385874621)
- [2026-02-22T20:23 @SCMPNews [关注] | Mexican army kills leader of Jalisco New Generation Cartel, official says https://www.scmp...](https://twitter.com/SCMPNews/status/2025667849197441295)
- [2026-02-22T19:30 @ReutersWorld [关注] | Air Canada, United Airlines halt flights to Mexico's Puerto Vallarta http://reut.rs/4rDvQn...](https://twitter.com/ReutersWorld/status/2025654440804381092)
- [2026-02-22T19:28 @zerohedge [关注] | Rubio realizing he’s going to have to be the new leader of the Jalisco New Generation Cart...](https://twitter.com/zerohedge/status/2025653899856855210)
- [2026-02-22T19:24 @VitalikButerin [关注] | How I think about "security": The goal is to minimize the divergence between the user's in...](https://twitter.com/VitalikButerin/status/2025653045414273438)
- [2026-02-22T19:12 @SCMPNews [关注] | France will summon US envoy Charles Kushner over comments on activist’s death https://www....](https://twitter.com/SCMPNews/status/2025650011376099767)
- [2026-02-22T19:09 @ylecun [关注] | This is a spectacularly important study. Published in Nature, it provides solid evidence t...](https://twitter.com/ylecun/status/2025649075840745881)
- [2026-02-22T18:57 @zerohedge [关注] | 1% sells .....NVDA still a massive consensus long among analysts. https://www.zerohedge.co...](https://twitter.com/zerohedge/status/2025646117883416876)
- [2026-02-22T18:40 @ReutersWorld [关注] | Mexican drug lord "El Mencho" killed in military operation, says government source http://...](https://twitter.com/ReutersWorld/status/2025641777382752536)
- [2026-02-22T18:30 @ReutersWorld [关注] | Iranian students protest for second day at some universities http://reut.rs/4s8C4es http:/...](https://twitter.com/ReutersWorld/status/2025639345210700260)

### 📱 微信公众号原文 (0/0 条)

- 暂无可用链接

### 🔥 NewsNow 原文 (120/120 条)

- [百度热搜 #1 | “上了高速发现全是聪明人”](https://www.baidu.com/s?wd=%E2%80%9C%E4%B8%8A%E4%BA%86%E9%AB%98%E9%80%9F%E5%8F%91%E7%8E%B0%E5%85%A8%E6%98%AF%E8%81%AA%E6%98%8E%E4%BA%BA%E2%80%9D)
- [贴吧 #1 | 黄牛亏麻!T1遭让二追三淘汰](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%BB%84%E7%89%9B%E4%BA%8F%E9%BA%BB%21T1%E9%81%AD%E8%AE%A9%E4%BA%8C%E8%BF%BD%E4%B8%89%E6%B7%98%E6%B1%B0&topic_id=28350863)
- [澎湃新闻 #1 | 完美收官！谷爱凌卫冕自由式滑雪U型场地金牌，李方慧夺银](https://www.thepaper.cn/newsDetail_forward_32642129)
- [知乎 #1 | 米兰冬奥自由式滑雪女子 U 型场地技巧决赛，谷爱凌卫冕，李方慧摘银，如何评价他们的发挥？](https://www.zhihu.com/question/2008677675422672634)
- [财联社热门 #1 | 特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405)
- [华尔街见闻 #1 | 玉渊谭天：美国对华哪些关税被停止征收？](https://wallstreetcn.com/articles/3765953)
- [bilibili 热搜 #1 | ​谷爱凌摘金](https://search.bilibili.com/all?keyword=%E2%80%8B%E8%B0%B7%E7%88%B1%E5%87%8C%E6%91%98%E9%87%91)
- [抖音 #1 | 赫伊森就转发争议内容道歉](https://www.douyin.com/hot/2408951)
- [微博 #1 | 半夜出发的大聪明全堵在高速上了](https://s.weibo.com/weibo?q=%23%E5%8D%8A%E5%A4%9C%E5%87%BA%E5%8F%91%E7%9A%84%E5%A4%A7%E8%81%AA%E6%98%8E%E5%85%A8%E5%A0%B5%E5%9C%A8%E9%AB%98%E9%80%9F%E4%B8%8A%E4%BA%86%23)
- [今日头条 #1 | “亚洲最大收费站”出口全开迎返程潮](https://www.toutiao.com/trending/7609797963648516139/)
- [凤凰网 #1 | 美最高法裁决后，对华IEEPA关税应自动取消](https://news.ifeng.com/c/8qxg9KwWwcj)
- [今日头条 #2 | 中国队5金4银6铜收官](https://www.toutiao.com/trending/7609123113803989035/)
- [华尔街见闻 #2 | 特朗普新加征关税税率加码至15% 美政府“越权”关税引企业诉讼潮](https://wallstreetcn.com/articles/3765942)
- [贴吧 #2 | 滑雪GOAT!谷爱凌U池夺金](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%BB%91%E9%9B%AAGOAT%21%E8%B0%B7%E7%88%B1%E5%87%8CU%E6%B1%A0%E5%A4%BA%E9%87%91&topic_id=28350862)
- [百度热搜 #2 | 历史第一人！谷爱凌冬奥刷爆纪录](https://www.baidu.com/s?wd=%E5%8E%86%E5%8F%B2%E7%AC%AC%E4%B8%80%E4%BA%BA%EF%BC%81%E8%B0%B7%E7%88%B1%E5%87%8C%E5%86%AC%E5%A5%A5%E5%88%B7%E7%88%86%E7%BA%AA%E5%BD%95)
- [凤凰网 #2 | 美国前商务部长：其他关税方案，都会削弱特朗普对华谈判筹码](https://news.ifeng.com/c/8qxAuTEgS6q)
- [知乎 #2 | 韩延哽咽恳求多给《星河入梦》有效排片，这部投资近四亿的电影为何面临排片困境？](https://www.zhihu.com/question/2008647492124827724)
- [财联社热门 #2 | 中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111)
- [bilibili 热搜 #2 | DK战胜T1](https://search.bilibili.com/all?keyword=DK%E6%88%98%E8%83%9CT1)
- [澎湃新闻 #2 | 傅莹：在2026年慕安会现场感受国际秩序变化的律动](https://www.thepaper.cn/newsDetail_forward_32639268)
- [微博 #2 | 意大利把闭幕式办成文旅宣传片](https://s.weibo.com/weibo?q=%23%E6%84%8F%E5%A4%A7%E5%88%A9%E6%8A%8A%E9%97%AD%E5%B9%95%E5%BC%8F%E5%8A%9E%E6%88%90%E6%96%87%E6%97%85%E5%AE%A3%E4%BC%A0%E7%89%87%23)
- [抖音 #2 | 米兰冬奥会闭幕式](https://www.douyin.com/hot/2408928)
- [今日头条 #3 | 曝伊朗革命卫队已接管黎巴嫩真主党](https://www.toutiao.com/trending/7608787946786996230/)
- [百度热搜 #3 | 假期返程天气、交通等服务指南来了](https://www.baidu.com/s?wd=%E5%81%87%E6%9C%9F%E8%BF%94%E7%A8%8B%E5%A4%A9%E6%B0%94%E3%80%81%E4%BA%A4%E9%80%9A%E7%AD%89%E6%9C%8D%E5%8A%A1%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86)
- [抖音 #3 | 数说新春出游](https://www.douyin.com/hot/2408933)
- [华尔街见闻 #3 | 大摩评价MiniMax“全球顶尖基座模型稀缺资产”，高估值核心逻辑在于“技术决定天花板、全球化决定估值”](https://wallstreetcn.com/articles/3765947)
- [凤凰网 #3 | 欧盟、英国、加拿大、墨西哥、德国，最新发声](https://news.ifeng.com/c/8qwaojRoDGX)
- [财联社热门 #3 | 什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326)
- [bilibili 热搜 #3 | 美在伊周边集结了多少兵力](https://search.bilibili.com/all?keyword=%E7%BE%8E%E5%9C%A8%E4%BC%8A%E5%91%A8%E8%BE%B9%E9%9B%86%E7%BB%93%E4%BA%86%E5%A4%9A%E5%B0%91%E5%85%B5%E5%8A%9B)
- [知乎 #3 | 如何评价基努•里维斯的演技？](https://www.zhihu.com/question/21486639)
- [微博 #3 | 返程前的告别看泪目了](https://s.weibo.com/weibo?q=%23%E8%BF%94%E7%A8%8B%E5%89%8D%E7%9A%84%E5%91%8A%E5%88%AB%E7%9C%8B%E6%B3%AA%E7%9B%AE%E4%BA%86%23)
- [贴吧 #3 | 冬奥5金收官,吧友评含金量](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%86%AC%E5%A5%A55%E9%87%91%E6%94%B6%E5%AE%98%2C%E5%90%A7%E5%8F%8B%E8%AF%84%E5%90%AB%E9%87%91%E9%87%8F&topic_id=28350864)
- [澎湃新闻 #3 | 新春走基层·见喜｜黄糕，在互联网火了的家乡美食](https://www.thepaper.cn/newsDetail_forward_32642312)
- [抖音 #4 | 谷爱凌李方慧包揽U池金银牌](https://www.douyin.com/hot/2408149)
- [澎湃新闻 #4 | 春启新程｜春节里一家亮灯的“烟火小馆”，迎来不少来沪游客](https://www.thepaper.cn/newsDetail_forward_32639299)
- [贴吧 #4 | 洗脚闹矛盾,男子跳桥失联](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B4%97%E8%84%9A%E9%97%B9%E7%9F%9B%E7%9B%BE%2C%E7%94%B7%E5%AD%90%E8%B7%B3%E6%A1%A5%E5%A4%B1%E8%81%94&topic_id=28350857)
- [凤凰网 #4 | 美州长向特朗普发账单，要求退回87亿美元关税](https://news.ifeng.com/c/8qxUeFL6TqS)
- [百度热搜 #4 | 开了12小时还要12小时：肉要臭了](https://www.baidu.com/s?wd=%E5%BC%80%E4%BA%8612%E5%B0%8F%E6%97%B6%E8%BF%98%E8%A6%8112%E5%B0%8F%E6%97%B6%EF%BC%9A%E8%82%89%E8%A6%81%E8%87%AD%E4%BA%86)
- [华尔街见闻 #4 | 春节期间，国内外都发生了什么？](https://wallstreetcn.com/articles/3765956)
- [财联社热门 #4 | 春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289)
- [今日头条 #4 | 女子跟男友回老家看到木棍梯子惊呆](https://www.toutiao.com/trending/7609150132161642502/)
- [知乎 #4 | 在你的专业领域，大模型目前最难跨越的一道「门坎」是什么？](https://www.zhihu.com/question/2003062708547843506)
- [微博 #4 | 苏翊鸣手持五星红旗入场](https://s.weibo.com/weibo?q=%23%E8%8B%8F%E7%BF%8A%E9%B8%A3%E6%89%8B%E6%8C%81%E4%BA%94%E6%98%9F%E7%BA%A2%E6%97%97%E5%85%A5%E5%9C%BA%23)
- [bilibili 热搜 #4 | Zywoo拿下第30个MVP](https://search.bilibili.com/all?keyword=Zywoo%E6%8B%BF%E4%B8%8B%E7%AC%AC30%E4%B8%AAMVP)
- [澎湃新闻 #5 | 新春走基层·见喜｜重新学会跟长辈相处](https://www.thepaper.cn/newsDetail_forward_32639761)
- [贴吧 #5 | 法外狂徒!罗翔帮黑老大减刑](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B3%95%E5%A4%96%E7%8B%82%E5%BE%92%21%E7%BD%97%E7%BF%94%E5%B8%AE%E9%BB%91%E8%80%81%E5%A4%A7%E5%87%8F%E5%88%91&topic_id=28350855)
- [百度热搜 #5 | 6元塑料盆用了41年仍完好](https://www.baidu.com/s?wd=6%E5%85%83%E5%A1%91%E6%96%99%E7%9B%86%E7%94%A8%E4%BA%8641%E5%B9%B4%E4%BB%8D%E5%AE%8C%E5%A5%BD)
- [凤凰网 #5 | 日方批特朗普再加征关税：混乱环境或致日企撤离美国](https://news.ifeng.com/c/8qxI3ju2UuK)
- [财联社热门 #5 | 美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233)
- [华尔街见闻 #5 | 智谱发布GLM-5技术细节：工程级智能，适配国产算力](https://wallstreetcn.com/articles/3765961)
- [bilibili 热搜 #5 | 李方慧斩获银牌](https://search.bilibili.com/all?keyword=%E6%9D%8E%E6%96%B9%E6%85%A7%E6%96%A9%E8%8E%B7%E9%93%B6%E7%89%8C)
- [今日头条 #5 | 谷爱凌：冬奥是用百米速度跑马拉松](https://www.toutiao.com/trending/7609673478799753243/)
- [知乎 #5 | 索尼关停王牌工作室 Bluepoint 引外媒怒批，为何收购未久便解散？](https://www.zhihu.com/question/2008236854617584217)
- [抖音 #5 | 中国代表团闭幕式入场](https://www.douyin.com/hot/2409026)
- [微博 #5 | 镖人连续4天票房逆跌](https://s.weibo.com/weibo?q=%23%E9%95%96%E4%BA%BA%E8%BF%9E%E7%BB%AD4%E5%A4%A9%E7%A5%A8%E6%88%BF%E9%80%86%E8%B7%8C%23)
- [bilibili 热搜 #6 | 虹猫蓝兔七侠传4K修复版定档](https://search.bilibili.com/all?keyword=%E8%99%B9%E7%8C%AB%E8%93%9D%E5%85%94%E4%B8%83%E4%BE%A0%E4%BC%A04K%E4%BF%AE%E5%A4%8D%E7%89%88%E5%AE%9A%E6%A1%A3)
- [知乎 #6 | 如何看待当所有国产大模型都在 2026 春节撒钱抢用户时，DeepSeek 却默不作声继续奋战？](https://www.zhihu.com/question/2004982651719812885)
- [抖音 #6 | 返程高速堵成什么样了](https://www.douyin.com/hot/2408691)
- [澎湃新闻 #6 | 中东睿评｜美以与伊朗博弈的混沌状态只能靠战争才能打破吗？](https://www.thepaper.cn/newsDetail_forward_32639434)
- [华尔街见闻 #6 | 欢迎来到AI智能体新时代：未来不是“为人创造”，而是“为AI服务”](https://wallstreetcn.com/articles/3765948)
- [贴吧 #6 | 撞破妻子出轨,丈夫报警告性侵](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%92%9E%E7%A0%B4%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8%2C%E4%B8%88%E5%A4%AB%E6%8A%A5%E8%AD%A6%E5%91%8A%E6%80%A7%E4%BE%B5&topic_id=28350840)
- [凤凰网 #6 | 一顿中餐掀翻秘鲁政坛，美国在背后做了什么？](https://news.ifeng.com/c/8qxLW2rbfUZ)
- [财联社热门 #6 | 特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246)
- [今日头条 #6 | 远嫁姐姐回家 47岁弟弟激动得像孩子](https://www.toutiao.com/trending/7608507947525849114/)
- [微博 #6 | 本届冬奥会最佳镜头](https://s.weibo.com/weibo?q=%E6%9C%AC%E5%B1%8A%E5%86%AC%E5%A5%A5%E4%BC%9A%E6%9C%80%E4%BD%B3%E9%95%9C%E5%A4%B4)
- [百度热搜 #6 | 全网关心的济南“出逃”鳌鱼找到了](https://www.baidu.com/s?wd=%E5%85%A8%E7%BD%91%E5%85%B3%E5%BF%83%E7%9A%84%E6%B5%8E%E5%8D%97%E2%80%9C%E5%87%BA%E9%80%83%E2%80%9D%E9%B3%8C%E9%B1%BC%E6%89%BE%E5%88%B0%E4%BA%86)
- [bilibili 热搜 #7 | DK战胜T1赛后数据](https://search.bilibili.com/all?keyword=DK%E6%88%98%E8%83%9CT1%E8%B5%9B%E5%90%8E%E6%95%B0%E6%8D%AE)
- [澎湃新闻 #7 | 这个春节，上海何以成为热门目的地？](https://www.thepaper.cn/newsDetail_forward_32639992)
- [抖音 #7 | 即使万般不舍 依然也要往前走](https://www.douyin.com/hot/2408221)
- [贴吧 #7 | 钓帝去世,钓鱼圈传奇落幕](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%92%93%E5%B8%9D%E5%8E%BB%E4%B8%96%2C%E9%92%93%E9%B1%BC%E5%9C%88%E4%BC%A0%E5%A5%87%E8%90%BD%E5%B9%95&topic_id=28350858)
- [华尔街见闻 #7 | 表面风光之下，OpenAI的“四大困境”](https://wallstreetcn.com/articles/3765945)
- [凤凰网 #7 | 韩美军方发生分歧，军演发布会被推迟](https://news.ifeng.com/c/8qxXk0OCONw)
- [财联社热门 #7 | 春晚人形机器人“大秀肌肉”背后：A股新材料产业链多点突破 这些企业抢占赛道先机](https://www.cls.cn/detail/2292433)
- [知乎 #7 | 电视剧《大宅门》的四房妻妾中，白景琦为什么唯独不在乎漂亮温柔的槐花？](https://www.zhihu.com/question/1987742399)
- [微博 #7 | 女子动车厕所冲走50g金手链](https://s.weibo.com/weibo?q=%23%E5%A5%B3%E5%AD%90%E5%8A%A8%E8%BD%A6%E5%8E%95%E6%89%80%E5%86%B2%E8%B5%B050g%E9%87%91%E6%89%8B%E9%93%BE%23)
- [百度热搜 #7 | 苏翊鸣手持五星红旗亮相闭幕式](https://www.baidu.com/s?wd=%E8%8B%8F%E7%BF%8A%E9%B8%A3%E6%89%8B%E6%8C%81%E4%BA%94%E6%98%9F%E7%BA%A2%E6%97%97%E4%BA%AE%E7%9B%B8%E9%97%AD%E5%B9%95%E5%BC%8F)
- [今日头条 #7 | 旗手苏翊鸣亮相冬奥会闭幕式](https://www.toutiao.com/trending/7609783177858698803/)
- [bilibili 热搜 #8 | 中华野兽先生](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%8D%8E%E9%87%8E%E5%85%BD%E5%85%88%E7%94%9F)
- [抖音 #8 | 当美妆达人回村后](https://www.douyin.com/hot/2408098)
- [澎湃新闻 #8 | 持续放风试探，美官员称或对伊朗发动针对特定个人的军事打击](https://www.thepaper.cn/newsDetail_forward_32641921)
- [贴吧 #8 | 麦当劳作死,联动柜子学院](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%BA%A6%E5%BD%93%E5%8A%B3%E4%BD%9C%E6%AD%BB%2C%E8%81%94%E5%8A%A8%E6%9F%9C%E5%AD%90%E5%AD%A6%E9%99%A2&topic_id=28350849)
- [财联社热门 #8 | 没有方向盘、没有脚踏板，特斯拉新车来了](https://www.cls.cn/detail/2292285)
- [凤凰网 #8 | 乌克兰制裁俄罗斯“影子舰队”](https://news.ifeng.com/c/8qwipyWWgXr)
- [华尔街见闻 #8 | 地热——一场静悄悄的美国能源变革](https://wallstreetcn.com/articles/3765952)
- [百度热搜 #8 | 北京市委市政府发贺电](https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%A7%94%E5%B8%82%E6%94%BF%E5%BA%9C%E5%8F%91%E8%B4%BA%E7%94%B5)
- [今日头条 #8 | 谷爱凌夺金央视女解说情绪激动哽咽](https://www.toutiao.com/trending/7609825166226640430/)
- [微博 #8 | 米兰冬奥会圣火熄灭](https://s.weibo.com/weibo?q=%23%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E4%BC%9A%E5%9C%A3%E7%81%AB%E7%86%84%E7%81%AD%23)
- [知乎 #8 | 存款有 100 万时，你们内心会有什么感觉？](https://www.zhihu.com/question/604496678)
- [百度热搜 #9 | 第一批返程的人已堵哭](https://www.baidu.com/s?wd=%E7%AC%AC%E4%B8%80%E6%89%B9%E8%BF%94%E7%A8%8B%E7%9A%84%E4%BA%BA%E5%B7%B2%E5%A0%B5%E5%93%AD)
- [澎湃新闻 #9 | 阿根廷田野手记：关停的工厂、变贵的账单与华商的新生意｜907编辑部](https://www.thepaper.cn/newsDetail_forward_32638732)
- [华尔街见闻 #9 | 过去30年来未见之局面！美股指数波动之小创1960年来之最，而个股波动率却高达指数7倍](https://wallstreetcn.com/articles/3765941)
- [抖音 #9 | 行李箱一装又该返程了](https://www.douyin.com/hot/2408932)
- [贴吧 #9 | 小国作妖,春节译名之争再起](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%B0%8F%E5%9B%BD%E4%BD%9C%E5%A6%96%2C%E6%98%A5%E8%8A%82%E8%AF%91%E5%90%8D%E4%B9%8B%E4%BA%89%E5%86%8D%E8%B5%B7&topic_id=28350853)
- [凤凰网 #9 | “有用的白痴王子”，又被利用了](https://news.ifeng.com/c/8qxQebeiSVb)
- [今日头条 #9 | 你如何看“成为中国人”海外爆火](https://www.toutiao.com/trending/7609309353933504554/)
- [财联社热门 #9 | 香港长江和记最新发声](https://www.cls.cn/detail/2292101)
- [知乎 #9 | 现在玩 HiFi 的人，年轻人的比例为什么越来越少了？](https://www.zhihu.com/question/666161645)
- [bilibili 热搜 #9 | 仙王5完结](https://search.bilibili.com/all?keyword=%E4%BB%99%E7%8E%8B5%E5%AE%8C%E7%BB%93)
- [bilibili 热搜 #10 | 谷爱凌夺冠后得知外婆去世](https://search.bilibili.com/all?keyword=%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0%E5%90%8E%E5%BE%97%E7%9F%A5%E5%A4%96%E5%A9%86%E5%8E%BB%E4%B8%96)
- [知乎 #10 | 贵州非遗传承人半年卖 800 只「点翠蟑螂」，如何理解这种反差美学？若人人喊打的蟑螂变好看了，你能接受吗？](https://www.zhihu.com/question/2007528287103051494)
- [澎湃新闻 #10 | 新春走基层丨崇湖湿地公园里的护鸟队员：春节轮班巡湖，鸟越来越多了](https://www.thepaper.cn/newsDetail_forward_32642202)
- [贴吧 #10 | 亲爹抛妻弃子,命丧俄乌战场](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E7%88%B9%E6%8A%9B%E5%A6%BB%E5%BC%83%E5%AD%90%2C%E5%91%BD%E4%B8%A7%E4%BF%84%E4%B9%8C%E6%88%98%E5%9C%BA&topic_id=28350847)
- [凤凰网 #10 | 男子试图闯入海湖庄园被击毙，疑似携带霰弹枪和燃油罐](https://news.ifeng.com/c/8qxbeT9MHp0)
- [华尔街见闻 #10 | SK会长崔泰源警告：AI正在吞噬一切，今年千亿美元利润或瞬间变巨亏](https://wallstreetcn.com/articles/3765949)
- [财联社热门 #10 | “内存荒”席卷全球，成AI竞赛关键瓶颈？又一硅谷大佬发声](https://www.cls.cn/detail/2292342)
- [抖音 #10 | 金正恩当选朝鲜劳动党总书记](https://www.douyin.com/hot/2409034)
- [今日头条 #10 | 媒体：中国冰雪新起点](https://www.toutiao.com/trending/7608945521272815652/)
- [微博 #10 | 一觉醒来米兰冬奥闭幕了](https://s.weibo.com/weibo?q=%23%E4%B8%80%E8%A7%89%E9%86%92%E6%9D%A5%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E9%97%AD%E5%B9%95%E4%BA%86%23)
- [抖音 #11 | 节后必带回北上广的老家特产](https://www.douyin.com/hot/2408554)
- [今日头条 #11 | 谷爱凌U池卫冕！中国队包揽金银](https://www.toutiao.com/trending/7609098288788176937/)
- [贴吧 #11 | 飞碟社官宣,原神动画稳了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%A3%9E%E7%A2%9F%E7%A4%BE%E5%AE%98%E5%AE%A3%2C%E5%8E%9F%E7%A5%9E%E5%8A%A8%E7%94%BB%E7%A8%B3%E4%BA%86&topic_id=28350851)
- [百度热搜 #11 | “江西丰城鞭炮炸死人”系编造](https://www.baidu.com/s?wd=%E2%80%9C%E6%B1%9F%E8%A5%BF%E4%B8%B0%E5%9F%8E%E9%9E%AD%E7%82%AE%E7%82%B8%E6%AD%BB%E4%BA%BA%E2%80%9D%E7%B3%BB%E7%BC%96%E9%80%A0)
- [凤凰网 #11 | 破开冰面潜水打捞，俄寻回所有坠湖溺亡的中国游客遗体](https://news.ifeng.com/c/8qxA3o3RFZg)
- [财联社热门 #11 | 环球下周看点：关税风暴叠加美伊博弈 英伟达能否再救AI牛市？](https://www.cls.cn/detail/2292422)
- [bilibili 热搜 #11 | 史蒂夫速通狗熊岭](https://search.bilibili.com/all?keyword=%E5%8F%B2%E8%92%82%E5%A4%AB%E9%80%9F%E9%80%9A%E7%8B%97%E7%86%8A%E5%B2%AD)
- [澎湃新闻 #11 | 谷爱凌发布会落泪：刚得知外婆去世，我向她保证过会勇敢](https://www.thepaper.cn/newsDetail_forward_32643518)
- [知乎 #11 | 科学家晚年经验丰富，为啥产出反而更少呢？](https://www.zhihu.com/question/58631980)
- [微博 #11 | 谷爱凌夺冠后得知奶奶去世](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0%E5%90%8E%E5%BE%97%E7%9F%A5%E5%A5%B6%E5%A5%B6%E5%8E%BB%E4%B8%96%23)
- [贴吧 #12 | 喂猫起争执,男子遭恶邻杀害](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%96%82%E7%8C%AB%E8%B5%B7%E4%BA%89%E6%89%A7%2C%E7%94%B7%E5%AD%90%E9%81%AD%E6%81%B6%E9%82%BB%E6%9D%80%E5%AE%B3&topic_id=28350838)
- [抖音 #12 | 所谓“超能量子水”是智商税](https://www.douyin.com/hot/2408948)

### 💻 GitHub 原文 (20/39 条)

- [openclaw/openclaw | ⭐ 218570 | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/openclaw/openclaw)
- [Significant-Gravitas/AutoGPT | ⭐ 181935 | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission i...](https://github.com/Significant-Gravitas/AutoGPT)
- [n8n-io/n8n | ⭐ 175835 | Fair-code workflow automation platform with native AI capabilities. Combine visual buildin...](https://github.com/n8n-io/n8n)
- [ollama/ollama | ⭐ 163150 | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and othe...](https://github.com/ollama/ollama)
- [huggingface/transformers | ⭐ 156827 | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning model...](https://github.com/huggingface/transformers)
- [f/prompts.chat | ⭐ 146661 | a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. F...](https://github.com/f/prompts.chat)
- [langflow-ai/langflow | ⭐ 144969 | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.](https://github.com/langflow-ai/langflow)
- [langgenius/dify | ⭐ 130007 | Production-ready platform for agentic workflow development.](https://github.com/langgenius/dify)
- [langchain-ai/langchain | ⭐ 127172 | 🦜🔗 The platform for reliable agents.](https://github.com/langchain-ai/langchain)
- [SimplifyJobs/New-Grad-Positions | ⭐ 16321 | A collection of full time roles in SWE, Quant, and PM for new grads.](https://github.com/SimplifyJobs/New-Grad-Positions)
- [tensorflow/tensorflow | ⭐ 193886 | An Open Source Machine Learning Framework for Everyone](https://github.com/tensorflow/tensorflow)
- [Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot | ⭐ 601 | Real-time polymarket trading bot that combines monitoring with strategy logic for Polymark...](https://github.com/Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot)
- [ebrasha/free-v2ray-public-list | ⭐ 524 | A simple and always-updated list of free, working V2Ray servers. including SS, SSR, Trojan...](https://github.com/ebrasha/free-v2ray-public-list)
- [MetaMask/eth-phishing-detect | ⭐ 1259 | Utility for detecting phishing domains targeting Web3 users](https://github.com/MetaMask/eth-phishing-detect)
- [piotrnar/gocoin | ⭐ 1002 | Full bitcoin solution written in Go (golang)](https://github.com/piotrnar/gocoin)
- [RightNow-AI/picolm | ⭐ 656 | Run a 1-billion parameter LLM on a $10 board with 256MB RAM](https://github.com/RightNow-AI/picolm)
- [phishdestroy/destroylist | ⭐ 915 | Real-time blocklist of crypto phishing, scam, and drainer domains. Auto-updated threat int...](https://github.com/phishdestroy/destroylist)
- [CraftyGeezer/Kalshi-Polymarket-Ai-bot | ⭐ 649](https://github.com/CraftyGeezer/Kalshi-Polymarket-Ai-bot)
- [Leonxlnx/taste-skill | ⭐ 550 | Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generatin...](https://github.com/Leonxlnx/taste-skill)
- [TraderAlice/OpenAlice | ⭐ 391 | File-driven AI trading agent engine for crypto and securities markets](https://github.com/TraderAlice/OpenAlice)

### 🌍 Yahoo Finance 原文 (12/12 条)

- [美股 | 标普500 (^GSPC) | +0.69%](https://finance.yahoo.com/quote/%5EGSPC)
- [美股 | 纳斯达克综合 (^IXIC) | +0.90%](https://finance.yahoo.com/quote/%5EIXIC)
- [美股 | 道琼斯工业指数 (^DJI) | +0.47%](https://finance.yahoo.com/quote/%5EDJI)
- [美股 | 罗素2000 (^RUT) | -0.05%](https://finance.yahoo.com/quote/%5ERUT)
- [美股 | VIX波动率指数 (^VIX) | -5.64%](https://finance.yahoo.com/quote/%5EVIX)
- [港股 | 恒生指数 (^HSI) | -1.10%](https://finance.yahoo.com/quote/%5EHSI)
- [日股 | 日经225 (^N225) | -1.12%](https://finance.yahoo.com/quote/%5EN225)
- [韩股 | 韩国综合指数 (^KS11) | +2.31%](https://finance.yahoo.com/quote/%5EKS11)
- [欧股 | 英国富时100 (^FTSE) | +0.56%](https://finance.yahoo.com/quote/%5EFTSE)
- [欧股 | 德国DAX (^GDAXI) | +0.87%](https://finance.yahoo.com/quote/%5EGDAXI)
- [欧股 | 法国CAC40 (^FCHI) | +1.39%](https://finance.yahoo.com/quote/%5EFCHI)
- [A股 | 上证综指 (000001.SS) | -1.26%](https://finance.yahoo.com/quote/000001.SS)

### 🌐 联网检索原文 (8/8 条)

- [2026-02-23 07:56 thepaper.cn | 首席展望｜联博基金朱良：外资配置逻辑转向长期持有“优质盈利驱动型资产” - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTFA0M09zQ2JiS2Q5SlhYbmxtcDY2RUlXb1JNR1hGTGNwQjRnZEV6TUVJSlA2S09wM0xIS0UwYXdBUzM2NkF5NENwMzRYOEs4dElDVmZQVWxGYzc3R0JCS1dDZA?oc=5)
- [2026-02-23 04:27 新浪财经 | 最高法院阻止关税重击后，特朗普开辟新道路 - 新浪财经](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQLTFLQnBiTEJ3ek43WkxLc2RLNWhqbHByejhDcUdjRC1IX2xCVnhuVk5QRE5RNTN4R2g3aHhZNm9JbS1QMXAzSjdtOW5MeTd6cTJPQ3dmTFBLeUp1a29rdWJEUUxHVDJkY3RWZmZlak81bV85Nmo2TFl5R3kxcG54X1FWRGM5TnF3UHVsNTNROE9yVHRRT3k2dmJUSFZvb2NSLUpOTHd1aGU2S3d4b0ZyU3BRMktDdnNTT05IdUtuY1lHUTRyWWNCajdsZXpQWmtZUkE?oc=5)
- [2026-02-23 02:22 3DM | [超话]#BET9是黄了吗 - 3DM](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SS2liS1NyY0p6Zkk1c3E0SGNLU3p5SndvSlBhMkdqLXFiN0JNZG9TMzVZbzVxcGJwQzhCSTdVX2pnY2VRODlZU2RoV0FLVUk?oc=5)
- [2026-02-22 20:22 游侠网 | 靠谱的博彩平台推荐「🔄神经镜像版」 - 游侠网](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9rSndnV3ZaY3BoS0R3QmFFSHhuM3F2YjlBNzlIQUdnbzFGVUlYcjl3YnU3d1Q5akRBQzB0MzlMZUlKaU9sWnYyc2ZNaDhKbzFL?oc=5)
- [2026-02-22 12:15 FinanceFeeds | 2026年最值得投资的山寨币：APEMARS上涨，SOL和XRP下跌 - FinanceFeeds](https://news.google.com/rss/articles/CBMi_gFBVV95cUxQT2lFUlNlSmhfSkMtYS1TdU5UX1E5YmJ1REVoNzlfQ3RnWFNxZVR1cDFkNk1acWUzT0Y4bDFCS2N1SkNlN2JfRmh0Zy11WkZNWVZfUGljTG1tclM1dF9uSnY5Z05tbmtQTWFOX0FmT0s4bW5VZ3JsYklCQTZRQ05GSW1oUjJlMW5WM1c1WnhNOEhuMFA0ZjJzOURNY0RjSnVKNVlmc2NpaUdpRVk3ME9pbnVnUGoxR2ItNUpDU2tjLWhfTFptSHNHSFBZR2lTcFhBbk9IVTJiano2XzRDZXpnV0FjN0g5Sk5GdFBuUlRLOUZvSWpxVVlqTmFUaXpaQQ?oc=5)
- [2026-02-22 12:05 yeeyi | 下周重磅日程：英伟达财报、特朗普国情咨文、美伊博弈、德总理访华-yeeyi - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1sRDlWQ1EzUzFKTk1weXo3TmNaRFVOemZ2X0FNLTNTNl9PcjlfUHJ4cXp4Uk82U0dlaGRaVUpSZlMxU09tZEpyWXJvYlNHRmt5VU5YQVVB?oc=5)
- [2026-02-22 09:48 3DM | 第一热点 澳门新葡新京网站 - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTFBUdS1LYWlzcDVUQUIzUHR6S0dHSmtIY1FHandITld0NmtCVDBLdEVKNDZOclBhNHA5My16MUdfYXBFNGQ5LUFFUkpSWEZBV2tuZzA5V0xVYw?oc=5)
- [2026-02-21 11:03 万维读者网 | 美股创20年来首年最差纪录 - 万维读者网](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1WSDNxZ3dzeWFoNWZpMlk3T05wZ2RPbFZZSllnajdvWXU4T0pxWk13eW1pd2xDSkZNaEhSQXQ1cURwRl96YTBaZC1mMTA5ZnFmMVE?oc=5)

---

*报告由 finradar 自动生成 | 2026-02-23 08:03:14（北京时间）*
