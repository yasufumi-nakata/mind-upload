#!/usr/bin/env ruby
# frozen_string_literal: true

require "pathname"

ROOT = File.expand_path("..", __dir__)
SRC_DIR = File.join(ROOT, "wiki")
DEST_DIR = File.join(ROOT, "github-wiki-export")
GITHUB_WIKI = "https://github.com/yasufumi-nakata/mind-upload/wiki"

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

def sidebar_target_for(page)
  slug = File.basename(page, ".md")
  slug == "Home" ? GITHUB_WIKI : "#{GITHUB_WIKI}/#{slug}"
end

def eeg_funding_csv_refs(path)
  return [] unless File.exist?(path)

  File.read(path).scan(/MindUpload-EEGDATA-FundMap-[A-Za-z0-9\-]+\.csv/).uniq.sort
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

eeg_funding_source = File.join(SRC_DIR, "mind-upload-eeg-data-fund-map.md")
eeg_funding_refs = eeg_funding_csv_refs(eeg_funding_source)
eeg_funding_source_root = File.join(SRC_DIR, "generated", "mind-upload-eeg-data-fund-map")
eeg_funding_export_root = File.join(DEST_DIR, "generated", "mind-upload-eeg-data-fund-map")

eeg_funding_refs.each do |name|
  source_path = File.join(eeg_funding_source_root, name)
  export_path = File.join(eeg_funding_export_root, name)

  errors << "Referenced CSV missing in source: #{name}" unless File.exist?(source_path)
  errors << "Referenced CSV missing in export: #{name}" unless File.exist?(export_path)
end

exported_pages.each do |page|
  next unless page.end_with?(".md")

  path = File.join(DEST_DIR, page)
  extract_targets(File.read(path)).each do |target|
    next if export_safe_target?(target)

    errors << "#{page}: non-export-safe relative link #{target}"
  end
end

sidebar_path = File.join(DEST_DIR, "_Sidebar.md")
if File.exist?(sidebar_path)
  sidebar_text = File.read(sidebar_path)
  exported_pages.each do |page|
    next unless page.end_with?(".md")
    next if %w[_Sidebar.md _Footer.md].include?(page)

    target = sidebar_target_for(page)
    unless sidebar_text.include?("(#{target})")
      errors << "Sidebar missing link for #{page}"
    end
  end
else
  errors << "Missing export sidebar: _Sidebar.md"
end

if errors.empty?
  puts "GitHub Wiki export validation passed."
  exit 0
end

warn "GitHub Wiki export validation failed:"
errors.each { |error| warn "- #{error}" }
exit 1
