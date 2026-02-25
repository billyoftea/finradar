# 📰 finradar 🌇 晚报
**2026-02-21** | 🌇 晚报 | 覆盖时段: 今日08:00 → 20:00 | 市场状态: ⚠️ A股休市
生成时间: 2026-02-21 20:03（北京时间）

**⚠️ 注意：今日为周末，A股休市，部分市场数据可能缺失或未更新**

---

## 🚨 数据源健康提醒

1. 检测到微信登录异常：财联社: invalid session。请重新扫码登录 wechat-exporter。
2. 本次抓取公众号文章为 0 篇，账号搜索失败占比 100%，请检查登录态或服务状态。

处理建议：
1. 打开 `wechat-article-exporter` 页面完成扫码登录（默认 `http://localhost:3001`）。
2. 登录后执行 `./scripts/local.sh run social` 刷新社交数据。
3. 然后执行 `./scripts/local.sh report evening 20260221` 与 `./scripts/local.sh notion-push evening 20260221` 覆盖 Notion 页面。

# 🤖 AI 分析摘要

## 一、摘要
- **社会**：国内社会关注点集中于**春节旅游安全事故**（贝加尔湖7名中国游客溺亡事件细节披露）[NW02, WB07]与**春节文化现象**（“迎财神”、送银砖压岁钱等）[NW04, NW05, NW08]。海外社会事件以**印度AI峰会**及**美国政治争议**为主。
- **经济**：**全球贸易政策不确定性仍是核心**，美国最高法院裁定特朗普关税违法，提振市场信心并引发巴西股市创历史新高[WB14]，但潜在的大规模税收退款与未来关税摩擦风险并存。国内机构观点显示对A股“慢牛”及外资回流的预期[WB01]。
- **市场**：隔夜美股收涨，核心驱动为**美国最高法院否决特朗普关税政策**[WB03, WB11]，市场风险偏好回升，VIX指数下跌。**贵金属价格（金银）再度大涨**[NW03, WB03]，反映滞胀担忧。A股休市，无新增盘面数据。
- **科技**：AI领域呈现**地缘合作与产业竞争并存**。积极信号包括：印度与巴西在AI峰会上的高层互动[TW02]，深圳拟研发14nm以下国产AI芯片以摆脱外部依赖[WB09, WB10]。风险信号包括：印度AI峰会曝出“机器狗冒充自研”等负面事件[WB11]，以及AI领域存在未经证实的政治化指控噪音。

## 二、分板块汇报
### 2.1 市场概况（仅有效交易时段数据）
较上期：**新增隔夜美股及全球其他市场在非A股交易时段的走势与驱动分析**。
**发生了什么**：隔夜（覆盖时段对应美股2月20日交易）全球主要股指多数上涨。美股三大指数收高，道指涨0.47%[WB04]，纳指领涨；欧洲股市表现强劲，德国DAX、法国CAC40显著上涨；巴西股市创历史新高[WB14]。**VIX波动率指数下跌**，显示市场恐慌情绪缓解。商品方面，**黄金价格重回5100元/克上方，白银大涨8%**[WB03]。
**为什么会这样（证据强度：高）**：核心驱动是美国最高法院裁定特朗普时期全球关税政策违法[WB11]。这一裁决**消除了巨大的贸易政策不确定性**，可能带来超1750亿美元的税收退款，直接提振了市场（尤其是对贸易敏感的巴西等新兴市场）信心[WB14]，并降低了避险需求（VIX下跌）。贵金属大涨则被解读为市场在“滞胀担忧”下的对冲行为[WB03]。关于美股上涨的直接原因，多个来源均指向最高法院裁决[WB03, WB11, WB14]，证据链清晰。
**下一步观察**：需紧密跟踪该裁决的法律执行细节、特朗普方面的后续反应（历史报告提及的新关税主张），以及其对美元、美债和全球资本流动的持续影响。同时，观察金银价格的强势能否延续，以验证市场对滞胀的担忧程度。

### 2.2 微信公众号共识与弱信号
数据不足。输入中未提供“微信公众号逐篇简介”或可引用的公众号文章内容，无法进行跨公众号的共识提炼或弱信号识别。

### 2.3 GitHub 热门项目雷达（金融科技/AI/Web3）
较上期：**延续对AI应用化、工程化工具的高度关注，金融科技与Web3项目保持稳定**。
最值得关注的项目仍集中于**AI应用与基础设施**领域。**openclaw/openclaw**（⭐215k）定位为跨平台个人AI助手，其超高星标反映社区对通用AI助手的强烈需求，但项目描述宽泛，存在概念模糊与落地路径不清晰的风险。**n8n-io/n8n**（⭐176k）作为集成AI能力的可视化工作流自动化平台，其“公平代码”与自托管特性在企业级自动化场景中具有明确的落地价值，但需评估其AI功能与竞品的差异化。**ollama/ollama**（⭐163k）简化了多模型本地部署，是AI平民化趋势的关键工具。
在**金融科技**领域，**nautechsystems/nautilus_trader**（⭐20k）是用Rust编写的高性能算法交易与回测平台，面向专业量化场景，技术栈先进，但缺乏公开的性能基准对比。**Web3**领域，**foundry-rs/foundry**（⭐10k）作为极快的以太坊开发工具包，是开发者生态的基础设施，其“可移植与模块化”特性符合当前开发效率需求。
总体趋势显示，开发者生态正全力推动AI从模型走向应用（助手、工作流、部署），而金融科技与Web3的创新更聚焦于专业工具和底层设施，噪音风险在于部分AI项目概念存在同质化。

### 2.4 Twitter 海外信号（英文内容中文汇报）
较上期：**新增Web3原生结算层发布、机构购买比特币传闻及地缘AI合作信号，同时充斥大量未经验证的政治指控**。
**Web3/加密信号**：1) **原生结算资产**：Nexus Labs推出USDX，旨在作为其生态内所有应用和市场的统一结算层与流动性中心[¹](https://twitter.com/NexusLabs/status/2024138532512567297)。2) **机构动向与链上数据**：有未经证实的消息称BlackRock购入**6450万美元比特币**[²](https://twitter.com/cryptorover/status/2025078124833116434)；同时，比特币算力自近期低点回升超28%[³](https://twitter.com/BitcoinMagazine/status/2024859538562662650)。3) **争议关联**：有推文指控Cantor Fitzgerald CEO Howard Lutnick与Epstein有关联，并涉及Tether、比特币操纵及收购关税退款权等操作[⁴](https://twitter.com/JacobKinge/status/2024906835610710212)，该指控缺乏可验证证据，属高噪音信号。
**AI与地缘信号**：印度总理莫迪欢迎巴西总统卢拉代表团，提及卢拉出席AI峰会，为双边合作注入新能量[⁵](https://twitter.com/narendramodi/status/2025149417636896912)。这与此前印度AI峰会引发群嘲的负面新闻[WB11]形成反差。
**政治与社会噪音**：多条高互动推文传播关于奥巴马、CIA伪造“通俄门”以破坏特朗普选举的爆炸性指控[⁶](https://twitter.com/the_17thletter4/status/2024859960853622861)[⁷](https://twitter.com/WHLeavitt/status/2024983554992840962)，以及关于议员AOC非法雇佣的指控[⁸](https://twitter.com/Milajoy/status/2024773028660559988)。这些内容均未提供可靠信源或官方文件证实，煽动性强，信息可靠性极低，应视为市场噪音。

### 2.5 国内新闻与政策脉络
较上期：**新增国内科技产业政策动向及春节文旅安全事件细节，延续对宏观市场的机构观点**。
**科技产业政策**：深圳市传出拟研发**14nm以下国产AI芯片**的消息，目标直指摆脱对英伟达等公司的依赖[WB09, WB10]。这是对“科技自立”政策的具体落实，若推进顺利，将利好国内半导体设备、材料及设计产业链，但需关注其技术可行性与产业化进度。
**社会与监管事件**：**贝加尔湖中国游客溺亡事件**细节进一步披露，俄方确认其旅游路线未经批准[NW02, WB07]，事件引发对出境游安全监管和旅行社责任的讨论。国内热搜同时出现“金银价再度大涨”[NW03]，这与隔夜国际贵金属走势呼应，反映国内投资者同样存在避险或抗通胀需求。
**机构市场观点**：摩根大通刘鸣镝发表观点，认为A股进入“慢牛”，外资回流可期[WB01]。这代表了部分外资机构对A股的积极展望，与近期市场关注的外资动向形成呼应。
**消费与产业**：有分析指出2025年消费并购进入“从流量到留量”的静水深流阶段[WB13]，显示消费投资逻辑可能从规模扩张转向深度运营和整合。

## 三、明日跟踪清单
1.  **延续跟进：美国关税政策裁决的市场后续演化**：紧密跟踪最高法院裁决后的官方执行声明、受影响企业的具体反应，以及特朗普是否会有新的政策主张，评估其对全球股市、汇市及大宗商品的第二轮影响。[⁹](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5)[¹⁰](https://news.google.com/rss/articles/CBMieEFVX3lxTFBsLUNoMDMxUE9KaXZKVUk5YXRkTFNKbEpFamNRVE9SZl8yMlJRdVB2UE5IdldKM1ptaG5jMFFWTFI3WFFud3g3M25sa0xXMW82V1BOdG4wMnVaMVVXWldWM3hNQWlEdXhMTHBRUUJvLXVWMmZkWVM4cA?oc=5)[¹¹](https://news.google.com/rss/articles/CBMigAFBVV95cUxQSm40Mk51bUs1ZGdzU3podHd3ckFBLUlma00waE5Vem5oSDZpd1Fib2hlVlBfMlJZR2pXbzhjckhEd3NHVzlxWHQzNnJ4LVVtUlB3dDFuckRWMS1JY3RHbmNndzBpTEgxTjNzVFdmYlBlTzd4VHdpeHlnVGNGT2Y3Nw?oc=5)
2.  **收口复盘：韩国股市独立行情的驱动逻辑验证**：结合历史关注，需补充韩国市场今日（2月21日）的盘面数据、领涨板块及资金流入情况，以确认其独立上涨的可持续性与具体驱动因素。（**本期数据仍不足**）
3.  **新增观察：国产AI芯片研发倡议的产业反馈**：跟踪市场对“深圳研发14nm以下AI芯片”消息的反应，观察国内半导体产业链（尤其是设备、EDA、制造环节）相关公司的股价与舆情变化，评估政策信号的强度。[¹²](https://news.google.com/rss/articles/CBMif0FVX3lxTE1OQlg5QnNON2hKWlFSclQ2bVh5ZVhqcXB4b0Itck5VRG5TcW81TVkzeVpEWXItM2xWOGo5QlpVSFVQSkNFWW45NWxubXMxMmNTSzhMazM3N21ybUhUR0t3aU4zMHRrTDluLVFBY1pEcFRMWlFKUDA4MkRYQ0l4QTA?oc=5)[¹³](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9SNi1JaUtGay14WGNGN0NfM1dzSkVOTVlWS0ZBdjVlNFZjWWRDdHd1cFBENEU5ekI2N1dzT3hvQzBZM0Y3R012SERVeUdtRFNFQ0l4WTM2WjVTa0ViLTM2VVpHcDlGdw?oc=5)


---

<details><summary>📑 点击展开各板块详细分析</summary>

### 📊 市场数据详细分析

### 1. 主要市场走势判断
今日全球市场呈现**显著的区域分化**格局。
*   **亚太市场普遍承压**：A股（**-1.26%**）、日股（**-1.12%**）、港股（**-1.10%**）领跌主要市场，而韩股（**+2.31%**）是唯一的强劲例外。
*   **欧美市场整体走强**：欧股表现突出，法国CAC40（**+1.39%**）、德国DAX（**+0.87%**）涨幅居前。美股三大指数亦录得上涨，纳斯达克（**+0.90%**）领涨。
*   **整体情绪偏积极**：跟踪的12个主要股指中，**7涨5跌**，上涨家数多于下跌家数。同时，**VIX波动率指数下跌5.64%**，表明市场恐慌情绪有所缓解。

### 2. 关键资产轮动分析
*   **领涨方向**：
    1.  **欧洲成长/蓝筹股**：以法国CAC40和德国DAX为代表的欧股大幅跑赢，显示资金在向欧洲市场，特别是其核心资产聚集。
    2.  **美国科技股**：纳斯达克指数涨幅显著高于道琼斯和标普500，表明在美股内部，**科技成长风格占优**。
    3.  **韩国股市**：韩国综合指数**+2.31%**的涨幅在全球主要市场中一骑绝尘，显示有强劲的本地或区域资金流入。

*   **领跌方向**：
    1.  **中国相关资产**：A股与港股同步下跌，且跌幅在主要市场中居前，反映资金对**中国资产的风险偏好下降**。
    2.  **日本股市**：日经225指数下跌**-1.12%**，与亚太其他市场（除韩国外）形成共振下跌。

*   **资金偏好解读**：资金明显从亚太（除韩国外）流向欧洲，并在美股内部偏好科技成长板块。这种“**西强东弱**”的格局，可能反映了对欧洲经济前景的相对乐观，以及对东亚部分经济体（特别是中国）的短期担忧。韩国市场的独立强势原因未提供。

### 3. 加密货币和商品期货的关键变化
*   **加密货币**：普遍温和上涨。BTC（**+1.08%**）、ETH（**+1.67%**）、SOL（**+2.19%**）均录得正收益，其中SOL领涨。走势与风险资产（如美股科技股）有一定同步性，显示其**风险属性**。
*   **商品期货**：
    *   **工业金属**：COMEX铜价上涨**+1.76%**，表现强劲，可能与全球制造业预期或美元走势有关（美元数据未提供）。
    *   **能源**：走势分化。天然气（**+1.70%**）和布伦特原油（**+0.14%**）微涨，WTI原油微跌（**-0.06%**），整体波动不大，未显示明确趋势。
    *   **贵金属**：数据未提供，无法分析。

### 4. 涨跌驱动链条分析
基于现有数据，可推导出部分链条，但驱动事件的直接证据不足。

*   **欧洲股市上涨链条（推测，证据强度：弱）**：
    *   潜在驱动（未提供）：可能受到优于预期的欧洲经济数据、企业财报或区域性政策利好提振。
    *   资金行为（数据支持）：资金流入欧洲主要股指，法国、德国股市领涨。
    *   价格表现（数据支持）：CAC40、DAX指数显著收高。

*   **A股/港股下跌链条（推测，证据强度：弱）**：
    *   潜在驱动（未提供）：可能受到国内经济数据、行业监管消息或外资流出情绪影响。
    *   资金行为（数据支持）：资金流出中国相关资产，上证综指与恒生指数同步下跌。
    *   价格表现（数据支持）：A股、港股成为今日全球主要市场中表现最差的方向之一。

*   **美股科技股领涨与市场恐慌缓解链条（数据支持，证据强度：中）**：
    *   情绪指标（数据支持）：**VIX指数大幅下降5.64%**，明确显示市场整体避险情绪降温。
    *   资金行为（数据支持）：在风险偏好回升的背景下，资金选择流入弹性更大的科技成长板块（纳斯达克）。
    *   价格表现（数据支持）：纳斯达克指数涨幅（**+0.90%**）跑赢其他美股主要指数。

*   **加密货币与风险情绪联动链条（数据支持，证据强度：中）**：
    *   市场情绪（数据支持）：全球股市（尤其欧美）多数上涨，VIX下降，**风险偏好整体回升**。
    *   资金行为（数据支持）：部分资金流入被视为高风险资产的加密货币。
    *   价格表现（数据支持）：主要加密货币**全线温和上涨**，与纳斯达克等风险资产走势正相关。

**总结**：今日市场核心特征是**区域分化与风险偏好结构性回升**。资金从东亚（除韩国外）流向欧洲，并在全球范围内增配科技成长及加密货币等风险资产。然而，导致亚欧市场表现迥异的具体政策或事件驱动因素，在提供的数据中**未明确显示**。铜价的大涨也缺乏直接的供需或宏观数据佐证。

### ⏱ 市场时效过滤说明

市场时效过滤结果：
1. 非交易日，不纳入 A 股盘面

### 🐦 Twitter 逐条简介

Twitter 逐条简介（共 12 条，按互动热度排序）：
1. [热门] @NexusLabs | 2026-02-21T12:00 | 互动=27433
   原文摘录: Introducing USDX — the native dollar of the Nexus economy. A shared settlement layer for all apps, trades, and markets on Nexus. One asset. Unified liquidity. P
   原文链接: [点击查看原文](https://twitter.com/NexusLabs/status/2024138532512567297)
   1) 讲了什么：Nexus Labs推出原生美元USDX，作为Nexus经济中所有应用、交易和市场的共享结算层。
   2) 关键信号：强调统一流动性、协议原生激励，并称资本正在汇聚。
   3) 阅读建议：略读 + 原因：内容为项目发布公告，核心信息已概括，细节需通过链接获取。
2. [热门] @narendramodi | 2026-02-21T12:00 | 互动=20023
   原文摘录: India is honoured to welcome President Lula and his delegation, which includes distinguished ministers and business leaders. India-Brazil relations have long be
   原文链接: [点击查看原文](https://twitter.com/narendramodi/status/2025149417636896912)
   1) 讲了什么：印度欢迎巴西总统卢拉代表团，提及卢拉出席AI峰会及双边会谈。
   2) 关键信号：卢拉出席AI峰会，双方会谈涵盖多领域合作。
   3) 阅读建议：略读 + 原因：内容为外交礼节性表态，无具体合作细节或数据。
3. [热门] @JacobKinge | 2026-02-21T12:00 | 互动=17398
   原文摘录: Howard Lutnick is arguably one of the slickest and most corrupt operators in modern finance. We now know he was close friends with Jeffrey Epstein, despite him 
   原文链接: [点击查看原文](https://twitter.com/JacobKinge/status/2024906835610710212)
   1) 讲了什么：推文指控Howard Lutnick腐败，与Epstein有联系，并揭露Cantor Fitzgerald低价收购关税退款权的新操作。
   2) 关键信号：指控涉及Epstein文件、Tether与比特币操纵、关税退款收购方案细节。
   3) 阅读建议：精读 + 原因：推文包含多项具体指控和操作步骤，信息密度高。
4. [热门] @MedicoLiberdade | 2026-02-21T12:00 | 互动=12417
   原文摘录: E aí@BlogdoNoblat, vai comentar o cartão de crédito corporativo de painho que gastou + de 50 vezes o que bonoro gastou, ou vai ficar calado como o inútil comuna
   原文链接: [点击查看原文](https://twitter.com/MedicoLiberdade/status/2024964381675569406)
   1) 讲了什么：用户质问博主为何不评论某人的公司信用卡支出远超另一人。
   2) 关键信号：支出比较数据未提供，仅提及“超过50倍”。
   3) 阅读建议：略读，内容为个人质问，无具体金融数据或事件细节。
5. [热门] @Milajoy | 2026-02-21T12:00 | 互动=10303
   原文摘录: REP. AOC’S ILLEGAL HIRE SCANDAL EXPLODES AOC knowingly put an illegal alien—zero work papers, pure lawbreaker—on payroll as her Legislative Assistant. AOC IS GO
   原文链接: [点击查看原文](https://twitter.com/Milajoy/status/2024773028660559988)
   1) 讲了什么：推文称AOC明知故犯雇佣无证移民作助理，违反法律并面临罚款与监禁。
   2) 关键信号：指控有具体法律条文和罚则，但未提供证据来源或官方行动。
   3) 阅读建议：略读 + 原因：内容为单方指控，缺乏核实信息，属争议性讨论。
6. [热门] @Playnance_ | 2026-02-21T12:00 | 互动=7645
   原文摘录: CryptoWisser spotlights the model behind G Coin 💎 As CryptoWisser writes, G Coin represents “a token-linked distribution economy with multiple measurable compon
   原文链接: [点击查看原文](https://twitter.com/Playnance_/status/2024515923630039477)
   1) 讲了什么：CryptoWisser介绍了G Coin的模型，称其为具有多个可测量组件的代币关联分发经济。
   2) 关键信号：新Boss平台成为分发节点，驱动活动并以G Coin结算，形成与收入挂钩的效用。
   3) 阅读建议：略读 + 原因：推文已概括模型核心机制与逻辑，链接为全文。
7. [热门] @kangminjlee | 2026-02-21T12:00 | 互动=5945
   原文摘录: Turns out mass immigration actually doesn't help the economy in the long run Instead Canadians got depressed wages, skyrocketed cost of living, and feeling like
   原文链接: [点击查看原文](https://twitter.com/kangminjlee/status/2024889042400055362)
   1) 讲了什么：一条推文称大规模移民长期无益经济，导致工资下降、生活成本飙升和本土居民被取代感。
   2) 关键信号：推文观点认为移民导致工资和生活成本问题，以及文化疏离感。
   3) 阅读建议：略读 + 原因：此为个人观点陈述，未提供数据或来源支持。
8. [热门] @the_17thletter4 | 2026-02-21T12:00 | 互动=4791
   原文摘录: BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hidden in CIA vault for ~10 years, to undermine Trump’s election via mani
   原文链接: [点击查看原文](https://twitter.com/the_17thletter4/status/2024859960853622861)
   1) 讲了什么：推文称有20名CIA/FBI探员确认奥巴马与前CIA局长伪造“俄罗斯骗局”以破坏特朗普选举。
   2) 关键信号：指控涉及伪造情报、破坏选举、要求逮捕奥巴马，并呼吁病毒式传播。
   3) 阅读建议：略读 + 原因：内容为单方面指控，未提供可验证证据，信息源与事实依据不足。
9. [热门] @jisoogaIIery | 2026-02-21T12:00 | 互动=4138
   原文摘录: FACE ECONOMY
   原文链接: [点击查看原文](https://twitter.com/jisoogaIIery/status/2024851114689188167)
   1) 讲了什么：一条推文提及“FACE ECONOMY”，无更多内容。
   2) 关键信号：未提供具体事件、数据或观点。
   3) 阅读建议：略读，因信息量极少，无实质内容。
10. [热门] @WHLeavitt | 2026-02-21T12:00 | 互动=3178
   原文摘录: 🚨 ALERT: Bombshell—20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hidden in CIA vault for ~10 years, to undermine Trump’s election vi
   原文链接: [点击查看原文](https://twitter.com/WHLeavitt/status/2024983554992840962)
   1) 讲了什么：推文称有情报人员确认奥巴马等人伪造“俄罗斯骗局”以破坏特朗普选举。
   2) 关键信号：未提供具体证据或文件，仅引用匿名人员说法。
   3) 阅读建议：略读，因其为未经证实的指控且缺乏可验证细节。
11. [热门] @RodiumInsights | 2026-02-21T12:00 | 互动=3051
   原文摘录: یاد ہے !”عاصم منیر نے کہا تھا تم اللہ کی جنگ لڑ رہے ہو وہ اسکے ساتھ نہیں ہے ۔“ آج یہ حالت ہے ریاست نے انکو پہچاننے سے انکار کر دیا ہے۔ میرا نہیں خیال کہ یہ کوئی
   原文链接: [点击查看原文](https://twitter.com/RodiumInsights/status/2024935415955030328)
   1) 讲了什么：推文引用他人言论，质疑国家拒绝承认某人，并询问是否应同情他们。
   2) 关键信号：提及特定日期事件，如26日、9日，描述救护车内枪击伤员。
   3) 阅读建议：略读 + 原因：内容为个人观点与情绪化提问，缺乏具体金融科技信息。
12. [热门] @RepOfSomaliland | 2026-02-21T12:00 | 互动=2089
   原文摘录: Hey@Grok, remove the unstable, persistently high-inflation currency.
   原文链接: [点击查看原文](https://twitter.com/RepOfSomaliland/status/2024570762263482644)
   1) 讲了什么：账号@RepOfSomaliland向Grok提出移除不稳定、持续高通胀货币的要求。
   2) 关键信号：未提供具体货币名称、通胀数据或移除背景。
   3) 阅读建议：略读，因信息不具体，仅为单方要求。

### 🌐 Twitter 英文信号详细分析

### 海外英文信号主线
1.  **加密货币/数字资产创新与整合**：Nexus Labs 推出原生美元 USDX，旨在作为其生态内所有应用、交易和市场的统一结算层与流动性中心。Ondo Finance 强调其代币化股票交易的低滑点优势，并指出流动性池的可扩展性问题是行业普遍挑战。
2.  **机构动态与市场指标**：有信号称 BlackRock 进行了大额比特币购买。比特币算力自近期低点显著回升。同时，有观点提示关注周一市场开盘前的潜在风险。
3.  **地缘与监管争议**：信号涉及印度与巴西在人工智能峰会上的高层互动。多条高互动推文指控美国前总统奥巴马及前中情局局长捏造“通俄门”以干预大选，并要求追责。另一争议涉及美国议员 AOC 被指控非法雇佣。
4.  **人工智能与高性能计算竞争**：信号指出 Nvidia 收购 Groq IP，以及初创公司 Taalas 在模型推理速度上展示出显著优势，并强调其成本效益是关键。

### 与金融科技/AI/Web3相关的具体线索
1.  **Web3 与 DeFi**：
    *   **统一结算资产**：Nexus Labs 推出 USDX，目标是成为其生态系统的原生美元，实现统一流动性和协议原生激励。
    *   **代币化现实世界资产 (RWA)**：Ondo Finance 展示其代币化股票交易的低滑点执行能力，并指出当前多数平台的流动性池难以扩展。
    *   **代币经济模型**：G Coin 被描述为一种具有“多个可衡量组件”的、与代币挂钩的分配经济模型。
2.  **人工智能 (AI)**：
    *   **地缘合作**：印度总理提及巴西总统卢拉出席 AI 峰会，为双边关系注入新能量。
    *   **技术竞赛**：Nvidia 收购 Groq 知识产权；Taalas 公司在相同模型上展示了比 Cerebras 快 8 倍的推理速度，并强调其成本约束优势。
    *   **行业活动**：有信号提及青年大会领袖参加 AI 峰会。
3.  **加密货币市场**：
    *   **机构动向**：有未经证实的消息称 BlackRock 大额购入比特币。
    *   **网络健康度**：比特币算力自近期低点上涨超过 28%。
    *   **争议关联**：有指控将 Cantor Fitzgerald 首席执行官 Howard Lutnick 与 Epstein、Tether 及比特币联系起来。

### 可执行关注点与潜在误导噪音
**可执行关注点**：
1.  **跟踪新协议与资产**：关注 Nexus Labs 的 USDX 作为潜在的新兴结算层概念及其生态发展。
2.  **评估 RWA 赛道进展**：关注 Ondo Finance 等平台在解决代币化资产流动性与滑点问题上的实际表现与技术方案。
3.  **关注 AI 基础设施性能**：跟踪类似 Taalas 公司在推理速度与成本约束方面的突破，这可能影响 AI 算力市场竞争格局。
4.  **监控比特币网络基本面**：比特币算力的显著回升是一个积极的链上基本面信号，值得持续观察。

**潜在误导噪音**：
1.  **未经证实的爆炸性指控**：关于奥巴马制造“通俄门”、AOC 非法雇佣将入狱、Howard Lutnick 与 Epstein/Tether 关联等指控，均来自高互动推文，但输入文本中未提供任何法庭文件、官方报告或可靠信源予以证实，属于高度争议性且未验证的信息。
2.  **模糊的市场预警与机构动向**：“周一市场开盘前囤货加油”的警告缺乏具体原因。关于 BlackRock 购买比特币的具体金额（$64,500,000）也未提供官方公告或交易验证来源。
3.  **煽动性投票与标签**：“是否支持逮捕奥巴马”的投票及“让此推文病毒式传播”的呼吁，具有明显的政治煽动和操纵互动嫌疑，信息本身可靠性存疑。
4.  **部分信号背景缺失**：关于“CIA撤回19份政治化情报产品”及“每年9.2万亿美元净零经济内幕”的信号，缺乏详细的报告链接或具体证据，难以独立评估其全面性与准确性。索马里兰账号要求 Grok 移除“高通胀货币”的具体背景和对象未提供。

### 📰 热榜详细分析

# 热榜分析报告

## 1. 跨平台共同关注的3-5个热点事件
1.  **美国最高法院裁定特朗普关税政策违法/被否决**：该事件在多个分片中被列为最重要事件，并直接关联美股波动、巨额税收退款（超1750亿美元）及特朗普后续反应（宣布加征10%全球关税）。
2.  **贝加尔湖中国游客重大伤亡事件**：7名中国游客在贝加尔湖因车辆冰面破裂落水溺亡，俄方称其路线未经批准。该事件在分片1和分片3中被提及，引发社会关注。
3.  **春节档电影市场表现**：2026年春节档总场次刷新中国影史纪录，总票房破40亿元，其中《飞驰人生3》以21亿元领跑。该话题在分片4和分片5中被重点提及。
4.  **社会暴力事件与公权力反应**：两起“当街暴打女孩”事件（“女孩被当街暴打当地何以沉默两天”、“夫妻当街暴打15岁女孩”）引发舆论对地方处理效率与公正性的质疑。该焦点在分片2中被突出。
5.  **体育人物王濛相关言论**：王濛公开批评短道速滑队问题，并称愿“签生死状复出保金牌”，相关讨论在多个平台热传。该事件在分片2和分片5中被提及。

## 2. 与金融市场相关的重要新闻
*   **美国关税政策与市场波动**：美国最高法院裁定特朗普关税违法，可能导致超1750亿美元税收退款。此事件引发美股（分片3、4、5、6提及收涨或下跌）、美债、汇市及黄金（价格重回5100，白银大涨8%）的显著波动。特朗普随后宣布加征10%全球关税，进一步影响市场预期。
*   **宏观经济数据**：美国四季度GDP增速大幅放缓至1.4%（分片2），政府停摆是主要拖累因素之一。美国12月核心PCE物价指数同比为3%，超出预期（分片3）。
*   **产业与资金动向**：中国顶流私募Q4集体加仓拼多多，AI投资重心发生转变（分片1）。公募基金在春节前集中调研机器人、半导体、有色金属领域（分片1）。节前资金已挤入与“马年科技春晚”及机器人概念相关的ETF（分片4）。三星HBM4据称涨价30%，韩国“芯片双雄”积极扩产（分片7）。
*   **其他市场线索**：存款利率跌入“0”字头（分片4）。印度正积极谈判购买委内瑞拉石油（分片2）。春节档票房破40亿，新闻提及需关注背后涉及的A股公司，但具体公司名称未提供（分片5）。

## 3. 科技/AI 相关热点
*   **OpenAI动态**：OpenAI大幅下调算力支出目标至6000亿美元（分片1）。
*   **AI行业事件与观点**：印度AI峰会引发全球群嘲（分片1），具体原因未提供。“谷歌天团”反驳AI泡沫质疑，称其为速度与规模均扩大10倍的工业革命（分片2）。ClaudeCode 之父称不再需要「planmode」（分片5）。莫迪举手全场欢呼，两大AI掌门人却各自握拳尴尬对峙（分片6），具体人物与背景未提供。
*   **产品与技术**：特斯拉无方向盘、无踏板、无后视镜的无人驾驶车正式下线（分片5）。实测Gemini 3.1 Pro（分片6），结果未提供。
*   **半导体与硬件**：公募基金调研热点包括机器人、半导体（分片1）。三星HBM4存储芯片涨价与扩产（分片7）。日企采用中国芯（分片6），具体企业与影响未提供。“马年科技春晚”与机器人概念相关（分片4），具体科技内容未提供。

## 4. 社会舆论焦点
*   **社会安全与公权力**：贝加尔湖中国游客遇难（分片1、3）及多起当街暴打女孩事件（分片2）引发对安全管理和公权力反应的广泛关注与质疑。
*   **春节社会文化现象**：围绕春节产生大量话题，包括“舅舅送30斤银砖当压岁钱”、“亲戚拜年不说话”、“景区空中撒钱”、“回村后用的都是名牌货”（分片4）、“年轻人走亲戚方式”（分片1）、“正月初五迎财神”、“300年打树花”（分片7）等，反映节日期间的社会话题与消费观。
*   **文娱体育话题**：春节档电影表现（分片4、5）、王濛批评短道速滑队（分片2、5）、运动员徐梦桃与王心迪成为奥运金牌夫妇（分片5、7）、综艺节目（分片2）、游戏“鸣潮”缺乏二创（分片1）、春晚歌曲锐评（分片6）等构成广泛讨论。
*   **网络谣言与争议**：“港人偷拍同胞”、“免统考补录硕士”被辟谣（分片1、7）。“错认国人，菲律宾女孩遭猎艳”（分片6）。“黄晓明曝艺人红毯上假摔”（分片6）。
*   **其他社会讨论**：关于开放与封闭系统的讨论（Windows vs. macOS，Android vs. iOS）（分片3）。宠物饲养争议（购买“小矮马”）（分片2）。职场文化叙事（被裁员工因“太优秀”）（分片2）。文旅监管，如湖北省认定那艺娜（翟革英）为劣迹艺人（分片3）。

### 💻 GitHub 项目详细分析

# GitHub热门项目技术趋势分析报告

## 一、精选重点项目分析

基于今日数据，以下为各领域最值得关注的5个项目：

**1. [AI] openclaw/openclaw (⭐215,202)**
*   **应用场景与价值**：被描述为“您自己的个人AI助手”，旨在实现跨操作系统和平台的通用AI助手服务。其高星标数表明社区对构建通用、可访问的个人AI工具存在强烈需求。
*   **潜在噪音**：项目描述较为宽泛（“The lobster way”），具体技术实现路径、与现有个人助手（如Siri、Cortana）的差异化优势未提供，可能存在概念重复或定位模糊的风险。

**2. [AI] n8n-io/n8n (⭐175,609)**
*   **应用场景与价值**：一个“公平代码”工作流自动化平台，集成了原生AI能力。它结合了可视化构建与自定义代码，支持自托管或云部署，拥有400多个集成。其落地价值在于为企业提供可定制、私有化部署的自动化与AI集成解决方案，降低技术门槛。
*   **潜在噪音**：数据未提供其与Zapier、Make等其他自动化平台在AI功能上的具体性能对比，需评估其AI能力的独特性和实际效果。

**3. [AI] ollama/ollama (⭐163,047)**
*   **应用场景与价值**：项目描述明确指出其帮助用户快速上手运行包括Kimi-K2.5、GLM-5、MiniMax、DeepSeek、gpt-oss、Qwen、Gemma在内的多种模型。这对应了本地化部署、管理和运行多样化开源大模型的应用场景，价值在于简化模型获取与部署流程。
*   **潜在噪音**：数据未提供其与同类模型管理工具（如LM Studio）的功能差异比较。

**4. [金融科技] nautechsystems/nautilus_trader (⭐20,094)**
*   **应用场景与价值**：一个用Rust编写的高性能算法交易平台和事件驱动回测系统。其高星标数在金融科技类别中突出，对应专业量化交易和策略研发场景，落地价值在于为机构或个人交易者提供高性能、可靠的回测与实盘交易基础设施。
*   **潜在噪音**：数据未提供其性能基准测试结果或与Backtrader、Zipline等知名回测框架的对比信息。

**5. [Web3] foundry-rs/foundry (⭐10,129)**
*   **应用场景与价值**：一个用Rust编写的“极快、可移植且模块化”的以太坊应用开发工具包。它是Web3类别中星标最高的项目，对应智能合约开发、测试和部署的全流程场景，价值在于提升以太坊生态的开发效率与体验。
*   **潜在噪音**：数据未提供其与Hardhat、Truffle等主流以太坊开发框架在具体性能指标和开发者体验上的详细对比。

## 二、趋势观察与风险提示

1.  **AI领域主导热度**：星标最高的项目均集中于AI类别，特别是**AI助手（openclaw）、AI工作流/代理平台（n8n, langflow, dify）和模型部署工具（ollama）** 这三个子方向。这反映了当前开发者生态对AI应用化、工程化和平民化的强烈关注。
2.  **金融科技聚焦专业工具**：除高性能交易平台（nautilus_trader）外，列表中还出现了加密货币交易机器人（jesse）和基于移动支付的计费系统（Mpesa-Based_Wi-Fi-Hotspot_Billing_System），显示金融科技创新正同时向专业化（量化）和场景化（特定支付融合）两个维度延伸。
3.  **Web3强调安全与开发效率**：除了开发工具（foundry），列表中出现两个反钓鱼/威胁检测项目（eth-phishing-detect, destroylist），表明在Web3领域，安全基础设施与开发者工具同等重要，是当前建设的重点。
4.  **通用开发基础稳固**：TensorFlow作为老牌机器学习框架仍保持极高热度，而BarraCUDA项目（将CUDA代码编译到AMD GPU）则指向了针对特定硬件生态的底层工具创新需求。

**综合风险提示**：
*   **AI概念泛化**：多个AI项目（如AutoGPT、langflow、dify）的描述均涉及“AI智能体/工作流”，但输入数据未提供它们之间清晰的功能边界或技术架构差异，存在概念重叠和同质化竞争的可能。
*   **数据不足领域**：对于部分项目（如free-v2ray-public-list, defillama-server），仅从名称和简短描述难以准确判断其核心技术创新点与长期价值，需更多信息进行评估。
*   **落地验证缺失**：所有项目的星标数仅反映GitHub社区关注度，输入数据未包含任何关于项目实际生产环境采用率、商业成功案例或性能基准的数据，因此无法判断其真实的商业落地成熟度。

### 🌐 联网检索摘要

联网检索共 15 条（关键词: 2026-02-21 全球市场 盘面 复盘 原因, 2026-02-21 中国 宏观 经济 政策 市场 影响, 2026-02-21 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 上涨 原因, 徐梦桃王心迪李天马出战混团 事件 背景, 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准 事件 背景, 金银价再度大涨 事件 背景）
1. [2026-02-21 13:43] nfnews.com | 2026年，谁来接棒公募基金233%的收益神话？ - nfnews.com
   摘要: 2026年，谁来接棒公募基金233%的收益神话？ nfnews.com
   链接: https://news.google.com/rss/articles/CBMiWkFVX3lxTE5oV21MeG5GVV9nQzN1c3NJVTRodU13UnM4TWw5VU04cWx2RVJZU1FuS01kS3FRb2JHdXVqanVRRzRwMWdSaE9ER3pBeFRaMlpTMkxUVXFGV3o3UQ?oc=5
2. [2026-02-21 13:29] 新浪财经 | 【环球财经】巴西股市创历史新高 美最高法院裁决提振市场信心 - 新浪财经
   摘要: 【环球财经】巴西股市创历史新高 美最高法院裁决提振市场信心 新浪财经
   链接: https://news.google.com/rss/articles/CBMigAFBVV95cUxQSm40Mk51bUs1ZGdzU3podHd3ckFBLUlma00waE5Vem5oSDZpd1Fib2hlVlBfMlJZR2pXbzhjckhEd3NHVzlxWHQzNnJ4LVVtUlB3dDFuckRWMS1JY3RHbmNndzBpTEgxTjNzVFdmYlBlTzd4VHdpeHlnVGNGT2Y3Nw?oc=5
3. [2026-02-21 11:51] 新浪财经 | 印度AI峰会连闹笑话！2家顶尖机构被曝用宇树机器狗冒充自研【附机器狗行业分析】 - 新浪财经
   摘要: 印度AI峰会连闹笑话！2家顶尖机构被曝用宇树机器狗冒充自研【附机器狗行业分析】 新浪财经
   链接: https://news.google.com/rss/articles/CBMieEFVX3lxTFBsLUNoMDMxUE9KaXZKVUk5YXRkTFNKbEpFamNRVE9SZl8yMlJRdVB2UE5IdldKM1ptaG5jMFFWTFI3WFFud3g3M25sa0xXMW82V1BOdG4wMnVaMVVXWldWM3hNQWlEdXhMTHBRUUJvLXVWMmZkWVM4cA?oc=5
4. [2026-02-21 11:03] 万维读者网 | 美股创20年来首年最差纪录 - 万维读者网
   摘要: 美股创20年来首年最差纪录 万维读者网
   链接: https://news.google.com/rss/articles/CBMiUkFVX3lxTE1WSDNxZ3dzeWFoNWZpMlk3T05wZ2RPbFZZSllnajdvWXU4T0pxWk13eW1pd2xDSkZNaEhSQXQ1cURwRl96YTBaZC1mMTA5ZnFmMVE?oc=5
5. [2026-02-21 10:11] 3DM | 环亚国际娱乐登录网址(娱乐行业资讯) - 3DM
   摘要: 环亚国际娱乐登录网址(娱乐行业资讯) 3DM
   链接: https://news.google.com/rss/articles/CBMiV0FVX3lxTE1ncGZab19BMlpHbUNCT0s0VlotTVhETjEwRVQwU3VfX21FNmxhemFaTk1MT19wekswS0w1SGpMYmV1alNUSUh3MHUxWDVId0hQU2xVQXFfRQ?oc=5
6. [2026-02-21 09:00] news.17173.com | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - news.17173.com
   摘要: 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 news.17173.com
   链接: https://news.google.com/rss/articles/CBMiZkFVX3lxTE9SNi1JaUtGay14WGNGN0NfM1dzSkVOTVlWS0ZBdjVlNFZjWWRDdHd1cFBENEU5ekI2N1dzT3hvQzBZM0Y3R012SERVeUdtRFNFQ0l4WTM2WjVTa0ViLTM2VVpHcDlGdw?oc=5
7. [2026-02-21 08:24] yeeyi | 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 - yeeyi
   摘要: 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 yeeyi
   链接: https://news.google.com/rss/articles/CBMiVkFVX3lxTE91dGZGTy1OSTZSb2VXUjhVVC1kRFFtM0g5aXRtNXdzUThFR2lCanJhRlVrUk9xTExQSmpramhzUzJPRXItSGFMYXdmZ2VRc1g3Nmk0c1VB?oc=5
8. [2026-02-21 08:20] thepaper.cn | 首席展望｜摩根大通刘鸣镝：A股进入“慢牛”，外资回流可期 - thepaper.cn
   摘要: 首席展望｜摩根大通刘鸣镝：A股进入“慢牛”，外资回流可期 thepaper.cn
   链接: https://news.google.com/rss/articles/CBMiYEFVX3lxTE0yemJ2MnYyX3ZFdlYtMloyQ0hDcWZGT01jZXZUQjRYV2t1bFRaM1Vfd094cUlyY1NSSU1JNGlJNUpSWFE5S1JMQ29XRTd6Z3VHX3lRVVhBQmlrRkZyXzUzYg?oc=5
9. [2026-02-21 08:09] 新浪财经 | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - 新浪财经
   摘要: 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 新浪财经
   链接: https://news.google.com/rss/articles/CBMif0FVX3lxTE1OQlg5QnNON2hKWlFSclQ2bVh5ZVhqcXB4b0Itck5VRG5TcW81TVkzeVpEWXItM2xWOGo5QlpVSFVQSkNFWW45NWxubXMxMmNTSzhMazM3N21ybUhUR0t3aU4zMHRrTDluLVFBY1pEcFRMWlFKUDA4MkRYQ0l4QTA?oc=5
10. [2026-02-21 08:01] 新浪财经 | 从流量到留量：2025年消费并购的静水深流 - 新浪财经
   摘要: 从流量到留量：2025年消费并购的静水深流 新浪财经
   链接: https://news.google.com/rss/articles/CBMif0FVX3lxTE9fY3dBaHlhQW84VUF6cXpvb3FBVWFSbTc4NG5pQThVZ3ZYMENxRm9zVS1XcWZXaEk2clJ4QkFLUlMyUnM1VFotazVWSUZEMkpzWVozY2ZOX1VMU19FSFNhYmdlV25LZkR4R05KTkNyS3NzeURRSmxsM2dnNW9pcjA?oc=5
11. [2026-02-21 07:47] 富途牛牛 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛
   摘要: 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% 富途牛牛
   链接: https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5
12. [2026-02-21 07:15] 新浪财经 | 新浪财经隔夜要闻大事汇总：2026年2月21日 - 新浪财经
   摘要: 新浪财经隔夜要闻大事汇总：2026年2月21日 新浪财经
   链接: https://news.google.com/rss/articles/CBMihAFBVV95cUxQY25wdUpCLWtCOUloS2FsaTFna0M1bEZoVTY3aXQ4OUY3WFNOLWFtU2lUMFYzeW8tdTc3RDBYVGF1YXdEeng0bTdZUzdWblhINGVfYnEtSHI5ZWFvOUNmaV9iTjliYTZMR3RDaHlfUTNwRFprdEhtdDdrS1dtTkQ2aUZFVlk?oc=5
13. [2026-02-21 07:11] 游侠网 | 热点第一 DAFA八百八十八国际 - 游侠网
   摘要: 热点第一 DAFA八百八十八国际 游侠网
   链接: https://news.google.com/rss/articles/CBMiTkFVX3lxTFA5aExXVjI3bF9PVDYxeWpQcnJzN0xQMzJXekhiaWJaMVh4MU95V3l1TTRwNERiMVE0RERvQ2F5SnNBdmI1Mk9sWTNkTDc5dw?oc=5
14. [2026-02-21 05:30] 英为财情 Investing.com | 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5
15. [2026-02-21 05:30] 英为财情 Investing.com | 加拿大股市上涨；截至收盘加拿大多伦多S&P/TSX 综合指数上涨0.66% 提供者 Investing.com - 英为财情 Investing.com
   摘要: 加拿大股市上涨；截至收盘加拿大多伦多S&P/TSX 综合指数上涨0.66% 提供者 Investing.com 英为财情 Investing.com
   链接: https://news.google.com/rss/articles/CBMicEFVX3lxTE40WFNNZHp1QW1SLUpVNG5LSUpoMFMyQlFJbkJWTW50VnFXcm9LWGZaM19LM0h2UXpOLVp4WEkwZ3p5azUyZHhQYmlzQy02dlVNRTcwOW1RU2hmMUNBUTd0Q2oyb2NxMGJGTEdWbHF3YVo?oc=5

</details>


### 📎 引用脚注

1. [2026-02-21T12:00 @NexusLabs | Introducing USDX — the native dollar of the Nexus economy. A shared settlement layer for...](https://twitter.com/NexusLabs/status/2024138532512567297)（Twitter，匹配分=100，来源ID=TW01）
2. [2026-02-21T12:00 @cryptorover | 💥BREAKING: BlackRock buys $64,500,000 worth of Bitcoin.](https://twitter.com/cryptorover/status/2025078124833116434)（Twitter，匹配分=100，来源ID=TW13）
3. [2026-02-21T12:00 @BitcoinMagazine | JUST IN: Bitcoin's hashrate has increased over 28% from its recent bottom! 🚀](https://twitter.com/BitcoinMagazine/status/2024859538562662650)（Twitter，匹配分=100，来源ID=TW15）
4. [2026-02-21T12:00 @JacobKinge | Howard Lutnick is arguably one of the slickest and most corrupt operators in modern fina...](https://twitter.com/JacobKinge/status/2024906835610710212)（Twitter，匹配分=100，来源ID=TW03）
5. [2026-02-21T12:00 @narendramodi | India is honoured to welcome President Lula and his delegation, which includes distingui...](https://twitter.com/narendramodi/status/2025149417636896912)（Twitter，匹配分=100，来源ID=TW02）
6. [2026-02-21T12:00 @the_17thletter4 | BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, h...](https://twitter.com/the_17thletter4/status/2024859960853622861)（Twitter，匹配分=100，来源ID=TW08）
7. [2026-02-21T12:00 @WHLeavitt | 🚨 ALERT: Bombshell—20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia H...](https://twitter.com/WHLeavitt/status/2024983554992840962)（Twitter，匹配分=100，来源ID=TW10）
8. [2026-02-21T12:00 @Milajoy | REP. AOC’S ILLEGAL HIRE SCANDAL EXPLODES AOC knowingly put an illegal alien—zero work pa...](https://twitter.com/Milajoy/status/2024773028660559988)（Twitter，匹配分=100，来源ID=TW05）
9. [2026-02-21 07:47 富途牛牛 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5)（联网检索，匹配分=100，来源ID=WB03）
10. [2026-02-21 11:51 新浪财经 | 印度AI峰会连闹笑话！2家顶尖机构被曝用宇树机器狗冒充自研【附机器狗行业分析】 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTFBsLUNoMDMxUE9KaXZKVUk5YXRkTFNKbEpFamNRVE9SZl8yMlJRdVB2UE5IdldKM1ptaG5jMFFWTFI3WFFud3g3M25sa0xXMW82V1BOdG4wMnVaMVVXWldWM3hNQWlEdXhMTHBRUUJvLXVWMmZkWVM4cA?oc=5)（联网检索，匹配分=100，来源ID=WB11）
11. [2026-02-21 13:29 新浪财经 | 【环球财经】巴西股市创历史新高 美最高法院裁决提振市场信心 - 新浪财经](https://news.google.com/rss/articles/CBMigAFBVV95cUxQSm40Mk51bUs1ZGdzU3podHd3ckFBLUlma00waE5Vem5oSDZpd1Fib2hlVlBfMlJZR2pXbzhjckhEd3NHVzlxWHQzNnJ4LVVtUlB3dDFuckRWMS1JY3RHbmNndzBpTEgxTjNzVFdmYlBlTzd4VHdpeHlnVGNGT2Y3Nw?oc=5)（联网检索，匹配分=100，来源ID=WB14）
12. [2026-02-21 08:09 新浪财经 | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTE1OQlg5QnNON2hKWlFSclQ2bVh5ZVhqcXB4b0Itck5VRG5TcW81TVkzeVpEWXItM2xWOGo5QlpVSFVQSkNFWW45NWxubXMxMmNTSzhMazM3N21ybUhUR0t3aU4zMHRrTDluLVFBY1pEcFRMWlFKUDA4MkRYQ0l4QTA?oc=5)（联网检索，匹配分=100，来源ID=WB09）
13. [2026-02-21 09:00 news.17173.com | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - news.17173.com](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9SNi1JaUtGay14WGNGN0NfM1dzSkVOTVlWS0ZBdjVlNFZjWWRDdHd1cFBENEU5ekI2N1dzT3hvQzBZM0Y3R012SERVeUdtRFNFQ0l4WTM2WjVTa0ViLTM2VVpHcDlGdw?oc=5)（联网检索，匹配分=100，来源ID=WB10）

## 🧪 引用匹配校验

- 已匹配引用条数: 13
- 未完成匹配标签: 0
- 低置信引用条数: 0
- 处理建议: 本次未发现低置信引用。

## 🎯 投机方向（超短）

- 海外指数方向：美股 VIX波动率指数 -5.64%（高波动回撤）
- 高波动资产：SOL 24h +2.19%（轻仓快进快出）
- 纪律：只跟踪 1-2 个方向，止损先于加仓，单笔风险不超本金 1%-2%。

## 🌐 联网检索补充

- 关键词：2026-02-21 全球市场 盘面 复盘 原因, 2026-02-21 中国 宏观 经济 政策 市场 影响, 2026-02-21 AI 科技 行业 动态 影响, VIX波动率指数 下跌 原因, SOL 上涨 原因, 徐梦桃王心迪李天马出战混团 事件 背景, 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准 事件 背景, 金银价再度大涨 事件 背景
- 命中结果：15 条（按发布时间倒序）

### 🔎 2026-02-21 中国 宏观 经济 政策 市场 影响

- [2026年，谁来接棒公募基金233%的收益神话？ - nfnews.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5oV21MeG5GVV9nQzN1c3NJVTRodU13UnM4TWw5VU04cWx2RVJZU1FuS01kS3FRb2JHdXVqanVRRzRwMWdSaE9ER3pBeFRaMlpTMkxUVXFGV3o3UQ?oc=5)
  - 来源: nfnews.com | 时间: 2026-02-21 13:43
  - 摘要: 2026年，谁来接棒公募基金233%的收益神话？ nfnews.com
- [【环球财经】巴西股市创历史新高 美最高法院裁决提振市场信心 - 新浪财经](https://news.google.com/rss/articles/CBMigAFBVV95cUxQSm40Mk51bUs1ZGdzU3podHd3ckFBLUlma00waE5Vem5oSDZpd1Fib2hlVlBfMlJZR2pXbzhjckhEd3NHVzlxWHQzNnJ4LVVtUlB3dDFuckRWMS1JY3RHbmNndzBpTEgxTjNzVFdmYlBlTzd4VHdpeHlnVGNGT2Y3Nw?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-21 13:29
  - 摘要: 【环球财经】巴西股市创历史新高 美最高法院裁决提振市场信心 新浪财经
- [环亚国际娱乐登录网址(娱乐行业资讯) - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTE1ncGZab19BMlpHbUNCT0s0VlotTVhETjEwRVQwU3VfX21FNmxhemFaTk1MT19wekswS0w1SGpMYmV1alNUSUh3MHUxWDVId0hQU2xVQXFfRQ?oc=5)
  - 来源: 3DM | 时间: 2026-02-21 10:11
  - 摘要: 环亚国际娱乐登录网址(娱乐行业资讯) 3DM
- [首席展望｜摩根大通刘鸣镝：A股进入“慢牛”，外资回流可期 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE0yemJ2MnYyX3ZFdlYtMloyQ0hDcWZGT01jZXZUQjRYV2t1bFRaM1Vfd094cUlyY1NSSU1JNGlJNUpSWFE5S1JMQ29XRTd6Z3VHX3lRVVhBQmlrRkZyXzUzYg?oc=5)
  - 来源: thepaper.cn | 时间: 2026-02-21 08:20
  - 摘要: 首席展望｜摩根大通刘鸣镝：A股进入“慢牛”，外资回流可期 thepaper.cn
- [从流量到留量：2025年消费并购的静水深流 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTE9fY3dBaHlhQW84VUF6cXpvb3FBVWFSbTc4NG5pQThVZ3ZYMENxRm9zVS1XcWZXaEk2clJ4QkFLUlMyUnM1VFotazVWSUZEMkpzWVozY2ZOX1VMU19FSFNhYmdlV25LZkR4R05KTkNyS3NzeURRSmxsM2dnNW9pcjA?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-21 08:01
  - 摘要: 从流量到留量：2025年消费并购的静水深流 新浪财经
- [新浪财经隔夜要闻大事汇总：2026年2月21日 - 新浪财经](https://news.google.com/rss/articles/CBMihAFBVV95cUxQY25wdUpCLWtCOUloS2FsaTFna0M1bEZoVTY3aXQ4OUY3WFNOLWFtU2lUMFYzeW8tdTc3RDBYVGF1YXdEeng0bTdZUzdWblhINGVfYnEtSHI5ZWFvOUNmaV9iTjliYTZMR3RDaHlfUTNwRFprdEhtdDdrS1dtTkQ2aUZFVlk?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-21 07:15
  - 摘要: 新浪财经隔夜要闻大事汇总：2026年2月21日 新浪财经

### 🔎 2026-02-21 AI 科技 行业 动态 影响

- [印度AI峰会连闹笑话！2家顶尖机构被曝用宇树机器狗冒充自研【附机器狗行业分析】 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTFBsLUNoMDMxUE9KaXZKVUk5YXRkTFNKbEpFamNRVE9SZl8yMlJRdVB2UE5IdldKM1ptaG5jMFFWTFI3WFFud3g3M25sa0xXMW82V1BOdG4wMnVaMVVXWldWM3hNQWlEdXhMTHBRUUJvLXVWMmZkWVM4cA?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-21 11:51
  - 摘要: 印度AI峰会连闹笑话！2家顶尖机构被曝用宇树机器狗冒充自研【附机器狗行业分析】 新浪财经
- [摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - news.17173.com](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9SNi1JaUtGay14WGNGN0NfM1dzSkVOTVlWS0ZBdjVlNFZjWWRDdHd1cFBENEU5ekI2N1dzT3hvQzBZM0Y3R012SERVeUdtRFNFQ0l4WTM2WjVTa0ViLTM2VVpHcDlGdw?oc=5)
  - 来源: news.17173.com | 时间: 2026-02-21 09:00
  - 摘要: 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 news.17173.com
- [摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTE1OQlg5QnNON2hKWlFSclQ2bVh5ZVhqcXB4b0Itck5VRG5TcW81TVkzeVpEWXItM2xWOGo5QlpVSFVQSkNFWW45NWxubXMxMmNTSzhMazM3N21ybUhUR0t3aU4zMHRrTDluLVFBY1pEcFRMWlFKUDA4MkRYQ0l4QTA?oc=5)
  - 来源: 新浪财经 | 时间: 2026-02-21 08:09
  - 摘要: 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 新浪财经
- [热点第一 DAFA八百八十八国际 - 游侠网](https://news.google.com/rss/articles/CBMiTkFVX3lxTFA5aExXVjI3bF9PVDYxeWpQcnJzN0xQMzJXekhiaWJaMVh4MU95V3l1TTRwNERiMVE0RERvQ2F5SnNBdmI1Mk9sWTNkTDc5dw?oc=5)
  - 来源: 游侠网 | 时间: 2026-02-21 07:11
  - 摘要: 热点第一 DAFA八百八十八国际 游侠网

### 🔎 VIX波动率指数 下跌 原因

- [美股创20年来首年最差纪录 - 万维读者网](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1WSDNxZ3dzeWFoNWZpMlk3T05wZ2RPbFZZSllnajdvWXU4T0pxWk13eW1pd2xDSkZNaEhSQXQ1cURwRl96YTBaZC1mMTA5ZnFmMVE?oc=5)
  - 来源: 万维读者网 | 时间: 2026-02-21 11:03
  - 摘要: 美股创20年来首年最差纪录 万维读者网
- [美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5)
  - 来源: 富途牛牛 | 时间: 2026-02-21 07:47
  - 摘要: 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% 富途牛牛
- [美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-21 05:30
  - 摘要: 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com 英为财情 Investing.com
- [加拿大股市上涨；截至收盘加拿大多伦多S&P/TSX 综合指数上涨0.66% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE40WFNNZHp1QW1SLUpVNG5LSUpoMFMyQlFJbkJWTW50VnFXcm9LWGZaM19LM0h2UXpOLVp4WEkwZ3p5azUyZHhQYmlzQy02dlVNRTcwOW1RU2hmMUNBUTd0Q2oyb2NxMGJGTEdWbHF3YVo?oc=5)
  - 来源: 英为财情 Investing.com | 时间: 2026-02-21 05:30
  - 摘要: 加拿大股市上涨；截至收盘加拿大多伦多S&P/TSX 综合指数上涨0.66% 提供者 Investing.com 英为财情 Investing.com

### 🔎 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准 事件 背景

- [春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTE91dGZGTy1OSTZSb2VXUjhVVC1kRFFtM0g5aXRtNXdzUThFR2lCanJhRlVrUk9xTExQSmpramhzUzJPRXItSGFMYXdmZ2VRc1g3Nmk0c1VB?oc=5)
  - 来源: yeeyi | 时间: 2026-02-21 08:24
  - 摘要: 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 yeeyi

## 🔗 AI 分析引用来源

> 以下链接与正文角标一一对应；完整候选链接请看后文“原始链接索引”。

### Twitter (8 条)

- [¹] [2026-02-21T12:00 @NexusLabs | Introducing USDX — the native dollar of the Nexus economy. A shared settlement layer for...](https://twitter.com/NexusLabs/status/2024138532512567297)（匹配分=100，来源ID=TW01）
- [²] [2026-02-21T12:00 @cryptorover | 💥BREAKING: BlackRock buys $64,500,000 worth of Bitcoin.](https://twitter.com/cryptorover/status/2025078124833116434)（匹配分=100，来源ID=TW13）
- [³] [2026-02-21T12:00 @BitcoinMagazine | JUST IN: Bitcoin's hashrate has increased over 28% from its recent bottom! 🚀](https://twitter.com/BitcoinMagazine/status/2024859538562662650)（匹配分=100，来源ID=TW15）
- [⁴] [2026-02-21T12:00 @JacobKinge | Howard Lutnick is arguably one of the slickest and most corrupt operators in modern fina...](https://twitter.com/JacobKinge/status/2024906835610710212)（匹配分=100，来源ID=TW03）
- [⁵] [2026-02-21T12:00 @narendramodi | India is honoured to welcome President Lula and his delegation, which includes distingui...](https://twitter.com/narendramodi/status/2025149417636896912)（匹配分=100，来源ID=TW02）
- [⁶] [2026-02-21T12:00 @the_17thletter4 | BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, h...](https://twitter.com/the_17thletter4/status/2024859960853622861)（匹配分=100，来源ID=TW08）
- [⁷] [2026-02-21T12:00 @WHLeavitt | 🚨 ALERT: Bombshell—20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia H...](https://twitter.com/WHLeavitt/status/2024983554992840962)（匹配分=100，来源ID=TW10）
- [⁸] [2026-02-21T12:00 @Milajoy | REP. AOC’S ILLEGAL HIRE SCANDAL EXPLODES AOC knowingly put an illegal alien—zero work pa...](https://twitter.com/Milajoy/status/2024773028660559988)（匹配分=100，来源ID=TW05）

### 联网检索 (5 条)

- [⁹] [2026-02-21 07:47 富途牛牛 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5)（匹配分=100，来源ID=WB03）
- [¹⁰] [2026-02-21 11:51 新浪财经 | 印度AI峰会连闹笑话！2家顶尖机构被曝用宇树机器狗冒充自研【附机器狗行业分析】 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTFBsLUNoMDMxUE9KaXZKVUk5YXRkTFNKbEpFamNRVE9SZl8yMlJRdVB2UE5IdldKM1ptaG5jMFFWTFI3WFFud3g3M25sa0xXMW82V1BOdG4wMnVaMVVXWldWM3hNQWlEdXhMTHBRUUJvLXVWMmZkWVM4cA?oc=5)（匹配分=100，来源ID=WB11）
- [¹¹] [2026-02-21 13:29 新浪财经 | 【环球财经】巴西股市创历史新高 美最高法院裁决提振市场信心 - 新浪财经](https://news.google.com/rss/articles/CBMigAFBVV95cUxQSm40Mk51bUs1ZGdzU3podHd3ckFBLUlma00waE5Vem5oSDZpd1Fib2hlVlBfMlJZR2pXbzhjckhEd3NHVzlxWHQzNnJ4LVVtUlB3dDFuckRWMS1JY3RHbmNndzBpTEgxTjNzVFdmYlBlTzd4VHdpeHlnVGNGT2Y3Nw?oc=5)（匹配分=100，来源ID=WB14）
- [¹²] [2026-02-21 08:09 新浪财经 | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTE1OQlg5QnNON2hKWlFSclQ2bVh5ZVhqcXB4b0Itck5VRG5TcW81TVkzeVpEWXItM2xWOGo5QlpVSFVQSkNFWW45NWxubXMxMmNTSzhMazM3N21ybUhUR0t3aU4zMHRrTDluLVFBY1pEcFRMWlFKUDA4MkRYQ0l4QTA?oc=5)（匹配分=100，来源ID=WB09）
- [¹³] [2026-02-21 09:00 news.17173.com | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - news.17173.com](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9SNi1JaUtGay14WGNGN0NfM1dzSkVOTVlWS0ZBdjVlNFZjWWRDdHd1cFBENEU5ekI2N1dzT3hvQzBZM0Y3R012SERVeUdtRFNFQ0l4WTM2WjVTa0ViLTM2VVpHcDlGdw?oc=5)（匹配分=100，来源ID=WB10）


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
| BTC | $68,074.00 | 🟢 +1.08% |
| ETH | $1,976.55 | 🟢 +1.67% |
| SOL | $85.33 | 🟢 +2.19% |

### 📈 国际期货

| 品种 | 价格 | 涨跌幅 |
|------|------|--------|
| WTI原油 | 66.39 | 🔴 -0.06% |
| 布伦特原油 | 71.76 | 🟢 +0.14% |
| 天然气 | 3.05 | 🟢 +1.70% |
| COMEX铜 | 5.83 | 🟢 +1.76% |

### 💻 GitHub 趋势

- ⭐ [**ClawWork**](https://github.com/HKUDS/ClawWork) (4692 stars)
  - "ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"
- ⭐ [**visual-explainer**](https://github.com/nicobailon/visual-explainer) (2022 stars)
  - Agent skill + prompt templates that generate rich HTML pages for visual diff rev
- ⭐ [**portless**](https://github.com/vercel-labs/portless) (1894 stars)
  - Replace port numbers with stable, named .localhost URLs. For humans and agents.
- ⭐ [**arscontexta**](https://github.com/agenticnotetaking/arscontexta) (1374 stars)
  - Claude Code plugin that generates individualized knowledge systems from conversa
- ⭐ [**nullclaw**](https://github.com/nullclaw/nullclaw) (1301 stars)
  - Fastest, smallest, and fully autonomous AI assistant infrastructure written in Z

## 🐦 Twitter 热点 (97 条)

- 来源统计: 关注账号 240 条 | 热门讨论 30 条

### 🔥 热门讨论推文

- `2026-02-21T12:00` @NexusLabs ❤️9535 🔁8580 💬9318
  - Introducing USDX — the native dollar of the Nexus economy.  A shared settlement layer for all apps, trades, and markets on Nexus.  One asset. Unified liquidity. Protocol-native incentives.  Capital is converging, and USDX is its native home.  Read more:blog.nexus.xyz/introducing-u…
  - [原文链接](https://twitter.com/NexusLabs/status/2024138532512567297)
- `2026-02-21T12:00` @narendramodi ❤️17779 🔁1567 💬677
  - India is honoured to welcome President Lula and his delegation, which includes distinguished ministers and business leaders. India-Brazil relations have long benefited from President Lula’s vision and inspiring leadership. His presence at the AI Summit has also infused new energy into our strategic partnership. Our talks covered the full range of India-Brazil friendship across diverse sectors.@LulaOficial
  - [原文链接](https://twitter.com/narendramodi/status/2025149417636896912)
- `2026-02-21T12:00` @JacobKinge ❤️12886 🔁4057 💬455
  - Howard Lutnick is arguably one of the slickest and most corrupt operators in modern finance.  We now know he was close friends with Jeffrey Epstein, despite him previously denying it. That link was confirmed in the Epstein files. He also has documented ties to Tether and Bitcoin market manipulation.  Now a brand new scheme has surfaced involving Cantor Fitzgerald, run by one of his sons.  The firm has been buying the rights to U.S. tariff refunds at massive discounts.   Here is how this scam wor
  - [原文链接](https://twitter.com/JacobKinge/status/2024906835610710212)
- `2026-02-21T12:00` @MedicoLiberdade ❤️10261 🔁1942 💬214
  - E aí@BlogdoNoblat, vai comentar o cartão de crédito corporativo de painho que gastou + de 50 vezes o que bonoro gastou, ou vai ficar calado como o inútil comuna que você é?
  - [原文链接](https://twitter.com/MedicoLiberdade/status/2024964381675569406)
- `2026-02-21T12:00` @Milajoy ❤️6073 🔁3608 💬622
  - REP. AOC’S ILLEGAL HIRE SCANDAL EXPLODES    AOC knowingly put an illegal alien—zero work papers, pure lawbreaker—on payroll as her Legislative Assistant.   AOC IS GOING TO JAIL.   Straight-up violated 8 U.S.C. § 1324a, the fed law banning this exact move.   She KNEW, hired anyway, and now faces the heat: $3,200–$16,000 in fines, maybe $3,000 more plus 6 months in jail.   Congress can’t shield her—IRCA doesn’t care about titles.   X’s buzzing: is this hypocrisy or just reckless?   Proof’s out the
  - [原文链接](https://twitter.com/Milajoy/status/2024773028660559988)
- `2026-02-21T12:00` @Playnance_ ❤️2379 🔁4395 💬871
  - CryptoWisser spotlights the model behind G Coin 💎  As CryptoWisser writes, G Coin represents “a token-linked distribution economy with multiple measurable components.”  That’s the mechanism.  Every new Boss platform becomes a distribution node. Every distribution node drives real activity. Every interaction settles in G Coin.  More partners → more platforms → more player activity → more token usage.  This is revenue-linked utility embedded directly into live infrastructure.  Read the full piece 
  - [原文链接](https://twitter.com/Playnance_/status/2024515923630039477)
- `2026-02-21T12:00` @kangminjlee ❤️5163 🔁671 💬111
  - Turns out mass immigration actually doesn't help the economy in the long run  Instead Canadians got depressed wages, skyrocketed cost of living, and feeling like a foreigner in their own country because they were displaced by millions of unassimilated foreigners
  - [原文链接](https://twitter.com/kangminjlee/status/2024889042400055362)
- `2026-02-21T12:00` @the_17thletter4 ❤️2646 🔁1045 💬1100
  - BREAKING 🅱️:  20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hidden in CIA vault for ~10 years, to undermine Trump’s election via manipulated intel.  Do you support arresting Hussein Obama for treason?  A. Hell yeah B. No  MAKE THIS GO VIRAL ON 𝕏.👏
  - [原文链接](https://twitter.com/the_17thletter4/status/2024859960853622861)
- `2026-02-21T12:00` @jisoogaIIery ❤️3522 🔁613 💬3
  - FACE ECONOMY
  - [原文链接](https://twitter.com/jisoogaIIery/status/2024851114689188167)
- `2026-02-21T12:00` @WHLeavitt ❤️1981 🔁534 💬663
  - 🚨 ALERT: Bombshell—20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hidden in CIA vault for ~10 years, to undermine Trump’s election via manipulated intel.  Do you support arresting Hussein Obama for treason?  A. Hell yeah B. Nah
  - [原文链接](https://twitter.com/WHLeavitt/status/2024983554992840962)
- `2026-02-21T12:00` @RodiumInsights ❤️1986 🔁1004 💬61
  - یاد ہے !”عاصم منیر نے کہا تھا تم اللہ کی جنگ لڑ رہے ہو وہ اسکے ساتھ نہیں ہے ۔“ آج یہ حالت ہے ریاست نے انکو پہچاننے سے انکار کر دیا ہے۔ میرا نہیں خیال کہ یہ کوئی AI وڈیو ہے ۔ لیکن میرا سوال ہے کیا آپ لوگوں کو انکے ساتھ ہمدردی کرنی چاہئیے ؟آپ لوگوں کو 26 نومبر یاد ہے ؟جب لوگ ایمبولینس میں زخمی پڑے ہوئے تھے تو انکو ایمبولینس کے اندر ہی گولیاں ماری جا رہی تھیں ،اور لوگ کہہ رہے تھے انکو مت مارو لیکن کوہی سننے والا نہیں تھا ۔ نو مئی یاد ہے ؟مرید کے یاد ہے ؟ کیا ان سے ہمدردی کرنی چاہئیے؟
  - [原文链接](https://twitter.com/RodiumInsights/status/2024935415955030328)
- `2026-02-21T12:00` @RepOfSomaliland ❤️1799 🔁159 💬131
  - Hey@Grok, remove the unstable, persistently high-inflation currency.
  - [原文链接](https://twitter.com/RepOfSomaliland/status/2024570762263482644)
- `2026-02-21T12:00` @cryptorover ❤️1473 🔁243 💬250
  - 💥BREAKING:  BlackRock buys $64,500,000 worth of Bitcoin.
  - [原文链接](https://twitter.com/cryptorover/status/2025078124833116434)
- `2026-02-21T12:00` @barkmeta ❤️1562 🔁98 💬233
  - Might want to stock up on groceries and fill your gas tank before the market opens Monday...
  - [原文链接](https://twitter.com/barkmeta/status/2024980940032737675)
- `2026-02-21T12:00` @BitcoinMagazine ❤️1335 🔁235 💬106
  - JUST IN: Bitcoin's hashrate has increased over 28% from its recent bottom! 🚀
  - [原文链接](https://twitter.com/BitcoinMagazine/status/2024859538562662650)
- `2026-02-21T12:00` @blueorms ❤️1249 🔁403 💬3
  - *guess the word game*  ling: this is something i did for orm yesterday  orm: peeling the prawn and feeding it ~   so ling peeled the prawns and fed it to orm yesterday 😭😭  LINGORM FAN MEET IN SG#LingOrm2ndFMinSingapore
  - [原文链接](https://twitter.com/blueorms/status/2025161384317817235)
- `2026-02-21T12:00` @Dank_jetha ❤️1516 🔁90 💬17
  - Youth congress leaders at the AI summit
  - [原文链接](https://twitter.com/Dank_jetha/status/2025142632289370245)
- `2026-02-21T12:00` @JerryDunleavy ❤️583 🔁123 💬15
  - NEW: The CIA is retracting *19* politicized intelligence products spanning the last decade or so, many of which improperly inserted DEI nonsense into intel analysis, including assessments on white women & violent extremism, LGBT issues, abortion, and more.justthenews.com/government/s…
  - [原文链接](https://twitter.com/JerryDunleavy/status/2024952714652971186)
- `2026-02-21T12:00` @PeterDClack ❤️385 🔁197 💬25
  - The 'inner circle' that is driving the $9.2 trillion a year net zero economy, also controls the satellites, the weather stations, media releases and formal IPCC summaries.  It's a closed-loop system where the crisis makers justify the funding, then the funding maintains the crisis makers.  We're told we are in a climate emergency yet global life expectancy is at an all-time high. Deaths from extreme weather have plunged by 98% over the last century.  The net zero narrative ignores the many 'upsi
  - [原文链接](https://twitter.com/PeterDClack/status/2025125352545362422)
- `2026-02-21T12:00` @OndoFinance ❤️485 🔁74 💬32
  - Tokenization goes mainstream by tapping into TradFi.  Ondo's tokenized stock trades execute under 5bps of slippage (compared to market order book prices).   No other platform has demonstrated the same.  ❎ PROBLEM: Liquidity pools do not scale  Most tokenized stock platforms operate in isolation from traditional markets, meaning they need to bootstrap onchain liquidity from scratch.  Even with a conservative $1 million pool per asset, supporting all 6,000+ stocks on NYSE and Nasdaq would require 
  - [原文链接](https://twitter.com/OndoFinance/status/2024863432927846547)

### @TheEconomist (10 条)

- `2026-02-21T12:00` Russia shows no sign of an impending breakdown, political or economic. But from travel and wages to the priesthood and innovation, the war is impinging on almost every aspect of everyday life: http://econ.st/4aZo1lm  Photo: AP
  - [原文链接](https://twitter.com/TheEconomist/status/2025178718574879184)
- `2026-02-21T11:40` “Three months ago we were just TikTokers.” On “The Weekend Intelligence” podcast we meet the Gen Z revolutionaries who toppled the government in Nepal https://www.economist.com/podcasts/2026/02/21/inside-nepals-gen-z-revolution
  - [原文链接](https://twitter.com/TheEconomist/status/2025173665805893672)
- `2026-02-21T11:20` A measles outbreak in London with 61 cases so far this year is causing alarm. The number of fully vaccinated five-year-olds is well below the national average https://www.economist.com/britain/2026/02/19/north-london-is-suffering-a-measles-outbreak
  - [原文链接](https://twitter.com/TheEconomist/status/2025168632716619926)
- `2026-02-21T11:00` If the kilt spread over gilts gets too wide, perhaps even the most ardent nationalist will blush https://www.economist.com/britain/2026/02/19/the-scottish-governments-new-bonds-will-waste-taxpayers-money
  - [原文链接](https://twitter.com/TheEconomist/status/2025163636172267714)
- `2026-02-21T10:50` Paying attention to a meeting, especially a pointless one, may be a waste of time. But it signals commitment https://www.economist.com/business/2026/02/19/the-case-for-workplace-inefficiency
  - [原文链接](https://twitter.com/TheEconomist/status/2025161082474553761)
- *... 及其他 5 条*

### @zerohedge (10 条)

- `2026-02-21T12:00` Macron's India Trip Exposes EU Tech Overreach And Policy Failures https://www.zerohedge.com/economics/macrons-india-trip-exposes-eu-tech-overreach-and-policy-failures
  - [原文链接](https://twitter.com/zerohedge/status/2025178717127917834)
- `2026-02-21T04:25` Is It Time To Reopen The Franklin Child Prostitution Case After Epstein Revelations? https://www.zerohedge.com/markets/its-time-reopen-franklin-child-prostitution-case-after-epstein-revelations
  - [原文链接](https://twitter.com/zerohedge/status/2025064216395153408)
- `2026-02-21T04:07` Kevin Hassett should be sending thank you notes to the NY Fed: recall they calculated US consumers paid for 90% of tariff burden. So 90% of IEEPA refunds - $120BN - should go direct to consumers/firms. And with refund timing open-ended, they can be sent any time before midterms  zerohedge (@zerohedg
  - [原文链接](https://twitter.com/zerohedge/status/2025059717114912891)
- `2026-02-21T04:00` AI Content 'Incidents' Skyrocket: A Growing Threat In The Digital Age https://www.zerohedge.com/ai/ai-content-incidents-skyrocket-growing-threat-digital-age
  - [原文链接](https://twitter.com/zerohedge/status/2025057924112867816)
- `2026-02-21T03:56` a word from our sponsor: Remember when the halving was supposed to kill public miners? Meanwhile, Bitdeer just recorded 226% revenue growth, EBITDA positive, and an expanding energy footprint to 3 GW.  Bitdeer now accounts for roughly 7% of the global Bitcoin hash rate.
  - [原文链接](https://twitter.com/zerohedge/status/2025057021263847552)
- *... 及其他 5 条*

### @business (10 条)

- `2026-02-21T11:49` While no country can fully decouple from US or Chinese AI models anytime soon, alternatives are emerging. https://www.bloomberg.com/news/newsletters/2026-02-21/india-has-a-unique-recipe-for-ai-sovereignty-new-economy?taid=69999bb08e21f400010d9c23&utm_campaign=trueanthem&utm_content=business&utm_medi
  - [原文链接](https://twitter.com/business/status/2025175939500347602)
- `2026-02-21T11:23` What if there was a handbook called “How to Make Money by Not Buying the Worst Companies in the World”? https://www.bloomberg.com/news/newsletters/2026-02-21/why-finding-the-losers-is-the-way-to-win-merryn-talks-money?taid=699995998e21f400010d9bfd&utm_campaign=trueanthem&utm_content=business&utm_med
  - [原文链接](https://twitter.com/business/status/2025169399104094400)
- `2026-02-21T10:51` Governments around the world reacted with caution after the US Supreme Court invalidated President Donald Trump’s broad emergency tariffs https://www.bloomberg.com/news/articles/2026-02-21/world-leaders-scope-out-us-s-next-steps-after-trump-tariff-loss?taid=69998e18773d17000105e6fb&utm_campaign=true
  - [原文链接](https://twitter.com/business/status/2025161342450032663)
- `2026-02-21T10:34` The US economy has borne most of the burden of tariffs imposed by Donald Trump, European Central Bank Governing Council member Fabio Panetta said on Saturday. https://www.bloomberg.com/news/articles/2026-02-21/ecb-s-panetta-says-tariffs-have-damaged-the-us-more-than-others?taid=69998a4b97a5cc0001c4f
  - [原文链接](https://twitter.com/business/status/2025157263556587986)
- `2026-02-21T10:32` French President Emmanuel Macron urged calm before a march in Lyon organized by far-right groups to honor a man beaten to death in a street fight https://www.bloomberg.com/news/articles/2026-02-21/macron-urges-calm-before-protest-in-lyon-over-death-of-activist?taid=699989cbcc473e0001dfb312&utm_campa
  - [原文链接](https://twitter.com/business/status/2025156724269682873)
- *... 及其他 5 条*

### @WuBlockchain (8 条)

- `2026-02-21T11:28` According to http://localhost/SpecterAnalyst, IoTeX' private key may have been compromised, resulting in its token safe being drained with a total loss of approximately $8.8 million. IoTeX has officially responded, confirming the breach but stating that initial estimates indicate the potential loss 
  - [原文链接](https://twitter.com/WuBlockchain/status/2025170847950938233)
- `2026-02-21T11:14` WuBlockchain Weekly: MicroStrategy Says It Can Withstand Bitcoin Drop to $8,000, Altcoin Selling Pressure Hits Five-Year High, Ethereum Foundation Releases 2026 Plan, RWA Scale on Ethereum Mainnet Surpasses $17 Billion, etc http://wublock.substack.com/p/wublockchain-weekly-microstrategy-6fe?r=jbpop&
  - [原文链接](https://twitter.com/WuBlockchain/status/2025167297674109146)
- `2026-02-21T10:27` Uniswap Labs announced the release of 7 new "Skills" to enable AI Agents to execute operations on Uniswap. The 7 core skills specifically include: v4-security-foundations, configurator, deployer, viem-integration, swap-integration, liquidity-planner, and swap-planner. https://nitter.net/Uniswap/stat
  - [原文链接](https://twitter.com/WuBlockchain/status/2025155521754374453)
- `2026-02-21T05:20` On Feb. 20 (ET), total net inflows into Bitcoin spot ETFs reached $88.04 million. The Bitcoin spot ETF with the largest single-day net inflow was BlackRock's IBIT, which recorded $64.46 million in net inflows, bringing its cumulative historical net inflows to $61.303 billion. Ethereum spot ETFs saw 
  - [原文链接](https://twitter.com/WuBlockchain/status/2025078053752463383)
- `2026-02-21T04:15` According to Fortune, Wintermute founder Evgeny Gaevoy said on the Crypto Playbook podcast that the industry has drifted from its cypherpunk roots toward a "number go up" narrative. He argued that stablecoins reinforce U.S. dollar dominance rather than build a decentralized parallel system, and that
  - [原文链接](https://twitter.com/WuBlockchain/status/2025061895724847375)
- *... 及其他 3 条*

### @NikkeiAsia (10 条)

- `2026-02-21T10:40` Despite China’s strong objections to missile launchers in the Philippines in 2024, the US plans to deploy more advanced missile systems to deter aggression in the South China Sea.  https://s.nikkei.com/4amUkKZ
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025158581314580706)
- `2026-02-21T10:00` This was our most read story of the week.  Sri Lanka rolls out red carpet to investors for $15bn Port City  https://s.nikkei.com/4kOYSxh
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025148534568206799)
- `2026-02-21T09:04` 7-Eleven operator backs regenerative farming to secure coffee supply https://s.nikkei.com/3OSqMfI
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025134489043681712)
- `2026-02-21T08:06` Anutin's surprise win marks conservative resurgence in Thailand https://s.nikkei.com/4qOWKqy
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025119971584430492)
- `2026-02-21T07:08` Indonesian classic-car maker picks up speed https://s.nikkei.com/3OSkDAa
  - [原文链接](https://twitter.com/NikkeiAsia/status/2025105448404128177)
- *... 及其他 5 条*

### @CNBC (2 条)

- `2026-02-21T09:02` Chaos, confusion and $200 billion dreams: What I saw at India’s AI summit https://www.cnbc.com/2026/02/21/ai-summit-india-tech.html?taid=69997491773d17000105e695&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025133933986218400)
- `2026-02-21T07:42` Tech giants commit billions to Indian AI as New Delhi pushes for superpower status https://www.cnbc.com/2026/02/21/india-ai-summit-tech-giants-billion-dollar-investments.html?taid=699961da6a26b000013cb936&utm_campaign=trueanthem&utm_content=main&utm_medium=social&utm_source=twitter
  - [原文链接](https://twitter.com/CNBC/status/2025113837318332716)

### @spectatorindex (3 条)

- `2026-02-21T07:22` Trump's aides are urging him to 'focus more on voters economic worries' and highlighting the 'political risks of military escalation' against Iran ahead of midterm elections, according to Reuters report.
  - [原文链接](https://twitter.com/spectatorindex/status/2025108869429821831)
- `2026-02-21T01:56` BREAKING: An option that has been presented to Trump is a scenario that 'takes out the ayatollah and his son and the mullahs', according to Axios report.
  - [原文链接](https://twitter.com/spectatorindex/status/2025026758656082025)
- `2026-02-21T01:53` BREAKING: US official says Trump could decide on a strike on Iran 'at any moment', according to Axios report.
  - [原文链接](https://twitter.com/spectatorindex/status/2025025945804169609)

### @QuantInsti (2 条)

- `2026-02-21T07:16` 🚀 Want to automate the boring stuff? Learn how to build an Agentic Quant Team that automatically handles data scouting and risk guardrails. Check out the Agentic AI for Trading course here: https://quantra.quantinsti.com/course/agentic-ai-trading
  - [原文链接](https://twitter.com/QuantInsti/status/2025107301133418716)
- `2026-02-21T07:16` Everyone loves talking about alpha and strategy logic, but the most underrated part of algo trading is the "boring" part: production operations. ⚙️📉  Explore the GIF to see my short production checklist for deploying robust trading systems. 👉  What is the one production failure mode you have seen mo
  - [原文链接](https://twitter.com/QuantInsti/status/2025107262029648265)

### @IanBremmer (1 条)

- `2026-02-21T03:07` president trump’s criticisms of the fed and supreme court would land more convincingly if he hadn’t appointed any of them…
  - [原文链接](https://twitter.com/IanBremmer/status/2025044609848451570)

### @TechCrunch (3 条)

- `2026-02-21T01:10` Raising a round may not be a signal to spend aggressively, and many of the best founders stay disciplined.   http://localhost/yuris from http://localhost/generalcatalyst advises to wait until the pain is real, then hire with intention. Taking your time can prevent painful layoffs, protect culture, a
  - [原文链接](https://twitter.com/TechCrunch/status/2025015189951697233)
- `2026-02-21T01:03` India’s Sarvam launches Indus AI chat app as competition heats up https://techcrunch.com/2026/02/20/indias-sarvam-launches-indus-ai-chat-app-as-competition-heats-up/?utm_source=dlvr.it&utm_medium=twitter
  - [原文链接](https://twitter.com/TechCrunch/status/2025013400066257035)
- `2026-02-21T00:15` ⏳ One week to go on the best Disrupt deals!  🎟️ Save up to $680 on your tickets to TechCrunch Disrupt 2026 before prices jump February 27, 11:59 p.m. PT: http://spr.ly/6015hi86d  🤝 Meet the connection that changes everything for your startup, portfolio, or career  🚀 Get front row access to tomorrow’
  - [原文链接](https://twitter.com/TechCrunch/status/2025001275176202512)

### @TheInformation (1 条)

- `2026-02-21T01:01` Exclusive: OpenAI boosts revenue forecast and cash burn.  http://localhost/srimuppidi reports OpenAI is projecting 27% more in revenue through 2030 than previously forecast on higher sales of ChatGPT subscriptions.  But the company also warns it will burn more cash in the same time period, as it spe
  - [原文链接](https://twitter.com/TheInformation/status/2025012874901360810)

### @ReutersBiz (3 条)

- `2026-02-21T00:40` WATCH: US stocks ended higher, led by gains in Alphabet, Amazon and other Wall Street heavyweights after the Supreme Court struck down Trump's global tariffs https://reut.rs/4tOjOIS  Video
  - [原文链接](https://twitter.com/ReutersBiz/status/2025007561867678148)
- `2026-02-21T00:30` WATCH: Trump responded with fury to a Supreme Court ruling that he did not have the power to unilaterally set tariffs on imports, denigrating individual justices as he vowed to wield a more restrictive law to continue his global trade war https://reut.rs/4qLKx60  Video
  - [原文链接](https://twitter.com/ReutersBiz/status/2025005047269204125)
- `2026-02-21T00:20` WATCH: From Nvidia's earnings report to potential political waves in Europe, these are the business stories to watch in the coming week  Video
  - [原文链接](https://twitter.com/ReutersBiz/status/2025002528660750386)

### @Sino_Market (2 条)

- `2026-02-21T00:37` 🇺🇸 Trump moved swiftly on Friday to replace tariffs struck down by the Supreme Court with a temporary 10% global import duty for 150 days while opening investigations under other laws that could allow him to re-impose the tariffs.  Trump told a briefing he was ordering new tariffs under Section 122 
  - [原文链接](https://twitter.com/Sino_Market/status/2025007012392960082)
- `2026-02-21T00:17` 🇺🇸The Supreme Court delivered a major blow to Trump, ruling Friday that he exceeded his authority when imposing sweeping tariffs using a law reserved for a national emergency.  The justices, divided 6-3, held that Trump's aggressive approach to tariffs on products entering the United States from acr
  - [原文链接](https://twitter.com/Sino_Market/status/2025001883002425646)

### @DeItaone (1 条)

- `2026-02-21T00:05` Trump: ‘Those members of the Supreme Court who voted against our very acceptable and proper method of TARIFFS should be ashamed of themselves. Their decision was ridiculous but, now the adjustment process begins, and we will do everything possible to take in even more money than we were taking in be
  - [原文链接](https://twitter.com/DeItaone/status/2024998811060588781)

### @BNONews (1 条)

- `2026-02-21T00:01` Trump imposes addtional 10% tariff on all countries "effective almost immediately"
  - [原文链接](https://twitter.com/BNONews/status/2024997803676627106)

## 📱 微信公众号

暂无数据

## 🔥 NewsNow 热榜 (120 条)

### 微博

| 排名 | 标题 |
|------|------|
| #1 | [徐梦桃王心迪李天马出战混团](https://s.weibo.com/weibo?q=%23%E5%BE%90%E6%A2%A6%E6%A1%83%E7%8E%8B%E5%BF%83%E8%BF%AA%E6%9D%8E%E5%A4%A9%E9%A9%AC%E5%87%BA%E6%88%98%E6%B7%B7%E5%9B%A2%23) |
| #3 | [多地气温断崖式下跌](https://s.weibo.com/weibo?q=%23%E5%A4%9A%E5%9C%B0%E6%B0%94%E6%B8%A9%E6%96%AD%E5%B4%96%E5%BC%8F%E4%B8%8B%E8%B7%8C%23) |
| #4 | [女孩被当街暴打当地何以沉默两天](https://s.weibo.com/weibo?q=%23%E5%A5%B3%E5%AD%A9%E8%A2%AB%E5%BD%93%E8%A1%97%E6%9A%B4%E6%89%93%E5%BD%93%E5%9C%B0%E4%BD%95%E4%BB%A5%E6%B2%89%E9%BB%98%E4%B8%A4%E5%A4%A9%23) |
| #5 | [徐梦桃第一跳81.99分](https://s.weibo.com/weibo?q=%23%E5%BE%90%E6%A2%A6%E6%A1%83%E7%AC%AC%E4%B8%80%E8%B7%B381.99%E5%88%86%23) |
| #6 | [黄晓明曝艺人红毯上假摔](https://s.weibo.com/weibo?q=%E9%BB%84%E6%99%93%E6%98%8E%E6%9B%9D%E8%89%BA%E4%BA%BA%E7%BA%A2%E6%AF%AF%E4%B8%8A%E5%81%87%E6%91%94) |
| #7 | [刘涛演妈祖 三次圣杯](https://s.weibo.com/weibo?q=%E5%88%98%E6%B6%9B%E6%BC%94%E5%A6%88%E7%A5%96+%E4%B8%89%E6%AC%A1%E5%9C%A3%E6%9D%AF) |
| #8 | [烤肠商战](https://s.weibo.com/weibo?q=%E7%83%A4%E8%82%A0%E5%95%86%E6%88%98) |
| #9 | [我家那小子](https://s.weibo.com/weibo?q=%E6%88%91%E5%AE%B6%E9%82%A3%E5%B0%8F%E5%AD%90) |
| #10 | [回村后用的都是名牌货](https://s.weibo.com/weibo?q=%E5%9B%9E%E6%9D%91%E5%90%8E%E7%94%A8%E7%9A%84%E9%83%BD%E6%98%AF%E5%90%8D%E7%89%8C%E8%B4%A7) |
| #11 | [idle演唱会](https://s.weibo.com/weibo?q=idle%E6%BC%94%E5%94%B1%E4%BC%9A) |

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
| #9 | [泽连斯基：乌克兰已准备好作出“真正的妥协”](https://news.ifeng.com/c/8quBSNXwvb9) |
| #10 | [夫妻当街暴打15岁女孩，底气从何而来？](https://news.ifeng.com/c/8qvbbpgFD4Q) |

### 抖音

| 排名 | 标题 |
|------|------|
| #1 | [金银价再度大涨](https://www.douyin.com/hot/2407703) |
| #2 | [中国队空中技巧混合团体摘铜](https://www.douyin.com/hot/2407411) |
| #3 | [“破五”出游注意防风沙](https://www.douyin.com/hot/2407742) |
| #4 | [正月初五接财神](https://www.douyin.com/hot/2407307) |
| #5 | [新闻联播](https://www.douyin.com/hot/2407939) |
| #6 | [消息称美考虑打击哈梅内伊父子](https://www.douyin.com/hot/2407540) |
| #7 | [美将终止部分关税措施](https://www.douyin.com/hot/2407328) |
| #8 | [克宫：俄日关系“已降至零点”](https://www.douyin.com/hot/2407159) |
| #9 | [王心迪夺冠后谈及徐梦桃](https://www.douyin.com/hot/2407334) |
| #10 | [与中国短道速滑队同在](https://www.douyin.com/hot/2407267) |

### 百度热搜

| 排名 | 标题 |
|------|------|
| #1 | [“天下第一财神庙”被游客挤爆](https://www.baidu.com/s?wd=%E2%80%9C%E5%A4%A9%E4%B8%8B%E7%AC%AC%E4%B8%80%E8%B4%A2%E7%A5%9E%E5%BA%99%E2%80%9D%E8%A2%AB%E6%B8%B8%E5%AE%A2%E6%8C%A4%E7%88%86) |
| #2 | [徐梦桃王心迪李天马摘铜](https://www.baidu.com/s?wd=%E5%BE%90%E6%A2%A6%E6%A1%83%E7%8E%8B%E5%BF%83%E8%BF%AA%E6%9D%8E%E5%A4%A9%E9%A9%AC%E6%91%98%E9%93%9C) |
| #3 | [探访春联里的中国](https://www.baidu.com/s?wd=%E6%8E%A2%E8%AE%BF%E6%98%A5%E8%81%94%E9%87%8C%E7%9A%84%E4%B8%AD%E5%9B%BD) |
| #4 | [“你的老鸭汤只剩汤了”](https://www.baidu.com/s?wd=%E2%80%9C%E4%BD%A0%E7%9A%84%E8%80%81%E9%B8%AD%E6%B1%A4%E5%8F%AA%E5%89%A9%E6%B1%A4%E4%BA%86%E2%80%9D) |
| #5 | [河南一景区空中撒钱 面值最高100元](https://www.baidu.com/s?wd=%E6%B2%B3%E5%8D%97%E4%B8%80%E6%99%AF%E5%8C%BA%E7%A9%BA%E4%B8%AD%E6%92%92%E9%92%B1+%E9%9D%A2%E5%80%BC%E6%9C%80%E9%AB%98100%E5%85%83) |
| #6 | [王濛：不行让我签生死状复出](https://www.baidu.com/s?wd=%E7%8E%8B%E6%BF%9B%EF%BC%9A%E4%B8%8D%E8%A1%8C%E8%AE%A9%E6%88%91%E7%AD%BE%E7%94%9F%E6%AD%BB%E7%8A%B6%E5%A4%8D%E5%87%BA) |
| #7 | [300年打树花年味儿爆棚](https://www.baidu.com/s?wd=300%E5%B9%B4%E6%89%93%E6%A0%91%E8%8A%B1%E5%B9%B4%E5%91%B3%E5%84%BF%E7%88%86%E6%A3%9A) |
| #8 | [“前方无厕所、无烤肠、无茶叶蛋”](https://www.baidu.com/s?wd=%E2%80%9C%E5%89%8D%E6%96%B9%E6%97%A0%E5%8E%95%E6%89%80%E3%80%81%E6%97%A0%E7%83%A4%E8%82%A0%E3%80%81%E6%97%A0%E8%8C%B6%E5%8F%B6%E8%9B%8B%E2%80%9D) |
| #10 | [被指到的人今年财源滚滚](https://www.baidu.com/s?wd=%E8%A2%AB%E6%8C%87%E5%88%B0%E7%9A%84%E4%BA%BA%E4%BB%8A%E5%B9%B4%E8%B4%A2%E6%BA%90%E6%BB%9A%E6%BB%9A) |
| #11 | [大连一大学免统考补录硕士系谣言](https://www.baidu.com/s?wd=%E5%A4%A7%E8%BF%9E%E4%B8%80%E5%A4%A7%E5%AD%A6%E5%85%8D%E7%BB%9F%E8%80%83%E8%A1%A5%E5%BD%95%E7%A1%95%E5%A3%AB%E7%B3%BB%E8%B0%A3%E8%A8%80) |

### 今日头条

| 排名 | 标题 |
|------|------|
| #1 | [舅舅送外甥女30斤银砖当压岁钱](https://www.toutiao.com/trending/7609183470594588718/) |
| #2 | [印度AI峰会为何引发全球群嘲](https://www.toutiao.com/trending/7609263367261261318/) |
| #3 | [全球多地举办活动 共庆新春佳节](https://www.toutiao.com/trending/7609221704333659658/) |
| #5 | [《新闻联播》正在直播](https://www.toutiao.com/trending/7608412791876993074/) |
| #6 | [《飞驰人生3》韩寒终于不再浪费天赋](https://www.toutiao.com/trending/7609262135771663915/) |
| #7 | [存款利率跌入“0”字头](https://www.toutiao.com/trending/7608141024543785014/) |
| #8 | [高速上鸭子掉落暴走 车主来认领](https://www.toutiao.com/trending/7609150350486126633/) |
| #9 | [王濛怒斥短道队：不行我签生死状复出](https://www.toutiao.com/trending/7608275916123095086/) |
| #10 | [卫星图像显示60余架美军机驻扎约旦基地](https://www.toutiao.com/trending/7609228742115724827/) |
| #11 | [免统考补录硕士？大连医科大学辟谣](https://www.toutiao.com/trending/7609122130168627242/) |

### 知乎

| 排名 | 标题 |
|------|------|
| #1 | [怎样看待王濛直言短道速滑问题太大，称自己敢签生死状，复出能保 1 金？短道速滑队目前面临哪些问题？](https://www.zhihu.com/question/2008501798680359345) |
| #2 | [特斯拉无人驾驶车正式下线，无方向盘、无踏板、无后视镜，能赢得大众信任并走向普及吗？你看好其前景吗？](https://www.zhihu.com/question/2008253352463528326) |
| #3 | [小伙撕去年对联天塌了，「门上全是胶，钢丝球都刷不下来」，你遇到过这情况吗？有什么有效去除方法么？](https://www.zhihu.com/question/2008211250732038004) |
| #4 | [为什么开放的 Windows 战胜了封闭的 macOS，但是开放的 Android 却战胜不了封闭的 iOS？](https://www.zhihu.com/question/2007124650916856053) |
| #5 | [「小矮马」马年火爆全网，最低六千元就能入手，但有买家称「每天要铲屎十斤」，矮脚马真的适合当宠物吗？](https://www.zhihu.com/question/2005330908966851008) |
| #6 | [手机为啥越卖越贵了？](https://www.zhihu.com/question/12538422686) |
| #7 | [如何评价湖北省文旅厅认定那艺娜（翟革英）为劣迹艺人，叫停其演出？](https://www.zhihu.com/question/2008437078631940159) |
| #8 | [你如何看待湛江东海岛拾石村妈祖女孩被替换？](https://www.zhihu.com/question/2008207494175011823) |
| #9 | [ClaudeCode 之父称不再需要「planmode」，将对 AI 编程带来哪些变革？](https://www.zhihu.com/question/2008176730532234790) |
| #10 | [经理拍拍我的肩，「裁你是因为你太优秀」，然后悄悄递来竞争对手的名片，你会怎么看待这件事？](https://www.zhihu.com/question/1986031665873707499) |

### 贴吧

| 排名 | 标题 |
|------|------|
| #1 | [错认国人,菲律宾女孩遭猎艳](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%94%99%E8%AE%A4%E5%9B%BD%E4%BA%BA%2C%E8%8F%B2%E5%BE%8B%E5%AE%BE%E5%A5%B3%E5%AD%A9%E9%81%AD%E7%8C%8E%E8%89%B3&topic_id=28350821) |
| #2 | [亲戚拜年不说话,沪漂了不起？](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E6%88%9A%E6%8B%9C%E5%B9%B4%E4%B8%8D%E8%AF%B4%E8%AF%9D%2C%E6%B2%AA%E6%BC%82%E4%BA%86%E4%B8%8D%E8%B5%B7%EF%BC%9F&topic_id=28350825) |
| #3 | [鸣潮没二创,二游痴急了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%B8%A3%E6%BD%AE%E6%B2%A1%E4%BA%8C%E5%88%9B%2C%E4%BA%8C%E6%B8%B8%E7%97%B4%E6%80%A5%E4%BA%86&topic_id=28350831) |
| #4 | [绿帽文争霸,新五绿诞生](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%BB%BF%E5%B8%BD%E6%96%87%E4%BA%89%E9%9C%B8%2C%E6%96%B0%E4%BA%94%E7%BB%BF%E8%AF%9E%E7%94%9F&topic_id=28350833) |
| #5 | [日企采用中国芯,岛民破防](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%97%A5%E4%BC%81%E9%87%87%E7%94%A8%E4%B8%AD%E5%9B%BD%E8%8A%AF%2C%E5%B2%9B%E6%B0%91%E7%A0%B4%E9%98%B2&topic_id=28350832) |
| #6 | [12人遇难!熊孩子放炮闯祸](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=12%E4%BA%BA%E9%81%87%E9%9A%BE%21%E7%86%8A%E5%AD%A9%E5%AD%90%E6%94%BE%E7%82%AE%E9%97%AF%E7%A5%B8&topic_id=28350829) |
| #7 | [国gal暴死,40万众筹打水漂](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%9B%BDgal%E6%9A%B4%E6%AD%BB%2C40%E4%B8%87%E4%BC%97%E7%AD%B9%E6%89%93%E6%B0%B4%E6%BC%82&topic_id=28350824) |
| #8 | [王濛痛骂短道队:林孝埈练废了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%8E%8B%E6%BF%9B%E7%97%9B%E9%AA%82%E7%9F%AD%E9%81%93%E9%98%9F%3A%E6%9E%97%E5%AD%9D%E5%9F%88%E7%BB%83%E5%BA%9F%E4%BA%86&topic_id=28350817) |
| #9 | [港人偷拍同胞,阴阳国人没素质](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B8%AF%E4%BA%BA%E5%81%B7%E6%8B%8D%E5%90%8C%E8%83%9E%2C%E9%98%B4%E9%98%B3%E5%9B%BD%E4%BA%BA%E6%B2%A1%E7%B4%A0%E8%B4%A8&topic_id=28350812) |
| #10 | [金牌夫妻!王心迪徐梦桃顶峰相见](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%BB%21%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83%E9%A1%B6%E5%B3%B0%E7%9B%B8%E8%A7%81&topic_id=28350813) |

### bilibili 热搜

| 排名 | 标题 |
|------|------|
| #1 | [正月初五迎财神](https://search.bilibili.com/all?keyword=%E6%AD%A3%E6%9C%88%E5%88%9D%E4%BA%94%E8%BF%8E%E8%B4%A2%E7%A5%9E) |
| #2 | [王力宏回忆中的方大同](https://search.bilibili.com/all?keyword=%E7%8E%8B%E5%8A%9B%E5%AE%8F%E5%9B%9E%E5%BF%86%E4%B8%AD%E7%9A%84%E6%96%B9%E5%A4%A7%E5%90%8C) |
| #3 | [终末地逐风联赛](https://search.bilibili.com/all?keyword=%E7%BB%88%E6%9C%AB%E5%9C%B0%E9%80%90%E9%A3%8E%E8%81%94%E8%B5%9B) |
| #4 | [英国首相斯塔默面临哪些困境](https://search.bilibili.com/all?keyword=%E8%8B%B1%E5%9B%BD%E9%A6%96%E7%9B%B8%E6%96%AF%E5%A1%94%E9%BB%98%E9%9D%A2%E4%B8%B4%E5%93%AA%E4%BA%9B%E5%9B%B0%E5%A2%83) |
| #5 | [经典IP寻秦记上线B站](https://search.bilibili.com/all?keyword=%E5%AF%BB%E7%A7%A6%E8%AE%B0) |
| #6 | [挑战在国外抓中国人共进年夜饭](https://search.bilibili.com/all?keyword=%E6%8C%91%E6%88%98%E5%9C%A8%E5%9B%BD%E5%A4%96%E6%8A%93%E4%B8%AD%E5%9B%BD%E4%BA%BA%E5%85%B1%E8%BF%9B%E5%B9%B4%E5%A4%9C%E9%A5%AD) |
| #7 | [苹果味饮品为何突然爆发](https://search.bilibili.com/all?keyword=%E8%8B%B9%E6%9E%9C%E5%91%B3%E9%A5%AE%E5%93%81%E4%B8%BA%E4%BD%95%E7%AA%81%E7%84%B6%E7%88%86%E5%8F%91) |
| #8 | [年轻人走亲戚的方式](https://search.bilibili.com/all?keyword=%E5%B9%B4%E8%BD%BB%E4%BA%BA%E8%B5%B0%E4%BA%B2%E6%88%9A%E7%9A%84%E6%96%B9%E5%BC%8F) |
| #9 | [实测Gemini 3.1 Pro](https://search.bilibili.com/all?keyword=%E5%AE%9E%E6%B5%8BGemini+3.1+Pro) |
| #10 | [春晚歌曲锐评](https://search.bilibili.com/all?keyword=%E6%98%A5%E6%99%9A%E6%AD%8C%E6%9B%B2%E9%94%90%E8%AF%84) |

### 财联社热门

| 排名 | 标题 |
|------|------|
| #1 | [中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111) |
| #2 | [美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233) |
| #3 | [特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246) |
| #4 | [原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772) |
| #5 | [美股收盘：多重利空压顶华尔街情绪恶化 三大指数集体下跌](https://www.cls.cn/detail/2291935) |
| #6 | [“存储荒”愈演愈烈！三星HBM4据称涨价30% 韩国“芯片双雄”积极扩产](https://www.cls.cn/detail/2291781) |
| #7 | [什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326) |
| #8 | [“马年科技春晚”让买机器人的股民都松了一口气？节前资金已挤入ETF](https://www.cls.cn/detail/2291748) |
| #9 | [春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289) |
| #10 | [香港长江和记最新发声](https://www.cls.cn/detail/2292101) |

### 澎湃新闻

| 排名 | 标题 |
|------|------|
| #1 | [载8名中国游客车辆因冰面破裂沉湖，其中1人逃生7人遇难](https://www.thepaper.cn/newsDetail_forward_32636500) |
| #2 | [第四金！王心迪斩获自由式滑雪男子空中技巧金牌](https://www.thepaper.cn/newsDetail_forward_32636832) |
| #3 | [人勤春早暖意先行！春节后首批“点对点”务工劳动者乘专机专列抵沪](https://www.thepaper.cn/newsDetail_forward_32636648) |
| #4 | [载8名中国游客汽车在贝加尔湖落水，目前仅一名中国游客获救](https://www.thepaper.cn/newsDetail_forward_32636440) |
| #5 | [春启新程｜在上海的第15个春节，她说老人们这个时候更需要自己](https://www.thepaper.cn/newsDetail_forward_32635177) |
| #6 | [王心迪、徐梦桃成为中国体育史上第六对奥运金牌夫妇](https://www.thepaper.cn/newsDetail_forward_32637045) |
| #7 | [释新闻｜美最高法院6比3裁定特朗普全球关税违法，意味着什么？](https://www.thepaper.cn/newsDetail_forward_32638670) |
| #8 | [视频丨硬核揭秘！福建舰“一马当先”底气何在？](https://www.thepaper.cn/newsDetail_forward_32638555) |
| #9 | [2026春节档总场次刷新中国影史纪录](https://www.thepaper.cn/newsDetail_forward_32638734) |
| #10 | [张艺谋人民日报撰文：于无声处听惊雷](https://www.thepaper.cn/newsDetail_forward_32638642) |

### 华尔街见闻

| 排名 | 标题 |
|------|------|
| #1 | [特朗普全球关税被推翻！美国最高法院裁定违法，超1750亿美元税收面临退款](https://wallstreetcn.com/articles/3765909) |
| #2 | [美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8%](https://wallstreetcn.com/articles/3765902) |
| #3 | [最高法裁决后特朗普动用替补工具，加征10%全球关税，放话关税会比之前“高得多”](https://wallstreetcn.com/articles/3765912) |
| #4 | [1750亿美元“关税退款”！对美股是“财政刺激”，对美债是“增加债务”，对金银是“不确定性重来”](https://wallstreetcn.com/articles/3765925) |
| #5 | [美国四季度GDP仅增1.4%！政府停摆拖累1个百分点，特朗普提前“开火”鲍威尔](https://wallstreetcn.com/articles/3765906) |
| #6 | [得知高院否决关税那一刻，特朗普“气炸了”，“破口大骂”](https://wallstreetcn.com/articles/3765923) |
| #7 | [“谷歌天团”反击AI泡沫质疑：这是工业革命，但速度快10倍、规模大10倍](https://wallstreetcn.com/articles/3765904) |
| #8 | [美联储最青睐的通胀指标超预期！美国12月核心PCE物价指数同比3%](https://wallstreetcn.com/articles/3765907) |
| #9 | [别为美最高法推翻特朗普关税高兴太早？华尔街预计市场反应或昙花一现](https://wallstreetcn.com/articles/3765913) |
| #10 | [华尔街见闻早餐FM-Radio \| 2026年2月21日](https://wallstreetcn.com/articles/3765920) |

## 🔗 原始链接索引

### 🐦 Twitter 原文 (80/97 条)

- [2026-02-21T12:00 @NexusLabs [热门] | Introducing USDX — the native dollar of the Nexus economy. A shared settlement layer for a...](https://twitter.com/NexusLabs/status/2024138532512567297)
- [2026-02-21T12:00 @narendramodi [热门] | India is honoured to welcome President Lula and his delegation, which includes distinguish...](https://twitter.com/narendramodi/status/2025149417636896912)
- [2026-02-21T12:00 @JacobKinge [热门] | Howard Lutnick is arguably one of the slickest and most corrupt operators in modern financ...](https://twitter.com/JacobKinge/status/2024906835610710212)
- [2026-02-21T12:00 @MedicoLiberdade [热门] | E aí@BlogdoNoblat, vai comentar o cartão de crédito corporativo de painho que gastou + de ...](https://twitter.com/MedicoLiberdade/status/2024964381675569406)
- [2026-02-21T12:00 @Milajoy [热门] | REP. AOC’S ILLEGAL HIRE SCANDAL EXPLODES AOC knowingly put an illegal alien—zero work pape...](https://twitter.com/Milajoy/status/2024773028660559988)
- [2026-02-21T12:00 @Playnance_ [热门] | CryptoWisser spotlights the model behind G Coin 💎 As CryptoWisser writes, G Coin represent...](https://twitter.com/Playnance_/status/2024515923630039477)
- [2026-02-21T12:00 @kangminjlee [热门] | Turns out mass immigration actually doesn't help the economy in the long run Instead Canad...](https://twitter.com/kangminjlee/status/2024889042400055362)
- [2026-02-21T12:00 @the_17thletter4 [热门] | BREAKING 🅱️: 20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoax, hid...](https://twitter.com/the_17thletter4/status/2024859960853622861)
- [2026-02-21T12:00 @jisoogaIIery [热门] | FACE ECONOMY](https://twitter.com/jisoogaIIery/status/2024851114689188167)
- [2026-02-21T12:00 @WHLeavitt [热门] | 🚨 ALERT: Bombshell—20 CIA/FBI agents confirm Obama & ex-CIA director fabricated Russia Hoa...](https://twitter.com/WHLeavitt/status/2024983554992840962)
- [2026-02-21T12:00 @RodiumInsights [热门] | یاد ہے !”عاصم منیر نے کہا تھا تم اللہ کی جنگ لڑ رہے ہو وہ اسکے ساتھ نہیں ہے ۔“ آج یہ حالت ...](https://twitter.com/RodiumInsights/status/2024935415955030328)
- [2026-02-21T12:00 @RepOfSomaliland [热门] | Hey@Grok, remove the unstable, persistently high-inflation currency.](https://twitter.com/RepOfSomaliland/status/2024570762263482644)
- [2026-02-21T12:00 @cryptorover [热门] | 💥BREAKING: BlackRock buys $64,500,000 worth of Bitcoin.](https://twitter.com/cryptorover/status/2025078124833116434)
- [2026-02-21T12:00 @barkmeta [热门] | Might want to stock up on groceries and fill your gas tank before the market opens Monday....](https://twitter.com/barkmeta/status/2024980940032737675)
- [2026-02-21T12:00 @BitcoinMagazine [热门] | JUST IN: Bitcoin's hashrate has increased over 28% from its recent bottom! 🚀](https://twitter.com/BitcoinMagazine/status/2024859538562662650)
- [2026-02-21T12:00 @blueorms [热门] | *guess the word game* ling: this is something i did for orm yesterday orm: peeling the pra...](https://twitter.com/blueorms/status/2025161384317817235)
- [2026-02-21T12:00 @Dank_jetha [热门] | Youth congress leaders at the AI summit](https://twitter.com/Dank_jetha/status/2025142632289370245)
- [2026-02-21T12:00 @JerryDunleavy [热门] | NEW: The CIA is retracting *19* politicized intelligence products spanning the last decade...](https://twitter.com/JerryDunleavy/status/2024952714652971186)
- [2026-02-21T12:00 @PeterDClack [热门] | The 'inner circle' that is driving the $9.2 trillion a year net zero economy, also control...](https://twitter.com/PeterDClack/status/2025125352545362422)
- [2026-02-21T12:00 @OndoFinance [热门] | Tokenization goes mainstream by tapping into TradFi. Ondo's tokenized stock trades execute...](https://twitter.com/OndoFinance/status/2024863432927846547)
- [2026-02-21T12:00 @un1versalist [热门] | People basically found out aliens were real yesterday. Stock market went up No one freaked...](https://twitter.com/un1versalist/status/2024999111833841889)
- [2026-02-21T12:00 @aakashgupta [热门] | Nvidia paid $20 billion for Groq’s IP. Taalas raised $169 million with 24 employees. And t...](https://twitter.com/aakashgupta/status/2025079498396631140)
- [2026-02-21T12:00 @Bitcoin_Teddy [热门] | CEO of $4.5 trillion dollar NVIDIA, Jensen Huang, says that “bitcoin is taking excess ener...](https://twitter.com/Bitcoin_Teddy/status/2025105456985776538)
- [2026-02-21T12:00 @cryptorover [热门] | This is a good zone to DCA some Bitcoin!](https://twitter.com/cryptorover/status/2025153020305313864)
- [2026-02-21T12:00 @oazteca_ [热门] | Aí você vai ver qual é o tal do argumento homofóbico e transfóbico que matou bilhões: Casa...](https://twitter.com/oazteca_/status/2024939164869792130)
- [2026-02-21T12:00 @MissCryptoGER [热门] | 55 Milliarden Dollar Krimi: Rutscht Saylors Imperium JETZT ins Minus? 😳 Der Markt testet d...](https://twitter.com/MissCryptoGER/status/2017700415421530382)
- [2026-02-21T12:00 @garrytan [热门] | Red Robin’s stock collapsed from $92 to $3.61 after management saved on labor costs and lo...](https://twitter.com/garrytan/status/2024869371944882181)
- [2026-02-21T12:00 @AdrianP_doc [热门] | Where the fuck are rich people gonna go? Dubai? To a shopping mall in the middle of the de...](https://twitter.com/AdrianP_doc/status/2024862455164244404)
- [2026-02-21T12:00 @EricLDaugh [热门] | 🚨 JUST IN: Sen. John Kennedy is warning the Democrats the economy would ROAR if Trump has ...](https://twitter.com/EricLDaugh/status/2025176101299929130)
- [2026-02-21T12:00 @SatlokChannel [热门] | SA News#Thread| 1/10 Artificial Intelligence is not a single technology but a layered syst...](https://twitter.com/SatlokChannel/status/2025140695665893379)
- [2026-02-21T12:00 @TheEconomist [关注] | Russia shows no sign of an impending breakdown, political or economic. But from travel and...](https://twitter.com/TheEconomist/status/2025178718574879184)
- [2026-02-21T12:00 @zerohedge [关注] | Macron's India Trip Exposes EU Tech Overreach And Policy Failures https://www.zerohedge.co...](https://twitter.com/zerohedge/status/2025178717127917834)
- [2026-02-21T11:49 @business [关注] | While no country can fully decouple from US or Chinese AI models anytime soon, alternative...](https://twitter.com/business/status/2025175939500347602)
- [2026-02-21T11:40 @TheEconomist [关注] | “Three months ago we were just TikTokers.” On “The Weekend Intelligence” podcast we meet t...](https://twitter.com/TheEconomist/status/2025173665805893672)
- [2026-02-21T11:28 @WuBlockchain [关注] | According to http://localhost/SpecterAnalyst, IoTeX' private key may have been compromised...](https://twitter.com/WuBlockchain/status/2025170847950938233)
- [2026-02-21T11:23 @business [关注] | What if there was a handbook called “How to Make Money by Not Buying the Worst Companies i...](https://twitter.com/business/status/2025169399104094400)
- [2026-02-21T11:20 @TheEconomist [关注] | A measles outbreak in London with 61 cases so far this year is causing alarm. The number o...](https://twitter.com/TheEconomist/status/2025168632716619926)
- [2026-02-21T11:14 @WuBlockchain [关注] | WuBlockchain Weekly: MicroStrategy Says It Can Withstand Bitcoin Drop to $8,000, Altcoin S...](https://twitter.com/WuBlockchain/status/2025167297674109146)
- [2026-02-21T11:00 @TheEconomist [关注] | If the kilt spread over gilts gets too wide, perhaps even the most ardent nationalist will...](https://twitter.com/TheEconomist/status/2025163636172267714)
- [2026-02-21T10:51 @business [关注] | Governments around the world reacted with caution after the US Supreme Court invalidated P...](https://twitter.com/business/status/2025161342450032663)
- [2026-02-21T10:50 @TheEconomist [关注] | Paying attention to a meeting, especially a pointless one, may be a waste of time. But it ...](https://twitter.com/TheEconomist/status/2025161082474553761)
- [2026-02-21T10:40 @NikkeiAsia [关注] | Despite China’s strong objections to missile launchers in the Philippines in 2024, the US ...](https://twitter.com/NikkeiAsia/status/2025158581314580706)
- [2026-02-21T10:40 @TheEconomist [关注] | The border guards who first faced Russia’s tanks in February 2022 were a close-knit family...](https://twitter.com/TheEconomist/status/2025158566231834648)
- [2026-02-21T10:34 @business [关注] | The US economy has borne most of the burden of tariffs imposed by Donald Trump, European C...](https://twitter.com/business/status/2025157263556587986)
- [2026-02-21T10:32 @business [关注] | French President Emmanuel Macron urged calm before a march in Lyon organized by far-right ...](https://twitter.com/business/status/2025156724269682873)
- [2026-02-21T10:30 @TheEconomist [关注] | Geopolitical threats from Russia, China and lately America have convinced many in Europe t...](https://twitter.com/TheEconomist/status/2025156053294334368)
- [2026-02-21T10:27 @WuBlockchain [关注] | Uniswap Labs announced the release of 7 new "Skills" to enable AI Agents to execute operat...](https://twitter.com/WuBlockchain/status/2025155521754374453)
- [2026-02-21T10:26 @business [关注] | What happened to the global economy this week — in charts https://www.bloomberg.com/news/a...](https://twitter.com/business/status/2025155097152332198)
- [2026-02-21T10:25 @business [关注] | Brazil and India sealed a framework pact on critical minerals with the two countries agree...](https://twitter.com/business/status/2025154800405328313)
- [2026-02-21T10:20 @TheEconomist [关注] | This loving remake of “Kind Hearts and Coronets” (1949) mimics some of its predecessor’s m...](https://twitter.com/TheEconomist/status/2025153532005941360)
- [2026-02-21T10:10 @TheEconomist [关注] | The 6-3 decision offers a lesson on the broader direction of the Supreme Court under Donal...](https://twitter.com/TheEconomist/status/2025151016472060191)
- [2026-02-21T10:00 @TheEconomist [关注] | Here’s why a ban on insider betting might do more harm than good https://www.economist.com...](https://twitter.com/TheEconomist/status/2025148581347225904)
- [2026-02-21T10:00 @NikkeiAsia [关注] | This was our most read story of the week. Sri Lanka rolls out red carpet to investors for ...](https://twitter.com/NikkeiAsia/status/2025148534568206799)
- [2026-02-21T09:46 @business [关注] | India’s opposition called for Prime Minister Narendra Modi’s administration to put the nat...](https://twitter.com/business/status/2025145137190309971)
- [2026-02-21T09:44 @business [关注] | Hungarian Prime Minister Viktor Orban’s re-election campaign, which has made attacks on Ky...](https://twitter.com/business/status/2025144588483145772)
- [2026-02-21T09:04 @NikkeiAsia [关注] | 7-Eleven operator backs regenerative farming to secure coffee supply https://s.nikkei.com/...](https://twitter.com/NikkeiAsia/status/2025134489043681712)
- [2026-02-21T09:04 @business [关注] | How the heterodoxy became the heterodoxy. https://www.bloomberg.com/news/articles/2026-02-...](https://twitter.com/business/status/2025134475298902253)
- [2026-02-21T09:02 @CNBC [关注] | Chaos, confusion and $200 billion dreams: What I saw at India’s AI summit https://www.cnbc...](https://twitter.com/CNBC/status/2025133933986218400)
- [2026-02-21T08:06 @NikkeiAsia [关注] | Anutin's surprise win marks conservative resurgence in Thailand https://s.nikkei.com/4qOWK...](https://twitter.com/NikkeiAsia/status/2025119971584430492)
- [2026-02-21T07:42 @CNBC [关注] | Tech giants commit billions to Indian AI as New Delhi pushes for superpower status https:/...](https://twitter.com/CNBC/status/2025113837318332716)
- [2026-02-21T07:22 @spectatorindex [关注] | Trump's aides are urging him to 'focus more on voters economic worries' and highlighting t...](https://twitter.com/spectatorindex/status/2025108869429821831)
- [2026-02-21T07:16 @QuantInsti [关注] | 🚀 Want to automate the boring stuff? Learn how to build an Agentic Quant Team that automat...](https://twitter.com/QuantInsti/status/2025107301133418716)
- [2026-02-21T07:16 @QuantInsti [关注] | Everyone loves talking about alpha and strategy logic, but the most underrated part of alg...](https://twitter.com/QuantInsti/status/2025107262029648265)
- [2026-02-21T07:08 @NikkeiAsia [关注] | Indonesian classic-car maker picks up speed https://s.nikkei.com/3OSkDAa](https://twitter.com/NikkeiAsia/status/2025105448404128177)
- [2026-02-21T06:45 @NikkeiAsia [关注] | Japan signals US tariff ruling won't affect agreed projects as Asia reacts https://s.nikke...](https://twitter.com/NikkeiAsia/status/2025099538223026474)
- [2026-02-21T05:52 @NikkeiAsia [关注] | Thailand prepares for a new government: Key post-election points PM Anutin is looking to f...](https://twitter.com/NikkeiAsia/status/2025086319928435138)
- [2026-02-21T05:30 @NikkeiAsia [关注] | Trump to travel to China next month, with Taiwan and tariffs in focus https://s.nikkei.com...](https://twitter.com/NikkeiAsia/status/2025080606598574344)
- [2026-02-21T05:24 @NikkeiAsia [关注] | Hong Kong plots student housing buildup as land revenue shrinks College accommodations una...](https://twitter.com/NikkeiAsia/status/2025079048930480186)
- [2026-02-21T05:20 @WuBlockchain [关注] | On Feb. 20 (ET), total net inflows into Bitcoin spot ETFs reached $88.04 million. The Bitc...](https://twitter.com/WuBlockchain/status/2025078053752463383)
- [2026-02-21T04:58 @NikkeiAsia [关注] | Japanese official says US tariff ruling 'won't affect' agreed projects https://s.nikkei.co...](https://twitter.com/NikkeiAsia/status/2025072629363732885)
- [2026-02-21T04:25 @zerohedge [关注] | Is It Time To Reopen The Franklin Child Prostitution Case After Epstein Revelations? https...](https://twitter.com/zerohedge/status/2025064216395153408)
- [2026-02-21T04:15 @WuBlockchain [关注] | According to Fortune, Wintermute founder Evgeny Gaevoy said on the Crypto Playbook podcast...](https://twitter.com/WuBlockchain/status/2025061895724847375)
- [2026-02-21T04:07 @zerohedge [关注] | Kevin Hassett should be sending thank you notes to the NY Fed: recall they calculated US c...](https://twitter.com/zerohedge/status/2025059717114912891)
- [2026-02-21T04:00 @zerohedge [关注] | AI Content 'Incidents' Skyrocket: A Growing Threat In The Digital Age https://www.zerohedg...](https://twitter.com/zerohedge/status/2025057924112867816)
- [2026-02-21T03:56 @zerohedge [关注] | a word from our sponsor: Remember when the halving was supposed to kill public miners? Mea...](https://twitter.com/zerohedge/status/2025057021263847552)
- [2026-02-21T03:53 @zerohedge [关注] | Since the October all time high, bitcoin spot ETF balances have posted their largest drawd...](https://twitter.com/zerohedge/status/2025056148722725065)
- [2026-02-21T03:35 @zerohedge [关注] | Riyadh Seeks To Replace Israel With Syria For EU Fiber-Optic Cable Route https://www.zeroh...](https://twitter.com/zerohedge/status/2025051633525125621)
- [2026-02-21T03:18 @zerohedge [关注] | Despite hiring a private tutor, Alice de Rothschild, the daughter of billionaire Ariane de...](https://twitter.com/zerohedge/status/2025047411878482402)
- [2026-02-21T03:10 @zerohedge [关注] | Iranian Starlink Black Market Prices Soar As War Risks Rise https://www.zerohedge.com/tech...](https://twitter.com/zerohedge/status/2025045342303949040)
- [2026-02-21T03:07 @IanBremmer [关注] | president trump’s criticisms of the fed and supreme court would land more convincingly if ...](https://twitter.com/IanBremmer/status/2025044609848451570)

### 📱 微信公众号原文 (0/0 条)

- 暂无可用链接

### 🔥 NewsNow 原文 (120/120 条)

- [微博 #1 | 徐梦桃王心迪李天马出战混团](https://s.weibo.com/weibo?q=%23%E5%BE%90%E6%A2%A6%E6%A1%83%E7%8E%8B%E5%BF%83%E8%BF%AA%E6%9D%8E%E5%A4%A9%E9%A9%AC%E5%87%BA%E6%88%98%E6%B7%B7%E5%9B%A2%23)
- [凤凰网 #1 | 7名中国游客在贝加尔湖溺亡，俄方：路线未经批准](https://news.ifeng.com/c/8qvY0GNd8tK)
- [抖音 #1 | 金银价再度大涨](https://www.douyin.com/hot/2407703)
- [百度热搜 #1 | “天下第一财神庙”被游客挤爆](https://www.baidu.com/s?wd=%E2%80%9C%E5%A4%A9%E4%B8%8B%E7%AC%AC%E4%B8%80%E8%B4%A2%E7%A5%9E%E5%BA%99%E2%80%9D%E8%A2%AB%E6%B8%B8%E5%AE%A2%E6%8C%A4%E7%88%86)
- [今日头条 #1 | 舅舅送外甥女30斤银砖当压岁钱](https://www.toutiao.com/trending/7609183470594588718/)
- [知乎 #1 | 怎样看待王濛直言短道速滑问题太大，称自己敢签生死状，复出能保 1 金？短道速滑队目前面临哪些问题？](https://www.zhihu.com/question/2008501798680359345)
- [贴吧 #1 | 错认国人,菲律宾女孩遭猎艳](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%94%99%E8%AE%A4%E5%9B%BD%E4%BA%BA%2C%E8%8F%B2%E5%BE%8B%E5%AE%BE%E5%A5%B3%E5%AD%A9%E9%81%AD%E7%8C%8E%E8%89%B3&topic_id=28350821)
- [bilibili 热搜 #1 | 正月初五迎财神](https://search.bilibili.com/all?keyword=%E6%AD%A3%E6%9C%88%E5%88%9D%E4%BA%94%E8%BF%8E%E8%B4%A2%E7%A5%9E)
- [财联社热门 #1 | 中国顶流私募Q4调仓大转向：集体加仓拼多多、AI重心悄然转变](https://www.cls.cn/detail/2292111)
- [澎湃新闻 #1 | 载8名中国游客车辆因冰面破裂沉湖，其中1人逃生7人遇难](https://www.thepaper.cn/newsDetail_forward_32636500)
- [华尔街见闻 #1 | 特朗普全球关税被推翻！美国最高法院裁定违法，超1750亿美元税收面临退款](https://wallstreetcn.com/articles/3765909)
- [百度热搜 #2 | 徐梦桃王心迪李天马摘铜](https://www.baidu.com/s?wd=%E5%BE%90%E6%A2%A6%E6%A1%83%E7%8E%8B%E5%BF%83%E8%BF%AA%E6%9D%8E%E5%A4%A9%E9%A9%AC%E6%91%98%E9%93%9C)
- [今日头条 #2 | 印度AI峰会为何引发全球群嘲](https://www.toutiao.com/trending/7609263367261261318/)
- [凤凰网 #2 | 印度将购买委内瑞拉石油？美大使：正积极谈判](https://news.ifeng.com/c/8qveM9IjpX0)
- [抖音 #2 | 中国队空中技巧混合团体摘铜](https://www.douyin.com/hot/2407411)
- [bilibili 热搜 #2 | 王力宏回忆中的方大同](https://search.bilibili.com/all?keyword=%E7%8E%8B%E5%8A%9B%E5%AE%8F%E5%9B%9E%E5%BF%86%E4%B8%AD%E7%9A%84%E6%96%B9%E5%A4%A7%E5%90%8C)
- [贴吧 #2 | 亲戚拜年不说话,沪漂了不起？](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E4%BA%B2%E6%88%9A%E6%8B%9C%E5%B9%B4%E4%B8%8D%E8%AF%B4%E8%AF%9D%2C%E6%B2%AA%E6%BC%82%E4%BA%86%E4%B8%8D%E8%B5%B7%EF%BC%9F&topic_id=28350825)
- [财联社热门 #2 | 美股收盘：特朗普关税“翻车”成利好 三大指数集体收涨](https://www.cls.cn/detail/2292233)
- [知乎 #2 | 特斯拉无人驾驶车正式下线，无方向盘、无踏板、无后视镜，能赢得大众信任并走向普及吗？你看好其前景吗？](https://www.zhihu.com/question/2008253352463528326)
- [澎湃新闻 #2 | 第四金！王心迪斩获自由式滑雪男子空中技巧金牌](https://www.thepaper.cn/newsDetail_forward_32636832)
- [华尔街见闻 #2 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8%](https://wallstreetcn.com/articles/3765902)
- [bilibili 热搜 #3 | 终末地逐风联赛](https://search.bilibili.com/all?keyword=%E7%BB%88%E6%9C%AB%E5%9C%B0%E9%80%90%E9%A3%8E%E8%81%94%E8%B5%9B)
- [贴吧 #3 | 鸣潮没二创,二游痴急了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%B8%A3%E6%BD%AE%E6%B2%A1%E4%BA%8C%E5%88%9B%2C%E4%BA%8C%E6%B8%B8%E7%97%B4%E6%80%A5%E4%BA%86&topic_id=28350831)
- [凤凰网 #3 | 泰国智库批特朗普关税政策：别人在搭桥，美国在筑墙](https://news.ifeng.com/c/8qvXaKA67vQ)
- [微博 #3 | 多地气温断崖式下跌](https://s.weibo.com/weibo?q=%23%E5%A4%9A%E5%9C%B0%E6%B0%94%E6%B8%A9%E6%96%AD%E5%B4%96%E5%BC%8F%E4%B8%8B%E8%B7%8C%23)
- [百度热搜 #3 | 探访春联里的中国](https://www.baidu.com/s?wd=%E6%8E%A2%E8%AE%BF%E6%98%A5%E8%81%94%E9%87%8C%E7%9A%84%E4%B8%AD%E5%9B%BD)
- [抖音 #3 | “破五”出游注意防风沙](https://www.douyin.com/hot/2407742)
- [今日头条 #3 | 全球多地举办活动 共庆新春佳节](https://www.toutiao.com/trending/7609221704333659658/)
- [知乎 #3 | 小伙撕去年对联天塌了，「门上全是胶，钢丝球都刷不下来」，你遇到过这情况吗？有什么有效去除方法么？](https://www.zhihu.com/question/2008211250732038004)
- [财联社热门 #3 | 特朗普宣布签署行政令 加征10%全球进口关税](https://www.cls.cn/detail/2292246)
- [华尔街见闻 #3 | 最高法裁决后特朗普动用替补工具，加征10%全球关税，放话关税会比之前“高得多”](https://wallstreetcn.com/articles/3765912)
- [澎湃新闻 #3 | 人勤春早暖意先行！春节后首批“点对点”务工劳动者乘专机专列抵沪](https://www.thepaper.cn/newsDetail_forward_32636648)
- [微博 #4 | 女孩被当街暴打当地何以沉默两天](https://s.weibo.com/weibo?q=%23%E5%A5%B3%E5%AD%A9%E8%A2%AB%E5%BD%93%E8%A1%97%E6%9A%B4%E6%89%93%E5%BD%93%E5%9C%B0%E4%BD%95%E4%BB%A5%E6%B2%89%E9%BB%98%E4%B8%A4%E5%A4%A9%23)
- [百度热搜 #4 | “你的老鸭汤只剩汤了”](https://www.baidu.com/s?wd=%E2%80%9C%E4%BD%A0%E7%9A%84%E8%80%81%E9%B8%AD%E6%B1%A4%E5%8F%AA%E5%89%A9%E6%B1%A4%E4%BA%86%E2%80%9D)
- [贴吧 #4 | 绿帽文争霸,新五绿诞生](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%BB%BF%E5%B8%BD%E6%96%87%E4%BA%89%E9%9C%B8%2C%E6%96%B0%E4%BA%94%E7%BB%BF%E8%AF%9E%E7%94%9F&topic_id=28350833)
- [凤凰网 #4 | 美大使：以色列拿下整个中东，也没问题](https://news.ifeng.com/c/8qvPCuKv7yI)
- [知乎 #4 | 为什么开放的 Windows 战胜了封闭的 macOS，但是开放的 Android 却战胜不了封闭的 iOS？](https://www.zhihu.com/question/2007124650916856053)
- [华尔街见闻 #4 | 1750亿美元“关税退款”！对美股是“财政刺激”，对美债是“增加债务”，对金银是“不确定性重来”](https://wallstreetcn.com/articles/3765925)
- [bilibili 热搜 #4 | 英国首相斯塔默面临哪些困境](https://search.bilibili.com/all?keyword=%E8%8B%B1%E5%9B%BD%E9%A6%96%E7%9B%B8%E6%96%AF%E5%A1%94%E9%BB%98%E9%9D%A2%E4%B8%B4%E5%93%AA%E4%BA%9B%E5%9B%B0%E5%A2%83)
- [抖音 #4 | 正月初五接财神](https://www.douyin.com/hot/2407307)
- [财联社热门 #4 | 原来公募春节前就在集中调研，机器人、半导体、有色金属都是调研热点](https://www.cls.cn/detail/2291772)
- [澎湃新闻 #4 | 载8名中国游客汽车在贝加尔湖落水，目前仅一名中国游客获救](https://www.thepaper.cn/newsDetail_forward_32636440)
- [抖音 #5 | 新闻联播](https://www.douyin.com/hot/2407939)
- [今日头条 #5 | 《新闻联播》正在直播](https://www.toutiao.com/trending/7608412791876993074/)
- [百度热搜 #5 | 河南一景区空中撒钱 面值最高100元](https://www.baidu.com/s?wd=%E6%B2%B3%E5%8D%97%E4%B8%80%E6%99%AF%E5%8C%BA%E7%A9%BA%E4%B8%AD%E6%92%92%E9%92%B1+%E9%9D%A2%E5%80%BC%E6%9C%80%E9%AB%98100%E5%85%83)
- [微博 #5 | 徐梦桃第一跳81.99分](https://s.weibo.com/weibo?q=%23%E5%BE%90%E6%A2%A6%E6%A1%83%E7%AC%AC%E4%B8%80%E8%B7%B381.99%E5%88%86%23)
- [贴吧 #5 | 日企采用中国芯,岛民破防](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%97%A5%E4%BC%81%E9%87%87%E7%94%A8%E4%B8%AD%E5%9B%BD%E8%8A%AF%2C%E5%B2%9B%E6%B0%91%E7%A0%B4%E9%98%B2&topic_id=28350832)
- [凤凰网 #5 | 学者：特朗普或遭众叛亲离](https://news.ifeng.com/c/8qvPCuKv7tH)
- [澎湃新闻 #5 | 春启新程｜在上海的第15个春节，她说老人们这个时候更需要自己](https://www.thepaper.cn/newsDetail_forward_32635177)
- [知乎 #5 | 「小矮马」马年火爆全网，最低六千元就能入手，但有买家称「每天要铲屎十斤」，矮脚马真的适合当宠物吗？](https://www.zhihu.com/question/2005330908966851008)
- [bilibili 热搜 #5 | 经典IP寻秦记上线B站](https://search.bilibili.com/all?keyword=%E5%AF%BB%E7%A7%A6%E8%AE%B0)
- [华尔街见闻 #5 | 美国四季度GDP仅增1.4%！政府停摆拖累1个百分点，特朗普提前“开火”鲍威尔](https://wallstreetcn.com/articles/3765906)
- [财联社热门 #5 | 美股收盘：多重利空压顶华尔街情绪恶化 三大指数集体下跌](https://www.cls.cn/detail/2291935)
- [今日头条 #6 | 《飞驰人生3》韩寒终于不再浪费天赋](https://www.toutiao.com/trending/7609262135771663915/)
- [凤凰网 #6 | “和平委员会”首次开会，48名代表身份藏玄机](https://news.ifeng.com/c/8qvTLaWprko)
- [微博 #6 | 黄晓明曝艺人红毯上假摔](https://s.weibo.com/weibo?q=%E9%BB%84%E6%99%93%E6%98%8E%E6%9B%9D%E8%89%BA%E4%BA%BA%E7%BA%A2%E6%AF%AF%E4%B8%8A%E5%81%87%E6%91%94)
- [贴吧 #6 | 12人遇难!熊孩子放炮闯祸](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=12%E4%BA%BA%E9%81%87%E9%9A%BE%21%E7%86%8A%E5%AD%A9%E5%AD%90%E6%94%BE%E7%82%AE%E9%97%AF%E7%A5%B8&topic_id=28350829)
- [抖音 #6 | 消息称美考虑打击哈梅内伊父子](https://www.douyin.com/hot/2407540)
- [百度热搜 #6 | 王濛：不行让我签生死状复出](https://www.baidu.com/s?wd=%E7%8E%8B%E6%BF%9B%EF%BC%9A%E4%B8%8D%E8%A1%8C%E8%AE%A9%E6%88%91%E7%AD%BE%E7%94%9F%E6%AD%BB%E7%8A%B6%E5%A4%8D%E5%87%BA)
- [bilibili 热搜 #6 | 挑战在国外抓中国人共进年夜饭](https://search.bilibili.com/all?keyword=%E6%8C%91%E6%88%98%E5%9C%A8%E5%9B%BD%E5%A4%96%E6%8A%93%E4%B8%AD%E5%9B%BD%E4%BA%BA%E5%85%B1%E8%BF%9B%E5%B9%B4%E5%A4%9C%E9%A5%AD)
- [知乎 #6 | 手机为啥越卖越贵了？](https://www.zhihu.com/question/12538422686)
- [华尔街见闻 #6 | 得知高院否决关税那一刻，特朗普“气炸了”，“破口大骂”](https://wallstreetcn.com/articles/3765923)
- [澎湃新闻 #6 | 王心迪、徐梦桃成为中国体育史上第六对奥运金牌夫妇](https://www.thepaper.cn/newsDetail_forward_32637045)
- [财联社热门 #6 | “存储荒”愈演愈烈！三星HBM4据称涨价30% 韩国“芯片双雄”积极扩产](https://www.cls.cn/detail/2291781)
- [凤凰网 #7 | 伊朗外长拒绝打开美方装有导弹提议的信函，并将其退回](https://news.ifeng.com/c/8qvb09i2f7O)
- [百度热搜 #7 | 300年打树花年味儿爆棚](https://www.baidu.com/s?wd=300%E5%B9%B4%E6%89%93%E6%A0%91%E8%8A%B1%E5%B9%B4%E5%91%B3%E5%84%BF%E7%88%86%E6%A3%9A)
- [bilibili 热搜 #7 | 苹果味饮品为何突然爆发](https://search.bilibili.com/all?keyword=%E8%8B%B9%E6%9E%9C%E5%91%B3%E9%A5%AE%E5%93%81%E4%B8%BA%E4%BD%95%E7%AA%81%E7%84%B6%E7%88%86%E5%8F%91)
- [财联社热门 #7 | 什么信号？OpenAI大幅下调算力支出目标：6000亿美元！](https://www.cls.cn/detail/2292326)
- [今日头条 #7 | 存款利率跌入“0”字头](https://www.toutiao.com/trending/7608141024543785014/)
- [澎湃新闻 #7 | 释新闻｜美最高法院6比3裁定特朗普全球关税违法，意味着什么？](https://www.thepaper.cn/newsDetail_forward_32638670)
- [知乎 #7 | 如何评价湖北省文旅厅认定那艺娜（翟革英）为劣迹艺人，叫停其演出？](https://www.zhihu.com/question/2008437078631940159)
- [贴吧 #7 | 国gal暴死,40万众筹打水漂](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E5%9B%BDgal%E6%9A%B4%E6%AD%BB%2C40%E4%B8%87%E4%BC%97%E7%AD%B9%E6%89%93%E6%B0%B4%E6%BC%82&topic_id=28350824)
- [微博 #7 | 刘涛演妈祖 三次圣杯](https://s.weibo.com/weibo?q=%E5%88%98%E6%B6%9B%E6%BC%94%E5%A6%88%E7%A5%96+%E4%B8%89%E6%AC%A1%E5%9C%A3%E6%9D%AF)
- [抖音 #7 | 美将终止部分关税措施](https://www.douyin.com/hot/2407328)
- [华尔街见闻 #7 | “谷歌天团”反击AI泡沫质疑：这是工业革命，但速度快10倍、规模大10倍](https://wallstreetcn.com/articles/3765904)
- [百度热搜 #8 | “前方无厕所、无烤肠、无茶叶蛋”](https://www.baidu.com/s?wd=%E2%80%9C%E5%89%8D%E6%96%B9%E6%97%A0%E5%8E%95%E6%89%80%E3%80%81%E6%97%A0%E7%83%A4%E8%82%A0%E3%80%81%E6%97%A0%E8%8C%B6%E5%8F%B6%E8%9B%8B%E2%80%9D)
- [今日头条 #8 | 高速上鸭子掉落暴走 车主来认领](https://www.toutiao.com/trending/7609150350486126633/)
- [微博 #8 | 烤肠商战](https://s.weibo.com/weibo?q=%E7%83%A4%E8%82%A0%E5%95%86%E6%88%98)
- [知乎 #8 | 你如何看待湛江东海岛拾石村妈祖女孩被替换？](https://www.zhihu.com/question/2008207494175011823)
- [澎湃新闻 #8 | 视频丨硬核揭秘！福建舰“一马当先”底气何在？](https://www.thepaper.cn/newsDetail_forward_32638555)
- [贴吧 #8 | 王濛痛骂短道队:林孝埈练废了](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E7%8E%8B%E6%BF%9B%E7%97%9B%E9%AA%82%E7%9F%AD%E9%81%93%E9%98%9F%3A%E6%9E%97%E5%AD%9D%E5%9F%88%E7%BB%83%E5%BA%9F%E4%BA%86&topic_id=28350817)
- [抖音 #8 | 克宫：俄日关系“已降至零点”](https://www.douyin.com/hot/2407159)
- [凤凰网 #8 | 多国敦促在伊朗公民尽快撤离](https://news.ifeng.com/c/8qurLBUotqV)
- [华尔街见闻 #8 | 美联储最青睐的通胀指标超预期！美国12月核心PCE物价指数同比3%](https://wallstreetcn.com/articles/3765907)
- [财联社热门 #8 | “马年科技春晚”让买机器人的股民都松了一口气？节前资金已挤入ETF](https://www.cls.cn/detail/2291748)
- [bilibili 热搜 #8 | 年轻人走亲戚的方式](https://search.bilibili.com/all?keyword=%E5%B9%B4%E8%BD%BB%E4%BA%BA%E8%B5%B0%E4%BA%B2%E6%88%9A%E7%9A%84%E6%96%B9%E5%BC%8F)
- [知乎 #9 | ClaudeCode 之父称不再需要「planmode」，将对 AI 编程带来哪些变革？](https://www.zhihu.com/question/2008176730532234790)
- [微博 #9 | 我家那小子](https://s.weibo.com/weibo?q=%E6%88%91%E5%AE%B6%E9%82%A3%E5%B0%8F%E5%AD%90)
- [财联社热门 #9 | 春节档总票房破40亿！《飞驰人生3》21亿领跑，背后涉及哪些A股公司？](https://www.cls.cn/detail/2292289)
- [抖音 #9 | 王心迪夺冠后谈及徐梦桃](https://www.douyin.com/hot/2407334)
- [澎湃新闻 #9 | 2026春节档总场次刷新中国影史纪录](https://www.thepaper.cn/newsDetail_forward_32638734)
- [华尔街见闻 #9 | 别为美最高法推翻特朗普关税高兴太早？华尔街预计市场反应或昙花一现](https://wallstreetcn.com/articles/3765913)
- [今日头条 #9 | 王濛怒斥短道队：不行我签生死状复出](https://www.toutiao.com/trending/7608275916123095086/)
- [bilibili 热搜 #9 | 实测Gemini 3.1 Pro](https://search.bilibili.com/all?keyword=%E5%AE%9E%E6%B5%8BGemini+3.1+Pro)
- [凤凰网 #9 | 泽连斯基：乌克兰已准备好作出“真正的妥协”](https://news.ifeng.com/c/8quBSNXwvb9)
- [贴吧 #9 | 港人偷拍同胞,阴阳国人没素质](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E6%B8%AF%E4%BA%BA%E5%81%B7%E6%8B%8D%E5%90%8C%E8%83%9E%2C%E9%98%B4%E9%98%B3%E5%9B%BD%E4%BA%BA%E6%B2%A1%E7%B4%A0%E8%B4%A8&topic_id=28350812)
- [凤凰网 #10 | 夫妻当街暴打15岁女孩，底气从何而来？](https://news.ifeng.com/c/8qvbbpgFD4Q)
- [百度热搜 #10 | 被指到的人今年财源滚滚](https://www.baidu.com/s?wd=%E8%A2%AB%E6%8C%87%E5%88%B0%E7%9A%84%E4%BA%BA%E4%BB%8A%E5%B9%B4%E8%B4%A2%E6%BA%90%E6%BB%9A%E6%BB%9A)
- [微博 #10 | 回村后用的都是名牌货](https://s.weibo.com/weibo?q=%E5%9B%9E%E6%9D%91%E5%90%8E%E7%94%A8%E7%9A%84%E9%83%BD%E6%98%AF%E5%90%8D%E7%89%8C%E8%B4%A7)
- [华尔街见闻 #10 | 华尔街见闻早餐FM-Radio | 2026年2月21日](https://wallstreetcn.com/articles/3765920)
- [今日头条 #10 | 卫星图像显示60余架美军机驻扎约旦基地](https://www.toutiao.com/trending/7609228742115724827/)
- [bilibili 热搜 #10 | 春晚歌曲锐评](https://search.bilibili.com/all?keyword=%E6%98%A5%E6%99%9A%E6%AD%8C%E6%9B%B2%E9%94%90%E8%AF%84)
- [澎湃新闻 #10 | 张艺谋人民日报撰文：于无声处听惊雷](https://www.thepaper.cn/newsDetail_forward_32638642)
- [抖音 #10 | 与中国短道速滑队同在](https://www.douyin.com/hot/2407267)
- [知乎 #10 | 经理拍拍我的肩，「裁你是因为你太优秀」，然后悄悄递来竞争对手的名片，你会怎么看待这件事？](https://www.zhihu.com/question/1986031665873707499)
- [财联社热门 #10 | 香港长江和记最新发声](https://www.cls.cn/detail/2292101)
- [贴吧 #10 | 金牌夫妻!王心迪徐梦桃顶峰相见](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E9%87%91%E7%89%8C%E5%A4%AB%E5%A6%BB%21%E7%8E%8B%E5%BF%83%E8%BF%AA%E5%BE%90%E6%A2%A6%E6%A1%83%E9%A1%B6%E5%B3%B0%E7%9B%B8%E8%A7%81&topic_id=28350813)
- [微博 #11 | idle演唱会](https://s.weibo.com/weibo?q=idle%E6%BC%94%E5%94%B1%E4%BC%9A)
- [凤凰网 #11 | 卫星图像曝光！“数十架美军机已驻扎在约旦基地”](https://news.ifeng.com/c/8qvWtj5wjsI)
- [知乎 #11 | 既然传统 RTS 的没落源于「战斗 5 分钟 + 种田 2 小时」，那「轻种田 + 重战斗」的新玩法能否复兴 RTS 呢？](https://www.zhihu.com/question/2008152050291200339)
- [百度热搜 #11 | 大连一大学免统考补录硕士系谣言](https://www.baidu.com/s?wd=%E5%A4%A7%E8%BF%9E%E4%B8%80%E5%A4%A7%E5%AD%A6%E5%85%8D%E7%BB%9F%E8%80%83%E8%A1%A5%E5%BD%95%E7%A1%95%E5%A3%AB%E7%B3%BB%E8%B0%A3%E8%A8%80)
- [今日头条 #11 | 免统考补录硕士？大连医科大学辟谣](https://www.toutiao.com/trending/7609122130168627242/)
- [抖音 #11 | 中国自由式滑雪空中技巧为何这么强](https://www.douyin.com/hot/2407257)
- [澎湃新闻 #11 | 俄紧急情况部：已发现7名遇难者遗体，计划展开打捞作业](https://www.thepaper.cn/newsDetail_forward_32636638)
- [贴吧 #11 | 老外栽跟头,约会华人遭敲诈](https://tieba.baidu.com/hottopic/browse/hottopic?amp%3Btopic_name=%E8%80%81%E5%A4%96%E6%A0%BD%E8%B7%9F%E5%A4%B4%2C%E7%BA%A6%E4%BC%9A%E5%8D%8E%E4%BA%BA%E9%81%AD%E6%95%B2%E8%AF%88&topic_id=28350814)
- [bilibili 热搜 #11 | 大学生回家过年合集](https://search.bilibili.com/all?keyword=%E5%A4%A7%E5%AD%A6%E7%94%9F%E5%9B%9E%E5%AE%B6%E8%BF%87%E5%B9%B4%E5%90%88%E9%9B%86)
- [财联社热门 #11 | 莫迪举手全场欢呼 两大AI掌门人却各自握拳尴尬对峙](https://www.cls.cn/detail/2291896)
- [微博 #12 | 陈丽君拍摄镖人时向梁家辉提了个请求](https://s.weibo.com/weibo?q=%23%E9%99%88%E4%B8%BD%E5%90%9B%E6%8B%8D%E6%91%84%E9%95%96%E4%BA%BA%E6%97%B6%E5%90%91%E6%A2%81%E5%AE%B6%E8%BE%89%E6%8F%90%E4%BA%86%E4%B8%AA%E8%AF%B7%E6%B1%82%23)
- [百度热搜 #12 | 寒潮+暴雪+大风+沙尘暴4预警齐发](https://www.baidu.com/s?wd=%E5%AF%92%E6%BD%AE%2B%E6%9A%B4%E9%9B%AA%2B%E5%A4%A7%E9%A3%8E%2B%E6%B2%99%E5%B0%98%E6%9A%B44%E9%A2%84%E8%AD%A6%E9%BD%90%E5%8F%91)
- [今日头条 #12 | 徐立凡：特朗普超级总统时代或将结束](https://www.toutiao.com/trending/7609238176095276607/)

### 💻 GitHub 原文 (20/40 条)

- [openclaw/openclaw | ⭐ 215202 | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞](https://github.com/openclaw/openclaw)
- [Significant-Gravitas/AutoGPT | ⭐ 181913 | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission i...](https://github.com/Significant-Gravitas/AutoGPT)
- [n8n-io/n8n | ⭐ 175609 | Fair-code workflow automation platform with native AI capabilities. Combine visual buildin...](https://github.com/n8n-io/n8n)
- [ollama/ollama | ⭐ 163047 | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and othe...](https://github.com/ollama/ollama)
- [huggingface/transformers | ⭐ 156772 | 🤗 Transformers: the model-definition framework for state-of-the-art machine learning model...](https://github.com/huggingface/transformers)
- [f/prompts.chat | ⭐ 146022 | a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. F...](https://github.com/f/prompts.chat)
- [langflow-ai/langflow | ⭐ 144940 | Langflow is a powerful tool for building and deploying AI-powered agents and workflows.](https://github.com/langflow-ai/langflow)
- [langgenius/dify | ⭐ 129896 | Production-ready platform for agentic workflow development.](https://github.com/langgenius/dify)
- [langchain-ai/langchain | ⭐ 127088 | 🦜🔗 The platform for reliable agents.](https://github.com/langchain-ai/langchain)
- [nautechsystems/nautilus_trader | ⭐ 20094 | A high-performance algorithmic trading platform and event-driven backtester](https://github.com/nautechsystems/nautilus_trader)
- [jesse-ai/jesse | ⭐ 7439 | An advanced crypto trading bot written in Python](https://github.com/jesse-ai/jesse)
- [tensorflow/tensorflow | ⭐ 193873 | An Open Source Machine Learning Framework for Everyone](https://github.com/tensorflow/tensorflow)
- [foundry-rs/foundry | ⭐ 10129 | Foundry is a blazing fast, portable and modular toolkit for Ethereum application developme...](https://github.com/foundry-rs/foundry)
- [HKUDS/ClawWork | ⭐ 4692 | "ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"](https://github.com/HKUDS/ClawWork)
- [nicobailon/visual-explainer | ⭐ 2022 | Agent skill + prompt templates that generate rich HTML pages for visual diff reviews, arch...](https://github.com/nicobailon/visual-explainer)
- [vercel-labs/portless | ⭐ 1894 | Replace port numbers with stable, named .localhost URLs. For humans and agents.](https://github.com/vercel-labs/portless)
- [ebrasha/free-v2ray-public-list | ⭐ 522 | A simple and always-updated list of free, working V2Ray servers. including SS, SSR, Trojan...](https://github.com/ebrasha/free-v2ray-public-list)
- [agenticnotetaking/arscontexta | ⭐ 1374 | Claude Code plugin that generates individualized knowledge systems from conversation. You ...](https://github.com/agenticnotetaking/arscontexta)
- [nullclaw/nullclaw | ⭐ 1301 | Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig](https://github.com/nullclaw/nullclaw)
- [AlexsJones/llmfit | ⭐ 1198 | 157 models. 30 providers. One command to find what runs on your hardware.](https://github.com/AlexsJones/llmfit)

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

### 🌐 联网检索原文 (15/15 条)

- [2026-02-21 13:43 nfnews.com | 2026年，谁来接棒公募基金233%的收益神话？ - nfnews.com](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5oV21MeG5GVV9nQzN1c3NJVTRodU13UnM4TWw5VU04cWx2RVJZU1FuS01kS3FRb2JHdXVqanVRRzRwMWdSaE9ER3pBeFRaMlpTMkxUVXFGV3o3UQ?oc=5)
- [2026-02-21 13:29 新浪财经 | 【环球财经】巴西股市创历史新高 美最高法院裁决提振市场信心 - 新浪财经](https://news.google.com/rss/articles/CBMigAFBVV95cUxQSm40Mk51bUs1ZGdzU3podHd3ckFBLUlma00waE5Vem5oSDZpd1Fib2hlVlBfMlJZR2pXbzhjckhEd3NHVzlxWHQzNnJ4LVVtUlB3dDFuckRWMS1JY3RHbmNndzBpTEgxTjNzVFdmYlBlTzd4VHdpeHlnVGNGT2Y3Nw?oc=5)
- [2026-02-21 11:51 新浪财经 | 印度AI峰会连闹笑话！2家顶尖机构被曝用宇树机器狗冒充自研【附机器狗行业分析】 - 新浪财经](https://news.google.com/rss/articles/CBMieEFVX3lxTFBsLUNoMDMxUE9KaXZKVUk5YXRkTFNKbEpFamNRVE9SZl8yMlJRdVB2UE5IdldKM1ptaG5jMFFWTFI3WFFud3g3M25sa0xXMW82V1BOdG4wMnVaMVVXWldWM3hNQWlEdXhMTHBRUUJvLXVWMmZkWVM4cA?oc=5)
- [2026-02-21 11:03 万维读者网 | 美股创20年来首年最差纪录 - 万维读者网](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1WSDNxZ3dzeWFoNWZpMlk3T05wZ2RPbFZZSllnajdvWXU4T0pxWk13eW1pd2xDSkZNaEhSQXQ1cURwRl96YTBaZC1mMTA5ZnFmMVE?oc=5)
- [2026-02-21 10:11 3DM | 环亚国际娱乐登录网址(娱乐行业资讯) - 3DM](https://news.google.com/rss/articles/CBMiV0FVX3lxTE1ncGZab19BMlpHbUNCT0s0VlotTVhETjEwRVQwU3VfX21FNmxhemFaTk1MT19wekswS0w1SGpMYmV1alNUSUh3MHUxWDVId0hQU2xVQXFfRQ?oc=5)
- [2026-02-21 09:00 news.17173.com | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - news.17173.com](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9SNi1JaUtGay14WGNGN0NfM1dzSkVOTVlWS0ZBdjVlNFZjWWRDdHd1cFBENEU5ekI2N1dzT3hvQzBZM0Y3R012SERVeUdtRFNFQ0l4WTM2WjVTa0ViLTM2VVpHcDlGdw?oc=5)
- [2026-02-21 08:24 yeeyi | 春节旅游成噩梦！7名中国游客坠湖遇难，目击者发声：车两三分钟就沉了 - yeeyi](https://news.google.com/rss/articles/CBMiVkFVX3lxTE91dGZGTy1OSTZSb2VXUjhVVC1kRFFtM0g5aXRtNXdzUThFR2lCanJhRlVrUk9xTExQSmpramhzUzJPRXItSGFMYXdmZ2VRc1g3Nmk0c1VB?oc=5)
- [2026-02-21 08:20 thepaper.cn | 首席展望｜摩根大通刘鸣镝：A股进入“慢牛”，外资回流可期 - thepaper.cn](https://news.google.com/rss/articles/CBMiYEFVX3lxTE0yemJ2MnYyX3ZFdlYtMloyQ0hDcWZGT01jZXZUQjRYV2t1bFRaM1Vfd094cUlyY1NSSU1JNGlJNUpSWFE5S1JMQ29XRTd6Z3VHX3lRVVhBQmlrRkZyXzUzYg?oc=5)
- [2026-02-21 08:09 新浪财经 | 摆脱英伟达等束缚！深圳：拟研发14nm以下国产AI芯片 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTE1OQlg5QnNON2hKWlFSclQ2bVh5ZVhqcXB4b0Itck5VRG5TcW81TVkzeVpEWXItM2xWOGo5QlpVSFVQSkNFWW45NWxubXMxMmNTSzhMazM3N21ybUhUR0t3aU4zMHRrTDluLVFBY1pEcFRMWlFKUDA4MkRYQ0l4QTA?oc=5)
- [2026-02-21 08:01 新浪财经 | 从流量到留量：2025年消费并购的静水深流 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTE9fY3dBaHlhQW84VUF6cXpvb3FBVWFSbTc4NG5pQThVZ3ZYMENxRm9zVS1XcWZXaEk2clJ4QkFLUlMyUnM1VFotazVWSUZEMkpzWVozY2ZOX1VMU19FSFNhYmdlV25LZkR4R05KTkNyS3NzeURRSmxsM2dnNW9pcjA?oc=5)
- [2026-02-21 07:47 富途牛牛 | 美最高院否决关税，美股收高，债汇承压，滞胀担忧撑黄金重回5100，白银大涨8% - 富途牛牛](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1Gc2lhd1R6dnVmdldwbWFaSVBWaHdoak16V0J1WmY1MGtZWlF3RWNoNkVrVklCNGxRRGE2bEk3dkhvN2t6MFNQdUpEdTZCdw?oc=5)
- [2026-02-21 07:15 新浪财经 | 新浪财经隔夜要闻大事汇总：2026年2月21日 - 新浪财经](https://news.google.com/rss/articles/CBMihAFBVV95cUxQY25wdUpCLWtCOUloS2FsaTFna0M1bEZoVTY3aXQ4OUY3WFNOLWFtU2lUMFYzeW8tdTc3RDBYVGF1YXdEeng0bTdZUzdWblhINGVfYnEtSHI5ZWFvOUNmaV9iTjliYTZMR3RDaHlfUTNwRFprdEhtdDdrS1dtTkQ2aUZFVlk?oc=5)
- [2026-02-21 07:11 游侠网 | 热点第一 DAFA八百八十八国际 - 游侠网](https://news.google.com/rss/articles/CBMiTkFVX3lxTFA5aExXVjI3bF9PVDYxeWpQcnJzN0xQMzJXekhiaWJaMVh4MU95V3l1TTRwNERiMVE0RERvQ2F5SnNBdmI1Mk9sWTNkTDc5dw?oc=5)
- [2026-02-21 05:30 英为财情 Investing.com | 美国股市上涨；截至收盘道琼斯工业平均指数上涨0.47% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE9wU0M2TlpFTHZ4T0wwa3dzR3Jnbm1aeVczZUpFVTMtOEpuci0xNjhvMHVJTDFsdFVvOVd1MmJOYlF4cmF4NlEyX3k1XzRMUUI4MGFkUkNqakNqTTNiZEhfWDJjYUMzeTA5OXFFRmZhUzE?oc=5)
- [2026-02-21 05:30 英为财情 Investing.com | 加拿大股市上涨；截至收盘加拿大多伦多S&P/TSX 综合指数上涨0.66% 提供者 Investing.com - 英为财情 Investing.com](https://news.google.com/rss/articles/CBMicEFVX3lxTE40WFNNZHp1QW1SLUpVNG5LSUpoMFMyQlFJbkJWTW50VnFXcm9LWGZaM19LM0h2UXpOLVp4WEkwZ3p5azUyZHhQYmlzQy02dlVNRTcwOW1RU2hmMUNBUTd0Q2oyb2NxMGJGTEdWbHF3YVo?oc=5)

---

*报告由 finradar 自动生成 | 2026-02-21 20:03:16（北京时间）*
