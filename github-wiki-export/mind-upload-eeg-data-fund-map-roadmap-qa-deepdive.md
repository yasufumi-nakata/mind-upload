# Wiki：Roadmap 51QA × EEG-DATA × 助成テーマ深掘り

> P/M/R/I/V/D の各QAを問い単位で判定・助成化
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-13 / 位置づけ: Roadmap QA deep dive

## このページの役割
このページは tech_roadmap.md の 51QA を、EEG-DATAでどこまで検証できるかを問い単位で判定し、auto-research-funds 向けの申請テーマ、使うEEG-DATAスライス、初期指標、12週成果物まで固定した深掘り版wikiです。

## 正確さの前提
助成制度の応募資格・締切・様式は変動するため、実応募前に制度本文を必ず確認してください。

## 公開ページへ戻る
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [Wiki: EEG-DATA × 助成マップ](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-data-fund-map)

## いま分かっていること
- 計測基盤・評価設計・追試設計は EEG-DATA で強く進められます。
- 本人性・社会実装・強い理論主張は EEG 単独では完結しません。
- ×判定のQAでも、前段課題へ分解すれば助成テーマ化は可能です。

## まだ分かっていないこと
- データライセンスと利用条件は個別データセットで差があります。
- 制度の今年度募集有無は時期で変わるため、常に最新確認が必要です。

---

# Roadmap 51QA の問い別判定

更新日: 2026-03-13

- 対象: `tech_roadmap.md` の P/M/R/I/V/D 全51QA
- 目的: 各QAを「EEG-DATAでどこまで検証可能か」「どの助成テーマで出すか」に分解
- companion CSV: `generated/mind-upload-eeg-data-fund-map/MindUpload-EEGDATA-FundMap-roadmap-qa-deepdive.csv`

## 判定ルール

- `○`: 公開EEGで主問題の検証まで進めやすい
- `△`: 一部検証は可能だが、問いの再定義または範囲限定が必要
- `×`: EEG単独では不可。前段課題へ分解して助成化する

## 全51QAサマリー

| 判定 | 件数 |
|---|---:|
| ○ | 6 |
| △ | 26 |
| × | 19 |

## Meta (P)

### P0 「マインドアップロード」の操作的定義は？（何を再現する？）

- 判定: `△`
- 判定理由: P0 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; カタログメタデータ で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した「マインドアップロード」の操作的定義は（何を再現する）の条件比較
- 推奨支援レーン: `activity_grant`
- 候補制度タイプ: 会議開催費助成公募 / 日本万国博覧会記念基金
- 使うEEG-DATAスライス: `測定基盤; カタログメタデータ`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 主張レベル整合率; 監査可能性
- 12週成果物: `p0_scope_and_gap_note`
- 主リスク: 定義が抽象に流れる

### P1 主張レベル（クレーム階段）をどこに置く？

- 判定: `△`
- 判定理由: P1 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; カタログメタデータ で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した主張レベル（クレーム階段）をどこに置くの条件比較
- 推奨支援レーン: `activity_grant`
- 候補制度タイプ: 会議開催費助成公募 / 日本万国博覧会記念基金
- 使うEEG-DATAスライス: `測定基盤; カタログメタデータ`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 主張レベル整合率; 監査可能性
- 12週成果物: `p1_scope_and_gap_note`
- 主リスク: 定義が抽象に流れる

### P2 最低限の成果物は何？（データ・コード・評価・監査）

- 判定: `△`
- 判定理由: P2 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; カタログメタデータ で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した最低限の成果物は何（データ・コード・評価・監査）の条件比較
- 推奨支援レーン: `activity_grant`
- 候補制度タイプ: 会議開催費助成公募 / 日本万国博覧会記念基金
- 使うEEG-DATAスライス: `測定基盤; カタログメタデータ`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 主張レベル整合率; 監査可能性
- 12週成果物: `p2_scope_and_gap_note`
- 主リスク: 定義が抽象に流れる

## Measurement (M)

### M0 計測の前提：in vivo / 侵襲 / 破壊スキャンのどれを想定？

- 判定: `△`
- 判定理由: M0 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; 睡眠/意識状態 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した計測の前提：in vivo / 侵襲 / 破壊スキャンのどれを想定の条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; 睡眠/意識状態`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m0_scope_and_gap_note`
- 主リスク: 測定条件の異質性

### M1 観測変数：電気（EEG）/血流（fMRI）/スパイク（侵襲）で何が違う？

- 判定: `△`
- 判定理由: M1 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; 睡眠/意識状態 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した観測変数：電気（EEG）/血流（fMRI）/スパイク（侵襲）で何が違うの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; 睡眠/意識状態`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m1_scope_and_gap_note`
- 主リスク: 測定条件の異質性

### M2 時間解像度の下限：どの時間スケールを“保存”すべき？

- 判定: `○`
- 判定理由: M2 は既存公開EEGのタスク群で評価軸を固定しやすく、測定基盤; ERP/P300; 睡眠/意識状態 の横断比較で12週の再現成果まで到達可能。
- 助成テーマ案: 公開EEGでの時間解像度の下限：どの時間スケールを“保存”すべきの再現ベンチマーク化
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; ERP/P300; 睡眠/意識状態`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m2_benchmark_v1`
- 主リスク: 測定条件の異質性

### M3 空間解像度の下限：どの粒度（領域/カラム/ニューロン/シナプス）を目指す？

- 判定: `△`
- 判定理由: M3 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; 睡眠/意識状態 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した空間解像度の下限：どの粒度（領域/カラム/ニューロン/シナプス）を目指すの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; 睡眠/意識状態`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m3_scope_and_gap_note`
- 主リスク: 測定条件の異質性

### M4 全脳カバレッジ：どこまで“全体”を測る必要がある？

- 判定: `×`
- 判定理由: M4 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、multimodal; 測定基盤 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した全脳カバレッジ：どこまで“全体”を測る必要があるの要件定義
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `multimodal; 測定基盤`
- 代表データ例: CuBiAAD / Data of Multimodal Fusion System for Cognitive Load Assessment in Psychological Experiments / A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m4_precondition_memo`
- 主リスク: 測定条件の異質性

### M5 マルチモーダル統合：位置合わせ（MRI/EEG/fMRI）をどう保証する？

- 判定: `△`
- 判定理由: M5 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; 睡眠/意識状態 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定したマルチモーダル統合：位置合わせ（MRI/EEG/fMRI）をどう保証するの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; 睡眠/意識状態`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m5_scope_and_gap_note`
- 主リスク: 測定条件の異質性

### M6 介入・刺激：同定可能性を上げる“実験デザイン”は？

- 判定: `△`
- 判定理由: M6 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; 睡眠/意識状態 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した介入・刺激：同定可能性を上げる“実験デザイン”はの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; 睡眠/意識状態`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m6_scope_and_gap_note`
- 主リスク: 測定条件の異質性

### M7 縦断：日内/日間変動に対して“本人性特徴”は安定か？

- 判定: `△`
- 判定理由: M7 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; 睡眠/意識状態 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した縦断：日内/日間変動に対して“本人性特徴”は安定かの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; 睡眠/意識状態`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m7_scope_and_gap_note`
- 主リスク: 測定条件の異質性

### M8 品質管理：アーチファクト/欠損/ノイズをどう“定量化”して扱う？

- 判定: `○`
- 判定理由: M8 は既存公開EEGのタスク群で評価軸を固定しやすく、測定基盤 の横断比較で12週の再現成果まで到達可能。
- 助成テーマ案: 公開EEGでの品質管理：アーチファクト/欠損/ノイズをどう“定量化”して扱うの再現ベンチマーク化
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m8_benchmark_v1`
- 主リスク: 測定条件の異質性

### M9 標準化：BIDS/メタデータで“他人が追試できる”形にするには？

- 判定: `○`
- 判定理由: M9 は既存公開EEGのタスク群で評価軸を固定しやすく、測定基盤; カタログメタデータ の横断比較で12週の再現成果まで到達可能。
- 助成テーマ案: 公開EEGでの標準化：BIDS/メタデータで“他人が追試できる”形にするにはの再現ベンチマーク化
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; カタログメタデータ`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: SNR; QC通過率; 再現率
- 12週成果物: `m9_benchmark_v1`
- 主リスク: 測定条件の異質性

## Reconstruction (R)

### R0 復元対象の最小セットは？（構造/状態/学習則）

- 判定: `△`
- 判定理由: R0 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した復元対象の最小セットは（構造/状態/学習則）の条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r0_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R1 逆問題：観測（M1）から何が一意に推定できる？

- 判定: `△`
- 判定理由: R1 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した逆問題：観測（M1）から何が一意に推定できるの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r1_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R2 ソース推定：EEGから“どの表現”の脳活動が欲しい？

- 判定: `△`
- 判定理由: R2 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定したソース推定：EEGから“どの表現”の脳活動が欲しいの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r2_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R3 状態推定：潜在状態（latent）をどう定義し、どう検証する？

- 判定: `△`
- 判定理由: R3 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した状態推定：潜在状態（latent）をどう定義し、どう検証するの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r3_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R4 因果：介入に対する反応を予測できるモデルは何？

- 判定: `△`
- 判定理由: R4 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した因果：介入に対する反応を予測できるモデルは何の条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r4_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R5 可塑性：学習則を“入れる/入れない”の境界は？

- 判定: `△`
- 判定理由: R5 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した可塑性：学習則を“入れる/入れない”の境界はの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r5_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R6 個人化：一般モデル＋個人パラメータ？それとも完全に個人別？

- 判定: `△`
- 判定理由: R6 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した個人化：一般モデル＋個人パラメータそれとも完全に個人別の条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r6_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R7 同定可能性：推定は“唯一解”に近づく？不確実性は？

- 判定: `×`
- 判定理由: R7 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、resting/connectivity; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した同定可能性：推定は“唯一解”に近づく不確実性はの要件定義
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `resting/connectivity; 記憶/注意`
- 代表データ例: Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness / Single-Channel EEG Dataset for Task-Based Mental Workload Analysis / ERP Data from a Longitudinal Working Memory Task in Children With and Without Dyslexia
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r7_precondition_memo`
- 主リスク: 同定可能性不足

### R8 圧縮：どの情報を捨てても“検証基準”は保てる？

- 判定: `△`
- 判定理由: R8 は一部要件のみ公開EEGで検証できる。強い主張は避け、ERP/P300; resting/connectivity; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した圧縮：どの情報を捨てても“検証基準”は保てるの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `ERP/P300; resting/connectivity; 記憶/注意`
- 代表データ例: Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r8_scope_and_gap_note`
- 主リスク: 同定可能性不足

### R9 監査：モデル差分と失敗例を“残す仕組み”は？

- 判定: `○`
- 判定理由: R9 は既存公開EEGのタスク群で評価軸を固定しやすく、測定基盤; カタログメタデータ の横断比較で12週の再現成果まで到達可能。
- 助成テーマ案: 公開EEGでの監査：モデル差分と失敗例を“残す仕組み”はの再現ベンチマーク化
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; カタログメタデータ`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r9_benchmark_v1`
- 主リスク: 同定可能性不足

### R10 神経修飾：気分や覚醒度（Volume Transmission）をどう組み込む？

- 判定: `×`
- 判定理由: R10 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、感情; 睡眠/意識状態 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した神経修飾：気分や覚醒度（Volume Transmission）をどう組み込むの要件定義
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `感情; 睡眠/意識状態`
- 代表データ例: A Multisensory EEG Dataset for Emotion Elicitation by Audiovisual-Haptic Stimuli / EEG-Dataset-for-Psychosocial-Stress-TSST-with-Personality-Labels / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: AUROC; calibration error; 反事実差分
- 12週成果物: `r10_precondition_memo`
- 主リスク: 同定可能性不足

## Implementation (I)

### I0 実行基盤：汎用計算/GPU/HPC/ニューロモーフィックのどれを狙う？

- 判定: `×`
- 判定理由: I0 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した実行基盤：汎用計算/GPU/HPC/ニューロモーフィックのどれを狙うの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i0_precondition_memo`
- 主リスク: 実装前提が不足

### I1 閉ループ：リアルタイムに何msの遅延まで許される？

- 判定: `△`
- 判定理由: I1 は一部要件のみ公開EEGで検証できる。強い主張は避け、SSVEP; 運動意図 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した閉ループ：リアルタイムに何msの遅延まで許されるの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `SSVEP; 運動意図`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i1_scope_and_gap_note`
- 主リスク: 実装前提が不足

### I2 モデル粒度：スパイキング/レート/抽象のどこで戦う？

- 判定: `×`
- 判定理由: I2 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解したモデル粒度：スパイキング/レート/抽象のどこで戦うの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i2_precondition_memo`
- 主リスク: 実装前提が不足

### I3 計算量：メモリ/電力/並列化のボトルネックはどこ？

- 判定: `×`
- 判定理由: I3 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した計算量：メモリ/電力/並列化のボトルネックはどこの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i3_precondition_memo`
- 主リスク: 実装前提が不足

### I4 初期化：モデルの“初期状態”をどう与える？

- 判定: `×`
- 判定理由: I4 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した初期化：モデルの“初期状態”をどう与えるの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i4_precondition_memo`
- 主リスク: 実装前提が不足

### I5 学習とドリフト：学習させるなら“安全な更新”をどう設計する？

- 判定: `×`
- 判定理由: I5 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した学習とドリフト：学習させるなら“安全な更新”をどう設計するの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i5_precondition_memo`
- 主リスク: 実装前提が不足

### I6 身体性：入力/出力（センサー/運動/言語）をどこまで持たせる？

- 判定: `×`
- 判定理由: I6 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した身体性：入力/出力（センサー/運動/言語）をどこまで持たせるの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i6_precondition_memo`
- 主リスク: 実装前提が不足

### I7 再現性：実装差（言語/ハード）で結果が変わらない保証は？

- 判定: `△`
- 判定理由: I7 は一部要件のみ公開EEGで検証できる。強い主張は避け、測定基盤; 運動意図 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した再現性：実装差（言語/ハード）で結果が変わらない保証はの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; 運動意図`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i7_scope_and_gap_note`
- 主リスク: 実装前提が不足

### I8 安全：隔離・監視・停止（containment）をどう作る？

- 判定: `×`
- 判定理由: I8 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した安全：隔離・監視・停止（containment）をどう作るの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i8_precondition_memo`
- 主リスク: 実装前提が不足

### I9 熱力学：デジタル基盤で“意識の物理的コスト”を払えるか？

- 判定: `×`
- 判定理由: I9 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、SSVEP; 運動意図; 記憶/注意 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した熱力学：デジタル基盤で“意識の物理的コスト”を払えるかの要件定義
- 推奨支援レーン: `loan_or_finance`
- 候補制度タイプ: 学生プロジェクト立ち上げ助成~The First Mile~ / 融資・金融支援（橋渡し）
- 使うEEG-DATAスライス: `SSVEP; 運動意図; 記憶/注意`
- 代表データ例: An Open Steady-State Visually Evoked Potentials dataset for AR-based Brain-Computer Interfaces / Single-flicker online SSVEP BCI dataset / REH-MI / Motor Imagery Dataset Using Emotiv Insight Device
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i9_precondition_memo`
- 主リスク: 実装前提が不足

### I10 時間連続性：離散時間(RNN)と連続時間(ODE)のどちらを選ぶ？

- 判定: `△`
- 判定理由: I10 は一部要件のみ公開EEGで検証できる。強い主張は避け、睡眠/意識状態; 記憶/注意 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した時間連続性：離散時間(RNN)と連続時間(ODE)のどちらを選ぶの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; 記憶/注意`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Single-Channel EEG Dataset for Task-Based Mental Workload Analysis / ERP Data from a Longitudinal Working Memory Task in Children With and Without Dyslexia
- 最初の指標: end-to-end latency; 実装再現率
- 12週成果物: `i10_scope_and_gap_note`
- 主リスク: 実装前提が不足

## Verification (V)

### V0 検証対象：同一性・意識・行動のどれを“工学的に”検証する？

- 判定: `△`
- 判定理由: V0 は一部要件のみ公開EEGで検証できる。強い主張は避け、睡眠/意識状態; ERP/P300; 測定基盤 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した検証対象：同一性・意識・行動のどれを“工学的に”検証するの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; ERP/P300; 測定基盤`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v0_scope_and_gap_note`
- 主リスク: proxy過大解釈

### V1 評価スイート：何を測れば“前進”と言える？（事前登録）

- 判定: `○`
- 判定理由: V1 は既存公開EEGのタスク群で評価軸を固定しやすく、測定基盤; ERP/P300; 運動意図 の横断比較で12週の再現成果まで到達可能。
- 助成テーマ案: 公開EEGでの評価スイート：何を測れば“前進”と言える（事前登録）の再現ベンチマーク化
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; ERP/P300; 運動意図`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v1_benchmark_v1`
- 主リスク: proxy過大解釈

### V2 因果テスト：刺激/介入で“同じ反応”を出せるか？

- 判定: `△`
- 判定理由: V2 は一部要件のみ公開EEGで検証できる。強い主張は避け、睡眠/意識状態; ERP/P300; 測定基盤 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した因果テスト：刺激/介入で“同じ反応”を出せるかの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; ERP/P300; 測定基盤`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v2_scope_and_gap_note`
- 主リスク: proxy過大解釈

### V3 一般化：分布外（OOD）でも“本人らしさ”は保てる？

- 判定: `△`
- 判定理由: V3 は一部要件のみ公開EEGで検証できる。強い主張は避け、睡眠/意識状態; ERP/P300; 測定基盤 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した一般化：分布外（OOD）でも“本人らしさ”は保てるの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; ERP/P300; 測定基盤`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v3_scope_and_gap_note`
- 主リスク: proxy過大解釈

### V4 長期：学習・ドリフト・忘却の扱いをどう評価する？

- 判定: `△`
- 判定理由: V4 は一部要件のみ公開EEGで検証できる。強い主張は避け、睡眠/意識状態; ERP/P300; 測定基盤 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定した長期：学習・ドリフト・忘却の扱いをどう評価するの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; ERP/P300; 測定基盤`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v4_scope_and_gap_note`
- 主リスク: proxy過大解釈

### V5 本人性：心理的連続性を超えた“因果的同一性”とは？

- 判定: `×`
- 判定理由: V5 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、睡眠/意識状態; resting/connectivity を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した本人性：心理的連続性を超えた“因果的同一性”とはの要件定義
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; resting/connectivity`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v5_precondition_memo`
- 主リスク: proxy過大解釈

### V6 意識：理論に依存した予測を、どこまで“検証可能”にできる？

- 判定: `×`
- 判定理由: V6 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、睡眠/意識状態; ERP/P300 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した意識：理論に依存した予測を、どこまで“検証可能”にできるの要件定義
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; ERP/P300`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v6_precondition_memo`
- 主リスク: proxy過大解釈

### V7 コピー/分岐：複数インスタンスが走ったら“本人”はどう扱う？

- 判定: `×`
- 判定理由: V7 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、カタログメタデータ; 測定基盤 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解したコピー/分岐：複数インスタンスが走ったら“本人”はどう扱うの要件定義
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `カタログメタデータ; 測定基盤`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v7_precondition_memo`
- 主リスク: proxy過大解釈

### V8 LLM/模倣との区別：外形が似ていても“中身が違う”をどう判定する？

- 判定: `△`
- 判定理由: V8 は一部要件のみ公開EEGで検証できる。強い主張は避け、睡眠/意識状態; ERP/P300; 測定基盤 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定したLLM/模倣との区別：外形が似ていても“中身が違う”をどう判定するの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; ERP/P300; 測定基盤`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v8_scope_and_gap_note`
- 主リスク: proxy過大解釈

### V9 追試：第三者が“同じ結論”に到達できる設計になっている？

- 判定: `○`
- 判定理由: V9 は既存公開EEGのタスク群で評価軸を固定しやすく、測定基盤; カタログメタデータ の横断比較で12週の再現成果まで到達可能。
- 助成テーマ案: 公開EEGでの追試：第三者が“同じ結論”に到達できる設計になっているの再現ベンチマーク化
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `測定基盤; カタログメタデータ`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v9_benchmark_v1`
- 主リスク: proxy過大解釈

### V10 モデル距離：生体脳とエミュレーションの“近さ”をどう測る？

- 判定: `△`
- 判定理由: V10 は一部要件のみ公開EEGで検証できる。強い主張は避け、睡眠/意識状態; ERP/P300; 測定基盤 で条件差と失敗条件を先に確定する必要がある。
- 助成テーマ案: 公開EEGで検証可能な範囲に限定したモデル距離：生体脳とエミュレーションの“近さ”をどう測るの条件比較
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `睡眠/意識状態; ERP/P300; 測定基盤`
- 代表データ例: 101-nights / Physiological Indicators of Driver Sleepiness / Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials / Data from P300-based Neurofeedback Training
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v10_scope_and_gap_note`
- 主リスク: proxy過大解釈

### V11 トポロジー：意識の“構造”は保存されているか？

- 判定: `×`
- 判定理由: V11 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、resting/connectivity; 睡眠/意識状態 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解したトポロジー：意識の“構造”は保存されているかの要件定義
- 推奨支援レーン: `research_grant`
- 候補制度タイプ: 高齢社会課題解決研究（AI）への助成 / 教育研究助成事業 / リバネス研究費
- 使うEEG-DATAスライス: `resting/connectivity; 睡眠/意識状態`
- 代表データ例: Wireless 32-Channel EEG Recordings During Rest / Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness / 101-nights / Physiological Indicators of Driver Sleepiness
- 最初の指標: 事前登録遵守率; OOD gap; drift
- 12週成果物: `v11_precondition_memo`
- 主リスク: proxy過大解釈

## Deployment (D)

### D0 倫理的フレームワーク：エミュレートされた存在の権利は？

- 判定: `×`
- 判定理由: D0 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、カタログメタデータ; 測定基盤 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した倫理的フレームワーク：エミュレートされた存在の権利はの要件定義
- 推奨支援レーン: `activity_grant`
- 候補制度タイプ: 会議開催費助成公募 / 日本万国博覧会記念基金
- 使うEEG-DATAスライス: `カタログメタデータ; 測定基盤`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 統治ルール明確性; 監査可能性
- 12週成果物: `d0_precondition_memo`
- 主リスク: 制度設計が先行不足

### D1 同意と撤回：本人のインフォームドコンセントをどう設計する？

- 判定: `×`
- 判定理由: D1 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、カタログメタデータ; 測定基盤 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した同意と撤回：本人のインフォームドコンセントをどう設計するの要件定義
- 推奨支援レーン: `activity_grant`
- 候補制度タイプ: 会議開催費助成公募 / 日本万国博覧会記念基金
- 使うEEG-DATAスライス: `カタログメタデータ; 測定基盤`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 統治ルール明確性; 監査可能性
- 12週成果物: `d1_precondition_memo`
- 主リスク: 制度設計が先行不足

### D2 アクセスと公正：誰がWBEにアクセスできるべきか？

- 判定: `×`
- 判定理由: D2 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、カタログメタデータ; 測定基盤 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解したアクセスと公正：誰がWBEにアクセスできるべきかの要件定義
- 推奨支援レーン: `activity_grant`
- 候補制度タイプ: 会議開催費助成公募 / 日本万国博覧会記念基金
- 使うEEG-DATAスライス: `カタログメタデータ; 測定基盤`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 統治ルール明確性; 監査可能性
- 12週成果物: `d2_precondition_memo`
- 主リスク: 制度設計が先行不足

### D3 安全保障：悪用リスクと制御をどう設計する？

- 判定: `×`
- 判定理由: D3 はEEG単独で完結しない。制度・理論・実装要件へ依存するため、カタログメタデータ; 測定基盤 を使って前段の可観測指標だけを助成テーマ化する。
- 助成テーマ案: 公開EEGで前段課題へ分解した安全保障：悪用リスクと制御をどう設計するの要件定義
- 推奨支援レーン: `activity_grant`
- 候補制度タイプ: 会議開催費助成公募 / 日本万国博覧会記念基金
- 使うEEG-DATAスライス: `カタログメタデータ; 測定基盤`
- 代表データ例: A Comparative Dataset of Commercial Portable Brain Monitoring Devices / Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals
- 最初の指標: 統治ルール明確性; 監査可能性
- 12週成果物: `d3_precondition_memo`
- 主リスク: 制度設計が先行不足

## 使い方

- 申請書を作るときは、対象QAの `助成テーマ案` と `12週成果物` をそのまま骨子へ入れる。
- `×` 判定QAは、同じ行の `判定理由` に書いた前段課題へ分解してから応募する。
- データ選定は `使うEEG-DATAスライス` → `代表データ例` の順で絞る。
