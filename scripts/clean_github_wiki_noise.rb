#!/usr/bin/env ruby
# frozen_string_literal: true

require "find"
require "pathname"
require "fileutils"

SCRIPT_ROOT = File.expand_path("..", __dir__)
ROOT = File.expand_path(ENV.fetch("GITHUB_WIKI_NOISE_ROOT", SCRIPT_ROOT))
DEFAULT_TARGET_DIRS = [
  File.join(ROOT, "wiki"),
  File.join(ROOT, "github-wiki-export")
].freeze
IGNORED_NOISE_FILES = [".DS_Store"].freeze
IGNORED_NOISE_PREFIXES = ["._"].freeze

def noise_entry?(name)
  IGNORED_NOISE_FILES.include?(name) || IGNORED_NOISE_PREFIXES.any? { |prefix| name.start_with?(prefix) }
end

removed = []

target_dirs =
  if ENV["GITHUB_WIKI_NOISE_TARGET_DIRS"]
    ENV.fetch("GITHUB_WIKI_NOISE_TARGET_DIRS").split(File::PATH_SEPARATOR).reject(&:empty?).map { |path| File.expand_path(path, ROOT) }
  else
    DEFAULT_TARGET_DIRS
  end

target_dirs.each do |root|
  next unless Dir.exist?(root)

  Find.find(root) do |path|
    next if File.directory?(path)
    next unless noise_entry?(File.basename(path))

    FileUtils.rm_f(path)
    removed << Pathname.new(path).relative_path_from(Pathname.new(ROOT)).to_s
  end
end

if removed.empty?
  puts "No GitHub Wiki noise files found."
else
  puts "Removed GitHub Wiki noise files:"
  removed.sort.each { |path| puts "- #{path}" }
end
