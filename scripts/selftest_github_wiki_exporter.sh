#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EXPORTER="$ROOT/scripts/export_github_wiki.rb"
TEST_ROOT="$ROOT/ignore/github-wiki-exporter-selftest-$PPID-$$"
SRC_DIR="$TEST_ROOT/wiki"
DEST_DIR="$TEST_ROOT/github-wiki-export"
PUBLIC_SITE="https://mind-upload.com"
GITHUB_WIKI="https://github.com/yasufumi-nakata/mind-upload/wiki"

log() {
  echo "[github-wiki-exporter-selftest] $1"
}

fail() {
  echo "[github-wiki-exporter-selftest] $1" >&2
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

assert_contains() {
  local path="$1"
  local expected="$2"
  grep -Fq "$expected" "$path" || fail "Expected text not found in $path: $expected"
}

assert_not_contains() {
  local path="$1"
  local unexpected="$2"
  if grep -Fq "$unexpected" "$path"; then
    fail "Unexpected text found in $path: $unexpected"
  fi
}

write_fixture() {
  rm -rf "$SRC_DIR" "$DEST_DIR"
  mkdir -p "$SRC_DIR/generated/demo"

  cat <<'EOF' > "$SRC_DIR/index.md"
---
title: はじめに
subtitle: 入口ページの概要
page_intro: このページは入口として機能します。
accuracy_note: 正確性を優先して読んでください。
recommended_pages:
  - label: データセット
    url: /datasets.html
    description: 公開ページへ戻ります。
wiki_links:
  - label: ガイド
    url: ./guide.html
    description: 補助 Wiki ページです。
known_points:
  - 既知の課題があります。
unknown_points:
  - 未解決の課題があります。
---
<main class="main-container">
  <article class="content-column">
    <!-- comment -->
    <div class="hero" id="hero" aria-label="hero" hidden>
      [ガイド](guide.html)
      [Wiki ホーム](/wiki/)
      [データセット](/datasets.html)
      <a href="./notes.html" class="cta">ノート</a>
    </div>
  </article>
  <aside class="sidebar-column">
    sidebar only
  </aside>
</main>
EOF

  cat <<'EOF' > "$SRC_DIR/guide.md"
---
title: ガイド
---
ガイド本文
EOF

  cat <<'EOF' > "$SRC_DIR/notes.md"
---
title: ノート
---
ノート本文
EOF

  cat <<'EOF' > "$SRC_DIR/ungrouped.md"
---
title: 未分類ページ
---
未分類本文
EOF

  printf 'demo,data\n' > "$SRC_DIR/generated/demo/demo.csv"
  touch "$SRC_DIR/generated/demo/.DS_Store"
  touch "$SRC_DIR/generated/demo/._demo.csv"
}

run_exporter() {
  local output
  output="$(
    env \
      GITHUB_WIKI_EXPORT_SRC_DIR="$SRC_DIR" \
      GITHUB_WIKI_EXPORT_DEST_DIR="$DEST_DIR" \
      "$EXPORTER" 2>&1
  )" || {
    printf '%s\n' "$output"
    fail "Exporter failed."
  }

  printf '%s\n' "$output"
  [[ "$output" == *"4 件の Wiki ページを $DEST_DIR へエクスポートしました"* ]] || fail "Unexpected exporter summary."
}

assert_output() {
  assert_file "$DEST_DIR/Home.md"
  assert_file "$DEST_DIR/guide.md"
  assert_file "$DEST_DIR/notes.md"
  assert_file "$DEST_DIR/ungrouped.md"
  assert_file "$DEST_DIR/_Sidebar.md"
  assert_file "$DEST_DIR/_Footer.md"
  assert_file "$DEST_DIR/generated/demo/demo.csv"

  assert_contains "$DEST_DIR/Home.md" "# はじめに"
  assert_contains "$DEST_DIR/Home.md" "> 入口ページの概要"
  assert_contains "$DEST_DIR/Home.md" "## このページの役割"
  assert_contains "$DEST_DIR/Home.md" "## 正確性に関する注記"
  assert_contains "$DEST_DIR/Home.md" "## 公開ページへ戻る"
  assert_contains "$DEST_DIR/Home.md" "## 関連 Wiki ページ"
  assert_contains "$DEST_DIR/Home.md" "## 現在わかっていること"
  assert_contains "$DEST_DIR/Home.md" "## まだわかっていないこと"
  assert_contains "$DEST_DIR/Home.md" "[ガイド](${GITHUB_WIKI}/guide)"
  assert_contains "$DEST_DIR/Home.md" "[Wiki ホーム](${GITHUB_WIKI})"
  assert_contains "$DEST_DIR/Home.md" "[データセット](${PUBLIC_SITE}/datasets.html)"
  assert_contains "$DEST_DIR/Home.md" "href=\"${GITHUB_WIKI}/notes\""
  assert_not_contains "$DEST_DIR/Home.md" "<main"
  assert_not_contains "$DEST_DIR/Home.md" "<article"
  assert_not_contains "$DEST_DIR/Home.md" "<aside"
  assert_not_contains "$DEST_DIR/Home.md" "class=\""
  assert_not_contains "$DEST_DIR/Home.md" "id=\""
  assert_not_contains "$DEST_DIR/Home.md" "aria-label="
  assert_not_contains "$DEST_DIR/Home.md" "hidden"
  assert_not_contains "$DEST_DIR/Home.md" "<!--"

  assert_contains "$DEST_DIR/_Sidebar.md" "## 開始とナビゲーション"
  assert_contains "$DEST_DIR/_Sidebar.md" "[はじめに](${GITHUB_WIKI})"
  assert_contains "$DEST_DIR/_Sidebar.md" "## その他"
  assert_contains "$DEST_DIR/_Sidebar.md" "[ガイド](${GITHUB_WIKI}/guide)"
  assert_contains "$DEST_DIR/_Sidebar.md" "[ノート](${GITHUB_WIKI}/notes)"
  assert_contains "$DEST_DIR/_Sidebar.md" "[未分類ページ](${GITHUB_WIKI}/ungrouped)"
  assert_not_contains "$DEST_DIR/_Sidebar.md" "mind-upload-basics"

  assert_contains "$DEST_DIR/_Footer.md" "公開ポータル"
  [[ ! -e "$DEST_DIR/generated/demo/.DS_Store" ]] || fail "Noise file copied into export: .DS_Store"
  [[ ! -e "$DEST_DIR/generated/demo/._demo.csv" ]] || fail "Noise file copied into export: ._demo.csv"
}

mkdir -p "$TEST_ROOT"

log "run"
write_fixture
run_exporter
assert_output
log "ok"
