#!/bin/bash
# FinRadar 每日数据抓取脚本
# 使用方法:
#   ./scripts/fetch.sh           # 抓取所有数据
#   ./scripts/fetch.sh -t        # 仅 Twitter
#   ./scripts/fetch.sh -w        # 仅微信公众号
#   ./scripts/fetch.sh -m        # 仅金融市场
#   ./scripts/fetch.sh -r        # 仅热榜新闻
#   ./scripts/fetch.sh -t -w     # Twitter + 微信

cd "$(dirname "$0")/.." || exit 1

# 激活 conda 环境（如果存在）
if command -v conda &> /dev/null; then
    eval "$(conda shell.bash hook)"
    conda activate base 2>/dev/null
fi

# 运行 Python 脚本
python scripts/daily_fetch.py "$@"
