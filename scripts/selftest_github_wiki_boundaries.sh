#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHECKER="$ROOT/scripts/check_github_wiki_boundaries.rb"
TEST_ROOT="$ROOT/ignore/github-wiki-boundary-selftest-$PPID-$$"

log() {
  echo "[github-wiki-boundary-selftest] $1"
}

fail() {
  echo "[github-wiki-boundary-selftest] $1" >&2
  exit 1
}

cleanup() {
  rm -rf "$TEST_ROOT"
}
trap cleanup EXIT

run_checker() {
  env GITHUB_WIKI_BOUNDARY_ROOT="$TEST_ROOT" "$CHECKER"
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

copy_fixture() {
  rm -rf "$TEST_ROOT"
  mkdir -p "$TEST_ROOT/scripts" "$TEST_ROOT/.github/workflows"
  cp -R "$ROOT/scripts/." "$TEST_ROOT/scripts/"
  cp "$ROOT/README.md" "$TEST_ROOT/README.md"
  cp "$ROOT/.github/workflows/validate-github-wiki-export.yml" "$TEST_ROOT/.github/workflows/validate-github-wiki-export.yml"
  cp "$ROOT/.github/workflows/sync-github-wiki.yml" "$TEST_ROOT/.github/workflows/sync-github-wiki.yml"
}

log "baseline-pass"
copy_fixture
run_checker >/dev/null

copy_fixture
rm -f "$TEST_ROOT/scripts/publish_github_wiki.sh"
run_expect_failure "missing-target" "scripts/publish_github_wiki.sh"

copy_fixture
perl -0pi -e 's/\n\s*VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST: "1"//' "$TEST_ROOT/.github/workflows/validate-github-wiki-export.yml"
run_expect_failure "missing-verify-guard" 'Missing verify workflow guard snippet: VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST: "1"'

copy_fixture
perl -0pi -e 's/\n\s*VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST: "1"//' "$TEST_ROOT/.github/workflows/sync-github-wiki.yml"
run_expect_failure "missing-sync-guard" 'Missing sync workflow guard snippet: VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST: "1"'

copy_fixture
cat <<'EOF' >> "$TEST_ROOT/scripts/publish_github_wiki.sh"
TMP_DIR="$(mktemp -d)"
EOF
run_expect_failure "publish-mktemp-regression" 'Forbidden temp directory helper remains: mktemp'

copy_fixture
perl -0pi -e 's/`VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1`//g' "$TEST_ROOT/README.md"
run_expect_failure "missing-readme-note" 'Missing README boundary note: `VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1`'

log "ok"
