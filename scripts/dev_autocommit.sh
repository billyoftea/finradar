#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHECKPOINT_SCRIPT="$ROOT_DIR/scripts/dev_checkpoint.sh"

if [ "$#" -lt 1 ]; then
  echo "用法: ./scripts/dev_autocommit.sh <commit-message> [--include path1,path2] [--all-tracked] [--intent text] [--next text]"
  exit 1
fi

COMMIT_MESSAGE="$1"
shift || true
INCLUDE_PATHS=""
ALL_TRACKED=0
INTENT=""
NEXT_STEP=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --include)
      INCLUDE_PATHS="${2:-}"
      shift 2 || true
      ;;
    --all-tracked)
      ALL_TRACKED=1
      shift || true
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

if [ "$ALL_TRACKED" -eq 1 ]; then
  # 显式允许时，提交所有已跟踪变更。
  git add -u
fi

if [ -n "$INCLUDE_PATHS" ]; then
  IFS=',' read -r -a path_arr <<< "$INCLUDE_PATHS"
  for p in "${path_arr[@]}"; do
    p="$(echo "$p" | xargs)"
    [ -z "$p" ] && continue
    git add "$p"
  done
fi

if [ "$ALL_TRACKED" -ne 1 ] && [ -z "$INCLUDE_PATHS" ]; then
  echo "请至少提供 --include，或显式使用 --all-tracked。"
  exit 1
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
