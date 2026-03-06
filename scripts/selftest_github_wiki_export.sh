#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VALIDATOR="$ROOT/scripts/check_github_wiki_export.rb"
TEST_ROOT="$ROOT/ignore/github-wiki-export-selftest-$PPID-$$"
SRC_DIR="$TEST_ROOT/wiki"
DEST_DIR="$TEST_ROOT/github-wiki-export"
GITHUB_WIKI="https://github.com/yasufumi-nakata/mind-upload/wiki"

log() {
  echo "[github-wiki-export-selftest] $1"
}

fail() {
  echo "[github-wiki-export-selftest] $1" >&2
  exit 1
}

cleanup() {
  rm -rf "$TEST_ROOT"
}
trap cleanup EXIT

run_validator() {
  env \
    GITHUB_WIKI_EXPORT_SRC_DIR="$SRC_DIR" \
    GITHUB_WIKI_EXPORT_DEST_DIR="$DEST_DIR" \
    GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 \
    "$VALIDATOR"
}

run_expect_failure() {
  local label="$1"
  local expected="$2"
  local output

  log "$label"
  if output="$(run_validator 2>&1)"; then
    fail "Validator unexpectedly succeeded for $label."
  fi

  printf '%s\n' "$output"
  [[ "$output" == *"$expected"* ]] || fail "Expected failure not found for $label: $expected"
}

write_source_fixture() {
  rm -rf "$SRC_DIR"
  mkdir -p "$SRC_DIR/generated/demo"

  cat <<'EOF' > "$SRC_DIR/index.md"
# Home

home body
EOF

  cat <<'EOF' > "$SRC_DIR/page.md"
# Page

page body
EOF

  printf 'demo,data\n' > "$SRC_DIR/generated/demo/demo.csv"
}

write_export_fixture() {
  rm -rf "$DEST_DIR"
  mkdir -p "$DEST_DIR/generated/demo"

  cat <<EOF > "$DEST_DIR/Home.md"
# Home

[Page](${GITHUB_WIKI}/page)
EOF

  cat <<'EOF' > "$DEST_DIR/page.md"
# Page

ok
EOF

  cat <<EOF > "$DEST_DIR/_Sidebar.md"
# Sidebar

- [Home](${GITHUB_WIKI})
- [Page](${GITHUB_WIKI}/page)
EOF

  cat <<'EOF' > "$DEST_DIR/_Footer.md"
footer
EOF

  printf 'demo,data\n' > "$DEST_DIR/generated/demo/demo.csv"
}

reset_fixture() {
  write_source_fixture
  write_export_fixture
}

mkdir -p "$TEST_ROOT"

log "baseline-pass"
reset_fixture
run_validator >/dev/null

reset_fixture
rm -f "$DEST_DIR/page.md"
run_expect_failure "missing-page" "Missing exported page: page.md"

reset_fixture
touch "$DEST_DIR/.DS_Store"
run_expect_failure "noise-file" "Noise file in wiki export: .DS_Store"

reset_fixture
cat <<'EOF' > "$DEST_DIR/Home.md"
# Home

[Bad](relative/path.md)
EOF
run_expect_failure "unsafe-link" "Home.md: non-export-safe relative link relative/path.md"

reset_fixture
cat <<EOF > "$DEST_DIR/_Sidebar.md"
# Sidebar

- [Home](${GITHUB_WIKI})
EOF
run_expect_failure "sidebar-missing" "Sidebar missing link for page.md"

reset_fixture
rm -f "$DEST_DIR/generated/demo/demo.csv"
run_expect_failure "missing-generated-asset" "Missing generated asset in export: generated/demo/demo.csv"

log "ok"
