#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOCK_DIR="$ROOT/ignore/github-wiki-toolchain.lock"
WAIT_SECONDS="${GITHUB_WIKI_LOCK_WAIT_SECONDS:-30}"
START_TIME="$(date +%s)"

if [[ "$#" -eq 0 ]]; then
  echo "Usage: scripts/with_github_wiki_lock.sh <command> [args...]" >&2
  exit 1
fi

mkdir -p "$ROOT/ignore"

while ! mkdir "$LOCK_DIR" 2>/dev/null; do
  NOW="$(date +%s)"
  if (( NOW - START_TIME >= WAIT_SECONDS )); then
    echo "Timed out waiting for GitHub Wiki toolchain lock: $LOCK_DIR" >&2
    exit 1
  fi
  sleep 1
done

cleanup() {
  rm -rf "$LOCK_DIR"
}
trap cleanup EXIT

printf '%s\n' "$$" > "$LOCK_DIR/pid"

"$@"
