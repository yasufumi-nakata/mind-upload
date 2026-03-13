#!/usr/bin/env ruby
# frozen_string_literal: true

require "pathname"
require "find"

ROOT = File.expand_path("..", __dir__)
SRC_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_SRC_DIR", File.join(ROOT, "wiki")))
DEST_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_DEST_DIR", File.join(ROOT, "github-wiki-export")))
GITHUB_WIKI = "https://github.com/yasufumi-nakata/mind-upload/wiki"
IGNORED_NOISE_FILES = [".DS_Store"].freeze
IGNORED_NOISE_PREFIXES = ["._"].freeze
SKIP_GIT_DRIFT = ENV["GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT"] == "1"

def changed_export_paths
  return [] if SKIP_GIT_DRIFT
  return [] unless system("git", "-C", ROOT, "rev-parse", "--is-inside-work-tree", out: File::NULL, err: File::NULL)

  changed =
    `git -C "#{ROOT}" diff --name-status -- "#{DEST_DIR}"`.lines
      .map(&:strip)
      .reject(&:empty?)
      .map { |line| line.sub(/\t+/, " ") }
  untracked = `git -C "#{ROOT}" ls-files --others --exclude-standard -- "#{DEST_DIR}"`.lines.map(&:strip).reject(&:empty?).map { |path| "?? #{path}" }
  (changed + untracked).uniq.sort
end

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

  files = []
  Find.find(root) do |path|
    next if File.directory?(path)

    files << Pathname.new(path).relative_path_from(Pathname.new(root)).to_s
  end
  files.sort
end

def noise_entry?(name)
  IGNORED_NOISE_FILES.include?(name) || IGNORED_NOISE_PREFIXES.any? { |prefix| name.start_with?(prefix) }
end

def noise_files(root)
  return [] unless Dir.exist?(root)

  files = []
  Find.find(root) do |path|
    next if File.directory?(path)
    next unless noise_entry?(File.basename(path))

    files << Pathname.new(path).relative_path_from(Pathname.new(root)).to_s
  end
  files.sort
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

def export_safe_target?(target)
  return true if target.nil? || target.empty?
  return true if target.start_with?("http://", "https://", "mailto:", "#")
  return true if target.start_with?("generated/")

  false
end

errors = []
noise_errors = []

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

noise_files(SRC_DIR).each do |path|
  message = "Noise file in wiki source: #{path}"
  errors << message
  noise_errors << message
end

noise_files(DEST_DIR).each do |path|
  message = "Noise file in wiki export: #{path}"
  errors << message
  noise_errors << message
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

changed_export_paths.each do |line|
  errors << "Uncommitted export drift: #{line}"
end

if errors.empty?
  puts "GitHub Wiki export validation passed."
  exit 0
end

warn "GitHub Wiki export validation failed:"
errors.each { |error| warn "- #{error}" }
warn "Run scripts/clean_github_wiki_noise.rb to remove wiki noise files." unless noise_errors.empty?
exit 1
