#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

run_step() {
  local label="$1"
  shift
  echo "[github-wiki-sync] $label"
  "$@"
}

cd "$ROOT"

run_step "verify" scripts/verify_github_wiki_toolchain.sh
run_step "publish" scripts/publish_github_wiki.sh
