# Mind Uploading Research Guide

Source for [mind-upload.com](https://mind-upload.com/) and its [Japanese edition](https://mind-upload.com/ja/). The November 2026 edition covers the technical foundations of whole-brain emulation, current experimental evidence, Carboncopies Foundation research, validation, research projects, and a searchable literature catalogue. Philosophy, ethics, and fictional timelines are outside this edition's scope.

## Editing and preview

Edit the bilingual text in `content/site_content.py` and bibliographic records in `content/references.json`. Do not edit generated HTML directly.

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
python3 -m http.server 8099
```

Open `http://localhost:8099/` or `http://localhost:8099/ja/`. Python 3's standard library is sufficient for building and checking the site. The site itself has no package dependencies or external JavaScript services.

## Structure

Each language contains nine matched pages: home, science, progress, Carboncopies, validation, roadmap, research projects, history, and resources. Legacy philosophy and scenario URLs redirect to validation and the technical roadmap. `assets/research.js` implements bibliography filtering and an illustrative data-volume calculator. `assets/figures/` contains credited scientific figures and original explanatory diagrams.

The generator resolves `[[REFERENCE_ID]]` to numbered references local to each page, renders `{{FIGURE_ID}}` with captions, exports BibTeX/JSON, and updates the sitemap and language metadata. Update the edition date in the generator and the dated prose together. Verify the calculator, library filters, navigation, and representative desktop/mobile layouts in Chrome after substantial changes.

## Editorial and source policy

- Support experimental claims with primary papers and organizational claims with official pages.
- Distinguish experiments, theoretical models, preprints, historical proposals, and our own suggested research designs.
- Record the organism, anatomical boundary, measured variables, and validation conditions. A structural connectome does not establish complete functional emulation.
- The catalogue is a scoped discovery collection, not an exhaustive systematic review. Retrieval status does not mean a paper was read in full or independently reproduced.
- Keep full texts, private collection manifests, browser logs, and Drive identifiers outside the public repository. Public records link to legitimate distribution sources.
- Keep English and Japanese claims, citations, figure credits, and metadata synchronized.

## Hosting and rights

GitHub Pages serves `main` from the repository root. `CNAME` preserves `mind-upload.com`. Check the deployed revision and actual public pages after pushing.

Figure sources and reuse conditions are documented in [assets/figures/README.md](assets/figures/README.md) and individual captions. Third-party CC BY figures retain their attribution; their licenses do not license the rest of this repository. No blanket repository license is granted here.

## 日本語

全脳エミュレーションを実験・測定・検証の課題として整理する技術研究ガイドです。2026年11月版ではCarboncopies Foundationの公開研究計画、周辺技術の文献カタログ、検証設計、技術ロードマップを追加しています。公式団体サイトではありません。本文の更新元は `content/site_content.py`、引用情報は `content/references.json` です。公開前に英日対応、引用、図版、リンク、画面を確認してください。
