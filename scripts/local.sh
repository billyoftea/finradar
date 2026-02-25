#!/usr/bin/env bash
#
# finradar 本地运行工具（本地优先，Docker 可选）
#
# 用法:
#   ./scripts/local.sh setup
#   ./scripts/local.sh run [all|news|market|social]
#   ./scripts/local.sh social-scan
#   ./scripts/local.sh cleanup-social-cache
#   ./scripts/local.sh cleanup-social-ttl
#   ./scripts/local.sh report [morning|evening|auto] [YYYYMMDD] [generate_report extra args]
#   ./scripts/local.sh notion-push [morning|evening|auto] [YYYYMMDD] [push_to_notion extra args]
#   ./scripts/local.sh checkpoint [intent] [next-step]
#   ./scripts/local.sh autocommit "<message>" [dev_autocommit extra args]
#   ./scripts/local.sh cron-install
#   ./scripts/local.sh cron-remove
#   ./scripts/local.sh status

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${VENV_DIR:-$ROOT_DIR/.venv}"
PYTHON_BIN="$VENV_DIR/bin/python"
PIP_BIN="$VENV_DIR/bin/pip"
LOG_DIR="$ROOT_DIR/output/logs"
CRON_BEGIN="# >>> finradar local schedule >>>"
CRON_END="# <<< finradar local schedule <<<"
NOTION_ENV_FILE="${NOTION_ENV_FILE:-$ROOT_DIR/.notion.env}"
CHECKPOINT_SCRIPT="$ROOT_DIR/scripts/dev_checkpoint.sh"
AUTOCOMMIT_SCRIPT="$ROOT_DIR/scripts/dev_autocommit.sh"
AUTO_CHECKPOINT_ON_REPORT="${AUTO_CHECKPOINT_ON_REPORT:-1}"
TWITTER_CACHE_FILE="${TWITTER_CACHE_FILE:-$ROOT_DIR/output/twitter/trending_cache.json}"
TWITTER_STATE_FILE="${TWITTER_STATE_FILE:-$ROOT_DIR/output/twitter/trending_state.json}"
TWITTER_FOLLOW_CACHE_FILE="${TWITTER_FOLLOW_CACHE_FILE:-$ROOT_DIR/output/twitter/follow_cache.json}"
TWITTER_FOLLOW_RETENTION_HOURS="${TWITTER_FOLLOW_RETENTION_HOURS:-48}"

ensure_venv() {
    if [ ! -x "$PYTHON_BIN" ]; then
        echo "❌ 未检测到虚拟环境: $VENV_DIR"
        echo "请先执行: ./scripts/local.sh setup"
        exit 1
    fi
}

cmd_setup() {
    echo "🔧 初始化本地 Python 环境..."
    python3 -m venv "$VENV_DIR"
    "$PIP_BIN" install --upgrade pip
    "$PIP_BIN" install -r "$ROOT_DIR/requirements.txt" -r "$ROOT_DIR/finradar/market/requirements.txt"
    mkdir -p "$ROOT_DIR/output/market" "$ROOT_DIR/output/news" "$ROOT_DIR/output/report" "$LOG_DIR"
    echo "✅ 本地环境初始化完成"
}

cmd_run() {
    ensure_venv
    local mode="${1:-all}"
    mkdir -p "$LOG_DIR"
    echo "▶️ 本地单次执行: mode=$mode"
    (cd "$ROOT_DIR" && "$PYTHON_BIN" -m finradar --mode "$mode")
}

cmd_social_scan() {
    ensure_venv
    mkdir -p "$LOG_DIR"
    echo "🔎 手动社交预扫描（仅关注账号缓存）: mode=social"
    (
        cd "$ROOT_DIR" && ENABLE_WECHAT=0 TWITTER_FOLLOW_ONLY_SCAN=1 "$PYTHON_BIN" -m finradar --mode social >> "$LOG_DIR/cron-social-scan.log" 2>&1
    )
}

cmd_cleanup_social_cache() {
    ensure_venv
    echo "🧹 清理社交本地缓存文件..."
    "$PYTHON_BIN" - <<PY
from pathlib import Path

paths = [
    Path(r"$TWITTER_CACHE_FILE"),
    Path(r"$TWITTER_STATE_FILE"),
    Path(r"$TWITTER_FOLLOW_CACHE_FILE"),
]
removed = []
for p in paths:
    if p.exists():
        p.unlink()
        removed.append(str(p))

if removed:
    print("removed:", ", ".join(removed))
else:
    print("no cache file found")
PY
}


cmd_cleanup_social_ttl() {
    ensure_venv
    echo "🧽 滚动清理关注推文缓存（保留最近 ${TWITTER_FOLLOW_RETENTION_HOURS} 小时）..."
    "$PYTHON_BIN" - <<PY
from pathlib import Path
from datetime import datetime, timedelta, timezone
import json

cache_file = Path(r"$TWITTER_FOLLOW_CACHE_FILE")
retention_hours = max(1, int(r"$TWITTER_FOLLOW_RETENTION_HOURS"))

if not cache_file.exists():
    print(f"no follow cache file found: {cache_file}")
    raise SystemExit(0)

try:
    data = json.loads(cache_file.read_text(encoding="utf-8"))
except Exception as e:
    print(f"failed to read {cache_file}: {e}")
    raise SystemExit(1)

items = data.get("tweets", []) if isinstance(data, dict) else []
if not isinstance(items, list):
    items = []

cutoff = datetime.now(timezone.utc) - timedelta(hours=retention_hours)

def parse_dt(value):
    if not value:
        return None
    text = str(value).strip().replace("Z", "+00:00")
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None

kept = []
for item in items:
    if not isinstance(item, dict):
        continue
    created = parse_dt(item.get("created_at"))
    fetched = parse_dt(item.get("fetched_at"))
    ref = created or fetched
    if ref is None or ref >= cutoff:
        kept.append(item)

kept.sort(
    key=lambda x: parse_dt(x.get("created_at")) or parse_dt(x.get("fetched_at")) or datetime.min.replace(tzinfo=timezone.utc),
    reverse=True,
)

if isinstance(data, dict):
    data["updated_at"] = datetime.now(timezone.utc).isoformat()
    data["retention_hours"] = retention_hours
    data["tweets"] = kept
else:
    data = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "retention_hours": retention_hours,
        "tweets": kept,
    }

cache_file.parent.mkdir(parents=True, exist_ok=True)
cache_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"follow cache pruned: {len(items)} -> {len(kept)} ({cache_file})")
PY
}

cmd_report() {
    ensure_venv
    local report_type="${1:-auto}"
    shift || true
    local date_arg=""
    if [ "${1:-}" != "" ] && [[ "${1}" =~ ^[0-9]{8}$ ]]; then
        date_arg="$1"
        shift || true
    fi
    local extra_args=("$@")
    mkdir -p "$LOG_DIR"
    local ai_mode="with-ai"
    for arg in "${extra_args[@]}"; do
        if [ "$arg" = "--no-ai" ]; then
            ai_mode="no-ai"
            break
        fi
    done
    if [ -n "$date_arg" ]; then
        echo "📝 生成报告: type=$report_type, date=$date_arg ${extra_args[*]}"
        (cd "$ROOT_DIR" && "$PYTHON_BIN" scripts/generate_report.py --type "$report_type" --date "$date_arg" "${extra_args[@]}")
    else
        echo "📝 生成报告: type=$report_type ${extra_args[*]}"
        (cd "$ROOT_DIR" && "$PYTHON_BIN" scripts/generate_report.py --type "$report_type" "${extra_args[@]}")
    fi
    if [ "$AUTO_CHECKPOINT_ON_REPORT" = "1" ] && [ -x "$CHECKPOINT_SCRIPT" ]; then
        local cp_date="$date_arg"
        if [ -z "$cp_date" ]; then
            cp_date="$(TZ=Asia/Shanghai date '+%Y%m%d')"
        fi
        local cp_intent="生成${cp_date} ${report_type} 报告（${ai_mode}）"
        local cp_next="查看 output/report 结果并持续优化分板块结构与时效过滤规则"
        (cd "$ROOT_DIR" && "$CHECKPOINT_SCRIPT" "$cp_intent" "$cp_next") || true
    fi
}

load_notion_env() {
    if [ -f "$NOTION_ENV_FILE" ]; then
        set -a
        # shellcheck disable=SC1090
        . "$NOTION_ENV_FILE"
        set +a
    fi
}

cmd_notion_config() {
    local token="${1:-}"
    local parent="${2:-}"
    if [ -z "$token" ] || [ -z "$parent" ]; then
        echo "❌ 用法: ./scripts/local.sh notion-config <notion_token> <parent_page_url_or_id>"
        exit 1
    fi
    local escaped_token escaped_parent
    escaped_token="${token//\'/\'\"\'\"\'}"
    escaped_parent="${parent//\'/\'\"\'\"\'}"
    cat > "$NOTION_ENV_FILE" <<EOF
NOTION_API_TOKEN='$escaped_token'
NOTION_PARENT_PAGE='$escaped_parent'
EOF
    chmod 600 "$NOTION_ENV_FILE"
    echo "✅ Notion 配置已写入: $NOTION_ENV_FILE"
}

cmd_notion_push() {
    ensure_venv
    load_notion_env
    local report_type="${1:-auto}"
    local date_arg="${2:-}"
    local extra_args=("${@:3}")
    mkdir -p "$LOG_DIR"
    if [ -n "$date_arg" ]; then
        echo "🧭 推送到 Notion: type=$report_type, date=$date_arg ${extra_args[*]}"
        (cd "$ROOT_DIR" && "$PYTHON_BIN" scripts/push_to_notion.py --type "$report_type" --date "$date_arg" "${extra_args[@]}")
    else
        echo "🧭 推送到 Notion: type=$report_type ${extra_args[*]}"
        (cd "$ROOT_DIR" && "$PYTHON_BIN" scripts/push_to_notion.py --type "$report_type" "${extra_args[@]}")
    fi
}

build_cron_block() {
    cat <<EOF
$CRON_BEGIN
*/30 * * * * cd $ROOT_DIR && $PYTHON_BIN -m finradar --mode market >> $LOG_DIR/cron-market.log 2>&1 && $PYTHON_BIN -m finradar --mode news >> $LOG_DIR/cron-news.log 2>&1
0 */6 * * * cd $ROOT_DIR && $ROOT_DIR/scripts/local.sh cleanup-social-ttl >> $LOG_DIR/cron-social-cleanup.log 2>&1
0 * * * * cd $ROOT_DIR && [ "\$(TZ=Asia/Shanghai date +\%H)" = "08" ] && $PYTHON_BIN -m finradar --mode social >> $LOG_DIR/cron-social.log 2>&1 && $PYTHON_BIN scripts/generate_report.py --type morning >> $LOG_DIR/cron-report.log 2>&1 && $ROOT_DIR/scripts/local.sh notion-push morning >> $LOG_DIR/cron-notion.log 2>&1
0 * * * * cd $ROOT_DIR && [ "\$(TZ=Asia/Shanghai date +\%H)" = "20" ] && $PYTHON_BIN -m finradar --mode social >> $LOG_DIR/cron-social.log 2>&1 && $PYTHON_BIN scripts/generate_report.py --type evening >> $LOG_DIR/cron-report.log 2>&1 && $ROOT_DIR/scripts/local.sh notion-push evening >> $LOG_DIR/cron-notion.log 2>&1
$CRON_END
EOF
}

cmd_cron_install() {
    ensure_venv
    mkdir -p "$LOG_DIR"
    local tmp_old tmp_new
    tmp_old="$(mktemp)"
    tmp_new="$(mktemp)"

    crontab -l 2>/dev/null | sed "/^$CRON_BEGIN\$/,/^$CRON_END\$/d" > "$tmp_old" || true
    cat "$tmp_old" > "$tmp_new"
    if [ -s "$tmp_new" ]; then
        echo "" >> "$tmp_new"
    fi
    build_cron_block >> "$tmp_new"
    crontab "$tmp_new"
    rm -f "$tmp_old" "$tmp_new"
    echo "✅ 本地定时任务已安装:"
    echo "   - 每30分钟: 市场 + 热榜"
    echo "   - 每6小时: 清理关注推文缓存（仅保留48小时）"
    echo "   - 每天08:00: 社交抓取 + 早报 + Notion 子页面推送"
    echo "   - 每天20:00: 社交抓取 + 晚报 + Notion 子页面推送"
}

cmd_cron_remove() {
    local tmp_old
    tmp_old="$(mktemp)"
    crontab -l 2>/dev/null | sed "/^$CRON_BEGIN\$/,/^$CRON_END\$/d" > "$tmp_old" || true
    crontab "$tmp_old"
    rm -f "$tmp_old"
    echo "✅ 已移除 finradar 本地定时任务"
}

cmd_status() {
    echo "📂 最新产出文件:"
    ls -lt "$ROOT_DIR/output/report" 2>/dev/null | head -n 5 || true
    ls -lt "$ROOT_DIR/output/market" 2>/dev/null | head -n 5 || true
    echo ""
    echo "📋 当前 crontab 中 finradar 段:"
    crontab -l 2>/dev/null | sed -n "/^$CRON_BEGIN\$/,/^$CRON_END\$/p" || true
}

cmd_checkpoint() {
    local intent="${1:-}"
    local next_step="${2:-}"
    if [ ! -x "$CHECKPOINT_SCRIPT" ]; then
        echo "❌ 未找到可执行脚本: $CHECKPOINT_SCRIPT"
        exit 1
    fi
    (cd "$ROOT_DIR" && "$CHECKPOINT_SCRIPT" "$intent" "$next_step")
}

cmd_autocommit() {
    local commit_message="${1:-}"
    shift || true
    if [ -z "$commit_message" ]; then
        echo "❌ 用法: ./scripts/local.sh autocommit \"<message>\" [dev_autocommit extra args]"
        exit 1
    fi
    if [ ! -x "$AUTOCOMMIT_SCRIPT" ]; then
        echo "❌ 未找到可执行脚本: $AUTOCOMMIT_SCRIPT"
        exit 1
    fi
    (cd "$ROOT_DIR" && "$AUTOCOMMIT_SCRIPT" "$commit_message" "$@")
}

case "${1:-help}" in
setup)
    cmd_setup
    ;;
run)
    cmd_run "${2:-all}"
    ;;
social-scan)
    cmd_social_scan
    ;;
cleanup-social-cache)
    cmd_cleanup_social_cache
    ;;
cleanup-social-ttl)
    cmd_cleanup_social_ttl
    ;;
report)
    cmd_report "${2:-auto}" "${@:3}"
    ;;
cron-install)
    cmd_cron_install
    ;;
cron-remove)
    cmd_cron_remove
    ;;
status)
    cmd_status
    ;;
checkpoint)
    cmd_checkpoint "${2:-}" "${3:-}"
    ;;
autocommit)
    cmd_autocommit "${2:-}" "${@:3}"
    ;;
notion-config)
    cmd_notion_config "${2:-}" "${3:-}"
    ;;
notion-push)
    cmd_notion_push "${2:-auto}" "${3:-}"
    ;;
help|*)
    cat <<'EOF'
finradar 本地运行工具

命令:
  setup                    初始化本地虚拟环境并安装依赖
  run [mode]               单次执行 (all/news/market/social)
  social-scan              手动执行一次社交预扫描（仅关注账号缓存）
  cleanup-social-cache     清理 Twitter 本地缓存文件（删除缓存文件）
  cleanup-social-ttl       仅清理关注推文缓存中的过期数据（保留48小时）
  report [type] [date] [extra-args]  生成报告 (morning/evening/auto)
  checkpoint [intent] [next-step]     记录会话 checkpoint
  autocommit "<msg>" [extra-args]     自动提交并记录 checkpoint
  notion-config <token> <parent>  写入 Notion 配置到 .notion.env
  notion-push [type] [date] [extra-args] 推送报告到 Notion 子页面
  cron-install             安装本地定时任务（08:00 / 20:00 + 每30分钟）
  cron-remove              删除本地定时任务
  status                   查看最近产出和定时任务状态

示例:
  ./scripts/local.sh setup
  ./scripts/local.sh run social
  ./scripts/local.sh report morning
  ./scripts/local.sh report evening 20260211 --keywords "A股,美股,AI芯片"
  ./scripts/local.sh checkpoint "补充联网检索" "继续优化关键词"
  ./scripts/local.sh autocommit "feat(report): xxx" --include "scripts/generate_report.py,README.local.md"
  ./scripts/local.sh notion-config ntn_xxx https://www.notion.so/xxx
  ./scripts/local.sh notion-push morning 20260209
  NOTION_MERGE_DAILY=1 ./scripts/local.sh notion-push evening 20260209
  ./scripts/local.sh cron-install
EOF
    ;;
esac
