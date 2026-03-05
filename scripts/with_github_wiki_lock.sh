#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOCK_DIR="$ROOT/ignore/github-wiki-toolchain.lock"
WAIT_SECONDS="${GITHUB_WIKI_LOCK_WAIT_SECONDS:-180}"
START_TIME="$(date +%s)"

if [[ "$#" -eq 0 ]]; then
  echo "Usage: scripts/with_github_wiki_lock.sh <command> [args...]" >&2
  exit 1
fi

mkdir -p "$ROOT/ignore"

while ! mkdir "$LOCK_DIR" 2>/dev/null; do
  if [[ -f "$LOCK_DIR/pid" ]]; then
    LOCK_PID="$(cat "$LOCK_DIR/pid" 2>/dev/null || true)"
    if [[ -n "$LOCK_PID" ]] && ! kill -0 "$LOCK_PID" 2>/dev/null; then
      rm -rf "$LOCK_DIR"
      continue
    fi
  fi

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
