# RQ60 × EEG-DATA × Funds 再検証ログ

- 実行日時 (JST): 2026-03-14 12:03
- 実行日時 (UTC): 2026-03-14T03:03:03Z
- 対象ページ: `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`

## 検証項目

1. RQ行数とU別内訳が `60件` であること
2. ページ内 `EEG-DATA 参照データセット` の `24 ID` が `EEG-DATA/eeg_dataset_summary_ja.csv` に実在すること
3. 助成キー `G1-G6` の実IDが `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` に実在すること

## 検証結果

- RQ行数: `60`
- U別内訳: `U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`
- EEG参照ID件数: `24`
- EEG欠落ID: `0`（欠落なし）
- 助成キー実在: `GR-2026-013, GR-2026-014, 9Lx4dPK6a4k2gOb7, Drbm6vBRDJkn0NGJ, 871pw3rLjNPKgqA0, 46z9VPE4wnkrvEJR`
- 助成ID欠落: `0`（欠落なし）

## 判定

- `mind-upload` 側の「1RQ=1検証命題=1応募テーマ」運用は、今回のデータ整合チェックでも維持可能。
- `A/B/C` 判定の運用境界（EEG単独可否）に矛盾は見つからず。

