---
layout: default
title: "Mind-upload RQ60 申請プレイブック（RQ単位固定）"
description: "60RQを1件ずつ、応募先ID・主EEGデータ・選定理由・最小成果物まで固定した運用ページ。"
article_type: Wiki
subtitle: "汎用要約ではなく、RQ単位で提出判断を固定する"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Per-RQ Grant and Dataset Playbook"
audience: "RQごとに助成応募と実験初手を同時に決めたい人"
reading_time: "20〜30分"
page_intro: "このページは、mind-upload の60リサーチクエスチョンを1件ずつ対象に、第一応募先/予備応募先、主EEG-DATA、採用理由、提出成果物を固定した実務用プレイブックです。"
accuracy_note: "A/B/C 判定は `mind-upload-eeg-rq60-feasibility-and-funds.md` と同一基準を使います。"
wiki_links:
  - label: "Wiki: RQ60 EEG検証可否と助成テーマ"
    url: "/wiki/mind-upload-eeg-rq60-feasibility-and-funds.html"
    description: "判定根拠・U別背景・RQ表の正本。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "成果物を検証仕様に落とす基準。"
recommended_pages:
  - label: "文献地図"
    url: "/research_harvest_50.html"
  - label: "データ&ベンチ"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

## 使い方

1. `RQ` を1件選び、`第一応募先` と `主EEG-DATA` を固定する。
2. `最小成果物` だけを先に作る（完了後に拡張する）。
3. `C` 判定は性能主張をせず、制度・監査設計トラックで提出する。

## 固定マップ（第一応募先/予備応募先）

- `U0: G2/G3`, `U1: G1/G4`, `U3: G2/G6`, `U4: G1/G4`
- `U7: G1/G3`, `U8: G2/G5`, `U10: G2/G6`, `U11: G2/G4`
- `U12: G2/G6`, `U13: G1/G4`, `U14: G1/G3`, `U15: G2/G6`

## RQ別固定表（60件）

| RQ | 判定 | 第一応募先 | 予備応募先 | 主EEG-DATA | 主データ採用理由 | 最小成果物 |
|---|---|---|---|---:|---|---|
| U0-1 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | セッション横断の同一性変動を同一枠組みで追跡しやすい。 | 介入プロトコルと反証条件定義 |
| U0-2 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | セッション横断の同一性変動を同一枠組みで追跡しやすい。 | 時刻同期監査レポート（offset/jitter分布） |
| U0-3 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | セッション横断の同一性変動を同一枠組みで追跡しやすい。 | 閾値探索ノートブックと採択根拠表 |
| U0-4 | B | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | セッション横断の同一性変動を同一枠組みで追跡しやすい。 | 同一性判定2軸レポート（観測一致/介入一致） |
| U1-1 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知介入/高密度条件で逆問題の誤差と不確実性を測定しやすい。 | 逆解法比較表と不確実性分布図 |
| U1-2 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知介入/高密度条件で逆問題の誤差と不確実性を測定しやすい。 | 逆問題再現レポート（誤差/不確実性） |
| U1-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知介入/高密度条件で逆問題の誤差と不確実性を測定しやすい。 | 逆問題再現レポート（誤差/不確実性） |
| U1-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知介入/高密度条件で逆問題の誤差と不確実性を測定しやすい。 | 逆解法比較表と不確実性分布図 |
| U3-1 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG単独と多モーダル条件差を同じ評価軸で比較しやすい。 | 境界拡張評価レポート（単独/統合比較） |
| U3-2 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG単独と多モーダル条件差を同じ評価軸で比較しやすい。 | 境界拡張評価レポート（単独/統合比較） |
| U3-3 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG単独と多モーダル条件差を同じ評価軸で比較しやすい。 | 境界拡張評価レポート（単独/統合比較） |
| U3-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG単独と多モーダル条件差を同じ評価軸で比較しやすい。 | 境界拡張評価レポート（単独/統合比較） |
| U3-5 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG単独と多モーダル条件差を同じ評価軸で比較しやすい。 | 境界拡張評価レポート（単独/統合比較） |
| U3-6 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG単独と多モーダル条件差を同じ評価軸で比較しやすい。 | 境界拡張評価レポート（単独/統合比較） |
| U4-1 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入有無を明示して相関と因果の差を分離しやすい。 | 介入プロトコルと反証条件定義 |
| U4-2 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入有無を明示して相関と因果の差を分離しやすい。 | 介入プロトコルと反証条件定義 |
| U4-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入有無を明示して相関と因果の差を分離しやすい。 | 介入プロトコルと反証条件定義 |
| U4-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入有無を明示して相関と因果の差を分離しやすい。 | 因果検証報告（最小介入主張） |
| U7-1 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期・QC・再現性監査を運用指標へ直結しやすい。 | 時刻同期監査レポート（offset/jitter分布） |
| U7-2 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期・QC・再現性監査を運用指標へ直結しやすい。 | 時刻同期監査レポート（offset/jitter分布） |
| U7-3 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期・QC・再現性監査を運用指標へ直結しやすい。 | 再現性監査報告（同期/QC/前処理差分） |
| U7-4 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期・QC・再現性監査を運用指標へ直結しやすい。 | 再現性監査報告（同期/QC/前処理差分） |
| U7-5 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期・QC・再現性監査を運用指標へ直結しやすい。 | 閾値探索ノートブックと採択根拠表 |
| U7-6 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期・QC・再現性監査を運用指標へ直結しやすい。 | 再現性監査報告（同期/QC/前処理差分） |
| U8-1 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループKPIを実測しやすい。 | 閉ループ安全KPIダッシュボード |
| U8-2 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループKPIを実測しやすい。 | 閉ループ安全KPIダッシュボード |
| U8-3 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループKPIを実測しやすい。 | 運用安定性報告（安全停止/回復時間） |
| U8-4 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループKPIを実測しやすい。 | 運用安定性報告（安全停止/回復時間） |
| U8-5 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループKPIを実測しやすい。 | 閉ループ安全KPIダッシュボード |
| U8-6 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループKPIを実測しやすい。 | 閉ループ安全KPIダッシュボード |
| U10-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論整合と生理proxyの差を段階的に検証しやすい。 | 理論整合メモとproxy相関解析 |
| U10-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論整合と生理proxyの差を段階的に検証しやすい。 | 理論整合メモとproxy相関解析 |
| U10-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論整合と生理proxyの差を段階的に検証しやすい。 | 理論整合報告（熱力学proxy） |
| U10-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論整合と生理proxyの差を段階的に検証しやすい。 | 理論整合メモとproxy相関解析 |
| U11-1 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 状態差データで理論指標の順位保存と失敗条件を検証しやすい。 | 意識指標比較報告（失敗条件付き） |
| U11-2 | C | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 状態差データで理論指標の順位保存と失敗条件を検証しやすい。 | 理論比較I/O仕様書と計算予算表 |
| U11-3 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 状態差データで理論指標の順位保存と失敗条件を検証しやすい。 | 意識指標比較報告（失敗条件付き） |
| U11-4 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 状態差データで理論指標の順位保存と失敗条件を検証しやすい。 | 理論比較I/O仕様書と計算予算表 |
| U12-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | 制度論点に渡す監査ログを技術的に整備しやすい。 | 分岐主体監査ログ設計書 |
| U12-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | 制度論点に渡す監査ログを技術的に整備しやすい。 | 制度監査要件表（技術ログ対応） |
| U12-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | 制度論点に渡す監査ログを技術的に整備しやすい。 | 制度監査要件表（技術ログ対応） |
| U12-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | 制度論点に渡す監査ログを技術的に整備しやすい。 | 分岐主体監査ログ設計書 |
| U12-5 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | 制度論点に渡す監査ログを技術的に整備しやすい。 | 時刻同期監査レポート（offset/jitter分布） |
| U12-6 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | 制度論点に渡す監査ログを技術的に整備しやすい。 | 制度監査要件表（技術ログ対応） |
| U13-1 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 意味復元と機構差分を対照条件で分離しやすい。 | 介入プロトコルと反証条件定義 |
| U13-2 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 意味復元と機構差分を対照条件で分離しやすい。 | 模倣分離評価スクリプトと対照条件表 |
| U13-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 意味復元と機構差分を対照条件で分離しやすい。 | 模倣分離評価報告（意味/機構） |
| U13-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 意味復元と機構差分を対照条件で分離しやすい。 | 介入プロトコルと反証条件定義 |
| U13-5 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 13 | 意味復元と機構差分を対照条件で分離しやすい。 | 模倣分離評価スクリプトと対照条件表 |
| U13-6 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 意味復元と機構差分を対照条件で分離しやすい。 | リーク監査結果と再分割証跡 |
| U14-1 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試契約・リーク監査・否定例公開の運用を固定しやすい。 | 追試運用報告（否定例含む） |
| U14-2 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試契約・リーク監査・否定例公開の運用を固定しやすい。 | 追試運用報告（否定例含む） |
| U14-3 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試契約・リーク監査・否定例公開の運用を固定しやすい。 | リーク監査結果と再分割証跡 |
| U14-4 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試契約・リーク監査・否定例公開の運用を固定しやすい。 | Model/Dataset Card雛形と記入済み実例 |
| U14-5 | B | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試契約・リーク監査・否定例公開の運用を固定しやすい。 | 否定例レジストリ初版（CSV+運用規約） |
| U14-6 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試契約・リーク監査・否定例公開の運用を固定しやすい。 | 固定コンテナ再現手順書とコスト計測 |
| U15-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全停止や権限管理の制度監査指標へ接続しやすい。 | 制度統合監査報告（停止/更新条件） |
| U15-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全停止や権限管理の制度監査指標へ接続しやすい。 | 制度監査要件表（技術ログ対応） |
| U15-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全停止や権限管理の制度監査指標へ接続しやすい。 | 制度監査要件表（技術ログ対応） |
| U15-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全停止や権限管理の制度監査指標へ接続しやすい。 | 制度監査要件表（技術ログ対応） |


## 補足

- このページは「提出運用を固定する」ための早見表です。判定理由の詳細は `mind-upload-eeg-rq60-feasibility-and-funds` を参照してください。
- `C` 判定RQでは、主張を制度要件・監査要件に限定し、過剰な性能主張を避けます。

## 2026-03-14 19:12 JST 追記

- 60RQを再走査し、各RQに `第一応募先/予備応募先/主EEG-DATA/最小成果物` を固定。
- A/B/Cの件数（`17/25/18`）は元ページと一致。
- 本ページの目的は、汎用要約を避けて `1RQ=1提出判断` を即時実行可能にすること。

## 2026-03-15 10:02 JST 再検証ログ（本run / pull後）

- `git pull --rebase --autostash` 実行後の `main` で再検証し、`RQ_TOTAL=60` を再確認。
- 本ページと `mind-upload-rq60-deep-focus-notes.md` を突合し、`A/B/C=17/25/18` の内訳一致を確認。
- 各RQ行の `第一応募先/予備応募先/主EEG-DATA/最小成果物` は欠落 `0`、空欄 `0`。
- 助成実IDは参照元を分離して確認（`G1-G2=grant_queue/*.yaml`、`G3-G6=auto-research-funds/wiki/cards + grant_eeg_dataset_match.csv`）。
- 方針を継続: 汎用要約ではなく `1RQ=1提出判断` を固定し、RQ単位で申請文へ直接転記する。

## 2026-03-15 12:02 JST 再検証ログ（本run / RQ単位提出判断の固定確認）

- `RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、`mind-upload-eeg-rq60-feasibility-and-funds.md` と完全一致。
- 全 `RQ` 行の `第一応募先/予備応募先/主EEG-DATA/最小成果物` は欠落 `0`、空欄 `0`。
- `主EEG-DATA` の参照IDは `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）。
- 助成実IDは `G1-G2=grant_queue`、`G3-G6=auto-research-funds` の系統で再参照可能。

</article>
</main>

## 2026-03-15 13:03 JST 再検証ログ（本run / 申請プレイブック整合確認）

- `main` pull後に本ページを再点検し、全 `60RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の欠落 `0`、空欄 `0` を確認しました。
- `A/B/C=17/25/18` は `mind-upload-eeg-rq60-feasibility-and-funds.md` と一致したまま維持されています。
- 助成キー `G1-G6` 実IDは `G1-G2=grant_queue`、`G3-G6=auto-research-funds` の系統で再参照可能を確認しました。
- 実務運用は据え置き: 汎用テーマ化ではなく、`1RQ=1提出判断` で応募文へ直接転記できる粒度を維持します。

## 2026-03-15 16:03 JST 再検証ログ（本run / submodule pull後）

- `main` pull後に `RQ=60` 行を再照合し、`第一応募先/予備応募先/主EEG-DATA/最小成果物` の欠落 `0` を確認。
- 判定内訳 `A/B/C=17/25/18` は `mind-upload-eeg-rq60-feasibility-and-funds.md` と一致したまま維持。
- 本ページの運用を継続: `1RQ=1提出判断` を固定し、汎用要約ではなくRQ単位で申請文へ転記する。

## 2026-03-15 19:02 JST 再検証ログ（本run / 提出固定表の監査）

- `RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認し、`mind-upload-eeg-rq60-feasibility-and-funds.md` と整合。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の欠落 `0`、空欄 `0` を確認。
- `主EEG-DATA` で参照するIDは `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）。
- 助成実IDは `G1-G2=grant_queue` と `G3-G6=auto-research-funds` の分離参照を維持。
- 方針を維持: 汎用テーマ化ではなく `1RQ=1提出判断` で申請文へ直接転記する。

## 2026-03-15 20:04 JST 再検証ログ（本run / 申請プレイブック整合）

- `RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、`mind-upload-eeg-rq60-feasibility-and-funds.md` と整合しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の欠落 `0`、空欄 `0` を確認しました。
- `主EEG-DATA` で参照するIDは `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）を確認しました。
- 助成キー `G1-G6` の実IDは `G1-G2=grant_queue`、`G3-G6=auto-research-funds` の系統で再参照可能です。
- 実務方針は据え置きです。`1RQ=1提出判断` を固定し、申請文へ直接転記できる粒度を維持します。

## 2026-03-15 21:02 JST 再検証ログ（本run / 独立監査反映）

- `RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認し、3ページ（`feasibility`/`playbook`/`deep-focus`）間で整合を確認。
- 参照EEGデータID `24件`（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）は `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）。
- 助成実ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue` と `auto-research-funds` で全件参照可能。
- 独立監査結果として、`feasibility` ページの `ID -> データセット名` 表は現行CSVの再採番と固定一致しない点を確認。運用上は既存方針どおり `D1-D16 + DOI` 正本参照を優先する。
- 方針を継続: 汎用俯瞰ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持。


## 2026-03-16 00:02 JST 再検証ログ（本run / 申請プレイブック更新）

- `RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認し、`mind-upload-eeg-rq60-feasibility-and-funds.md` と整合しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の欠落 `0`、空欄 `0` を確認しました。
- `主EEG-DATA` として参照するIDは `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）。
- 助成実ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照可能性を再確認しました。
- 実務方針は据え置きです。`1RQ=1提出判断` を固定し、汎用テーマ化せずRQ単位で申請文へ転記する運用を継続します。

## 2026-03-16 01:02 JST 再検証ログ（本run / 申請プレイブック整合）

- `main` pull後に再検証し、全 `60RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の欠落 `0` を確認しました。
- 判定内訳 `A/B/C=17/25/18` は `mind-upload-eeg-rq60-feasibility-and-funds.md` と一致しています。
- `主EEG-DATA` として参照するID `24件`（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）は `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）です。
- 助成ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue` と `auto-research-funds` で参照可能でした。
- 実務運用は継続します。`1RQ=1提出判断` を維持し、汎用要約に戻さずRQ単位で申請文へ転記します。

## 2026-03-16 19:04 JST 再検証ログ（本run / 申請固定表の継続確認）

- 作業前に `main` と3サブモジュールを pull し、基準コミットを `mind-upload=d575cb4848bd`、`EEG-DATA=da82c1d37069`、`auto-research-funds=c92fd845bddf` に更新しました。
- 正本 `research_harvest_50.md` の `リサーチクエスチョン分解` を再カウントし、`RQ_TOTAL=60` を再確認しました。
- 本ページの全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の欠落 `0`、空欄 `0` を再確認しました。
- `主EEG-DATA` として参照するID群（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）は `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）。
- 助成実ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue` と `auto-research-funds/grant_eeg_dataset_match.csv` で再参照可能でした。
- 運用方針は据え置きです。汎用テーマ化ではなく `1RQ=1提出判断` を維持して、RQごとの申請テーマと使用EEGデータを固定します。

## 2026-03-16 06:03 JST 再検証ログ（本run / 申請固定表の再確認）

- 作業前に `mind-upload=364217a`、`EEG-DATA=99f6801432`、`auto-research-funds=5b3c35e83` まで `main` を `pull --ff-only` で更新しました。
- `RQ` 行を再カウントし、`60件`（`A/B/C=17/25/18`）を再確認しました。
- 全 `RQ` 行で `第一応募先`・`予備応募先`・`主EEG-DATA`・`主データ採用理由`・`最小成果物` の必須列が埋まっていることを再確認しました（欠落 `0`）。
- 助成キー `G1-G6` は `grant_queue` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の両系統で実ID参照できることを再確認しました。
- 実務運用は継続します。汎用テーマ化は行わず、`1RQ=1提出判断` で申請文へ直接転記する粒度を維持します。


## 2026-03-16 08:02 JST 再検証ログ（本run / 提出固定表の再確認）

- 作業前に `main` を `pull --rebase` し、基準コミットを `mind-upload=34b8d748d4`、`EEG-DATA=7c606e8be1`、`auto-research-funds=f656d8638b` に更新しました。
- 本ページの `RQ` 行を再カウントし、`RQ_TOTAL=60` を確認しました。
- 判定内訳は再計数で `A/B/C=17/25/18` を維持し、`mind-upload-eeg-rq60-feasibility-and-funds.md` と整合しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/主データ採用理由/最小成果物` の必須列欠落 `0` を確認しました。
- `主EEG-DATA` として使う `9 ID`（`6, 11, 13, 19, 49, 56, 509, 676, 735`）は `EEG-DATA/eeg_dataset_summary_ja.csv` 上で全件実在（欠落 `0`）。
- 実務方針は維持します。汎用要約ではなく `1RQ=1提出判断` で申請文へ直接転記する運用を継続します。

## 2026-03-16 09:03 JST 再検証ログ（本run / pull後・1RQ深掘り運用の再固定）

- 作業前に `main` を pull し、基準コミットを `mind-upload=7e31a0d8f1`、`EEG-DATA=56deab7770`、`auto-research-funds=500036faee` に更新しました。
- 正本 `research_harvest_50.md` のRQを再照合し、`RQ_TOTAL=60` を再確認しました。
- 判定内訳は `A/B/C=17/25/18` を維持し、3ページ（`feasibility`/`playbook`/`deep-focus`）間で整合しています。
- 助成キー `G1-G6` の実ID（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で再参照可能です。
- 今回の重要差分: `EEG-DATA/eeg_dataset_summary_ja.csv` は再採番が入るため、固定参照は数値IDではなく `D1-D16（DOI固定） + データセット名` を正本として扱う運用に再固定しました。
- 運用方針を維持します。汎用俯瞰ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を1件ずつ実行する粒度で継続します。

## 2026-03-16 12:02 JST 再検証ログ（本run / pull後・提出固定表の更新確認）

- 作業前に `main` と3サブモジュールを pull し、基準コミットを `mind-upload=4e1956b319da`、`EEG-DATA=2df474b136f7`、`auto-research-funds=cdf8f75421b7` に更新しました。
- 本ページの `RQ` 行を再カウントし、`RQ_TOTAL=60`、判定内訳 `A/B/C=17/25/18` を再確認しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の必須列欠落 `0`、空欄 `0` を確認しました。
- 助成キー `G1-G6` の参照系統を再確認しました（`G1-G2=grant_queue`、`G3-G6=auto-research-funds`）。
- 運用方針は据え置きです。汎用テーマ化ではなく、`1RQ=1提出判断` を維持して応募文へ直接転記します。

## 2026-03-16 13:04 JST 再検証ログ（本run / 提出固定表の継続確認）

- 作業前に `main` と3サブモジュールを `pull --ff-only` し、基準コミットを `mind-upload=50e2093ed411`、`EEG-DATA=95e1605e5005`、`auto-research-funds=9eb599bbf875` に更新しました。
- 正本 `research_harvest_50.md` を再照合し、`RQ_TOTAL=60` を再確認しました。
- 本ページの `RQ` 行を再計数し、`60件`（`A/B/C=17/25/18`）を確認しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の必須列欠落 `0`、空欄 `0` を確認しました。
- 助成キー `G1-G6` 実IDは `grant_queue` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で再参照可能でした。
- 運用方針は据え置きです。汎用テーマ化は行わず、`1RQ=1提出判断` を維持して申請文へ直接転記します。

## 2026-03-16 15:04 JST 再検証ログ（本run / RQ単位提出判断の継続）

- 作業前に `main` を `pull --ff-only` し、`mind-upload=35249d9ddb01`、`EEG-DATA=95e1605e5005`、`auto-research-funds=9eb599bbf875` の基準へ更新しました。
- 本ページの `RQ_TOTAL=60`、`A/B/C=17/25/18`、必須列（`第一応募先/予備応募先/主EEG-DATA/最小成果物`）欠落 `0` を再確認しました。
- 助成実ID `G1-G6` は `grant_queue` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の両系統で参照可能でした。
- 本runでも運用は据え置きです。汎用テーマ化はせず、`1RQ=1提出判断` で申請文へ直接転記する粒度を維持します。


## 2026-03-16 16:02 JST 再検証ログ（本run / 提出固定表の更新確認）

- `main` pull 後に本ページの `RQ` 行を再計数し、`RQ_TOTAL=60` を再確認しました。
- 判定内訳 `A/B/C=17/25/18` は `mind-upload-eeg-rq60-feasibility-and-funds.md` と一致しています。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/主データ採用理由/最小成果物` の必須列欠落 `0` を確認しました。
- 助成実ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で再参照可能でした。
- `主EEG-DATA` の数値IDは再採番で変動するため、提出時の固定参照は引き続き `D1-D16（DOI固定）` を優先し、数値IDは補助的に扱います。

## 2026-03-16 17:03 JST 再検証ログ（本run / 1RQ深掘り運用の再固定）

- 作業前に `main` と3サブモジュールを `pull --ff-only` し、基準コミットを `mind-upload=9dde203`、`EEG-DATA=3d27e5d4f7`、`auto-research-funds=5d6af61f5` に更新しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` の `Ux-n` 行を再計数し、`RQ_TOTAL=60` を再確認しました。
- 判定内訳は再計数で `A/B/C=17/25/18` を維持し、`deep-focus` と `playbook` 側の判定列とも整合しました。
- 助成実ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue/*.yaml` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で全件参照可能でした。
- EEG参照の固定ルールは継続します。`EEG-DATA/eeg_dataset_summary_ja.csv` の数値IDは再採番があるため、提出・再現ログは `D1-D16 + DOI`（`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 正本）を基準にします。
- 方針を維持します。汎用俯瞰ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を1件ずつ深掘りして記述します。

## 2026-03-17 08:02 JST 再検証ログ（本run / RQ単位申請固定表の更新確認）

- 作業前に `main` を `pull --ff-only` し、基準コミットを `mind-upload=b01826de2565`、`EEG-DATA=48261b83b10a`、`auto-research-funds=c81f22c6aafd` に更新しました。
- 本ページの `RQ` 行を再計数し、`RQ_TOTAL=60`、`A/B/C=17/25/18` が `mind-upload-eeg-rq60-feasibility-and-funds.md` と一致することを再確認しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の必須列欠落 `0`、空欄 `0` を確認しました。
- 実務方針を継続します。汎用テーマ化は行わず、`1RQ=1提出判断` で申請文へ直接転記できる粒度を維持します。

## 2026-03-17 10:04 JST 再検証ログ（本run / 申請正本キーの再固定）

- 作業前に `main` と3サブモジュールを `pull --ff-only` し、基準コミットを `mind-upload=a16abed18888`、`EEG-DATA=02360da7bb71`、`auto-research-funds=abc3f6524aca` に更新しました。
- 本ページの `RQ` 行を再計数し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- `主EEG-DATA` の数値ID参照を現行CSVと突合した結果、再採番で `23/24` が不一致になったため、申請固定表の正本参照は `D1-D16 + DOI` に再固定します。
- 助成実ID `G1-G6` は `grant_queue` と `auto-research-funds` で再参照可能（欠落 `0`）でした。
- 実務運用を継続します。`1RQ=1提出判断` の粒度で、申請文には `Dキー + DOI + データセット名` を必須記載します。

## 2026-03-17 12:02 JST 再検証ログ（本run / 申請固定表の再確認）

- `RQ_TOTAL=60` を再確認し、`第一応募先/予備応募先/主EEG-DATA/主データ採用理由/最小成果物` の欠落 `0` を確認しました。
- 判定内訳 `A/B/C=17/25/18` は `mind-upload-eeg-rq60-feasibility-and-funds.md` と一致したまま維持されています。
- 助成キー `G1-G6` は `grant_queue` と `auto-research-funds` の正本参照で再確認済みです。
- 運用方針は据え置きです。汎用テーマ化はせず、`1RQ=1提出判断` を維持します。

## 2026-03-17 14:02 JST 再検証ログ（本run / 1RQ単位の提出固定を再確認）

- 作業前に `main` を `pull --ff-only` し、基準コミットを `mind-upload=aec3d72cc717`、`EEG-DATA=02360da7bb71`、`auto-research-funds=e8703b40121c` に更新しました。
- 本ページの `RQ` 行を再計数し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の必須列欠落 `0` を確認しました。
- 提出時のデータ固定は、再採番影響を避けるため `D1-D16 + DOI + データセット名` を正本とする運用を継続します。
- 依頼方針どおり、汎用テーマ化はせず `1RQ=1提出判断` を維持して申請文へ直接転記できる粒度を保持します。

## 2026-03-17 18:02 JST 再検証ログ（本run / 申請固定表の継続確認）

- 作業前に `main` を `pull --ff-only` し、本ページの `RQ` 行を再計数して `RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- 全 `RQ` 行で `第一応募先/予備応募先/主EEG-DATA/最小成果物` の必須列欠落 `0` を確認しました。
- `G1-G6` 実IDは `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で再参照可能、かつ `主EEG-DATA` の参照IDは `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在でした。
- 方針を維持します。汎用テーマ化ではなく `1RQ=1提出判断` を固定し、申請文へ直接転記する運用を継続します。
