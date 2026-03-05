#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

run_step() {
  local label="$1"
  shift
  echo "[github-wiki] $label"
  "$@"
}

cd "$ROOT"

run_step "syntax-boundary" ruby -c scripts/check_github_wiki_boundaries.rb
run_step "syntax-noise-cleanup" ruby -c scripts/clean_github_wiki_noise.rb
run_step "syntax-export" ruby -c scripts/export_github_wiki.rb
run_step "syntax-export-validate" ruby -c scripts/check_github_wiki_export.rb
run_step "syntax-publish" bash -n scripts/publish_github_wiki.sh
run_step "boundary-check" scripts/check_github_wiki_boundaries.rb
run_step "noise-cleanup" scripts/clean_github_wiki_noise.rb
run_step "export" scripts/export_github_wiki.rb
run_step "export-validate" scripts/check_github_wiki_export.rb

if [[ "${VERIFY_GITHUB_WIKI_BUILD:-0}" == "1" ]]; then
  run_step "jekyll-build" env BUNDLE_PATH="${BUNDLE_PATH:-vendor/bundle}" bundle exec jekyll build
fi
