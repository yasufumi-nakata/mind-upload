#!/usr/bin/env ruby
# frozen_string_literal: true

require "fileutils"
require "find"
require "yaml"

ROOT = File.expand_path("..", __dir__)
SRC_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_SRC_DIR", File.join(ROOT, "wiki")))
DEST_DIR = File.expand_path(ENV.fetch("GITHUB_WIKI_EXPORT_DEST_DIR", File.join(ROOT, "github-wiki-export")))
PUBLIC_SITE = "https://mind-upload.com"
GITHUB_WIKI = "https://github.com/yasufumi-nakata/mind-upload/wiki"
IGNORED_NOISE_FILES = [".DS_Store"].freeze
IGNORED_NOISE_PREFIXES = ["._"].freeze

SIDEBAR_GROUPS = {
  "開始とナビゲーション" => %w[
    Home
    public-page-reading-guide
    page-header-reading-guide
    site-usage-modes
    first-30-minutes-by-goal
    claim-level-reading-routes
  ],
  "基礎" => %w[
    mind-upload-basics
    claims-and-evidence
    eeg-basics
    verification-basics
    known-unknown-and-status-reading
    facts-hypotheses-proposals-and-tasks
  ],
  "理論と検証" => %w[
    roadmap-reading-guide
    theory-pages-reading-guide
    practical-pages-reading-guide
    observation-to-estimation
    counterfactual-and-perturbation-verification
    identity-and-continuity-tests
  ],
  "文献と参加" => %w[
    literature-and-evidence-reading
    paper-source-types-and-evidence-status
    proposal-status-reading
    issue-writing-basics
    content-placement-basics
    reading-to-change-workflow
  ]
}.freeze

def grouped_sidebar_slugs
  SIDEBAR_GROUPS.values.flatten.uniq
end

def noise_entry?(name)
  IGNORED_NOISE_FILES.include?(name) || IGNORED_NOISE_PREFIXES.any? { |prefix| name.start_with?(prefix) }
end

def each_file(root)
  return enum_for(:each_file, root) unless block_given?
  return unless Dir.exist?(root)

  Find.find(root) do |path|
    next if File.directory?(path)

    yield path
  end
end

def load_page(path)
  raw = File.read(path)
  return [{}, raw] unless raw.start_with?("---\n")

  match = raw.match(/\A---\s*\n(.*?)\n---\s*\n/m)
  return [{}, raw] unless match

  front_matter = YAML.safe_load(match[1], aliases: true) || {}
  body = raw[match[0].length..] || ""
  [front_matter, body]
end

def split_suffix(url)
  if (match = url.match(/\A([^?#]*)([?#].*)?\z/))
    [match[1], match[2] || ""]
  else
    [url, ""]
  end
end

def github_wiki_url(slug)
  slug == "Home" ? GITHUB_WIKI : "#{GITHUB_WIKI}/#{slug}"
end

def public_site_url(path)
  normalized = path.sub(%r{\A\.\./}, "").sub(%r{\A\./}, "").sub(%r{\A/}, "")
  return PUBLIC_SITE if normalized.empty? || normalized == "index.html"

  "#{PUBLIC_SITE}/#{normalized}"
end

def rewrite_url(url)
  return url if url.nil? || url.empty?
  return url if url.start_with?("http://", "https://", "mailto:", "#")

  path, suffix = split_suffix(url)
  normalized = path.sub(%r{\A\./}, "")

  case normalized
  when "", ".", "./", "../", "/", "/wiki", "/wiki/", "../wiki", "../wiki/", "wiki", "wiki/"
    "#{GITHUB_WIKI}#{suffix}"
  else
    if normalized.match?(%r{\A/?wiki/}) || path.match?(%r{\A\.\./wiki/})
      slug = normalized.sub(%r{\A/?wiki/}, "").sub(%r{\.html\z}, "")
      slug = "Home" if slug.empty? || slug == "index"
      "#{github_wiki_url(slug)}#{suffix}"
    elsif path.match?(%r{\A(?:\./)?[^/]+\.html\z})
      slug = File.basename(path, ".html")
      slug = "Home" if slug == "index"
      "#{github_wiki_url(slug)}#{suffix}"
    elsif normalized.end_with?(".html")
      "#{public_site_url(normalized)}#{suffix}"
    else
      "#{public_site_url(normalized)}#{suffix}"
    end
  end
end

def rewrite_links(text)
  rewritten = text.dup
  rewritten.gsub!(%r{href="([^"]+)"}) { %(href="#{rewrite_url(Regexp.last_match(1))}") }
  rewritten.gsub!(%r{href='([^']+)'}) { %(href='#{rewrite_url(Regexp.last_match(1))}') }
  rewritten.gsub!(%r{(?<!!)\]\(([^)]+)\)}) { "](#{rewrite_url(Regexp.last_match(1))})" }
  rewritten
end

def strip_site_wrappers(body)
  stripped = body.dup
  stripped.sub!(%r{\A\s*<main class="main-container">\s*<article class="content-column">\s*}m, "")
  stripped.sub!(%r{\s*</article>\s*(<aside class="sidebar-column">.*?</aside>\s*)?</main>\s*\z}m, "")
  stripped.gsub!(%r{<aside class="sidebar-column">.*?</aside>}m, "")
  stripped.strip
end

def normalize_html_for_github(text)
  normalized = text.dup
  normalized.gsub!(%r{<!--.*?-->}m, "")
  normalized.gsub!(%r{\sclass="[^"]*"}, "")
  normalized.gsub!(%r{\sid="[^"]*"}, "")
  normalized.gsub!(%r{\saria-label="[^"]*"}, "")
  normalized.gsub!(%r{(<[^>]*?)\shidden(="hidden")?(?=[\s>])}) { Regexp.last_match(1) }
  normalized.gsub!(%r{</?div[^>]*>}, "")
  normalized.gsub!(%r{</?section[^>]*>}, "")
  normalized.gsub!(/\n{3,}/, "\n\n")
  normalized.strip
end

def render_link_list(entries)
  Array(entries).map do |entry|
    next unless entry.is_a?(Hash)
    label = entry["label"]
    url = rewrite_url(entry["url"].to_s)
    description = entry["description"]
    line = "- [#{label}](#{url})"
    line += " - #{description}" if description && !description.empty?
    line
  end.compact
end

def render_page(front_matter, body, slug)
  lines = []
  lines << "# #{front_matter["title"] || slug}"
  lines << ""
  lines << "> #{front_matter["subtitle"]}" if front_matter["subtitle"]
  lines << ">"
  lines << "> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](#{PUBLIC_SITE}) で管理しています。"
  lines << ""

  meta = []
  meta << "Updated: #{front_matter["last_updated"]}" if front_matter["last_updated"]
  meta << "Role: #{front_matter["note"]}" if front_matter["note"]
  lines << "- #{meta.join(" / ")}" unless meta.empty?
  lines << ""

  if front_matter["page_intro"]
    lines << "## このページの役割"
    lines << front_matter["page_intro"].to_s
    lines << ""
  end

  if front_matter["accuracy_note"]
    lines << "## 正確性に関する注記"
    lines << front_matter["accuracy_note"].to_s
    lines << ""
  end

  if front_matter["recommended_pages"]
    lines << "## 公開ページへ戻る"
    lines.concat(render_link_list(front_matter["recommended_pages"]))
    lines << ""
  end

  if front_matter["wiki_links"]
    lines << "## 関連 Wiki ページ"
    lines.concat(render_link_list(front_matter["wiki_links"]))
    lines << ""
  end

  if front_matter["known_points"]
    lines << "## 現在わかっていること"
    Array(front_matter["known_points"]).each { |item| lines << "- #{item}" }
    lines << ""
  end

  if front_matter["unknown_points"]
    lines << "## まだわかっていないこと"
    Array(front_matter["unknown_points"]).each { |item| lines << "- #{item}" }
    lines << ""
  end

  lines << "---"
  lines << ""
  lines << normalize_html_for_github(rewrite_links(strip_site_wrappers(body)))
  lines.join("\n").strip + "\n"
end

def build_sidebar(front_matters)
  lines = ["# サイドバー", ""]
  rendered = []

  SIDEBAR_GROUPS.each do |heading, slugs|
    available_slugs = slugs.select { |slug| front_matters.key?(slug) }
    next if available_slugs.empty?

    lines << "## #{heading}"
    available_slugs.each do |slug|
      title = front_matters.fetch(slug, {})["title"] || slug
      url = slug == "Home" ? GITHUB_WIKI : github_wiki_url(slug)
      lines << "- [#{title}](#{url})"
      rendered << slug
    end
    lines << ""
  end

  remaining = front_matters.keys.reject { |slug| rendered.include?(slug) }.sort_by do |slug|
    [(slug == "Home" ? 0 : 1), (front_matters.fetch(slug, {})["title"] || slug).downcase]
  end

  unless remaining.empty?
    lines << "## その他"
    remaining.each do |slug|
      title = front_matters.fetch(slug, {})["title"] || slug
      url = slug == "Home" ? GITHUB_WIKI : github_wiki_url(slug)
      lines << "- [#{title}](#{url})"
    end
    lines << ""
  end

  lines << "## 公開サイト"
  lines << "- [開始ページ](#{PUBLIC_SITE}/index.html)"
  lines << "- [検証コモンズ](#{PUBLIC_SITE}/verification.html)"
  lines << "- [公開コンテンツ統合ハブ](#{PUBLIC_SITE}/content_hub.html)"
  lines.join("\n").strip + "\n"
end

def build_footer
  <<~FOOTER
  ---

  この学習 Wiki のソースファイルは、リポジトリ内の `wiki/` で管理しています。

  - 公開ポータル: [mind-upload.com](#{PUBLIC_SITE})
  - 統合先ルーティング: [公開コンテンツ統合ハブ](#{PUBLIC_SITE}/content_hub.html)
  - 誤りの報告と改善提案: [GitHub Issues](https://github.com/yasufumi-nakata/mind-upload/issues)
  FOOTER
end

pages = {}
front_matters = {}
page_paths = Dir.glob(File.join(SRC_DIR, "**", "*.md")).sort

page_paths.each do |path|
  slug = File.basename(path, ".md")
  output_slug = slug == "index" ? "Home" : slug
  front_matter, body = load_page(path)
  pages[output_slug] = render_page(front_matter, body, output_slug)
  front_matters[output_slug] = front_matter
end

FileUtils.rm_rf(DEST_DIR)
FileUtils.mkdir_p(DEST_DIR)

pages.each do |slug, content|
  File.write(File.join(DEST_DIR, "#{slug}.md"), content)
end

generated_src = File.join(SRC_DIR, "generated")
if Dir.exist?(generated_src)
  FileUtils.mkdir_p(File.join(DEST_DIR, "generated"))
  generated_children = Dir.children(generated_src).reject { |child| noise_entry?(child) }
  FileUtils.cp_r(generated_children.map { |child| File.join(generated_src, child) }, File.join(DEST_DIR, "generated")) unless generated_children.empty?
end

each_file(DEST_DIR).each do |path|
  next unless noise_entry?(File.basename(path))

  FileUtils.rm_f(path)
end

File.write(File.join(DEST_DIR, "_Sidebar.md"), build_sidebar(front_matters))
File.write(File.join(DEST_DIR, "_Footer.md"), build_footer)

puts "#{pages.length} 件の Wiki ページを #{DEST_DIR} へエクスポートしました"
