# finradar（本地优先版）

这个仓库目前定位为：
- 主程序在本机/服务器本地运行（推荐）
- Docker 作为可选方案（用于复现或迁移）
- AI 摘要固定使用 DeepSeek API

## 1. 2 行快速部署（推荐）

```bash
./scripts/local.sh setup
./scripts/local.sh cron-install
```

执行后会安装依赖并写入本地 `crontab`：
- 每 30 分钟：`market + news`
- 每天 08:00：`social + 早报`
- 每天 20:00：`social + 晚报`

## 2. 快速功能测试

```bash
./scripts/local.sh run social
./scripts/local.sh report evening
# 指定联网检索关键词（逗号分隔）
./.venv/bin/python scripts/generate_report.py --type evening --keywords "A股,美股,比特币,AI芯片"
```

## 3. DeepSeek 配置

默认读取 `config/config.yaml` 的：
- `ai.api_key`
- `ai.model`（支持 `deepseek/deepseek-chat`，会自动归一化）
- `ai.api_base`（为空则默认 `https://api.deepseek.com`）

也可用环境变量覆盖：
- `DEEPSEEK_API_KEY`
- `DEEPSEEK_MODEL`
- `DEEPSEEK_API_BASE`

## 4. 微信公众号抓取说明（需要登录）

你需要先让 `wechat-article-exporter` 有有效登录态，否则会返回空数据。

可选启动（Docker）：
```bash
./run.sh start all
```

然后浏览器访问：
- `http://<你的服务器IP>/`（当前 `docker/.env` 默认映射到 80）
- 或 `http://127.0.0.1:${WECHAT_EXPORTER_PORT}`

说明：`docker/docker-compose-unified.yml` 已默认启用 HTTP 兼容登录镜像（移除登录 cookie 的 `Secure`），
用于支持 `http://公网IP` 直接扫码登录。

扫码登录后，把 auth key 写入：
- `config/config.yaml` 的 `wechat.auth_key`
或环境变量：
- `WECHAT_AUTH_KEY`

## 5. Notion 自动写入（早晚报子页面）

先配置 Notion Token 和父页面（只需一次）：
```bash
./scripts/local.sh notion-config "<YOUR_NOTION_TOKEN>" "https://www.notion.so/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

手动推送某天报告：
```bash
./scripts/local.sh notion-push morning 20260209
./scripts/local.sh notion-push evening 20260209
```

说明：
- 配置保存在项目根目录 `.notion.env`（已加入 `.gitignore`）
- `cron-install` 后会在每天 08:00 / 20:00 自动执行 Notion 子页面写入

## 6. Docker 可选用法

```bash
./run.sh build
./run.sh start all
```

只启动主服务（不拉起社交源容器）：
```bash
./run.sh start all --no-sources
```

## 7. 开发连续性（跨会话）

```bash
# 记录当前进展与下一步，写入 docs/SESSION_CHECKPOINT.md
./scripts/dev_checkpoint.sh "当前目标" "下一步"
```

建议先阅读：
- `docs/开发流程与会话交接.md`
- `docs/SESSION_CHECKPOINT.md`

## 8. 当前状态

- Twitter：已支持“关注账号 + 热门讨论（关键词搜索）”合并抓取
- 微信：已支持“关注公众号 + 热门文章”合并抓取，支持正文采集
- 报告：早报/晚报按 12 小时窗口汇总，并调用 DeepSeek 生成结构化摘要（Summary + 分段拆解）
- 报告：支持联网检索补充（Google News RSS），并自动衔接上一期报告上下文
- 推送：已支持 Notion 子页面自动写入（08:00 / 20:00），飞书可按原配置继续使用
