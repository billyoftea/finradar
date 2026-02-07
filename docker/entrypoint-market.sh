#!/bin/bash
set -e

echo "🚀 FinRadar 市场追踪服务启动"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📅 时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "🕐 时区: ${TZ:-Asia/Shanghai}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 保存环境变量供 cron 使用
env >> /etc/environment

case "${RUN_MODE:-cron}" in
"once")
    echo "🔄 单次执行模式"
    echo ""
    echo "📊 执行 fin_module (金融市场+Twitter+微信)..."
    /usr/local/bin/python -m fin_module
    echo ""
    echo "🔥 执行 trendradar (热榜新闻)..."
    /usr/local/bin/python -m trendradar
    ;;
"cron")
    # 默认定时: 每30分钟执行
    CRON_SCHEDULE="${CRON_SCHEDULE:-*/30 * * * *}"
    
    # 生成 crontab - 同时运行两个模块
    cat > /tmp/crontab <<EOF
${CRON_SCHEDULE} cd /app && /usr/local/bin/python -m fin_module >> /var/log/market.log 2>&1 && /usr/local/bin/python -m trendradar >> /var/log/trendradar.log 2>&1
EOF
    
    echo "📅 定时任务配置:"
    echo "   调度: ${CRON_SCHEDULE}"
    echo "   任务1: fin_module (金融市场+Twitter+微信)"
    echo "   任务2: trendradar (热榜新闻)"
    cat /tmp/crontab

    if ! /usr/local/bin/supercronic -test /tmp/crontab; then
        echo "❌ crontab 格式验证失败"
        exit 1
    fi

    # 立即执行一次（如果配置了）
    if [ "${IMMEDIATE_RUN:-true}" = "true" ]; then
        echo ""
        echo "▶️ 立即执行一次..."
        echo "📊 执行 fin_module..."
        /usr/local/bin/python -m fin_module || true
        echo ""
        echo "🔥 执行 trendradar..."
        /usr/local/bin/python -m trendradar || true
    fi

    echo ""
    echo "⏰ 启动定时任务: ${CRON_SCHEDULE}"
    echo "🎯 supercronic 将作为 PID 1 运行"
    echo ""
    
    exec /usr/local/bin/supercronic -passthrough-logs /tmp/crontab
    ;;
*)
    # 执行传入的命令
    exec "$@"
    ;;
esac
