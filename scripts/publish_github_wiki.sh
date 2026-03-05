#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EXPORT_DIR="$ROOT/github-wiki-export"
REMOTE_BASE="https://github.com/yasufumi-nakata/mind-upload.wiki.git"

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
  exit 1
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

git clone "$REMOTE_URL" "$TMP_DIR/wiki"
rsync -a --delete "$EXPORT_DIR"/ "$TMP_DIR/wiki"/

cd "$TMP_DIR/wiki"

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
