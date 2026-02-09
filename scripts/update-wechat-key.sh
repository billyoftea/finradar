#!/bin/bash
#
# 微信公众号 Auth Key 一键更新脚本
# 
# 使用方法:
#   ./update-wechat-key.sh
#
# 功能:
#   1. 自动从 cookie 目录获取最新的 auth_key
#   2. 更新 config/config.yaml 中的 auth_key
#   3. 重建并重启 Docker 服务
#

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 项目根目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 配置文件路径
COOKIE_DIR="$PROJECT_ROOT/output/wechat/.data/kv/cookie"
CONFIG_FILE="$PROJECT_ROOT/config/config.yaml"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}   微信公众号 Auth Key 一键更新脚本${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 检查 cookie 目录是否存在
if [ ! -d "$COOKIE_DIR" ]; then
    echo -e "${RED}❌ 错误: Cookie 目录不存在${NC}"
    echo -e "   路径: $COOKIE_DIR"
    echo -e "   请先启动微信服务并登录"
    exit 1
fi

# 获取最新的 auth_key（按修改时间排序）
echo -e "${YELLOW}📂 正在查找最新的 Auth Key...${NC}"
LATEST_KEY=$(ls -t "$COOKIE_DIR" 2>/dev/null | head -1)

if [ -z "$LATEST_KEY" ]; then
    echo -e "${RED}❌ 错误: Cookie 目录为空${NC}"
    echo -e "   请访问微信服务界面并扫码登录:"
    echo -e "   http://你的服务器IP:3001"
    exit 1
fi

echo -e "${GREEN}✅ 找到 Auth Key: ${LATEST_KEY}${NC}"
echo ""

# 显示当前配置中的 auth_key
CURRENT_KEY=$(grep -oP 'auth_key:\s*"\K[^"]+' "$CONFIG_FILE" 2>/dev/null || echo "未配置")
echo -e "${YELLOW}📋 当前配置的 Auth Key: ${CURRENT_KEY}${NC}"
echo -e "${YELLOW}📋 最新的 Auth Key:     ${LATEST_KEY}${NC}"
echo ""

# 如果 key 相同，无需更新
if [ "$CURRENT_KEY" == "$LATEST_KEY" ]; then
    echo -e "${GREEN}✅ Auth Key 已是最新，无需更新${NC}"
    exit 0
fi

# 确认更新
echo -e "${YELLOW}是否更新 Auth Key? [Y/n]${NC}"
read -r CONFIRM
if [[ "$CONFIRM" =~ ^[Nn] ]]; then
    echo -e "${YELLOW}已取消${NC}"
    exit 0
fi

# 备份配置文件
echo -e "${YELLOW}📦 备份配置文件...${NC}"
cp "$CONFIG_FILE" "$CONFIG_FILE.bak.$(date +%Y%m%d%H%M%S)"

# 更新配置文件中的 auth_key
echo -e "${YELLOW}📝 更新配置文件...${NC}"
if grep -q 'auth_key:' "$CONFIG_FILE"; then
    # 使用 sed 替换 auth_key
    sed -i "s/auth_key:.*$/auth_key: \"$LATEST_KEY\"/" "$CONFIG_FILE"
    echo -e "${GREEN}✅ 配置文件已更新${NC}"
else
    echo -e "${RED}❌ 错误: 配置文件中未找到 auth_key 字段${NC}"
    echo -e "   请手动在 wechat 部分添加: auth_key: \"$LATEST_KEY\""
    exit 1
fi

# 询问是否重建 Docker
echo ""
echo -e "${YELLOW}是否重建并重启 Docker 服务? [Y/n]${NC}"
read -r REBUILD
if [[ ! "$REBUILD" =~ ^[Nn] ]]; then
    echo ""
    echo ""
    echo -e "${YELLOW}🔄 重启服务...${NC}"
    cd "$PROJECT_ROOT/docker"
    docker compose -f docker-compose-unified.yml --profile social-sources up -d wechat-exporter finradar

    echo ""
    echo -e "${GREEN}✅ 服务已重启${NC}"
    echo ""
    echo -e "${YELLOW}📊 等待 30 秒后查看日志...${NC}"
    sleep 30
    docker logs finradar --tail 50 || true
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}   ✅ Auth Key 更新完成!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
