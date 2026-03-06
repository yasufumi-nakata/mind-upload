#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLEANER="$ROOT/scripts/clean_github_wiki_noise.rb"
TEST_ROOT="$ROOT/ignore/github-wiki-noise-selftest-$PPID-$$"
WIKI_DIR="$TEST_ROOT/wiki"
EXPORT_DIR="$TEST_ROOT/github-wiki-export"
TARGETS="$WIKI_DIR${PATH_SEPARATOR:-:}$EXPORT_DIR"

log() {
  echo "[github-wiki-noise-selftest] $1"
}

fail() {
  echo "[github-wiki-noise-selftest] $1" >&2
  exit 1
}

cleanup() {
  rm -rf "$TEST_ROOT"
}
trap cleanup EXIT

assert_file() {
  local path="$1"
  [[ -f "$path" ]] || fail "Missing file: $path"
}

assert_missing() {
  local path="$1"
  [[ ! -e "$path" ]] || fail "Unexpected file remains: $path"
}

assert_contains_text() {
  local text="$1"
  local expected="$2"
  [[ "$text" == *"$expected"* ]] || fail "Expected text not found: $expected"
}

write_fixture() {
  rm -rf "$TEST_ROOT"
  mkdir -p "$WIKI_DIR/nested" "$EXPORT_DIR/assets"

  printf 'keep\n' > "$WIKI_DIR/keep.md"
  printf 'keep\n' > "$EXPORT_DIR/assets/keep.csv"
  printf 'noise\n' > "$WIKI_DIR/.DS_Store"
  printf 'noise\n' > "$WIKI_DIR/nested/._page.md"
  printf 'noise\n' > "$EXPORT_DIR/.DS_Store"
  printf 'noise\n' > "$EXPORT_DIR/assets/._keep.csv"
}

run_cleaner() {
  env \
    GITHUB_WIKI_NOISE_ROOT="$TEST_ROOT" \
    GITHUB_WIKI_NOISE_TARGET_DIRS="$TARGETS" \
    "$CLEANER"
}

log "remove-noise"
write_fixture
output="$(run_cleaner)"
printf '%s\n' "$output"
assert_contains_text "$output" "Removed GitHub Wiki noise files:"
assert_contains_text "$output" "- wiki/.DS_Store"
assert_contains_text "$output" "- wiki/nested/._page.md"
assert_contains_text "$output" "- github-wiki-export/.DS_Store"
assert_contains_text "$output" "- github-wiki-export/assets/._keep.csv"
assert_missing "$WIKI_DIR/.DS_Store"
assert_missing "$WIKI_DIR/nested/._page.md"
assert_missing "$EXPORT_DIR/.DS_Store"
assert_missing "$EXPORT_DIR/assets/._keep.csv"
assert_file "$WIKI_DIR/keep.md"
assert_file "$EXPORT_DIR/assets/keep.csv"

log "no-noise"
output="$(run_cleaner)"
printf '%s\n' "$output"
assert_contains_text "$output" "No GitHub Wiki noise files found."

log "ok"
