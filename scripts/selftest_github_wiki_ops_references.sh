#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHECKER="$ROOT/scripts/check_github_wiki_ops_references.rb"
TEST_ROOT="$ROOT/ignore/github-wiki-ops-refs-selftest-$PPID-$$"
TARGETS="README.md${PATH_SEPARATOR:-:}ops.md"

log() {
  echo "[github-wiki-ops-refs-selftest] $1"
}

fail() {
  echo "[github-wiki-ops-refs-selftest] $1" >&2
  exit 1
}

cleanup() {
  rm -rf "$TEST_ROOT"
}
trap cleanup EXIT

run_checker() {
  env \
    GITHUB_WIKI_OPS_REFERENCE_ROOT="$TEST_ROOT" \
    GITHUB_WIKI_OPS_REFERENCE_FILES="$TARGETS" \
    "$CHECKER"
}

run_expect_failure() {
  local label="$1"
  local expected="$2"
  local output

  log "$label"
  if output="$(run_checker 2>&1)"; then
    fail "Checker unexpectedly succeeded for $label."
  fi

  printf '%s\n' "$output"
  [[ "$output" == *"$expected"* ]] || fail "Expected failure not found for $label: $expected"
}

write_clean_fixture() {
  rm -rf "$TEST_ROOT"
  mkdir -p "$TEST_ROOT"

  cat <<'EOF' > "$TEST_ROOT/README.md"
safe readme
EOF

  cat <<'EOF' > "$TEST_ROOT/ops.md"
safe ops note
EOF
}

mkdir -p "$TEST_ROOT"

log "baseline-pass"
write_clean_fixture
run_checker >/dev/null

write_clean_fixture
DOT_DOT=".."
printf 'bad path %s/wiki is back\n' "$DOT_DOT" > "$TEST_ROOT/README.md"
run_expect_failure "external-wiki-path" "Forbidden external wiki path reference: README.md"

write_clean_fixture
LEGACY_OWNER="AoyamaLab"
printf 'legacy remote %s/wiki should not appear\n' "$LEGACY_OWNER" > "$TEST_ROOT/ops.md"
run_expect_failure "legacy-remote" "Forbidden legacy wiki remote reference: ops.md"

write_clean_fixture
rm -f "$TEST_ROOT/ops.md"
run_expect_failure "missing-target" "Missing ops reference target: ops.md"

log "ok"
