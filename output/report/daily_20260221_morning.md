# 📰 finradar 🌅 早报
**2026-02-21** | 🌅 早报 | 覆盖时段: 昨日20:00 → 今日08:00 | 市场状态: ⚠️ A股休市
生成时间: 2026-02-21 08:03（北京时间）

**⚠️ 注意：今日为周末，A股休市，部分市场数据可能缺失或未更新**

---

## 🚨 数据源健康提醒

1. 检测到微信登录异常：财联社: invalid session。请重新扫码登录 wechat-exporter。
2. 本次抓取公众号文章为 0 篇，账号搜索失败占比 100%，请检查登录态或服务状态。

处理建议：
1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。
2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。
3. 然后执行 `./scripts/local.sh report morning 20260221` 与 `./scripts/local.sh notion-push morning 20260221` 覆盖 Notion 页面。

# 🤖 AI 分析摘要

## 一、摘要
- **社会**：国内社会关注点集中于**冬奥夺金捷报**（王心迪男子空中技巧夺冠）[NW01, WB08]与**社会道德争议**（网传“初中生扶老人被索赔22万”事件发酵）[NW02, WB11]。海外中国公民安全事故（贝加尔湖沉车致7名中国游客遇难）[NW08]引发持续关注。
- **经济**：**全球贸易政策不确定性急剧升温**，核心矛盾为美国最高法院裁定特朗普时期关税违法[NW06, NW11]与特朗普本人宣布将对全球加征10%进口关税[NW09, WB06]之间的冲突，可能引发大规模税收退款与新的贸易摩擦。国内机构调研显示对**机器人、半导体、有色金属**等新质生产力方向关注度提升[NW13]。
- **市场**：隔夜美股全线收涨，道指涨0.47%[WB04, WB06]，市场情绪受**特朗普宣布新关税计划**提振[WB06]，但深层驱动逻辑存在矛盾。港股马年首日交易呈现**科技股内部分化**，恒科指跌超2%，但**AI大模型（智谱+43%）、存储、机器人概念股逆势大涨**[NW12]。韩国股市独立行情延续。
- **科技**：AI领域呈现**应用落地与风险并存**。积极信号包括：印度马哈拉施特拉邦宣布全领域AI赋能[¹](https://twitter.com/Dev_Fadnavis/status/2024746356016107729)、黄仁勋预告3月发布“世界前所未见”的新芯片。风险信号包括：AI深度伪造冒用创作者身份[²](https://twitter.com/newhurizons/status/2024621032422756747)、社交媒体出现诱导关注虚假AI/加密账号的新型欺诈[³](https://twitter.com/NikeiNikeiNiii/status/2024792881613897760)。

## 二、分板块汇报
### 2.1 市场概况（仅有效交易时段数据）
较上期：美股由跌转涨，市场关注点从地缘风险转向国内政策预期；港股开市呈现显著的结构性分化。

**发生了什么**：覆盖时段内（主要为2月20日美股交易时段），**美国三大股指全线收涨**，道琼斯工业平均指数上涨0.47%[WB04, WB06]。与此前一日因美伊紧张局势下跌形成对比[WB05, WB13]。**港股**在马年首个交易日（2月20日）表现分化，恒生科技指数下跌超2%，但**AI大模型、存储及机器人概念股逆势大涨**，例如智谱股价大涨近43%[NW12]。

**为什么会这样（证据强弱：中）**：
1.  **美股上涨驱动**：直接催化剂可能为**特朗普宣布将对全球加征10%进口关税**的消息[WB06]。此消息被部分市场参与者解读为有利于美国本土产业的保护主义政策，从而提振市场情绪。然而，这与美国最高法院裁定其过往关税违法的消息[NW06, NW11]形成矛盾，显示市场在短期选择了对政策预期的交易。**VIX波动率指数下跌5.64%**[市场数据分析]表明市场恐慌情绪缓解，为上涨提供了环境。
2.  **港股结构性行情**：下跌主要受科技权重股拖累，而逆势大涨的**AI、存储、机器人板块**则与国内机构节前集中调研方向[NW13]及全球AI产业叙事（如英伟达新芯片预告）形成共振，显示资金在泛科技板块内部进行高切低或聚焦细分景气赛道。

**下一步观察**：
1.  关注**特朗普新关税主张**与**最高法院裁定**之间的政策博弈进展，及其对全球贸易流、企业盈利预期的实质性影响。
2.  验证**港股AI、机器人等领涨板块**的持续性，观察其是否能够形成独立于整体科技股的强势主线。
3.  延续跟进**韩国股市独立行情**的驱动逻辑，本期输入未提供新增信息，需补充其领涨板块及资金数据。

### 2.2 微信公众号共识与弱信号
数据不足。本期输入未提供“微信公众号逐篇简介”或具体公众号文章内容，无法进行跨公众号共识提炼或弱信号识别。

### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）
较上期：新增关注到服务于Web3 DeFi及预测市场的自动化交易工具，反映了该领域专业化、工具化的发展趋势。

本期最值得关注的项目聚焦于**AI应用平民化**与**Web3金融自动化**两大方向。
1.  **AI智能体与工作流平台群（openclaw, AutoGPT, n8n, langflow, dify）**：这些高星项目共同指向降低AI应用门槛的趋势。`openclaw`（⭐214k）定位为个人AI助手，`n8n`（⭐175k）和`langflow`（⭐144k）等提供可视化/低代码的AI工作流构建能力。其**可落地价值**在于赋能企业和开发者快速集成、定制AI能力，实现业务流程自动化。**噪音风险**在于功能概念高度重叠，需甄别各项目的实际差异化优势与生产环境采用率。
2.  **Web3金融自动化工具（tradingstrategy-ai/trading-strategy, SeungMaeda/polymarket-copy-bot-ts）**：`trading-strategy`（⭐347）是针对去中心化交易所的量化框架，`polymarket-copy-bot-ts`（⭐852）是预测市场跟单机器人。**应用场景**明确，服务于快速增长的链上金融和预测市场，**可落地价值**体现在为这些新兴市场提供专业的策略开发和执行工具。**噪音风险**较高：后者严重依赖单一平台（Polymarket）生态，而预测市场本身波动大、监管不确定；前者作为框架，其实际策略有效性和资金容量未经大规模验证。

### 2.4 Twitter 海外信号（英文内容中文汇报）
较上期：政治经济叙事对立加剧，AI相关信号中新增明确的**安全风险警告**和**区域发展政策**。

1.  **美国政治经济叙事极端对立**：特朗普方面宣称其关税政策使股市创新高（道指破5万点）[⁴](https://twitter.com/WhiteHouse/status/2024926556880031987)；反对者则指责其破坏经济且多项承诺（如发放加密货币支票）未兑现[⁵](https://twitter.com/NotAvgLiberal/status/2024648812233363868)[⁶](https://twitter.com/MikeNellis/status/2024854541221433650)。同时有指控称民主党人“蓄意破坏”了经济增长[⁷](https://twitter.com/GuntherEagleman/status/2024856986441994564)。这些均为高度政治化的单方面宣称，证据强度**低**。
2.  **AI：深度伪造风险与区域赋能并举**：有创作者称遭AI冒用身份[²](https://twitter.com/newhurizons/status/2024621032422756747)。更值得警惕的是，用户警告一种名为“Twitter家庭互动圈”的欺诈趋势，会**强制用户关注虚假的AI和加密货币账户**，存在账户安全风险[³](https://twitter.com/NikeiNikeiNiii/status/2024792881613897760)。另一方面，**印度马哈拉施特拉邦宣布将在所有领域实现“AI赋能”**[¹](https://twitter.com/Dev_Fadnavis/status/2024746356016107729)，这是一个明确的区域产业政策信号。
3.  **英国经济积极信号**：英国影子财政大臣宣称通胀、利率、借贷下降，零售销售上升，英国是G7中增长最快的欧洲经济体[⁸](https://twitter.com/RachelReevesMP/status/2024779618587156555)。此为趋势性陈述，需后续数据验证。

### 2.5 国内新闻与政策脉络
较上期：新增**重大贸易政策变量**（美国关税争端），国内产业政策线索聚焦**制造业降碳**与**机构调研方向**。

1.  **外部重大政策变量冲击**：**美国最高法院裁定特朗普时期关税违法**，可能导致超1750亿美元税收退款[NW11]；与此同时，**特朗普宣布将对全球加征10%进口关税**[NW09]。这一矛盾构成影响全球贸易和产业链预期的核心变量，可能加剧市场波动，并影响中国出口导向型行业的盈利前景。
2.  **产业与投资线索**：
    *   **制造业绿色转型**：国内媒体报道聚焦制造业降碳，路径包括扩大绿电应用和落地能碳平台[WB10]，这为新能源、节能服务、碳管理软件等领域带来长期主题。
    *   **机构调研方向**：公募基金节前集中调研**机器人、半导体、有色金属**行业[NW13]，与市场表现中机器人、AI硬件等板块走强形成呼应，显示机构资金可能正在布局相关“新质生产力”方向。
3.  **社会事件影响**：网传“初中生扶老人被索赔22万”事件成为社交平台热点[NW02, WB11]，触及社会信任与道德议题，短期内可能引发公众情绪波动，但对金融市场无直接因果影响。

## 三、明日跟踪清单
1.  **延续跟进：韩国股市独立行情的驱动逻辑验证**：结合历史关注，需补充今日韩国市场领涨板块、资金流入数据及具体产业政策催化，判断其上涨的可持续性。
2.  **收口复盘：美国关税政策矛盾的市场演化**：紧密跟踪特朗普新关税主张与最高法院裁定之间的官方表态、法律程序进展，以及美股、美元、美债对此的后续反应，评估其对全球资产定价的冲击。
3.  **新增观察：港股AI/机器人强势板块的持续性**：观察智谱AI等领涨股能否延续强势，以及板块效应是否会扩散至A股相关的机器人、半导体产业链，验证机构调研逻辑的市场认同度[⁹](https://wallstreetcn.com/articles/3765892)[¹⁰](https://www.cls.cn/detail/2291772)。


---

<details><summary>📑 点击展开各板块详细分析</summary>

### 📊 市场数据详细分析

### 1. 主要市场走势判断
覆盖时段内，全球主要市场呈现**区域分化**格局。**亚太市场普遍承压**，其中A股（-1.26%）、日股（-1.12%）和港股（-1.10%）领跌。与此形成鲜明对比的是，**欧美市场整体走强**，法国CAC40（+1.39%）、德国DAX（+0.87%）和纳斯达克综合指数（+0.90%）表现突出。美股三大指数（标普500、纳斯达克、道琼斯）均录得上涨，而罗素2000指数微跌（-0.05%）。**韩国市场（+2.31%）成为全球涨幅最大的主要市场**。

### 2. 关键资产轮动分析
*   **领涨方向**：
    1.  **欧洲蓝筹股**：法国CAC40与德国DAX的显著上涨，显示资金在时段内偏好欧洲核心资产。
    2.  **美国科技股**：纳斯达克指数涨幅（+0.90%）显著跑赢道琼斯指数（+0.47%），表明市场风险偏好有所回升，资金流向成长型板块。
    3.  **韩国股市**：韩国综合指数**大涨2.31%**，成为全球最强市场，反映特定区域或行业资金流入。具体驱动因素数据不足/未提供。
*   **领跌方向**：
    1.  **大中华区股市**：A股与港股同步下跌，显示该区域资产面临抛压。
    2.  **日本股市**：日经225指数下跌，与亚太市场疲软趋势一致。
*   **资金偏好解读**：时段内资金呈现 **“西强东弱”** 的流动特征，从亚太（除韩国外）流向欧美市场。同时，在美股内部，资金从代表小盘股的罗素2000指数流出，转向以科技股为代表的大盘成长股，显示资金在追求确定性的同时，保留了一定的进攻性。

### 3. 加密货币和商品期货的关键变化
*   **加密货币**：主要加密货币普遍上涨。**BTC (+1.56%)、ETH (+1.05%)、SOL (+2.64%)** 均录得正收益，其中SOL涨幅领先。这表明加密货币市场风险情绪偏积极，与美股科技股走强形成呼应。
*   **商品期货**：
    *   **工业金属**：**COMEX铜价大涨2.44%**，是商品中表现最强的品种，可能反映对全球工业需求的乐观预期。
    *   **能源**：WTI原油（-0.18%）与布伦特原油（-0.66%）小幅下跌，天然气（-0.07%）几乎平盘，显示能源市场供需预期稳定，缺乏方向性驱动。
    *   **贵金属**：数据不足/未提供。

### 4. 涨跌驱动链条分析
基于现有数据，可梳理出以下部分驱动链条（证据强弱标注：强证据为**直接数据关联**，弱证据为**同步性关联**）：

*   **链条一：风险情绪局部回暖 -> 资金流向科技股与加密货币 -> 纳斯达克与加密资产上涨**
    *   **事件/政策/情绪**：数据不足/未提供具体事件。但**VIX波动率指数下跌5.64%**，是市场恐慌情绪缓解的直接证据（强证据）。
    *   **资金行为**：资金减少避险，增加对风险资产的配置。具体表现为：买入纳斯达克科技股（强证据：指数上涨）、买入加密货币（强证据：价格普涨）。
    *   **价格表现**：纳斯达克综合指数上涨0.90%；BTC、ETH、SOL价格上涨。

*   **链条二：区域资金流向变化 -> 欧股与韩股受追捧，亚太其他市场被抛售 -> 区域指数显著分化**
    *   **事件/政策/情绪**：数据不足/未提供导致资金跨区域流动的具体原因。
    *   **资金行为**：资金流出A股、港股、日股（强证据：指数下跌）；资金流入欧洲股市（强证据：法、德股指上涨）和韩国股市（强证据：指数大涨）。
    *   **价格表现**：法国CAC40（+1.39%）、韩国综合指数（+2.31%）领涨；上证综指、恒生指数、日经225指数下跌。

*   **链条三：工业需求预期变化 -> 资金买入铜 -> 铜价大涨**
    *   **事件/政策/情绪**：数据不足/未提供改变工业金属需求预期的具体信息。
    *   **资金行为**：资金在商品期货市场买入铜合约（强证据：价格大幅上涨2.44%）。
    *   **价格表现**：COMEX铜价显著走强，表现远超同期波动的原油。

**总结**：覆盖时段内，市场主线是**风险情绪的局部改善（VIX下降）与资金的区域/板块再配置**。资金从部分亚太市场流出，转而流入欧洲、美国科技股及韩国市场，同时推高了加密货币和铜价。然而，**导致这种跨市场资金大轮动的核心宏观催化剂，在提供的数据中并未明确**。

### ⏱ 市场时效过滤说明

市场时效过滤结果：
1. 早报阶段不纳入 A 股盘面，避免使用非交易时段快照

### 🐦 Twitter 逐条简介

Twitter 逐条简介（共 12 条，按互动热度排序）：
1. [热门] @rickcomenta | 2026-02-21T00:00 | 互动=19310
   原文摘录: aí vem uns pamonha dizendo que ela é diva por ignorar a doidinha do centro 🤪🤪🤪 se ela não fosse uma leoa no quarto até daria pra considerar isso como desprezo, 
   原文链接: [点击查看原文](https://twitter.com/rickcomenta/status/2024942662961303868)
   1) 讲了什么：用户评论某女性因无视他人被称“女神”，但实际是软弱。
   2) 关键信号：未提供金融科技相关信号。
   3) 阅读建议：略读，内容为个人社交评论，无金融科技信息。
2. [热门] @atrupar | 2026-02-21T00:00 | 互动=17023
   原文摘录: NEWSMAX: Do you think Jeffrey Epstein killed himself? REP. NANCY MACE: No, absolutely not. I think he was murdered. I don't know if it was an intel agency or wh
   原文链接: [点击查看原文](https://twitter.com/atrupar/status/2024466512359154023)
   1) 讲了什么：众议员Nancy Mace在Newsmax采访中认为Jeffrey Epstein是被谋杀而非自杀。
   2) 关键信号：她提到监控录像数据被删除，但未指明具体机构。
   3) 阅读建议：略读 + 原因：仅为单一政治人物观点陈述，未提供新证据或数据。
3. [热门] @Yodobashi_X | 2026-02-21T00:00 | 互动=13582
   原文摘录: ＼買うなら、Office 2024搭載PC／ 最新のRyzen AI 5 Pro 搭載💻 カフェに映える上質ボディも魅力✨ 見た目も中身も妥協したくない人に👍 DELLのノートPC【MCR54-GHHB】 フォロー＆リポストで 1⃣名様にプレゼント🎁 2/26まで‼️ このPCはどんな用途で活躍しそうですか❓ コメント
   原文链接: [点击查看原文](https://twitter.com/Yodobashi_X/status/2024725707725976019)
   1) 讲了什么：DELL推出搭载Office 2024和Ryzen AI 5 Pro的笔记本电脑，并举办转发抽奖活动。
   2) 关键信号：产品发布与营销活动；高互动量（点赞2827，转发9506）。
   3) 阅读建议：略读 + 原因：内容为常规产品推广与抽奖，无具体金融科技动态或深度分析。
4. [热门] @WhiteHouse | 2026-02-21T00:00 | 互动=9872
   原文摘录: President Donald J. Trump has effectively used TARIFFS over the past year to MAKE AMERICA GREAT AGAIN: ✅ Stock Market recently broke the 50,000 mark on the Dow 
   原文链接: [点击查看原文](https://twitter.com/WhiteHouse/status/2024926556880031987)
   1) 讲了什么：特朗普总统利用关税使美国再次伟大，列举了股市、战争、国家安全和芬太尼减少等成果。
   2) 关键信号：股市达特定点位，结束部分战争，芬太尼流入减少30%。
   3) 阅读建议：略读 + 原因：内容为单方面政策宣传，缺乏具体数据来源和背景说明。
5. [热门] @NotAvgLiberal | 2026-02-21T00:00 | 互动=9836
   原文摘录: MAGA thinks the Epstein Files exonerate Trump. MAGA also believed - They’d get a $5000 DOGE check. They’d get a $2000 Tariff check. Mexico would pay for the wal
   原文链接: [点击查看原文](https://twitter.com/NotAvgLiberal/status/2024648812233363868)
   1) 讲了什么：推文讽刺MAGA群体相信特朗普多项未兑现承诺，并认为其关心他们。
   2) 关键信号：列举了多项特朗普被提及但未提供的承诺，如关税支票、降低物价等。
   3) 阅读建议：略读 + 原因：内容为个人情绪化讽刺，无具体金融科技信息或数据。
6. [热门] @RachelReevesMP | 2026-02-21T00:00 | 互动=9690
   原文摘录: ⬇️ Inflation down ⬇️ Interest rates down ⬇️ Borrowing down ⬆️ Retail sales up ⬆️ UK fastest growing European G7 economy There's more to do, but our economic pla
   原文链接: [点击查看原文](https://twitter.com/RachelReevesMP/status/2024779618587156555)
   1) 讲了什么：英国通胀、利率、借贷下降，零售销售上升，经济为欧洲G7增长最快。
   2) 关键信号：数据未提供具体数值，仅提供趋势方向。
   3) 阅读建议：略读 + 原因：内容为宏观趋势陈述，无具体数据或分析。
7. [热门] @newhurizons | 2026-02-21T00:00 | 互动=8117
   原文摘录: Someone is using AI to impersonate me 💔#ai#gaming#animalcrossing#creator#content
   原文链接: [点击查看原文](https://twitter.com/newhurizons/status/2024621032422756747)
   1) 讲了什么：有人用AI冒充推文作者，作者表达伤心。
   2) 关键信号：AI冒充、作者身份、相关标签。
   3) 阅读建议：略读 + 原因：信息有限，未提供具体事件细节或影响。
8. [热门] @bounty_atm | 2026-02-21T00:00 | 互动=6403
   原文摘录: "지금 난리난" 제미나이 3개월 무료 요약 : 구글 AI 강의 10분 들으면 제미나이 프로 3개월 무료 1. 아래 LINK 접속 2. 'Get Started' 클릭 3. Coursera 에서 강의료 0원 결제 4. 강의 듣기 - 바로 넘기면됨 - 2-2 에서 구독권 링크 나오면 클릭 5
   原文链接: [点击查看原文](https://twitter.com/bounty_atm/status/2024823621651255501)
   1) 讲了什么：推文介绍通过听谷歌AI课程免费获得Gemini Pro三个月订阅的方法步骤。
   2) 关键信号：提供具体操作步骤，提及自动续费需手动取消。
   3) 阅读建议：略读 + 原因：内容为具体操作指南，无行业深度分析或趋势研判。
9. [热门] @MikeNellis | 2026-02-21T00:00 | 互动=5790
   原文摘录: Every single Republican president in my lifetime has crashed the economy. Trump is the first to do it twice.
   原文链接: [点击查看原文](https://twitter.com/MikeNellis/status/2024854541221433650)
   1) 讲了什么：推文称作者一生中每位共和党总统都搞垮了经济，特朗普是首个搞垮两次的。
   2) 关键信号：未提供具体经济数据或事件，仅为个人政治观点陈述。
   3) 阅读建议：略读，因缺乏具体事实依据，属观点表达。
10. [热门] @DemocraticWins | 2026-02-21T00:00 | 互动=5441
   原文摘录: BREAKING: Watch the exact moment that Fox News is forced to show their audience the proof that Donald Trump is destroying the economy. Wow.
   原文链接: [点击查看原文](https://twitter.com/DemocraticWins/status/2024859558783426571)
   1) 讲了什么：Fox News被迫向观众展示特朗普破坏经济的证据。
   2) 关键信号：BREAKING新闻，互动量高，原文称“Wow”。
   3) 阅读建议：略读 + 原因：仅为单方宣称，未提供具体证据或数据。
11. [热门] @NikeiNikeiNiii | 2026-02-21T00:00 | 互动=3743
   原文摘录: hi oomfs. i've been seeing the twitter family and interaction circle trend going around again DO NOT PARTICIPATE IN THIS TREND. DO NOT CLICK THE LINK. it forces
   原文链接: [点击查看原文](https://twitter.com/NikeiNikeiNiii/status/2024792881613897760)
   1) 讲了什么：用户警告不要参与“Twitter家庭和互动圈”趋势，称其会强制关注AI和加密账户。
   2) 关键信号：趋势包含可疑链接，可能导致账户被控制；建议已参与者立即改密码。
   3) 阅读建议：精读 + 原因：这是针对特定社交媒体威胁的直接安全警告，具有行动指导性。
12. [热门] @NizNellie3 | 2026-02-21T00:00 | 互动=3065
   原文摘录: 🚨 Left pic: A 16-year-old in Asheville, N.C., vomiting anti-ICE propaganda, fed to him by adult activists. Right pic: A violent illegal from Mexico charged with
   原文链接: [点击查看原文](https://twitter.com/NizNellie3/status/2024650662198313182)
   1) 讲了什么：对比两张图片，一张显示青少年受活动人士影响，另一张显示被指控犯罪的非法移民被捕。
   2) 关键信号：未提供具体数据或事件交叉验证，仅为单方描述。
   3) 阅读建议：略读 + 原因：内容为单点事件陈述，缺乏可验证的广泛金融科技关联信息。

### 🌐 Twitter 英文信号详细分析

### 海外英文信号主线
1.  **美国国内政治与经济叙事激烈对立**：特朗普支持者（MAGA）宣称其关税政策提振了股市（道指突破50000点，标普突破7000点）并增强了国家安全；而反对者则指责特朗普破坏了经济，并列举其多项承诺（如发放加密货币支票、墨西哥支付边境墙费用）未能兑现。同时，有指控称民主党人通过政策“蓄意破坏”了经济增长。
2.  **围绕爱泼斯坦案与国内安全议题的争议持续**：有国会议员公开质疑爱泼斯坦是遭谋杀而非自杀，并提及监控数据被删除。移民问题也成为焦点，存在将青少年抗议者与非法移民暴力犯罪并置对比的叙事。
3.  **英国与印度展现积极经济与科技政策信号**：英国方面强调通胀、利率和借贷成本下降，零售销售上升，自称是G7中增长最快的欧洲经济体。印度方面，马哈拉施特拉邦宣布将在所有领域实现“AI赋能”，同时国内政治围绕AI峰会上的抗议活动产生激烈争论。

### 与金融科技/AI/Web3相关的具体线索
1.  **AI应用与风险**：
    *   **深度伪造与身份冒用**：有创作者表示其形象被AI冒用。
    *   **AI赋能趋势**：印度马哈拉施特拉邦宣布将在所有领域部署AI能力。日本推文显示搭载Ryzen AI 5 Pro芯片的PC成为营销卖点。
    *   **行业影响**：游戏行业意见认为，缺乏游戏背景、出身AI或互联网公司的高管（如微软Xbox新CEO）可能不利于游戏产品发展。
    *   **AI与政治**：日本有观点认为新兴政党类似“政治咨询党”，主打用AI推进政策。
2.  **加密货币与相关欺诈**：
    *   **市场观点**：有分析指出比特币相对于黄金的图表RSI处于历史低位，并正处于约14个月的熊市中。
    *   **欺诈警告**：用户警告不要参与所谓的“Twitter家庭互动圈”趋势，该趋势会强制用户关注虚假的AI和加密货币账户，存在安全风险。
3.  **金融科技促销**：有推文详细介绍了通过完成谷歌AI课程免费获得Gemini Pro三个月订阅的步骤。

### 可执行关注点与潜在误导噪音
*   **可执行关注点**：
    1.  **政策与区域发展**：关注印度马哈拉施特拉邦“全领域AI赋能”计划的后续具体政策与投资动向。
    2.  **行业人才动向**：关注科技公司（如Meta、微软）的AI业务高管向传统行业（如游戏）流动的趋势及其对产品战略的影响。
    3.  **安全风险**：警惕社交媒体上以“互动”、“家庭”为名诱导点击链接，从而导致账户自动关注垃圾AI/加密账号的新型欺诈手法。
*   **潜在误导噪音**：
    1.  **情绪化经济断言**：关于特朗普“两次搞垮经济”或民主党“蓄意破坏GDP增长2个百分点”的指控属于高度政治化的单方面宣称，缺乏具体数据支撑，需谨慎对待。
    2.  **未证实的阴谋论**：关于爱泼斯坦案“情报机构谋杀”及“监控数据被删除”的说法仅为单方面指控，事件真相数据不足/未提供。
    3.  **促销信息混杂**：关于加密货币（DOGE）支票、关税支票等过往承诺的列举，主要用于政治攻击，而非当前可执行的金融政策信号。

### 📰 热榜详细分析

# 热榜综合分析报告

基于提供的七个分片摘要，经过去重与整合，分析如下：

## 1. 跨平台共同关注的3-5个热点事件
1.  **特朗普关税政策动向**：这是最突出的跨平台焦点。事件包含两个相互关联的层面：一是**美国最高法院裁定特朗普政府时期的大规模关税政策违法**（分片1、2、5、7），分片2提及可能导致超1750亿美元税收退款；二是**特朗普本人宣称将对全球商品加征10%进口关税**（分片3、6、7），形成政策预期上的矛盾与不确定性。
2.  **重大安全事故**：**载有8名中国游客的车辆在贝加尔湖沉没事故**（分片2、4），造成7人遇难、1人获救，后续遗体被找到（分片7），引发广泛关注。
3.  **体育赛事捷报**：**王心迪在自由式滑雪男子空中技巧项目中为中国队夺得金牌**（分片1、3、4、5、6），其与同为冬奥冠军的妻子徐梦桃组成的“金牌夫妻档”也成为热点（分片1、6）。
4.  **地缘政治与军事紧张**：多个分片提及相关事件，包括：**美军在黄海的活动被解放军有效处置**（分片1）；**美以可能联合袭击伊朗或美国考虑对伊朗进行“有限军事打击”**（分片2、3、7），分片7指出美军在中东集结近23年来最大空中兵力，伊朗威胁反击；**日本九成议员支持修宪**（分片2），被指“彻底撕掉和平伪装”。

## 2. 与金融市场相关的重要新闻
*   **美国政策与经济数据影响**：**美国最高法院裁定关税违法**（分片2、5）与**特朗普宣称将加征新关税**（分片3、6、7）共同构成重大政策风险，影响全球贸易预期。分片5指出，关税裁决后美股收高但债市汇市承压，滞胀担忧推动黄金白银价格大涨。此外，**美国四季度GDP仅增长1.4%**（分片2），政府停摆拖累增长；**美国12月核心PCE物价指数同比为3%**（分片3），超出预期。
*   **地缘政治推高商品价格**：因美以可能袭击伊朗的消息，**原油与贵金属价格大幅收涨**（分片2）。
*   **港股与特定板块动态**：港股马年首个交易日**科技股分化**，恒生科技指数下跌，但**AI、大模型、存储及机器人概念股逆势大涨**，例如智谱股价大涨近43%（分片3）。分片6则指出美股三大指数集体下跌。
*   **半导体/存储市场供需**：**三星HBM4据称涨价30%**，韩国“芯片双雄”积极扩产，反映“存储荒”问题（分片7）。
*   **机构动向与产业投资**：中国顶流私募Q4**集体加仓拼多多**，且AI投资重心发生转变（分片1）。公募基金在节前集中调研**机器人、半导体、有色金属**行业（分片7）。节前资金已挤入**机器人相关ETF**（分片4）。

## 3. 科技/AI 相关热点
*   **芯片与硬件发布**：**英伟达CEO黄仁勋宣布将在3月发布“世界前所未见”的全新芯片**（分片4）。
*   **自动驾驶进展**：**特斯拉无人驾驶车正式下线**，该车型无方向盘、踏板和后视镜（分片5）。
*   **资本市场关注度**：AI概念在金融市场受到追捧，如港股AI、大模型、机器人概念股大涨（分片3）。AI投资是私募（分片1）和公募（分片7）的关注方向。
*   **行业影响预测与讨论**：**微软AI负责人预测，未来18个月内多数白领工作可能被AI彻底替代**（分片6）。“谷歌天团”反驳AI泡沫质疑，称其为一场规模和速度远超工业革命的变革（分片6）。清华学霸俞浩提出要超越马斯克与黄仁勋的商业目标（分片6）。
*   **应用与舆论事件**：AI视频应用**Seedance2.0在春晚出圈**（分片1）。台媒质疑春晚机器人是合成效果（分片6）。机器人复刻成龙醉拳幕后引发关注（分片5）。
*   **产业政策**：**日本首相在施政演讲中明确提及加大AI产业投资**（分片1）。

## 4. 社会舆论焦点
*   **春节期间的社会文化话题**：这是多个分片共同的社会焦点，包括：“迎财神”（分片4）、年轻人走亲戚的方式（分片4、5）、返乡年轻人“挤爆”县城酒店（分片5）、非遗表演（分片7）、破除“喝酒暖身”等养生谣言（分片5），以及《中国婚姻报告2026》发布（分片7）和家庭矛盾/离婚咨询（分片1）等衍生讨论。
*   **社会道德与信任议题**：**网传“初中生扶老人被索赔22w”** 事件成为贴吧热榜第一（分片4），触及社会信任问题。
*   **娱乐与文体热点**：除前述体育赛事（王心迪夺金等）外，还包括：2026年春晚相关话题（Remix版本、机器人、名场面盘点）（分片5、6）；娱乐事件如李天马喊“回家生孩子”（分片2）、沈腾稳坐票房最高男主演（分片2）、吴京称培养年轻功夫明星难（分片2）等。
*   **安全事故与民生问题**：除贝加尔湖事故外，**国务院安委办通报两起烟花爆竹爆燃事故并部署安全监管**（分片7）。超大城市粪便处理问题引发知乎热议（分片6）。
*   **国际政治与网络争议**：国际事件如中国代表重申日本没资格“入常”（分片6）等引发关注。网络上也出现“港人偷拍同胞”等涉及地域的争议性话题（分片5）。

### 💻 GitHub 项目详细分析

# GitHub热门项目技术趋势分析报告

## 一、最值得关注的项目筛选

基于提供的项目热度（Star数）与主题相关性，筛选出以下7个最值得关注的项目：

1.  **openclaw/openclaw** (AI): ⭐214,239
2.  **AutoGPT** (AI): ⭐181,902
3.  **n8n-io/n8n** (AI): ⭐175,541
4.  **ollama/ollama** (AI): ⭐163,021
5.  **bitcoin/bitcoin** (Web3): ⭐88,201
6.  **tradingstrategy-ai/trading-strategy** (金融科技): ⭐347
7.  **SeungMaeda/polymarket-copy-bot-ts** (金融科技): ⭐852

## 二、应用场景与落地价值分析

*   **AI 代理与自动化平台 (openclaw, AutoGPT, n8n, langflow, dify)**: 这些高星项目共同指向一个核心趋势：**AI 应用的平民化与工作流自动化**。`openclaw`定位为跨平台个人AI助手，`AutoGPT`旨在提供可构建的AI工具，`n8n`和`langflow`、`dify`则聚焦于通过可视化或低代码方式构建、部署AI驱动的自动化工作流和智能体。其落地价值在于降低企业和开发者集成、定制AI能力的门槛，提升业务流程效率。`ollama`作为模型运行工具，为上述应用提供了本地化部署多种开源大模型的基础能力。

*   **去中心化金融 (DeFi) 与预测市场工具**: 在金融科技领域，`tradingstrategy-ai/trading-strategy`是一个针对去中心化交易所的量化交易算法框架，其价值在于为链上金融活动提供系统化的分析、策略开发和执行工具。`SeungMaeda/polymarket-copy-bot-ts`是针对Polymarket预测市场的跟单交易机器人，体现了预测市场这一细分场景的自动化交易需求。两者均服务于快速增长的Web3金融生态。

*   **Web3 基础设施与安全**: `bitcoin/bitcoin`作为比特币核心客户端，是加密货币领域的基石基础设施，其持续更新维护对整个网络的安全与稳定至关重要。同时，`MetaMask/eth-phishing-detect`和`phishdestroy/destroylist`等项目专注于实时检测和屏蔽钓鱼域名，反映了随着Web3用户增长，安全防护已成为刚需，具有明确的落地防御价值。

## 三、可能的泡沫噪音或重复概念提示

1.  **AI 工作流/智能体平台概念集中**: 输入列表中，`n8n`、`langflow`、`dify`以及`AutoGPT`的部分目标均涉及AI工作流或智能体构建。虽然各自在实现方式（如可视化、代码、专注生产环境）上可能有差异，但存在**功能与概念高度重叠**的可能性。需要警惕市场是否在重复解决相似问题，以及部分项目是否因概念热门而获得过高关注。

2.  **金融科技项目中的特定场景依赖**: `SeungMaeda/polymarket-copy-bot-ts`的价值紧密绑定于Polymarket单一预测市场平台的生态与规则。预测市场本身是一个**波动性大、监管环境不明确**的领域，此类工具的应用范围和可持续性存在较高不确定性，可能伴随市场或政策变化迅速失去价值。

3.  **数据不足的评估**: 对于`ebrasha/free-v2ray-public-list`（免费代理服务器列表）这类项目，其技术原理与金融科技的关联性未提供明确说明，归类依据不足。同时，所有项目的实际生产环境采用率、商业成功案例等关键落地价值指标**均未提供**，无法评估其真实影响力与市场渗透情况。

### 🌐 联网检索摘要

联网检索共 14 条（关键词: 2026-02-21 全球市场 盘面 复盘 原因, 2026-02-21 中国 宏观 经济 政策 市场 影响, 2026-02-21 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 上涨 原因, 第4金！王心迪夺男子空中技巧冠军 事件 背景, 初中生扶老人被索赔22w 事件 背景, 2026春晚Remix 事件 背景）
1. [2026-02-21 07:48] 新浪财经 | 深夜，全线大涨！特朗普，重磅宣布！ - 新浪财经
   摘要: 深夜，全线大涨！特朗普，重磅宣布！ 新浪财经
   链接: https://news.google.com/rss/articles/CBMihwJBVV95cUxNLWtLNzhkS0hJTHhmZEtwWEJ0cXUyWlNoNDlwU2U3SEpfdFVEM0gwbmI0Uzlfdi1Qb1RNdWpJNW1TM0NLUjhVLTBOX0xxaG5WNHNSTEVKOG9zNURoMDlWWXFkQ2N4YThvaEF4Z1FfR2NqT3U2SVFMdkRMUDQwd1Rpby1kSFpyX0FxUm9BMHl4cWUzWGVaVkxuRTJlRV9QZzhSRGdxWHVxek9MYzZ5TzVYektUZzRfTDU5VjRvY3hEY01ucjFrUGozUG9oTVBtMlFUREY0dmN3YXZTZ1J1OXh3TnM4VFZxeDJ4YlRESmJBYUNXZktuakMyWjFpM1lMXzRMUTV6dFJUZw?oc=5
2. [2026-02-21 07:35] 搜狐网 | 徐梦桃、王心迪，夫妻双双把金夺！ - 搜狐网
   摘要: 徐梦桃、王心迪，夫妻双双把金夺！ 搜狐网
   链接: https://news.google.com/rss/articles/CBMihwFBVV95cUxQMG1ienBaYVBPX2xEeEx0TWNNNmdPZS0waDBFOGNEWWRwSUxoNVlxbE1fN2hxM29PUW9MRDV0TVN2WUJWTHJxMzZlMkgtUTNvdm5xSXJkaGFUZlF6b1RTdHlKcXoyODYwTVozb1lIMkNqSm9wNGRta1Y4cUVwSWhLbUVkRGZ2cjg?oc=5
3. [2026-02-21 07:31] thepaper.cn | 城市年鉴2025｜制造业降碳：扩大绿电应用，落地能碳平台 - thepaper.cn
   摘要: 城市年鉴2025｜制造业降碳：扩大绿电应用，落地能碳平台 thepaper.cn
   链接: https://news.google.com/rss/articles/CBMiXkFVX3lxTE5VNWRMOVNGZzhsZFBJLUswY3Q4X1VaR3pYUHpNU3RHU0t5VEJkbzI4aWtNNVZ1UEEzcW40dWlQeVBLbUxLNkZJck5kaFdvUE1SNXlXektfT21XS1VtcEE?oc=5
4. [2026-02-21 07:15] 搜狐网 | “我不能让中国队包揽！”王心迪夺金背后的“集团优势” - 搜狐网
   摘要: “我不能让中国队包揽！”王心迪夺金背后的“集团优势” 搜狐网
   链接: https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVFpVMGlSQ0VJdEstT3ptNkFaVWZ5dkFZcmZoSUZnOVJEUnpMUml5TUo3QTR4Vl9peUllNHJNcGNCeE0wb3R0XzAyZVo2ZVZYX2d1aDkxbVhvNEpSQzZoYXd6OWxrNjFnRTRWZE8wenNaeGVIVXB1bVo2TW5JaDRiaG1ETmZlMUVKT3NR?oc=5
5. [2026-02-21 07:15] 新浪财经 | 新浪财经隔夜要闻大事汇总：2026年2月21日 - 新浪财经
   摘要: 新浪财经隔夜要闻大事汇总：2026年2月21日 新浪财经
   链接: https://news.google.com/rss/articles/CBMihAFBVV95cUxQY25wdUpCLWtCOUloS2FsaTFna0M1bEZoVTY3aXQ4OUY3WFNOLWFtU2lUMFYzeW8tdTc3RDBYVGF1YXdEeng0bTdZUzdWblhINGVfYnEtSHI5ZWFvOUNmaV9iTjliYTZMR3RDaHlfUTNwRFprdEhtdDdrS1dtTkQ2aUZFVlk?oc=5
6. [2026-02-21 05:30] 英为财情 Investing.com | 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5
7. [2026-02-21 04:22] 游侠网 | 平博APP - 游侠网
   摘要: 平博APP 游侠网
   链接: https://news.google.com/rss/articles/CBMiVEFVX3lxTE5qcFhxZnlvS3Jwblh6UEcxcWM4Zkl2aWc5RnlMaEYtc0tlVjVBVHYydEFBTndySWozYnZFekVRUzQzSEtpY0N2YnZsNTBUS0tySld0bQ?oc=5
8. [2026-02-20 19:48] OR新媒体 | OR新媒体| 美股为何如此诡异？ - OR新媒体
   摘要: OR新媒体| 美股为何如此诡异？ OR新媒体
   链接: https://news.google.com/rss/articles/CBMiREFVX3lxTE9EeFVtMVR6V1p3ckhwSHhLT29tTVZHYkRFcFhNQW5wbU82WEd4eDdfN2FLSkpTaEcyTGJWelF2bWR0ekJf?oc=5
9. [2026-02-20 19:27] 中國報 China Press | 2026米兰冬奥｜父因天安门事件被监视 刘美贤花滑逆转夺金 - 中國報 China Press
   摘要: 2026米兰冬奥｜父因天安门事件被监视 刘美贤花滑逆转夺金 中國報 China Press
   链接: https://news.google.com/rss/articles/CBMi1AJBVV95cUxQN19rOFNKdzdEaGFEcnFldFFHTmFQWm5VWFhmZEd0RHdpSTBvMjNLcEFOVlpqUFpGQmNVTHJxTnlLZGJYZVRua2NkZTRxbERDSlR1aUkyY3dWdWhMam5aNW5MZVJFSVJNWWtiRUlDWEdZeXdBZ2N4MWsyakZsNmVxWm12NTZnS1Y4Ylg0ZWtqMVNDRWttVVd0Q2E3cXRiSDBVSTBUeGk5U2VQNUFSalJUTE1ZNHBhT1FZSmlVT19qaGNadTFKcllYa0RGNDNzaFRUOFZ0amVZZWV4WHp5MWF0TGRPSTdDTTJBaVZQaEhtYXNGaW1lbkp2VzBjaGp3ZjhxUHJrN2dqLXp3NGpXMF85anZlaWV1c2Y2cUFYWm1WU2RaZFBjbDd3clBsZzIxalE2MTFwekZCRkVFZF9xRFlJOXQ3TVdZTHFrdndRMHFxZk94ZG1z?oc=5
10. [2026-02-20 14:45] Bitget | 美银对较高的股票风险敞口发出逆势“卖出”信号 - Bitget
   摘要: 美银对较高的股票风险敞口发出逆势“卖出”信号 Bitget
   链接: https://news.google.com/rss/articles/CBMia0FVX3lxTE5LLUpQSDBuUUxLbkRLSDRWRV84VFJ4SmUwSFNJNFNPY0tWbFBweVVDYkF6SG5jZlktZEtsbTc4dWEzU0FrRFdhWnd2WFRMb3FkeWFwVmdGc2t2WkFqTlZ6UmdfZlFqTHBEZmZn0gFrQVVfeXFMTkstSlBIMG5RTEtuREtINFZFXzhUUnhKZTBIU0k0U09jS1ZsUHB5VUNiQXpIbmNmWS1kS2xtNzh1YTNTQWtEV2Fad3ZYVExvcWR5YXBWZ0Zza3ZaQWpOVnpSZ19mUWpMcERmZmc?oc=5
11. [2026-02-20 14:26] World Journal | 閩老婦自摔 初中生去扶竟須負次責、被索賠22萬…網炸鍋 - World Journal
   摘要: 閩老婦自摔 初中生去扶竟須負次責、被索賠22萬…網炸鍋 World Journal
   链接: https://news.google.com/rss/articles/CBMihgFBVV95cUxNRnFiV2ZXLVVMbE5RNTJmNWY0TnViRzg0eW1nMGx2YzhFLU9heXFNSXNmU1VQbGcwWldJSFhzWTRISGw4UjZ3RUN1dFdpVGx0VzUwWDhLdElYU2pEbVJmckJSNUttbW8xSmlrWFhCUmFRcTQxSlZGZzJNSHh4WlRFdmRoRUc5d9IBZ0FVX3lxTE03c0E0dkllbzhDUk8yd3dXclJiUm5TbmFkbHZ1U1JQU1hQM09CY3hPajN0MV9TdUl1T0ZLMWlNal9UWXlDX1ZvWlZrX3d2cUF5YjBDV2J5QlJtUFdTV0JZSjRJOG9FQVk?oc=5
12. [2026-02-20 05:30] 英为财情 Investing.com | 美国股市收低；截至收盘道琼斯工业平均指数下跌0.54% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 美国股市收低；截至收盘道琼斯工业平均指数下跌0.54% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTE1mLUhCeDg1RGJEWEhwdlA0SkxOQWtoS2kxYzUxQTdYSnZCcTd5SU5USS0tZzZKdFhRb0E0bWZSNGVhR285dGlqNFQ0dDZLTFg0M1VaMWEyVjJ4OWpBV3dNdmJldG5wQlBOc3pzVXZpTkc?oc=5
13. [2026-02-19 22:57] Mix Vale | 由于美伊紧张局势以及沃尔玛和 DoorDash 的盈利好坏参半，美国股市下跌 - Mix Vale
   摘要: 由于美伊紧张局势以及沃尔玛和 DoorDash 的盈利好坏参半，美国股市下跌 Mix Vale
   链接: https://news.google.com/rss/articles/CBMi2gJBVV95cUxPcGpzTW5ZSGtwVzlLMVhkanFPR0VoYkFSelFBaU9tdGwtTEd4ajM0NGdMeWxNMXdKb01mZHFXcHJ6a0h4UFdkQzZpODhxenduMlVTSjdjVkNnQV9mQkNjb2pEUkR2ZGMtQTZiTWQwSHVXa0pPWHNZaGU1ZHVJTDFDT2o4MmlFd3lFbTZfYjB2YTAtUjJTUk5McE1HWnBMU3Q4dzB2VTRLZzBNa3c4MVB1M3IyT0drdjlpYzRTYlNJLTlOcU5MMnAyaThYeVV2ZjdpaC1CSTIwckFaQUZ0aXNpYkdzQ0ZtcjBtdlF2c2xHT3dPR0FhY1dhWXRnbmlucl9PSmlOdlJNREJKaW9ndUN0blNFdHE5U3lrT0xheDROWW1MSHd2YXlFTzFJWUVZcGJrMlFPNDFmSmJBZ0lRZXp1UFZGN3VGWHBHcHdiRHEzUlJXWjVhaU1KZFlR0gHfAkFVX3lxTE51dVBBeVJaMGVtVlZaMndmS25SSmNvNEp2d1hxQXNZWXRlLW10Y2FJOWdyLU9FV0UwaDdDcjZ4bzNHS1pfX052ejFIZjFWTHhkbHJmaDBzcWlSRm9Xdi0yNTNjOGJpZ0VMdllNV3FNYVk1MGFDd3p3eU5NQzF3cUlxZVBPdW1rMWFldDB0d2lCQ3NhQ1BrWGRHb2ltWmxRR05FMm9qdFpNSU5pSXFuU3NYQTBkYXYybWg4b2xRTGlPV3k1SmUwSmRYa1hpT1FObHlCXzluVlVfd18zQTYzN3htaTJoYjFyM0daSnhtZW5tUUk3QTFERzdYZjZWTm45VHA3M2RrLThDY0ZpUS1ucWFfVFlZV1pkdjByVU5uRXdNSTI3X09XMVNXV2hVMm55VkFYWGFrRXZaM3JHWTRSR3NHai1zVU05U1dGbmZsTS1HTXlMVmh2ZGdRbVJ6MnZIQQ?oc=5
14. [2026-02-19 18:30] 英为财情 Investing.com | 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.41% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.41% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTFAwMVNXS0VUVUlITVE0MjBMNkdVVGRyQUZ1a3VxZEtveVhIM3g3VDVDdE1zRWtEU3pPRTl6ZV9QRjRoRUktT000UHNKczRYS1Zha0VJYVNyYVpsS2pmaEF5dUcydE1PQmYwX0pWU3VFVE4?oc=5

</details>


### 📎 引用脚注

1. [2026-02-21T00:00 @Dev_Fadnavis | येत्या काळात महाराष्ट्र सर्व क्षेत्रात 'AI' सज्ज असेल! आने वाले समय में महाराष्ट्र सभी क...](https://twitter.com/Dev_Fadnavis/status/2024746356016107729)（Twitter，匹配分=100，来源ID=TW15）
2. [2026-02-21T00:00 @newhurizons | Someone is using AI to impersonate me 💔#ai#gaming#animalcrossing#creator#content](https://twitter.com/newhurizons/status/2024621032422756747)（Twitter，匹配分=100，来源ID=TW07）
3. [2026-02-21T00:00 @NikeiNikeiNiii | hi oomfs. i've been seeing the twitter family and interaction circle trend going around ...](https://twitter.com/NikeiNikeiNiii/status/2024792881613897760)（Twitter，匹配分=100，来源ID=TW11）
4. [2026-02-21T00:00 @WhiteHouse | President Donald J. Trump has effectively used TARIFFS over the past year to MAKE AMERIC...](https://twitter.com/WhiteHouse/status/2024926556880031987)（Twitter，匹配分=100，来源ID=TW04）
5. [2026-02-21T00:00 @NotAvgLiberal | MAGA thinks the Epstein Files exonerate Trump. MAGA also believed - They’d get a $5000 D...](https://twitter.com/NotAvgLiberal/status/2024648812233363868)（Twitter，匹配分=100，来源ID=TW05）
6. [2026-02-21T00:00 @MikeNellis | Every single Republican president in my lifetime has crashed the economy. Trump is the f...](https://twitter.com/MikeNellis/status/2024854541221433650)（Twitter，匹配分=100，来源ID=TW09）
7. [2026-02-21T00:00 @GuntherEagleman | 🚨White House CONFIRMS, Democrats and Chuck Schumer straight-up SABOTAGED the economy by ...](https://twitter.com/GuntherEagleman/status/2024856986441994564)（Twitter，匹配分=100，来源ID=TW13）
8. [2026-02-21T00:00 @RachelReevesMP | ⬇️ Inflation down ⬇️ Interest rates down ⬇️ Borrowing down ⬆️ Retail sales up ⬆️ UK fast...](https://twitter.com/RachelReevesMP/status/2024779618587156555)（Twitter，匹配分=100，来源ID=TW06）
9. [华尔街见闻 #2 | 港股马年首个交易日：恒科指跌超2%，大模型和存储逆势大涨，智谱大涨近43%，机器人概念股爆发](https://wallstreetcn.com/articles/3765892)（NewsNow热榜，匹配分=100，来源ID=NW12）
10. [财联社热门 #2 | 原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772)（NewsNow热榜，匹配分=100，来源ID=NW13）

## 🧪 引用匹配校验

- 已匹配引用条数: 10
- 未完成匹配标签: 0
- 低置信引用条数: 0
- 处理建议: 本次未发现低置信引用。

## 🎯 投机方向（超短）

- 海外指数方向：美股 VIX波动率指数 -5.64%（高波动回撤）
- 高波动资产：SOL 24h +2.64%（轻仓快进快出）
- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。

## 🌐 联网检索补充

- 关键词：2026-02-21 全球市场 盘面 复盘 原因, 2026-02-21 中国 宏观 经济 政策 市场 影响, 2026-02-21 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 上涨 原因, 第4金！王心迪夺男子空中技巧冠军 事件 背景, 初中生扶老人被索赔22w 事件 背景, 2026春晚Remix 事件 背景
- 命中结果：14 条（按发布时间倒序）

### 🔎 2026-02-21 中国 宏观 经济 政策 市场 影响

- [深夜，全线大涨！特朗普，重磅宣布！ - 新浪财经](https://news.google.com/rss/articles/CBMihwJBVV95cUxNLWtLNzhkS0hJTHhmZEtwWEJ0cXUyWlNoNDlwU2U3SEpfdFVEM0gwbmI0Uzlfdi1Qb1RNdWpJNW1TM0NLUjhVLTBOX0xxaG5WNHNSTEVKOG9zNURoMDlWWXFkQ2N4YThvaEF4Z1FfR2NqT3U2SVFMdkRMUDQwd1Rpby1kSFpyX0FxUm9BMHl4cWUzWGVaVkxuRTJlRV9QZzhSRGdxWHVxek9MYzZ5TzVYektUZzRfTDU5VjRvY3hEY01ucjFrUGozUG9oTVBtMlFUREY0dmN3YXZTZ1J1OXh3TnM4VFZxeDJ4YlRESmJBYUNXZktuakMyWjFpM1lMXzRMUTV6dFJUZw?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-21 07:48
  - 摘要: 深夜，全线大涨！特朗普，重磅宣布！ 新浪财经
- [城市年鉴2025｜制造业降碳：扩大绿电应用，落地能碳平台 - thepaper.cn](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5VNWRMOVNGZzhsZFBJLUswY3Q4X1VaR3pYUHpNU3RHU0t5VEJkbzI4aWtNNVZ1UEEzcW40dWlQeVBLbUxLNkZJck5kaFdvUE1SNXlXektfT21XS1VtcEE?oc=5)
  - 来源: thepaper.cn | 时间: 2026-02-21 07:31
  - 摘要: 城市年鉴2025｜制造业降碳：扩大绿电应用，落地能碳平台 thepaper.cn
- [新浪财经隔夜要闻大事汇总：2026年2月21日 - 新浪财经](https://news.google.com/rss/articles/CBMihAFBVV95cUxQY25wdUpCLWtCOUloS2FsaTFna0M1bEZoVTY3aXQ4OUY3WFNOLWFtU2lUMFYzeW8tdTc3RDBYVGF1YXdEeng0bTdZUzdWblhINGVfYnEtSHI5ZWFvOUNmaV9iTjliYTZMR3RDaHlfUTNwRFprdEhtdDdrS1dtTkQ2aUZFVlk?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-21 07:15
  - 摘要: 新浪财经隔夜要闻大事汇总：2026年2月21日 新浪财经
- [平博APP - 游侠网](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5qcFhxZnlvS3Jwblh6UEcxcWM4Zkl2aWc5RnlMaEYtc0tlVjVBVHYydEFBTndySWozYnZFekVRUzQzSEtpY0N2YnZsNTBUS0tySld0bQ?oc=5)
  - 来源: 游侠网 | 时间: 2026-02-21 04:22
  - 摘要: 平博APP 游侠网

### 🔎 第4金！王心迪夺男子空中技巧冠军 事件 背景

- [徐梦桃、王心迪，夫妻双双把金夺！ - 搜狐网](https://news.google.com/rss/articles/CBMihwFBVV95cUxQMG1ienBaYVBPX2xEeEx0TWNNNmdPZS0waDBFOGNEWWRwSUxoNVlxbE1fN2hxM29PUW9MRDV0TVN2WUJWTHJxMzZlMkgtUTNvdm5xSXJkaGFUZlF6b1RTdHlKcXoyODYwTVozb1lIMkNqSm9wNGRta1Y4cUVwSWhLbUVkRGZ2cjg?oc=5)
  - 来源: 搜狐网 | 时间: 2026-02-21 07:35
  - 摘要: 徐梦桃、王心迪，夫妻双双把金夺！ 搜狐网
- [“我不能让中国队包揽！”王心迪夺金背后的“集团优势” - 搜狐网](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVFpVMGlSQ0VJdEstT3ptNkFaVWZ5dkFZcmZoSUZnOVJEUnpMUml5TUo3QTR4Vl9peUllNHJNcGNCeE0wb3R0XzAyZVo2ZVZYX2d1aDkxbVhvNEpSQzZoYXd6OWxrNjFnRTRWZE8wenNaeGVIVXB1bVo2TW5JaDRiaG1ETmZlMUVKT3NR?oc=5)
  - 来源: 搜狐网 | 时间: 2026-02-21 07:15
  - 摘要: “我不能让中国队包揽！”王心迪夺金背后的“集团优势” 搜狐网
- [2026米兰冬奥｜父因天安门事件被监视 刘美贤花滑逆转夺金 - 中國報 China Press](https://news.google.com/rss/articles/CBMi1AJBVV95cUxQN19rOFNKdzdEaGFEcnFldFFHTmFQWm5VWFhmZEd0RHdpSTBvMjNLcEFOVlpqUFpGQmNVTHJxTnlLZGJYZVRua2NkZTRxbERDSlR1aUkyY3dWdWhMam5aNW5MZVJFSVJNWWtiRUlDWEdZeXdBZ2N4MWsyakZsNmVxWm12NTZnS1Y4Ylg0ZWtqMVNDRWttVVd0Q2E3cXRiSDBVSTBUeGk5U2VQNUFSalJUTE1ZNHBhT1FZSmlVT19qaGNadTFKcllYa0RGNDNzaFRUOFZ0amVZZWV4WHp5MWF0TGRPSTdDTTJBaVZQaEhtYXNGaW1lbkp2VzBjaGp3ZjhxUHJrN2dqLXp3NGpXMF85anZlaWV1c2Y2cUFYWm1WU2RaZFBjbDd3clBsZzIxalE2MTFwekZCRkVFZF9xRFlJOXQ3TVdZTHFrdndRMHFxZk94ZG1z?oc=5)
  - 来源: 中國報 China Press | 时间: 2026-02-20 19:27
  - 摘要: 2026米兰冬奥｜父因天安门事件被监视 刘美贤花滑逆转夺金 中國報 China Press

### 🔎 VIX波动率指数 下跌 原因

- [美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-21 05:30
  - 摘要: 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com 英为财情 Investing.com
- [OR新媒体| 美股为何如此诡异？ - OR新媒体](https://news.google.com/rss/articles/CBMiREFVX3lxTE9EeFVtMVR6V1p3ckhwSHhLT29tTVZHYkRFcFhNQW5wbU82WEd4eDdfN2FLSkpTaEcyTGJWelF2bWR0ekJf?oc=5)
  - 来源: OR新媒体 | 时间: 2026-02-20 19:48
  - 摘要: OR新媒体| 美股为何如此诡异？ OR新媒体
- [美银对较高的股票风险敞口发出逆势“卖出”信号 - Bitget](https://news.google.com/rss/articles/CBMia0FVX3lxTE5LLUpQSDBuUUxLbkRLSDRWRV84VFJ4SmUwSFNJNFNPY0tWbFBweVVDYkF6SG5jZlktZEtsbTc4dWEzU0FrRFdhWnd2WFRMb3FkeWFwVmdGc2t2WkFqTlZ6UmdfZlFqTHBEZmZn0gFrQVVfeXFMTkstSlBIMG5RTEtuREtINFZFXzhUUnhKZTBIU0k0U09jS1ZsUHB5VUNiQXpIbmNmWS1kS2xtNzh1YTNTQWtEV2Fad3ZYVExvcWR5YXBWZ0Zza3ZaQWpOVnpSZ19mUWpMcERmZmc?oc=5)
  - 来源: Bitget | 时间: 2026-02-20 14:45
  - 摘要: 美银对较高的股票风险敞口发出逆势“卖出”信号 Bitget
- [美国股市收低；截至收盘道琼斯工业平均指数下跌0.54% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE1mLUhCeDg1RGJEWEhwdlA0SkxOQWtoS2kxYzUxQTdYSnZCcTd5SU5USS0tZzZKdFhRb0E0bWZSNGVhR285dGlqNFQ0dDZLTFg0M1VaMWEyVjJ4OWpBV3dNdmJldG5wQlBOc3pzVXZpTkc?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-20 05:30
  - 摘要: 美国股市收低；截至收盘道琼斯工业平均指数下跌0.54% 提供者 Investing.com 英为财情 Investing.com
- [由于美伊紧张局势以及沃尔玛和 DoorDash 的盈利好坏参半，美国股市下跌 - Mix Vale](https://news.google.com/rss/articles/CBMi2gJBVV95cUxPcGpzTW5ZSGtwVzlLMVhkanFPR0VoYkFSelFBaU9tdGwtTEd4ajM0NGdMeWxNMXdKb01mZHFXcHJ6a0h4UFdkQzZpODhxenduMlVTSjdjVkNnQV9mQkNjb2pEUkR2ZGMtQTZiTWQwSHVXa0pPWHNZaGU1ZHVJTDFDT2o4MmlFd3lFbTZfYjB2YTAtUjJTUk5McE1HWnBMU3Q4dzB2VTRLZzBNa3c4MVB1M3IyT0drdjlpYzRTYlNJLTlOcU5MMnAyaThYeVV2ZjdpaC1CSTIwckFaQUZ0aXNpYkdzQ0ZtcjBtdlF2c2xHT3dPR0FhY1dhWXRnbmlucl9PSmlOdlJNREJKaW9ndUN0blNFdHE5U3lrT0xheDROWW1MSHd2YXlFTzFJWUVZcGJrMlFPNDFmSmJBZ0lRZXp1UFZGN3VGWHBHcHdiRHEzUlJXWjVhaU1KZFlR0gHfAkFVX3lxTE51dVBBeVJaMGVtVlZaMndmS25SSmNvNEp2d1hxQXNZWXRlLW10Y2FJOWdyLU9FV0UwaDdDcjZ4bzNHS1pfX052ejFIZjFWTHhkbHJmaDBzcWlSRm9Xdi0yNTNjOGJpZ0VMdllNV3FNYVk1MGFDd3p3eU5NQzF3cUlxZVBPdW1rMWFldDB0d2lCQ3NhQ1BrWGRHb2ltWmxRR05FMm9qdFpNSU5pSXFuU3NYQTBkYXYybWg4b2xRTGlPV3k1SmUwSmRYa1hpT1FObHlCXzluVlVfd18zQTYzN3htaTJoYjFyM0daSnhtZW5tUUk3QTFERzdYZjZWTm45VHA3M2RrLThDY0ZpUS1ucWFfVFlZV1pkdjByVU5uRXdNSTI3X09XMVNXV2hVMm55VkFYWGFrRXZaM3JHWTRSR3NHai1zVU05U1dGbmZsTS1HTXlMVmh2ZGdRbVJ6MnZIQQ?oc=5)
  - 来源: Mix Vale | 时间: 2026-02-19 22:57
  - 摘要: 由于美伊紧张局势以及沃尔玛和 DoorDash 的盈利好坏参半，美国股市下跌 Mix Vale
- [印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.41% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTFAwMVNXS0VUVUlITVE0MjBMNkdVVGRyQUZ1a3VxZEtveVhIM3g3VDVDdE1zRWtEU3pPRTl6ZV9QRjRoRUktT000UHNKczRYS1Zha0VJYVNyYVpsS2pmaEF5dUcydE1PQmYwX0pWU3VFVE4?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-19 18:30
  - 摘要: 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.41% 提供者 Investing.com 英为财情 Investing.com

### 🔎 初中生扶老人被索赔22w 事件 背景

- [閩老婦自摔 初中生去扶竟須負次責、被索賠22萬…網炸鍋 - World Journal](https://news.google.com/rss/articles/CBMihgFBVV95cUxNRnFiV2ZXLVVMbE5RNTJmNWY0TnViRzg0eW1nMGx2YzhFLU9heXFNSXNmU1VQbGcwWldJSFhzWTRISGw4UjZ3RUN1dFdpVGx0VzUwWDhLdElYU2pEbVJmckJSNUttbW8xSmlrWFhCUmFRcTQxSlZGZzJNSHh4WlRFdmRoRUc5d9IBZ0FVX3lxTE03c0E0dkllbzhDUk8yd3dXclJiUm5TbmFkbHZ1U1JQU1hQM09CY3hPajN0MV9TdUl1T0ZLMWlNal9UWXlDX1ZvWlZrX3d2cUF5YjBDV2J5QlJtUFdTV0JZSjRJOG9FQVk?oc=5)
  - 来源: World Journal | 时间: 2026-02-20 14:26
  - 摘要: 閩老婦自摔 初中生去扶竟須負次責、被索賠22萬…網炸鍋 World Journal

## 🔗 AI 分析引用来源

> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。

### Twitter (8 条)

- [¹] [2026-02-21T00:00 @Dev_Fadnavis | येत्या काळात महाराष्ट्र सर्व क्षेत्रात 'AI' सज्ज असेल! आने वाले समय में महाराष्ट्र सभी क...](https://twitter.com/Dev_Fadnavis/status/2024746356016107729)（匹配分=100，来源ID=TW15）
- [²] [2026-02-21T00:00 @newhurizons | Someone is using AI to impersonate me 💔#ai#gaming#animalcrossing#creator#content](https://twitter.com/newhurizons/status/2024621032422756747)（匹配分=100，来源ID=TW07）
- [³] [2026-02-21T00:00 @NikeiNikeiNiii | hi oomfs. i've been seeing the twitter family and interaction circle trend going around ...](https://twitter.com/NikeiNikeiNiii/status/2024792881613897760)（匹配分=100，来源ID=TW11）
- [⁴] [2026-02-21T00:00 @WhiteHouse | President Donald J. Trump has effectively used TARIFFS over the past year to MAKE AMERIC...](https://twitter.com/WhiteHouse/status/2024926556880031987)（匹配分=100，来源ID=TW04）
- [⁵] [2026-02-21T00:00 @NotAvgLiberal | MAGA thinks the Epstein Files exonerate Trump. MAGA also believed - They’d get a $5000 D...](https://twitter.com/NotAvgLiberal/status/2024648812233363868)（匹配分=100，来源ID=TW05）
- [⁶] [2026-02-21T00:00 @MikeNellis | Every single Republican president in my lifetime has crashed the economy. Trump is the f...](https://twitter.com/MikeNellis/status/2024854541221433650)（匹配分=100，来源ID=TW09）
- [⁷] [2026-02-21T00:00 @GuntherEagleman | 🚨White House CONFIRMS, Democrats and Chuck Schumer straight-up SABOTAGED the economy by ...](https://twitter.com/GuntherEagleman/status/2024856986441994564)（匹配分=100，来源ID=TW13）
- [⁸] [2026-02-21T00:00 @RachelReevesMP | ⬇️ Inflation down ⬇️ Interest rates down ⬇️ Borrowing down ⬆️ Retail sales up ⬆️ UK fast...](https://twitter.com/RachelReevesMP/status/2024779618587156555)（匹配分=100，来源ID=TW06）

### NewsNow热榜 (2 条)

- [⁹] [华尔街见闻 #2 | 港股马年首个交易日：恒科指跌超2%，大模型和存储逆势大涨，智谱大涨近43%，机器人概念股爆发](https://wallstreetcn.com/articles/3765892)（匹配分=100，来源ID=NW12）
- [¹⁰] [财联社热门 #2 | 原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772)（匹配分=100，来源ID=NW13）

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
| 欧股 | [英国富时100](https://finance.yahoo.com/quote/%5EFTSE) | 10,686.89 | 🟢 +0.56% | GBP |
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
| BTC | $67,999.00 | 🟢 +1.56% |
| ETH | $1,968.49 | 🟢 +1.05% |
| SOL | $84.55 | 🟢 +2.64% |

### 📈 国际期货

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|
| WTI原油 | 66.31 | 🔴 -0.18% |
| 布伦特原油 | 71.19 | 🔴 -0.66% |
| 天然气 | 2.99 | 🔴 -0.07% |
| COMEX铜 | 5.87 | 🟢 +2.44% |

### 💻 GitHub 趋势

- ⭐ [**ClawWork**](https://github.com/HKUDS/ClawWork) (4564 stars)
  - "ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"
- ⭐ [**visual-explainer**](https://github.com/nicobailon/visual-explainer) (1833 stars)
  - Agent skill + prompt templates that generate rich HTML pages for visual diff rev
- ⭐ [**portless**](https://github.com/vercel-labs/portless) (1805 stars)
  - Replace port numbers with stable, named .localhost URLs. For humans and agents.
- ⭐ [**arscontexta**](https://github.com/agenticnotetaking/arscontexta) (1273 stars)
  - Claude Code plugin that generates individualized knowledge systems from conversa
- ⭐ [**BarraCUDA**](https://github.com/Zaneham/BarraCUDA) (1206 stars)
  - Open-source CUDA compiler targeting AMD GPUs (and more in the future!). Compiles

## 🐦 Twitter 热点 (116 条)

- 来源统计: 关注账号 190 条 | 热门讨论 30 条

### 🔥 热门讨论推文

- `2026-02-21T00:00` @rickcomenta ❤️17278 🔁1938 💬94
  - aí vem uns pamonha dizendo que ela é diva por ignorar a doidinha do centro 🤪🤪🤪 se ela não fosse uma leoa no quarto até daria pra considerar isso como desprezo, mas sabemos bem que ela não passa de uma frouxa que não tem disposição pra sustentar a rivalidade que ela msm criou
  - [原文链接](https://twitter.com/rickcomenta/status/2024942662961303868)
- `2026-02-21T00:00` @atrupar ❤️13970 🔁2787 💬266
  - NEWSMAX: Do you think Jeffrey Epstein killed himself?  REP. NANCY MACE: No, absolutely not. I think he was murdered. I don't know if it was an intel agency or what it is. The data from the videos cameras was erased.
  - [原文链接](https://twitter.com/atrupar/status/2024466512359154023)
- `2026-02-21T00:00` @Yodobashi_X ❤️2827 🔁9506 💬1249
  - ＼買うなら、Office 2024搭載PC／  最新のRyzen AI 5 Pro 搭載💻 カフェに映える上質ボディも魅力✨ 見た目も中身も妥協したくない人に👍  DELLのノートPC【MCR54-GHHB】  フォロー＆リポストで 1⃣名様にプレゼント🎁 2/26まで‼️  このPCはどんな用途で活躍しそうですか❓ コメントお待ちしてます🙇‍♂️
  - [原文链接](https://twitter.com/Yodobashi_X/status/2024725707725976019)
- `2026-02-21T00:00` @WhiteHouse ❤️7200 🔁1499 💬1173
  - President Donald J. Trump has effectively used TARIFFS over the past year to MAKE AMERICA GREAT AGAIN:   ✅ Stock Market recently broke the 50,000 mark on the Dow & simultaneously 7,000 on the S&P  ✅ Used to end five of the eight wars ✅ Great national security  ✅ Reduced fentanyl coming in by 30%, when used as a penalty against countries illegally sending poison to the U.S.
  - [原文链接](https://twitter.com/WhiteHouse/status/2024926556880031987)
- `2026-02-21T00:00` @NotAvgLiberal ❤️7016 🔁2406 💬414
  - MAGA thinks the Epstein Files exonerate Trump.  MAGA also believed -  They’d get a $5000 DOGE check.  They’d get a $2000 Tariff check.  Mexico would pay for the wall.  Trump would lower the price of groceries,  Trump would improve the economy,  Trump would replace the Affordable Care Act,  End the war in Ukraine in the first 24 hours of his presidency.  Trump would give them larger tax breaks,  Reduce the cost of natural gas and electricity,  Reduce the price of housing,  Trump would decrease th
  - [原文链接](https://twitter.com/NotAvgLiberal/status/2024648812233363868)
- `2026-02-21T00:00` @RachelReevesMP ❤️5139 🔁1052 💬3499
  - ⬇️ Inflation down ⬇️ Interest rates down ⬇️ Borrowing down ⬆️ Retail sales up ⬆️ UK fastest growing European G7 economy  There's more to do, but our economic plan is the right one.bbc.co.uk/news/articles/c93w…
  - [原文链接](https://twitter.com/RachelReevesMP/status/2024779618587156555)
- `2026-02-21T00:00` @newhurizons ❤️6956 🔁1115 💬46
  - Someone is using AI to impersonate me 💔#ai#gaming#animalcrossing#creator#content
  - [原文链接](https://twitter.com/newhurizons/status/2024621032422756747)
- `2026-02-21T00:00` @bounty_atm ❤️4370 🔁1993 💬40
  - "지금 난리난" 제미나이 3개월 무료  요약 : 구글 AI 강의 10분 들으면 제미나이 프로 3개월 무료  1. 아래 LINK 접속 2. 'Get Started' 클릭 3. Coursera 에서 강의료 0원 결제 4. 강의 듣기 - 바로 넘기면됨 - 2-2 에서 구독권 링크 나오면 클릭 5. 구독권 등록 6. 강의료/구독권 둘다 자동 결제 해지  * 추후 자동 결제 안되게 등록 후 바로 구독 삭제 필요#gemini#gpt
  - [原文链接](https://twitter.com/bounty_atm/status/2024823621651255501)
- `2026-02-21T00:00` @MikeNellis ❤️4182 🔁1551 💬57
  - Every single Republican president in my lifetime has crashed the economy. Trump is the first to do it twice.
  - [原文链接](https://twitter.com/MikeNellis/status/2024854541221433650)
- `2026-02-21T00:00` @DemocraticWins ❤️4358 🔁1021 💬62
  - BREAKING: Watch the exact moment that Fox News is forced to show their audience the proof that Donald Trump is destroying the economy. Wow.
  - [原文链接](https://twitter.com/DemocraticWins/status/2024859558783426571)
- `2026-02-21T00:00` @NikeiNikeiNiii ❤️2617 🔁1111 💬15
  - hi oomfs. i've been seeing the twitter family and interaction circle trend going around again  DO NOT PARTICIPATE IN THIS TREND. DO NOT CLICK THE LINK. it forces your account to follow bullshit AI and crypto profiles. if you did this trend, CHANGE YOUR PASSWORD ASAP.  stay safe!!
  - [原文链接](https://twitter.com/NikeiNikeiNiii/status/2024792881613897760)
- `2026-02-21T00:00` @NizNellie3 ❤️2401 🔁637 💬27
  - 🚨 Left pic: A 16-year-old in Asheville, N.C., vomiting anti-ICE propaganda, fed to him by adult activists.  Right pic: A violent illegal from Mexico charged with multiple r*pes of a child.  The illegal was arrested by ICE just a few blocks away from this kid’s high school.
  - [原文链接](https://twitter.com/NizNellie3/status/2024650662198313182)
- `2026-02-21T00:00` @GuntherEagleman ❤️2306 🔁656 💬78
  - 🚨White House CONFIRMS, Democrats and Chuck Schumer straight-up SABOTAGED the economy by yanking -2 percentage points off GDP, tanking it to a pathetic 1.4% instead of the roaring 3%+ it should've been!
  - [原文链接](https://twitter.com/GuntherEagleman/status/2024856986441994564)
- `2026-02-21T00:00` @Amockx2022 ❤️1552 🔁345 💬14
  - Sandeep Chaudhary 🔥 : If Youth Congress protest is national shame then what was Galgotia robot at AI summit?  BJP spokie : It was mistake done by Galgotia   Sandeep Chaudhary 😂 : Who gave permission to Galgotia for putting stall?   BJP spokie : 🤐
  - [原文链接](https://twitter.com/Amockx2022/status/2024904423223558587)
- `2026-02-21T00:00` @Dev_Fadnavis ❤️910 🔁875 💬111
  - येत्या काळात महाराष्ट्र सर्व क्षेत्रात 'AI' सज्ज असेल!  आने वाले समय में महाराष्ट्र सभी क्षेत्रों में 'AI' सक्षम होगा!  (नवी दिल्ली \| 20-2-2026)#NewDelhi#AIImpactSummit#IndiaAIImpactSummit2026
  - [原文链接](https://twitter.com/Dev_Fadnavis/status/2024746356016107729)
- `2026-02-21T00:00` @JethmalaniM ❤️1291 🔁483 💬113
  - National Shame.  At the India AI Impact Summit, when India is hosting global leaders, Congress chose crass gutter politics over dignity. Rahul Gandhi’s ecosystem sent Youth Congress workers to go topless, storm the venue, raise slogans and create a spectacle designed for one purpose: to embarrass India on the world stage.  High time to call out the deeper instinct: the Gandhi pariwaar & their lackeys has historically thrived when India is kept small in ambition and low in expectations - a perman
  - [原文链接](https://twitter.com/JethmalaniM/status/2024768920566288878)
- `2026-02-21T00:00` @Juliedonuts ❤️1202 🔁337 💬50
  - You know this ENDS THE FED right?   You know this is coming right?  You know it is THE TRUMP ADMINISTRATION bringing us HONEST MONEY right? 😏🔥🔥  HOLD THE LINE GUYS! 👏🏻🙌🏻
  - [原文链接](https://twitter.com/Juliedonuts/status/2024907633526702423)
- `2026-02-21T00:00` @Grummz ❤️1192 🔁120 💬127
  - Until game companies start putting gamers back in charge of gaming, it will never be fixed.  Microsoft’s new CEO of Xbox has no game experience, ran AI, at MS, was COO of Instacart, and head of messaging at Meta.  The problem is games require a game product focused CEO.  This is Xbox’s John Scully moment, who was a Pepsi exec brought in to run Apple and who ousted Jobs.  How’d that work out? Apple nearly died, and they had to beg Jobs to come back.
  - [原文链接](https://twitter.com/Grummz/status/2024978891300110719)
- `2026-02-21T00:00` @Croesus_BTC ❤️1082 🔁215 💬90
  - This is the Bitcoin/Gold chart - currently lowest RSI in history.  Bitcoin peaked relative to Gold in Dec 2024.  We have been in a ~14 month bear market ever since.  Prior major bear markets: - April 2021 to June 2022 = 14 months  - Dec 2017 to Feb 2019 = 14 months - Nov 2013 to Jan 2015 = 14 months  The current prevailing view seems to be that because we had a Bitcoin all-time-high (in dollars) in Oct 2025, that we are just a few months in to a bear market.  But that ATH may have been just beca
  - [原文链接](https://twitter.com/Croesus_BTC/status/2024875126194319809)
- `2026-02-21T00:00` @CAgovernor ❤️824 🔁131 💬419
  - Bay Area transit is essential to California's economy, workforce, and climate goals.  That's why I'm authorizing a $590 million loan to help stabilize Bay Area transit services as ridership continues to recover from the pandemic.
  - [原文链接](https://twitter.com/CAgovernor/status/2024629690892214363)

### @business (10 条)

- `2026-02-20T23:54` Canada’s aviation regulator issued certificates for some Gulfstream jet models after President Donald Trump complained the country had “refused” to greenlight the aircraft and threatened tariffs and other measures in retaliation https://www.bloomberg.com/news/articles/2026-02-20/canada-approves-some
  - [原文链接](https://twitter.com/business/status/2024996028080898211)
- `2026-02-20T23:46` Detroit’s automakers asked the White House to shield them from new tariffs that President Trump vowed to impose after the Supreme Court struck down most of his global duties https://www.bloomberg.com/news/articles/2026-02-20/detroit-automakers-ask-white-house-to-be-spared-from-new-tariffs?taid=6998f
  - [原文链接](https://twitter.com/business/status/2024994100588564989)
- `2026-02-20T23:21` OpenAI is projecting that its revenue will grow at a fast clip in the next few years and exceed $280 billion in 2030, according to a person familiar with the matter. https://www.bloomberg.com/news/articles/2026-02-20/openai-forecasts-its-revenue-will-top-280-billion-in-2030?taid=6998ec5d8e21f400010d
  - [原文链接](https://twitter.com/business/status/2024987684532277571)
- `2026-02-20T22:55` .http://localhost/sarahsholder talks to the CEO who took his case against tariffs all the way to the Supreme Court — and asks SCOTUS reporter Greg Stohr and global trade editor Brendan Murray what’s next http://bit.ly/4c1Or7a  Video
  - [原文链接](https://twitter.com/business/status/2024981146199638372)
- `2026-02-20T22:52` President Donald Trump took the Supreme Court’s tariffs ruling personally, and he made it personal in response https://www.bloomberg.com/news/articles/2026-02-20/reeling-from-tariff-ruling-trump-lobs-insults-at-supreme-court?taid=6998e59572357e0001315889&utm_campaign=trueanthem&utm_content=business&
  - [原文链接](https://twitter.com/business/status/2024980404478853506)
- *... 及其他 5 条*

### @DeItaone (10 条)

- `2026-02-20T23:42` TRUMP: HAVE JUST SIGNED, FROM OVAL OFFICE, A GLOBAL 10% TARIFF ON ALL COUNTRIES
  - [原文链接](https://twitter.com/DeItaone/status/2024993146489217198)
- `2026-02-20T19:28` VANCE ON SUPREME COURT RULING ON TARIFFS: "THIS IS LAWLESSNESS FROM THE COURT, PLAIN AND SIMPLE"
  - [原文链接](https://twitter.com/DeItaone/status/2024929047029993704)
- `2026-02-20T19:14` BESSENT IN PREPARED REMARKS: TREASURY'S ESTIMATES SHOW THAT USE OF SECTION 122 AUTHORITY, COMBINED WITH POTENTIALLY ENHANCED SECTION 232 AND SECTION 301 TARIFFS WILL RESULT IN VIRTUALLY UNCHANGED TARIFF REVENUE IN 2026
  - [原文链接](https://twitter.com/DeItaone/status/2024925572216803545)
- `2026-02-20T19:03` TRUMP: EUROPE IS GETTING KILLED ON ENERGY AND IMMIGRATION
  - [原文链接](https://twitter.com/DeItaone/status/2024922944481206426)
- `2026-02-20T19:03` TRUMP: 'YOU'RE GOING TO FIND OUT' ABOUT FOREIGN INFLUENCE ON SUPREME COURT
  - [原文链接](https://twitter.com/DeItaone/status/2024922867255681265)
- *... 及其他 5 条*

### @ReutersWorld (10 条)

- `2026-02-20T23:40` Attackers kill at least 50, abduct women and children in Nigeria's Zamfara state http://reut.rs/4b0rRe2 http://reut.rs/4b0rRe2
  - [原文链接](https://twitter.com/ReutersWorld/status/2024992516085297176)
- `2026-02-20T22:30` North Korea's Kim reviews country's progress at key party congress http://reut.rs/4kOtqzg http://reut.rs/4kOtqzg
  - [原文链接](https://twitter.com/ReutersWorld/status/2024975078027309188)
- `2026-02-20T21:40` IOC boss Coventry hails Milano Cortina Games as success http://reut.rs/46fg2Oz http://reut.rs/46fg2Oz
  - [原文链接](https://twitter.com/ReutersWorld/status/2024962368497721589)
- `2026-02-20T20:30` Two youths arrested as France says it has foiled planned attack http://reut.rs/3ZNkws4 http://reut.rs/3ZNkws4
  - [原文链接](https://twitter.com/ReutersWorld/status/2024944889792741471)
- `2026-02-20T19:40` Norway set new gold medal record at Winter Games with 17 after biathlon win http://reut.rs/3OCBPtn http://reut.rs/3OCBPtn
  - [原文链接](https://twitter.com/ReutersWorld/status/2024932152048078848)
- *... 及其他 5 条*

### @karpathy (1 条)

- `2026-02-20T23:18` Bought a new Mac mini to properly tinker with claws over the weekend. The apple store person told me they are selling like hotcakes and everyone is confused :)  I'm definitely a bit sus'd to run OpenClaw specifically - giving my private data/keys to 400K lines of vibe coded monster that is being act
  - [原文链接](https://twitter.com/karpathy/status/2024987174077432126)

### @ReutersBiz (10 条)

- `2026-02-20T23:10` WATCH: The US Supreme Court ruling that struck down President Trump's global tariff policy may, at best, bring a 'slow, gradual' decline to US consumer prices, if it occurs at all, said Anna Rathbun, founder and CEO of Grenadilla Advisory  Video
  - [原文链接](https://twitter.com/ReutersBiz/status/2024984912634487213)
- `2026-02-20T21:43` VIDEO CORRECTION: Munich-based robotics firm RobCo raised $100 million from investors, including Volkswagen's venture arm and Lingotto Innovation, to expand in the US and develop its ‘physical AI’ robotic arms. We are deleting a video containing an incorrect company name  Video
  - [原文链接](https://twitter.com/ReutersBiz/status/2024963262585139405)
- `2026-02-20T19:45` German finance minister calls talk of ECB president succession 'speculation' http://reut.rs/4qRE0qC http://reut.rs/4qRE0qC
  - [原文链接](https://twitter.com/ReutersBiz/status/2024933387161534484)
- `2026-02-20T19:30` Canada December retail sales down 0.4%; seen up 1.5% in January http://reut.rs/4aZCm1b http://reut.rs/4aZCm1b
  - [原文链接](https://twitter.com/ReutersBiz/status/2024929775773528267)
- `2026-02-20T19:00` WATCH: US economic growth slowed more than expected in the fourth quarter amid disruptions from last year's government shutdown and moderate consumer spending, but tax cuts and investment in AI were expected to support activity this year https://reut.rs/4kOBYWH  Video
  - [原文链接](https://twitter.com/ReutersBiz/status/2024922000104313106)
- *... 及其他 5 条*

### @TheInformation (10 条)

- `2026-02-20T22:48` Exclusive: OpenAI has boosted its revenue forecasts while predicting $112 billion more cash burn through 2030.  Read more from http://localhost/srimuppidi and http://localhost/stephpalazzolo 👇   https://thein.fo/4s7mlwe
  - [原文链接](https://twitter.com/TheInformation/status/2024979458139037715)
- `2026-02-20T22:00` AI chatbots are a threat to Pinterest and Reddit, Senior Editor http://localhost/meredithmazz explains.  “Pinterest is a place you go for ideas and inspiration.”  “I think that's something that a chatbot can kind of step on the toes of ... a chatbot to curate these kinds of things for you.”  Video
  - [原文链接](https://twitter.com/TheInformation/status/2024967467353698393)
- `2026-02-20T21:45` If SpaceX goes public, should more IPO shares go to everyday investors or institutions? https://thein.fo/4aVl05G
  - [原文链接](https://twitter.com/TheInformation/status/2024963538561728871)
- `2026-02-20T21:30` A new longevity experiment is mitochondrial transplants.   "The way it works right now is they are having a family member donate blood, a young family member, because the idea is as you age, your mitochondria don't work as well." — http://localhost/AmyDMarcus, Health and Science Reporte  Video
  - [原文链接](https://twitter.com/TheInformation/status/2024959891538911327)
- `2026-02-20T21:12` The Big Read: Silicon Valley is pouring billions into longevity. One startup is already testing mitochondrial transplants on paying patients—including a 91-year-old. https://thein.fo/4ay8BmI
  - [原文链接](https://twitter.com/TheInformation/status/2024955237870506016)
- *... 及其他 5 条*

### @WuBlockchain (7 条)

- `2026-02-20T22:00` Vitalik on What Cypherpunk Is  On January 27, Ethereum founder Vitalik Buterin stated at the ETH ChiangMai togETHer Tuesday event that the cypherpunk movement emerged as early as the 1980s and 1990s, initially focusing on privacy-preserving technologies such as digital cash and encrypted communicati
  - [原文链接](https://twitter.com/WuBlockchain/status/2024967307085168759)
- `2026-02-20T19:00` Eric Trump: Being Besieged and De-platformed Strengthens My Belief in Crypto's Future  On October 27, Eric Trump, the second son of Donald Trump, said in an interview on The Iced Coffee Hour that Bitcoin as "digital gold" is already a settled fact. He asserted that the SWIFT system will disappear, f
  - [原文链接](https://twitter.com/WuBlockchain/status/2024922004697006559)
- `2026-02-20T15:55` The Netherlands regulator has banned Polymarket from offering its prediction market services in the country, ruling that the platform’s contracts constitute illegal gambling under Dutch law. The authority said operators must comply with local licensing requirements or cease operations in the jurisdi
  - [原文链接](https://twitter.com/WuBlockchain/status/2024875524976238848)
- `2026-02-20T14:36` According to CryptoRank, the Trump family meme tokens TRUMP and MELANIA have fallen 92% and 99% from their respective all-time highs. Insiders reportedly earned over $600 million through fees and token sales, while 45 whale wallets realized a combined $1.2 billion in gains. Nearly 2 million retail w
  - [原文链接](https://twitter.com/WuBlockchain/status/2024855698199224691)
- `2026-02-20T13:53` Fourth-quarter U.S. GDP up 1.4%, badly missing estimate. Economists surveyed by Dow Jones had been looking for a 2.5% gain. For the full year in 2025, the U.S. economy grew at a 2.2% pace, down from the 2.8% increase in 2024.
  - [原文链接](https://twitter.com/WuBlockchain/status/2024844756325409212)
- *... 及其他 2 条*

### @PeterSchiff (10 条)

- `2026-02-20T21:05` The big winners today were gold and silver. Gold is up over $100, a 2% gain, while silver is up almost $6, a 7.5% gain. All of this trade uncertainty will drive more money out of U.S. dollars and into precious metals. Make this trade yourself today. http://www.schiffgold.com
  - [原文链接](https://twitter.com/PeterSchiff/status/2024953545036800113)
- `2026-02-20T20:35` Friday Gold Wrap podcast today LIVE at 4:30pm EST  https://piped.video/live/27TttT-5scQ?utm_source=twitter&utm_medium=Peter+Schiff&utm_campaign=publer
  - [原文链接](https://twitter.com/PeterSchiff/status/2024945961160638514)
- `2026-02-20T18:48` No country has been ripping off America. We rip off the world by exchanging our fiat money for the consumer goods our trading partners produce. Let’s see what happens to America when all those consumer goods stop coming in and all of our inflation stays within our own borders.
  - [原文链接](https://twitter.com/PeterSchiff/status/2024919066398326801)
- `2026-02-20T18:32` Trump brags that the Dow rose about 12% since he took office just over a year ago, about 40% less than the rise during Biden’s first year. According to Trump, this 12% gain should have taken four years. Meanwhile, just about every stock market in the world has gained much more.
  - [原文链接](https://twitter.com/PeterSchiff/status/2024914984270995533)
- `2026-02-20T17:40` Last June, we featured a silver mining company in our investment research newsletter Strategic Assets. It had just restructured its debt, was profitable, and was trading at a fraction of what it was worth. It returned over 10x in eight months.  We closed the position recently — locking in extraordin
  - [原文链接](https://twitter.com/PeterSchiff/status/2024902044738338816)
- *... 及其他 5 条*

### @QuantaMagazine (6 条)

- `2026-02-20T20:45` Symmetry has long been a guide for mathematicians, but sometimes the most beautiful answer to a problem is not the best answer. In the bubble problem, beauty and symmetry have prevailed once more. (From the archive) https://www.quantamagazine.org/monumental-math-proof-solves-triple-bubble-problem-an
  - [原文链接](https://twitter.com/QuantaMagazine/status/2024948465491398793)
- `2026-02-20T20:31` At the subatomic scale, things only make sense from a quantum perspective. How do those rules make the leap to classical physics, the macro language of everyday life?   https://www.quantamagazine.org/are-the-mysteries-of-quantum-mechanics-beginning-to-dissolve-20260213/
  - [原文链接](https://twitter.com/QuantaMagazine/status/2024944903222956328)
- `2026-02-20T20:06` For over 30 years, complexity theorists have identified problems where quantum computers surpass classical ones. But there's a broader class of problems that they've barely begun to study, whose inputs and outputs aren't ordinary strings of bits, but are themselves inherently quantum.  https://www.q
  - [原文链接](https://twitter.com/QuantaMagazine/status/2024938642808983978)
- `2026-02-20T15:13` Forget the textbook view of a cell as a calm, orderly place. Glowing trackers reveal that it is jam-packed as a crowded nightclub — raising questions about how molecules can encounter their partners for the reactions that enable life. https://www.quantamagazine.org/the-biophysical-world-inside-a-jam
  - [原文链接](https://twitter.com/QuantaMagazine/status/2024864921607938524)
- `2026-02-20T15:13` The original version of this post featured an incorrect version of this video. We have reposted here with the correct version.
  - [原文链接](https://twitter.com/QuantaMagazine/status/2024864923382116595)
- *... 及其他 1 条*

### @swyx (5 条)

- `2026-02-20T20:07` in 2026 you no longer have an excuse to have a slow ass website. one prompt and 38-56% better LCP, FCP, and Speed Index  as the youtube fengshui guy would say, "FIX IT"  (this cost 5 mins and like $5. felt great)
  - [原文链接](https://twitter.com/swyx/status/2024939066803061104)
- `2026-02-20T19:57` The higher tiers of AI psychosis are incompatible with today’s “App Store”
  - [原文链接](https://twitter.com/swyx/status/2024936435816796165)
- `2026-02-20T17:27` ok day 2 for http://localhost/sama is looking much better better. glad he stayed behind a bit to talk to the little folk  https://piped.video/embed/qH7thwrCluM
  - [原文链接](https://twitter.com/swyx/status/2024898670781759563)
- `2026-02-20T15:29` Takeaways from my talk with http://localhost/swyx, http://localhost/FanaHOVA, and http://localhost/martin_casado about frontier labs, AGI, coding agents, the new capital flywheel, talent wars, and more:  Latent.Space (@latentspacepod)  From pioneering software-defined networking to backing many of t
  - [原文链接](https://twitter.com/swyx/status/2024868959225594171)
- `2026-02-20T15:07` http://x.com/i/article/2024567292856807424
  - [原文链接](https://twitter.com/swyx/status/2024863500468629584)

### @AP (6 条)

- `2026-02-20T18:53` President Trump says he'll sign an executive order to enact a 10% global tariff after the Supreme Court defeat. https://apnews.com/live/supreme-court-tariff-ruling-updates
  - [原文链接](https://twitter.com/AP/status/2024920255726784543)
- `2026-02-20T18:38` LIVE UPDATES: President Trump says he's "absolutely ashamed" of the Supreme Court justices who issued "deeply disappointing" tariff decision. https://apnews.com/live/supreme-court-tariff-ruling-updates
  - [原文链接](https://twitter.com/AP/status/2024916464176693474)
- `2026-02-20T15:08` BREAKING: The Supreme Court strikes down President Trump’s sweeping tariffs, upending the central plank of his economic agenda. Follow the latest updates.  https://apnews.com/live/trump-iran-nuclear-deal-2-20-2026
  - [原文链接](https://twitter.com/AP/status/2024863744111558840)
- `2026-02-20T14:15` BREAKING: Norway breaks the record for most gold medals won by a nation in a single Winter Olympics as biathlete Johannes Dale-Skjevdal wins its 17th. https://apnews.com/article/winter-olympics-norway-gold-record-biathlon-8d64eaeceeaf2d94e36df59d8d204639?utm_campaign=trueAnthem%3A+New+Content+%28Fee
  - [原文链接](https://twitter.com/AP/status/2024850465310101636)
- `2026-02-20T13:58` BREAKING: The U.S. economy's growth slowed in the final three months of 2025 after a robust expansion, the Commerce Department reported. https://apnews.com/article/gdp-economy-consumer-shutdown-immigration-0e5caca783b93eaf2231496e3e0f54f3?utm_campaign=trueAnthem%3A+New+Content+%28Feed%29&utm_medium=
  - [原文链接](https://twitter.com/AP/status/2024846079426994380)
- *... 及其他 1 条*

### @ylecun (1 条)

- `2026-02-20T12:47` Trump sought deep cuts to the EPA, HUD, CDC, NIH, and more. Congress by and large left spending levels unchanged.  My http://localhost/Morning_Joe Chart
  - [原文链接](https://twitter.com/ylecun/status/2024828207619326409)

## 📱 微信公众号

暂无数据

## 🔥 NewsNow 热榜 (120 条)

### 百度热搜

| 排名 | 标题 |
|------|------|
| #1 | [第4金！王心迪夺男子空中技巧冠军](https://www.baidu.com/s?wd=%E7%AC%AC4%E9%87%91%EF%BC%81%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%A4%BA%E7%94%B7%E5%AD%90%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E5%86%A0%E5%86%9B) |
| #2 | [王心迪徐梦桃夫妻双双夺金](https://www.baidu.com/s?wd=%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83%E5%A4%AB%E5%A6%BB%E5%8F%8C%E5%8F%8C%E5%A4%BA%E9%87%91) |
| #3 | [“变成中国人”在中国过春节](https://www.baidu.com/s?wd=%E2%80%9C%E5%8F%98%E6%88%90%E4%B8%AD%E5%9B%BD%E4%BA%BA%E2%80%9D%E5%9C%A8%E4%B8%AD%E5%9B%BD%E8%BF%87%E6%98%A5%E8%8A%82) |
| #4 | [返乡年轻人“挤爆”县城酒店](https://www.baidu.com/s?wd=%E8%BF%94%E4%B9%A1%E5%B9%B4%E8%BD%BB%E4%BA%BA%E2%80%9C%E6%8C%A4%E7%88%86%E2%80%9D%E5%8E%BF%E5%9F%8E%E9%85%92%E5%BA%97) |
| #5 | [全能型强冷空气来了](https://www.baidu.com/s?wd=%E5%85%A8%E8%83%BD%E5%9E%8B%E5%BC%BA%E5%86%B7%E7%A9%BA%E6%B0%94%E6%9D%A5%E4%BA%86) |
| #6 | [今日“破五” 朱广权送你20个财](https://www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E2%80%9C%E7%A0%B4%E4%BA%94%E2%80%9D+%E6%9C%B1%E5%B9%BF%E6%9D%83%E9%80%81%E4%BD%A020%E4%B8%AA%E8%B4%A2) |
| #7 | [王心迪夺冠后回应“家庭地位”](https://www.baidu.com/s?wd=%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%A4%BA%E5%86%A0%E5%90%8E%E5%9B%9E%E5%BA%94%E2%80%9C%E5%AE%B6%E5%BA%AD%E5%9C%B0%E4%BD%8D%E2%80%9D) |
| #8 | [李天马获自由式滑雪空中技巧铜牌](https://www.baidu.com/s?wd=%E6%9D%8E%E5%A4%A9%E9%A9%AC%E8%8E%B7%E8%87%AA%E7%94%B1%E5%BC%8F%E6%BB%91%E9%9B%AA%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E9%93%9C%E7%89%8C) |
| #9 | [小伙撕去年对联天塌了](https://www.baidu.com/s?wd=%E5%B0%8F%E4%BC%99%E6%92%95%E5%8E%BB%E5%B9%B4%E5%AF%B9%E8%81%94%E5%A4%A9%E5%A1%8C%E4%BA%86) |
| #10 | [孙佳旭赛后久久掩面哭泣](https://www.baidu.com/s?wd=%E5%AD%99%E4%BD%B3%E6%97%AD%E8%B5%9B%E5%90%8E%E4%B9%85%E4%B9%85%E6%8E%A9%E9%9D%A2%E5%93%AD%E6%B3%A3) |

### 贴吧

| 排名 | 标题 |
|------|------|
| #1 | [初中生扶老人被索赔22w](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%88%9D%E4%B8%AD%E7%94%9F%E6%89%B6%E8%80%81%E4%BA%BA%E8%A2%AB%E7%B4%A2%E8%B5%9422w&topic_id=28350810) |
| #2 | [港人偷拍同胞,阴阳国人没素质](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B8%AF%E4%BA%BA%E5%81%B7%E6%8B%8D%E5%90%8C%E8%83%9E%2C%E9%98%B4%E9%98%B3%E5%9B%BD%E4%BA%BA%E6%B2%A1%E7%B4%A0%E8%B4%A8&topic_id=28350812) |
| #3 | [金牌夫妻!王心迪徐梦桃顶峰相见](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%BB%21%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83%E9%A1%B6%E5%B3%B0%E7%9B%B8%E8%A7%81&topic_id=28350813) |
| #4 | [老外栽跟头,约会华人遭敲诈](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%80%81%E5%A4%96%E6%A0%BD%E8%B7%9F%E5%A4%B4%2C%E7%BA%A6%E4%BC%9A%E5%8D%8E%E4%BA%BA%E9%81%AD%E6%95%B2%E8%AF%88&topic_id=28350814) |
| #5 | [台媒酸了:春晚机器人是合成](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%8F%B0%E5%AA%92%E9%85%B8%E4%BA%86%3A%E6%98%A5%E6%99%9A%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%98%AF%E5%90%88%E6%88%90&topic_id=28350811) |
| #6 | [哲伟捕虾,猎鹰止步八强](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%93%B2%E4%BC%9F%E6%8D%95%E8%99%BE%2C%E7%8C%8E%E9%B9%B0%E6%AD%A2%E6%AD%A5%E5%85%AB%E5%BC%BA&topic_id=28350809) |
| #7 | [难绷,孙吧黄牌成时尚单品](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%9A%BE%E7%BB%B7%2C%E5%AD%99%E5%90%A7%E9%BB%84%E7%89%8C%E6%88%90%E6%97%B6%E5%B0%9A%E5%8D%95%E5%93%81&topic_id=28350798) |
| #8 | [萝莉反派登场,痴汉狂欢](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%90%9D%E8%8E%89%E5%8F%8D%E6%B4%BE%E7%99%BB%E5%9C%BA%2C%E7%97%B4%E6%B1%89%E7%8B%82%E6%AC%A2&topic_id=28350803) |
| #9 | [新年红包13元,男友抠到没边](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%96%B0%E5%B9%B4%E7%BA%A2%E5%8C%8513%E5%85%83%2C%E7%94%B7%E5%8F%8B%E6%8A%A0%E5%88%B0%E6%B2%A1%E8%BE%B9&topic_id=28350800) |
| #10 | [机器人太秀,白皮转行喷环保](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%A4%AA%E7%A7%80%2C%E7%99%BD%E7%9A%AE%E8%BD%AC%E8%A1%8C%E5%96%B7%E7%8E%AF%E4%BF%9D&topic_id=28350801) |

### bilibili 热搜

| 排名 | 标题 |
|------|------|
| #1 | [2026春晚Remix](https://search.bilibili.com/all?keyword=2026%E6%98%A5%E6%99%9ARemix) |
| #2 | [王心迪男子空中技巧夺金](https://search.bilibili.com/all?keyword=%E7%8E%8B%E5%BF%83%E8%BF%AA%E7%94%B7%E5%AD%90%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E5%A4%BA%E9%87%91) |
| #3 | [十五五开局之年的经济布局](https://search.bilibili.com/all?keyword=%E5%8D%81%E4%BA%94%E4%BA%94%E5%BC%80%E5%B1%80%E4%B9%8B%E5%B9%B4%E7%9A%84%E7%BB%8F%E6%B5%8E%E5%B8%83%E5%B1%80) |
| #4 | [年轻人走亲戚的方式](https://search.bilibili.com/all?keyword=%E5%B9%B4%E8%BD%BB%E4%BA%BA%E8%B5%B0%E4%BA%B2%E6%88%9A%E7%9A%84%E6%96%B9%E5%BC%8F) |
| #5 | [美考虑对伊朗有限军事打击](https://search.bilibili.com/all?keyword=%E7%BE%8E%E8%80%83%E8%99%91%E5%AF%B9%E4%BC%8A%E6%9C%97%E6%9C%89%E9%99%90%E5%86%9B%E4%BA%8B%E6%89%93%E5%87%BB) |
| #6 | [机器人复刻成龙醉拳幕后](https://search.bilibili.com/all?keyword=%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%A4%8D%E5%88%BB%E6%88%90%E9%BE%99%E9%86%89%E6%8B%B3%E5%B9%95%E5%90%8E) |
| #7 | [永生风白羽霸气一穿四](https://search.bilibili.com/all?keyword=%E9%A3%8E%E7%99%BD%E7%BE%BD) |
| #8 | [熊出没12年国产动画的逆袭之路](https://search.bilibili.com/all?keyword=%E7%86%8A%E5%87%BA%E6%B2%A112%E5%B9%B4%E5%9B%BD%E4%BA%A7%E5%8A%A8%E7%94%BB%E7%9A%84%E9%80%86%E8%A2%AD%E4%B9%8B%E8%B7%AF) |
| #9 | [安德鲁王子为何被捕](https://search.bilibili.com/all?keyword=%E5%AE%89%E5%BE%B7%E9%B2%81%E7%8E%8B%E5%AD%90%E4%B8%BA%E4%BD%95%E8%A2%AB%E6%8D%95) |
| #10 | [2026春晚超神名场面盘点](https://search.bilibili.com/all?keyword=2026%E6%98%A5%E6%99%9A%E8%B6%85%E7%A5%9E%E5%90%8D%E5%9C%BA%E9%9D%A2%E7%9B%98%E7%82%B9) |

### 财联社热门

| 排名 | 标题 |
|------|------|
| #1 | [中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111) |
| #2 | [原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772) |
| #3 | [黄仁勋：将在3月发布“世界前所未见”的全新芯片](https://www.cls.cn/detail/2291708) |
| #4 | [美股收盘：多重利空压顶华尔街情绪恶化 三大指数集体下跌](https://www.cls.cn/detail/2291935) |
| #5 | [“存储荒”愈演愈烈！三星HBM4据称涨价30% 韩国“芯片双雄”积极扩产](https://www.cls.cn/detail/2291781) |
| #6 | [原油贵金属大幅收涨 消息称美以或将联合袭击伊朗 \| 环球市场](https://www.cls.cn/detail/2291663) |
| #7 | [“马年科技春晚”让买机器人的股民都松了一口气？节前资金已挤入ETF](https://www.cls.cn/detail/2291748) |
| #8 | [美股收盘：“七巨头”集体走高 三大指数齐收涨](https://www.cls.cn/detail/2291660) |
| #9 | [Seedance2.0春晚出圈，AI视频应用浮现哪些风口？](https://www.cls.cn/detail/2291704) |
| #10 | [莫迪举手全场欢呼 两大AI掌门人却各自握拳尴尬对峙](https://www.cls.cn/detail/2291896) |

### 知乎

| 排名 | 标题 |
|------|------|
| #1 | [现在超大城市的人每天的大便去哪里了？](https://www.zhihu.com/question/2004607413769241485) |
| #2 | [为什么古代中国一直没有发现澳大利亚?](https://www.zhihu.com/question/30227588) |
| #3 | [美国最高法院裁定特朗普政府大规模关税政策违法 ，这会带来哪些影响？关税政策会撤回吗？](https://www.zhihu.com/question/2008321129270486041) |
| #4 | [清华学霸俞浩放言要超越马斯克、黄仁勋，并批评马斯克「PUA」，如何评价其言论与商业目标？](https://www.zhihu.com/question/2005421279541483469) |
| #5 | [特斯拉无人驾驶车正式下线，无方向盘、无踏板、无后视镜，能赢得大众信任并走向普及吗？你看好其前景吗？](https://www.zhihu.com/question/2008253352463528326) |
| #6 | [过完年老公不想陪我回娘家，我们在初一晚上吵了一架，他妈妈帮着他说话，我觉得好没意思，想离婚该怎么办？](https://www.zhihu.com/question/2007402053488632974) |
| #7 | [《镖人：风起大漠》路演时吴京说现在培养一个年轻的功夫明星太难了，真的如此吗？为什么这么难？](https://www.zhihu.com/question/2007359346384859639) |
| #8 | [美军在中东集结近 23 年来最大空中兵力，伊朗致信联合国称若遭军事侵略将反击，局势会怎样发展？](https://www.zhihu.com/question/2008093003923808772) |
| #9 | [亲戚一年到头不见一回，一到过年为什么要走亲戚？](https://www.zhihu.com/question/2007029306942059550) |
| #10 | [初五迎财神，如果孩子问「财神真的存在吗」，你会怎么告诉他？](https://www.zhihu.com/question/2005648703763997404) |

### 抖音

| 排名 | 标题 |
|------|------|
| #1 | [美最高法院裁定特朗普关税违法](https://www.douyin.com/hot/2407242) |
| #2 | [王心迪徐梦桃冬奥金牌夫妻档](https://www.douyin.com/hot/2407186) |
| #3 | [春节新能源汽车高速充电大增](https://www.douyin.com/hot/2407147) |
| #4 | [杨婧茹1500米第四](https://www.douyin.com/hot/2407166) |
| #5 | [空中技巧王心迪李天马分获冠季军](https://www.douyin.com/hot/2407057) |
| #6 | [非遗表演才是年味天花板](https://www.douyin.com/hot/2406906) |
| #7 | [我的新年旅行第一站](https://www.douyin.com/hot/2406531) |
| #8 | [富得流油在食物上具象化了](https://www.douyin.com/hot/2406790) |
| #9 | [无论多少岁都是赢的好年纪](https://www.douyin.com/hot/2406941) |
| #10 | [特朗普：将再对全球商品加税10%](https://www.douyin.com/hot/2407264) |

### 今日头条

| 排名 | 标题 |
|------|------|
| #1 | [小镇相亲会女村支书与小伙一见钟情](https://www.toutiao.com/trending/7608141866747953162/) |
| #2 | [王心迪徐梦桃双金夫妻档](https://www.toutiao.com/trending/7608393726502961202/) |
| #3 | [贺新春！“马”不停蹄竞出游](https://www.toutiao.com/trending/7608451069450403891/) |
| #4 | [特朗普称将加征10%全球进口关税](https://www.toutiao.com/trending/7609086732507565587/) |
| #5 | [第4金！王心迪自由式滑雪空中技巧夺冠](https://www.toutiao.com/trending/7608315713584922643/) |
| #6 | [男友第一次上门把准老丈人的车干翻了](https://www.toutiao.com/trending/7608815462302384171/) |
| #7 | [中国婚姻报告2026](https://www.toutiao.com/trending/7608816836171271726/) |
| #8 | [王心迪是哈工大力学专业在读博士生](https://www.toutiao.com/trending/7608953965572558346/) |
| #9 | [沈腾稳坐中国电影票房最高男主演](https://www.toutiao.com/trending/7608049331439534086/) |
| #10 | [大年初五吃饺子你选啥馅料](https://www.toutiao.com/trending/7608825109620621358/) |

### 澎湃新闻

| 排名 | 标题 |
|------|------|
| #1 | [载8名中国游客车辆因冰面破裂沉湖，其中1人逃生7人遇难](https://www.thepaper.cn/newsDetail_forward_32636500) |
| #2 | [第四金！王心迪斩获自由式滑雪男子空中技巧金牌](https://www.thepaper.cn/newsDetail_forward_32636832) |
| #3 | [国务院安委办通报两起烟花爆竹爆燃事故，部署全链条安全监管](https://www.thepaper.cn/newsDetail_forward_32635340) |
| #4 | [年龄最大的中国运动员，徐晓明遗憾未能弥补男子冰壶的遗憾](https://www.thepaper.cn/newsDetail_forward_32631189) |
| #5 | [对谈ZaZaZsu咂咂苏：被王菲选中后，更相信音乐有自己的旅程](https://www.thepaper.cn/newsDetail_forward_32635115) |
| #6 | [韩国前总统尹锡悦就一审被判无期徒刑发表声明：无法接受](https://www.thepaper.cn/newsDetail_forward_32635451) |
| #7 | [有中国公民在奥克兰街头遇袭，我领馆表达严重关切](https://www.thepaper.cn/newsDetail_forward_32634986) |
| #8 | [史上最长春节假期｜假期第六天景区仍然“谁来都得排队”，旅游产品价格“阶梯式回落”](https://www.thepaper.cn/newsDetail_forward_32635815) |
| #9 | [载8名中国游客汽车在贝加尔湖落水，目前仅一名中国游客获救](https://www.thepaper.cn/newsDetail_forward_32636440) |
| #10 | [放马过来，“申”情款待丨这个马年，和鲁迅“搭伙”看电影](https://www.thepaper.cn/newsDetail_forward_32543949) |

### 凤凰网

| 排名 | 标题 |
|------|------|
| #1 | [特朗普：将对全球加征10%的进口关税](https://news.ifeng.com/c/8quuPHVWc4v) |
| #2 | [特朗普确认正在考虑对伊朗进行“有限军事打击”](https://news.ifeng.com/c/8qumlGo0uMH) |
| #3 | [日本一货船与渔船发生相撞，多人死伤](https://news.ifeng.com/c/8qu6fj6FuQy) |
| #4 | [中国再次成为德国最大贸易伙伴](https://news.ifeng.com/c/8quC4QqfJYV) |
| #5 | [高市早苗宣称仍致力于缔结“和平条约”，克宫：不太可能](https://news.ifeng.com/c/8qu7w9eaQzf) |
| #6 | [中国代表重申：日本没资格要求入常](https://news.ifeng.com/c/8qurLBUotqS) |
| #7 | [英政府考虑取消安德鲁的王位继承权](https://news.ifeng.com/c/8qumlGo0uNo) |
| #8 | [特朗普回忆2017年访华经历，赞叹中国仪仗队强大阵容](https://news.ifeng.com/c/8qu28qoqKpX) |
| #9 | [终于，美国开始还钱了](https://news.ifeng.com/c/8qtv0U1LKYV) |
| #10 | [九成议员支持修宪，日本彻底撕掉和平伪装](https://news.ifeng.com/c/8qu28qoqKsI) |

### 微博

| 排名 | 标题 |
|------|------|
| #1 | [迎财神](https://s.weibo.com/weibo?q=%E8%BF%8E%E8%B4%A2%E7%A5%9E) |
| #2 | [金吉莉1500米金牌](https://s.weibo.com/weibo?q=%23%E9%87%91%E5%90%89%E8%8E%891500%E7%B1%B3%E9%87%91%E7%89%8C%23) |
| #3 | [中国非遗给你亿点点震撼](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E9%9D%9E%E9%81%97%E7%BB%99%E4%BD%A0%E4%BA%BF%E7%82%B9%E7%82%B9%E9%9C%87%E6%92%BC%23) |
| #4 | [王心迪夺冠后李天马大喊回家生孩子](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%A4%BA%E5%86%A0%E5%90%8E%E6%9D%8E%E5%A4%A9%E9%A9%AC%E5%A4%A7%E5%96%8A%E5%9B%9E%E5%AE%B6%E7%94%9F%E5%AD%A9%E5%AD%90%23) |
| #5 | [将门毒后不是大ip是巨ip](https://s.weibo.com/weibo?q=%E5%B0%86%E9%97%A8%E6%AF%92%E5%90%8E%E4%B8%8D%E6%98%AF%E5%A4%A7ip%E6%98%AF%E5%B7%A8ip) |
| #6 | [王心迪金牌](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E5%BF%83%E8%BF%AA%E9%87%91%E7%89%8C%23) |
| #7 | [王心迪徐梦桃 金牌夫妻](https://s.weibo.com/weibo?q=%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83+%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%BB) |
| #8 | [中国队男子5000米接力B组第一](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E9%98%9F%E7%94%B7%E5%AD%905000%E7%B1%B3%E6%8E%A5%E5%8A%9BB%E7%BB%84%E7%AC%AC%E4%B8%80%23) |
| #9 | [杨幂无意中摔出来意外的感觉](https://s.weibo.com/weibo?q=%E6%9D%A8%E5%B9%82%E6%97%A0%E6%84%8F%E4%B8%AD%E6%91%94%E5%87%BA%E6%9D%A5%E6%84%8F%E5%A4%96%E7%9A%84%E6%84%9F%E8%A7%89) |
| #10 | [中国短道队结束米兰冬奥征程](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E7%9F%AD%E9%81%93%E9%98%9F%E7%BB%93%E6%9D%9F%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E5%BE%81%E7%A8%8B%23) |

### 华尔街见闻

| 排名 | 标题 |
|------|------|
| #1 | [特朗普全球关税被推翻！美国最高法院裁定违法，超1750亿美元税收面临退款](https://wallstreetcn.com/articles/3765909) |
| #2 | [港股马年首个交易日：恒科指跌超2%，大模型和存储逆势大涨，智谱大涨近43%，机器人概念股爆发](https://wallstreetcn.com/articles/3765892) |
| #3 | [美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8%](https://wallstreetcn.com/articles/3765902) |
| #4 | [华尔街见闻早餐FM-Radio \| 2026年2月20日](https://wallstreetcn.com/articles/3765885) |
| #5 | [日本首相施政演讲：打破“过度财政紧缩”，暂停食品消费税，加大投资AI等产业](https://wallstreetcn.com/articles/3765896) |
| #6 | [港股科技股分化：“AI新贵”受追捧，"变现担忧"拖累互联网巨头](https://wallstreetcn.com/articles/3765898) |
| #7 | [美国四季度GDP仅增1.4%！政府停摆拖累1个百分点，特朗普提前“开火”鲍威尔](https://wallstreetcn.com/articles/3765906) |
| #8 | [“谷歌天团”反击AI泡沫质疑：这是工业革命，但速度快10倍、规模大10倍](https://wallstreetcn.com/articles/3765904) |
| #9 | [一文读懂2026年至今的全球市场：什么在涨？美股为何不行？这种趋势会持续吗？](https://wallstreetcn.com/articles/3765893) |
| #10 | [美联储最青睐的通胀指标超预期！美国12月核心PCE物价指数同比3%](https://wallstreetcn.com/articles/3765907) |

## 🔗 原始链接索引

### 🐦 Twitter 原文 (80/116 条)

- [2026-02-21T00:00 @rickcomenta [热门] | aí vem uns pamonha dizendo que ela é diva por ignorar a doidinha do centro 🤪🤪🤪 se ela não ...](https://twitter.com/rickcomenta/status/2024942662961303868)
- [2026-02-21T00:00 @atrupar [热门] | NEWSMAX: Do you think Jeffrey Epstein killed himself? REP. NANCY MACE: No, absolutely not....](https://twitter.com/atrupar/status/2024466512359154023)
- [2026-02-21T00:00 @Yodobashi_X [热门] | ＼買うなら、Office 2024搭載PC／ 最新のRyzen AI 5 Pro 搭載💻 カフェに映える上質ボディも魅力✨ 見た目も中身も妥協したくない人に👍 DELLのノートPC...](https://twitter.com/Yodobashi_X/status/2024725707725976019)
- [2026-02-21T00:00 @WhiteHouse [热门] | President Donald J. Trump has effectively used TARIFFS over the past year to MAKE AMERICA ...](https://twitter.com/WhiteHouse/status/2024926556880031987)
- [2026-02-21T00:00 @NotAvgLiberal [热门] | MAGA thinks the Epstein Files exonerate Trump. MAGA also believed - They’d get a $5000 DOG...](https://twitter.com/NotAvgLiberal/status/2024648812233363868)
- [2026-02-21T00:00 @RachelReevesMP [热门] | ⬇️ Inflation down ⬇️ Interest rates down ⬇️ Borrowing down ⬆️ Retail sales up ⬆️ UK fastes...](https://twitter.com/RachelReevesMP/status/2024779618587156555)
- [2026-02-21T00:00 @newhurizons [热门] | Someone is using AI to impersonate me 💔#ai#gaming#animalcrossing#creator#content](https://twitter.com/newhurizons/status/2024621032422756747)
- [2026-02-21T00:00 @bounty_atm [热门] | "지금 난리난" 제미나이 3개월 무료 요약 : 구글 AI 강의 10분 들으면 제미나이 프로 3개월 무료 1. 아래 LINK 접속 2. 'Get Started' 클...](https://twitter.com/bounty_atm/status/2024823621651255501)
- [2026-02-21T00:00 @MikeNellis [热门] | Every single Republican president in my lifetime has crashed the economy. Trump is the fir...](https://twitter.com/MikeNellis/status/2024854541221433650)
- [2026-02-21T00:00 @DemocraticWins [热门] | BREAKING: Watch the exact moment that Fox News is forced to show their audience the proof ...](https://twitter.com/DemocraticWins/status/2024859558783426571)
- [2026-02-21T00:00 @NikeiNikeiNiii [热门] | hi oomfs. i've been seeing the twitter family and interaction circle trend going around ag...](https://twitter.com/NikeiNikeiNiii/status/2024792881613897760)
- [2026-02-21T00:00 @NizNellie3 [热门] | 🚨 Left pic: A 16-year-old in Asheville, N.C., vomiting anti-ICE propaganda, fed to him by ...](https://twitter.com/NizNellie3/status/2024650662198313182)
- [2026-02-21T00:00 @GuntherEagleman [热门] | 🚨White House CONFIRMS, Democrats and Chuck Schumer straight-up SABOTAGED the economy by ya...](https://twitter.com/GuntherEagleman/status/2024856986441994564)
- [2026-02-21T00:00 @Amockx2022 [热门] | Sandeep Chaudhary 🔥 : If Youth Congress protest is national shame then what was Galgotia r...](https://twitter.com/Amockx2022/status/2024904423223558587)
- [2026-02-21T00:00 @Dev_Fadnavis [热门] | येत्या काळात महाराष्ट्र सर्व क्षेत्रात 'AI' सज्ज असेल! आने वाले समय में महाराष्ट्र सभी क्ष...](https://twitter.com/Dev_Fadnavis/status/2024746356016107729)
- [2026-02-21T00:00 @JethmalaniM [热门] | National Shame. At the India AI Impact Summit, when India is hosting global leaders, Congr...](https://twitter.com/JethmalaniM/status/2024768920566288878)
- [2026-02-21T00:00 @Juliedonuts [热门] | You know this ENDS THE FED right? You know this is coming right? You know it is THE TRUMP ...](https://twitter.com/Juliedonuts/status/2024907633526702423)
- [2026-02-21T00:00 @Grummz [热门] | Until game companies start putting gamers back in charge of gaming, it will never be fixed...](https://twitter.com/Grummz/status/2024978891300110719)
- [2026-02-21T00:00 @Croesus_BTC [热门] | This is the Bitcoin/Gold chart - currently lowest RSI in history. Bitcoin peaked relative ...](https://twitter.com/Croesus_BTC/status/2024875126194319809)
- [2026-02-21T00:00 @CAgovernor [热门] | Bay Area transit is essential to California's economy, workforce, and climate goals. That'...](https://twitter.com/CAgovernor/status/2024629690892214363)
- [2026-02-21T00:00 @factpostnews [热门] | New economic data has revealed that inflation increased last month to the highest level in...](https://twitter.com/factpostnews/status/2024859144470069612)
- [2026-02-21T00:00 @RapidResponse47 [热门] | "38% of American families have no exposure to the U.S. stock market... and with@TrumpAccou...](https://twitter.com/RapidResponse47/status/2024958380847095954)
- [2026-02-21T00:00 @CaptMarkKelly [热门] | The Supreme Court’s decision is good news for everyone. Trump’s tariffs are a tax on every...](https://twitter.com/CaptMarkKelly/status/2024924078465830954)
- [2026-02-21T00:00 @Krak [热门] | Ready to Get Krak’d? 💰 This week, we’re giving 2 winners $300 in BTC each. 1️⃣ Follow@Krak...](https://twitter.com/Krak/status/2023530699463041127)
- [2026-02-21T00:00 @cryptofergani [热门] | If you’re 21-35 years old, Pay attention. The next 3-6 months will feel like a money print...](https://twitter.com/cryptofergani/status/2024915703828983906)
- [2026-02-21T00:00 @barkmeta [热门] | Might want to stock up on groceries and fill your gas tank before the market opens Monday....](https://twitter.com/barkmeta/status/2024980940032737675)
- [2026-02-21T00:00 @lingualandjp [热门] | チームみらいは、従来の政党とちがって、「政治コンサル党」みたいなものだろうと思っている。「AIを導入すると、めんどうだった政策がこんなに進みますよ－」みたいな。それ以上の期待はない...](https://twitter.com/lingualandjp/status/2024653448135004319)
- [2026-02-21T00:00 @infodexx [热门] | Cities Leading the AI Investment Race 🤖 1. 🇨🇳 Beijing, China — 66.20% 2. 🇺🇸 Silicon Valley...](https://twitter.com/infodexx/status/2024737266166616233)
- [2026-02-21T00:00 @SecScottBessent [热门] | .@TrumpAccountsgive every American child a stake in our market and our economy. $1,000 inv...](https://twitter.com/SecScottBessent/status/2024994240422416408)
- [2026-02-21T00:00 @DeryaTR_ [热门] | The moment of truth has arrived. The AI takeoff will happen this year. As some of us have ...](https://twitter.com/DeryaTR_/status/2024898630960689494)
- [2026-02-20T23:54 @business [关注] | Canada’s aviation regulator issued certificates for some Gulfstream jet models after Presi...](https://twitter.com/business/status/2024996028080898211)
- [2026-02-20T23:46 @business [关注] | Detroit’s automakers asked the White House to shield them from new tariffs that President ...](https://twitter.com/business/status/2024994100588564989)
- [2026-02-20T23:42 @DeItaone [关注] | TRUMP: HAVE JUST SIGNED, FROM OVAL OFFICE, A GLOBAL 10% TARIFF ON ALL COUNTRIES](https://twitter.com/DeItaone/status/2024993146489217198)
- [2026-02-20T23:40 @ReutersWorld [关注] | Attackers kill at least 50, abduct women and children in Nigeria's Zamfara state http://re...](https://twitter.com/ReutersWorld/status/2024992516085297176)
- [2026-02-20T23:21 @business [关注] | OpenAI is projecting that its revenue will grow at a fast clip in the next few years and e...](https://twitter.com/business/status/2024987684532277571)
- [2026-02-20T23:18 @karpathy [关注] | Bought a new Mac mini to properly tinker with claws over the weekend. The apple store pers...](https://twitter.com/karpathy/status/2024987174077432126)
- [2026-02-20T23:10 @ReutersBiz [关注] | WATCH: The US Supreme Court ruling that struck down President Trump's global tariff policy...](https://twitter.com/ReutersBiz/status/2024984912634487213)
- [2026-02-20T22:55 @business [关注] | .http://localhost/sarahsholder talks to the CEO who took his case against tariffs all the ...](https://twitter.com/business/status/2024981146199638372)
- [2026-02-20T22:52 @business [关注] | President Donald Trump took the Supreme Court’s tariffs ruling personally, and he made it ...](https://twitter.com/business/status/2024980404478853506)
- [2026-02-20T22:50 @business [关注] | The US Supreme Court, given oral arguments in which several justices expressed skepticism ...](https://twitter.com/business/status/2024980123154317500)
- [2026-02-20T22:50 @business [关注] | Netflix co-CEO Ted Sarandos is defending his company’s plans for movies if its acquisition...](https://twitter.com/business/status/2024979908091371677)
- [2026-02-20T22:48 @TheInformation [关注] | Exclusive: OpenAI has boosted its revenue forecasts while predicting $112 billion more cas...](https://twitter.com/TheInformation/status/2024979458139037715)
- [2026-02-20T22:46 @business [关注] | After months of suspense, the US Supreme Court struck down President Donald Trump’s emerge...](https://twitter.com/business/status/2024979015598035082)
- [2026-02-20T22:45 @business [关注] | Blue Owl Capital, facing a looming deadline to return cash in one of its private credit fu...](https://twitter.com/business/status/2024978825625383381)
- [2026-02-20T22:36 @business [关注] | The Supreme Court struck down Trump’s signature tariffs. Here’s how his trade strategy is ...](https://twitter.com/business/status/2024976524340850959)
- [2026-02-20T22:30 @ReutersWorld [关注] | North Korea's Kim reviews country's progress at key party congress http://reut.rs/4kOtqzg ...](https://twitter.com/ReutersWorld/status/2024975078027309188)
- [2026-02-20T22:00 @TheInformation [关注] | AI chatbots are a threat to Pinterest and Reddit, Senior Editor http://localhost/meredithm...](https://twitter.com/TheInformation/status/2024967467353698393)
- [2026-02-20T22:00 @WuBlockchain [关注] | Vitalik on What Cypherpunk Is On January 27, Ethereum founder Vitalik Buterin stated at th...](https://twitter.com/WuBlockchain/status/2024967307085168759)
- [2026-02-20T21:45 @TheInformation [关注] | If SpaceX goes public, should more IPO shares go to everyday investors or institutions? ht...](https://twitter.com/TheInformation/status/2024963538561728871)
- [2026-02-20T21:43 @ReutersBiz [关注] | VIDEO CORRECTION: Munich-based robotics firm RobCo raised $100 million from investors, inc...](https://twitter.com/ReutersBiz/status/2024963262585139405)
- [2026-02-20T21:40 @ReutersWorld [关注] | IOC boss Coventry hails Milano Cortina Games as success http://reut.rs/46fg2Oz http://reut...](https://twitter.com/ReutersWorld/status/2024962368497721589)
- [2026-02-20T21:30 @TheInformation [关注] | A new longevity experiment is mitochondrial transplants. "The way it works right now is th...](https://twitter.com/TheInformation/status/2024959891538911327)
- [2026-02-20T21:12 @TheInformation [关注] | The Big Read: Silicon Valley is pouring billions into longevity. One startup is already te...](https://twitter.com/TheInformation/status/2024955237870506016)
- [2026-02-20T21:05 @PeterSchiff [关注] | The big winners today were gold and silver. Gold is up over $100, a 2% gain, while silver ...](https://twitter.com/PeterSchiff/status/2024953545036800113)
- [2026-02-20T21:00 @TheInformation [关注] | Is AI truly a threat to the software sector? Evan Skorpen, Partner at http://localhost/Lea...](https://twitter.com/TheInformation/status/2024952380173787583)
- [2026-02-20T20:45 @QuantaMagazine [关注] | Symmetry has long been a guide for mathematicians, but sometimes the most beautiful answer...](https://twitter.com/QuantaMagazine/status/2024948465491398793)
- [2026-02-20T20:45 @TheInformation [关注] | AI coding agents are moving from copilots to autonomous builders — and that shift could up...](https://twitter.com/TheInformation/status/2024948446159921345)
- [2026-02-20T20:35 @TheInformation [关注] | OpenAI is developing a family of new hardware devices. Details on the first release: "Basi...](https://twitter.com/TheInformation/status/2024946101552374034)
- [2026-02-20T20:35 @PeterSchiff [关注] | Friday Gold Wrap podcast today LIVE at 4:30pm EST https://piped.video/live/27TttT-5scQ?utm...](https://twitter.com/PeterSchiff/status/2024945961160638514)
- [2026-02-20T20:31 @QuantaMagazine [关注] | At the subatomic scale, things only make sense from a quantum perspective. How do those ru...](https://twitter.com/QuantaMagazine/status/2024944903222956328)
- [2026-02-20T20:30 @ReutersWorld [关注] | Two youths arrested as France says it has foiled planned attack http://reut.rs/3ZNkws4 htt...](https://twitter.com/ReutersWorld/status/2024944889792741471)
- [2026-02-20T20:15 @TheInformation [关注] | As adoption surges, a question emerges: does the do-it-yourself CEO accelerate innovation ...](https://twitter.com/TheInformation/status/2024940888065998925)
- [2026-02-20T20:07 @swyx [关注] | in 2026 you no longer have an excuse to have a slow ass website. one prompt and 38-56% bet...](https://twitter.com/swyx/status/2024939066803061104)
- [2026-02-20T20:06 @QuantaMagazine [关注] | For over 30 years, complexity theorists have identified problems where quantum computers s...](https://twitter.com/QuantaMagazine/status/2024938642808983978)
- [2026-02-20T19:57 @swyx [关注] | The higher tiers of AI psychosis are incompatible with today’s “App Store”](https://twitter.com/swyx/status/2024936435816796165)
- [2026-02-20T19:45 @ReutersBiz [关注] | German finance minister calls talk of ECB president succession 'speculation' http://reut.r...](https://twitter.com/ReutersBiz/status/2024933387161534484)
- [2026-02-20T19:45 @TheInformation [关注] | AI data centers are now 10x larger than traditional facilities, and the executives who can...](https://twitter.com/TheInformation/status/2024933347672183147)
- [2026-02-20T19:40 @ReutersWorld [关注] | Norway set new gold medal record at Winter Games with 17 after biathlon win http://reut.rs...](https://twitter.com/ReutersWorld/status/2024932152048078848)
- [2026-02-20T19:30 @ReutersBiz [关注] | Canada December retail sales down 0.4%; seen up 1.5% in January http://reut.rs/4aZCm1b htt...](https://twitter.com/ReutersBiz/status/2024929775773528267)
- [2026-02-20T19:30 @ReutersWorld [关注] | Attackers kill at least 50, abduct women and children in Nigeria's Zamfara state http://re...](https://twitter.com/ReutersWorld/status/2024929741858382046)
- [2026-02-20T19:28 @DeItaone [关注] | VANCE ON SUPREME COURT RULING ON TARIFFS: "THIS IS LAWLESSNESS FROM THE COURT, PLAIN AND S...](https://twitter.com/DeItaone/status/2024929047029993704)
- [2026-02-20T19:14 @DeItaone [关注] | BESSENT IN PREPARED REMARKS: TREASURY'S ESTIMATES SHOW THAT USE OF SECTION 122 AUTHORITY, ...](https://twitter.com/DeItaone/status/2024925572216803545)
- [2026-02-20T19:03 @DeItaone [关注] | TRUMP: EUROPE IS GETTING KILLED ON ENERGY AND IMMIGRATION](https://twitter.com/DeItaone/status/2024922944481206426)
- [2026-02-20T19:03 @DeItaone [关注] | TRUMP: 'YOU'RE GOING TO FIND OUT' ABOUT FOREIGN INFLUENCE ON SUPREME COURT](https://twitter.com/DeItaone/status/2024922867255681265)
- [2026-02-20T19:00 @DeItaone [关注] | TRUMP: IRAN BETTER NEGOTIATE A FAIR DEAL](https://twitter.com/DeItaone/status/2024922205746811229)
- [2026-02-20T19:00 @WuBlockchain [关注] | Eric Trump: Being Besieged and De-platformed Strengthens My Belief in Crypto's Future On O...](https://twitter.com/WuBlockchain/status/2024922004697006559)
- [2026-02-20T19:00 @ReutersBiz [关注] | WATCH: US economic growth slowed more than expected in the fourth quarter amid disruptions...](https://twitter.com/ReutersBiz/status/2024922000104313106)
- [2026-02-20T18:59 @DeItaone [关注] | TRUMP SAYS NOTHING CHANGES ON INDIA TRAD DEAL](https://twitter.com/DeItaone/status/2024921774610129369)
- [2026-02-20T18:58 @DeItaone [关注] | TRUMP SAYS SOME TRADE DEALS NEGOTIATED UNDER IEEPA DON'T STAND](https://twitter.com/DeItaone/status/2024921716078588415)
- [2026-02-20T18:55 @DeItaone [关注] | TRUMP: 'WE HAVE A VERY INCOMPETENT FED CHAIRMAN WHO LIKES HIGH INTEREST RATES'](https://twitter.com/DeItaone/status/2024920739749450110)

### 📱 微信公众号原文 (0/0 条)

- 暂无可用链接

### 🔥 NewsNow 原文 (120/120 条)

- [百度热搜 #1 | 第4金！王心迪夺男子空中技巧冠军](https://www.baidu.com/s?wd=%E7%AC%AC4%E9%87%91%EF%BC%81%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%A4%BA%E7%94%B7%E5%AD%90%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E5%86%A0%E5%86%9B)
- [贴吧 #1 | 初中生扶老人被索赔22w](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%88%9D%E4%B8%AD%E7%94%9F%E6%89%B6%E8%80%81%E4%BA%BA%E8%A2%AB%E7%B4%A2%E8%B5%9422w&topic_id=28350810)
- [bilibili 热搜 #1 | 2026春晚Remix](https://search.bilibili.com/all?keyword=2026%E6%98%A5%E6%99%9ARemix)
- [财联社热门 #1 | 中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111)
- [知乎 #1 | 现在超大城市的人每天的大便去哪里了？](https://www.zhihu.com/question/2004607413769241485)
- [抖音 #1 | 美最高法院裁定特朗普关税违法](https://www.douyin.com/hot/2407242)
- [今日头条 #1 | 小镇相亲会女村支书与小伙一见钟情](https://www.toutiao.com/trending/7608141866747953162/)
- [澎湃新闻 #1 | 载8名中国游客车辆因冰面破裂沉湖，其中1人逃生7人遇难](https://www.thepaper.cn/newsDetail_forward_32636500)
- [凤凰网 #1 | 特朗普：将对全球加征10%的进口关税](https://news.ifeng.com/c/8quuPHVWc4v)
- [微博 #1 | 迎财神](https://s.weibo.com/weibo?q=%E8%BF%8E%E8%B4%A2%E7%A5%9E)
- [华尔街见闻 #1 | 特朗普全球关税被推翻！美国最高法院裁定违法，超1750亿美元税收面临退款](https://wallstreetcn.com/articles/3765909)
- [华尔街见闻 #2 | 港股马年首个交易日：恒科指跌超2%，大模型和存储逆势大涨，智谱大涨近43%，机器人概念股爆发](https://wallstreetcn.com/articles/3765892)
- [财联社热门 #2 | 原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772)
- [bilibili 热搜 #2 | 王心迪男子空中技巧夺金](https://search.bilibili.com/all?keyword=%E7%8E%8B%E5%BF%83%E8%BF%AA%E7%94%B7%E5%AD%90%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E5%A4%BA%E9%87%91)
- [百度热搜 #2 | 王心迪徐梦桃夫妻双双夺金](https://www.baidu.com/s?wd=%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83%E5%A4%AB%E5%A6%BB%E5%8F%8C%E5%8F%8C%E5%A4%BA%E9%87%91)
- [今日头条 #2 | 王心迪徐梦桃双金夫妻档](https://www.toutiao.com/trending/7608393726502961202/)
- [抖音 #2 | 王心迪徐梦桃冬奥金牌夫妻档](https://www.douyin.com/hot/2407186)
- [凤凰网 #2 | 特朗普确认正在考虑对伊朗进行“有限军事打击”](https://news.ifeng.com/c/8qumlGo0uMH)
- [微博 #2 | 金吉莉1500米金牌](https://s.weibo.com/weibo?q=%23%E9%87%91%E5%90%89%E8%8E%891500%E7%B1%B3%E9%87%91%E7%89%8C%23)
- [澎湃新闻 #2 | 第四金！王心迪斩获自由式滑雪男子空中技巧金牌](https://www.thepaper.cn/newsDetail_forward_32636832)
- [贴吧 #2 | 港人偷拍同胞,阴阳国人没素质](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B8%AF%E4%BA%BA%E5%81%B7%E6%8B%8D%E5%90%8C%E8%83%9E%2C%E9%98%B4%E9%98%B3%E5%9B%BD%E4%BA%BA%E6%B2%A1%E7%B4%A0%E8%B4%A8&topic_id=28350812)
- [知乎 #2 | 为什么古代中国一直没有发现澳大利亚?](https://www.zhihu.com/question/30227588)
- [澎湃新闻 #3 | 国务院安委办通报两起烟花爆竹爆燃事故，部署全链条安全监管](https://www.thepaper.cn/newsDetail_forward_32635340)
- [贴吧 #3 | 金牌夫妻!王心迪徐梦桃顶峰相见](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%BB%21%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83%E9%A1%B6%E5%B3%B0%E7%9B%B8%E8%A7%81&topic_id=28350813)
- [抖音 #3 | 春节新能源汽车高速充电大增](https://www.douyin.com/hot/2407147)
- [微博 #3 | 中国非遗给你亿点点震撼](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E9%9D%9E%E9%81%97%E7%BB%99%E4%BD%A0%E4%BA%BF%E7%82%B9%E7%82%B9%E9%9C%87%E6%92%BC%23)
- [百度热搜 #3 | “变成中国人”在中国过春节](https://www.baidu.com/s?wd=%E2%80%9C%E5%8F%98%E6%88%90%E4%B8%AD%E5%9B%BD%E4%BA%BA%E2%80%9D%E5%9C%A8%E4%B8%AD%E5%9B%BD%E8%BF%87%E6%98%A5%E8%8A%82)
- [今日头条 #3 | 贺新春！“马”不停蹄竞出游](https://www.toutiao.com/trending/7608451069450403891/)
- [财联社热门 #3 | 黄仁勋：将在3月发布“世界前所未见”的全新芯片](https://www.cls.cn/detail/2291708)
- [凤凰网 #3 | 日本一货船与渔船发生相撞，多人死伤](https://news.ifeng.com/c/8qu6fj6FuQy)
- [bilibili 热搜 #3 | 十五五开局之年的经济布局](https://search.bilibili.com/all?keyword=%E5%8D%81%E4%BA%94%E4%BA%94%E5%BC%80%E5%B1%80%E4%B9%8B%E5%B9%B4%E7%9A%84%E7%BB%8F%E6%B5%8E%E5%B8%83%E5%B1%80)
- [知乎 #3 | 美国最高法院裁定特朗普政府大规模关税政策违法 ，这会带来哪些影响？关税政策会撤回吗？](https://www.zhihu.com/question/2008321129270486041)
- [华尔街见闻 #3 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8%](https://wallstreetcn.com/articles/3765902)
- [凤凰网 #4 | 中国再次成为德国最大贸易伙伴](https://news.ifeng.com/c/8quC4QqfJYV)
- [澎湃新闻 #4 | 年龄最大的中国运动员，徐晓明遗憾未能弥补男子冰壶的遗憾](https://www.thepaper.cn/newsDetail_forward_32631189)
- [bilibili 热搜 #4 | 年轻人走亲戚的方式](https://search.bilibili.com/all?keyword=%E5%B9%B4%E8%BD%BB%E4%BA%BA%E8%B5%B0%E4%BA%B2%E6%88%9A%E7%9A%84%E6%96%B9%E5%BC%8F)
- [百度热搜 #4 | 返乡年轻人“挤爆”县城酒店](https://www.baidu.com/s?wd=%E8%BF%94%E4%B9%A1%E5%B9%B4%E8%BD%BB%E4%BA%BA%E2%80%9C%E6%8C%A4%E7%88%86%E2%80%9D%E5%8E%BF%E5%9F%8E%E9%85%92%E5%BA%97)
- [财联社热门 #4 | 美股收盘：多重利空压顶华尔街情绪恶化 三大指数集体下跌](https://www.cls.cn/detail/2291935)
- [华尔街见闻 #4 | 华尔街见闻早餐FM-Radio | 2026年2月20日](https://wallstreetcn.com/articles/3765885)
- [知乎 #4 | 清华学霸俞浩放言要超越马斯克、黄仁勋，并批评马斯克「PUA」，如何评价其言论与商业目标？](https://www.zhihu.com/question/2005421279541483469)
- [今日头条 #4 | 特朗普称将加征10%全球进口关税](https://www.toutiao.com/trending/7609086732507565587/)
- [抖音 #4 | 杨婧茹1500米第四](https://www.douyin.com/hot/2407166)
- [微博 #4 | 王心迪夺冠后李天马大喊回家生孩子](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%A4%BA%E5%86%A0%E5%90%8E%E6%9D%8E%E5%A4%A9%E9%A9%AC%E5%A4%A7%E5%96%8A%E5%9B%9E%E5%AE%B6%E7%94%9F%E5%AD%A9%E5%AD%90%23)
- [贴吧 #4 | 老外栽跟头,约会华人遭敲诈](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%80%81%E5%A4%96%E6%A0%BD%E8%B7%9F%E5%A4%B4%2C%E7%BA%A6%E4%BC%9A%E5%8D%8E%E4%BA%BA%E9%81%AD%E6%95%B2%E8%AF%88&topic_id=28350814)
- [抖音 #5 | 空中技巧王心迪李天马分获冠季军](https://www.douyin.com/hot/2407057)
- [今日头条 #5 | 第4金！王心迪自由式滑雪空中技巧夺冠](https://www.toutiao.com/trending/7608315713584922643/)
- [贴吧 #5 | 台媒酸了:春晚机器人是合成](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%8F%B0%E5%AA%92%E9%85%B8%E4%BA%86%3A%E6%98%A5%E6%99%9A%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%98%AF%E5%90%88%E6%88%90&topic_id=28350811)
- [凤凰网 #5 | 高市早苗宣称仍致力于缔结“和平条约”，克宫：不太可能](https://news.ifeng.com/c/8qu7w9eaQzf)
- [澎湃新闻 #5 | 对谈ZaZaZsu咂咂苏：被王菲选中后，更相信音乐有自己的旅程](https://www.thepaper.cn/newsDetail_forward_32635115)
- [微博 #5 | 将门毒后不是大ip是巨ip](https://s.weibo.com/weibo?q=%E5%B0%86%E9%97%A8%E6%AF%92%E5%90%8E%E4%B8%8D%E6%98%AF%E5%A4%A7ip%E6%98%AF%E5%B7%A8ip)
- [财联社热门 #5 | “存储荒”愈演愈烈！三星HBM4据称涨价30% 韩国“芯片双雄”积极扩产](https://www.cls.cn/detail/2291781)
- [华尔街见闻 #5 | 日本首相施政演讲：打破“过度财政紧缩”，暂停食品消费税，加大投资AI等产业](https://wallstreetcn.com/articles/3765896)
- [bilibili 热搜 #5 | 美考虑对伊朗有限军事打击](https://search.bilibili.com/all?keyword=%E7%BE%8E%E8%80%83%E8%99%91%E5%AF%B9%E4%BC%8A%E6%9C%97%E6%9C%89%E9%99%90%E5%86%9B%E4%BA%8B%E6%89%93%E5%87%BB)
- [百度热搜 #5 | 全能型强冷空气来了](https://www.baidu.com/s?wd=%E5%85%A8%E8%83%BD%E5%9E%8B%E5%BC%BA%E5%86%B7%E7%A9%BA%E6%B0%94%E6%9D%A5%E4%BA%86)
- [知乎 #5 | 特斯拉无人驾驶车正式下线，无方向盘、无踏板、无后视镜，能赢得大众信任并走向普及吗？你看好其前景吗？](https://www.zhihu.com/question/2008253352463528326)
- [微博 #6 | 王心迪金牌](https://s.weibo.com/weibo?q=%23%E7%8E%8B%E5%BF%83%E8%BF%AA%E9%87%91%E7%89%8C%23)
- [抖音 #6 | 非遗表演才是年味天花板](https://www.douyin.com/hot/2406906)
- [知乎 #6 | 过完年老公不想陪我回娘家，我们在初一晚上吵了一架，他妈妈帮着他说话，我觉得好没意思，想离婚该怎么办？](https://www.zhihu.com/question/2007402053488632974)
- [澎湃新闻 #6 | 韩国前总统尹锡悦就一审被判无期徒刑发表声明：无法接受](https://www.thepaper.cn/newsDetail_forward_32635451)
- [贴吧 #6 | 哲伟捕虾,猎鹰止步八强](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%93%B2%E4%BC%9F%E6%8D%95%E8%99%BE%2C%E7%8C%8E%E9%B9%B0%E6%AD%A2%E6%AD%A5%E5%85%AB%E5%BC%BA&topic_id=28350809)
- [今日头条 #6 | 男友第一次上门把准老丈人的车干翻了](https://www.toutiao.com/trending/7608815462302384171/)
- [财联社热门 #6 | 原油贵金属大幅收涨 消息称美以或将联合袭击伊朗 | 环球市场](https://www.cls.cn/detail/2291663)
- [华尔街见闻 #6 | 港股科技股分化：“AI新贵”受追捧，"变现担忧"拖累互联网巨头](https://wallstreetcn.com/articles/3765898)
- [bilibili 热搜 #6 | 机器人复刻成龙醉拳幕后](https://search.bilibili.com/all?keyword=%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%A4%8D%E5%88%BB%E6%88%90%E9%BE%99%E9%86%89%E6%8B%B3%E5%B9%95%E5%90%8E)
- [凤凰网 #6 | 中国代表重申：日本没资格要求入常](https://news.ifeng.com/c/8qurLBUotqS)
- [百度热搜 #6 | 今日“破五” 朱广权送你20个财](https://www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E2%80%9C%E7%A0%B4%E4%BA%94%E2%80%9D+%E6%9C%B1%E5%B9%BF%E6%9D%83%E9%80%81%E4%BD%A020%E4%B8%AA%E8%B4%A2)
- [微博 #7 | 王心迪徐梦桃 金牌夫妻](https://s.weibo.com/weibo?q=%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83+%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%BB)
- [贴吧 #7 | 难绷,孙吧黄牌成时尚单品](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%9A%BE%E7%BB%B7%2C%E5%AD%99%E5%90%A7%E9%BB%84%E7%89%8C%E6%88%90%E6%97%B6%E5%B0%9A%E5%8D%95%E5%93%81&topic_id=28350798)
- [澎湃新闻 #7 | 有中国公民在奥克兰街头遇袭，我领馆表达严重关切](https://www.thepaper.cn/newsDetail_forward_32634986)
- [抖音 #7 | 我的新年旅行第一站](https://www.douyin.com/hot/2406531)
- [财联社热门 #7 | “马年科技春晚”让买机器人的股民都松了一口气？节前资金已挤入ETF](https://www.cls.cn/detail/2291748)
- [百度热搜 #7 | 王心迪夺冠后回应“家庭地位”](https://www.baidu.com/s?wd=%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%A4%BA%E5%86%A0%E5%90%8E%E5%9B%9E%E5%BA%94%E2%80%9C%E5%AE%B6%E5%BA%AD%E5%9C%B0%E4%BD%8D%E2%80%9D)
- [bilibili 热搜 #7 | 永生风白羽霸气一穿四](https://search.bilibili.com/all?keyword=%E9%A3%8E%E7%99%BD%E7%BE%BD)
- [今日头条 #7 | 中国婚姻报告2026](https://www.toutiao.com/trending/7608816836171271726/)
- [凤凰网 #7 | 英政府考虑取消安德鲁的王位继承权](https://news.ifeng.com/c/8qumlGo0uNo)
- [华尔街见闻 #7 | 美国四季度GDP仅增1.4%！政府停摆拖累1个百分点，特朗普提前“开火”鲍威尔](https://wallstreetcn.com/articles/3765906)
- [知乎 #7 | 《镖人：风起大漠》路演时吴京说现在培养一个年轻的功夫明星太难了，真的如此吗？为什么这么难？](https://www.zhihu.com/question/2007359346384859639)
- [今日头条 #8 | 王心迪是哈工大力学专业在读博士生](https://www.toutiao.com/trending/7608953965572558346/)
- [百度热搜 #8 | 李天马获自由式滑雪空中技巧铜牌](https://www.baidu.com/s?wd=%E6%9D%8E%E5%A4%A9%E9%A9%AC%E8%8E%B7%E8%87%AA%E7%94%B1%E5%BC%8F%E6%BB%91%E9%9B%AA%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E9%93%9C%E7%89%8C)
- [抖音 #8 | 富得流油在食物上具象化了](https://www.douyin.com/hot/2406790)
- [贴吧 #8 | 萝莉反派登场,痴汉狂欢](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%90%9D%E8%8E%89%E5%8F%8D%E6%B4%BE%E7%99%BB%E5%9C%BA%2C%E7%97%B4%E6%B1%89%E7%8B%82%E6%AC%A2&topic_id=28350803)
- [凤凰网 #8 | 特朗普回忆2017年访华经历，赞叹中国仪仗队强大阵容](https://news.ifeng.com/c/8qu28qoqKpX)
- [知乎 #8 | 美军在中东集结近 23 年来最大空中兵力，伊朗致信联合国称若遭军事侵略将反击，局势会怎样发展？](https://www.zhihu.com/question/2008093003923808772)
- [财联社热门 #8 | 美股收盘：“七巨头”集体走高 三大指数齐收涨](https://www.cls.cn/detail/2291660)
- [澎湃新闻 #8 | 史上最长春节假期｜假期第六天景区仍然“谁来都得排队”，旅游产品价格“阶梯式回落”](https://www.thepaper.cn/newsDetail_forward_32635815)
- [bilibili 热搜 #8 | 熊出没12年国产动画的逆袭之路](https://search.bilibili.com/all?keyword=%E7%86%8A%E5%87%BA%E6%B2%A112%E5%B9%B4%E5%9B%BD%E4%BA%A7%E5%8A%A8%E7%94%BB%E7%9A%84%E9%80%86%E8%A2%AD%E4%B9%8B%E8%B7%AF)
- [华尔街见闻 #8 | “谷歌天团”反击AI泡沫质疑：这是工业革命，但速度快10倍、规模大10倍](https://wallstreetcn.com/articles/3765904)
- [微博 #8 | 中国队男子5000米接力B组第一](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E9%98%9F%E7%94%B7%E5%AD%905000%E7%B1%B3%E6%8E%A5%E5%8A%9BB%E7%BB%84%E7%AC%AC%E4%B8%80%23)
- [澎湃新闻 #9 | 载8名中国游客汽车在贝加尔湖落水，目前仅一名中国游客获救](https://www.thepaper.cn/newsDetail_forward_32636440)
- [贴吧 #9 | 新年红包13元,男友抠到没边](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%96%B0%E5%B9%B4%E7%BA%A2%E5%8C%8513%E5%85%83%2C%E7%94%B7%E5%8F%8B%E6%8A%A0%E5%88%B0%E6%B2%A1%E8%BE%B9&topic_id=28350800)
- [抖音 #9 | 无论多少岁都是赢的好年纪](https://www.douyin.com/hot/2406941)
- [凤凰网 #9 | 终于，美国开始还钱了](https://news.ifeng.com/c/8qtv0U1LKYV)
- [百度热搜 #9 | 小伙撕去年对联天塌了](https://www.baidu.com/s?wd=%E5%B0%8F%E4%BC%99%E6%92%95%E5%8E%BB%E5%B9%B4%E5%AF%B9%E8%81%94%E5%A4%A9%E5%A1%8C%E4%BA%86)
- [今日头条 #9 | 沈腾稳坐中国电影票房最高男主演](https://www.toutiao.com/trending/7608049331439534086/)
- [华尔街见闻 #9 | 一文读懂2026年至今的全球市场：什么在涨？美股为何不行？这种趋势会持续吗？](https://wallstreetcn.com/articles/3765893)
- [财联社热门 #9 | Seedance2.0春晚出圈，AI视频应用浮现哪些风口？](https://www.cls.cn/detail/2291704)
- [微博 #9 | 杨幂无意中摔出来意外的感觉](https://s.weibo.com/weibo?q=%E6%9D%A8%E5%B9%82%E6%97%A0%E6%84%8F%E4%B8%AD%E6%91%94%E5%87%BA%E6%9D%A5%E6%84%8F%E5%A4%96%E7%9A%84%E6%84%9F%E8%A7%89)
- [bilibili 热搜 #9 | 安德鲁王子为何被捕](https://search.bilibili.com/all?keyword=%E5%AE%89%E5%BE%B7%E9%B2%81%E7%8E%8B%E5%AD%90%E4%B8%BA%E4%BD%95%E8%A2%AB%E6%8D%95)
- [知乎 #9 | 亲戚一年到头不见一回，一到过年为什么要走亲戚？](https://www.zhihu.com/question/2007029306942059550)
- [bilibili 热搜 #10 | 2026春晚超神名场面盘点](https://search.bilibili.com/all?keyword=2026%E6%98%A5%E6%99%9A%E8%B6%85%E7%A5%9E%E5%90%8D%E5%9C%BA%E9%9D%A2%E7%9B%98%E7%82%B9)
- [贴吧 #10 | 机器人太秀,白皮转行喷环保](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%A4%AA%E7%A7%80%2C%E7%99%BD%E7%9A%AE%E8%BD%AC%E8%A1%8C%E5%96%B7%E7%8E%AF%E4%BF%9D&topic_id=28350801)
- [百度热搜 #10 | 孙佳旭赛后久久掩面哭泣](https://www.baidu.com/s?wd=%E5%AD%99%E4%BD%B3%E6%97%AD%E8%B5%9B%E5%90%8E%E4%B9%85%E4%B9%85%E6%8E%A9%E9%9D%A2%E5%93%AD%E6%B3%A3)
- [凤凰网 #10 | 九成议员支持修宪，日本彻底撕掉和平伪装](https://news.ifeng.com/c/8qu28qoqKsI)
- [今日头条 #10 | 大年初五吃饺子你选啥馅料](https://www.toutiao.com/trending/7608825109620621358/)
- [财联社热门 #10 | 莫迪举手全场欢呼 两大AI掌门人却各自握拳尴尬对峙](https://www.cls.cn/detail/2291896)
- [知乎 #10 | 初五迎财神，如果孩子问「财神真的存在吗」，你会怎么告诉他？](https://www.zhihu.com/question/2005648703763997404)
- [华尔街见闻 #10 | 美联储最青睐的通胀指标超预期！美国12月核心PCE物价指数同比3%](https://wallstreetcn.com/articles/3765907)
- [微博 #10 | 中国短道队结束米兰冬奥征程](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E7%9F%AD%E9%81%93%E9%98%9F%E7%BB%93%E6%9D%9F%E7%B1%B3%E5%85%B0%E5%86%AC%E5%A5%A5%E5%BE%81%E7%A8%8B%23)
- [抖音 #10 | 特朗普：将再对全球商品加税10%](https://www.douyin.com/hot/2407264)
- [澎湃新闻 #10 | 放马过来，“申”情款待丨这个马年，和鲁迅“搭伙”看电影](https://www.thepaper.cn/newsDetail_forward_32543949)
- [抖音 #11 | 解放军有效处置美军在黄海活动](https://www.douyin.com/hot/2406645)
- [贴吧 #11 | 叒开战?米库对线不消停](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%8F%92%E5%BC%80%E6%88%98%3F%E7%B1%B3%E5%BA%93%E5%AF%B9%E7%BA%BF%E4%B8%8D%E6%B6%88%E5%81%9C&topic_id=28350802)
- [凤凰网 #11 | 扎哈罗娃：美国在乌克兰问题上的立场具有双重性](https://news.ifeng.com/c/8qttIC1x9wi)
- [百度热搜 #11 | 春节熬夜“补觉能补回来”是误区](https://www.baidu.com/s?wd=%E6%98%A5%E8%8A%82%E7%86%AC%E5%A4%9C%E2%80%9C%E8%A1%A5%E8%A7%89%E8%83%BD%E8%A1%A5%E5%9B%9E%E6%9D%A5%E2%80%9D%E6%98%AF%E8%AF%AF%E5%8C%BA)
- [今日头条 #11 | 春节“喝酒暖身”是谣言](https://www.toutiao.com/trending/7608765402002063410/)
- [财联社热门 #11 | 美联储纪要曝利率路线裂痕：降息、暂停、加息三派混战](https://www.cls.cn/detail/2291646)
- [bilibili 热搜 #11 | 锐评春节档5部新片](https://search.bilibili.com/all?keyword=%E9%94%90%E8%AF%84%E6%98%A5%E8%8A%82%E6%A1%A35%E9%83%A8%E6%96%B0%E7%89%87)
- [知乎 #11 | 如何看待微软 AI 负责人预测称，「未来 18 个月内，多数白领工作将被 AI 彻底替代」？](https://www.zhihu.com/question/2005731383423824873)
- [微博 #11 | 贝加尔湖事故遇难者遗体被找到](https://s.weibo.com/weibo?q=%23%E8%B4%9D%E5%8A%A0%E5%B0%94%E6%B9%96%E4%BA%8B%E6%95%85%E9%81%87%E9%9A%BE%E8%80%85%E9%81%97%E4%BD%93%E8%A2%AB%E6%89%BE%E5%88%B0%23)
- [澎湃新闻 #11 | 直播回放｜新春“骨力”全开，选对护具不马虎](https://www.thepaper.cn/newsDetail_forward_32540956)

### 💻 GitHub 原文 (20/39 条)

- [openclaw/openclaw | ⭐ 214239 | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/openclaw/openclaw)
- [Significant-Gravitas/AutoGPT | ⭐ 181902 | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission i...](https://github.com/Significant-Gravitas/AutoGPT)
- [n8n-io/n8n | ⭐ 175541 | Fair-code workflow automation platform with native AI capabilities. Combine visual buildin...](https://github.com/n8n-io/n8n)
- [ollama/ollama | ⭐ 163021 | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and othe...](https://github.com/ollama/ollama)
- [huggingface/transformers | ⭐ 156756 | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning model...](https://github.com/huggingface/transformers)
- [f/prompts.chat | ⭐ 145855 | a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. F...](https://github.com/f/prompts.chat)
- [langflow-ai/langflow | ⭐ 144931 | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.](https://github.com/langflow-ai/langflow)
- [langgenius/dify | ⭐ 129874 | Production-ready platform for agentic workflow development.](https://github.com/langgenius/dify)
- [langchain-ai/langchain | ⭐ 127059 | 🦜🔗 The platform for reliable agents.](https://github.com/langchain-ai/langchain)
- [bitcoin/bitcoin | ⭐ 88201 | Bitcoin Core integration/staging tree](https://github.com/bitcoin/bitcoin)
- [tensorflow/tensorflow | ⭐ 193872 | An Open Source Machine Learning Framework for Everyone](https://github.com/tensorflow/tensorflow)
- [ethereum/EIPs | ⭐ 13788 | The Ethereum Improvement Proposal repository](https://github.com/ethereum/EIPs)
- [MystenLabs/sui | ⭐ 7611 | Sui, a next-generation smart contract platform with high throughput, low latency, and an a...](https://github.com/MystenLabs/sui)
- [HKUDS/ClawWork | ⭐ 4564 | "ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"](https://github.com/HKUDS/ClawWork)
- [SeungMaeda/polymarket-copy-bot-ts | ⭐ 852 | Polymarket || Polymarket Bot || Polymarket Copy Bot || Polymarket Copy Trading Bot || Poly...](https://github.com/SeungMaeda/polymarket-copy-bot-ts)
- [nicobailon/visual-explainer | ⭐ 1833 | Agent skill + prompt templates that generate rich HTML pages for visual diff reviews, arch...](https://github.com/nicobailon/visual-explainer)
- [vercel-labs/portless | ⭐ 1805 | Replace port numbers with stable, named .localhost URLs. For humans and agents.](https://github.com/vercel-labs/portless)
- [ebrasha/free-v2ray-public-list | ⭐ 522 | A simple and always-updated list of free, working V2Ray servers. including SS, SSR, Trojan...](https://github.com/ebrasha/free-v2ray-public-list)
- [agenticnotetaking/arscontexta | ⭐ 1273 | Claude Code plugin that generates individualized knowledge systems from conversation. You ...](https://github.com/agenticnotetaking/arscontexta)
- [nullclaw/nullclaw | ⭐ 1163 | Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig](https://github.com/nullclaw/nullclaw)

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

### 🌐 联网检索原文 (14/14 条)

- [2026-02-21 07:48 新浪财经 | 深夜，全线大涨！特朗普，重磅宣布！ - 新浪财经](https://news.google.com/rss/articles/CBMihwJBVV95cUxNLWtLNzhkS0hJTHhmZEtwWEJ0cXUyWlNoNDlwU2U3SEpfdFVEM0gwbmI0Uzlfdi1Qb1RNdWpJNW1TM0NLUjhVLTBOX0xxaG5WNHNSTEVKOG9zNURoMDlWWXFkQ2N4YThvaEF4Z1FfR2NqT3U2SVFMdkRMUDQwd1Rpby1kSFpyX0FxUm9BMHl4cWUzWGVaVkxuRTJlRV9QZzhSRGdxWHVxek9MYzZ5TzVYektUZzRfTDU5VjRvY3hEY01ucjFrUGozUG9oTVBtMlFUREY0dmN3YXZTZ1J1OXh3TnM4VFZxeDJ4YlRESmJBYUNXZktuakMyWjFpM1lMXzRMUTV6dFJUZw?oc=5)
- [2026-02-21 07:35 搜狐网 | 徐梦桃、王心迪，夫妻双双把金夺！ - 搜狐网](https://news.google.com/rss/articles/CBMihwFBVV95cUxQMG1ienBaYVBPX2xEeEx0TWNNNmdPZS0waDBFOGNEWWRwSUxoNVlxbE1fN2hxM29PUW9MRDV0TVN2WUJWTHJxMzZlMkgtUTNvdm5xSXJkaGFUZlF6b1RTdHlKcXoyODYwTVozb1lIMkNqSm9wNGRta1Y4cUVwSWhLbUVkRGZ2cjg?oc=5)
- [2026-02-21 07:31 thepaper.cn | 城市年鉴2025｜制造业降碳：扩大绿电应用，落地能碳平台 - thepaper.cn](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5VNWRMOVNGZzhsZFBJLUswY3Q4X1VaR3pYUHpNU3RHU0t5VEJkbzI4aWtNNVZ1UEEzcW40dWlQeVBLbUxLNkZJck5kaFdvUE1SNXlXektfT21XS1VtcEE?oc=5)
- [2026-02-21 07:15 搜狐网 | “我不能让中国队包揽！”王心迪夺金背后的“集团优势” - 搜狐网](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVFpVMGlSQ0VJdEstT3ptNkFaVWZ5dkFZcmZoSUZnOVJEUnpMUml5TUo3QTR4Vl9peUllNHJNcGNCeE0wb3R0XzAyZVo2ZVZYX2d1aDkxbVhvNEpSQzZoYXd6OWxrNjFnRTRWZE8wenNaeGVIVXB1bVo2TW5JaDRiaG1ETmZlMUVKT3NR?oc=5)
- [2026-02-21 07:15 新浪财经 | 新浪财经隔夜要闻大事汇总：2026年2月21日 - 新浪财经](https://news.google.com/rss/articles/CBMihAFBVV95cUxQY25wdUpCLWtCOUloS2FsaTFna0M1bEZoVTY3aXQ4OUY3WFNOLWFtU2lUMFYzeW8tdTc3RDBYVGF1YXdEeng0bTdZUzdWblhINGVfYnEtSHI5ZWFvOUNmaV9iTjliYTZMR3RDaHlfUTNwRFprdEhtdDdrS1dtTkQ2aUZFVlk?oc=5)
- [2026-02-21 05:30 英为财情 Investing.com | 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5)
- [2026-02-21 04:22 游侠网 | 平博APP - 游侠网](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5qcFhxZnlvS3Jwblh6UEcxcWM4Zkl2aWc5RnlMaEYtc0tlVjVBVHYydEFBTndySWozYnZFekVRUzQzSEtpY0N2YnZsNTBUS0tySld0bQ?oc=5)
- [2026-02-20 19:48 OR新媒体 | OR新媒体| 美股为何如此诡异？ - OR新媒体](https://news.google.com/rss/articles/CBMiREFVX3lxTE9EeFVtMVR6V1p3ckhwSHhLT29tTVZHYkRFcFhNQW5wbU82WEd4eDdfN2FLSkpTaEcyTGJWelF2bWR0ekJf?oc=5)
- [2026-02-20 19:27 中國報 China Press | 2026米兰冬奥｜父因天安门事件被监视 刘美贤花滑逆转夺金 - 中國報 China Press](https://news.google.com/rss/articles/CBMi1AJBVV95cUxQN19rOFNKdzdEaGFEcnFldFFHTmFQWm5VWFhmZEd0RHdpSTBvMjNLcEFOVlpqUFpGQmNVTHJxTnlLZGJYZVRua2NkZTRxbERDSlR1aUkyY3dWdWhMam5aNW5MZVJFSVJNWWtiRUlDWEdZeXdBZ2N4MWsyakZsNmVxWm12NTZnS1Y4Ylg0ZWtqMVNDRWttVVd0Q2E3cXRiSDBVSTBUeGk5U2VQNUFSalJUTE1ZNHBhT1FZSmlVT19qaGNadTFKcllYa0RGNDNzaFRUOFZ0amVZZWV4WHp5MWF0TGRPSTdDTTJBaVZQaEhtYXNGaW1lbkp2VzBjaGp3ZjhxUHJrN2dqLXp3NGpXMF85anZlaWV1c2Y2cUFYWm1WU2RaZFBjbDd3clBsZzIxalE2MTFwekZCRkVFZF9xRFlJOXQ3TVdZTHFrdndRMHFxZk94ZG1z?oc=5)
- [2026-02-20 14:45 Bitget | 美银对较高的股票风险敞口发出逆势“卖出”信号 - Bitget](https://news.google.com/rss/articles/CBMia0FVX3lxTE5LLUpQSDBuUUxLbkRLSDRWRV84VFJ4SmUwSFNJNFNPY0tWbFBweVVDYkF6SG5jZlktZEtsbTc4dWEzU0FrRFdhWnd2WFRMb3FkeWFwVmdGc2t2WkFqTlZ6UmdfZlFqTHBEZmZn0gFrQVVfeXFMTkstSlBIMG5RTEtuREtINFZFXzhUUnhKZTBIU0k0U09jS1ZsUHB5VUNiQXpIbmNmWS1kS2xtNzh1YTNTQWtEV2Fad3ZYVExvcWR5YXBWZ0Zza3ZaQWpOVnpSZ19mUWpMcERmZmc?oc=5)
- [2026-02-20 14:26 World Journal | 閩老婦自摔 初中生去扶竟須負次責、被索賠22萬…網炸鍋 - World Journal](https://news.google.com/rss/articles/CBMihgFBVV95cUxNRnFiV2ZXLVVMbE5RNTJmNWY0TnViRzg0eW1nMGx2YzhFLU9heXFNSXNmU1VQbGcwWldJSFhzWTRISGw4UjZ3RUN1dFdpVGx0VzUwWDhLdElYU2pEbVJmckJSNUttbW8xSmlrWFhCUmFRcTQxSlZGZzJNSHh4WlRFdmRoRUc5d9IBZ0FVX3lxTE03c0E0dkllbzhDUk8yd3dXclJiUm5TbmFkbHZ1U1JQU1hQM09CY3hPajN0MV9TdUl1T0ZLMWlNal9UWXlDX1ZvWlZrX3d2cUF5YjBDV2J5QlJtUFdTV0JZSjRJOG9FQVk?oc=5)
- [2026-02-20 05:30 英为财情 Investing.com | 美国股市收低；截至收盘道琼斯工业平均指数下跌0.54% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE1mLUhCeDg1RGJEWEhwdlA0SkxOQWtoS2kxYzUxQTdYSnZCcTd5SU5USS0tZzZKdFhRb0E0bWZSNGVhR285dGlqNFQ0dDZLTFg0M1VaMWEyVjJ4OWpBV3dNdmJldG5wQlBOc3pzVXZpTkc?oc=5)
- [2026-02-19 22:57 Mix Vale | 由于美伊紧张局势以及沃尔玛和 DoorDash 的盈利好坏参半，美国股市下跌 - Mix Vale](https://news.google.com/rss/articles/CBMi2gJBVV95cUxPcGpzTW5ZSGtwVzlLMVhkanFPR0VoYkFSelFBaU9tdGwtTEd4ajM0NGdMeWxNMXdKb01mZHFXcHJ6a0h4UFdkQzZpODhxenduMlVTSjdjVkNnQV9mQkNjb2pEUkR2ZGMtQTZiTWQwSHVXa0pPWHNZaGU1ZHVJTDFDT2o4MmlFd3lFbTZfYjB2YTAtUjJTUk5McE1HWnBMU3Q4dzB2VTRLZzBNa3c4MVB1M3IyT0drdjlpYzRTYlNJLTlOcU5MMnAyaThYeVV2ZjdpaC1CSTIwckFaQUZ0aXNpYkdzQ0ZtcjBtdlF2c2xHT3dPR0FhY1dhWXRnbmlucl9PSmlOdlJNREJKaW9ndUN0blNFdHE5U3lrT0xheDROWW1MSHd2YXlFTzFJWUVZcGJrMlFPNDFmSmJBZ0lRZXp1UFZGN3VGWHBHcHdiRHEzUlJXWjVhaU1KZFlR0gHfAkFVX3lxTE51dVBBeVJaMGVtVlZaMndmS25SSmNvNEp2d1hxQXNZWXRlLW10Y2FJOWdyLU9FV0UwaDdDcjZ4bzNHS1pfX052ejFIZjFWTHhkbHJmaDBzcWlSRm9Xdi0yNTNjOGJpZ0VMdllNV3FNYVk1MGFDd3p3eU5NQzF3cUlxZVBPdW1rMWFldDB0d2lCQ3NhQ1BrWGRHb2ltWmxRR05FMm9qdFpNSU5pSXFuU3NYQTBkYXYybWg4b2xRTGlPV3k1SmUwSmRYa1hpT1FObHlCXzluVlVfd18zQTYzN3htaTJoYjFyM0daSnhtZW5tUUk3QTFERzdYZjZWTm45VHA3M2RrLThDY0ZpUS1ucWFfVFlZV1pkdjByVU5uRXdNSTI3X09XMVNXV2hVMm55VkFYWGFrRXZaM3JHWTRSR3NHai1zVU05U1dGbmZsTS1HTXlMVmh2ZGdRbVJ6MnZIQQ?oc=5)
- [2026-02-19 18:30 英为财情 Investing.com | 印度股市收低；截至收盘印度S&P CNX NIFTY指数下跌1.41% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTFAwMVNXS0VUVUlITVE0MjBMNkdVVGRyQUZ1a3VxZEtveVhIM3g3VDVDdE1zRWtEU3pPRTl6ZV9QRjRoRUktT000UHNKczRYS1Zha0VJYVNyYVpsS2pmaEF5dUcydE1PQmYwX0pWU3VFVE4?oc=5)

---

*报告由 finradar 自动生成 | 2026-02-21 08:03:08（北京时间）*
