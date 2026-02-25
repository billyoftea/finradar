# 📰 finradar 🌅 早报
**2026-02-22** | 🌅 早报 | 覆盖时段: 昨日20:00 → 今日08:00 | 市场状态: ⚠️ A股休市
生成时间: 2026-02-22 08:03（北京时间）

**⚠️ 注意：今日为周末，A股休市，部分市场数据可能缺失或未更新**

---

## 🚨 数据源健康提醒

1. 检测到微信登录异常：财联社: invalid session。请重新扫码登录 wechat-exporter。
2. 微信登录凭据最近更新已 4.4 天（阈值 4 天），建议尽快重新扫码登录。
3. 本次抓取公众号文章为 0 篇，账号搜索失败占比 100%，请检查登录态或服务状态。

处理建议：
1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。
2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。
3. 然后执行 `./scripts/local.sh report morning 20260222` 与 `./scripts/local.sh notion-push morning 20260222` 覆盖 Notion 页面。

# 🤖 AI 分析摘要

## 一、摘要
- **社会**：国内社会关注点集中于**春节旅游安全事故与公共服务短板**。贝加尔湖7名中国游客溺亡事件细节进一步披露，俄方称其路线未经批准[NW03, WB07]；同时，“前方无厕所、无烤肠、无茶叶蛋”成为热搜，反映景区服务供给不足引发公众共鸣[NW02, NW11]。海外社会信号则聚焦于**美国政治议程与地缘指控**。
- **经济**：**全球贸易政策不确定性仍是核心宏观变量**。美国最高法院否决关税的裁决持续提振市场风险偏好，但潜在的大规模退税（约**1750亿美元**）被解读为对美股的“财政刺激”与对美债的“增加债务”[NW06]。IMF首次指中国产业补贴为宏观失调，引发关注[WB11]。
- **市场**：隔夜（覆盖时段）**美股延续涨势**，核心驱动仍为**关税否决带来的乐观情绪**[WB03, WB06, WB07]。市场呈现**区域分化**：欧美股市（尤其科技股）走强，VIX指数下跌；东亚市场（A股、日股、港股）普遍承压。**贵金属（金银）因滞胀担忧继续大涨**[NW12, WB03]。
- **科技**：AI领域呈现**硬件供应链瓶颈与应用风险并存**。积极信号包括：日本公司Nittobo控制**AI芯片关键材料T-glass 90%份额**，凸显上游垄断风险与投资机会[¹](https://twitter.com/Gaurab/status/2024959539511275769)。风险信号包括：AI技术被指用于选举干预等政治目的[²](https://twitter.com/nikkei/status/2025309061068067168)。

## 二、分板块汇报
### 2.1 市场概况（仅有效交易时段数据）
较上期：**延续了美股上涨、风险情绪改善的格局，但新增了市场区域分化的显著特征**。
**发生了什么**：在覆盖时段内，全球股市呈现**东西分化**。**欧美市场强劲**：美股三大指数收涨（标普500 +0.69%，纳斯达克 +0.90%）[WB04, WB07]，欧洲股市如法国CAC40（+1.39%）、德国DAX（+0.87%）领涨。**亚太市场普遍承压**：A股、日股、港股均下跌超过1%。**VIX波动率指数下跌5.64%**，显示市场恐慌情绪下降。商品方面，COMEX铜上涨1.76%，与风险资产同步；贵金属大涨（黄金重回5100，白银涨8%）[NW12, WB03]。
**为什么会这样（证据强度：高）**：核心驱动仍是**美国最高法院否决关税政策**，这被市场视为消除贸易不确定性的利好，直接提振了风险偏好[WB03, WB06]。证据链清晰：1）政策事件（关税否决）明确；2）市场反应（美股上涨、VIX下跌）同步；3）媒体报道直接归因[WB03, WB06]。东西市场分化可能源于对同一事件的不同解读或区域自身因素，但具体驱动东亚市场下跌的原因数据不足。
**下一步观察**：1）观察**1750亿美元关税退款**的具体执行方案及其对美股流动性、美债供给的实际影响[NW06]。2）跟踪**欧美与东亚市场的分化**是否会收敛，需关注亚太市场是否有新的催化剂。3）监测**贵金属涨势**的持续性，验证其反映的是短期避险还是长期的滞胀交易逻辑。

### 2.2 微信公众号共识与弱信号
数据不足。输入中未提供“微信公众号逐篇简介”或具体文章内容，无法提炼跨公众号共识或弱信号。

### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）
较上期：**延续了AI应用开发平台的热度，金融科技项目聚焦于自动化交易，未发现显著新增趋势**。
最值得关注的项目集中在两个方向：
1.  **AI应用开发与工作流平台**：`langflow-ai/langflow`（构建AI智能体工作流）和`langgenius/dify`（生产就绪的智能体开发平台）持续受到关注。其应用场景在于**降低企业集成和部署AI能力的门槛**，实现业务流程自动化。可落地价值高，是企业进行AI改造的实际工具。但需注意该领域项目（如n8n、AutoGPT）功能存在重叠，存在**同质化竞争和概念过热**的噪音风险。
2.  **金融科技自动化交易**：`nautechsystems/nautilus_trader`（高性能算法交易平台）和`hummingbot/hummingbot`（加密货币交易机器人）是典型代表。应用场景明确，服务于量化交易、做市和套利，**提升交易效率的价值清晰**。风险在于策略的有效性高度依赖市场环境和开发者能力，且加密货币市场波动性大。
3.  **Web3安全工具**：`MetaMask/eth-phishing-detect`（钓鱼域名检测）是生态健康发展的基础设施，落地价值在于**保护用户资产安全**，但项目本身商业想象力有限。

### 2.4 Twitter 海外信号（英文内容中文汇报）
较上期：**新增关于AI硬件供应链关键瓶颈的具体信息，以及更多涉及政治指控的噪音信号**。
基于逐条信息提炼：
1.  **AI硬件供应链出现明确瓶颈**：日本玻璃纤维公司Nittobo控制了**AI芯片基板核心材料T-glass 90%的市场份额**，其价格远高于标准品。英伟达已签订长期合同锁定供应，且新产能2027年前不会到位。包括英伟达、苹果、谷歌在内的多家科技巨头高管曾亲赴日本争取供应[¹](https://twitter.com/Gaurab/status/2024959539511275769)。这是一个高价值的产业信号，揭示了AI算力竞赛中的上游材料垄断风险。
2.  **AI技术被用于地缘政治操作**：日本《日经新闻》报道，在众议院选举期间，约有**400个中国相关账户利用AI进行“反高市早苗工作”**[²](https://twitter.com/nikkei/status/2025309061068067168)。这增加了AI技术滥用的政治风险维度。
3.  **市场情绪与争议性政治指控并存**：有观点援引**韩国在打击裸卖空后股市上涨近150%** 的案例，呼吁美国采取类似行动[³](https://twitter.com/xMarketNews/status/2025296878707913043)。同时，平台出现大量未经证实的、情绪化的政治指控，例如指控伯尼·桑德斯卷入“中国丑闻”[⁴](https://twitter.com/mcafeenew/status/2025280842499531121)，或指控奥巴马伪造“通俄门”[⁵](https://twitter.com/EshaAA33/status/2025147573838000572)。这些属于**高噪音、低证据强度**的信息，投资决策应避免采信。

### 2.5 国内新闻与政策脉络
较上期：**延续了对春节旅游安全事件的关注，并新增对公共服务短板的社会讨论，产业政策方面出现国际机构批评声音**。
- **社会事件持续发酵**：**贝加尔湖7名中国游客溺亡**事件，俄方明确指出其旅游路线“未经批准”[NW03]，这或将引发对境外高风险旅游项目监管的讨论。同时，“**前方无厕所、无烤肠、无茶叶蛋**”成为百度、微博等多平台热搜[NW02, NW11]，这反映了春节假期景区客流超载下的**公共服务供给短板**，可能影响后续旅游消费信心与相关板块预期。
- **经济政策受到国际关注**：**IMF首次指中国产业补贴为“宏观失调”** [WB11]。这一表态可能加剧国际间关于产业政策的争论，并对相关出口行业构成潜在的外部压力，需关注后续官方回应及国际经贸关系变化。
- **机构动向**：财联社报道显示，中国顶流私募在Q4**集体加仓拼多多，且AI投资重心发生转变**[NW05]。这提供了观察头部资金在消费与科技领域配置偏好的微观线索，但具体转向何方数据不足。

## 三、明日跟踪清单
1.  **延续跟进：美国关税退款（1750亿美元）的执行细节与市场影响**：跟踪美国财政部关于退税的具体时间表与规模确认，观察其对美股流动性、美债收益率以及美元汇率的实际影响，评估“财政刺激”与“债务增加”两种叙事何者主导市场。[NW06, WB03]
2.  **收口复盘：韩国股市独立行情（+2.31%）的驱动验证**：结合历史关注，需补充今日韩国市场领涨板块、资金流入（尤其是外资）数据，并与“打击裸卖空”政策效应进行关联分析，判断其上涨的可持续性与独特性。[³](https://twitter.com/xMarketNews/status/2025296878707913043)
3.  **新增观察：AI芯片关键材料（T-glass）供应链紧张态势**：跟踪Nittobo及其竞争对手的产能动态、客户签约情况，以及此事对英伟达等下游客户成本及AI芯片产能规划的潜在影响，挖掘上游材料领域的投资线索。[¹](https://twitter.com/Gaurab/status/2024959539511275769)


---

<details><summary>📑 点击展开各板块详细分析</summary>

### 📊 市场数据详细分析

### 1. 主要市场走势判断
在覆盖时段内，全球股市呈现**区域分化**格局。**亚太市场普遍承压**，其中A股（-1.26%）、日股（-1.12%）和港股（-1.10%）领跌。**欧美市场则表现强劲**，法国CAC40（+1.39%）、韩股（+2.31%）、德国DAX（+0.87%）和美股三大指数（标普500 +0.69%，纳斯达克 +0.90%）均录得上涨。整体来看，市场风险偏好呈现**由东向西转移**的特征。

### 2. 关键资产轮动分析
*   **领涨方向**：
    1.  **欧洲股市**：法国CAC40（+1.39%）和德国DAX（+0.87%）涨幅居前，显示资金在欧洲区域的风险偏好显著提升。具体领涨板块数据未提供。
    2.  **科技成长股**：纳斯达克综合指数（+0.90%）涨幅明显高于道琼斯工业指数（+0.47%）和罗素2000小盘股指数（-0.05%），表明资金在美股内部偏好**大型科技/成长股**。
    3.  **韩国股市**：韩国综合指数（+2.31%）表现异常突出，成为全球主要市场中涨幅最大的标的。具体驱动板块数据未提供。

*   **领跌方向**：
    1.  **东亚股市**：A股、日股、港股同步下跌，显示该区域面临共同的抛售压力或负面情绪。具体领跌板块数据未提供。
    2.  **美股小盘股**：罗素2000指数微跌（-0.05%），与纳斯达克和标普500的上涨形成反差，反映资金在风险偏好提升时，仍更倾向于流动性更好、确定性更高的大盘股，而非对利率更敏感的小盘股。

*   **反映的资金偏好**：资金明显偏好**欧美发达市场**及**大盘科技股**，同时从**东亚市场**流出。这可能反映了对区域经济前景、货币政策或地缘政治风险的差异化定价。**VIX波动率指数下跌5.64%**，与欧美股市上涨同步，印证了覆盖时段内市场整体恐慌情绪下降，风险偏好回升。

### 3. 加密货币和商品期货的关键变化
*   **加密货币**：主流加密货币波动极小，**BTC（+0.04%）、ETH（+0.29%）、SOL（+0.86%）** 均呈微幅上涨，与股市的剧烈分化形成对比，显示该时段内加密市场资金流动平静，未出现明显的风险追逐或规避行为。
*   **商品期货**：
    *   **工业金属**：**COMEX铜（+1.76%）** 显著上涨，其走势与欧洲股市及纳斯达克的强势表现正相关，可能反映了对全球（尤其是欧美）工业需求或经济韧性的乐观预期。
    *   **能源**：**WTI原油（-0.06%）** 与**布伦特原油（+0.14%）** 涨跌互现且幅度极小，市场处于平衡状态。**天然气（+1.70%）** 涨幅相对明显，但具体驱动因素（如天气、库存）数据未提供。
    *   **贵金属**：数据未提供，无法分析。

### 4. 涨跌驱动链条分析
基于现有数据，可梳理出以下部分逻辑链条：

*   **链条一（欧洲股市上涨）**：
    *   **事件/政策/情绪**：数据未提供具体事件。但从**VIX指数显著下跌**可推断，市场整体风险情绪改善。
    *   **资金行为**：资金流入欧洲主要股指（法国、德国），同时流出东亚市场。
    *   **价格表现**：**法国CAC40（+1.39%）、德国DAX（+0.87%）** 领涨欧美股市。**证据强度：中**。有价格表现与资金流向（区域强弱对比）及情绪指标（VIX下跌）的同步性作为证据，但缺乏直接的政策或消息面驱动信息。

*   **链条二（美股内部风格分化）**：
    *   **事件/政策/情绪**：数据未提供。风险情绪改善（VIX下跌）是背景。
    *   **资金行为**：资金在美股内部选择性地流入以科技股为代表的成长型大盘股，而非广泛性地流入小盘股。
    *   **价格表现**：**纳斯达克（+0.90%）> 标普500（+0.69%）> 道指（+0.47%）> 罗素2000（-0.05%）**。**证据强度：强**。指数间的涨跌幅差异清晰反映了这一资金选择行为。

*   **链条三（铜价与风险资产联动）**：
    *   **事件/政策/情绪**：与股市上涨共享相同的宏观情绪背景（经济乐观预期）。
    *   **资金行为**：资金同时流入股市（尤其是欧股、美股科技）和工业金属铜。
    *   **价格表现**：**COMEX铜（+1.76%）** 与欧洲股市、纳斯达克指数同步上涨。**证据强度：中**。存在明确的价格同步相关性，可作为经济乐观情绪在商品端的体现，但具体的供需面证据未提供。

**总结**：覆盖时段内市场的核心特征是**风险情绪回暖（VIX下跌）下的区域与风格再平衡**。资金从东亚撤出，转而流入欧洲和美股大盘科技股，并带动了对经济增长敏感的铜价上涨。加密货币市场表现独立且平静。所有分析均严格基于提供的数据，对于具体的政策消息、板块明细及贵金属表现，目前**数据不足**。

### ⏱ 市场时效过滤说明

市场时效过滤结果：
1. 早报阶段不纳入 A 股盘面，避免使用非交易时段快照

### 🐦 Twitter 逐条简介

Twitter 逐条简介（共 12 条，按互动热度排序）：
1. [热门] @akiko_lawson | 2026-02-22T00:00 | 互动=44468
   原文摘录: 5日間限定の無料券チャレンジ(^^) 今日は冷凍米飯無料の最終日です♪ 1）このアカウントをフォロー 2）この投稿をリポスト 3）抽選で毎日1万名様に無料券！結果は自動でお知らせ
   原文链接: [点击查看原文](https://twitter.com/akiko_lawson/status/2025344790129455528)
   1) 讲了什么：账号发布限时免费券活动，涉及冷冻米饭免费领取。
   2) 关键信号：活动为五天限时，今日是冷冻米饭免费最后一天。
   3) 阅读建议：略读 + 原因：内容为营销推广活动，与金融科技核心关联度低。
2. [热门] @needtheIight | 2026-02-22T00:00 | 互动=31679
   原文摘录: ai lembrando desse print aqui...
   原文链接: [点击查看原文](https://twitter.com/needtheIight/status/2025044319095144644)
   1) 讲了什么：用户分享了一张截图，内容未提供。
   2) 关键信号：推文互动数据高，但截图具体信息数据不足/未提供。
   3) 阅读建议：略读 + 原因：推文本身信息有限，仅提及一张截图。
3. [热门] @TadaaVoila | 2026-02-22T00:00 | 互动=23721
   原文摘录: อย่าเลิกตามการเมืองเด็ดขาด คือพักได้แต่อย่าเลิก อย่าคิดว่าสังคมมันเฮงซวยเหมือนเดิม ถ้าวันนั้นไม่มีใครสนใจการเมืองไม่มีเนติวิทย์ไม่มีนักเรียนเลวเด็กไทยคงได้ตัดผม
   原文链接: [点击查看原文](https://twitter.com/TadaaVoila/status/2025115801377022067)
   1) 讲了什么：推文呼吁不要完全放弃关注政治，认为若无人关心则社会将倒退。
   2) 关键信号：未提供具体金融科技相关信号或数据。
   3) 阅读建议：略读 + 原因：内容为政治社会评论，与金融科技主题无直接关联。
4. [热门] @pupxtra_ | 2026-02-22T00:00 | 互动=18733
   原文摘录: i ♥️ nerds
   原文链接: [点击查看原文](https://twitter.com/pupxtra_/status/2025014218282471547)
   1) 讲了什么：一条推文表达了对“书呆子”的喜爱。
   2) 关键信号：推文互动数据高，但内容与金融科技无关。
   3) 阅读建议：略读。内容仅为个人情感表达，无金融科技信息。
5. [热门] @WhiteHouse | 2026-02-22T00:00 | 互动=11206
   原文摘录: TRUST IN TRUMP 🔥 A busy week at the White House 🕊️ Inaugural Board of Peace 🏭 Georgia Visit on Economy 🍔 The Varsity Stop 🤝 Governors' Breakfast 🇺🇸 Black Histor
   原文链接: [点击查看原文](https://twitter.com/WhiteHouse/status/2025292911903212018)
   1) 讲了什么：白宫账号发布多条活动预告，涵盖和平、经济、贸易、历史纪念等议题。
   2) 关键信号：提及对特朗普的信任、最低抵押贷款利率、印尼贸易协议。
   3) 阅读建议：略读 + 原因：内容为活动预告与议题罗列，无具体政策细节或数据。
6. [热门] @kaaleeby | 2026-02-22T00:00 | 互动=7647
   原文摘录: Ai calica eu grito Ave Maria Ela joga a raba e depois vai pra missa Aí danada, ela não é santa Agora se ajoelha e vou mostrar quem é que manda 🎶
   原文链接: [点击查看原文](https://twitter.com/kaaleeby/status/2025033822920647153)
   1) 讲了什么：用户分享了一段葡萄牙语歌词，内容涉及宗教意象与个人表达。
   2) 关键信号：数据不足/未提供。
   3) 阅读建议：略读，因内容为歌词片段，无明确金融科技信息。
7. [热门] @nikkei | 2026-02-22T00:00 | 互动=5909
   原文摘录: 衆議院選挙、中国系400アカウントが「反高市工作」 AIで巧妙にnikkei.com/article/DGXZTS000…
   原文链接: [点击查看原文](https://twitter.com/nikkei/status/2025309061068067168)
   1) 讲了什么：日本众议院选举期间，中国系账户进行反高市工作，AI技术被巧妙运用。
   2) 关键信号：中国系400账户参与，AI技术被用于选举相关工作。
   3) 阅读建议：精读 + 原因：涉及选举干预和AI技术应用，信息具体且互动量高。
8. [热门] @mcafeenew | 2026-02-22T00:00 | 互动=5592
   原文摘录: 🚨BOMBSHELL ALERT: BERNIE SANDERS EXPOSED IN MASSIVE CHINA SCANDAL! 🔗t.me/+bWjXP07v90xlYWFkNational Intel Agency UNCOVERS SHOCKING SECRET LINKS – Dozens of HIDDE
   原文链接: [点击查看原文](https://twitter.com/mcafeenew/status/2025280842499531121)
   1) 讲了什么：账号称桑德斯卷入中国相关丑闻，涉及隐藏账户和公司。
   2) 关键信号：指控严重但未提供证据，来源为单一电报频道链接。
   3) 阅读建议：略读 + 原因：信息源单一且情绪化，缺乏可验证事实。
9. [热门] @bitget | 2026-02-22T00:00 | 互动=3826
   原文摘录: Level up your trading on Bitget stock perps With ultra-low fees, you can seize every market opportunity Want more? Check out all the features 👇
   原文链接: [点击查看原文](https://twitter.com/bitget/status/2023336325282508801)
   1) 讲了什么：Bitget推广其股票永续合约交易，强调超低费用和把握市场机会。
   2) 关键信号：未提供具体数据或事件，仅为平台功能宣传。
   3) 阅读建议：略读，因内容为常规产品推广，无实质市场信息。
10. [热门] @Gaurab | 2026-02-22T00:00 | 互动=3473
   原文摘录: Nittobo is a Japanese glass fiber company with 2,745 employees. Nvidia, Apple, Google, Amazon, AMD, Microsoft, and Qualcomm have all sent executives to Japan to
   原文链接: [点击查看原文](https://twitter.com/Gaurab/status/2024959539511275769)
   1) 讲了什么：日本玻璃纤维公司Nittobo控制AI芯片基板核心材料T-glass的90%份额，多家科技巨头高管赴日争取供应。
   2) 关键信号：T-glass价格远高于标准品，Nvidia已签订长期合同锁定供应，新产能2027年前不会到位。
   3) 阅读建议：精读。提供了具体公司、市场份额、价格对比和供应约束的关键细节。
11. [热门] @culianax | 2026-02-22T00:00 | 互动=3177
   原文摘录: ai gente 😭😭😭
   原文链接: [点击查看原文](https://twitter.com/culianax/status/2025020394143416385)
   1) 讲了什么：账号@culianax在2026-02-22发布了一条情绪化推文。
   2) 关键信号：推文内容为“ai gente 😭😭😭”，互动数据已提供。
   3) 阅读建议：略读。推文内容简短且无具体金融科技信息。
12. [热门] @EshaAA33 | 2026-02-22T00:00 | 互动=2566
   原文摘录: BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hidden in CIA vault for ~10 years, to undermine Trump’s election via mani
   原文链接: [点击查看原文](https://twitter.com/EshaAA33/status/2025147573838000572)
   1) 讲了什么：一条推文称有情报人员确认奥巴马等人伪造“俄罗斯骗局”以破坏特朗普选举。
   2) 关键信号：未提供具体证据，但呼吁病毒式传播并就是否逮捕奥巴马进行投票。
   3) 阅读建议：略读 + 原因：内容为未经证实的指控，且带有明显煽动性。

### 🌐 Twitter 英文信号详细分析

### 海外英文信号主线
1.  **美国政治经济议程**：信号显示特朗普政府正推动一系列经济与外交议程，包括建立“和平委员会”、访问佐治亚州讨论经济、与州长会晤、庆祝黑人历史月、调整关税、达成与印度尼西亚的贸易协议，并提及自2022年以来的最低抵押贷款利率。同时，有关于为新生儿设立1000美元指数基金投资账户的“变革性”政策讨论。
2.  **金融市场与监管议题**：讨论聚焦于韩国在打击裸卖空后股市大幅上涨的案例，并呼吁美国采取类似行动。市场情绪关注个股极端表现（如PayPal股价在牛市中大跌）和高做空兴趣股票（如Hims & Hers）。此外，有关于内幕交易、技术分析规则和比特币价格可能大幅下跌的警告性观点。
3.  **地缘政治与争议指控**：信号中包含多项针对美国政治人物的严重指控，包括指控伯尼·桑德斯与中国存在秘密财务联系，以及指控前总统奥巴马及前中情局局长为破坏特朗普选举而伪造“通俄门”情报。另有提及俄罗斯袭击了美国企业在乌克兰的工厂。

### 金融科技/AI/Web3相关线索
1.  **AI硬件供应链**：有信号指出，日本玻璃纤维公司Nittobo控制了90%的T-glass生产，该材料是每个AI芯片基板的结构核心，并提及英伟达、苹果、谷歌、亚马逊、AMD、微软和高通的高管曾为此亲赴日本游说供应。
2.  **加密货币与Web3**：
    *   **交易平台**：Bitget推广其股票永续合约交易，主打超低费用。
    *   **公链生态**：有观点列举了可能推动Cardano（ADA）上涨的多个技术与发展因素，包括USDCx、Midnight主网、比特币DeFi层、Leios、Hydra、LayerZero以及多个现货ETF上市预期。
    *   **市场预测**：有预警称比特币可能从下周开始出现“大规模抛售”，并在10天内跌至35,000美元。
3.  **AI应用与影响**：有用户对AI生成的视频内容表示强烈情绪反应（正面）。另有一条日文信号提及，在众议院选举期间，有约400个中国相关账户利用AI进行“反高市早苗工作”。

### 可执行关注点与潜在误导噪音
**可执行关注点**：
1.  **供应链关键节点**：可关注AI芯片上游材料（如T-glass）的垄断性供应商及其动态，这可能构成硬件投资的关键瓶颈。
2.  **政策映射交易**：关注韩国打击裸卖空与股市表现的关系，可作为评估美国或其他市场类似潜在政策影响的参考案例。
3.  **加密生态发展**：跟踪Cardano（ADA）提及的多项技术升级和产品主网上线进展，这些是评估其基本面的具体项目节点。

**潜在误导噪音**：
1.  **未经证实的重磅指控**：关于伯尼·桑德斯“中国账户”、奥巴马“伪造通俄门”等指控，用词极端（如“BOMBSHELL”、“TREASON”），缺乏可验证证据，属于高度政治化的争议信息，投资决策应避免采信。
2.  **情绪化与煽动性内容**：多条高互动信号包含明显的政治立场（支持特朗普）、煽动性标签（如#ImranKhanNeedsProperCare）和呼吁病毒式传播的指令，其核心目的是动员而非传递事实。
3.  **确定性市场预测**：“比特币将跌至35,000美元”等断言基于特定“模式”预测，属于个人观点，市场实际影响因素复杂，此类确定性预测风险极高。
4.  **数据不足领域**：关于“38%美国家庭无股市敞口”的具体数据来源及“特朗普账户”政策细节未提供；PayPal CEO“震惊世界”言论的具体背景和上下文未提供。

### 📰 热榜详细分析

# 热榜综合分析报告

基于提供的分片摘要，以下是融合分析结果：

## 1. 跨平台共同关注的3-5个热点事件
1.  **美国关税政策变动与争议**：这是最突出的跨平台热点。事件核心是**美国最高法院否决了（特朗普时期的）关税政策**（分片1、3、5、7），导致特朗普方面需退税（分片1）。同时，**特朗普宣布或计划加征新的全球进口关税**（分片3、5、7），税率有“10%”（分片3）和“升至15%”（分片7）两种说法，形成政策张力。此事件被市场解读为利好（分片6），也被分析为财政刺激与增加债务并存（分片2）。
2.  **春节档电影票房与社会文化**：**春节档电影总票房突破40亿元**（分片2、5），其中《飞驰人生3》以21亿领跑（分片5）。同时，“热气腾腾的中国年”（分片3）、春节旅游景点热度（分片4）、春晚小品（分片2）等春节相关话题广泛讨论。
3.  **存储芯片供需紧张**：“存储荒”持续（分片3），**SK海力士表示所有客户需求都无法满足**（分片2），**三星HBM4据称涨价30%**（分片3），韩国芯片公司积极扩产（分片3）。
4.  **国际关系与安全事件**：**多国敦促在伊朗公民尽快撤离**（分片3），伊朗外长退回美方信函（分片1），美伊关系受关注（分片2）。此外，**7名中国游客在贝加尔湖溺亡**（分片6）、俄日关系紧张（分片6）也是焦点。

## 2. 与金融市场相关的重要新闻
*   **美国关税政策影响**：该事件是核心金融线索。一方面，最高法院否决关税导致**特朗普需退税**，华尔街被指“早就下注”（分片1）。另一方面，政策变动被分析为对美股是财政刺激，对美债是增加债务（分片2），并引发**滞胀担忧，推动黄金价格重回5100（单位未提供），白银大涨8%**（分片3）。市场反应不一，有“美股三大指数集体下跌”（分片1）和“美股收高”（分片3）或“收涨”（分片6）的表述。
*   **半导体与黄金市场**：存储芯片需求旺盛、价格看涨（分片2、3）是明确的产业动态。**高盛指出黄金波动性大幅走高，央行购金力度将暂时放缓**（分片2）。**俄罗斯央行1月卖出30万盎司黄金储备**（分片7）。
*   **投资动向**：**中国顶流私募Q4集体加仓拼多多**，AI投资重心转变（分片1）。公募基金春节前集中调研机器人、半导体、有色金属（分片4）。
*   **其他**：**香港长江和记最新发声**（分片4），具体内容未提供。印度谈判购买委内瑞拉石油（分片7）。匈牙利拟否决欧盟对乌克兰900亿欧元贷款（分片7）。

## 3. 科技/AI 相关热点
*   **AI硬件与算力**：**OpenAI大幅下调算力支出目标**（分片4），具体目标数值未提供。**三星HBM4（高带宽存储器）据称涨价30%**（分片3），与AI加速卡供应链直接相关。
*   **自动驾驶**：**特斯拉发布无方向盘、踏板、后视镜的无人驾驶车**（分片1、3）。
*   **投资与关注**：中国顶流私募的**AI投资重心发生转变**（分片1），具体方向未提供。B站热搜有“实测Gemini 3.1 Pro”（分片5），但结论未提供。公募调研热点包括机器人（分片4）。
*   **开发者话题**：大一计算机新生如何利用GitHub的讨论（分片4）。

## 4. 社会舆论焦点
*   **春节体验与公共服务**：**“前方无厕所、无烤肠、无茶叶蛋”** 成为热搜（分片5），反映对景区服务的不满。春节旅游“游客过度拥挤引发后悔情绪”（分片2）、“天下第一财神庙被挤爆”（分片3）也是话题。
*   **社会民生与安全**：**瓶装水塑料颗粒污染**引发健康担忧（分片1）。国内发生因“熊孩子放炮”导致12人遇难的悲剧（分片2）。贴吧热议“喂猫起争执，男子遭恶邻杀害”（分片3）、“夫妻当街暴打15岁女孩”（分片3）等暴力事件。
*   **社会现象与讨论**：**“00后女孩月租200元住养老院两年”** 被讨论（分片1）。“钱到底还要不要存银行”登上热搜（分片5）。亲戚拜年不说话引发“沪漂”话题（分片3）。
*   **文化娱乐与学术争议**：春节档电影（分片2、5）、辽宁春晚小品（分片2）、《镖人》电影（分片3、4）受关注。关于**BCS超导理论是否为“庞氏骗局”的学术争议**被提及（分片1）。“日企采用中国芯”引发网络反应（分片2）。

### 💻 GitHub 项目详细分析

# GitHub热门项目技术趋势分析报告

基于2026年2月22日早报提供的GitHub项目样本，按金融科技、AI、Web3、通用四大领域进行筛选与分析。

## 一、 最值得关注的项目（5-8个）

1.  **nautechsystems/nautilus_trader** (金融科技): 一个用Rust编写的高性能算法交易平台和事件驱动回测器。
2.  **hummingbot/hummingbot** (金融科技): 开源软件，帮助用户创建和部署高频加密货币交易机器人。
3.  **openclaw/openclaw** (AI): 一个跨操作系统和平台的个人AI助手。
4.  **n8n-io/n8n** (AI): 具有原生AI功能的公平代码工作流自动化平台，结合可视化构建与自定义代码。
5.  **langflow-ai/langflow** (AI): 用于构建和部署AI驱动的智能体与工作流的强大工具。
6.  **langgenius/dify** (AI): 用于智能体工作流开发的生产就绪平台。
7.  **MetaMask/eth-phishing-detect** (Web3): 用于检测针对Web3用户的钓鱼域名的工具。

## 二、 应用场景与落地价值

*   **金融科技领域**: `nautilus_trader`和`hummingbot`等项目专注于**自动化交易**。前者提供机构级的回测与交易执行平台，后者则降低了创建加密货币交易机器人的门槛。其核心价值在于通过程序化策略提升交易效率与执行速度，服务于量化交易、做市、套利等场景。`polymarket-copy-bot-ts`等针对Polymarket预测市场的机器人，则指向了**预测市场自动化交易**这一细分场景。
*   **AI领域**: 趋势明显集中于**AI应用开发与工作流自动化**。`openclaw`定位为通用个人助手。`n8n`、`langflow`和`dify`则提供了从可视化编排(`n8n`)、智能体构建(`langflow`)到生产部署(`dify`)的完整工具链，旨在降低企业集成和部署AI能力的复杂度，赋能业务流程自动化与智能化改造。`ollama`简化了多种主流大模型的本地运行。
*   **Web3领域**: `eth-phishing-detect`直接应对**安全威胁**，其落地价值在于保护用户资产安全，是Web3生态健康发展的基础设施之一。`degenbot`提供了在去中心化交易所开发套利机器人的工具类，服务于**DeFi领域的自动化策略**。

## 三、 可能的泡沫噪音或重复概念

*   **AI工作流/智能体平台概念集中**: `n8n`、`langflow`、`dify`以及`AutoGPT`均涉及AI工作流或智能体构建，功能定位存在重叠。虽然各有侧重（如自动化、智能体、生产化），但需警惕市场过热可能导致的**概念重复与同质化竞争**，其长期差异化和实际商业价值需进一步观察。
*   **预测市场交易机器人扎堆**: 在金融科技领域，出现了两个针对Polymarket预测市场的交易机器人项目(`polymarket-copy-bot-ts`和`Polymarket-rsi-macd-index-trading-bot`)。这表明该细分赛道热度较高，但策略（复制交易、技术指标）相对传统，可能存在**创新性不足**和**市场容量有限**的风险。
*   **通用AI助手定位宽泛**: `openclaw`宣称是“任何OS、任何平台”的个人AI助手，此类项目通常面临与现有巨头产品（数据未提供具体名称）的竞争，其**具体技术优势、差异化特性及实际用户体验**未在提供信息中明确，成功与否存在不确定性。
*   **部分项目关联性存疑**: `free-v2ray-public-list`（免费代理服务器列表）被归类在金融科技下，但其描述与应用场景与金融科技核心关联度低，可能属于**分类噪音**。

### 🌐 联网检索摘要

联网检索共 11 条（关键词: 2026-02-22 全球市场 盘面 复盘 原因, 2026-02-22 中国 宏观 经济 政策 市场 影响, 2026-02-22 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 上涨 原因, 男子自驾游开10小时后弃车换高铁 事件 背景, “前方无厕所、无烤肠、无茶叶蛋” 事件 背景, 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准 事件 背景）
1. [2026-02-22 07:10] 大紀元新聞網 | IMF首次指中共產業補貼為宏觀失調 專家解析 - 大紀元新聞網
   摘要: IMF首次指中共產業補貼為宏觀失調 專家解析 大紀元新聞網
   链接: https://news.google.com/rss/articles/CBMiYEFVX3lxTE5zbGllVVcwYmtKMkZJQ29wbV9Zb1BXdTNMWEpuQnFLZnJ0Z3RMYlRJOEo5RU0zdGw1VXNMV0lpZDA1TVIzZTdxaUEwQUk3QW1LNE1tWW95M2w4YVRNbVdyd9IBZkFVX3lxTE9ZbXdvSmFXUWdTajJDanNPejFFNFJLRXVsd0tacy1jTExTcjFXNVJ5RXJCWGpGN09EMTBjZTB0UHk1bTRPbTlKTk1tdm4zYTZldnpPWURYdUpWbW9FYnNtZnYxcUM2Zw?oc=5
2. [2026-02-22 04:27] 游侠网 | 国际AG|联合多国艺术家打造和平主题艺术展 - 游侠网
   摘要: 国际AG|联合多国艺术家打造和平主题艺术展 游侠网
   链接: https://news.google.com/rss/articles/CBMiSkFVX3lxTE1yLUZkYXdXNXFiS3NiUThLNGI5UXJXbER3YXl3Q244UkpYSW91cEg0aHlHUjZxazBxcDNQaGQ2UmdqTTRqOVRTbWVB?oc=5
3. [2026-02-22 04:15] 游侠网 | 乐彩网全国彩票,合作梅赛德斯-AMG车队豪华与性能联动 - 游侠网
   摘要: 乐彩网全国彩票,合作梅赛德斯-AMG车队豪华与性能联动 游侠网
   链接: https://news.google.com/rss/articles/CBMiW0FVX3lxTE9QdEZSNGN6eTNEOGMydWY2QlJaWHBwM2FWbDJOS1BjcWR2amRvcjBmV2VYTGZ1aExZOXlLZGhvT2Z4SWtaWjRQRmkwMllWcUlnNVRzZ2RScGlPZ2M?oc=5
4. [2026-02-22 03:47] 3DM | 海洋娱乐平台(官方)综合娱乐APP下载-AppleAppStore - 3DM
   摘要: 海洋娱乐平台(官方)综合娱乐APP下载-AppleAppStore 3DM
   链接: https://news.google.com/rss/articles/CBMiWEFVX3lxTFBuNFNEWE11dmFSRnQyd3lyalo1bzZaYXlvXzdhUjVQU3cxb0ktQmE0QkNBQ095TVZBbDVkcnpQVkJkekRPQVNKTUd4cXVHS3pLMnBHQkJydHE?oc=5
5. [2026-02-21 08:24] yeeyi | 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 - yeeyi
   摘要: 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 yeeyi
   链接: https://news.google.com/rss/articles/CBMiVkFVX3lxTE91dGZGTy1OSTZSb2VXUjhVVC1kRFFtM0g5aXRtNXdzUThFR2lCanJhRlVrUk9xTExQSmpramhzUzJPRXItSGFMYXdmZ2VRc1g3Nmk0c1VB?oc=5
6. [2026-02-21 07:47] 富途牛牛 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛
   摘要: 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% 富途牛牛
   链接: https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5
7. [2026-02-21 05:30] 英为财情 Investing.com | 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5
8. [2026-02-20 19:48] OR新媒体 | OR新媒体| 美股为何如此诡异？ - OR新媒体
   摘要: OR新媒体| 美股为何如此诡异？ OR新媒体
   链接: https://news.google.com/rss/articles/CBMiREFVX3lxTE9EeFVtMVR6V1p3ckhwSHhLT29tTVZHYkRFcFhNQW5wbU82WEd4eDdfN2FLSkpTaEcyTGJWelF2bWR0ekJf?oc=5
9. [2026-02-20 18:45] 富途牛牛 | 芝加哥期权交易所波动率指数在特朗普据报道将伊朗外交期限延长10至15天后，盘前下跌0.5% - 富途牛牛
   摘要: 芝加哥期权交易所波动率指数在特朗普据报道将伊朗外交期限延长10至15天后，盘前下跌0.5% 富途牛牛
   链接: https://news.google.com/rss/articles/CBMilAFBVV95cUxPY2tONUdHUUthRm9SWk1kZ0ZERk9kWEoxb3Y2X000LTE0bmtxNmprNXlRSlE1SGpfZk5QdHE4NlUyX214QnRPcHptODJZNUFqY3B1emN0WlN0aHVOem5OY2ozbEk0d2lDZWlNLU9rM3lZb3Yxb1NxYlZDSDd3NS1DNFJRb3V3bElqUjNFRDUtWHJOV0pv?oc=5
10. [2026-02-20 14:45] Bitget | 美银对较高的股票风险敞口发出逆势“卖出”信号 - Bitget
   摘要: 美银对较高的股票风险敞口发出逆势“卖出”信号 Bitget
   链接: https://news.google.com/rss/articles/CBMia0FVX3lxTE5LLUpQSDBuUUxLbkRLSDRWRV84VFJ4SmUwSFNJNFNPY0tWbFBweVVDYkF6SG5jZlktZEtsbTc4dWEzU0FrRFdhWnd2WFRMb3FkeWFwVmdGc2t2WkFqTlZ6UmdfZlFqTHBEZmZn0gFrQVVfeXFMTkstSlBIMG5RTEtuREtINFZFXzhUUnhKZTBIU0k0U09jS1ZsUHB5VUNiQXpIbmNmWS1kS2xtNzh1YTNTQWtEV2Fad3ZYVExvcWR5YXBWZ0Zza3ZaQWpOVnpSZ19mUWpMcERmZmc?oc=5
11. [2026-02-20 13:30] 英为财情 Investing.com | 澳大利亚股市收低；截至收盘澳大利亚S&P/ASX200指数下跌0.05% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 澳大利亚股市收低；截至收盘澳大利亚S&P/ASX200指数下跌0.05% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTE1VRXd4WTVIdU42dGRiZXNSMHlmWWx6UW9pWjlRTWswYm1CT3U0ZGxfelh2UDI4dG9vdTFabFNUcTVoQlJSb0d1UDJDbnEteGRXYXgxN2kwRHNMX1otbHNmVVBjWDV6QTlBYUY5NHVTR0g?oc=5

</details>


### 📎 引用脚注

1. [2026-02-22T00:00 @Gaurab | Nittobo is a Japanese glass fiber company with 2,745 employees. Nvidia, Apple, Google, A...](https://twitter.com/Gaurab/status/2024959539511275769)（Twitter，匹配分=100，来源ID=TW10）
2. [2026-02-22T00:00 @nikkei | 衆議院選挙、中国系400アカウントが「反高市工作」 AIで巧妙にnikkei.com/article/DGXZTS000…](https://twitter.com/nikkei/status/2025309061068067168)（Twitter，匹配分=100，来源ID=TW07）
3. [2026-02-22T00:00 @xMarketNews | SOUTH KOREA STOCK MARKET HAS SURGED NEARLY 150% SINCE THEY TOOK ACTION AGAINST NAKED SHO...](https://twitter.com/xMarketNews/status/2025296878707913043)（Twitter，匹配分=100，来源ID=TW15）
4. [2026-02-22T00:00 @mcafeenew | 🚨BOMBSHELL ALERT: BERNIE SANDERS EXPOSED IN MASSIVE CHINA SCANDAL! 🔗t.me/+bWjXP07v90xlYW...](https://twitter.com/mcafeenew/status/2025280842499531121)（Twitter，匹配分=100，来源ID=TW08）
5. [2026-02-22T00:00 @EshaAA33 | BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, h...](https://twitter.com/EshaAA33/status/2025147573838000572)（Twitter，匹配分=100，来源ID=TW12）

## 🧪 引用匹配校验

- 已匹配引用条数: 5
- 未完成匹配标签: 0
- 低置信引用条数: 0
- 处理建议: 本次未发现低置信引用。

## 🎯 投机方向（超短）

- 海外指数方向：美股 VIX波动率指数 -5.64%（高波动回撤）
- 商品波段方向：COMEX铜 +1.76%
- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。

## 🌐 联网检索补充

- 关键词：2026-02-22 全球市场 盘面 复盘 原因, 2026-02-22 中国 宏观 经济 政策 市场 影响, 2026-02-22 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 上涨 原因, 男子自驾游开10小时后弃车换高铁 事件 背景, “前方无厕所、无烤肠、无茶叶蛋” 事件 背景, 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准 事件 背景
- 命中结果：11 条（按发布时间倒序）

### 🔎 2026-02-22 中国 宏观 经济 政策 市场 影响

- [IMF首次指中共產業補貼為宏觀失調 專家解析 - 大紀元新聞網](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5zbGllVVcwYmtKMkZJQ29wbV9Zb1BXdTNMWEpuQnFLZnJ0Z3RMYlRJOEo5RU0zdGw1VXNMV0lpZDA1TVIzZTdxaUEwQUk3QW1LNE1tWW95M2w4YVRNbVdyd9IBZkFVX3lxTE9ZbXdvSmFXUWdTajJDanNPejFFNFJLRXVsd0tacy1jTExTcjFXNVJ5RXJCWGpGN09EMTBjZTB0UHk1bTRPbTlKTk1tdm4zYTZldnpPWURYdUpWbW9FYnNtZnYxcUM2Zw?oc=5)
  - 来源: 大紀元新聞網 | 时间: 2026-02-22 07:10
  - 摘要: IMF首次指中共產業補貼為宏觀失調 專家解析 大紀元新聞網
- [海洋娱乐平台(官方)综合娱乐APP下载-AppleAppStore - 3DM](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBuNFNEWE11dmFSRnQyd3lyalo1bzZaYXlvXzdhUjVQU3cxb0ktQmE0QkNBQ095TVZBbDVkcnpQVkJkekRPQVNKTUd4cXVHS3pLMnBHQkJydHE?oc=5)
  - 来源: 3DM | 时间: 2026-02-22 03:47
  - 摘要: 海洋娱乐平台(官方)综合娱乐APP下载-AppleAppStore 3DM

### 🔎 2026-02-22 AI 科技 行业 动态 影响

- [国际AG|联合多国艺术家打造和平主题艺术展 - 游侠网](https://news.google.com/rss/articles/CBMiSkFVX3lxTE1yLUZkYXdXNXFiS3NiUThLNGI5UXJXbER3YXl3Q244UkpYSW91cEg0aHlHUjZxazBxcDNQaGQ2UmdqTTRqOVRTbWVB?oc=5)
  - 来源: 游侠网 | 时间: 2026-02-22 04:27
  - 摘要: 国际AG|联合多国艺术家打造和平主题艺术展 游侠网
- [乐彩网全国彩票,合作梅赛德斯-AMG车队豪华与性能联动 - 游侠网](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9QdEZSNGN6eTNEOGMydWY2QlJaWHBwM2FWbDJOS1BjcWR2amRvcjBmV2VYTGZ1aExZOXlLZGhvT2Z4SWtaWjRQRmkwMllWcUlnNVRzZ2RScGlPZ2M?oc=5)
  - 来源: 游侠网 | 时间: 2026-02-22 04:15
  - 摘要: 乐彩网全国彩票,合作梅赛德斯-AMG车队豪华与性能联动 游侠网

### 🔎 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准 事件 背景

- [春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTE91dGZGTy1OSTZSb2VXUjhVVC1kRFFtM0g5aXRtNXdzUThFR2lCanJhRlVrUk9xTExQSmpramhzUzJPRXItSGFMYXdmZ2VRc1g3Nmk0c1VB?oc=5)
  - 来源: yeeyi | 时间: 2026-02-21 08:24
  - 摘要: 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 yeeyi

### 🔎 VIX波动率指数 下跌 原因

- [美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5)
  - 来源: 富途牛牛 | 时间: 2026-02-21 07:47
  - 摘要: 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% 富途牛牛
- [美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-21 05:30
  - 摘要: 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com 英为财情 Investing.com
- [OR新媒体| 美股为何如此诡异？ - OR新媒体](https://news.google.com/rss/articles/CBMiREFVX3lxTE9EeFVtMVR6V1p3ckhwSHhLT29tTVZHYkRFcFhNQW5wbU82WEd4eDdfN2FLSkpTaEcyTGJWelF2bWR0ekJf?oc=5)
  - 来源: OR新媒体 | 时间: 2026-02-20 19:48
  - 摘要: OR新媒体| 美股为何如此诡异？ OR新媒体
- [芝加哥期权交易所波动率指数在特朗普据报道将伊朗外交期限延长10至15天后，盘前下跌0.5% - 富途牛牛](https://news.google.com/rss/articles/CBMilAFBVV95cUxPY2tONUdHUUthRm9SWk1kZ0ZERk9kWEoxb3Y2X000LTE0bmtxNmprNXlRSlE1SGpfZk5QdHE4NlUyX214QnRPcHptODJZNUFqY3B1emN0WlN0aHVOem5OY2ozbEk0d2lDZWlNLU9rM3lZb3Yxb1NxYlZDSDd3NS1DNFJRb3V3bElqUjNFRDUtWHJOV0pv?oc=5)
  - 来源: 富途牛牛 | 时间: 2026-02-20 18:45
  - 摘要: 芝加哥期权交易所波动率指数在特朗普据报道将伊朗外交期限延长10至15天后，盘前下跌0.5% 富途牛牛
- [美银对较高的股票风险敞口发出逆势“卖出”信号 - Bitget](https://news.google.com/rss/articles/CBMia0FVX3lxTE5LLUpQSDBuUUxLbkRLSDRWRV84VFJ4SmUwSFNJNFNPY0tWbFBweVVDYkF6SG5jZlktZEtsbTc4dWEzU0FrRFdhWnd2WFRMb3FkeWFwVmdGc2t2WkFqTlZ6UmdfZlFqTHBEZmZn0gFrQVVfeXFMTkstSlBIMG5RTEtuREtINFZFXzhUUnhKZTBIU0k0U09jS1ZsUHB5VUNiQXpIbmNmWS1kS2xtNzh1YTNTQWtEV2Fad3ZYVExvcWR5YXBWZ0Zza3ZaQWpOVnpSZ19mUWpMcERmZmc?oc=5)
  - 来源: Bitget | 时间: 2026-02-20 14:45
  - 摘要: 美银对较高的股票风险敞口发出逆势“卖出”信号 Bitget
- [澳大利亚股市收低；截至收盘澳大利亚S&P/ASX200指数下跌0.05% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE1VRXd4WTVIdU42dGRiZXNSMHlmWWx6UW9pWjlRTWswYm1CT3U0ZGxfelh2UDI4dG9vdTFabFNUcTVoQlJSb0d1UDJDbnEteGRXYXgxN2kwRHNMX1otbHNmVVBjWDV6QTlBYUY5NHVTR0g?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-20 13:30
  - 摘要: 澳大利亚股市收低；截至收盘澳大利亚S&P/ASX200指数下跌0.05% 提供者 Investing.com 英为财情 Investing.com

## 🔗 AI 分析引用来源

> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。

### Twitter (5 条)

- [¹] [2026-02-22T00:00 @Gaurab | Nittobo is a Japanese glass fiber company with 2,745 employees. Nvidia, Apple, Google, A...](https://twitter.com/Gaurab/status/2024959539511275769)（匹配分=100，来源ID=TW10）
- [²] [2026-02-22T00:00 @nikkei | 衆議院選挙、中国系400アカウントが「反高市工作」 AIで巧妙にnikkei.com/article/DGXZTS000…](https://twitter.com/nikkei/status/2025309061068067168)（匹配分=100，来源ID=TW07）
- [³] [2026-02-22T00:00 @xMarketNews | SOUTH KOREA STOCK MARKET HAS SURGED NEARLY 150% SINCE THEY TOOK ACTION AGAINST NAKED SHO...](https://twitter.com/xMarketNews/status/2025296878707913043)（匹配分=100，来源ID=TW15）
- [⁴] [2026-02-22T00:00 @mcafeenew | 🚨BOMBSHELL ALERT: BERNIE SANDERS EXPOSED IN MASSIVE CHINA SCANDAL! 🔗t.me/+bWjXP07v90xlYW...](https://twitter.com/mcafeenew/status/2025280842499531121)（匹配分=100，来源ID=TW08）
- [⁵] [2026-02-22T00:00 @EshaAA33 | BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, h...](https://twitter.com/EshaAA33/status/2025147573838000572)（匹配分=100，来源ID=TW12）

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
| BTC | $67,996.00 | 🟢 +0.04% |
| ETH | $1,973.50 | 🟢 +0.29% |
| SOL | $85.21 | 🟢 +0.86% |

### 📈 国际期货

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|
| WTI原油 | 66.39 | 🔴 -0.06% |
| 布伦特原油 | 71.76 | 🟢 +0.14% |
| 天然气 | 3.05 | 🟢 +1.70% |
| COMEX铜 | 5.83 | 🟢 +1.76% |

### 💻 GitHub 趋势

- ⭐ [**visual-explainer**](https://github.com/nicobailon/visual-explainer) (2201 stars)
  - Agent skill + prompt templates that generate rich HTML pages for visual diff rev
- ⭐ [**nullclaw**](https://github.com/nullclaw/nullclaw) (1485 stars)
  - Fastest, smallest, and fully autonomous AI assistant infrastructure written in Z
- ⭐ [**BarraCUDA**](https://github.com/Zaneham/BarraCUDA) (1258 stars)
  - Open-source CUDA compiler targeting AMD GPUs (and more in the future!). Compiles
- ⭐ [**OpenPlanter**](https://github.com/ShinMegamiBoson/OpenPlanter) (788 stars)
- ⭐ [**ai-engineer-handbook**](https://github.com/DataExpert-io/ai-engineer-handbook) (773 stars)
  - All the links, books, and creators you need to follow to stay up to date with AI

## 🐦 Twitter 热点 (74 条)

- 来源统计: 关注账号 210 条 | 热门讨论 30 条

### 🔥 热门讨论推文

- `2026-02-22T00:00` @akiko_lawson ❤️6564 🔁37786 💬118
  - 5日間限定の無料券チャレンジ(^^) 今日は冷凍米飯無料の最終日です♪  1）このアカウントをフォロー 2）この投稿をリポスト 3）抽選で毎日1万名様に無料券！結果は自動でお知らせ
  - [原文链接](https://twitter.com/akiko_lawson/status/2025344790129455528)
- `2026-02-22T00:00` @needtheIight ❤️30546 🔁1065 💬68
  - ai lembrando desse print aqui...
  - [原文链接](https://twitter.com/needtheIight/status/2025044319095144644)
- `2026-02-22T00:00` @TadaaVoila ❤️6715 🔁16995 💬11
  - อย่าเลิกตามการเมืองเด็ดขาด คือพักได้แต่อย่าเลิก อย่าคิดว่าสังคมมันเฮงซวยเหมือนเดิม ถ้าวันนั้นไม่มีใครสนใจการเมืองไม่มีเนติวิทย์ไม่มีนักเรียนเลวเด็กไทยคงได้ตัดผมสั้นเท่ากะลาครอบหัวเหมือนคนคุก
  - [原文链接](https://twitter.com/TadaaVoila/status/2025115801377022067)
- `2026-02-22T00:00` @pupxtra_ ❤️12736 🔁5961 💬36
  - i ♥️  nerds
  - [原文链接](https://twitter.com/pupxtra_/status/2025014218282471547)
- `2026-02-22T00:00` @WhiteHouse ❤️7564 🔁1808 💬1834
  - TRUST IN TRUMP 🔥  A busy week at the White House  🕊️ Inaugural Board of Peace 🏭 Georgia Visit on Economy 🍔 The Varsity Stop 🤝 Governors' Breakfast  🇺🇸 Black History Month ⚖️ Tariffs 🏡 Lowest Mortgage Rates Since ’22 🌏 Indonesia Trade Deal@PressSec's MAGA Min is BACK ⬇️
  - [原文链接](https://twitter.com/WhiteHouse/status/2025292911903212018)
- `2026-02-22T00:00` @kaaleeby ❤️6782 🔁787 💬78
  - Ai calica eu grito Ave Maria Ela joga a raba e depois vai pra missa  Aí danada, ela não é santa  Agora se ajoelha e vou mostrar quem é que manda 🎶
  - [原文链接](https://twitter.com/kaaleeby/status/2025033822920647153)
- `2026-02-22T00:00` @nikkei ❤️3912 🔁1769 💬228
  - 衆議院選挙、中国系400アカウントが「反高市工作」　AIで巧妙にnikkei.com/article/DGXZTS000…
  - [原文链接](https://twitter.com/nikkei/status/2025309061068067168)
- `2026-02-22T00:00` @mcafeenew ❤️2908 🔁2382 💬302
  - 🚨BOMBSHELL ALERT: BERNIE SANDERS EXPOSED IN MASSIVE CHINA SCANDAL!  🔗t.me/+bWjXP07v90xlYWFkNational Intel Agency UNCOVERS SHOCKING SECRET LINKS – Dozens of HIDDEN BANK ACCOUNTS in Beijing, OWNERSHIP of SHADY COMPANIES, ALL KEPT OFF HIS CONGRESSIONAL RECORDS!  Is This TREASON? ILLEGAL HOLDINGS That Could DESTROY HIS CAREER – Or WORSE! You Won't Believe How DEEP This Communist Rabbit Hole Goes!🇨🇳  SHARE IF YOU DEMAND ANSWERS NOW!  Follow@mcafeenewfor more drops.
  - [原文链接](https://twitter.com/mcafeenew/status/2025280842499531121)
- `2026-02-22T00:00` @bitget ❤️3457 🔁300 💬69
  - Level up your trading on Bitget stock perps  With ultra-low fees, you can seize every market opportunity  Want more? Check out all the features 👇
  - [原文链接](https://twitter.com/bitget/status/2023336325282508801)
- `2026-02-22T00:00` @Gaurab ❤️3041 🔁397 💬35
  - Nittobo is a Japanese glass fiber company with 2,745 employees. Nvidia, Apple, Google, Amazon, AMD, Microsoft, and Qualcomm have all sent executives to Japan to personally lobby for supply. T-glass forms the structural core of every AI chip substrate. Nittobo controls 90% of it. It sells for $80 to $100 per kilogram. Standard glass fiber is $3 to $5. The thermal expansion has to match silicon almost exactly or the substrate warps and the chip fails. Nvidia locked up supply through long-term bind
  - [原文链接](https://twitter.com/Gaurab/status/2024959539511275769)
- `2026-02-22T00:00` @culianax ❤️3065 🔁106 💬6
  - ai gente 😭😭😭
  - [原文链接](https://twitter.com/culianax/status/2025020394143416385)
- `2026-02-22T00:00` @EshaAA33 ❤️1349 🔁641 💬576
  - BREAKING 🅱️:  20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hidden in CIA vault for ~10 years, to undermine Trump’s election via manipulated intel.  Do you support arresting Hussein Obama for treason?  A. Hell yeah B. No  MAKE THIS GO VIRAL ON 𝕏.👏
  - [原文链接](https://twitter.com/EshaAA33/status/2025147573838000572)
- `2026-02-22T00:00` @RapidResponse47 ❤️1637 🔁294 💬61
  - "38% of American families have no exposure to the U.S. stock market... and with@TrumpAccounts, for the next four years, every child born...@USTreasuryputs in $1,000, it goes into an index fund," says@SecScottBessent.  "I think these are going to be transformational."
  - [原文链接](https://twitter.com/RapidResponse47/status/2024958380847095954)
- `2026-02-22T00:00` @TheProfInvestor ❤️1562 🔁207 💬40
  - Here are some basic rules:  When insiders buy, you pay attention.  Stock gets below 200-week SMA, you avoid.  Ignore stocks making new lows when the market is making highs.  If it's down 50% in a bull market, there's a reason - and it's not "opportunity."  When a stock breaks down on earnings, don't try to catch it. Let it find a floor first.  Stock pumps 30% in a week with no news? That's not opportunity. That's someone's exit liquidity.  If you can't explain the thesis in two sentences, you do
  - [原文链接](https://twitter.com/TheProfInvestor/status/2024640490617049561)
- `2026-02-22T00:00` @xMarketNews ❤️1381 🔁284 💬39
  - SOUTH KOREA STOCK MARKET HAS SURGED NEARLY 150% SINCE THEY TOOK ACTION AGAINST NAKED SHORT SELLING🚨  - South Korea Suspended Short Selling to Probe Naked Shorting, Introduced Imprisonment and Heavy Fines…   LIKE 👍 IF YOU THINK DONALD TRUMP SHOULD DO THE SAME
  - [原文链接](https://twitter.com/xMarketNews/status/2025296878707913043)
- `2026-02-22T00:00` @agentjay2009 ❤️931 🔁532 💬13
  - This economic disaster is also a natural security debacle! Asim Munir’s SIFC has failed miserably.  No one in the world has confidence in Pakistan’s economy because of lawlessness they see via regime’s fascist treatment to Imran Khan!#ImranKhanNeedsProperCare
  - [原文链接](https://twitter.com/agentjay2009/status/2025287147159228776)
- `2026-02-22T00:00` @Barchart ❤️1081 🔁73 💬112
  - 2 years ago, PayPal’s CEO said “we will shock the world.”$PYPLhas plunged more than 30% since 🚨 We have indeed been shocked at how bad a stock can perform in a raging bull market 🫡
  - [原文链接](https://twitter.com/Barchart/status/2025185172958683287)
- `2026-02-22T00:00` @_yayeezy ❤️0 🔁1229 💬0
  - RT@6uhle: AI videos usually piss me tf off but this is KILLINGGG me 😭😭😭😭😭
  - [原文链接](https://twitter.com/_yayeezy/status/2025360031646904504)
- `2026-02-22T00:00` @hNzisacVzBB1QR1 ❤️0 🔁948 💬0
  - RT@shinjirokoiz: 防衛省AIチームの皆さんから答弁作成ツールを実際に使いながら説明を受けました。職員曰く、一度使ったらもう今までの答弁作成には戻れないそうです。新たな取組みによって職員が少しでも効率よく仕事が出来て、防衛省に入って良かったとモチベーション高く働…
  - [原文链接](https://twitter.com/hNzisacVzBB1QR1/status/2025360028799279490)
- `2026-02-22T00:00` @WiganAndrew ❤️621 🔁227 💬69
  - Not a peep from Charlie and Naga.  If it was bad news for the economy, they would have run the story on the hour and every five minutes. They would also have the two Tory creeps@ChrisMasonBBCand@hzeffmansmirking.@BBCPoliticsis no longer an impartial news programme.
  - [原文链接](https://twitter.com/WiganAndrew/status/2025144052266504530)

### @NikkeiAsia (10 条)

- `2026-02-22T00:00` LISTEN: Nikkei Asia News Roundup   Indonesian coffee chains test overseas tastes in global expansion  Available on Spotify, Apple and YouTube:  https://s.nikkei.com/4u0X3Sa
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025359906874773859)
- `2026-02-22T00:00` This was our most read opinion piece for the week.  Xi's anti-corruption drive has removed the PLA's safety valve  https://s.nikkei.com/4rt2g3u
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025359894111547504)
- `2026-02-21T23:26` 10 Japan trips for fun in the snow -- not just skiing  Ride, trek or float through some of the county's best winter landscapes  https://s.nikkei.com/4b36cC3
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025351431524393000)
- `2026-02-21T23:09` Chinese consumers snap up gold jewelry merch for fandom and investment https://s.nikkei.com/3MXfINQ
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025347244006703259)
- `2026-02-21T23:00` Japan has cut its rare-earth dependence on China from around 90% to only about 60% in 15 years. The US faces a similarly long road to rebuilding its ability to refine and process such minerals.  https://s.nikkei.com/4cwuWUn
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025345019733737791)
- *... 及其他 5 条*

### @SCMPNews (7 条)

- `2026-02-21T23:48` ‘I could not walk’: how exercise helped a mother manage serious knee pain https://www.scmp.com/lifestyle/health-wellness/article/3344133/how-exercise-helped-mother-tackle-serious-knee-pain-and-return-cane-free-walking?utm_medium=Social&utm_source=Twitter#Echobox=1771716262-1
  - [原文链接](https://twitter.com/SCMPNews/status/2025356993054060853)
- `2026-02-21T22:03` K-pop’s big freeze: are cracks in China’s cultural blockade a thaw?  https://www.scmp.com/news/china/diplomacy/article/3344205/k-pops-big-freeze-are-cracks-chinas-cultural-blockade-thaw
  - [原文链接](https://twitter.com/SCMPNews/status/2025330439146053909)
- `2026-02-21T21:53` US ambassador says Israel has right to much of Middle East, sparking uproar  https://www.scmp.com/news/world/middle-east/article/3344233/us-ambassador-says-israel-has-right-much-middle-east-sparking-uproar
  - [原文链接](https://twitter.com/SCMPNews/status/2025328001559237020)
- `2026-02-21T18:14` Bus with Chinese tourists crashes through ice on Russia’s Lake Baikal, killing 8  https://www.scmp.com/news/world/russia-central-asia/article/3344231/bus-chinese-tourists-crashes-through-ice-russias-lake-baikal-killing-8
  - [原文链接](https://twitter.com/SCMPNews/status/2025272809157427458)
- `2026-02-21T18:11` Nasa moon rocket hit by new problem, pushing launch with astronauts into April  https://www.scmp.com/news/world/united-states-canada/article/3344230/nasa-moon-rocket-hit-new-problem-putting-march-launch-astronauts-jeopardy
  - [原文链接](https://twitter.com/SCMPNews/status/2025272159598203258)
- *... 及其他 2 条*

### @WuBlockchain (3 条)

- `2026-02-21T22:00` CZ: Real Capital and Builders Will Shift Focus to RWA and Prediction Markets  On February 12, 2026, during a Binance Square AMA, CZ predicted that the industry's focus is shifting toward Real World Asset (RWA) tokenization.   He noted that countries could tokenize assets like gold, rare earth minera
  - [原文链接](https://twitter.com/WuBlockchain/status/2025329686352695722)
- `2026-02-21T19:00` CZ on Life After Immigrating to Canada: Mom Worked in a Sewing Factory, I Worked at McDonald's  On February 10, 2026, in an exclusive interview with The All-In Podcast, Binance founder CZ recalled the hardships of his early immigration to Canada. He mentioned that his father worked as a university t
  - [原文链接](https://twitter.com/WuBlockchain/status/2025284391400804461)
- `2026-02-21T16:04` Vitalik Buterin published a post stating that the core issue of current decentralized governance (such as DAOs) lies in the scarcity of human attention, while traditional mechanisms tend to lead to the concentration of power. To this end, he proposed utilizing personal Large Language Models (LLMs) t
  - [原文链接](https://twitter.com/WuBlockchain/status/2025240326533997000)

### @ReutersBiz (1 条)

- `2026-02-21T20:40` WATCH:President Trump said he will raise a temporary tariff from 10% to 15% on US imports from all countries, the maximum level allowed under the law, after the Supreme Court struck down his previous tariff program https://reut.rs/3MX4n0e  Video
  - [原文链接](https://twitter.com/ReutersBiz/status/2025309551692525586)

### @WSJ (10 条)

- `2026-02-21T19:09` From http://localhost/WSJFreeEx via http://localhost/WSJopinion: While new AI technologies will save many lives, it could also render many of us unable to complete daily tasks without assistance, writes http://localhost/jamesbmeigs  https://on.wsj.com/4b1upbS
  - [原文链接](https://twitter.com/WSJ/status/2025286674926682276)
- `2026-02-21T18:48` From http://localhost/WSJFreeEx via http://localhost/WSJopinion: Elite female athletes often face a trade-off between competition and motherhood. Italian speedskater Francesca Lollobrigida proves both are possible, writes http://localhost/MJ_Koch.  https://on.wsj.com/3OoVf53
  - [原文链接](https://twitter.com/WSJ/status/2025281614184391153)
- `2026-02-21T18:27` From http://localhost/WSJopinion: Rubio Plays Good Cop to Vance’s Bad by http://localhost/Peggynoonannyc  https://on.wsj.com/473ll3R
  - [原文链接](https://twitter.com/WSJ/status/2025276147626369422)
- `2026-02-21T18:06` From http://localhost/WSJopinion: The Warner Bros. fight isn’t over. Investors start to see past Trump and ask which takeover offer is really better, writes Holman Jenkins.  https://on.wsj.com/4c1Rigt
  - [原文链接](https://twitter.com/WSJ/status/2025270909678825560)
- `2026-02-21T17:44` From http://localhost/WSJopinion: Christianity isn’t dead in the West. Marco Rubio rightly urges Europeans to remember their religious origins, writes Barton Swaim.  https://on.wsj.com/46m832i
  - [原文链接](https://twitter.com/WSJ/status/2025265352406397154)
- *... 及其他 5 条*

### @PeterSchiff (1 条)

- `2026-02-21T18:26` So happy to have this original Market Price in our living room in our Puerto Rico home.   http://localhost/1MarketPrice
  - [原文链接](https://twitter.com/PeterSchiff/status/2025275961499898071)

### @CNBC (7 条)

- `2026-02-21T17:32` Airlines waive change fees ahead of another monster winter storm https://www.cnbc.com/2026/02/21/blizzard-prompts-airlines-waive-flight-change-fees.html?taid=6999ec18773d17000105e994&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025262275263598924)
- `2026-02-21T15:03` This week’s most overbought stocks include Deere and Quanta Services https://www.cnbc.com/2026/02/21/this-weeks-most-overbought-stocks-include-deere-and-quanta-services.html?taid=6999c92d169313000113951b&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025224781507760636)
- `2026-02-21T14:54` Five key takeaways from the Supreme Court's landmark decision against Trump's tariffs https://www.cnbc.com/2026/02/21/supreme-courts-trump-tariff-decision-five-takeaways.html?taid=6999c7418e21f400010d9d89&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025222719990616196)
- `2026-02-21T14:52` Bank of America names five stocks best positioned for shareholder returns https://www.cnbc.com/2026/02/21/five-stocks-for-shareholder-returns-according-to-bank-of-america.html?taid=6999c6c16a26b000013cbb32&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025222182746353852)
- `2026-02-21T14:44` Trump accounts have 'more unanswered questions than answered,' expert says. What's still unknown https://www.cnbc.com/2026/02/21/trump-accounts.html?taid=6999c4b7773d17000105e86f&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025219993550434394)
- *... 及其他 2 条*

### @BNONews (1 条)

- `2026-02-21T16:17` JUST IN: Trump says 10% worldwide tariff rate announced yesterday will rise to 15% "effective immediately"  BNO News (@BNONews)  Trump imposes addtional 10% tariff on all countries "effective almost immediately"  — http://localhost/BNONews/status/2024997803676627106#m
  - [原文链接](https://twitter.com/BNONews/status/2025243509314519504)

### @ylecun (1 条)

- `2026-02-21T16:01` Corruption  Meet Kevin (@realMeetKevin)  🚨 Howard Lutnick's family firm bought up the rights to tariff refunds for 20-30 cents on the dollar after Liberation Day last year.  Today, the Supreme Court struck the tariffs down. For every $100 invested, Lutnick's sons just made 3-5x.  Welcome to Crony Co
  - [原文链接](https://twitter.com/ylecun/status/2025239374930346300)

### @SoberLook (1 条)

- `2026-02-21T15:09` 🇺🇸 US high-frequency dashboard, composed of daily and weekly economic indicators (updated as of Feb. 20, 2026).  http://localhost/search?q=%23economy
  - [原文链接](https://twitter.com/SoberLook/status/2025226354732490914)

### @VitalikButerin (1 条)

- `2026-02-21T15:05` "AI becomes the government" is dystopian: it leads to slop when AI is weak, and is doom-maximizing once AI becomes strong. But AI used well can be empowering, and push the frontier of democratic / decentralized modes of governance.  The core problem with democratic / decentralized modes of governanc
  - [原文链接](https://twitter.com/VitalikButerin/status/2025225247088402581)

### @globaltimesnews (1 条)

- `2026-02-21T13:12` China won the bronze medal in the freestyle skiing mixed team aerials of the Milan-Cortina Winter Olympics on February 21. The Chinese trio of Xu Mengtao, Wang Xindi and Li Tianma scored a combined 279.68 points to secure a place on the podium. Team USA defended its title to take gold, while Switzer
  - [原文链接](https://twitter.com/globaltimesnews/status/2025196856264028574)

## 📱 微信公众号

暂无数据

## 🔥 NewsNow 热榜 (120 条)

### 今日头条

| 排名 | 标题 |
|------|------|
| #1 | [男子自驾游开10小时后弃车换高铁](https://www.toutiao.com/trending/7608953617383587886/) |
| #2 | [钱到底还要不要存银行](https://www.toutiao.com/trending/7609305215459659302/) |
| #3 | [春节哪些景点更热门？一组数据盘点](https://www.toutiao.com/trending/7608388814415072787/) |
| #4 | [00后女孩月租200住养老院两年](https://www.toutiao.com/trending/7609139159411753014/) |
| #5 | [中国体育史上六对奥运金牌夫妇](https://www.toutiao.com/trending/7607817106020945427/) |
| #6 | [杨幂带火白绿条纹吊带裙](https://www.toutiao.com/trending/7608917512491221055/) |
| #7 | [网友家有个塑料盆用了40多年仍完好](https://www.toutiao.com/trending/7609287094111944714/) |
| #8 | [专家解读本次沙尘天气从何而来](https://www.toutiao.com/trending/7609308817964289586/) |
| #9 | [黑龙江现大型动物咬死小牛](https://www.toutiao.com/trending/7609294060034375716/) |
| #10 | [匈牙利将否决欧盟对乌900亿欧元贷款](https://www.toutiao.com/trending/7609031193127813126/) |

### 百度热搜

| 排名 | 标题 |
|------|------|
| #1 | [“前方无厕所、无烤肠、无茶叶蛋”](https://www.baidu.com/s?wd=%E2%80%9C%E5%89%8D%E6%96%B9%E6%97%A0%E5%8E%95%E6%89%80%E3%80%81%E6%97%A0%E7%83%A4%E8%82%A0%E3%80%81%E6%97%A0%E8%8C%B6%E5%8F%B6%E8%9B%8B%E2%80%9D) |
| #2 | [山东网友自驾去重庆 开了10小时弃车](https://www.baidu.com/s?wd=%E5%B1%B1%E4%B8%9C%E7%BD%91%E5%8F%8B%E8%87%AA%E9%A9%BE%E5%8E%BB%E9%87%8D%E5%BA%86+%E5%BC%80%E4%BA%8610%E5%B0%8F%E6%97%B6%E5%BC%83%E8%BD%A6) |
| #3 | [“赛博”中国年](https://www.baidu.com/s?wd=%E2%80%9C%E8%B5%9B%E5%8D%9A%E2%80%9D%E4%B8%AD%E5%9B%BD%E5%B9%B4) |
| #4 | [游客挤到悔不当初不如在家刷手机](https://www.baidu.com/s?wd=%E6%B8%B8%E5%AE%A2%E6%8C%A4%E5%88%B0%E6%82%94%E4%B8%8D%E5%BD%93%E5%88%9D%E4%B8%8D%E5%A6%82%E5%9C%A8%E5%AE%B6%E5%88%B7%E6%89%8B%E6%9C%BA) |
| #5 | [“假蔡明”被送给了真蔡明](https://www.baidu.com/s?wd=%E2%80%9C%E5%81%87%E8%94%A1%E6%98%8E%E2%80%9D%E8%A2%AB%E9%80%81%E7%BB%99%E4%BA%86%E7%9C%9F%E8%94%A1%E6%98%8E) |
| #6 | [哈尔滨冰雪大世界：正式闭园](https://www.baidu.com/s?wd=%E5%93%88%E5%B0%94%E6%BB%A8%E5%86%B0%E9%9B%AA%E5%A4%A7%E4%B8%96%E7%95%8C%EF%BC%9A%E6%AD%A3%E5%BC%8F%E9%97%AD%E5%9B%AD) |
| #7 | [中国有六对奥运金牌夫妇](https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E6%9C%89%E5%85%AD%E5%AF%B9%E5%A5%A5%E8%BF%90%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%87) |
| #8 | [83岁外婆拿竹扫帚给孙女洗车](https://www.baidu.com/s?wd=83%E5%B2%81%E5%A4%96%E5%A9%86%E6%8B%BF%E7%AB%B9%E6%89%AB%E5%B8%9A%E7%BB%99%E5%AD%99%E5%A5%B3%E6%B4%97%E8%BD%A6) |
| #9 | [“天下第一财神庙”被游客挤爆](https://www.baidu.com/s?wd=%E2%80%9C%E5%A4%A9%E4%B8%8B%E7%AC%AC%E4%B8%80%E8%B4%A2%E7%A5%9E%E5%BA%99%E2%80%9D%E8%A2%AB%E6%B8%B8%E5%AE%A2%E6%8C%A4%E7%88%86) |
| #10 | [景区女财神被游客追得满场跑](https://www.baidu.com/s?wd=%E6%99%AF%E5%8C%BA%E5%A5%B3%E8%B4%A2%E7%A5%9E%E8%A2%AB%E6%B8%B8%E5%AE%A2%E8%BF%BD%E5%BE%97%E6%BB%A1%E5%9C%BA%E8%B7%91) |

### 凤凰网

| 排名 | 标题 |
|------|------|
| #1 | [7名中国游客在贝加尔湖溺亡，俄方：路线未经批准](https://news.ifeng.com/c/8qvY0GNd8tK) |
| #2 | [印度将购买委内瑞拉石油？美大使：正积极谈判](https://news.ifeng.com/c/8qveM9IjpX0) |
| #3 | [泰国智库批特朗普关税政策：别人在搭桥，美国在筑墙](https://news.ifeng.com/c/8qvXaKA67vQ) |
| #4 | [美大使：以色列拿下整个中东，也没问题](https://news.ifeng.com/c/8qvPCuKv7yI) |
| #5 | [学者：特朗普或遭众叛亲离](https://news.ifeng.com/c/8qvPCuKv7tH) |
| #6 | [“和平委员会”首次开会，48名代表身份藏玄机](https://news.ifeng.com/c/8qvTLaWprko) |
| #7 | [伊朗外长拒绝打开美方装有导弹提议的信函，并将其退回](https://news.ifeng.com/c/8qvb09i2f7O) |
| #8 | [多国敦促在伊朗公民尽快撤离](https://news.ifeng.com/c/8qurLBUotqV) |
| #9 | [美最高法院推翻特朗普关税，日本被曝打算咬牙继续落实贸易协议](https://news.ifeng.com/c/8qvhnjq5970) |
| #10 | [夫妻当街暴打15岁女孩，底气从何而来？](https://news.ifeng.com/c/8qvbbpgFD4Q) |

### 澎湃新闻

| 排名 | 标题 |
|------|------|
| #1 | [春启新程｜在上海的第15个春节，她说老人们这个时候更需要自己](https://www.thepaper.cn/newsDetail_forward_32635177) |
| #2 | [佩斯科夫：日本对俄罗斯一直充满敌意，俄日关系已跌至冰点](https://www.thepaper.cn/newsDetail_forward_32639569) |
| #3 | [释新闻｜美最高法院6比3裁定特朗普全球关税违法，意味着什么？](https://www.thepaper.cn/newsDetail_forward_32638670) |
| #4 | [2026春节档总场次刷新中国影史纪录](https://www.thepaper.cn/newsDetail_forward_32638734) |
| #5 | [电影《镖人》主演陈丽君人民日报撰文：感受中国人的侠义情怀](https://www.thepaper.cn/newsDetail_forward_32638815) |
| #6 | [张艺谋人民日报撰文：于无声处听惊雷](https://www.thepaper.cn/newsDetail_forward_32638642) |
| #7 | [视频丨硬核揭秘！福建舰“一马当先”底气何在？](https://www.thepaper.cn/newsDetail_forward_32638555) |
| #8 | [乘势而上｜专访董煜：投资于物和投资于人相结合，要瞄准人在各成长阶段的痛点难点](https://www.thepaper.cn/newsDetail_forward_32453643) |
| #9 | [读懂城市丨冬游西宁，“暖”由内而生](https://www.thepaper.cn/newsDetail_forward_32600881) |
| #10 | [放马过来，“申”情款待丨“马路艺术家”喊你街头寻“马”](https://www.thepaper.cn/newsDetail_forward_32543995) |

### 财联社热门

| 排名 | 标题 |
|------|------|
| #1 | [中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111) |
| #2 | [什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326) |
| #3 | [春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289) |
| #4 | [美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233) |
| #5 | [特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246) |
| #6 | [原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772) |
| #7 | [特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405) |
| #8 | [美股收盘：多重利空压顶华尔街情绪恶化 三大指数集体下跌](https://www.cls.cn/detail/2291935) |
| #9 | [“存储荒”愈演愈烈！三星HBM4据称涨价30% 韩国“芯片双雄”积极扩产](https://www.cls.cn/detail/2291781) |
| #10 | [没有方向盘、没有脚踏板，特斯拉新车来了](https://www.cls.cn/detail/2292285) |

### 华尔街见闻

| 排名 | 标题 |
|------|------|
| #1 | [1750亿美元“关税退款”！对美股是“财政刺激”，对美债是“增加债务”，对金银是“不确定性重来”](https://wallstreetcn.com/articles/3765925) |
| #2 | [美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8%](https://wallstreetcn.com/articles/3765902) |
| #3 | [得知高院否决关税那一刻，特朗普“气炸了”，“破口大骂”](https://wallstreetcn.com/articles/3765923) |
| #4 | [SK海力士高盛电话会：所有客户需求都无法满足，今年存储价格持续上涨](https://wallstreetcn.com/articles/3765932) |
| #5 | [俄罗斯央行1月卖出30万盎司黄金储备，价值达14亿美元](https://wallstreetcn.com/articles/3765931) |
| #6 | [高院否决、特朗普再加！美国关税税率现在变成什么样了？](https://wallstreetcn.com/articles/3765933) |
| #7 | [华尔街见闻早餐FM-Radio \| 2026年2月21日](https://wallstreetcn.com/articles/3765920) |
| #8 | [高盛：黄金波动性大幅走高，央行购金力度将暂时放缓](https://wallstreetcn.com/articles/3765934) |
| #9 | [高院否决，特朗普将被迫退税！华尔街“早就下注”，商务部长儿子甚至一度参与](https://wallstreetcn.com/articles/3765924) |
| #10 | [高院否决是"一回事"，美国退税是"另一回事”](https://wallstreetcn.com/articles/3765922) |

### bilibili 热搜

| 排名 | 标题 |
|------|------|
| #1 | [中国空中技巧队2金3铜](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%9B%BD%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E9%98%9F2%E9%87%913%E9%93%9C) |
| #2 | [王建华回应大状师翻红](https://search.bilibili.com/all?keyword=%E7%8E%8B%E5%BB%BA%E5%8D%8E%E5%9B%9E%E5%BA%94%E5%A4%A7%E7%8A%B6%E5%B8%88%E7%BF%BB%E7%BA%A2) |
| #3 | [中国队空中技巧混合团体摘铜](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%9B%BD%E9%98%9F%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E6%B7%B7%E5%90%88%E5%9B%A2%E4%BD%93%E6%91%98%E9%93%9C) |
| #4 | [苹果味饮品为何突然爆发](https://search.bilibili.com/all?keyword=%E8%8B%B9%E6%9E%9C%E5%91%B3%E9%A5%AE%E5%93%81%E4%B8%BA%E4%BD%95%E7%AA%81%E7%84%B6%E7%88%86%E5%8F%91) |
| #5 | [实测Gemini 3.1 Pro](https://search.bilibili.com/all?keyword=%E5%AE%9E%E6%B5%8BGemini+3.1+Pro) |
| #6 | [美国伊朗是否会达成协议](https://search.bilibili.com/all?keyword=%E7%BE%8E%E5%9B%BD%E4%BC%8A%E6%9C%97%E6%98%AF%E5%90%A6%E4%BC%9A%E8%BE%BE%E6%88%90%E5%8D%8F%E8%AE%AE) |
| #7 | [美国会返还关税吗](https://search.bilibili.com/all?keyword=%E7%BE%8E%E5%9B%BD%E4%BC%9A%E8%BF%94%E8%BF%98%E5%85%B3%E7%A8%8E%E5%90%97) |
| #8 | [GEN晋级全球先锋赛](https://search.bilibili.com/all?keyword=GEN%E6%99%8B%E7%BA%A7%E5%85%A8%E7%90%83%E5%85%88%E9%94%8B%E8%B5%9B) |
| #9 | [挑战在国外抓中国人共进年夜饭](https://search.bilibili.com/all?keyword=%E6%8C%91%E6%88%98%E5%9C%A8%E5%9B%BD%E5%A4%96%E6%8A%93%E4%B8%AD%E5%9B%BD%E4%BA%BA%E5%85%B1%E8%BF%9B%E5%B9%B4%E5%A4%9C%E9%A5%AD) |
| #10 | [星河入梦3200个特效镜头](https://search.bilibili.com/all?keyword=%E6%98%9F%E6%B2%B3%E5%85%A5%E6%A2%A63200%E4%B8%AA%E7%89%B9%E6%95%88%E9%95%9C%E5%A4%B4) |

### 知乎

| 排名 | 标题 |
|------|------|
| #1 | [研究发现瓶装水塑料颗粒是自来水的三倍，每次晃动会把塑料颗粒「抖」进水里，其他装食品的塑料也会这样吗？](https://www.zhihu.com/question/2004606914932262838) |
| #2 | [吴京说如果观众认可支持，会争取拍镖人第二部，你觉得有希望看到《镖人 2》吗？](https://www.zhihu.com/question/2008575802451649399) |
| #3 | [苹果官宣春季发布会 3 月 4 日落地上海，系首次在中国举办，对此你有哪些期待？](https://www.zhihu.com/question/2007050103865762395) |
| #4 | [说说你们压着 140Km/h 跑，到底油耗是多少？](https://www.zhihu.com/question/2004541528186581763) |
| #5 | [有哪些人生道理越早懂越好?](https://www.zhihu.com/question/1897799257186112744) |
| #6 | [白宫官员确认，美国总统特朗普计划于 3 月 31 日至 4 月 2 日访问中国，哪些信息值得关注？](https://www.zhihu.com/question/2008503061484631366) |
| #7 | [大一计算机新生怎么合理利用 GitHub？](https://www.zhihu.com/question/11379810074) |
| #8 | [掷圣杯，圣杯阴杯阳杯的概率是稳定的吗？连续八次阴杯的概率有多大？](https://www.zhihu.com/question/2008565406856603328) |
| #9 | [为什么开放的 Windows 战胜了封闭的 macOS，但是开放的 Android 却战胜不了封闭的 iOS？](https://www.zhihu.com/question/2007124650916856053) |
| #10 | [如何看待 UCSD 教授 J. E. Hirsch 关于「BCS 超导理论是个庞氏骗局」的系列文章？](https://www.zhihu.com/question/641430230) |

### 抖音

| 排名 | 标题 |
|------|------|
| #1 | [谷爱凌U型场地决赛推迟](https://www.douyin.com/hot/2408149) |
| #2 | [过年好像一场热闹的梦](https://www.douyin.com/hot/2407722) |
| #3 | [春节档电影总票房突破40亿元](https://www.douyin.com/hot/2408064) |
| #4 | [新春穿搭不重样挑战](https://www.douyin.com/hot/2407798) |
| #6 | [消息称美考虑打击哈梅内伊父子](https://www.douyin.com/hot/2407540) |
| #7 | [宁忠岩直播“验”冬奥金牌](https://www.douyin.com/hot/2408088) |
| #8 | [与中国短道速滑队同在](https://www.douyin.com/hot/2407267) |
| #9 | [王心迪夺冠后谈及徐梦桃](https://www.douyin.com/hot/2407334) |
| #10 | [水果烂一小块 削掉后能吃吗](https://www.douyin.com/hot/2408048) |
| #11 | [村里又恢复了往日的宁静](https://www.douyin.com/hot/2407877) |

### 贴吧

| 排名 | 标题 |
|------|------|
| #1 | [喂猫起争执,男子遭恶邻杀害](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%96%82%E7%8C%AB%E8%B5%B7%E4%BA%89%E6%89%A7%2C%E7%94%B7%E5%AD%90%E9%81%AD%E6%81%B6%E9%82%BB%E6%9D%80%E5%AE%B3&topic_id=28350838) |
| #2 | [春节闯关,神人亲戚大赏](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%98%A5%E8%8A%82%E9%97%AF%E5%85%B3%2C%E7%A5%9E%E4%BA%BA%E4%BA%B2%E6%88%9A%E5%A4%A7%E8%B5%8F&topic_id=28350839) |
| #3 | [夫妻暴打未成年,双双进局子](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%A4%AB%E5%A6%BB%E6%9A%B4%E6%89%93%E6%9C%AA%E6%88%90%E5%B9%B4%2C%E5%8F%8C%E5%8F%8C%E8%BF%9B%E5%B1%80%E5%AD%90&topic_id=28350837) |
| #4 | [空中技巧混团摘铜,瑞士人躺赢](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E6%B7%B7%E5%9B%A2%E6%91%98%E9%93%9C%2C%E7%91%9E%E5%A3%AB%E4%BA%BA%E8%BA%BA%E8%B5%A2&topic_id=28350834) |
| #5 | [错认国人,菲律宾女孩遭猎艳](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%94%99%E8%AE%A4%E5%9B%BD%E4%BA%BA%2C%E8%8F%B2%E5%BE%8B%E5%AE%BE%E5%A5%B3%E5%AD%A9%E9%81%AD%E7%8C%8E%E8%89%B3&topic_id=28350821) |
| #6 | [亲戚拜年不说话,沪漂了不起？](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E6%88%9A%E6%8B%9C%E5%B9%B4%E4%B8%8D%E8%AF%B4%E8%AF%9D%2C%E6%B2%AA%E6%BC%82%E4%BA%86%E4%B8%8D%E8%B5%B7%EF%BC%9F&topic_id=28350825) |
| #7 | [鸣潮没二创,二游痴急了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%B8%A3%E6%BD%AE%E6%B2%A1%E4%BA%8C%E5%88%9B%2C%E4%BA%8C%E6%B8%B8%E7%97%B4%E6%80%A5%E4%BA%86&topic_id=28350831) |
| #8 | [绿帽文争霸,新五绿诞生](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%BB%BF%E5%B8%BD%E6%96%87%E4%BA%89%E9%9C%B8%2C%E6%96%B0%E4%BA%94%E7%BB%BF%E8%AF%9E%E7%94%9F&topic_id=28350833) |
| #9 | [日企采用中国芯,岛民破防](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%97%A5%E4%BC%81%E9%87%87%E7%94%A8%E4%B8%AD%E5%9B%BD%E8%8A%AF%2C%E5%B2%9B%E6%B0%91%E7%A0%B4%E9%98%B2&topic_id=28350832) |
| #10 | [12人遇难!熊孩子放炮闯祸](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=12%E4%BA%BA%E9%81%87%E9%9A%BE%21%E7%86%8A%E5%AD%A9%E5%AD%90%E6%94%BE%E7%82%AE%E9%97%AF%E7%A5%B8&topic_id=28350829) |

### 微博

| 排名 | 标题 |
|------|------|
| #2 | [前方无厕所无烤肠无茶叶蛋](https://s.weibo.com/weibo?q=%23%E5%89%8D%E6%96%B9%E6%97%A0%E5%8E%95%E6%89%80%E6%97%A0%E7%83%A4%E8%82%A0%E6%97%A0%E8%8C%B6%E5%8F%B6%E8%9B%8B%23) |
| #3 | [热气腾腾的中国年](https://s.weibo.com/weibo?q=%23%E7%83%AD%E6%B0%94%E8%85%BE%E8%85%BE%E7%9A%84%E4%B8%AD%E5%9B%BD%E5%B9%B4%23) |
| #4 | [王传君录综艺崩溃爆哭](https://s.weibo.com/weibo?q=%E7%8E%8B%E4%BC%A0%E5%90%9B%E5%BD%95%E7%BB%BC%E8%89%BA%E5%B4%A9%E6%BA%83%E7%88%86%E5%93%AD) |
| #5 | [大年初六](https://s.weibo.com/weibo?q=%23%E5%A4%A7%E5%B9%B4%E5%88%9D%E5%85%AD%23) |
| #7 | [白鹿 我家923](https://s.weibo.com/weibo?q=%E7%99%BD%E9%B9%BF+%E6%88%91%E5%AE%B6923) |
| #8 | [辽宁春晚最大黑马小品以貌取人](https://s.weibo.com/weibo?q=%E8%BE%BD%E5%AE%81%E6%98%A5%E6%99%9A%E6%9C%80%E5%A4%A7%E9%BB%91%E9%A9%AC%E5%B0%8F%E5%93%81%E4%BB%A5%E8%B2%8C%E5%8F%96%E4%BA%BA) |
| #9 | [苏翊鸣闭幕式旗手](https://s.weibo.com/weibo?q=%23%E8%8B%8F%E7%BF%8A%E9%B8%A3%E9%97%AD%E5%B9%95%E5%BC%8F%E6%97%97%E6%89%8B%23) |
| #10 | [谷爱凌决赛时间](https://s.weibo.com/weibo?q=%E8%B0%B7%E7%88%B1%E5%87%8C%E5%86%B3%E8%B5%9B%E6%97%B6%E9%97%B4) |
| #11 | [齐思钧回应分手](https://s.weibo.com/weibo?q=%23%E9%BD%90%E6%80%9D%E9%92%A7%E5%9B%9E%E5%BA%94%E5%88%86%E6%89%8B%23) |

## 🔗 原始链接索引

### 🐦 Twitter 原文 (74/74 条)

- [2026-02-22T00:00 @akiko_lawson [热门] | 5日間限定の無料券チャレンジ(^^) 今日は冷凍米飯無料の最終日です♪ 1）このアカウントをフォロー 2）この投稿をリポスト 3）抽選で毎日1万名様に無料券！結果は自動でお知らせ](https://twitter.com/akiko_lawson/status/2025344790129455528)
- [2026-02-22T00:00 @needtheIight [热门] | ai lembrando desse print aqui...](https://twitter.com/needtheIight/status/2025044319095144644)
- [2026-02-22T00:00 @TadaaVoila [热门] | อย่าเลิกตามการเมืองเด็ดขาด คือพักได้แต่อย่าเลิก อย่าคิดว่าสังคมมันเฮงซวยเหมือนเดิม ถ้าวันน...](https://twitter.com/TadaaVoila/status/2025115801377022067)
- [2026-02-22T00:00 @pupxtra_ [热门] | i ♥️ nerds](https://twitter.com/pupxtra_/status/2025014218282471547)
- [2026-02-22T00:00 @WhiteHouse [热门] | TRUST IN TRUMP 🔥 A busy week at the White House 🕊️ Inaugural Board of Peace 🏭 Georgia Visi...](https://twitter.com/WhiteHouse/status/2025292911903212018)
- [2026-02-22T00:00 @kaaleeby [热门] | Ai calica eu grito Ave Maria Ela joga a raba e depois vai pra missa Aí danada, ela não é s...](https://twitter.com/kaaleeby/status/2025033822920647153)
- [2026-02-22T00:00 @nikkei [热门] | 衆議院選挙、中国系400アカウントが「反高市工作」 AIで巧妙にnikkei.com/article/DGXZTS000…](https://twitter.com/nikkei/status/2025309061068067168)
- [2026-02-22T00:00 @mcafeenew [热门] | 🚨BOMBSHELL ALERT: BERNIE SANDERS EXPOSED IN MASSIVE CHINA SCANDAL! 🔗t.me/+bWjXP07v90xlYWFk...](https://twitter.com/mcafeenew/status/2025280842499531121)
- [2026-02-22T00:00 @bitget [热门] | Level up your trading on Bitget stock perps With ultra-low fees, you can seize every marke...](https://twitter.com/bitget/status/2023336325282508801)
- [2026-02-22T00:00 @Gaurab [热门] | Nittobo is a Japanese glass fiber company with 2,745 employees. Nvidia, Apple, Google, Ama...](https://twitter.com/Gaurab/status/2024959539511275769)
- [2026-02-22T00:00 @culianax [热门] | ai gente 😭😭😭](https://twitter.com/culianax/status/2025020394143416385)
- [2026-02-22T00:00 @EshaAA33 [热门] | BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hid...](https://twitter.com/EshaAA33/status/2025147573838000572)
- [2026-02-22T00:00 @RapidResponse47 [热门] | "38% of American families have no exposure to the U.S. stock market... and with@TrumpAccou...](https://twitter.com/RapidResponse47/status/2024958380847095954)
- [2026-02-22T00:00 @TheProfInvestor [热门] | Here are some basic rules: When insiders buy, you pay attention. Stock gets below 200-week...](https://twitter.com/TheProfInvestor/status/2024640490617049561)
- [2026-02-22T00:00 @xMarketNews [热门] | SOUTH KOREA STOCK MARKET HAS SURGED NEARLY 150% SINCE THEY TOOK ACTION AGAINST NAKED SHORT...](https://twitter.com/xMarketNews/status/2025296878707913043)
- [2026-02-22T00:00 @agentjay2009 [热门] | This economic disaster is also a natural security debacle! Asim Munir’s SIFC has failed mi...](https://twitter.com/agentjay2009/status/2025287147159228776)
- [2026-02-22T00:00 @Barchart [热门] | 2 years ago, PayPal’s CEO said “we will shock the world.”$PYPLhas plunged more than 30% si...](https://twitter.com/Barchart/status/2025185172958683287)
- [2026-02-22T00:00 @_yayeezy [热门] | RT@6uhle: AI videos usually piss me tf off but this is KILLINGGG me 😭😭😭😭😭](https://twitter.com/_yayeezy/status/2025360031646904504)
- [2026-02-22T00:00 @hNzisacVzBB1QR1 [热门] | RT@shinjirokoiz: 防衛省AIチームの皆さんから答弁作成ツールを実際に使いながら説明を受けました。職員曰く、一度使ったらもう今までの答弁作成には戻れないそうです。新た...](https://twitter.com/hNzisacVzBB1QR1/status/2025360028799279490)
- [2026-02-22T00:00 @WiganAndrew [热门] | Not a peep from Charlie and Naga. If it was bad news for the economy, they would have run ...](https://twitter.com/WiganAndrew/status/2025144052266504530)
- [2026-02-22T00:00 @Suzierizzo1 [热门] | Jacob Kunzelman was on a flight from Orlando to Philly & so was Kelsey Zwick with her 11 m...](https://twitter.com/Suzierizzo1/status/2025310992431992878)
- [2026-02-22T00:00 @Sssebi [热门] | The secret ingredients that will send$ADAto $10 in the next bull rally. - USDCx - Midnight...](https://twitter.com/Sssebi/status/2025244121456124243)
- [2026-02-22T00:00 @xMarketNews [热门] | $2 BILLION SHARES SOLD SHORT 🚨 Hims & Hers currently has the highest short interest (40%) ...](https://twitter.com/xMarketNews/status/2025235349241274552)
- [2026-02-22T00:00 @kouamouo [热门] | J'ai été témoin de cette scène d'agression policière sur un livreur dans un quartier absol...](https://twitter.com/kouamouo/status/2025316094156657080)
- [2026-02-22T00:00 @Maks_NAFO_FELLA [热门] | 🇺🇦🇺🇸🙏 Sybiha: Today, Russia struck another American business in Ukraine—a civilian product...](https://twitter.com/Maks_NAFO_FELLA/status/2025330784047882654)
- [2026-02-22T00:00 @0xLofty [热门] | Another MASSIVE Bitcoin dump starts next week... If the pattern holds,$BTCwill drop to $35...](https://twitter.com/0xLofty/status/2025291630098395332)
- [2026-02-22T00:00 @BakwasNaKarain [热门] | Stock market dropping. Inflation at all times high. Poverty touching new highs. Daily terr...](https://twitter.com/BakwasNaKarain/status/2025219053111902298)
- [2026-02-22T00:00 @OG_DrC [热门] | They passed Paul Warburg’s federal reserve act of 1913, handing over Americas gold and sil...](https://twitter.com/OG_DrC/status/1824655185525752229)
- [2026-02-22T00:00 @danroodt [热门] | Another day, another water protest in Johannesburg. No water. That is what you call "democ...](https://twitter.com/danroodt/status/2025191584526926010)
- [2026-02-22T00:00 @tokyorosiecr [热门] | ETH fees into NVIDIA & TESLA? No joke, it's really happening.$ONDOsummit is live with 10% ...](https://twitter.com/tokyorosiecr/status/2025359801715441781)
- [2026-02-22T00:00 @NikkeiAsia [关注] | LISTEN: Nikkei Asia News Roundup Indonesian coffee chains test overseas tastes in global e...](https://twitter.com/NikkeiAsia/status/2025359906874773859)
- [2026-02-22T00:00 @NikkeiAsia [关注] | This was our most read opinion piece for the week. Xi's anti-corruption drive has removed ...](https://twitter.com/NikkeiAsia/status/2025359894111547504)
- [2026-02-21T23:48 @SCMPNews [关注] | ‘I could not walk’: how exercise helped a mother manage serious knee pain https://www.scmp...](https://twitter.com/SCMPNews/status/2025356993054060853)
- [2026-02-21T23:26 @NikkeiAsia [关注] | 10 Japan trips for fun in the snow -- not just skiing Ride, trek or float through some of ...](https://twitter.com/NikkeiAsia/status/2025351431524393000)
- [2026-02-21T23:09 @NikkeiAsia [关注] | Chinese consumers snap up gold jewelry merch for fandom and investment https://s.nikkei.co...](https://twitter.com/NikkeiAsia/status/2025347244006703259)
- [2026-02-21T23:00 @NikkeiAsia [关注] | Japan has cut its rare-earth dependence on China from around 90% to only about 60% in 15 y...](https://twitter.com/NikkeiAsia/status/2025345019733737791)
- [2026-02-21T22:16 @NikkeiAsia [关注] | Japan PM Takaichi chases mentor Abe's dream Cost-of-living crisis an early obstacle to cem...](https://twitter.com/NikkeiAsia/status/2025333920078717048)
- [2026-02-21T22:03 @SCMPNews [关注] | K-pop’s big freeze: are cracks in China’s cultural blockade a thaw? https://www.scmp.com/n...](https://twitter.com/SCMPNews/status/2025330439146053909)
- [2026-02-21T22:00 @WuBlockchain [关注] | CZ: Real Capital and Builders Will Shift Focus to RWA and Prediction Markets On February 1...](https://twitter.com/WuBlockchain/status/2025329686352695722)
- [2026-02-21T21:53 @SCMPNews [关注] | US ambassador says Israel has right to much of Middle East, sparking uproar https://www.sc...](https://twitter.com/SCMPNews/status/2025328001559237020)
- [2026-02-21T21:22 @NikkeiAsia [关注] | Sri Lanka rolls out red carpet to investors for $15bn Port City Project that began as part...](https://twitter.com/NikkeiAsia/status/2025320133732827155)
- [2026-02-21T21:00 @NikkeiAsia [关注] | Why are Taiwan's Nvidia suppliers investing billions in the US? Jensen Huang lauds island'...](https://twitter.com/NikkeiAsia/status/2025314778684469608)
- [2026-02-21T20:40 @ReutersBiz [关注] | WATCH:President Trump said he will raise a temporary tariff from 10% to 15% on US imports ...](https://twitter.com/ReutersBiz/status/2025309551692525586)
- [2026-02-21T20:07 @NikkeiAsia [关注] | Yoon Suk Yeol's verdict is a test for South Korean democracy https://s.nikkei.com/3Oq1Wnu](https://twitter.com/NikkeiAsia/status/2025301421474672994)
- [2026-02-21T19:09 @WSJ [关注] | From http://localhost/WSJFreeEx via http://localhost/WSJopinion: While new AI technologies...](https://twitter.com/WSJ/status/2025286674926682276)
- [2026-02-21T19:00 @WuBlockchain [关注] | CZ on Life After Immigrating to Canada: Mom Worked in a Sewing Factory, I Worked at McDona...](https://twitter.com/WuBlockchain/status/2025284391400804461)
- [2026-02-21T18:48 @WSJ [关注] | From http://localhost/WSJFreeEx via http://localhost/WSJopinion: Elite female athletes oft...](https://twitter.com/WSJ/status/2025281614184391153)
- [2026-02-21T18:27 @WSJ [关注] | From http://localhost/WSJopinion: Rubio Plays Good Cop to Vance’s Bad by http://localhost/...](https://twitter.com/WSJ/status/2025276147626369422)
- [2026-02-21T18:26 @PeterSchiff [关注] | So happy to have this original Market Price in our living room in our Puerto Rico home. ht...](https://twitter.com/PeterSchiff/status/2025275961499898071)
- [2026-02-21T18:14 @SCMPNews [关注] | Bus with Chinese tourists crashes through ice on Russia’s Lake Baikal, killing 8 https://w...](https://twitter.com/SCMPNews/status/2025272809157427458)
- [2026-02-21T18:11 @SCMPNews [关注] | Nasa moon rocket hit by new problem, pushing launch with astronauts into April https://www...](https://twitter.com/SCMPNews/status/2025272159598203258)
- [2026-02-21T18:06 @WSJ [关注] | From http://localhost/WSJopinion: The Warner Bros. fight isn’t over. Investors start to se...](https://twitter.com/WSJ/status/2025270909678825560)
- [2026-02-21T17:44 @WSJ [关注] | From http://localhost/WSJopinion: Christianity isn’t dead in the West. Marco Rubio rightly...](https://twitter.com/WSJ/status/2025265352406397154)
- [2026-02-21T17:32 @CNBC [关注] | Airlines waive change fees ahead of another monster winter storm https://www.cnbc.com/2026...](https://twitter.com/CNBC/status/2025262275263598924)
- [2026-02-21T17:24 @WSJ [关注] | From http://localhost/WSJFreeEx via http://localhost/WSJopinion: As we brace for AI’s domi...](https://twitter.com/WSJ/status/2025260249796473140)
- [2026-02-21T17:11 @NikkeiAsia [关注] | Trump now wants to impose 15% tariff after Supreme Court decision https://s.nikkei.com/4kN...](https://twitter.com/NikkeiAsia/status/2025257008455184574)
- [2026-02-21T17:02 @WSJ [关注] | In the original Game of Life, players could land on some disheartening spaces, including R...](https://twitter.com/WSJ/status/2025254899399737504)
- [2026-02-21T16:59 @WSJ [关注] | From http://localhost/WSJopinion: America’s economic strength rests on sustained capital i...](https://twitter.com/WSJ/status/2025253941060030607)
- [2026-02-21T16:37 @WSJ [关注] | A Yale professor's new investment formula says you're too light on stocks. Here's how it w...](https://twitter.com/WSJ/status/2025248440641262020)
- [2026-02-21T16:21 @SCMPNews [关注] | Breaking | Trump says raising US global tariff rate from 10 to 15 per cent https://www.scm...](https://twitter.com/SCMPNews/status/2025244390210273757)
- [2026-02-21T16:17 @BNONews [关注] | JUST IN: Trump says 10% worldwide tariff rate announced yesterday will rise to 15% "effect...](https://twitter.com/BNONews/status/2025243509314519504)
- [2026-02-21T16:14 @WSJ [关注] | More college kids than ever claim to have disabilities. But what is lost when we allow the...](https://twitter.com/WSJ/status/2025242855577370705)
- [2026-02-21T16:04 @WuBlockchain [关注] | Vitalik Buterin published a post stating that the core issue of current decentralized gove...](https://twitter.com/WuBlockchain/status/2025240326533997000)
- [2026-02-21T16:01 @ylecun [关注] | Corruption Meet Kevin (@realMeetKevin) 🚨 Howard Lutnick's family firm bought up the rights...](https://twitter.com/ylecun/status/2025239374930346300)
- [2026-02-21T15:11 @SCMPNews [关注] | Wang Fuk Court buyback plan disappoints some residents despite ‘generous’ offer https://ww...](https://twitter.com/SCMPNews/status/2025226870355079543)
- [2026-02-21T15:09 @SoberLook [关注] | 🇺🇸 US high-frequency dashboard, composed of daily and weekly economic indicators (updated ...](https://twitter.com/SoberLook/status/2025226354732490914)
- [2026-02-21T15:05 @VitalikButerin [关注] | "AI becomes the government" is dystopian: it leads to slop when AI is weak, and is doom-ma...](https://twitter.com/VitalikButerin/status/2025225247088402581)
- [2026-02-21T15:03 @CNBC [关注] | This week’s most overbought stocks include Deere and Quanta Services https://www.cnbc.com/...](https://twitter.com/CNBC/status/2025224781507760636)
- [2026-02-21T14:54 @CNBC [关注] | Five key takeaways from the Supreme Court's landmark decision against Trump's tariffs http...](https://twitter.com/CNBC/status/2025222719990616196)
- [2026-02-21T14:52 @CNBC [关注] | Bank of America names five stocks best positioned for shareholder returns https://www.cnbc...](https://twitter.com/CNBC/status/2025222182746353852)
- [2026-02-21T14:44 @CNBC [关注] | Trump accounts have 'more unanswered questions than answered,' expert says. What's still u...](https://twitter.com/CNBC/status/2025219993550434394)
- [2026-02-21T14:43 @CNBC [关注] | Berkshire was a net seller of stocks in Buffett's final quarter as CEO https://www.cnbc.co...](https://twitter.com/CNBC/status/2025219718529843381)
- [2026-02-21T13:12 @CNBC [关注] | Under mounting toy pressures, Hasbro has a secret sauce that Mattel hasn't matched https:/...](https://twitter.com/CNBC/status/2025197017861951605)
- [2026-02-21T13:12 @globaltimesnews [关注] | China won the bronze medal in the freestyle skiing mixed team aerials of the Milan-Cortina...](https://twitter.com/globaltimesnews/status/2025196856264028574)

### 📱 微信公众号原文 (0/0 条)

- 暂无可用链接

### 🔥 NewsNow 原文 (120/120 条)

- [今日头条 #1 | 男子自驾游开10小时后弃车换高铁](https://www.toutiao.com/trending/7608953617383587886/)
- [百度热搜 #1 | “前方无厕所、无烤肠、无茶叶蛋”](https://www.baidu.com/s?wd=%E2%80%9C%E5%89%8D%E6%96%B9%E6%97%A0%E5%8E%95%E6%89%80%E3%80%81%E6%97%A0%E7%83%A4%E8%82%A0%E3%80%81%E6%97%A0%E8%8C%B6%E5%8F%B6%E8%9B%8B%E2%80%9D)
- [凤凰网 #1 | 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准](https://news.ifeng.com/c/8qvY0GNd8tK)
- [澎湃新闻 #1 | 春启新程｜在上海的第15个春节，她说老人们这个时候更需要自己](https://www.thepaper.cn/newsDetail_forward_32635177)
- [财联社热门 #1 | 中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111)
- [华尔街见闻 #1 | 1750亿美元“关税退款”！对美股是“财政刺激”，对美债是“增加债务”，对金银是“不确定性重来”](https://wallstreetcn.com/articles/3765925)
- [bilibili 热搜 #1 | 中国空中技巧队2金3铜](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%9B%BD%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E9%98%9F2%E9%87%913%E9%93%9C)
- [知乎 #1 | 研究发现瓶装水塑料颗粒是自来水的三倍，每次晃动会把塑料颗粒「抖」进水里，其他装食品的塑料也会这样吗？](https://www.zhihu.com/question/2004606914932262838)
- [抖音 #1 | 谷爱凌U型场地决赛推迟](https://www.douyin.com/hot/2408149)
- [贴吧 #1 | 喂猫起争执,男子遭恶邻杀害](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%96%82%E7%8C%AB%E8%B5%B7%E4%BA%89%E6%89%A7%2C%E7%94%B7%E5%AD%90%E9%81%AD%E6%81%B6%E9%82%BB%E6%9D%80%E5%AE%B3&topic_id=28350838)
- [微博 #2 | 前方无厕所无烤肠无茶叶蛋](https://s.weibo.com/weibo?q=%23%E5%89%8D%E6%96%B9%E6%97%A0%E5%8E%95%E6%89%80%E6%97%A0%E7%83%A4%E8%82%A0%E6%97%A0%E8%8C%B6%E5%8F%B6%E8%9B%8B%23)
- [华尔街见闻 #2 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8%](https://wallstreetcn.com/articles/3765902)
- [百度热搜 #2 | 山东网友自驾去重庆 开了10小时弃车](https://www.baidu.com/s?wd=%E5%B1%B1%E4%B8%9C%E7%BD%91%E5%8F%8B%E8%87%AA%E9%A9%BE%E5%8E%BB%E9%87%8D%E5%BA%86+%E5%BC%80%E4%BA%8610%E5%B0%8F%E6%97%B6%E5%BC%83%E8%BD%A6)
- [凤凰网 #2 | 印度将购买委内瑞拉石油？美大使：正积极谈判](https://news.ifeng.com/c/8qveM9IjpX0)
- [财联社热门 #2 | 什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326)
- [抖音 #2 | 过年好像一场热闹的梦](https://www.douyin.com/hot/2407722)
- [bilibili 热搜 #2 | 王建华回应大状师翻红](https://search.bilibili.com/all?keyword=%E7%8E%8B%E5%BB%BA%E5%8D%8E%E5%9B%9E%E5%BA%94%E5%A4%A7%E7%8A%B6%E5%B8%88%E7%BF%BB%E7%BA%A2)
- [知乎 #2 | 吴京说如果观众认可支持，会争取拍镖人第二部，你觉得有希望看到《镖人 2》吗？](https://www.zhihu.com/question/2008575802451649399)
- [贴吧 #2 | 春节闯关,神人亲戚大赏](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%98%A5%E8%8A%82%E9%97%AF%E5%85%B3%2C%E7%A5%9E%E4%BA%BA%E4%BA%B2%E6%88%9A%E5%A4%A7%E8%B5%8F&topic_id=28350839)
- [今日头条 #2 | 钱到底还要不要存银行](https://www.toutiao.com/trending/7609305215459659302/)
- [澎湃新闻 #2 | 佩斯科夫：日本对俄罗斯一直充满敌意，俄日关系已跌至冰点](https://www.thepaper.cn/newsDetail_forward_32639569)
- [bilibili 热搜 #3 | 中国队空中技巧混合团体摘铜](https://search.bilibili.com/all?keyword=%E4%B8%AD%E5%9B%BD%E9%98%9F%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E6%B7%B7%E5%90%88%E5%9B%A2%E4%BD%93%E6%91%98%E9%93%9C)
- [澎湃新闻 #3 | 释新闻｜美最高法院6比3裁定特朗普全球关税违法，意味着什么？](https://www.thepaper.cn/newsDetail_forward_32638670)
- [百度热搜 #3 | “赛博”中国年](https://www.baidu.com/s?wd=%E2%80%9C%E8%B5%9B%E5%8D%9A%E2%80%9D%E4%B8%AD%E5%9B%BD%E5%B9%B4)
- [抖音 #3 | 春节档电影总票房突破40亿元](https://www.douyin.com/hot/2408064)
- [微博 #3 | 热气腾腾的中国年](https://s.weibo.com/weibo?q=%23%E7%83%AD%E6%B0%94%E8%85%BE%E8%85%BE%E7%9A%84%E4%B8%AD%E5%9B%BD%E5%B9%B4%23)
- [今日头条 #3 | 春节哪些景点更热门？一组数据盘点](https://www.toutiao.com/trending/7608388814415072787/)
- [凤凰网 #3 | 泰国智库批特朗普关税政策：别人在搭桥，美国在筑墙](https://news.ifeng.com/c/8qvXaKA67vQ)
- [华尔街见闻 #3 | 得知高院否决关税那一刻，特朗普“气炸了”，“破口大骂”](https://wallstreetcn.com/articles/3765923)
- [财联社热门 #3 | 春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289)
- [知乎 #3 | 苹果官宣春季发布会 3 月 4 日落地上海，系首次在中国举办，对此你有哪些期待？](https://www.zhihu.com/question/2007050103865762395)
- [贴吧 #3 | 夫妻暴打未成年,双双进局子](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%A4%AB%E5%A6%BB%E6%9A%B4%E6%89%93%E6%9C%AA%E6%88%90%E5%B9%B4%2C%E5%8F%8C%E5%8F%8C%E8%BF%9B%E5%B1%80%E5%AD%90&topic_id=28350837)
- [贴吧 #4 | 空中技巧混团摘铜,瑞士人躺赢](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%A9%BA%E4%B8%AD%E6%8A%80%E5%B7%A7%E6%B7%B7%E5%9B%A2%E6%91%98%E9%93%9C%2C%E7%91%9E%E5%A3%AB%E4%BA%BA%E8%BA%BA%E8%B5%A2&topic_id=28350834)
- [澎湃新闻 #4 | 2026春节档总场次刷新中国影史纪录](https://www.thepaper.cn/newsDetail_forward_32638734)
- [财联社热门 #4 | 美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233)
- [百度热搜 #4 | 游客挤到悔不当初不如在家刷手机](https://www.baidu.com/s?wd=%E6%B8%B8%E5%AE%A2%E6%8C%A4%E5%88%B0%E6%82%94%E4%B8%8D%E5%BD%93%E5%88%9D%E4%B8%8D%E5%A6%82%E5%9C%A8%E5%AE%B6%E5%88%B7%E6%89%8B%E6%9C%BA)
- [凤凰网 #4 | 美大使：以色列拿下整个中东，也没问题](https://news.ifeng.com/c/8qvPCuKv7yI)
- [抖音 #4 | 新春穿搭不重样挑战](https://www.douyin.com/hot/2407798)
- [华尔街见闻 #4 | SK海力士高盛电话会：所有客户需求都无法满足，今年存储价格持续上涨](https://wallstreetcn.com/articles/3765932)
- [知乎 #4 | 说说你们压着 140Km/h 跑，到底油耗是多少？](https://www.zhihu.com/question/2004541528186581763)
- [bilibili 热搜 #4 | 苹果味饮品为何突然爆发](https://search.bilibili.com/all?keyword=%E8%8B%B9%E6%9E%9C%E5%91%B3%E9%A5%AE%E5%93%81%E4%B8%BA%E4%BD%95%E7%AA%81%E7%84%B6%E7%88%86%E5%8F%91)
- [微博 #4 | 王传君录综艺崩溃爆哭](https://s.weibo.com/weibo?q=%E7%8E%8B%E4%BC%A0%E5%90%9B%E5%BD%95%E7%BB%BC%E8%89%BA%E5%B4%A9%E6%BA%83%E7%88%86%E5%93%AD)
- [今日头条 #4 | 00后女孩月租200住养老院两年](https://www.toutiao.com/trending/7609139159411753014/)
- [贴吧 #5 | 错认国人,菲律宾女孩遭猎艳](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%94%99%E8%AE%A4%E5%9B%BD%E4%BA%BA%2C%E8%8F%B2%E5%BE%8B%E5%AE%BE%E5%A5%B3%E5%AD%A9%E9%81%AD%E7%8C%8E%E8%89%B3&topic_id=28350821)
- [财联社热门 #5 | 特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246)
- [凤凰网 #5 | 学者：特朗普或遭众叛亲离](https://news.ifeng.com/c/8qvPCuKv7tH)
- [华尔街见闻 #5 | 俄罗斯央行1月卖出30万盎司黄金储备，价值达14亿美元](https://wallstreetcn.com/articles/3765931)
- [澎湃新闻 #5 | 电影《镖人》主演陈丽君人民日报撰文：感受中国人的侠义情怀](https://www.thepaper.cn/newsDetail_forward_32638815)
- [bilibili 热搜 #5 | 实测Gemini 3.1 Pro](https://search.bilibili.com/all?keyword=%E5%AE%9E%E6%B5%8BGemini+3.1+Pro)
- [今日头条 #5 | 中国体育史上六对奥运金牌夫妇](https://www.toutiao.com/trending/7607817106020945427/)
- [知乎 #5 | 有哪些人生道理越早懂越好?](https://www.zhihu.com/question/1897799257186112744)
- [微博 #5 | 大年初六](https://s.weibo.com/weibo?q=%23%E5%A4%A7%E5%B9%B4%E5%88%9D%E5%85%AD%23)
- [百度热搜 #5 | “假蔡明”被送给了真蔡明](https://www.baidu.com/s?wd=%E2%80%9C%E5%81%87%E8%94%A1%E6%98%8E%E2%80%9D%E8%A2%AB%E9%80%81%E7%BB%99%E4%BA%86%E7%9C%9F%E8%94%A1%E6%98%8E)
- [贴吧 #6 | 亲戚拜年不说话,沪漂了不起？](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E6%88%9A%E6%8B%9C%E5%B9%B4%E4%B8%8D%E8%AF%B4%E8%AF%9D%2C%E6%B2%AA%E6%BC%82%E4%BA%86%E4%B8%8D%E8%B5%B7%EF%BC%9F&topic_id=28350825)
- [凤凰网 #6 | “和平委员会”首次开会，48名代表身份藏玄机](https://news.ifeng.com/c/8qvTLaWprko)
- [抖音 #6 | 消息称美考虑打击哈梅内伊父子](https://www.douyin.com/hot/2407540)
- [澎湃新闻 #6 | 张艺谋人民日报撰文：于无声处听惊雷](https://www.thepaper.cn/newsDetail_forward_32638642)
- [财联社热门 #6 | 原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772)
- [知乎 #6 | 白宫官员确认，美国总统特朗普计划于 3 月 31 日至 4 月 2 日访问中国，哪些信息值得关注？](https://www.zhihu.com/question/2008503061484631366)
- [百度热搜 #6 | 哈尔滨冰雪大世界：正式闭园](https://www.baidu.com/s?wd=%E5%93%88%E5%B0%94%E6%BB%A8%E5%86%B0%E9%9B%AA%E5%A4%A7%E4%B8%96%E7%95%8C%EF%BC%9A%E6%AD%A3%E5%BC%8F%E9%97%AD%E5%9B%AD)
- [bilibili 热搜 #6 | 美国伊朗是否会达成协议](https://search.bilibili.com/all?keyword=%E7%BE%8E%E5%9B%BD%E4%BC%8A%E6%9C%97%E6%98%AF%E5%90%A6%E4%BC%9A%E8%BE%BE%E6%88%90%E5%8D%8F%E8%AE%AE)
- [今日头条 #6 | 杨幂带火白绿条纹吊带裙](https://www.toutiao.com/trending/7608917512491221055/)
- [华尔街见闻 #6 | 高院否决、特朗普再加！美国关税税率现在变成什么样了？](https://wallstreetcn.com/articles/3765933)
- [今日头条 #7 | 网友家有个塑料盆用了40多年仍完好](https://www.toutiao.com/trending/7609287094111944714/)
- [微博 #7 | 白鹿 我家923](https://s.weibo.com/weibo?q=%E7%99%BD%E9%B9%BF+%E6%88%91%E5%AE%B6923)
- [贴吧 #7 | 鸣潮没二创,二游痴急了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%B8%A3%E6%BD%AE%E6%B2%A1%E4%BA%8C%E5%88%9B%2C%E4%BA%8C%E6%B8%B8%E7%97%B4%E6%80%A5%E4%BA%86&topic_id=28350831)
- [澎湃新闻 #7 | 视频丨硬核揭秘！福建舰“一马当先”底气何在？](https://www.thepaper.cn/newsDetail_forward_32638555)
- [凤凰网 #7 | 伊朗外长拒绝打开美方装有导弹提议的信函，并将其退回](https://news.ifeng.com/c/8qvb09i2f7O)
- [华尔街见闻 #7 | 华尔街见闻早餐FM-Radio | 2026年2月21日](https://wallstreetcn.com/articles/3765920)
- [抖音 #7 | 宁忠岩直播“验”冬奥金牌](https://www.douyin.com/hot/2408088)
- [bilibili 热搜 #7 | 美国会返还关税吗](https://search.bilibili.com/all?keyword=%E7%BE%8E%E5%9B%BD%E4%BC%9A%E8%BF%94%E8%BF%98%E5%85%B3%E7%A8%8E%E5%90%97)
- [知乎 #7 | 大一计算机新生怎么合理利用 GitHub？](https://www.zhihu.com/question/11379810074)
- [财联社热门 #7 | 特朗普：原本10%的全球进口关税税率将升至15%](https://www.cls.cn/detail/2292405)
- [百度热搜 #7 | 中国有六对奥运金牌夫妇](https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E6%9C%89%E5%85%AD%E5%AF%B9%E5%A5%A5%E8%BF%90%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%87)
- [bilibili 热搜 #8 | GEN晋级全球先锋赛](https://search.bilibili.com/all?keyword=GEN%E6%99%8B%E7%BA%A7%E5%85%A8%E7%90%83%E5%85%88%E9%94%8B%E8%B5%9B)
- [今日头条 #8 | 专家解读本次沙尘天气从何而来](https://www.toutiao.com/trending/7609308817964289586/)
- [贴吧 #8 | 绿帽文争霸,新五绿诞生](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%BB%BF%E5%B8%BD%E6%96%87%E4%BA%89%E9%9C%B8%2C%E6%96%B0%E4%BA%94%E7%BB%BF%E8%AF%9E%E7%94%9F&topic_id=28350833)
- [微博 #8 | 辽宁春晚最大黑马小品以貌取人](https://s.weibo.com/weibo?q=%E8%BE%BD%E5%AE%81%E6%98%A5%E6%99%9A%E6%9C%80%E5%A4%A7%E9%BB%91%E9%A9%AC%E5%B0%8F%E5%93%81%E4%BB%A5%E8%B2%8C%E5%8F%96%E4%BA%BA)
- [财联社热门 #8 | 美股收盘：多重利空压顶华尔街情绪恶化 三大指数集体下跌](https://www.cls.cn/detail/2291935)
- [凤凰网 #8 | 多国敦促在伊朗公民尽快撤离](https://news.ifeng.com/c/8qurLBUotqV)
- [澎湃新闻 #8 | 乘势而上｜专访董煜：投资于物和投资于人相结合，要瞄准人在各成长阶段的痛点难点](https://www.thepaper.cn/newsDetail_forward_32453643)
- [抖音 #8 | 与中国短道速滑队同在](https://www.douyin.com/hot/2407267)
- [百度热搜 #8 | 83岁外婆拿竹扫帚给孙女洗车](https://www.baidu.com/s?wd=83%E5%B2%81%E5%A4%96%E5%A9%86%E6%8B%BF%E7%AB%B9%E6%89%AB%E5%B8%9A%E7%BB%99%E5%AD%99%E5%A5%B3%E6%B4%97%E8%BD%A6)
- [知乎 #8 | 掷圣杯，圣杯阴杯阳杯的概率是稳定的吗？连续八次阴杯的概率有多大？](https://www.zhihu.com/question/2008565406856603328)
- [华尔街见闻 #8 | 高盛：黄金波动性大幅走高，央行购金力度将暂时放缓](https://wallstreetcn.com/articles/3765934)
- [知乎 #9 | 为什么开放的 Windows 战胜了封闭的 macOS，但是开放的 Android 却战胜不了封闭的 iOS？](https://www.zhihu.com/question/2007124650916856053)
- [今日头条 #9 | 黑龙江现大型动物咬死小牛](https://www.toutiao.com/trending/7609294060034375716/)
- [贴吧 #9 | 日企采用中国芯,岛民破防](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%97%A5%E4%BC%81%E9%87%87%E7%94%A8%E4%B8%AD%E5%9B%BD%E8%8A%AF%2C%E5%B2%9B%E6%B0%91%E7%A0%B4%E9%98%B2&topic_id=28350832)
- [百度热搜 #9 | “天下第一财神庙”被游客挤爆](https://www.baidu.com/s?wd=%E2%80%9C%E5%A4%A9%E4%B8%8B%E7%AC%AC%E4%B8%80%E8%B4%A2%E7%A5%9E%E5%BA%99%E2%80%9D%E8%A2%AB%E6%B8%B8%E5%AE%A2%E6%8C%A4%E7%88%86)
- [抖音 #9 | 王心迪夺冠后谈及徐梦桃](https://www.douyin.com/hot/2407334)
- [财联社热门 #9 | “存储荒”愈演愈烈！三星HBM4据称涨价30% 韩国“芯片双雄”积极扩产](https://www.cls.cn/detail/2291781)
- [凤凰网 #9 | 美最高法院推翻特朗普关税，日本被曝打算咬牙继续落实贸易协议](https://news.ifeng.com/c/8qvhnjq5970)
- [澎湃新闻 #9 | 读懂城市丨冬游西宁，“暖”由内而生](https://www.thepaper.cn/newsDetail_forward_32600881)
- [bilibili 热搜 #9 | 挑战在国外抓中国人共进年夜饭](https://search.bilibili.com/all?keyword=%E6%8C%91%E6%88%98%E5%9C%A8%E5%9B%BD%E5%A4%96%E6%8A%93%E4%B8%AD%E5%9B%BD%E4%BA%BA%E5%85%B1%E8%BF%9B%E5%B9%B4%E5%A4%9C%E9%A5%AD)
- [华尔街见闻 #9 | 高院否决，特朗普将被迫退税！华尔街“早就下注”，商务部长儿子甚至一度参与](https://wallstreetcn.com/articles/3765924)
- [微博 #9 | 苏翊鸣闭幕式旗手](https://s.weibo.com/weibo?q=%23%E8%8B%8F%E7%BF%8A%E9%B8%A3%E9%97%AD%E5%B9%95%E5%BC%8F%E6%97%97%E6%89%8B%23)
- [贴吧 #10 | 12人遇难!熊孩子放炮闯祸](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=12%E4%BA%BA%E9%81%87%E9%9A%BE%21%E7%86%8A%E5%AD%A9%E5%AD%90%E6%94%BE%E7%82%AE%E9%97%AF%E7%A5%B8&topic_id=28350829)
- [华尔街见闻 #10 | 高院否决是"一回事"，美国退税是"另一回事”](https://wallstreetcn.com/articles/3765922)
- [凤凰网 #10 | 夫妻当街暴打15岁女孩，底气从何而来？](https://news.ifeng.com/c/8qvbbpgFD4Q)
- [抖音 #10 | 水果烂一小块 削掉后能吃吗](https://www.douyin.com/hot/2408048)
- [财联社热门 #10 | 没有方向盘、没有脚踏板，特斯拉新车来了](https://www.cls.cn/detail/2292285)
- [百度热搜 #10 | 景区女财神被游客追得满场跑](https://www.baidu.com/s?wd=%E6%99%AF%E5%8C%BA%E5%A5%B3%E8%B4%A2%E7%A5%9E%E8%A2%AB%E6%B8%B8%E5%AE%A2%E8%BF%BD%E5%BE%97%E6%BB%A1%E5%9C%BA%E8%B7%91)
- [bilibili 热搜 #10 | 星河入梦3200个特效镜头](https://search.bilibili.com/all?keyword=%E6%98%9F%E6%B2%B3%E5%85%A5%E6%A2%A63200%E4%B8%AA%E7%89%B9%E6%95%88%E9%95%9C%E5%A4%B4)
- [今日头条 #10 | 匈牙利将否决欧盟对乌900亿欧元贷款](https://www.toutiao.com/trending/7609031193127813126/)
- [知乎 #10 | 如何看待 UCSD 教授 J. E. Hirsch 关于「BCS 超导理论是个庞氏骗局」的系列文章？](https://www.zhihu.com/question/641430230)
- [微博 #10 | 谷爱凌决赛时间](https://s.weibo.com/weibo?q=%E8%B0%B7%E7%88%B1%E5%87%8C%E5%86%B3%E8%B5%9B%E6%97%B6%E9%97%B4)
- [澎湃新闻 #10 | 放马过来，“申”情款待丨“马路艺术家”喊你街头寻“马”](https://www.thepaper.cn/newsDetail_forward_32543995)
- [贴吧 #11 | 国gal暴死,40万众筹打水漂](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%9B%BDgal%E6%9A%B4%E6%AD%BB%2C40%E4%B8%87%E4%BC%97%E7%AD%B9%E6%89%93%E6%B0%B4%E6%BC%82&topic_id=28350824)
- [财联社热门 #11 | 香港长江和记最新发声](https://www.cls.cn/detail/2292101)
- [百度热搜 #11 | 上海财神庙辟谣香炉起火](https://www.baidu.com/s?wd=%E4%B8%8A%E6%B5%B7%E8%B4%A2%E7%A5%9E%E5%BA%99%E8%BE%9F%E8%B0%A3%E9%A6%99%E7%82%89%E8%B5%B7%E7%81%AB)
- [凤凰网 #11 | 卫星图像曝光！“数十架美军机已驻扎在约旦基地”](https://news.ifeng.com/c/8qvWtj5wjsI)
- [今日头条 #11 | 免统考补录硕士？大连医科大学辟谣](https://www.toutiao.com/trending/7609122130168627242/)
- [知乎 #11 | 特斯拉无人驾驶车正式下线，无方向盘、无踏板、无后视镜，能赢得大众信任并走向普及吗？你看好其前景吗？](https://www.zhihu.com/question/2008253352463528326)
- [微博 #11 | 齐思钧回应分手](https://s.weibo.com/weibo?q=%23%E9%BD%90%E6%80%9D%E9%92%A7%E5%9B%9E%E5%BA%94%E5%88%86%E6%89%8B%23)
- [bilibili 热搜 #11 | 初五的财神有多忙](https://search.bilibili.com/all?keyword=%E5%88%9D%E4%BA%94%E7%9A%84%E8%B4%A2%E7%A5%9E%E6%9C%89%E5%A4%9A%E5%BF%99)
- [澎湃新闻 #11 | 寻马记｜北齐壁画博物馆里的86匹骏马](https://www.thepaper.cn/newsDetail_forward_32601317)
- [抖音 #11 | 村里又恢复了往日的宁静](https://www.douyin.com/hot/2407877)
- [贴吧 #12 | 港人偷拍同胞,阴阳国人没素质](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B8%AF%E4%BA%BA%E5%81%B7%E6%8B%8D%E5%90%8C%E8%83%9E%2C%E9%98%B4%E9%98%B3%E5%9B%BD%E4%BA%BA%E6%B2%A1%E7%B4%A0%E8%B4%A8&topic_id=28350812)
- [今日头条 #12 | 刘涛回应妈祖照爆火被设壁纸](https://www.toutiao.com/trending/7609266112585072681/)
- [凤凰网 #12 | 美国支持对朝鲜制裁豁免，特朗普向金正恩释放信号？](https://v.ifeng.com/c/8qvj0HzaSkk)

### 💻 GitHub 原文 (20/38 条)

- [openclaw/openclaw | ⭐ 216254 | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/openclaw/openclaw)
- [Significant-Gravitas/AutoGPT | ⭐ 181924 | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission i...](https://github.com/Significant-Gravitas/AutoGPT)
- [n8n-io/n8n | ⭐ 175684 | Fair-code workflow automation platform with native AI capabilities. Combine visual buildin...](https://github.com/n8n-io/n8n)
- [ollama/ollama | ⭐ 163079 | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and othe...](https://github.com/ollama/ollama)
- [huggingface/transformers | ⭐ 156785 | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning model...](https://github.com/huggingface/transformers)
- [f/prompts.chat | ⭐ 146280 | a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. F...](https://github.com/f/prompts.chat)
- [langflow-ai/langflow | ⭐ 144949 | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.](https://github.com/langflow-ai/langflow)
- [langgenius/dify | ⭐ 129948 | Production-ready platform for agentic workflow development.](https://github.com/langgenius/dify)
- [langchain-ai/langchain | ⭐ 127117 | 🦜🔗 The platform for reliable agents.](https://github.com/langchain-ai/langchain)
- [nautechsystems/nautilus_trader | ⭐ 20183 | A high-performance algorithmic trading platform and event-driven backtester](https://github.com/nautechsystems/nautilus_trader)
- [hummingbot/hummingbot | ⭐ 17373 | Open source software that helps you create and deploy high-frequency crypto trading bots](https://github.com/hummingbot/hummingbot)
- [tensorflow/tensorflow | ⭐ 193877 | An Open Source Machine Learning Framework for Everyone](https://github.com/tensorflow/tensorflow)
- [bennycode/trading-signals | ⭐ 880 | Technical indicators to run technical analysis with JavaScript & TypeScript. 📈](https://github.com/bennycode/trading-signals)
- [SeungMaeda/polymarket-copy-bot-ts | ⭐ 857 | Polymarket || Polymarket Bot || Polymarket Copy Bot || Polymarket Copy Trading Bot || Poly...](https://github.com/SeungMaeda/polymarket-copy-bot-ts)
- [nicobailon/visual-explainer | ⭐ 2201 | Agent skill + prompt templates that generate rich HTML pages for visual diff reviews, arch...](https://github.com/nicobailon/visual-explainer)
- [nullclaw/nullclaw | ⭐ 1485 | Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig](https://github.com/nullclaw/nullclaw)
- [ebrasha/free-v2ray-public-list | ⭐ 523 | A simple and always-updated list of free, working V2Ray servers. including SS, SSR, Trojan...](https://github.com/ebrasha/free-v2ray-public-list)
- [Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot | ⭐ 512 | Real-time polymarket trading bot that combines monitoring with strategy logic for Polymark...](https://github.com/Daniel-Dias001/Polymarket-rsi-macd-index-trading-bot)
- [MetaMask/eth-phishing-detect | ⭐ 1258 | Utility for detecting phishing domains targeting Web3 users](https://github.com/MetaMask/eth-phishing-detect)
- [DataExpert-io/ai-engineer-handbook | ⭐ 773 | All the links, books, and creators you need to follow to stay up to date with AI!](https://github.com/DataExpert-io/ai-engineer-handbook)

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

### 🌐 联网检索原文 (11/11 条)

- [2026-02-22 07:10 大紀元新聞網 | IMF首次指中共產業補貼為宏觀失調 專家解析 - 大紀元新聞網](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5zbGllVVcwYmtKMkZJQ29wbV9Zb1BXdTNMWEpuQnFLZnJ0Z3RMYlRJOEo5RU0zdGw1VXNMV0lpZDA1TVIzZTdxaUEwQUk3QW1LNE1tWW95M2w4YVRNbVdyd9IBZkFVX3lxTE9ZbXdvSmFXUWdTajJDanNPejFFNFJLRXVsd0tacy1jTExTcjFXNVJ5RXJCWGpGN09EMTBjZTB0UHk1bTRPbTlKTk1tdm4zYTZldnpPWURYdUpWbW9FYnNtZnYxcUM2Zw?oc=5)
- [2026-02-22 04:27 游侠网 | 国际AG|联合多国艺术家打造和平主题艺术展 - 游侠网](https://news.google.com/rss/articles/CBMiSkFVX3lxTE1yLUZkYXdXNXFiS3NiUThLNGI5UXJXbER3YXl3Q244UkpYSW91cEg0aHlHUjZxazBxcDNQaGQ2UmdqTTRqOVRTbWVB?oc=5)
- [2026-02-22 04:15 游侠网 | 乐彩网全国彩票,合作梅赛德斯-AMG车队豪华与性能联动 - 游侠网](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9QdEZSNGN6eTNEOGMydWY2QlJaWHBwM2FWbDJOS1BjcWR2amRvcjBmV2VYTGZ1aExZOXlLZGhvT2Z4SWtaWjRQRmkwMllWcUlnNVRzZ2RScGlPZ2M?oc=5)
- [2026-02-22 03:47 3DM | 海洋娱乐平台(官方)综合娱乐APP下载-AppleAppStore - 3DM](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBuNFNEWE11dmFSRnQyd3lyalo1bzZaYXlvXzdhUjVQU3cxb0ktQmE0QkNBQ095TVZBbDVkcnpQVkJkekRPQVNKTUd4cXVHS3pLMnBHQkJydHE?oc=5)
- [2026-02-21 08:24 yeeyi | 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTE91dGZGTy1OSTZSb2VXUjhVVC1kRFFtM0g5aXRtNXdzUThFR2lCanJhRlVrUk9xTExQSmpramhzUzJPRXItSGFMYXdmZ2VRc1g3Nmk0c1VB?oc=5)
- [2026-02-21 07:47 富途牛牛 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5)
- [2026-02-21 05:30 英为财情 Investing.com | 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5)
- [2026-02-20 19:48 OR新媒体 | OR新媒体| 美股为何如此诡异？ - OR新媒体](https://news.google.com/rss/articles/CBMiREFVX3lxTE9EeFVtMVR6V1p3ckhwSHhLT29tTVZHYkRFcFhNQW5wbU82WEd4eDdfN2FLSkpTaEcyTGJWelF2bWR0ekJf?oc=5)
- [2026-02-20 18:45 富途牛牛 | 芝加哥期权交易所波动率指数在特朗普据报道将伊朗外交期限延长10至15天后，盘前下跌0.5% - 富途牛牛](https://news.google.com/rss/articles/CBMilAFBVV95cUxPY2tONUdHUUthRm9SWk1kZ0ZERk9kWEoxb3Y2X000LTE0bmtxNmprNXlRSlE1SGpfZk5QdHE4NlUyX214QnRPcHptODJZNUFqY3B1emN0WlN0aHVOem5OY2ozbEk0d2lDZWlNLU9rM3lZb3Yxb1NxYlZDSDd3NS1DNFJRb3V3bElqUjNFRDUtWHJOV0pv?oc=5)
- [2026-02-20 14:45 Bitget | 美银对较高的股票风险敞口发出逆势“卖出”信号 - Bitget](https://news.google.com/rss/articles/CBMia0FVX3lxTE5LLUpQSDBuUUxLbkRLSDRWRV84VFJ4SmUwSFNJNFNPY0tWbFBweVVDYkF6SG5jZlktZEtsbTc4dWEzU0FrRFdhWnd2WFRMb3FkeWFwVmdGc2t2WkFqTlZ6UmdfZlFqTHBEZmZn0gFrQVVfeXFMTkstSlBIMG5RTEtuREtINFZFXzhUUnhKZTBIU0k0U09jS1ZsUHB5VUNiQXpIbmNmWS1kS2xtNzh1YTNTQWtEV2Fad3ZYVExvcWR5YXBWZ0Zza3ZaQWpOVnpSZ19mUWpMcERmZmc?oc=5)
- [2026-02-20 13:30 英为财情 Investing.com | 澳大利亚股市收低；截至收盘澳大利亚S&P/ASX200指数下跌0.05% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE1VRXd4WTVIdU42dGRiZXNSMHlmWWx6UW9pWjlRTWswYm1CT3U0ZGxfelh2UDI4dG9vdTFabFNUcTVoQlJSb0d1UDJDbnEteGRXYXgxN2kwRHNMX1otbHNmVVBjWDV6QTlBYUY5NHVTR0g?oc=5)

---

*报告由 finradar 自动生成 | 2026-02-22 08:03:03（北京时间）*
