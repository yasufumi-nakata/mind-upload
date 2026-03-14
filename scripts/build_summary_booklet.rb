#!/usr/bin/env ruby
# frozen_string_literal: true

require "cgi"
require "date"
require "erb"
require "yaml"

ROOT = File.expand_path("..", __dir__)
OUTPUT_PATH = File.join(ROOT, "summary_booklet.md")
SOURCE_PATHS = %w[
  index.md
  verification.md
  tech_roadmap.md
  perspective.md
  datasets.md
  issue.md
  content_hub.md
  wbe_101.md
  eeg_101.md
  faq.md
  glossary.md
].freeze

PageData = Struct.new(
  :path,
  :slug,
  :url,
  :title,
  :article_type,
  :subtitle,
  :last_updated,
  :reading_time,
  :audience,
  :page_intro,
  :accuracy_note,
  :page_highlights,
  :known_points,
  :unknown_points,
  :recommended_pages,
  :abstract_html,
  keyword_init: true
)

def normalize_text(value)
  value.to_s.gsub(/\s+/, " ").strip
end

def compact_html(value)
  value.to_s.gsub(/>\s+</, "><").gsub(/\s+/, " ").strip
end

def parse_front_matter(path)
  text = File.read(path)
  match = text.match(/\A---\s*\n(.*?)\n---\s*\n/m)
  raise "front matter not found: #{path}" unless match

  yaml = YAML.safe_load(match[1], permitted_classes: [Date], aliases: true) || {}
  [yaml, text[match[0].length..]]
end

def extract_abstract_html(body)
  abstract_box = body.match(/<div class="abstract-box">.*?<p>(.*?)<\/p>.*?<\/div>/m)
  return compact_html(abstract_box[1]) if abstract_box

  first_paragraph = body.match(/<p>(.*?)<\/p>/m)
  compact_html(first_paragraph[1]) if first_paragraph
end

def normalize_points(items)
  Array(items).map do |item|
    text = normalize_text(item)
    text unless text.empty?
  end.compact
end

def normalize_recommended(items)
  Array(items).map do |item|
    next unless item.is_a?(Hash)

    label = normalize_text(item["label"])
    url = normalize_text(item["url"])
    next if label.empty? || url.empty?

    { "label" => label, "url" => url }
  end.compact
end

def load_page(path)
  absolute_path = File.join(ROOT, path)
  yaml, body = parse_front_matter(absolute_path)
  slug = File.basename(path, ".md")

  PageData.new(
    path: path,
    slug: slug,
    url: slug == "index" ? "/index.html" : "/#{slug}.html",
    title: normalize_text(yaml["title"]),
    article_type: normalize_text(yaml["article_type"]),
    subtitle: normalize_text(yaml["subtitle"]),
    last_updated: normalize_text(yaml["last_updated"]),
    reading_time: normalize_text(yaml["reading_time"]),
    audience: normalize_text(yaml["audience"]),
    page_intro: normalize_text(yaml["page_intro"]),
    accuracy_note: normalize_text(yaml["accuracy_note"]),
    page_highlights: normalize_points(yaml["page_highlights"]),
    known_points: normalize_points(yaml["known_points"]),
    unknown_points: normalize_points(yaml["unknown_points"]),
    recommended_pages: normalize_recommended(yaml["recommended_pages"]),
    abstract_html: extract_abstract_html(body)
  )
end

class SummaryBookletTemplate
  def initialize(pages)
    @pages = pages
    @page_map = pages.to_h { |page| [page.slug, page] }
  end

  def render
    ERB.new(template, trim_mode: "-").result(binding)
  end

  private

  def template
    <<~'ERB'
      ---
      layout: default
      title: "Mind-Upload Summary Booklet"
      description: "公開ページの要点を A4 冊子向けに自動生成した要約ページ。"
      article_type: "Briefing Booklet"
      subtitle: "公開ページの front matter と冒頭要約から再生成される A4 要約版"
      author: Mind Uploading Research Project
      last_updated: "<%= latest_date %>"
      note: "Auto-generated from public pages"
      body_class: "summary-booklet-page"
      ---
      <!-- AUTO-GENERATED FILE. Run `ruby scripts/build_summary_booklet.rb`. -->
      <!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

      <main class="main-container summary-booklet-main">
      <article class="content-column">

      <section class="booklet-sheet booklet-cover">
        <p class="booklet-kicker">Mind-Upload Commons</p>
        <h2 class="booklet-cover-title">公開ページ要約冊子</h2>
        <p class="booklet-cover-lead">
          <%= intro_page.page_intro %>
        </p>

        <div class="booklet-cover-band">
          <%= cover_band_html %>
        </div>

        <div class="booklet-card-grid booklet-card-grid-3">
          <%= cover_cards_html %>
        </div>
      </section>

      <section class="booklet-sheet booklet-page-break">
        <div class="booklet-section-header">
          <p class="booklet-kicker">Contents</p>
          <h2>この冊子の見取り図</h2>
        </div>

        <div class="booklet-card-grid booklet-card-grid-2">
          <%= contents_cards_html %>
        </div>

        <div class="booklet-status-grid">
          <%= status_cards_html %>
        </div>
      </section>

      <section class="booklet-sheet booklet-page-break">
        <div class="booklet-section-header">
          <p class="booklet-kicker">Project Scope</p>
          <h2>何を目指すサイトか</h2>
        </div>

        <div class="booklet-quote">
          <p><%= verification_page.abstract_html || h(verification_page.page_intro) %></p>
        </div>

        <div class="booklet-two-column">
          <div>
            <h3>先に固定すること</h3>
            <ul class="booklet-list">
              <%= list_items(project_scope_points) %>
            </ul>
          </div>
          <div>
            <h3>入口で断言しないこと</h3>
            <ul class="booklet-list">
              <%= list_items(project_limits) %>
            </ul>
          </div>
        </div>

        <table class="data-table booklet-table">
          <thead>
            <tr>
              <th>観点</th>
              <th>いま読むべき説明</th>
            </tr>
          </thead>
          <tbody>
            <%= overview_rows_html %>
          </tbody>
        </table>
      </section>

      <section class="booklet-sheet booklet-page-break">
        <div class="booklet-section-header">
          <p class="booklet-kicker">Known vs Unknown</p>
          <h2>何が既知で、何が未解決か</h2>
        </div>

        <div class="booklet-card-grid booklet-card-grid-2">
          <article class="booklet-card booklet-card-positive">
            <h3>比較的はっきりしていること</h3>
            <ul class="booklet-list">
              <%= list_items(known_points) %>
            </ul>
          </article>
          <article class="booklet-card booklet-card-caution">
            <h3>まだ保留すべきこと</h3>
            <ul class="booklet-list">
              <%= list_items(unknown_points) %>
            </ul>
          </article>
        </div>

        <div class="booklet-timeline">
          <%= timeline_cards_html %>
        </div>
      </section>

      <section class="booklet-sheet booklet-page-break">
        <div class="booklet-section-header">
          <p class="booklet-kicker">Core Pages</p>
          <h2>主ページの役割分担</h2>
        </div>

        <table class="data-table booklet-table">
          <thead>
            <tr>
              <th>ページ</th>
              <th>役割</th>
              <th>要約</th>
            </tr>
          </thead>
          <tbody>
            <%= page_rows_html(core_pages) %>
          </tbody>
        </table>

        <div class="booklet-card-grid booklet-card-grid-2">
          <%= brief_cards_html(core_pages) %>
        </div>
      </section>

      <section class="booklet-sheet booklet-page-break">
        <div class="booklet-section-header">
          <p class="booklet-kicker">Support Pages</p>
          <h2>補助ページと実務導線</h2>
        </div>

        <table class="data-table booklet-table">
          <thead>
            <tr>
              <th>ページ</th>
              <th>役割</th>
              <th>要約</th>
            </tr>
          </thead>
          <tbody>
            <%= page_rows_html(support_pages) %>
          </tbody>
        </table>

        <div class="booklet-card-grid booklet-card-grid-2">
          <%= brief_cards_html(support_pages) %>
        </div>
      </section>

      <section class="booklet-sheet booklet-page-break">
        <div class="booklet-section-header">
          <p class="booklet-kicker">Next Actions</p>
          <h2>次に何をすればよいか</h2>
        </div>

        <div class="booklet-card-grid booklet-card-grid-3">
          <%= next_action_cards_html %>
        </div>

        <div class="booklet-status-grid">
          <%= final_status_cards_html %>
        </div>

        <h3>元ページ一覧</h3>
        <ul class="booklet-link-list">
          <%= source_links_html %>
        </ul>

        <div class="booklet-quote">
          <p>
            この冊子は公開ページから自動生成される入口版でございます。各ページの <strong>page_intro</strong>、<strong>page_highlights</strong>、<strong>known / unknown</strong>、冒頭要約の更新が、そのまま冊子と PDF に反映されます。
          </p>
        </div>
      </section>

      </article>
      </main>
    ERB
  end

  def page(slug)
    @page_map.fetch(slug)
  end

  def intro_page
    page("index")
  end

  def verification_page
    page("verification")
  end

  def roadmap_page
    page("tech_roadmap")
  end

  def perspective_page
    page("perspective")
  end

  def datasets_page
    page("datasets")
  end

  def issue_page
    page("issue")
  end

  def wbe_page
    page("wbe_101")
  end

  def eeg_page
    page("eeg_101")
  end

  def faq_page
    page("faq")
  end

  def glossary_page
    page("glossary")
  end

  def content_hub_page
    page("content_hub")
  end

  def core_pages
    [
      intro_page,
      verification_page,
      roadmap_page,
      perspective_page,
      datasets_page,
      issue_page
    ]
  end

  def support_pages
    [
      wbe_page,
      eeg_page,
      faq_page,
      glossary_page,
      content_hub_page
    ]
  end

  def latest_date
    @latest_date ||= begin
      parsed = @pages.map do |page_data|
        next if page_data.last_updated.empty?
        Date.parse(page_data.last_updated)
      rescue Date::Error
        nil
      end.compact
      (parsed.max || Date.today).iso8601
    end
  end

  def cover_band_html
    items = [
      ["更新基準日", latest_date],
      ["現在の重点", verification_page.page_highlights.first],
      ["最初の入口", "#{intro_page.title} / #{verification_page.title}"]
    ]
    items.map do |label, value|
      <<~HTML
        <div>
          <span>#{h(label)}</span>
          <strong>#{h(shorten(value, 58))}</strong>
        </div>
      HTML
    end.join
  end

  def cover_cards_html
    cards = [
      ["このサイトが最初に作るもの", verification_page.abstract_html || h(verification_page.page_intro)],
      ["すぐ断言しないもの", h(shorten((intro_page.unknown_points + perspective_page.unknown_points).uniq.first(3).join(" / "), 140))],
      ["いま読むべき主ページ", h(core_pages.map(&:title).join(" / "))]
    ]
    render_cards(cards)
  end

  def contents_cards_html
    cards = [
      ["1. 何を目指すサイトか", intro_page.page_intro],
      ["2. 何が既知で何が未解決か", verification_page.accuracy_note],
      ["3. 主ページの役割分担", roadmap_page.page_intro],
      ["4. 補助ページと導線", content_hub_page.page_intro],
      ["5. 次のアクション", issue_page.page_intro],
      ["6. 元ページ一覧", "詳細確認へ戻るための公開ページ導線を最後に集約します。"]
    ]
    render_cards(cards.map { |title, body| [title, h(shorten(body, 120))] })
  end

  def status_cards_html
    cards = [
      ["ひとことで言うと", intro_page.page_highlights.first, "booklet-status-card booklet-status-card-strong"],
      ["読了後に持ち帰るもの", "全体像、現実的な作業範囲、読む順番、協力の入口", "booklet-status-card"]
    ]
    cards.map do |title, body, klass|
      <<~HTML
        <div class="#{klass}">
          <span>#{h(title)}</span>
          <strong>#{h(body)}</strong>
        </div>
      HTML
    end.join
  end

  def project_scope_points
    (verification_page.page_highlights + wbe_page.page_highlights).uniq.first(4)
  end

  def project_limits
    (intro_page.unknown_points + perspective_page.unknown_points + eeg_page.unknown_points).uniq.first(4)
  end

  def overview_rows_html
    rows = [
      ["入口", intro_page],
      ["検証基盤", verification_page],
      ["技術地図", roadmap_page],
      ["理論整理", perspective_page]
    ]

    rows.map do |label, page_data|
      <<~HTML
        <tr>
          <td>#{h(label)}</td>
          <td><strong><a href="#{page_data.url}">#{h(page_data.title)}</a></strong><br>#{h(shorten(page_data.page_intro, 190))}</td>
        </tr>
      HTML
    end.join
  end

  def known_points
    (intro_page.known_points + verification_page.known_points + datasets_page.known_points).uniq.first(5)
  end

  def unknown_points
    (intro_page.unknown_points + verification_page.unknown_points + perspective_page.unknown_points + eeg_page.unknown_points).uniq.first(5)
  end

  def timeline_cards_html
    items = [
      ["Step 1", "入口", intro_page.page_highlights.first || intro_page.page_intro],
      ["Step 2", "L0", datasets_page.page_highlights.first || datasets_page.page_intro],
      ["Step 3", "L1-L2", verification_page.page_highlights[1] || verification_page.page_intro],
      ["Later", "上位主張", roadmap_page.unknown_points.first || perspective_page.unknown_points.first]
    ]

    items.map do |label, title, body|
      <<~HTML
        <div class="booklet-step">
          <span>#{h(label)}</span>
          <strong>#{h(title)}</strong>
          <p>#{h(shorten(body, 120))}</p>
        </div>
      HTML
    end.join
  end

  def page_rows_html(pages)
    pages.map do |page_data|
      <<~HTML
        <tr>
          <td><a href="#{page_data.url}">#{h(page_data.title)}</a></td>
          <td>#{h(page_role(page_data))}</td>
          <td>#{h(shorten(page_data.page_intro, 190))}</td>
        </tr>
      HTML
    end.join
  end

  def brief_cards_html(pages)
    pages.map do |page_data|
      bullets = (page_data.page_highlights + page_data.known_points).uniq.first(3)
      <<~HTML
        <article class="booklet-card booklet-page-card">
          <h3><a href="#{page_data.url}">#{h(page_data.title)}</a></h3>
          <p class="booklet-page-meta">#{h(page_role(page_data))} / #{h(page_data.reading_time)}</p>
          <p>#{page_data.abstract_html || h(page_data.page_intro)}</p>
          <ul class="booklet-list booklet-page-link-list">
            #{list_items(bullets)}
          </ul>
          #{recommended_links_html(page_data)}
        </article>
      HTML
    end.join
  end

  def recommended_links_html(page_data)
    return "" if page_data.recommended_pages.empty?

    items = page_data.recommended_pages.first(3).map do |item|
      %(<li><a href="#{item.fetch("url")}">#{h(item.fetch("label"))}</a></li>)
    end.join

    <<~HTML
      <p class="booklet-page-meta">次に読む</p>
      <ul class="booklet-link-list booklet-page-link-list">
        #{items}
      </ul>
    HTML
  end

  def next_action_cards_html
    cards = [
      ["全体像を掴む", "#{intro_page.title} -> #{verification_page.title} -> #{roadmap_page.title}", intro_page.recommended_pages],
      ["初歩から学ぶ", "#{wbe_page.title} -> #{eeg_page.title} -> #{faq_page.title}", wbe_page.recommended_pages],
      ["参加と統合", "#{issue_page.title} / #{content_hub_page.title}", issue_page.recommended_pages]
    ]

    cards.map do |title, body, links|
      extra_links = links.first(2).map { |item| %(<li><a href="#{item.fetch("url")}">#{h(item.fetch("label"))}</a></li>) }.join
      <<~HTML
        <article class="booklet-card">
          <h3>#{h(title)}</h3>
          <p>#{h(body)}</p>
          <ul class="booklet-link-list booklet-page-link-list">
            #{extra_links}
          </ul>
        </article>
      HTML
    end.join
  end

  def final_status_cards_html
    cards = [
      ["実務上の原則", issue_page.page_highlights.first || issue_page.page_intro, "booklet-status-card booklet-status-card-strong"],
      ["更新ルール", "公開ページが変わるたびに deploy / PDF workflow 内で booklet を再生成いたします。", "booklet-status-card"]
    ]

    cards.map do |title, body, klass|
      <<~HTML
        <div class="#{klass}">
          <span>#{h(title)}</span>
          <strong>#{h(shorten(body, 150))}</strong>
        </div>
      HTML
    end.join
  end

  def source_links_html
    @pages.map do |page_data|
      %(<li><a href="#{page_data.url}">#{h(page_data.title)}</a></li>)
    end.join
  end

  def page_role(page_data)
    [page_data.article_type, page_data.subtitle].reject(&:empty?).join(" - ")
  end

  def render_cards(cards)
    cards.map do |title, body|
      <<~HTML
        <article class="booklet-card">
          <h3>#{h(title)}</h3>
          <p>#{body}</p>
        </article>
      HTML
    end.join
  end

  def list_items(items)
    Array(items).map { |item| "<li>#{h(item)}</li>" }.join
  end

  def shorten(text, max)
    plain = normalize_text(text)
    return plain if plain.length <= max

    "#{plain[0, max - 1].rstrip}…"
  end

  def h(text)
    CGI.escapeHTML(text.to_s)
  end
end

pages = SOURCE_PATHS.map { |path| load_page(path) }
output = SummaryBookletTemplate.new(pages).render
File.write(OUTPUT_PATH, output)
puts "generated #{OUTPUT_PATH}"
