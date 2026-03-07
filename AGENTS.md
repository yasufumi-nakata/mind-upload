# AGENTS.md — AI Agent Guide for Mind-Upload

> このファイルは Codex・Cursor・Devin 等の AI エージェントが最初に読む運用ガイドです。
> 人間向けの概要は `README.md` を参照してください。

---

## プロジェクト概要

- **リポジトリ**: `github.com/yasufumi-nakata/mind-upload`
- **公開URL**: `https://mind-upload.com`
- **目的**: マインドアップロード（WBE）を「検証可能な科学」に寄せるための公共財サイト
- **技術スタック**: Jekyll (GitHub Pages) + Markdown + HTML/CSS（フレームワーク不使用）
- **言語**: 日本語（コード・コミットメッセージは英語可）

---

## ディレクトリ構成

```
/
├── index.md                  # トップページ（ランディング）
├── _config.yml               # Jekyll 設定
├── _layouts/
│   └── default.html          # 全ページ共通レイアウト（HTML/CSS含む）
├── assets/
│   └── css/                  # スタイルシート
│
├── *.md (ルート直下)          # 公開ページ群 ── 下記「公開ページ一覧」参照
│
├── wiki/                     # GitHub Wiki ソース（学習・入門コンテンツ）
│   ├── index.md              # Wiki トップ
│   ├── generated/            # Wiki 用自動生成アセット
│   └── *.md                  # 各 Wiki ページ
│
├── .agent/
│   └── agent.md              # エージェント行動規範・思考サイクル
├── AGENTS.md                 # ← このファイル（AI 向け運用ガイド）
├── README.md                 # 人間向けプロジェクト概要
│
├── automation/               # 中間成果・作業ログ・自動生成物（非公開）
│   ├── research_deepening/   # 研究深堀りラウンドログ（114ファイル）
│   ├── rq_*.csv              # リサーチクエスチョン関連CSV
│   └── ...
│
├── scripts/                  # GitHub Wiki 運用スクリプト群
│   ├── export_github_wiki.rb
│   ├── publish_github_wiki.sh
│   ├── verify_github_wiki_toolchain.sh
│   └── selftest_*.sh
│
├── github-wiki-export/       # Wiki エクスポート先（自動生成）
├── ignore/                   # 一時ファイル（.gitignore 対象）
│
├── .github/
│   └── workflows/            # CI/CD（Wiki sync、PR validation）
│
├── Gemfile                   # Ruby 依存（github-pages）
├── CNAME                     # カスタムドメイン設定
├── requirements.txt          # Python 依存（補助スクリプト用）
└── dataset_description.json  # データセット記述メタデータ
```

---

## 公開ページ一覧（ルート直下の .md）

以下のファイルが Jekyll でビルドされ `mind-upload.com` に公開されます。

| ファイル | 役割 | URL |
|---------|------|-----|
| `index.md` | ランディングページ（読む順番・導線） | `/` |
| `verification.md` | 検証基盤（勝利条件・標準・ベンチ・登録） | `/verification.html` |
| `tech_roadmap.md` | 技術ロードマップ（問題分解・到達条件） | `/tech_roadmap.html` |
| `perspective.md` | 研究ノート（理論・技術・批判点） | `/perspective.html` |
| `idea.md` | 理論フレーム（動的プロセスとしての意識） | `/idea.html` |
| `proposals.md` | 技術提案統合（Issue対応状況） | `/proposals.html` |
| `issue.md` | 参加ガイド・Issue対応トラッカー | `/issue.html` |
| `collaborations.md` | 協業候補（研究機関・助成制度） | `/collaborations.html` |
| `research_harvest_50.md` | 未解決問題 × 文献地図 | `/research_harvest_50.html` |
| `mind_uploading_papers.md` | 論文アーカイブ | `/mind_uploading_papers.html` |
| `wbe_101.md` | WBE 入門 | `/wbe_101.html` |
| `eeg_101.md` | EEG 入門 | `/eeg_101.html` |
| `datasets.md` | データ & ベンチマーク | `/datasets.html` |
| `hands_on.md` | ハンズオン（L0 最小ループ） | `/hands_on.html` |
| `casework.md` | 歴史のケースワーク | `/casework.html` |
| `glossary.md` | 用語集 | `/glossary.html` |
| `faq.md` | FAQ | `/faq.html` |
| `content_hub.md` | 公開コンテンツ統合ハブ（運用） | `/content_hub.html` |

---

## ビルド・テスト方法

### Jekyll ローカルビルド

```bash
bundle install
bundle exec jekyll serve
# → http://localhost:4000 で確認
```

### GitHub Wiki ツールチェーン検証

```bash
bash scripts/verify_github_wiki_toolchain.sh
```

### セルフテスト一括実行

```bash
VERIFY_GITHUB_WIKI_LOCK_SELFTEST=1 \
VERIFY_GITHUB_WIKI_BOUNDARY_SELFTEST=1 \
VERIFY_GITHUB_WIKI_NOISE_SELFTEST=1 \
VERIFY_GITHUB_WIKI_OPS_SELFTEST=1 \
VERIFY_GITHUB_WIKI_EXPORTER_SELFTEST=1 \
VERIFY_GITHUB_WIKI_EXPORT_SELFTEST=1 \
bash scripts/verify_github_wiki_toolchain.sh
```

---

## AI エージェントの行動規則

### 必須ルール

1. **常に敬語**で記述すること。
2. **「提案」より「実行可能な変更」を優先**すること。
3. 詳細な行動規範は `.agent/agent.md` に従うこと。

### 握れるボール原則

- 今のセッションで自分が実行できる作業のみを主提案すること。
- 被験者実験、IRB、機材調達、法務判断、長期運用の確約は主提案にしないこと。
- 実行不能事項は `外部依存タスク` として分離し、担当者・前提条件・完了条件を明記すること。
- 曖昧な表現（「〜してはどうでしょうか」）を避け、`今回実行する変更` と `外部依存で保留` を明確に区別すること。
- 成果は必ず証跡（変更ファイル、差分、検証結果）で示すこと。

### ファイル配置ルール

| 配置先 | 置くもの |
|--------|---------|
| ルート直下（`*.md`） | 公開ページのみ。上記一覧以外のページを新規作成しないこと。 |
| `wiki/` | 学習・入門コンテンツ。GitHub Wiki ソースとして扱う。 |
| `automation/` | 中間成果・作業ログ・自動生成物・CSV。公開導線に直結させない。 |
| `scripts/` | GitHub Wiki 運用スクリプト。 |
| `ignore/` | 一時ファイル（`.gitignore` 対象）。 |

### 禁止事項

- **ルート直下に新規 `.md` ファイルを作成しないこと。** 既存ページへの統合を優先する。統合先は `content_hub.md` を参照。
- **中間成果物・作業ログをルートに置かないこと。** `automation/` を使う。
- **`layout: default` 付きの大量ファイル生成を避けること。** Jekyll ビルドが肥大化する。
- **公開ページの既存コンテンツを上書き削除しないこと。** 追記・修正は可。

### コミットルール

- ページ変更時は YAML front matter の `last_updated` を更新する。
- コミットメッセージで Issue を閉じる場合は `Fixes #N` を含める。
- ルート直下のファイル構成を変える場合は、このファイル（`AGENTS.md`）と `README.md` の該当箇所も更新する。

---

## 公開コンテンツ統合ポリシー

新しい情報を追加する前に、以下の手順を踏むこと。

1. `content_hub.md` の統合マップを確認する。
2. 既存ページの 1 節として統合できるかを検討する。
3. 統合先が見つからない場合のみ、wiki への新規ページ追加を検討する。
4. ルート直下への新規ページ追加は原則禁止。

---

## 主要リンク

| リソース | URL |
|---------|-----|
| 公開サイト | https://mind-upload.com |
| GitHub | https://github.com/yasufumi-nakata/mind-upload |
| GitHub Wiki | https://github.com/yasufumi-nakata/mind-upload/wiki |
| Issues | https://github.com/yasufumi-nakata/mind-upload/issues |

---

## 参照ファイル

- `.agent/agent.md` — エージェント行動規範・思考サイクル・判断の規律
- `content_hub.md` — 公開ページの統合先ルーティングテーブル
- `README.md` — 人間向けプロジェクト概要・システム構成
