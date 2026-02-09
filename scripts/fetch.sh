#!/bin/bash
# finradar 每日数据抓取脚本
# 使用方法:
#   ./scripts/fetch.sh           # 抓取全部 (all)
#   ./scripts/fetch.sh all       # 同上
#   ./scripts/fetch.sh news      # 仅热榜新闻
#   ./scripts/fetch.sh market    # 仅金融市场
#   ./scripts/fetch.sh social    # 仅社交媒体
#   ./scripts/fetch.sh report evening  # 生成晚报 (可选 morning/evening/auto)

set -euo pipefail

cd "$(dirname "$0")/.." || exit 1

if [ "${1:-all}" = "report" ]; then
    TYPE="${2:-auto}"
    shift 2 || true
    ./scripts/local.sh report "$TYPE" "${1:-}"
    exit 0
fi

MODE="${1:-all}"
./scripts/local.sh run "$MODE"
