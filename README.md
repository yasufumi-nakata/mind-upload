# Mind-Upload

<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

マインドアップロード（WBE: Whole Brain Emulation）を「検証可能な科学」に寄せるための公共財サイト。

ここでいうマインドアップロードとは、**意識や記憶の交換・複製を可能とする技術**を指します。

## リンク

| リソース | URL |
|---------|-----|
| 公開サイト | https://mind-upload.com |
| GitHub | https://github.com/yasufumi-nakata/mind-upload |
| GitHub Wiki | https://github.com/yasufumi-nakata/mind-upload/wiki |

## ディレクトリ構成

```
/
├── index.md                  # トップページ
├── *.md (ルート直下)          # 公開ページ群（Jekyll でビルド）
├── _config.yml               # Jekyll 設定
├── _layouts/default.html     # 全ページ共通レイアウト
├── assets/css/               # スタイルシート
├── wiki/                     # GitHub Wiki ソース（学習・入門コンテンツ）
├── automation/               # 中間成果・作業ログ・自動生成物（非公開）
├── scripts/                  # GitHub Wiki 運用スクリプト群
├── github-wiki-export/       # Wiki エクスポート先（自動生成）
├── .agent/agent.md           # AI エージェント行動規範
├── AGENTS.md                 # AI エージェント向け運用ガイド
├── .github/workflows/        # CI/CD
└── ignore/                   # 一時ファイル（.gitignore 対象）
```

公開ページの一覧と各ファイルの役割は `AGENTS.md` を参照してください。

## セットアップ

```bash
bundle install
bundle exec jekyll serve
# → http://localhost:4000
```

## 公開コンテンツ統合ポリシー

- 公開ページの統合先は [content_hub.md](content_hub.md) で一元管理します。
- 新規ファイルを作成する前に、既存ページへ統合可能かを確認します。
- 中間成果・作業ログ・自動生成物は `automation/` または `ignore/` で管理し、公開導線は `index.md` と `content_hub.md` に集約します。

## システム構成

AIエージェントを活用した半自動的なコンテンツ更新ワークフローを採用しています。

```mermaid
graph LR
    A[ユーザー] -->|Issue作成| B(Manus AI)
    B -->|Issue登録| C[GitHub Issues]
    C -->|Issue取得| D(Antigravity)
    D -->|コード修正・コミット| E[GitHub Repository]
    E -->|自動デプロイ| F[GitHub Pages]
    F -->|閲覧| A
```

1. **Issue作成**: ユーザーが Manus AI へ改善提案を伝え、GitHub Issue が自動作成されます。
2. **Issue処理**: AI エージェントが Issue を取得・実装し、`Fixes #N` 付きでコミットします。
3. **デプロイ**: `main` ブランチへの push で GitHub Pages が自動更新されます。

## GitHub Wiki 運用

- Wiki 本体は GitHub Wiki を前提にします。リポジトリ内の `wiki/` が Wiki ソースです。
- エクスポート: `scripts/export_github_wiki.rb`
- 公開: `scripts/publish_github_wiki.sh`
- 検証: `scripts/verify_github_wiki_toolchain.sh`
- 同期（検証→公開）: `scripts/sync_github_wiki_toolchain.sh`
- CI: `.github/workflows/sync-github-wiki.yml`（main push 時に自動実行）
- PR 検証: `.github/workflows/validate-github-wiki-export.yml`

各スクリプトのセルフテストは `scripts/selftest_*.sh` にあります。`verify_github_wiki_toolchain.sh` に環境変数を付けると個別に実行できます（詳細は各スクリプトのヘッダーコメントを参照）。

## AI エージェント向け情報

- 運用ルール・ファイル配置ルール・禁止事項の詳細は [`AGENTS.md`](AGENTS.md) を参照してください。
- 行動規範・思考サイクルは [`.agent/agent.md`](.agent/agent.md) を参照してください。

## 貢献方法

- [issue.md](issue.md) を参照
- [Issue を立てる](https://github.com/yasufumi-nakata/mind-upload/issues)

## ホスティング

- GitHub Pages（カスタムドメイン: mind-upload.com）
