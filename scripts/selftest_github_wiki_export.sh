#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VALIDATOR="$ROOT/scripts/check_github_wiki_export.rb"
TEST_ROOT="$ROOT/ignore/github-wiki-export-selftest-$PPID-$$"
SRC_DIR="$TEST_ROOT/wiki"
DEST_DIR="$TEST_ROOT/github-wiki-export"
DRIFT_ROOT="$TEST_ROOT/drift-repo"
DRIFT_SRC_DIR="$DRIFT_ROOT/wiki"
DRIFT_DEST_DIR="$DRIFT_ROOT/github-wiki-export"
DRIFT_VALIDATOR="$DRIFT_ROOT/scripts/check_github_wiki_export.rb"
NO_GIT_ROOT="$TEST_ROOT/no-git-root"
NO_GIT_SRC_DIR="$NO_GIT_ROOT/wiki"
NO_GIT_DEST_DIR="$NO_GIT_ROOT/github-wiki-export"
NO_GIT_VALIDATOR="$NO_GIT_ROOT/scripts/check_github_wiki_export.rb"
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

run_drift_validator() {
  env \
    GITHUB_WIKI_EXPORT_SRC_DIR="$DRIFT_SRC_DIR" \
    GITHUB_WIKI_EXPORT_DEST_DIR="$DRIFT_DEST_DIR" \
    "$DRIFT_VALIDATOR"
}

run_no_git_validator() {
  env \
    GITHUB_WIKI_EXPORT_SRC_DIR="$NO_GIT_SRC_DIR" \
    GITHUB_WIKI_EXPORT_DEST_DIR="$NO_GIT_DEST_DIR" \
    "$NO_GIT_VALIDATOR"
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

run_expect_drift_failure() {
  local label="$1"
  shift
  local output

  log "$label"
  if output="$(run_drift_validator 2>&1)"; then
    fail "Validator unexpectedly succeeded for $label."
  fi

  printf '%s\n' "$output"
  local expected
  for expected in "$@"; do
    [[ "$output" == *"$expected"* ]] || fail "Expected failure not found for $label: $expected"
  done
}

write_source_fixture() {
  local dir="$1"
  rm -rf "$dir"
  mkdir -p "$dir/generated/demo"

  cat <<'EOF' > "$dir/index.md"
# Home

home body
EOF

  cat <<'EOF' > "$dir/page.md"
# Page

page body
EOF

  printf 'demo,data\n' > "$dir/generated/demo/demo.csv"
}

write_export_fixture() {
  local dir="$1"
  rm -rf "$dir"
  mkdir -p "$dir/generated/demo"

  cat <<EOF > "$dir/Home.md"
# Home

[Page](${GITHUB_WIKI}/page)
EOF

  cat <<'EOF' > "$dir/page.md"
# Page

ok
EOF

  cat <<EOF > "$dir/_Sidebar.md"
# Sidebar

- [Home](${GITHUB_WIKI})
- [Page](${GITHUB_WIKI}/page)
EOF

  cat <<'EOF' > "$dir/_Footer.md"
footer
EOF

  printf 'demo,data\n' > "$dir/generated/demo/demo.csv"
}

reset_fixture() {
  write_source_fixture "$SRC_DIR"
  write_export_fixture "$DEST_DIR"
}

reset_drift_fixture() {
  rm -rf "$DRIFT_ROOT"
  mkdir -p "$DRIFT_ROOT/scripts"
  cp "$VALIDATOR" "$DRIFT_VALIDATOR"
  chmod +x "$DRIFT_VALIDATOR"
  write_source_fixture "$DRIFT_SRC_DIR"
  write_export_fixture "$DRIFT_DEST_DIR"
  git -C "$DRIFT_ROOT" init --initial-branch=main >/dev/null
  git -C "$DRIFT_ROOT" config user.name "GitHub Wiki Export Selftest"
  git -C "$DRIFT_ROOT" config user.email "wiki-selftest@example.com"
  git -C "$DRIFT_ROOT" add .
  git -C "$DRIFT_ROOT" commit -m "baseline" >/dev/null
}

reset_no_git_fixture() {
  rm -rf "$NO_GIT_ROOT"
  mkdir -p "$NO_GIT_ROOT/scripts"
  cp "$VALIDATOR" "$NO_GIT_VALIDATOR"
  chmod +x "$NO_GIT_VALIDATOR"
  write_source_fixture "$NO_GIT_SRC_DIR"
  write_export_fixture "$NO_GIT_DEST_DIR"
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

log "baseline-drift-pass"
reset_drift_fixture
run_drift_validator >/dev/null

log "staged-drift-ignored"
reset_drift_fixture
printf '\nstaged\n' >> "$DRIFT_DEST_DIR/Home.md"
git -C "$DRIFT_ROOT" add github-wiki-export/Home.md
printf 'staged\n' > "$DRIFT_DEST_DIR/staged-only.txt"
git -C "$DRIFT_ROOT" add github-wiki-export/staged-only.txt
run_drift_validator >/dev/null

reset_drift_fixture
printf '\nchanged\n' >> "$DRIFT_DEST_DIR/Home.md"
printf 'draft\n' > "$DRIFT_DEST_DIR/drift-untracked.txt"
run_expect_drift_failure \
  "unstaged-drift" \
  "Uncommitted export drift: M github-wiki-export/Home.md" \
  "Uncommitted export drift: ?? github-wiki-export/drift-untracked.txt"

log "skip-git-drift"
env \
  GITHUB_WIKI_EXPORT_SRC_DIR="$DRIFT_SRC_DIR" \
  GITHUB_WIKI_EXPORT_DEST_DIR="$DRIFT_DEST_DIR" \
  GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 \
  "$DRIFT_VALIDATOR" >/dev/null

log "non-git-root-skips-drift"
reset_no_git_fixture
printf '\nchanged\n' >> "$NO_GIT_DEST_DIR/Home.md"
printf 'draft\n' > "$NO_GIT_DEST_DIR/no-git-untracked.txt"
run_no_git_validator >/dev/null

log "ok"
