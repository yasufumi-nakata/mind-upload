# マインドアップロード・コモンズ

このリポジトリは、マインドアップロードと Whole Brain Emulation を、検証可能な研究課題として読むための公開サイトです。

公開サイトに載せる内容は、読者がそのまま参照できる日本語のページに限定します。作業報告、生成ログ、内部監査、重複エクスポート、個別の運用手順は公開コンテンツには含めません。

## 公開ページ

- `index.html`: 最初に読む入口
- `verification.html`: 検証条件、反証条件、再現性の基準
- `tech_roadmap.html`: 技術ロードマップ
- `datasets.html`: 公開データと L0 実践
- `research_harvest_50.html`: 未解決課題と文献マップ
- `classic_mu_archive.html`: ibiblio 版 Mind Uploading Home Page の日本語ガイド
- `external/compcogneuro/`: compcogneuro 公開リポジトリ群の日本語全文翻訳
- `external/netpyne/`: NetPyNE docs の日本語全文翻訳
- `external/opensourcebrain/documentation/`: OpenSourceBrain Documentation の日本語全文翻訳

## 公開範囲

GitHub Pages には Jekyll が生成した `_site` だけを配信します。リポジトリ直下の設定ファイル、ビルド用スクリプト、GitHub Actions 設定は、公開ページとして配信しません。

ページを追加する場合は、まず既存の公開 HTML ページへ統合できるかを確認します。独立ページにするのは、読者の導線が明確に改善される場合だけです。

## ローカル確認

```bash
ruby scripts/build_summary_booklet.rb
bundle exec jekyll build
```

ビルド後は `_site` の中身だけが公開成果物です。

## コントリビューション

誤字修正、翻訳修正、出典追加、表示改善、ビルド保守などを歓迎します。初めて参加する場合は [CONTRIBUTING.md](CONTRIBUTING.md) を読んでください。

- 行動規範: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- セキュリティ報告: [SECURITY.md](SECURITY.md)
- Pull Request の確認事項: [.github/pull_request_template.md](.github/pull_request_template.md)

大きな新規ページ、大量翻訳、ライセンス判断が必要な変更は、先に Issue で相談してください。
