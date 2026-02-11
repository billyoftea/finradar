#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHECKPOINT_SCRIPT="$ROOT_DIR/scripts/dev_checkpoint.sh"

if [ "$#" -lt 1 ]; then
  echo "用法: ./scripts/dev_autocommit.sh <commit-message> [--include path1,path2] [--intent text] [--next text]"
  exit 1
fi

COMMIT_MESSAGE="$1"
shift || true
INCLUDE_PATHS=""
INTENT=""
NEXT_STEP=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --include)
      INCLUDE_PATHS="${2:-}"
      shift 2 || true
      ;;
    --intent)
      INTENT="${2:-}"
      shift 2 || true
      ;;
    --next)
      NEXT_STEP="${2:-}"
      shift 2 || true
      ;;
    *)
      echo "未知参数: $1"
      exit 1
      ;;
  esac
done

cd "$ROOT_DIR"

# 默认只提交已跟踪文件，避免误把 output/ 等未跟踪大文件提交。
git add -u

if [ -n "$INCLUDE_PATHS" ]; then
  IFS=',' read -r -a path_arr <<< "$INCLUDE_PATHS"
  for p in "${path_arr[@]}"; do
    p="$(echo "$p" | xargs)"
    [ -z "$p" ] && continue
    git add "$p"
  done
fi

if git diff --cached --quiet; then
  echo "没有可提交的变更。"
  exit 0
fi

git commit -m "$COMMIT_MESSAGE"

if [ -x "$CHECKPOINT_SCRIPT" ]; then
  "$CHECKPOINT_SCRIPT" "$INTENT" "$NEXT_STEP"
fi

echo "✅ 自动提交完成"
