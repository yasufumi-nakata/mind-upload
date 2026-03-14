# rq60_eeg_funds_revalidation_2026-03-14_1602JST

## 実行時刻
- 2026-03-14 16:02 JST

## 実行内容
1. `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` の U別RQ行数を再計数。
2. `A/B/C` 判定数を再計数。
3. 参照している EEG-DATA 24ID の実在を `EEG-DATA/eeg_dataset_summary_ja.csv` で確認。
4. 助成ID（G1-G6 + 追加候補ID）の実在を `auto-research-funds` 内検索で確認。

## 確認結果
- RQ件数: `60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）
- 判定内訳: `A/B/C = 17/25/18`
- EEG-DATA 24ID: 欠落 `0`
- 助成ID: 全件ヒットあり
  - `GR-2026-013`, `GR-2026-014`
  - `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`
  - `1geD73ZENwB8yaor`, `lEYmRP97ng3perjO`, `1geD73Z9K2B8yaor`, `QKYgNPxZxN38bO1Z`, `46z9VPE6E0BrvEJR`, `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor`

## 判断
- 既存方針（`1RQ=1検証命題=1応募テーマ`）を維持。
- 汎用要約ではなく、RQ行単位で実験手順へ落とせる粒度を維持。
