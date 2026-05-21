## 概要

-

## 変更の種類

- [ ] 誤字・表記修正
- [ ] 本文・構成改善
- [ ] 出典・論文・データセット追加
- [ ] 外部翻訳ページ修正
- [ ] 表示・アクセシビリティ改善
- [ ] ビルド・CI・運用保守

## 確認したこと

- [ ] 公開ページの導線は `index.html` / `content_hub.html` から自然につながっています。
- [ ] 出典、原典URL、ライセンス表示を必要な箇所に残しています。
- [ ] 秘密情報、非公開データ、個人情報、認証情報を含めていません。
- [ ] 外部翻訳ページを変更した場合、該当 `.html` を直接確認しました。

## 実行したチェック

- [ ] `ruby scripts/build_summary_booklet.rb`
- [ ] `bundle exec jekyll build`
- [ ] `git diff --check`
- [ ] `node --check .github/pdf/render-summary-pdf.mjs`（PDF生成や該当JSを変更した場合）

## 補足

- レビュー時に重点的に見てほしい点:
- 未確認の点:
