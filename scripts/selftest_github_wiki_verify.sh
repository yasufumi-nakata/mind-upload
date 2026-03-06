#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEST_ROOT="$ROOT/ignore/github-wiki-verify-selftest-$PPID-$$"
FIXTURE_SCRIPTS="$TEST_ROOT/scripts"
FIXTURE_BIN="$TEST_ROOT/bin"
FIXTURE_VERIFY="$FIXTURE_SCRIPTS/verify_github_wiki_toolchain.sh"
LOG_FILE="$TEST_ROOT/run.log"
OUTPUT_FILE="$TEST_ROOT/output.log"
LOCK_DIR="$TEST_ROOT/ignore/github-wiki-toolchain.lock"

log() {
  echo "[github-wiki-verify-selftest] $1"
}

fail() {
  echo "[github-wiki-verify-selftest] $1" >&2
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

assert_output_contains_in_order() {
  local previous_line=0
  local expected

  for expected in "$@"; do
    local line_number
    line_number="$(grep -nF "$expected" "$OUTPUT_FILE" | head -n1 | cut -d: -f1 || true)"
    [[ -n "$line_number" ]] || fail "Expected output line not found: $expected"
    (( line_number > previous_line )) || fail "Output line out of order: $expected"
    previous_line="$line_number"
  done
}

assert_output_not_contains() {
  local unexpected="$1"
  if grep -Fq "$unexpected" "$OUTPUT_FILE" 2>/dev/null; then
    fail "Unexpected output found: $unexpected"
  fi
}

write_shell_stub() {
  local path="$1"
  local expected_lock="$2"
  local exit_code="$3"
  local label="$4"

  cat > "$path" <<EOF
#!/usr/bin/env bash
set -euo pipefail
[[ "\${GITHUB_WIKI_LOCK_HELD:-0}" == "$expected_lock" ]] || exit $exit_code
printf '%s\n' '$label' >> '$LOG_FILE'
EOF
  chmod +x "$path"
}

write_ruby_stub() {
  local path="$1"
  local expected_lock="$2"
  local exit_code="$3"
  local label="$4"
  local fail_env="${5:-}"

  cat > "$path" <<EOF
#!/usr/bin/env ruby
lock = ENV.fetch("GITHUB_WIKI_LOCK_HELD", "0")
exit $exit_code unless lock == "$expected_lock"
File.open("$LOG_FILE", "a") do |file|
  file.puts("$label")
end
EOF
  if [[ -n "$fail_env" ]]; then
    cat >> "$path" <<EOF
exit 91 if ENV.fetch("$fail_env", "0") == "1"
EOF
  fi
  chmod +x "$path"
}

prepare_fixture() {
  rm -rf "$TEST_ROOT"
  mkdir -p "$FIXTURE_SCRIPTS" "$FIXTURE_BIN" "$TEST_ROOT/ignore"
  cp "$ROOT/scripts/verify_github_wiki_toolchain.sh" "$FIXTURE_VERIFY"
  cp "$ROOT/scripts/with_github_wiki_lock.sh" "$FIXTURE_SCRIPTS/with_github_wiki_lock.sh"
  : > "$LOG_FILE"
  : > "$OUTPUT_FILE"

  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_lock.sh" "0" 41 "lock-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_sync.sh" "0" 42 "sync-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_verify.sh" "0" 43 "verify-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_boundaries.sh" "0" 44 "boundary-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_noise.sh" "0" 45 "noise-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_ops_references.sh" "0" 46 "ops-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_exporter.sh" "0" 47 "exporter-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_export.sh" "0" 48 "export-selftest"
  write_shell_stub "$FIXTURE_SCRIPTS/selftest_github_wiki_publish.sh" "0" 49 "publish-selftest"

  write_ruby_stub "$FIXTURE_SCRIPTS/check_github_wiki_boundaries.rb" "1" 51 "boundary-check" "SELFTEST_BOUNDARY_FAIL"
  write_ruby_stub "$FIXTURE_SCRIPTS/check_github_wiki_ops_references.rb" "1" 52 "ops-reference-check"
  write_ruby_stub "$FIXTURE_SCRIPTS/clean_github_wiki_noise.rb" "1" 53 "noise-cleanup"
  write_ruby_stub "$FIXTURE_SCRIPTS/export_github_wiki.rb" "1" 54 "export"
  write_ruby_stub "$FIXTURE_SCRIPTS/check_github_wiki_export.rb" "1" 55 "export-validate"

  cat > "$FIXTURE_SCRIPTS/publish_github_wiki.sh" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
exit 0
EOF
  chmod +x "$FIXTURE_SCRIPTS/publish_github_wiki.sh"

  cat > "$FIXTURE_BIN/bundle" <<EOF
#!/usr/bin/env bash
set -euo pipefail
[[ "\${GITHUB_WIKI_LOCK_HELD:-0}" == "1" ]] || exit 81
[[ "\${BUNDLE_PATH:-}" == "vendor/bundle" ]] || exit 82
[[ "\$#" -eq 3 && "\$1" == "exec" && "\$2" == "jekyll" && "\$3" == "build" ]] || exit 83
printf '%s\n' 'build' >> '$LOG_FILE'
EOF
  chmod +x "$FIXTURE_BIN/bundle"
}

run_verify_no_build() {
  log "success-without-build"
  prepare_fixture
  env \
    PATH="$FIXTURE_BIN:$PATH" \
    VERIFY_GITHUB_WIKI_LOCK_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_SYNC_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_VERIFY_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_BUILD=0 \
    VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_NOISE_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_OPS_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_EXPORT_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST=1 \
    "$FIXTURE_VERIFY" >"$OUTPUT_FILE" 2>&1

  assert_log_equals "$(cat <<'EOF'
lock-selftest
sync-selftest
verify-selftest
boundary-selftest
noise-selftest
ops-selftest
exporter-selftest
export-selftest
publish-selftest
boundary-check
ops-reference-check
noise-cleanup
export
export-validate
EOF
)"
  assert_output_contains_in_order \
    "[github-wiki] lock-selftest" \
    "[github-wiki] sync-selftest" \
    "[github-wiki] verify-selftest" \
    "[github-wiki] boundary-selftest" \
    "[github-wiki] syntax-boundary" \
    "[github-wiki] syntax-sync-selftest" \
    "[github-wiki] syntax-publish" \
    "[github-wiki] boundary-check" \
    "[github-wiki] export-validate"
  assert_output_not_contains "[github-wiki] jekyll-build"
  assert_log_not_contains_line "build"
  [[ ! -d "$LOCK_DIR" ]] || fail "Lock directory still exists after successful verify without build."
}

run_verify_with_build() {
  log "success-with-build"
  prepare_fixture
  env \
    PATH="$FIXTURE_BIN:$PATH" \
    VERIFY_GITHUB_WIKI_LOCK_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_SYNC_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_VERIFY_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_NOISE_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_OPS_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_EXPORT_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_BUILD=1 \
    "$FIXTURE_VERIFY" >"$OUTPUT_FILE" 2>&1

  assert_log_equals "$(cat <<'EOF'
lock-selftest
sync-selftest
verify-selftest
boundary-selftest
noise-selftest
ops-selftest
exporter-selftest
export-selftest
publish-selftest
boundary-check
ops-reference-check
noise-cleanup
export
export-validate
build
EOF
)"
  assert_output_contains_in_order \
    "[github-wiki] lock-selftest" \
    "[github-wiki] verify-selftest" \
    "[github-wiki] syntax-export-validate" \
    "[github-wiki] boundary-check" \
    "[github-wiki] export-validate" \
    "[github-wiki] jekyll-build"
  [[ ! -d "$LOCK_DIR" ]] || fail "Lock directory still exists after successful verify with build."
}

run_verify_boundary_failure() {
  log "boundary-failure"
  prepare_fixture
  if env \
    PATH="$FIXTURE_BIN:$PATH" \
    VERIFY_GITHUB_WIKI_VERIFY_SELFTEST=1 \
    VERIFY_GITHUB_WIKI_BUILD=0 \
    SELFTEST_BOUNDARY_FAIL=1 \
    "$FIXTURE_VERIFY" >"$OUTPUT_FILE" 2>&1; then
    fail "Verify unexpectedly succeeded when boundary check failed."
  fi

  assert_log_contains_line "verify-selftest"
  assert_log_contains_line "boundary-check"
  assert_log_not_contains_line "ops-reference-check"
  assert_log_not_contains_line "build"
  assert_output_contains_in_order \
    "[github-wiki] verify-selftest" \
    "[github-wiki] syntax-boundary" \
    "[github-wiki] boundary-check"
  assert_output_not_contains "[github-wiki] ops-reference-check"
  [[ ! -d "$LOCK_DIR" ]] || fail "Lock directory still exists after failed verify."
}

run_verify_no_build
run_verify_with_build
run_verify_boundary_failure
log "ok"
