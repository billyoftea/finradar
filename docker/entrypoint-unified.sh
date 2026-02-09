#!/bin/bash
set -e

echo "🚀 finradar 统一服务启动"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📅 时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "🕐 时区: ${TZ:-Asia/Shanghai}"
echo "🎯 任务模式: ${TASK_MODE:-all}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 保存环境变量供 cron 使用
env >> /etc/environment

PY="/usr/local/bin/python"

# TASK_MODE 决定跑哪些功能
# all: 全部 (news + market + social)
# news: 仅热榜新闻
# market: 仅市场数据
# social: 仅社交媒体
TASK_MODE="${TASK_MODE:-all}"

case "${RUN_MODE:-cron}" in
"once")
    echo "🔄 单次执行模式 [${TASK_MODE}]"
    echo ""
    $PY -m finradar --mode "${TASK_MODE}"
    ;;
"cron")
    # ┌──────────────────────────────────────────────┐
    # │  调度策略:                                    │
    # │  • 市场数据 + 热榜新闻: 每30分钟              │
    # │  • 社交媒体:           08:00 / 20:00          │
    # └──────────────────────────────────────────────┘

    case "${TASK_MODE}" in
    "all")
        cat > /tmp/crontab <<'EOF'
# 每30分钟: 市场数据 + 热榜新闻
*/30 * * * * cd /app && /usr/local/bin/python -m finradar --mode market >> /var/log/market.log 2>&1 && /usr/local/bin/python -m finradar --mode news >> /var/log/finradar.log 2>&1

# 每天 08:00: 抓取社交媒体 + 生成早报
0 8 * * * cd /app && /usr/local/bin/python -m finradar --mode social >> /var/log/social.log 2>&1 && /usr/local/bin/python scripts/generate_report.py --type morning >> /var/log/report.log 2>&1

# 每天 20:00: 抓取社交媒体 + 生成晚报
0 20 * * * cd /app && /usr/local/bin/python -m finradar --mode social >> /var/log/social.log 2>&1 && /usr/local/bin/python scripts/generate_report.py --type evening >> /var/log/report.log 2>&1
EOF
        echo "📅 定时任务:"
        echo "   ⏱  每30分钟  → 市场数据 + 热榜新闻"
        echo "   🌅 每天08:00 → 社交媒体 + 早报"
        echo "   🌇 每天20:00 → 社交媒体 + 晚报"
        ;;
    "news")
        echo "${CRON_SCHEDULE:-*/30 * * * *} cd /app && /usr/local/bin/python -m finradar --mode news >> /var/log/finradar.log 2>&1" > /tmp/crontab
        echo "📅 定时任务: 每 ${CRON_SCHEDULE:-*/30 * * * *} → 热榜新闻"
        ;;
    "market")
        echo "${CRON_SCHEDULE:-*/30 * * * *} cd /app && /usr/local/bin/python -m finradar --mode market >> /var/log/market.log 2>&1" > /tmp/crontab
        echo "📅 定时任务: 每 ${CRON_SCHEDULE:-*/30 * * * *} → 市场数据"
        ;;
    "social")
        cat > /tmp/crontab <<'EOF'
0 8 * * * cd /app && /usr/local/bin/python -m finradar --mode social >> /var/log/social.log 2>&1 && /usr/local/bin/python scripts/generate_report.py --type morning >> /var/log/report.log 2>&1
0 20 * * * cd /app && /usr/local/bin/python -m finradar --mode social >> /var/log/social.log 2>&1 && /usr/local/bin/python scripts/generate_report.py --type evening >> /var/log/report.log 2>&1
EOF
        echo "📅 定时任务: 08:00 / 20:00 → 社交媒体 + 报告"
        ;;
    esac

    echo ""

    if ! /usr/local/bin/supercronic -test /tmp/crontab; then
        echo "❌ crontab 格式验证失败"
        exit 1
    fi

    # 立即执行一次
    if [ "${IMMEDIATE_RUN:-true}" = "true" ]; then
        echo "▶️ 立即执行一次 [${TASK_MODE}]..."
        $PY -m finradar --mode "${TASK_MODE}" || true
        echo ""
    fi

    # 启动 Web 服务器（如果配置了）
    if [ "${ENABLE_WEBSERVER:-false}" = "true" ]; then
        echo "🌐 启动 Web 服务器 (端口 ${WEBSERVER_PORT:-8080})..."
        $PY manage.py start_webserver &
    fi

    echo "⏰ 启动定时任务..."
    exec /usr/local/bin/supercronic -passthrough-logs /tmp/crontab
    ;;
*)
    exec "$@"
    ;;
esac
