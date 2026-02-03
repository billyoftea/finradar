#!/bin/bash
#
# Twitter Token 一键更新脚本
#
# 使用方法:
#   ./update-twitter-token.sh <auth_token> <ct0>
#
# 参数获取方法:
#   1. 登录 https://twitter.com
#   2. F12 打开开发者工具
#   3. Application → Cookies → https://twitter.com
#   4. 复制 auth_token 和 ct0 的值
#

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 项目根目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 配置文件路径
SESSIONS_FILE="$PROJECT_ROOT/fin_module/nitter/sessions.jsonl"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}   Twitter Token 一键更新脚本${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# 检查参数
if [ $# -lt 2 ]; then
    echo -e "${YELLOW}使用方法:${NC}"
    echo -e "  $0 <auth_token> <ct0>"
    echo ""
    echo -e "${YELLOW}如何获取参数:${NC}"
    echo -e "  1. 登录 https://twitter.com"
    echo -e "  2. F12 打开开发者工具"
    echo -e "  3. Application → Cookies → https://twitter.com"
    echo -e "  4. 复制 auth_token 和 ct0 的值"
    echo ""
    
    # 交互式输入
    echo -e "${YELLOW}或者现在输入:${NC}"
    echo -n "auth_token: "
    read -r AUTH_TOKEN
    echo -n "ct0: "
    read -r CT0
else
    AUTH_TOKEN="$1"
    CT0="$2"
fi

# 验证输入
if [ -z "$AUTH_TOKEN" ] || [ -z "$CT0" ]; then
    echo -e "${RED}❌ 错误: auth_token 和 ct0 都不能为空${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}📋 新的 Token:${NC}"
echo -e "   auth_token: ${AUTH_TOKEN:0:20}..."
echo -e "   ct0: ${CT0:0:20}..."
echo ""

# 备份原文件
if [ -f "$SESSIONS_FILE" ]; then
    echo -e "${YELLOW}📦 备份原配置...${NC}"
    cp "$SESSIONS_FILE" "$SESSIONS_FILE.bak.$(date +%Y%m%d%H%M%S)"
fi

# 获取用户 ID（如果原文件存在）
USER_ID="1963053124467490820"  # 默认 ID
if [ -f "$SESSIONS_FILE" ]; then
    EXISTING_ID=$(grep -oP '"id":\s*"\K[^"]+' "$SESSIONS_FILE" 2>/dev/null || echo "")
    if [ -n "$EXISTING_ID" ]; then
        USER_ID="$EXISTING_ID"
    fi
fi

# 写入新配置
echo -e "${YELLOW}📝 更新配置文件...${NC}"
echo "{\"kind\": \"cookie\", \"auth_token\": \"$AUTH_TOKEN\", \"ct0\": \"$CT0\", \"id\": \"$USER_ID\"}" > "$SESSIONS_FILE"
echo -e "${GREEN}✅ 配置文件已更新${NC}"

# 重启 Nitter
echo ""
echo -e "${YELLOW}🔄 重启 Nitter 服务...${NC}"
cd "$PROJECT_ROOT/fin_module/nitter"
sudo docker compose restart

# 等待服务启动
echo -e "${YELLOW}⏳ 等待服务启动...${NC}"
sleep 5

# 测试
echo ""
echo -e "${YELLOW}🧪 测试 Twitter RSS...${NC}"
NITTER_HOST=$(grep -oP 'nitter_instance:\s*"\K[^"]+' "$PROJECT_ROOT/config/config.yaml" 2>/dev/null || echo "http://localhost:8080")
TEST_URL="${NITTER_HOST}/elonmusk/rss"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$TEST_URL" 2>/dev/null || echo "000")

if [ "$HTTP_CODE" == "200" ]; then
    echo -e "${GREEN}✅ Nitter 服务正常！${NC}"
    echo ""
    echo -e "${YELLOW}📰 最新推文预览:${NC}"
    curl -s "$TEST_URL" | grep -oP '<title>\K[^<]+' | head -3
else
    echo -e "${RED}⚠️ 测试返回 HTTP $HTTP_CODE，可能需要等待服务完全启动${NC}"
    echo -e "   手动测试: curl $TEST_URL"
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}   ✅ Twitter Token 更新完成!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
