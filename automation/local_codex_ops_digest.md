# Local Codex Ops Digest

このファイルは `auto-startup/scripts/run_codex_machine_ops.sh` から自動更新されます。

- generated_at_local: 2026-03-06T05:28:47+09:00
- generated_at_utc: 2026-03-05T20:28:47+00:00
- eeg_repo: [EEG-DATA](https://github.com/yasufumi-nakata/EEG-DATA)
- funds_repo: [auto-research-funds](https://github.com/yasufumi-nakata/auto-research-funds)

## mind-upload への反映方針

- このページはローカル自動運用の中継メモです。
- 公開ページへ反映する場合は `content_hub.md` の統合先に寄せます。
- GitHub Wiki を使う場合は同内容を `Codex-Machine-Ops.md` に同期します。

## EEG-DATA

- カタログ: [eeg_dataset_summary_ja.csv](https://github.com/yasufumi-nakata/EEG-DATA/blob/main/eeg_dataset_summary_ja.csv)
- 監査サマリー: [audit/global_eeg/summary.json](https://github.com/yasufumi-nakata/EEG-DATA/blob/main/audit/global_eeg/summary.json)
- 日本語サマリー行数: 19325
- merged_unique: 23670
- high_confidence: 19325
- latest_generated_at_utc: 2026-03-01 10:52 UTC
- weekly_candidate_rows: 0

### 直近候補
- 現在の `weekly_new_datasets.csv` には候補がありません。

## auto-research-funds

- 主要CSV: 未生成
- 主要CSV行数: 0
- フォーマット棚卸しCSV: 未生成
- 最新 union JSON: [data/aid_ids_union_massive_2026-03-01.json](https://github.com/yasufumi-nakata/auto-research-funds/blob/main/data/aid_ids_union_massive_2026-03-01.json)
- union aid_id 数: 3538
- 最新 Codex レポート: [data/docs/research_funding_daily_codex_2026-03-01.md](https://github.com/yasufumi-nakata/auto-research-funds/blob/main/data/docs/research_funding_daily_codex_2026-03-01.md)
- 最新 validation レポート: [data/docs/daily_run_validation_2026-03-01.md](https://github.com/yasufumi-nakata/auto-research-funds/blob/main/data/docs/daily_run_validation_2026-03-01.md)

## 運用メモ

- `EEG-DATA` は高頻度更新、`auto-research-funds` は日次更新を前提にしています。
- 本ページの更新自体は `mind-upload` の公開ページ更新と分離し、まず証跡を固定します。
