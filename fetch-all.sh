#!/bin/bash
# FinRadar 一键抓取所有数据
# 快捷入口脚本

cd "$(dirname "$0")" || exit 1

# 显示帮助信息
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    echo "FinRadar 每日数据抓取"
    echo ""
    echo "使用方法:"
    echo "  ./fetch-all.sh              # 抓取所有数据（推荐）"
    echo "  ./fetch-all.sh -t           # 仅 Twitter"
    echo "  ./fetch-all.sh -w           # 仅微信公众号"
    echo "  ./fetch-all.sh -m           # 仅金融市场"
    echo "  ./fetch-all.sh -r           # 仅热榜新闻"
    echo "  ./fetch-all.sh -t -w        # Twitter + 微信"
    echo ""
    echo "参数说明:"
    echo "  -t, --twitter     抓取 Twitter 数据"
    echo "  -w, --wechat      抓取微信公众号文章"
    echo "  -m, --market      抓取金融市场数据"
    echo "  -r, --trendradar  运行 TrendRadar 热榜抓取"
    echo "  -a, --all         抓取所有数据（默认）"
    echo "  -h, --help        显示帮助信息"
    exit 0
fi

# 激活 conda 环境（如果存在）
if command -v conda &> /dev/null; then
    eval "$(conda shell.bash hook)"
    conda activate base 2>/dev/null
fi

# 运行抓取脚本
python scripts/daily_fetch.py "$@"
