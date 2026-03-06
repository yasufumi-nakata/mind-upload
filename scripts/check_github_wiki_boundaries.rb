#!/usr/bin/env ruby
# frozen_string_literal: true

SCRIPT_ROOT = File.expand_path("..", __dir__)
ROOT = File.expand_path(ENV.fetch("GITHUB_WIKI_BOUNDARY_ROOT", SCRIPT_ROOT))
PUBLISH_SCRIPT = File.join(ROOT, "scripts", "publish_github_wiki.sh")
VERIFY_SCRIPT = File.join(ROOT, "scripts", "verify_github_wiki_toolchain.sh")
SYNC_SCRIPT = File.join(ROOT, "scripts", "sync_github_wiki_toolchain.sh")
OPS_REFERENCE_SCRIPT = File.join(ROOT, "scripts", "check_github_wiki_ops_references.rb")
LOCK_SCRIPT = File.join(ROOT, "scripts", "with_github_wiki_lock.sh")
LOCK_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_lock.sh")
BOUNDARY_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_boundaries.sh")
NOISE_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_noise.sh")
OPS_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_ops_references.sh")
EXPORTER_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_exporter.sh")
EXPORT_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_export.sh")
PUBLISH_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_publish.sh")
VERIFY_WORKFLOW = File.join(ROOT, ".github", "workflows", "validate-github-wiki-export.yml")
SYNC_WORKFLOW = File.join(ROOT, ".github", "workflows", "sync-github-wiki.yml")
README = File.join(ROOT, "README.md")

[
  PUBLISH_SCRIPT,
  VERIFY_SCRIPT,
  SYNC_SCRIPT,
  OPS_REFERENCE_SCRIPT,
  LOCK_SCRIPT,
  LOCK_SELFTEST_SCRIPT,
  BOUNDARY_SELFTEST_SCRIPT,
  NOISE_SELFTEST_SCRIPT,
  OPS_SELFTEST_SCRIPT,
  EXPORTER_SELFTEST_SCRIPT,
  EXPORT_SELFTEST_SCRIPT,
  PUBLISH_SELFTEST_SCRIPT,
  VERIFY_WORKFLOW,
  SYNC_WORKFLOW,
  README
].each do |path|
  next if File.exist?(path)

  warn "Missing boundary target: #{path}"
  exit 1
end

errors = []

publish_text = File.read(PUBLISH_SCRIPT)

required_publish_snippets = [
  'DEFAULT_REMOTE_BASE="https://github.com/yasufumi-nakata/mind-upload.wiki.git"',
  'REMOTE_BASE="${GITHUB_WIKI_REMOTE_BASE:-$DEFAULT_REMOTE_BASE}"',
  'REMOTE_URL="$REMOTE_BASE"',
  'elif [[ "$REMOTE_BASE" == https://github.com/* ]]; then',
  'REMOTE_URL="https://x-access-token:${TOKEN}@${REMOTE_BASE#https://}"',
  'WORK_ROOT="$ROOT/ignore/github-wiki-publish"',
  'WORK_DIR="$WORK_ROOT/repo"',
  'if [[ -n "${GITHUB_WIKI_REMOTE_URL:-}" ]]; then',
  'REMOTE_URL="${GITHUB_WIKI_REMOTE_URL}"',
  'git clone "$REMOTE_URL" "$WORK_DIR"',
  'rsync -a --delete --exclude ".git/" --exclude ".DS_Store" "$EXPORT_DIR"/ "$WORK_DIR"/',
  'find "$WORK_DIR" -name ".DS_Store" -delete',
  'GitHub Wiki の作業先はリポジトリ内に固定しています'
]

required_publish_snippets.each do |snippet|
  errors << "Missing publish guard snippet: #{snippet}" unless publish_text.include?(snippet)
end

forbidden_publish_patterns = {
  /GITHUB_WIKI_WORKDIR/ => "Forbidden override remains: GITHUB_WIKI_WORKDIR",
  /\bmktemp\b/ => "Forbidden temp directory helper remains: mktemp",
  %r{\$TMP_DIR/wiki} => "Forbidden temp wiki checkout path remains: $TMP_DIR/wiki"
}

forbidden_publish_patterns.each do |pattern, message|
  errors << message if publish_text.match?(pattern)
end

verify_script_text = File.read(VERIFY_SCRIPT)
required_verify_script_snippets = [
  'if [[ "${VERIFY_GITHUB_WIKI_LOCK_SELFTEST:-0}" == "1" ]]; then',
  'run_step "lock-selftest" scripts/selftest_github_wiki_lock.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST:-0}" == "1" ]]; then',
  'run_step "boundary-selftest" scripts/selftest_github_wiki_boundaries.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_NOISE_SELFTEST:-0}" == "1" ]]; then',
  'run_step "noise-selftest" scripts/selftest_github_wiki_noise.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_OPS_SELFTEST:-0}" == "1" ]]; then',
  'run_step "ops-selftest" scripts/selftest_github_wiki_ops_references.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST:-0}" == "1" ]]; then',
  'run_step "exporter-selftest" scripts/selftest_github_wiki_exporter.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_EXPORT_SELFTEST:-0}" == "1" ]]; then',
  'run_step "export-selftest" scripts/selftest_github_wiki_export.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST:-0}" == "1" ]]; then',
  'run_step "publish-selftest" scripts/selftest_github_wiki_publish.sh',
  'exec env GITHUB_WIKI_LOCK_HELD=1 "$ROOT/scripts/with_github_wiki_lock.sh" "$SCRIPT_PATH" "$@"',
  'run_step "syntax-boundary" ruby -c scripts/check_github_wiki_boundaries.rb',
  'run_step "syntax-ops-refs" ruby -c scripts/check_github_wiki_ops_references.rb',
  'run_step "syntax-noise-cleanup" ruby -c scripts/clean_github_wiki_noise.rb',
  'run_step "syntax-export" ruby -c scripts/export_github_wiki.rb',
  'run_step "syntax-export-validate" ruby -c scripts/check_github_wiki_export.rb',
  'run_step "syntax-lock-selftest" bash -n scripts/selftest_github_wiki_lock.sh',
  'run_step "syntax-boundary-selftest" bash -n scripts/selftest_github_wiki_boundaries.sh',
  'run_step "syntax-noise-selftest" bash -n scripts/selftest_github_wiki_noise.sh',
  'run_step "syntax-ops-selftest" bash -n scripts/selftest_github_wiki_ops_references.sh',
  'run_step "syntax-exporter-selftest" bash -n scripts/selftest_github_wiki_exporter.sh',
  'run_step "syntax-export-selftest" bash -n scripts/selftest_github_wiki_export.sh',
  'run_step "syntax-publish-selftest" bash -n scripts/selftest_github_wiki_publish.sh',
  'run_step "syntax-publish" bash -n scripts/publish_github_wiki.sh',
  'run_step "boundary-check" scripts/check_github_wiki_boundaries.rb',
  'run_step "ops-reference-check" scripts/check_github_wiki_ops_references.rb',
  'run_step "noise-cleanup" scripts/clean_github_wiki_noise.rb',
  'run_step "export" scripts/export_github_wiki.rb',
  'run_step "export-validate" scripts/check_github_wiki_export.rb',
  'env BUNDLE_PATH="${BUNDLE_PATH:-vendor/bundle}" bundle exec jekyll build'
]

required_verify_script_snippets.each do |snippet|
  errors << "Missing verify script guard snippet: #{snippet}" unless verify_script_text.include?(snippet)
end

sync_script_text = File.read(SYNC_SCRIPT)
required_sync_script_snippets = [
  'if [[ "${VERIFY_GITHUB_WIKI_LOCK_SELFTEST:-0}" == "1" ]]; then',
  'run_step "lock-selftest" scripts/selftest_github_wiki_lock.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST:-0}" == "1" ]]; then',
  'run_step "boundary-selftest" scripts/selftest_github_wiki_boundaries.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_NOISE_SELFTEST:-0}" == "1" ]]; then',
  'run_step "noise-selftest" scripts/selftest_github_wiki_noise.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_OPS_SELFTEST:-0}" == "1" ]]; then',
  'run_step "ops-selftest" scripts/selftest_github_wiki_ops_references.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST:-0}" == "1" ]]; then',
  'run_step "exporter-selftest" scripts/selftest_github_wiki_exporter.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_EXPORT_SELFTEST:-0}" == "1" ]]; then',
  'run_step "export-selftest" scripts/selftest_github_wiki_export.sh',
  'if [[ "${VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST:-0}" == "1" ]]; then',
  'run_step "publish-selftest" scripts/selftest_github_wiki_publish.sh',
  'exec env GITHUB_WIKI_LOCK_HELD=1 "$ROOT/scripts/with_github_wiki_lock.sh" "$SCRIPT_PATH" "$@"',
  'run_step "verify" scripts/verify_github_wiki_toolchain.sh',
  'run_step "publish" scripts/publish_github_wiki.sh'
]

required_sync_script_snippets.each do |snippet|
  errors << "Missing sync script guard snippet: #{snippet}" unless sync_script_text.include?(snippet)
end

verify_workflow_text = File.read(VERIFY_WORKFLOW)
required_verify_workflow_snippets = [
  'run: scripts/verify_github_wiki_toolchain.sh',
  'VERIFY_GITHUB_WIKI_BUILD: "1"',
  'VERIFY_GITHUB_WIKI_LOCK_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_NOISE_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_OPS_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_EXPORT_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST: "1"'
]

required_verify_workflow_snippets.each do |snippet|
  errors << "Missing verify workflow guard snippet: #{snippet}" unless verify_workflow_text.include?(snippet)
end

required_verify_workflow_paths = [
  '"scripts/export_github_wiki.rb"',
  '"scripts/check_github_wiki_export.rb"',
  '"scripts/check_github_wiki_boundaries.rb"',
  '"scripts/check_github_wiki_ops_references.rb"',
  '"scripts/clean_github_wiki_noise.rb"',
  '"scripts/with_github_wiki_lock.sh"',
  '"scripts/selftest_github_wiki_lock.sh"',
  '"scripts/selftest_github_wiki_boundaries.sh"',
  '"scripts/selftest_github_wiki_noise.sh"',
  '"scripts/selftest_github_wiki_ops_references.sh"',
  '"scripts/selftest_github_wiki_exporter.sh"',
  '"scripts/selftest_github_wiki_export.sh"',
  '"scripts/selftest_github_wiki_publish.sh"',
  '"scripts/verify_github_wiki_toolchain.sh"',
  '"scripts/sync_github_wiki_toolchain.sh"',
  '"scripts/publish_github_wiki.sh"'
]

required_verify_workflow_paths.each do |snippet|
  errors << "Missing verify workflow path trigger: #{snippet}" unless verify_workflow_text.include?(snippet)
end

sync_workflow_text = File.read(SYNC_WORKFLOW)
required_sync_workflow_snippets = [
  'run: |',
  'scripts/sync_github_wiki_toolchain.sh',
  'VERIFY_GITHUB_WIKI_LOCK_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_NOISE_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_OPS_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_EXPORT_SELFTEST: "1"',
  'VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST: "1"'
]

required_sync_workflow_snippets.each do |snippet|
  errors << "Missing sync workflow guard snippet: #{snippet}" unless sync_workflow_text.include?(snippet)
end

required_sync_workflow_paths = [
  '"scripts/export_github_wiki.rb"',
  '"scripts/check_github_wiki_export.rb"',
  '"scripts/check_github_wiki_boundaries.rb"',
  '"scripts/check_github_wiki_ops_references.rb"',
  '"scripts/clean_github_wiki_noise.rb"',
  '"scripts/with_github_wiki_lock.sh"',
  '"scripts/selftest_github_wiki_lock.sh"',
  '"scripts/selftest_github_wiki_boundaries.sh"',
  '"scripts/selftest_github_wiki_noise.sh"',
  '"scripts/selftest_github_wiki_ops_references.sh"',
  '"scripts/selftest_github_wiki_exporter.sh"',
  '"scripts/selftest_github_wiki_export.sh"',
  '"scripts/selftest_github_wiki_publish.sh"',
  '"scripts/verify_github_wiki_toolchain.sh"',
  '"scripts/sync_github_wiki_toolchain.sh"',
  '"scripts/publish_github_wiki.sh"'
]

required_sync_workflow_paths.each do |snippet|
  errors << "Missing sync workflow path trigger: #{snippet}" unless sync_workflow_text.include?(snippet)
end

readme_text = File.read(README)
required_readme_snippets = [
  '`scripts/verify_github_wiki_toolchain.sh`',
  '`scripts/sync_github_wiki_toolchain.sh`',
  '`scripts/check_github_wiki_boundaries.rb`',
  '`scripts/check_github_wiki_ops_references.rb`',
  '`scripts/with_github_wiki_lock.sh`',
  '`scripts/selftest_github_wiki_lock.sh`',
  '`scripts/selftest_github_wiki_boundaries.sh`',
  '`scripts/selftest_github_wiki_noise.sh`',
  '`scripts/selftest_github_wiki_ops_references.sh`',
  '`scripts/selftest_github_wiki_exporter.sh`',
  '`scripts/selftest_github_wiki_export.sh`',
  '`scripts/selftest_github_wiki_publish.sh`',
  '`GITHUB_WIKI_LOCK_WAIT_SECONDS`',
  '`VERIFY_GITHUB_WIKI_LOCK_SELFTEST=1`',
  '`VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1`',
  '`VERIFY_GITHUB_WIKI_NOISE_SELFTEST=1`',
  '`VERIFY_GITHUB_WIKI_OPS_SELFTEST=1`',
  '`VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST=1`',
  '`VERIFY_GITHUB_WIKI_EXPORT_SELFTEST=1`',
  '`VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST=1`',
  '`ignore/github-wiki-publish/`',
  'BUNDLE_PATH=vendor/bundle bundle exec jekyll build'
]

required_readme_snippets.each do |snippet|
  errors << "Missing README boundary note: #{snippet}" unless readme_text.include?(snippet)
end

lock_text = File.read(LOCK_SCRIPT)
required_lock_snippets = [
  'LOCK_DIR="$ROOT/ignore/github-wiki-toolchain.lock"',
  'WAIT_SECONDS="${GITHUB_WIKI_LOCK_WAIT_SECONDS:-180}"',
  'if [[ -f "$LOCK_DIR/pid" ]]; then',
  '! kill -0 "$LOCK_PID" 2>/dev/null',
  'rm -rf "$LOCK_DIR"'
]

required_lock_snippets.each do |snippet|
  errors << "Missing lock guard snippet: #{snippet}" unless lock_text.include?(snippet)
end

selftest_export_text = File.read(EXPORT_SELFTEST_SCRIPT)
required_export_selftest_snippets = [
  'VALIDATOR="$ROOT/scripts/check_github_wiki_export.rb"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-export-selftest-$PPID-$$"',
  'GITHUB_WIKI_EXPORT_SRC_DIR="$SRC_DIR"',
  'GITHUB_WIKI_EXPORT_DEST_DIR="$DEST_DIR"',
  'GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1',
  'run_expect_failure "missing-page" "Missing exported page: page.md"',
  'run_expect_failure "noise-file" "Noise file in wiki export: .DS_Store"',
  'run_expect_failure "unsafe-link" "Home.md: non-export-safe relative link relative/path.md"',
  'run_expect_failure "sidebar-missing" "Sidebar missing link for page.md"',
  'run_expect_failure "missing-generated-asset" "Missing generated asset in export: generated/demo/demo.csv"'
]

required_export_selftest_snippets.each do |snippet|
  errors << "Missing export selftest guard snippet: #{snippet}" unless selftest_export_text.include?(snippet)
end

boundary_selftest_text = File.read(BOUNDARY_SELFTEST_SCRIPT)
required_boundary_selftest_snippets = [
  'CHECKER="$ROOT/scripts/check_github_wiki_boundaries.rb"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-boundary-selftest-$PPID-$$"',
  'GITHUB_WIKI_BOUNDARY_ROOT="$TEST_ROOT"',
  'run_expect_failure "missing-target" "scripts/publish_github_wiki.sh"',
  'run_expect_failure "missing-verify-guard"',
  'VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST: "1"',
  'run_expect_failure "missing-readme-note"',
  'Missing README boundary note: `VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1`'
]

required_boundary_selftest_snippets.each do |snippet|
  errors << "Missing boundary selftest guard snippet: #{snippet}" unless boundary_selftest_text.include?(snippet)
end

noise_selftest_text = File.read(NOISE_SELFTEST_SCRIPT)
required_noise_selftest_snippets = [
  'CLEANER="$ROOT/scripts/clean_github_wiki_noise.rb"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-noise-selftest-$PPID-$$"',
  'GITHUB_WIKI_NOISE_ROOT="$TEST_ROOT"',
  'GITHUB_WIKI_NOISE_TARGET_DIRS="$TARGETS"',
  'assert_contains_text "$output" "- wiki/.DS_Store"',
  'assert_contains_text "$output" "No GitHub Wiki noise files found."'
]

required_noise_selftest_snippets.each do |snippet|
  errors << "Missing noise selftest guard snippet: #{snippet}" unless noise_selftest_text.include?(snippet)
end

ops_selftest_text = File.read(OPS_SELFTEST_SCRIPT)
required_ops_selftest_snippets = [
  'CHECKER="$ROOT/scripts/check_github_wiki_ops_references.rb"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-ops-refs-selftest-$PPID-$$"',
  'GITHUB_WIKI_OPS_REFERENCE_ROOT="$TEST_ROOT"',
  'GITHUB_WIKI_OPS_REFERENCE_FILES="$TARGETS"',
  'run_expect_failure "external-wiki-path" "Forbidden external wiki path reference: README.md"',
  'run_expect_failure "legacy-remote" "Forbidden legacy wiki remote reference: ops.md"',
  'run_expect_failure "missing-target" "Missing ops reference target: ops.md"'
]

required_ops_selftest_snippets.each do |snippet|
  errors << "Missing ops selftest guard snippet: #{snippet}" unless ops_selftest_text.include?(snippet)
end

exporter_selftest_text = File.read(EXPORTER_SELFTEST_SCRIPT)
required_exporter_selftest_snippets = [
  'EXPORTER="$ROOT/scripts/export_github_wiki.rb"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-exporter-selftest-$PPID-$$"',
  'GITHUB_WIKI_EXPORT_SRC_DIR="$SRC_DIR"',
  'GITHUB_WIKI_EXPORT_DEST_DIR="$DEST_DIR"',
  'assert_contains "$DEST_DIR/Home.md" "[Guide](${GITHUB_WIKI}/guide)"',
  'assert_contains "$DEST_DIR/_Sidebar.md" "## その他"',
  'assert_not_contains "$DEST_DIR/_Sidebar.md" "mind-upload-basics"',
  '[[ ! -e "$DEST_DIR/generated/demo/.DS_Store" ]] || fail "Noise file copied into export: .DS_Store"'
]

required_exporter_selftest_snippets.each do |snippet|
  errors << "Missing exporter selftest guard snippet: #{snippet}" unless exporter_selftest_text.include?(snippet)
end

selftest_text = File.read(LOCK_SELFTEST_SCRIPT)
required_selftest_snippets = [
  'SELFTEST_LOCK_DIR="$ROOT/ignore/github-wiki-lock-selftest.lock"',
  'WAIT_SECONDS="${GITHUB_WIKI_LOCK_WAIT_SECONDS:-180}"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-lock-selftest-$PPID-$$"',
  'SELFTEST_LOCK_HELD=0',
  'if [[ "$SELFTEST_LOCK_HELD" == "1" ]]; then',
  'if (( now - start_time >= WAIT_SECONDS )); then',
  'while ! mkdir "$SELFTEST_LOCK_DIR" 2>/dev/null; do',
  'SELFTEST_LOCK_HELD=1',
  'Timed out waiting for lock self-test guard',
  'while [[ -d "$LOCK_DIR" ]]; do',
  'Timed out waiting for the GitHub Wiki toolchain lock to become idle.',
  'run_stale_lock_recovery',
  'run_serialization',
  'run_timeout'
]

required_selftest_snippets.each do |snippet|
  errors << "Missing lock selftest guard snippet: #{snippet}" unless selftest_text.include?(snippet)
end

publish_selftest_text = File.read(PUBLISH_SELFTEST_SCRIPT)
required_publish_selftest_snippets = [
  'PUBLISH_SCRIPT="$ROOT/scripts/publish_github_wiki.sh"',
  'LOCK_SCRIPT="$ROOT/scripts/with_github_wiki_lock.sh"',
  'WORK_ROOT="$ROOT/ignore/github-wiki-publish"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-publish-selftest-$PPID-$$"',
  'MISSING_REMOTE="$TEST_ROOT/missing-remote.git"',
  'run_publish_with_env() {',
  'run_missing_remote_failure() {',
  'run_missing_remote_skip() {',
  'GITHUB_WIKI_REMOTE_BASE="$MISSING_REMOTE"',
  'WIKI_PUBLISH_ALLOW_SKIP=1',
  'GitHub Wiki の git リポジトリがまだ初期化されていません。',
  '想定 remote: $MISSING_REMOTE',
  'WIKI_PUBLISH_ALLOW_SKIP=1 のため、失敗扱いにはしません。',
  'git init --bare --initial-branch=master "$REMOTE_BARE" >/dev/null',
  'git init --initial-branch=master "$SEED_REPO" >/dev/null',
  'run_publish_success() {',
  'GITHUB_WIKI_REMOTE_BASE="$REMOTE_BARE"',
  'env "$@" "$LOCK_SCRIPT" "$PUBLISH_SCRIPT"',
  'cmp "$EXPORT_DIR/Home.md" "$VERIFY_REPO/Home.md" >/dev/null',
  'cmp "$EXPORT_DIR/_Sidebar.md" "$VERIFY_REPO/_Sidebar.md" >/dev/null',
  'GitHub Wiki に反映すべき差分はありません。',
  'run_missing_remote_failure',
  'run_missing_remote_skip'
]

required_publish_selftest_snippets.each do |snippet|
  errors << "Missing publish selftest guard snippet: #{snippet}" unless publish_selftest_text.include?(snippet)
end

export_script_text = File.read(File.join(ROOT, "scripts", "export_github_wiki.rb"))
required_export_script_snippets = [
  'SRC_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_SRC_DIR", File.join(ROOT, "wiki")))',
  'DEST_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_DEST_DIR", File.join(ROOT, "github-wiki-export")))',
  'available_slugs = slugs.select { |slug| front_matters.key?(slug) }',
  'next if available_slugs.empty?',
  'lines << "## その他"'
]

required_export_script_snippets.each do |snippet|
  errors << "Missing export script guard snippet: #{snippet}" unless export_script_text.include?(snippet)
end

export_validation_text = File.read(File.join(ROOT, "scripts", "check_github_wiki_export.rb"))
required_export_validation_snippets = [
  'SRC_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_SRC_DIR", File.join(ROOT, "wiki")))',
  'DEST_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_DEST_DIR", File.join(ROOT, "github-wiki-export")))',
  'SKIP_GIT_DRIFT = ENV["GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT"] == "1"',
  'return [] if SKIP_GIT_DRIFT',
  'system("git", "-C", ROOT, "rev-parse", "--is-inside-work-tree"'
]

required_export_validation_snippets.each do |snippet|
  errors << "Missing export validation guard snippet: #{snippet}" unless export_validation_text.include?(snippet)
end

ops_reference_text = File.read(File.join(ROOT, "scripts", "check_github_wiki_ops_references.rb"))
required_ops_reference_snippets = [
  'SCRIPT_ROOT = File.expand_path("..", __dir__)',
  'ROOT = File.expand_path(ENV.fetch("GITHUB_WIKI_OPS_REFERENCE_ROOT", SCRIPT_ROOT))',
  'DEFAULT_OPS_FILES = [',
  'if ENV["GITHUB_WIKI_OPS_REFERENCE_FILES"]',
  'ENV.fetch("GITHUB_WIKI_OPS_REFERENCE_FILES").split(File::PATH_SEPARATOR).reject(&:empty?)'
]

required_ops_reference_snippets.each do |snippet|
  errors << "Missing ops reference guard snippet: #{snippet}" unless ops_reference_text.include?(snippet)
end

noise_cleanup_text = File.read(File.join(ROOT, "scripts", "clean_github_wiki_noise.rb"))
required_noise_cleanup_snippets = [
  'SCRIPT_ROOT = File.expand_path("..", __dir__)',
  'ROOT = File.expand_path(ENV.fetch("GITHUB_WIKI_NOISE_ROOT", SCRIPT_ROOT))',
  'DEFAULT_TARGET_DIRS = [',
  'if ENV["GITHUB_WIKI_NOISE_TARGET_DIRS"]',
  'ENV.fetch("GITHUB_WIKI_NOISE_TARGET_DIRS").split(File::PATH_SEPARATOR).reject(&:empty?)'
]

required_noise_cleanup_snippets.each do |snippet|
  errors << "Missing noise cleanup guard snippet: #{snippet}" unless noise_cleanup_text.include?(snippet)
end

boundary_script_text = File.read(File.join(ROOT, "scripts", "check_github_wiki_boundaries.rb"))
required_boundary_script_snippets = [
  'SCRIPT_ROOT = File.expand_path("..", __dir__)',
  'ROOT = File.expand_path(ENV.fetch("GITHUB_WIKI_BOUNDARY_ROOT", SCRIPT_ROOT))',
  'BOUNDARY_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_boundaries.sh")'
]

required_boundary_script_snippets.each do |snippet|
  errors << "Missing boundary script guard snippet: #{snippet}" unless boundary_script_text.include?(snippet)
end

if errors.empty?
  puts "GitHub Wiki boundary validation passed."
  exit 0
end

warn "GitHub Wiki boundary validation failed:"
errors.each { |error| warn "- #{error}" }
exit 1
