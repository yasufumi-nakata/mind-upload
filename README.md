# Mind Uploading Research Guide

This site's purpose is to help turn the idea of mind uploading into a concrete research programme: show the foundations already available, the routes worth pursuing, the experiments that connect them, and what each successful step would make possible. Readers should be able to see where the field stands and how they can help it advance. The editorial principles are recorded in [AGENTS.md](AGENTS.md).

Source for [mind-upload.com](https://mind-upload.com/) and its [Japanese edition](https://mind-upload.com/ja/), a personal research guide written and edited by [yasufumi-nakata](https://github.com/yasufumi-nakata). Carboncopies Foundation material is cited as a source; the Foundation is not the publisher or editorial supervisor of this site. The November 2026 edition covers the technical foundations of whole-brain emulation, experimental evidence, validation, research projects, and a searchable literature catalogue. Philosophy and institutional ethics are outside this edition's scope; review, consent and sample access appear only as prerequisites for research data acquisition. The 2050 roadmap is a conditional research plan with editorial review windows, not a forecast or an official organisational schedule.

## Editing and preview

Edit the bilingual text in `content/site_content.py`, the shared six-domain dashboard and five planning windows in `content/dashboard.py`, the complementary research routes in `content/routes.py`, the shared stages, stable task IDs and achievement rubric in `content/research_plan.py`, terminology in `content/terms.py`, and bibliographic records in `content/references.json`. Do not edit generated HTML directly.

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
python3 -m unittest discover -s tests
python3 -m http.server 8099
```

Open `http://localhost:8099/` or `http://localhost:8099/ja/`. Python 3's standard library is sufficient for building and checking the site. The optional `scripts/render_share_image.py` image regeneration requires Matplotlib; ordinary builds use the existing image. The site itself has no package dependencies or external JavaScript services.

## Structure

Each language contains nine matched pages: home, science, progress, Carboncopies, validation, roadmap, research projects, history, and resources. Legacy philosophy and scenario URLs redirect to validation and the technical roadmap. `assets/research.js` implements bibliography filtering, an illustrative data-volume calculator, and an imaging-throughput calculator. `assets/figures/` contains credited scientific figures and original explanatory diagrams.

The generator resolves `[[REFERENCE_ID]]` to numbered references local to each page, renders `{{FIGURE_ID}}` with captions, exports BibTeX/JSON and `CITATION.cff`, and updates the sitemap and language metadata. Set the edition date only in `content/edition.py`; individual source access dates remain in their reference records. Use `{{edition_date}}` for edition dates inside page bodies. Verify calculators, library filters, navigation, and representative desktop/mobile layouts in Chrome after substantial changes. CI runs the regression checks, rebuilds, rejects generated-file drift, and checks the site.

## Editorial and source policy

- Support experimental claims with primary papers and organizational claims with official pages.
- Distinguish experiments, theoretical models, preprints, historical proposals, and our own suggested research designs.
- Record the organism, anatomical boundary, measured variables, and validation conditions. A structural connectome does not establish complete functional emulation.
- Publish only sources whose acquired full text was read and whose claims were checked. The November 2026 revision uses 57 papers, reports, chapters and commentaries plus 10 official or historical web sources. Each catalogue entry records its review scope; caption reading, visual inspection and separate supplements are distinguished.
- Exclude unavailable material and stored-but-unread papers from public claims, references and BibTeX/JSON. The private storage inventory is separate. This is a scoped guide, not an exhaustive systematic review or an experimental replication.
- Keep full texts, private collection manifests, browser logs, and Drive identifiers outside the public repository. Public records link to legitimate distribution sources.
- Keep English and Japanese claims, citations, figure credits, and metadata synchronized.

The 6 November update addresses Issues #282–292. A focused Scopus query of 20 candidate DOIs returned 19 records. Eleven additional sources were adopted after full-text review from legitimate distribution sources. Search matches and download notifications alone do not establish retrieval or review. White (1986) is attributed through the reviewed Cook (2019) account; the unreviewed White original and Markram (2015) candidate are not new catalogue entries. This update adds no experimental results or simulations.

The 9 November update adds six scoped full-text reviews after 35 cross-domain queries. The [search method](docs/literature-search-2026-11-09.md) records scope, inclusion decisions and limits. The generated [literature index](data/literature-index.json) maps all 67 adopted sources to actual bilingual page citations. DOI normalization, duplicate detection and review-scope validation run during every build. Six proposed experiments connect these findings to existing task IDs; they are designs, not new experimental results.

## Hosting and rights

GitHub Pages serves `main` from the repository root. `CNAME` preserves `mind-upload.com`. Check the deployed revision and actual public pages after pushing.

Figure sources and reuse conditions are documented in [assets/figures/README.md](assets/figures/README.md) and individual captions. Third-party CC BY figures retain their attribution; their licenses do not license the rest of this repository. No blanket repository license is granted here.

Use [CITATION.cff](CITATION.cff) to cite the guide, adding the specific page, access date and a commit permalink when a fixed version is needed. No DOI is assigned. Questions and correction requests belong in [GitHub Issues](https://github.com/yasufumi-nakata/mind-upload/issues), with the affected statement and supporting evidence. Accepted changes remain visible in the commit history. Earlier editions and third-party materials should be consulted with their own attached terms.

## 日本語

理念は「SFを現実にするために、マインドアップロードの実現へ向けた技術的な道筋を示すこと」です。現在の成果から出発し、複数の研究ルート、残る実証、次に行える研究、その成功が開く可能性を分かりやすく示します。実現までの距離を具体的な段階と接続で示し，公開した実証条件を満たした分を「達成率（本サイト基準）」として算出します。配点は編集上の判断で，成功確率・作業量・残り年数を表しません。未評価の配点も100点の分母に残し，必須条件を合計点と別に確認します。詳しい編集方針は [AGENTS.md](AGENTS.md) に記載しています。

yasufumi-nakataが執筆・編集する個人の技術研究ガイドです。Carboncopies Foundationの公開資料を引用元として扱います。2026年11月の改訂では、取得した本文を確認した57資料と公式・歴史的ウェブ資料10件を使用しています。未取得資料と保管のみの未読資料は公開引用から除外し、図説明・図像・別添補足の確認範囲を区別しています。11月6日の追補はIssue #282–292に対応し、追加11資料を採用しました。11月7日の追補はIssue #293–307に対応し，Scopusの7件の書誌照合と原典の確認を経て4資料を追加しました。11月9日の追補では英日35検索式の横断探索から6資料を追加し、全67資料の引用箇所索引とDOI重複検査、既存の研究課題に対応する六つの実験案を加えました。探索方法と採用基準・限界は [検索方法](docs/literature-search-2026-11-09.md) を参照してください。未読候補は公開引用へ混ぜていません。本文は `content/site_content.py`，正式題名 `SITE_TITLE` と版の日付は `content/edition.py`，引用情報は `content/references.json` で管理します。本サイト全体への包括的な再利用許諾は付与していません。公開前に英日対応、引用、図版、リンク、画面を確認してください。


The rubric starts at 10/100 points (version 1.0, 7 November 2026): four bounded foundational achievements. M1–M4 do not yet meet all criteria in the reviewed evidence; later items totaling 55 points remain unassessed in this scoped audit. `score()` derives current and conditional increments from stable IDs. Stage completion also requires all preceding mandatory items; points elsewhere cannot replace them. The same data generate Japanese/English summaries and `data/progress.json`. Evidence changes and rubric/weight changes must be logged separately.

`{{site_title}}` uses the shared formal title. `{{edition_date}}` expands to Japanese or English display dates; ISO dates remain in machine-readable metadata. Historical change entries retain their actual dates. The glossary and first-use explanations are generated from the term registry; bibliography titles and existing links are protected.
