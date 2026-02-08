#!/bin/bash
set -e

echo "🚀 FinRadar 数据服务启动"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📅 时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "🕐 时区: ${TZ:-Asia/Shanghai}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 保存环境变量供 cron 使用
env >> /etc/environment

PY="/usr/local/bin/python"

case "${RUN_MODE:-cron}" in
"once")
    echo "🔄 单次执行模式"
    echo ""
    echo "📊 执行市场数据抓取..."
    $PY -m fin_module --mode market
    echo ""
    echo "🔥 执行热榜新闻抓取..."
    $PY -m trendradar
    echo ""
    echo "📱🐦 执行 Twitter + 微信抓取..."
    $PY -m fin_module --mode social
    ;;
"cron")
    # ┌──────────────────────────────────────────────┐
    # │  调度策略:                                    │
    # │  • 市场数据 + NewsNow热榜: 每30分钟           │
    # │  • Twitter + 微信公众号:   07:00 / 19:00      │
    # │  早报覆盖 19:00→07:00，晚报覆盖 07:00→19:00   │
    # └──────────────────────────────────────────────┘

    cat > /tmp/crontab <<'EOF'
# 每30分钟: 市场数据 + NewsNow热榜
*/30 * * * * cd /app && /usr/local/bin/python -m fin_module --mode market >> /var/log/market.log 2>&1 && /usr/local/bin/python -m trendradar >> /var/log/trendradar.log 2>&1

# 每天 07:00: 抓取 Twitter + 微信 (早报素材，覆盖过去12小时 19:00→07:00)
# 抓取完成后自动生成早报
0 7 * * * cd /app && /usr/local/bin/python -m fin_module --mode social >> /var/log/social.log 2>&1 && /usr/local/bin/python scripts/generate_report.py --type morning >> /var/log/report.log 2>&1

# 每天 19:00: 抓取 Twitter + 微信 (晚报素材，覆盖过去12小时 07:00→19:00)
# 抓取完成后自动生成晚报
0 19 * * * cd /app && /usr/local/bin/python -m fin_module --mode social >> /var/log/social.log 2>&1 && /usr/local/bin/python scripts/generate_report.py --type evening >> /var/log/report.log 2>&1
EOF

    echo "📅 定时任务配置:"
    echo "   ⏱  每30分钟  → 市场数据 + NewsNow热榜"
    echo "   🌅 每奩07:00 → Twitter + 微信 + 生成早报"
    echo "   🌇 每奩19:00 → Twitter + 微信 + 生成晚报"
    echo ""

    if ! /usr/local/bin/supercronic -test /tmp/crontab; then
        echo "❌ crontab 格式验证失败"
        exit 1
    fi

    # 立即执行一次市场数据
    if [ "${IMMEDIATE_RUN:-true}" = "true" ]; then
        echo ""
        echo "▶️ 立即执行一次市场数据..."
        $PY -m fin_module --mode market || true
        echo ""
        echo "🔥 执行热榜新闻抓取..."
        $PY -m trendradar || true
    fi

    echo ""
    echo "⏰ 启动定时任务..."
    exec /usr/local/bin/supercronic -passthrough-logs /tmp/crontab
    ;;
*)
    exec "$@"
    ;;
esac
