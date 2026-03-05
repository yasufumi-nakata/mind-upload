#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EXPORT_DIR="$ROOT/github-wiki-export"
REMOTE_BASE="https://github.com/yasufumi-nakata/mind-upload.wiki.git"
WORK_ROOT="$ROOT/ignore/github-wiki-publish"
WORK_DIR="$WORK_ROOT/repo"
ALLOW_SKIP="${WIKI_PUBLISH_ALLOW_SKIP:-0}"

if [[ ! -d "$EXPORT_DIR" ]]; then
  echo "github-wiki-export/ がありません。先に scripts/export_github_wiki.rb を実行してください。"
  exit 1
fi

TOKEN="${GITHUB_TOKEN:-$(gh auth token)}"
REMOTE_URL="https://x-access-token:${TOKEN}@github.com/yasufumi-nakata/mind-upload.wiki.git"

if ! git ls-remote "$REMOTE_URL" >/dev/null 2>&1; then
  echo "GitHub Wiki の git リポジトリがまだ初期化されていません。"
  echo "GitHub の Web UI で最初の Wiki ページを 1 つ作成した後に、再度このスクリプトを実行してください。"
  echo "想定 remote: $REMOTE_BASE"
  if [[ "$ALLOW_SKIP" == "1" ]]; then
    echo "WIKI_PUBLISH_ALLOW_SKIP=1 のため、失敗扱いにはしません。"
    exit 0
  fi
  exit 1
fi

mkdir -p "$WORK_ROOT"
ROOT_REAL="$(cd "$ROOT" && pwd -P)"
WORK_ROOT_REAL="$(cd "$WORK_ROOT" && pwd -P)"

case "$WORK_ROOT_REAL/" in
  "$ROOT_REAL"/*) ;;
  *)
    echo "GitHub Wiki の作業先はリポジトリ内に固定しています: $WORK_ROOT_REAL"
    exit 1
    ;;
esac

cleanup() {
  rm -rf "$WORK_DIR"
  rmdir "$WORK_ROOT" 2>/dev/null || true
}
trap cleanup EXIT

rm -rf "$WORK_DIR"

git clone "$REMOTE_URL" "$WORK_DIR"
rsync -a --delete --exclude ".git/" --exclude ".DS_Store" "$EXPORT_DIR"/ "$WORK_DIR"/
find "$WORK_DIR" -name ".DS_Store" -delete

cd "$WORK_DIR"

if git diff --quiet && git diff --cached --quiet; then
  echo "GitHub Wiki に反映すべき差分はありません。"
  exit 0
fi

git config user.name "${GIT_AUTHOR_NAME:-Codex}"
git config user.email "${GIT_AUTHOR_EMAIL:-codex@example.com}"
git add .

if git diff --cached --quiet; then
  echo "GitHub Wiki に反映すべき差分はありません。"
  exit 0
fi

git commit -m "Sync GitHub Wiki export"
git push origin HEAD:master
