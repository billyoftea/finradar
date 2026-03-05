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

## 2026-02-25 20:13:16 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260225 auto 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/debug/test_new_report_20260225_morning.md
?? output/debug/test_new_report_20260225_morning_v2.md
?? output/html/2026-02-25/20-02.html
?? output/report/daily_20260225_evening.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/state/
?? output/twitter/report_used_tweets.jsonl
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

## 2026-02-26 19:09:57 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260226 evening 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/nitter_rss.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/debug/test_new_report_20260225_morning.md
?? output/debug/test_new_report_20260225_morning_v2.md
?? output/debug/test_report_20260225_evening_ai.md
?? output/debug/test_report_20260225_evening_ai_v2.md
?? output/debug/test_report_20260225_evening_ai_v3.md
?? output/debug/test_report_20260225_evening_ai_v4.md
?? output/debug/test_report_20260225_evening_ai_v5.md
?? output/debug/test_report_20260225_evening_noai.md
?? output/debug/test_report_20260226_morning_ai_v6.md
?? output/html/2026-02-25/20-02.html
?? output/html/2026-02-25/20-32.html
?? output/html/2026-02-25/21-02.html
?? output/html/2026-02-25/21-32.html
?? output/html/2026-02-25/22-02.html
?? output/html/2026-02-25/22-32.html
?? output/html/2026-02-25/23-01.html
?? output/html/2026-02-25/23-31.html
?? output/html/2026-02-26/
?? output/market/market_data_20260226.json
?? output/market/market_data_20260226_evening.json
?? output/market/market_data_20260226_morning.json
?? output/market/market_report_20260226.txt
?? output/market/market_report_20260226_evening.txt
?? output/market/market_report_20260226_morning.txt
?? output/news/2026-02-26.db
?? output/report/daily_20260225_evening.md
?? output/report/daily_20260226_evening.md
?? output/report/daily_20260226_morning.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/rss/2026-02-26.db
?? output/state/
?? output/twitter/report_used_tweets.jsonl
?? "\345\267\245\344\275\234\346\265\201.md"
?? "\346\250\241\346\235\277.md"
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

## 2026-02-27 10:14:11 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260227 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/nitter_rss.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/wechat_article.py
 M finradar/market/tracker.py
 M index.html
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/debug/test_new_report_20260225_morning.md
?? output/debug/test_new_report_20260225_morning_v2.md
?? output/debug/test_report_20260225_evening_ai.md
?? output/debug/test_report_20260225_evening_ai_v2.md
?? output/debug/test_report_20260225_evening_ai_v3.md
?? output/debug/test_report_20260225_evening_ai_v4.md
?? output/debug/test_report_20260225_evening_ai_v5.md
?? output/debug/test_report_20260225_evening_noai.md
?? output/debug/test_report_20260226_morning_ai_v6.md
?? output/html/2026-02-25/20-02.html
?? output/html/2026-02-25/20-32.html
?? output/html/2026-02-25/21-02.html
?? output/html/2026-02-25/21-32.html
?? output/html/2026-02-25/22-02.html
?? output/html/2026-02-25/22-32.html
?? output/html/2026-02-25/23-01.html
?? output/html/2026-02-25/23-31.html
?? output/html/2026-02-26/
?? output/html/2026-02-27/
?? output/market/market_data_20260226.json
?? output/market/market_data_20260226_evening.json
?? output/market/market_data_20260226_morning.json
?? output/market/market_data_20260227.json
?? output/market/market_data_20260227_morning.json
?? output/market/market_report_20260226.txt
?? output/market/market_report_20260226_evening.txt
?? output/market/market_report_20260226_morning.txt
?? output/market/market_report_20260227.txt
?? output/market/market_report_20260227_morning.txt
?? output/news/2026-02-26.db
?? output/news/2026-02-27.db
?? output/report/daily_20260225_evening.md
?? output/report/daily_20260226_evening.md
?? output/report/daily_20260226_morning.md
?? output/report/daily_20260227_morning.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/rss/2026-02-26.db
?? output/rss/2026-02-27.db
?? output/state/
?? output/twitter/report_used_tweets.jsonl
?? "\345\267\245\344\275\234\346\265\201.md"
?? "\346\250\241\346\235\277.md"
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

## 2026-02-27 10:55:06 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260227 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 D finradar/__pycache__/__init__.cpython-312.pyc
 D finradar/__pycache__/__main__.cpython-312.pyc
 D finradar/__pycache__/context.cpython-312.pyc
 D finradar/ai/__pycache__/__init__.cpython-312.pyc
 D finradar/ai/__pycache__/analyzer.cpython-312.pyc
 D finradar/ai/__pycache__/client.cpython-312.pyc
 D finradar/ai/__pycache__/formatter.cpython-312.pyc
 D finradar/ai/__pycache__/translator.cpython-312.pyc
 D finradar/core/__pycache__/__init__.cpython-312.pyc
 D finradar/core/__pycache__/analyzer.cpython-312.pyc
 D finradar/core/__pycache__/config.cpython-312.pyc
 D finradar/core/__pycache__/data.cpython-312.pyc
 D finradar/core/__pycache__/frequency.cpython-312.pyc
 D finradar/core/__pycache__/loader.cpython-312.pyc
 D finradar/crawler/__pycache__/__init__.cpython-312.pyc
 D finradar/crawler/__pycache__/fetcher.cpython-312.pyc
 D finradar/market/__pycache__/__init__.cpython-312.pyc
 D finradar/market/__pycache__/tracker.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/__init__.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/crypto.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/futures.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/github.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/nitter_rss.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/precious_metal.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/social_config.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/stock_cn.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/twitter.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/wechat_article.cpython-312.pyc
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/nitter_rss.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/stock_cn.py
 M finradar/market/fetcher/wechat_article.py
 D finradar/market/models/__pycache__/__init__.cpython-312.pyc
 D finradar/market/models/__pycache__/market_data.cpython-312.pyc
 M finradar/market/tracker.py
 D finradar/notification/__pycache__/__init__.cpython-312.pyc
 D finradar/notification/__pycache__/batch.cpython-312.pyc
 D finradar/notification/__pycache__/dispatcher.cpython-312.pyc
 D finradar/notification/__pycache__/formatters.cpython-312.pyc
 D finradar/notification/__pycache__/push_manager.cpython-312.pyc
 D finradar/notification/__pycache__/renderer.cpython-312.pyc
 D finradar/notification/__pycache__/senders.cpython-312.pyc
 D finradar/notification/__pycache__/splitter.cpython-312.pyc
 D finradar/report/__pycache__/__init__.cpython-312.pyc
 D finradar/report/__pycache__/formatter.cpython-312.pyc
 D finradar/report/__pycache__/generator.cpython-312.pyc
 D finradar/report/__pycache__/helpers.cpython-312.pyc
 D finradar/report/__pycache__/html.cpython-312.pyc
 D finradar/storage/__pycache__/__init__.cpython-312.pyc
 D finradar/storage/__pycache__/base.cpython-312.pyc
 D finradar/storage/__pycache__/local.cpython-312.pyc
 D finradar/storage/__pycache__/manager.cpython-312.pyc
 D finradar/storage/__pycache__/remote.cpython-312.pyc
 D finradar/storage/__pycache__/sqlite_mixin.cpython-312.pyc
 D finradar/utils/__pycache__/__init__.cpython-312.pyc
 D finradar/utils/__pycache__/time.cpython-312.pyc
 D finradar/utils/__pycache__/url.cpython-312.pyc
 M index.html
 D mcp_server/__pycache__/__init__.cpython-312.pyc
 D mcp_server/__pycache__/server.cpython-312.pyc
 D mcp_server/services/__pycache__/__init__.cpython-312.pyc
 D mcp_server/services/__pycache__/cache_service.cpython-312.pyc
 D mcp_server/services/__pycache__/data_service.cpython-312.pyc
 D mcp_server/services/__pycache__/parser_service.cpython-312.pyc
 D mcp_server/tools/__pycache__/__init__.cpython-312.pyc
 D mcp_server/tools/__pycache__/analytics.cpython-312.pyc
 D mcp_server/tools/__pycache__/config_mgmt.cpython-312.pyc
 D mcp_server/tools/__pycache__/data_query.cpython-312.pyc
 D mcp_server/tools/__pycache__/search_tools.cpython-312.pyc
 D mcp_server/tools/__pycache__/storage_sync.cpython-312.pyc
 D mcp_server/tools/__pycache__/system.cpython-312.pyc
 D mcp_server/utils/__pycache__/__init__.cpython-312.pyc
 D mcp_server/utils/__pycache__/date_parser.cpython-312.pyc
 D mcp_server/utils/__pycache__/errors.cpython-312.pyc
 D mcp_server/utils/__pycache__/validators.cpython-312.pyc
 D output/debug/test_follow_cache.json
 D output/debug/twitter_account_health_full.json
 D output/debug/twitter_brief_output_20260225_070933.md
 D output/debug/twitter_fetch_20260225_060603.json
 D output/debug/twitter_fetch_20260225_060603.md
 D output/debug/twitter_fetch_20260225_070933.json
 D output/debug/twitter_fetch_20260225_151602.json
 D output/debug/twitter_fetch_20260225_151602.md
 D output/debug/twitter_fetch_20260225_152228.json
 D output/debug/twitter_fetch_20260225_152331.json
 D output/debug/twitter_fetch_20260225_153839.json
 D output/debug/twitter_fetch_20260225_153941.json
 D output/debug/twitter_fetch_20260225_154313.json
 D output/debug/twitter_fetch_live_20260225_090836.json
 D output/debug/twitter_fetch_live_20260225_090836.md
 D output/debug/twitter_io_bundle_20260225_070933.md
 D output/debug/twitter_io_bundle_20260225_151602.md
 D output/debug/twitter_missing_accounts_20260225_evening.json
 D output/debug/twitter_missing_accounts_live_probe_20260225_evening.json
 D output/debug/twitter_output_20260225_151602.md
 D output/debug/twitter_profile_probe_slow.json
 D output/debug/twitter_prompt_20260225_070933.md
 D output/debug/twitter_prompt_20260225_151602.md
 D output/debug/twitter_replacement_probe_20260225_085910.json
 D output/debug/twitter_replacement_probe_20260225_085948.json
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-25/20-02.html
?? output/html/2026-02-25/20-32.html
?? output/html/2026-02-25/21-02.html
?? output/html/2026-02-25/21-32.html
?? output/html/2026-02-25/22-02.html
?? output/html/2026-02-25/22-32.html
?? output/html/2026-02-25/23-01.html
?? output/html/2026-02-25/23-31.html
?? output/html/2026-02-26/
?? output/html/2026-02-27/
?? output/market/market_data_20260226.json
?? output/market/market_data_20260226_evening.json
?? output/market/market_data_20260226_morning.json
?? output/market/market_data_20260227.json
?? output/market/market_data_20260227_morning.json
?? output/market/market_report_20260226.txt
?? output/market/market_report_20260226_evening.txt
?? output/market/market_report_20260226_morning.txt
?? output/market/market_report_20260227.txt
?? output/market/market_report_20260227_morning.txt
?? output/news/2026-02-26.db
?? output/news/2026-02-27.db
?? output/report/daily_20260225_evening.md
?? output/report/daily_20260226_evening.md
?? output/report/daily_20260226_morning.md
?? output/report/daily_20260227_morning.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/rss/2026-02-26.db
?? output/rss/2026-02-27.db
?? output/state/
?? output/twitter/report_used_tweets.jsonl
?? "\345\267\245\344\275\234\346\265\201.md"
?? "\346\250\241\346\235\277.md"
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

## 2026-02-27 11:05:59 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260227 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 D finradar/__pycache__/__init__.cpython-312.pyc
 D finradar/__pycache__/__main__.cpython-312.pyc
 D finradar/__pycache__/context.cpython-312.pyc
 D finradar/ai/__pycache__/__init__.cpython-312.pyc
 D finradar/ai/__pycache__/analyzer.cpython-312.pyc
 D finradar/ai/__pycache__/client.cpython-312.pyc
 D finradar/ai/__pycache__/formatter.cpython-312.pyc
 D finradar/ai/__pycache__/translator.cpython-312.pyc
 D finradar/core/__pycache__/__init__.cpython-312.pyc
 D finradar/core/__pycache__/analyzer.cpython-312.pyc
 D finradar/core/__pycache__/config.cpython-312.pyc
 D finradar/core/__pycache__/data.cpython-312.pyc
 D finradar/core/__pycache__/frequency.cpython-312.pyc
 D finradar/core/__pycache__/loader.cpython-312.pyc
 D finradar/crawler/__pycache__/__init__.cpython-312.pyc
 D finradar/crawler/__pycache__/fetcher.cpython-312.pyc
 D finradar/market/__pycache__/__init__.cpython-312.pyc
 D finradar/market/__pycache__/tracker.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/__init__.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/crypto.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/futures.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/github.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/nitter_rss.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/precious_metal.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/social_config.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/stock_cn.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/twitter.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/wechat_article.cpython-312.pyc
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/nitter_rss.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/stock_cn.py
 M finradar/market/fetcher/wechat_article.py
 D finradar/market/models/__pycache__/__init__.cpython-312.pyc
 D finradar/market/models/__pycache__/market_data.cpython-312.pyc
 M finradar/market/tracker.py
 D finradar/notification/__pycache__/__init__.cpython-312.pyc
 D finradar/notification/__pycache__/batch.cpython-312.pyc
 D finradar/notification/__pycache__/dispatcher.cpython-312.pyc
 D finradar/notification/__pycache__/formatters.cpython-312.pyc
 D finradar/notification/__pycache__/push_manager.cpython-312.pyc
 D finradar/notification/__pycache__/renderer.cpython-312.pyc
 D finradar/notification/__pycache__/senders.cpython-312.pyc
 D finradar/notification/__pycache__/splitter.cpython-312.pyc
 D finradar/report/__pycache__/__init__.cpython-312.pyc
 D finradar/report/__pycache__/formatter.cpython-312.pyc
 D finradar/report/__pycache__/generator.cpython-312.pyc
 D finradar/report/__pycache__/helpers.cpython-312.pyc
 D finradar/report/__pycache__/html.cpython-312.pyc
 D finradar/storage/__pycache__/__init__.cpython-312.pyc
 D finradar/storage/__pycache__/base.cpython-312.pyc
 D finradar/storage/__pycache__/local.cpython-312.pyc
 D finradar/storage/__pycache__/manager.cpython-312.pyc
 D finradar/storage/__pycache__/remote.cpython-312.pyc
 D finradar/storage/__pycache__/sqlite_mixin.cpython-312.pyc
 D finradar/utils/__pycache__/__init__.cpython-312.pyc
 D finradar/utils/__pycache__/time.cpython-312.pyc
 D finradar/utils/__pycache__/url.cpython-312.pyc
 M index.html
 D mcp_server/__pycache__/__init__.cpython-312.pyc
 D mcp_server/__pycache__/server.cpython-312.pyc
 D mcp_server/services/__pycache__/__init__.cpython-312.pyc
 D mcp_server/services/__pycache__/cache_service.cpython-312.pyc
 D mcp_server/services/__pycache__/data_service.cpython-312.pyc
 D mcp_server/services/__pycache__/parser_service.cpython-312.pyc
 D mcp_server/tools/__pycache__/__init__.cpython-312.pyc
 D mcp_server/tools/__pycache__/analytics.cpython-312.pyc
 D mcp_server/tools/__pycache__/config_mgmt.cpython-312.pyc
 D mcp_server/tools/__pycache__/data_query.cpython-312.pyc
 D mcp_server/tools/__pycache__/search_tools.cpython-312.pyc
 D mcp_server/tools/__pycache__/storage_sync.cpython-312.pyc
 D mcp_server/tools/__pycache__/system.cpython-312.pyc
 D mcp_server/utils/__pycache__/__init__.cpython-312.pyc
 D mcp_server/utils/__pycache__/date_parser.cpython-312.pyc
 D mcp_server/utils/__pycache__/errors.cpython-312.pyc
 D mcp_server/utils/__pycache__/validators.cpython-312.pyc
 D output/debug/test_follow_cache.json
 D output/debug/twitter_account_health_full.json
 D output/debug/twitter_brief_output_20260225_070933.md
 D output/debug/twitter_fetch_20260225_060603.json
 D output/debug/twitter_fetch_20260225_060603.md
 D output/debug/twitter_fetch_20260225_070933.json
 D output/debug/twitter_fetch_20260225_151602.json
 D output/debug/twitter_fetch_20260225_151602.md
 D output/debug/twitter_fetch_20260225_152228.json
 D output/debug/twitter_fetch_20260225_152331.json
 D output/debug/twitter_fetch_20260225_153839.json
 D output/debug/twitter_fetch_20260225_153941.json
 D output/debug/twitter_fetch_20260225_154313.json
 D output/debug/twitter_fetch_live_20260225_090836.json
 D output/debug/twitter_fetch_live_20260225_090836.md
 D output/debug/twitter_io_bundle_20260225_070933.md
 D output/debug/twitter_io_bundle_20260225_151602.md
 D output/debug/twitter_missing_accounts_20260225_evening.json
 D output/debug/twitter_missing_accounts_live_probe_20260225_evening.json
 D output/debug/twitter_output_20260225_151602.md
 D output/debug/twitter_profile_probe_slow.json
 D output/debug/twitter_prompt_20260225_070933.md
 D output/debug/twitter_prompt_20260225_151602.md
 D output/debug/twitter_replacement_probe_20260225_085910.json
 D output/debug/twitter_replacement_probe_20260225_085948.json
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-25/20-02.html
?? output/html/2026-02-25/20-32.html
?? output/html/2026-02-25/21-02.html
?? output/html/2026-02-25/21-32.html
?? output/html/2026-02-25/22-02.html
?? output/html/2026-02-25/22-32.html
?? output/html/2026-02-25/23-01.html
?? output/html/2026-02-25/23-31.html
?? output/html/2026-02-26/
?? output/html/2026-02-27/
?? output/market/market_data_20260226.json
?? output/market/market_data_20260226_evening.json
?? output/market/market_data_20260226_morning.json
?? output/market/market_data_20260227.json
?? output/market/market_data_20260227_morning.json
?? output/market/market_report_20260226.txt
?? output/market/market_report_20260226_evening.txt
?? output/market/market_report_20260226_morning.txt
?? output/market/market_report_20260227.txt
?? output/market/market_report_20260227_morning.txt
?? output/news/2026-02-26.db
?? output/news/2026-02-27.db
?? output/report/daily_20260225_evening.md
?? output/report/daily_20260226_evening.md
?? output/report/daily_20260226_morning.md
?? output/report/daily_20260227_morning.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/rss/2026-02-26.db
?? output/rss/2026-02-27.db
?? output/state/
?? output/twitter/report_used_tweets.jsonl
?? "\345\267\245\344\275\234\346\265\201.md"
?? "\346\250\241\346\235\277.md"
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

## 2026-02-27 11:13:42 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260227 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 D finradar/__pycache__/__init__.cpython-312.pyc
 D finradar/__pycache__/__main__.cpython-312.pyc
 D finradar/__pycache__/context.cpython-312.pyc
 D finradar/ai/__pycache__/__init__.cpython-312.pyc
 D finradar/ai/__pycache__/analyzer.cpython-312.pyc
 D finradar/ai/__pycache__/client.cpython-312.pyc
 D finradar/ai/__pycache__/formatter.cpython-312.pyc
 D finradar/ai/__pycache__/translator.cpython-312.pyc
 D finradar/core/__pycache__/__init__.cpython-312.pyc
 D finradar/core/__pycache__/analyzer.cpython-312.pyc
 D finradar/core/__pycache__/config.cpython-312.pyc
 D finradar/core/__pycache__/data.cpython-312.pyc
 D finradar/core/__pycache__/frequency.cpython-312.pyc
 D finradar/core/__pycache__/loader.cpython-312.pyc
 D finradar/crawler/__pycache__/__init__.cpython-312.pyc
 D finradar/crawler/__pycache__/fetcher.cpython-312.pyc
 D finradar/market/__pycache__/__init__.cpython-312.pyc
 D finradar/market/__pycache__/tracker.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/__init__.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/crypto.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/futures.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/github.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/nitter_rss.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/precious_metal.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/social_config.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/stock_cn.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/twitter.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/wechat_article.cpython-312.pyc
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/nitter_rss.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/stock_cn.py
 M finradar/market/fetcher/wechat_article.py
 D finradar/market/models/__pycache__/__init__.cpython-312.pyc
 D finradar/market/models/__pycache__/market_data.cpython-312.pyc
 M finradar/market/tracker.py
 D finradar/notification/__pycache__/__init__.cpython-312.pyc
 D finradar/notification/__pycache__/batch.cpython-312.pyc
 D finradar/notification/__pycache__/dispatcher.cpython-312.pyc
 D finradar/notification/__pycache__/formatters.cpython-312.pyc
 D finradar/notification/__pycache__/push_manager.cpython-312.pyc
 D finradar/notification/__pycache__/renderer.cpython-312.pyc
 D finradar/notification/__pycache__/senders.cpython-312.pyc
 D finradar/notification/__pycache__/splitter.cpython-312.pyc
 D finradar/report/__pycache__/__init__.cpython-312.pyc
 D finradar/report/__pycache__/formatter.cpython-312.pyc
 D finradar/report/__pycache__/generator.cpython-312.pyc
 D finradar/report/__pycache__/helpers.cpython-312.pyc
 D finradar/report/__pycache__/html.cpython-312.pyc
 D finradar/storage/__pycache__/__init__.cpython-312.pyc
 D finradar/storage/__pycache__/base.cpython-312.pyc
 D finradar/storage/__pycache__/local.cpython-312.pyc
 D finradar/storage/__pycache__/manager.cpython-312.pyc
 D finradar/storage/__pycache__/remote.cpython-312.pyc
 D finradar/storage/__pycache__/sqlite_mixin.cpython-312.pyc
 D finradar/utils/__pycache__/__init__.cpython-312.pyc
 D finradar/utils/__pycache__/time.cpython-312.pyc
 D finradar/utils/__pycache__/url.cpython-312.pyc
 M index.html
 D mcp_server/__pycache__/__init__.cpython-312.pyc
 D mcp_server/__pycache__/server.cpython-312.pyc
 D mcp_server/services/__pycache__/__init__.cpython-312.pyc
 D mcp_server/services/__pycache__/cache_service.cpython-312.pyc
 D mcp_server/services/__pycache__/data_service.cpython-312.pyc
 D mcp_server/services/__pycache__/parser_service.cpython-312.pyc
 D mcp_server/tools/__pycache__/__init__.cpython-312.pyc
 D mcp_server/tools/__pycache__/analytics.cpython-312.pyc
 D mcp_server/tools/__pycache__/config_mgmt.cpython-312.pyc
 D mcp_server/tools/__pycache__/data_query.cpython-312.pyc
 D mcp_server/tools/__pycache__/search_tools.cpython-312.pyc
 D mcp_server/tools/__pycache__/storage_sync.cpython-312.pyc
 D mcp_server/tools/__pycache__/system.cpython-312.pyc
 D mcp_server/utils/__pycache__/__init__.cpython-312.pyc
 D mcp_server/utils/__pycache__/date_parser.cpython-312.pyc
 D mcp_server/utils/__pycache__/errors.cpython-312.pyc
 D mcp_server/utils/__pycache__/validators.cpython-312.pyc
 D output/debug/test_follow_cache.json
 D output/debug/twitter_account_health_full.json
 D output/debug/twitter_brief_output_20260225_070933.md
 D output/debug/twitter_fetch_20260225_060603.json
 D output/debug/twitter_fetch_20260225_060603.md
 D output/debug/twitter_fetch_20260225_070933.json
 D output/debug/twitter_fetch_20260225_151602.json
 D output/debug/twitter_fetch_20260225_151602.md
 D output/debug/twitter_fetch_20260225_152228.json
 D output/debug/twitter_fetch_20260225_152331.json
 D output/debug/twitter_fetch_20260225_153839.json
 D output/debug/twitter_fetch_20260225_153941.json
 D output/debug/twitter_fetch_20260225_154313.json
 D output/debug/twitter_fetch_live_20260225_090836.json
 D output/debug/twitter_fetch_live_20260225_090836.md
 D output/debug/twitter_io_bundle_20260225_070933.md
 D output/debug/twitter_io_bundle_20260225_151602.md
 D output/debug/twitter_missing_accounts_20260225_evening.json
 D output/debug/twitter_missing_accounts_live_probe_20260225_evening.json
 D output/debug/twitter_output_20260225_151602.md
 D output/debug/twitter_profile_probe_slow.json
 D output/debug/twitter_prompt_20260225_070933.md
 D output/debug/twitter_prompt_20260225_151602.md
 D output/debug/twitter_replacement_probe_20260225_085910.json
 D output/debug/twitter_replacement_probe_20260225_085948.json
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-25/20-02.html
?? output/html/2026-02-25/20-32.html
?? output/html/2026-02-25/21-02.html
?? output/html/2026-02-25/21-32.html
?? output/html/2026-02-25/22-02.html
?? output/html/2026-02-25/22-32.html
?? output/html/2026-02-25/23-01.html
?? output/html/2026-02-25/23-31.html
?? output/html/2026-02-26/
?? output/html/2026-02-27/
?? output/market/market_data_20260226.json
?? output/market/market_data_20260226_evening.json
?? output/market/market_data_20260226_morning.json
?? output/market/market_data_20260227.json
?? output/market/market_data_20260227_morning.json
?? output/market/market_report_20260226.txt
?? output/market/market_report_20260226_evening.txt
?? output/market/market_report_20260226_morning.txt
?? output/market/market_report_20260227.txt
?? output/market/market_report_20260227_morning.txt
?? output/news/2026-02-26.db
?? output/news/2026-02-27.db
?? output/report/daily_20260225_evening.md
?? output/report/daily_20260226_evening.md
?? output/report/daily_20260226_morning.md
?? output/report/daily_20260227_morning.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/rss/2026-02-26.db
?? output/rss/2026-02-27.db
?? output/state/
?? output/twitter/report_used_tweets.jsonl
?? "\345\267\245\344\275\234\346\265\201.md"
?? "\346\250\241\346\235\277.md"
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

## 2026-02-27 11:21:19 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260227 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 D finradar/__pycache__/__init__.cpython-312.pyc
 D finradar/__pycache__/__main__.cpython-312.pyc
 D finradar/__pycache__/context.cpython-312.pyc
 D finradar/ai/__pycache__/__init__.cpython-312.pyc
 D finradar/ai/__pycache__/analyzer.cpython-312.pyc
 D finradar/ai/__pycache__/client.cpython-312.pyc
 D finradar/ai/__pycache__/formatter.cpython-312.pyc
 D finradar/ai/__pycache__/translator.cpython-312.pyc
 D finradar/core/__pycache__/__init__.cpython-312.pyc
 D finradar/core/__pycache__/analyzer.cpython-312.pyc
 D finradar/core/__pycache__/config.cpython-312.pyc
 D finradar/core/__pycache__/data.cpython-312.pyc
 D finradar/core/__pycache__/frequency.cpython-312.pyc
 D finradar/core/__pycache__/loader.cpython-312.pyc
 D finradar/crawler/__pycache__/__init__.cpython-312.pyc
 D finradar/crawler/__pycache__/fetcher.cpython-312.pyc
 D finradar/market/__pycache__/__init__.cpython-312.pyc
 D finradar/market/__pycache__/tracker.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/__init__.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/crypto.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/futures.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/github.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/nitter_rss.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/precious_metal.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/social_config.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/stock_cn.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/twitter.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/wechat_article.cpython-312.pyc
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/nitter_rss.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/stock_cn.py
 M finradar/market/fetcher/wechat_article.py
 D finradar/market/models/__pycache__/__init__.cpython-312.pyc
 D finradar/market/models/__pycache__/market_data.cpython-312.pyc
 M finradar/market/tracker.py
 D finradar/notification/__pycache__/__init__.cpython-312.pyc
 D finradar/notification/__pycache__/batch.cpython-312.pyc
 D finradar/notification/__pycache__/dispatcher.cpython-312.pyc
 D finradar/notification/__pycache__/formatters.cpython-312.pyc
 D finradar/notification/__pycache__/push_manager.cpython-312.pyc
 D finradar/notification/__pycache__/renderer.cpython-312.pyc
 D finradar/notification/__pycache__/senders.cpython-312.pyc
 D finradar/notification/__pycache__/splitter.cpython-312.pyc
 D finradar/report/__pycache__/__init__.cpython-312.pyc
 D finradar/report/__pycache__/formatter.cpython-312.pyc
 D finradar/report/__pycache__/generator.cpython-312.pyc
 D finradar/report/__pycache__/helpers.cpython-312.pyc
 D finradar/report/__pycache__/html.cpython-312.pyc
 D finradar/storage/__pycache__/__init__.cpython-312.pyc
 D finradar/storage/__pycache__/base.cpython-312.pyc
 D finradar/storage/__pycache__/local.cpython-312.pyc
 D finradar/storage/__pycache__/manager.cpython-312.pyc
 D finradar/storage/__pycache__/remote.cpython-312.pyc
 D finradar/storage/__pycache__/sqlite_mixin.cpython-312.pyc
 D finradar/utils/__pycache__/__init__.cpython-312.pyc
 D finradar/utils/__pycache__/time.cpython-312.pyc
 D finradar/utils/__pycache__/url.cpython-312.pyc
 M index.html
 D mcp_server/__pycache__/__init__.cpython-312.pyc
 D mcp_server/__pycache__/server.cpython-312.pyc
 D mcp_server/services/__pycache__/__init__.cpython-312.pyc
 D mcp_server/services/__pycache__/cache_service.cpython-312.pyc
 D mcp_server/services/__pycache__/data_service.cpython-312.pyc
 D mcp_server/services/__pycache__/parser_service.cpython-312.pyc
 D mcp_server/tools/__pycache__/__init__.cpython-312.pyc
 D mcp_server/tools/__pycache__/analytics.cpython-312.pyc
 D mcp_server/tools/__pycache__/config_mgmt.cpython-312.pyc
 D mcp_server/tools/__pycache__/data_query.cpython-312.pyc
 D mcp_server/tools/__pycache__/search_tools.cpython-312.pyc
 D mcp_server/tools/__pycache__/storage_sync.cpython-312.pyc
 D mcp_server/tools/__pycache__/system.cpython-312.pyc
 D mcp_server/utils/__pycache__/__init__.cpython-312.pyc
 D mcp_server/utils/__pycache__/date_parser.cpython-312.pyc
 D mcp_server/utils/__pycache__/errors.cpython-312.pyc
 D mcp_server/utils/__pycache__/validators.cpython-312.pyc
 D output/debug/test_follow_cache.json
 D output/debug/twitter_account_health_full.json
 D output/debug/twitter_brief_output_20260225_070933.md
 D output/debug/twitter_fetch_20260225_060603.json
 D output/debug/twitter_fetch_20260225_060603.md
 D output/debug/twitter_fetch_20260225_070933.json
 D output/debug/twitter_fetch_20260225_151602.json
 D output/debug/twitter_fetch_20260225_151602.md
 D output/debug/twitter_fetch_20260225_152228.json
 D output/debug/twitter_fetch_20260225_152331.json
 D output/debug/twitter_fetch_20260225_153839.json
 D output/debug/twitter_fetch_20260225_153941.json
 D output/debug/twitter_fetch_20260225_154313.json
 D output/debug/twitter_fetch_live_20260225_090836.json
 D output/debug/twitter_fetch_live_20260225_090836.md
 D output/debug/twitter_io_bundle_20260225_070933.md
 D output/debug/twitter_io_bundle_20260225_151602.md
 D output/debug/twitter_missing_accounts_20260225_evening.json
 D output/debug/twitter_missing_accounts_live_probe_20260225_evening.json
 D output/debug/twitter_output_20260225_151602.md
 D output/debug/twitter_profile_probe_slow.json
 D output/debug/twitter_prompt_20260225_070933.md
 D output/debug/twitter_prompt_20260225_151602.md
 D output/debug/twitter_replacement_probe_20260225_085910.json
 D output/debug/twitter_replacement_probe_20260225_085948.json
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-25/20-02.html
?? output/html/2026-02-25/20-32.html
?? output/html/2026-02-25/21-02.html
?? output/html/2026-02-25/21-32.html
?? output/html/2026-02-25/22-02.html
?? output/html/2026-02-25/22-32.html
?? output/html/2026-02-25/23-01.html
?? output/html/2026-02-25/23-31.html
?? output/html/2026-02-26/
?? output/html/2026-02-27/
?? output/market/market_data_20260226.json
?? output/market/market_data_20260226_evening.json
?? output/market/market_data_20260226_morning.json
?? output/market/market_data_20260227.json
?? output/market/market_data_20260227_morning.json
?? output/market/market_report_20260226.txt
?? output/market/market_report_20260226_evening.txt
?? output/market/market_report_20260226_morning.txt
?? output/market/market_report_20260227.txt
?? output/market/market_report_20260227_morning.txt
?? output/news/2026-02-26.db
?? output/news/2026-02-27.db
?? output/report/daily_20260225_evening.md
?? output/report/daily_20260226_evening.md
?? output/report/daily_20260226_morning.md
?? output/report/daily_20260227_morning.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/rss/2026-02-26.db
?? output/rss/2026-02-27.db
?? output/state/
?? output/twitter/report_used_tweets.jsonl
?? "\345\267\245\344\275\234\346\265\201.md"
?? "\346\250\241\346\235\277.md"
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

## 2026-02-27 22:58:03 CST
- 分支: `main`
- 最新提交: `28ecd90`
- 当前意图: 生成20260227 morning 报告（with-ai）
- 下一步: 查看 output/report 结果并持续优化分板块结构与时效过滤规则
- 工作区状态:
```
 M README.local.md
 M config/config.yaml
 M docs/SESSION_CHECKPOINT.md
 D finradar/__pycache__/__init__.cpython-312.pyc
 D finradar/__pycache__/__main__.cpython-312.pyc
 D finradar/__pycache__/context.cpython-312.pyc
 D finradar/ai/__pycache__/__init__.cpython-312.pyc
 D finradar/ai/__pycache__/analyzer.cpython-312.pyc
 D finradar/ai/__pycache__/client.cpython-312.pyc
 D finradar/ai/__pycache__/formatter.cpython-312.pyc
 D finradar/ai/__pycache__/translator.cpython-312.pyc
 D finradar/core/__pycache__/__init__.cpython-312.pyc
 D finradar/core/__pycache__/analyzer.cpython-312.pyc
 D finradar/core/__pycache__/config.cpython-312.pyc
 D finradar/core/__pycache__/data.cpython-312.pyc
 D finradar/core/__pycache__/frequency.cpython-312.pyc
 D finradar/core/__pycache__/loader.cpython-312.pyc
 D finradar/crawler/__pycache__/__init__.cpython-312.pyc
 D finradar/crawler/__pycache__/fetcher.cpython-312.pyc
 D finradar/market/__pycache__/__init__.cpython-312.pyc
 D finradar/market/__pycache__/tracker.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/__init__.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/crypto.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/futures.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/github.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/nitter_rss.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/precious_metal.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/social_config.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/stock_cn.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/twitter.cpython-312.pyc
 D finradar/market/fetcher/__pycache__/wechat_article.cpython-312.pyc
 M finradar/market/fetcher/github.py
 M finradar/market/fetcher/nitter_rss.py
 M finradar/market/fetcher/social_config.py
 M finradar/market/fetcher/stock_cn.py
 M finradar/market/fetcher/wechat_article.py
 D finradar/market/models/__pycache__/__init__.cpython-312.pyc
 D finradar/market/models/__pycache__/market_data.cpython-312.pyc
 M finradar/market/tracker.py
 D finradar/notification/__pycache__/__init__.cpython-312.pyc
 D finradar/notification/__pycache__/batch.cpython-312.pyc
 D finradar/notification/__pycache__/dispatcher.cpython-312.pyc
 D finradar/notification/__pycache__/formatters.cpython-312.pyc
 D finradar/notification/__pycache__/push_manager.cpython-312.pyc
 D finradar/notification/__pycache__/renderer.cpython-312.pyc
 D finradar/notification/__pycache__/senders.cpython-312.pyc
 D finradar/notification/__pycache__/splitter.cpython-312.pyc
 D finradar/report/__pycache__/__init__.cpython-312.pyc
 D finradar/report/__pycache__/formatter.cpython-312.pyc
 D finradar/report/__pycache__/generator.cpython-312.pyc
 D finradar/report/__pycache__/helpers.cpython-312.pyc
 D finradar/report/__pycache__/html.cpython-312.pyc
 D finradar/storage/__pycache__/__init__.cpython-312.pyc
 D finradar/storage/__pycache__/base.cpython-312.pyc
 D finradar/storage/__pycache__/local.cpython-312.pyc
 D finradar/storage/__pycache__/manager.cpython-312.pyc
 D finradar/storage/__pycache__/remote.cpython-312.pyc
 D finradar/storage/__pycache__/sqlite_mixin.cpython-312.pyc
 D finradar/utils/__pycache__/__init__.cpython-312.pyc
 D finradar/utils/__pycache__/time.cpython-312.pyc
 D finradar/utils/__pycache__/url.cpython-312.pyc
 M index.html
 D mcp_server/__pycache__/__init__.cpython-312.pyc
 D mcp_server/__pycache__/server.cpython-312.pyc
 D mcp_server/services/__pycache__/__init__.cpython-312.pyc
 D mcp_server/services/__pycache__/cache_service.cpython-312.pyc
 D mcp_server/services/__pycache__/data_service.cpython-312.pyc
 D mcp_server/services/__pycache__/parser_service.cpython-312.pyc
 D mcp_server/tools/__pycache__/__init__.cpython-312.pyc
 D mcp_server/tools/__pycache__/analytics.cpython-312.pyc
 D mcp_server/tools/__pycache__/config_mgmt.cpython-312.pyc
 D mcp_server/tools/__pycache__/data_query.cpython-312.pyc
 D mcp_server/tools/__pycache__/search_tools.cpython-312.pyc
 D mcp_server/tools/__pycache__/storage_sync.cpython-312.pyc
 D mcp_server/tools/__pycache__/system.cpython-312.pyc
 D mcp_server/utils/__pycache__/__init__.cpython-312.pyc
 D mcp_server/utils/__pycache__/date_parser.cpython-312.pyc
 D mcp_server/utils/__pycache__/errors.cpython-312.pyc
 D mcp_server/utils/__pycache__/validators.cpython-312.pyc
 D output/debug/test_follow_cache.json
 D output/debug/twitter_account_health_full.json
 D output/debug/twitter_brief_output_20260225_070933.md
 D output/debug/twitter_fetch_20260225_060603.json
 D output/debug/twitter_fetch_20260225_060603.md
 D output/debug/twitter_fetch_20260225_070933.json
 D output/debug/twitter_fetch_20260225_151602.json
 D output/debug/twitter_fetch_20260225_151602.md
 D output/debug/twitter_fetch_20260225_152228.json
 D output/debug/twitter_fetch_20260225_152331.json
 D output/debug/twitter_fetch_20260225_153839.json
 D output/debug/twitter_fetch_20260225_153941.json
 D output/debug/twitter_fetch_20260225_154313.json
 D output/debug/twitter_fetch_live_20260225_090836.json
 D output/debug/twitter_fetch_live_20260225_090836.md
 D output/debug/twitter_io_bundle_20260225_070933.md
 D output/debug/twitter_io_bundle_20260225_151602.md
 D output/debug/twitter_missing_accounts_20260225_evening.json
 D output/debug/twitter_missing_accounts_live_probe_20260225_evening.json
 D output/debug/twitter_output_20260225_151602.md
 D output/debug/twitter_profile_probe_slow.json
 D output/debug/twitter_prompt_20260225_070933.md
 D output/debug/twitter_prompt_20260225_151602.md
 D output/debug/twitter_replacement_probe_20260225_085910.json
 D output/debug/twitter_replacement_probe_20260225_085948.json
 M output/html/latest/current.html
 M output/index.html
 M output/market/market_data_20260225.json
 M output/market/market_data_20260225_evening.json
 M output/market/market_report_20260225.txt
 M output/market/market_report_20260225_evening.txt
 M output/news/2026-02-25.db
 M output/rss/2026-02-25.db
 M output/twitter/follow_cache.json
 M scripts/generate_report.py
 M scripts/local.sh
 M scripts/push_to_notion.py
?? output/html/2026-02-25/20-02.html
?? output/html/2026-02-25/20-32.html
?? output/html/2026-02-25/21-02.html
?? output/html/2026-02-25/21-32.html
?? output/html/2026-02-25/22-02.html
?? output/html/2026-02-25/22-32.html
?? output/html/2026-02-25/23-01.html
?? output/html/2026-02-25/23-31.html
?? output/html/2026-02-26/
?? output/html/2026-02-27/
?? output/market/market_data_20260226.json
?? output/market/market_data_20260226_evening.json
?? output/market/market_data_20260226_morning.json
?? output/market/market_data_20260227.json
?? output/market/market_data_20260227_evening.json
?? output/market/market_data_20260227_morning.json
?? output/market/market_report_20260226.txt
?? output/market/market_report_20260226_evening.txt
?? output/market/market_report_20260226_morning.txt
?? output/market/market_report_20260227.txt
?? output/market/market_report_20260227_evening.txt
?? output/market/market_report_20260227_morning.txt
?? output/news/2026-02-26.db
?? output/news/2026-02-27.db
?? output/report/daily_20260225_evening.md
?? output/report/daily_20260226_evening.md
?? output/report/daily_20260226_morning.md
?? output/report/daily_20260227_evening.md
?? output/report/daily_20260227_morning.md
?? output/report/next_track_history.jsonl
?? output/report/next_track_state.json
?? output/rss/2026-02-26.db
?? output/rss/2026-02-27.db
?? output/state/
?? output/twitter/report_used_tweets.jsonl
?? "\345\267\245\344\275\234\346\265\201.md"
?? "\346\250\241\346\235\277.md"
```
- 最近提交:
```
28ecd90 1
3971735 chore(twitter): remove public nitter instance references
b79ff84 feat(market): integrate Yahoo Finance global stock overview
44e502c feat(report): sanitize AI preambles and auto-checkpoint report runs
b2ae0c4 docs(process): checkpoint after adding local workflow commands
207a292 feat(process): add local.sh commands for checkpoint and auto-commit
ebee66e docs(process): checkpoint after auto-commit safety update
1128610 fix(process): make auto-commit require explicit include by default
```

