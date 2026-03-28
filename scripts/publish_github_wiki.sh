#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EXPORT_DIR="$ROOT/github-wiki-export"
DEFAULT_REMOTE_BASE="https://github.com/yasufumi-nakata/mind-upload.wiki.git"
REMOTE_BASE="${GITHUB_WIKI_REMOTE_BASE:-$DEFAULT_REMOTE_BASE}"
WORK_ROOT="$ROOT/ignore/github-wiki-publish"
WORK_DIR="$WORK_ROOT/repo"
ALLOW_SKIP="${WIKI_PUBLISH_ALLOW_SKIP:-0}"

if [[ ! -d "$EXPORT_DIR" ]]; then
  echo "github-wiki-export/ is missing. Run scripts/export_github_wiki.rb first."
  exit 1
fi

REMOTE_URL="$REMOTE_BASE"

if [[ -n "${GITHUB_WIKI_REMOTE_URL:-}" ]]; then
  REMOTE_URL="${GITHUB_WIKI_REMOTE_URL}"
elif [[ "$REMOTE_BASE" == https://github.com/* ]]; then
  TOKEN="${GITHUB_TOKEN:-$(gh auth token)}"
  REMOTE_URL="https://x-access-token:${TOKEN}@${REMOTE_BASE#https://}"
fi

if ! git ls-remote "$REMOTE_URL" >/dev/null 2>&1; then
  echo "The GitHub Wiki git repository has not been initialized yet."
  echo "Create the first Wiki page in GitHub's Web UI, then run this script again."
  echo "Expected remote: $REMOTE_BASE"
  if [[ "$ALLOW_SKIP" == "1" ]]; then
    echo "Because WIKI_PUBLISH_ALLOW_SKIP=1, this will not be treated as a failure."
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
    echo "The GitHub Wiki working directory must stay inside the repository: $WORK_ROOT_REAL"
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
  echo "There are no GitHub Wiki changes to publish."
  exit 0
fi

git config user.name "${GIT_AUTHOR_NAME:-Codex}"
git config user.email "${GIT_AUTHOR_EMAIL:-codex@example.com}"
git add .

if git diff --cached --quiet; then
  echo "There are no GitHub Wiki changes to publish."
  exit 0
fi

git commit -m "Sync GitHub Wiki export"
git push origin HEAD:master
