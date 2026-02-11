#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHECKPOINT_FILE="${CHECKPOINT_FILE:-$ROOT_DIR/docs/SESSION_CHECKPOINT.md}"
TZ_NAME="${CHECKPOINT_TZ:-Asia/Shanghai}"

CURRENT_INTENT="${1:-}"
NEXT_STEP="${2:-}"

timestamp="$(TZ="$TZ_NAME" date '+%Y-%m-%d %H:%M:%S %Z')"
branch="$(git -C "$ROOT_DIR" branch --show-current 2>/dev/null || echo "unknown")"
head_commit="$(git -C "$ROOT_DIR" rev-parse --short HEAD 2>/dev/null || echo "none")"
status_text="$(git -C "$ROOT_DIR" status --short || true)"
recent_commits="$(git -C "$ROOT_DIR" log --oneline -n 8 || true)"

mkdir -p "$(dirname "$CHECKPOINT_FILE")"

if [ ! -f "$CHECKPOINT_FILE" ]; then
  cat > "$CHECKPOINT_FILE" <<'EOF'
# 会话 Checkpoint 记录

> 每次重要改动后追加一条，便于跨会话续做。

EOF
fi

{
  echo "## ${timestamp}"
  echo "- 分支: \`${branch}\`"
  echo "- 最新提交: \`${head_commit}\`"
  if [ -n "$CURRENT_INTENT" ]; then
    echo "- 当前意图: ${CURRENT_INTENT}"
  fi
  if [ -n "$NEXT_STEP" ]; then
    echo "- 下一步: ${NEXT_STEP}"
  fi
  echo "- 工作区状态:"
  if [ -n "$status_text" ]; then
    echo '```'
    echo "$status_text"
    echo '```'
  else
    echo "  - clean"
  fi
  echo "- 最近提交:"
  echo '```'
  echo "$recent_commits"
  echo '```'
  echo
} >> "$CHECKPOINT_FILE"

echo "✅ checkpoint 已写入: $CHECKPOINT_FILE"
