#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"

run_step() {
  local label="$1"
  shift
  echo "[github-wiki-sync] $label"
  "$@"
}

cd "$ROOT"

if [[ "${GITHUB_WIKI_LOCK_HELD:-0}" != "1" ]]; then
  if [[ "${VERIFY_GITHUB_WIKI_LOCK_SELFTEST:-0}" == "1" ]]; then
    run_step "lock-selftest" scripts/selftest_github_wiki_lock.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_SYNC_SELFTEST:-0}" == "1" ]]; then
    run_step "sync-selftest" scripts/selftest_github_wiki_sync.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_VERIFY_SELFTEST:-0}" == "1" ]]; then
    run_step "verify-selftest" scripts/selftest_github_wiki_verify.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST:-0}" == "1" ]]; then
    run_step "boundary-selftest" scripts/selftest_github_wiki_boundaries.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_NOISE_SELFTEST:-0}" == "1" ]]; then
    run_step "noise-selftest" scripts/selftest_github_wiki_noise.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_OPS_SELFTEST:-0}" == "1" ]]; then
    run_step "ops-selftest" scripts/selftest_github_wiki_ops_references.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST:-0}" == "1" ]]; then
    run_step "exporter-selftest" scripts/selftest_github_wiki_exporter.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_EXPORT_SELFTEST:-0}" == "1" ]]; then
    run_step "export-selftest" scripts/selftest_github_wiki_export.sh
  fi
  if [[ "${VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST:-0}" == "1" ]]; then
    run_step "publish-selftest" scripts/selftest_github_wiki_publish.sh
  fi
  exec env GITHUB_WIKI_LOCK_HELD=1 "$ROOT/scripts/with_github_wiki_lock.sh" "$SCRIPT_PATH" "$@"
fi

run_step "verify" scripts/verify_github_wiki_toolchain.sh
run_step "publish" scripts/publish_github_wiki.sh
