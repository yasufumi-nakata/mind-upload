# 自動化

このフォルダーには、GitHub の未解決 Issue を取得し、AI CLI に解決を依頼し、変更をコミットし、修正提案または変更概要コメントを投稿して、Issue をクローズする自動フローが含まれています。

## ファイル
- `resolve-issues.sh`: メイン自動化スクリプト
- `server.js`: スクリプトを実行するための HTTP トリガー
- `.env.example`: 構成テンプレート (`.env` にコピー)
- `logs/`: 実行時ログ (git によって無視されます)
- `EegflowResolver.app/`: オプションのアプリバンドル (git によって無視されます)
- `swarm150_site/out/worker_suggestions.jsonl`: 150 ワーカーの実行からの集約出力 (`worker*.md` ワーカーごとのファイルは冗長として廃止されました)

## セットアップ
1. `.env.example` を `.env` にコピーします。
2. オプション: `AI_CMD` を、STDIN からプロンプトを読み取るローカル AI ランナー コマンド (例: `your-ai-cli --non-interactive`) に設定します。省略した場合、`resolve-issues.sh` は `codex exec --full-auto -` を使用します。
3. AI ツールをリポジトリ ルートの外部で実行する必要がある場合は、オプションで `AI_WORKDIR` を設定します。
4. `gh` と `jq` がインストールされ、認証されていることを確認します。
5. 実行環境の値は、追跡対象ファイルではなく、ローカル `.env` (git 無視) にのみ保持します。
6. `.env` のオプションの安全設定:
   - `RUN_TIMEOUT_SECONDS` / `RUN_TIMEOUT_GRACE_SECONDS` によりハングした実行を防止します。
   - `QUEUE_ON_BUSY=true` は、実行がすでに進行中の場合、スキップする代わりに 1 つのフォローアップ実行をキューに入れます。
   - `AUTO_STASH_DIRTY=true` は、既存の変更を起動時に一度退避し、最後に復元します。
   - `SCHEDULE_MINUTE=0` は 1 時間に 1 回、0 分に実行されます (`server.js`)。

コマンドがファイルからの読み取りを優先する場合、スクリプトは `AI_PROMPT_FILE` をプロンプト ファイル パスに設定します。
デフォルトでは、追跡されたコミットされていない変更がある場合、スクリプトは停止します。このチェックをバイパスするには、`ALLOW_DIRTY=true` を設定します。既存の追跡されていないファイルは自動コミットから除外されます。

## 実行
- ドライラン:
  - `bash resolve-issues.sh --dry-run`
- 通常の実行:
  - `bash resolve-issues.sh`
- サーバーを起動:
  - `node server.js`
  - `http://localhost:3000/resolve` を呼び出す
  - サーバーも 1 時間に 1 回自動的に実行されます。
