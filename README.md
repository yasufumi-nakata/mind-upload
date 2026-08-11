# Mind Uploading: An Integrated Guide

This is the source repository for [`mind-upload.com`](https://mind-upload.com/), a static reference site about mind uploading (whole brain emulation, or WBE). It brings together the field's history, scientific foundations, current progress, forecasts, philosophy and ethics, and practical next steps, with an emphasis on primary sources.

The site distinguishes established facts, conditional extrapolations, and philosophical or speculative arguments. English is the primary language; Japanese is provided as a secondary, chapter-matched translation.

## Live site

- [English site — primary](https://mind-upload.com/)
- [Japanese site — secondary](https://mind-upload.com/ja/)

## Site map

| Content | English | Japanese |
| --- | --- | --- |
| Home | [`index.html`](index.html) | [`ja/index.html`](ja/index.html) |
| Chapter 1: History | [`history.html`](history.html) | [`ja/history.html`](ja/history.html) |
| Chapter 2: Scientific foundations | [`science.html`](science.html) | [`ja/science.html`](ja/science.html) |
| Chapter 3: Current status and progress dashboard | [`progress.html`](progress.html) | [`ja/progress.html`](ja/progress.html) |
| Chapter 4: Forecasts | [`future.html`](future.html) | [`ja/future.html`](ja/future.html) |
| Chapter 5: Philosophy and ethics | [`philosophy.html`](philosophy.html) | [`ja/philosophy.html`](ja/philosophy.html) |
| Chapter 6: What to do now | [`action.html`](action.html) | [`ja/action.html`](ja/action.html) |
| Appendix: Resources, glossary, and FAQ | [`resources.html`](resources.html) | [`ja/resources.html`](ja/resources.html) |
| Companion: Scenario 2050 | [`scenario.html`](scenario.html) | [`ja/scenario.html`](ja/scenario.html) |

## Repository layout

```text
.
├── index.html              # English home page
├── *.html                  # English chapters and appendices
├── ja/*.html               # Japanese chapters and appendices
├── assets/
│   ├── site.css            # Shared site design
│   ├── site.js             # Shared interactions
│   ├── scenario.css        # Scenario page styles
│   ├── scenario.js         # Scenario page interactions
│   ├── favicon.svg
│   └── og-image.*
├── CNAME                   # Custom domain: mind-upload.com
├── robots.txt
├── sitemap.xml
└── .claude/launch.json     # Local launch configuration, port 8099
```

## Local preview

No package installation or build step is required. From the repository root, start a static file server:

```bash
python3 -m http.server 8099
```

Then open:

- <http://localhost:8099/>
- <http://localhost:8099/ja/>
- <http://localhost:8099/scenario.html>

The pages use root-relative paths such as `/assets/` and `/ja/`. Serve the repository root rather than opening HTML files directly with `file://`.

## Updating the site

1. When changing an English chapter, review and update its matching Japanese chapter.
2. Check the page body as well as `title`, description, canonical URL, `hreflang`, Open Graph metadata, and JSON-LD.
3. When changing the site date, keep the visible date, structured data, and `lastmod` values in [`sitemap.xml`](sitemap.xml) consistent.
4. Test chapter links, the English/Japanese switcher, the mobile navigation, and the scenario page's scroll interactions locally.
5. Run the following check before and after changes:

   ```bash
   git diff --check
   ```

There is currently no automated build or test suite. Before publishing, check the main pages in a browser for broken links and layout issues.

## Editorial policy

- Link claims to peer-reviewed papers, official announcements, or other primary sources whenever possible.
- Make it clear when a claim relies only on secondary reporting.
- Keep fact, extrapolation, and speculation separate. Treat forecasts as conditional estimates.
- Maintain the progress dashboard (Chapter 3) as a dated snapshot, and label editorial estimates as such.
- Information about brain-preservation services, medicine, and end-of-life decisions is informational only; it is not a recommendation or medical advice.

## Hosting

[`CNAME`](CNAME) declares the custom domain `mind-upload.com`. If the hosting configuration changes, keep the canonical URLs, alternate-language URLs, Open Graph URLs, [`robots.txt`](robots.txt), and [`sitemap.xml`](sitemap.xml) consistent.

## License

There is currently no `LICENSE` file in this repository. Check the rights and license of the relevant copyright holder before reusing the text, artwork, or cited materials.

## 日本語（概要）

本リポジトリは、マインドアップロード（全脳エミュレーション）を扱う静的なリファレンスサイト [`mind-upload.com`](https://mind-upload.com/) のソースです。英語版をメインとし、日本語版を[`/ja/`](https://mind-upload.com/ja/)で提供しています。

歴史、科学的基礎、現在の進捗、未来予測、哲学・倫理、行動指針、資料集、シナリオ2050を、一次資料を中心に整理しています。ローカル確認、更新時の英日同期、メタデータ・サイトマップの整合、免責事項については、上記の英語版説明をご確認ください。
