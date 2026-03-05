# Mind-Upload
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

マインドアップロード実現のための中核となるコアサイト。

## 目的

このサイトは、マインドアップロードの実現に向けた技術・研究・コミュニティの中心的ハブとなることを目指しています。

ここでいうマインドアップロードとは、**意識や記憶の交換・複製を可能とする技術**を指します。

## 今後の展望

本プロジェクトは、最終的にサイトの更新や運用プロセスを完全に自動化することを目指しています。現在は手動で行っているタスクも、順次自動化ツールやCI/CDパイプラインへ移行する予定です。

## 貢献方法

- [issue.md](issue.md) を参照
- [Issueを立てる](https://github.com/yasufumi-nakata/mind-upload/issues)

## 公開コンテンツ統合ポリシー

- 公開ページの統合先は [content_hub.md](content_hub.md) で一元管理します。
- 新規ファイルを作成する前に、既存ページ（`verification.md` / `tech_roadmap.md` / `perspective.md` / `research_harvest_50.md` / `issue.md`）へ統合可能かを確認します。
- 中間成果・作業ログ・自動生成物は原則 `automation/` または `ignore/` で管理し、公開導線は `index.md` と `content_hub.md` に集約します。

## GitHub Wiki 運用

- 学習用の wiki 本体は GitHub Wiki を前提にします。
- リポジトリ内の `wiki/` は GitHub Wiki 用ソースとして扱い、サイト内の学習ページ編集もここで行います。
- 閲覧入口:
  - GitHub Wiki Home: https://github.com/yasufumi-nakata/mind-upload/wiki
  - EEG-DATA × 助成マップ: https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-data-fund-map
- 編集入口:
  - Wiki Home source: [wiki/index.md](wiki/index.md)
  - EEG-DATA × 助成マップ source: [wiki/mind-upload-eeg-data-fund-map.md](wiki/mind-upload-eeg-data-fund-map.md)
- GitHub Wiki 用の出力は `github-wiki-export/` に生成します。
- 生成は `scripts/export_github_wiki.rb`、反映は `scripts/publish_github_wiki.sh` を使います。
- `scripts/publish_github_wiki.sh` は、GitHub Wiki の clone 先をリポジトリ内の `ignore/github-wiki-publish/` に固定しており、リポジトリ外に `wiki/` フォルダを作りません。
- `scripts/clean_github_wiki_noise.rb` は、`wiki/` と `github-wiki-export/` に混入した `.DS_Store` や `._*` を除去します。
- `scripts/check_github_wiki_boundaries.rb` は、`publish` が repo 内 `ignore/github-wiki-publish/` 固定のままで、`mktemp` や外部作業先 override が戻っていないことを検査します。
- `scripts/verify_github_wiki_toolchain.sh` は、syntax check、boundary check、noise cleanup、export、export validate をまとめて実行します。`VERIFY_GITHUB_WIKI_BUILD=1` を付けると `BUNDLE_PATH=vendor/bundle bundle exec jekyll build` まで含めて確認できます。
- export 検査は `scripts/check_github_wiki_export.rb` を使います。`wiki/**/*.md` の export 漏れ、`wiki/generated/` のコピー漏れ、GitHub Wiki 上で解決できない相対リンク、`_Sidebar.md` への掲載漏れ、`EEG-DATA × 助成マップ` 本文で参照している CSV 名と実ファイルの不一致、`.DS_Store` などの混入、`github-wiki-export/` の未反映更新を検出します。
- `scripts/export_github_wiki.rb` は、`SIDEBAR_GROUPS` に未分類の wiki ページがあっても、`その他` セクションへ自動掲載します。
- GitHub Wiki の git リポジトリは、GitHub の Web UI で最初の Wiki ページを 1 つ作成した後でないと clone / push できません。その初期化後に `scripts/publish_github_wiki.sh` を実行してください。
- `.github/workflows/sync-github-wiki.yml` も追加してあり、初期化後は `main` への push で `export -> validate -> publish` を自動実行できます。
- `.github/workflows/validate-github-wiki-export.yml` も追加してあり、Pull Request 段階で `export -> validate -> jekyll build` を先に確認できます。
- GitHub Actions の既定トークンで不足する場合は、`GH_WIKI_TOKEN` シークレットに `repo` 権限のトークンを設定してください。

## LLM向けプロンプトの利用

- LLMに調査や分析を依頼する際の科学者スタイルのプロンプト例は [.agent/agent.md](.agent/agent.md) にまとめています。
- AI運用時は、実行可能な作業だけを提案・実施する「握れるボール原則」を必ず遵守してください（[.agent/agent.md](.agent/agent.md) の該当節）。

## リンク

- **GitHub**: https://github.com/yasufumi-nakata/mind-upload
- **GitHub Wiki**: https://github.com/yasufumi-nakata/mind-upload/wiki

## システム構成 (System Architecture)

本プロジェクトでは、AIエージェントを活用した半自動的なコンテンツ更新ワークフローを採用しています。

```mermaid
graph LR
    A[ユーザー] -->|Issue作成| B(Manus AI)
    B -->|Issue登録| C[GitHub Issues]
    C -->|Issue取得| D(Antigravity)
    D -->|コード修正・コミット| E[GitHub Repository]
    E -->|自動デプロイ| F[GitHub Pages]
    F -->|閲覧| A
```

### ワークフロー

1.  **Issue作成 (Manus)**: ユーザーがManus AIに対して改善提案や新機能のリクエストを伝えると、ManusがGitHub Issueを自動作成します。
2.  **Issue処理 (Antigravity)**: Antigravity（本エージェント）がオープンなIssueを取得し、コードベースを分析・修正し、コミット＆プッシュを行います。コミットメッセージに `Fixes #N` を含めることで、Issueは自動的にクローズされます。
3.  **デプロイ (GitHub Pages)**: `main` ブランチへのプッシュをトリガーに、GitHub Pagesが自動的にサイトを更新します。

## ホスティング

- GitHub Pages
