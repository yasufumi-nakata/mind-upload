#!/usr/bin/env ruby
# frozen_string_literal: true

ROOT = File.expand_path("..", __dir__)
PUBLISH_SCRIPT = File.join(ROOT, "scripts", "publish_github_wiki.sh")
VERIFY_SCRIPT = File.join(ROOT, "scripts", "verify_github_wiki_toolchain.sh")
SYNC_SCRIPT = File.join(ROOT, "scripts", "sync_github_wiki_toolchain.sh")
OPS_REFERENCE_SCRIPT = File.join(ROOT, "scripts", "check_github_wiki_ops_references.rb")
LOCK_SCRIPT = File.join(ROOT, "scripts", "with_github_wiki_lock.sh")
LOCK_SELFTEST_SCRIPT = File.join(ROOT, "scripts", "selftest_github_wiki_lock.sh")
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
  'WORK_ROOT="$ROOT/ignore/github-wiki-publish"',
  'WORK_DIR="$WORK_ROOT/repo"',
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
  'exec env GITHUB_WIKI_LOCK_HELD=1 "$ROOT/scripts/with_github_wiki_lock.sh" "$SCRIPT_PATH" "$@"',
  'run_step "syntax-boundary" ruby -c scripts/check_github_wiki_boundaries.rb',
  'run_step "syntax-ops-refs" ruby -c scripts/check_github_wiki_ops_references.rb',
  'run_step "syntax-noise-cleanup" ruby -c scripts/clean_github_wiki_noise.rb',
  'run_step "syntax-export" ruby -c scripts/export_github_wiki.rb',
  'run_step "syntax-export-validate" ruby -c scripts/check_github_wiki_export.rb',
  'run_step "syntax-lock-selftest" bash -n scripts/selftest_github_wiki_lock.sh',
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
  'VERIFY_GITHUB_WIKI_LOCK_SELFTEST: "1"'
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
  'VERIFY_GITHUB_WIKI_LOCK_SELFTEST: "1"'
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
  '`GITHUB_WIKI_LOCK_WAIT_SECONDS`',
  '`VERIFY_GITHUB_WIKI_LOCK_SELFTEST=1`',
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

selftest_text = File.read(LOCK_SELFTEST_SCRIPT)
required_selftest_snippets = [
  'SELFTEST_LOCK_DIR="$ROOT/ignore/github-wiki-lock-selftest.lock"',
  'WAIT_SECONDS="${GITHUB_WIKI_LOCK_WAIT_SECONDS:-180}"',
  'TEST_ROOT="$ROOT/ignore/github-wiki-lock-selftest-$PPID-$$"',
  'SELFTEST_LOCK_HELD=0',
  'if [[ "$SELFTEST_LOCK_HELD" == "1" ]]; then',
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

if errors.empty?
  puts "GitHub Wiki boundary validation passed."
  exit 0
end

warn "GitHub Wiki boundary validation failed:"
errors.each { |error| warn "- #{error}" }
exit 1
