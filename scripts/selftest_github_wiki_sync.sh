#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEST_ROOT="$ROOT/ignore/github-wiki-sync-selftest-$PPID-$$"
FIXTURE_SCRIPTS="$TEST_ROOT/scripts"
FIXTURE_SYNC="$FIXTURE_SCRIPTS/sync_github_wiki_toolchain.sh"
LOG_FILE="$TEST_ROOT/run.log"
LOCK_DIR="$TEST_ROOT/ignore/github-wiki-toolchain.lock"

log() {
  echo "[github-wiki-sync-selftest] $1"
}

fail() {
  echo "[github-wiki-sync-selftest] $1" >&2
  exit 1
}

cleanup() {
  rm -rf "$TEST_ROOT"
}
trap cleanup EXIT

assert_log_equals() {
  local expected="$1"
  local actual
  actual="$(cat "$LOG_FILE" 2>/dev/null || true)"
  [[ "$actual" == "$expected" ]] || fail "Unexpected log contents:\n$actual"
}

assert_log_contains_line() {
  local expected="$1"
  grep -Fxq "$expected" "$LOG_FILE" || fail "Expected log line not found: $expected"
}

assert_log_not_contains_line() {
  local unexpected="$1"
  if grep -Fxq "$unexpected" "$LOG_FILE" 2>/dev/null; then
    fail "Unexpected log line found: $unexpected"
  fi
}

write_stub() {
  local path="$1"
  local body="$2"
  printf '%s\n' "$body" > "$path"
  chmod +x "$path"
}

prepare_fixture() {
  rm -rf "$TEST_ROOT"
  mkdir -p "$FIXTURE_SCRIPTS" "$TEST_ROOT/ignore"
  cp "$ROOT/scripts/sync_github_wiki_toolchain.sh" "$FIXTURE_SYNC"
  cp "$ROOT/scripts/with_github_wiki_lock.sh" "$FIXTURE_SCRIPTS/with_github_wiki_lock.sh"
  : > "$LOG_FILE"

  write_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_lock.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" != \"1\" ]] || exit 41
printf '%s\n' 'lock-selftest' >> '$LOG_FILE'
"

  write_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_boundaries.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" != \"1\" ]] || exit 42
printf '%s\n' 'boundary-selftest' >> '$LOG_FILE'
"

  write_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_noise.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" != \"1\" ]] || exit 43
printf '%s\n' 'noise-selftest' >> '$LOG_FILE'
"

  write_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_ops_references.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" != \"1\" ]] || exit 44
printf '%s\n' 'ops-selftest' >> '$LOG_FILE'
"

  write_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_exporter.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" != \"1\" ]] || exit 45
printf '%s\n' 'exporter-selftest' >> '$LOG_FILE'
"

  write_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_export.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" != \"1\" ]] || exit 46
printf '%s\n' 'export-selftest' >> '$LOG_FILE'
"

  write_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_publish.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" != \"1\" ]] || exit 47
printf '%s\n' 'publish-selftest' >> '$LOG_FILE'
"

  write_stub "$FIXTURE_SCRIPTS/verify_github_wiki_toolchain.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" == \"1\" ]] || exit 51
printf '%s\n' 'verify' >> '$LOG_FILE'
if [[ \"\${SELFTEST_VERIFY_FAIL:-0}\" == \"1\" ]]; then
  exit 91
fi
"

  write_stub "$FIXTURE_SCRIPTS/publish_github_wiki.sh" "#!/usr/bin/env bash
set -euo pipefail
[[ \"\${GITHUB_WIKI_LOCK_HELD:-0}\" == \"1\" ]] || exit 52
printf '%s\n' 'publish' >> '$LOG_FILE'
"
}

run_sync_success() {
  log "success"
  prepare_fixture
  env \
    VERIFY_GITHUB_WIKI_SYNC_SELFTEST=0 \
    VERIFY_GITHUB_WIKI_LOCK_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_NOISE_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_OPS_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_EXPORT_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST=1 \
    "$FIXTURE_SYNC" >/dev/null

  assert_log_equals "$(cat <<'EOF'
lock-selftest
boundary-selftest
noise-selftest
ops-selftest
exporter-selftest
export-selftest
publish-selftest
verify
publish
EOF
)"
  [[ ! -d "$LOCK_DIR" ]] || fail "Lock directory still exists after successful sync."
}

run_sync_verify_failure() {
  log "verify-failure"
  prepare_fixture
  if env \
    VERIFY_GITHUB_WIKI_SYNC_SELFTEST=0 \
    SELFTEST_VERIFY_FAIL=1 \
    "$FIXTURE_SYNC" >/dev/null 2>&1; then
    fail "Sync unexpectedly succeeded when verify failed."
  fi

  assert_log_contains_line "verify"
  assert_log_not_contains_line "publish"
  [[ ! -d "$LOCK_DIR" ]] || fail "Lock directory still exists after failed sync."
}

run_sync_success
run_sync_verify_failure
log "ok"
