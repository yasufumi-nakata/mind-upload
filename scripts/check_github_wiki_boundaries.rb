#!/usr/bin/env ruby
# frozen_string_literal: true

ROOT = File.expand_path("..", __dir__)
PUBLISH_SCRIPT = File.join(ROOT, "scripts", "publish_github_wiki.sh")

unless File.exist?(PUBLISH_SCRIPT)
  warn "Missing publish script: #{PUBLISH_SCRIPT}"
  exit 1
end

text = File.read(PUBLISH_SCRIPT)
errors = []

required_snippets = [
  'WORK_ROOT="$ROOT/ignore/github-wiki-publish"',
  'WORK_DIR="$WORK_ROOT/repo"',
  'git clone "$REMOTE_URL" "$WORK_DIR"',
  'rsync -a --delete --exclude ".git/" --exclude ".DS_Store" "$EXPORT_DIR"/ "$WORK_DIR"/',
  'find "$WORK_DIR" -name ".DS_Store" -delete',
  'GitHub Wiki の作業先はリポジトリ内に固定しています'
]

required_snippets.each do |snippet|
  errors << "Missing publish guard snippet: #{snippet}" unless text.include?(snippet)
end

forbidden_patterns = {
  /GITHUB_WIKI_WORKDIR/ => "Forbidden override remains: GITHUB_WIKI_WORKDIR",
  /\bmktemp\b/ => "Forbidden temp directory helper remains: mktemp",
  %r{\$TMP_DIR/wiki} => "Forbidden temp wiki checkout path remains: $TMP_DIR/wiki"
}

forbidden_patterns.each do |pattern, message|
  errors << message if text.match?(pattern)
end

if errors.empty?
  puts "GitHub Wiki boundary validation passed."
  exit 0
end

warn "GitHub Wiki boundary validation failed:"
errors.each { |error| warn "- #{error}" }
exit 1
