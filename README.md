# マインドアップロード・コモンズ

このリポジトリは、マインドアップロードと Whole Brain Emulation を、検証可能な研究課題として読むための公開サイトです。

公開サイトに載せる内容は、読者がそのまま参照できる日本語のページに限定します。作業報告、生成ログ、内部監査、重複エクスポート、個別の運用手順は公開コンテンツには含めません。

## 公開ページ

- `index.md`: 最初に読む入口
- `verification.md`: 検証条件、反証条件、再現性の基準
- `tech_roadmap.md`: 技術ロードマップ
- `datasets.md`: 公開データと L0 実践
- `mind_uploading_papers.md`: 論文アーカイブ
- `research_harvest_50.md`: 未解決課題と文献マップ
- `classic_mu_archive.md`: ibiblio 版 Mind Uploading Home Page の日本語ガイド
- `external/compcogneuro/`: compcogneuro 公開リポジトリ群の日本語全文翻訳
- `external/netpyne/`: NetPyNE docs の日本語全文翻訳
- `external/opensourcebrain/documentation/`: OpenSourceBrain Documentation の日本語全文翻訳
- `wiki/`: 基礎学習、用語、読み方の補助ページ

## 公開範囲

GitHub Pages には Jekyll が生成した `_site` だけを配信します。リポジトリ直下の設定ファイル、ビルド用スクリプト、GitHub Actions 設定は、公開ページとして配信しません。

ページを追加する場合は、まず既存の公開ページまたは `wiki/` の学習ページに統合できるかを確認します。独立ページにするのは、読者の導線が明確に改善される場合だけです。

## ローカル確認

```bash
ruby scripts/build_summary_booklet.rb
bundle exec jekyll build
```

ビルド後は `_site` の中身だけが公開成果物です。
