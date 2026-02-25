# 📰 finradar 🌅 早报
**2026-02-17** | 🌅 早报 | 覆盖时段: 昨日20:00 → 今日08:00 | 市场状态: ✅ 正常交易
生成时间: 2026-02-17 08:03（北京时间）

---

## 🚨 数据源健康提醒

1. 检测到微信登录异常：财联社: invalid session。请重新扫码登录 wechat-exporter。
2. 本次抓取公众号文章为 0 篇，账号搜索失败占比 100%，请检查登录态或服务状态。

处理建议：
1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。
2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。
3. 然后执行 `./scripts/local.sh report morning 20260217` 与 `./scripts/local.sh notion-push morning 20260217` 覆盖 Notion 页面。

# 🤖 AI 分析摘要

## 一、摘要
- **社会**：**2026年央视马年春晚**成为绝对社会焦点，其“科技与内容深度融合”的特征显著，机器人表演《武 BOT》等节目引发广泛讨论 [¹](https://www.zhihu.com/question/2006817906369979378)[²](https://www.toutiao.com/trending/7607438781827366955/)[³](https://www.zhihu.com/question/2006826244814104012)。海外舆论场持续分化，围绕爱泼斯坦案、政治腐败及社会不公的激烈争论仍在发酵 [⁴](https://twitter.com/elonmusk/status/2023302989872771110)[⁵](https://twitter.com/thejackhopkins/status/2023516999754932398)。
- **经济**：国内政策面延续开放姿态，**中方宣布对英国、加拿大实施单方面免签**，旨在促进国际人员往来 [⁶](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBREdBeGNHbld6ZXhtUmZJQ1FnZ1lleWRBbld0eTlDWm11UkdUZmMzTk43UkFReEVDd3lqYXM3RE9wQ2QtVTNPbG5POGpZWjZvcHJ6RDRR?oc=5)[⁷](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBiTmRySmt3a3MzOGdCWnVHR1BtSXZ3bklIb2Nvci1qTDN6Z0lCUXQ1Ty1IMnVTWmpXZlgzR0Rzc2swS2NlUWxDTFpFWlJvY2o0amZicnB4NlIzREZOQmpoY2tPREl4dw?oc=5)。海外经济信号矛盾，一方面美国住房市场被指达历史“最难以负担”水平 [⁸](https://twitter.com/LeadingReport/status/2023421333477179570)，另一方面日本市场出现**日元与日股相关性自2005年来首次转正**的罕见结构性变化 [⁹](https://twitter.com/KobeissiLetter/status/2023473956674838651)。
- **市场**：报告覆盖时段内，全球市场呈现**结构性分化**。美股内部轮动延续，**罗素2000小盘股指数（+1.18%）** 显著跑赢纳斯达克（-0.22%）[来源ID: 历史报告1]。港股蛇年收官受AI热潮驱动，**MiniMax暴涨25%**、智谱AI涨4.74%齐创新高 [¹⁰](https://wallstreetcn.com/articles/3765773)。A股休市，无有效交易时段数据。
- **科技**：AI领域竞争与安全议题并存。**阿里巴巴开源千问3.5模型**并强调其极低API价格 [来源ID: 历史报告1]。同时，**AI安全与滥用风险凸显**，有指控称AI智能体被用于入侵Palantir系统 [¹¹](https://twitter.com/KimDotcom/status/2023165849721536672)，另有案例显示生成式AI被用于伪造虚假商业差评 [¹²](https://twitter.com/nuknikklgku/status/2023372509819834799)。机器人技术在春晚等场景的应用展示成为热点 [²](https://www.toutiao.com/trending/7607438781827366955/)[³](https://www.zhihu.com/question/2006826244814104012)。

## 二、分板块汇报
### 2.1 市场概况（仅有效交易时段数据）
较上期：延续美股内部从小盘股领涨的轮动格局，并新增港股受AI驱动强势收官的信号。

**发生了什么**：在报告覆盖的有效交易时段内，全球市场分化。美股方面，**罗素2000指数（+1.18%）** 继续大幅跑赢道指（+0.10%）和纳指（-0.22%），延续了从小盘股领涨的轮动 [来源ID: 历史报告1]。亚太市场，**港股蛇年收官表现强劲**，恒生指数具体涨幅未提供，但AI公司**MiniMax股价暴涨25%**、智谱AI涨4.74%并均创新高，同时带动有色板块拉升 [¹⁰](https://wallstreetcn.com/articles/3765773)。欧洲市场涨跌互现，法国CAC40指数微涨0.06% [¹³](https://news.google.com/rss/articles/CBMicEFVX3lxTE9NSm1hMzlXN2hoQmVrOTJ5dXRsWU9YUklIS25NN19xTno0MzBrWDBuM0stYVBEMnBRbkxzODVoWGlQWE1IdVVZWGJsQnkxMjNWY2plVlJXSlhueDVJNUNqbWhyaVN2SXdkZGw5eURYZ2Q?oc=5)。A股处于春节休市期，无有效交易数据。

**为什么会这样（证据强弱：中）**：1) **美股风格轮动延续**：资金从大型科技股（纳指承压）流向中小市值公司（罗素2000走强），可能反映市场在指数高位下寻求更具增长弹性或对国内经济更敏感的标的，此轮动趋势与上期报告一致 [来源ID: 历史报告1]。2) **AI主题驱动港股**：AI热潮是推动港股收官日行情的关键因素，具体公司如MiniMax的暴涨显示市场对AI应用层公司的强烈追捧 [¹⁰](https://wallstreetcn.com/articles/3765773)。对于欧洲及其他市场涨跌的具体驱动因素，输入信息不足。

**下一步观察**：1) 观察美股小盘股相对强势能否在节后首个交易日持续，以及大型科技股对AI领域新动态（如模型开源、安全事件）的反应。2) 关注港股AI板块在春节假期后的资金持续性。3) 等待A股开市后，观察春节期间的社会消费数据及科技热点（如春晚机器人）是否对相关板块形成催化。

### 2.2 微信公众号共识与弱信号
数据不足。输入文本中未提供“微信公众号逐篇简介”或具体的公众号文章内容，无法提炼跨公众号的共识议题或弱信号。需补充信息来源。

### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）
较上期：无显著新增，延续对AI工作流/智能体开发平台的高度关注，金融科技与Web3项目保持稳定。

当前GitHub趋势显示，**AI工作流/智能体开发平台是绝对热点**，但项目间概念重叠度高，存在同质化竞争风险 [¹⁴](https://github.com/Significant-Gravitas/AutoGPT)[¹⁵](https://github.com/langflow-ai/langflow)[¹⁶](https://github.com/langgenius/dify)。最值得关注的项目包括：
1.  **nautechsystems/nautilus_trader (⭐19,761)**：基于Rust的高性能算法交易与回测平台。其应用场景明确服务于量化交易，**可落地价值在于为专业交易团队提供低延迟、高可靠性的策略研发与执行基础设施**，是金融科技领域少有的硬核工具 [¹⁷](https://github.com/nautechsystems/nautilus_trader)。
2.  **langflow-ai/langflow (⭐144,834) 与 langgenius/dify (⭐129,696)**：两者均定位为构建和部署AI驱动代理与工作流的平台。应用场景覆盖企业流程自动化、智能客服、数据分析等。其**可落地价值在于降低AI应用开发门槛，加速企业智能化改造**。主要**噪音风险**在于与n8n等项目功能描述相似，需具体技术细节区分其核心优势，警惕概念炒作 [¹⁵](https://github.com/langflow-ai/langflow)[¹⁶](https://github.com/langgenius/dify)。
3.  **openclaw/openclaw (⭐201,537)**：描述为跨平台个人AI助手。虽然星数最高，但输入信息未提供其具体技术架构或独特功能，**应用场景宽泛，可落地价值不明确**，存在定位模糊的风险，可能只是一个热门概念封装 [¹⁸](https://github.com/openclaw/openclaw)。

### 2.4 Twitter 海外信号（英文内容中文汇报）
较上期：新增对AI安全风险、日本市场结构性变化及美国经济深层矛盾的讨论，爱泼斯坦案相关讨论延续。

海外信号呈现高度情绪化与分化特征，需谨慎甄别：
1.  **AI安全与监控伦理风险激增**：有高互动推文指控**Palantir遭黑客入侵，AI智能体被用于获取超级用户权限**，并发现其进行大规模政商监控 [¹¹](https://twitter.com/KimDotcom/status/2023165849721536672)。同时，有非英文推文警告，商业竞争中利用**生成式AI伪造图片进行虚假差评**以牟利 [¹²](https://twitter.com/nuknikklgku/status/2023372509819834799)。这显示AI技术滥用正从内容生成向商业欺诈、系统入侵等高风险领域蔓延。
2.  **日本市场出现罕见历史信号**：分析师指出，**日元与东证股价指数（Topix）的相关性自2005年以来首次转为正相关**（即同涨）。这一结构性变化可能预示着日本宏观经济或市场逻辑的深层转变，值得高度关注 [⁹](https://twitter.com/KobeissiLetter/status/2023473956674838651)。
3.  **美国经济与社会矛盾信号尖锐但证据弱**：多条推文表达对美国现状的强烈不满，包括：圣路易斯联储报告称**美国住房市场达历史最“难以负担”水平** [⁸](https://twitter.com/LeadingReport/status/2023421333477179570)；有观点认为美国政府正经历“人类历史上最大的抢劫” [¹⁹](https://twitter.com/adamscochran/status/2023492620039946737)；游戏机发售后涨价被视作经济扭曲的“前所未有”信号 [²⁰](https://twitter.com/TheNCSmaster/status/2023511382130671724)。这些信号情绪浓重，多数缺乏具体数据支撑，可信度存疑，但反映了部分群体的普遍焦虑。
4.  **历史恩怨与政治叙事延续**：马斯克提及爱泼斯坦做空特斯拉的旧事 [⁴](https://twitter.com/elonmusk/status/2023302989872771110)，以及关于爱泼斯坦案受害者可能公开揭露的预测 [⁵](https://twitter.com/thejackhopkins/status/2023516999754932398)，均属于延续性社会政治话题，市场直接影响有限。

### 2.5 国内新闻与政策脉络
较上期：春晚的科技展示成为核心社会热点，对外开放政策（免签）获确认，金融产品风险处置出现案例。

国内动态聚焦春节社会热点与政策延续：
1.  **春晚成为科技展示国家级舞台**：**2026年央视马年春晚**是压倒性的舆论中心 [¹](https://www.zhihu.com/question/2006817906369979378)[²¹](https://www.baidu.com/s?wd=%E6%80%BB%E5%8F%B0%E9%A9%AC%E5%B9%B4%E6%98%A5%E6%99%9A)[²²](https://www.douyin.com/hot/2402899)。其核心亮点之一是**科技与内容的深度融合**，特别是宇树科技机器人的武术表演《武 BOT》引发关于技术进步（与去年《秧 BOT》对比）的广泛讨论 [²](https://www.toutiao.com/trending/7607438781827366955/)[³](https://www.zhihu.com/question/2006826244814104012)。这为**机器人、AI生成内容等硬科技赛道提供了极高的品牌曝光和应用场景想象**，有助于提升市场关注度和产业信心。
2.  **对外开放政策落地**：**中方宣布对英国、加拿大公民实施单方面免签政策**得到确认 [⁶](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBREdBeGNHbld6ZXhtUmZJQ1FnZ1lleWRBbld0eTlDWm11UkdUZmMzTk43UkFReEVDd3lqYXM3RE9wQ2QtVTNPbG5POGpZWjZvcHJ6RDRR?oc=5)[⁷](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBiTmRySmt3a3MzOGdCWnVHR1BtSXZ3bklIb2Nvci1qTDN6Z0lCUXQ1Ty1IMnVTWmpXZlgzR0Rzc2swS2NlUWxDTFpFWlJvY2o0amZicnB4NlIzREZOQmpoY2tPREl4dw?oc=5)。此举旨在促进国际人员往来，服务于更高水平对外开放，**对文旅、航空及高端消费服务业构成长期利好**。
3.  **金融产品风险处置案例**：**国投白银LOF出台了行业首例补偿方案**，对1000元以下损失进行全额补偿 [²³](https://www.cls.cn/detail/2290657)。这反映了监管层及金融机构在应对产品净值波动、维护投资者权益方面的积极姿态，有助于稳定市场情绪，但个案不代表普遍模式。
4.  **产业观点与风险提示**：有观点指出科技产业需在“速度”和“泡沫”中找平衡 [²⁴](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1FN1pzQUhiTlRHQVJBajFLOFBkc0FCbnpOeXBiTThLNXFFY29Zb3ZkZEtfMl82UTNzMWV0dV83alpwUWlFcWJvYjVtNkpQcDRyalp4RWhxWG9KRTYtNHc?oc=5)，同时“AI电荒”推高燃气轮机需求至“极其旺盛” [²⁵](https://wallstreetcn.com/articles/3765768)。这提示AI高歌猛进的同时，需关注其带来的能源成本与基础设施压力。

## 三、明日跟踪清单
1.  **延续跟进：美股风格轮动的持续性**：观察**罗素2000指数相对纳斯达克的强势**在节后是否延续，并关注Palantir被黑等AI安全事件对相关科技股的影响 [¹¹](https://twitter.com/KimDotcom/status/2023165849721536672)。
2.  **收口复盘：国内春节消费与科技热点反馈**：关注A股开市后，**大消费板块**对春节假期数据的反应，以及**机器人、AI**等受春晚催化的科技板块能否获得资金青睐 [²](https://www.toutiao.com/trending/7607438781827366955/)[³](https://www.zhihu.com/question/2006826244814104012)。
3.  **新增观察：日本市场结构性变化的验证**：紧密跟踪**日元与日股（如Topix指数）的正相关性**是否持续，并探究其背后的宏观政策（如央行）或资金流动原因 [⁹](https://twitter.com/KobeissiLetter/status/2023473956674838651)。


---

<details><summary>📑 点击展开各板块详细分析</summary>

### 📊 市场数据详细分析

### 主要市场走势判断
在报告覆盖时段内，全球主要股市呈现**分化**格局。美股整体微幅上行，但内部结构不一，其中**罗素2000指数（+1.18%）** 表现显著强于大盘指数。欧股涨跌互现，亚太市场除港股外普遍收跌。**A股（-1.26%）** 和**德国DAX指数（-0.46%）** 是主要下跌市场。整体风险偏好呈现结构性特征，而非普涨或普跌。

### 关键资产轮动分析
*   **领涨方向**：
    1.  **美股中小盘股**：**罗素2000指数（+1.18%）** 的涨幅远超道指（+0.10%）和纳指（-0.22%），显示资金在美股内部向**中小市值公司**轮动。这可能反映了市场在主要股指高位震荡时，寻求更具增长潜力的标的，或是对美国国内经济前景的特定押注。
    2.  **原油**：**WTI原油（+1.37%）** 与**布伦特原油（+1.21%）** 同步上涨，在商品中表现突出，显示有资金流入能源板块。
    3.  **以太坊（ETH）**：在主要加密货币中，**ETH（+1.65%）** 涨幅领先，表现强于BTC（+0.10%）和SOL（+0.63%），显示加密市场内部资金向特定主流资产倾斜。

*   **领跌方向**：
    1.  **天然气**：**天然气（-4.59%）** 是报告期内跌幅最大的主要商品，与原油走势形成鲜明反差。
    2.  **A股与部分欧亚股指**：**上证综指（-1.26%）** 跌幅居前，**德国DAX（-0.46%）**、**日经225（-0.24%）** 和**韩国综合指数（-0.28%）** 也录得下跌，显示亚太和欧洲部分市场承压。

*   **资金偏好解读**：
    资金偏好呈现**“避险与风险并存”** 的复杂特征。一方面，资金流入原油和美股中小盘，显示一定的风险承担意愿；另一方面，**VIX波动率指数（+2.91%）** 的上升，以及主要股指的窄幅震荡，又表明市场整体情绪**偏向谨慎**。资金在板块和区域间进行快速轮动，而非单向流动。

### 加密货币和商品期货的关键变化
*   **加密货币**：市场整体波动不大，BTC近乎平盘，ETH录得超过1.5%的涨幅，成为相对强势资产。SOL小幅跟涨。数据未提供驱动ETH走强的具体原因。
*   **商品期货**：
    *   **能源**：**原油价格显著上涨**（WTI +1.37%，布伦特 +1.21%），而**天然气价格大幅下挫**（-4.59%），二者走势完全背离，表明驱动因素并非宏观能源需求预期，而是各自独立的供需基本面。
    *   **工业金属**：**COMEX铜（-0.53%）** 小幅下跌，与全球股市分化格局及A股下跌可能反映的全球增长担忧情绪有一定吻合。

### 涨跌驱动链条分析
基于现有数据，可推断以下部分驱动链条，但需注意证据强度有限：

1.  **事件/政策/情绪**：数据未提供明确的宏观事件或政策信息。
2.  **资金行为 -> 价格表现**：
    *   **证据较强**：
        *   资金从大型科技股（纳指下跌）流向中小盘股（罗素2000大涨），导致**美股内部风格显著分化**。
        *   资金在商品市场进行**跨品种调仓**，同时买入原油、卖出天然气，导致二者价格走势背离。
        *   资金在加密市场**偏好ETH**，使其表现优于其他主要加密货币。
    *   **证据较弱/需更多信息**：
        *   **VIX指数上升（+2.91%）** 结合主要股指窄幅震荡，可能反映了市场在关键点位前的**犹豫和焦虑情绪**，但这种情绪并未引发广泛的抛售（仅5/12指数下跌）。
        *   A股、德国DAX等市场的下跌，可能与区域性或行业性因素有关，但数据未提供具体原因，无法建立明确驱动链。

**总结**：报告时段内，市场缺乏统一的宏观叙事驱动。资金行为呈现**结构性特征**，在美股内部进行风格切换（从小盘股），在商品市场进行品种切换（多原油、空天然气），在加密市场进行资产切换（多ETH）。整体市场情绪谨慎（VIX上升），但并未形成恐慌性抛售。对于A股、欧股下跌以及原油上涨的具体原因，**数据不足**，无法做出进一步判断。

### ⏱ 市场时效过滤说明

市场时效过滤结果：
1. 早报阶段不纳入 A 股盘面，避免使用非交易时段快照

### 🐦 Twitter 逐条简介

Twitter 逐条简介（共 12 条，按互动热度排序）：
1. [热门] @KimDotcom | 2026-02-17T00:00 | 互动=94126
   原文摘录: Breaking Palantir was allegedly hacked. An AI agent was used to gain super-user access and here”s what the hackers allegedly found: Peter Thiel and Alex Karp co
   原文链接: [点击查看原文](https://twitter.com/KimDotcom/status/2023165849721536672)
   1) 讲了什么：据称Palantir被黑，黑客发现其大规模监控政商领袖并积累勒索材料。
   2) 关键信号：指控涉及监控特朗普等人物、为乌克兰开发生化核能力、与CIA合作。
   3) 阅读建议：略读 + 原因：信息源自单一推文且为指控，未提供证据或第三方验证。
2. [热门] @elonmusk | 2026-02-17T00:00 | 互动=86784
   原文摘录: Yup 😂 That really made him upset. After I ghosted him, Epstein went on a massive campaign to short Tesla and got Gates to short 1% of Tesla stock when the marke
   原文链接: [点击查看原文](https://twitter.com/elonmusk/status/2023302989872771110)
   1) 讲了什么：马斯克称爱泼斯坦做空特斯拉并拉盖茨做空1%股份，盖茨可能仍持有空头。
   2) 关键信号：指控爱泼斯坦与盖茨做空特斯拉，市场市值400亿美元时做空。
   3) 阅读建议：略读 + 原因：仅为个人指控，未提供独立证据或新数据。
3. [热门] @TBSCDTV | 2026-02-17T00:00 | 互动=25333
   原文摘录: #CDTVライブライブ3月9日(月)よる7時⚡️ ＼👑豪華出演者発表🌟／#AI「ラッキーアイラブユー」#WEST.「これでいいのだ！」#キタニタツヤfeat.#BABYMETAL「かすかなはな」#GENERATIONS「本心」#中島健人「XTC」「IDOLIC」#MILK「爆裂愛してる」#TBS
   原文链接: [点击查看原文](https://twitter.com/TBSCDTV/status/2023365491948245021)
   1) 讲了什么：TBS电视台预告3月9日晚7点直播节目，并公布了豪华出演者名单。
   2) 关键信号：节目涉及多位艺人及AI，主题标签包含#CDTVライブライブ。
   3) 阅读建议：略读 + 原因：内容为特定娱乐节目预告，与金融科技直接关联未提供。
4. [热门] @SpacemanAp | 2026-02-17T00:00 | 互动=21294
   原文摘录: Western media won’t air this bc they don’t want you to grow a brain & realize “wait, I can shut down the economy. All the wealth is built off my labor. I can ow
   原文链接: [点击查看原文](https://twitter.com/SpacemanAp/status/2022438260275056995)
   1) 讲了什么：推文批评西方媒体不播放特定内容，并讨论劳工对经济与财富的作用。
   2) 关键信号：未提供具体事件或数据，仅表达观点。
   3) 阅读建议：略读 + 原因：内容为个人观点陈述，无具体事实或数据支撑。
5. [热门] @LeadingReport | 2026-02-17T00:00 | 互动=16797
   原文摘录: BREAKING: US housing market reaches most “unaffordable” level in history, per St. Louis Fed report.
   原文链接: [点击查看原文](https://twitter.com/LeadingReport/status/2023421333477179570)
   1) 讲了什么：圣路易斯联储报告称美国住房市场达到历史最“难以负担”水平。
   2) 关键信号：数据不足/未提供。
   3) 阅读建议：略读 + 原因：仅提供单一机构结论，无具体数据或背景。
6. [热门] @Flicky0ps | 2026-02-17T00:00 | 互动=16797
   原文摘录: i will never get over the fact that people now associate em dashes and semicolons with ai like god forbid a girl likes to read sorry i’m literate
   原文链接: [点击查看原文](https://twitter.com/Flicky0ps/status/2023455023112614236)
   1) 讲了什么：用户对人们将破折号和分号与AI关联表示不满。
   2) 关键信号：推文互动数据高，表达了对语言使用被标签化的情绪。
   3) 阅读建议：略读 + 原因：内容为个人情绪表达，与金融科技直接关联未提供。
7. [热门] @nuknikklgku | 2026-02-17T00:00 | 互动=12839
   原文摘录: เตือน‼️ เจ้าของกิจการจังหวัดท่องเที่ยว อีพวก Israeli มีทริคใหม่คือ gen ai เอารูปไม่จริงมารีวิวให้ 1 ดาว จะขอเงินคืน อีชนชาติสัตว์หมานรกนี่ ถ้ารัฐบาลจะทบทวนฟรีวี
   原文链接: [点击查看原文](https://twitter.com/nuknikklgku/status/2023372509819834799)
   1) 讲了什么：推文警告旅游企业，称有以色列人用AI生成虚假图片写差评以索要退款。
   2) 关键信号：未提供具体数据或事件，仅为个人指控。
   3) 阅读建议：略读 + 原因：内容为主观情绪化指控，缺乏可验证事实。
8. [热门] @SJallamion | 2026-02-17T00:00 | 互动=7805
   原文摘录: J’ai exercé mes fonctions en tant qu’Officier de Police Judiciaire à Lyon pendant 17 ans. Jamais, je dis bien JAMAIS, je n’ai connu d’affaire criminelle où une 
   原文链接: [点击查看原文](https://twitter.com/SJallamion/status/2023391996652449798)
   1) 讲了什么：前警官质疑里昂检方在嫌犯被捕前召开身份确认记者会的做法。
   2) 关键信号：作者称17年职业生涯从未见过此类程序，并用标签呼吁正义。
   3) 阅读建议：略读 + 原因：此为个人观点陈述，未提供具体案件细节或数据。
9. [热门] @adamscochran | 2026-02-17T00:00 | 互动=7248
   原文摘录: Between the stock market, national secrets, and billions in self-dealing government contracts, people do not realize just how looted and ransacked the US govern
   原文链接: [点击查看原文](https://twitter.com/adamscochran/status/2023492620039946737)
   1) 讲了什么：推文称美国政府正被掠夺，涉及股市、国家机密和巨额自利合同。
   2) 关键信号：作者认为这是人类史上最大抢劫，但多数人未察觉。
   3) 阅读建议：略读 + 原因：仅为个人观点陈述，未提供具体证据或数据。
10. [热门] @TheNCSmaster | 2026-02-17T00:00 | 互动=4804
   原文摘录: It still doesn’t feel like it’s emphasized enough how fucked the economy and tech prices are that video game consoles are increasing in price post launch Like t
   原文链接: [点击查看原文](https://twitter.com/TheNCSmaster/status/2023511382130671724)
   1) 讲了什么：用户认为游戏机发售后涨价史无前例，反映经济和科技价格问题严重。
   2) 关键信号：游戏机发售后涨价被描述为“史无前例”。
   3) 阅读建议：略读 + 原因：仅为个人观点，未提供具体数据或事件支撑。
11. [热门] @thejackhopkins | 2026-02-17T00:00 | 互动=4566
   原文摘录: I have a prediction: Sooner than later, one of Epstein’s victims is going to get fed up with the slow-walking BS, step to a mic, and light a match that sets pro
   原文链接: [点击查看原文](https://twitter.com/thejackhopkins/status/2023516999754932398)
   1) 讲了什么：预测爱泼斯坦案受害者将公开揭露真相，引发重大影响。
   2) 关键信号：受害者对拖延不满，可能公开行动，系统拖延会触发事件。
   3) 阅读建议：略读 + 原因：仅为个人预测，无具体事件或数据支撑。
12. [热门] @EricLDaugh | 2026-02-17T00:00 | 互动=4219
   原文摘录: 🚨 BREAKING: President Trump drops BOMB on the Democrats for President’s Day, they can’t stand the winning “Happy President’s Day! Prices and Inflation are Way D
   原文链接: [点击查看原文](https://twitter.com/EricLDaugh/status/2023479635153916290)
   1) 讲了什么：特朗普在总统日发表推文，列举多项积极数据并祝民众节日快乐。
   2) 关键信号：声称物价、通胀下降，股市、军力、执法、边境安全及国家状态均表现优异。
   3) 阅读建议：略读 + 原因：内容为单方面宣传性声明，未提供具体数据或事件支撑。

### 🌐 Twitter 英文信号详细分析

### 海外英文信号主线
*   **科技巨头与政治监控指控**：有指控称Palantir被黑客攻击，发现其联合创始人Peter Thiel和Alex Karp对世界领导人和行业巨头进行大规模监控。
*   **历史恩怨与市场操纵指控**：埃隆·马斯克提及杰弗里·爱泼斯坦曾因个人恩怨大规模做空特斯拉，并称比尔·盖茨至今仍持有特斯拉空头头寸。
*   **美国经济与社会矛盾**：信号显示对美国现状的强烈不满，包括：美国住房市场达到历史“最难以负担”水平；有观点认为美国政府正经历“人类历史上最大的抢劫”，涉及股市、国家机密和政府合同；游戏机在发售后涨价被视作经济与科技价格扭曲的 unprecedented（前所未有）信号。同时，有观点批判资本主义体系，认为劳动者应掌控自身劳动价值。
*   **地缘与市场动态**：日本市场出现罕见信号，日元与东证股价指数（Topix）的相关性自2005年以来首次转为正相关，即同向上涨。乌克兰方面强调需要“新工业化”并获取现代技术。

### 与金融科技/AI/Web3相关的具体线索
*   **AI安全与滥用**：有指控称AI智能体被用于入侵Palantir系统以获取超级用户权限。另有非英文信号提及，有商业实体利用生成式AI（gen ai）伪造图片进行虚假差评以牟利。
*   **AI产品发布**：NVIDIA发布了名为PersonaPlex-7B的实时语音对话模型，据称为免费开源。
*   **创作者经济与AI娱乐**：有活动将探讨创作者主导经济下的货币化新时代。另有信号提及涉及高性能AI主播的娱乐角色。

### 可执行关注点与潜在误导噪音
*   **可执行关注点**：
    1.  **监控科技伦理风险**：关注围绕Palantir等数据公司的黑客事件与监控指控可能引发的监管审查与公众信任危机。
    2.  **日本市场结构性变化**：关注日元与日股相关性转正这一罕见历史信号是否预示日本宏观经济或市场逻辑的深层转变。
    3.  **AI工具的双刃剑效应**：关注开源AI语音模型（如PersonaPlex-7B）的普及，同时警惕生成式AI在商业竞争中被用于虚假信息攻击的案例。
*   **潜在误导噪音**：
    1.  **未经证实的重磅指控**：关于Palantir大规模监控、美国政府被“抢劫”等描述均来自单一社交媒体指控，缺乏事实核查与官方证实，需高度警惕其真实性。
    2.  **个人叙事与市场解读**：马斯克提及的爱泼斯坦与盖茨做空特斯拉属于个人历史陈述，无法核实其当前市场头寸与影响，不宜作为直接的投资依据。
    3.  **情绪化与阴谋论内容**：多条信号包含强烈的政治立场与阴谋论色彩（如“深层政府”掩盖行动、50年去工业化阴谋），信息可信度低，应视为情绪噪音而非有效情报。
    4.  **数据不足领域**：关于“游戏机涨价”的具体产品、幅度及经济影响，输入文本未提供详细数据。

### 📰 热榜详细分析

# 热榜综合分析报告

## 1. 跨平台共同关注的3-5个热点事件
1.  **2026年央视马年春晚**：这是覆盖所有分片的绝对核心热点。讨论焦点包括节目单发布、收视率、具体节目内容（如沈腾、马丽与银河通用机器人合作的微电影、王菲表演、机器人武术表演《武 BOT》）、演员造型（如尼格买提、迪丽热巴妆容），以及“科技与内容深度融合”的现象（机器人同台、AI参与制作）。
2.  **AI与机器人技术的突破与展示**：多个分片提及AI大模型发布（如阿里千问3.5）及机器人在春晚等场景的应用（如宇树科技机器人表演《武 BOT》、银河通用机器人亮相），引发关于技术变革和社会应用的广泛讨论。
3.  **谷爱凌冬奥摘银**：在自由式滑雪女子大跳台项目中获得银牌并创造奖牌纪录，是多个分片提及的体育热点。
4.  **国际政治动态**：包括俄乌冲突相关动态（英国防卫大臣称俄军伤亡惨重并有朝鲜军人参战）、美伊谈判风险增加、中日外交交涉（日方提出交涉，中国使馆驳回）等事件受到关注。

## 2. 与金融市场相关的重要新闻
*   **具体事件**：
    *   **白银基金补偿方案**：国投白银LOF出台行业首例补偿方案，对1000元以下损失进行全额补偿，2月26日可办理。分片6同时提及个人投资者“负债小白梭哈白银遭胖揍”的案例。
    *   **AI驱动港股行情**：AI热潮推动港股蛇年收官，AI公司MiniMax股价暴涨25%，智谱AI涨4.74%，均创新高，并带动有色板块。
    *   **存储芯片市场风险**：有分析称存储芯片市场“走向失控”。
    *   **金融机构活动**：春节期间券商电话会近300场，显示机构在假期保持活跃。
*   **观点与趋势**：
    *   **达利欧宏观判断**：桥水创始人认为旧秩序已死，世界重回“丛林法则”，贸易战和资本战将成常态。
    *   **“木头姐”对市场波动的归因**：ARK Invest创始人认为当前市场波动由算法交易导致，而非基本面。
    *   **产业需求**：“AI电荒”将燃气轮机需求推至“极其旺盛”，龙头企业交付已排到2030年。
*   **其他线索**：输入文本提及“新春伊始的人民币升值现象”和“习近平主席指出当前经济工作的重点任务”，但具体内容与数据未提供。

## 3. 科技/AI 相关热点
*   **大模型发布与竞争**：**阿里巴巴开源千问3.5模型**，宣称其性能媲美Gemini 3 Pro，实现了原生多模态的代际跃迁，且Token价格仅为后者的1/18。国产大模型在春节期间竞速AI编程。
*   **AI的能源与硬件影响**：“AI电荒”现象被明确提出，显示AI算力增长强力拉动了燃气轮机等能源装备的需求。
*   **机器人技术落地与展示**：机器人成为春晚科技焦点，从去年的《秧 BOT》到今年的《武 BOT》，表演“中国功夫”，并探讨其“能演亦能干”的应用前景。银河通用机器人亮相春晚微电影。
*   **AI对行业的影响讨论**：包括AI视频工具（如Seedance 2.0）可能导致导演失业的担忧，以及虚拟歌手（洛天依）作品抄袭的界定问题。
*   **人才流动与产品目标**：OpenClaw创始人加入OpenAI，目标是开发“连妈妈都能用的AI助手”。
*   **其他线索**：输入文本提及“AI遇上最强春节档”涉及Token通胀，以及“大国重器硬核拜年”，但具体关联与内容未提供。

## 4. 社会舆论焦点
*   **核心焦点**：**2026年春晚**是压倒性的舆论中心，涵盖节目评价、文化现象（如“不看春晚开电话会”）、科技融合等多个维度。
*   **春节档电影**：2026年春节档电影票房（含预售突破6亿，《飞驰人生3》预售破2亿）受关注。
*   **娱乐与网络争议**：虚拟歌手洛天依新歌被曝抄袭并已处理相关人员；“软饭男喊冤”成为贴吧热门话题；游戏存档误删、Steam平台内容争议等。
*   **社会议题与生活方式**：包括“过年点外卖是否给骑手添麻烦”的伦理讨论、“炖肉浮沫是营养精华”的辟谣、对群发祝福的看法、年轻人去大城市的原因等。
*   **两岸与国际话题**：台湾地区政治人物（张善政、马英九、蒋万安）在除夕活动中的连线受关注；中国学者在慕安会驳斥“中国威胁论”；希拉里与捷克副总理争吵等国际摩擦也有提及。
*   **其他焦点**：“凤凰传奇”新广场舞曲及形象引发热议；历史剧《大明王朝》生活细节真实性的讨论；奥巴马称外星人存在等话题也有一定讨论度。关于“高市早苗迎来坏消息”及“闯岛救人”的具体内容，输入信息不足。

### 💻 GitHub 项目详细分析

# GitHub热门项目技术趋势分析

## 一、最值得关注的项目

基于项目热度（Star数）与主题代表性，筛选出以下7个核心项目：

**金融科技 (FinTech)**
1. **nautechsystems/nautilus_trader** (⭐19,761): 基于Rust的高性能算法交易平台和事件驱动回测器。
2. **SimplifyJobs/New-Grad-Positions** (⭐16,284): 面向新毕业生的软件工程、量化、产品管理等全职职位集合。

**人工智能 (AI)**
3. **openclaw/openclaw** (⭐201,537): 跨OS和平台的个人AI助手。
4. **n8n-io/n8n** (⭐174,812): 具备原生AI能力的公平代码工作流自动化平台，支持400+集成。
5. **langflow-ai/langflow** (⭐144,834): 用于构建和部署AI驱动代理与工作流的强大工具。
6. **langgenius/dify** (⭐129,696): 面向智能体工作流开发的生产就绪平台。

**Web3**
7. **ethereum-optimism/optimism** (⭐6,376): 以太坊扩容方案。

## 二、应用场景与落地价值分析

*   **金融科技**：
    *   **nautilus_trader**：服务于量化交易团队与个人交易者，提供高性能、低延迟的交易执行与策略回测环境，直接对应自动化交易场景，落地价值在于提升策略研发与执行的效率与可靠性。
    *   **New-Grad-Positions**：作为求职信息聚合工具，服务于应届毕业生与招聘方，落地价值在于降低信息不对称，但其本身并非技术产品，而是资源列表。

*   **人工智能**：
    *   **openclaw**：定位为通用个人AI助手，潜在应用场景广泛，但具体功能与差异化价值数据不足/未提供。
    *   **n8n**、**langflow**、**dify**：三者均聚焦于**AI工作流/智能体开发与自动化**。n8n强调与现有业务系统的可视化集成；langflow和dify则更专注于AI原生应用的构建。其落地价值在于降低企业或开发者构建复杂AI应用的门槛，实现业务流程的智能化改造。

*   **Web3**：
    *   **optimism**：作为以太坊Layer 2扩容解决方案，应用场景是提升以太坊网络交易吞吐量、降低费用，落地价值在于改善区块链应用的用户体验和可扩展性。

## 三、潜在泡沫噪音与重复概念

1.  **AI工作流平台概念重复**：**n8n**、**langflow**、**dify** 在核心功能描述上存在显著重叠（工作流、智能体、开发平台），可能反映了当前市场的热点集中度，存在同质化竞争与概念炒作的风险。需要具体功能细节以区分其核心差异。
2.  **部分项目定位模糊**：**openclaw** 描述为“个人AI助手”，但未提供具体技术架构或独特功能，可能只是一个宽泛的概念封装。
3.  **金融科技项目样本偏差**：列表中部分项目（如 `free-v2ray-public-list`）与金融科技核心关联性弱，而 `New-Grad-Positions` 是资源列表而非技术项目，可能影响对金融科技真实技术趋势的判断。
4.  **通用开发项目界定**：`tensorflow` 作为机器学习框架被归类为“通用开发”，而 `nearcore` 作为区块链客户端被归类为“通用开发”，此分类标准与项目实际技术领域（AI、Web3）存在交叉，可能造成分析噪音。

**结论**：当前趋势显示，**AI工作流/智能体开发平台**是绝对热点，但项目间概念重叠度高。金融科技领域的高性能交易基础设施和Web3的扩容方案仍是持续发展的刚需方向。需警惕AI赛道可能出现的概念泡沫。

### 🌐 联网检索摘要

联网检索共 19 条（关键词: 2026-02-17 全球市场 盘面 复盘 原因, 2026-02-17 中国 宏观 经济 政策 市场 影响, 2026-02-17 AI 科技 行业 动态 影响, VIX波动率指数 上涨 原因, ETH 上涨 原因, 2026 年央视春晚中有哪些亮点？哪个节目最让你印象深刻？ 事件 背景, 春晚机器人中国功夫夯爆了 事件 背景, 总台马年春晚 事件 背景）
1. [2026-02-17 07:54] thepaper.cn | 城市年鉴2025｜科技产业：“速度”和 “泡沫”中找平衡 - thepaper.cn
   摘要: 城市年鉴2025｜科技产业：“速度”和 “泡沫”中找平衡 thepaper.cn
   链接: https://news.google.com/rss/articles/CBMiXkFVX3lxTE1FN1pzQUhiTlRHQVJBajFLOFBkc0FCbnpOeXBiTThLNXFFY29Zb3ZkZEtfMl82UTNzMWV0dV83alpwUWlFcWJvYjVtNkpQcDRyalp4RWhxWG9KRTYtNHc?oc=5
2. [2026-02-17 07:46] thepaper.cn | 首席展望｜中欧基金任飞：周期板块将迎量价共振，看好有色、新能源及化工 - thepaper.cn
   摘要: 首席展望｜中欧基金任飞：周期板块将迎量价共振，看好有色、新能源及化工 thepaper.cn
   链接: https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wdlNqdllSZTB6NUVwMEtUQnM1R1gyOVlodzF6cDNCcTEzRzlkLW5tZEhiODI0UW5SZHJHS0c1NWF1QkxvWXUzMFlXOW5jenZ1V3RpWWxHenFpZ1JTQmVVTg?oc=5
3. [2026-02-17 07:35] 新浪财经 | 新浪财经隔夜要闻大事汇总：2026年2月17日|债券市场|金融市场|原油期货|宇树科技|惊蛰无声_手机新浪网 - 新浪财经
   摘要: 新浪财经隔夜要闻大事汇总：2026年2月17日|债券市场|金融市场|原油期货|宇树科技|惊蛰无声_手机新浪网 新浪财经
   链接: https://news.google.com/rss/articles/CBMijgJBVV95cUxPSmczWGVmS3U1YThtMExmdlFPaVgwNkcxT3BFZjd5dFZ5MWhKM1hBY1IxdVg4QjR5MmNPVmVjWXhldUhkMlU2S2RLLVlwcXRjaF9zME5VMmJmMUdFWDdLVFZzSk1wbkQzT3V6M0htdWh3OUhiYi03NC11MjcxUEp0UEFEenR6N1h2QXZ2cTgxQTloWG9Zb2xTM2JsV0hBUlZVVVRrYWlqcE9oQVJ6dHZLdURjdUo0TGxIQmtvekZJMVFmSTAtWmd1RU1fYUpRaDFrVHZUemp5TGZXVktvYkl3VGJmUHFGSFVtYkw3a2VEblVVSzE0ZGR1Umw0bVoxNlFwMGFsaV9faWh4VmczbVE?oc=5
4. [2026-02-17 07:01] 新浪财经 | 2026新年献词|景顺长城基金总经理康乐：主动有为，静待春来 - 新浪财经
   摘要: 2026新年献词|景顺长城基金总经理康乐：主动有为，静待春来 新浪财经
   链接: https://news.google.com/rss/articles/CBMiigJBVV95cUxQdENIeW1LUzV2WjZhX2FEVnpSTEJyeDFhajFDTVhqT0lDMUZQeDV5aTJwSFBUZzk0aHhNQXF0NmN1WXhrcUxQYXZBX1FXUkF1RFR4VGZ1NXFSWHdkM1pHRzNxSGZPX1AyU3IyOWZ6akFJNDg3R2gxUEM4SDZVM1JGTGU5eXE2S21lUHJNT2stU1pZakJKaWNFTzZTT0hhOEtaTmkxQWlDSEFLTkxlMm9ndTR4b0JBZ2pkTWt1b21yU0I3dWw4TVFHaWt6cnI5MWMxYkx0M0Vmb2FiSEFFUmRFODBMTjRBQTVlUGRfTUN2U3Z0ejlkU1ZWTm0zcXBrSHVDUVZNTEZpdW1VQQ?oc=5
5. [2026-02-17 01:05] 英为财情 Investing.com | 法国股市上涨；截至收盘法国CAC40指数上涨0.06% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 法国股市上涨；截至收盘法国CAC40指数上涨0.06% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTE9NSm1hMzlXN2hoQmVrOTJ5dXRsWU9YUklIS25NN19xTno0MzBrWDBuM0stYVBEMnBRbkxzODVoWGlQWE1IdVVZWGJsQnkxMjNWY2plVlJXSlhueDVJNUNqbWhyaVN2SXdkZGw5eURYZ2Q?oc=5
6. [2026-02-17 00:51] 新浪财经 | 骐骥驰骋 势不可挡 总台马年春晚精彩上演 - 新浪财经
   摘要: 骐骥驰骋 势不可挡 总台马年春晚精彩上演 新浪财经
   链接: https://news.google.com/rss/articles/CBMiiAJBVV95cUxPMFBUSUVpOVdBTGRhdXQyMUFQaUNRTUJlaUdtVHFrUmdwX2dTellONzI0d3VQeS1FQTVlMzVZZXNVdURPUGZPS3R5Rk5scGlvVjRWQ00zU1VSbWVlajJYV3RXUFJSQjRLVlhUeGJHUVpHM3BPNFVrel9iSDhaOThGMUpZM3VKekNabWJ6eWlFYXJuMGduVms0Y2c2aHJQMkxZMDV1NVFqZGRacXlkQWJjY3RYcHBFV3pMSVJMMnpXQVBvcm0tZXdyT0tTQWtBSWQ5cDd6UDJYNVhpX3NEaTgwTkd3VzlJUThtVlFQR0xsbXY5QW8yQTBET3hUNFM4VzNyZUMyRjBndEs?oc=5
7. [2026-02-17 00:34] SOHU | 华米科技：AI眼镜量产、业绩指引与股价波动引关注 - SOHU
   摘要: 华米科技：AI眼镜量产、业绩指引与股价波动引关注 SOHU
   链接: https://news.google.com/rss/articles/CBMihwFBVV95cUxQNnBkMnZsZlMyRzU0LUdPODFPLVB4ZjlXTWptUVBHMHpYdVRTSFg2dHMzQ19LWjY0NlRCU0I2UGUwcFZURmhBWUg4TXZXUU1wckctc2JKUmVLcjRLMmxjbDhCcHNKcEhNeEVCMWY0XzhteEJORWJrcVJNRlowVkl0TkluV0YtSTA?oc=5
8. [2026-02-16 20:01] 中华网 | 总台马年春晚 看点满满迎新春 - 中华网
   摘要: 总台马年春晚 看点满满迎新春 中华网
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTFBmdktjcWV1MnBvUnlGQW1uWTlxS2w3UUZOSl9qNkk0cHVxLTRiNjR0WHFyZDNpSkdJam9ka1FGakJyUU1JTjJxMjNvaXRlNUZubGRDUWZEemgtYU9XM0pBdlp1YVJ4bWhYZ1ZadWJYNk0?oc=5
9. [2026-02-16 20:00] 央视网 | 欢乐吉祥 喜气洋洋 总台《2026年春节联欢晚会》等着您 - 央视网
   摘要: 欢乐吉祥 喜气洋洋 总台《2026年春节联欢晚会》等着您 央视网
   链接: https://news.google.com/rss/articles/CBMid0FVX3lxTE5Xa25JdVc1SVROOW8wcmhRVDJNLTJub3RzWWMxakUxTVBBaGhlQ3BTYkEyTWFpUXAxWTJ5UWRRUlBwQUZlZnRCZjYzUmZ1ZmhUYjBnREg1Y2RucUUyMVNHUmF2LU1vY2RYSkVWeHN0NmVTdWtPcnFJ?oc=5
10. [2026-02-16 16:49] yeeyi | 重磅喜讯！中国官宣免签扩大！贸易谈判推进！从机票到车价都可能被改写！两大政策进展背后，普通人最该关注的现实影响全解读...-yeeyi - yeeyi
   摘要: 重磅喜讯！中国官宣免签扩大！贸易谈判推进！从机票到车价都可能被改写！两大政策进展背后，普通人最该关注的现实影响全解读...-yeeyi yeeyi
   链接: https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBREdBeGNHbld6ZXhtUmZJQ1FnZ1lleWRBbld0eTlDWm11UkdUZmMzTk43UkFReEVDd3lqYXM3RE9wQ2QtVTNPbG5POGpZWjZvcHJ6RDRR?oc=5
11. [2026-02-16 15:04] Traders Union | Ethereum 下跌 5.71%，原因是 FinCEN 加大执法力度，看跌信号占主导地位 - Traders Union
   摘要: Ethereum 下跌 5.71%，原因是 FinCEN 加大执法力度，看跌信号占主导地位 Traders Union
   链接: https://news.google.com/rss/articles/CBMipgFBVV95cUxPdTVsdTFlanJBNnVHREVVOW9rRm9BQTZ0S1FJdFNGVDVCUEN0MEtqZTcxbjlMQ2ZiNVRoMDhUWUlzSGhDTTN4a0VnZFdpY1V4VjJFRlMtVVpaazkwRVNVandnRVlKYV9ySm9QQTF5UDIxbC1Sa09VbUpBbkY5eWRLOWFEcFNRaFJjMVNiY2E4OXU0NXNHekQ0N05yZ1dmY0FacEYwbHdR?oc=5
12. [2026-02-16 13:30] 英为财情 Investing.com | 澳大利亚股市上涨；截至收盘澳大利亚S&P/ASX200指数上涨0.22% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 澳大利亚股市上涨；截至收盘澳大利亚S&P/ASX200指数上涨0.22% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTFBXTkxGWWlpT2VIRnhZRTFVUEtLUnZxQUNJRW1TMXVDZTBIWWdRbWItUUFOTHBuUHNEbTNYT0VxbmhWZ19ZQkhGMWpRVk9JTVNoZ3BMOUl2b0E5Zmh4blpZNjRaTnNEUkFhbFBSOER5M1U?oc=5
13. [2026-02-16 12:05] FX168财经 | 7张图表，说明为何美股的压力山大 - FX168财经
   摘要: 7张图表，说明为何美股的压力山大 FX168财经
   链接: https://news.google.com/rss/articles/CBMia0FVX3lxTE01SHBRTzRiTkV0cXhuV1R2RFA3RzJfRndYUFkzUXlJSC1hVG1nVVViNGg4UE9VSWF0MzZHckpoNHdHLUVQeFp3eDJSNjZnWmp2NjZXeHhlU1dBV0ktd2JFcGRoUWtpaHJpbF9N?oc=5
14. [2026-02-16 07:58] 每日经济新闻 | 江苏连云港一烟花零售店爆炸致8人遇难2人受伤，应急管理部紧急召开调度会；中方宣布对英、加免签；马斯克：Grok 4.20本周发布丨每经早参 - 每日经济新闻
   摘要: 江苏连云港一烟花零售店爆炸致8人遇难2人受伤，应急管理部紧急召开调度会；中方宣布对英、加免签；马斯克：Grok 4.20本周发布丨每经早参 每日经济新闻
   链接: https://news.google.com/rss/articles/CBMiZkFVX3lxTFBiTmRySmt3a3MzOGdCWnVHR1BtSXZ3bklIb2Nvci1qTDN6Z0lCUXQ1Ty1IMnVTWmpXZlgzR0Rzc2swS2NlUWxDTFpFWlJvY2o0amZicnB4NlIzREZOQmpoY2tPREl4dw?oc=5
15. [2026-02-16 07:42] FX168财经 | 财经早餐：本周A股开启“春节休假”模式，DeepSeek V4或将发布，国投白银LOF出台补偿方案，超九成投资者将获全额补偿 - FX168财经
   摘要: 财经早餐：本周A股开启“春节休假”模式，DeepSeek V4或将发布，国投白银LOF出台补偿方案，超九成投资者将获全额补偿 FX168财经
   链接: https://news.google.com/rss/articles/CBMiUkFVX3lxTFBDSjM3X0pZLTZsTEZYYzBYNXc4ZDU4cUpJblZmZHRhNmk3bXdxVWpPeDFPR2txTWgzV2lZV1dpWTFFRFhMbUdkbVhkSkhGMHpXb2c?oc=5
16. [2026-02-16 06:31] 封面新闻 | 此沙、李子柒、谭松韵、丁真！春晚宜宾分会场沉浸式解锁百项非遗 - 封面新闻
   摘要: 此沙、李子柒、谭松韵、丁真！春晚宜宾分会场沉浸式解锁百项非遗 封面新闻
   链接: https://news.google.com/rss/articles/CBMiZkFVX3lxTFBoU3FxVjlGYThQX3FSUDd6ZnFFYVlnQXZUYjZCaTJXSHdWUDloSTV3aHdrMEtWQjFFaThVTndoaG1oMWpZSUtCREh0aEpTQlNhdU9DeElLLTNvV05QWTQwYUNOTDUzZw?oc=5
17. [2026-02-15 20:25] 雷科技 | 马年春晚科技秀终极前瞻：硬科技成新头牌，机器人再做「群演」 - 雷科技
   摘要: 马年春晚科技秀终极前瞻：硬科技成新头牌，机器人再做「群演」 雷科技
   链接: https://news.google.com/rss/articles/CBMiTkFVX3lxTE1ETXhzUEVuczZDSWkyV3RrQS1oZl9GclViVm4tS1hLVGJGR3ZCSVkyc3ZKYV9mRUhGc01KcGJJY3laajBhck53SFRYTUxEZw?oc=5
18. [2026-02-15 20:19] Binance | Pi Network 价格上涨50%的主要原因| Berserker_09发布于币安广场 - Binance
   摘要: Pi Network 价格上涨50%的主要原因| Berserker_09发布于币安广场 Binance
   链接: https://news.google.com/rss/articles/CBMiaEFVX3lxTE1RTjU0bkpQdEdXeW5wTjZCUjJ2bTNraFhLT0Q4Mks5NlJrUTBFMDhWVGtocjkycDRlclNtelNRYzl6Q3k0T1RCRTdnNlpkQzNfVGlNbGNEeDRtc1RGNjgtQVR0Qkl5UFJt?oc=5
19. [2026-02-15 11:29] 中央广播电视总台 | 准备就绪！总台马年春晚完成全部五次彩排 - 中央广播电视总台
   摘要: 准备就绪！总台马年春晚完成全部五次彩排 中央广播电视总台
   链接: https://news.google.com/rss/articles/CBMic0FVX3lxTE9KVzVydG5lVjdYcWh4Mkk5ZE9xOFYtMENDTmZSLXhVMWFrY3Nqd3p1R2U3WnFIZmN6VEZsdEJ6c3ZXa3AtNVhTS1IwcUdFZTdyRU5zWnBpU2hVQnoweXBZc3lZenRDTldzMDk1S2haNmdkTnc?oc=5

</details>


### 📎 引用脚注

1. [知乎 #1 | 2026 年央视春晚中有哪些亮点？哪个节目最让你印象深刻？](https://www.zhihu.com/question/2006817906369979378)（NewsNow热榜，匹配分=100，来源ID=NW01）
2. [今日头条 #1 | 春晚机器人中国功夫夯爆了](https://www.toutiao.com/trending/7607438781827366955/)（NewsNow热榜，匹配分=100，来源ID=NW02）
3. [知乎 #2 | 如何评价宇树科技机器人在 2026 年春晚的武术表演《武 BOT》？与去年的《秧 BOT》相比有哪些进步？](https://www.zhihu.com/question/2006826244814104012)（NewsNow热榜，匹配分=100，来源ID=NW14）
4. [2026-02-17T00:00 @elonmusk | Yup 😂 That really made him upset. After I ghosted him, Epstein went on a massive campaig...](https://twitter.com/elonmusk/status/2023302989872771110)（Twitter，匹配分=100，来源ID=TW02）
5. [2026-02-17T00:00 @thejackhopkins | I have a prediction: Sooner than later, one of Epstein’s victims is going to get fed up ...](https://twitter.com/thejackhopkins/status/2023516999754932398)（Twitter，匹配分=100，来源ID=TW11）
6. [2026-02-16 16:49 yeeyi | 重磅喜讯！中国官宣免签扩大！贸易谈判推进！从机票到车价都可能被改写！两大政策进展背后，普通人最该关注的现实影响全解读...-yeeyi - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBREdBeGNHbld6ZXhtUmZJQ1FnZ1lleWRBbld0eTlDWm11UkdUZmMzTk43UkFReEVDd3lqYXM3RE9wQ2QtVTNPbG5POGpZWjZvcHJ6RDRR?oc=5)（联网检索，匹配分=100，来源ID=WB04）
7. [2026-02-16 07:58 每日经济新闻 | 江苏连云港一烟花零售店爆炸致8人遇难2人受伤，应急管理部紧急召开调度会；中方宣布对英、加免签；马斯克：Grok 4.20本周发布丨每经早参 - 每日经济新闻](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBiTmRySmt3a3MzOGdCWnVHR1BtSXZ3bklIb2Nvci1qTDN6Z0lCUXQ1Ty1IMnVTWmpXZlgzR0Rzc2swS2NlUWxDTFpFWlJvY2o0amZicnB4NlIzREZOQmpoY2tPREl4dw?oc=5)（联网检索，匹配分=100，来源ID=WB08）
8. [2026-02-17T00:00 @LeadingReport | BREAKING: US housing market reaches most “unaffordable” level in history, per St. Louis ...](https://twitter.com/LeadingReport/status/2023421333477179570)（Twitter，匹配分=100，来源ID=TW05）
9. [2026-02-17T00:00 @KobeissiLetter | Japanese markets are making history: The correlation between the Japanese Yen and the To...](https://twitter.com/KobeissiLetter/status/2023473956674838651)（Twitter，匹配分=100，来源ID=TW15）
10. [华尔街见闻 #1 | AI热潮助力港股蛇年收官战告捷，MiniMax暴涨25%、智谱涨4.74%齐创新高，有色板块拉升](https://wallstreetcn.com/articles/3765773)（NewsNow热榜，匹配分=100，来源ID=NW07）
11. [2026-02-17T00:00 @KimDotcom | Breaking Palantir was allegedly hacked. An AI agent was used to gain super-user access a...](https://twitter.com/KimDotcom/status/2023165849721536672)（Twitter，匹配分=100，来源ID=TW01）
12. [2026-02-17T00:00 @nuknikklgku | เตือน‼️ เจ้าของกิจการจังหวัดท่องเที่ยว อีพวก Israeli มีทริคใหม่คือ gen ai เอารูปไม่จริงม...](https://twitter.com/nuknikklgku/status/2023372509819834799)（Twitter，匹配分=100，来源ID=TW07）
13. [2026-02-17 01:05 英为财情 Investing.com | 法国股市上涨；截至收盘法国CAC40指数上涨0.06% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9NSm1hMzlXN2hoQmVrOTJ5dXRsWU9YUklIS25NN19xTno0MzBrWDBuM0stYVBEMnBRbkxzODVoWGlQWE1IdVVZWGJsQnkxMjNWY2plVlJXSlhueDVJNUNqbWhyaVN2SXdkZGw5eURYZ2Q?oc=5)（联网检索，匹配分=100，来源ID=WB07）
14. [Significant-Gravitas/AutoGPT | ⭐ 181836](https://github.com/Significant-Gravitas/AutoGPT)（GitHub，匹配分=100，来源ID=GH02）
15. [langflow-ai/langflow | ⭐ 144834](https://github.com/langflow-ai/langflow)（GitHub，匹配分=100，来源ID=GH07）
16. [langgenius/dify | ⭐ 129696](https://github.com/langgenius/dify)（GitHub，匹配分=100，来源ID=GH08）
17. [nautechsystems/nautilus_trader | ⭐ 19761](https://github.com/nautechsystems/nautilus_trader)（GitHub，匹配分=100，来源ID=GH10）
18. [openclaw/openclaw | ⭐ 201537](https://github.com/openclaw/openclaw)（GitHub，匹配分=100，来源ID=GH01）
19. [2026-02-17T00:00 @adamscochran | Between the stock market, national secrets, and billions in self-dealing government cont...](https://twitter.com/adamscochran/status/2023492620039946737)（Twitter，匹配分=100，来源ID=TW09）
20. [2026-02-17T00:00 @TheNCSmaster | It still doesn’t feel like it’s emphasized enough how fucked the economy and tech prices...](https://twitter.com/TheNCSmaster/status/2023511382130671724)（Twitter，匹配分=100，来源ID=TW10）
21. [百度热搜 #1 | 总台马年春晚](https://www.baidu.com/s?wd=%E6%80%BB%E5%8F%B0%E9%A9%AC%E5%B9%B4%E6%98%A5%E6%99%9A)（NewsNow热榜，匹配分=100，来源ID=NW03）
22. [抖音 #1 | 央视马年春晚](https://www.douyin.com/hot/2402899)（NewsNow热榜，匹配分=100，来源ID=NW04）
23. [财联社热门 #1 | 白银基金出台补偿方案！2月26日可办理，1000元以下损失全额补偿](https://www.cls.cn/detail/2290657)（NewsNow热榜，匹配分=100，来源ID=NW06）
24. [2026-02-17 07:54 thepaper.cn | 城市年鉴2025｜科技产业：“速度”和 “泡沫”中找平衡 - thepaper.cn](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1FN1pzQUhiTlRHQVJBajFLOFBkc0FCbnpOeXBiTThLNXFFY29Zb3ZkZEtfMl82UTNzMWV0dV83alpwUWlFcWJvYjVtNkpQcDRyalp4RWhxWG9KRTYtNHc?oc=5)（联网检索，匹配分=100，来源ID=WB13）
25. [华尔街见闻 #10 | 行业首例！国投白银LOF估值调整补偿方案出炉：1000元以下损失全额补偿](https://wallstreetcn.com/articles/3765768)（NewsNow热榜，匹配分=40）

## 🧪 引用匹配校验

- 已匹配引用条数: 25
- 未完成匹配标签: 4
- 未匹配示例: 历史报告1；历史报告1；历史报告1
- 低置信引用条数: 0
- 处理建议: 本次未发现低置信引用。

## 🎯 投机方向（超短）

- 商品波段方向：天然气 -4.59%
- 海外指数方向：美股 VIX波动率指数 +2.91%（强动量延续）
- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。

## 🌐 联网检索补充

- 关键词：2026-02-17 全球市场 盘面 复盘 原因, 2026-02-17 中国 宏观 经济 政策 市场 影响, 2026-02-17 AI 科技 行业 动态 影响, VIX波动率指数 上涨 原因, ETH 上涨 原因, 2026 年央视春晚中有哪些亮点？哪个节目最让你印象深刻？ 事件 背景, 春晚机器人中国功夫夯爆了 事件 背景, 总台马年春晚 事件 背景
- 命中结果：19 条（按发布时间倒序）

### 🔎 2026-02-17 中国 宏观 经济 政策 市场 影响

- [城市年鉴2025｜科技产业：“速度”和 “泡沫”中找平衡 - thepaper.cn](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1FN1pzQUhiTlRHQVJBajFLOFBkc0FCbnpOeXBiTThLNXFFY29Zb3ZkZEtfMl82UTNzMWV0dV83alpwUWlFcWJvYjVtNkpQcDRyalp4RWhxWG9KRTYtNHc?oc=5)
  - 来源: thepaper.cn | 时间: 2026-02-17 07:54
  - 摘要: 城市年鉴2025｜科技产业：“速度”和 “泡沫”中找平衡 thepaper.cn
- [首席展望｜中欧基金任飞：周期板块将迎量价共振，看好有色、新能源及化工 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wdlNqdllSZTB6NUVwMEtUQnM1R1gyOVlodzF6cDNCcTEzRzlkLW5tZEhiODI0UW5SZHJHS0c1NWF1QkxvWXUzMFlXOW5jenZ1V3RpWWxHenFpZ1JTQmVVTg?oc=5)
  - 来源: thepaper.cn | 时间: 2026-02-17 07:46
  - 摘要: 首席展望｜中欧基金任飞：周期板块将迎量价共振，看好有色、新能源及化工 thepaper.cn
- [2026新年献词|景顺长城基金总经理康乐：主动有为，静待春来 - 新浪财经](https://news.google.com/rss/articles/CBMiigJBVV95cUxQdENIeW1LUzV2WjZhX2FEVnpSTEJyeDFhajFDTVhqT0lDMUZQeDV5aTJwSFBUZzk0aHhNQXF0NmN1WXhrcUxQYXZBX1FXUkF1RFR4VGZ1NXFSWHdkM1pHRzNxSGZPX1AyU3IyOWZ6akFJNDg3R2gxUEM4SDZVM1JGTGU5eXE2S21lUHJNT2stU1pZakJKaWNFTzZTT0hhOEtaTmkxQWlDSEFLTkxlMm9ndTR4b0JBZ2pkTWt1b21yU0I3dWw4TVFHaWt6cnI5MWMxYkx0M0Vmb2FiSEFFUmRFODBMTjRBQTVlUGRfTUN2U3Z0ejlkU1ZWTm0zcXBrSHVDUVZNTEZpdW1VQQ?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-17 07:01
  - 摘要: 2026新年献词|景顺长城基金总经理康乐：主动有为，静待春来 新浪财经
- [重磅喜讯！中国官宣免签扩大！贸易谈判推进！从机票到车价都可能被改写！两大政策进展背后，普通人最该关注的现实影响全解读...-yeeyi - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBREdBeGNHbld6ZXhtUmZJQ1FnZ1lleWRBbld0eTlDWm11UkdUZmMzTk43UkFReEVDd3lqYXM3RE9wQ2QtVTNPbG5POGpZWjZvcHJ6RDRR?oc=5)
  - 来源: yeeyi | 时间: 2026-02-16 16:49
  - 摘要: 重磅喜讯！中国官宣免签扩大！贸易谈判推进！从机票到车价都可能被改写！两大政策进展背后，普通人最该关注的现实影响全解读...-yeeyi yeeyi
- [财经早餐：本周A股开启“春节休假”模式，DeepSeek V4或将发布，国投白银LOF出台补偿方案，超九成投资者将获全额补偿 - FX168财经](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBDSjM3X0pZLTZsTEZYYzBYNXc4ZDU4cUpJblZmZHRhNmk3bXdxVWpPeDFPR2txTWgzV2lZV1dpWTFFRFhMbUdkbVhkSkhGMHpXb2c?oc=5)
  - 来源: FX168财经 | 时间: 2026-02-16 07:42
  - 摘要: 财经早餐：本周A股开启“春节休假”模式，DeepSeek V4或将发布，国投白银LOF出台补偿方案，超九成投资者将获全额补偿 FX168财经

### 🔎 2026-02-17 AI 科技 行业 动态 影响

- [新浪财经隔夜要闻大事汇总：2026年2月17日|债券市场|金融市场|原油期货|宇树科技|惊蛰无声_手机新浪网 - 新浪财经](https://news.google.com/rss/articles/CBMijgJBVV95cUxPSmczWGVmS3U1YThtMExmdlFPaVgwNkcxT3BFZjd5dFZ5MWhKM1hBY1IxdVg4QjR5MmNPVmVjWXhldUhkMlU2S2RLLVlwcXRjaF9zME5VMmJmMUdFWDdLVFZzSk1wbkQzT3V6M0htdWh3OUhiYi03NC11MjcxUEp0UEFEenR6N1h2QXZ2cTgxQTloWG9Zb2xTM2JsV0hBUlZVVVRrYWlqcE9oQVJ6dHZLdURjdUo0TGxIQmtvekZJMVFmSTAtWmd1RU1fYUpRaDFrVHZUemp5TGZXVktvYkl3VGJmUHFGSFVtYkw3a2VEblVVSzE0ZGR1Umw0bVoxNlFwMGFsaV9faWh4VmczbVE?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-17 07:35
  - 摘要: 新浪财经隔夜要闻大事汇总：2026年2月17日|债券市场|金融市场|原油期货|宇树科技|惊蛰无声_手机新浪网 新浪财经
- [华米科技：AI眼镜量产、业绩指引与股价波动引关注 - SOHU](https://news.google.com/rss/articles/CBMihwFBVV95cUxQNnBkMnZsZlMyRzU0LUdPODFPLVB4ZjlXTWptUVBHMHpYdVRTSFg2dHMzQ19LWjY0NlRCU0I2UGUwcFZURmhBWUg4TXZXUU1wckctc2JKUmVLcjRLMmxjbDhCcHNKcEhNeEVCMWY0XzhteEJORWJrcVJNRlowVkl0TkluV0YtSTA?oc=5)
  - 来源: SOHU | 时间: 2026-02-17 00:34
  - 摘要: 华米科技：AI眼镜量产、业绩指引与股价波动引关注 SOHU
- [江苏连云港一烟花零售店爆炸致8人遇难2人受伤，应急管理部紧急召开调度会；中方宣布对英、加免签；马斯克：Grok 4.20本周发布丨每经早参 - 每日经济新闻](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBiTmRySmt3a3MzOGdCWnVHR1BtSXZ3bklIb2Nvci1qTDN6Z0lCUXQ1Ty1IMnVTWmpXZlgzR0Rzc2swS2NlUWxDTFpFWlJvY2o0amZicnB4NlIzREZOQmpoY2tPREl4dw?oc=5)
  - 来源: 每日经济新闻 | 时间: 2026-02-16 07:58
  - 摘要: 江苏连云港一烟花零售店爆炸致8人遇难2人受伤，应急管理部紧急召开调度会；中方宣布对英、加免签；马斯克：Grok 4.20本周发布丨每经早参 每日经济新闻

### 🔎 VIX波动率指数 上涨 原因

- [法国股市上涨；截至收盘法国CAC40指数上涨0.06% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9NSm1hMzlXN2hoQmVrOTJ5dXRsWU9YUklIS25NN19xTno0MzBrWDBuM0stYVBEMnBRbkxzODVoWGlQWE1IdVVZWGJsQnkxMjNWY2plVlJXSlhueDVJNUNqbWhyaVN2SXdkZGw5eURYZ2Q?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-17 01:05
  - 摘要: 法国股市上涨；截至收盘法国CAC40指数上涨0.06% 提供者 Investing.com 英为财情 Investing.com
- [澳大利亚股市上涨；截至收盘澳大利亚S&P/ASX200指数上涨0.22% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTFBXTkxGWWlpT2VIRnhZRTFVUEtLUnZxQUNJRW1TMXVDZTBIWWdRbWItUUFOTHBuUHNEbTNYT0VxbmhWZ19ZQkhGMWpRVk9JTVNoZ3BMOUl2b0E5Zmh4blpZNjRaTnNEUkFhbFBSOER5M1U?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-16 13:30
  - 摘要: 澳大利亚股市上涨；截至收盘澳大利亚S&P/ASX200指数上涨0.22% 提供者 Investing.com 英为财情 Investing.com
- [7张图表，说明为何美股的压力山大 - FX168财经](https://news.google.com/rss/articles/CBMia0FVX3lxTE01SHBRTzRiTkV0cXhuV1R2RFA3RzJfRndYUFkzUXlJSC1hVG1nVVViNGg4UE9VSWF0MzZHckpoNHdHLUVQeFp3eDJSNjZnWmp2NjZXeHhlU1dBV0ktd2JFcGRoUWtpaHJpbF9N?oc=5)
  - 来源: FX168财经 | 时间: 2026-02-16 12:05
  - 摘要: 7张图表，说明为何美股的压力山大 FX168财经

### 🔎 总台马年春晚 事件 背景

- [骐骥驰骋 势不可挡 总台马年春晚精彩上演 - 新浪财经](https://news.google.com/rss/articles/CBMiiAJBVV95cUxPMFBUSUVpOVdBTGRhdXQyMUFQaUNRTUJlaUdtVHFrUmdwX2dTellONzI0d3VQeS1FQTVlMzVZZXNVdURPUGZPS3R5Rk5scGlvVjRWQ00zU1VSbWVlajJYV3RXUFJSQjRLVlhUeGJHUVpHM3BPNFVrel9iSDhaOThGMUpZM3VKekNabWJ6eWlFYXJuMGduVms0Y2c2aHJQMkxZMDV1NVFqZGRacXlkQWJjY3RYcHBFV3pMSVJMMnpXQVBvcm0tZXdyT0tTQWtBSWQ5cDd6UDJYNVhpX3NEaTgwTkd3VzlJUThtVlFQR0xsbXY5QW8yQTBET3hUNFM4VzNyZUMyRjBndEs?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-17 00:51
  - 摘要: 骐骥驰骋 势不可挡 总台马年春晚精彩上演 新浪财经
- [总台马年春晚 看点满满迎新春 - 中华网](https://news.google.com/rss/articles/CBMicEFVX3lxTFBmdktjcWV1MnBvUnlGQW1uWTlxS2w3UUZOSl9qNkk0cHVxLTRiNjR0WHFyZDNpSkdJam9ka1FGakJyUU1JTjJxMjNvaXRlNUZubGRDUWZEemgtYU9XM0pBdlp1YVJ4bWhYZ1ZadWJYNk0?oc=5)
  - 来源: 中华网 | 时间: 2026-02-16 20:01
  - 摘要: 总台马年春晚 看点满满迎新春 中华网
- [欢乐吉祥 喜气洋洋 总台《2026年春节联欢晚会》等着您 - 央视网](https://news.google.com/rss/articles/CBMid0FVX3lxTE5Xa25JdVc1SVROOW8wcmhRVDJNLTJub3RzWWMxakUxTVBBaGhlQ3BTYkEyTWFpUXAxWTJ5UWRRUlBwQUZlZnRCZjYzUmZ1ZmhUYjBnREg1Y2RucUUyMVNHUmF2LU1vY2RYSkVWeHN0NmVTdWtPcnFJ?oc=5)
  - 来源: 央视网 | 时间: 2026-02-16 20:00
  - 摘要: 欢乐吉祥 喜气洋洋 总台《2026年春节联欢晚会》等着您 央视网
- [此沙、李子柒、谭松韵、丁真！春晚宜宾分会场沉浸式解锁百项非遗 - 封面新闻](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBoU3FxVjlGYThQX3FSUDd6ZnFFYVlnQXZUYjZCaTJXSHdWUDloSTV3aHdrMEtWQjFFaThVTndoaG1oMWpZSUtCREh0aEpTQlNhdU9DeElLLTNvV05QWTQwYUNOTDUzZw?oc=5)
  - 来源: 封面新闻 | 时间: 2026-02-16 06:31
  - 摘要: 此沙、李子柒、谭松韵、丁真！春晚宜宾分会场沉浸式解锁百项非遗 封面新闻
- [马年春晚科技秀终极前瞻：硬科技成新头牌，机器人再做「群演」 - 雷科技](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1ETXhzUEVuczZDSWkyV3RrQS1oZl9GclViVm4tS1hLVGJGR3ZCSVkyc3ZKYV9mRUhGc01KcGJJY3laajBhck53SFRYTUxEZw?oc=5)
  - 来源: 雷科技 | 时间: 2026-02-15 20:25
  - 摘要: 马年春晚科技秀终极前瞻：硬科技成新头牌，机器人再做「群演」 雷科技
- [准备就绪！总台马年春晚完成全部五次彩排 - 中央广播电视总台](https://news.google.com/rss/articles/CBMic0FVX3lxTE9KVzVydG5lVjdYcWh4Mkk5ZE9xOFYtMENDTmZSLXhVMWFrY3Nqd3p1R2U3WnFIZmN6VEZsdEJ6c3ZXa3AtNVhTS1IwcUdFZTdyRU5zWnBpU2hVQnoweXBZc3lZenRDTldzMDk1S2haNmdkTnc?oc=5)
  - 来源: 中央广播电视总台 | 时间: 2026-02-15 11:29
  - 摘要: 准备就绪！总台马年春晚完成全部五次彩排 中央广播电视总台

### 🔎 ETH 上涨 原因

- [Ethereum 下跌 5.71%，原因是 FinCEN 加大执法力度，看跌信号占主导地位 - Traders Union](https://news.google.com/rss/articles/CBMipgFBVV95cUxPdTVsdTFlanJBNnVHREVVOW9rRm9BQTZ0S1FJdFNGVDVCUEN0MEtqZTcxbjlMQ2ZiNVRoMDhUWUlzSGhDTTN4a0VnZFdpY1V4VjJFRlMtVVpaazkwRVNVandnRVlKYV9ySm9QQTF5UDIxbC1Sa09VbUpBbkY5eWRLOWFEcFNRaFJjMVNiY2E4OXU0NXNHekQ0N05yZ1dmY0FacEYwbHdR?oc=5)
  - 来源: Traders Union | 时间: 2026-02-16 15:04
  - 摘要: Ethereum 下跌 5.71%，原因是 FinCEN 加大执法力度，看跌信号占主导地位 Traders Union
- [Pi Network 价格上涨50%的主要原因| Berserker_09发布于币安广场 - Binance](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1RTjU0bkpQdEdXeW5wTjZCUjJ2bTNraFhLT0Q4Mks5NlJrUTBFMDhWVGtocjkycDRlclNtelNRYzl6Q3k0T1RCRTdnNlpkQzNfVGlNbGNEeDRtc1RGNjgtQVR0Qkl5UFJt?oc=5)
  - 来源: Binance | 时间: 2026-02-15 20:19
  - 摘要: Pi Network 价格上涨50%的主要原因| Berserker_09发布于币安广场 Binance

## 🔗 AI 分析引用来源

> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。

### Twitter (8 条)

- [⁴] [2026-02-17T00:00 @elonmusk | Yup 😂 That really made him upset. After I ghosted him, Epstein went on a massive campaig...](https://twitter.com/elonmusk/status/2023302989872771110)（匹配分=100，来源ID=TW02）
- [⁵] [2026-02-17T00:00 @thejackhopkins | I have a prediction: Sooner than later, one of Epstein’s victims is going to get fed up ...](https://twitter.com/thejackhopkins/status/2023516999754932398)（匹配分=100，来源ID=TW11）
- [⁸] [2026-02-17T00:00 @LeadingReport | BREAKING: US housing market reaches most “unaffordable” level in history, per St. Louis ...](https://twitter.com/LeadingReport/status/2023421333477179570)（匹配分=100，来源ID=TW05）
- [⁹] [2026-02-17T00:00 @KobeissiLetter | Japanese markets are making history: The correlation between the Japanese Yen and the To...](https://twitter.com/KobeissiLetter/status/2023473956674838651)（匹配分=100，来源ID=TW15）
- [¹¹] [2026-02-17T00:00 @KimDotcom | Breaking Palantir was allegedly hacked. An AI agent was used to gain super-user access a...](https://twitter.com/KimDotcom/status/2023165849721536672)（匹配分=100，来源ID=TW01）
- [¹²] [2026-02-17T00:00 @nuknikklgku | เตือน‼️ เจ้าของกิจการจังหวัดท่องเที่ยว อีพวก Israeli มีทริคใหม่คือ gen ai เอารูปไม่จริงม...](https://twitter.com/nuknikklgku/status/2023372509819834799)（匹配分=100，来源ID=TW07）
- [¹⁹] [2026-02-17T00:00 @adamscochran | Between the stock market, national secrets, and billions in self-dealing government cont...](https://twitter.com/adamscochran/status/2023492620039946737)（匹配分=100，来源ID=TW09）
- [²⁰] [2026-02-17T00:00 @TheNCSmaster | It still doesn’t feel like it’s emphasized enough how fucked the economy and tech prices...](https://twitter.com/TheNCSmaster/status/2023511382130671724)（匹配分=100，来源ID=TW10）

### NewsNow热榜 (8 条)

- [¹] [知乎 #1 | 2026 年央视春晚中有哪些亮点？哪个节目最让你印象深刻？](https://www.zhihu.com/question/2006817906369979378)（匹配分=100，来源ID=NW01）
- [²] [今日头条 #1 | 春晚机器人中国功夫夯爆了](https://www.toutiao.com/trending/7607438781827366955/)（匹配分=100，来源ID=NW02）
- [³] [知乎 #2 | 如何评价宇树科技机器人在 2026 年春晚的武术表演《武 BOT》？与去年的《秧 BOT》相比有哪些进步？](https://www.zhihu.com/question/2006826244814104012)（匹配分=100，来源ID=NW14）
- [¹⁰] [华尔街见闻 #1 | AI热潮助力港股蛇年收官战告捷，MiniMax暴涨25%、智谱涨4.74%齐创新高，有色板块拉升](https://wallstreetcn.com/articles/3765773)（匹配分=100，来源ID=NW07）
- [²¹] [百度热搜 #1 | 总台马年春晚](https://www.baidu.com/s?wd=%E6%80%BB%E5%8F%B0%E9%A9%AC%E5%B9%B4%E6%98%A5%E6%99%9A)（匹配分=100，来源ID=NW03）
- [²²] [抖音 #1 | 央视马年春晚](https://www.douyin.com/hot/2402899)（匹配分=100，来源ID=NW04）
- [²³] [财联社热门 #1 | 白银基金出台补偿方案！2月26日可办理，1000元以下损失全额补偿](https://www.cls.cn/detail/2290657)（匹配分=100，来源ID=NW06）
- [²⁵] [华尔街见闻 #10 | 行业首例！国投白银LOF估值调整补偿方案出炉：1000元以下损失全额补偿](https://wallstreetcn.com/articles/3765768)（匹配分=40）

### GitHub (5 条)

- [¹⁴] [Significant-Gravitas/AutoGPT | ⭐ 181836](https://github.com/Significant-Gravitas/AutoGPT)（匹配分=100，来源ID=GH02）
- [¹⁵] [langflow-ai/langflow | ⭐ 144834](https://github.com/langflow-ai/langflow)（匹配分=100，来源ID=GH07）
- [¹⁶] [langgenius/dify | ⭐ 129696](https://github.com/langgenius/dify)（匹配分=100，来源ID=GH08）
- [¹⁷] [nautechsystems/nautilus_trader | ⭐ 19761](https://github.com/nautechsystems/nautilus_trader)（匹配分=100，来源ID=GH10）
- [¹⁸] [openclaw/openclaw | ⭐ 201537](https://github.com/openclaw/openclaw)（匹配分=100，来源ID=GH01）

### 联网检索 (4 条)

- [⁶] [2026-02-16 16:49 yeeyi | 重磅喜讯！中国官宣免签扩大！贸易谈判推进！从机票到车价都可能被改写！两大政策进展背后，普通人最该关注的现实影响全解读...-yeeyi - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBREdBeGNHbld6ZXhtUmZJQ1FnZ1lleWRBbld0eTlDWm11UkdUZmMzTk43UkFReEVDd3lqYXM3RE9wQ2QtVTNPbG5POGpZWjZvcHJ6RDRR?oc=5)（匹配分=100，来源ID=WB04）
- [⁷] [2026-02-16 07:58 每日经济新闻 | 江苏连云港一烟花零售店爆炸致8人遇难2人受伤，应急管理部紧急召开调度会；中方宣布对英、加免签；马斯克：Grok 4.20本周发布丨每经早参 - 每日经济新闻](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBiTmRySmt3a3MzOGdCWnVHR1BtSXZ3bklIb2Nvci1qTDN6Z0lCUXQ1Ty1IMnVTWmpXZlgzR0Rzc2swS2NlUWxDTFpFWlJvY2o0amZicnB4NlIzREZOQmpoY2tPREl4dw?oc=5)（匹配分=100，来源ID=WB08）
- [¹³] [2026-02-17 01:05 英为财情 Investing.com | 法国股市上涨；截至收盘法国CAC40指数上涨0.06% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9NSm1hMzlXN2hoQmVrOTJ5dXRsWU9YUklIS25NN19xTno0MzBrWDBuM0stYVBEMnBRbkxzODVoWGlQWE1IdVVZWGJsQnkxMjNWY2plVlJXSlhueDVJNUNqbWhyaVN2SXdkZGw5eURYZ2Q?oc=5)（匹配分=100，来源ID=WB07）
- [²⁴] [2026-02-17 07:54 thepaper.cn | 城市年鉴2025｜科技产业：“速度”和 “泡沫”中找平衡 - thepaper.cn](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1FN1pzQUhiTlRHQVJBajFLOFBkc0FCbnpOeXBiTThLNXFFY29Zb3ZkZEtfMl82UTNzMWV0dV83alpwUWlFcWJvYjVtNkpQcDRyalp4RWhxWG9KRTYtNHc?oc=5)（匹配分=100，来源ID=WB13）

> 注：早报 AI 已按规则跳过 A 股盘面数据分析。


---

# 📋 原始数据

<a id="raw-market-data"></a>
## 📊 金融市场数据

### 🧭 股票总览

> 跟踪 **12** 个标的：上涨 **7** | 下跌 **5** | 平盘 **0** | 上涨占比 **58.3%**
> 区域强弱：美股 +0.80% (4/5) | 港股 +0.52% (1/1) | 欧股 -0.05% (2/3) | 日股 -0.24% (0/1) | 韩股 -0.28% (0/1) | A股 -1.26% (0/1)

> ⏸ A股休市

### 🌍 全球股票概览（Yahoo Finance）

| 区域 | 指标 | 最新价 | 涨跌幅 | 币种 |
|------|------|--------|--------|------|
| 美股 | [标普500](https://finance.yahoo.com/quote/%5EGSPC) | 6,836.17 | 🟢 +0.05% | USD |
| 美股 | [纳斯达克综合](https://finance.yahoo.com/quote/%5EIXIC) | 22,546.67 | 🔴 -0.22% | USD |
| 美股 | [道琼斯工业指数](https://finance.yahoo.com/quote/%5EDJI) | 49,500.93 | 🟢 +0.10% | USD |
| 美股 | [罗素2000](https://finance.yahoo.com/quote/%5ERUT) | 2,646.70 | 🟢 +1.18% | USD |
| 美股 | [VIX波动率指数](https://finance.yahoo.com/quote/%5EVIX) | 21.20 | 🟢 +2.91% | USD |
| 港股 | [恒生指数](https://finance.yahoo.com/quote/%5EHSI) | 26,705.94 | 🟢 +0.52% | HKD |
| 日股 | [日经225](https://finance.yahoo.com/quote/%5EN225) | 56,806.41 | 🔴 -0.24% | JPY |
| 韩股 | [韩国综合指数](https://finance.yahoo.com/quote/%5EKS11) | 5,507.01 | 🔴 -0.28% | KRW |
| 欧股 | [英国富时100](https://finance.yahoo.com/quote/%5EFTSE) | 10,473.69 | 🟢 +0.26% | GBP |
| 欧股 | [德国DAX](https://finance.yahoo.com/quote/%5EGDAXI) | 24,800.91 | 🔴 -0.46% | EUR |
| 欧股 | [法国CAC40](https://finance.yahoo.com/quote/%5EFCHI) | 8,316.50 | 🟢 +0.06% | EUR |
| A股 | [上证综指](https://finance.yahoo.com/quote/000001.SS) | 4,082.07 | 🔴 -1.26% | CNY |

> 概览：上涨 7 | 下跌 5 | 平盘 0 | 总计 12

### 🥇 贵金属

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|

### ₿ 加密货币

| 币种 | 价格 | 24h涨跌 |
|------|------|---------|
| BTC | $68,849.00 | 🟢 +0.10% |
| ETH | $1,997.50 | 🟢 +1.65% |
| SOL | $86.48 | 🟢 +0.63% |

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
| WTI原油 | 63.75 | 🟢 +1.37% |
| 布伦特原油 | 68.57 | 🟢 +1.21% |
| 天然气 | 3.09 | 🔴 -4.59% |
| COMEX铜 | 5.76 | 🔴 -0.53% |

### 💻 GitHub 趋势

- ⭐ [**zeroclaw**](https://github.com/zeroclaw-labs/zeroclaw) (7055 stars)
  - Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere,
- ⭐ [**vscode-dark-islands**](https://github.com/bwya77/vscode-dark-islands) (2310 stars)
  - VSCode theme based off the easemate IDE and Jetbrains islands theme
- ⭐ [**k-id-age-verifier**](https://github.com/xyzeva/k-id-age-verifier) (1571 stars)
  - automatically verify your age on discord, twitch, kick, quora and more (k-id)
- ⭐ [**greenlight**](https://github.com/RevylAI/greenlight) (1028 stars)
  - Pre-submission compliance scanner for the Apple App Store
- ⭐ [**sql-tap**](https://github.com/mickamy/sql-tap) (816 stars)
  - Watch SQL traffic in real-time with a TUI

## 🐦 Twitter 热点 (113 条)

- 来源统计: 关注账号 190 条 | 热门讨论 30 条

### 🔥 热门讨论推文

- `2026-02-17T00:00` @KimDotcom ❤️69937 🔁20745 💬3444
  - Breaking  Palantir was allegedly hacked. An AI agent was used to gain super-user access and here”s what the hackers allegedly found:  Peter Thiel and Alex Karp commit mass surveillance of world leaders and titans of industry on a massive scale.  They have thousands of hours of transcribed and searchable conversations of Donald Trump, JD Vance and Elon Musk.  They have backdoored the devices, cars and jets of world leaders and accumulated the biggest archive of blackmail material.  Palantir is cr
  - [原文链接](https://twitter.com/KimDotcom/status/2023165849721536672)
- `2026-02-17T00:00` @elonmusk ❤️77622 🔁6995 💬2167
  - Yup 😂  That really made him upset. After I ghosted him, Epstein went on a massive campaign to short Tesla and got Gates to short 1% of Tesla stock when the market cap was $40B. As far as I know, Gates still has the short open.   Someone should ask him how that’s working out 🤗
  - [原文链接](https://twitter.com/elonmusk/status/2023302989872771110)
- `2026-02-17T00:00` @TBSCDTV ❤️20636 🔁4606 💬91
  - #CDTVライブライブ3月9日(月)よる7時⚡️  ＼👑豪華出演者発表🌟／#AI「ラッキーアイラブユー」#WEST.「これでいいのだ！」#キタニタツヤfeat.#BABYMETAL「かすかなはな」#GENERATIONS「本心」#中島健人「XTC」「IDOLIC」#MILK「爆裂愛してる」#TBS
  - [原文链接](https://twitter.com/TBSCDTV/status/2023365491948245021)
- `2026-02-17T00:00` @SpacemanAp ❤️15628 🔁5644 💬22
  - Western media won’t air this bc they don’t want you to grow a brain & realize “wait, I can shut down the economy. All the wealth is built off my labor. I can own my labor, without my labor there are no billionaires”. That is capitalisms worse nightmare. Imagine a system that runs
  - [原文链接](https://twitter.com/SpacemanAp/status/2022438260275056995)
- `2026-02-17T00:00` @LeadingReport ❤️14320 🔁2136 💬341
  - BREAKING: US housing market reaches most “unaffordable” level in history, per St. Louis Fed report.
  - [原文链接](https://twitter.com/LeadingReport/status/2023421333477179570)
- `2026-02-17T00:00` @Flicky0ps ❤️14542 🔁2175 💬80
  - i will never get over the fact that people now associate em dashes and semicolons with ai like god forbid a girl likes to read sorry i’m literate
  - [原文链接](https://twitter.com/Flicky0ps/status/2023455023112614236)
- `2026-02-17T00:00` @nuknikklgku ❤️3029 🔁9796 💬14
  - เตือน‼️   เจ้าของกิจการจังหวัดท่องเที่ยว อีพวก Israeli   มีทริคใหม่คือ gen ai เอารูปไม่จริงมารีวิวให้ 1 ดาว จะขอเงินคืน อีชนชาติสัตว์หมานรกนี่ ถ้ารัฐบาลจะทบทวนฟรีวีซ่าประเทศไหนขอให้อีพวกนี้เป็นกลุ่มแรกเลยค่ะ
  - [原文链接](https://twitter.com/nuknikklgku/status/2023372509819834799)
- `2026-02-17T00:00` @SJallamion ❤️5925 🔁1713 💬167
  - J’ai exercé mes fonctions en tant qu’Officier de Police Judiciaire à Lyon pendant 17 ans.  Jamais, je dis bien JAMAIS, je n’ai connu d’affaire criminelle où une conférence de presse du procureur de la République au cours de laquelle il serait dit que l’identité des auteurs était connue des services de police serait programmée avant la moindre interpellation.  Nous sommes dans la 4eme dimension…#JusticePourQuentin
  - [原文链接](https://twitter.com/SJallamion/status/2023391996652449798)
- `2026-02-17T00:00` @adamscochran ❤️5081 🔁2063 💬104
  - Between the stock market, national secrets, and billions in self-dealing government contracts, people do not realize just how looted and ransacked the US government is right now.  It is likely the largest single robbery in human history, and most people are clueless.
  - [原文链接](https://twitter.com/adamscochran/status/2023492620039946737)
- `2026-02-17T00:00` @TheNCSmaster ❤️4381 🔁390 💬33
  - It still doesn’t feel like it’s emphasized enough how fucked the economy and tech prices are that video game consoles are increasing in price post launch  Like that is UNPRECEDENTED
  - [原文链接](https://twitter.com/TheNCSmaster/status/2023511382130671724)
- `2026-02-17T00:00` @thejackhopkins ❤️3750 🔁688 💬128
  - I have a prediction: Sooner than later, one of Epstein’s victims is going to get fed up with the slow-walking BS, step to a mic, and light a match that sets proverbial asses on fire. When the system stalls long enough...someone decides it’s time. ALWAYS.
  - [原文链接](https://twitter.com/thejackhopkins/status/2023516999754932398)
- `2026-02-17T00:00` @EricLDaugh ❤️3158 🔁926 💬135
  - 🚨 BREAKING: President Trump drops BOMB on the Democrats for President’s Day, they can’t stand the winning  “Happy President’s Day! Prices and Inflation are Way Down. The Stock Market, and your 401k’s, are Way Up. Our Military is Strong and Powerful, Our Law Enforcement is GREAT, and Our Border is 100% Secure. Murders (YEAR 1900!) and Crime are at RECORD LOWS, and Our Country is Bigger, Better, and Stronger than EVER BEFORE!!! Working Hard - ENJOY YOUR DAY! President DJT”  🔥🔥🇺🇸
  - [原文链接](https://twitter.com/EricLDaugh/status/2023479635153916290)
- `2026-02-17T00:00` @WatcherGuru ❤️2817 🔁205 💬679
  - JUST IN: 🇺🇸 President Trump says "prices and inflation are way down, stock market and your 401ks are way up."
  - [原文链接](https://twitter.com/WatcherGuru/status/2023479955079000456)
- `2026-02-17T00:00` @PrometheanActn ❤️1958 🔁715 💬27
  - Secretary of State Marco Rubio revealed a 50-year-old conspiracy: the deliberate de-industrialization of America wasn't inevitable, but a conscious policy choice. This plan stripped nations of wealth and independence. We have the receipts.#USPolitics#Economy#Conspiracy
  - [原文链接](https://twitter.com/PrometheanActn/status/2023499707385803169)
- `2026-02-17T00:00` @KobeissiLetter ❤️1719 🔁398 💬96
  - Japanese markets are making history:  The correlation between the Japanese Yen and the Topix stock index just flipped positive for the first time since 2005.  This means both the Yen and Japanese stocks are rising together, a rare historical signal in this market.  The shift comes as the Yen has strengthened +1% against the USD over the last year while the Topix index has rallied +38%.  Historically, such a pattern has typically occurred during secular bull markets like Japan in 1982-1990, Germa
  - [原文链接](https://twitter.com/KobeissiLetter/status/2023473956674838651)
- `2026-02-17T00:00` @worldlibertyfi ❤️1511 🔁300 💬219
  - We’re excited to welcome global icon Nicki Minaj to the#WLF2026stage!   From dominating the charts to mastering the business of music, she will be exploring how artists are becoming entrepreneurs and what the next era of monetization looks like in a creator-led economy.@NICKIMINAJ
  - [原文链接](https://twitter.com/worldlibertyfi/status/2023488464063271180)
- `2026-02-17T00:00` @RealAlexJones ❤️1149 🔁482 💬188
  - KEY INTEL: AG Pam Bondi & Todd Blanche Are Running A Disinformation Campaign Against The President & The American People!  If Trump Doesn't Fire Bondi & Blanche He Will Be Known As The Pedo-Protector President!  "This Is A Deep State Cover-Up Operation, And They Tricked The President Of The United States Into Being Complicit In It!"
  - [原文链接](https://twitter.com/RealAlexJones/status/2023502909690835186)
- `2026-02-17T00:00` @_guillecasaus ❤️1327 🔁153 💬18
  - 🚨 NVIDIA acaba de lanzar PersonaPlex-7B.  Un modelo de voz que puede escucharte mientras responde, manteniendo conversaciones en tiempo real como un humano.  Es gratis y 100% open-source 👇
  - [原文链接](https://twitter.com/_guillecasaus/status/2023353489162973322)
- `2026-02-17T00:00` @Kyrylo_Budanov ❤️1198 🔁215 💬45
  - Ukraine needs neo-industrialization. We must gain access to modern technologies and have a highly skilled workforce. This is one of today’s key tasks, and it was exactly what we discussed this weekend at the Forum “Economy of Resilience: Leadership Challenges 2026” in Kyiv. The event was held by the Aspen Institute Kyiv in partnership with CEO Club Ukraine and the Frontier Institute.  It is obvious that no matter how heroic and professional our military is, without a strong economy the army will
  - [原文链接](https://twitter.com/Kyrylo_Budanov/status/2023463946636689709)
- `2026-02-17T00:00` @SimonDanczuk ❤️817 🔁360 💬39
  - Labour in the Gorton & Denton By-Election, at their recent event: “If you want to get fed” you’ve got to hold up a poster supporting our Parliamentary Candidate. This is treating, a criminal offence - I hope@gmpoliceare taking it seriously.
  - [原文链接](https://twitter.com/SimonDanczuk/status/2023498407273525433)

### @TheEconomist (10 条)

- `2026-02-17T00:00` An awful lot of the chatter about AI is about the final destination, artificial general intelligence, the end of humanity, an age of abundance. But what about the near future? Listen to our “Boss Class” podcast https://www.economist.com/podcasts/2026/01/29/5-closed-problem-spaces
  - [原文链接](https://twitter.com/TheEconomist/status/2023548041551077598)
- `2026-02-17T00:00` The bloody history of fatherhood bends towards co-parenting https://www.economist.com/culture/2025/05/15/why-the-best-time-to-be-a-dad-is-now?taid=6993af908d6c4d00013485b0&utm_campaign=editorial-social&utm_content=discovery.content&utm_medium=social-media.content.np&utm_source=twitter
  - [原文链接](https://twitter.com/TheEconomist/status/2023548011423334503)
- `2026-02-16T23:40` A viral reservation-trading website allows anyone who is willing to pay to get a seat at the world’s coolest restaurants. The industry wants to shut it down https://www.economist.com/culture/2025/07/24/how-much-would-you-pay-to-nab-a-table-at-a-swanky-restaurant?taid=6993aadb3889c2000167b2c4&utm_cam
  - [原文链接](https://twitter.com/TheEconomist/status/2023542958042100148)
- `2026-02-16T23:20` Many people worry about overpopulation. But an increasing number, especially in rich countries, fret about demographic shrinkage. There are several reasons to doubt the doomsayers https://www.economist.com/leaders/2025/09/11/dont-panic-about-the-global-fertility-crash?taid=6993a62a3889c2000167b2a3&u
  - [原文链接](https://twitter.com/TheEconomist/status/2023537922511606189)
- `2026-02-16T23:00` It seems conservative consumers would rather press mainstream brands to hew to their views than buy politically charged coffee beans or SIM cards http://econ.st/3MzzH4X  Photo: Reuters
  - [原文链接](https://twitter.com/TheEconomist/status/2023532948289359955)
- *... 及其他 5 条*

### @business (10 条)

- `2026-02-16T23:58` Trump pledges federal aid to stem a Potomac River sewage spill near Washington, blaming Democrats for an environmental “calamity,” prompting a rebuttal by Maryland Governor Wes Moore https://www.bloomberg.com/news/articles/2026-02-16/trump-offers-aid-for-potomac-river-spill-in-clash-with-democrats?t
  - [原文链接](https://twitter.com/business/status/2023547520882778148)
- `2026-02-16T23:55` Gold was little changed, with many traders in Asia offline for the Lunar New Year and the US closed on Monday https://www.bloomberg.com/news/articles/2026-02-16/gold-holds-near-5-000-as-lunar-new-year-holiday-mutes-trade?taid=6993ae55c4c82c00019f58ac&utm_campaign=trueanthem&utm_content=business&utm_
  - [原文链接](https://twitter.com/business/status/2023546690213474783)
- `2026-02-16T23:52` Here’s the latest news and analysis on the oil market https://www.bloomberg.com/news/articles/2026-02-16/latest-oil-market-news-and-analysis-for-feb-17?taid=6993add583e3b60001c5f113&utm_campaign=trueanthem&utm_content=business&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/business/status/2023546154584060047)
- `2026-02-16T23:46` A judge dismissed a long-running legal challenge against Santos, which had accused the Australian oil and gas producer of misleading investors over its climate strategy https://www.bloomberg.com/news/articles/2026-02-16/landmark-greenwashing-case-against-gas-producer-santos-dismissed?taid=6993ac5438
  - [原文链接](https://twitter.com/business/status/2023544538682331293)
- `2026-02-16T22:42` Get up to speed on what's moving global markets https://www.bloomberg.com/news/articles/2026-02-16/asian-stocks-set-for-muted-start-in-holiday-trade-markets-wrap?taid=69939d4a83e3b60001c5f082&utm_campaign=trueanthem&utm_content=business&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/business/status/2023528392436466126)
- *... 及其他 5 条*

### @NikkeiAsia (9 条)

- `2026-02-16T23:53` Japan's Mizuho Securities faces insider trading probe  https://s.nikkei.com/4csGKXO
  - [原文链接](https://twitter.com/NikkeiAsia/status/2023546405038461305)
- `2026-02-16T23:35` Japan's Sojitz to expand Australian rare earth imports  https://s.nikkei.com/4cxjBDA
  - [原文链接](https://twitter.com/NikkeiAsia/status/2023541695040663957)
- `2026-02-16T23:19` Japan eases screening for US-made cars in boost for Toyota's reverse imports  https://s.nikkei.com/46OhbN5
  - [原文链接](https://twitter.com/NikkeiAsia/status/2023537761316114456)
- `2026-02-16T23:04` India needs action to manage AI threat to jobs, experts tell key summit  https://s.nikkei.com/4rlF6f5
  - [原文链接](https://twitter.com/NikkeiAsia/status/2023533939986444291)
- `2026-02-16T22:44` Anthropic opens first office in India as usage and revenue surge  https://s.nikkei.com/4awlL3H
  - [原文链接](https://twitter.com/NikkeiAsia/status/2023528902593818681)
- *... 及其他 4 条*

### @WSJ (10 条)

- `2026-02-16T23:47` BHP Group has opportunities to unlock more value from its portfolio of assets, but won’t put a deadline on a target for generating as much as $10 billion from deals. https://on.wsj.com/4qEl3aM
  - [原文链接](https://twitter.com/WSJ/status/2023544823886573604)
- `2026-02-16T23:40` The Oscar-winning actor, who died Sunday at age 95, memorably performed roles ranging from a cool consigliere in ‘The Godfather’ to a military madman in ‘Apocalypse Now’ and a recovering alcoholic in ‘Tender Mercies.’ https://on.wsj.com/40d8059
  - [原文链接](https://twitter.com/WSJ/status/2023543073444082030)
- `2026-02-16T23:40` Boy Throb is a new boy band going viral on social media. But member Darshan Magdum needs an "extraordinary ability" visa to travel from India to the U.S.   The band tells The Journal podcast about their quest to get Magdum stateside. 🎧 Listen: https://on.wsj.com/469TXkv  Video
  - [原文链接](https://twitter.com/WSJ/status/2023542994394034268)
- `2026-02-16T23:20` How are points scored in curling? WSJ's Laine Higgins took a trip to Ardsley Curling Club to find out.  Video
  - [原文链接](https://twitter.com/WSJ/status/2023537970024702312)
- `2026-02-16T23:05` Beretta is taking aim at one of its biggest American rivals, amassing a 10% stake in rifle maker Ruger https://on.wsj.com/4bXmdKT
  - [原文链接](https://twitter.com/WSJ/status/2023534221780783191)
- *... 及其他 5 条*

### @TheInformation (10 条)

- `2026-02-16T22:45` A University of Michigan team is adapting ultra-light carbon fluorine chemistry used in space, once thought to be non-rechargeable. https://thein.fo/4tzrHSm
  - [原文链接](https://twitter.com/TheInformation/status/2023529074958688636)
- `2026-02-16T21:45` ServiceNow positions itself as the “middleman” connecting a company’s fragmented systems—exactly the kind of role businesses may need more of as they deploy AI. https://thein.fo/4coTdf3
  - [原文链接](https://twitter.com/TheInformation/status/2023513981642539148)
- `2026-02-16T20:15` For OpenAI, preventing leaks isn’t just about PR—it’s also about protecting intellectual property like model weights and trade secrets. https://thein.fo/4rO9WNx
  - [原文链接](https://twitter.com/TheInformation/status/2023491329620087276)
- `2026-02-16T19:45` Despite their limitations, AI “skills” are written in plain language — making them easier to audit and update than model weights. https://thein.fo/4rQBfH3
  - [原文链接](https://twitter.com/TheInformation/status/2023483777444438251)
- `2026-02-16T18:45` Despite talk of space-based compute, xAI is expanding on Earth — including plans to bring up to 1 million Nvidia GPUs online near Memphis. https://thein.fo/3MF9vGd
  - [原文链接](https://twitter.com/TheInformation/status/2023468684153401476)
- *... 及其他 5 条*

### @SCMPNews (10 条)

- `2026-02-16T22:38` Iran’s foreign minister in Geneva for second round of talks with US.  https://www.scmp.com/news/world/middle-east/article/3343656/irans-top-diplomat-attend-indirect-talks-us-geneva-state-news-says?utm_medium=Social&utm_source=Twitter#Echobox=1771275645-1
  - [原文链接](https://twitter.com/SCMPNews/status/2023527499917844811)
- `2026-02-16T21:49` ‘Work to be done’: EU says it’s not ready to give Ukraine a membership date.  https://www.scmp.com/news/world/europe/article/3343638/eu-not-ready-give-ukraine-date-membership-says-blocs-foreign-policy-chief-kallas?utm_medium=Social&utm_source=Twitter#Echobox=1771275452-1
  - [原文链接](https://twitter.com/SCMPNews/status/2023515156135731643)
- `2026-02-16T21:23` http://localhost/SCMPNews Read more: https://sc.mp/80b722
  - [原文链接](https://twitter.com/SCMPNews/status/2023508547720364356)
- `2026-02-16T21:23` Anthropic wants to put safeguards in place to stop Claude from being used for mass surveillance of Americans or to develop weapons.  (Link in comments)  http://localhost/search?q=%23usa http://localhost/search?q=%23pentagon http://localhost/search?q=%23ai http://localhost/search?q=%23claude http://l
  - [原文链接](https://twitter.com/SCMPNews/status/2023508538882990328)
- `2026-02-16T20:34` http://localhost/SCMPNews Read more: https://sc.mp/f67ab1
  - [原文链接](https://twitter.com/SCMPNews/status/2023496137513062875)
- *... 及其他 5 条*

### @elonmusk (8 条)

- `2026-02-16T21:53` If you’re in Korea and want to work on chip design, fabrication or AI software, join Tesla!  Tesla AI (@Tesla_AI)  We’re hiring AI chip design engineers in Korea  — http://localhost/Tesla_AI/status/2022853328707948847#m
  - [原文链接](https://twitter.com/elonmusk/status/2023516129457758483)
- `2026-02-16T21:34` 🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷  Tesla Korea (@tesla_korea)  [Tesla Korea 채용공고 - AI Chip Design Engineer]  Tesla에서 세계 최고 수준의 대량 생산 AI 칩 개발에 함께할 인재를 찾습니다.  해당 프로젝트는 향후 세계에서 가장 높은 생산량을 기록할 AI 칩 아키텍처 개발을 목표로 합니다.  📌 모집 직무  AI Chip Design Engineer  📌 지원 방법  아래 내용을 포함하여 Ai_Chips@Tesla.com 이메일 지원  - 본인이 
  - [原文链接](https://twitter.com/elonmusk/status/2023511421779354015)
- `2026-02-16T21:29` Model S & X are great cars!  Order yours before we sunset the program in a few months.   http://Tesla.com  Sawyer Merritt (@SawyerMerritt)  Doug DeMuro ranked the http://localhost/Tesla Model S as the #1 most important car of the last 30 years in his new video.  Doug: "The Model S really changed the
  - [原文链接](https://twitter.com/elonmusk/status/2023510007577538718)
- `2026-02-16T20:27` Important read  Gad Saad (@GadSaad)  My inaugural X article is at 40,000 views.  Not bad but let's increase that figure!  Read and share.  — http://localhost/GadSaad/status/2023408019703501084#m
  - [原文链接](https://twitter.com/elonmusk/status/2023494489781006691)
- `2026-02-16T19:43` 🚨http://localhost/search?q=%23BREAKING: In a horrifying revelation, Chapel Hill NC police have confirmed that the two men who broke into a North Carolina man's home, tied him up, beat him, and then se*ually assaulted him at knife-point...  ...ARE BOTH ILLEGAL IMMIGRANTS!!!!!!!  There will be no prot
  - [原文链接](https://twitter.com/elonmusk/status/2023483416126390346)
- *... 及其他 3 条*

### @karpathy (1 条)

- `2026-02-16T19:15` I think it must be a very interesting time to be in programming languages and formal methods because LLMs change the whole constraints landscape of software completely. Hints of this can already be seen, e.g. in the rising momentum behind porting C to Rust or the growing interest in upgrading legacy
  - [原文链接](https://twitter.com/karpathy/status/2023476423055601903)

### @TechCrunch (4 条)

- `2026-02-16T18:56` Have money, will travel: a16z’s hunt for the next European unicorn https://techcrunch.com/2026/02/16/have-money-will-travel-a16zs-hunt-for-the-next-european-unicorn/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2023471508631494892)
- `2026-02-16T17:03` How Ricursive Intelligence raised $335M at a $4B valuation in 4 months https://techcrunch.com/2026/02/16/how-ricursive-intelligence-raised-335m-at-a-4b-valuation-in-4-months/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2023443178863686135)
- `2026-02-16T14:03` Flapping Airplanes on the future of AI: ‘We want to try really radically different things’ https://techcrunch.com/2026/02/16/flapping-airplanes-on-the-future-of-ai-we-want-to-try-really-radically-different-things/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2023397885854044396)
- `2026-02-16T13:18` After all the hype, some AI experts don’t think OpenClaw is all that exciting https://techcrunch.com/2026/02/16/after-all-the-hype-some-ai-experts-dont-think-openclaw-is-all-that-exciting/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2023386547249426658)

### @sama (3 条)

- `2026-02-16T18:24` 🦞
  - [原文链接](https://twitter.com/sama/status/2023463428892094655)
- `2026-02-16T17:43` (Also best family ❤️)
  - [原文链接](https://twitter.com/sama/status/2023453150334906839)
- `2026-02-16T17:43` Best OpenAI sweatshirt ever
  - [原文链接](https://twitter.com/sama/status/2023453083595141411)

### @MessariCrypto (1 条)

- `2026-02-16T16:35` Join http://localhost/0xCryptoSam for not one...but TWO panels at ETH Denver!  Panel #1: Institutional DeFi Panel - Feb 17 @ 12:50  DeFi for big players  Panel #2: HypeFest - Feb 17 @ 2:30PM  All about Hyperliquid and the "perpification of everything."  You won't want to miss EITHER of these
  - [原文链接](https://twitter.com/MessariCrypto/status/2023435977444737442)

### @VitalikButerin (1 条)

- `2026-02-16T16:27` You do not have to agree with me on which applications are and are not corposlop to use Ethereum.  You do not have to agree with me on what trust assumptions are acceptable in which situations to use Ethereum.  You do not have to agree with me on political topics to use Ethereum.  You do not have to
  - [原文链接](https://twitter.com/VitalikButerin/status/2023433964082602009)

### @DefiLlama (2 条)

- `2026-02-16T15:58` RWA dashboard available here:  https://defillama.com/rwa
  - [原文链接](https://twitter.com/DefiLlama/status/2023426841214898569)
- `2026-02-16T15:58` We added nested treemaps to our RWA page to better visualize which asset categories, classes and platforms make up the RWA landscape.  Drill down to over 500 tokenized assets across multiple dimensions.  Video
  - [原文链接](https://twitter.com/DefiLlama/status/2023426838119207110)

### @globaltimesnews (2 条)

- `2026-02-16T15:27` In "WuBot," the robot martial arts performance at the 2026 Year of the Horse Spring Festival Gala, the bots transformed into kung fu warriors, nailing backflips, drunken fist, and nunchaku with seamless, pinpoint precision. From dance in 2025 gala to kung fu in 2026 gala, witness the leaps in China’
  - [原文链接](https://twitter.com/globaltimesnews/status/2023418913053458734)
- `2026-02-16T15:22` Chinese tech firm http://localhost/search?q=%23Unitree humanoid robots made a spectacular return to the Spring Festival Gala on Monday, captivating audiences this year with a dynamic routine featuring parkour, Drunken Fist, and nunchaku—a significant upgrade from their stunning Yangko dance performa
  - [原文链接](https://twitter.com/globaltimesnews/status/2023417671640080623)

### @DeItaone (2 条)

- `2026-02-16T14:47` GOLD $20,000 CALLS SURGE DESPITE RECORD SELLOFF  Deep out-of-the-money bullish bets on gold are building even after a historic correction.  After COMEX gold futures briefly topped $5,600 an ounce in late January before suffering their largest one-day drop in decades, traders began accumulating Decem
  - [原文链接](https://twitter.com/DeItaone/status/2023408940692697301)
- `2026-02-16T14:33` DOLLAR SHORTS HIT 14-YEAR EXTREME  Dollar positioning turned the most negative in over 14 years in February, according to Bank of America’s latest FX and rates sentiment survey. Short bets against the dollar are now at their highest since January 2012, the earliest data point available.  Fund manage
  - [原文链接](https://twitter.com/DeItaone/status/2023405376100823261)

## 📱 微信公众号

暂无数据

## 🔥 NewsNow 热榜 (120 条)

### 知乎

| 排名 | 标题 |
|------|------|
| #1 | [2026 年央视春晚中有哪些亮点？哪个节目最让你印象深刻？](https://www.zhihu.com/question/2006817906369979378) |
| #2 | [如何评价宇树科技机器人在 2026 年春晚的武术表演《武 BOT》？与去年的《秧 BOT》相比有哪些进步？](https://www.zhihu.com/question/2006826244814104012) |
| #3 | [如何评价 2026 年春晚王菲表演的歌曲《你我经历的一刻》？](https://www.zhihu.com/question/2006854372475232588) |
| #4 | [如何评价沈腾、马丽、银河通用机器人等 2026 年春晚上表演的贺岁微电影《我最难忘的今宵》？](https://www.zhihu.com/question/2006865473459942662) |
| #5 | [2026 春节档总票房含预售突破 6 亿，《飞驰人生 3》预售破 2 亿，今年春节档是否格局已定？](https://www.zhihu.com/question/2006732300956694383) |
| #6 | [2026 央视春晚无相声节目，怎样看待这一变化？相声这种艺术形式真的过时了吗？](https://www.zhihu.com/question/2006741289241113569) |
| #7 | [电视剧《大明王朝》里，司礼监大太监们夜宵就是吃碗面条，是不是太寒酸了点，真实吗？](https://www.zhihu.com/question/2006058834934916188) |
| #8 | [很多年轻人明知去大城市没前途，为什么还要去？](https://www.zhihu.com/question/457100446) |
| #9 | [「年夜饭摄影大赛」又开始了，可以看看你的参赛作品吗？](https://www.zhihu.com/question/2005635243948917798) |
| #10 | [Seedance 2.0 分镜运镜做的这么好，未来导演会不会逐渐失业？](https://www.zhihu.com/question/2004599527957557412) |

### 今日头条

| 排名 | 标题 |
|------|------|
| #1 | [春晚机器人中国功夫夯爆了](https://www.toutiao.com/trending/7607438781827366955/) |
| #2 | [谷爱凌自由式滑雪女子大跳台摘银](https://www.toutiao.com/trending/7607051298696908330/) |
| #3 | [骏马迎春焕新潮](https://www.toutiao.com/trending/7606669748105170451/) |
| #5 | [从秧BOT到武BOT 机器人发展有多快](https://www.toutiao.com/trending/7607451566442184758/) |
| #6 | [秦岚李沁王楚然美成啥了](https://www.toutiao.com/trending/7606869652907576838/) |
| #7 | [拼手气红包怎么抢最大](https://www.toutiao.com/trending/7606273692196408895/) |
| #8 | [春晚再出金句](https://www.toutiao.com/trending/7607078259876003876/) |
| #9 | [你如何看待过年群发祝福](https://www.toutiao.com/trending/7607284935024181298/) |
| #10 | [冬奥最强教练执教13国 现场飞速换队服](https://www.toutiao.com/trending/7607307736673455626/) |
| #11 | [菲律宾总统：欢迎中国的决定](https://www.toutiao.com/trending/7606306238615453702/) |

### 百度热搜

| 排名 | 标题 |
|------|------|
| #1 | [总台马年春晚](https://www.baidu.com/s?wd=%E6%80%BB%E5%8F%B0%E9%A9%AC%E5%B9%B4%E6%98%A5%E6%99%9A) |
| #2 | [王菲一开口时间都慢了](https://www.baidu.com/s?wd=%E7%8E%8B%E8%8F%B2%E4%B8%80%E5%BC%80%E5%8F%A3%E6%97%B6%E9%97%B4%E9%83%BD%E6%85%A2%E4%BA%86) |
| #3 | [来自天宫的新春问候请查收](https://www.baidu.com/s?wd=%E6%9D%A5%E8%87%AA%E5%A4%A9%E5%AE%AB%E7%9A%84%E6%96%B0%E6%98%A5%E9%97%AE%E5%80%99%E8%AF%B7%E6%9F%A5%E6%94%B6) |
| #4 | [尼格买提终于和大家一样了](https://www.baidu.com/s?wd=%E5%B0%BC%E6%A0%BC%E4%B9%B0%E6%8F%90%E7%BB%88%E4%BA%8E%E5%92%8C%E5%A4%A7%E5%AE%B6%E4%B8%80%E6%A0%B7%E4%BA%86) |
| #5 | [30年后春晚真有蔡明同款机器人了](https://www.baidu.com/s?wd=30%E5%B9%B4%E5%90%8E%E6%98%A5%E6%99%9A%E7%9C%9F%E6%9C%89%E8%94%A1%E6%98%8E%E5%90%8C%E6%AC%BE%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%BA%86) |
| #6 | [谷爱凌自由式滑雪女子大跳台夺银](https://www.baidu.com/s?wd=%E8%B0%B7%E7%88%B1%E5%87%8C%E8%87%AA%E7%94%B1%E5%BC%8F%E6%BB%91%E9%9B%AA%E5%A5%B3%E5%AD%90%E5%A4%A7%E8%B7%B3%E5%8F%B0%E5%A4%BA%E9%93%B6) |
| #7 | [初一迎春接福 马年跃马呈祥](https://www.baidu.com/s?wd=%E5%88%9D%E4%B8%80%E8%BF%8E%E6%98%A5%E6%8E%A5%E7%A6%8F+%E9%A9%AC%E5%B9%B4%E8%B7%83%E9%A9%AC%E5%91%88%E7%A5%A5) |
| #8 | [凤凰传奇一开口就是国泰民安](https://www.baidu.com/s?wd=%E5%87%A4%E5%87%B0%E4%BC%A0%E5%A5%87%E4%B8%80%E5%BC%80%E5%8F%A3%E5%B0%B1%E6%98%AF%E5%9B%BD%E6%B3%B0%E6%B0%91%E5%AE%89) |
| #11 | [炖肉时的浮沫是营养精华？假的](https://www.baidu.com/s?wd=%E7%82%96%E8%82%89%E6%97%B6%E7%9A%84%E6%B5%AE%E6%B2%AB%E6%98%AF%E8%90%A5%E5%85%BB%E7%B2%BE%E5%8D%8E%EF%BC%9F%E5%81%87%E7%9A%84) |

### 抖音

| 排名 | 标题 |
|------|------|
| #1 | [央视马年春晚](https://www.douyin.com/hot/2402899) |
| #2 | [大国重器硬核拜年](https://www.douyin.com/hot/2402837) |
| #3 | [快来看看神二十一的年夜饭有什么](https://www.douyin.com/hot/2403348) |
| #4 | [又是一年难忘今宵](https://www.douyin.com/hot/2403466) |
| #5 | [谷爱凌大跳台摘银](https://www.douyin.com/hot/2402478) |
| #6 | [机器人中国功夫夯爆了](https://www.douyin.com/hot/2403259) |
| #7 | [春晚机器人齐聚抖音](https://www.douyin.com/hot/2403438) |
| #8 | [刘少昂林孝埈晋级1/4决赛](https://www.douyin.com/hot/2402760) |
| #9 | [今年的春节祝福这样说](https://www.douyin.com/hot/2401854) |
| #10 | [家庭春节联欢晚会](https://www.douyin.com/hot/2402742) |

### 澎湃新闻

| 排名 | 标题 |
|------|------|
| #1 | [今晚见！央视总台《2026年春节联欢晚会》节目单发布](https://www.thepaper.cn/newsDetail_forward_32620957) |
| #2 | [阿里除夕开源千问3.5：性能媲美Gemini 3 Pro， 实现原生多模态模型代际跃迁](https://www.thepaper.cn/newsDetail_forward_32621821) |
| #3 | [中青评论：过年点外卖，是在给骑手添麻烦吗](https://www.thepaper.cn/newsDetail_forward_32620979) |
| #4 | [内塔尼亚胡：以色列计划10年内停止接受美国资金援助](https://www.thepaper.cn/newsDetail_forward_32620966) |
| #5 | [放马过来，“申”情款待丨年味马不停蹄，抢“鲜”一步](https://www.thepaper.cn/newsDetail_forward_32543760) |
| #6 | [中国学者慕安会驳斥所谓“中国威胁”：臆测！中国始终在合作](https://www.thepaper.cn/newsDetail_forward_32620360) |
| #7 | [驻日本使馆发言人就日方所谓交涉答记者问](https://www.thepaper.cn/newsDetail_forward_32622456) |
| #8 | [爱我中华·千里江山图丨灵蛇起舞辞旧岁，骏马昂首迎新春](https://www.thepaper.cn/newsDetail_forward_25061346) |
| #9 | [希拉里回应爱泼斯坦案：可怕，但名字出现在文件中不意味犯罪](https://www.thepaper.cn/newsDetail_forward_32621182) |
| #10 | [这个春节，人形机器人正在实现“能演亦能干”](https://www.thepaper.cn/newsDetail_forward_32618240) |

### 财联社热门

| 排名 | 标题 |
|------|------|
| #1 | [白银基金出台补偿方案！2月26日可办理，1000元以下损失全额补偿](https://www.cls.cn/detail/2290657) |
| #2 | [盘点春晚合作公司名单，覆盖智能出行、人工智能机器人、白酒等领域](https://www.cls.cn/detail/2290769) |
| #3 | [马年春晚黑科技！四家机器人同台献技 AI大模型渗透内容制作](https://www.cls.cn/detail/2290959) |
| #4 | [AI遇上最强春节档 Token通胀已成必然？](https://www.cls.cn/detail/2290600) |
| #5 | [今年春晚，机器人刷屏了](https://www.cls.cn/detail/2290956) |
| #6 | [除夕不看春晚开电话会，这些券商太拼了！春节期间电话会近300场](https://www.cls.cn/detail/2290646) |
| #7 | [习近平：当前经济工作的重点任务](https://www.cls.cn/detail/2290573) |
| #8 | [AI电荒把燃气轮机“捧上C位” 龙头企业：需求极其旺盛 交付排到2030年](https://www.cls.cn/detail/2290580) |
| #9 | [告别“码农”时代？马斯克预言“就在年底”，国产大模型春节竞速AI编程](https://www.cls.cn/detail/2290650) |
| #10 | [保利集团发布严正声明](https://www.cls.cn/detail/2290639) |

### 华尔街见闻

| 排名 | 标题 |
|------|------|
| #1 | [AI热潮助力港股蛇年收官战告捷，MiniMax暴涨25%、智谱涨4.74%齐创新高，有色板块拉升](https://wallstreetcn.com/articles/3765773) |
| #2 | [AI圈内人士：巨大变革正在发生，人们还懵懂不知](https://wallstreetcn.com/articles/3765774) |
| #3 | [达利欧万字长文：旧秩序已死，世界重回“丛林法则”，贸易战和资本战将成常态](https://wallstreetcn.com/articles/3765762) |
| #4 | [阿里发布千问3.5，性能媲美Gemini 3， Token价格仅为其1/18](https://wallstreetcn.com/articles/3765786) |
| #5 | [OpenClaw创始人加入OpenAI，目标“开发一款连我妈妈都能用的AI助手”](https://wallstreetcn.com/articles/3765772) |
| #6 | [华尔街见闻早餐FM-Radio \| 2026年2月16日](https://wallstreetcn.com/articles/3765727) |
| #7 | [存储芯片，走向失控](https://wallstreetcn.com/articles/3765777) |
| #8 | [木头姐：这轮市场波动是算法导致，而非基本面](https://wallstreetcn.com/articles/3765784) |
| #9 | [新春伊始，如何看待人民币升值？](https://wallstreetcn.com/articles/3765776) |
| #10 | [行业首例！国投白银LOF估值调整补偿方案出炉：1000元以下损失全额补偿](https://wallstreetcn.com/articles/3765768) |

### 凤凰网

| 排名 | 标题 |
|------|------|
| #1 | [日方提出交涉，中使馆：纯属狡辩、已予驳回](https://news.ifeng.com/c/8qnzjAl3cU5) |
| #2 | [2026慕安会闭幕，欧洲开始有一个新变化](https://news.ifeng.com/c/8qnD3B7dZfA) |
| #3 | [荷兰国防官员：F-35战机或可像iPhone手机一样“越狱”](https://news.ifeng.com/c/8qnEVl9tHXs) |
| #4 | [学者：美伊这轮谈判的逻辑变了，风险陡增](https://news.ifeng.com/c/8qnxRMK23SB) |
| #5 | [爱泼斯坦案“政治敏感人物”名单公布](https://news.ifeng.com/c/8qnNgCTDt2B) |
| #6 | [英防卫大臣：俄军伤亡惨重，1.7万朝军在俄作战](https://news.ifeng.com/c/8qn6JNCebd2) |
| #7 | [希拉里与捷克副总理，当众“吵起来了”](https://news.ifeng.com/c/8qn7o7BaUvS) |
| #8 | [克宫：这次谈判将讨论领土问题](https://news.ifeng.com/c/8qnNYAZwwTm) |
| #9 | [除夕玩“开运转盘”，张善政连线马英九、蒋万安等人](https://news.ifeng.com/c/8qnbuZ7y4z4) |
| #10 | [高市早苗，迎来坏消息](https://news.ifeng.com/c/8qnPmJKPPlq) |

### bilibili 热搜

| 排名 | 标题 |
|------|------|
| #1 | [总台马年春晚完整版](https://search.bilibili.com/all?keyword=%E6%80%BB%E5%8F%B0%E9%A9%AC%E5%B9%B4%E6%98%A5%E6%99%9A%E5%AE%8C%E6%95%B4%E7%89%88) |
| #2 | [凤凰传奇广场舞神曲上新](https://search.bilibili.com/all?keyword=%E5%87%A4%E5%87%B0%E4%BC%A0%E5%A5%87%E5%B9%BF%E5%9C%BA%E8%88%9E%E7%A5%9E%E6%9B%B2%E4%B8%8A%E6%96%B0) |
| #3 | [2026拜年纪全程回顾](https://search.bilibili.com/all?keyword=2026%E6%8B%9C%E5%B9%B4%E7%BA%AA%E5%85%A8%E7%A8%8B%E5%9B%9E%E9%A1%BE) |
| #4 | [蔡明30年后成真机器人](https://search.bilibili.com/all?keyword=%E8%94%A1%E6%98%8E30%E5%B9%B4%E5%90%8E%E6%88%90%E7%9C%9F%E6%9C%BA%E5%99%A8%E4%BA%BA) |
| #5 | [沈马组合春晚短剧来了](https://search.bilibili.com/all?keyword=%E6%B2%88%E9%A9%AC%E7%BB%84%E5%90%88%E6%98%A5%E6%99%9A%E7%9F%AD%E5%89%A7%E6%9D%A5%E4%BA%86) |
| #7 | [大学生春晚压中春晚魔术题](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%94%9F%E6%98%A5%E6%99%9A%E5%8E%8B%E4%B8%AD%E6%98%A5%E6%99%9A%E9%AD%94%E6%9C%AF%E9%A2%98) |
| #8 | [和留守儿童一起过新年](https://search.bilibili.com/all?keyword=%E5%92%8C%E7%95%99%E5%AE%88%E5%84%BF%E7%AB%A5%E4%B8%80%E8%B5%B7%E8%BF%87%E6%96%B0%E5%B9%B4) |
| #9 | [难忘今宵再次唱响春晚](https://search.bilibili.com/all?keyword=%E9%9A%BE%E5%BF%98%E4%BB%8A%E5%AE%B5%E5%86%8D%E6%AC%A1%E5%94%B1%E5%93%8D%E6%98%A5%E6%99%9A) |
| #10 | [春晚机器人硬核诠释中国功夫](https://search.bilibili.com/all?keyword=%E6%98%A5%E6%99%9A%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%A1%AC%E6%A0%B8%E8%AF%A0%E9%87%8A%E4%B8%AD%E5%9B%BD%E5%8A%9F%E5%A4%AB) |
| #11 | [拜年神曲的全新打开方式](https://search.bilibili.com/all?keyword=%E6%8B%9C%E5%B9%B4%E7%A5%9E%E6%9B%B2%E7%9A%84%E5%85%A8%E6%96%B0%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F) |

### 微博

| 排名 | 标题 |
|------|------|
| #1 | [春晚收视率](https://s.weibo.com/weibo?q=%E6%98%A5%E6%99%9A%E6%94%B6%E8%A7%86%E7%8E%87) |
| #2 | [谷爱凌大跳台银牌](https://s.weibo.com/weibo?q=%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%A7%E8%B7%B3%E5%8F%B0%E9%93%B6%E7%89%8C) |
| #3 | [春晚分会场上大分](https://s.weibo.com/weibo?q=%23%E6%98%A5%E6%99%9A%E5%88%86%E4%BC%9A%E5%9C%BA%E4%B8%8A%E5%A4%A7%E5%88%86%23) |
| #4 | [沈腾 说错词](https://s.weibo.com/weibo?q=%E6%B2%88%E8%85%BE+%E8%AF%B4%E9%94%99%E8%AF%8D) |
| #5 | [春晚](https://s.weibo.com/weibo?q=%E6%98%A5%E6%99%9A) |
| #6 | [谷爱凌创造自由式滑雪奖牌纪录](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E5%88%9B%E9%80%A0%E8%87%AA%E7%94%B1%E5%BC%8F%E6%BB%91%E9%9B%AA%E5%A5%96%E7%89%8C%E7%BA%AA%E5%BD%95%23) |
| #7 | [马丽单飞了 沈腾怎么办](https://s.weibo.com/weibo?q=%E9%A9%AC%E4%B8%BD%E5%8D%95%E9%A3%9E%E4%BA%86+%E6%B2%88%E8%85%BE%E6%80%8E%E4%B9%88%E5%8A%9E) |
| #8 | [短剧上春晚了](https://s.weibo.com/weibo?q=%E7%9F%AD%E5%89%A7%E4%B8%8A%E6%98%A5%E6%99%9A%E4%BA%86) |
| #9 | [过年好](https://s.weibo.com/weibo?q=%E8%BF%87%E5%B9%B4%E5%A5%BD) |
| #10 | [大年初一](https://s.weibo.com/weibo?q=%E5%A4%A7%E5%B9%B4%E5%88%9D%E4%B8%80) |

### 贴吧

| 排名 | 标题 |
|------|------|
| #1 | [手滑删存档,亚瑟真人谢罪](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%89%8B%E6%BB%91%E5%88%A0%E5%AD%98%E6%A1%A3%2C%E4%BA%9A%E7%91%9F%E7%9C%9F%E4%BA%BA%E8%B0%A2%E7%BD%AA&topic_id=28350747) |
| #2 | [C妈怒砍2分,百貌哈桑封神](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=C%E5%A6%88%E6%80%92%E7%A0%8D2%E5%88%86%2C%E7%99%BE%E8%B2%8C%E5%93%88%E6%A1%91%E5%B0%81%E7%A5%9E&topic_id=28350748) |
| #3 | [软饭男喊冤,贴吧判官怒了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%BD%AF%E9%A5%AD%E7%94%B7%E5%96%8A%E5%86%A4%2C%E8%B4%B4%E5%90%A7%E5%88%A4%E5%AE%98%E6%80%92%E4%BA%86&topic_id=28350741) |
| #4 | [留学新思路:打包教授带回国](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%95%99%E5%AD%A6%E6%96%B0%E6%80%9D%E8%B7%AF%3A%E6%89%93%E5%8C%85%E6%95%99%E6%8E%88%E5%B8%A6%E5%9B%9E%E5%9B%BD&topic_id=28350742) |
| #5 | [26年春晚:到位or不到味](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=26%E5%B9%B4%E6%98%A5%E6%99%9A%3A%E5%88%B0%E4%BD%8Dor%E4%B8%8D%E5%88%B0%E5%91%B3&topic_id=28350743) |
| #6 | [太夯!宇树机器人三刷春晚](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%A4%AA%E5%A4%AF%21%E5%AE%87%E6%A0%91%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%B8%89%E5%88%B7%E6%98%A5%E6%99%9A&topic_id=28350744) |
| #7 | [Steam擦边,恭喜发财变发春](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=Steam%E6%93%A6%E8%BE%B9%2C%E6%81%AD%E5%96%9C%E5%8F%91%E8%B4%A2%E5%8F%98%E5%8F%91%E6%98%A5&topic_id=28350738) |
| #8 | [闺蜜创业内斗,7人8群吵翻天](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%97%BA%E8%9C%9C%E5%88%9B%E4%B8%9A%E5%86%85%E6%96%97%2C7%E4%BA%BA8%E7%BE%A4%E5%90%B5%E7%BF%BB%E5%A4%A9&topic_id=28350737) |
| #9 | [罗翔悟了:人不该有偶像](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%BD%97%E7%BF%94%E6%82%9F%E4%BA%86%3A%E4%BA%BA%E4%B8%8D%E8%AF%A5%E6%9C%89%E5%81%B6%E5%83%8F&topic_id=28350736) |
| #10 | [今晚见!央视春晚节目单公开](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BB%8A%E6%99%9A%E8%A7%81%21%E5%A4%AE%E8%A7%86%E6%98%A5%E6%99%9A%E8%8A%82%E7%9B%AE%E5%8D%95%E5%85%AC%E5%BC%80&topic_id=28350740) |

## 🔗 原始链接索引

### 🐦 Twitter 原文 (80/113 条)

- [2026-02-17T00:00 @KimDotcom [热门] | Breaking Palantir was allegedly hacked. An AI agent was used to gain super-user access and...](https://twitter.com/KimDotcom/status/2023165849721536672)
- [2026-02-17T00:00 @elonmusk [热门] | Yup 😂 That really made him upset. After I ghosted him, Epstein went on a massive campaign ...](https://twitter.com/elonmusk/status/2023302989872771110)
- [2026-02-17T00:00 @TBSCDTV [热门] | #CDTVライブライブ3月9日(月)よる7時⚡️ ＼👑豪華出演者発表🌟／#AI「ラッキーアイラブユー」#WEST.「これでいいのだ！」#キタニタツヤfeat.#BABYMETAL「...](https://twitter.com/TBSCDTV/status/2023365491948245021)
- [2026-02-17T00:00 @SpacemanAp [热门] | Western media won’t air this bc they don’t want you to grow a brain & realize “wait, I can...](https://twitter.com/SpacemanAp/status/2022438260275056995)
- [2026-02-17T00:00 @LeadingReport [热门] | BREAKING: US housing market reaches most “unaffordable” level in history, per St. Louis Fe...](https://twitter.com/LeadingReport/status/2023421333477179570)
- [2026-02-17T00:00 @Flicky0ps [热门] | i will never get over the fact that people now associate em dashes and semicolons with ai ...](https://twitter.com/Flicky0ps/status/2023455023112614236)
- [2026-02-17T00:00 @nuknikklgku [热门] | เตือน‼️ เจ้าของกิจการจังหวัดท่องเที่ยว อีพวก Israeli มีทริคใหม่คือ gen ai เอารูปไม่จริงมาร...](https://twitter.com/nuknikklgku/status/2023372509819834799)
- [2026-02-17T00:00 @SJallamion [热门] | J’ai exercé mes fonctions en tant qu’Officier de Police Judiciaire à Lyon pendant 17 ans. ...](https://twitter.com/SJallamion/status/2023391996652449798)
- [2026-02-17T00:00 @adamscochran [热门] | Between the stock market, national secrets, and billions in self-dealing government contra...](https://twitter.com/adamscochran/status/2023492620039946737)
- [2026-02-17T00:00 @TheNCSmaster [热门] | It still doesn’t feel like it’s emphasized enough how fucked the economy and tech prices a...](https://twitter.com/TheNCSmaster/status/2023511382130671724)
- [2026-02-17T00:00 @thejackhopkins [热门] | I have a prediction: Sooner than later, one of Epstein’s victims is going to get fed up wi...](https://twitter.com/thejackhopkins/status/2023516999754932398)
- [2026-02-17T00:00 @EricLDaugh [热门] | 🚨 BREAKING: President Trump drops BOMB on the Democrats for President’s Day, they can’t st...](https://twitter.com/EricLDaugh/status/2023479635153916290)
- [2026-02-17T00:00 @WatcherGuru [热门] | JUST IN: 🇺🇸 President Trump says "prices and inflation are way down, stock market and your...](https://twitter.com/WatcherGuru/status/2023479955079000456)
- [2026-02-17T00:00 @PrometheanActn [热门] | Secretary of State Marco Rubio revealed a 50-year-old conspiracy: the deliberate de-indust...](https://twitter.com/PrometheanActn/status/2023499707385803169)
- [2026-02-17T00:00 @KobeissiLetter [热门] | Japanese markets are making history: The correlation between the Japanese Yen and the Topi...](https://twitter.com/KobeissiLetter/status/2023473956674838651)
- [2026-02-17T00:00 @worldlibertyfi [热门] | We’re excited to welcome global icon Nicki Minaj to the#WLF2026stage! From dominating the ...](https://twitter.com/worldlibertyfi/status/2023488464063271180)
- [2026-02-17T00:00 @RealAlexJones [热门] | KEY INTEL: AG Pam Bondi & Todd Blanche Are Running A Disinformation Campaign Against The P...](https://twitter.com/RealAlexJones/status/2023502909690835186)
- [2026-02-17T00:00 @_guillecasaus [热门] | 🚨 NVIDIA acaba de lanzar PersonaPlex-7B. Un modelo de voz que puede escucharte mientras re...](https://twitter.com/_guillecasaus/status/2023353489162973322)
- [2026-02-17T00:00 @Kyrylo_Budanov [热门] | Ukraine needs neo-industrialization. We must gain access to modern technologies and have a...](https://twitter.com/Kyrylo_Budanov/status/2023463946636689709)
- [2026-02-17T00:00 @SimonDanczuk [热门] | Labour in the Gorton & Denton By-Election, at their recent event: “If you want to get fed”...](https://twitter.com/SimonDanczuk/status/2023498407273525433)
- [2026-02-17T00:00 @dom_lucre [热门] | 🔥🚨VIRAL NOW: Footage of NBA star Steph Curry being fed by 3 men in 2018 has resurfaced ami...](https://twitter.com/dom_lucre/status/2023536647501910332)
- [2026-02-17T00:00 @zanelittlemusic [热门] | The rant about why our current AI systems are useless and stupid from that video:](https://twitter.com/zanelittlemusic/status/2023512460477772174)
- [2026-02-17T00:00 @LisaSu [热门] | Happy#LunarNewYear! Wishing our friends, colleagues and the@AMDfamily around the world a h...](https://twitter.com/LisaSu/status/2023531313891066133)
- [2026-02-17T00:00 @i_aadk [热门] | Heureusement j’ai le rire facile purée parce que vu comme la vie c’est dur manquerait plus...](https://twitter.com/i_aadk/status/2023426917307945337)
- [2026-02-17T00:00 @yuyake_hino [热门] | 超かぐや姫のメインキャラクター3人が高性能AI配信者、月から来た輝夜、クリエイティブ限界バイト世知辛狐娘ってコト？(キズナアイ、輝夜月、バーチャルのじゃロリ狐娘Youtuberおじ...](https://twitter.com/yuyake_hino/status/2023325661344203039)
- [2026-02-17T00:00 @patinhoriki [热门] | ai meu deus elas tão muito perfeitas tô passando mal minhas princesas lindas](https://twitter.com/patinhoriki/status/2023421044846182674)
- [2026-02-17T00:00 @MaryBowdenMD [热门] | Nonprofit hospital Houston Methodist earning billions off security tradings YET PAYS NO TA...](https://twitter.com/MaryBowdenMD/status/2023535689678417967)
- [2026-02-17T00:00 @Bankless [热门] | LIVE NOW - Lyn Alden: How to Survive The Gradual Print Era — Fed Chair Warsh, Gold & Bitco...](https://twitter.com/Bankless/status/2023406889472504004)
- [2026-02-17T00:00 @WojaksX [热门] | $PUNCHannounces Binance partnership to drive Solana exposure and liquidity. Celebrate with...](https://twitter.com/WojaksX/status/2023547749149667620)
- [2026-02-17T00:00 @broadwaybabyto [热门] | The Dow is not the economy. The stock market is not the economy. When Bondi screamed about...](https://twitter.com/broadwaybabyto/status/2023498993721090308)
- [2026-02-17T00:00 @TheEconomist [关注] | An awful lot of the chatter about AI is about the final destination, artificial general in...](https://twitter.com/TheEconomist/status/2023548041551077598)
- [2026-02-17T00:00 @TheEconomist [关注] | The bloody history of fatherhood bends towards co-parenting https://www.economist.com/cult...](https://twitter.com/TheEconomist/status/2023548011423334503)
- [2026-02-16T23:58 @business [关注] | Trump pledges federal aid to stem a Potomac River sewage spill near Washington, blaming De...](https://twitter.com/business/status/2023547520882778148)
- [2026-02-16T23:55 @business [关注] | Gold was little changed, with many traders in Asia offline for the Lunar New Year and the ...](https://twitter.com/business/status/2023546690213474783)
- [2026-02-16T23:53 @NikkeiAsia [关注] | Japan's Mizuho Securities faces insider trading probe https://s.nikkei.com/4csGKXO](https://twitter.com/NikkeiAsia/status/2023546405038461305)
- [2026-02-16T23:52 @business [关注] | Here’s the latest news and analysis on the oil market https://www.bloomberg.com/news/artic...](https://twitter.com/business/status/2023546154584060047)
- [2026-02-16T23:47 @WSJ [关注] | BHP Group has opportunities to unlock more value from its portfolio of assets, but won’t p...](https://twitter.com/WSJ/status/2023544823886573604)
- [2026-02-16T23:46 @business [关注] | A judge dismissed a long-running legal challenge against Santos, which had accused the Aus...](https://twitter.com/business/status/2023544538682331293)
- [2026-02-16T23:40 @WSJ [关注] | The Oscar-winning actor, who died Sunday at age 95, memorably performed roles ranging from...](https://twitter.com/WSJ/status/2023543073444082030)
- [2026-02-16T23:40 @WSJ [关注] | Boy Throb is a new boy band going viral on social media. But member Darshan Magdum needs a...](https://twitter.com/WSJ/status/2023542994394034268)
- [2026-02-16T23:40 @TheEconomist [关注] | A viral reservation-trading website allows anyone who is willing to pay to get a seat at t...](https://twitter.com/TheEconomist/status/2023542958042100148)
- [2026-02-16T23:35 @NikkeiAsia [关注] | Japan's Sojitz to expand Australian rare earth imports https://s.nikkei.com/4cxjBDA](https://twitter.com/NikkeiAsia/status/2023541695040663957)
- [2026-02-16T23:20 @WSJ [关注] | How are points scored in curling? WSJ's Laine Higgins took a trip to Ardsley Curling Club ...](https://twitter.com/WSJ/status/2023537970024702312)
- [2026-02-16T23:20 @TheEconomist [关注] | Many people worry about overpopulation. But an increasing number, especially in rich count...](https://twitter.com/TheEconomist/status/2023537922511606189)
- [2026-02-16T23:19 @NikkeiAsia [关注] | Japan eases screening for US-made cars in boost for Toyota's reverse imports https://s.nik...](https://twitter.com/NikkeiAsia/status/2023537761316114456)
- [2026-02-16T23:05 @WSJ [关注] | Beretta is taking aim at one of its biggest American rivals, amassing a 10% stake in rifle...](https://twitter.com/WSJ/status/2023534221780783191)
- [2026-02-16T23:04 @NikkeiAsia [关注] | India needs action to manage AI threat to jobs, experts tell key summit https://s.nikkei.c...](https://twitter.com/NikkeiAsia/status/2023533939986444291)
- [2026-02-16T23:00 @TheEconomist [关注] | It seems conservative consumers would rather press mainstream brands to hew to their views...](https://twitter.com/TheEconomist/status/2023532948289359955)
- [2026-02-16T22:50 @WSJ [关注] | An AI bot wrote a blog post attacking an engineer because he had rejected lines of code th...](https://twitter.com/WSJ/status/2023530551940923525)
- [2026-02-16T22:45 @TheInformation [关注] | A University of Michigan team is adapting ultra-light carbon fluorine chemistry used in sp...](https://twitter.com/TheInformation/status/2023529074958688636)
- [2026-02-16T22:44 @NikkeiAsia [关注] | Anthropic opens first office in India as usage and revenue surge https://s.nikkei.com/4awl...](https://twitter.com/NikkeiAsia/status/2023528902593818681)
- [2026-02-16T22:42 @business [关注] | Get up to speed on what's moving global markets https://www.bloomberg.com/news/articles/20...](https://twitter.com/business/status/2023528392436466126)
- [2026-02-16T22:40 @WSJ [关注] | The Pima County sheriff said rumors that her children or their spouses were involved were ...](https://twitter.com/WSJ/status/2023528019155984497)
- [2026-02-16T22:40 @TheEconomist [关注] | Around the world, politicians are fixated on factories. But this obsession with factories ...](https://twitter.com/TheEconomist/status/2023527862330966351)
- [2026-02-16T22:38 @SCMPNews [关注] | Iran’s foreign minister in Geneva for second round of talks with US. https://www.scmp.com/...](https://twitter.com/SCMPNews/status/2023527499917844811)
- [2026-02-16T22:38 @WSJ [关注] | In remote southern Utah, Amangiri resort—a crown jewel in the Aman hospitality company’s p...](https://twitter.com/WSJ/status/2023527387716067417)
- [2026-02-16T22:20 @TheEconomist [关注] | Can anything truly replace the framework and buzz of being part of the action? Retirement ...](https://twitter.com/TheEconomist/status/2023522822476181605)
- [2026-02-16T22:18 @WSJ [关注] | Authorities said the shooting appeared to be the result of a family dispute. https://on.ws...](https://twitter.com/WSJ/status/2023522286326702532)
- [2026-02-16T22:16 @WSJ [关注] | Many of the victims in the hamlet of Tumbler Ridge, B.C., have links to Conuma Resources, ...](https://twitter.com/WSJ/status/2023521922428895389)
- [2026-02-16T22:03 @business [关注] | Russia has turned a record-breaking expansion of its national church into a formidable ass...](https://twitter.com/business/status/2023518574984229092)
- [2026-02-16T22:00 @TheEconomist [关注] | “They see themselves as pro-medical freedom, pro-parental choice,” says http://localhost/d...](https://twitter.com/TheEconomist/status/2023517851403882548)
- [2026-02-16T21:56 @business [关注] | BHP Group’s earnings for the six months to December rose by more than a fifth thanks to a ...](https://twitter.com/business/status/2023516979391316278)
- [2026-02-16T21:53 @elonmusk [关注] | If you’re in Korea and want to work on chip design, fabrication or AI software, join Tesla...](https://twitter.com/elonmusk/status/2023516129457758483)
- [2026-02-16T21:49 @SCMPNews [关注] | ‘Work to be done’: EU says it’s not ready to give Ukraine a membership date. https://www.s...](https://twitter.com/SCMPNews/status/2023515156135731643)
- [2026-02-16T21:45 @TheInformation [关注] | ServiceNow positions itself as the “middleman” connecting a company’s fragmented systems—e...](https://twitter.com/TheInformation/status/2023513981642539148)
- [2026-02-16T21:40 @TheEconomist [关注] | Tenor voices are like gold, and not only because they are rare and valuable. They need to ...](https://twitter.com/TheEconomist/status/2023512754397524304)
- [2026-02-16T21:39 @business [关注] | Read today's Australia Briefing for your daily dose of the best of Bloomberg from Down Und...](https://twitter.com/business/status/2023512471416238516)
- [2026-02-16T21:35 @business [关注] | Asia has taken a beating from climate change, but you'd never know it from the adaptation ...](https://twitter.com/business/status/2023511491144466597)
- [2026-02-16T21:34 @elonmusk [关注] | 🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷🇰🇷 Tesla Korea (@tesla_korea) [Tesla Korea 채용공고 - AI Chip De...](https://twitter.com/elonmusk/status/2023511421779354015)
- [2026-02-16T21:30 @business [关注] | Chile notched a second disappointing season of cherry sales in China after exporting too m...](https://twitter.com/business/status/2023510351220756731)
- [2026-02-16T21:29 @elonmusk [关注] | Model S & X are great cars! Order yours before we sunset the program in a few months. http...](https://twitter.com/elonmusk/status/2023510007577538718)
- [2026-02-16T21:23 @SCMPNews [关注] | http://localhost/SCMPNews Read more: https://sc.mp/80b722](https://twitter.com/SCMPNews/status/2023508547720364356)
- [2026-02-16T21:23 @SCMPNews [关注] | Anthropic wants to put safeguards in place to stop Claude from being used for mass surveil...](https://twitter.com/SCMPNews/status/2023508538882990328)
- [2026-02-16T21:20 @TheEconomist [关注] | China’s expats in Dubai can live much as they would at home. The city offers not just a sc...](https://twitter.com/TheEconomist/status/2023507719794115044)
- [2026-02-16T20:34 @SCMPNews [关注] | http://localhost/SCMPNews Read more: https://sc.mp/f67ab1](https://twitter.com/SCMPNews/status/2023496137513062875)
- [2026-02-16T20:34 @SCMPNews [关注] | The social club is “a cornerstone of the Harvard experience”, according to the organisatio...](https://twitter.com/SCMPNews/status/2023496128935629014)
- [2026-02-16T20:27 @elonmusk [关注] | Important read Gad Saad (@GadSaad) My inaugural X article is at 40,000 views. Not bad but ...](https://twitter.com/elonmusk/status/2023494489781006691)
- [2026-02-16T20:15 @TheInformation [关注] | For OpenAI, preventing leaks isn’t just about PR—it’s also about protecting intellectual p...](https://twitter.com/TheInformation/status/2023491329620087276)
- [2026-02-16T20:08 @NikkeiAsia [关注] | Democracy in doubt? Look to the Global South for hope https://s.nikkei.com/4kFwD44](https://twitter.com/NikkeiAsia/status/2023489795213635625)
- [2026-02-16T20:04 @SCMPNews [关注] | Hamas ‘used emojis’ to signal start of the October 7, 2023 attack on Israel. https://www.s...](https://twitter.com/SCMPNews/status/2023488615649603788)

### 📱 微信公众号原文 (0/0 条)

- 暂无可用链接

### 🔥 NewsNow 原文 (120/120 条)

- [知乎 #1 | 2026 年央视春晚中有哪些亮点？哪个节目最让你印象深刻？](https://www.zhihu.com/question/2006817906369979378)
- [今日头条 #1 | 春晚机器人中国功夫夯爆了](https://www.toutiao.com/trending/7607438781827366955/)
- [百度热搜 #1 | 总台马年春晚](https://www.baidu.com/s?wd=%E6%80%BB%E5%8F%B0%E9%A9%AC%E5%B9%B4%E6%98%A5%E6%99%9A)
- [抖音 #1 | 央视马年春晚](https://www.douyin.com/hot/2402899)
- [澎湃新闻 #1 | 今晚见！央视总台《2026年春节联欢晚会》节目单发布](https://www.thepaper.cn/newsDetail_forward_32620957)
- [财联社热门 #1 | 白银基金出台补偿方案！2月26日可办理，1000元以下损失全额补偿](https://www.cls.cn/detail/2290657)
- [华尔街见闻 #1 | AI热潮助力港股蛇年收官战告捷，MiniMax暴涨25%、智谱涨4.74%齐创新高，有色板块拉升](https://wallstreetcn.com/articles/3765773)
- [凤凰网 #1 | 日方提出交涉，中使馆：纯属狡辩、已予驳回](https://news.ifeng.com/c/8qnzjAl3cU5)
- [bilibili 热搜 #1 | 总台马年春晚完整版](https://search.bilibili.com/all?keyword=%E6%80%BB%E5%8F%B0%E9%A9%AC%E5%B9%B4%E6%98%A5%E6%99%9A%E5%AE%8C%E6%95%B4%E7%89%88)
- [微博 #1 | 春晚收视率](https://s.weibo.com/weibo?q=%E6%98%A5%E6%99%9A%E6%94%B6%E8%A7%86%E7%8E%87)
- [贴吧 #1 | 手滑删存档,亚瑟真人谢罪](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%89%8B%E6%BB%91%E5%88%A0%E5%AD%98%E6%A1%A3%2C%E4%BA%9A%E7%91%9F%E7%9C%9F%E4%BA%BA%E8%B0%A2%E7%BD%AA&topic_id=28350747)
- [凤凰网 #2 | 2026慕安会闭幕，欧洲开始有一个新变化](https://news.ifeng.com/c/8qnD3B7dZfA)
- [百度热搜 #2 | 王菲一开口时间都慢了](https://www.baidu.com/s?wd=%E7%8E%8B%E8%8F%B2%E4%B8%80%E5%BC%80%E5%8F%A3%E6%97%B6%E9%97%B4%E9%83%BD%E6%85%A2%E4%BA%86)
- [知乎 #2 | 如何评价宇树科技机器人在 2026 年春晚的武术表演《武 BOT》？与去年的《秧 BOT》相比有哪些进步？](https://www.zhihu.com/question/2006826244814104012)
- [bilibili 热搜 #2 | 凤凰传奇广场舞神曲上新](https://search.bilibili.com/all?keyword=%E5%87%A4%E5%87%B0%E4%BC%A0%E5%A5%87%E5%B9%BF%E5%9C%BA%E8%88%9E%E7%A5%9E%E6%9B%B2%E4%B8%8A%E6%96%B0)
- [财联社热门 #2 | 盘点春晚合作公司名单，覆盖智能出行、人工智能机器人、白酒等领域](https://www.cls.cn/detail/2290769)
- [华尔街见闻 #2 | AI圈内人士：巨大变革正在发生，人们还懵懂不知](https://wallstreetcn.com/articles/3765774)
- [澎湃新闻 #2 | 阿里除夕开源千问3.5：性能媲美Gemini 3 Pro， 实现原生多模态模型代际跃迁](https://www.thepaper.cn/newsDetail_forward_32621821)
- [今日头条 #2 | 谷爱凌自由式滑雪女子大跳台摘银](https://www.toutiao.com/trending/7607051298696908330/)
- [微博 #2 | 谷爱凌大跳台银牌](https://s.weibo.com/weibo?q=%E8%B0%B7%E7%88%B1%E5%87%8C%E5%A4%A7%E8%B7%B3%E5%8F%B0%E9%93%B6%E7%89%8C)
- [抖音 #2 | 大国重器硬核拜年](https://www.douyin.com/hot/2402837)
- [贴吧 #2 | C妈怒砍2分,百貌哈桑封神](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=C%E5%A6%88%E6%80%92%E7%A0%8D2%E5%88%86%2C%E7%99%BE%E8%B2%8C%E5%93%88%E6%A1%91%E5%B0%81%E7%A5%9E&topic_id=28350748)
- [华尔街见闻 #3 | 达利欧万字长文：旧秩序已死，世界重回“丛林法则”，贸易战和资本战将成常态](https://wallstreetcn.com/articles/3765762)
- [澎湃新闻 #3 | 中青评论：过年点外卖，是在给骑手添麻烦吗](https://www.thepaper.cn/newsDetail_forward_32620979)
- [抖音 #3 | 快来看看神二十一的年夜饭有什么](https://www.douyin.com/hot/2403348)
- [微博 #3 | 春晚分会场上大分](https://s.weibo.com/weibo?q=%23%E6%98%A5%E6%99%9A%E5%88%86%E4%BC%9A%E5%9C%BA%E4%B8%8A%E5%A4%A7%E5%88%86%23)
- [bilibili 热搜 #3 | 2026拜年纪全程回顾](https://search.bilibili.com/all?keyword=2026%E6%8B%9C%E5%B9%B4%E7%BA%AA%E5%85%A8%E7%A8%8B%E5%9B%9E%E9%A1%BE)
- [百度热搜 #3 | 来自天宫的新春问候请查收](https://www.baidu.com/s?wd=%E6%9D%A5%E8%87%AA%E5%A4%A9%E5%AE%AB%E7%9A%84%E6%96%B0%E6%98%A5%E9%97%AE%E5%80%99%E8%AF%B7%E6%9F%A5%E6%94%B6)
- [今日头条 #3 | 骏马迎春焕新潮](https://www.toutiao.com/trending/7606669748105170451/)
- [凤凰网 #3 | 荷兰国防官员：F-35战机或可像iPhone手机一样“越狱”](https://news.ifeng.com/c/8qnEVl9tHXs)
- [知乎 #3 | 如何评价 2026 年春晚王菲表演的歌曲《你我经历的一刻》？](https://www.zhihu.com/question/2006854372475232588)
- [贴吧 #3 | 软饭男喊冤,贴吧判官怒了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%BD%AF%E9%A5%AD%E7%94%B7%E5%96%8A%E5%86%A4%2C%E8%B4%B4%E5%90%A7%E5%88%A4%E5%AE%98%E6%80%92%E4%BA%86&topic_id=28350741)
- [财联社热门 #3 | 马年春晚黑科技！四家机器人同台献技 AI大模型渗透内容制作](https://www.cls.cn/detail/2290959)
- [财联社热门 #4 | AI遇上最强春节档 Token通胀已成必然？](https://www.cls.cn/detail/2290600)
- [bilibili 热搜 #4 | 蔡明30年后成真机器人](https://search.bilibili.com/all?keyword=%E8%94%A1%E6%98%8E30%E5%B9%B4%E5%90%8E%E6%88%90%E7%9C%9F%E6%9C%BA%E5%99%A8%E4%BA%BA)
- [华尔街见闻 #4 | 阿里发布千问3.5，性能媲美Gemini 3， Token价格仅为其1/18](https://wallstreetcn.com/articles/3765786)
- [澎湃新闻 #4 | 内塔尼亚胡：以色列计划10年内停止接受美国资金援助](https://www.thepaper.cn/newsDetail_forward_32620966)
- [贴吧 #4 | 留学新思路:打包教授带回国](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%95%99%E5%AD%A6%E6%96%B0%E6%80%9D%E8%B7%AF%3A%E6%89%93%E5%8C%85%E6%95%99%E6%8E%88%E5%B8%A6%E5%9B%9E%E5%9B%BD&topic_id=28350742)
- [百度热搜 #4 | 尼格买提终于和大家一样了](https://www.baidu.com/s?wd=%E5%B0%BC%E6%A0%BC%E4%B9%B0%E6%8F%90%E7%BB%88%E4%BA%8E%E5%92%8C%E5%A4%A7%E5%AE%B6%E4%B8%80%E6%A0%B7%E4%BA%86)
- [微博 #4 | 沈腾 说错词](https://s.weibo.com/weibo?q=%E6%B2%88%E8%85%BE+%E8%AF%B4%E9%94%99%E8%AF%8D)
- [凤凰网 #4 | 学者：美伊这轮谈判的逻辑变了，风险陡增](https://news.ifeng.com/c/8qnxRMK23SB)
- [抖音 #4 | 又是一年难忘今宵](https://www.douyin.com/hot/2403466)
- [知乎 #4 | 如何评价沈腾、马丽、银河通用机器人等 2026 年春晚上表演的贺岁微电影《我最难忘的今宵》？](https://www.zhihu.com/question/2006865473459942662)
- [贴吧 #5 | 26年春晚:到位or不到味](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=26%E5%B9%B4%E6%98%A5%E6%99%9A%3A%E5%88%B0%E4%BD%8Dor%E4%B8%8D%E5%88%B0%E5%91%B3&topic_id=28350743)
- [财联社热门 #5 | 今年春晚，机器人刷屏了](https://www.cls.cn/detail/2290956)
- [微博 #5 | 春晚](https://s.weibo.com/weibo?q=%E6%98%A5%E6%99%9A)
- [华尔街见闻 #5 | OpenClaw创始人加入OpenAI，目标“开发一款连我妈妈都能用的AI助手”](https://wallstreetcn.com/articles/3765772)
- [知乎 #5 | 2026 春节档总票房含预售突破 6 亿，《飞驰人生 3》预售破 2 亿，今年春节档是否格局已定？](https://www.zhihu.com/question/2006732300956694383)
- [bilibili 热搜 #5 | 沈马组合春晚短剧来了](https://search.bilibili.com/all?keyword=%E6%B2%88%E9%A9%AC%E7%BB%84%E5%90%88%E6%98%A5%E6%99%9A%E7%9F%AD%E5%89%A7%E6%9D%A5%E4%BA%86)
- [百度热搜 #5 | 30年后春晚真有蔡明同款机器人了](https://www.baidu.com/s?wd=30%E5%B9%B4%E5%90%8E%E6%98%A5%E6%99%9A%E7%9C%9F%E6%9C%89%E8%94%A1%E6%98%8E%E5%90%8C%E6%AC%BE%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%BA%86)
- [今日头条 #5 | 从秧BOT到武BOT 机器人发展有多快](https://www.toutiao.com/trending/7607451566442184758/)
- [抖音 #5 | 谷爱凌大跳台摘银](https://www.douyin.com/hot/2402478)
- [凤凰网 #5 | 爱泼斯坦案“政治敏感人物”名单公布](https://news.ifeng.com/c/8qnNgCTDt2B)
- [澎湃新闻 #5 | 放马过来，“申”情款待丨年味马不停蹄，抢“鲜”一步](https://www.thepaper.cn/newsDetail_forward_32543760)
- [贴吧 #6 | 太夯!宇树机器人三刷春晚](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%A4%AA%E5%A4%AF%21%E5%AE%87%E6%A0%91%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%B8%89%E5%88%B7%E6%98%A5%E6%99%9A&topic_id=28350744)
- [抖音 #6 | 机器人中国功夫夯爆了](https://www.douyin.com/hot/2403259)
- [财联社热门 #6 | 除夕不看春晚开电话会，这些券商太拼了！春节期间电话会近300场](https://www.cls.cn/detail/2290646)
- [知乎 #6 | 2026 央视春晚无相声节目，怎样看待这一变化？相声这种艺术形式真的过时了吗？](https://www.zhihu.com/question/2006741289241113569)
- [澎湃新闻 #6 | 中国学者慕安会驳斥所谓“中国威胁”：臆测！中国始终在合作](https://www.thepaper.cn/newsDetail_forward_32620360)
- [凤凰网 #6 | 英防卫大臣：俄军伤亡惨重，1.7万朝军在俄作战](https://news.ifeng.com/c/8qn6JNCebd2)
- [华尔街见闻 #6 | 华尔街见闻早餐FM-Radio | 2026年2月16日](https://wallstreetcn.com/articles/3765727)
- [今日头条 #6 | 秦岚李沁王楚然美成啥了](https://www.toutiao.com/trending/7606869652907576838/)
- [百度热搜 #6 | 谷爱凌自由式滑雪女子大跳台夺银](https://www.baidu.com/s?wd=%E8%B0%B7%E7%88%B1%E5%87%8C%E8%87%AA%E7%94%B1%E5%BC%8F%E6%BB%91%E9%9B%AA%E5%A5%B3%E5%AD%90%E5%A4%A7%E8%B7%B3%E5%8F%B0%E5%A4%BA%E9%93%B6)
- [微博 #6 | 谷爱凌创造自由式滑雪奖牌纪录](https://s.weibo.com/weibo?q=%23%E8%B0%B7%E7%88%B1%E5%87%8C%E5%88%9B%E9%80%A0%E8%87%AA%E7%94%B1%E5%BC%8F%E6%BB%91%E9%9B%AA%E5%A5%96%E7%89%8C%E7%BA%AA%E5%BD%95%23)
- [微博 #7 | 马丽单飞了 沈腾怎么办](https://s.weibo.com/weibo?q=%E9%A9%AC%E4%B8%BD%E5%8D%95%E9%A3%9E%E4%BA%86+%E6%B2%88%E8%85%BE%E6%80%8E%E4%B9%88%E5%8A%9E)
- [今日头条 #7 | 拼手气红包怎么抢最大](https://www.toutiao.com/trending/7606273692196408895/)
- [财联社热门 #7 | 习近平：当前经济工作的重点任务](https://www.cls.cn/detail/2290573)
- [bilibili 热搜 #7 | 大学生春晚压中春晚魔术题](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%94%9F%E6%98%A5%E6%99%9A%E5%8E%8B%E4%B8%AD%E6%98%A5%E6%99%9A%E9%AD%94%E6%9C%AF%E9%A2%98)
- [华尔街见闻 #7 | 存储芯片，走向失控](https://wallstreetcn.com/articles/3765777)
- [凤凰网 #7 | 希拉里与捷克副总理，当众“吵起来了”](https://news.ifeng.com/c/8qn7o7BaUvS)
- [贴吧 #7 | Steam擦边,恭喜发财变发春](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=Steam%E6%93%A6%E8%BE%B9%2C%E6%81%AD%E5%96%9C%E5%8F%91%E8%B4%A2%E5%8F%98%E5%8F%91%E6%98%A5&topic_id=28350738)
- [澎湃新闻 #7 | 驻日本使馆发言人就日方所谓交涉答记者问](https://www.thepaper.cn/newsDetail_forward_32622456)
- [抖音 #7 | 春晚机器人齐聚抖音](https://www.douyin.com/hot/2403438)
- [知乎 #7 | 电视剧《大明王朝》里，司礼监大太监们夜宵就是吃碗面条，是不是太寒酸了点，真实吗？](https://www.zhihu.com/question/2006058834934916188)
- [百度热搜 #7 | 初一迎春接福 马年跃马呈祥](https://www.baidu.com/s?wd=%E5%88%9D%E4%B8%80%E8%BF%8E%E6%98%A5%E6%8E%A5%E7%A6%8F+%E9%A9%AC%E5%B9%B4%E8%B7%83%E9%A9%AC%E5%91%88%E7%A5%A5)
- [今日头条 #8 | 春晚再出金句](https://www.toutiao.com/trending/7607078259876003876/)
- [财联社热门 #8 | AI电荒把燃气轮机“捧上C位” 龙头企业：需求极其旺盛 交付排到2030年](https://www.cls.cn/detail/2290580)
- [贴吧 #8 | 闺蜜创业内斗,7人8群吵翻天](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%97%BA%E8%9C%9C%E5%88%9B%E4%B8%9A%E5%86%85%E6%96%97%2C7%E4%BA%BA8%E7%BE%A4%E5%90%B5%E7%BF%BB%E5%A4%A9&topic_id=28350737)
- [抖音 #8 | 刘少昂林孝埈晋级1/4决赛](https://www.douyin.com/hot/2402760)
- [微博 #8 | 短剧上春晚了](https://s.weibo.com/weibo?q=%E7%9F%AD%E5%89%A7%E4%B8%8A%E6%98%A5%E6%99%9A%E4%BA%86)
- [知乎 #8 | 很多年轻人明知去大城市没前途，为什么还要去？](https://www.zhihu.com/question/457100446)
- [凤凰网 #8 | 克宫：这次谈判将讨论领土问题](https://news.ifeng.com/c/8qnNYAZwwTm)
- [百度热搜 #8 | 凤凰传奇一开口就是国泰民安](https://www.baidu.com/s?wd=%E5%87%A4%E5%87%B0%E4%BC%A0%E5%A5%87%E4%B8%80%E5%BC%80%E5%8F%A3%E5%B0%B1%E6%98%AF%E5%9B%BD%E6%B3%B0%E6%B0%91%E5%AE%89)
- [澎湃新闻 #8 | 爱我中华·千里江山图丨灵蛇起舞辞旧岁，骏马昂首迎新春](https://www.thepaper.cn/newsDetail_forward_25061346)
- [华尔街见闻 #8 | 木头姐：这轮市场波动是算法导致，而非基本面](https://wallstreetcn.com/articles/3765784)
- [bilibili 热搜 #8 | 和留守儿童一起过新年](https://search.bilibili.com/all?keyword=%E5%92%8C%E7%95%99%E5%AE%88%E5%84%BF%E7%AB%A5%E4%B8%80%E8%B5%B7%E8%BF%87%E6%96%B0%E5%B9%B4)
- [澎湃新闻 #9 | 希拉里回应爱泼斯坦案：可怕，但名字出现在文件中不意味犯罪](https://www.thepaper.cn/newsDetail_forward_32621182)
- [凤凰网 #9 | 除夕玩“开运转盘”，张善政连线马英九、蒋万安等人](https://news.ifeng.com/c/8qnbuZ7y4z4)
- [华尔街见闻 #9 | 新春伊始，如何看待人民币升值？](https://wallstreetcn.com/articles/3765776)
- [贴吧 #9 | 罗翔悟了:人不该有偶像](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%BD%97%E7%BF%94%E6%82%9F%E4%BA%86%3A%E4%BA%BA%E4%B8%8D%E8%AF%A5%E6%9C%89%E5%81%B6%E5%83%8F&topic_id=28350736)
- [财联社热门 #9 | 告别“码农”时代？马斯克预言“就在年底”，国产大模型春节竞速AI编程](https://www.cls.cn/detail/2290650)
- [抖音 #9 | 今年的春节祝福这样说](https://www.douyin.com/hot/2401854)
- [知乎 #9 | 「年夜饭摄影大赛」又开始了，可以看看你的参赛作品吗？](https://www.zhihu.com/question/2005635243948917798)
- [bilibili 热搜 #9 | 难忘今宵再次唱响春晚](https://search.bilibili.com/all?keyword=%E9%9A%BE%E5%BF%98%E4%BB%8A%E5%AE%B5%E5%86%8D%E6%AC%A1%E5%94%B1%E5%93%8D%E6%98%A5%E6%99%9A)
- [今日头条 #9 | 你如何看待过年群发祝福](https://www.toutiao.com/trending/7607284935024181298/)
- [微博 #9 | 过年好](https://s.weibo.com/weibo?q=%E8%BF%87%E5%B9%B4%E5%A5%BD)
- [贴吧 #10 | 今晚见!央视春晚节目单公开](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BB%8A%E6%99%9A%E8%A7%81%21%E5%A4%AE%E8%A7%86%E6%98%A5%E6%99%9A%E8%8A%82%E7%9B%AE%E5%8D%95%E5%85%AC%E5%BC%80&topic_id=28350740)
- [今日头条 #10 | 冬奥最强教练执教13国 现场飞速换队服](https://www.toutiao.com/trending/7607307736673455626/)
- [华尔街见闻 #10 | 行业首例！国投白银LOF估值调整补偿方案出炉：1000元以下损失全额补偿](https://wallstreetcn.com/articles/3765768)
- [凤凰网 #10 | 高市早苗，迎来坏消息](https://news.ifeng.com/c/8qnPmJKPPlq)
- [财联社热门 #10 | 保利集团发布严正声明](https://www.cls.cn/detail/2290639)
- [bilibili 热搜 #10 | 春晚机器人硬核诠释中国功夫](https://search.bilibili.com/all?keyword=%E6%98%A5%E6%99%9A%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%A1%AC%E6%A0%B8%E8%AF%A0%E9%87%8A%E4%B8%AD%E5%9B%BD%E5%8A%9F%E5%A4%AB)
- [抖音 #10 | 家庭春节联欢晚会](https://www.douyin.com/hot/2402742)
- [微博 #10 | 大年初一](https://s.weibo.com/weibo?q=%E5%A4%A7%E5%B9%B4%E5%88%9D%E4%B8%80)
- [澎湃新闻 #10 | 这个春节，人形机器人正在实现“能演亦能干”](https://www.thepaper.cn/newsDetail_forward_32618240)
- [知乎 #10 | Seedance 2.0 分镜运镜做的这么好，未来导演会不会逐渐失业？](https://www.zhihu.com/question/2004599527957557412)
- [微博 #11 | 谁给迪丽热巴化的妆](https://s.weibo.com/weibo?q=%E8%B0%81%E7%BB%99%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4%E5%8C%96%E7%9A%84%E5%A6%86)
- [贴吧 #11 | 闯岛救人?MJ魔窟救孩童](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%97%AF%E5%B2%9B%E6%95%91%E4%BA%BA%3FMJ%E9%AD%94%E7%AA%9F%E6%95%91%E5%AD%A9%E7%AB%A5&topic_id=28350732)
- [今日头条 #11 | 菲律宾总统：欢迎中国的决定](https://www.toutiao.com/trending/7606306238615453702/)
- [凤凰网 #11 | 赖清德当局春节当“老赖”！持续拖欠“军公教警消”工资福利](https://news.ifeng.com/c/8qjruhyBJ3z)
- [百度热搜 #11 | 炖肉时的浮沫是营养精华？假的](https://www.baidu.com/s?wd=%E7%82%96%E8%82%89%E6%97%B6%E7%9A%84%E6%B5%AE%E6%B2%AB%E6%98%AF%E8%90%A5%E5%85%BB%E7%B2%BE%E5%8D%8E%EF%BC%9F%E5%81%87%E7%9A%84)
- [财联社热门 #11 | 奥巴马称外星人确实存在](https://www.cls.cn/detail/2290699)
- [澎湃新闻 #11 | 美伊第二轮开谈前，内塔尼亚胡提条件、特朗普放狠话](https://www.thepaper.cn/newsDetail_forward_32621372)
- [知乎 #11 | 洛天依新歌被曝抄袭薛之谦，发行方已开除相关人员，虚拟歌手的作品为什么会涉及抄袭？和普通明星有不同吗？](https://www.zhihu.com/question/2005228516074020928)
- [bilibili 热搜 #11 | 拜年神曲的全新打开方式](https://search.bilibili.com/all?keyword=%E6%8B%9C%E5%B9%B4%E7%A5%9E%E6%9B%B2%E7%9A%84%E5%85%A8%E6%96%B0%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F)
- [抖音 #11 | 总算等到沈腾马丽了](https://www.douyin.com/hot/2403443)
- [bilibili 热搜 #12 | 春晚致敬各行各业发光的你](https://search.bilibili.com/all?keyword=%E6%98%A5%E6%99%9A%E8%87%B4%E6%95%AC%E5%90%84%E8%A1%8C%E5%90%84%E4%B8%9A%E5%8F%91%E5%85%89%E7%9A%84%E4%BD%A0)
- [澎湃新闻 #12 | 文化为根，马年新象，央视春晚马上开席](https://www.thepaper.cn/newsDetail_forward_32620358)
- [贴吧 #12 | 负债小白梭哈白银遭胖揍](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%B4%9F%E5%80%BA%E5%B0%8F%E7%99%BD%E6%A2%AD%E5%93%88%E7%99%BD%E9%93%B6%E9%81%AD%E8%83%96%E6%8F%8D&topic_id=28350731)
- [财联社热门 #12 | 外交部：对加拿大、英国持普通护照人员实施免签政策](https://www.cls.cn/detail/2290624)

### 💻 GitHub 原文 (20/40 条)

- [openclaw/openclaw | ⭐ 201537 | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/openclaw/openclaw)
- [Significant-Gravitas/AutoGPT | ⭐ 181836 | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission i...](https://github.com/Significant-Gravitas/AutoGPT)
- [n8n-io/n8n | ⭐ 174812 | Fair-code workflow automation platform with native AI capabilities. Combine visual buildin...](https://github.com/n8n-io/n8n)
- [ollama/ollama | ⭐ 162711 | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and othe...](https://github.com/ollama/ollama)
- [huggingface/transformers | ⭐ 156552 | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning model...](https://github.com/huggingface/transformers)
- [f/prompts.chat | ⭐ 145340 | a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. F...](https://github.com/f/prompts.chat)
- [langflow-ai/langflow | ⭐ 144834 | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.](https://github.com/langflow-ai/langflow)
- [langgenius/dify | ⭐ 129696 | Production-ready platform for agentic workflow development.](https://github.com/langgenius/dify)
- [langchain-ai/langchain | ⭐ 126761 | 🦜🔗 The platform for reliable agents.](https://github.com/langchain-ai/langchain)
- [nautechsystems/nautilus_trader | ⭐ 19761 | A high-performance algorithmic trading platform and event-driven backtester](https://github.com/nautechsystems/nautilus_trader)
- [SimplifyJobs/New-Grad-Positions | ⭐ 16284 | A collection of full time roles in SWE, Quant, and PM for new grads.](https://github.com/SimplifyJobs/New-Grad-Positions)
- [tensorflow/tensorflow | ⭐ 193740 | An Open Source Machine Learning Framework for Everyone](https://github.com/tensorflow/tensorflow)
- [zeroclaw-labs/zeroclaw | ⭐ 7055 | Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anyt...](https://github.com/zeroclaw-labs/zeroclaw)
- [flowglad/flowglad | ⭐ 1684 | Open source, zero webhooks payment provider](https://github.com/flowglad/flowglad)
- [ethereum-optimism/optimism | ⭐ 6376 | Optimism is Ethereum, scaled.](https://github.com/ethereum-optimism/optimism)
- [paradigmxyz/reth | ⭐ 5410 | Modular, contributor-friendly and blazing-fast implementation of the Ethereum protocol, in...](https://github.com/paradigmxyz/reth)
- [bennycode/trading-signals | ⭐ 877 | Technical indicators to run technical analysis with JavaScript & TypeScript. 📈](https://github.com/bennycode/trading-signals)
- [bwya77/vscode-dark-islands | ⭐ 2310 | VSCode theme based off the easemate IDE and Jetbrains islands theme](https://github.com/bwya77/vscode-dark-islands)
- [ebrasha/free-v2ray-public-list | ⭐ 515 | A simple and always-updated list of free, working V2Ray servers. including SS, SSR, Trojan...](https://github.com/ebrasha/free-v2ray-public-list)
- [RevylAI/greenlight | ⭐ 1028 | Pre-submission compliance scanner for the Apple App Store](https://github.com/RevylAI/greenlight)

### 🌍 Yahoo Finance 原文 (12/12 条)

- [美股 | 标普500 (^GSPC) | +0.05%](https://finance.yahoo.com/quote/%5EGSPC)
- [美股 | 纳斯达克综合 (^IXIC) | -0.22%](https://finance.yahoo.com/quote/%5EIXIC)
- [美股 | 道琼斯工业指数 (^DJI) | +0.10%](https://finance.yahoo.com/quote/%5EDJI)
- [美股 | 罗素2000 (^RUT) | +1.18%](https://finance.yahoo.com/quote/%5ERUT)
- [美股 | VIX波动率指数 (^VIX) | +2.91%](https://finance.yahoo.com/quote/%5EVIX)
- [港股 | 恒生指数 (^HSI) | +0.52%](https://finance.yahoo.com/quote/%5EHSI)
- [日股 | 日经225 (^N225) | -0.24%](https://finance.yahoo.com/quote/%5EN225)
- [韩股 | 韩国综合指数 (^KS11) | -0.28%](https://finance.yahoo.com/quote/%5EKS11)
- [欧股 | 英国富时100 (^FTSE) | +0.26%](https://finance.yahoo.com/quote/%5EFTSE)
- [欧股 | 德国DAX (^GDAXI) | -0.46%](https://finance.yahoo.com/quote/%5EGDAXI)
- [欧股 | 法国CAC40 (^FCHI) | +0.06%](https://finance.yahoo.com/quote/%5EFCHI)
- [A股 | 上证综指 (000001.SS) | -1.26%](https://finance.yahoo.com/quote/000001.SS)

### 🌐 联网检索原文 (19/19 条)

- [2026-02-17 07:54 thepaper.cn | 城市年鉴2025｜科技产业：“速度”和 “泡沫”中找平衡 - thepaper.cn](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1FN1pzQUhiTlRHQVJBajFLOFBkc0FCbnpOeXBiTThLNXFFY29Zb3ZkZEtfMl82UTNzMWV0dV83alpwUWlFcWJvYjVtNkpQcDRyalp4RWhxWG9KRTYtNHc?oc=5)
- [2026-02-17 07:46 thepaper.cn | 首席展望｜中欧基金任飞：周期板块将迎量价共振，看好有色、新能源及化工 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1wdlNqdllSZTB6NUVwMEtUQnM1R1gyOVlodzF6cDNCcTEzRzlkLW5tZEhiODI0UW5SZHJHS0c1NWF1QkxvWXUzMFlXOW5jenZ1V3RpWWxHenFpZ1JTQmVVTg?oc=5)
- [2026-02-17 07:35 新浪财经 | 新浪财经隔夜要闻大事汇总：2026年2月17日|债券市场|金融市场|原油期货|宇树科技|惊蛰无声_手机新浪网 - 新浪财经](https://news.google.com/rss/articles/CBMijgJBVV95cUxPSmczWGVmS3U1YThtMExmdlFPaVgwNkcxT3BFZjd5dFZ5MWhKM1hBY1IxdVg4QjR5MmNPVmVjWXhldUhkMlU2S2RLLVlwcXRjaF9zME5VMmJmMUdFWDdLVFZzSk1wbkQzT3V6M0htdWh3OUhiYi03NC11MjcxUEp0UEFEenR6N1h2QXZ2cTgxQTloWG9Zb2xTM2JsV0hBUlZVVVRrYWlqcE9oQVJ6dHZLdURjdUo0TGxIQmtvekZJMVFmSTAtWmd1RU1fYUpRaDFrVHZUemp5TGZXVktvYkl3VGJmUHFGSFVtYkw3a2VEblVVSzE0ZGR1Umw0bVoxNlFwMGFsaV9faWh4VmczbVE?oc=5)
- [2026-02-17 07:01 新浪财经 | 2026新年献词|景顺长城基金总经理康乐：主动有为，静待春来 - 新浪财经](https://news.google.com/rss/articles/CBMiigJBVV95cUxQdENIeW1LUzV2WjZhX2FEVnpSTEJyeDFhajFDTVhqT0lDMUZQeDV5aTJwSFBUZzk0aHhNQXF0NmN1WXhrcUxQYXZBX1FXUkF1RFR4VGZ1NXFSWHdkM1pHRzNxSGZPX1AyU3IyOWZ6akFJNDg3R2gxUEM4SDZVM1JGTGU5eXE2S21lUHJNT2stU1pZakJKaWNFTzZTT0hhOEtaTmkxQWlDSEFLTkxlMm9ndTR4b0JBZ2pkTWt1b21yU0I3dWw4TVFHaWt6cnI5MWMxYkx0M0Vmb2FiSEFFUmRFODBMTjRBQTVlUGRfTUN2U3Z0ejlkU1ZWTm0zcXBrSHVDUVZNTEZpdW1VQQ?oc=5)
- [2026-02-17 01:05 英为财情 Investing.com | 法国股市上涨；截至收盘法国CAC40指数上涨0.06% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9NSm1hMzlXN2hoQmVrOTJ5dXRsWU9YUklIS25NN19xTno0MzBrWDBuM0stYVBEMnBRbkxzODVoWGlQWE1IdVVZWGJsQnkxMjNWY2plVlJXSlhueDVJNUNqbWhyaVN2SXdkZGw5eURYZ2Q?oc=5)
- [2026-02-17 00:51 新浪财经 | 骐骥驰骋 势不可挡 总台马年春晚精彩上演 - 新浪财经](https://news.google.com/rss/articles/CBMiiAJBVV95cUxPMFBUSUVpOVdBTGRhdXQyMUFQaUNRTUJlaUdtVHFrUmdwX2dTellONzI0d3VQeS1FQTVlMzVZZXNVdURPUGZPS3R5Rk5scGlvVjRWQ00zU1VSbWVlajJYV3RXUFJSQjRLVlhUeGJHUVpHM3BPNFVrel9iSDhaOThGMUpZM3VKekNabWJ6eWlFYXJuMGduVms0Y2c2aHJQMkxZMDV1NVFqZGRacXlkQWJjY3RYcHBFV3pMSVJMMnpXQVBvcm0tZXdyT0tTQWtBSWQ5cDd6UDJYNVhpX3NEaTgwTkd3VzlJUThtVlFQR0xsbXY5QW8yQTBET3hUNFM4VzNyZUMyRjBndEs?oc=5)
- [2026-02-17 00:34 SOHU | 华米科技：AI眼镜量产、业绩指引与股价波动引关注 - SOHU](https://news.google.com/rss/articles/CBMihwFBVV95cUxQNnBkMnZsZlMyRzU0LUdPODFPLVB4ZjlXTWptUVBHMHpYdVRTSFg2dHMzQ19LWjY0NlRCU0I2UGUwcFZURmhBWUg4TXZXUU1wckctc2JKUmVLcjRLMmxjbDhCcHNKcEhNeEVCMWY0XzhteEJORWJrcVJNRlowVkl0TkluV0YtSTA?oc=5)
- [2026-02-16 20:01 中华网 | 总台马年春晚 看点满满迎新春 - 中华网](https://news.google.com/rss/articles/CBMicEFVX3lxTFBmdktjcWV1MnBvUnlGQW1uWTlxS2w3UUZOSl9qNkk0cHVxLTRiNjR0WHFyZDNpSkdJam9ka1FGakJyUU1JTjJxMjNvaXRlNUZubGRDUWZEemgtYU9XM0pBdlp1YVJ4bWhYZ1ZadWJYNk0?oc=5)
- [2026-02-16 20:00 央视网 | 欢乐吉祥 喜气洋洋 总台《2026年春节联欢晚会》等着您 - 央视网](https://news.google.com/rss/articles/CBMid0FVX3lxTE5Xa25JdVc1SVROOW8wcmhRVDJNLTJub3RzWWMxakUxTVBBaGhlQ3BTYkEyTWFpUXAxWTJ5UWRRUlBwQUZlZnRCZjYzUmZ1ZmhUYjBnREg1Y2RucUUyMVNHUmF2LU1vY2RYSkVWeHN0NmVTdWtPcnFJ?oc=5)
- [2026-02-16 16:49 yeeyi | 重磅喜讯！中国官宣免签扩大！贸易谈判推进！从机票到车价都可能被改写！两大政策进展背后，普通人最该关注的现实影响全解读...-yeeyi - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBREdBeGNHbld6ZXhtUmZJQ1FnZ1lleWRBbld0eTlDWm11UkdUZmMzTk43UkFReEVDd3lqYXM3RE9wQ2QtVTNPbG5POGpZWjZvcHJ6RDRR?oc=5)
- [2026-02-16 15:04 Traders Union | Ethereum 下跌 5.71%，原因是 FinCEN 加大执法力度，看跌信号占主导地位 - Traders Union](https://news.google.com/rss/articles/CBMipgFBVV95cUxPdTVsdTFlanJBNnVHREVVOW9rRm9BQTZ0S1FJdFNGVDVCUEN0MEtqZTcxbjlMQ2ZiNVRoMDhUWUlzSGhDTTN4a0VnZFdpY1V4VjJFRlMtVVpaazkwRVNVandnRVlKYV9ySm9QQTF5UDIxbC1Sa09VbUpBbkY5eWRLOWFEcFNRaFJjMVNiY2E4OXU0NXNHekQ0N05yZ1dmY0FacEYwbHdR?oc=5)
- [2026-02-16 13:30 英为财情 Investing.com | 澳大利亚股市上涨；截至收盘澳大利亚S&P/ASX200指数上涨0.22% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTFBXTkxGWWlpT2VIRnhZRTFVUEtLUnZxQUNJRW1TMXVDZTBIWWdRbWItUUFOTHBuUHNEbTNYT0VxbmhWZ19ZQkhGMWpRVk9JTVNoZ3BMOUl2b0E5Zmh4blpZNjRaTnNEUkFhbFBSOER5M1U?oc=5)
- [2026-02-16 12:05 FX168财经 | 7张图表，说明为何美股的压力山大 - FX168财经](https://news.google.com/rss/articles/CBMia0FVX3lxTE01SHBRTzRiTkV0cXhuV1R2RFA3RzJfRndYUFkzUXlJSC1hVG1nVVViNGg4UE9VSWF0MzZHckpoNHdHLUVQeFp3eDJSNjZnWmp2NjZXeHhlU1dBV0ktd2JFcGRoUWtpaHJpbF9N?oc=5)
- [2026-02-16 07:58 每日经济新闻 | 江苏连云港一烟花零售店爆炸致8人遇难2人受伤，应急管理部紧急召开调度会；中方宣布对英、加免签；马斯克：Grok 4.20本周发布丨每经早参 - 每日经济新闻](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBiTmRySmt3a3MzOGdCWnVHR1BtSXZ3bklIb2Nvci1qTDN6Z0lCUXQ1Ty1IMnVTWmpXZlgzR0Rzc2swS2NlUWxDTFpFWlJvY2o0amZicnB4NlIzREZOQmpoY2tPREl4dw?oc=5)
- [2026-02-16 07:42 FX168财经 | 财经早餐：本周A股开启“春节休假”模式，DeepSeek V4或将发布，国投白银LOF出台补偿方案，超九成投资者将获全额补偿 - FX168财经](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBDSjM3X0pZLTZsTEZYYzBYNXc4ZDU4cUpJblZmZHRhNmk3bXdxVWpPeDFPR2txTWgzV2lZV1dpWTFFRFhMbUdkbVhkSkhGMHpXb2c?oc=5)
- [2026-02-16 06:31 封面新闻 | 此沙、李子柒、谭松韵、丁真！春晚宜宾分会场沉浸式解锁百项非遗 - 封面新闻](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBoU3FxVjlGYThQX3FSUDd6ZnFFYVlnQXZUYjZCaTJXSHdWUDloSTV3aHdrMEtWQjFFaThVTndoaG1oMWpZSUtCREh0aEpTQlNhdU9DeElLLTNvV05QWTQwYUNOTDUzZw?oc=5)
- [2026-02-15 20:25 雷科技 | 马年春晚科技秀终极前瞻：硬科技成新头牌，机器人再做「群演」 - 雷科技](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1ETXhzUEVuczZDSWkyV3RrQS1oZl9GclViVm4tS1hLVGJGR3ZCSVkyc3ZKYV9mRUhGc01KcGJJY3laajBhck53SFRYTUxEZw?oc=5)
- [2026-02-15 20:19 Binance | Pi Network 价格上涨50%的主要原因| Berserker_09发布于币安广场 - Binance](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1RTjU0bkpQdEdXeW5wTjZCUjJ2bTNraFhLT0Q4Mks5NlJrUTBFMDhWVGtocjkycDRlclNtelNRYzl6Q3k0T1RCRTdnNlpkQzNfVGlNbGNEeDRtc1RGNjgtQVR0Qkl5UFJt?oc=5)
- [2026-02-15 11:29 中央广播电视总台 | 准备就绪！总台马年春晚完成全部五次彩排 - 中央广播电视总台](https://news.google.com/rss/articles/CBMic0FVX3lxTE9KVzVydG5lVjdYcWh4Mkk5ZE9xOFYtMENDTmZSLXhVMWFrY3Nqd3p1R2U3WnFIZmN6VEZsdEJ6c3ZXa3AtNVhTS1IwcUdFZTdyRU5zWnBpU2hVQnoweXBZc3lZenRDTldzMDk1S2haNmdkTnc?oc=5)

---

*报告由 finradar 自动生成 | 2026-02-17 08:03:01（北京时间）*
