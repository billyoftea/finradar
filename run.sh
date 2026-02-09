#!/bin/bash
# finradar Docker 便捷操作脚本
# 用法:
#   ./run.sh build     构建镜像
#   ./run.sh start     启动服务 (定时模式)
#   ./run.sh run       单次执行全部
#   ./run.sh run news  单次执行热榜新闻
#   ./run.sh run market 单次执行市场数据
#   ./run.sh logs      查看日志
#   ./run.sh stop      停止服务
#   ./run.sh status    查看状态

set -e

cd "$(dirname "$0")"
COMPOSE_FILE="docker/docker-compose-unified.yml"

case "${1:-help}" in
build)
    echo "🔨 构建 finradar 镜像..."
    docker compose -f "$COMPOSE_FILE" build
    echo "✅ 构建完成"
    ;;
start)
    MODE="${2:-all}"
    echo "🚀 启动 finradar (定时模式, 任务: ${MODE})..."
    TASK_MODE="$MODE" docker compose -f "$COMPOSE_FILE" up -d
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
    docker compose -f "$COMPOSE_FILE" down
    echo "✅ 已停止"
    ;;
status)
    docker compose -f "$COMPOSE_FILE" ps
    ;;
restart)
    MODE="${2:-all}"
    echo "🔄 重启 finradar..."
    docker compose -f "$COMPOSE_FILE" down
    TASK_MODE="$MODE" docker compose -f "$COMPOSE_FILE" up -d
    echo "✅ 已重启"
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
    echo ""
    echo "模式: all | news | market | social (默认: all)"
    echo ""
    echo "示例:"
    echo "  ./run.sh build          # 首次使用，构建镜像"
    echo "  ./run.sh start          # 启动全部定时任务"
    echo "  ./run.sh start market   # 只启动市场数据定时"
    echo "  ./run.sh run news       # 单次抓取热榜新闻"
    echo "  ./run.sh run market     # 单次抓取市场数据"
    echo "  ./run.sh logs           # 查看日志"
    echo "  ./run.sh stop           # 停止"
    ;;
esac
