# 会话 Checkpoint 记录

> 每次重要改动后追加一条，便于跨会话续做。

## 2026-02-11 16:32:04 CST
- 分支: `main`
- 最新提交: `0426360`
- 当前意图: 接入联网检索+结构化摘要
- 下一步: 继续优化检索关键词质量与AI提示词
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\344\275\277\347\224\250\346\214\207\345\215\227.md"
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\351\203\250\347\275\262\346\214\207\345\215\227.md"
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? "docs/\345\274\200\345\217\221\346\265\201\347\250\213\344\270\216\344\274\232\350\257\235\344\272\244\346\216\245.md"
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
?? scripts/dev_checkpoint.sh
```
- 最近提交:
```
0426360 v2.0
c672326 v 1.3
a828342 stable v1.2
7f8a8e8 stable v1.1
650e931 stable v1
bdf2b26 one docker
af65521 feat: 添加时间过滤功能和全文抓取功能
c6784b0 docs: 添加使用指南和一键更新脚本
```

## 2026-02-11 16:32:40 CST
- 分支: `main`
- 最新提交: `43f7d1a`
- 当前意图: 已完成联网检索与结构化摘要改造并提交
- 下一步: 下一步观察报告质量并迭代检索关键词
- 工作区状态:
```
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
```
- 最近提交:
```
43f7d1a docs(process): add session handoff workflow and checkpoint tooling
f527c73 feat(report): add web search context and structured brief format
0426360 v2.0
c672326 v 1.3
a828342 stable v1.2
7f8a8e8 stable v1.1
650e931 stable v1
bdf2b26 one docker
```

## 2026-02-11 16:34:31 CST
- 分支: `main`
- 最新提交: `eddef6d`
- 当前意图: 已新增自动提交脚本并完善流程文档
- 下一步: 下一步在真实晚报窗口观察AI输出质量
- 工作区状态:
```
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
```
- 最近提交:
```
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
3fe6e08 docs(process): update session checkpoint after report refactor
43f7d1a docs(process): add session handoff workflow and checkpoint tooling
f527c73 feat(report): add web search context and structured brief format
0426360 v2.0
c672326 v 1.3
a828342 stable v1.2
7f8a8e8 stable v1.1
```

## 2026-02-11 16:35:23 CST
- 分支: `main`
- 最新提交: `1128610`
- 当前意图: 自动提交脚本已改为安全模式
- 下一步: 下一步根据真实日内数据优化关键词提取
- 工作区状态:
```
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
```
- 最近提交:
```
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
3fe6e08 docs(process): update session checkpoint after report refactor
43f7d1a docs(process): add session handoff workflow and checkpoint tooling
f527c73 feat(report): add web search context and structured brief format
0426360 v2.0
c672326 v 1.3
```

## 2026-02-11 16:36:21 CST
- 分支: `main`
- 最新提交: `ebee66e`
- 当前意图: 测试意图
- 下一步: 测试下一步
- 工作区状态:
```
 M README.local.md
 M "docs/\345\274\200\345\217\221\346\265\201\347\250\213\344\270\216\344\274\232\350\257\235\344\272\244\346\216\245.md"
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\351\203\250\347\275\262\346\214\207\345\215\227.md"
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
```
- 最近提交:
```
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
3fe6e08 docs(process): update session checkpoint after report refactor
43f7d1a docs(process): add session handoff workflow and checkpoint tooling
f527c73 feat(report): add web search context and structured brief format
0426360 v2.0
```

## 2026-02-11 17:06:50 CST
- 分支: `main`
- 最新提交: `b2ae0c4`
- 当前意图: 生成20260211 evening 报告（no-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
```
- 最近提交:
```
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
3fe6e08 docs(process): update session checkpoint after report refactor
43f7d1a docs(process): add session handoff workflow and checkpoint tooling
```

## 2026-02-11 17:07:08 CST
- 分支: `main`
- 最新提交: `44e502c`
- 当前意图: 增强中文晚报结构化体验
- 下一步: 持续观察 evening 社交数据和分板块长度
- 工作区状态:
```
 M docs/SESSION_CHECKPOINT.md
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
```
- 最近提交:
```
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
3fe6e08 docs(process): update session checkpoint after report refactor
```

## 2026-02-11 17:16:53 CST
- 分支: `main`
- 最新提交: `b79ff84`
- 当前意图: 接入 Yahoo Finance 股票总览并进入日报
- 下一步: 优化晚报社交数据时段匹配与市场板块压缩
- 工作区状态:
```
 M docs/SESSION_CHECKPOINT.md
 M finradar/market/fetcher/wechat_article.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
```
- 最近提交:
```
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
```

## 2026-02-13 13:39:11 CST
- 分支: `main`
- 最新提交: `b79ff84`
- 当前意图: 生成20260213 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\344\275\277\347\224\250\346\214\207\345\215\227.md"
 M finradar/__main__.py
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/generate_report.py
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/html/2026-02-12/
?? output/html/2026-02-13/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_evening.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_data_20260212.json
?? output/market/market_data_20260212_evening.json
?? output/market/market_data_20260212_morning.json
?? output/market/market_data_20260213.json
?? output/market/market_data_20260213_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_evening.txt
?? output/market/market_report_20260211_morning.txt
?? output/market/market_report_20260212.txt
?? output/market/market_report_20260212_evening.txt
?? output/market/market_report_20260212_morning.txt
?? output/market/market_report_20260213.txt
?? output/market/market_report_20260213_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/news/2026-02-12.db
?? output/news/2026-02-13.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/report/daily_20260212_evening.md
?? output/report/daily_20260212_morning.md
?? output/report/daily_20260213_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
?? output/rss/2026-02-12.db
?? output/rss/2026-02-13.db
```
- 最近提交:
```
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
```

## 2026-02-14 11:29:37 CST
- 分支: `main`
- 最新提交: `b79ff84`
- 当前意图: 生成20260213 evening 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\344\275\277\347\224\250\346\214\207\345\215\227.md"
 M finradar/__main__.py
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/html/2026-02-12/
?? output/html/2026-02-13/
?? output/html/2026-02-14/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_evening.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_data_20260212.json
?? output/market/market_data_20260212_evening.json
?? output/market/market_data_20260212_morning.json
?? output/market/market_data_20260213.json
?? output/market/market_data_20260213_evening.json
?? output/market/market_data_20260213_morning.json
?? output/market/market_data_20260214.json
?? output/market/market_data_20260214_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_evening.txt
?? output/market/market_report_20260211_morning.txt
?? output/market/market_report_20260212.txt
?? output/market/market_report_20260212_evening.txt
?? output/market/market_report_20260212_morning.txt
?? output/market/market_report_20260213.txt
?? output/market/market_report_20260213_evening.txt
?? output/market/market_report_20260213_morning.txt
?? output/market/market_report_20260214.txt
?? output/market/market_report_20260214_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/news/2026-02-12.db
?? output/news/2026-02-13.db
?? output/news/2026-02-14.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/report/daily_20260212_evening.md
?? output/report/daily_20260212_morning.md
?? output/report/daily_20260213_evening.md
?? output/report/daily_20260213_morning.md
?? output/report/daily_20260214_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
?? output/rss/2026-02-12.db
?? output/rss/2026-02-13.db
?? output/rss/2026-02-14.db
```
- 最近提交:
```
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
```

## 2026-02-14 11:34:19 CST
- 分支: `main`
- 最新提交: `b79ff84`
- 当前意图: 生成20260213 evening 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\344\275\277\347\224\250\346\214\207\345\215\227.md"
 M finradar/__main__.py
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/html/2026-02-12/
?? output/html/2026-02-13/
?? output/html/2026-02-14/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_evening.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_data_20260212.json
?? output/market/market_data_20260212_evening.json
?? output/market/market_data_20260212_morning.json
?? output/market/market_data_20260213.json
?? output/market/market_data_20260213_evening.json
?? output/market/market_data_20260213_morning.json
?? output/market/market_data_20260214.json
?? output/market/market_data_20260214_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_evening.txt
?? output/market/market_report_20260211_morning.txt
?? output/market/market_report_20260212.txt
?? output/market/market_report_20260212_evening.txt
?? output/market/market_report_20260212_morning.txt
?? output/market/market_report_20260213.txt
?? output/market/market_report_20260213_evening.txt
?? output/market/market_report_20260213_morning.txt
?? output/market/market_report_20260214.txt
?? output/market/market_report_20260214_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/news/2026-02-12.db
?? output/news/2026-02-13.db
?? output/news/2026-02-14.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/report/daily_20260212_evening.md
?? output/report/daily_20260212_morning.md
?? output/report/daily_20260213_evening.md
?? output/report/daily_20260213_morning.md
?? output/report/daily_20260214_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
?? output/rss/2026-02-12.db
?? output/rss/2026-02-13.db
?? output/rss/2026-02-14.db
```
- 最近提交:
```
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
```

## 2026-02-14 11:38:45 CST
- 分支: `main`
- 最新提交: `b79ff84`
- 当前意图: 生成20260213 evening 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\344\275\277\347\224\250\346\214\207\345\215\227.md"
 M finradar/__main__.py
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/html/2026-02-12/
?? output/html/2026-02-13/
?? output/html/2026-02-14/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_evening.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_data_20260212.json
?? output/market/market_data_20260212_evening.json
?? output/market/market_data_20260212_morning.json
?? output/market/market_data_20260213.json
?? output/market/market_data_20260213_evening.json
?? output/market/market_data_20260213_morning.json
?? output/market/market_data_20260214.json
?? output/market/market_data_20260214_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_evening.txt
?? output/market/market_report_20260211_morning.txt
?? output/market/market_report_20260212.txt
?? output/market/market_report_20260212_evening.txt
?? output/market/market_report_20260212_morning.txt
?? output/market/market_report_20260213.txt
?? output/market/market_report_20260213_evening.txt
?? output/market/market_report_20260213_morning.txt
?? output/market/market_report_20260214.txt
?? output/market/market_report_20260214_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/news/2026-02-12.db
?? output/news/2026-02-13.db
?? output/news/2026-02-14.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/report/daily_20260212_evening.md
?? output/report/daily_20260212_morning.md
?? output/report/daily_20260213_evening.md
?? output/report/daily_20260213_morning.md
?? output/report/daily_20260214_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
?? output/rss/2026-02-12.db
?? output/rss/2026-02-13.db
?? output/rss/2026-02-14.db
```
- 最近提交:
```
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
```

## 2026-02-14 11:44:10 CST
- 分支: `main`
- 最新提交: `b79ff84`
- 当前意图: 生成20260213 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 M "docs/\346\257\217\346\227\245\345\270\202\345\234\272\350\277\275\350\270\252\344\275\277\347\224\250\346\214\207\345\215\227.md"
 M finradar/__main__.py
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-10/
?? output/html/2026-02-11/
?? output/html/2026-02-12/
?? output/html/2026-02-13/
?? output/html/2026-02-14/
?? output/market/market_data_20260210.json
?? output/market/market_data_20260210_evening.json
?? output/market/market_data_20260210_morning.json
?? output/market/market_data_20260211.json
?? output/market/market_data_20260211_evening.json
?? output/market/market_data_20260211_morning.json
?? output/market/market_data_20260212.json
?? output/market/market_data_20260212_evening.json
?? output/market/market_data_20260212_morning.json
?? output/market/market_data_20260213.json
?? output/market/market_data_20260213_evening.json
?? output/market/market_data_20260213_morning.json
?? output/market/market_data_20260214.json
?? output/market/market_data_20260214_morning.json
?? output/market/market_report_20260210.txt
?? output/market/market_report_20260210_evening.txt
?? output/market/market_report_20260210_morning.txt
?? output/market/market_report_20260211.txt
?? output/market/market_report_20260211_evening.txt
?? output/market/market_report_20260211_morning.txt
?? output/market/market_report_20260212.txt
?? output/market/market_report_20260212_evening.txt
?? output/market/market_report_20260212_morning.txt
?? output/market/market_report_20260213.txt
?? output/market/market_report_20260213_evening.txt
?? output/market/market_report_20260213_morning.txt
?? output/market/market_report_20260214.txt
?? output/market/market_report_20260214_morning.txt
?? output/news/2026-02-10.db
?? output/news/2026-02-11.db
?? output/news/2026-02-12.db
?? output/news/2026-02-13.db
?? output/news/2026-02-14.db
?? output/report/daily_20260210_evening.md
?? output/report/daily_20260210_morning.md
?? output/report/daily_20260211_evening.md
?? output/report/daily_20260211_morning.md
?? output/report/daily_20260212_evening.md
?? output/report/daily_20260212_morning.md
?? output/report/daily_20260213_evening.md
?? output/report/daily_20260213_morning.md
?? output/report/daily_20260214_morning.md
?? output/rss/2026-02-10.db
?? output/rss/2026-02-11.db
?? output/rss/2026-02-12.db
?? output/rss/2026-02-13.db
?? output/rss/2026-02-14.db
```
- 最近提交:
```
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
9169d82 docs(process): checkpoint latest workflow updates
eddef6d feat(process): add safe auto-commit helper with checkpoint logging
```

