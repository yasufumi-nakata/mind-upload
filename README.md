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
- `scripts/clean_github_wiki_noise.rb` は、`wiki/` と `github-wiki-export/` に混入した `.DS_Store` や `._*` を除去します。isolated self-test 用に `GITHUB_WIKI_NOISE_ROOT` / `GITHUB_WIKI_NOISE_TARGET_DIRS` も受けられます。
- `scripts/check_github_wiki_boundaries.rb` は、`publish` が repo 内 `ignore/github-wiki-publish/` 固定のままで、`mktemp` や外部作業先 override が戻っていないことを検査します。
- `scripts/check_github_wiki_boundaries.rb` は、`publish` が repo 内 `ignore/github-wiki-publish/` 固定のままで、`mktemp` や外部作業先 override が戻っていないことを検査します。isolated self-test 用に `GITHUB_WIKI_BOUNDARY_ROOT` も受けられます。
- `scripts/check_github_wiki_ops_references.rb` は、運用ファイル群に親ディレクトリの `wiki` 参照や古い外部 wiki remote 参照が戻っていないことを検査します。isolated self-test 用に `GITHUB_WIKI_OPS_REFERENCE_ROOT` / `GITHUB_WIKI_OPS_REFERENCE_FILES` も受けられます。
- `scripts/with_github_wiki_lock.sh` は、GitHub Wiki の export/publish 系処理を repo 内 lock で直列化します。既定待機は 180 秒で、`GITHUB_WIKI_LOCK_WAIT_SECONDS` で変更できます。孤立した `pid` を見つけた場合は stale lock を自動回収します。
- `scripts/selftest_github_wiki_lock.sh` は、stale lock 回収、lock 直列化、timeout を repo 内 `ignore/` 配下で再現確認します。self-test 自体も repo 内 guard で直列化し、実行前に live な toolchain lock が空くまで待ちます。
- `scripts/selftest_github_wiki_sync.sh` は、isolated な sync fixture を `ignore/` 配下に作り、`sync_github_wiki_toolchain.sh` が self-test 群の前置実行、`verify -> publish` の順序、verify 失敗時の publish 停止、lock 解放を守ることを確認します。
- `scripts/selftest_github_wiki_verify.sh` は、isolated な verify fixture を `ignore/` 配下に作り、`verify_github_wiki_toolchain.sh` が self-test 群の前置実行、syntax/runtime の実行順序、build 条件分岐、失敗時停止、lock 解放を守ることを確認します。
- `scripts/selftest_github_wiki_boundaries.sh` は、現行の運用ファイル群を `ignore/` 配下に複製し、`check_github_wiki_boundaries.rb` が対象ファイル欠落、workflow guard 欠落、README 注記欠落を検出できることを確認します。
- `scripts/selftest_github_wiki_noise.sh` は、isolated な `wiki/` と `github-wiki-export/` を `ignore/` 配下に作り、`clean_github_wiki_noise.rb` が `.DS_Store` と `._*` を除去しつつ通常ファイルを残すこと、および 2 回目に no-op になることを確認します。
- `scripts/selftest_github_wiki_ops_references.sh` は、isolated な運用ファイル群を `ignore/` 配下に作り、`check_github_wiki_ops_references.rb` が親ディレクトリ経由の wiki 参照、古い remote 参照、対象ファイル欠落を検出できることを確認します。
- `scripts/selftest_github_wiki_exporter.sh` は、isolated な `wiki/` と `github-wiki-export/` を `ignore/` 配下に作り、`scripts/export_github_wiki.rb` が `Home.md`、`_Sidebar.md`、`_Footer.md`、generated assets、wrapper 除去、link rewrite、ノイズ除去を正しく出力できることを確認します。
- `scripts/selftest_github_wiki_export.sh` は、isolated な source/export を `ignore/` 配下に作り、export validator が missing page、noise file、unsafe link、sidebar 漏れ、generated asset 漏れ、`github-wiki-export/` の unstaged drift を検出できることと、`GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1` で drift 検査を明示的に外せることを確認します。
- `scripts/selftest_github_wiki_publish.sh` は、missing remote の失敗、`WIKI_PUBLISH_ALLOW_SKIP=1` の skip 成功、local bare repo を remote に見立てた publish 2 回実行を通し、repo 内作業先 cleanup と no-diff 再実行を確認します。
- `scripts/verify_github_wiki_toolchain.sh` は、syntax check、boundary check、ops reference check、noise cleanup、export、export validate をまとめて実行します。`VERIFY_GITHUB_WIKI_LOCK_SELFTEST=1` を付けると lock self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_SYNC_SELFTEST=1` を付けると sync wrapper self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_VERIFY_SELFTEST=1` を付けると verify wrapper self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1` を付けると boundary self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_NOISE_SELFTEST=1` を付けると noise cleanup self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_OPS_SELFTEST=1` を付けると ops reference self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST=1` を付けると exporter self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_EXPORT_SELFTEST=1` を付けると export validator self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_PUBLISH_SELFTEST=1` を付けると publish self-test を先頭で実行し、`VERIFY_GITHUB_WIKI_BUILD=1` を付けると `BUNDLE_PATH=vendor/bundle bundle exec jekyll build` まで含めて確認できます。
- `scripts/sync_github_wiki_toolchain.sh` は、`scripts/verify_github_wiki_toolchain.sh` の成功後に `scripts/publish_github_wiki.sh` を実行する統合 sync 入口です。
- export 検査は `scripts/check_github_wiki_export.rb` を使います。`wiki/**/*.md` の export 漏れ、`wiki/generated/` のコピー漏れ、GitHub Wiki 上で解決できない相対リンク、`_Sidebar.md` への掲載漏れ、`EEG-DATA × 助成マップ` 本文で参照している CSV 名と実ファイルの不一致、`.DS_Store` などの混入、`github-wiki-export/` の未反映更新を検出します。isolated self-test 用に `GITHUB_WIKI_EXPORT_SRC_DIR` / `GITHUB_WIKI_EXPORT_DEST_DIR` / `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1` も受けられます。
- `scripts/export_github_wiki.rb` は、`GITHUB_WIKI_EXPORT_SRC_DIR` / `GITHUB_WIKI_EXPORT_DEST_DIR` で source/export 先を差し替えられます。`SIDEBAR_GROUPS` に未分類の wiki ページがあっても、存在ページだけを既定グループへ出し、残りは `その他` セクションへ自動掲載します。
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
