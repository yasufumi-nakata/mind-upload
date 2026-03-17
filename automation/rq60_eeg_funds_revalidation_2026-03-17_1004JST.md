# RQ60 EEG-DATA × auto-research-funds 再検証ログ（2026-03-17 10:04 JST）

## 実行概要
- 目的: `mind-upload` の60RQについて、EEG-DATAでの可否検証と auto-research-funds 向け申請テーマ/使用データ対応を再検証し、wikiへ反映する。
- 方針: 汎用俯瞰ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を維持。
- pull後基準コミット:
  - `mind-upload=a16abed18888`
  - `EEG-DATA=02360da7bb71`
  - `auto-research-funds=abc3f6524aca`

## 再検証結果
- `RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）
- `A/B/C=17/25/18`
- `mind-upload-rq60-deep-focus-notes.md` の候補数値ID `24件` を `EEG-DATA/eeg_dataset_summary_ja.csv` に突合:
  - 一致: `1件`（`6`）
  - 不一致: `23件`（`11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）

## 運用決定
- 数値IDは再採番影響を受けるため、申請正本参照は `D1-D16 + DOI + データセット名` に固定。
- `G1-G6` 助成キー実IDは継続利用（欠落なし）。
- RQ更新は引き続き「1件ずつ深掘り」で実施する。

## 更新ファイル
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`
- `mind-upload/wiki/mind-upload-eeg-rq60-grant-dataset-playbook.md`
- `mind-upload/wiki/mind-upload-rq60-deep-focus-notes.md`
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`
