#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PUBLISH_SCRIPT="$ROOT/scripts/publish_github_wiki.sh"
LOCK_SCRIPT="$ROOT/scripts/with_github_wiki_lock.sh"
EXPORT_DIR="$ROOT/github-wiki-export"
WORK_ROOT="$ROOT/ignore/github-wiki-publish"
TEST_ROOT="$ROOT/ignore/github-wiki-publish-selftest-$PPID-$$"
REMOTE_BARE="$TEST_ROOT/remote.git"
SEED_REPO="$TEST_ROOT/seed"
VERIFY_REPO="$TEST_ROOT/verify"

log() {
  echo "[github-wiki-publish-selftest] $1"
}

fail() {
  echo "[github-wiki-publish-selftest] $1" >&2
  exit 1
}

cleanup() {
  rm -rf "$TEST_ROOT"
}
trap cleanup EXIT

require_clean_work_root() {
  [[ ! -e "$WORK_ROOT/repo" ]] || fail "Publish work repo remained: $WORK_ROOT/repo"
  [[ ! -d "$WORK_ROOT" ]] || fail "Publish work root remained: $WORK_ROOT"
}

run_publish() {
  GITHUB_WIKI_REMOTE_BASE="$REMOTE_BARE" \
  GITHUB_WIKI_REMOTE_URL="$REMOTE_BARE" \
  "$LOCK_SCRIPT" "$PUBLISH_SCRIPT"
}

log "prepare-remote"
mkdir -p "$TEST_ROOT"
git init --bare --initial-branch=master "$REMOTE_BARE" >/dev/null
git init --initial-branch=master "$SEED_REPO" >/dev/null
git -C "$SEED_REPO" config user.name "Codex"
git -C "$SEED_REPO" config user.email "codex@example.com"
printf 'seed\n' > "$SEED_REPO/seed.md"
git -C "$SEED_REPO" add seed.md
git -C "$SEED_REPO" commit -m "Seed wiki remote" >/dev/null
git -C "$SEED_REPO" remote add origin "$REMOTE_BARE"
git -C "$SEED_REPO" push origin master >/dev/null

log "first-publish"
first_output="$(run_publish 2>&1)"
printf '%s\n' "$first_output"
require_clean_work_root

git clone "$REMOTE_BARE" "$VERIFY_REPO" >/dev/null 2>&1
cmp "$EXPORT_DIR/Home.md" "$VERIFY_REPO/Home.md" >/dev/null || fail "Published Home.md does not match export."
cmp "$EXPORT_DIR/_Sidebar.md" "$VERIFY_REPO/_Sidebar.md" >/dev/null || fail "Published _Sidebar.md does not match export."

log "second-publish"
second_output="$(run_publish 2>&1)"
printf '%s\n' "$second_output"
[[ "$second_output" == *"GitHub Wiki に反映すべき差分はありません。"* ]] || fail "Second publish did not report no diff."
require_clean_work_root

log "ok"
