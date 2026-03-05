#!/usr/bin/env ruby
# frozen_string_literal: true

ROOT = File.expand_path("..", __dir__)
PUBLISH_SCRIPT = File.join(ROOT, "scripts", "publish_github_wiki.sh")
VERIFY_SCRIPT = File.join(ROOT, "scripts", "verify_github_wiki_toolchain.sh")
SYNC_SCRIPT = File.join(ROOT, "scripts", "sync_github_wiki_toolchain.sh")
VERIFY_WORKFLOW = File.join(ROOT, ".github", "workflows", "validate-github-wiki-export.yml")
SYNC_WORKFLOW = File.join(ROOT, ".github", "workflows", "sync-github-wiki.yml")
README = File.join(ROOT, "README.md")

[
  PUBLISH_SCRIPT,
  VERIFY_SCRIPT,
  SYNC_SCRIPT,
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
  'run_step "syntax-boundary" ruby -c scripts/check_github_wiki_boundaries.rb',
  'run_step "syntax-noise-cleanup" ruby -c scripts/clean_github_wiki_noise.rb',
  'run_step "syntax-export" ruby -c scripts/export_github_wiki.rb',
  'run_step "syntax-export-validate" ruby -c scripts/check_github_wiki_export.rb',
  'run_step "syntax-publish" bash -n scripts/publish_github_wiki.sh',
  'run_step "boundary-check" scripts/check_github_wiki_boundaries.rb',
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
  'run_step "verify" scripts/verify_github_wiki_toolchain.sh',
  'run_step "publish" scripts/publish_github_wiki.sh'
]

required_sync_script_snippets.each do |snippet|
  errors << "Missing sync script guard snippet: #{snippet}" unless sync_script_text.include?(snippet)
end

verify_workflow_text = File.read(VERIFY_WORKFLOW)
required_verify_workflow_snippets = [
  'run: scripts/verify_github_wiki_toolchain.sh',
  'VERIFY_GITHUB_WIKI_BUILD: "1"'
]

required_verify_workflow_snippets.each do |snippet|
  errors << "Missing verify workflow guard snippet: #{snippet}" unless verify_workflow_text.include?(snippet)
end

sync_workflow_text = File.read(SYNC_WORKFLOW)
required_sync_workflow_snippets = [
  'run: |',
  'scripts/sync_github_wiki_toolchain.sh'
]

required_sync_workflow_snippets.each do |snippet|
  errors << "Missing sync workflow guard snippet: #{snippet}" unless sync_workflow_text.include?(snippet)
end

readme_text = File.read(README)
required_readme_snippets = [
  '`scripts/verify_github_wiki_toolchain.sh`',
  '`scripts/sync_github_wiki_toolchain.sh`',
  '`scripts/check_github_wiki_boundaries.rb`',
  '`ignore/github-wiki-publish/`',
  'BUNDLE_PATH=vendor/bundle bundle exec jekyll build'
]

required_readme_snippets.each do |snippet|
  errors << "Missing README boundary note: #{snippet}" unless readme_text.include?(snippet)
end

if errors.empty?
  puts "GitHub Wiki boundary validation passed."
  exit 0
end

warn "GitHub Wiki boundary validation failed:"
errors.each { |error| warn "- #{error}" }
exit 1
