#!/usr/bin/env ruby
# frozen_string_literal: true

ROOT = File.expand_path("..", __dir__)

OPS_FILES = [
  "README.md",
  ".github/workflows/validate-github-wiki-export.yml",
  ".github/workflows/sync-github-wiki.yml",
  "scripts/publish_github_wiki.sh",
  "scripts/verify_github_wiki_toolchain.sh",
  "scripts/sync_github_wiki_toolchain.sh",
  "scripts/with_github_wiki_lock.sh",
  "scripts/selftest_github_wiki_lock.sh",
  "scripts/selftest_github_wiki_exporter.sh",
  "scripts/selftest_github_wiki_export.sh",
  "scripts/selftest_github_wiki_publish.sh",
  "scripts/clean_github_wiki_noise.rb"
].freeze

FORBIDDEN_PATTERNS = {
  /\.\.\/wiki\b/ => "Forbidden external wiki path reference",
  /AoyamaLab\/wiki/ => "Forbidden legacy wiki remote reference"
}.freeze

errors = []

OPS_FILES.each do |relative_path|
  path = File.join(ROOT, relative_path)
  unless File.exist?(path)
    errors << "Missing ops reference target: #{relative_path}"
    next
  end

  text = File.read(path)
  FORBIDDEN_PATTERNS.each do |pattern, message|
    next unless text.match?(pattern)

    errors << "#{message}: #{relative_path}"
  end
end

if errors.empty?
  puts "GitHub Wiki ops reference validation passed."
  exit 0
end

warn "GitHub Wiki ops reference validation failed:"
errors.each { |error| warn "- #{error}" }
exit 1
