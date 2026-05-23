#!/usr/bin/env ruby
# frozen_string_literal: true

require "cgi"
require "digest"
require "fileutils"
require "json"
require "nokogiri"
require "time"

ROOT = File.expand_path("..", __dir__)
SITE_DIR = File.expand_path(ARGV[0] || File.join(ROOT, "_site"))
OUTPUT_DIR = File.expand_path(ARGV[1] || File.join(ROOT, "output", "language-package", "mind-upload-language-package"))
SITE_URL = "https://mind-upload.com"

BLOCK_TAGS = %w[
  address article aside blockquote br dd div dl dt figcaption figure footer h1 h2 h3 h4 h5 h6
  header hr li main nav ol p pre section table tbody td tfoot th thead tr ul
].freeze

def clean_text(value)
  value.to_s
       .gsub("\u00a0", " ")
       .gsub(/[ \t]+/, " ")
       .gsub(/[ \t]*\n[ \t]*/, "\n")
       .gsub(/\n{3,}/, "\n\n")
       .strip
end

def raw_text_with_breaks(node)
  return node.text if node.text?

  text = +""
  if node.element? && BLOCK_TAGS.include?(node.name)
    text << "\n"
  end

  node.children.each do |child|
    text << raw_text_with_breaks(child)
  end

  if node.element? && BLOCK_TAGS.include?(node.name)
    text << "\n"
  end

  text
end

def html_to_text(node)
  clean_text(raw_text_with_breaks(node))
end

def page_url(relative_path)
  if relative_path == "index.html"
    "/"
  elsif relative_path.end_with?("/index.html")
    "/#{relative_path.delete_suffix("/index.html")}/"
  else
    "/#{relative_path}"
  end
end

def package_page_path(relative_path)
  normalized = relative_path.sub(%r{/index\.html\z}, "/index.html")
  normalized.gsub(%r{[^A-Za-z0-9._/-]}, "_").sub(/\.html\z/, ".txt")
end

def content_node(doc)
  doc.at_css("article.paper") ||
    doc.at_css(".content-column") ||
    doc.at_css("main") ||
    doc.at_css("body")
end

abort "site directory not found: #{SITE_DIR}" unless Dir.exist?(SITE_DIR)

FileUtils.rm_rf(OUTPUT_DIR)
FileUtils.mkdir_p(File.join(OUTPUT_DIR, "pages"))

html_files = Dir.glob(File.join(SITE_DIR, "**", "*.html")).sort
records = html_files.map do |path|
  relative_path = path.delete_prefix("#{SITE_DIR}/")
  html = File.read(path, encoding: "UTF-8")
  doc = Nokogiri::HTML(html)

  doc.css("script, style, svg, noscript, template").remove

  title = clean_text(doc.at_css("title")&.text || relative_path)
  description = clean_text(doc.at_css('meta[name="description"]')&.[]("content"))
  node = content_node(doc)
  text = html_to_text(node ? node.dup : doc)
  headings = node ? node.css("h1, h2, h3").map { |h| clean_text(h.text) }.reject(&:empty?) : []
  url_path = page_url(relative_path)
  absolute_url = "#{SITE_URL}#{url_path}"
  section = relative_path.start_with?("external/") ? "external_translation" : "core_site"
  page_text_path = File.join("pages", package_page_path(relative_path))

  FileUtils.mkdir_p(File.join(OUTPUT_DIR, File.dirname(page_text_path)))
  File.write(
    File.join(OUTPUT_DIR, page_text_path),
    [
      "# #{title}",
      "URL: #{absolute_url}",
      ("説明: #{description}" unless description.empty?),
      "区分: #{section}",
      "",
      text
    ].compact.join("\n"),
    encoding: "UTF-8"
  )

  {
    "path" => relative_path,
    "url" => absolute_url,
    "title" => title,
    "description" => description,
    "section" => section,
    "headings" => headings,
    "text_file" => page_text_path,
    "text_chars" => text.length,
    "html_sha256" => Digest::SHA256.file(path).hexdigest,
    "text" => text
  }
end

manifest_records = records.map { |record| record.reject { |key, _| key == "text" } }
summary = {
  "name" => "mind-upload-language-package",
  "generated_at_utc" => Time.now.utc.iso8601,
  "site_url" => SITE_URL,
  "source" => "Jekyll output under _site",
  "page_count" => records.length,
  "sections" => records.group_by { |record| record["section"] }.transform_values(&:length),
  "files" => {
    "manifest" => "manifest.json",
    "corpus_jsonl" => "corpus.jsonl",
    "corpus_txt" => "corpus.txt",
    "page_texts" => "pages/**/*.txt"
  },
  "usage_note" => "GPTや検索拡張生成に渡す場合は corpus.jsonl をページ単位の文書集合として扱ってください。人間が読む場合は corpus.txt または pages/*.txt を使ってください。"
}

File.write(File.join(OUTPUT_DIR, "manifest.json"), JSON.pretty_generate(summary.merge("pages" => manifest_records)), encoding: "UTF-8")

File.open(File.join(OUTPUT_DIR, "corpus.jsonl"), "w:UTF-8") do |file|
  records.each do |record|
    file.puts(JSON.generate(record))
  end
end

File.open(File.join(OUTPUT_DIR, "corpus.txt"), "w:UTF-8") do |file|
  file.puts "マインドアップロード・コモンズ 自然言語コーパス"
  file.puts "生成元: #{SITE_URL}"
  file.puts "ページ数: #{records.length}"
  file.puts
  records.each_with_index do |record, index|
    file.puts "=" * 80
    file.puts "Document #{index + 1}: #{record["title"]}"
    file.puts "URL: #{record["url"]}"
    file.puts "Path: #{record["path"]}"
    file.puts "Section: #{record["section"]}"
    file.puts "-" * 80
    file.puts record["text"]
    file.puts
  end
end

File.write(
  File.join(OUTPUT_DIR, "README.txt"),
  <<~TEXT,
    マインドアップロード・コモンズ 自然言語パッケージ

    このパッケージは、https://mind-upload.com/ の公開HTMLを、GPTなどのLLMや検索拡張生成で扱いやすい自然言語コーパスに変換したものです。

    含まれるファイル:
    - manifest.json: ページ一覧、URL、タイトル、文字数、SHA-256、区分
    - corpus.jsonl: 1行1ページのJSON Lines。RAGやベクトル化の入力に向きます。
    - corpus.txt: 全ページを区切り付きで連結したプレーンテキスト。
    - pages/**/*.txt: ページごとのプレーンテキスト。

    注意:
    - 外部翻訳ページは原典URLとライセンス表示を各ページ内に残しています。
    - 研究・実装判断に使う場合は、必ず原典と出典リンクも確認してください。
    - このパッケージは公開サイトから生成したもので、秘密情報や内部ログを含める用途ではありません。
  TEXT
  encoding: "UTF-8"
)

puts "Generated #{records.length} page records in #{OUTPUT_DIR}"
