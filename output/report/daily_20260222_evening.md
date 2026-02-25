# 📰 finradar 🌇 晚报
**2026-02-22** | 🌇 晚报 | 覆盖时段: 今日08:00 → 20:00 | 市场状态: ⚠️ A股休市
生成时间: 2026-02-22 20:03（北京时间）

**⚠️ 注意：今日为周末，A股休市，部分市场数据可能缺失或未更新**

---

## 🚨 数据源健康提醒

1. 检测到微信登录异常：财联社: invalid session。请重新扫码登录 wechat-exporter。
2. 微信登录凭据最近更新已 4.9 天（阈值 4 天），建议尽快重新扫码登录。
3. 本次抓取公众号文章为 0 篇，账号搜索失败占比 100%，请检查登录态或服务状态。

处理建议：
1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。
2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。
3. 然后执行 `./scripts/local.sh report evening 20260222` 与 `./scripts/local.sh notion-push evening 20260222` 覆盖 Notion 页面。

# 🤖 AI 分析摘要

## 一、摘要
- **社会**：国内舆论焦点高度集中于**冬奥体育盛事**，谷爱凌卫冕夺金及中国队奖牌收官引发全网热议，形成积极社会情绪[NW01, NW02, NW03, NW04, NW10, NW12, NW13]。同时，“初中生扶老人被讹22万后撤诉”事件引发对司法公正与社会信任的讨论[NW06]。
- **经济**：**全球贸易政策不确定性持续发酵**。特朗普宣布将全球进口关税税率从10%加码至**15%**，引发企业诉讼潮，市场关注其后续执行与全球影响[NW05, NW08, NW11, NW14]。国内方面，1月社融增速为**8.2%**，货币政策效应待观察[WB13]。
- **市场**：今日为周末，**A股休市，无有效交易时段数据**。隔夜市场（历史报告）呈现**强烈的区域分化**，东亚市场（除韩国外）普遍承压，欧美市场（尤其科技股）走强，资金轮动特征明显。VIX指数下跌显示恐慌情绪有所缓和。
- **科技**：AI领域呈现**加速竞争与深层反思并存**。中美AI产业同步加速迭代，中国大模型春节“撒钱抢用户”与DeepSeek的沉默形成对比[NW07, WB08]。同时，对AI的负面社会情绪（“讨厌AI很酷”）[TW01]与关于“AI宪法”的深度讨论[WB01]并存，显示行业进入价值重估与规范构建期。

## 二、分板块汇报
### 2.1 市场概况（仅有效交易时段数据）
数据不足。今日（2026年2月22日）为周末，A股休市。根据“市场时效过滤说明”，非交易日数据不纳入盘面分析。需补充下周开盘后的实时交易数据以进行有效分析。

### 2.2 微信公众号共识与弱信号
数据不足。输入中未提供“微信公众号逐篇简介”或具体的公众号内容分析，无法提炼跨公众号的共识议题或弱信号候选。

### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）
较上期：延续对AI智能体/工作流开发工具的高度关注，新增对Web3安全工具的观察。

本次样本显示，**AI应用开发工具**仍是绝对热点，且向**低代码/可视化、生产就绪**方向演进。`langflow-ai/langflow`（可视化构建AI智能体工作流）与`langgenius/dify`（生产就绪的智能体工作流平台）功能高度重叠，均致力于降低AI应用开发门槛，其落地价值在于赋能企业快速实现业务流程自动化与智能化[GH07, GH08]。潜在噪音在于该赛道可能已出现同质化竞争，需甄别各项目的核心技术壁垒与生态成熟度。

**金融科技**领域，`Haehnchen/crypto-trading-bot`（加密货币交易机器人）与`AlexWan/OsEngine`（开源算法交易平台）提供了自动化交易的基础设施，应用场景明确，但面临策略有效性、市场适应性与合规性风险[GH12, GH13]。

**Web3**领域出现明确的安全需求信号。`MetaMask/eth-phishing-detect`项目专注于检测钓鱼域名，其应用场景是集成到钱包等产品中保护用户资产，具有防御性落地价值，反映了随着加密货币普及，安全防护成为刚需[来源ID: GH项目雷达分析]。

### 2.4 Twitter 海外信号（英文内容中文汇报）
较上期：新增对AI的负面社会情绪表达，延续对经济民生压力、政治对立及加密货币普及化的讨论。

核心信号有三条主线：1) **AI的社会接受度出现裂痕**：高互动推文“讨厌AI很酷”[¹](https://twitter.com/GarageGuyChase/status/2025255625815376033)以及用户分享“手工制作比AI生成更有趣”的经历[²](https://twitter.com/KietaJibun/status/2025459434517135581)，反映了部分群体对AI技术的情感排斥与对“手工”价值的重申，这可能构成AI产品推广的社会心理阻力。2) **经济民生压力感普遍**：用户抱怨“在这种经济下一切都很紧急”，呼应了“生活方式通胀”从童年开始的讨论[³](https://twitter.com/insidefolkative/status/2025192508901429626)[⁴](https://twitter.com/psvit/status/2025419843554681018)，显示高生活成本已成为全球性焦虑。3) **政治与地缘冲突言论极端化**：多条推文包含针对特定国家、宗教族群的激烈指控与煽动性言论[⁵](https://twitter.com/TheMuslim786/status/2025251859762680206)[⁶](https://twitter.com/Jvnior/status/2025192295264334093)[⁷](https://twitter.com/Urhobo_Mudiaga/status/2025465798899155327)，情绪化严重且缺乏事实依据，属于高噪音信号，主要反映网络空间的割裂态势。

在金融科技/Web3方面，币安推广低门槛（10美元起）交易550+种代币[⁸](https://twitter.com/binance/status/2013965079512076296)，显示平台持续推动加密货币投资“平民化”。另有观点将AI、芯片与算力定义为21世纪国家实力的新基石[⁹](https://twitter.com/raghav_chadha/status/2023632195148280168)。

### 2.5 国内新闻与政策脉络
较上期：新增特朗普关税加码的具体政策细节及国内1月社融数据，冬奥热点达到顶峰。

**核心政策动态**：美国前总统特朗普宣布，将此前计划的**10%** 全球进口关税税率提升至**15%**[¹⁰](https://wallstreetcn.com/articles/3765942)[¹¹](https://www.cls.cn/detail/2292405)。此举被指“越权”并已引发企业诉讼潮[¹⁰](https://wallstreetcn.com/articles/3765942)。分析认为，此举意在强化对华谈判筹码，其他关税方案都会削弱其筹码[¹²](https://news.ifeng.com/c/8qxAuTEgS6q)。该政策加码进一步提升了全球贸易政策的不确定性，可能加剧市场波动。**国内宏观数据**：1月社会融资规模存量同比增速为**8.2%**，报道指出货币政策累计效应仍需观察，降准降息等工具的使用有待进一步评估[¹³](https://news.google.com/rss/articles/CBMieEFVX3lxTE94WG1Ba2dpOEVQTzBrUjVPODF2V2tPajlISHVMRnhRd1F2ekFGSkNlaTY1S0tmNUFuYldGZXFyRnRaWk43WU1OdU9peUZuM1lQOWZ6cVcxOVhiMlhqaWlCUm94Rk44Y2FYQzZCU2E4T3Nxb3BIazhxVQ?oc=5)。

**产业与科技影响**：AI领域，国产大模型在2026年春节出现“撒钱抢用户”的营销战，而DeepSeek选择沉默深耕，引发市场对其不同策略的讨论[¹⁴](https://www.zhihu.com/question/2004982651719812885)。同时，有分析指出“AI恐慌交易”仍未完全消散[¹⁵](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5vMV9jMnV2WDNEejRuNjUybFVWSkNKSGhLbk1MOGNwVk9PSWwzamdacjZacmFRSUMxSmpXNmcxRVIzRlU5dDBsSUdfSGEwMVcyQlFqR3JobmRlYlpiUkRfdA?oc=5)，且AI数据中心全球扩张引发了与农业争地的社会讨论[¹⁶](https://news.google.com/rss/articles/CBMigwFBVV95cUxQU0l6RnpCTGZDby1QN1dmajlYa3RDUzhmUjJqZW5kM0FJWG1kSzdfODJWRl9lYUh4QzBOOUVjOXpXMjZrLUc0ZWtzcGF5NjFnY1BSd3M4cXJFSTRsN21YNTg1ajZYMHllRTFvLWZUVF8yQ3ZxMk9FbUswR1BQLU1STXotUQ?oc=5)。硬件方面，Intel与AMD的新一代桌面CPU（Nova Lake, Zen 6）被曝双双推迟至2027年[¹⁷](https://news.google.com/rss/articles/CBMiWEFVX3lxTFA0ZmVzMm5lUkFMQldxUk9EZzA0c2Q1WjVDNmRRZzZwbnhuMzdrYnFibjhLUndZRS1HOC01eUJkdGpZMndVcjFsOEVIWGM3b0pQTTJORlZsWUU?oc=5)，可能影响算力供给预期。

**社会热点**：谷爱凌在冬奥会自由式滑雪女子U型场地技巧项目夺冠，为中国队摘得第5金，并与队友李方慧包揽金银牌，成为全网绝对焦点[¹⁸](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E7%AC%AC%E4%B8%89%E6%BB%9194.75%E5%88%86%23)[¹⁹](https://search.bilibili.com/all?keyword=%E2%80%8B%E8%B0%B7%E7%88%B1%E5%87%8C%E6%91%98%E9%87%91)[²⁰](https://www.baidu.com/s?wd=%E7%AC%AC5%E9%87%91%EF%BC%81%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0)[²¹](https://www.toutiao.com/trending/7609123113803989035/)[²²](https://www.douyin.com/hot/2408149)[²³](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E9%87%91%E7%89%8C%23)[²⁴](https://www.baidu.com/s?wd=%E6%9D%8E%E6%96%B9%E6%85%A7%E5%A4%BA%E5%A5%B3%E5%AD%90U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E9%93%B6%E7%89%8C)。

## 三、明日跟踪清单
1.  **延续跟进：美国加征关税（15%）的后续市场与法律反应**：紧密跟踪美股、汇市及全球主要贸易股指对关税加码消息的消化情况，同时关注美国国内企业诉讼进展及他国可能的反制措施声明，评估其对全球供应链情绪的二次冲击。[¹⁰](https://wallstreetcn.com/articles/3765942)[¹¹](https://www.cls.cn/detail/2292405)[¹²](https://news.ifeng.com/c/8qxAuTEgS6q)
2.  **收口复盘：韩国股市独立行情的驱动逻辑验证**：结合历史两期关注，需尽快补充韩国市场在近期交易日（2月21-22日）的详细盘面数据、板块资金流向及政策面消息，以确认其强劲表现的可持续性与具体驱动因素。（**本期数据仍不足**）
3.  **新增观察：AI社会情绪分化对产业发展的潜在影响**：跟踪“讨厌AI很酷”等负面情绪是否在更广范围内发酵，并观察AI公司（特别是2C应用端）的营销策略、产品设计或ESG沟通是否出现相应调整，评估社会接受度成为产业发展新变量的可能性。[¹](https://twitter.com/GarageGuyChase/status/2025255625815376033)[¹⁵](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5vMV9jMnV2WDNEejRuNjUybFVWSkNKSGhLbk1MOGNwVk9PSWwzamdacjZacmFRSUMxSmpXNmcxRVIzRlU5dDBsSUdfSGEwMVcyQlFqR3JobmRlYlpiUkRfdA?oc=5)


---

<details><summary>📑 点击展开各板块详细分析</summary>

### 📊 市场数据详细分析

### 1. 主要市场走势判断
今日全球市场呈现**明显的区域分化**格局。
*   **亚太市场普遍承压**：A股（**-1.26%**）、日股（**-1.12%**）、港股（**-1.10%**）领跌主要市场，显示该区域面临显著抛压。韩股（**+2.31%**）是亚太市场的唯一亮点，表现异常强劲。
*   **欧美市场整体偏强**：欧洲股市表现突出，法国CAC40（**+1.39%**）、德国DAX（**+0.87%**）涨幅居前。美股三大指数亦录得上涨，纳斯达克（**+0.90%**）领涨，但罗素2000小盘股指数（**-0.05%**）微跌，显示内部存在分化。
*   **整体情绪**：跟踪的12个主要股指中，上涨7个，下跌5个，市场整体情绪偏向谨慎乐观，但区域间差异巨大。

### 2. 关键资产轮动分析
*   **领涨方向**：
    1.  **欧洲蓝筹股**：法国CAC40与德国DAX的显著上涨，显示资金在流向欧洲主要经济体的核心资产。这可能是对欧洲特定积极因素的反应，但具体驱动因素数据未提供。
    2.  **美国科技股**：纳斯达克指数涨幅（**+0.90%**）显著高于道琼斯指数（**+0.47%**），表明在美股内部，资金偏好**成长型/科技板块**。
    3.  **韩国股市**：韩国综合指数**+2.31%**的涨幅在全球主要市场中一骑绝尘，显示有强劲的本地化资金流入或积极事件驱动，但具体原因数据未提供。

*   **领跌方向**：
    1.  **大中华区股市**：A股与港股同步下跌超过1%，是今日主要的下跌区域，反映资金从该区域流出或避险情绪浓厚。
    2.  **日本股市**：日经225指数下跌**-1.12%**，与亚太疲软氛围一致。

*   **资金偏好解读**：资金明显从**东亚（除韩国外）** 流向**欧洲**和**美国科技板块**。这种轮动可能反映了对区域经济前景、政策环境或地缘风险的差异化定价。小盘股（罗素2000）的疲软与大盘科技股的强势，进一步印证了资金在追求确定性和流动性。

### 3. 加密货币和商品期货的关键变化
*   **加密货币**：主流加密货币（BTC, ETH）价格波动极小（涨跌幅约**+0.16%**），SOL微跌**-0.12%**。这表明在今日观察时段内，加密货币市场处于**极度盘整**状态，未受股票市场区域分化的显著影响。
*   **商品期货**：
    *   **工业金属**：COMEX铜价上涨**+1.90%**，表现突出，可能与全球制造业需求预期或供应端因素有关，但具体驱动数据未提供。
    *   **能源**：原油价格窄幅震荡，WTI微涨**+0.08%**，布伦特微跌**-0.50%**；天然气下跌**-0.40%**。能源市场整体缺乏明确方向。
    *   **贵金属**：数据未提供，无法分析。

### 4. 涨跌驱动链条分析
基于现有数据，可推断以下部分驱动链条：

*   **亚太市场下跌链条（证据强度：中）**
    *   **事件/情绪**：数据未提供具体负面事件。但A股、港股、日股同步下跌，暗示可能存在影响整个东亚地区的**区域性担忧或负面情绪**。
    *   **资金行为**：资金从上述市场**流出**（表现为指数下跌）。
    *   **价格表现**：A股（**-1.26%**）、日股（**-1.12%**）、港股（**-1.10%**）显著收跌。

*   **欧洲股市上涨链条（证据强度：中）**
    *   **事件/政策**：数据未提供具体利好政策或事件。
    *   **资金行为**：资金**流入**欧洲主要股指，特别是法国和德国股市。
    *   **价格表现**：法国CAC40（**+1.39%**）、德国DAX（**+0.87%**）大幅上涨。

*   **美股科技股领涨链条（证据强度：中）**
    *   **情绪/偏好**：市场风险偏好更集中于**大盘成长股**。
    *   **资金行为**：资金在美股内部**轮动至科技板块**。
    *   **价格表现**：纳斯达克指数（**+0.90%**）跑赢道琼斯指数（**+0.47%**），罗素2000小盘股指数收跌。

*   **市场波动率下降链条（证据强度：强）**
    *   **事件/情绪**：尽管股市区域分化，但欧美主要市场上涨可能缓和了部分担忧情绪。
    *   **资金行为**：数据未直接提供，但VIX指数下跌通常反映期权市场对冲需求下降。
    *   **价格表现**：**VIX波动率指数下跌-5.64%**，至19.09，表明市场整体恐慌情绪在今日观察时段内有所降温。

**总结**：今日市场核心特征是**强烈的区域轮动**，东亚（除韩国）与欧美市场走势完全背离。资金从东方流向西方，并在美股内部聚焦科技龙头。商品中铜价异动值得关注，而加密货币陷入沉寂。所有涨跌背后的具体宏观政策或事件驱动因素，**数据均未提供**。

### ⏱ 市场时效过滤说明

市场时效过滤结果：
1. 非交易日，不纳入 A 股盘面

### 🐦 Twitter 逐条简介

Twitter 逐条简介（共 12 条，按互动热度排序）：
1. [热门] @GarageGuyChase | 2026-02-22T12:00 | 互动=39384
   原文摘录: It’s so cool to hate AI
   原文链接: [点击查看原文](https://twitter.com/GarageGuyChase/status/2025255625815376033)
   1) 讲了什么：一条推文称“讨厌AI很酷”，互动数据较高。
   2) 关键信号：推文内容为观点性陈述，未提供具体事件或数据。
   3) 阅读建议：略读 + 原因：仅为个人观点表达，无具体信息或分析。
2. [热门] @elonmusk | 2026-02-22T12:00 | 互动=21923
   原文摘录: Yes
   原文链接: [点击查看原文](https://twitter.com/elonmusk/status/2024819025298235611)
   1) 讲了什么：埃隆·马斯克账号发布了一条内容为“Yes”的推文。
   2) 关键信号：推文互动数据较高，但内容本身无具体信息。
   3) 阅读建议：略读 + 原因：推文仅有一个单词，无具体事件或观点阐述。
3. [热门] @ClaireGeronimii | 2026-02-22T12:00 | 互动=11014
   原文摘录: J’ai le plaisir de vous annoncer ma candidature aux municipales les 15 et 22 mars prochains dans la ville de Saint-Quentin ! Au plaisir de vous rencontrer et de
   原文链接: [点击查看原文](https://twitter.com/ClaireGeronimii/status/2025201582590025974)
   1) 讲了什么：账号宣布将参加圣康坦市3月15日和22日的市政选举。
   2) 关键信号：未提供。
   3) 阅读建议：略读 + 原因：内容为个人政治参选声明，与金融科技关联度低。
4. [热门] @TheMuslim786 | 2026-02-22T12:00 | 互动=7243
   原文摘录: Location: Badaun,UP "Get out of the village, you're jihadis, you're Katuas," Akshay Singh said, starting to beat them. The victim, Abdul Salam, said, "We had go
   原文链接: [点击查看原文](https://twitter.com/TheMuslim786/status/2025251859762680206)
   1) 讲了什么：报道了在巴道恩发生的基于宗教身份的袭击事件及受害者的陈述。
   2) 关键信号：袭击基于宗教身份，受害者称是为宗教学校募捐。
   3) 阅读建议：略读 + 原因：提供了事件基本事实，但未提供更广泛的背景或数据。
5. [热门] @insidefolkative | 2026-02-22T12:00 | 互动=7189
   原文摘录: "Siapin dana darurat makanya". In this economy semuanya darurat bjirr 😭😭😭😭😭😭😭😭
   原文链接: [点击查看原文](https://twitter.com/insidefolkative/status/2025192508901429626)
   1) 讲了什么：一条关于经济状况和应急资金的推文，表达了情绪。
   2) 关键信号：推文提到“应急资金”和“在这种经济下一切都很紧急”。
   3) 阅读建议：略读 + 原因：内容为个人情绪化表达，无具体事件或数据。
6. [热门] @lebscit | 2026-02-22T12:00 | 互动=6079
   原文摘录: por causa de um hat-trick no vitória, disseram que o pedro era melhor que esse mano aí
   原文链接: [点击查看原文](https://twitter.com/lebscit/status/2025326348202278958)
   1) 讲了什么：因在维多利亚队上演帽子戏法，有人说佩德罗比那个人更好。
   2) 关键信号：未提供具体比较对象、背景及数据。
   3) 阅读建议：略读，内容仅为一句球迷间的比较性评论，信息有限。
7. [热门] @Mattpetti32 | 2026-02-22T12:00 | 互动=5294
   原文摘录: - Trump didn't legalize deadly drugs like Fentanyl - Trump didn't flood Canada with millions of immigrants - Trump didn't cause massive food inflation - Trump d
   原文链接: [点击查看原文](https://twitter.com/Mattpetti32/status/2025237089340555347)
   1) 讲了什么：推文列举特朗普未做的一系列负面事件，如未导致毒品合法化、移民涌入等。
   2) 关键信号：未提供具体数据或证据，仅为否定性陈述列表。
   3) 阅读建议：略读 + 原因：内容为单方面主张，缺乏事实支撑与背景信息。
8. [热门] @Jvnior | 2026-02-22T12:00 | 互动=4558
   原文摘录: Israeli jews are: - serial liars - baby killers - minor lovers - skin stealers - sex traffickers - organ harvesters - home destroyers - enemies of Islam - satan
   原文链接: [点击查看原文](https://twitter.com/Jvnior/status/2025192295264334093)
   1) 讲了什么：账号@Jvnior发布一条包含对以色列犹太人多项负面指控的推文。
   2) 关键信号：推文互动数据较高，内容包含强烈指控，但未提供任何事实依据。
   3) 阅读建议：略读。内容为情绪化指控，缺乏事实与数据支撑，信息价值低。
9. [热门] @binance | 2026-02-22T12:00 | 互动=4000
   原文摘录: From Bitcoin to altcoins, explore 550+ tokens and trade easily on Binance starting with just $10
   原文链接: [点击查看原文](https://twitter.com/binance/status/2013965079512076296)
   1) 讲了什么：币安平台宣传可交易550多种代币，最低10美元起。
   2) 关键信号：提及比特币、山寨币，强调交易便捷性和低门槛。
   3) 阅读建议：略读 + 原因：内容为平台常规推广，无具体事件或数据更新。
10. [热门] @KietaJibun | 2026-02-22T12:00 | 互动=3269
   原文摘录: こうやってAIに画像を作らせることも出来た、でも手作りの方が面白くなると思ったから30分くらいかけてコラ画像を作ったんだ
   原文链接: [点击查看原文](https://twitter.com/KietaJibun/status/2025459434517135581)
   1) 讲了什么：用户分享了自己用AI生成图像后又花时间手工制作合成图的经历。
   2) 关键信号：AI可生成图像，但用户认为手工制作更有趣。
   3) 阅读建议：略读 + 原因：内容为个人创作体验分享，无具体金融科技信息。
11. [热门] @psvit | 2026-02-22T12:00 | 互动=2418
   原文摘录: สิ่งนี้คือ Lifestyle Inflation ซึ่งเดี๋ยวนี้เกิดตั้งแต่เด็ก เพราะตามพ่อแม่มา ซูชิโระทุกอาทิตย์ หรือถ้าเป็นทางผ่านหลักเลิกเรียนได้มีกินบ่อยกว่านั้น ซูชิตลาดนัด ซ
   原文链接: [点击查看原文](https://twitter.com/psvit/status/2025419843554681018)
   1) 讲了什么：讨论生活方式通胀，从童年开始，因跟随父母每周吃寿司，现在无法接受廉价寿司。
   2) 关键信号：生活方式通胀从童年开始，对廉价食品口味标准提高。
   3) 阅读建议：略读 + 原因：观点描述为主，未提供具体数据或金融科技直接关联。
12. [热门] @Urhobo_Mudiaga | 2026-02-22T12:00 | 互动=1886
   原文摘录: Stop complaining and nagging every single day, about elections, the system, the economy, religion and so forth. COME OUT AND LETS KiLL THEM ALL. Without KiLLING
   原文链接: [点击查看原文](https://twitter.com/Urhobo_Mudiaga/status/2025465798899155327)
   1) 讲了什么：用户呼吁停止抱怨，主张采取极端行动以改善国家。
   2) 关键信号：未提供具体金融科技事件或数据。
   3) 阅读建议：略读，内容与金融科技主题无关。

### 🌐 Twitter 英文信号详细分析

### 海外英文信号主线
1.  **政治与地缘冲突**：信号中充斥着强烈的政治对立与宗教/民族冲突。包括法国地方选举、印度宗教暴力事件、美国前总统特朗普与现政府的对比、以及针对以色列的激烈指控。这些讨论情绪化严重，可能加剧社会分裂。
2.  **经济与市场关切**：用户普遍表达对经济状况的担忧，如通货膨胀、生活成本危机（尤其在退休人群中）以及呼吁关注具体民生问题（如收费诈骗、医院腐败）。同时，对尼日利亚、巴基斯坦卡拉奇等特定区域的经济前景和投资机会有集中讨论。
3.  **科技与未来叙事**：人工智能（AI）和算力被明确视为21世纪国家实力的新基石（“AI、芯片和算力能力”）。同时，存在关于外星人存在的轻松讨论，并暗示此类消息已被市场平淡消化。

### 金融科技/AI/Web3相关线索
1.  **加密货币与交易**：币安（Binance）推广其平台，支持从比特币到山寨币等550多种代币的交易，入门门槛低至10美元。另有用户提及印度的加密货币税收体系是需要被讨论的“实际问题”之一。
2.  **人工智能（AI）的核心地位与争议**：
    *   **战略重要性**：有观点指出，AI、芯片和算力是21世纪权力的来源，GPU短缺不仅是供应链问题，更是“主权问题”。
    *   **社会反思与批评**：出现对AI的负面情绪（“讨厌AI很酷”），并担忧其高能耗问题及可能加剧的“资本家的梦想”（即取代付费劳动力）。
3.  **市场表现与预测**：
    *   提及英伟达（NVIDIA）市值从2024年初的1.22万亿美元增长至当前的4.63万亿美元。
    *   有账号传播美国前总统特朗普关于美股在其任期内将翻倍的预测。

### 可执行关注点与潜在误导噪音
**可执行关注点**：
*   **主权AI与算力竞赛**：关注将GPU等算力资源提升到国家主权高度的论述，这可能预示着相关产业政策、供应链安全及投资主题的持续升温。
*   **新兴市场金融科普需求**：尼日利亚股市的“完整初学者指南”获得高互动，显示特定新兴市场本地投资者的教育需求旺盛，可能存在相关的金融信息服务和产品机会。
*   **加密货币的“平民化”推广**：主流交易平台持续降低投资门槛（如10美元起投），致力于扩大用户基础，是观察市场渗透率的窗口。

**潜在误导噪音**：
*   **极端化政治与冲突言论**：大量信号涉及煽动暴力、宗教仇恨和政治人身攻击（如“杀死他们全部”、“婴儿杀手”等）。这些内容情绪极端，事实依据未提供，主要反映社会对立情绪，对判断具体事件真相价值低，且易引发误导。
*   **缺乏依据的市场预测**：关于美股“翻倍”的预测仅为个人观点引用，未提供任何分析依据，应视为噪音。
*   **情绪化与泛化讨论**：关于AI“高能耗”、“取代人类”的讨论较为泛化，属于社会情绪反映，未提供具体数据或案例，需谨慎对待其对于短期产业趋势的判断价值。

### 📰 热榜详细分析

# 热榜综合分析报告

基于提供的多个分片摘要，现将去重后的跨平台热点事件、金融市场、科技/AI及社会舆论焦点分析如下：

## 1. 跨平台共同关注的3-5个热点事件
1.  **特朗普关税政策**：该事件在多个分片中被反复提及，是当前最核心的国际政治经济事件。具体事实包括：特朗普宣布签署行政令，将全球进口关税从10%加征至15%；此举已引发企业诉讼潮，被指“越权”；有分析认为其可能“翻车”并利好美股，也有观点关注其对全球贸易的潜在影响。
2.  **谷爱凌冬奥夺金及相关赛事**：该体育事件是贯穿多个分片的社会热点。具体事实包括：谷爱凌在米兰冬奥会自由式滑雪女子U型场地技巧项目中卫冕冠军，并与队友李方慧包揽金银牌；其夺冠话题在微博、Bilibili等多平台成为高热度内容；中国队在本届冬奥会以5金4银6铜收官。
3.  **春节档电影票房与春节尾声**：春节文化相关事件是重要的社会焦点。具体事实包括：春节档总票房突破40亿，其中《飞驰人生3》以21亿领跑；最长春节假期步入尾声，返程客流即将迎来高峰，相关话题（如春运返程、压岁钱、拜年习俗等）持续受到讨论。
4.  **AI领域的动态与争议**：AI相关事件在科技和金融层面均受关注。具体事实包括：OpenAI被报道面临“四大困境”（具体内容未提供）并大幅下调算力支出目标至6000亿美元；同时，国产大模型在2026年春节出现“撒钱抢用户”的营销竞争，而DeepSeek则采取“默不作声继续奋战”的策略。

## 2. 与金融市场相关的重要新闻
*   **关税政策的市场影响**：特朗普加征全球进口关税至15%是直接影响金融市场的核心政策信号。市场反应出现分歧：一方面有线索称此举可能“翻车”并推动美股三大指数集体收涨；另一方面，该政策已直接引发企业诉讼潮，可能影响全球贸易与相关企业。美股市场出现结构分化现象：指数波动率创1960年来新低，但个股波动率高达指数的7倍。
*   **私募与投资动向**：有线索显示中国顶流私募在Q4集体加仓拼多多，同时AI投资重心发生转变。另一方面，对冲基金以比净值低20-35%的价格收购Blue Owl旗下私募股权基金份额，加剧了市场对私募股权流动性与估值的质疑。
*   **其他市场线索**：春节档票房破40亿，分析提及背后涉及A股公司（具体公司未提供）。全球“内存荒”被指为AI竞赛的关键瓶颈，可能构成潜在市场波动因素。OpenAI下调算力支出目标，可能影响相关产业链预期。

## 3. 科技/AI 相关热点
*   **AI产业的风险与竞争**：AI领域存在显著分歧与动态。一方面，有企业领袖（如SK会长崔泰源）警告AI可能带来巨大盈利风险；另一方面，机构（如大摩）将MiniMax评价为“全球顶尖基座模型稀缺资产”。产业层面，OpenAI被指面临困境并下调算力目标，而国产大模型在春节期间展开营销抢用户大战。
*   **关键技术瓶颈与产品**：“内存荒”被明确指为全球性现象，并成为AI竞赛的关键瓶颈。在产品层面，特斯拉发布了没有方向盘和脚踏板的新车型，涉及自动驾驶技术创新。
*   **其他科技线索**：春晚人形机器人表演引发关注，其背后涉及A股新材料产业链，有企业被指抢占赛道先机。关于AI未来，有观点提出将进入“为AI服务”而非“为人创造”的智能体新时代。

## 4. 社会舆论焦点
*   **体育盛事与运动员**：谷爱凌、李方慧等运动员在冬奥会的表现及中国队整体成绩是绝对的舆论焦点，占据多条热搜。
*   **法律、道德与社会事件**：多个具体事件引发广泛讨论，包括：“初中生扶老人被讹22万元”案件以撤诉告终；四川广元法院在春节执行行动中一日拘传38名“老赖”；罗翔涉及为黑老大减刑的事件；以及平顶山夫妻暴打15岁女孩事件。这些事件共同指向社会信任、司法公正与诚信问题。
*   **春节文化与民生百态**：舆论广泛关注春节相关话题，包括：春节民俗（如送穷日、拜年）、压岁钱争议、春运返程、家庭相处模式（如情侣家庭责任讨论）、过年新方式（如洗浴中心过年），以及虚假信息（如“江西丰城鞭炮炸死人”被证实编造）。
*   **国际政治与争议**：除特朗普关税政策外，舆论还关注：中东局势（沙特等14国谴责以色列相关言论、美以与伊朗博弈）；韩国外交部抗议日本举行“竹岛日”活动；韩国队抗议米兰冬奥会多次印错其国旗；“一顿中餐掀翻秘鲁政坛”的报道引发对大国博弈的猜测。

### 💻 GitHub 项目详细分析

# GitHub热门项目技术趋势分析报告

基于今日（2026-02-22）GitHub项目样本，按领域筛选出最值得关注的7个项目，并分析其应用场景、落地价值及潜在噪音。

## 一、最值得关注的项目

**金融科技 (FinTech)**
1.  **Haehnchen/crypto-trading-bot**：一个支持多个主流加密货币交易所的自动化交易机器人。
2.  **AlexWan/OsEngine**：一个开源的算法交易平台。

**人工智能 (AI)**
3.  **openclaw/openclaw**：一个跨平台、跨操作系统的个人AI助手。
4.  **n8n-io/n8n**：一个具备原生AI能力的公平代码工作流自动化平台。
5.  **langflow-ai/langflow**：一个用于构建和部署AI智能体与工作流的工具。
6.  **langgenius/dify**：一个用于智能体工作流开发的生产就绪平台。

**Web3**
7.  **MetaMask/eth-phishing-detect**：一个用于检测针对Web3用户的钓鱼域名的工具。

## 二、应用场景与落地价值分析

1.  **加密货币交易自动化**：`crypto-trading-bot`和`OsEngine`项目为个人和机构投资者提供了自动化交易策略执行的能力，其价值在于提升交易效率、减少人为情绪干扰，并可能通过算法捕捉市场机会。应用场景包括量化交易、套利和风险管理。
2.  **AI智能体与工作流开发**：`openclaw`、`langflow`和`dify`项目共同指向一个明确的趋势：降低AI应用开发门槛，让非专业开发者也能构建复杂的AI驱动流程。其落地价值在于赋能企业快速将AI能力集成到业务流程、客户服务或内部工具中，实现自动化与智能化升级。
3.  **企业级自动化平台**：`n8n`项目将可视化工作流构建与AI能力、大量集成相结合，其核心价值是为企业提供灵活、可自托管（或云端部署）的自动化解决方案，连接不同系统与服务，优化运营效率。
4.  **Web3安全防护**：`eth-phishing-detect`项目直接应对加密货币领域日益严重的钓鱼威胁。其应用场景是集成到钱包或安全产品中，实时保护用户资产安全，具有明确的、防御性的落地价值。

## 三、潜在泡沫噪音与重复概念

*   **AI智能体/工作流平台概念集中**：`langflow`与`dify`在项目描述上高度相似，均聚焦于“AI智能体”和“工作流”的构建与部署。这反映出该赛道竞争激烈，可能存在功能重叠或概念炒作，需要仔细甄别各项目的独特优势与成熟度。
*   **金融科技项目功能边界模糊**：样本中出现了多个针对Polymarket预测市场的交易机器人。这些项目可能基于相似策略（如RSI、MACD），存在重复造轮子的可能性，其长期价值和差异化优势数据不足。
*   **通用AI助手定位宽泛**：`openclaw`宣称是“任何OS、任何平台”的个人AI助手，此类项目通常面临如何实现真正通用、实用且优于现有专用工具的挑战，其具体能力边界和核心技术亮点未提供。
*   **数据不足的领域**：在本次样本中，“通用开发”类别仅列出一个长期存在的机器学习框架（Tensorflow），无新兴趋势项目。Web3领域除安全工具外，未出现新的热门智能合约或去中心化应用项目，可能表明今日热度集中于AI与自动化。

### 🌐 联网检索摘要

联网检索共 13 条（关键词: 2026-02-22 全球市场 盘面 复盘 原因, 2026-02-22 中国 宏观 经济 政策 市场 影响, 2026-02-22 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, ETH 上涨 原因, 谷爱凌第三滑94.75分 事件 背景, ​谷爱凌摘金 事件 背景, 第5金！谷爱凌夺冠 事件 背景）
1. [2026-02-22 18:31] 新浪财经 | 中美AI同步加速：47天30次更新，中国AI的最强主场究竟在哪？ - 新浪财经
   摘要: 中美AI同步加速：47天30次更新，中国AI的最强主场究竟在哪？ 新浪财经
   链接: https://news.google.com/rss/articles/CBMifEFVX3lxTE9wRTgwVjFlMGJFd0l1dU9acENZOVJ1NGdTVmRHcFVvMWF5UDZ0d3gyenlnYVJlTGhsZEl4aVJZQzJ4UXJ4QnRCZmxMOVhwUHNLbWlpSUFaLS1KOU54NUt6QUc3dkVfR3luWlVPZkl3a2pOeDROZjZ0SEpaTDA?oc=5
2. [2026-02-22 17:20] 3DM | 【均已开售】2024 易博APP下载 - 3DM
   摘要: 【均已开售】2024 易博APP下载 3DM
   链接: https://news.google.com/rss/articles/CBMiV0FVX3lxTE9aclIxZjlJVUM4WlEtSkJCOHZFMTJtOGNRbFdZREZ1T0t1YklDRW9VMjdReldySFMzNF9FcDdJTkk4VHZ0SEw5QVdjSnBiYXl3NE1ySktaNA?oc=5
3. [2026-02-22 16:03] news.17173.com | 详读 2 万 3 千字的新「AI 宪法」之后，我理解了 Anthropic 的痛苦 - news.17173.com
   摘要: 详读 2 万 3 千字的新「AI 宪法」之后，我理解了 Anthropic 的痛苦 news.17173.com
   链接: https://news.google.com/rss/articles/CBMiZkFVX3lxTE5PbkUyNzRCMEU1d2J5TE1EdHpUenhWeGNZQ0s2eGdiTE9HX3lUeWpCMDlVenVJcUp5SGZzUVVTN19INW9fdUdBU1hSUndkRmtUOVVHRGhNbS1hQ0pEbFhwZUpqTE5QQQ?oc=5
4. [2026-02-22 14:09] 新浪财经 | 恒生科技估值跌至低位，汇添富恒生科技ETF联接发起式(QDII)C(013128)捕捉AI叙事加持下估值修复红利 - 新浪财经
   摘要: 恒生科技估值跌至低位，汇添富恒生科技ETF联接发起式(QDII)C(013128)捕捉AI叙事加持下估值修复红利 新浪财经
   链接: https://news.google.com/rss/articles/CBMieEFVX3lxTFBiSF9DZnBtTktNa25RTXZhdnB4V3lFOGRIME5aZWdpa182SVE5cFkwclQ1WEFSQXRHMnVEaUUtRUxlUEFXazFPd0tqRnViWFg1c0RyaWVtUWszZGtfRVJPZkFsVFhyNWV0d0R2Qlo1clNXSTFnNU1weA?oc=5
5. [2026-02-22 13:55] 新浪财经 | 1月社融规模增速8.2% 降准降息仍待观察货币政策累计效应 - 新浪财经
   摘要: 1月社融规模增速8.2% 降准降息仍待观察货币政策累计效应 新浪财经
   链接: https://news.google.com/rss/articles/CBMieEFVX3lxTE94WG1Ba2dpOEVQTzBrUjVPODF2V2tPajlISHVMRnhRd1F2ekFGSkNlaTY1S0tmNUFuYldGZXFyRnRaWk43WU1OdU9peUZuM1lQOWZ6cVcxOVhiMlhqaWlCUm94Rk44Y2FYQzZCU2E4T3Nxb3BIazhxVQ?oc=5
6. [2026-02-22 13:11] 大紀元新聞網 | 井友倫：如何解讀最高院關稅裁決的影響 - 大紀元新聞網
   摘要: 井友倫：如何解讀最高院關稅裁決的影響 大紀元新聞網
   链接: https://news.google.com/rss/articles/CBMiZkFVX3lxTE9FSlVZQjk4RWpIQUNocmJTcG42a2M0RXRMSzRaSEJsVmVvcVJfVHFDZm9TeG5sbU4xMzl0WGdmSkZYY0dsQW9BUXNHZWNBT0RHX25zNUNfb3h0ZnFGQ1RnakZIRlVKd9IBZkFVX3lxTE9FSlVZQjk4RWpIQUNocmJTcG42a2M0RXRMSzRaSEJsVmVvcVJfVHFDZm9TeG5sbU4xMzl0WGdmSkZYY0dsQW9BUXNHZWNBT0RHX25zNUNfb3h0ZnFGQ1RnakZIRlVKdw?oc=5
7. [2026-02-22 10:30] 证券之星 | 回归“小央行”：美联储“沃什时代”前瞻_宏观研究_研报 - 证券之星
   摘要: 回归“小央行”：美联储“沃什时代”前瞻_宏观研究_研报 证券之星
   链接: https://news.google.com/rss/articles/CBMiYkFVX3lxTE8wWV84MlRNUklJNGJBbmlvWEhPWE9RWE5Pc0NXZXBLc21ERl9wZmF6LWlNZ1g3LTJRc2xZUEViZi0wUjVydGZwQnhuZmRGWGdZQ1d0X0lWUkJYWDRsTUJuYUFR?oc=5
8. [2026-02-22 09:48] 3DM | 第一热点 澳门新葡新京网站 - 3DM
   摘要: 第一热点 澳门新葡新京网站 3DM
   链接: https://news.google.com/rss/articles/CBMiV0FVX3lxTFBUdS1LYWlzcDVUQUIzUHR6S0dHSmtIY1FHandITld0NmtCVDBLdEVKNDZOclBhNHA5My16MUdfYXBFNGQ5LUFFUkpSWEZBV2tuZzA5V0xVYw?oc=5
9. [2026-02-22 09:10] thepaper.cn | 乘势而上｜专访张晓晶：引导政府部门存量财富向居民部门适度转移 - thepaper.cn
   摘要: 乘势而上｜专访张晓晶：引导政府部门存量财富向居民部门适度转移 thepaper.cn
   链接: https://news.google.com/rss/articles/CBMiYEFVX3lxTFAzUjREV1kySDZiaThkdVNCMUdtOWEwaDdIMFN4aGdsczIwenpMekIxODExQmUxMXlSRkYtWjZ3ZlBnMGhfMFUxOHBiSE90Ni1RMy13cDRuYjFlSkdvM2hSSg?oc=5
10. [2026-02-22 09:02] 新浪新闻_手机新浪网 | AI数据中心全球扩张浪潮下，农民坚守土地如何影响科技与农业的平衡发展？ - 新浪新闻_手机新浪网
   摘要: AI数据中心全球扩张浪潮下，农民坚守土地如何影响科技与农业的平衡发展？ 新浪新闻_手机新浪网
   链接: https://news.google.com/rss/articles/CBMigwFBVV95cUxQU0l6RnpCTGZDby1QN1dmajlYa3RDUzhmUjJqZW5kM0FJWG1kSzdfODJWRl9lYUh4QzBOOUVjOXpXMjZrLUc0ZWtzcGF5NjFnY1BSd3M4cXJFSTRsN21YNTg1ajZYMHllRTFvLWZUVF8yQ3ZxMk9FbUswR1BQLU1STXotUQ?oc=5
11. [2026-02-22 08:19] thepaper.cn | “AI恐慌交易”仍未完全消散 - thepaper.cn
   摘要: “AI恐慌交易”仍未完全消散 thepaper.cn
   链接: https://news.google.com/rss/articles/CBMiYEFVX3lxTE5vMV9jMnV2WDNEejRuNjUybFVWSkNKSGhLbk1MOGNwVk9PSWwzamdacjZacmFRSUMxSmpXNmcxRVIzRlU5dDBsSUdfSGEwMVcyQlFqR3JobmRlYlpiUkRfdA?oc=5
12. [2026-02-22 08:17] 驱动之家 | Intel、AMD新一代桌面CPU发布时间曝光！Nova Lake、Zen 6双双推迟到2027年 - 驱动之家
   摘要: Intel、AMD新一代桌面CPU发布时间曝光！Nova Lake、Zen 6双双推迟到2027年 驱动之家
   链接: https://news.google.com/rss/articles/CBMiWEFVX3lxTFA0ZmVzMm5lUkFMQldxUk9EZzA0c2Q1WjVDNmRRZzZwbnhuMzdrYnFibjhLUndZRS1HOC01eUJkdGpZMndVcjFsOEVIWGM3b0pQTTJORlZsWUU?oc=5
13. [2026-02-22 04:27] 游侠网 | 国际AG|联合多国艺术家打造和平主题艺术展 - 游侠网
   摘要: 国际AG|联合多国艺术家打造和平主题艺术展 游侠网
   链接: https://news.google.com/rss/articles/CBMiSkFVX3lxTE1yLUZkYXdXNXFiS3NiUThLNGI5UXJXbER3YXl3Q244UkpYSW91cEg0aHlHUjZxazBxcDNQaGQ2UmdqTTRqOVRTbWVB?oc=5

</details>


### 📎 引用脚注

1. [2026-02-22T12:00 @GarageGuyChase | It’s so cool to hate AI](https://twitter.com/GarageGuyChase/status/2025255625815376033)（Twitter，匹配分=100，来源ID=TW01）
2. [2026-02-22T12:00 @KietaJibun | こうやってAIに画像を作らせることも出来た、でも手作りの方が面白くなると思ったから30分くらいかけてコラ画像を作ったんだ](https://twitter.com/KietaJibun/status/2025459434517135581)（Twitter，匹配分=100，来源ID=TW10）
3. [2026-02-22T12:00 @insidefolkative | "Siapin dana darurat makanya". In this economy semuanya darurat bjirr 😭😭😭😭😭😭😭😭](https://twitter.com/insidefolkative/status/2025192508901429626)（Twitter，匹配分=100，来源ID=TW05）
4. [2026-02-22T12:00 @psvit | สิ่งนี้คือ Lifestyle Inflation ซึ่งเดี๋ยวนี้เกิดตั้งแต่เด็ก เพราะตามพ่อแม่มา ซูชิโระทุกอ...](https://twitter.com/psvit/status/2025419843554681018)（Twitter，匹配分=100，来源ID=TW11）
5. [2026-02-22T12:00 @TheMuslim786 | Location: Badaun,UP "Get out of the village, you're jihadis, you're Katuas," Akshay Sing...](https://twitter.com/TheMuslim786/status/2025251859762680206)（Twitter，匹配分=100，来源ID=TW04）
6. [2026-02-22T12:00 @Jvnior | Israeli jews are: - serial liars - baby killers - minor lovers - skin stealers - sex tra...](https://twitter.com/Jvnior/status/2025192295264334093)（Twitter，匹配分=100，来源ID=TW08）
7. [2026-02-22T12:00 @Urhobo_Mudiaga | Stop complaining and nagging every single day, about elections, the system, the economy,...](https://twitter.com/Urhobo_Mudiaga/status/2025465798899155327)（Twitter，匹配分=100，来源ID=TW12）
8. [2026-02-22T12:00 @binance | From Bitcoin to altcoins, explore 550+ tokens and trade easily on Binance starting with ...](https://twitter.com/binance/status/2013965079512076296)（Twitter，匹配分=100，来源ID=TW09）
9. [2026-02-22T12:00 @raghav_chadha | In the 20th century, power depended on OIL and STEEL. In the 21st century, power depends...](https://twitter.com/raghav_chadha/status/2023632195148280168)（Twitter，匹配分=100，来源ID=TW14）
10. [华尔街见闻 #1 | 特朗普新加征关税税率加码至15% 美政府“越权”关税引企业诉讼潮](https://wallstreetcn.com/articles/3765942)（NewsNow热榜，匹配分=100，来源ID=NW05）
11. [财联社热门 #1 | 特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405)（NewsNow热榜，匹配分=100，来源ID=NW11）
12. [凤凰网 #2 | 美国前商务部长：其他关税方案，都会削弱特朗普对华谈判筹码](https://news.ifeng.com/c/8qxAuTEgS6q)（NewsNow热榜，匹配分=100，来源ID=NW14）
13. [2026-02-22 13:55 新浪财经 | 1月社融规模增速8.2% 降准降息仍待观察货币政策累计效应 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE94WG1Ba2dpOEVQTzBrUjVPODF2V2tPajlISHVMRnhRd1F2ekFGSkNlaTY1S0tmNUFuYldGZXFyRnRaWk43WU1OdU9peUZuM1lQOWZ6cVcxOVhiMlhqaWlCUm94Rk44Y2FYQzZCU2E4T3Nxb3BIazhxVQ?oc=5)（联网检索，匹配分=100，来源ID=WB13）
14. [知乎 #1 | 如何看待当所有国产大模型都在 2026 春节撒钱抢用户时，DeepSeek 却默不作声继续奋战？](https://www.zhihu.com/question/2004982651719812885)（NewsNow热榜，匹配分=100，来源ID=NW07）
15. [2026-02-22 08:19 thepaper.cn | “AI恐慌交易”仍未完全消散 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5vMV9jMnV2WDNEejRuNjUybFVWSkNKSGhLbk1MOGNwVk9PSWwzamdacjZacmFRSUMxSmpXNmcxRVIzRlU5dDBsSUdfSGEwMVcyQlFqR3JobmRlYlpiUkRfdA?oc=5)（联网检索，匹配分=100，来源ID=WB10）
16. [2026-02-22 09:02 新浪新闻_手机新浪网 | AI数据中心全球扩张浪潮下，农民坚守土地如何影响科技与农业的平衡发展？ - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMigwFBVV95cUxQU0l6RnpCTGZDby1QN1dmajlYa3RDUzhmUjJqZW5kM0FJWG1kSzdfODJWRl9lYUh4QzBOOUVjOXpXMjZrLUc0ZWtzcGF5NjFnY1BSd3M4cXJFSTRsN21YNTg1ajZYMHllRTFvLWZUVF8yQ3ZxMk9FbUswR1BQLU1STXotUQ?oc=5)（联网检索，匹配分=100，来源ID=WB12）
17. [2026-02-22 08:17 驱动之家 | Intel、AMD新一代桌面CPU发布时间曝光！Nova Lake、Zen 6双双推迟到2027年 - 驱动之家](https://news.google.com/rss/articles/CBMiWEFVX3lxTFA0ZmVzMm5lUkFMQldxUk9EZzA0c2Q1WjVDNmRRZzZwbnhuMzdrYnFibjhLUndZRS1HOC01eUJkdGpZMndVcjFsOEVIWGM3b0pQTTJORlZsWUU?oc=5)（联网检索，匹配分=100，来源ID=WB11）
18. [微博 #1 | 谷爱凌第三滑94.75分](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E7%AC%AC%E4%B8%89%E6%BB%9194.75%E5%88%86%23)（NewsNow热榜，匹配分=100，来源ID=NW01）
19. [bilibili 热搜 #1 | ​谷爱凌摘金](https://search.bilibili.com/all?keyword=%E2%80%8B%E8%B0%B7%E7%88%B1%E5%87%8C%E6%91%98%E9%87%91)（NewsNow热榜，匹配分=100，来源ID=NW02）
20. [百度热搜 #1 | 第5金！谷爱凌夺冠](https://www.baidu.com/s?wd=%E7%AC%AC5%E9%87%91%EF%BC%81%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0)（NewsNow热榜，匹配分=100，来源ID=NW03）
21. [今日头条 #1 | 中国队5金4银6铜收官](https://www.toutiao.com/trending/7609123113803989035/)（NewsNow热榜，匹配分=100，来源ID=NW04）
22. [抖音 #1 | 谷爱凌李方慧包揽U池金银牌](https://www.douyin.com/hot/2408149)（NewsNow热榜，匹配分=100，来源ID=NW10）
23. [微博 #2 | 谷爱凌金牌](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E9%87%91%E7%89%8C%23)（NewsNow热榜，匹配分=100，来源ID=NW12）
24. [百度热搜 #2 | 李方慧夺女子U型场地银牌](https://www.baidu.com/s?wd=%E6%9D%8E%E6%96%B9%E6%85%A7%E5%A4%BA%E5%A5%B3%E5%AD%90U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E9%93%B6%E7%89%8C)（NewsNow热榜，匹配分=100，来源ID=NW13）

## 🧪 引用匹配校验

- 已匹配引用条数: 24
- 未完成匹配标签: 1
- 未匹配示例: GH项目雷达分析
- 低置信引用条数: 0
- 处理建议: 本次未发现低置信引用。

## 🎯 投机方向（超短）

- 海外指数方向：美股 VIX波动率指数 -5.64%（高波动回撤）
- 商品波段方向：COMEX铜 +1.90%
- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。

## 🌐 联网检索补充

- 关键词：2026-02-22 全球市场 盘面 复盘 原因, 2026-02-22 中国 宏观 经济 政策 市场 影响, 2026-02-22 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, ETH 上涨 原因, 谷爱凌第三滑94.75分 事件 背景, ​谷爱凌摘金 事件 背景, 第5金！谷爱凌夺冠 事件 背景
- 命中结果：13 条（按发布时间倒序）

### 🔎 2026-02-22 AI 科技 行业 动态 影响

- [中美AI同步加速：47天30次更新，中国AI的最强主场究竟在哪？ - 新浪财经](https://news.google.com/rss/articles/CBMifEFVX3lxTE9wRTgwVjFlMGJFd0l1dU9acENZOVJ1NGdTVmRHcFVvMWF5UDZ0d3gyenlnYVJlTGhsZEl4aVJZQzJ4UXJ4QnRCZmxMOVhwUHNLbWlpSUFaLS1KOU54NUt6QUc3dkVfR3luWlVPZkl3a2pOeDROZjZ0SEpaTDA?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-22 18:31
  - 摘要: 中美AI同步加速：47天30次更新，中国AI的最强主场究竟在哪？ 新浪财经
- [详读 2 万 3 千字的新「AI 宪法」之后，我理解了 Anthropic 的痛苦 - news.17173.com](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5PbkUyNzRCMEU1d2J5TE1EdHpUenhWeGNZQ0s2eGdiTE9HX3lUeWpCMDlVenVJcUp5SGZzUVVTN19INW9fdUdBU1hSUndkRmtUOVVHRGhNbS1hQ0pEbFhwZUpqTE5QQQ?oc=5)
  - 来源: news.17173.com | 时间: 2026-02-22 16:03
  - 摘要: 详读 2 万 3 千字的新「AI 宪法」之后，我理解了 Anthropic 的痛苦 news.17173.com
- [恒生科技估值跌至低位，汇添富恒生科技ETF联接发起式(QDII)C(013128)捕捉AI叙事加持下估值修复红利 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTFBiSF9DZnBtTktNa25RTXZhdnB4V3lFOGRIME5aZWdpa182SVE5cFkwclQ1WEFSQXRHMnVEaUUtRUxlUEFXazFPd0tqRnViWFg1c0RyaWVtUWszZGtfRVJPZkFsVFhyNWV0d0R2Qlo1clNXSTFnNU1weA?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-22 14:09
  - 摘要: 恒生科技估值跌至低位，汇添富恒生科技ETF联接发起式(QDII)C(013128)捕捉AI叙事加持下估值修复红利 新浪财经
- [AI数据中心全球扩张浪潮下，农民坚守土地如何影响科技与农业的平衡发展？ - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMigwFBVV95cUxQU0l6RnpCTGZDby1QN1dmajlYa3RDUzhmUjJqZW5kM0FJWG1kSzdfODJWRl9lYUh4QzBOOUVjOXpXMjZrLUc0ZWtzcGF5NjFnY1BSd3M4cXJFSTRsN21YNTg1ajZYMHllRTFvLWZUVF8yQ3ZxMk9FbUswR1BQLU1STXotUQ?oc=5)
  - 来源: 新浪新闻_手机新浪网 | 时间: 2026-02-22 09:02
  - 摘要: AI数据中心全球扩张浪潮下，农民坚守土地如何影响科技与农业的平衡发展？ 新浪新闻_手机新浪网
- [“AI恐慌交易”仍未完全消散 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5vMV9jMnV2WDNEejRuNjUybFVWSkNKSGhLbk1MOGNwVk9PSWwzamdacjZacmFRSUMxSmpXNmcxRVIzRlU5dDBsSUdfSGEwMVcyQlFqR3JobmRlYlpiUkRfdA?oc=5)
  - 来源: thepaper.cn | 时间: 2026-02-22 08:19
  - 摘要: “AI恐慌交易”仍未完全消散 thepaper.cn
- [Intel、AMD新一代桌面CPU发布时间曝光！Nova Lake、Zen 6双双推迟到2027年 - 驱动之家](https://news.google.com/rss/articles/CBMiWEFVX3lxTFA0ZmVzMm5lUkFMQldxUk9EZzA0c2Q1WjVDNmRRZzZwbnhuMzdrYnFibjhLUndZRS1HOC01eUJkdGpZMndVcjFsOEVIWGM3b0pQTTJORlZsWUU?oc=5)
  - 来源: 驱动之家 | 时间: 2026-02-22 08:17
  - 摘要: Intel、AMD新一代桌面CPU发布时间曝光！Nova Lake、Zen 6双双推迟到2027年 驱动之家

### 🔎 2026-02-22 中国 宏观 经济 政策 市场 影响

- [【均已开售】2024 易博APP下载 - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9aclIxZjlJVUM4WlEtSkJCOHZFMTJtOGNRbFdZREZ1T0t1YklDRW9VMjdReldySFMzNF9FcDdJTkk4VHZ0SEw5QVdjSnBiYXl3NE1ySktaNA?oc=5)
  - 来源: 3DM | 时间: 2026-02-22 17:20
  - 摘要: 【均已开售】2024 易博APP下载 3DM
- [1月社融规模增速8.2% 降准降息仍待观察货币政策累计效应 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE94WG1Ba2dpOEVQTzBrUjVPODF2V2tPajlISHVMRnhRd1F2ekFGSkNlaTY1S0tmNUFuYldGZXFyRnRaWk43WU1OdU9peUZuM1lQOWZ6cVcxOVhiMlhqaWlCUm94Rk44Y2FYQzZCU2E4T3Nxb3BIazhxVQ?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-22 13:55
  - 摘要: 1月社融规模增速8.2% 降准降息仍待观察货币政策累计效应 新浪财经
- [井友倫：如何解讀最高院關稅裁決的影響 - 大紀元新聞網](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9FSlVZQjk4RWpIQUNocmJTcG42a2M0RXRMSzRaSEJsVmVvcVJfVHFDZm9TeG5sbU4xMzl0WGdmSkZYY0dsQW9BUXNHZWNBT0RHX25zNUNfb3h0ZnFGQ1RnakZIRlVKd9IBZkFVX3lxTE9FSlVZQjk4RWpIQUNocmJTcG42a2M0RXRMSzRaSEJsVmVvcVJfVHFDZm9TeG5sbU4xMzl0WGdmSkZYY0dsQW9BUXNHZWNBT0RHX25zNUNfb3h0ZnFGQ1RnakZIRlVKdw?oc=5)
  - 来源: 大紀元新聞網 | 时间: 2026-02-22 13:11
  - 摘要: 井友倫：如何解讀最高院關稅裁決的影響 大紀元新聞網
- [回归“小央行”：美联储“沃什时代”前瞻_宏观研究_研报 - 证券之星](https://news.google.com/rss/articles/CBMiYkFVX3lxTE8wWV84MlRNUklJNGJBbmlvWEhPWE9RWE5Pc0NXZXBLc21ERl9wZmF6LWlNZ1g3LTJRc2xZUEViZi0wUjVydGZwQnhuZmRGWGdZQ1d0X0lWUkJYWDRsTUJuYUFR?oc=5)
  - 来源: 证券之星 | 时间: 2026-02-22 10:30
  - 摘要: 回归“小央行”：美联储“沃什时代”前瞻_宏观研究_研报 证券之星
- [乘势而上｜专访张晓晶：引导政府部门存量财富向居民部门适度转移 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTFAzUjREV1kySDZiaThkdVNCMUdtOWEwaDdIMFN4aGdsczIwenpMekIxODExQmUxMXlSRkYtWjZ3ZlBnMGhfMFUxOHBiSE90Ni1RMy13cDRuYjFlSkdvM2hSSg?oc=5)
  - 来源: thepaper.cn | 时间: 2026-02-22 09:10
  - 摘要: 乘势而上｜专访张晓晶：引导政府部门存量财富向居民部门适度转移 thepaper.cn
- [国际AG|联合多国艺术家打造和平主题艺术展 - 游侠网](https://news.google.com/rss/articles/CBMiSkFVX3lxTE1yLUZkYXdXNXFiS3NiUThLNGI5UXJXbER3YXl3Q244UkpYSW91cEg0aHlHUjZxazBxcDNQaGQ2UmdqTTRqOVRTbWVB?oc=5)
  - 来源: 游侠网 | 时间: 2026-02-22 04:27
  - 摘要: 国际AG|联合多国艺术家打造和平主题艺术展 游侠网

### 🔎 VIX波动率指数 下跌 原因

- [第一热点 澳门新葡新京网站 - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTFBUdS1LYWlzcDVUQUIzUHR6S0dHSmtIY1FHandITld0NmtCVDBLdEVKNDZOclBhNHA5My16MUdfYXBFNGQ5LUFFUkpSWEZBV2tuZzA5V0xVYw?oc=5)
  - 来源: 3DM | 时间: 2026-02-22 09:48
  - 摘要: 第一热点 澳门新葡新京网站 3DM

## 🔗 AI 分析引用来源

> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。

### Twitter (9 条)

- [¹] [2026-02-22T12:00 @GarageGuyChase | It’s so cool to hate AI](https://twitter.com/GarageGuyChase/status/2025255625815376033)（匹配分=100，来源ID=TW01）
- [²] [2026-02-22T12:00 @KietaJibun | こうやってAIに画像を作らせることも出来た、でも手作りの方が面白くなると思ったから30分くらいかけてコラ画像を作ったんだ](https://twitter.com/KietaJibun/status/2025459434517135581)（匹配分=100，来源ID=TW10）
- [³] [2026-02-22T12:00 @insidefolkative | "Siapin dana darurat makanya". In this economy semuanya darurat bjirr 😭😭😭😭😭😭😭😭](https://twitter.com/insidefolkative/status/2025192508901429626)（匹配分=100，来源ID=TW05）
- [⁴] [2026-02-22T12:00 @psvit | สิ่งนี้คือ Lifestyle Inflation ซึ่งเดี๋ยวนี้เกิดตั้งแต่เด็ก เพราะตามพ่อแม่มา ซูชิโระทุกอ...](https://twitter.com/psvit/status/2025419843554681018)（匹配分=100，来源ID=TW11）
- [⁵] [2026-02-22T12:00 @TheMuslim786 | Location: Badaun,UP "Get out of the village, you're jihadis, you're Katuas," Akshay Sing...](https://twitter.com/TheMuslim786/status/2025251859762680206)（匹配分=100，来源ID=TW04）
- [⁶] [2026-02-22T12:00 @Jvnior | Israeli jews are: - serial liars - baby killers - minor lovers - skin stealers - sex tra...](https://twitter.com/Jvnior/status/2025192295264334093)（匹配分=100，来源ID=TW08）
- [⁷] [2026-02-22T12:00 @Urhobo_Mudiaga | Stop complaining and nagging every single day, about elections, the system, the economy,...](https://twitter.com/Urhobo_Mudiaga/status/2025465798899155327)（匹配分=100，来源ID=TW12）
- [⁸] [2026-02-22T12:00 @binance | From Bitcoin to altcoins, explore 550+ tokens and trade easily on Binance starting with ...](https://twitter.com/binance/status/2013965079512076296)（匹配分=100，来源ID=TW09）
- [⁹] [2026-02-22T12:00 @raghav_chadha | In the 20th century, power depended on OIL and STEEL. In the 21st century, power depends...](https://twitter.com/raghav_chadha/status/2023632195148280168)（匹配分=100，来源ID=TW14）

### NewsNow热榜 (11 条)

- [¹⁰] [华尔街见闻 #1 | 特朗普新加征关税税率加码至15% 美政府“越权”关税引企业诉讼潮](https://wallstreetcn.com/articles/3765942)（匹配分=100，来源ID=NW05）
- [¹¹] [财联社热门 #1 | 特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405)（匹配分=100，来源ID=NW11）
- [¹²] [凤凰网 #2 | 美国前商务部长：其他关税方案，都会削弱特朗普对华谈判筹码](https://news.ifeng.com/c/8qxAuTEgS6q)（匹配分=100，来源ID=NW14）
- [¹⁴] [知乎 #1 | 如何看待当所有国产大模型都在 2026 春节撒钱抢用户时，DeepSeek 却默不作声继续奋战？](https://www.zhihu.com/question/2004982651719812885)（匹配分=100，来源ID=NW07）
- [¹⁸] [微博 #1 | 谷爱凌第三滑94.75分](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E7%AC%AC%E4%B8%89%E6%BB%9194.75%E5%88%86%23)（匹配分=100，来源ID=NW01）
- [¹⁹] [bilibili 热搜 #1 | ​谷爱凌摘金](https://search.bilibili.com/all?keyword=%E2%80%8B%E8%B0%B7%E7%88%B1%E5%87%8C%E6%91%98%E9%87%91)（匹配分=100，来源ID=NW02）
- [²⁰] [百度热搜 #1 | 第5金！谷爱凌夺冠](https://www.baidu.com/s?wd=%E7%AC%AC5%E9%87%91%EF%BC%81%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0)（匹配分=100，来源ID=NW03）
- [²¹] [今日头条 #1 | 中国队5金4银6铜收官](https://www.toutiao.com/trending/7609123113803989035/)（匹配分=100，来源ID=NW04）
- [²²] [抖音 #1 | 谷爱凌李方慧包揽U池金银牌](https://www.douyin.com/hot/2408149)（匹配分=100，来源ID=NW10）
- [²³] [微博 #2 | 谷爱凌金牌](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E9%87%91%E7%89%8C%23)（匹配分=100，来源ID=NW12）
- [²⁴] [百度热搜 #2 | 李方慧夺女子U型场地银牌](https://www.baidu.com/s?wd=%E6%9D%8E%E6%96%B9%E6%85%A7%E5%A4%BA%E5%A5%B3%E5%AD%90U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E9%93%B6%E7%89%8C)（匹配分=100，来源ID=NW13）

### 联网检索 (4 条)

- [¹³] [2026-02-22 13:55 新浪财经 | 1月社融规模增速8.2% 降准降息仍待观察货币政策累计效应 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE94WG1Ba2dpOEVQTzBrUjVPODF2V2tPajlISHVMRnhRd1F2ekFGSkNlaTY1S0tmNUFuYldGZXFyRnRaWk43WU1OdU9peUZuM1lQOWZ6cVcxOVhiMlhqaWlCUm94Rk44Y2FYQzZCU2E4T3Nxb3BIazhxVQ?oc=5)（匹配分=100，来源ID=WB13）
- [¹⁵] [2026-02-22 08:19 thepaper.cn | “AI恐慌交易”仍未完全消散 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5vMV9jMnV2WDNEejRuNjUybFVWSkNKSGhLbk1MOGNwVk9PSWwzamdacjZacmFRSUMxSmpXNmcxRVIzRlU5dDBsSUdfSGEwMVcyQlFqR3JobmRlYlpiUkRfdA?oc=5)（匹配分=100，来源ID=WB10）
- [¹⁶] [2026-02-22 09:02 新浪新闻_手机新浪网 | AI数据中心全球扩张浪潮下，农民坚守土地如何影响科技与农业的平衡发展？ - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMigwFBVV95cUxQU0l6RnpCTGZDby1QN1dmajlYa3RDUzhmUjJqZW5kM0FJWG1kSzdfODJWRl9lYUh4QzBOOUVjOXpXMjZrLUc0ZWtzcGF5NjFnY1BSd3M4cXJFSTRsN21YNTg1ajZYMHllRTFvLWZUVF8yQ3ZxMk9FbUswR1BQLU1STXotUQ?oc=5)（匹配分=100，来源ID=WB12）
- [¹⁷] [2026-02-22 08:17 驱动之家 | Intel、AMD新一代桌面CPU发布时间曝光！Nova Lake、Zen 6双双推迟到2027年 - 驱动之家](https://news.google.com/rss/articles/CBMiWEFVX3lxTFA0ZmVzMm5lUkFMQldxUk9EZzA0c2Q1WjVDNmRRZzZwbnhuMzdrYnFibjhLUndZRS1HOC01eUJkdGpZMndVcjFsOEVIWGM3b0pQTTJORlZsWUU?oc=5)（匹配分=100，来源ID=WB11）


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
| BTC | $68,190.00 | 🟢 +0.16% |
| ETH | $1,980.06 | 🟢 +0.17% |
| SOL | $85.23 | 🔴 -0.12% |

### 📈 国际期货

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|
| WTI原油 | 66.48 | 🟢 +0.08% |
| 布伦特原油 | 71.3 | 🔴 -0.50% |
| 天然气 | 2.98 | 🔴 -0.40% |
| COMEX铜 | 5.84 | 🟢 +1.90% |

### 💻 GitHub 趋势

- ⭐ [**visual-explainer**](https://github.com/nicobailon/visual-explainer) (2292 stars)
  - Agent skill + prompt templates that generate rich HTML pages for visual diff rev
- ⭐ [**nullclaw**](https://github.com/nullclaw/nullclaw) (1629 stars)
  - Fastest, smallest, and fully autonomous AI assistant infrastructure written in Z
- ⭐ [**BarraCUDA**](https://github.com/Zaneham/BarraCUDA) (1292 stars)
  - Open-source CUDA compiler targeting AMD GPUs (and more in the future!). Compiles
- ⭐ [**OpenPlanter**](https://github.com/ShinMegamiBoson/OpenPlanter) (863 stars)
- ⭐ [**ai-engineer-handbook**](https://github.com/DataExpert-io/ai-engineer-handbook) (782 stars)
  - All the links, books, and creators you need to follow to stay up to date with AI

## 🐦 Twitter 热点 (52 条)

- 来源统计: 关注账号 170 条 | 热门讨论 30 条

### 🔥 热门讨论推文

- `2026-02-22T12:00` @GarageGuyChase ❤️37165 🔁2188 💬31
  - It’s so cool to hate AI
  - [原文链接](https://twitter.com/GarageGuyChase/status/2025255625815376033)
- `2026-02-22T12:00` @elonmusk ❤️18414 🔁2208 💬1301
  - Yes
  - [原文链接](https://twitter.com/elonmusk/status/2024819025298235611)
- `2026-02-22T12:00` @ClaireGeronimii ❤️9341 🔁1198 💬475
  - J’ai le plaisir de vous annoncer ma candidature aux municipales les 15 et 22 mars prochains dans la ville de Saint-Quentin !   Au plaisir de vous rencontrer et de pouvoir échanger avec vous !
  - [原文链接](https://twitter.com/ClaireGeronimii/status/2025201582590025974)
- `2026-02-22T12:00` @TheMuslim786 ❤️4834 🔁2239 💬170
  - Location: Badaun,UP  "Get out of the village, you're jihadis, you're Katuas," Akshay Singh said, starting to beat them. The victim, Abdul Salam, said, "We had gone to collect donations for the madrasa."  Please note this attack was carried out based on religious identity.
  - [原文链接](https://twitter.com/TheMuslim786/status/2025251859762680206)
- `2026-02-22T12:00` @insidefolkative ❤️5967 🔁1167 💬55
  - "Siapin dana darurat makanya". In this economy semuanya darurat bjirr 😭😭😭😭😭😭😭😭
  - [原文链接](https://twitter.com/insidefolkative/status/2025192508901429626)
- `2026-02-22T12:00` @lebscit ❤️5786 🔁252 💬41
  - por causa de um hat-trick no vitória, disseram que o pedro era melhor que esse mano aí
  - [原文链接](https://twitter.com/lebscit/status/2025326348202278958)
- `2026-02-22T12:00` @Mattpetti32 ❤️3478 🔁1392 💬424
  - - Trump didn't legalize deadly drugs like Fentanyl - Trump didn't flood Canada with millions of immigrants - Trump didn't cause massive food inflation  - Trump didn't cause us to into recession - Trump didn't try to introduce draconian censorship bills - Trump didn't cause our healthcare to go to shit - Trump didn't let Terrorists and Terrorist Sympathizers to run all over our country and burn our flag - Trump didn't let crime go out of control - Trump didn't cause the conditions for the tragedy
  - [原文链接](https://twitter.com/Mattpetti32/status/2025237089340555347)
- `2026-02-22T12:00` @Jvnior ❤️3538 🔁846 💬174
  - Israeli jews are:  - serial liars - baby killers - minor lovers - skin stealers - sex traffickers - organ harvesters - home destroyers - enemies of Islam - satanic genociders - disbelievers of Jesus - diaper wearing terrorists  What else did I miss?
  - [原文链接](https://twitter.com/Jvnior/status/2025192295264334093)
- `2026-02-22T12:00` @binance ❤️3605 🔁308 💬87
  - From Bitcoin to altcoins, explore 550+ tokens and trade easily on Binance starting with just $10
  - [原文链接](https://twitter.com/binance/status/2013965079512076296)
- `2026-02-22T12:00` @KietaJibun ❤️3093 🔁156 💬20
  - こうやってAIに画像を作らせることも出来た、でも手作りの方が面白くなると思ったから30分くらいかけてコラ画像を作ったんだ
  - [原文链接](https://twitter.com/KietaJibun/status/2025459434517135581)
- `2026-02-22T12:00` @psvit ❤️877 🔁1531 💬10
  - สิ่งนี้คือ Lifestyle Inflation ซึ่งเดี๋ยวนี้เกิดตั้งแต่เด็ก เพราะตามพ่อแม่มา  ซูชิโระทุกอาทิตย์ หรือถ้าเป็นทางผ่านหลักเลิกเรียนได้มีกินบ่อยกว่านั้น ซูชิตลาดนัด ซูชิราคาถูกกินไม่ได้แล้ว ข้าวแข็ง ไม่อร่อย  สมัยก่อนเราก็กินเค้กร่วนๆ ขนมไทยหวานๆ 5 บาท 10 บาทอร่อยๆ แต่เดี๋ยวนี้ก็กินไม่ได้แล้ว
  - [原文链接](https://twitter.com/psvit/status/2025419843554681018)
- `2026-02-22T12:00` @Urhobo_Mudiaga ❤️1246 🔁540 💬100
  - Stop complaining and nagging every single day, about elections, the system, the economy, religion and so forth.  COME OUT AND LETS KiLL THEM ALL.  Without KiLLING THEM, THIS COUNTRY WILL NEVER BE BETTER, WE MUST CLEANSE THE LAND OFF THESE ANIMALS.
  - [原文链接](https://twitter.com/Urhobo_Mudiaga/status/2025465798899155327)
- `2026-02-22T12:00` @un1versalist ❤️1621 🔁126 💬101
  - People basically found out aliens were real yesterday.   Stock market went up  No one freaked out   Everyone went to work   It was a normal day  Just make the announcement, we're ready.#ufoX
  - [原文链接](https://twitter.com/un1versalist/status/2024999111833841889)
- `2026-02-22T12:00` @raghav_chadha ❤️1406 🔁269 💬90
  - In the 20th century, power depended on OIL and STEEL. In the 21st century, power depends on AI, CHIPS and COMPUTE CAPABILITY.  At AI Summit 2026 India, I spoke about why the GPU challenge is not just a ‘supply chain issue’ but a ‘sovereignty issue’.  In the AI century, power will rest with those who control chips, compute capacity and data centres.  Today, design monopolies, manufacturing concentration and export controls determine who gets access. India controls none of these critical levers.  
  - [原文链接](https://twitter.com/raghav_chadha/status/2023632195148280168)
- `2026-02-22T12:00` @cryptorover ❤️1367 🔁158 💬202
  - BULLISH: 🇺🇸 President Trump predicts the US stock market will double by the end of his term.
  - [原文链接](https://twitter.com/cryptorover/status/2025370435727003782)
- `2026-02-22T12:00` @TomolaGroup ❤️1023 🔁481 💬69
  - THE NIGERIAN STOCK MARKET — A Complete Beginner’s Guide  I’ve been getting tons of DMs asking how to start investing in Nigerian stocks.  So I put together the most detailed thread you’ll ever read on this topic.  Bookmark this. Share it. Your future self will thank you. 🧵👇
  - [原文链接](https://twitter.com/TomolaGroup/status/2025139638659060042)
- `2026-02-22T12:00` @spectatorindex ❤️1028 🔁94 💬71
  - NVIDIA market value  1st of January, 2024: $1.22 trillion  Now: $4.63 trillion
  - [原文链接](https://twitter.com/spectatorindex/status/2025254194605948955)
- `2026-02-22T12:00` @gakeau ❤️886 🔁263 💬3
  - あとAIは死ぬほど電力を喰うのでエネルギー資源をそこまで割くべきなのかというのも大問題で、つまり日常的に「便利道具」として使えるカジュアルさと見えないデメリットや搾取構造のギャップがすごい。
  - [原文链接](https://twitter.com/gakeau/status/2025441363190501784)
- `2026-02-22T12:00` @rindochihaya ❤️634 🔁180 💬60
  - 🎧配信告知  このあと22:00 START  【デヴィエーション・ゲーム】  FGでAIにばれないようにお絵描きするゾ！！！！piped.video/live/zm6lxIXl-m8…@YouTubeより
  - [原文链接](https://twitter.com/rindochihaya/status/2025538234277835256)
- `2026-02-22T12:00` @TheQuint ❤️546 🔁258 💬9
  - Nargis was pregnant when Delhi riots took away her husband, Mursaleen. Nargis gave birth to a fragile baby, one who was later adopted by Mursaleen’s brother so the baby could have a father figure.  Exactly six years ago, 21 February 2020, Mursaleen left for work and then he was killed in the pogrom. The Quint has also seen the post-mortem report which laid out details of the body. Nargis is among the 25 women who were widowed in the Delhi riots. For the worse, Nargis is now almost always fraught
  - [原文链接](https://twitter.com/TheQuint/status/2025196406571762024)

### @CoinDesk (4 条)

- `2026-02-22T11:51` New: http://localhost/VitalikButerin proposes AI “stewards” to vote on behalf of DAO users, using zero-knowledge proofs and secure MPC/TEE environments to protect identity and prevent coercion.
  - [原文链接](https://twitter.com/CoinDesk/status/2025539040108237253)
- `2026-02-22T10:29` Markets: http://localhost/search?q=%23XRP just logged its largest realized loss spike since Nov 2022, with $1.93B in weekly losses as holders capitulated, per http://localhost/santimentfeed.
  - [原文链接](https://twitter.com/CoinDesk/status/2025518421664755895)
- `2026-02-22T09:35` http://localhost/shauryamalwa reports:  https://www.coindesk.com/markets/2026/02/22/bitcoin-to-zero-searches-spike-in-the-u-s-but-the-bottom-signal-is-mixed
  - [原文链接](https://twitter.com/CoinDesk/status/2025504616784232779)
- `2026-02-22T09:18` Insight: U.S. Google searches for “Bitcoin to zero” just hit a record high as http://localhost/search?q=%23BTC slid toward $60K, a spike that previously aligned with local bottoms in 2021 and 2022.
  - [原文链接](https://twitter.com/CoinDesk/status/2025500474594545846)

### @BBCWorld (9 条)

- `2026-02-22T11:27` US ambassador's Israel comments condemned by Arab and Muslim nations https://bbc.in/40kcreC
  - [原文链接](https://twitter.com/BBCWorld/status/2025532800338690464)
- `2026-02-22T09:24` Teenage girl dies after hit-and-run collision https://bbc.in/4s43Ybm
  - [原文链接](https://twitter.com/BBCWorld/status/2025501893850472570)
- `2026-02-22T08:10` Pakistan launches strikes on Afghanistan, with Taliban saying dozens killed https://bbc.in/4saeCNX
  - [原文链接](https://twitter.com/BBCWorld/status/2025483393480151066)
- `2026-02-22T06:56` Could this be wreckage from a 214-year-old maritime disaster? https://bbc.in/4aM324v
  - [原文链接](https://twitter.com/BBCWorld/status/2025464812944134601)
- `2026-02-22T05:07` More than 1,500 Venezuelan political prisoners apply for amnesty https://bbc.in/4l89Qyd
  - [原文链接](https://twitter.com/BBCWorld/status/2025437360175862245)
- *... 及其他 4 条*

### @bindureddy (1 条)

- `2026-02-22T11:13` While Gemini 3.1 at least tries to compete with Opus 4.6….   OpenAI feels like it’s no longer in the arena   GPT 5.3 is long overdue - almost two whole weeks 😂
  - [原文链接](https://twitter.com/bindureddy/status/2025529429150278063)

### @CNBC (1 条)

- `2026-02-22T10:33` India delays Washington trade visit as U.S. tariff policy shifts, source tells CNBC https://www.cnbc.com/2026/02/22/trump-tariffs-india-trade-deal.html?taid=699adb618e21f400010da3de&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025519207765430414)

### @elonmusk (7 条)

- `2026-02-22T08:41` Try Grok Imagine. It keeps getting better.  DogeDesigner (@cb_doge)  BREAKING: xAI's Grok Imagine continues to rank #1 on Image to Video Leaderboard of Arena .AI beating Google VEO and others. 🥇  Download http://localhost/grok and try Imagine.  — http://localhost/cb_doge/status/2025490292963754296#m
  - [原文链接](https://twitter.com/elonmusk/status/2025491021073674549)
- `2026-02-22T08:39` Come a long way  X Freeze (@XFreeze)  How it started vs. how it’s going  — http://localhost/XFreeze/status/2025488621848191228#m
  - [原文链接](https://twitter.com/elonmusk/status/2025490500011089995)
- `2026-02-22T08:30` Grok Imagine keeps improving  Art Muse (@art_muse)  Happy Sunday!  Video  — http://localhost/art_muse/status/2025447627194544312#m
  - [原文链接](https://twitter.com/elonmusk/status/2025488230401937723)
- `2026-02-22T08:23` Grok understands jokes   https://nitter.net/i/grok/share/7f65e9dd3e7f42dcb81c5fb6496ec3cb
  - [原文链接](https://twitter.com/elonmusk/status/2025486491057541209)
- `2026-02-22T04:57` Starship = Hope
  - [原文链接](https://twitter.com/elonmusk/status/2025434732335677655)
- *... 及其他 2 条*

## 📱 微信公众号

暂无数据

## 🔥 NewsNow 热榜 (120 条)

### 微博

| 排名 | 标题 |
|------|------|
| #1 | [谷爱凌第三滑94.75分](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E7%AC%AC%E4%B8%89%E6%BB%9194.75%E5%88%86%23) |
| #2 | [谷爱凌金牌](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E9%87%91%E7%89%8C%23) |
| #3 | [热气腾腾的中国年](https://s.weibo.com/weibo?q=%23%E7%83%AD%E6%B0%94%E8%85%BE%E8%85%BE%E7%9A%84%E4%B8%AD%E5%9B%BD%E5%B9%B4%23) |
| #4 | [女子U型场地决赛](https://s.weibo.com/weibo?q=%23%E5%A5%B3%E5%AD%90U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E5%86%B3%E8%B5%9B%23) |
| #5 | [谷爱凌第二滑94.00分](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E7%AC%AC%E4%BA%8C%E6%BB%9194.00%E5%88%86%23) |
| #6 | [李方慧银牌](https://s.weibo.com/weibo?q=%E6%9D%8E%E6%96%B9%E6%85%A7%E9%93%B6%E7%89%8C) |
| #7 | [李方慧第二滑91.50分](https://s.weibo.com/weibo?q=%23%E6%9D%8E%E6%96%B9%E6%85%A7%E7%AC%AC%E4%BA%8C%E6%BB%9191.50%E5%88%86%23) |
| #8 | [谷爱凌李方慧拥抱](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E6%9D%8E%E6%96%B9%E6%85%A7%E6%8B%A5%E6%8A%B1%23) |
| #9 | [韩国队抗议米兰冬奥至少4次印错国旗](https://s.weibo.com/weibo?q=%E9%9F%A9%E5%9B%BD%E9%98%9F%E6%8A%97%E8%AE%AE%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E8%87%B3%E5%B0%914%E6%AC%A1%E5%8D%B0%E9%94%99%E5%9B%BD%E6%97%97) |
| #10 | [淀粉肠进入瑜伽裤时代](https://s.weibo.com/weibo?q=%E6%B7%80%E7%B2%89%E8%82%A0%E8%BF%9B%E5%85%A5%E7%91%9C%E4%BC%BD%E8%A3%A4%E6%97%B6%E4%BB%A3) |

### bilibili 热搜

| 排名 | 标题 |
|------|------|
| #1 | [​谷爱凌摘金](https://search.bilibili.com/all?keyword=%E2%80%8B%E8%B0%B7%E7%88%B1%E5%87%8C%E6%91%98%E9%87%91) |
| #2 | [虹猫蓝兔七侠传4K修复版定档](https://search.bilibili.com/all?keyword=%E8%99%B9%E7%8C%AB%E8%93%9D%E5%85%94%E4%B8%83%E4%BE%A0%E4%BC%A04K%E4%BF%AE%E5%A4%8D%E7%89%88%E5%AE%9A%E6%A1%A3) |
| #3 | [解读特朗普提高全球进口关税](https://search.bilibili.com/all?keyword=%E8%A7%A3%E8%AF%BB%E7%89%B9%E6%9C%97%E6%99%AE%E6%8F%90%E9%AB%98%E5%85%A8%E7%90%83%E8%BF%9B%E5%8F%A3%E5%85%B3%E7%A8%8E) |
| #4 | [李方慧斩获银牌](https://search.bilibili.com/all?keyword=%E6%9D%8E%E6%96%B9%E6%85%A7%E6%96%A9%E8%8E%B7%E9%93%B6%E7%89%8C) |
| #5 | [挑战去第一财神庙刮彩票](https://search.bilibili.com/all?keyword=%E6%8C%91%E6%88%98%E5%8E%BB%E7%AC%AC%E4%B8%80%E8%B4%A2%E7%A5%9E%E5%BA%99%E5%88%AE%E5%BD%A9%E7%A5%A8) |
| #6 | [中华野兽先生](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%8D%8E%E9%87%8E%E5%85%BD%E5%85%88%E7%94%9F) |
| #7 | [史蒂夫速通狗熊岭](https://search.bilibili.com/all?keyword=%E5%8F%B2%E8%92%82%E5%A4%AB%E9%80%9F%E9%80%9A%E7%8B%97%E7%86%8A%E5%B2%AD) |
| #8 | [熊人修仙传](https://search.bilibili.com/all?keyword=%E7%86%8A%E4%BA%BA%E4%BF%AE%E4%BB%99%E4%BC%A0) |
| #9 | [拜年小技巧](https://search.bilibili.com/all?keyword=%E6%8B%9C%E5%B9%B4%E5%B0%8F%E6%8A%80%E5%B7%A7) |
| #10 | [原神同人新春会](https://search.bilibili.com/all?keyword=%E5%8E%9F%E7%A5%9E%E5%90%8C%E4%BA%BA%E6%96%B0%E6%98%A5%E4%BC%9A) |

### 百度热搜

| 排名 | 标题 |
|------|------|
| #1 | [第5金！谷爱凌夺冠](https://www.baidu.com/s?wd=%E7%AC%AC5%E9%87%91%EF%BC%81%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0) |
| #2 | [李方慧夺女子U型场地银牌](https://www.baidu.com/s?wd=%E6%9D%8E%E6%96%B9%E6%85%A7%E5%A4%BA%E5%A5%B3%E5%AD%90U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E9%93%B6%E7%89%8C) |
| #3 | [春运返程这些准备要做好](https://www.baidu.com/s?wd=%E6%98%A5%E8%BF%90%E8%BF%94%E7%A8%8B%E8%BF%99%E4%BA%9B%E5%87%86%E5%A4%87%E8%A6%81%E5%81%9A%E5%A5%BD) |
| #4 | [谷爱凌U池第二滑94.00分](https://www.baidu.com/s?wd=%E8%B0%B7%E7%88%B1%E5%87%8CU%E6%B1%A0%E7%AC%AC%E4%BA%8C%E6%BB%9194.00%E5%88%86) |
| #5 | [远嫁姐姐回家 47岁弟弟激动得像孩子](https://www.baidu.com/s?wd=%E8%BF%9C%E5%AB%81%E5%A7%90%E5%A7%90%E5%9B%9E%E5%AE%B6+47%E5%B2%81%E5%BC%9F%E5%BC%9F%E6%BF%80%E5%8A%A8%E5%BE%97%E5%83%8F%E5%AD%A9%E5%AD%90) |
| #6 | [给妈妈的红包被放回 女儿打开后破防](https://www.baidu.com/s?wd=%E7%BB%99%E5%A6%88%E5%A6%88%E7%9A%84%E7%BA%A2%E5%8C%85%E8%A2%AB%E6%94%BE%E5%9B%9E+%E5%A5%B3%E5%84%BF%E6%89%93%E5%BC%80%E5%90%8E%E7%A0%B4%E9%98%B2) |
| #7 | [“银发留学”正在悄然兴起](https://www.baidu.com/s?wd=%E2%80%9C%E9%93%B6%E5%8F%91%E7%95%99%E5%AD%A6%E2%80%9D%E6%AD%A3%E5%9C%A8%E6%82%84%E7%84%B6%E5%85%B4%E8%B5%B7) |
| #8 | [彩民随手扔掉千万彩票2天才发现](https://www.baidu.com/s?wd=%E5%BD%A9%E6%B0%91%E9%9A%8F%E6%89%8B%E6%89%94%E6%8E%89%E5%8D%83%E4%B8%87%E5%BD%A9%E7%A5%A82%E5%A4%A9%E6%89%8D%E5%8F%91%E7%8E%B0) |
| #9 | [男子晒监控：春节像做了一场热闹的梦](https://www.baidu.com/s?wd=%E7%94%B7%E5%AD%90%E6%99%92%E7%9B%91%E6%8E%A7%EF%BC%9A%E6%98%A5%E8%8A%82%E5%83%8F%E5%81%9A%E4%BA%86%E4%B8%80%E5%9C%BA%E7%83%AD%E9%97%B9%E7%9A%84%E6%A2%A6) |
| #10 | [谷爱凌领衔4朵金花U型场地决赛冲金](https://www.baidu.com/s?wd=%E8%B0%B7%E7%88%B1%E5%87%8C%E9%A2%86%E8%A1%944%E6%9C%B5%E9%87%91%E8%8A%B1U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E5%86%B3%E8%B5%9B%E5%86%B2%E9%87%91) |

### 今日头条

| 排名 | 标题 |
|------|------|
| #1 | [中国队5金4银6铜收官](https://www.toutiao.com/trending/7609123113803989035/) |
| #2 | [谷爱凌金牌！中国队包揽女子U型池金银](https://www.toutiao.com/trending/7609098288788176937/) |
| #3 | [各地活动精彩纷呈 喜气洋洋庆新春](https://www.toutiao.com/trending/7609591683432631818/) |
| #4 | [河南矿山客户排队交钱：大厅挤满人](https://www.toutiao.com/trending/7608838132696563731/) |
| #5 | [《新闻联播》正在直播](https://www.toutiao.com/trending/7609640843644882478/) |
| #6 | [老人带茅台乘火车被拦欲当场喝完](https://www.toutiao.com/trending/7609283906038399018/) |
| #7 | [河南矿山女销售去年签约4个亿](https://www.toutiao.com/trending/7609117198203748393/) |
| #8 | [父亲屋外透气看见儿子坠楼接住](https://www.toutiao.com/trending/7609292140770328582/) |
| #9 | [年轻人过年把洗浴中心玩成性价比酒店](https://www.toutiao.com/trending/7608593086784094218/) |
| #10 | [犯困小狗跟主人过年返程表情可爱](https://www.toutiao.com/trending/7608962917555798042/) |

### 华尔街见闻

| 排名 | 标题 |
|------|------|
| #1 | [特朗普新加征关税税率加码至15% 美政府“越权”关税引企业诉讼潮](https://wallstreetcn.com/articles/3765942) |
| #2 | [大摩评价MiniMax“全球顶尖基座模型稀缺资产”，高估值核心逻辑在于“技术决定天花板、全球化决定估值”](https://wallstreetcn.com/articles/3765947) |
| #3 | [玉渊谭天：美国对华哪些关税被停止征收？](https://wallstreetcn.com/articles/3765953) |
| #4 | [春节期间，国内外都发生了什么？](https://wallstreetcn.com/articles/3765956) |
| #5 | [过去30年来未见之局面！美股指数波动之小创1960年来之最，而个股波动率却高达指数7倍](https://wallstreetcn.com/articles/3765941) |
| #6 | [欢迎来到AI智能体新时代：未来不是“为人创造”，而是“为AI服务”](https://wallstreetcn.com/articles/3765948) |
| #7 | [表面风光之下，OpenAI的“四大困境”](https://wallstreetcn.com/articles/3765945) |
| #8 | [SK会长崔泰源警告：AI正在吞噬一切，今年千亿美元利润或瞬间变巨亏](https://wallstreetcn.com/articles/3765949) |
| #9 | [地热——一场静悄悄的美国能源变革](https://wallstreetcn.com/articles/3765952) |
| #10 | [比净值低20-35%！对冲基金报价收购Blue Owl旗下基金份额，加剧市场对PE的质疑](https://wallstreetcn.com/articles/3765939) |

### 贴吧

| 排名 | 标题 |
|------|------|
| #1 | [撤诉!初中生扶老人被讹22w](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%92%A4%E8%AF%89%21%E5%88%9D%E4%B8%AD%E7%94%9F%E6%89%B6%E8%80%81%E4%BA%BA%E8%A2%AB%E8%AE%B922w&topic_id=28350844) |
| #2 | [洗脚闹矛盾,男子跳桥失联](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B4%97%E8%84%9A%E9%97%B9%E7%9F%9B%E7%9B%BE%2C%E7%94%B7%E5%AD%90%E8%B7%B3%E6%A1%A5%E5%A4%B1%E8%81%94&topic_id=28350857) |
| #3 | [法外狂徒!罗翔帮黑老大减刑](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B3%95%E5%A4%96%E7%8B%82%E5%BE%92%21%E7%BD%97%E7%BF%94%E5%B8%AE%E9%BB%91%E8%80%81%E5%A4%A7%E5%87%8F%E5%88%91&topic_id=28350855) |
| #4 | [撞破妻子出轨,丈夫报警告性侵](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%92%9E%E7%A0%B4%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8%2C%E4%B8%88%E5%A4%AB%E6%8A%A5%E8%AD%A6%E5%91%8A%E6%80%A7%E4%BE%B5&topic_id=28350840) |
| #5 | [麦当劳作死,联动柜子学院](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%BA%A6%E5%BD%93%E5%8A%B3%E4%BD%9C%E6%AD%BB%2C%E8%81%94%E5%8A%A8%E6%9F%9C%E5%AD%90%E5%AD%A6%E9%99%A2&topic_id=28350849) |
| #6 | [钓帝去世,钓鱼圈传奇落幕](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%92%93%E5%B8%9D%E5%8E%BB%E4%B8%96%2C%E9%92%93%E9%B1%BC%E5%9C%88%E4%BC%A0%E5%A5%87%E8%90%BD%E5%B9%95&topic_id=28350858) |
| #7 | [小国作妖,春节译名之争再起](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%B0%8F%E5%9B%BD%E4%BD%9C%E5%A6%96%2C%E6%98%A5%E8%8A%82%E8%AF%91%E5%90%8D%E4%B9%8B%E4%BA%89%E5%86%8D%E8%B5%B7&topic_id=28350853) |
| #8 | [亲爹抛妻弃子,命丧俄乌战场](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E7%88%B9%E6%8A%9B%E5%A6%BB%E5%BC%83%E5%AD%90%2C%E5%91%BD%E4%B8%A7%E4%BF%84%E4%B9%8C%E6%88%98%E5%9C%BA&topic_id=28350847) |
| #9 | [飞碟社官宣,原神动画稳了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%A3%9E%E7%A2%9F%E7%A4%BE%E5%AE%98%E5%AE%A3%2C%E5%8E%9F%E7%A5%9E%E5%8A%A8%E7%94%BB%E7%A8%B3%E4%BA%86&topic_id=28350851) |
| #10 | [喂猫起争执,男子遭恶邻杀害](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%96%82%E7%8C%AB%E8%B5%B7%E4%BA%89%E6%89%A7%2C%E7%94%B7%E5%AD%90%E9%81%AD%E6%81%B6%E9%82%BB%E6%9D%80%E5%AE%B3&topic_id=28350838) |

### 知乎

| 排名 | 标题 |
|------|------|
| #1 | [如何看待当所有国产大模型都在 2026 春节撒钱抢用户时，DeepSeek 却默不作声继续奋战？](https://www.zhihu.com/question/2004982651719812885) |
| #2 | [韩延哽咽恳求多给《星河入梦》有效排片，这部投资近四亿的电影为何面临排片困境？](https://www.zhihu.com/question/2008647492124827724) |
| #3 | [今年大年初一给我的直属领导发了一条祝福微信，但是领导一直没有回我，这是为什么？](https://www.zhihu.com/question/2007378989140952602) |
| #4 | [贵州非遗传承人半年卖 800 只「点翠蟑螂」，如何理解这种反差美学？若人人喊打的蟑螂变好看了，你能接受吗？](https://www.zhihu.com/question/2007528287103051494) |
| #5 | [舅舅送外甥女 30 斤银砖当压岁钱，家长因为礼物贵重主动归还，如何看待双方的举动？](https://www.zhihu.com/question/2008606498859742105) |
| #6 | [米兰冬奥自由式滑雪女子 U 型场地技巧决赛，谷爱凌卫冕，李方慧摘银，如何评价他们的发挥？](https://www.zhihu.com/question/2008677675422672634) |
| #7 | [长辈说「饿一饿更长寿」，春节少吃一顿真的养生吗，空腹有哪些风险？](https://www.zhihu.com/question/2005954269753390531) |
| #8 | [看完《飞驰人生 3》好多人喜欢叶经理，你如何评价这个人物？](https://www.zhihu.com/question/2008127511381370827) |
| #9 | [妈祖文化中的掷圣杯是一种怎样的仪式？各种落法有哪些寓意？](https://www.zhihu.com/question/2008542148102943240) |
| #10 | [晚上九点想让男朋友开车送妈妈回家，男朋友拒绝后我一直很伤心，我是不是太自私了，该怎么改变自己的想法？](https://www.zhihu.com/question/2008483127039902430) |

### 凤凰网

| 排名 | 标题 |
|------|------|
| #1 | [特朗普的报复来了](https://news.ifeng.com/c/8qwaojRoDP6) |
| #2 | [美国前商务部长：其他关税方案，都会削弱特朗普对华谈判筹码](https://news.ifeng.com/c/8qxAuTEgS6q) |
| #3 | [特朗普新加征关税加码至15%](https://news.ifeng.com/c/8qwaojRoDKf) |
| #4 | [欧盟、英国、加拿大、墨西哥、德国，最新发声](https://news.ifeng.com/c/8qwaojRoDGX) |
| #5 | [一顿中餐掀翻秘鲁政坛，美国在背后做了什么？](https://news.ifeng.com/c/8qxLW2rbfUZ) |
| #6 | [12天72只老虎集中死亡，泰国官方通报](https://v.ifeng.com/c/8qx23a92Pwn) |
| #7 | [“以色列拿下整个中东也没问题”？沙特等14国强烈谴责](https://news.ifeng.com/c/8qwiW7aAKXh) |
| #8 | [乌克兰制裁俄罗斯“影子舰队”](https://news.ifeng.com/c/8qwipyWWgXr) |
| #9 | [韩国外交部强烈抗议日本举行“竹岛日”活动](https://news.ifeng.com/c/8qx0g6BhHN6) |
| #10 | [破开冰面潜水打捞，俄寻回所有坠湖溺亡的中国游客遗体](https://news.ifeng.com/c/8qxA3o3RFZg) |

### 澎湃新闻

| 排名 | 标题 |
|------|------|
| #1 | [过年的9个晚上｜为什么我们总是怀念儿时的年](https://www.thepaper.cn/newsDetail_forward_32599785) |
| #2 | [四川广元法院春节执行攻坚专项行动：一日拘传38名“老赖”](https://www.thepaper.cn/newsDetail_forward_32639463) |
| #3 | [春启新程｜春节里一家亮灯的“烟火小馆”，迎来不少来沪游客](https://www.thepaper.cn/newsDetail_forward_32639299) |
| #4 | [新春走基层·见喜｜重新学会跟长辈相处](https://www.thepaper.cn/newsDetail_forward_32639761) |
| #5 | [中东睿评｜美以与伊朗博弈的混沌状态只能靠战争才能打破吗？](https://www.thepaper.cn/newsDetail_forward_32639434) |
| #6 | [这个春节，上海何以成为热门目的地？](https://www.thepaper.cn/newsDetail_forward_32639992) |
| #7 | [阿根廷田野手记：关停的工厂、变贵的账单与华商的新生意｜907编辑部](https://www.thepaper.cn/newsDetail_forward_32638732) |
| #8 | [持续放风试探，美官员称或对伊朗发动针对特定个人的军事打击](https://www.thepaper.cn/newsDetail_forward_32641921) |
| #9 | [暴雪大风沙尘大范围降雨上线，北方气温“跳水”冷暖快速反转](https://www.thepaper.cn/newsDetail_forward_32639776) |
| #10 | [单笔金额不高的压岁钱，银行为何纷纷开“抢”？](https://www.thepaper.cn/newsDetail_forward_32639775) |

### 抖音

| 排名 | 标题 |
|------|------|
| #1 | [谷爱凌李方慧包揽U池金银牌](https://www.douyin.com/hot/2408149) |
| #2 | [苏翊鸣担任闭幕式旗手](https://www.douyin.com/hot/2408150) |
| #3 | [最长春节假期步入尾声](https://www.douyin.com/hot/2408700) |
| #4 | [即使万般不舍 依然也要往前走](https://www.douyin.com/hot/2408221) |
| #5 | [新闻联播](https://www.douyin.com/hot/2408846) |
| #6 | [刘少昂赛后真诚局直播](https://www.douyin.com/hot/2408765) |
| #7 | [当美妆达人回村后](https://www.douyin.com/hot/2408098) |
| #8 | [赵心童6:5艾伦](https://www.douyin.com/hot/2408157) |
| #9 | [大年初六送穷日](https://www.douyin.com/hot/2408106) |
| #10 | [格雷莫德说谷爱凌最能推动自己](https://www.douyin.com/hot/2408018) |

### 财联社热门

| 排名 | 标题 |
|------|------|
| #1 | [特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405) |
| #2 | [中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111) |
| #3 | [什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326) |
| #4 | [春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289) |
| #5 | [美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233) |
| #6 | [特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246) |
| #7 | [没有方向盘、没有脚踏板，特斯拉新车来了](https://www.cls.cn/detail/2292285) |
| #8 | [春晚人形机器人“大秀肌肉”背后：A股新材料产业链多点突破 这些企业抢占赛道先机](https://www.cls.cn/detail/2292433) |
| #9 | [香港长江和记最新发声](https://www.cls.cn/detail/2292101) |
| #10 | [“内存荒”席卷全球，成AI竞赛关键瓶颈？又一硅谷大佬发声](https://www.cls.cn/detail/2292342) |

## 🔗 原始链接索引

### 🐦 Twitter 原文 (52/52 条)

- [2026-02-22T12:00 @GarageGuyChase [热门] | It’s so cool to hate AI](https://twitter.com/GarageGuyChase/status/2025255625815376033)
- [2026-02-22T12:00 @elonmusk [热门] | Yes](https://twitter.com/elonmusk/status/2024819025298235611)
- [2026-02-22T12:00 @ClaireGeronimii [热门] | J’ai le plaisir de vous annoncer ma candidature aux municipales les 15 et 22 mars prochain...](https://twitter.com/ClaireGeronimii/status/2025201582590025974)
- [2026-02-22T12:00 @TheMuslim786 [热门] | Location: Badaun,UP "Get out of the village, you're jihadis, you're Katuas," Akshay Singh ...](https://twitter.com/TheMuslim786/status/2025251859762680206)
- [2026-02-22T12:00 @insidefolkative [热门] | "Siapin dana darurat makanya". In this economy semuanya darurat bjirr 😭😭😭😭😭😭😭😭](https://twitter.com/insidefolkative/status/2025192508901429626)
- [2026-02-22T12:00 @lebscit [热门] | por causa de um hat-trick no vitória, disseram que o pedro era melhor que esse mano aí](https://twitter.com/lebscit/status/2025326348202278958)
- [2026-02-22T12:00 @Mattpetti32 [热门] | - Trump didn't legalize deadly drugs like Fentanyl - Trump didn't flood Canada with millio...](https://twitter.com/Mattpetti32/status/2025237089340555347)
- [2026-02-22T12:00 @Jvnior [热门] | Israeli jews are: - serial liars - baby killers - minor lovers - skin stealers - sex traff...](https://twitter.com/Jvnior/status/2025192295264334093)
- [2026-02-22T12:00 @binance [热门] | From Bitcoin to altcoins, explore 550+ tokens and trade easily on Binance starting with ju...](https://twitter.com/binance/status/2013965079512076296)
- [2026-02-22T12:00 @KietaJibun [热门] | こうやってAIに画像を作らせることも出来た、でも手作りの方が面白くなると思ったから30分くらいかけてコラ画像を作ったんだ](https://twitter.com/KietaJibun/status/2025459434517135581)
- [2026-02-22T12:00 @psvit [热门] | สิ่งนี้คือ Lifestyle Inflation ซึ่งเดี๋ยวนี้เกิดตั้งแต่เด็ก เพราะตามพ่อแม่มา ซูชิโระทุกอาท...](https://twitter.com/psvit/status/2025419843554681018)
- [2026-02-22T12:00 @Urhobo_Mudiaga [热门] | Stop complaining and nagging every single day, about elections, the system, the economy, r...](https://twitter.com/Urhobo_Mudiaga/status/2025465798899155327)
- [2026-02-22T12:00 @un1versalist [热门] | People basically found out aliens were real yesterday. Stock market went up No one freaked...](https://twitter.com/un1versalist/status/2024999111833841889)
- [2026-02-22T12:00 @raghav_chadha [热门] | In the 20th century, power depended on OIL and STEEL. In the 21st century, power depends o...](https://twitter.com/raghav_chadha/status/2023632195148280168)
- [2026-02-22T12:00 @cryptorover [热门] | BULLISH: 🇺🇸 President Trump predicts the US stock market will double by the end of his ter...](https://twitter.com/cryptorover/status/2025370435727003782)
- [2026-02-22T12:00 @TomolaGroup [热门] | THE NIGERIAN STOCK MARKET — A Complete Beginner’s Guide I’ve been getting tons of DMs aski...](https://twitter.com/TomolaGroup/status/2025139638659060042)
- [2026-02-22T12:00 @spectatorindex [热门] | NVIDIA market value 1st of January, 2024: $1.22 trillion Now: $4.63 trillion](https://twitter.com/spectatorindex/status/2025254194605948955)
- [2026-02-22T12:00 @gakeau [热门] | あとAIは死ぬほど電力を喰うのでエネルギー資源をそこまで割くべきなのかというのも大問題で、つまり日常的に「便利道具」として使えるカジュアルさと見えないデメリットや搾取構造のギャップ...](https://twitter.com/gakeau/status/2025441363190501784)
- [2026-02-22T12:00 @rindochihaya [热门] | 🎧配信告知 このあと22:00 START 【デヴィエーション・ゲーム】 FGでAIにばれないようにお絵描きするゾ！！！！piped.video/live/zm6lxIXl-m8…...](https://twitter.com/rindochihaya/status/2025538234277835256)
- [2026-02-22T12:00 @TheQuint [热门] | Nargis was pregnant when Delhi riots took away her husband, Mursaleen. Nargis gave birth t...](https://twitter.com/TheQuint/status/2025196406571762024)
- [2026-02-22T12:00 @pushpendrakum [热门] | Imagine if just 25% of MPs spoke about real issues instead of caste math. Toll scams. Hosp...](https://twitter.com/pushpendrakum/status/2025466732975194578)
- [2026-02-22T12:00 @17QStorm [热门] | 🚨 DEVIN NUNES DROPS MAR-A-LAGO RAID MEGABOMB: FBI STORMED TRUMP'S FORTRESS TO SHIELD OBAMA...](https://twitter.com/17QStorm/status/2025220823854752098)
- [2026-02-22T12:00 @SShabbarZaidi [热门] | Dhaka will have 5 mass transit by 2028. 3 underground. Karachi being 2 time larger, has no...](https://twitter.com/SShabbarZaidi/status/2025513861252808805)
- [2026-02-22T12:00 @himantabiswa [热门] | Calling our youth to be a part of the Orange Economy- Let your creative ideas do the talki...](https://twitter.com/himantabiswa/status/2025525655417557126)
- [2026-02-22T12:00 @Shinsho_ni [热门] | Während Millionen Rentner mit steigenden Lebenshaltungskosten kämpfen, fordert der JU-Chef...](https://twitter.com/Shinsho_ni/status/2025132564130763031)
- [2026-02-22T12:00 @mikebeckhamsm [热门] | I’ve probably spent 150 hours in the last month working with AI. One thing has become crys...](https://twitter.com/mikebeckhamsm/status/2025411571464216937)
- [2026-02-22T12:00 @LlyrPowell [热门] | Labour and Plaid’s 20mph obsession is slowing the nation to a crawl and holding our econom...](https://twitter.com/LlyrPowell/status/2025512059631186346)
- [2026-02-22T12:00 @amaliyakusumaa [热门] | PLSS GA RUGI KAH JUAL SELAI SEBANYAK INI🫵🏻 in this economy, kapan lagi nemu selai strawber...](https://twitter.com/amaliyakusumaa/status/2025518257088929902)
- [2026-02-22T12:00 @shioshio38 [热门] | パトレイバーの一コマに、資本家の夢は、給料のいらない従業員というセリフがある。 一連のAIの進化を見るとこれが進んだ先が資本家の夢なのだろうなと思った。](https://twitter.com/shioshio38/status/1636336124200378368)
- [2026-02-22T12:00 @Vivek4real_ [热门] | On CNN: "President Trump should hire Nancy Pelosi in retirement to manage Americans' stock...](https://twitter.com/Vivek4real_/status/2025501848703041853)
- [2026-02-22T11:51 @CoinDesk [关注] | New: http://localhost/VitalikButerin proposes AI “stewards” to vote on behalf of DAO users...](https://twitter.com/CoinDesk/status/2025539040108237253)
- [2026-02-22T11:27 @BBCWorld [关注] | US ambassador's Israel comments condemned by Arab and Muslim nations https://bbc.in/40kcre...](https://twitter.com/BBCWorld/status/2025532800338690464)
- [2026-02-22T11:13 @bindureddy [关注] | While Gemini 3.1 at least tries to compete with Opus 4.6…. OpenAI feels like it’s no longe...](https://twitter.com/bindureddy/status/2025529429150278063)
- [2026-02-22T10:33 @CNBC [关注] | India delays Washington trade visit as U.S. tariff policy shifts, source tells CNBC https:...](https://twitter.com/CNBC/status/2025519207765430414)
- [2026-02-22T10:29 @CoinDesk [关注] | Markets: http://localhost/search?q=%23XRP just logged its largest realized loss spike sinc...](https://twitter.com/CoinDesk/status/2025518421664755895)
- [2026-02-22T09:35 @CoinDesk [关注] | http://localhost/shauryamalwa reports: https://www.coindesk.com/markets/2026/02/22/bitcoin...](https://twitter.com/CoinDesk/status/2025504616784232779)
- [2026-02-22T09:24 @BBCWorld [关注] | Teenage girl dies after hit-and-run collision https://bbc.in/4s43Ybm](https://twitter.com/BBCWorld/status/2025501893850472570)
- [2026-02-22T09:18 @CoinDesk [关注] | Insight: U.S. Google searches for “Bitcoin to zero” just hit a record high as http://local...](https://twitter.com/CoinDesk/status/2025500474594545846)
- [2026-02-22T08:41 @elonmusk [关注] | Try Grok Imagine. It keeps getting better. DogeDesigner (@cb_doge) BREAKING: xAI's Grok Im...](https://twitter.com/elonmusk/status/2025491021073674549)
- [2026-02-22T08:39 @elonmusk [关注] | Come a long way X Freeze (@XFreeze) How it started vs. how it’s going — http://localhost/X...](https://twitter.com/elonmusk/status/2025490500011089995)
- [2026-02-22T08:30 @elonmusk [关注] | Grok Imagine keeps improving Art Muse (@art_muse) Happy Sunday! Video — http://localhost/a...](https://twitter.com/elonmusk/status/2025488230401937723)
- [2026-02-22T08:23 @elonmusk [关注] | Grok understands jokes https://nitter.net/i/grok/share/7f65e9dd3e7f42dcb81c5fb6496ec3cb](https://twitter.com/elonmusk/status/2025486491057541209)
- [2026-02-22T08:10 @BBCWorld [关注] | Pakistan launches strikes on Afghanistan, with Taliban saying dozens killed https://bbc.in...](https://twitter.com/BBCWorld/status/2025483393480151066)
- [2026-02-22T06:56 @BBCWorld [关注] | Could this be wreckage from a 214-year-old maritime disaster? https://bbc.in/4aM324v](https://twitter.com/BBCWorld/status/2025464812944134601)
- [2026-02-22T05:07 @BBCWorld [关注] | More than 1,500 Venezuelan political prisoners apply for amnesty https://bbc.in/4l89Qyd](https://twitter.com/BBCWorld/status/2025437360175862245)
- [2026-02-22T04:57 @elonmusk [关注] | Starship = Hope](https://twitter.com/elonmusk/status/2025434732335677655)
- [2026-02-22T02:00 @BBCWorld [关注] | Final missing Lake Tahoe avalanche skier found dead after 5-day search https://bbc.in/3Oqn...](https://twitter.com/BBCWorld/status/2025390117645365274)
- [2026-02-22T01:51 @BBCWorld [关注] | Willie Colón, trombonist who pioneered salsa music, dies aged 75 https://bbc.in/4cGbNiQ](https://twitter.com/BBCWorld/status/2025387838842294712)
- [2026-02-22T00:40 @elonmusk [关注] | (无正文)](https://twitter.com/elonmusk/status/2025370061553471561)
- [2026-02-22T00:35 @BBCWorld [关注] | How football is helping girls fight against forced marriage https://bbc.in/46URkDl](https://twitter.com/BBCWorld/status/2025368703307522386)
- [2026-02-22T00:07 @elonmusk [关注] | Goodnight 😴 Video](https://twitter.com/elonmusk/status/2025361852952109563)
- [2026-02-22T00:06 @BBCWorld [关注] | From Venezuela to immigration crackdown, Project 2025 provided Trump's roadmap https://bbc...](https://twitter.com/BBCWorld/status/2025361547988455581)

### 📱 微信公众号原文 (0/0 条)

- 暂无可用链接

### 🔥 NewsNow 原文 (120/120 条)

- [微博 #1 | 谷爱凌第三滑94.75分](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E7%AC%AC%E4%B8%89%E6%BB%9194.75%E5%88%86%23)
- [bilibili 热搜 #1 | ​谷爱凌摘金](https://search.bilibili.com/all?keyword=%E2%80%8B%E8%B0%B7%E7%88%B1%E5%87%8C%E6%91%98%E9%87%91)
- [百度热搜 #1 | 第5金！谷爱凌夺冠](https://www.baidu.com/s?wd=%E7%AC%AC5%E9%87%91%EF%BC%81%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%BA%E5%86%A0)
- [今日头条 #1 | 中国队5金4银6铜收官](https://www.toutiao.com/trending/7609123113803989035/)
- [华尔街见闻 #1 | 特朗普新加征关税税率加码至15% 美政府“越权”关税引企业诉讼潮](https://wallstreetcn.com/articles/3765942)
- [贴吧 #1 | 撤诉!初中生扶老人被讹22w](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%92%A4%E8%AF%89%21%E5%88%9D%E4%B8%AD%E7%94%9F%E6%89%B6%E8%80%81%E4%BA%BA%E8%A2%AB%E8%AE%B922w&topic_id=28350844)
- [知乎 #1 | 如何看待当所有国产大模型都在 2026 春节撒钱抢用户时，DeepSeek 却默不作声继续奋战？](https://www.zhihu.com/question/2004982651719812885)
- [凤凰网 #1 | 特朗普的报复来了](https://news.ifeng.com/c/8qwaojRoDP6)
- [澎湃新闻 #1 | 过年的9个晚上｜为什么我们总是怀念儿时的年](https://www.thepaper.cn/newsDetail_forward_32599785)
- [抖音 #1 | 谷爱凌李方慧包揽U池金银牌](https://www.douyin.com/hot/2408149)
- [财联社热门 #1 | 特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405)
- [微博 #2 | 谷爱凌金牌](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E9%87%91%E7%89%8C%23)
- [百度热搜 #2 | 李方慧夺女子U型场地银牌](https://www.baidu.com/s?wd=%E6%9D%8E%E6%96%B9%E6%85%A7%E5%A4%BA%E5%A5%B3%E5%AD%90U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E9%93%B6%E7%89%8C)
- [凤凰网 #2 | 美国前商务部长：其他关税方案，都会削弱特朗普对华谈判筹码](https://news.ifeng.com/c/8qxAuTEgS6q)
- [今日头条 #2 | 谷爱凌金牌！中国队包揽女子U型池金银](https://www.toutiao.com/trending/7609098288788176937/)
- [知乎 #2 | 韩延哽咽恳求多给《星河入梦》有效排片，这部投资近四亿的电影为何面临排片困境？](https://www.zhihu.com/question/2008647492124827724)
- [贴吧 #2 | 洗脚闹矛盾,男子跳桥失联](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B4%97%E8%84%9A%E9%97%B9%E7%9F%9B%E7%9B%BE%2C%E7%94%B7%E5%AD%90%E8%B7%B3%E6%A1%A5%E5%A4%B1%E8%81%94&topic_id=28350857)
- [bilibili 热搜 #2 | 虹猫蓝兔七侠传4K修复版定档](https://search.bilibili.com/all?keyword=%E8%99%B9%E7%8C%AB%E8%93%9D%E5%85%94%E4%B8%83%E4%BE%A0%E4%BC%A04K%E4%BF%AE%E5%A4%8D%E7%89%88%E5%AE%9A%E6%A1%A3)
- [华尔街见闻 #2 | 大摩评价MiniMax“全球顶尖基座模型稀缺资产”，高估值核心逻辑在于“技术决定天花板、全球化决定估值”](https://wallstreetcn.com/articles/3765947)
- [澎湃新闻 #2 | 四川广元法院春节执行攻坚专项行动：一日拘传38名“老赖”](https://www.thepaper.cn/newsDetail_forward_32639463)
- [抖音 #2 | 苏翊鸣担任闭幕式旗手](https://www.douyin.com/hot/2408150)
- [财联社热门 #2 | 中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111)
- [华尔街见闻 #3 | 玉渊谭天：美国对华哪些关税被停止征收？](https://wallstreetcn.com/articles/3765953)
- [百度热搜 #3 | 春运返程这些准备要做好](https://www.baidu.com/s?wd=%E6%98%A5%E8%BF%90%E8%BF%94%E7%A8%8B%E8%BF%99%E4%BA%9B%E5%87%86%E5%A4%87%E8%A6%81%E5%81%9A%E5%A5%BD)
- [抖音 #3 | 最长春节假期步入尾声](https://www.douyin.com/hot/2408700)
- [bilibili 热搜 #3 | 解读特朗普提高全球进口关税](https://search.bilibili.com/all?keyword=%E8%A7%A3%E8%AF%BB%E7%89%B9%E6%9C%97%E6%99%AE%E6%8F%90%E9%AB%98%E5%85%A8%E7%90%83%E8%BF%9B%E5%8F%A3%E5%85%B3%E7%A8%8E)
- [今日头条 #3 | 各地活动精彩纷呈 喜气洋洋庆新春](https://www.toutiao.com/trending/7609591683432631818/)
- [贴吧 #3 | 法外狂徒!罗翔帮黑老大减刑](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B3%95%E5%A4%96%E7%8B%82%E5%BE%92%21%E7%BD%97%E7%BF%94%E5%B8%AE%E9%BB%91%E8%80%81%E5%A4%A7%E5%87%8F%E5%88%91&topic_id=28350855)
- [澎湃新闻 #3 | 春启新程｜春节里一家亮灯的“烟火小馆”，迎来不少来沪游客](https://www.thepaper.cn/newsDetail_forward_32639299)
- [凤凰网 #3 | 特朗普新加征关税加码至15%](https://news.ifeng.com/c/8qwaojRoDKf)
- [知乎 #3 | 今年大年初一给我的直属领导发了一条祝福微信，但是领导一直没有回我，这是为什么？](https://www.zhihu.com/question/2007378989140952602)
- [微博 #3 | 热气腾腾的中国年](https://s.weibo.com/weibo?q=%23%E7%83%AD%E6%B0%94%E8%85%BE%E8%85%BE%E7%9A%84%E4%B8%AD%E5%9B%BD%E5%B9%B4%23)
- [财联社热门 #3 | 什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326)
- [bilibili 热搜 #4 | 李方慧斩获银牌](https://search.bilibili.com/all?keyword=%E6%9D%8E%E6%96%B9%E6%85%A7%E6%96%A9%E8%8E%B7%E9%93%B6%E7%89%8C)
- [百度热搜 #4 | 谷爱凌U池第二滑94.00分](https://www.baidu.com/s?wd=%E8%B0%B7%E7%88%B1%E5%87%8CU%E6%B1%A0%E7%AC%AC%E4%BA%8C%E6%BB%9194.00%E5%88%86)
- [微博 #4 | 女子U型场地决赛](https://s.weibo.com/weibo?q=%23%E5%A5%B3%E5%AD%90U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E5%86%B3%E8%B5%9B%23)
- [华尔街见闻 #4 | 春节期间，国内外都发生了什么？](https://wallstreetcn.com/articles/3765956)
- [今日头条 #4 | 河南矿山客户排队交钱：大厅挤满人](https://www.toutiao.com/trending/7608838132696563731/)
- [知乎 #4 | 贵州非遗传承人半年卖 800 只「点翠蟑螂」，如何理解这种反差美学？若人人喊打的蟑螂变好看了，你能接受吗？](https://www.zhihu.com/question/2007528287103051494)
- [抖音 #4 | 即使万般不舍 依然也要往前走](https://www.douyin.com/hot/2408221)
- [澎湃新闻 #4 | 新春走基层·见喜｜重新学会跟长辈相处](https://www.thepaper.cn/newsDetail_forward_32639761)
- [贴吧 #4 | 撞破妻子出轨,丈夫报警告性侵](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%92%9E%E7%A0%B4%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8%2C%E4%B8%88%E5%A4%AB%E6%8A%A5%E8%AD%A6%E5%91%8A%E6%80%A7%E4%BE%B5&topic_id=28350840)
- [凤凰网 #4 | 欧盟、英国、加拿大、墨西哥、德国，最新发声](https://news.ifeng.com/c/8qwaojRoDGX)
- [财联社热门 #4 | 春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289)
- [抖音 #5 | 新闻联播](https://www.douyin.com/hot/2408846)
- [bilibili 热搜 #5 | 挑战去第一财神庙刮彩票](https://search.bilibili.com/all?keyword=%E6%8C%91%E6%88%98%E5%8E%BB%E7%AC%AC%E4%B8%80%E8%B4%A2%E7%A5%9E%E5%BA%99%E5%88%AE%E5%BD%A9%E7%A5%A8)
- [今日头条 #5 | 《新闻联播》正在直播](https://www.toutiao.com/trending/7609640843644882478/)
- [微博 #5 | 谷爱凌第二滑94.00分](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E7%AC%AC%E4%BA%8C%E6%BB%9194.00%E5%88%86%23)
- [凤凰网 #5 | 一顿中餐掀翻秘鲁政坛，美国在背后做了什么？](https://news.ifeng.com/c/8qxLW2rbfUZ)
- [百度热搜 #5 | 远嫁姐姐回家 47岁弟弟激动得像孩子](https://www.baidu.com/s?wd=%E8%BF%9C%E5%AB%81%E5%A7%90%E5%A7%90%E5%9B%9E%E5%AE%B6+47%E5%B2%81%E5%BC%9F%E5%BC%9F%E6%BF%80%E5%8A%A8%E5%BE%97%E5%83%8F%E5%AD%A9%E5%AD%90)
- [华尔街见闻 #5 | 过去30年来未见之局面！美股指数波动之小创1960年来之最，而个股波动率却高达指数7倍](https://wallstreetcn.com/articles/3765941)
- [知乎 #5 | 舅舅送外甥女 30 斤银砖当压岁钱，家长因为礼物贵重主动归还，如何看待双方的举动？](https://www.zhihu.com/question/2008606498859742105)
- [贴吧 #5 | 麦当劳作死,联动柜子学院](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%BA%A6%E5%BD%93%E5%8A%B3%E4%BD%9C%E6%AD%BB%2C%E8%81%94%E5%8A%A8%E6%9F%9C%E5%AD%90%E5%AD%A6%E9%99%A2&topic_id=28350849)
- [澎湃新闻 #5 | 中东睿评｜美以与伊朗博弈的混沌状态只能靠战争才能打破吗？](https://www.thepaper.cn/newsDetail_forward_32639434)
- [财联社热门 #5 | 美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233)
- [知乎 #6 | 米兰冬奥自由式滑雪女子 U 型场地技巧决赛，谷爱凌卫冕，李方慧摘银，如何评价他们的发挥？](https://www.zhihu.com/question/2008677675422672634)
- [抖音 #6 | 刘少昂赛后真诚局直播](https://www.douyin.com/hot/2408765)
- [微博 #6 | 李方慧银牌](https://s.weibo.com/weibo?q=%E6%9D%8E%E6%96%B9%E6%85%A7%E9%93%B6%E7%89%8C)
- [今日头条 #6 | 老人带茅台乘火车被拦欲当场喝完](https://www.toutiao.com/trending/7609283906038399018/)
- [贴吧 #6 | 钓帝去世,钓鱼圈传奇落幕](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%92%93%E5%B8%9D%E5%8E%BB%E4%B8%96%2C%E9%92%93%E9%B1%BC%E5%9C%88%E4%BC%A0%E5%A5%87%E8%90%BD%E5%B9%95&topic_id=28350858)
- [bilibili 热搜 #6 | 中华野兽先生](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%8D%8E%E9%87%8E%E5%85%BD%E5%85%88%E7%94%9F)
- [华尔街见闻 #6 | 欢迎来到AI智能体新时代：未来不是“为人创造”，而是“为AI服务”](https://wallstreetcn.com/articles/3765948)
- [凤凰网 #6 | 12天72只老虎集中死亡，泰国官方通报](https://v.ifeng.com/c/8qx23a92Pwn)
- [百度热搜 #6 | 给妈妈的红包被放回 女儿打开后破防](https://www.baidu.com/s?wd=%E7%BB%99%E5%A6%88%E5%A6%88%E7%9A%84%E7%BA%A2%E5%8C%85%E8%A2%AB%E6%94%BE%E5%9B%9E+%E5%A5%B3%E5%84%BF%E6%89%93%E5%BC%80%E5%90%8E%E7%A0%B4%E9%98%B2)
- [澎湃新闻 #6 | 这个春节，上海何以成为热门目的地？](https://www.thepaper.cn/newsDetail_forward_32639992)
- [财联社热门 #6 | 特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246)
- [微博 #7 | 李方慧第二滑91.50分](https://s.weibo.com/weibo?q=%23%E6%9D%8E%E6%96%B9%E6%85%A7%E7%AC%AC%E4%BA%8C%E6%BB%9191.50%E5%88%86%23)
- [知乎 #7 | 长辈说「饿一饿更长寿」，春节少吃一顿真的养生吗，空腹有哪些风险？](https://www.zhihu.com/question/2005954269753390531)
- [百度热搜 #7 | “银发留学”正在悄然兴起](https://www.baidu.com/s?wd=%E2%80%9C%E9%93%B6%E5%8F%91%E7%95%99%E5%AD%A6%E2%80%9D%E6%AD%A3%E5%9C%A8%E6%82%84%E7%84%B6%E5%85%B4%E8%B5%B7)
- [bilibili 热搜 #7 | 史蒂夫速通狗熊岭](https://search.bilibili.com/all?keyword=%E5%8F%B2%E8%92%82%E5%A4%AB%E9%80%9F%E9%80%9A%E7%8B%97%E7%86%8A%E5%B2%AD)
- [今日头条 #7 | 河南矿山女销售去年签约4个亿](https://www.toutiao.com/trending/7609117198203748393/)
- [华尔街见闻 #7 | 表面风光之下，OpenAI的“四大困境”](https://wallstreetcn.com/articles/3765945)
- [抖音 #7 | 当美妆达人回村后](https://www.douyin.com/hot/2408098)
- [贴吧 #7 | 小国作妖,春节译名之争再起](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%B0%8F%E5%9B%BD%E4%BD%9C%E5%A6%96%2C%E6%98%A5%E8%8A%82%E8%AF%91%E5%90%8D%E4%B9%8B%E4%BA%89%E5%86%8D%E8%B5%B7&topic_id=28350853)
- [澎湃新闻 #7 | 阿根廷田野手记：关停的工厂、变贵的账单与华商的新生意｜907编辑部](https://www.thepaper.cn/newsDetail_forward_32638732)
- [凤凰网 #7 | “以色列拿下整个中东也没问题”？沙特等14国强烈谴责](https://news.ifeng.com/c/8qwiW7aAKXh)
- [财联社热门 #7 | 没有方向盘、没有脚踏板，特斯拉新车来了](https://www.cls.cn/detail/2292285)
- [微博 #8 | 谷爱凌李方慧拥抱](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E6%9D%8E%E6%96%B9%E6%85%A7%E6%8B%A5%E6%8A%B1%23)
- [百度热搜 #8 | 彩民随手扔掉千万彩票2天才发现](https://www.baidu.com/s?wd=%E5%BD%A9%E6%B0%91%E9%9A%8F%E6%89%8B%E6%89%94%E6%8E%89%E5%8D%83%E4%B8%87%E5%BD%A9%E7%A5%A82%E5%A4%A9%E6%89%8D%E5%8F%91%E7%8E%B0)
- [华尔街见闻 #8 | SK会长崔泰源警告：AI正在吞噬一切，今年千亿美元利润或瞬间变巨亏](https://wallstreetcn.com/articles/3765949)
- [bilibili 热搜 #8 | 熊人修仙传](https://search.bilibili.com/all?keyword=%E7%86%8A%E4%BA%BA%E4%BF%AE%E4%BB%99%E4%BC%A0)
- [澎湃新闻 #8 | 持续放风试探，美官员称或对伊朗发动针对特定个人的军事打击](https://www.thepaper.cn/newsDetail_forward_32641921)
- [知乎 #8 | 看完《飞驰人生 3》好多人喜欢叶经理，你如何评价这个人物？](https://www.zhihu.com/question/2008127511381370827)
- [今日头条 #8 | 父亲屋外透气看见儿子坠楼接住](https://www.toutiao.com/trending/7609292140770328582/)
- [财联社热门 #8 | 春晚人形机器人“大秀肌肉”背后：A股新材料产业链多点突破 这些企业抢占赛道先机](https://www.cls.cn/detail/2292433)
- [贴吧 #8 | 亲爹抛妻弃子,命丧俄乌战场](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E7%88%B9%E6%8A%9B%E5%A6%BB%E5%BC%83%E5%AD%90%2C%E5%91%BD%E4%B8%A7%E4%BF%84%E4%B9%8C%E6%88%98%E5%9C%BA&topic_id=28350847)
- [凤凰网 #8 | 乌克兰制裁俄罗斯“影子舰队”](https://news.ifeng.com/c/8qwipyWWgXr)
- [抖音 #8 | 赵心童6:5艾伦](https://www.douyin.com/hot/2408157)
- [bilibili 热搜 #9 | 拜年小技巧](https://search.bilibili.com/all?keyword=%E6%8B%9C%E5%B9%B4%E5%B0%8F%E6%8A%80%E5%B7%A7)
- [知乎 #9 | 妈祖文化中的掷圣杯是一种怎样的仪式？各种落法有哪些寓意？](https://www.zhihu.com/question/2008542148102943240)
- [微博 #9 | 韩国队抗议米兰冬奥至少4次印错国旗](https://s.weibo.com/weibo?q=%E9%9F%A9%E5%9B%BD%E9%98%9F%E6%8A%97%E8%AE%AE%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E8%87%B3%E5%B0%914%E6%AC%A1%E5%8D%B0%E9%94%99%E5%9B%BD%E6%97%97)
- [华尔街见闻 #9 | 地热——一场静悄悄的美国能源变革](https://wallstreetcn.com/articles/3765952)
- [百度热搜 #9 | 男子晒监控：春节像做了一场热闹的梦](https://www.baidu.com/s?wd=%E7%94%B7%E5%AD%90%E6%99%92%E7%9B%91%E6%8E%A7%EF%BC%9A%E6%98%A5%E8%8A%82%E5%83%8F%E5%81%9A%E4%BA%86%E4%B8%80%E5%9C%BA%E7%83%AD%E9%97%B9%E7%9A%84%E6%A2%A6)
- [今日头条 #9 | 年轻人过年把洗浴中心玩成性价比酒店](https://www.toutiao.com/trending/7608593086784094218/)
- [凤凰网 #9 | 韩国外交部强烈抗议日本举行“竹岛日”活动](https://news.ifeng.com/c/8qx0g6BhHN6)
- [贴吧 #9 | 飞碟社官宣,原神动画稳了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%A3%9E%E7%A2%9F%E7%A4%BE%E5%AE%98%E5%AE%A3%2C%E5%8E%9F%E7%A5%9E%E5%8A%A8%E7%94%BB%E7%A8%B3%E4%BA%86&topic_id=28350851)
- [抖音 #9 | 大年初六送穷日](https://www.douyin.com/hot/2408106)
- [澎湃新闻 #9 | 暴雪大风沙尘大范围降雨上线，北方气温“跳水”冷暖快速反转](https://www.thepaper.cn/newsDetail_forward_32639776)
- [财联社热门 #9 | 香港长江和记最新发声](https://www.cls.cn/detail/2292101)
- [今日头条 #10 | 犯困小狗跟主人过年返程表情可爱](https://www.toutiao.com/trending/7608962917555798042/)
- [百度热搜 #10 | 谷爱凌领衔4朵金花U型场地决赛冲金](https://www.baidu.com/s?wd=%E8%B0%B7%E7%88%B1%E5%87%8C%E9%A2%86%E8%A1%944%E6%9C%B5%E9%87%91%E8%8A%B1U%E5%9E%8B%E5%9C%BA%E5%9C%B0%E5%86%B3%E8%B5%9B%E5%86%B2%E9%87%91)
- [凤凰网 #10 | 破开冰面潜水打捞，俄寻回所有坠湖溺亡的中国游客遗体](https://news.ifeng.com/c/8qxA3o3RFZg)
- [华尔街见闻 #10 | 比净值低20-35%！对冲基金报价收购Blue Owl旗下基金份额，加剧市场对PE的质疑](https://wallstreetcn.com/articles/3765939)
- [微博 #10 | 淀粉肠进入瑜伽裤时代](https://s.weibo.com/weibo?q=%E6%B7%80%E7%B2%89%E8%82%A0%E8%BF%9B%E5%85%A5%E7%91%9C%E4%BC%BD%E8%A3%A4%E6%97%B6%E4%BB%A3)
- [知乎 #10 | 晚上九点想让男朋友开车送妈妈回家，男朋友拒绝后我一直很伤心，我是不是太自私了，该怎么改变自己的想法？](https://www.zhihu.com/question/2008483127039902430)
- [财联社热门 #10 | “内存荒”席卷全球，成AI竞赛关键瓶颈？又一硅谷大佬发声](https://www.cls.cn/detail/2292342)
- [bilibili 热搜 #10 | 原神同人新春会](https://search.bilibili.com/all?keyword=%E5%8E%9F%E7%A5%9E%E5%90%8C%E4%BA%BA%E6%96%B0%E6%98%A5%E4%BC%9A)
- [澎湃新闻 #10 | 单笔金额不高的压岁钱，银行为何纷纷开“抢”？](https://www.thepaper.cn/newsDetail_forward_32639775)
- [抖音 #10 | 格雷莫德说谷爱凌最能推动自己](https://www.douyin.com/hot/2408018)
- [贴吧 #10 | 喂猫起争执,男子遭恶邻杀害](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%96%82%E7%8C%AB%E8%B5%B7%E4%BA%89%E6%89%A7%2C%E7%94%B7%E5%AD%90%E9%81%AD%E6%81%B6%E9%82%BB%E6%9D%80%E5%AE%B3&topic_id=28350838)
- [今日头条 #11 | 蔚来汽车换电量连续四日创新高](https://www.toutiao.com/trending/7609248794152534057/)
- [百度热搜 #11 | “江西丰城鞭炮炸死人”系编造](https://www.baidu.com/s?wd=%E2%80%9C%E6%B1%9F%E8%A5%BF%E4%B8%B0%E5%9F%8E%E9%9E%AD%E7%82%AE%E7%82%B8%E6%AD%BB%E4%BA%BA%E2%80%9D%E7%B3%BB%E7%BC%96%E9%80%A0)
- [微博 #11 | 杨幂演技](https://s.weibo.com/weibo?q=%E6%9D%A8%E5%B9%82%E6%BC%94%E6%8A%80)
- [财联社热门 #11 | 环球下周看点：关税风暴叠加美伊博弈 英伟达能否再救AI牛市？](https://www.cls.cn/detail/2292422)
- [bilibili 热搜 #11 | 牧神记秦牧灭门难陀宗](https://search.bilibili.com/all?keyword=%E7%89%A7%E7%A5%9E%E8%AE%B0%E7%A7%A6%E7%89%A7%E7%81%AD%E9%97%A8%E9%9A%BE%E9%99%80%E5%AE%97)
- [凤凰网 #11 | 平顶山夫妻暴打15岁女孩，律师：打人者最高判10年](https://news.ifeng.com/c/8qwo3v3w2cI)
- [知乎 #11 | 美国加征「全球进口关税」一日后，将新关税税率升至 15%，会有哪些影响？税率还会增加吗？](https://www.zhihu.com/question/2008803593088623486)
- [澎湃新闻 #11 | 大年初五全国道路交通平稳有序，明后两天将迎来返程大客流](https://www.thepaper.cn/newsDetail_forward_32639782)
- [抖音 #11 | 老姨夫有点跳天鹅湖的功底](https://www.douyin.com/hot/2408099)
- [贴吧 #11 | 春节闯关,神人亲戚大赏](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%98%A5%E8%8A%82%E9%97%AF%E5%85%B3%2C%E7%A5%9E%E4%BA%BA%E4%BA%B2%E6%88%9A%E5%A4%A7%E8%B5%8F&topic_id=28350839)

### 💻 GitHub 原文 (20/40 条)

- [openclaw/openclaw | ⭐ 217385 | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/openclaw/openclaw)
- [Significant-Gravitas/AutoGPT | ⭐ 181928 | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission i...](https://github.com/Significant-Gravitas/AutoGPT)
- [n8n-io/n8n | ⭐ 175762 | Fair-code workflow automation platform with native AI capabilities. Combine visual buildin...](https://github.com/n8n-io/n8n)
- [ollama/ollama | ⭐ 163115 | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and othe...](https://github.com/ollama/ollama)
- [huggingface/transformers | ⭐ 156804 | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning model...](https://github.com/huggingface/transformers)
- [f/prompts.chat | ⭐ 146489 | a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. F...](https://github.com/f/prompts.chat)
- [langflow-ai/langflow | ⭐ 144962 | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.](https://github.com/langflow-ai/langflow)
- [langgenius/dify | ⭐ 129993 | Production-ready platform for agentic workflow development.](https://github.com/langgenius/dify)
- [langchain-ai/langchain | ⭐ 127143 | 🦜🔗 The platform for reliable agents.](https://github.com/langchain-ai/langchain)
- [tensorflow/tensorflow | ⭐ 193884 | An Open Source Machine Learning Framework for Everyone](https://github.com/tensorflow/tensorflow)
- [argotorg/solidity | ⭐ 25563 | Solidity, the Smart Contract Programming Language](https://github.com/argotorg/solidity)
- [Haehnchen/crypto-trading-bot | ⭐ 3424 | Cryptocurrency trading bot in javascript for Bitfinex, Bitmex, Binance, Bybit ... (public ...](https://github.com/Haehnchen/crypto-trading-bot)
- [AlexWan/OsEngine | ⭐ 952 | Open Source algo trading platform](https://github.com/AlexWan/OsEngine)
- [SeungMaeda/polymarket-copy-bot-ts | ⭐ 861 | Polymarket || Polymarket Bot || Polymarket Copy Bot || Polymarket Copy Trading Bot || Poly...](https://github.com/SeungMaeda/polymarket-copy-bot-ts)
- [nicobailon/visual-explainer | ⭐ 2292 | Agent skill + prompt templates that generate rich HTML pages for visual diff reviews, arch...](https://github.com/nicobailon/visual-explainer)
- [nullclaw/nullclaw | ⭐ 1629 | Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig](https://github.com/nullclaw/nullclaw)
- [Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot | ⭐ 570 | Real-time polymarket trading bot that combines monitoring with strategy logic for Polymark...](https://github.com/Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot)
- [ebrasha/free-v2ray-public-list | ⭐ 523 | A simple and always-updated list of free, working V2Ray servers. including SS, SSR, Trojan...](https://github.com/ebrasha/free-v2ray-public-list)
- [michaelchu/optopsy | ⭐ 1259 | An AI enabled nimble options backtesting library for Python](https://github.com/michaelchu/optopsy)
- [NethermindEth/nethermind | ⭐ 1521 | A robust execution client for Ethereum node operators.](https://github.com/NethermindEth/nethermind)

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

### 🌐 联网检索原文 (13/13 条)

- [2026-02-22 18:31 新浪财经 | 中美AI同步加速：47天30次更新，中国AI的最强主场究竟在哪？ - 新浪财经](https://news.google.com/rss/articles/CBMifEFVX3lxTE9wRTgwVjFlMGJFd0l1dU9acENZOVJ1NGdTVmRHcFVvMWF5UDZ0d3gyenlnYVJlTGhsZEl4aVJZQzJ4UXJ4QnRCZmxMOVhwUHNLbWlpSUFaLS1KOU54NUt6QUc3dkVfR3luWlVPZkl3a2pOeDROZjZ0SEpaTDA?oc=5)
- [2026-02-22 17:20 3DM | 【均已开售】2024 易博APP下载 - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9aclIxZjlJVUM4WlEtSkJCOHZFMTJtOGNRbFdZREZ1T0t1YklDRW9VMjdReldySFMzNF9FcDdJTkk4VHZ0SEw5QVdjSnBiYXl3NE1ySktaNA?oc=5)
- [2026-02-22 16:03 news.17173.com | 详读 2 万 3 千字的新「AI 宪法」之后，我理解了 Anthropic 的痛苦 - news.17173.com](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5PbkUyNzRCMEU1d2J5TE1EdHpUenhWeGNZQ0s2eGdiTE9HX3lUeWpCMDlVenVJcUp5SGZzUVVTN19INW9fdUdBU1hSUndkRmtUOVVHRGhNbS1hQ0pEbFhwZUpqTE5QQQ?oc=5)
- [2026-02-22 14:09 新浪财经 | 恒生科技估值跌至低位，汇添富恒生科技ETF联接发起式(QDII)C(013128)捕捉AI叙事加持下估值修复红利 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTFBiSF9DZnBtTktNa25RTXZhdnB4V3lFOGRIME5aZWdpa182SVE5cFkwclQ1WEFSQXRHMnVEaUUtRUxlUEFXazFPd0tqRnViWFg1c0RyaWVtUWszZGtfRVJPZkFsVFhyNWV0d0R2Qlo1clNXSTFnNU1weA?oc=5)
- [2026-02-22 13:55 新浪财经 | 1月社融规模增速8.2% 降准降息仍待观察货币政策累计效应 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTE94WG1Ba2dpOEVQTzBrUjVPODF2V2tPajlISHVMRnhRd1F2ekFGSkNlaTY1S0tmNUFuYldGZXFyRnRaWk43WU1OdU9peUZuM1lQOWZ6cVcxOVhiMlhqaWlCUm94Rk44Y2FYQzZCU2E4T3Nxb3BIazhxVQ?oc=5)
- [2026-02-22 13:11 大紀元新聞網 | 井友倫：如何解讀最高院關稅裁決的影響 - 大紀元新聞網](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9FSlVZQjk4RWpIQUNocmJTcG42a2M0RXRMSzRaSEJsVmVvcVJfVHFDZm9TeG5sbU4xMzl0WGdmSkZYY0dsQW9BUXNHZWNBT0RHX25zNUNfb3h0ZnFGQ1RnakZIRlVKd9IBZkFVX3lxTE9FSlVZQjk4RWpIQUNocmJTcG42a2M0RXRMSzRaSEJsVmVvcVJfVHFDZm9TeG5sbU4xMzl0WGdmSkZYY0dsQW9BUXNHZWNBT0RHX25zNUNfb3h0ZnFGQ1RnakZIRlVKdw?oc=5)
- [2026-02-22 10:30 证券之星 | 回归“小央行”：美联储“沃什时代”前瞻_宏观研究_研报 - 证券之星](https://news.google.com/rss/articles/CBMiYkFVX3lxTE8wWV84MlRNUklJNGJBbmlvWEhPWE9RWE5Pc0NXZXBLc21ERl9wZmF6LWlNZ1g3LTJRc2xZUEViZi0wUjVydGZwQnhuZmRGWGdZQ1d0X0lWUkJYWDRsTUJuYUFR?oc=5)
- [2026-02-22 09:48 3DM | 第一热点 澳门新葡新京网站 - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTFBUdS1LYWlzcDVUQUIzUHR6S0dHSmtIY1FHandITld0NmtCVDBLdEVKNDZOclBhNHA5My16MUdfYXBFNGQ5LUFFUkpSWEZBV2tuZzA5V0xVYw?oc=5)
- [2026-02-22 09:10 thepaper.cn | 乘势而上｜专访张晓晶：引导政府部门存量财富向居民部门适度转移 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTFAzUjREV1kySDZiaThkdVNCMUdtOWEwaDdIMFN4aGdsczIwenpMekIxODExQmUxMXlSRkYtWjZ3ZlBnMGhfMFUxOHBiSE90Ni1RMy13cDRuYjFlSkdvM2hSSg?oc=5)
- [2026-02-22 09:02 新浪新闻_手机新浪网 | AI数据中心全球扩张浪潮下，农民坚守土地如何影响科技与农业的平衡发展？ - 新浪新闻_手机新浪网](https://news.google.com/rss/articles/CBMigwFBVV95cUxQU0l6RnpCTGZDby1QN1dmajlYa3RDUzhmUjJqZW5kM0FJWG1kSzdfODJWRl9lYUh4QzBOOUVjOXpXMjZrLUc0ZWtzcGF5NjFnY1BSd3M4cXJFSTRsN21YNTg1ajZYMHllRTFvLWZUVF8yQ3ZxMk9FbUswR1BQLU1STXotUQ?oc=5)
- [2026-02-22 08:19 thepaper.cn | “AI恐慌交易”仍未完全消散 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5vMV9jMnV2WDNEejRuNjUybFVWSkNKSGhLbk1MOGNwVk9PSWwzamdacjZacmFRSUMxSmpXNmcxRVIzRlU5dDBsSUdfSGEwMVcyQlFqR3JobmRlYlpiUkRfdA?oc=5)
- [2026-02-22 08:17 驱动之家 | Intel、AMD新一代桌面CPU发布时间曝光！Nova Lake、Zen 6双双推迟到2027年 - 驱动之家](https://news.google.com/rss/articles/CBMiWEFVX3lxTFA0ZmVzMm5lUkFMQldxUk9EZzA0c2Q1WjVDNmRRZzZwbnhuMzdrYnFibjhLUndZRS1HOC01eUJkdGpZMndVcjFsOEVIWGM3b0pQTTJORlZsWUU?oc=5)
- [2026-02-22 04:27 游侠网 | 国际AG|联合多国艺术家打造和平主题艺术展 - 游侠网](https://news.google.com/rss/articles/CBMiSkFVX3lxTE1yLUZkYXdXNXFiS3NiUThLNGI5UXJXbER3YXl3Q244UkpYSW91cEg0aHlHUjZxazBxcDNQaGQ2UmdqTTRqOVRTbWVB?oc=5)

---

*报告由 finradar 自动生成 | 2026-02-22 20:03:02（北京时间）*
