#!/usr/bin/env ruby
# frozen_string_literal: true

require "pathname"

ROOT = File.expand_path("..", __dir__)
SRC_DIR = File.join(ROOT, "wiki")
DEST_DIR = File.join(ROOT, "github-wiki-export")

def source_pages
  Dir.glob(File.join(SRC_DIR, "**", "*.md")).sort
end

def expected_export_pages
  source_pages.map do |path|
    slug = File.basename(path, ".md")
    slug == "index" ? "Home.md" : "#{slug}.md"
  end.sort
end

def exported_pages
  Dir.glob(File.join(DEST_DIR, "*.md")).map { |path| File.basename(path) }.sort
end

def relative_files(root)
  return [] unless Dir.exist?(root)

  Dir.glob(File.join(root, "**", "*"), File::FNM_DOTMATCH)
     .reject { |path| File.directory?(path) }
     .map { |path| Pathname.new(path).relative_path_from(Pathname.new(root)).to_s }
     .sort
end

def extract_targets(text)
  targets = []
  text.scan(/(?<!!)\]\(([^)]+)\)/) { |match| targets << match.first }
  text.scan(/href="([^"]+)"/) { |match| targets << match.first }
  text.scan(/href='([^']+)'/) { |match| targets << match.first }
  targets.uniq
end

def export_safe_target?(target)
  return true if target.nil? || target.empty?
  return true if target.start_with?("http://", "https://", "mailto:", "#")
  return true if target.start_with?("generated/")

  false
end

errors = []

unless Dir.exist?(DEST_DIR)
  warn "Missing export directory: #{DEST_DIR}"
  exit 1
end

missing_pages = expected_export_pages - exported_pages
unexpected_pages = exported_pages - (expected_export_pages + %w[_Sidebar.md _Footer.md])

missing_pages.each do |page|
  errors << "Missing exported page: #{page}"
end

unexpected_pages.each do |page|
  errors << "Unexpected exported page: #{page}"
end

source_generated = relative_files(File.join(SRC_DIR, "generated"))
export_generated = relative_files(File.join(DEST_DIR, "generated"))

(source_generated - export_generated).each do |path|
  errors << "Missing generated asset in export: generated/#{path}"
end

exported_pages.each do |page|
  next unless page.end_with?(".md")

  path = File.join(DEST_DIR, page)
  extract_targets(File.read(path)).each do |target|
    next if export_safe_target?(target)

    errors << "#{page}: non-export-safe relative link #{target}"
  end
end

if errors.empty?
  puts "GitHub Wiki export validation passed."
  exit 0
end

warn "GitHub Wiki export validation failed:"
errors.each { |error| warn "- #{error}" }
exit 1
