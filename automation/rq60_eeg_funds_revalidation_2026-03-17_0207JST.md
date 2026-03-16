# rq60_eeg_funds_revalidation_2026-03-17_0207JST

## 実行時刻
- 2026-03-17 02:07 JST

## 実行内容
1. `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` のRQ行を再計数。
2. `A/B/C` 判定数を再計数。
3. 参照EEG ID（24件）を `EEG-DATA/eeg_dataset_summary_ja.csv` で実在確認。
4. 助成ID（G1-G6 + 追加候補）を `grant_queue/*.yaml` と `auto-research-funds/wiki/cards/*.md` で実在確認。

## 確認結果
- RQ件数: `60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）
- 判定内訳: `A/B/C = 17/25/18`
- EEG ID 24件: 欠落 `0`
- 助成ID: 欠落 `0`
  - `GR-2026-013`, `GR-2026-014`
  - `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`
  - `1geD73ZENwB8yaor`, `lEYmRP97ng3perjO`, `1geD73Z9K2B8yaor`, `QKYgNPxZxN38bO1Z`, `46z9VPE6E0BrvEJR`, `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor`

## 判断
- 既存方針を維持: `1RQ=1検証命題=1応募テーマ=1主データ`。
- 数値EEG IDは再採番影響があるため、正本キーは `D1-D16 + DOI` を継続利用。
