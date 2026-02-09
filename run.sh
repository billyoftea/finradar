#!/bin/bash
# finradar Docker 便捷操作脚本
# 用法:
#   ./run.sh build     构建镜像
#   ./run.sh start     启动服务 (定时模式)
#   ./run.sh run       单次执行全部
#   ./run.sh run news  单次执行热榜新闻
#   ./run.sh run market 单次执行市场数据
#   ./run.sh start all --no-sources  仅启动 finradar 主容器
#   ./run.sh local setup   本地安装依赖与环境
#   ./run.sh local run all 本地单次执行
#   ./run.sh logs      查看日志
#   ./run.sh stop      停止服务
#   ./run.sh status    查看状态

set -e

cd "$(dirname "$0")"
COMPOSE_FILE="docker/docker-compose-unified.yml"

compose_with_sources_args() {
    local no_sources_flag="${1:-}"
    local with_sources="${WITH_SOCIAL_SOURCES:-true}"
    if [ "$no_sources_flag" = "--no-sources" ]; then
        with_sources="false"
    fi
    if [ "$with_sources" = "true" ]; then
        echo "--profile social-sources"
    fi
}

case "${1:-help}" in
build)
    echo "🔨 构建 finradar 镜像..."
    docker compose -f "$COMPOSE_FILE" build
    echo "✅ 构建完成"
    ;;
start)
    MODE="${2:-all}"
    EXTRA_FLAG="${3:-}"
    PROFILE_ARG=$(compose_with_sources_args "$EXTRA_FLAG")
    if [ -n "$PROFILE_ARG" ]; then
        echo "🚀 启动 finradar + 社交源服务 (定时模式, 任务: ${MODE})..."
        TASK_MODE="$MODE" docker compose -f "$COMPOSE_FILE" $PROFILE_ARG up -d
    else
        echo "🚀 启动 finradar (定时模式, 任务: ${MODE})..."
        TASK_MODE="$MODE" docker compose -f "$COMPOSE_FILE" up -d
    fi
    echo "✅ 服务已启动"
    echo "   查看日志: ./run.sh logs"
    ;;
run)
    MODE="${2:-all}"
    echo "▶️ 单次执行 finradar (模式: ${MODE})..."
    TASK_MODE="$MODE" RUN_MODE=once docker compose -f "$COMPOSE_FILE" run --rm finradar
    ;;
logs)
    docker compose -f "$COMPOSE_FILE" logs -f --tail=100
    ;;
stop)
    echo "⏹ 停止 finradar..."
    docker compose -f "$COMPOSE_FILE" --profile social-sources down
    echo "✅ 已停止"
    ;;
status)
    docker compose -f "$COMPOSE_FILE" ps
    ;;
restart)
    MODE="${2:-all}"
    EXTRA_FLAG="${3:-}"
    PROFILE_ARG=$(compose_with_sources_args "$EXTRA_FLAG")
    echo "🔄 重启 finradar..."
    docker compose -f "$COMPOSE_FILE" --profile social-sources down
    if [ -n "$PROFILE_ARG" ]; then
        TASK_MODE="$MODE" docker compose -f "$COMPOSE_FILE" $PROFILE_ARG up -d
    else
        TASK_MODE="$MODE" docker compose -f "$COMPOSE_FILE" up -d
    fi
    echo "✅ 已重启"
    ;;
local)
    shift
    exec ./scripts/local.sh "${@:-help}"
    ;;
help|*)
    echo "finradar Docker 操作脚本"
    echo ""
    echo "用法: ./run.sh <命令> [模式]"
    echo ""
    echo "命令:"
    echo "  build           构建 Docker 镜像"
    echo "  start [模式]    启动定时服务 (后台运行)"
    echo "  run [模式]      单次执行"
    echo "  logs            查看实时日志"
    echo "  stop            停止服务"
    echo "  restart [模式]  重启服务"
    echo "  status          查看运行状态"
    echo "  local ...       使用本地运行工具（不走 Docker）"
    echo ""
    echo "模式: all | news | market | social (默认: all)"
    echo "附加参数: --no-sources (不启动 nitter/wechat 源服务)"
    echo ""
    echo "示例:"
    echo "  ./run.sh build          # 首次使用，构建镜像"
    echo "  ./run.sh start          # 启动全部定时任务（含 nitter/wechat 服务）"
    echo "  ./run.sh start all --no-sources  # 只启动 finradar 主服务"
    echo "  ./run.sh start market   # 只启动市场数据定时"
    echo "  ./run.sh run news       # 单次抓取热榜新闻"
    echo "  ./run.sh run market     # 单次抓取市场数据"
    echo "  ./run.sh logs           # 查看日志"
    echo "  ./run.sh stop           # 停止"
    echo "  ./run.sh local setup    # 本地初始化环境"
    echo "  ./run.sh local cron-install # 本地安装定时任务"
    ;;
esac
