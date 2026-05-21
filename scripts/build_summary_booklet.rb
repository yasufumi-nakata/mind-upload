#!/usr/bin/env ruby
# frozen_string_literal: true

require "cgi"
require "date"
require "erb"
require "yaml"

ROOT = File.expand_path("..", __dir__)
OUTPUT_PATH = File.join(ROOT, "summary_booklet.html")
SOURCE_PATHS = %w[
  index.html
  verification.html
  tech_roadmap.html
  perspective.html
  datasets.html
  issue.html
  content_hub.html
  wbe_101.html
  eeg_101.html
  faq.html
  glossary.html
].freeze

SCIENCE_STOPLINE_PATTERNS = [
  [/connectome|wiring|cell type/i, 8],
  [/hidden-state|maintenance-state|latent-state/i, 8],
  [/proxy-rich|proxy class|proxy bundle|same-subject|same-brain|state closure|state-identification|calibrator|composition/i, 7],
  [/same named quantity|method-family non-equivalence|interchangeable/i, 7],
  [/bridge|drift|cross-day|temporal|same-state/i, 7],
  [/foundation-model|leaderboard|general neural decoder|self-supervised/i, 8],
  [/pretraining|recording-frame|coordinate route|reference family|benchmark governance|label-limited adaptation|linear probes?|fine-tuning|label budget/i, 6],
  [/measurement model|model burden|quantification|tracer|partial-volume|spectral QC|scan window|kinetic/i, 6],
  [/shortcut|fingerprint|acquisition-distribution|specificity/i, 6],
  [/SV2A|synaptic-density PET|MRSI|metabolic connectome|dynamic DMI|myelin|ionic|bioenergetic|astrocyte|clearance|sleep replay/i, 5]
].freeze

OBSERVABILITY_PATTERNS = [
  [/connectome|wiring|cell type/i, 8],
  [/hidden-state|maintenance-state|latent-state/i, 8],
  [/human evidence is layered|proxy-rich|proxy class|current human|whole-brain/i, 7],
  [/SV2A|synaptic-density PET|MRSI|metabolic connectome|myelin|ionic|bioenergetic|astrocyte|clearance/i, 6]
].freeze

AUDIT_PATTERNS = [
  [/same-subject|same-brain|composition|calibrator|proxy bundle|state closure/i, 8],
  [/same named quantity|method-family non-equivalence|interchangeable/i, 8],
  [/bridge|drift|cross-day|temporal|same-state/i, 8],
  [/foundation-model|leaderboard|general neural decoder|self-supervised/i, 8],
  [/pretraining|recording-frame|coordinate route|reference family|benchmark governance|label-limited adaptation|linear probes?|fine-tuning|label budget/i, 7],
  [/measurement model|model burden|quantification|tracer|partial-volume|spectral QC|scan window|kinetic/i, 7],
  [/shortcut|fingerprint|acquisition-distribution|specificity|pretraining|fusion card|temporal validity/i, 7]
].freeze

TECHNICAL_UNRESOLVED_PATTERNS = [
  [/still|remain|missing|latent|unresolved|not yet|cannot|do not|insufficient|ceiling/i, 4],
  [/noninvasive|whole-brain|same-subject|bridge|drift|proxy|human route/i, 4],
  [/transcription|RNA|phospho|proteostasis|cargo|chloride|mitochondrial|ECM|myelin|astrocyte|clearance|synaptic efficacy/i, 5]
].freeze

NONTECHNICAL_PATTERNS = [
  /identity|personhood|institutional|social deployment|philosoph|consciousness/i
].freeze

SUMMARY_REJECT_PATTERNS = (
  NONTECHNICAL_PATTERNS + [
    /eleven technical guardrails/i,
    /route card/i,
    /Observability Budget now requires/i,
    /maintenance-state budget now requires/i
  ]
).freeze

SUMMARY_PRIORITY_QUERIES = [
  /Connectome-complete does not mean emulation-complete/i,
  /human evidence is layered/i,
  /same-subject or same-brain.*one state sample/i,
  /Several living-human proxy rows are not promoted together/i,
  /same named quantity.*validated row/i,
  /Temporal Validity Card/i,
  /same decode score is not a target-specific biomarker/i
].freeze

OBSERVABILITY_PRIORITY_QUERIES = [
  /Maintenance-state variables.*remain outside the wiring diagram/i,
  /Connectome-complete does not mean emulation-complete/i,
  /human evidence is layered/i,
  /human whole-brain evidence remains layered and proxy-based/i
].freeze

AUDIT_PRIORITY_QUERIES = [
  /same-subject or same-brain.*one state sample/i,
  /Several living-human proxy rows are not promoted together/i,
  /same named quantity.*validated row/i,
  /Temporal Validity Card/i,
  /Specificity & Shortcut Card|same decode score is not a target-specific biomarker/i
].freeze

FAQ_PRIORITY_QUERIES = [
  /foundation-model evidence is now split/i,
  /Recent EEG foundation-model benchmarks still show regime-dependent trade-offs/i,
  /same-subject \/ same-brain bridges/i
].freeze

COMPACT_STOPLINE_RULES = [
  [/Connectome-complete does not mean emulation-complete|コネクトーム.*エミュレーション.*同じではない/i, "コネクトーム完全性はエミュレーション完全性ではありません。"],
  [/human evidence is layered|ヒト.*証拠.*階層/i, "ヒト証拠は階層的で、なおプロキシに基づきます。"],
  [/Several living-human proxy rows are not promoted together|複数.*ヒト.*プロキシ/i, "プロキシ束には互換性、反復性、不一致監査が必要です。"],
  [/same-subject or same-brain.*one state sample|同一被験者|同一脳/i, "同一被験者という表現だけでは、一つの状態サンプルにはなりません。"],
  [/foundation-model|leaderboard result.*general neural decoder|基盤モデル|リーダーボード/i, "基盤モデルのスコアはベンチマーク条件付きであり、汎用デコーダではありません。"],
  [/same decode score is not a target-specific biomarker|デコード.*バイオマーカー/i, "高いデコードスコアでもショートカット駆動の可能性があります。"],
  [/Temporal Validity Card|時間的妥当性/i, "同日内の成功は、別日や長期の主張ではありません。"]
].freeze

COMPACT_TITLE_MAP = {
  "index" => "Mind-Upload",
  "verification" => "検証コモンズ",
  "tech_roadmap" => "技術ロードマップ",
  "perspective" => "展望",
  "datasets" => "データセットと L0",
  "issue" => "参加ガイド",
  "content_hub" => "コンテンツハブ",
  "wbe_101" => "WBE 101",
  "eeg_101" => "EEG 101",
  "faq" => "FAQ",
  "glossary" => "用語集"
}.freeze

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
  slug = File.basename(path, File.extname(path))

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
      title: "マインドアップロード要約冊子"
      description: "サイトの公開ページから作成した、自動生成の A4 形式ブリーフィングページ。"
      article_type: "ブリーフィング冊子"
      subtitle: "公開ページの front matter と冒頭要約から再生成した A4 ブリーフィング"
      author: マインドアップロード研究プロジェクト
      last_updated: "<%= latest_date %>"
      note: "公開ページから自動生成"
      body_class: "summary-booklet-page"
      ---
      <!-- 自動生成ファイルです。`ruby scripts/build_summary_booklet.rb` を実行してください。 -->
      <!-- 重要: この情報を削除したり上書きしたりしないでください。これはプロジェクトの恒久的な知識ベースです。 -->

      <main class="main-container summary-booklet-main">
      <article class="content-column">

      <section class="booklet-sheet booklet-cover">
        <p class="booklet-kicker">マインドアップロード・コモンズ</p>
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
          <h2>Booklet Overview</h2>
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
          <h2>What This Site Is Trying To Build</h2>
        </div>

        <div class="booklet-quote">
          <p><%= verification_page.abstract_html || h(verification_page.page_intro) %></p>
        </div>

        <div class="booklet-two-column">
          <div>
            <h3>What We Fix First</h3>
            <ul class="booklet-list">
              <%= list_items(project_scope_points) %>
            </ul>
          </div>
          <div>
            <h3>What We Do Not Claim Up Front</h3>
            <ul class="booklet-list">
              <%= list_items(project_limits) %>
            </ul>
          </div>
        </div>

        <table class="data-table booklet-table">
          <thead>
            <tr>
              <th>Lens</th>
              <th>What To Read Now</th>
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
          <h2>What Is Known and What Remains Open</h2>
        </div>

        <div class="booklet-card-grid booklet-card-grid-2">
          <article class="booklet-card booklet-card-positive">
            <h3>Relatively Well Supported</h3>
            <ul class="booklet-list">
              <%= list_items(known_points) %>
            </ul>
          </article>
          <article class="booklet-card booklet-card-caution">
            <h3>Still Open or Conditional</h3>
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
          <p class="booklet-kicker">Technical Stop Lines</p>
          <h2>Technical Stop Lines At The Front Door</h2>
        </div>

        <div class="booklet-card-grid booklet-card-grid-2">
          <article class="booklet-card booklet-card-positive">
            <h3>Observation Ceiling</h3>
            <ul class="booklet-list">
              <%= list_items(observability_stop_lines) %>
            </ul>
          </article>
          <article class="booklet-card booklet-card-caution">
            <h3>Interpretation Ceiling</h3>
            <ul class="booklet-list">
              <%= list_items(audit_stop_lines) %>
            </ul>
          </article>
        </div>

        <div class="booklet-quote">
          <p><%= h(shorten(summary_stop_lines.join(" / "), 260)) %></p>
        </div>
      </section>

      <section class="booklet-sheet booklet-page-break">
        <div class="booklet-section-header">
          <p class="booklet-kicker">Core Pages</p>
          <h2>Role of the Core Pages</h2>
        </div>

        <table class="data-table booklet-table">
          <thead>
            <tr>
              <th>Page</th>
              <th>Role</th>
              <th>Summary</th>
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
          <h2>Support Pages and Practical Routes</h2>
        </div>

        <table class="data-table booklet-table">
          <thead>
            <tr>
              <th>Page</th>
              <th>Role</th>
              <th>Summary</th>
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
          <h2>What To Do Next</h2>
        </div>

        <div class="booklet-card-grid booklet-card-grid-3">
          <%= next_action_cards_html %>
        </div>

        <div class="booklet-status-grid">
          <%= final_status_cards_html %>
        </div>

        <h3>Source Pages</h3>
        <ul class="booklet-link-list">
          <%= source_links_html %>
        </ul>

        <div class="booklet-quote">
          <p>
            This booklet is an auto-generated entry layer built from the site's public pages. Updates to each page's <strong>page_intro</strong>, <strong>page_highlights</strong>, <strong>known / unknown</strong>, and opening summary flow directly into the booklet and PDF output.
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
      ["Reference Date", latest_date],
      ["Current Focus", compact_stop_line(summary_stop_lines.first || verification_page.page_highlights.first)],
      ["Primary Entry", "#{compact_title(intro_page)} -> #{compact_title(verification_page)}"]
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
      ["What This Site Builds First", verification_page.abstract_html || h(verification_page.page_intro)],
      ["What It Does Not Claim Yet", bullet_list_html(cover_stop_lines)],
      ["Core Pages To Read Now", h(core_pages.map(&:title).join(" / "))]
    ]
    render_cards(cards)
  end

  def contents_cards_html
    cards = [
      ["1. Site Scope", intro_page.page_intro],
      ["2. Known vs Unknown", verification_page.accuracy_note],
      ["3. Core Page Roles", roadmap_page.page_intro],
      ["4. Support Routes", content_hub_page.page_intro],
      ["5. Next Actions", issue_page.page_intro],
      ["6. Source Pages", "The booklet closes with a compact route back to the detailed public pages."]
    ]
    render_cards(cards.map { |title, body| [title, h(shorten(body, 120))] })
  end

  def status_cards_html
    cards = [
      ["In One Sentence", intro_page.page_highlights.first, "booklet-status-card booklet-status-card-strong"],
      ["Main Takeaway", "The project scope, realistic work range, reading order, and the stop lines around hidden-state / proxy / drift claims", "booklet-status-card"]
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
    (technical_unknown_points + intro_page.unknown_points + perspective_page.unknown_points + eeg_page.unknown_points).uniq.first(4)
  end

  def overview_rows_html
    rows = [
      ["入口", intro_page],
      ["検証コモンズ", verification_page],
      ["技術マップ", roadmap_page],
      ["理論的整理", perspective_page]
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
    (summary_stop_lines + intro_page.known_points + verification_page.known_points + datasets_page.known_points).uniq.first(5)
  end

  def unknown_points
    (technical_unknown_points + intro_page.unknown_points + verification_page.unknown_points + perspective_page.unknown_points + eeg_page.unknown_points).uniq.first(5)
  end

  def timeline_cards_html
    items = [
      ["ステップ 1", "入口", intro_page.page_highlights.first || intro_page.page_intro],
      ["ステップ 2", "L0", datasets_page.page_highlights.first || datasets_page.page_intro],
      ["ステップ 3", "L1-L2", verification_page.page_highlights[1] || verification_page.page_intro],
      ["後続", "高レベル主張", roadmap_page.unknown_points.first || perspective_page.unknown_points.first]
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
      bullets = (prioritized_page_bullets(page_data) + page_data.page_highlights + page_data.known_points).uniq.first(3)
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
      ["全体像をつかむ", "#{intro_page.title} -> #{verification_page.title} -> #{roadmap_page.title}", intro_page.recommended_pages],
      ["ヒト・プロキシ束を監査する", "#{wbe_page.title} -> ヒト・プロキシ構成 -> 測定スタック", [
        { "label" => "WBE 101", "url" => wbe_page.url },
        { "label" => "ヒト・プロキシ構成", "url" => "/wiki/human-proxy-composition.html" },
        { "label" => "測定スタック", "url" => "/wiki/measurement-stack-and-claim-ceiling.html" }
      ]],
      ["参加して統合する", "#{issue_page.title} / #{content_hub_page.title}", issue_page.recommended_pages]
    ]

    cards.map do |title, body, links|
      extra_links = links.first(3).map { |item| %(<li><a href="#{item.fetch("url")}">#{h(item.fetch("label"))}</a></li>) }.join
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
      ["Working Principle", issue_page.page_highlights.first || issue_page.page_intro, "booklet-status-card booklet-status-card-strong"],
      ["Update Rule", "Whenever a public page changes, the deploy/PDF workflow regenerates the booklet.", "booklet-status-card"]
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

  def summary_stop_lines
    @summary_stop_lines ||= preferred_points(
      technical_point_pool,
      queries: SUMMARY_PRIORITY_QUERIES,
      fallback_patterns: SCIENCE_STOPLINE_PATTERNS,
      reject_patterns: SUMMARY_REJECT_PATTERNS,
      limit: 6
    )
  end

  def cover_stop_lines
    preferred = summary_stop_lines.map { |line| compact_stop_line(line) }.uniq
    fallback = [
      "Connectome-complete is not emulation-complete.",
      "Human evidence remains layered and proxy-based.",
      "Same-subject wording does not make one state sample.",
      "Proxy bundles need compatibility, repeatability, and disagreement audits."
    ]
    (preferred + fallback).uniq.first(4)
  end

  def observability_stop_lines
    @observability_stop_lines ||= preferred_points(
      technical_point_pool,
      queries: OBSERVABILITY_PRIORITY_QUERIES,
      fallback_patterns: OBSERVABILITY_PATTERNS,
      reject_patterns: SUMMARY_REJECT_PATTERNS,
      limit: 4
    )
  end

  def audit_stop_lines
    @audit_stop_lines ||= preferred_points(
      technical_point_pool,
      queries: AUDIT_PRIORITY_QUERIES,
      fallback_patterns: AUDIT_PATTERNS,
      reject_patterns: SUMMARY_REJECT_PATTERNS,
      limit: 4
    )
  end

  def technical_unknown_points
    @technical_unknown_points ||= begin
      points = select_points(
        technical_unknown_pool,
        patterns: TECHNICAL_UNRESOLVED_PATTERNS,
        reject_patterns: SUMMARY_REJECT_PATTERNS,
        limit: 5
      )
      points.empty? ? summary_stop_lines.first(5) : points
    end
  end

  def prioritized_page_bullets(page_data)
    if page_data.slug == "faq"
      return preferred_points(
        page_data.page_highlights + page_data.known_points,
        queries: FAQ_PRIORITY_QUERIES,
        fallback_patterns: SCIENCE_STOPLINE_PATTERNS,
        reject_patterns: SUMMARY_REJECT_PATTERNS,
        limit: 3
      )
    end

    points = select_points(
      page_data.page_highlights + page_data.known_points,
      patterns: SCIENCE_STOPLINE_PATTERNS,
      reject_patterns: SUMMARY_REJECT_PATTERNS,
      limit: 3
    )
    points.empty? ? (page_data.page_highlights + page_data.known_points).uniq.first(3) : points
  end

  def technical_point_pool
    @technical_point_pool ||= [
      intro_page,
      verification_page,
      roadmap_page,
      perspective_page,
      datasets_page,
      wbe_page,
      eeg_page,
      faq_page
    ].flat_map { |page_data| page_data.page_highlights + page_data.known_points }.uniq
  end

  def technical_unknown_pool
    @technical_unknown_pool ||= [
      intro_page,
      verification_page,
      perspective_page,
      datasets_page,
      wbe_page,
      eeg_page,
      faq_page
    ].flat_map { |page_data| page_data.unknown_points + page_data.known_points + page_data.page_highlights }.uniq
  end

  def select_points(points, patterns:, reject_patterns:, limit:)
    ranked = Array(points).each_with_index.map do |point, index|
      text = normalize_text(point)
      next if text.empty?
      next if reject_patterns.any? { |pattern| pattern.match?(text) }

      score = patterns.sum { |pattern, weight| pattern.match?(text) ? weight : 0 }
      next if score.zero?

      [text, score, index]
    end.compact

    ranked
      .sort_by { |text, score, index| [-score, index, text.length] }
      .each_with_object([]) do |(text, _score, _index), selected|
        selected << text unless selected.include?(text)
        break selected if selected.length >= limit
      end
  end

  def preferred_points(points, queries:, fallback_patterns:, reject_patterns:, limit:)
    pool = Array(points).map { |point| normalize_text(point) }
                        .reject(&:empty?)
                        .reject { |text| reject_patterns.any? { |pattern| pattern.match?(text) } }
                        .uniq

    preferred = queries.each_with_object([]) do |query, selected|
      match = pool.find { |text| query.match?(text) }
      selected << match if match && !selected.include?(match)
    end

    return preferred.first(limit) if preferred.length >= limit

    fallback = select_points(
      pool,
      patterns: fallback_patterns,
      reject_patterns: reject_patterns,
      limit: limit
    )

    (preferred + fallback).uniq.first(limit)
  end

  def page_role(page_data)
    [page_data.article_type, page_data.subtitle].reject(&:empty?).join(" - ")
  end

  def render_cards(cards)
    cards.map do |title, body|
      rendered_body = body.to_s.lstrip.start_with?("<") ? body : "<p>#{body}</p>"
      <<~HTML
        <article class="booklet-card">
          <h3>#{h(title)}</h3>
          #{rendered_body}
        </article>
      HTML
    end.join
  end

  def list_items(items)
    Array(items).map { |item| "<li>#{h(item)}</li>" }.join
  end

  def bullet_list_html(items)
    <<~HTML
      <ul class="booklet-list">
        #{list_items(items)}
      </ul>
    HTML
  end

  def compact_title(page_data)
    COMPACT_TITLE_MAP.fetch(page_data.slug, page_data.title)
  end

  def compact_stop_line(text)
    plain = normalize_text(text)
    rule = COMPACT_STOPLINE_RULES.find { |pattern, _replacement| pattern.match?(plain) }
    return rule[1] if rule

    shorten(plain, 72)
  end

  def shorten(text, max)
    plain = normalize_text(text)
    return plain if plain.length <= max

    sentence = plain.match(/\A(.{1,#{max}}?[.!?])(?:\s|$)/)
    return sentence[1].rstrip if sentence

    snippet = plain[0, max - 1].rstrip
    cut = snippet.rindex(/\s/)
    snippet = snippet[0...cut].rstrip if cut && cut >= (max / 2)
    "#{snippet}…"
  end

  def h(text)
    CGI.escapeHTML(text.to_s)
  end
end

pages = SOURCE_PATHS.map { |path| load_page(path) }
output = SummaryBookletTemplate.new(pages).render
File.write(OUTPUT_PATH, output)
puts "生成しました: #{OUTPUT_PATH}"
