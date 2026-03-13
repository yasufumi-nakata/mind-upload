---
layout: default
title: "Wiki：EEG-DATA × 助成マップ"
description: "mind-upload の研究トピックを EEG-DATA と auto-research-funds でどう検証し、どの制度タイプへ申請テーマ化するかをまとめた実務向け wiki です。"
article_type: Wiki
subtitle: "25トピック × EEG公開データ × 助成制度の実務対応表"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Research-to-funding map"
audience: "mind-upload の論点を EEG 公開データと助成申請へ落としたい人"
reading_time: "30〜90分"
page_intro: "このページは、mind-upload の 25 トピックを EEG-DATA と auto-research-funds の観点で再配置し、どこまで EEG 公開データで検証できるか、どの制度タイプにどんな書き方で出すかをまとめた長文 wiki です。"
accuracy_note: "助成制度の応募資格、締切、提出様式は更新されるため、実応募前には制度本文を必ず再確認してください。"
page_highlights:
  - "25トピックごとに EEG-DATA での可否、使うべきスライス、助成テーマ案を整理します。"
  - "制度タイプごとの題目、要旨、面談、再申請テンプレまで含めます。"
  - "companion CSV は generated/mind-upload-eeg-data-fund-map/ に集約しています。"
known_points:
  - "EEG 公開データで強く進めやすいのは測定基盤、デコーディング、睡眠/意識状態です。"
  - "本人性や WBE の最終主張は EEG 単独では解けず、前段の検証課題へ分解する必要があります。"
  - "研究助成、奨励金、活動助成では書き方と成果物の見せ方が変わります。"
unknown_points:
  - "制度ごとの締切、資格、提出様式は固定ではありません。"
  - "EEG-DATA の即時利用可能件数やテンプレ適用範囲は今後の更新で変わり得ます。"
wiki_links:
  - label: "Wiki: ロードマップの読み方"
    url: "/wiki/roadmap-reading-guide.html"
    description: "25トピックの依存関係を先に掴みたい人向けです。"
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "EEG の観測限界を先に押さえたい人向けです。"
  - label: "Wiki: マルチモーダル統合の基本"
    url: "/wiki/multimodal-integration-basics.html"
    description: "EEG 単独で足りない部分の補い方を整理します。"
recommended_pages:
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "協業候補"
    url: "/collaborations.html"
---

# mind-upload × EEG-DATA × auto-research-funds 対応表

更新日: 2026-03-06

> Companion CSV は `generated/mind-upload-eeg-data-fund-map/` に集約しています。  
> すべて `MindUpload-EEGDATA-FundMap-*.csv` の接頭辞で揃えています。
>
> `tech_roadmap.md` の 51QA を問い単位で深掘りした版は  
> [`/wiki/mind-upload-eeg-data-fund-map-roadmap-qa-deepdive.html`](/wiki/mind-upload-eeg-data-fund-map-roadmap-qa-deepdive.html) を参照してください。  
> `research_harvest_50.md` の 60RQ を問い単位で深掘りした版は  
> [`/wiki/mind-upload-eeg-data-fund-map-rq60-deepdive.html`](/wiki/mind-upload-eeg-data-fund-map-rq60-deepdive.html) を参照してください。

## 0. 結論

- `EEG-DATA` だけで強く進めやすいのは、`mind-upload` のうち **測定基盤**, **神経デコーディング**, **感情/睡眠/注意系**, **意識状態分類** です。
- **部分的に進められる**のは、高密度EEGの空間限界, マルチモーダル統合, 記憶, 言語/意味, 意思決定, 社会的認知, NCC, GWT, IIT proxy です。
- **EEG-DATA 単独では解けない**のは、本人性そのもの, コピー/分岐, 倫理/権利, 安全保障, WBEの理論的最終主張です。ここは「EEGで測れる前段の検証課題」に落として助成テーマ化するのが現実的です。

## 1. 参照したローカル資産

- `mind-upload`
  - `config/mind_upload_roadmap.yaml`: 4フェーズ 25トピック
  - `mind-upload/tech_roadmap.md`: 51個の広義QA
  - `mind-upload/verification.md`, `mind-upload/proposals.md`: 検証要求の方向性
- `EEG-DATA`
  - `EEG-DATA/eeg_dataset_summary_ja.csv`: 11,309件
  - アクセス内訳: `すぐに使える` 8,102件 / `公開だが要確認` 2,490件 / `要アカウント/利用登録` 717件
  - 既存即時実行テンプレート観点では、2026-02-24スナップショットで 1,559件が即時テンプレート適用可能
- `auto-research-funds`
  - `auto-research-funds/grant_eeg_dataset_match.csv`: 2,702制度ぶんのテーマ語マッチ結果

## 2. 先に固定しておく注意点

- ここでいう「解ける」は、`EEG-DATA` の公開データから **研究として検証可能なサブ問題に落とせる** ことを意味します。
- `EEG-DATA` はデータカタログであって、全テーマに完成済み解析パイプラインがあるわけではありません。
- `EEG-DATA` で `すぐに使える` が 8,102件あっても、**現行テンプレートで即時に実験へ入れる件数** は別です。既存レポート基準では 1,559件が「即時テンプレート適用可能」でした。
- `auto-research-funds` は現チェックアウトでは `data/keio_funding_single.csv` が無く、締切や応募可否の最終確認まではこの場ではできません。
- `grant_eeg_dataset_match.csv` は **テーマ語の相性マッチ** なので、「出し先の候補例」として使い、実応募前に制度本文の再確認が必要です。
- `grant_eeg_dataset_match.csv` 2,702件のうち `high` 判定は 252件で、上位に broad grant が偏りやすいです。
- `grant_eeg_dataset_match.csv` では `grant_key_categories` が空の制度もあり、カテゴリ付与が弱い制度は過小評価されている可能性があります。
- 下の件数は `EEG-DATA/eeg_dataset_summary_ja.csv` へのキーワード照合ベースの **proxy count** です。厳密ラベル件数ではありません。

## 3. EEG-DATA の使いどころ

| EEG-DATAスライス | 即時利用proxy件数 | 使い道 | 代表例 |
|---|---:|---|---|
| 測定基盤 | 1,180 | 品質管理, ノイズ, 長時間安定性, multimodal | `Comparative Dataset of Commercial Portable Brain Monitoring Devices`, `CuBiAAD`, `Single-channel wearable EEG ... drowsiness` |
| 運動意図 | 446 | motor imagery, リハビリ, BCI汎化 | `Motor Imagery Dataset Using Emotiv Insight Device`, `REH-MI` |
| ERP/P300 | 589 | 感覚誘発, 認知負荷, GWT proxy | `ERP Data from a Longitudinal Working Memory Task...` |
| SSVEP | 96 | 視覚知覚, 高速BCI, リアルタイム系 | `Open SSVEP dataset for AR-based BCI`, `EdgeSSVEP_Dataset` |
| 睡眠/意識状態 | 708 | 覚醒-睡眠境界, drowsiness, dream, NCC proxy | `101-nights`, `Physiological Indicators of Driver Sleepiness` |
| resting/connectivity | 192 / 302 | 安静時再現性, ネットワーク指標, source/connectivity | `Wireless 32-Channel EEG Recordings During Rest...` |
| 感情 | 359 | emotion/stress/anxiety の cross-subject 評価 | `A Multisensory EEG Dataset for Emotion Elicitation...` |
| 記憶/注意 | 245 / 318 | working memory, attention, workload | `CuBiAAD`, `ERP Data from a Longitudinal Working Memory Task...` |
| 言語/意味 | 415 | imagined speech, semantic congruency, auditory attention | `A Multi-Class Electroencephalography Dataset for Imagined Speech Decoding`, `3M-CPSEED` |
| multimodal | 736 | EEG-fNIRS, EEG-eye tracking, portable neurotech | `CuBiAAD`, `Data of Multimodal Fusion System for Cognitive Load Assessment...` |

## 4. Phase 1-4 トピック別の判定

判定:

- `○`: EEG-DATA で主問題のかなりの部分を直接検証できる
- `△`: 一部は検証できるが、解析拡張か問いの再定義が必要
- `×`: EEG-DATA 単独では無理。前段テーマへ落として助成化する

| Phase | `mind-upload` トピック | 判定 | 助成に出すならこの題目 | 使う EEG-DATA スライス | 向く助成レーン |
|---|---|---|---|---|---|
| 1 | EEG信号品質の限界検証 | ○ | 公開EEG横断での信号品質・アーチファクト耐性の再現性評価 | 測定基盤 | 研究助成 |
| 1 | 高密度EEG空間分解能評価 | △ | HD-EEGソース推定の空間限界と再現性評価 | 測定基盤, resting/connectivity | 研究助成 |
| 1 | マルチモーダル統合の基礎 | △ | EEG-fNIRS/eye-tracking 同期統合の標準化 | multimodal, 測定基盤 | 研究助成, 活動助成 |
| 1 | ノイズ除去・信号分離手法の比較 | ○ | ASR/ICA/ZapLine 系前処理の横断比較ベンチマーク | 測定基盤 | 研究助成 |
| 1 | 長時間記録の安定性評価 | ○ | 長時間EEGにおける drift・疲労・睡眠遷移の安定性評価 | 睡眠/意識状態, 測定基盤 | 研究助成 |
| 2 | デコーディング精度ベンチマーク | ○ | 公開EEGベンチマークでの decoding 精度基盤構築 | 運動意図, ERP/P300, SSVEP | 研究助成, 奨励金 |
| 2 | クロスデータセット汎化 | △ | 公開EEG横断での cross-dataset generalization 限界測定 | 運動意図, ERP/P300, SSVEP, 感情 | 研究助成 |
| 2 | リアルタイムデコーディング | △ | リアルタイムEEG decoding の replay ベース遅延評価 | SSVEP, 運動意図, 記憶/注意 | 研究助成, 起業支援 |
| 2 | Foundation Modelの適用 | △ | 公開EEG自己教師あり表現学習の基盤化 | 運動意図, 睡眠/意識状態, 感情, resting/connectivity | 研究助成 |
| 2 | 運動意図デコーディング | ○ | cross-subject motor imagery decoding の汎化限界 | 運動意図 | 研究助成, 奨励金 |
| 2 | 感覚知覚デコーディング | ○ | ERP/P300/SSVEP による感覚知覚 decoding の再現性評価 | ERP/P300, SSVEP, 記憶/注意 | 研究助成, 奨励金 |
| 2 | 言語/意味デコーディング | △ | imagined speech / semantic EEG decoding の成立条件 | 言語/意味, 記憶/注意 | 研究助成 |
| 3 | 感情状態の推定・分類 | ○ | emotion/stress EEG の被験者間頑健性評価 | 感情 | 研究助成, 奨励金 |
| 3 | 記憶のエンコーディング/検索 | △ | working memory / retrieval EEG 指標の再現性検証 | 記憶/注意, ERP/P300 | 研究助成 |
| 3 | 注意・ワーキングメモリ | △ | attention/workload EEG の汎化評価とWM課題拡張 | 記憶/注意, ERP/P300 | 研究助成, 奨励金 |
| 3 | 意思決定過程 | △ | リスク選択・報酬予測のEEG指標化 | 記憶/注意, 感情 | 研究助成 |
| 3 | 社会的認知 | △ | social stress / joint attention / hyperscanning EEG の基礎評価 | 感情, multimodal | 研究助成, 活動助成 |
| 3 | 創造性・問題解決 | △ | 問題解決過程のEEG proxy 指標探索 | 記憶/注意, 感情 | 奨励金, 研究助成 |
| 3 | 主観的経験の定量化 | △ | pain/subjective rating と EEG 指標の対応づけ | 感情, 睡眠/意識状態 | 研究助成 |
| 4 | 意識の神経相関（NCC）定量化 | △ | 覚醒-睡眠-夢-麻酔境界のEEG指標化 | 睡眠/意識状態, resting/connectivity | 研究助成 |
| 4 | 意識状態の分類（覚醒/睡眠/麻酔/DoC） | ○ | consciousness boundary classification の公開EEGベンチマーク | 睡眠/意識状態 | 研究助成 |
| 4 | 統合情報理論(IIT)の実証的検証 | △ | IIT proxy と複雑性指標のEEG上での再計算 | 睡眠/意識状態, resting/connectivity | 研究助成 |
| 4 | Global Workspace Theory の検証 | △ | P300/ignition/broadcast proxy のEEG検証 | ERP/P300, 記憶/注意, 睡眠/意識状態 | 研究助成 |
| 4 | 意識の連続性と同一性 | × | 縦断EEGによる個人内安定性と状態連続性の指標化 | 睡眠/意識状態, resting/connectivity | 研究助成 |
| 4 | mind-upload可能性の理論的枠組み | × | EEGベース検証可能性のクレーム階段設計と benchmark commons | 全スライス + カタログメタデータ | 活動助成, 起業支援 |

## 5. いま優先して出すべきテーマ

| 優先 | テーマ | いま出しやすい理由 | まず使うデータ | 向く助成レーン |
|---:|---|---|---|---|
| 1 | 信号品質・前処理再現性 | Phase 1の土台で、L0主張が安全 | P1: Signal QC Benchmark | 研究助成 |
| 2 | motor imagery cross-dataset 汎化 | データが厚く、学生テーマにも落ちる | P4: MI Generalization | 研究助成, 奨励金 |
| 3 | 睡眠/眠気/覚醒境界分類 | Phase 4の中で最も現実的 | P10: Consciousness Boundary | 研究助成 |
| 4 | emotion/stress robustness | Phase 3 で件数が多く、応用にも寄せやすい | P7: Emotion / Stress Robustness | 研究助成, 奨励金 |
| 5 | ERP/P300/SSVEP benchmark | 知覚 decoding と GWT proxy の中間に置ける | P5: ERP/P300/SSVEP Perception | 研究助成, 奨励金 |
| 6 | attention/workload multimodal | multimodal と高次認知の接点で助成文脈が広い | P3 + P8 | 研究助成, 活動助成 |
| 7 | 長時間EEG安定性評価 | Phase 1と identity proxy の橋渡しになる | P1 + P10 | 研究助成 |
| 8 | imagined speech / semantic EEG | 野心性がありつつ EEG で実験可能 | P6: Imagined Speech / Semantics | 研究助成 |
| 9 | HD-EEG source localization | 工学色が強く、理論主張を抑えやすい | P2: HD-EEG Source Limit | 研究助成 |
| 10 | NCC/IIT/GWT proxy の再評価 | 強い主張を避ければ Phase 4 の入口になる | P10: Consciousness Boundary | 研究助成 |

## 6. どこまで本当に言えるか

### 6.1 今すぐ強く言える

- EEGの **計測品質**, **前処理**, **cross-subject/cross-dataset decoding**, **睡眠/覚醒/疲労の状態分類** はこのレポジトリ資産だけでかなり前進できる
- `mind-upload` の Phase 1-2 は、`EEG-DATA` を使うと「検証課題」に落としやすい
- Phase 3 も、感情・注意・一部記憶は十分に走れる

### 6.2 言い過ぎになる

- EEGだけで「本人性」や「意識の連続性」そのものを証明する
- EEGだけで IIT / GWT の決着をつける
- EEGデコーディングの成功を、そのまま `mind-upload` 実現可能性の強い証拠として語る

## 7. `tech_roadmap.md` の広義QAを EEG-DATA 単独で見るとどうなるか

| QA群 | QA ID | EEG-DATA 単独判定 | コメント |
|---|---|---|---|
| Meta | P0-P2 | △ | P2 の再現資産設計には使えるが、P0/P1 の定義自体はデータだけでは決まらない |
| Measurement 基礎 | M0-M2 | △-○ | EEGで何が見えるか, 時間分解能, 非侵襲路線の限界はかなり検証できる |
| Measurement 空間/全脳 | M3-M5 | △ | 高密度EEGやmultimodalの一部までは可能だが、全脳完全性や厳密位置合わせは不足 |
| Measurement 実験設計/縦断/QC | M6-M9 | △-○ | 縦断安定性, QC, BIDS化はかなり進められる。介入は弱い |
| Reconstruction 状態推定 | R1-R3, R6, R8-R9 | △ | source/state/individualization は進むが、唯一解や完全復元には届かない |
| Reconstruction 因果/可塑性/神経修飾 | R4-R5, R7, R10 | △ | proxy は作れるが、介入・因果・生理機序の決着には不足 |
| Implementation | I0-I10 | × | 実装基盤, 電力, containment, body, initial state は EEG-DATA 単独では決められない |
| Verification | V1, V3, V4, V9, V10 | △-○ | benchmark, OOD, 長期ドリフト, 追試設計は進められる |
| Verification 強い同一性/意識 | V0, V2, V5-V8, V11 | ×-△ | 因果介入や本人性の強い主張には不足。state-boundary proxy まで |
| Deployment | D0-D3 | × | 倫理, 公正, 権利, 安全保障は別系統の検討が必要 |

## 8. auto-research-funds ではどのレーンに出すべきか

### 8.1 研究助成

向くテーマ:

- 公開EEG横断ベンチマーク
- 高密度EEG/前処理/品質管理
- 睡眠・覚醒・疲労・長時間安定性
- 感情/注意/記憶/言語の神経デコーディング

候補例:

- `高齢社会課題解決研究（AI）への助成` / 公益財団法人 長寿科学振興財団
- `リバネス研究費` / 株式会社 リバネス
- `学術・研究助成（2025年度）` / 公益財団法人 住友電工グループ社会貢献基金
- `研究助成金` / 一般財団法人 日本産業科学研究所
- `教育研究資金・研究補助金` / 公益財団法人 軽金属奨学会

### 8.2 奨励金・奨学金

向くテーマ:

- 1タスクに絞った学生スケール研究
- motor imagery / emotion / workload / imagined speech の単課題研究
- ベンチマーク再現や cross-subject 検証

候補例:

- `学生チャレンジ奨学金` / 公益財団法人 東京コミュニティー財団
- `奨学金給付事業` / 公益財団法人 ＺＥＮ　ＣＬＵＢ
- `奨学金` / 一般財団法人 鷹野学術振興財団
- `奨学金事業` / 公益財団法人 エイブル文化振興財団

### 8.3 活動助成・会議助成

向くテーマ:

- EEG benchmark commons の公開
- EEG-BIDS 変換会, 再現性ワークショップ, データ統合会議
- 社会的認知や multimodal の共同研究ネットワーク形成

候補例:

- `会議開催費助成公募` / 公益財団法人 中辻創智社
- `コンベンション開催支援補助金` / 一般社団法人 つくば観光コンベンション協会
- `助成事業` / 公益財団法人 北九州観光コンベンション協会
- `日本万国博覧会記念基金` / 公益財団法人 関西・大阪21世紀協会

### 8.4 起業支援・事業化寄り

向くテーマ:

- portable EEG の品質監査ツール
- drowsiness / workload / neuro-wellbeing の実装研究
- real-time decoding を使う neurotech プロトタイプ

候補例:

- `リバネス研究費` / 株式会社 リバネス
- `奨学金助成、研究開発助成、スポーツ活動助成` / 公益財団法人 Ｇ－７奨学財団
- `ニュービジネス助成金　イノベーション研究開発助成金` / 株式会社 池田泉州銀行
- `日本ソーシャル・スタートアップAWARD` / 公益財団法人 日本フィランソロピック財団

### 8.5 代表プログラム10件の使い分け

| プログラム | 種別 | 向くテーマ群 | どういう出し方が安全か |
|---|---|---|---|
| 高齢社会課題解決研究（AI）への助成 / 公益財団法人 長寿科学振興財団 | research_grant | 測定基盤, 高次認知, 意識 | 高齢者の眠気, 痛み, 注意状態, 睡眠境界を EEG で定量化する AI 研究 |
| 教育研究助成事業 / 公益財団法人 ZEN CLUB | research_grant | 測定基盤, decoding, 高次認知, 意識 | EEG基盤整備, cross-dataset benchmark, 睡眠/感情/注意の横断研究 |
| 教育研究資金・研究補助金 / 公益財団法人 軽金属奨学会 | research_grant | 測定基盤, decoding | 可搬EEG, 信号品質, motor imagery, P300 の工学寄り研究 |
| リバネス研究費 / 株式会社 リバネス | research_grant | 測定基盤, decoding, 高次認知, 意識 | ベンチマーク基盤, neurotech プロトタイプ, 基礎から事業化橋渡し |
| 奨学金助成、研究開発助成、スポーツ活動助成 / 公益財団法人 G-7奨学財団 | research_grant | 測定基盤, decoding, 高次認知 | 研究開発と応用の両方に寄せやすい。睡眠, 運動意図, 神経工学実装の橋渡し向け |
| 未解の知〜The ANRI Fellowship〜 基礎科学研究奨学金 / ANRI 株式会社 | research_grant | decoding, 意識 | foundation model, 意識状態推定, 基礎科学寄りの野心枠 |
| 学生チャレンジ奨学金 / 公益財団法人 東京コミュニティー財団 | award_or_prize | decoding, 高次認知 | 学生主導の MI/P300/感情認識ベンチマークや再現性研究 |
| 奨学金 / 一般財団法人 鷹野学術振興財団 | award_or_prize | 測定基盤, decoding | 小規模立ち上げ向け。可搬EEG, 信号品質, 運動意図 decoding |
| ゆめバンクとくしま助成事業 / 特定非営利活動法人 とくしま県民活動プラザ | activity_grant | 高次認知, 意識 | 睡眠, ストレス, 感情, 注意の可視化を地域・教育・福祉文脈で出す |
| 学生プロジェクト立ち上げ助成 The First Mile / ANRI 株式会社 | activity_grant | decoding, 高次認知 | 眠気検知, 集中度推定, neurofeedback など MVP 立ち上げ |

補欠:

- `会議開催費助成公募` / 公益財団法人 中辻創智社: 研究費本体よりも、成果後の workshop や benchmark meeting 向け
- `国際会議発表渡航助成` 系: 論文化・採択後の発表費に回すのが自然

## 9. 申請題目ひな形

- 公開EEG横断ベンチマークによる運動意図デコーディングの汎化限界評価
- 高密度EEGと公開多施設データを用いた脳波ソース推定の再現性検証
- 睡眠・覚醒・眠気境界におけるEEG状態分類と個人差の定量化
- EEG-fNIRS・眼球運動統合による注意状態推定の標準化基盤構築
- 感情・ストレス状態の cross-subject EEG decoding における頑健性評価
- imagined speech EEG の公開データ横断検証と意味デコーディング条件の整理
- 公開EEGを用いた複雑性指標の再評価による意識状態 proxy の検証
- EEGデータカタログを用いた mind-upload 研究のクレーム階段と検証可能性マップの構築

## 10. そのまま走れる初手研究パッケージ

| パッケージ | 主にカバーする `mind-upload` トピック | まず使うデータセット | 最初にやる解析 | 向く助成レーン |
|---|---|---|---|---|
| P1: Signal QC Benchmark | EEG信号品質, ノイズ除去, 長時間安定性 | `A Comparative Dataset of Commercial Portable Brain Monitoring Devices`, `Single-channel wearable EEG ... drowsiness`, `Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals` | SNR/QC 指標, artifact耐性, 前処理前後の保存率比較 | 研究助成 |
| P2: HD-EEG Source Limit | 高密度EEG空間分解能評価 | `Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods`, `Localize-MI` | source localization 誤差, electrode数依存の劣化曲線 | 研究助成 |
| P3: Multimodal Sync Core | マルチモーダル統合の基礎 | `CuBiAAD`, `Data of Multimodal Fusion System for Cognitive Load Assessment`, `Simultaneous EEG-fMRI ... 50 healthy participants` | modality alignment, 同期誤差, feature fusion 有無の比較 | 研究助成, 活動助成 |
| P4: MI Generalization | デコーディング精度, クロスデータセット汎化, 運動意図 | `Motor Imagery Dataset Using Emotiv Insight Device`, `REH-MI`, `Upper Limb Rehabilitation Motor Imagery EEG Signals`, `Indonesian Motor Imagery Dataset` | cross-subject, cross-session, cross-dataset split | 研究助成, 奨励金 |
| P5: ERP/P300/SSVEP Perception | 感覚知覚, GWT proxy, リアルタイム系 | `16 channel Three speaker dynamic switch cEEGrid Auditory Attention Decoding Dataset`, `An Open Steady-State Visually Evoked Potentials dataset for AR-based BCI`, `Predicting Navigational Decisions Through Visually Evoked P300 ...` | ERP latency, P300再現性, SSVEP周波数識別, online replay | 研究助成, 奨励金 |
| P6: Imagined Speech / Semantics | 言語/意味デコーディング | `A Multi-Class Electroencephalography Dataset for Imagined Speech Decoding`, `MSEEG`, `3M-CPSEED`, `N400 eggplants sentence set` | imagined speech 分類, semantic congruency ERP, subject transfer | 研究助成 |
| P7: Emotion / Stress Robustness | 感情状態, 主観的経験の一部 | `A Multisensory EEG Dataset for Emotion Elicitation`, `EEG-Dataset-for-Psychosocial-Stress-TSST-with-Personality-Labels`, `Frontal Alpha and Parietal Theta Asymmetries ...` | valence/arousal, stress分類, session差頑健性 | 研究助成, 奨励金 |
| P8: Memory / Attention / Workload | 記憶, 注意, ワーキングメモリ | `ERP Data from a Longitudinal Working Memory Task in Children With and Without Dyslexia`, `Neural reinstatement of features in audiovisual working memory ...`, `Single-Channel EEG Dataset for Task-Based Mental Workload Analysis`, `CuBiAAD` | WM負荷, attention/workload, longitudinal drift | 研究助成 |
| P9: Decision / Social Cognition | 意思決定, 社会的認知, 創造性の一部 | `The Neuroscience of Moral Choice`, `Decision-making in dynamic, continuously evolving environments`, `Inter-brain ERPs alignment during a joint Simon task`, `EEG-Dataset-for-Psychosocial-Stress-TSST-with-Personality-Labels` | reward/risk, social interaction, hyperscanning, stress反応 | 研究助成, 活動助成 |
| P10: Consciousness Boundary | NCC, 意識状態分類, IIT/GWT proxy, 同一性proxy | `101-nights`, `Physiological Indicators of Driver Sleepiness`, `Transient Topographical Dynamics ... During Drowsiness`, `EEG recordings in rats anesthetized with isoflurane ...`, `CSTE: A Dataset for Cross-Sessions and Cross-Tasks EEG Biometrics` | awake-sleep-drowsy-anesthesia 境界分類, complexity proxy, cross-session stability | 研究助成 |

## 11. EEG-DATA だけでは足りないときに何を足すか

| 解きたい問い | EEG-DATA だけで足りない理由 | 追加で必要なもの |
|---|---|---|
| 高密度EEGの厳密な空間限界 | EEGだけだと ground truth が弱い | 刺激部位既知データ, MRI, source model |
| マルチモーダル統合の厳密検証 | EEGカタログだけでは位置合わせ誤差が詰まらない | EEG-fMRI, EEG-fNIRS, eye tracking の同時計測 |
| 因果・IIT・GWT の決着 | 観測だけでなく摂動が必要 | TMS-EEG, 薬理/麻酔, PCI 系データ |
| 意識の連続性・同一性 | EEGのみでは心理的・行動的連続性が不足 | 縦断行動, 自伝的記憶課題, 主観報告, 長期追跡 |
| 倫理・権利・安全保障 | データからは規範が出ない | 倫理設計, 法制度, ガバナンス文書 |

## 12. 何を主張してよいか

| 研究パッケージ / テーマ帯 | 主張してよいレベル | 主張してはいけないこと |
|---|---|---|
| 測定基盤, QC, 標準化 | L0 | 「脳の本質を捉えた」とまでは言わない |
| MI, ERP/P300, SSVEP, emotion, workload の decoding | L1 | decode 成功を本人性や意識継続の証拠にしない |
| cross-dataset benchmark, foundation model の表現学習 | L1-L2弱 | 汎化性能を WBE 実現可能性へ直結させない |
| sleep/drowsiness/anesthesia の状態分類 | L1 | 意識理論の決着と書かない |
| NCC/IIT/GWT proxy | L1-L2弱 | IIT/GWT を証明した, 意識を完全に測ったとは書かない |
| identity / continuity proxy | L0-L1 | 「同一人物性を証明した」とは言わない |
| benchmark commons / claim ladder 設計 | L0 | 技術実証そのものと混同しない |

## 13. 最初に報告すべき指標

| テーマ帯 | 最低限報告したい指標 |
|---|---|
| 信号品質 / QC | SNR, bad channel率, artifact除去前後の保存率, sessionごとの欠損率 |
| source localization / HD-EEG | localization error, electrode数依存の劣化曲線, 再構成の安定性 |
| multimodal | modality同期誤差, fusion有無での性能差, modality欠損時の劣化 |
| motor imagery | balanced accuracy, macro-F1, LOSO精度, cross-dataset gap |
| ERP/P300 | amplitude, latency, single-trial AUC, subject-transfer gap |
| SSVEP | frequency classification accuracy, ITR, online replay latency |
| emotion / stress | macro-F1, subject/session transfer gap, calibration error |
| memory / workload / attention | AUROCまたはmacro-F1, workloadレベル別混同行列, longitudinal drift |
| sleep / consciousness boundary | stage or state accuracy, Cohen's kappa, transition entropy, wake-sleep-drowsy confusion |
| identity / continuity proxy | cross-session identification accuracy, within-person / between-person distance, session drift |

## 14. テーマ選びの実務ルール

- `○` のテーマは、そのまま研究計画にしてよい
- `△` のテーマは、必ず **1段弱い問い** に落とす
- `×` のテーマは、「理論主張」ではなく **EEGで測れる前段指標** に変換して出す

変換例:

- `意識の連続性と同一性` → `縦断EEGで個人内安定性はどこまで保たれるか`
- `mind-upload可能性の理論的枠組み` → `EEGベース研究が L0-L2 のどこまで前進できるかを測る共通評価系`
- `IITの実証` → `睡眠/覚醒境界で複雑性 proxy はどう変化するか`

## 15. すぐ使う代表データセット

| 用途 | データセット | URL |
|---|---|---|
| 可搬EEG品質比較 | `A Comparative Dataset of Commercial Portable Brain Monitoring Devices for Research-Oriented Acquisition (2025)` | https://ieee-dataport.org/documents/comparative-dataset-commercial-portable-brain-monitoring-devices-research-oriented |
| multimodal attention | `CuBiAAD: A cue-masked bimodal auditory attention dataset based on EEG and fNIRS` | https://doi.org/10.21227/18vd-6870 |
| cognitive load + eye tracking | `Data of Multimodal Fusion System for Cognitive Load Assessment in Psychological Experiments` | https://doi.org/10.21227/6106-6120 |
| wearable sleepiness | `Single-channel wearable EEG using low-power Qvar sensor and machine learning for drowsiness detection` | https://doi.org/10.21227/5qzc-gm79 |
| motor imagery | `Motor Imagery Dataset Using Emotiv Insight Device` | https://ieee-dataport.org/documents/motor-imagery-dataset-using-emotiv-insight-device |
| rehabilitation MI | `REH-MI: EEG Motor Imagery Dataset from the Same Limb for Rehabilitation Applications` | https://doi.org/10.21227/xgzb-6s98 |
| auditory attention decoding | `16 channel Three speaker dynamic switch cEEGrid Auditory Attention Decoding Dataset Nanjing University` | https://ieee-dataport.org/documents/16-channel-three-speaker-dynamic-switch-ceegrid-auditory-attention-decoding-dataset |
| SSVEP | `An Open Steady-State Visually Evoked Potentials dataset for Augmented Reality-based Brain-Computer Interfaces` | https://ieee-dataport.org/documents/open-steady-state-visually-evoked-potentials-dataset-augmented-reality-based-brain |
| imagined speech | `A Multi-Class Electroencephalography Dataset for Imagined Speech Decoding` | https://doi.org/10.21227/2ybw-rt36 |
| sleep/dream | `101-nights` | https://doi.org/10.5281/zenodo.5338770 |

## 16. 付録A: Phase 1-2 トピック別の初手候補

### EEG信号品質の限界検証

- 候補データセット: `A Comparative Dataset of Commercial Portable Brain Monitoring Devices for Research-Oriented Acquisition (2025)`, `Single-channel wearable EEG using low-power Qvar sensor and machine learning for drowsiness detection`, `Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `教育研究資金・研究補助金`
- 位置づけ: 最も安全な L0 テーマ

### 高密度EEG空間分解能評価

- 候補データセット: `Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods`, `Localize-MI`, `Ultra high-density EEG recording of interictal migraine and controls: sensory and rest`
- 出し先候補: `学術・研究助成（2025年度）`, `教育研究助成事業`
- 位置づけ: source localization の工学テーマとして出しやすい

### マルチモーダル統合の基礎

- 候補データセット: `CuBiAAD`, `Data of Multimodal Fusion System for Cognitive Load Assessment in Psychological Experiments`, `Simultaneous EEG-fMRI, structural and diffusion-weighted MRI from 50 healthy participants`
- 出し先候補: `教育研究助成事業`, `会議開催費助成公募`, `日本万国博覧会記念基金`
- 位置づけ: research grant と活動助成の両方に振れる

### ノイズ除去・信号分離手法の比較

- 候補データセット: `Synthetic EEG Dataset for CNN Training: Clean and Artifact-Contaminated Signals`, `Wearable Ambulatory Electrocardiogram (ECG) and EEG dataset`, `A Comparative Dataset of Commercial Portable Brain Monitoring Devices for Research-Oriented Acquisition (2025)`
- 出し先候補: `教育研究資金・研究補助金`, `リバネス研究費`
- 位置づけ: 前処理ベンチマークとして書きやすい

### 長時間記録の安定性評価

- 候補データセット: `101-nights`, `Aalborg University Wearable Sleep Study (AAUWSS)`, `ERP Data from a Longitudinal Working Memory Task in Children With and Without Dyslexia`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `教育研究助成事業`
- 位置づけ: sleep / longitudinal / wearable の橋渡し

### デコーディング精度ベンチマーク

- 候補データセット: `Motor Imagery Dataset Using Emotiv Insight Device`, `An Open Steady-State Visually Evoked Potentials dataset for Augmented Reality-based Brain-Computer Interfaces`, `16 channel Three speaker dynamic switch cEEGrid Auditory Attention Decoding Dataset Nanjing University`
- 出し先候補: `学生チャレンジ奨学金`, `リバネス研究費`
- 位置づけ: 学生テーマにも論文化にも乗せやすい

### クロスデータセット汎化

- 候補データセット: `REH-MI`, `Motor Imagery Dataset Using Emotiv Insight Device`, `Upper Limb Rehabilitation Motor Imagery EEG Signals`
- 出し先候補: `教育研究助成事業`, `奨学金助成、研究開発助成、スポーツ活動助成`
- 位置づけ: Phase 2 の中心テーマ

### リアルタイムデコーディング

- 候補データセット: `Single-flicker online SSVEP BCI dataset`, `Synthetic and real EEG datasets for closed-loop neuroscience`, `16 channel Three speaker dynamic switch cEEGrid Auditory Attention Decoding Dataset Nanjing University`
- 出し先候補: `学生プロジェクト立ち上げ助成 The First Mile`, `リバネス研究費`
- 位置づけ: replay 評価から始めるのが安全

### Foundation Modelの適用

- 候補データセット: `TF-C Pretrain SleepEEG`, `Motor Imagery Dataset Using Emotiv Insight Device`, `A Multi-Class Electroencephalography Dataset for Imagined Speech Decoding`
- 出し先候補: `未解の知 The ANRI Fellowship 基礎科学研究奨学金`, `リバネス研究費`
- 位置づけ: 野心的だが、自己教師あり表現学習に落とせば書きやすい

### 運動意図デコーディング

- 候補データセット: `REH-MI`, `Motor Imagery Dataset Using Emotiv Insight Device`, `Indonesian Motor Imagery Dataset`
- 出し先候補: `学生チャレンジ奨学金`, `奨学金`
- 位置づけ: 修士の主題にしやすい

### 感覚知覚デコーディング

- 候補データセット: `An Open Steady-State Visually Evoked Potentials dataset for Augmented Reality-based Brain-Computer Interfaces`, `Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials`, `16 channel Three speaker dynamic switch cEEGrid Auditory Attention Decoding Dataset Nanjing University`
- 出し先候補: `教育研究助成事業`, `学生チャレンジ奨学金`
- 位置づけ: ERP/P300/SSVEP をまとめて扱える

### 言語/意味デコーディング

- 候補データセット: `A Multi-Class Electroencephalography Dataset for Imagined Speech Decoding`, `MSEEG`, `3M-CPSEED`, `N400 event-related potential sentence set`
- 出し先候補: `未解の知 The ANRI Fellowship 基礎科学研究奨学金`, `教育研究助成事業`
- 位置づけ: Phase 2 の中では難しめだが、テーマ映えする

## 17. 付録B: Phase 3-4 トピック別の初手候補

### 感情状態の推定・分類

- 候補データセット: `A Multisensory EEG Dataset for Emotion Elicitation by Audiovisual-Haptic Stimuli`, `Frontal Alpha and Parietal Theta Asymmetries Associated with Color-Induced Emotions`, `EEG-Dataset-for-Psychosocial-Stress-TSST-with-Personality-Labels`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `学生チャレンジ奨学金`
- 位置づけ: Phase 3 の主力

### 記憶のエンコーディング/検索

- 候補データセット: `ERP Data from a Longitudinal Working Memory Task in Children With and Without Dyslexia`, `Neural reinstatement of features in audiovisual working memory indicates object-based retrieval`, `Processing in working memory boosts long-term memory representations and their retrieval`
- 出し先候補: `教育研究助成事業`, `奨学金`
- 位置づけ: memory retrieval まで欲張らず、まず WM から入る

### 注意・ワーキングメモリ

- 候補データセット: `Single-Channel EEG Dataset for Task-Based Mental Workload Analysis`, `CuBiAAD`, `Multimethod data on mental workload in pilots`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `学生チャレンジ奨学金`
- 位置づけ: workload / vigilance は実務テーマ化しやすい

### 意思決定過程

- 候補データセット: `The Neuroscience of Moral Choice`, `Decision-making in dynamic, continuously evolving environments`, `Subjective value-weights on benefit and risk in human neurocomputation`
- 出し先候補: `教育研究助成事業`, `リバネス研究費`
- 位置づけ: reward / risk に限定すると書きやすい

### 社会的認知

- 候補データセット: `Inter-brain ERPs alignment during a joint Simon task: an EEG hyperscanning study`, `EEG-Dataset-for-Psychosocial-Stress-TSST-with-Personality-Labels`, `Endogenous oscillatory rhythms and interactive contingencies jointly influence infant attention during early infant-caregiver interaction`
- 出し先候補: `ゆめバンクとくしま助成事業`, `日本万国博覧会記念基金`
- 位置づけ: 活動助成や共同研究形成とも相性が良い

### 創造性・問題解決

- 候補データセット: `Playing 20 Questions with the mind: collaborative problem solving by humans using a brain-to-brain interface`, `Temporal Priming and Creative Insight EEGPrimer_218`, `Temporal Priming and Creative Insight EEGPrimer_216`
- 出し先候補: `学生チャレンジ奨学金`, `リバネス研究費`
- 位置づけ: exploratory 扱いで出すのが安全

### 主観的経験の定量化

- 候補データセット: `PhysioPain Dataset`, `Multimodal Pain Dataset`, `EEG correlates of detection and identification awareness for digits and letters`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `教育研究助成事業`
- 位置づけ: subjective report と EEG の対応づけに絞る

### 意識の神経相関（NCC）定量化

- 候補データセット: `101-nights`, `EEG and fMRI signals during REM Sleep`, `Physiological Indicators of Driver Sleepiness`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `リバネス研究費`
- 位置づけ: awake-sleep-dream 境界の proxy で始める

### 意識状態の分類（覚醒/睡眠/麻酔/DoC）

- 候補データセット: `101-nights`, `Transient Topographical Dynamics of the Electroencephalogram Predict Brain Connectivity and Behavioural Responsiveness During Drowsiness`, `EEG recordings in rats anesthetized with isoflurane and after awakening from anesthesia`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `教育研究助成事業`
- 位置づけ: Phase 4 で最初に取るべきテーマ

### 統合情報理論(IIT)の実証的検証

- 候補データセット: `Visual and Auditory Oddball Tasks During Waking and Hypnotic States: An EEG Dataset`, `101-nights`, `Transient Topographical Dynamics ... During Drowsiness`
- 出し先候補: `未解の知 The ANRI Fellowship 基礎科学研究奨学金`, `教育研究助成事業`
- 位置づけ: proxy 指標の再計算に留める

### Global Workspace Theory の検証

- 候補データセット: `Data from P300-based Neurofeedback Training for Attention Enhancement with 4 EEG Electrodes`, `Adaptive P300-Based Brain-Computer Interface for Attention Training`, `Predicting Navigational Decisions Through Visually Evoked P300 Event-Related Potentials`
- 出し先候補: `教育研究助成事業`, `学生チャレンジ奨学金`
- 位置づけ: P300 / ignition proxy に限定する

### 意識の連続性と同一性

- 候補データセット: `CSTE: A Dataset for Cross-Sessions and Cross-Tasks EEG Biometrics`, `ERP Data from a Longitudinal Working Memory Task in Children With and Without Dyslexia`, `Frequency-tagging EEG reveals spontaneous categorical discrimination of visual self-identity`
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `奨学金`
- 位置づけ: 同一性そのものではなく、cross-session stability と self-related EEG まで

### mind-upload可能性の理論的枠組み

- 候補データセット: `A Comparative Dataset of Commercial Portable Brain Monitoring Devices for Research-Oriented Acquisition (2025)`, `CuBiAAD`, `101-nights`
- 出し先候補: `会議開催費助成公募`, `日本万国博覧会記念基金`, `リバネス研究費`
- 位置づけ: 技術実証ではなく benchmark commons / claim ladder 設計として出す

## 18. 研究カード雛形

### Card-01: Signal QC Benchmark

- 問い: 公開EEG横断で前処理の頑健性はどこまで保てるか
- データ: `A Comparative Dataset of Commercial Portable Brain Monitoring Devices`, `Single-channel wearable EEG ... drowsiness`
- 指標: SNR, channel dropout, artifact除去前後の情報保持率
- 主張レベル: L0
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `教育研究資金・研究補助金`

### Card-02: MI Generalization

- 問い: motor imagery decoding は cross-subject / cross-dataset でどこまで保つか
- データ: `REH-MI`, `Motor Imagery Dataset Using Emotiv Insight Device`, `Indonesian Motor Imagery Dataset`
- 指標: accuracy, macro-F1, subject holdout, dataset holdout
- 主張レベル: L1
- 出し先候補: `学生チャレンジ奨学金`, `奨学金`, `リバネス研究費`

### Card-03: ERP/P300/SSVEP Perception

- 問い: ERP/P300/SSVEP は知覚分類と attention proxy をどこまで再現できるか
- データ: `An Open Steady-State Visually Evoked Potentials dataset for AR-based BCI`, `Predicting Navigational Decisions Through Visually Evoked P300 ...`
- 指標: latency, amplitude, frequency classification, online replay accuracy
- 主張レベル: L1
- 出し先候補: `教育研究助成事業`, `学生チャレンジ奨学金`

### Card-04: Emotion / Stress Robustness

- 問い: emotion/stress EEG は session差と subject差に耐えるか
- データ: `A Multisensory EEG Dataset for Emotion Elicitation`, `EEG-Dataset-for-Psychosocial-Stress-TSST-with-Personality-Labels`
- 指標: valence/arousal classification, stress detection, session transfer
- 主張レベル: L1
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `学生チャレンジ奨学金`

### Card-05: Multimodal Attention Core

- 問い: EEG単独より multimodal 融合で attention/workload 推定は安定するか
- データ: `CuBiAAD`, `Data of Multimodal Fusion System for Cognitive Load Assessment`
- 指標: unimodal vs multimodal 差分, alignment error, workload estimation
- 主張レベル: L1-L2弱
- 出し先候補: `教育研究助成事業`, `会議開催費助成公募`, `日本万国博覧会記念基金`

### Card-06: Consciousness Boundary

- 問い: awake-sleep-drowsy-anesthesia 境界は EEG でどこまで安定に分類できるか
- データ: `101-nights`, `Transient Topographical Dynamics ... During Drowsiness`, `EEG recordings in rats anesthetized with isoflurane ...`
- 指標: state classification, transition stability, complexity proxy
- 主張レベル: L1
- 出し先候補: `高齢社会課題解決研究（AI）への助成`, `未解の知 The ANRI Fellowship 基礎科学研究奨学金`

## 19. いま着手する順番

1. Phase 1 の `EEG信号品質`, `ノイズ除去`, `長時間安定性` を先に固める  
2. Phase 2 の `運動意図`, `ERP/P300`, `SSVEP` で cross-dataset benchmark を作る  
3. Phase 3 は `感情` と `注意/workload` を先行し、`記憶` と `言語` はその後  
4. Phase 4 は `意識状態分類` を先にやり、`NCC/IIT/GWT` は proxy 主張に限定する  
5. 助成申請では、強い `mind-upload` 主張を避けて、**公開EEGで検証可能なサブ問題** として書く

## 20. このページの読み方

- 研究テーマを立てるときは `4. Phase 1-4 トピック別の判定` を見る
- 助成金に合わせて題目を調整するときは `8. auto-research-funds ではどのレーンに出すべきか` を見る
- 「その問いは EEG-DATA 単独では無理では?」を確認するときは `7. tech_roadmap.md の広義QA` を見る
- 25トピックを1枚で扱いたいときは `MindUpload-EEGDATA-FundMap-matrix.csv` を使う
- そのままカードに起こすときは `18. 研究カード雛形` を使う

## 21. `grant_eeg_dataset_match.csv` の読み解き方

- 現チェックアウトで制度候補を最も安定して引けるのは `auto-research-funds/grant_eeg_dataset_match.csv` です
- このCSVは `program_name`, `provider`, `support_type_primary`, `research_field`, `grant_key_categories`, `rec1-3_dataset_name` を持つ、**制度とEEG候補データの粗い接続表** です
- 現在の 2,702 行の内訳は `research_grant` 1,026件, `activity_grant` 845件, `award_or_prize` 414件, `loan_or_finance` 206件, `not_stated` 131件, `other` 80件です
- したがって、研究テーマとして最初に使うべき主戦場は `research_grant`、共同体形成や標準化は `activity_grant`、学生個人の初手は `award_or_prize` と読むのが実務的です
- `grant_key_categories` は `engineering_ai`, `medical`, `education`, `social_humanities` などの粗い付与です。複数カテゴリを跨ぐテーマほど、採択余地のある制度が増えます
- `research_field` は表記ゆれが大きいので、厳密な自動絞り込みよりも、`工学`, `医学`, `保健・医療`, `教育・スポーツ`, `起業支援` の語が含まれる制度から人手で拾い直す前提で使う方が安全です

### 21.1 制度タイプ別の出し分け

| 制度タイプ | 何を出すか | 向く `mind-upload` 側テーマ | EEG-DATA の使い方 |
|---|---|---|---|
| `research_grant` | ベンチマーク, 汎化評価, 前処理比較, state classification | Phase 1 全般, Phase 2 主力, Phase 3 の感情/注意, Phase 4 の state分類 | 複数公開データを束ねて性能差と再現性を示す |
| `activity_grant` | benchmark commons, 研究会, 共同ワークショップ, データ標準化活動 | マルチモーダル統合, 社会的認知, theoretical framework | カタログ横断整理と実験計画共有基盤として使う |
| `award_or_prize` | 学生単独テーマ, exploratory study, 小規模PoC | MI, ERP/P300, emotion, workload | データ1-3本で短期間に結果を作る |
| `loan_or_finance` | wearable EEG, neurotech product, BCI UI 実装 | real-time decoding, portable measurement, assistive application | `single-channel`, `portable`, `wearable`, `online` 系を優先する |
| `not_stated` / `other` | 補欠候補 | broad topic | 制度本文の確認が前提 |

### 21.2 カテゴリ別の安全な題目の寄せ方

| カテゴリ寄せ | 題目の寄せ方 | 避けるべき言い方 |
|---|---|---|
| `engineering_ai` | 再現性評価, 汎化性能, 前処理, 自己教師あり表現学習 | mind-upload実現, 人格復元 |
| `medical` | 睡眠, 疲労, 覚醒境界, pain/stress 指標, 認知負荷 | 意識の本質解明, 同一性証明 |
| `education` | workload, attention, neurofeedback, student project | 哲学的主張を前面に出すこと |
| `social_humanities` | 主観評価との対応, 倫理的含意の整理, benchmark commons | EEGだけで倫理問題を解決できるという書き方 |

## 22. 90日で形にする申請パッケージ

| パッケージ | 最初の2週間 | 3-6週 | 7-10週 | 11-12週 | 12週時点の納品物 |
|---|---|---|---|---|---|
| Signal QC | データ3本固定, 前処理条件固定 | artifact/QC 指標算出 | 比較表作成 | 申請文へ圧縮 | QC benchmark 1本 |
| MI Generalization | データ3本固定, split確定 | LOSO / cross-session 評価 | cross-dataset 評価 | 図表化 | subject/dataset gap レポート |
| ERP/P300/SSVEP | ERP系2本 + SSVEP1本確定 | feature抽出 | タスク差比較 | 題目整理 | perception benchmark |
| Emotion / Stress | valence/arousal と stress を分離 | subject holdout 評価 | session transfer 評価 | 応用文脈化 | robustness note |
| Multimodal Attention | multimodal 2本固定 | unimodal vs fusion 比較 | alignment 誤差分析 | 活動助成用に言い換え | fusion評価ノート |
| Consciousness Boundary | sleep/drowsy/anesthesia 3本固定 | state分類器作成 | transition/complexity proxy | 強い主張を削る | boundary classification note |

### 22.1 申請書の骨子テンプレート

1. 背景: `mind-upload` の最終主張ではなく、公開EEGで検証可能なサブ問題として位置づける  
2. ギャップ: 現状はデータセット単位の報告が多く、cross-dataset の比較軸が不足していると書く  
3. 方法: `EEG-DATA` から 2-5データセットを束ね、split, metric, preprocessing を固定して比較する  
4. 成果: benchmark, reproducible pipeline, negative result を含む再現可能な知見に置く  
5. 波及: 医療, 教育, BCI, human-in-the-loop AI など制度カテゴリに応じて言い換える  

## 23. 審査で落ちにくい書き方と落ちやすい書き方

### 23.1 落ちにくい書き方

- `公開EEGデータ横断での再現性評価`
- `cross-dataset generalization の限界測定`
- `覚醒-眠気-睡眠境界の分類性能比較`
- `subjective report と EEG 指標の対応づけ`
- `multimodal fusion の標準化と性能差評価`

### 23.2 落ちやすい書き方

- `mind-upload の実現可能性を検証する`
- `EEGから人格や自己を復元する`
- `EEGだけで意識理論の真偽を決着させる`
- `公開データだけで人間の同一性を証明する`

### 23.3 安全な言い換え

| 強すぎる表現 | 安全な言い換え |
|---|---|
| `意識を解明する` | `意識状態に関連するEEG proxy を比較する` |
| `本人性を判定する` | `cross-session EEG biometrics の安定性を測る` |
| `mind-upload を検証する` | `mind-upload 議論に必要な計測・汎化・状態推定の前段課題を検証する` |
| `理論を実証する` | `理論が要請する proxy 指標を比較する` |

## 24. companion CSV の使い方

- `MindUpload-EEGDATA-FundMap-matrix.csv` は 25トピックを1行ずつ持つ実務向け一覧です
- `MindUpload-EEGDATA-FundMap-proposals.csv` は 題目案・要旨の芯・想定審査カテゴリを1行で引くための申請向け一覧です
- `MindUpload-EEGDATA-FundMap-review.csv` は 想定審査コメント・弱点・返答軸を1行で引くための審査対応向け一覧です
- `MindUpload-EEGDATA-FundMap-rebuttal.csv` は 長文の審査コメントと返答例を1行で引くための詳細版です
- `MindUpload-EEGDATA-FundMap-rewrite.csv` は 通りにくい書き方と通しやすい書き換えを1行で引くための題目調整向け一覧です
- `MindUpload-EEGDATA-FundMap-abstracts.csv` は 約200字・約400字・約800字の要旨テンプレを1行で引くための要旨作成向け一覧です
- `MindUpload-EEGDATA-FundMap-pitch-seeds.csv` は 人手寄りの題目書き換え案と約200字 seed を1行で引くための初稿向け一覧です
- `MindUpload-EEGDATA-FundMap-fund-writing.csv` は 制度タイプ別の1段落応募文と審査員向け一言を1行で引くための応募文向け一覧です
- `MindUpload-EEGDATA-FundMap-budget.csv` は テーマ群別の費目テンプレと予算説明の強弱を1行で引くための予算設計向け一覧です
- `MindUpload-EEGDATA-FundMap-support-playbook.csv` は 制度タイプ別の応募文3パターン・成果物一覧・口頭回答テンプレを1行で引くための実戦向け一覧です
- `MindUpload-EEGDATA-FundMap-dual-tone.csv` は 制度タイプ別の「審査書類向けの硬い版」と「面談向けの柔らかい版」を1行で引くための話法切替一覧です
- `MindUpload-EEGDATA-FundMap-qa.csv` は 制度タイプ別の想定質問50本と30秒回答を1行で引くための面談準備一覧です
- `MindUpload-EEGDATA-FundMap-mock-interviews.csv` は 制度タイプ別の模擬面談台本を1行で引くためのロールプレイ一覧です
- `MindUpload-EEGDATA-FundMap-oral-scripts.csv` は 制度タイプ別の1分版・3分版口頭説明テンプレを1行で引くための口頭説明一覧です
- `MindUpload-EEGDATA-FundMap-reverse-questions.csv` は 制度タイプ別の逆質問テンプレを1行で引くための逆質問一覧です
- `MindUpload-EEGDATA-FundMap-followup-mails.csv` は 制度タイプ別の面談後フォローメール草案を1行で引くための事後連絡一覧です
- `MindUpload-EEGDATA-FundMap-oral-scripts-5min.csv` は 制度タイプ別の5分版口頭説明テンプレを1行で引くための長尺説明一覧です
- `MindUpload-EEGDATA-FundMap-reviewer-tone.csv` は 審査員タイプ別の刺さる言い換えを1行で引くための話法調整一覧です
- `MindUpload-EEGDATA-FundMap-resubmission.csv` は 不採択後の再申請テンプレを1行で引くための再申請一覧です
- `MindUpload-EEGDATA-FundMap-document-checklist.csv` は 制度別の提出書類チェックリストを1行で引くための提出前確認一覧です
- `MindUpload-EEGDATA-FundMap-comment-rewrites.csv` は 審査コメント別の1文修正版を1行で引くための修文一覧です
- `MindUpload-EEGDATA-FundMap-budget-fallback.csv` は 制度タイプ別の予算削減 fallback を1行で引くための縮小運用一覧です
- `MindUpload-EEGDATA-FundMap-post-award-ops.csv` は 採択後30日 / 60日 / 90日の運用チェックを1行で引くための運用一覧です
- `MindUpload-EEGDATA-FundMap-failure-cases.csv` は 制度タイプ別の失敗例集を1行で引くための失敗パターン一覧です
- `MindUpload-EEGDATA-FundMap-post-pass-qa.csv` は 審査通過後の面談想定追加質問を1行で引くための通過後QA一覧です
- `MindUpload-EEGDATA-FundMap-collab-outreach.csv` は 共同研究打診メールの初稿を1行で引くための連携打診一覧です
- `MindUpload-EEGDATA-FundMap-collab-rubric.csv` は 共同研究先の選び方ルーブリックを1行で引くための相手先評価一覧です
- `MindUpload-EEGDATA-FundMap-re-outreach.csv` は 断られたときの再打診テンプレを1行で引くための再接触一覧です
- `MindUpload-EEGDATA-FundMap-one-page-apps.csv` は 制度タイプ別の1ページ申請書ひな形を1行で引くための圧縮申請一覧です
- `MindUpload-EEGDATA-FundMap-report-templates.csv` は 制度タイプ別の採択後レポート雛形を1行で引くための報告書一覧です
- `MindUpload-EEGDATA-FundMap-collab-roles.csv` は 共同研究の役割分担テンプレを1行で引くための分担一覧です
- `MindUpload-EEGDATA-FundMap-topic-collab-fit.csv` は 25トピックと連携先タイプの相性を1行で引くための相性一覧です
- `MindUpload-EEGDATA-FundMap-midterm-templates.csv` は 制度タイプ別の中間報告テンプレを1行で引くための中間報告一覧です
- `MindUpload-EEGDATA-FundMap-collab-agenda.csv` は 共同研究会議の30分アジェンダを1行で引くための会議進行一覧です
- `MindUpload-EEGDATA-FundMap-topic-first-outreach.csv` は 25トピック別の最初の打診先候補メモを1行で引くための初動一覧です
- `MindUpload-EEGDATA-FundMap-monthly-review.csv` は 制度タイプ別の月次レビュー表を1行で引くための定例確認一覧です
- `MindUpload-EEGDATA-FundMap-kickoff-memo.csv` は 共同研究開始時の合意メモ雛形を1行で引くための開始合意一覧です
- `MindUpload-EEGDATA-FundMap-topic-first-artifacts.csv` は 25トピック別の first artifact 下書きを1行で引くための初稿一覧です
- `MindUpload-EEGDATA-FundMap-quarterly-review.csv` は 制度タイプ別の四半期レビュー表を1行で引くための四半期確認一覧です
- `MindUpload-EEGDATA-FundMap-close-memo.csv` は 共同研究終了時のクローズメモ雛形を1行で引くための終了整理一覧です
- `MindUpload-EEGDATA-FundMap-short-abstracts-100.csv` は 25トピック別の100字要約を1行で引くための短要約一覧です
- `MindUpload-EEGDATA-FundMap-pitches-30s.csv` は 25トピック別の30秒ピッチを1行で引くための口頭説明一覧です
- `MindUpload-EEGDATA-FundMap-pre-submit-check.csv` は 制度タイプ別の提出直前チェックを1行で引くための最終確認一覧です
- `MindUpload-EEGDATA-FundMap-first-meeting-memo.csv` は 共同研究先タイプ別の初回面談メモ雛形を1行で引くための初回会話一覧です
- `MindUpload-EEGDATA-FundMap-one-slide-skeletons.csv` は 25トピック別の1枚スライド骨子を1行で引くためのスライド初稿一覧です
- `MindUpload-EEGDATA-FundMap-submit-day-ops.csv` は 制度タイプ別の提出当日オペレーションを1行で引くための当日運用一覧です
- `MindUpload-EEGDATA-FundMap-second-meeting-agenda.csv` は 共同研究先タイプ別の2回目面談アジェンダを1行で引くための次回会話一覧です
- `MindUpload-EEGDATA-FundMap-figure-captions.csv` は 25トピック別の図表キャプションを1行で引くための図表説明一覧です
- `MindUpload-EEGDATA-FundMap-post-submit-followup.csv` は 制度タイプ別の提出後フォロー運用を1行で引くための提出後運用一覧です
- `MindUpload-EEGDATA-FundMap-collab-continue-stop.csv` は 共同研究先タイプ別の継続条件と断り条件を1行で引くための連携判定一覧です
- `MindUpload-EEGDATA-FundMap-reviewer-figure-talk.csv` は 25トピック別の審査員向け図1枚の読み上げ文を1行で引くための図説明一覧です
- `MindUpload-EEGDATA-FundMap-rejection-48h.csv` は 制度タイプ別の不採択通知後48時間運用を1行で引くための再起動一覧です
- `MindUpload-EEGDATA-FundMap-collab-resume-hold.csv` は 共同研究先タイプ別の再開条件と保留条件を1行で引くための保留再開一覧です
- `MindUpload-EEGDATA-FundMap-review-roundtrip.csv` は 25トピック別の最初の査読コメント想定と返し1往復を1行で引くための査読初動一覧です
- `MindUpload-EEGDATA-FundMap-reapply-1week.csv` は 制度タイプ別の再応募1週間プランを1行で引くための再応募週間一覧です
- `MindUpload-EEGDATA-FundMap-lost-deal-followup.csv` は 共同研究先タイプ別の失注後フォロー文面を1行で引くための失注後連絡一覧です
- `MindUpload-EEGDATA-FundMap-first-30days.csv` は 25トピック別の採択後最初の30日タスクを1行で引くための初月運用一覧です
- `MindUpload-EEGDATA-FundMap-interview-recovery.csv` は 制度タイプ別の面談失敗からの立て直しを1行で引くための面談修復一覧です
- `MindUpload-EEGDATA-FundMap-next-proposal-onepager.csv` は 共同研究先タイプ別の次回提案1ページ骨子を1行で引くための次回提案一覧です
- `MindUpload-EEGDATA-FundMap-topic-month-end-review.csv` は 25トピック別の月末レビュー観点を1行で引くための topic 月次確認一覧です
- `MindUpload-EEGDATA-FundMap-second-meeting-plus.csv` は 制度タイプ別の2回目面談テンプレ強化版を1行で引くための制度別面談一覧です
- `MindUpload-EEGDATA-FundMap-nda-tone-switch.csv` は 共同研究先タイプ別のNDA前後で変える説明文を1行で引くための NDA 切替一覧です
- `MindUpload-EEGDATA-FundMap-topic-quarterly-review.csv` は 25トピック別の四半期レビュー観点を1行で引くための topic 四半期確認一覧です
- `MindUpload-EEGDATA-FundMap-final-meeting-close.csv` は 制度タイプ別の最終面談クロージング文を1行で引くための最終面談一覧です
- `MindUpload-EEGDATA-FundMap-first-data-share-checklist.csv` は 共同研究先タイプ別の first data share 前チェックリストを1行で引くための共有前確認一覧です
- `MindUpload-EEGDATA-FundMap-topic-halfyear-review.csv` は 25トピック別の半年レビュー観点を1行で引くための topic 半年確認一覧です
- `MindUpload-EEGDATA-FundMap-post-award-kickoff.csv` は 制度タイプ別の採択後キックオフ面談文を1行で引くための採択後開始一覧です
- `MindUpload-EEGDATA-FundMap-pre-publication-checklist.csv` は 共同研究先タイプ別の成果公開前チェックリストを1行で引くための公開前確認一覧です
- `MindUpload-EEGDATA-FundMap-topic-annual-review.csv` は 25トピック別の年間レビュー観点を1行で引くための topic 年次確認一覧です
- `MindUpload-EEGDATA-FundMap-reportback-talk.csv` は 制度タイプ別の成果報告会トークトラックを1行で引くための成果報告話法一覧です
- `MindUpload-EEGDATA-FundMap-post-publication-followup.csv` は 共同研究先タイプ別の公開後フォロー文面を1行で引くための公開後連絡一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-year-start.csv` は 25トピック別の翌年度開始メモを1行で引くための topic 翌年度開始一覧です
- `MindUpload-EEGDATA-FundMap-final-deliverable-onepager.csv` は 制度タイプ別の最終成果物1枚要約を1行で引くための最終成果要約一覧です
- `MindUpload-EEGDATA-FundMap-collab-reconnect-timing.csv` は 共同研究先タイプ別の再接続タイミング表を1行で引くための再接続運用一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-year-q1.csv` は 25トピック別の翌年度Q1タスクを1行で引くための topic Q1実行一覧です
- `MindUpload-EEGDATA-FundMap-final-report-mail.csv` は 制度タイプ別の最終報告メール文面を1行で引くための最終報告連絡一覧です
- `MindUpload-EEGDATA-FundMap-reconnect-first-meeting.csv` は 共同研究先タイプ別の再接続後初回面談メモを1行で引くための再接続初回面談一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-year-q2.csv` は 25トピック別の翌年度Q2タスクを1行で引くための topic Q2実行一覧です
- `MindUpload-EEGDATA-FundMap-final-deliverable-submit-check.csv` は 制度タイプ別の最終成果物提出チェックを1行で引くための提出前確認一覧です
- `MindUpload-EEGDATA-FundMap-reconnect-30days.csv` は 共同研究先タイプ別の再接続後30日運用を1行で引くための再接続30日一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-year-q3.csv` は 25トピック別の翌年度Q3タスクを1行で引くための topic Q3実行一覧です
- `MindUpload-EEGDATA-FundMap-final-archive-check.csv` は 制度タイプ別の最終成果物アーカイブチェックを1行で引くための保存前確認一覧です
- `MindUpload-EEGDATA-FundMap-reconnect-60days.csv` は 共同研究先タイプ別の再接続後60日レビューを1行で引くための再接続60日一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-year-q4.csv` は 25トピック別の翌年度Q4タスクを1行で引くための topic Q4実行一覧です
- `MindUpload-EEGDATA-FundMap-final-publication-check.csv` は 制度タイプ別の最終成果物公開チェックを1行で引くための公開前確認一覧です
- `MindUpload-EEGDATA-FundMap-reconnect-90days.csv` は 共同研究先タイプ別の再接続後90日レビューを1行で引くための再接続90日一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-year-close.csv` は 25トピック別の翌年度年末クローズメモを1行で引くための topic 年末クローズ一覧です
- `MindUpload-EEGDATA-FundMap-final-publication-followup.csv` は 制度タイプ別の最終成果物公開後フォローを1行で引くための公開後フォロー一覧です
- `MindUpload-EEGDATA-FundMap-collab-reconnect-close.csv` は 共同研究先タイプ別の再接続クローズ文面を1行で引くための再接続終了一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-cycle-summary.csv` は 25トピック別の次年度初動総括を1行で引くための topic 初動総括一覧です
- `MindUpload-EEGDATA-FundMap-publication-30days-review.csv` は 制度タイプ別の公開後30日レビューを1行で引くための公開後30日確認一覧です
- `MindUpload-EEGDATA-FundMap-collab-reopen-lines.csv` は 共同研究先タイプ別の再開文面を1行で引くための再開連絡一覧です
- `MindUpload-EEGDATA-FundMap-topic-strategy-onepager.csv` は 25トピック別の次年度1ページ戦略メモを1行で引くための topic 戦略1枚一覧です
- `MindUpload-EEGDATA-FundMap-publication-90days-review.csv` は 制度タイプ別の公開後90日レビューを1行で引くための公開後90日確認一覧です
- `MindUpload-EEGDATA-FundMap-collab-reopen-reply.csv` は 共同研究先タイプ別の再開後初回メール返信テンプレを1行で引くための再開返信一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-cycle-3month.csv` は 25トピック別の次年度3か月戦略を1行で引くための topic 3か月戦略一覧です
- `MindUpload-EEGDATA-FundMap-publication-halfyear-review.csv` は 制度タイプ別の公開後半年レビューを1行で引くための公開後半年確認一覧です
- `MindUpload-EEGDATA-FundMap-collab-reopen-second-reply.csv` は 共同研究先タイプ別の再開後2通目返信テンプレを1行で引くための再開2通目返信一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-cycle-6month.csv` は 25トピック別の次年度6か月戦略を1行で引くための topic 6か月戦略一覧です
- `MindUpload-EEGDATA-FundMap-publication-1year-review.csv` は 制度タイプ別の公開後1年レビューを1行で引くための公開後1年確認一覧です
- `MindUpload-EEGDATA-FundMap-collab-reopen-third-reply.csv` は 共同研究先タイプ別の再開後3通目返信テンプレを1行で引くための再開3通目返信一覧です
- `MindUpload-EEGDATA-FundMap-topic-next-cycle-annual.csv` は 25トピック別の次年度年次戦略を1行で引くための topic 年次戦略一覧です
- `MindUpload-EEGDATA-FundMap-publication-close-decision.csv` は 制度タイプ別の公開後クローズ判断を1行で引くための公開後終了判断一覧です
- `MindUpload-EEGDATA-FundMap-collab-reopen-close-reply.csv` は 共同研究先タイプ別の再開後クローズ返信テンプレを1行で引くための再開後終了一覧です
- `MindUpload-EEGDATA-FundMap-topic-multiyear-roadmap.csv` は 25トピック別の複数年ロードマップ要約を1行で引くための topic 複数年要約一覧です
- `MindUpload-EEGDATA-FundMap-publication-archive-ops.csv` は 制度タイプ別の公開後アーカイブ運用を1行で引くための公開後保存運用一覧です
- `MindUpload-EEGDATA-FundMap-collab-restart-rubric.csv` は 共同研究先タイプ別の再始動判断ルーブリックを1行で引くための再始動判断一覧です
- `MindUpload-EEGDATA-FundMap-topic-multiyear-exit.csv` は 25トピック別の複数年撤退条件を1行で引くための topic 撤退条件一覧です
- `MindUpload-EEGDATA-FundMap-publication-spillover-notes.csv` は 制度タイプ別の公開後波及効果メモを1行で引くための公開後波及効果一覧です
- `MindUpload-EEGDATA-FundMap-collab-restart-deferral.csv` は 共同研究先タイプ別の再始動見送り文面を1行で引くための再始動見送り一覧です
- `MindUpload-EEGDATA-FundMap-topic-multiyear-reentry.csv` は 25トピック別の複数年復帰条件を1行で引くための topic 復帰条件一覧です
- `MindUpload-EEGDATA-FundMap-publication-spillover-score.csv` は 制度タイプ別の公開後波及効果スコア表を1行で引くための公開後波及スコア一覧です
- `MindUpload-EEGDATA-FundMap-collab-deferral-followup.csv` は 共同研究先タイプ別の見送り後フォロー文面を1行で引くための見送り後フォロー一覧です
- `MindUpload-EEGDATA-FundMap-topic-reentry-90days.csv` は 25トピック別の複数年復帰後90日プランを1行で引くための topic 復帰後90日一覧です
- `MindUpload-EEGDATA-FundMap-publication-spillover-evidence.csv` は 制度タイプ別の波及効果を示す証拠メモを1行で引くための波及証拠一覧です
- `MindUpload-EEGDATA-FundMap-collab-deferral-reoutreach.csv` は 共同研究先タイプ別の見送り後再打診テンプレを1行で引くための再打診一覧です
- `MindUpload-EEGDATA-FundMap-topic-reentry-180days.csv` は 25トピック別の復帰後180日プランを1行で引くための topic 復帰後180日一覧です
- `MindUpload-EEGDATA-FundMap-publication-spillover-report.csv` は 制度タイプ別の波及効果報告テンプレを1行で引くための波及報告一覧です
- `MindUpload-EEGDATA-FundMap-collab-reoutreach-first-meeting.csv` は 共同研究先タイプ別の再打診後初回面談メモを1行で引くための再打診後初回面談一覧です
- `MindUpload-EEGDATA-FundMap-topic-reentry-1year.csv` は 25トピック別の復帰後1年プランを1行で引くための topic 復帰後1年一覧です
- `MindUpload-EEGDATA-FundMap-publication-spillover-mail.csv` は 制度タイプ別の波及効果報告メール文面を1行で引くための波及報告メール一覧です
- `MindUpload-EEGDATA-FundMap-collab-reoutreach-agreement-memo.csv` は 共同研究先タイプ別の再打診後合意メモを1行で引くための再打診後合意一覧です
- `MindUpload-EEGDATA-FundMap-topic-reentry-close.csv` は 25トピック別の復帰後クローズ判断表を1行で引くための topic 復帰後終了判断一覧です
- `MindUpload-EEGDATA-FundMap-publication-spillover-onepager.csv` は 制度タイプ別の波及効果報告1ページ版を1行で引くための波及報告1枚一覧です
- `MindUpload-EEGDATA-FundMap-collab-reoutreach-close-conditions.csv` は 共同研究先タイプ別の再打診後クローズ条件を1行で引くための再打診後終了条件一覧です
- `MindUpload-EEGDATA-FundMap-topic-reentry-restop.csv` は 25トピック別の復帰後再停止テンプレを1行で引くための topic 再停止一覧です
- `MindUpload-EEGDATA-FundMap-publication-spillover-final-check.csv` は 制度タイプ別の波及効果最終報告チェックを1行で引くための波及最終確認一覧です
- `MindUpload-EEGDATA-FundMap-collab-reoutreach-archive-memo.csv` は 共同研究先タイプ別の再打診後アーカイブメモを1行で引くための再打診後保存一覧です
- `MindUpload-EEGDATA-FundMap-topic-reentry-retry.csv` は 25トピック別の復帰後再挑戦条件を1行で引くための topic 再挑戦一覧です
- `MindUpload-EEGDATA-FundMap-publication-final-followup.csv` は 制度タイプ別の最終報告送付後フォローを1行で引くための最終報告後フォロー一覧です
- `MindUpload-EEGDATA-FundMap-collab-reoutreach-resume-conditions.csv` は 共同研究先タイプ別の再打診後再開条件メモを1行で引くための再打診後再開条件一覧です
- `MindUpload-EEGDATA-FundMap-topic-retry-90days.csv` は 25トピック別の再挑戦後90日プランを1行で引くための topic 再挑戦後90日一覧です
- `MindUpload-EEGDATA-FundMap-publication-final-30days-review.csv` は 制度タイプ別の最終報告後30日レビューを1行で引くための最終報告後30日確認一覧です
- `MindUpload-EEGDATA-FundMap-collab-resume-first-30days.csv` は 共同研究先タイプ別の再開後最初の30日メモを1行で引くための再開後30日一覧です
- `MindUpload-EEGDATA-FundMap-topic-retry-180days.csv` は 25トピック別の再挑戦後180日プランを1行で引くための topic 再挑戦後180日一覧です
- `MindUpload-EEGDATA-FundMap-publication-final-90days-review.csv` は 制度タイプ別の最終報告後90日レビューを1行で引くための最終報告後90日確認一覧です
- `MindUpload-EEGDATA-FundMap-collab-resume-60days.csv` は 共同研究先タイプ別の再開後60日メモを1行で引くための再開後60日一覧です
- `MindUpload-EEGDATA-FundMap-topic-retry-1year.csv` は 25トピック別の再挑戦後1年プランを1行で引くための topic 再挑戦後1年一覧です
- `MindUpload-EEGDATA-FundMap-publication-final-close.csv` は 制度タイプ別の最終報告後クローズ判断を1行で引くための最終報告後終了判断一覧です
- `MindUpload-EEGDATA-FundMap-collab-resume-90days.csv` は 共同研究先タイプ別の再開後90日メモを1行で引くための再開後90日一覧です
- 現在の列は `phase`, `topic`, `verdict`, `grant_theme`, `eeg_data_slices`, `candidate_datasets`, `first_metrics`, `candidate_programs`, `claim_level`, `support_type_priority`, `12_week_deliverable`, `main_risk` です
- 申請先を先に決めるなら `support_type_priority` で絞る
- 3か月で何を出すか先に見るなら `12_week_deliverable` を使う
- 危ない主張を避けるなら `claim_level` と `main_risk` を先に確認する

## 25. 25トピック別 申請タイトル案バンク

### EEG信号品質の限界検証

- 題目案1: 公開EEG横断における信号品質指標の再現性評価
- 題目案2: 携帯型・単チャネルEEGを含むアーチファクト耐性ベンチマーク
- 題目案3: 公開EEGに基づく品質管理指標標準化のための比較研究

### 高密度EEG空間分解能評価

- 題目案1: 高密度EEGソース推定の空間限界と電極数依存性の評価
- 題目案2: ground-truth 付きHD-EEGに基づく局在精度ベンチマーク
- 題目案3: 公開高密度EEGで検証する source localization 再現性研究

### マルチモーダル統合の基礎

- 題目案1: EEG-fNIRS・視線統合における時系列同期誤差の定量化
- 題目案2: 公開マルチモーダル脳データの融合性能比較と標準化
- 題目案3: 認知負荷推定に向けた EEG マルチモーダル統合基盤の検証

### ノイズ除去・信号分離手法の比較

- 題目案1: 公開EEGにおける ASR/ICA 系前処理の横断比較
- 題目案2: アーチファクト混入EEGの信号保存率ベンチマーク
- 題目案3: ノイズ除去手法差がEEG指標に与える影響の再現性評価

### 長時間記録の安定性評価

- 題目案1: 長時間EEG記録におけるドリフトと状態遷移の安定性評価
- 題目案2: 睡眠・疲労を含む縦断EEGの品質変動解析
- 題目案3: 公開長時間EEGデータによる session stability benchmark

### デコーディング精度ベンチマーク

- 題目案1: 公開EEGデコーディング課題における統一ベンチマーク構築
- 題目案2: MI・ERP・SSVEP を横断した decoding 精度の再現性評価
- 題目案3: 複数公開EEG課題に基づく decoding 基盤性能の比較研究

### クロスデータセット汎化

- 題目案1: 公開EEG横断での cross-dataset generalization 限界測定
- 題目案2: EEG decoding におけるデータセット移送性能の体系比較
- 題目案3: subject shift と dataset shift を分離したEEG汎化評価

### リアルタイムデコーディング

- 題目案1: replay ベースで評価するリアルタイムEEG decoding の遅延限界
- 題目案2: SSVEP・MI課題におけるオンライン近似評価基盤の構築
- 題目案3: 公開EEGを用いたリアルタイムBCI性能の事前検証

### Foundation Modelの適用

- 題目案1: 公開EEG自己教師あり表現学習の基盤性能評価
- 題目案2: 睡眠・運動意図・感情を横断する EEG foundation representation の検証
- 題目案3: 少数ラベル条件におけるEEG表現学習の汎化限界測定

### 運動意図デコーディング

- 題目案1: cross-subject motor imagery decoding の汎化限界評価
- 題目案2: 公開MIデータに基づく被験者間一般化ベンチマーク
- 題目案3: リハビリ応用を見据えた運動意図EEG decoding の再現性研究

### 感覚知覚デコーディング

- 題目案1: ERP/P300/SSVEP による感覚知覚 decoding の再現性評価
- 題目案2: 視覚・聴覚誘発EEGを用いた知覚分類ベンチマーク
- 題目案3: 知覚関連ERPとSSVEPの統合比較による attention proxy 解析

### 言語/意味デコーディング

- 題目案1: imagined speech EEG decoding の成立条件に関する比較研究
- 題目案2: semantic congruency と内言課題を用いた EEG 言語表現の検証
- 題目案3: 公開言語EEGデータ横断による意味デコーディング限界測定

### 感情状態の推定・分類

- 題目案1: emotion/stress EEG の被験者間頑健性評価
- 題目案2: valence-arousal と stress 反応を横断したEEG分類ベンチマーク
- 題目案3: 公開感情EEGに基づく session transfer 性能の比較研究

### 記憶のエンコーディング/検索

- 題目案1: working memory と retrieval EEG 指標の再現性検証
- 題目案2: 記憶課題における encoding-retrieval EEG proxy の比較研究
- 題目案3: longitudinal EEG を用いた記憶関連指標の安定性評価

### 注意・ワーキングメモリ

- 題目案1: attention/workload EEG の汎化評価と作業負荷指標の標準化
- 題目案2: 単チャネルを含む公開EEGによるワーキングメモリ負荷推定
- 題目案3: 認知負荷推定のためのEEG workload benchmark 構築

### 意思決定過程

- 題目案1: リスク選択・報酬予測に関するEEG指標の比較研究
- 題目案2: 公開意思決定課題EEGに基づく価値評価 proxy の検証
- 題目案3: 報酬・損失条件差からみる意思決定EEGの再現性評価

### 社会的認知

- 題目案1: social stress と joint attention に関するEEG基礎評価
- 題目案2: hyperscanning EEG を用いた相互作用指標の探索的比較
- 題目案3: 公開社会的課題EEGに基づく inter-brain synchrony の検証

### 創造性・問題解決

- 題目案1: 問題解決過程のEEG proxy 指標探索
- 題目案2: creative insight に関連するERP指標の再現性評価
- 題目案3: 発想転換課題を用いた公開EEGの探索的比較研究

### 主観的経験の定量化

- 題目案1: subjective rating と EEG 指標の対応づけに関する比較研究
- 題目案2: pain・awareness 課題を用いた主観報告EEG proxy の検証
- 題目案3: 主観評価と生理信号の橋渡しとしての公開EEGベンチマーク

### 意識の神経相関（NCC）定量化

- 題目案1: 覚醒・睡眠・夢・眠気境界におけるEEG proxy の定量比較
- 題目案2: 公開睡眠EEGに基づく NCC 関連指標の再現性評価
- 題目案3: state transition を用いた consciousness proxy benchmark

### 意識状態の分類（覚醒/睡眠/麻酔/DoC）

- 題目案1: consciousness boundary classification の公開EEGベンチマーク
- 題目案2: 覚醒・眠気・睡眠・麻酔状態のEEG分類性能比較
- 題目案3: 複数公開データに基づく意識状態境界推定の再現性研究

### 統合情報理論(IIT)の実証的検証

- 題目案1: EEG複雑性指標を用いた IIT proxy の再計算と比較
- 題目案2: 睡眠・催眠・覚醒課題における統合情報 proxy の検証
- 題目案3: 公開EEGを用いた complexity-based consciousness 指標の評価

### Global Workspace Theory の検証

- 題目案1: P300/ignition proxy に基づく Global Workspace 指標の比較研究
- 題目案2: 知覚更新課題EEGにおける broadcast proxy の再現性評価
- 題目案3: 公開ERPデータ横断による GWT 関連指標の検証

### 意識の連続性と同一性

- 題目案1: 縦断EEGによる個人内安定性と状態連続性の指標化
- 題目案2: cross-session EEG biometrics を用いた自己関連安定性評価
- 題目案3: self-related EEG 指標と個人内変動の公開データ比較

### mind-upload可能性の理論的枠組み

- 題目案1: EEGベース検証可能性のクレーム階段設計と benchmark commons
- 題目案2: 公開EEGカタログに基づく mind-upload 前段課題の体系整理
- 題目案3: mind-upload 議論のための検証可能サブ問題アトラス構築

## 26. 25トピック別 要旨の芯と想定審査カテゴリ

### EEG信号品質の限界検証

- 要旨の芯: 公開EEGを用いてデバイス差と計測条件差を横断した品質指標を再計算し、SNR、bad channel率、artifact除去前後の情報保持率を比較する。後続の decoding や state classification の前提条件を benchmark として定量化する。
- 想定審査カテゴリ: `engineering_ai`, `medical`

### 高密度EEG空間分解能評価

- 要旨の芯: ground-truth 参照が可能な高密度EEGを中心に、電極数や前処理条件の差が局在誤差へ与える影響を比較する。空間分解能の上限を誇張せず、source localization の実用限界を整理する。
- 想定審査カテゴリ: `engineering_ai`, `medical`

### マルチモーダル統合の基礎

- 要旨の芯: EEG-fNIRS や eye-tracking を含む公開データを用いて、モダリティ同期誤差と融合有無による性能差を比較する。単一モダリティより頑健な認知負荷推定基盤を設計するための標準化条件を示す。
- 想定審査カテゴリ: `engineering_ai`, `education`

### ノイズ除去・信号分離手法の比較

- 要旨の芯: artifact 混入EEGと実測EEGを横断して ASR、ICA、周波数ノイズ除去系の前処理を比較し、信号保存率と下流性能への影響を測定する。前処理選択の経験則を benchmark として可視化する。
- 想定審査カテゴリ: `engineering_ai`

### 長時間記録の安定性評価

- 要旨の芯: 睡眠や疲労を含む長時間EEGを用いて、session drift、欠損率、状態遷移の安定性を評価する。長時間観測でどこまで信号品質と状態分類が保てるかを明らかにし、縦断研究の前提条件を整備する。
- 想定審査カテゴリ: `medical`, `engineering_ai`

### デコーディング精度ベンチマーク

- 要旨の芯: MI、ERP/P300、SSVEP をまたぐ複数公開課題に統一splitと統一metricを適用し、EEG decoding の基盤性能を比較する。個別論文依存の数値を離れ、再現可能な横断ベンチマークを作る。
- 想定審査カテゴリ: `engineering_ai`, `education`

### クロスデータセット汎化

- 要旨の芯: 同種課題を持つ複数EEGデータセット間で学習・評価を交差させ、dataset shift と subject shift の影響を切り分ける。公開EEGで一般化性能がどこで崩れるかを限界測定として示す。
- 想定審査カテゴリ: `engineering_ai`

### リアルタイムデコーディング

- 要旨の芯: オンライン収録そのものではなく、公開EEGの replay 評価を用いて遅延、窓長、更新頻度が decoding 性能へ与える影響を測定する。リアルタイムBCI実装前の事前条件を低コストで検証する。
- 想定審査カテゴリ: `engineering_ai`, `education`

### Foundation Modelの適用

- 要旨の芯: 睡眠、運動意図、感情など異種EEGを束ねて自己教師あり学習を行い、少数ラベル条件での linear probe と OOD gap を評価する。foundation model を誇張せず、表現学習が効く条件と効かない条件を切り分ける。
- 想定審査カテゴリ: `engineering_ai`

### 運動意図デコーディング

- 要旨の芯: 公開MIデータを用いて cross-subject 条件を中心に decoding 性能を評価し、被験者差が汎化へ与える影響を測る。リハビリや補助技術に接続できる実務的なMI benchmark を整備する。
- 想定審査カテゴリ: `engineering_ai`, `education`

### 感覚知覚デコーディング

- 要旨の芯: ERP/P300/SSVEP をまたぐ知覚課題で latency、amplitude、classification accuracy を比較し、知覚更新や attention proxy の再現性を調べる。感覚誘発EEGの評価軸を統一することを狙う。
- 想定審査カテゴリ: `engineering_ai`, `medical`

### 言語/意味デコーディング

- 要旨の芯: imagined speech、semantic congruency、N400 系公開EEGを用いて、言語ラベル定義と課題構造の差が decoding 成立性へ与える影響を比較する。強い言語復元主張ではなく、成立条件の整理に焦点を当てる。
- 想定審査カテゴリ: `engineering_ai`, `social_humanities`

### 感情状態の推定・分類

- 要旨の芯: valence-arousal と psychosocial stress を含む感情EEGを横断し、subject holdout と session transfer を用いて頑健性を評価する。感情推定がデータセット外でどこまで保つかを再現性の観点から明らかにする。
- 想定審査カテゴリ: `medical`, `engineering_ai`

### 記憶のエンコーディング/検索

- 要旨の芯: working memory と retrieval 課題を用いて、記憶関連EEG指標の再現性と longitudinal drift を比較する。記憶そのものの読取りではなく、encoding と retrieval に関わる proxy 指標の安定性評価として組み立てる。
- 想定審査カテゴリ: `medical`, `education`

### 注意・ワーキングメモリ

- 要旨の芯: workload と attention を含む公開EEGに統一的な分類設定を適用し、単チャネルを含む軽量条件での汎化性能を比較する。教育や実務現場でも展開しやすい認知負荷指標の標準化を目指す。
- 想定審査カテゴリ: `education`, `engineering_ai`

### 意思決定過程

- 要旨の芯: 報酬・損失・リスク選好を扱う公開課題EEGを比較し、価値評価 proxy と条件差の再現性を調べる。複雑な意思決定理論の証明ではなく、再現可能な行動条件差の抽出に論点を絞る。
- 想定審査カテゴリ: `social_humanities`, `engineering_ai`

### 社会的認知

- 要旨の芯: hyperscanning や social stress を含むデータを用いて、相互作用条件での inter-brain synchrony と task差を探索的に比較する。大きな理論主張は避け、共同研究形成に使える pilot 研究として位置づける。
- 想定審査カテゴリ: `social_humanities`, `medical`

### 創造性・問題解決

- 要旨の芯: creative insight や problem solving 課題の公開EEGを比較し、問題解決過程に関わる ERP proxy の再現性を測る。創造性の本質論ではなく、探索的に再利用可能な課題設計と指標候補を残す。
- 想定審査カテゴリ: `education`, `social_humanities`

### 主観的経験の定量化

- 要旨の芯: pain や awareness の主観評価を伴う公開データを用いて、self-report と EEG 指標の対応関係を比較する。主観そのものを還元するのではなく、報告可能な proxy 指標の限界を定量化する。
- 想定審査カテゴリ: `medical`, `social_humanities`

### 意識の神経相関（NCC）定量化

- 要旨の芯: awake-sleep-dream-drowsy の境界を含む公開EEGを用いて、複雑性指標や遷移指標の変化を比較する。NCC の決着ではなく、状態境界に敏感な proxy 群の再現性評価として整理する。
- 想定審査カテゴリ: `medical`, `engineering_ai`

### 意識状態の分類（覚醒/睡眠/麻酔/DoC）

- 要旨の芯: 複数の睡眠・眠気・麻酔関連EEGデータに統一分類設定を与え、state accuracy と confusion pattern を比較する。意識状態境界の判定可能性を安全な工学・医療テーマとしてベンチマーク化する。
- 想定審査カテゴリ: `medical`, `engineering_ai`

### 統合情報理論(IIT)の実証的検証

- 要旨の芯: 睡眠や催眠の公開EEGから複雑性 proxy を再計算し、状態差と指標安定性を比較する。IIT そのものの真偽を論じるのではなく、理論が要求する proxy 指標の挙動比較に限定する。
- 想定審査カテゴリ: `engineering_ai`, `medical`

### Global Workspace Theory の検証

- 要旨の芯: P300 や ignition/broadcast proxy を含む公開ERP課題を用いて、知覚更新条件での成分差と再現性を比較する。GWT の全面検証ではなく、理論が予測する proxy の挙動を比較する工学的研究として書く。
- 想定審査カテゴリ: `engineering_ai`, `medical`

### 意識の連続性と同一性

- 要旨の芯: cross-session EEG biometrics と self-related EEG 指標を用いて、個人内安定性と状態変動の関係を比較する。本人性の証明を避け、縦断観測で得られる stability proxy の上限を示す。
- 想定審査カテゴリ: `social_humanities`, `engineering_ai`

### mind-upload可能性の理論的枠組み

- 要旨の芯: `EEG-DATA` の公開カタログと主要課題を整理し、どの主張がどの測定・汎化・状態分類の前提に依存するかをクレーム階段として設計する。理論決着ではなく、検証可能サブ問題の共有基盤を作る活動として位置づける。
- 想定審査カテゴリ: `social_humanities`, `education`

## 27. 300字前後の要旨叩き台

### 27.1 Phase 1

#### EEG信号品質の限界検証

- 要旨叩き台: 公開EEGデータを対象に、電極数、サンプリング周波数、記録長、欠損チャネル率、眼電・筋電混入度の違いが、周波数特徴量、ERP振幅、単純分類性能の再現性に与える影響を定量化する。統一前処理と被験者外分割を固定し、品質指標ごとの閾値、誤差幅、破綻条件を信頼区間付きで整理して、再利用可能な品質監査基準を提案する。
- 想定審査カテゴリ: `医工学`, `神経科学`

#### 高密度EEG空間分解能評価

- 要旨叩き台: 高密度EEG公開データを低密度構成へ段階的にサブサンプリングし、電極密度の差が空間トポグラフィ再現性、チャネル冗長性、課題弁別性能に与える利得を比較する。ソース推定そのものの強主張は避け、電極配置別に情報利得の逓減点と被験者間ばらつきを定量化し、高密度化が有効な条件を実証的に整理する。
- 想定審査カテゴリ: `電気・電子工学`, `神経科学`

#### マルチモーダル統合の基礎

- 要旨叩き台: EEGとEOG、ECG、加速度、行動ログが併記された公開同時計測データを用い、同期ずれ、欠測、モダリティ不均衡が解析結果に与える影響を評価する。早期統合と後期統合を、状態分類やアーチファクト検出など保守的な課題で比較し、単独EEGに対する追加情報の実利と再現コストのバランスを監査可能な形で示す。
- 想定審査カテゴリ: `医工学`, `情報学`

#### ノイズ除去・信号分離手法の比較

- 要旨叩き台: ICA、ASR、回帰法、SSP、成分自動分類など複数の前処理手法を、公開EEGデータ上で同一条件比較し、ノイズ除去量と神経由来成分の保持率の両面から評価する。EOG/EMGを伴うデータやERP課題を用いて、手法ごとのSNR改善、波形歪み、下流解析の安定性、再実行容易性を測定し、用途別の推奨条件を整理する。
- 想定審査カテゴリ: `情報学`, `医工学`

#### 長時間記録の安定性評価

- 要旨叩き台: 長時間安静時EEG、睡眠EEG、ウェアラブル連続記録などの公開データを用い、時間経過に伴うスペクトル基線の漂移、チャネル脱落、ラベル安定性の変化を定量化する。区間長、再較正間隔、品質管理頻度を変えた擬似運用実験を行い、どの条件で解析結果が安定し続けるかを被験者内外で比較して、長時間運用の実務指針を示す。
- 想定審査カテゴリ: `計測工学`, `医工学`

### 27.2 Phase 2

#### デコーディング精度ベンチマーク

- 要旨叩き台: 運動想起、ERP、SSVEPなど公開EEG課題を横断し、統一前処理、固定分割、共通統計指標の下で、古典手法と深層学習手法の基礎性能を再評価する。単純な最高精度競争ではなく、効果量、校正誤差、失敗率、計算資源、再実行安定性をあわせて報告し、助成研究で再利用しやすいベンチマーク基準を整備する。
- 想定審査カテゴリ: `情報学`, `医工学`

#### クロスデータセット汎化

- 要旨叩き台: 同種課題の公開EEGデータ間で学習・評価を分離し、施設差、電極配置差、前処理差が汎化性能に与える劣化幅を定量化する。被験者外評価に加えてデータセット外評価を標準化し、ドメイン適応や特徴正規化の効果を過度に一般化せず比較することで、汎化が成立しやすい条件と破綻しやすい条件を明確化する。
- 想定審査カテゴリ: `情報学`, `AI`

#### リアルタイムデコーディング

- 要旨叩き台: 連続公開EEGを用いた擬似オンライン再生環境を構築し、窓長、更新間隔、特徴抽出法、分類器構成の違いが遅延と判別安定性に与える影響を評価する。実機制御の強主張は避け、オフライン再生から得られる処理時間、予測変動、誤警報率を比較し、リアルタイム化へ進む前段階として必要な計算条件と性能下限を整理する。
- 想定審査カテゴリ: `情報学`, `電気・電子工学`

#### Foundation Modelの適用

- 要旨叩き台: 複数の公開EEGデータを用いて自己教師あり学習や事前学習モデルの表現を構築し、少量ラベル条件での適応性能、校正、分布外頑健性を比較する。万能モデルの主張ではなく、課題類似度、電極数、記録長の違いが転移効果を左右する条件を検証し、公開データ規模で実行可能な基盤表現の有効範囲を限定付きで示す。
- 想定審査カテゴリ: `情報学`, `AI`

#### 運動意図デコーディング

- 要旨叩き台: 公開運動想起EEGと運動準備関連データを対象に、左手・右手・足など基本クラスの弁別性能と、その被験者差・セッション差への感度を定量化する。CSP系手法と深層学習手法を同一条件で比較し、較正試行数の削減、誤分類の偏り、特徴の時間周波数安定性を評価して、運動意図推定の現実的な適用範囲を整理する。
- 想定審査カテゴリ: `医工学`, `情報学`

#### 感覚知覚デコーディング

- 要旨叩き台: 視覚刺激、聴覚刺激、オドボール、SSVEPなど公開EEG課題を用い、刺激種別や知覚条件の弁別可能性を横断比較する。課題ごとに異なるラベル定義を統一し、ERP成分、周波数応答、試行数依存性、被験者外劣化を検証することで、感覚知覚関連指標の再現性と、課題間で移植しやすい特徴の範囲を保守的に明らかにする。
- 想定審査カテゴリ: `神経科学`, `情報学`

#### 言語/意味デコーディング

- 要旨叩き台: 想起発話データ、N400課題、語彙判断課題などの公開EEGを用い、自由文の復元ではなく、語彙カテゴリ、意味一致・不一致、発話準備条件といった限定的ラベルの弁別可能性を検証する。前処理、時間窓、表現学習法を統一して被験者外性能と不確実性を評価し、言語関連EEG解析で何が安定して測れるかを段階的に整理する。
- 想定審査カテゴリ: `認知神経科学`, `情報学`

### 27.3 Phase 3

#### 感情状態の推定・分類

- 要旨叩き台: 公開EEGデータに含まれる感情誘発課題を対象に、快不快・覚醒度の二軸ラベルが被験者外・セッション外でもどこまで再現可能かを検証する。高精度追求そのものではなく、周波数帯・時間窓・前頭頭頂分布のうち頑健な特徴と崩れやすい条件を切り分け、データセット差をまたいだ感情推定の実用的な上限と評価手順を整理する。
- 想定審査カテゴリ: `認知神経科学`, `精神生理学`

#### 記憶のエンコーディング/検索

- 要旨叩き台: 公開EEGの記銘・再認・ワーキングメモリ課題を横断し、符号化時活動が後続の想起成否や再認反応とどの程度対応するかを検証する。課題間で共通する事象関連成分と周波数特徴を抽出し、被験者外評価で維持される記憶指標と課題依存で崩れる指標を分離することで、EEGで追える記憶過程の範囲を限定的に明確化する。
- 想定審査カテゴリ: `記憶神経科学`, `認知神経科学`

#### 注意・ワーキングメモリ

- 要旨叩き台: 公開EEGデータの持続注意課題と認知負荷課題を用い、注意低下とワーキングメモリ負荷上昇を区別できる特徴量の再現性を評価する。単一データセット最適化を避け、被験者外・装置差あり条件で性能劣化を測定し、前頭正中θや頭頂α抑制など既知指標がどの条件で安定し、どの条件で混同されるかを整理する。
- 想定審査カテゴリ: `認知神経科学`, `生体医工学`

#### 意思決定過程

- 要旨叩き台: 公開EEGの二択選択課題や報酬学習課題を対象に、選択前の不確実性、選択後の確信度、フィードバック処理が時間周波数特徴としてどこまで分離できるかを検証する。正答率の最大化ではなく、被験者外・課題外でも保たれる意思決定段階の境界を測り、判断過程を過度に一般化しない比較基盤を整える。
- 想定審査カテゴリ: `計算論的神経科学`, `認知科学`

#### 社会的認知

- 要旨叩き台: 公開EEGに含まれる顔表情、視線、自己他者判断、協調課題を対象に、社会的手掛かりの処理に共通する時系列特徴を比較する。特定課題での高性能分類ではなく、刺激種別や文化差、セッション差をまたいでも残る成分を抽出し、社会的認知のうちEEGで比較的安定に観測できる処理段階と不安定な段階を切り分ける。
- 想定審査カテゴリ: `社会神経科学`, `認知神経科学`

#### 創造性・問題解決

- 要旨叩き台: 公開EEGの発散的思考課題や洞察課題を用いて、課題準備、探索、解答到達の各段階に対応する周波数変化と機能結合の再現性を検証する。創造性そのものの高低を断定するのではなく、被験者内外で比較可能な問題解決過程の指標を整理し、課題形式や採点法の違いで崩れにくいEEG特徴の候補を絞り込む。
- 想定審査カテゴリ: `認知科学`, `神経情報学`

#### 主観的経験の定量化

- 要旨叩き台: 公開EEGデータに付随する主観評定、確信度、鮮明さ、眠気、心的迷走の自己報告を対象に、主観尺度と神経指標の対応の再現性を検証する。単回帰の有意差に依存せず、評定のばらつき、再テスト信頼性、被験者外予測を合わせて評価し、主観的経験のうちEEGで安定して近似できる側面と近似が難しい側面を明確化する。
- 想定審査カテゴリ: `意識研究`, `認知神経科学`

### 27.4 Phase 4

#### 意識の神経相関（NCC）定量化

- 要旨叩き台: 公開EEGの覚醒、睡眠、麻酔、意識障害関連データを統一前処理で再解析し、複雑性、長距離結合、遅延応答などの候補指標が状態差をどこまで一貫して説明するかを比較する。単一理論への適合を急がず、施設差と装置差を含む条件で再現する指標だけを抽出し、NCC候補の実務的な評価順序を定める。
- 想定審査カテゴリ: `意識神経科学`, `医用信号解析`

#### 意識状態の分類（覚醒/睡眠/麻酔/DoC）

- 要旨叩き台: 公開EEGデータを用いて覚醒、睡眠段階、麻酔深度、意識障害群の識別を同一パイプラインで比較し、状態分類の再現可能性を評価する。重要視するのは最高精度ではなく、データセット外評価時の劣化、ラベル粒度の違い、信号品質の影響であり、臨床・基礎研究の双方で使える堅実な基準線モデルを整備する。
- 想定審査カテゴリ: `臨床神経科学`, `医用AI`

#### 統合情報理論(IIT)の実証的検証

- 要旨叩き台: 公開EEGの睡眠、麻酔、覚醒データに対し、複雑性指標、情報統合の近似量、ネットワーク分断度を計算し、意識水準の変化とどの程度整合するかを比較する。IIT全体の真偽を結論づけるのではなく、公開データで再現可能な近似指標の感度と限界を定量化し、理論検証に必要な追加計測条件を具体化する。
- 想定審査カテゴリ: `理論神経科学`, `生体信号解析`

#### Global Workspace Theory の検証

- 要旨叩き台: 公開EEGの知覚報告課題や注意操作課題を対象に、遅い広域成分、前頭頭頂結合、刺激後の全頭皮への拡散が報告成否や検出成功とどこまで対応するかを検証する。Global Workspace Theoryを包括的に証明するのではなく、課題依存性を明示したうえで、公開EEGだけで比較可能なイグニッション類似指標の頑健性を評価する。
- 想定審査カテゴリ: `認知神経科学`, `神経情報学`

#### 意識の連続性と同一性

- 要旨叩き台: 公開EEGの縦断測定、反復安静時、睡眠遷移データを用い、個人内で安定する特徴と状態変化で揺らぐ特徴を分離する。個人識別精度の高さをそのまま同一性の証拠とはみなさず、日差、課題差、睡眠段階差をまたいでも保持される成分の範囲を推定し、意識の連続性を論じるための最小限の実証基盤を整える。
- 想定審査カテゴリ: `意識研究`, `神経情報学`

#### mind-upload可能性の理論的枠組み

- 要旨叩き台: 公開EEGデータで追跡可能な個人差、状態差、再テスト安定性を整理し、デジタル再構成論で最低限必要となる情報要件を逆算する。実現可能性を直接主張するのではなく、EEGだけで保存できる特徴と失われる特徴を切り分け、どの粒度なら比較的堅い再現記述が可能かを示す理論枠組みを構築する。
- 想定審査カテゴリ: `神経情報学`, `理論神経科学`

## 28. 審査で来やすい論点

### 28.1 共通論点

- `新規性が弱いのでは` というコメントには、**新規アルゴリズム開発ではなく、公開EEG横断の benchmark commons を作る価値** で返す
- `ラベルや課題が揃っていない` というコメントには、**比較可能なサブ課題だけに絞ること、劣化幅そのものを成果とみなすこと** で返す
- `EEGだけで言い過ぎでは` というコメントには、**proxy 指標, state classification, stability 評価までに主張を限定する** ことで返す
- `公開データなので実験性が弱い` というコメントには、**統一split, calibration, negative result, cross-dataset 評価を含む再解析基盤の不足** を強調する
- `波及効果が見えにくい` というコメントには、制度カテゴリに応じて `医療`, `教育`, `BCI`, `標準化活動` へ言い換える

### 28.2 制度タイプ別に強調すべき点

| 制度タイプ | 審査が見がちな点 | 強調する返答軸 |
|---|---|---|
| `research_grant` | 新規性, 再現性, 方法の妥当性 | cross-dataset benchmark, fixed split, effect size, negative result |
| `award_or_prize` | 3か月で終わるか, 学生でも回るか | データ3本, 指標3個, 12週納品物を先に示す |
| `activity_grant` | 共同体性, 波及, 公開性 | benchmark commons, 研究会, 標準化ノート, wiki/CSV 公開 |
| `loan_or_finance` | 実装可能性, 事業化の接点 | portable, wearable, replay latency, UI/運用導線 |

### 28.3 Phase 4 で特に避けるべきこと

- `意識を解明する`, `理論を実証する`, `自己を復元する` のような決着表現
- `EEGだけで本人性を証明する` という含意
- `mind-upload 実現可能性を直接検証する` という書き方
- 代わりに、`proxy`, `boundary`, `stability`, `claim ladder`, `benchmark` という語に寄せる

## 29. 25トピック別 想定審査コメント・弱点・返答

### 29.1 Phase 1

#### EEG信号品質の限界検証

- 想定コメント1: 既存のQC研究との差分が弱く見える
- 想定コメント2: データセットごとに metadata が不均一で比較が崩れないか
- 弱点: `metadata_heterogeneity`
- 返答軸: 新規手法提案ではなく、公開EEG横断での品質閾値整理と再利用可能な監査基準の整備として位置づける

#### 高密度EEG空間分解能評価

- 想定コメント1: ground-truth が乏しく、空間分解能の結論を強く言えないのでは
- 想定コメント2: source localization の妥当性をEEGだけで判定し切れないのでは
- 弱点: `ground_truth_scarcity`
- 返答軸: 解剖学的真値の証明ではなく、電極数依存の利得と再現性の上限評価に限定する

#### マルチモーダル統合の基礎

- 想定コメント1: 同期誤差や欠測で融合効果が不安定ではないか
- 想定コメント2: EEG単独との差分が小さいと新規性が薄くならないか
- 弱点: `modality_alignment`
- 返答軸: 認知負荷推定や artifact 検出など限定課題で unimodal vs fusion を比較し、性能差だけでなく導入コストも報告する

#### ノイズ除去・信号分離手法の比較

- 想定コメント1: 正解信号が分からない以上、除去性能の比較は難しくないか
- 想定コメント2: 手法選択が恣意的だと結論が揺れないか
- 弱点: `artifact_label_mismatch`
- 返答軸: synthetic EEG と annotation 付き実測EEGを併用し、SNR だけでなく下流解析の安定性で比較する

#### 長時間記録の安定性評価

- 想定コメント1: 長時間になるほどラベル品質の劣化が混ざるのでは
- 想定コメント2: 睡眠と疲労を同時に扱うと解釈が曖昧ではないか
- 弱点: `session_protocol_gap`
- 返答軸: state family を分けて drift と欠損率を先に定量化し、長時間安定性を運用条件の問題として整理する

### 29.2 Phase 2

#### デコーディング精度ベンチマーク

- 想定コメント1: 既に多くのベンチマークがあるのでは
- 想定コメント2: MI と ERP と SSVEP を同列比較するのは不公平ではないか
- 弱点: `task_definition_mismatch`
- 返答軸: accuracy 競争ではなく、統一split, calibration, failure mode, compute cost を含む再現基盤として差別化する

#### クロスデータセット汎化

- 想定コメント1: ラベル空間やプロトコル差が大きすぎて比較困難ではないか
- 想定コメント2: 汎化低下が出るのは当然で、新規知見が薄くならないか
- 弱点: `label_space_mismatch`
- 返答軸: 対応するサブ課題だけを束ね、どの差分が劣化要因かを定量分解すること自体を成果に置く

#### リアルタイムデコーディング

- 想定コメント1: replay 評価では真のオンライン性を示せないのでは
- 想定コメント2: 実運用UIやデバイス制御まで繋がっていないのでは
- 弱点: `true_online_absence`
- 返答軸: 本研究は事前検証段階と明示し、遅延下限・窓長依存・誤警報率を示す前段 benchmark として出す

#### Foundation Modelの適用

- 想定コメント1: 公開EEG規模で foundation model と呼ぶのは誇大ではないか
- 想定コメント2: 課題差が大きく、表現学習の一般化が過剰に見えないか
- 弱点: `compute_and_label_bias`
- 返答軸: `foundation model` を避けて自己教師あり表現学習 baseline と呼び、OOD gap の限界を含めて報告する

#### 運動意図デコーディング

- 想定コメント1: MI decoding は既存研究が多く新規性が薄いのでは
- 想定コメント2: 被験者差が大きく、一般化の見通しが立たないのでは
- 弱点: `subject_shift`
- 返答軸: 被験者外性能と較正試行数削減に論点を絞り、リハビリ応用に向けた実務 benchmark として位置づける

#### 感覚知覚デコーディング

- 想定コメント1: ERP/P300 と SSVEP は別系統で、まとめると曖昧ではないか
- 想定コメント2: 刺激条件差が大きく横断比較が難しいのでは
- 弱点: `protocol_variation`
- 返答軸: ERP 系と SSVEP 系をサブ群に分け、共通 metric のみ横串比較する設計にする

#### 言語/意味デコーディング

- 想定コメント1: EEGで言語 decoding を主張するのは無理があるのでは
- 想定コメント2: imagined speech と semantic congruency を同列に扱えないのでは
- 弱点: `label_definition_gap`
- 返答軸: 文復元ではなく、カテゴリ分類と congruency 判定に限定し、成立条件の整理として出す

### 29.3 Phase 3

#### 感情状態の推定・分類

- 想定コメント1: 感情ラベルが主観依存でノイズが大きいのでは
- 想定コメント2: 被験者外・文化差で性能が崩れやすいのでは
- 弱点: `subjective_label_noise`
- 返答軸: 精度最大化ではなく、session transfer と calibration を含む頑健性 benchmark として示す

#### 記憶のエンコーディング/検索

- 想定コメント1: encoding と retrieval が課題上で分離できていないのでは
- 想定コメント2: 効果量が小さく再現性が低いのでは
- 弱点: `retrieval_label_sparsity`
- 返答軸: WM と retrieval proxy に絞り、事象関連成分と longitudinal drift を中心に限定主張で返す

#### 注意・ワーキングメモリ

- 想定コメント1: attention と workload が混同されやすいのでは
- 想定コメント2: 単チャネル条件では応用性が限られないか
- 弱点: `task_scale_mismatch`
- 返答軸: task family を分けた上で、軽量条件は lower bound、マルチチャネル条件は upper bound として整理する

#### 意思決定過程

- 想定コメント1: 意思決定という構成概念が広すぎないか
- 想定コメント2: 課題ごとに reward/risk の意味が違い比較しづらいのでは
- 弱点: `construct_ambiguity`
- 返答軸: 報酬・損失・不確実性の条件差に限定し、理論一般化ではなく condition contrast の再現性評価として出す

#### 社会的認知

- 想定コメント1: hyperscanning 系はサンプルが小さく不安定ではないか
- 想定コメント2: 社会的認知というラベルが広すぎるのでは
- 弱点: `sample_size_small`
- 返答軸: joint attention / social stress など狭い課題へ限定し、pilot 研究または活動助成向けに位置づける

#### 創造性・問題解決

- 想定コメント1: 創造性課題の採点が主観的で再現性が低いのでは
- 想定コメント2: exploratory に留まり、堅い結論が出にくいのでは
- 弱点: `low_reproducibility`
- 返答軸: trait の測定ではなく problem-solving process の proxy 探索として出し、探索研究であることを先に明示する

#### 主観的経験の定量化

- 想定コメント1: self-report の信頼性が低いと神経指標との対応も不安定ではないか
- 想定コメント2: 主観そのものを EEG に還元しているように見えないか
- 弱点: `annotation_variability`
- 返答軸: 主観の還元ではなく correspondence と限界測定を目的とし、近似可能な側面だけを報告する

### 29.4 Phase 4

#### 意識の神経相関（NCC）定量化

- 想定コメント1: proxy 指標の比較だけでは NCC と言い切れないのでは
- 想定コメント2: 覚醒・睡眠・麻酔を同一軸で比較するのは危うくないか
- 弱点: `proxy_overclaim`
- 返答軸: NCC の決着ではなく、state family ごとに再現する proxy の順位付けとして整理する

#### 意識状態の分類（覚醒/睡眠/麻酔/DoC）

- 想定コメント1: 臨床ラベルと研究ラベルの粒度差が大きいのでは
- 想定コメント2: 状態分類はデータセット外で急に落ちるのでは
- 弱点: `domain_shift`
- 返答軸: family 別に基準線を持ち、cross-dataset 劣化幅を主要成果として報告する

#### 統合情報理論(IIT)の実証的検証

- 想定コメント1: 複雑性 proxy を計算しても IIT の検証にはならないのでは
- 想定コメント2: 理論の射程に対してEEG指標が粗すぎるのでは
- 弱点: `theory_overreach`
- 返答軸: IITそのものの真偽ではなく、理論が要請する proxy 群の挙動比較と限界整理に限定する

#### Global Workspace Theory の検証

- 想定コメント1: P300 は GWT に固有ではないのでは
- 想定コメント2: report/no-report 課題の交絡が強いのでは
- 弱点: `proxy_definition_instability`
- 返答軸: GWT の証明ではなく、broadcast/ignition 類似指標の比較研究として出し、課題依存性も結果に含める

#### 意識の連続性と同一性

- 想定コメント1: EEG biometrics の安定性を本人性に読み替えていないか
- 想定コメント2: 縦断安定性だけでは同一性の議論に足りないのでは
- 弱点: `identity_overclaim`
- 返答軸: identity ではなく stability proxy と self-related feature の比較に限定し、哲学的主張を避ける

#### mind-upload可能性の理論的枠組み

- 想定コメント1: 理論整理だけで実証性が弱く見えないか
- 想定コメント2: scope が広すぎて採択後の成果物が曖昧ではないか
- 弱点: `scope_inflation`
- 返答軸: claim ladder, dataset atlas, benchmark commons という具体的納品物を前に出し、活動助成寄りに設計する

## 30. 返答テンプレの短文集

- `新規性が弱い` への返答: 新規アルゴリズム提案ではなく、公開EEG横断の再現基盤が未整備である点を課題設定の中心に置いています
- `公開データ再解析だけでは弱い` への返答: 固定split, calibration, negative result, cross-dataset 劣化幅まで含めた比較は未整備で、再利用可能性に直接寄与します
- `EEGだけで言い過ぎでは` への返答: 本申請は本人性や理論決着を目指さず、proxy 指標と state boundary の検証可能部分に限定しています
- `波及が見えにくい` への返答: 成果物は benchmark, CSV, reproducible note として医療・教育・BCI の各文脈に転用可能です

## 31. 高リスクテーマの長文返答案

### Foundation Modelの適用

- 想定コメント: 公開EEG規模で foundation model と呼ぶのは誇大ではないか。改善がモデル規模の効果か事前学習の効果かも切り分けにくい
- 返答例: 本申請では `foundation model` という強い表現は採らず、公開EEGに対する自己教師あり表現学習の限定的評価として位置づけます。主張したいのは万能性ではなく、少量ラベル条件・被験者外条件・データセット外条件で既存基線より安定した表現が得られるかどうかです。重複監査と OOD gap を必須報告項目に置き、効く条件と効かない条件を両方示します。

### 言語/意味デコーディング

- 想定コメント: EEGだけで意味や内的言語を読んだと誤解されやすく、低次刺激特徴を拾っているだけではないか
- 返答例: 本研究のスコープは自由文復元や内的言語の完全解読ではなく、公開EEGで整列可能な語カテゴリ、N400 条件差、想起発話クラスの識別可能性に限定しています。意味の復元を主張するのではなく、どのラベル粒度なら被験者外でも再現し得るかを整理する benchmark として出し、刺激長や語彙頻度などの交絡は共変量として管理します。

### 社会的認知

- 想定コメント: 社会的認知というラベルが広すぎ、実際は報酬処理や情動反応を見ているだけではないか
- 返答例: 対象課題は fairness, trust, social evaluation など公開EEGで条件整理しやすい下位成分に限定します。社会的認知全体の説明を目指すのではなく、社会的手掛かりが入ったときに再現する FRN/P300 などの条件差を、非社会的条件との差として比較する設計です。したがって主張は pilot benchmark と再現性評価までに留まり、生態学的妥当性の限界も明示します。

### 意識の神経相関（NCC）定量化

- 想定コメント: EEG単独で NCC と呼ぶのは強すぎ、薬剤や病態や報告要件の交絡も大きい
- 返答例: 本申請は NCC の証明や理論決着を目的にせず、公開EEG上で再計算可能な複雑性・結合性・遷移指標の比較研究として定義しています。睡眠、麻酔、DoC を一括同一視するのではなく state family ごとに整理し、報告依存性の低いラベルを優先します。成果は「どの proxy がどの状態群で比較的安定か」という順位付けであり、強い ontological claim は置きません。

### 統合情報理論(IIT)の実証的検証

- 想定コメント: proxy は Φ そのものではなく、複雑性の低下は徐波化やノイズでも説明できるのではないか
- 返答例: 本研究は IIT の真偽を判定するものではなく、IIT整合的とされる proxy 群が公開EEGでどの程度一貫して状態差と対応するかを調べる限定的検証です。PCI-ST や複雑性指標の値だけで議論せず、スペクトル変化、信号品質、ラベル粒度を共変量として併記します。したがって結論は理論の証明ではなく、公開EEGで到達可能な proxy 検証の上限整理になります。

### Global Workspace Theory の検証

- 想定コメント: P300 は GWT 固有ではなく、report confound が強いのではないか
- 返答例: 本申請は GWT の全面検証ではなく、公開ERP課題で broadcast / ignition 類似パターンがどこまで再現するかを比較する研究です。利用可能なら no-report 条件を優先し、report 条件しかない場合も課題依存性を弱点として明示します。従って成果物は理論証明ではなく、GWT整合的 proxy の再現性表と失敗条件の整理です。

### 意識の連続性と同一性

- 想定コメント: EEG fingerprint の安定性をそのまま本人性へ読み替えているのではないか
- 返答例: このテーマで主張するのは本人性の証明ではなく、公開縦断EEGにおける個人内シグネチャの下限的安定性評価です。状態差、日差、課題差をまたいで残る成分と消える成分を分けて報告し、identity という哲学的語は避けて stability proxy と self-related feature という工学的表現に置き換えます。強い主張を封じること自体が採択可能性の条件だと考えています。

### mind-upload可能性の理論的枠組み

- 想定コメント: EEG分類から mind-upload 可能性へ飛躍しており、scope が広すぎるのではないか
- 返答例: この項目は実現可能性の主張ではなく、公開EEGで検証できる必要条件と停止条件の整理を目的とする活動設計です。成果物は claim ladder, dataset atlas, benchmark commons の3点に限定し、何が検証可能で何が不可能かを明示すること自体を貢献とします。したがって、技術実証よりも標準化・研究形成・議論の交通整理に近い位置づけで出すのが安全です。

## 32. 採択率を上げる書き換え前後

### 32.1 基本ルール

| 通りにくい表現 | 通しやすい表現 |
|---|---|
| `解明する` | `比較する`, `評価する`, `再現性を検証する` |
| `復元する` | `分類可能性を測る`, `proxy を比較する` |
| `証明する` | `整合性を評価する`, `上限を整理する` |
| `実現する` | `前段条件を検証する`, `事前評価を行う` |
| `人格/自己/意味を読む` | `限定ラベルの識別条件を調べる` |
| `理論を実証する` | `理論整合的 proxy の挙動を比較する` |

### 32.2 代表例

| トピック | 通りにくい書き方 | 通しやすい書き換え |
|---|---|---|
| EEG信号品質の限界検証 | `EEGだけで脳計測の限界を証明する` | `公開EEG横断における信号品質指標の再現性評価` |
| デコーディング精度ベンチマーク | `公開EEGで最高精度を達成する` | `公開EEGデコーディング課題における統一ベンチマーク構築` |
| 言語/意味デコーディング | `思考や意味内容をEEGから読む` | `imagined speech EEG decoding の成立条件に関する比較研究` |
| 社会的認知 | `社会性をEEGだけで測定する` | `social stress と joint attention に関するEEG基礎評価` |
| 統合情報理論(IIT)の実証的検証 | `IITをEEGで証明する` | `EEG複雑性指標を用いた IIT proxy の再計算と比較` |
| 意識の連続性と同一性 | `本人性をEEGで証明する` | `縦断EEGによる個人内安定性と状態連続性の指標化` |
| mind-upload可能性の理論的枠組み | `mind-uploadの実現可能性をEEGで示す` | `EEGベース検証可能性のクレーム階段設計と benchmark commons` |

### 32.3 全25トピックを引く場所

- 全件の書き換え前後は `MindUpload-EEGDATA-FundMap-rewrite.csv` を使う
- 列は `hard_to_pass_framing`, `easier_to_pass_framing`, `danger_word`, `preferred_support_type`
- 面談前の修正では `danger_word` を先に確認すると事故が少ない
- より人手寄りの phrasing が欲しいときは `MindUpload-EEGDATA-FundMap-pitch-seeds.csv` の `hard_to_pass_curated`, `easier_to_pass_curated` を使う

## 33. 200字/400字/800字 要旨テンプレの使い方

### 33.1 約200字版

- 用途: 奨励金, エントリーシート, タイトル直下の概要
- 構成: `何を比較するか` + `どの公開EEGを使うか` + `主張をどこまでに制限するか`
- 書き方: 2文か3文で止め、データセット名は 0-2個までに抑える

### 33.2 約400字版

- 用途: 研究計画書の概要欄, 面談前配布メモ
- 構成: `背景ギャップ` + `方法` + `指標` + `成果物`
- 書き方: `固定前処理`, `被験者外分割`, `cross-dataset 評価`, `benchmark` の語を入れると守りが強い

### 33.3 約800字版

- 用途: 本申請の要旨欄, 面談で渡す詳細版
- 構成: `背景` + `既存の不足` + `方法` + `評価` + `主張制限` + `成果物`
- 書き方: 強い主張を避ける一文と、失敗条件も成果として扱う一文を必ず入れる

### 33.4 代表例

- 約200字の例: `本研究は公開EEG横断における信号品質指標の再現性評価を目的とし、公開EEGデータを横断してSNRを中心に比較する。主張はL0相当に限定し、再現可能な benchmark として成果を整理する。`
- 約400字の例: `本研究は公開EEG横断における信号品質指標の再現性評価を目的とする。EEG-DATA から整列可能な公開データを選び、固定前処理・被験者外分割・cross-dataset 評価を適用して、SNRを含む主要指標を比較する。公開EEGを用いてデバイス差と計測条件差を横断した品質指標を再計算し、SNRとartifact耐性の下限を benchmark として定量化する。強い理論主張ではなく再現範囲と失敗条件を明示する。`
- 約800字の例: `本研究は公開EEG横断における信号品質指標の再現性評価を目的とし、公開EEGデータの横断再解析によって検証可能なサブ問題を明確化する。具体的には EEG-DATA から課題定義を揃えられるデータを選定し、固定前処理、被験者外分割、必要に応じて cross-dataset 評価を適用する。主要評価は SNR、bad channel率、artifact除去前後の保存率とし、性能だけでなく calibration、失敗率、劣化幅も報告する。中心となる問いは、デバイス差と計測条件差を横断した品質指標がどこまで再現するかであるが、主張はL0相当に限定し、脳の完全読解のような表現は採らない。結果として、再現しやすい条件、破綻しやすい条件、次段階で追加計測が必要な論点を切り分け、research grant に提出可能な benchmark／短報／実務ノートとしてまとめる。`

### 33.5 全25トピックを引く場所

- 全件の字数別テンプレは `MindUpload-EEGDATA-FundMap-abstracts.csv` を使う
- 列は `abstract_200_template`, `abstract_400_template`, `abstract_800_template`
- まず `abstract_200_template` で骨格を決め、その後 `abstract_400_template` で method を足し、最後に `abstract_800_template` で主張制限と成果物を足すと崩れにくい
- 最初の1稿を早く作るときは `MindUpload-EEGDATA-FundMap-pitch-seeds.csv` の `abstract_200_curated` から始めるとよい

## 34. 制度タイプ別の1段落応募文テンプレ

### 34.1 `research_grant`

- テンプレ: `本研究は、[公開EEGデータ] を用いて [テーマ] に関する [検証項目] を再現可能な条件で検証し、その成立条件と限界を定量的に整理するものである。新規被験者募集や高額機器導入は行わず、公開データの範囲で前処理・評価指標・失敗条件を明示し、過大な性能主張を避けつつ、将来の関連研究に再利用可能な [成果物] を整備する。`
- 一言要約: `公開EEGデータだけで再現可能な検証基盤を整える、低リスクの研究助成案件`

### 34.2 `award_or_prize`

- テンプレ: `本件は、[公開EEGデータ] を用いた [テーマ] の継続的な再解析と成果公開を通じて、監査可能で再現可能な研究実践を積み上げてきた点をご評価いただくものである。新規性は大きな性能主張ではなく、手順の透明化、比較可能な評価表の整備、公開可能な [成果物] の蓄積にあり、受賞後も公開性と検証可能性を維持しながら着実に発展させる。`
- 一言要約: `公開EEGデータを用いた地道で再現可能な研究基盤整備への表彰案件`

### 34.3 `activity_grant`

- テンプレ: `本活動は、[公開EEGデータ] を題材に [テーマ] の再解析手順、注意点、評価基準を共有するための実践的な活動である。研究成果を誇張するのではなく、追試しやすい手順書、勉強会、公開資料として [成果物] を整備し、公開データを起点としたEEG研究の再現性向上と参加者の実務理解の底上げを目指す。`
- 一言要約: `公開EEGデータを使った再現性教育・共有基盤づくりの活動助成案件`

### 34.4 `loan_or_finance`

- テンプレ: `本件は、[公開EEGデータ] を用いた [テーマ] の既存研究基盤を継続運用するためのつなぎ資金として申請するものである。資金使途は、再解析環境の維持、成果公開、申請・報告対応など管理可能な範囲に限定し、新規被験者募集や高額設備投資は伴わない。短期に確認可能な [成果物] を積み上げる計画とし、返済または資金回収の見通しを明確にした運用を行う。`
- 一言要約: `公開EEGデータ基盤の継続運用を支える、使途限定の低リスク金融支援案件`

### 34.5 全25トピックを引く場所

- topic 別の制度向け文面は `MindUpload-EEGDATA-FundMap-fund-writing.csv` を使う
- 列は `research_grant_pitch`, `award_or_prize_pitch`, `activity_grant_pitch`, `loan_or_finance_pitch`, `reviewer_one_liner`
- 制度名がまだ曖昧でも、まず `preferred_support_type` 近辺の paragraph を下書きに使うと崩れにくい

## 35. 審査員向け一言要約の作り方

### 35.1 型

- `公開EEGデータだけで`
- `何を比較/評価するか`
- `強い主張を避けた守りの強いテーマ`

### 35.2 代表例

- `公開EEG横断で計測品質と再現性の下限を示す、守りの強い基盤テーマです`
- `公開EEGの被験者外・データセット外性能を benchmark として示す実装寄りテーマです`
- `高次認知を強く語らず、既存ラベル条件の再現範囲を整理する比較テーマです`
- `理論決着を避け、状態境界と proxy 指標の比較に限定した保守的テーマです`
- `実証可能域と停止条件を明文化する研究基盤整備テーマです`

## 36. 研究費の使い道テンプレ

### 36.1 基本原則

- 公開EEG前提なら、まず `計算資源`, `保存領域`, `再現実行`, `図表整備`, `公開・報告費` に寄せる
- `被験者募集費`, `大規模設備更新`, `高額機材ありき` の書き方は弱い
- 予算説明では `何を買うか` より `何を再現可能にするか` を前に出す

### 36.2 テーマ群別の強い書き方

| テーマ群 | 典型費目 | 通しやすい説明 | 通りにくい説明 |
|---|---|---|---|
| `measurement` | 計算資源, 保存領域, 可視化 | 品質監査と再現比較に必要な費用 | 機材を増やせば本質が解ける |
| `decoding` | GPU/クラウド, データ整列, baseline 再現 | 被験者外・データセット外比較のための費用 | 最高精度更新のための費用 |
| `higher_cognition` | 前処理・統計検証, ラベル整理, 比較資料 | 課題差をまたぐ保守的な効果量評価の費用 | 心の中身を読むための費用 |
| `consciousness` | 再解析計算, 状態整列, proxy 指標検証 | 状態境界と proxy 比較のための費用 | 意識の本質を解明するための費用 |
| `theory_commons` | 調査整理, wiki/CSV整備, 共有資料 | 検証可能域と停止条件を整理する費用 | mind-upload 実現を証明するための費用 |

### 36.3 金額帯の置き方

- `10万円前後`: ストレージ, クラウド計算, ラベル整理, 図表整備に集中
- `30万円前後`: cross-dataset 比較, 再現ノート, 短報化, 学会発表準備まで含める
- `100万円前後`: benchmark atlas, 共有資料, 研究会・会議発表, 維持ノートまで一体で組む

### 36.4 全25トピックを引く場所

- 予算テンプレは `MindUpload-EEGDATA-FundMap-budget.csv` を使う
- topic 別の紐付けは `MindUpload-EEGDATA-FundMap-fund-writing.csv` の `budget_template_key` を見る

## 37. 制度タイプ別 応募文3パターン

### 37.1 `research_grant`

- パターンA: `公開EEG横断の再現 benchmark を整備する研究`
- パターンB: `cross-dataset 比較で成立条件と失敗条件を切り分ける研究`
- パターンC: `proxy 指標と主張限界を整理する低リスク検証研究`

### 37.2 `award_or_prize`

- パターンA: `公開EEGを用いた継続的な再解析と成果公開の蓄積`
- パターンB: `学生主体で完結した再現研究と図表・短報の整備`
- パターンC: `公開可能な benchmark 資産を作った地道な研究実践`

### 37.3 `activity_grant`

- パターンA: `再解析手順・注意点・評価基準を共有する活動`
- パターンB: `勉強会・教材・公開資料を整備する再現性向上活動`
- パターンC: `benchmark commons を作るための共同研究形成活動`

### 37.4 `loan_or_finance`

- パターンA: `公開EEG再解析基盤の継続運用を支えるつなぎ資金`
- パターンB: `軽量推論や portable 条件の PoC 前評価を支える運用資金`
- パターンC: `成果公開と再解析環境維持に限定した低リスク資金`

## 38. 採択後の成果物一覧

### 38.1 `research_grant`

- benchmark 表
- 再現ノート
- 比較図表
- 短報または予稿

### 38.2 `award_or_prize`

- 図表付き short report
- 発表スライド
- 整理済み notebook
- 1ページ要約

### 38.3 `activity_grant`

- 手順書
- 勉強会資料
- 公開 wiki/CSV
- 共有用サマリー図

### 38.4 `loan_or_finance`

- 運用メモ
- 低遅延/軽量評価ノート
- 成果公開計画
- 次段申請用の材料

## 39. 口頭回答テンプレ

### 39.1 `research_grant`

- `公開EEGだけで再現可能な範囲に限定しており、強い理論主張は置いていません`
- `新規機器導入ではなく、比較可能な benchmark 基盤を作ることが主目的です`
- `失敗条件も成果として残す設計なので、再利用価値があります`

### 39.2 `award_or_prize`

- `3か月単位で図表と短報まで出せる、学生主体の再現研究として組んでいます`
- `派手な性能主張ではなく、透明な手順と公開可能な成果を重視しています`
- `受賞後も公開データを用いて継続的に積み上げられるテーマです`

### 39.3 `activity_grant`

- `個別性能よりも、追試しやすい手順と教材を残す活動として設計しています`
- `公開EEGを使うので参加者が手元で再現しやすいのが強みです`
- `研究会・共有資料・wiki整備までを成果物に含めています`

### 39.4 `loan_or_finance`

- `資金使途は再解析環境の維持と成果公開に限定しており、高額設備投資は伴いません`
- `公開EEGで成立条件を確認したうえで、低リスクのPoCに接続します`
- `短期に確認可能な成果物を積み上げる運用なので、見通しを説明しやすいです`

### 39.5 詳細版を引く場所

- 制度タイプ別の詳細は `MindUpload-EEGDATA-FundMap-support-playbook.csv` を使う
- 列は `application_pattern_1-3`, `strong_deliverable_1-3`, `deliverables`, `oral_answer_1-3`, `avoid_phrases`

## 40. 成果物の強い言い換えと避ける表現

### 40.1 `research_grant`

- 強い言い換え: `再現可能な検証基盤一式`
- 強い言い換え: `公開可能なデータ・解析コード・評価指標の成果パッケージ`
- 強い言い換え: `mind-upload ロードマップ上の技術ボトルネックを定量化した研究成果`
- 避ける表現: `まずは面白いので試してみたい`
- 避ける表現: `成果は論文が出れば十分`
- 避ける表現: `必要そうな経費を広めに計上している`

### 40.2 `award_or_prize`

- 強い言い換え: `研究の独立性と継続性を示す代表実績`
- 強い言い換え: `次段階の研究を加速する信用付き成果`
- 強い言い換え: `社会的信頼を可視化した到達点`
- 避ける表現: `評価してもらえたら励みになる`
- 避ける表現: `知名度を上げたい`
- 避ける表現: `受賞後の使い道は柔軟に考える`

### 40.3 `activity_grant`

- 強い言い換え: `共同研究と検証参加を生む実証の場`
- 強い言い換え: `記録・教材・導線まで残る活動成果パッケージ`
- 強い言い換え: `単発で終わらない公開アーカイブ型アウトプット`
- 避ける表現: `交流の場を作りたい`
- 避ける表現: `啓発したい`
- 避ける表現: `参加者に満足してもらえれば成功`

### 40.4 `loan_or_finance`

- 強い言い換え: `回収計画のある研究インフラ投資`
- 強い言い換え: `継続利用で単価を下げる生産基盤`
- 強い言い換え: `次の外部資金獲得までをつなぐ橋渡し資本`
- 避ける表現: `まず資金を確保してから考える`
- 避ける表現: `返済は採択次第`
- 避ける表現: `必要そうなものを一通り買いたい`

## 41. 審査書類向けの硬い版 / 面談向けの柔らかい版

### 41.1 `research_grant`

| 用途 | テンプレ |
|---|---|
| 書類向け | `本研究は、公開EEGデータの横断再解析を通じて、比較可能な benchmark と再現条件を整備し、[テーマ] に関する成立条件と限界を定量的に整理する。新規被験者募集や高額設備導入は行わず、固定前処理・被験者外分割・cross-dataset 評価を明示した再利用可能な成果パッケージを整備する。` |
| 面談向け | `やることは、公開EEGを同じ条件で比べて、どこまで再現するかを先に固めることです。派手な主張ではなく、後続の研究や申請で使い回せる benchmark を残します。` |

### 41.2 `award_or_prize`

| 用途 | テンプレ |
|---|---|
| 書類向け | `本件は、公開EEGデータを用いた継続的な再解析、評価表整備、成果公開を通じて、再現可能な研究実践を蓄積してきた点を評価いただくものである。新規性は単発の性能更新ではなく、透明な手順、比較可能な図表、公開可能な成果資産の継続的整備にある。` |
| 面談向け | `評価してほしいのは発想だけではなく、公開EEGで地道に再現して、図表と短報まで積み上げてきた実行力です。この賞を次の研究展開の加速材にしたいです。` |

### 41.3 `activity_grant`

| 用途 | テンプレ |
|---|---|
| 書類向け | `本活動は、公開EEGデータを題材として、[テーマ] に関する再解析手順、注意点、評価基準を共有し、追試可能な教材・資料・公開アーカイブを整備するものである。活動成果は単発イベントではなく、共同研究形成と再現性向上に資する共有基盤として残す。` |
| 面談向け | `イベントを開いて終わりではなく、手順書と資料と記録を残して、次の共同研究に繋がる形にします。公開EEGなので参加者も手元で追試しやすいです。` |

### 41.4 `loan_or_finance`

| 用途 | テンプレ |
|---|---|
| 書類向け | `本件は、公開EEG再解析基盤の継続運用と成果公開を支えるつなぎ資金として申請するものである。資金使途はクラウド計算、保存環境、成果公開、申請・報告対応に限定し、高額設備投資や新規被験者募集は伴わない。短期に確認可能な PoC 成果を積み上げ、次段の外部資金獲得に接続する。` |
| 面談向け | `不足分の穴埋めではなく、止めずに回し続けるための橋渡し資金です。公開EEGで成立条件を先に確認して、次の助成や共同研究を取りに行くスピードを確保します。` |

## 42. 使い分けルール

### 42.1 書類向けの硬い版で入れるもの

- `固定前処理`, `被験者外分割`, `cross-dataset 評価`, `benchmark`, `再利用可能`
- `成立条件`, `限界`, `失敗条件`, `成果パッケージ`
- 名詞中心で書き、願望より設計を前に出す

### 42.2 面談向けの柔らかい版で入れるもの

- `何を先に確かめるか`
- `何を残すか`
- `なぜ低リスクか`
- 1文目で要点、2文目で成果物、3文目で次段資金や共同研究への接続を言うと通りやすい

### 42.3 切り替えるときの注意

- 書類向けで `面白い`, `挑戦的`, `夢がある` に寄せすぎない
- 面談向けで名詞を積みすぎて読み上げ原稿にしない
- どちらでも `証明する`, `解明する`, `実現する` は避け、`比較する`, `整備する`, `整理する` に寄せる

### 42.4 詳細版を引く場所

- 制度タイプ別の hard/soft 切替は `MindUpload-EEGDATA-FundMap-dual-tone.csv` を使う
- 列は `hard_application`, `soft_application`, `hard_deliverable`, `soft_deliverable`, `hard_budget`, `soft_budget`, `tone_rule`

## 43. 想定質問50本と30秒回答集

### 43.1 `research_grant` の代表質問

- Q: なぜ新規実験ではなく公開EEGだけで十分なのか  
  A: 本申請の目的は新規記録ではなく、公開EEG横断で再現条件と失敗条件を benchmark として整理することです。固定前処理と被験者外評価を揃えるだけでも未整備部分が大きく、次段の実験設計に直接効きます。
- Q: 新規性はどこにあるのか  
  A: 新規アルゴリズムではなく、公開EEGを同一条件で比べる再現基盤の整備に新規性があります。個別論文の数値を並べるのではなく、cross-dataset 条件まで含めて比較可能にします。
- Q: うまく性能が出なかったら何が残るのか  
  A: 失敗条件そのものが成果です。どの条件で崩れるかが分かれば、次の大型資金や共同研究で無駄な探索を減らせます。

### 43.2 `award_or_prize` の代表質問

- Q: なぜ賞や奨学の対象として評価されるべきか  
  A: 着想よりも、公開EEGを使って再現可能な成果を継続的に積み上げてきた実行力を評価していただきたいです。図表、短報、整理済み notebook まで残している点が強みです。
- Q: 受賞後の資金や副賞は何に使うのか  
  A: 成果公開、英文校閲、小規模計算資源、発表整備に限定して使います。受賞実績を次段の申請や連携に繋げるための整備費と考えています。
- Q: 学生主体性はどこにあるのか  
  A: テーマ設定、再解析、図表化、短報化までを学生主導で完結できる形にしています。公開EEG前提なので、主体的に回せる範囲が明確です。

### 43.3 `activity_grant` の代表質問

- Q: この活動は単発で終わらないのか  
  A: 終わらせません。手順書、配布資料、録画、wiki、再現用 CSV を残し、参加後に各自が追試できる形まで成果物に含めます。
- Q: 研究会や勉強会をやる意味は何か  
  A: 公開EEGは参加者が手元で再現しやすいので、教材化と共同研究形成に向いています。活動を通じて benchmark commons を広げるのが狙いです。
- Q: 活動成果はどう測るのか  
  A: 開催回数ではなく、資料公開数、再現手順の整備、参加後の実装・連携・次段申請への接続件数で見ます。

### 43.4 `loan_or_finance` の代表質問

- Q: なぜ融資や金融支援が必要なのか  
  A: 資金不足の穴埋めではなく、公開EEG再解析基盤を止めずに回し、次段の助成獲得まで繋ぐ橋渡し資金だからです。使途は計算、保存、公開、申請対応に限定します。
- Q: 返済や回収の見通しはどう考えるのか  
  A: 返済を希望で語らず、何に投資して何のコストを下げ、どの外部資金や連携に繋げるかで説明します。短期の成果物も先に設定します。
- Q: 大きな設備投資をしない理由は何か  
  A: 今回は成立条件の整理が目的で、高額設備は不要です。低リスク PoC と成果公開に絞るほうが、金融支援としても説明しやすいです。

### 43.5 全50本を引く場所

- 全件の質問集は `MindUpload-EEGDATA-FundMap-qa.csv` を使う
- 列は `support_type`, `question`, `answer_30s`, `intent_tag`, `avoid_point`
- 面談前は `support_type` で絞り、`intent_tag` で似た質問をまとめて練習すると効率がよい

## 44. 30秒回答の組み立て方

### 44.1 基本形

1. `結論`: 何をやるかを先に言う  
2. `根拠`: 公開EEG, 固定前処理, 被験者外評価など守りの条件を言う  
3. `着地`: benchmark, 短報, 共有資料, 次段申請への接続を言う  

### 44.2 崩れにくい型

- `本件は [大きい夢] ではなく、[公開EEGで検証可能な下位課題] を扱います`
- `方法は [固定前処理 / cross-dataset 比較 / proxy 比較] に限定します`
- `成果物は [benchmark / 図表 / 手順書 / 次段申請材料] として残します`

### 44.3 避けること

- 最初の一文で `解明する`, `証明する`, `実現する` を言わない
- 途中で `でも`, `ただ`, `まだ` を重ねて弱くしすぎない
- 30秒回答でデータセット名を3個以上並べない

## 45. 模擬面談の台本

### 45.1 `research_grant` 向け

- 面接官: この申請で何をやるのか
- 申請者: `mind-upload` の大きい主張を直接扱うのではなく、公開EEGで検証可能な下位課題を横断比較します。固定前処理と被験者外評価を揃え、どの条件で再現しやすく、どこで崩れるかを benchmark として整理します。
- 追質問: 新規性は何か
- 申請者: 個別論文の最高性能を追うのでなく、公開EEGを同条件で並べる再現基盤を作る点です。性能が伸びなくても、失敗条件と使える proxy を残せるので次段の実験設計に直接効きます。
- 締めの一言: 12週間で比較表、再現 notebook、短報ドラフトまで出し、次段の大型申請や共同研究に繋げます。

### 45.2 `award_or_prize` 向け

- 面接官: なぜ受賞対象として評価されるべきか
- 申請者: 発想の大きさより、公開EEGを使って再現可能な成果を継続的に積み上げる実行力を見ていただきたいです。題目、図表、再解析、短報、wiki までを自分で閉じられる点が強みです。
- 追質問: 受賞後に何を前進させるのか
- 申請者: 成果公開、英文校閲、小規模計算資源、発表整備に使い、公開EEG benchmark を外部に見える形にします。個人の受賞実績で終わらせず、次段申請と共同研究の入口に変えます。
- 締めの一言: 受賞後3か月で公開資料一式と短い成果報告を出し、継続可能性を示します。

### 45.3 `activity_grant` 向け

- 面接官: 活動助成として何を残すのか
- 申請者: 公開EEGを題材にした再現ハンズオンと小規模勉強会を運営し、参加者が各自で追試できる教材を残します。単発イベントではなく、手順書、配布資料、録画、CSV、wiki を残して再利用可能な形にします。
- 追質問: 成果は開催回数以外でどう測るのか
- 申請者: 資料公開数、追試完了件数、派生実装数、次段の共同研究や申請への接続件数で見ます。参加者がその場で終わらず、自分の環境で再現できることを重視します。
- 締めの一言: 助成期間中に最低1本の教材パッケージと1回の公開成果共有を確実に出します。

### 45.4 `loan_or_finance` 向け

- 面接官: なぜ金融支援が必要なのか
- 申請者: 高額設備の購入ではなく、公開EEG再解析基盤を止めずに回すための橋渡し資金として必要です。計算、保存、公開、申請準備の小口コストに限定し、次段助成の獲得確率を上げます。
- 追質問: 回収や返済の見通しはどう考えるのか
- 申請者: 希望ではなく成果物で説明します。短期では benchmark 表、再現コード、申請書ドラフトを出し、それを用いて外部助成や共同研究費に接続します。
- 締めの一言: 設備拡張ではなく低リスク PoC の継続に絞るので、用途と成果の対応を明確に示せます。

### 45.5 使い方

- 最初の練習では `面接官`, `申請者`, `追質問`, `締めの一言` の4ブロックだけ読む
- 2回目以降は `追質問` を別制度タイプに差し替えても崩れないか確認する
- 強く言いすぎる箇所が出たら `比較する`, `整備する`, `共有する` に言い換える

### 45.6 詳細版を引く場所

- 模擬面談の1行版は `MindUpload-EEGDATA-FundMap-mock-interviews.csv` を使う
- 列は `support_type`, `script_name`, `scene`, `interviewer_prompt`, `applicant_answer`, `followup_prompt`, `closing_line`

## 46. 1分版 / 3分版の口頭説明テンプレ

### 46.1 `research_grant`

- 1分版: 本件では `mind-upload` 全体を直接証明するのではなく、公開EEGで検証可能な下位課題を横断比較します。固定前処理、被験者外評価、cross-dataset 比較を揃えて、何が再現しやすく何が崩れるかを benchmark として整理します。まず12週間で比較表、再現 notebook、短報ドラフトを出し、次段の実験提案に繋げます。
- 3分版: 研究の焦点は大きい理論主張ではなく、公開EEGで再解析できる proxy 課題の成立条件です。データセット依存の見かけ上の性能を避けるため、前処理を固定し、被験者外評価と cross-dataset 比較を中心に置きます。成果物は性能表だけでなく、失敗条件、再現 notebook、手順書、短報ドラフトです。これにより、次段で新規実験をやるべき条件と、まだ公開EEGで詰めるべき条件を切り分けられます。

### 46.2 `award_or_prize`

- 1分版: 私の強みは大きい主張を語ることではなく、公開EEGを使って再現可能な成果を継続して出せることです。題目整理、再解析、図表化、短報、wiki 整備までを一人で閉じ、失敗条件も成果として残します。受賞後は成果公開と発表整備を進め、次段の申請と共同研究に接続します。
- 3分版: 受賞対象として伝えたいのは、着想の派手さよりも実装と公開の継続性です。公開EEGを使えば、新規測定を待たずに再解析、比較表、図表、短報まで自分で回せます。私は `mind-upload` のうち EEG で扱える下位課題を切り出し、過大主張を避けながら成果物を積み上げる方針を取っています。受賞後はその成果を公開資料、発表、次段申請に変換し、個人の受賞で終わらない形にします。

### 46.3 `activity_grant`

- 1分版: 活動助成では、公開EEGを使った再現ハンズオンを実施し、参加者が各自で追試できる教材パッケージを残します。単発イベントではなく、配布資料、録画、CSV、wiki を整え、終了後も使える形にします。成果は開催回数でなく、追試完了件数と次段の連携件数で測ります。
- 3分版: 公開EEGは、学習者が同じデータに触れながら再解析手順を共有できるため、活動助成と相性がよいです。本件では `mind-upload` に関係する下位課題を題材に、再現ハンズオン、資料公開、手順書整備を一体で進めます。参加者がその場で終わらず、後から手元環境で追試し、派生実装や共同研究に進める状態を成果物とみなします。期間中は教材一式と公開共有の場を少なくとも1セット残します。

### 46.4 `loan_or_finance`

- 1分版: 金融支援が必要な理由は、高額設備ではなく、公開EEG再解析を止めずに回すための橋渡し資金だからです。用途は計算、保存、公開、申請準備に限定し、短期で benchmark 表と再現コードを出します。それを使って外部助成や共同研究費への接続を早めます。
- 3分版: 本件は大規模設備投資ではなく、低コストで進められる公開EEG再解析基盤の継続が目的です。必要なのは計算資源、保存、公開環境、申請準備といった小口費用で、支出と成果物の対応を明確にできます。短期では比較表、再現 notebook、申請書ドラフトを出し、その成果を使って次段の助成獲得確率を上げます。金融支援は研究の夢を語るためでなく、止めずに回すための橋渡しとして説明します。

### 46.5 話し方の実務ルール

- 1分版では `何をやるか`, `なぜ公開EEGで十分か`, `何を残すか` の3点だけを残す
- 3分版では `守りの条件`, `成果物`, `次段接続` を足す
- どちらでもデータセット名の列挙より `固定前処理`, `被験者外評価`, `cross-dataset 比較` を先に言う
- 最後の一文は `大型の夢` ではなく `次の申請や共同研究にどう繋ぐか` で閉じる

### 46.6 詳細版を引く場所

- 口頭説明テンプレの1行版は `MindUpload-EEGDATA-FundMap-oral-scripts.csv` を使う
- 列は `support_type`, `purpose`, `script_1min`, `script_3min`, `opening_hook`, `closing_hook`, `avoid_point`

## 47. 逆質問テンプレ

### 47.1 `research_grant`

- 逆質問1: 今回の制度では、`性能の高さ` と `再現基盤の整備` のどちらをより強く評価されますか
- 逆質問2: 公開EEGを使う提案では、短期成果物として `benchmark 表`, `再現 notebook`, `短報ドラフト` のうち何が最も評価されやすいですか
- 逆質問3: 次段で新規実験を提案するとき、今回の成果として最低限必要な比較条件は何でしょうか

### 47.2 `award_or_prize`

- 逆質問1: 受賞審査では `テーマの将来性` と `ここまでの実行力` のどちらに重みがありますか
- 逆質問2: 公開資料や再現 notebook のような地道な成果物は、どの程度評価対象になりますか
- 逆質問3: 受賞後3か月で見せる成果として、発表・短報・資料公開のどれが最も期待されていますか

### 47.3 `activity_grant`

- 逆質問1: この制度では `参加者数` と `参加後の追試継続` のどちらをより重視されますか
- 逆質問2: ハンズオン型の活動で、録画・手順書・CSV のどれが最も再利用価値として見られますか
- 逆質問3: 次年度以降につながる活動として評価されるには、共同研究化と教材公開のどちらがより重要でしょうか

### 47.4 `loan_or_finance`

- 逆質問1: 橋渡し資金として説明する場合、短期成果物と次段資金接続のどちらをより明確に示すべきですか
- 逆質問2: 小口費用の内訳では、計算資源・保存・公開環境のうちどこが最も納得されやすいですか
- 逆質問3: 回収可能性の説明では、外部助成見込みと共同研究形成のどちらが重視されますか

### 47.5 逆質問の使い方

- 逆質問は `相手に教えてもらう` 形にし、自己主張の延長にしない
- 3問全部は使わず、面談の流れに合わせて1問か2問に絞る
- `何を重視しますか`, `どこを見ますか`, `何が最低限必要ですか` の形にすると崩れにくい

### 47.6 避ける逆質問

- `採択率はどのくらいですか`
- `通りやすい書き方を教えてください`
- `他の応募者より有利ですか`
- `今回ダメでも次回ありますか`

### 47.7 詳細版を引く場所

- 逆質問テンプレの1行版は `MindUpload-EEGDATA-FundMap-reverse-questions.csv` を使う
- 列は `support_type`, `question_1`, `question_2`, `question_3`, `intent`, `avoid_point`

## 48. 面談後フォローメール草案

### 48.1 共通ルール

- 当日か翌営業日までに送る
- `お礼`, `1行要約`, `面談で話した成果物`, `必要なら補足資料` の順に並べる
- 新しい主張を増やさず、面談で話した守りの条件を短く再確認する

### 48.2 `research_grant`

- 件名例: 面談のお礼 `公開EEG benchmark 整備提案`
- 本文例: 本日は面談のお時間をいただきありがとうございました。公開EEGを用いた固定前処理・被験者外評価・cross-dataset 比較により、`mind-upload` 関連の下位課題について成立条件と失敗条件を整理する方針をご説明しました。短期成果物として比較表、再現 notebook、短報ドラフトを12週間で整える計画です。必要でしたら、評価条件一覧と候補データセット表をお送りします。引き続きよろしくお願いいたします。

### 48.3 `award_or_prize`

- 件名例: 面談のお礼 `公開EEG再解析の継続成果について`
- 本文例: 本日は面談の機会をいただきありがとうございました。公開EEGを用いて題目整理、再解析、図表化、短報化までを継続して進めている点をご説明しました。受賞後は成果公開、英文校閲、発表整備を進め、個人の実績で終わらず次段申請と共同研究に接続する計画です。必要でしたら、公開済み資料と再現用 notebook の一覧をお送りします。引き続きよろしくお願いいたします。

### 48.4 `activity_grant`

- 件名例: 面談のお礼 `公開EEG再現ハンズオン計画`
- 本文例: 本日は面談のお時間をいただきありがとうございました。公開EEGを題材にした再現ハンズオンと教材整備を通じて、参加者が各自で追試できる状態を残す計画をご説明しました。成果は参加者数でなく、配布資料、録画、CSV、wiki、追試完了件数で確認します。必要でしたら、教材構成案と実施後に残す成果物一覧をお送りします。引き続きよろしくお願いいたします。

### 48.5 `loan_or_finance`

- 件名例: 面談のお礼 `公開EEG再解析基盤の橋渡し資金`
- 本文例: 本日は面談のお時間をいただきありがとうございました。高額設備ではなく、公開EEG再解析基盤を止めずに回すための橋渡し資金として、計算、保存、公開、申請準備の小口費用に限定して使う方針をご説明しました。短期では比較表、再現 notebook、申請書ドラフトを整え、次段の助成や共同研究費への接続を進めます。必要でしたら、費目内訳案と短期成果物一覧をお送りします。引き続きよろしくお願いいたします。

### 48.6 詳細版を引く場所

- フォローメール草案の1行版は `MindUpload-EEGDATA-FundMap-followup-mails.csv` を使う
- 列は `support_type`, `subject_template`, `opening_line`, `summary_line`, `deliverable_line`, `attachment_offer`, `closing_line`, `avoid_point`

## 49. 5分版の口頭説明テンプレ

### 49.1 `research_grant`

- 5分版: 本件で扱うのは `mind-upload` 全体の直接証明ではなく、公開EEGで検証可能な下位課題の成立条件です。第一に、公開EEGごとに評価条件がばらつくと見かけ上の性能差が大きくなるため、固定前処理と被験者外評価を揃えます。第二に、単一データセットでの当てはまりを避けるため、cross-dataset 比較を基本に置きます。第三に、性能が高いかどうかだけでなく、どの条件で崩れるか、どの proxy が比較的安定するかを成果として残します。短期では比較表、再現 notebook、手順書、短報ドラフトを整え、次段で新規実験をやるべき論点と、まだ公開EEGで詰めるべき論点を切り分けます。この提案の価値は派手な主張ではなく、再現性のある基盤を先に作ることにあります。

### 49.2 `award_or_prize`

- 5分版: 受賞対象として伝えたいのは、大きいビジョンそのものより、公開EEGを使って再現可能な成果を継続して出せる実行力です。私は `mind-upload` に関わる大きい問いをそのまま語るのではなく、EEGで扱える下位課題へ切り分け、題目整理、再解析、図表化、短報化、wiki整備までを閉じる形で進めています。公開EEGを使うことで、新規測定を待たずに失敗条件も含めて成果物にできます。受賞後は成果公開、英文校閲、発表整備に資源を使い、個人の実績で終わらず、次段の助成申請や共同研究形成につなげます。評価していただきたいのは、夢を大きく語ることではなく、守りの条件を置きながら着実に成果物を積む姿勢です。

### 49.3 `activity_grant`

- 5分版: 活動助成としては、公開EEGを使った再現ハンズオンと教材整備を一体で進める計画です。公開EEGは全員が同じ素材に触れられるので、勉強会やワークショップの題材として再利用しやすい利点があります。本件では `mind-upload` に関連する下位課題を題材に、固定前処理、簡易評価、図表作成までを参加者が追試できる教材に落とします。成果は開催回数ではなく、配布資料、録画、CSV、wiki、追試完了件数、派生実装数で測ります。期間中に少なくとも1つの教材パッケージと1回の公開共有を残し、終了後も各自が同じ手順で再現できることを重視します。活動の価値はイベント実施そのものではなく、再利用可能な学習基盤を残す点にあります。

### 49.4 `loan_or_finance`

- 5分版: 金融支援として説明する場合、本件は高額設備投資ではなく、公開EEG再解析基盤を止めずに回すための橋渡し資金です。必要なのは計算資源、保存、公開環境、申請準備といった小口費用で、用途と成果物の対応を明確にできます。研究内容としては、`mind-upload` のうち公開EEGで検証可能な下位課題に絞り、固定前処理、被験者外評価、cross-dataset 比較を中心に benchmark を整備します。短期では比較表、再現 notebook、手順書、申請書ドラフトを出し、その成果を用いて外部助成や共同研究費への接続を進めます。返済や回収の説明も希望ではなく、何に投資し、どのコストを下げ、どの次段資金につなぐかで示します。つまり、夢を広げるための資金ではなく、低リスクのPoCを継続するための資金として位置付けます。

### 49.5 5分版の組み立て方

1. `対象の限定`: EEGで扱える下位課題に絞る  
2. `守りの条件`: 固定前処理, 被験者外評価, cross-dataset 比較を置く  
3. `成果物`: 比較表, notebook, 手順書, 短報, 教材などを言う  
4. `次段接続`: 新規実験, 次段申請, 共同研究への接続で閉じる  

### 49.6 詳細版を引く場所

- 5分版テンプレの1行版は `MindUpload-EEGDATA-FundMap-oral-scripts-5min.csv` を使う
- 列は `support_type`, `purpose`, `script_5min`, `opening_hook`, `middle_anchor`, `closing_hook`, `avoid_point`

## 50. 審査員タイプ別の刺さる言い換え

### 50.1 再現性重視型

- 刺さる言い方: `公開EEG横断で固定前処理と被験者外評価を揃え benchmark を整備する`
- 弱い言い方: `最高性能を出して mind-upload の核心を解明する`
- 先に置く要素: `比較可能性`, `失敗条件`, `再現 notebook`
- 閉じ方: `失敗条件も次段実験の設計材料として残す`

### 50.2 遂行力重視型

- 刺さる言い方: `12週間で比較表, notebook, 短報ドラフトを出す`
- 弱い言い方: `まず挑戦的に広く探索してみる`
- 先に置く要素: `短期成果物`, `工程の固定`, `やらない範囲`
- 閉じ方: `小さく閉じて次段申請に接続する`

### 50.3 将来性重視型

- 刺さる言い方: `公開EEGで小さく確実に積み上げられるテーマに限定する`
- 弱い言い方: `一気に大発見へつなげる`
- 先に置く要素: `継続性`, `次の成長余地`, `公開資料化`
- 閉じ方: `今回の成果を次段の助成と共同研究の入口にする`

### 50.4 教育・公共性重視型

- 刺さる言い方: `参加者が各自で追試できる教材と手順書を残す`
- 弱い言い方: `面白いイベントを開催する`
- 先に置く要素: `教材`, `録画`, `CSV`, `wiki`
- 閉じ方: `単発で終わらず再利用可能な形にする`

### 50.5 財務・保守重視型

- 刺さる言い方: `高額設備ではなく橋渡し資金として小口費用に限定する`
- 弱い言い方: `研究の夢に投資してほしい`
- 先に置く要素: `費目の限定`, `短期成果物`, `次段資金への接続`
- 閉じ方: `用途と成果の対応を明確に示す`

### 50.6 実務ルール

- 内容を変えずに `何を先に言うか` だけ変える
- 再現性重視型には `条件統一` を先頭に置く
- 遂行力重視型には `12週間で何を出すか` を先頭に置く
- 将来性重視型には `無理のない成長曲線` を先頭に置く
- 教育・公共性重視型には `残る教材` を先頭に置く
- 財務・保守重視型には `用途の限定` を先頭に置く

### 50.7 詳細版を引く場所

- 審査員タイプ別の1行版は `MindUpload-EEGDATA-FundMap-reviewer-tone.csv` を使う
- 列は `support_type`, `reviewer_type`, `strong_framing`, `weak_framing`, `opening_line`, `closing_line`, `avoid_point`

## 51. 不採択後の再申請テンプレ

### 51.1 まずやること

- コメントを `範囲が広い`, `成果物が弱い`, `費目が弱い`, `実行力が見えない` の4種類に分ける
- 直すのは `最初の3文`, `成果物一覧`, `予算説明`, `タイトル` の順にする
- 1回目で全部直そうとせず、まず `何を削るか` を決める

### 51.2 よくある不採択理由の翻訳

- `壮大すぎる`: EEGで扱える下位課題へ切り直せという意味
- `新規性が不明`: 新しい理論より比較可能な再現基盤を示せという意味
- `実現可能性が弱い`: 12週間成果物と前処理固定を明示せという意味
- `予算の妥当性が弱い`: 費目と成果物の対応を1対1で示せという意味

### 51.3 再申請の冒頭テンプレ

- `research_grant`: 前回申請では対象範囲が広く短期成果物の明確さが不足していたため、今回は公開EEGで検証可能な下位課題に対象を限定し、固定前処理・被験者外評価・cross-dataset 比較に基づく benchmark 整備へ再構成した。
- `award_or_prize`: 前回申請では将来像が前に出すぎていたため、今回は公開EEGを用いた題目整理、再解析、図表化、短報化といった継続成果を中心に構成し直した。
- `activity_grant`: 前回申請では活動の継続性が弱かったため、今回は教材、録画、CSV、wiki を残す再利用可能なハンズオン計画として整理し直した。
- `loan_or_finance`: 前回申請では資金使途が広すぎたため、今回は計算、保存、公開、申請準備の小口費用に限定し、短期成果物との対応を明確にした。

### 51.4 再申請で足すべき証拠

- 比較表の試作1枚
- 再現 notebook の dry-run 1本
- 候補データセット一覧 1ページ
- 12週間工程表 1枚
- 費目と成果物の対応表 1枚

### 51.5 再申請時に削るべき表現

- `解明する`, `証明する`, `実現する`
- `革新的`, `世界初`, `唯一`
- `幅広く検討する`
- `必要に応じて進める`

### 51.6 詳細版を引く場所

- 再申請テンプレの1行版は `MindUpload-EEGDATA-FundMap-resubmission.csv` を使う
- 列は `support_type`, `common_rejection`, `rewrite_strategy`, `revised_opening`, `added_evidence`, `next_deliverable`, `avoid_point`

## 52. 制度別の提出書類チェックリスト

### 52.1 `research_grant`

- タイトル: `公開EEG`, `下位課題`, `benchmark`, `再現` のどれかが入っているか
- 要旨: `対象を限定したか`, `固定前処理`, `被験者外評価`, `短期成果物` が入っているか
- 予算: 計算資源, 保存, 公開, 校閲などが成果物に直結しているか
- 添付: 候補データセット表, 工程表, 比較指標一覧があるか

### 52.2 `award_or_prize`

- タイトル: `継続成果`, `実行力`, `再解析` の語感になっているか
- 要旨: 将来像より `ここまで出したもの` が前に来ているか
- 実績欄: 図表, notebook, wiki, 発表, 短報のどれを残したか明記したか
- 添付: 代表成果物 1-3 点に絞っているか

### 52.3 `activity_grant`

- タイトル: `ハンズオン`, `教材`, `公開`, `再現` の語感になっているか
- 要旨: 開催内容より `終了後に何が残るか` が前に来ているか
- 予算: 会場や備品より資料整備, 録画, 配布物, 公開基盤に重点があるか
- 添付: 教材構成案, 参加後の追試導線, 成果公開計画があるか

### 52.4 `loan_or_finance`

- タイトル: `橋渡し`, `基盤継続`, `公開EEG再解析` の語感になっているか
- 要旨: 資金難の説明でなく `何に使い何を出すか` が前に来ているか
- 予算: 小口費用ごとに成果物と対応づけたか
- 添付: 短期成果物一覧, 次段助成接続計画, 費目内訳があるか

### 52.5 最終確認の赤信号

- タイトルが大きすぎて EEG で扱える範囲を超えている
- 要旨に `何をやらないか` が書かれていない
- 予算説明が成果物ではなく希望や理想に寄っている
- データセット名ばかり並び、評価条件が見えない
- 添付資料が多すぎて代表成果物が埋もれている

### 52.6 詳細版を引く場所

- 提出前チェックの1行版は `MindUpload-EEGDATA-FundMap-document-checklist.csv` を使う
- 列は `support_type`, `title_check`, `abstract_check`, `budget_check`, `deliverable_check`, `attachment_check`, `final_red_flag`

## 53. 審査コメント別の1文修正版

### 53.1 `範囲が広すぎる`

- 修正前: `mind-upload の成立可能性を公開EEGから総合的に解明する`
- 修正後: `公開EEGで検証可能な下位課題に限定し benchmark と失敗条件を整理する`
- 直し方の芯: `全体像` を `下位課題` に落とし、`解明` を `整理` に変える

### 53.2 `新規性が見えにくい`

- 修正前: `既存手法を適用して性能向上を目指す`
- 修正後: `公開EEGを同一条件で比較可能にする再現基盤の整備を主成果とする`
- 直し方の芯: モデル新規性ではなく `比較可能性` を前に出す

### 53.3 `実現可能性が弱い`

- 修正前: `まず幅広く試しながら有望な方向を探索する`
- 修正後: `固定前処理と被験者外評価を先に固定し 12週間で比較表と再現 notebook を出す`
- 直し方の芯: `探索` を減らし `固定条件と期限` を入れる

### 53.4 `成果物が曖昧`

- 修正前: `知見を得て今後の研究に役立てる`
- 修正後: `比較表 手順書 notebook 短報ドラフトを残して次段申請に接続する`
- 直し方の芯: `知見` を具体物に置き換える

### 53.5 `予算の妥当性が弱い`

- 修正前: `研究を円滑に進めるため計算環境を整える`
- 修正後: `比較表と再現 notebook の作成に必要な計算 保存 公開費へ限定する`
- 直し方の芯: `環境整備` を `成果物に直結する費目` に置き換える

### 53.6 `公開データ頼みで浅い`

- 修正前: `公開データなので手軽に検証できる`
- 修正後: `公開EEG横断で前処理と評価条件を揃え 再現条件と崩壊条件を見極める`
- 直し方の芯: `手軽さ` を言わず `条件統一の価値` を言う

### 53.7 `活動がイベント止まり`

- 修正前: `勉強会を開いて議論を深める`
- 修正後: `勉強会で使った教材 録画 CSV wiki を残し 参加後の追試を可能にする`
- 直し方の芯: `開催` より `終了後に残るもの` を前に出す

### 53.8 `金融支援として夢寄り`

- 修正前: `将来の大きな研究展開のために資金を確保する`
- 修正後: `比較表と申請書ドラフトを止めずに出すための橋渡し資金として小口費用に限定する`
- 直し方の芯: `将来の夢` を `短期成果物` と `用途の限定` に変える

### 53.9 実務ルール

- 1文だけ直すなら `目的語を小さくする`
- 動詞は `解明する` より `比較する`, `整理する`, `整備する` を使う
- 終わりは `役立てる` で閉じず `何を残すか` で閉じる

### 53.10 詳細版を引く場所

- 1文修正版の一覧は `MindUpload-EEGDATA-FundMap-comment-rewrites.csv` を使う
- 列は `comment_type`, `bad_sentence`, `better_sentence`, `why_it_works`, `avoid_point`

## 54. 制度タイプ別の予算削減 fallback

### 54.1 基本原則

- 先に削るのは `広報の飾り`, `余白的な探索`, `説明しにくい雑費`
- 最後まで残すのは `比較条件を揃える最低限の計算`, `公開物作成`, `再現 notebook`, `短期成果物`
- 減額時ほど `何をやらないか` を明記する

### 54.2 `research_grant`

- 軽度減額: データセット数を絞っても `固定前処理 / 被験者外評価 / 比較表` は残す
- 中度減額: cross-dataset 比較を主要2条件に絞り `短報ドラフト` までを守る
- 重度減額: 新規比較軸を捨てて `1つの benchmark 表 + 1本の再現 notebook` に閉じる

### 54.3 `award_or_prize`

- 軽度減額: 発表機会を減らしても `公開資料と成果整理` は残す
- 中度減額: 英文校閲や外部発表を後ろ倒しし `図表と notebook 公開` を優先する
- 重度減額: 見せ方を最小化して `継続成果の可視化` だけ守る

### 54.4 `activity_grant`

- 軽度減額: 会場や配布物を削っても `教材と録画` は残す
- 中度減額: 開催回数を減らし `1回の高密度ハンズオン + 教材パッケージ` に寄せる
- 重度減額: 同期イベントを縮小して `非同期教材と追試導線` を主成果にする

### 54.5 `loan_or_finance`

- 軽度減額: 保存や公開の余裕分を削っても `比較表と申請書ドラフト` は守る
- 中度減額: 外部発表や追加検証を削り `橋渡しとして必要な最小費目` に絞る
- 重度減額: `止めないための計算 保存 申請準備` だけ残して短期接続を最優先する

### 54.6 減額時の言い方

- `縮小したが成立条件は守った`
- `比較軸を減らしたが評価条件は固定した`
- `件数を減らしたが成果物の形式は維持した`
- `外側を削って中核成果物を守った`

### 54.7 詳細版を引く場所

- 予算削減 fallback の一覧は `MindUpload-EEGDATA-FundMap-budget-fallback.csv` を使う
- 列は `support_type`, `cut_level`, `keep_first`, `cut_first`, `fallback_plan`, `strong_line`, `avoid_point`

## 55. 採択後30日 / 60日 / 90日の運用チェックリスト

### 55.1 30日

- `research_grant`: 前処理と評価条件を固定し 候補データセット表と工程表を確定する
- `award_or_prize`: 代表成果物を3点以内に絞り 履歴と図表の見せ方を固定する
- `activity_grant`: 教材構成案と追試導線を固め 録画や配布物の型を決める
- `loan_or_finance`: 小口費用の内訳と短期成果物の対応を1対1で確定する

### 55.2 60日

- `research_grant`: 比較表の初版と再現 notebook の dry-run を出す
- `award_or_prize`: 公開資料の初版と短い成果報告を整える
- `activity_grant`: 教材パッケージ初版と1回分の実施準備を完了する
- `loan_or_finance`: 比較表初版と次段申請ドラフトの骨子を作る

### 55.3 90日

- `research_grant`: 比較表 notebook 手順書 短報ドラフトを揃える
- `award_or_prize`: 代表成果物の公開と次段申請への接続文を揃える
- `activity_grant`: 教材公開 録画整理 追試完了件数の確認まで行う
- `loan_or_finance`: 短期成果物を公開し 次段助成または共同研究費への接続を開始する

### 55.4 共通の赤信号

- 30日で `評価条件` がまだ固定されていない
- 60日で `初版成果物` が1つも出ていない
- 90日で `外部に見える成果物` がない
- 作業ログはあるが `比較表 / notebook / 教材 / 申請骨子` のどれにも変換されていない

### 55.5 詳細版を引く場所

- 採択後運用の一覧は `MindUpload-EEGDATA-FundMap-post-award-ops.csv` を使う
- 列は `support_type`, `day_bucket`, `priority_1`, `priority_2`, `priority_3`, `artifact_to_leave`, `risk_watch`

## 56. 制度タイプ別の失敗例集

### 56.1 `research_grant`

- 失敗例1: `公開EEGで mind-upload 全体を実証する` と書き、評価条件を固定していない
- なぜ落ちるか: 対象が広すぎて、失敗しても何が残るのか見えない
- 直し方: `公開EEGで検証可能な下位課題`, `固定前処理`, `被験者外評価`, `比較表` を先に置く
- 失敗例2: データセット名を大量に並べるが、主要2条件の cross-dataset 比較に絞れていない
- なぜ落ちるか: 豊富さではなく比較設計の弱さとして読まれる
- 直し方: 件数を減らしても `比較条件の統一` を見せる

### 56.2 `award_or_prize`

- 失敗例1: 将来の夢を長く語り、ここまで出した図表や notebook が前に出ていない
- なぜ落ちるか: 受賞後の伸びしろ以前に、現在の実行力が見えない
- 直し方: `代表成果物 1-3点`, `継続成果`, `自分で閉じた工程` を先頭に置く
- 失敗例2: 実績を大量に列挙して焦点がぼける
- なぜ落ちるか: 強い1本がなく、何を評価すべきか分からない
- 直し方: 代表図表と短い成果報告に絞り、次段申請への接続で閉じる

### 56.3 `activity_grant`

- 失敗例1: `勉強会をやる`, `交流を促進する` で止まり、教材や録画の残し方がない
- なぜ落ちるか: 単発イベントにしか見えず、助成後に何が残るかが不明
- 直し方: `教材`, `録画`, `CSV`, `wiki`, `追試導線` を成果物として明記する
- 失敗例2: 参加人数だけを成果指標に置く
- なぜ落ちるか: 熱量は伝わっても、再利用性と持続性が評価できない
- 直し方: `追試完了件数`, `派生実装`, `次段連携` を指標に置く

### 56.4 `loan_or_finance`

- 失敗例1: `将来の大型研究のために資金が必要` とだけ書き、短期成果物がない
- なぜ落ちるか: 返済や回収の説明が希望的観測に見える
- 直し方: `比較表`, `再現 notebook`, `申請書ドラフト` など短期で出るものに落とす
- 失敗例2: 費目が広く、橋渡し資金なのか設備投資なのかが曖昧
- なぜ落ちるか: 何に使って何を残すかの対応が見えない
- 直し方: `計算`, `保存`, `公開`, `申請準備` の小口費用に限定する

### 56.5 共通の赤信号

- `やりたいこと` は多いのに `やらないこと` が書かれていない
- `成果` が抽象語で、比較表や notebook のような具体物になっていない
- `公開EEGを使う理由` が手軽さだけで、比較設計の価値になっていない
- `次段接続` が夢で終わり、次の申請や共同研究の入口になっていない

### 56.6 詳細版を引く場所

- 失敗例集の一覧は `MindUpload-EEGDATA-FundMap-failure-cases.csv` を使う
- 列は `support_type`, `failure_case`, `why_it_fails`, `repair_move`, `warning_sign`

## 57. 審査通過後の面談想定追加質問

### 57.1 `research_grant`

- Q: なぜその公開EEGを主要候補にしたのか  
  A: 課題設定, ラベル品質, 被験者数, 前処理の再現可能性が揃っているからです。件数を増やすより比較条件を揃えることを優先します。
- Q: negative result でも何が残るのか  
  A: 主要条件で崩れる場所が分かれば、次段で新規実験に回すべき論点が明確になります。比較表と失敗条件の整理自体が成果です。
- Q: 実施体制は足りるのか  
  A: 新規収集を前提にせず、固定前処理と再解析に限定しているため、現行体制で12週間成果物まで到達できます。

### 57.2 `award_or_prize`

- Q: どこまでが本人主導の成果か  
  A: 題目整理, 再解析, 図表化, 短報化, wiki 整備までを本人が閉じています。支援は補助線で、成果物の芯は自分で作っています。
- Q: 受賞後に何を一段進めるのか  
  A: 成果公開と発表整備を進め、代表図表と短い成果報告を外から見える形にします。そのまま次段申請へ接続します。
- Q: 受賞しなくても続くのか  
  A: 続きます。受賞は加速要因であり、公開EEGで回る最小成果物は自己資源でも継続できます。

### 57.3 `activity_grant`

- Q: 参加後に本当に追試されるのか  
  A: 追試導線を教材, CSV, 手順書に埋め込み、終了後に個別に追える形にします。回数より追試完了件数を見ます。
- Q: 活動成果は研究にどう戻るのか  
  A: 質問ログと派生実装を整理し、次段の申請書や共同研究テーマの論点表に変換します。
- Q: 実施規模を広げすぎないのか  
  A: 広げません。まず1回分の教材パッケージを完成させ、その再利用性を確認してから次を考えます。

### 57.4 `loan_or_finance`

- Q: 何が返済や回収の起点になるのか  
  A: 比較表や再現 notebook を使った次段助成申請、または小口の解析支援・共同研究費への接続です。希望ではなく接続点で説明します。
- Q: 借入がなくてもできる部分は何か  
  A: あります。借入は止めないための最小費用に限定し、なくても回る部分と借入が必要な部分を分けて示します。
- Q: どこで拡張を止めるのか  
  A: 評価条件が固定できない拡張、新規収集前提の拡張、説明しにくい費目は止めます。橋渡し資金として成立する範囲を越えません。

### 57.5 答え方の実務ルール

- 書類審査より一段具体的にするが、主張は広げない
- `なぜその設計か`, `失敗しても何が残るか`, `体制で回るか` の3点に戻す
- 質問が広くても `公開EEGで扱える範囲` に引き戻す

### 57.6 詳細版を引く場所

- 通過後QAの一覧は `MindUpload-EEGDATA-FundMap-post-pass-qa.csv` を使う
- 列は `support_type`, `question`, `what_they_are_really_asking`, `answer_axis`, `avoid_point`

## 58. 共同研究打診メールの初稿

### 58.1 共通ルール

- 1通目では `大きい夢` を語らず `小さく一緒にできること` を示す
- 送る情報は `何を見たか`, `何を一緒にやりたいか`, `こちらが先に出せるもの` の順にする
- 添付は `比較表 1枚`, `候補データセット表`, `短いメモ` 程度に絞る

### 58.2 解析協力者 / 研究室向け

- 件名例: 公開EEG横断比較の小規模共同検討のお願い
- 初稿例: 突然のご連絡失礼します。公開EEGを用いた固定前処理・被験者外評価の比較基盤を整備しており、貴研究室の関連テーマを拝見してご連絡しました。`mind-upload` 全体を扱うのでなく、EEGで検証可能な下位課題に限定して benchmark と失敗条件を整理したいと考えています。こちらで比較表の初版と候補データセット表を用意できますので、もし関心があれば30分ほど意見交換の機会をいただけないでしょうか。

### 58.3 データ管理者 / 既存DB関係者向け

- 件名例: 公開EEG再解析条件についての短いご相談
- 初稿例: ご連絡失礼します。公開EEG横断で前処理条件を揃えた再解析を進めており、貴データ資産の利用条件とラベル解釈について確認したくご連絡しました。対象は記憶や注意など EEG で扱える下位課題に限定し、比較表と再現 notebook を成果物として残す予定です。こちらで整理した利用候補表を共有できますので、短時間でも確認の機会をいただければ助かります。

### 58.4 活動共催先 / 教材連携先向け

- 件名例: 公開EEG再現ハンズオンの共催ご相談
- 初稿例: ご連絡失礼します。公開EEGを題材にした再現ハンズオンの教材整備を進めており、単発イベントではなく教材, 録画, CSV, wiki を残す形で共催先を探しています。参加人数を追うより、参加後に各自が追試できる状態を成果にしたいと考えています。こちらで教材目次案と追試導線図を準備できますので、関心があれば一度ご相談できればと思います。

### 58.5 共同研究費 / 受託接続先向け

- 件名例: 公開EEG再解析の小規模共同検証のご相談
- 初稿例: ご連絡失礼します。公開EEGで再解析可能な下位課題に絞った benchmark 整備を進めており、小規模な共同検証または解析支援の形で連携可能性をご相談したくご連絡しました。高額設備や大規模収集を前提にせず、比較表, 再現 notebook, 短い成果報告までを短期で整える方針です。まずはこちらで比較条件メモを共有しますので、関心があれば短時間で意見交換いただけますと幸いです。

### 58.6 送る前の確認

- 相手の最近の論文や活動を1つは明示しているか
- `一緒に世界を変えたい` のような大きすぎる言い方になっていないか
- こちらが先に出せるものが明記されているか
- 30分以内の短い打合せ依頼になっているか

### 58.7 詳細版を引く場所

- 共同研究打診の一覧は `MindUpload-EEGDATA-FundMap-collab-outreach.csv` を使う
- 列は `counterpart_type`, `subject_template`, `opening_line`, `shared_context`, `what_we_offer`, `what_we_ask`, `closing_line`, `avoid_point`

## 59. 共同研究先の選び方ルーブリック

### 59.1 先に見るべき軸

- `テーマ適合`: EEGで扱える下位課題と相手の既存テーマが重なるか
- `データ適合`: 公開EEGや関連データ資産との接点があるか
- `工程適合`: こちらが出す比較表や notebook を受け取れる工程か
- `応答速度`: 30分打合せや短い確認に乗る速さがあるか
- `次段接続`: 次の助成や共同研究費に接続する見込みがあるか

### 59.2 強い相手のサイン

- 最近の論文や発表が `記憶`, `注意`, `意識 proxy`, `EEG decoding`, `benchmark` に近い
- `比較条件`, `前処理`, `再現性` の語彙が相手の成果物に出てくる
- 大規模共同研究より前に `短い確認`, `1枚の比較表`, `1つのデータ条件` で話が進む
- こちらが先に出す資料に対して具体的な修正点を返してくる

### 59.3 弱い相手のサイン

- テーマは近そうでも、新規収集や大型設備が前提で公開EEGの再解析に関心が薄い
- 1通目から `大きな構想` や `包括連携` を求めてくる
- データ利用条件や成果物の分担が曖昧なまま話を進めようとする
- 返信は来るが `何を見ればよいか` が一切具体化しない

### 59.4 相手タイプ別の見方

- `analysis_lab`: 比較条件と失敗条件の議論ができるかを見る
- `dataset_curator`: 利用条件とラベル解釈の確認に協力的かを見る
- `activity_partner`: 教材と録画を残す発想があるかを見る
- `pilot_partner`: 小規模検証や解析支援の請求単位に理解があるかを見る

### 59.5 スコアリングの実務ルール

- 5軸を `0 / 1 / 2` で仮採点する
- 合計 `8点以上` は先に打診する
- `6-7点` は1枚資料を送って反応を見る
- `5点以下` は追わず、別候補を優先する
- `応答速度` と `工程適合` が0点なら、テーマ適合が高くても後回しにする

### 59.6 詳細版を引く場所

- 相手先ルーブリックの一覧は `MindUpload-EEGDATA-FundMap-collab-rubric.csv` を使う
- 列は `counterpart_type`, `criterion`, `strong_signal`, `weak_signal`, `why_it_matters`, `action_if_weak`

## 60. 断られたときの再打診テンプレ

### 60.1 基本原則

- すぐ再送せず、断り理由に応じて `2週間-8週間` は空ける
- 再打診では `範囲を狭くする`, `先に出す資料を増やす`, `依頼時間を短くする`
- `前回と同じお願い` を送らず、何を変えたかを一文で示す

### 60.2 `今はタイミングが悪い` への再打診

- 件名例: 前回ご相談の件 `範囲を絞った再共有`
- 本文の芯: 前回は幅が広かったため、今回は公開EEG一条件の比較表と短いメモに絞りました。もし時期が合えば15分だけご意見をいただけると助かります。
- 変える点: 依頼時間を短くし、添付を1枚に減らす

### 60.3 `範囲が広すぎる` への再打診

- 件名例: 公開EEG一条件に絞った再相談
- 本文の芯: ご指摘を受けて、対象を記憶課題の公開EEG一条件に限定しました。比較条件と候補データセットも1ページに整理したので、改めて短時間だけご相談できれば幸いです。
- 変える点: `何をやらないか` を先に書く

### 60.4 `手が足りない` への再打診

- 件名例: ご負担を抑えた短い確認のお願い
- 本文の芯: こちらで比較表初版と利用候補表を用意したため、今回は確認していただきたい点を2点に絞りました。メールで一言いただくだけでも大変助かります。
- 変える点: 打合せ前提を外し、確認点を2つまでにする

### 60.5 `データ利用条件が難しい` への再打診

- 件名例: 利用条件確認の前提整理を更新しました
- 本文の芯: 前回の懸念を踏まえ、利用条件と成果物の切り分けを整理しました。再解析条件と公開範囲を明確にした短いメモを添えますので、確認可能な範囲だけご教示いただければ十分です。
- 変える点: `お願い` ではなく `確認可能範囲の限定` を前に出す

### 60.6 再打診で避けること

- `前回返信がなかったので再送します` と圧を出す
- 相手の事情に触れず、前回と同じ件名・同じ依頼を送る
- 断られた理由を `誤解だった` と処理して押し直す
- いきなり `共同研究契約`, `包括連携` に飛ぶ

### 60.7 詳細版を引く場所

- 再打診テンプレの一覧は `MindUpload-EEGDATA-FundMap-re-outreach.csv` を使う
- 列は `rejection_type`, `wait_window`, `revised_subject`, `revised_offer`, `ask_line`, `close_line`, `avoid_point`

## 61. 制度タイプ別の1ページ申請書ひな形

### 61.1 共通の型

1. `題目`: 公開EEG, 下位課題, benchmark のいずれかを入れる  
2. `課題設定`: `大きい夢` ではなく `今回扱う範囲` を1-2文で書く  
3. `方法`: 固定前処理, 被験者外評価, cross-dataset 比較のどれを使うか書く  
4. `成果物`: 比較表, notebook, 短報, 教材など具体物を書く  
5. `予算/使途`: 成果物に直結する費目だけを書く  
6. `次段接続`: 次の助成, 共同研究, 実験設計への接続で閉じる  

### 61.2 `research_grant`

- 題目行: 公開EEG横断での下位課題 benchmark 整備
- 課題設定行: `mind-upload` 全体を直接扱わず、公開EEGで検証可能な下位課題の成立条件と失敗条件を整理する。
- 方法行: 固定前処理, 被験者外評価, cross-dataset 比較を用いて主要2条件を比較する。
- 成果物行: 比較表, 再現 notebook, 手順書, 短報ドラフトを12週間で整える。
- 予算行: 計算, 保存, 公開, 校閲など成果物に直結する費目に限定する。
- 締め行: 次段の新規実験提案や大型助成の設計材料として接続する。

### 61.3 `award_or_prize`

- 題目行: 公開EEG再解析による継続成果の可視化
- 課題設定行: 将来像の提示ではなく、公開EEGを用いた再解析, 図表化, 短報化の継続成果を示す。
- 方法行: EEGで扱える下位課題に限定し、代表成果物を1から3点に絞って提示する。
- 成果物行: 代表図表, notebook, 短い成果報告, 公開資料を整える。
- 予算行: 成果公開, 発表整備, 英文校閲など見える成果に直結する費目に限定する。
- 締め行: 受賞後は外部から見える成果物を増やし、次段申請と共同研究の入口を作る。

### 61.4 `activity_grant`

- 題目行: 公開EEG再現ハンズオン教材の整備と共有
- 課題設定行: 単発イベントではなく、参加後に各自で追試できる教材基盤を残す。
- 方法行: 公開EEGを題材に、固定前処理, 簡易評価, 図表作成までを1回分の教材に落とす。
- 成果物行: 教材, 録画, CSV, wiki, 追試導線, 実施記録を残す。
- 予算行: 会場演出より資料整備, 録画, 配布物, 公開基盤に重点を置く。
- 締め行: 活動成果を次段の研究申請や共同研究形成に接続する。

### 61.5 `loan_or_finance`

- 題目行: 公開EEG再解析基盤の橋渡し運用
- 課題設定行: 高額設備ではなく、公開EEG再解析を止めずに回すための最小基盤を維持する。
- 方法行: 公開EEGで検証可能な下位課題に絞り、比較表と申請骨子までを短期で整える。
- 成果物行: 比較表, 再現 notebook, 申請書ドラフト, 費目対応表を残す。
- 予算行: 計算, 保存, 公開, 申請準備の小口費用に限定する。
- 締め行: 次段助成や共同研究費への接続点を作り、橋渡し資金として説明可能にする。

### 61.6 詳細版を引く場所

- 1ページ申請の一覧は `MindUpload-EEGDATA-FundMap-one-page-apps.csv` を使う
- 列は `support_type`, `title_line`, `problem_line`, `method_line`, `deliverable_line`, `budget_line`, `next_step_line`, `avoid_point`

## 62. 制度タイプ別の採択後レポート雛形

### 62.1 共通ルール

- 最初の1段落で `何をやると言って`, `何を実際にやったか`, `何が残ったか` を揃える
- 結果は `知見` より `比較表`, `notebook`, `教材`, `申請骨子` のような具体物で書く
- うまくいかなかった点も `失敗条件` として書き、次段でどう扱うかを添える
- 予算欄は `何に使ったか` だけでなく `何を残したか` と対応づける

### 62.2 `research_grant`

- 題目行: 公開EEG横断 benchmark 整備の実施報告
- 要約行: 固定前処理と被験者外評価を揃え、主要条件の比較表と再現 notebook を整備した。
- 結果行: 主要条件での成立条件と崩壊条件を整理し、短報ドラフトまで作成した。
- 費目行: 計算, 保存, 公開, 校閲に限定し、成果物と1対1で対応づけた。
- 次段行: 比較表と失敗条件を次段の実験提案または助成申請へ接続する。

### 62.3 `award_or_prize`

- 題目行: 公開EEG再解析による継続成果の報告
- 要約行: 題目整理から再解析, 図表化, 短報化, 公開資料化までの継続成果をまとめた。
- 結果行: 代表成果物を1から3点に絞り、外部から見える形に整理した。
- 費目行: 成果公開, 発表整備, 英文校閲など見える成果に直結する費目へ使った。
- 次段行: 受賞成果を次段申請と共同研究打診の入口として再利用する。

### 62.4 `activity_grant`

- 題目行: 公開EEG再現ハンズオン教材整備の実施報告
- 要約行: 単発イベントではなく、教材, 録画, CSV, wiki を残す形で活動を行った。
- 結果行: 教材パッケージと追試導線を整え、追試完了件数や派生実装を確認した。
- 費目行: 会場演出より資料整備, 録画, 配布物, 公開基盤に重点を置いた。
- 次段行: 活動で得た論点を研究申請や共同研究テーマへ戻した。

### 62.5 `loan_or_finance`

- 題目行: 公開EEG再解析基盤の橋渡し運用報告
- 要約行: 高額設備ではなく、比較表と申請骨子を止めずに出すための最小費用に限定して運用した。
- 結果行: 比較表, 再現 notebook, 申請書ドラフト, 費目対応表を整備した。
- 費目行: 計算, 保存, 公開, 申請準備の小口費用に限定し、成果物との対応を明示した。
- 次段行: 次段助成または共同研究費への接続点を作ったかで総括する。

### 62.6 詳細版を引く場所

- 採択後レポートの一覧は `MindUpload-EEGDATA-FundMap-report-templates.csv` を使う
- 列は `support_type`, `report_title`, `opening_line`, `result_line`, `artifact_line`, `budget_line`, `next_step_line`, `avoid_point`

## 63. 共同研究の役割分担テンプレ

### 63.1 原則

- こちらは `固定前処理`, `比較条件`, `初版成果物` を先に持つ
- 相手には `データ解釈`, `条件妥当性確認`, `追加視点` のいずれかを依頼する
- 最初から `全工程を共同` にせず、1つの成果物ごとに責任を切る
- 分担表は `誰が何を出すか` と `いつ止めるか` をセットで書く

### 63.2 `analysis_lab`

- こちらの役割: 比較設計 固定前処理 初版 benchmark 表の作成
- 相手の役割: 条件妥当性の確認 失敗条件の解釈 追加比較軸の助言
- 共同成果物: 比較表1枚 再現 notebook 1本 短いメモ 1本
- 止め時: 比較条件が増えすぎて12週間成果物が崩れる前

### 63.3 `dataset_curator`

- こちらの役割: 利用候補表 再解析条件メモ 成果物の公開範囲整理
- 相手の役割: 利用条件 ラベル解釈 欠損や注意点の確認
- 共同成果物: 利用条件メモ 候補データセット表 比較条件表
- 止め時: データ利用条件が長期間確定しないとき

### 63.4 `activity_partner`

- こちらの役割: 教材構成案 追試導線 実施後の成果整理
- 相手の役割: 共催導線 参加者接点 実施運営の補助
- 共同成果物: 教材 録画 CSV wiki 実施記録
- 止め時: 参加人数の拡大が教材品質を崩し始めたとき

### 63.5 `pilot_partner`

- こちらの役割: 小規模検証 比較表 解析メモ 費目対応表の作成
- 相手の役割: 利用場面の提示 検証観点の優先順位付け 小口予算の判断
- 共同成果物: 比較表 再現 notebook 短い成果報告 接続メモ
- 止め時: 大型契約や大規模収集の話に飛ぶ前

### 63.6 詳細版を引く場所

- 役割分担の一覧は `MindUpload-EEGDATA-FundMap-collab-roles.csv` を使う
- 列は `counterpart_type`, `our_role_1`, `our_role_2`, `their_role_1`, `their_role_2`, `shared_artifact`, `stop_rule`, `avoid_point`

## 64. 25トピック×連携先タイプの相性表

### 64.1 `analysis_lab` と相性が強い群

- EEG信号品質の限界検証
- 高密度EEG空間分解能評価
- ノイズ除去・信号分離手法の比較
- デコーディング精度ベンチマーク
- クロスデータセット汎化
- 運動意図デコーディング
- 感覚知覚デコーディング
- 感情状態の推定・分類
- 意識状態の分類（覚醒/睡眠/麻酔/DoC）

### 64.2 `dataset_curator` と相性が強い群

- 高密度EEG空間分解能評価
- クロスデータセット汎化
- 言語/意味デコーディング
- 記憶のエンコーディング/検索
- 統合情報理論(IIT)の実証的検証
- Global Workspace Theory の検証
- 意識の連続性と同一性

### 64.3 `activity_partner` と相性が強い群

- 社会的認知
- 創造性・問題解決
- mind-upload可能性の理論的枠組み
- 注意・ワーキングメモリ
- 公開EEG再現ハンズオン化しやすい基礎比較テーマ

### 64.4 `pilot_partner` と相性が強い群

- リアルタイムデコーディング
- ノイズ除去・信号分離手法の比較
- 運動意図デコーディング
- 感覚知覚デコーディング
- 感情状態の推定・分類
- 意識状態の分類（覚醒/睡眠/麻酔/DoC）

### 64.5 使い方

- まず `best_counterpart` を見て最初の打診先を決める
- 次に `second_counterpart` を見て断られた場合の代替線を作る
- `first_artifact` は 1通目で先に出す資料の種類として使う
- `avoid_match` は 話が大きくなりすぎる相手を避ける目安にする

### 64.6 詳細版を引く場所

- 25トピックの相性一覧は `MindUpload-EEGDATA-FundMap-topic-collab-fit.csv` を使う
- 列は `phase`, `topic`, `analysis_lab_fit`, `dataset_curator_fit`, `activity_partner_fit`, `pilot_partner_fit`, `best_counterpart`, `second_counterpart`, `fit_reason`, `first_artifact`, `avoid_match`

## 65. 制度タイプ別の中間報告テンプレ

### 65.1 共通ルール

- 中間報告は `完了したこと` より `途中でも残せたもの` を先に書く
- `遅れている理由` だけでなく `何を削って何を守ったか` を書く
- `次の30日` は抽象計画ではなく、比較表や notebook の更新単位で書く
- 予算欄は消化率ではなく `何に使って何を残したか` を併記する

### 65.2 `research_grant`

- 冒頭行: 固定前処理と被験者外評価を先に固定し、主要条件の比較表初版を作成した。
- 進捗行: 予定した比較軸のうち中核条件を優先し、再現 notebook の dry-run まで完了した。
- 変更行: 補助比較は後ろ倒しにし、benchmark の骨格を守る構成へ調整した。
- 次30日行: 比較表の更新, 手順書の整理, 短報ドラフトの骨子化を進める。

### 65.3 `award_or_prize`

- 冒頭行: 代表成果物を1から3点に絞り、図表と説明文の見せ方を固定した。
- 進捗行: 再解析結果と短い成果報告の初版を整え、外部から見える形に整理した。
- 変更行: 周辺発表より代表成果物の磨き込みを優先する構成へ切り替えた。
- 次30日行: 公開資料, 発表用説明, 次段申請への接続文を整える。

### 65.4 `activity_grant`

- 冒頭行: 単発イベントではなく、教材と録画と追試導線を残す構成で進行している。
- 進捗行: 教材目次, 実施台本, 配布CSV, wiki 導線の初版を整えた。
- 変更行: 開催回数より教材品質を優先し、1回分の完成度を上げる方針にした。
- 次30日行: 実施1回分の完了, 録画整理, 追試完了件数の確認を進める。

### 65.5 `loan_or_finance`

- 冒頭行: 高額設備を避け、比較表と申請骨子を止めずに出すための最小費用で運用している。
- 進捗行: 比較表初版, 再現 notebook, 費目対応表の骨子を整えた。
- 変更行: 外部発表や追加検証を抑え、短期成果物の可視化を優先した。
- 次30日行: 申請書ドラフト, 接続先メモ, 成果物公開の最小セットを揃える。

### 65.6 詳細版を引く場所

- 中間報告の一覧は `MindUpload-EEGDATA-FundMap-midterm-templates.csv` を使う
- 列は `support_type`, `opening_line`, `progress_line`, `change_line`, `artifact_line`, `budget_line`, `next_30d_line`, `avoid_point`

## 66. 共同研究会議の30分アジェンダ

### 66.1 共通構成

1. `5分`: 何を扱わないかを含めて今回の範囲を固定する  
2. `10分`: 比較表や候補データセット表など、こちらが先に出す資料を確認する  
3. `10分`: 相手に確認したい論点を2-3個に絞って聞く  
4. `5分`: 次に残す成果物と、次回までにやらないことを確認する  

### 66.2 `analysis_lab`

- 目的: 比較条件と失敗条件の解釈を揃える
- 先出し資料: 比較表初版, 再現 notebook, 主要指標メモ
- 確認論点: 前処理固定で十分か, 追加比較軸を入れるか, どこで止めるか
- 会議後に残すもの: 修正版比較表と次の1週間タスク

### 66.3 `dataset_curator`

- 目的: 利用条件とラベル解釈の確認を短時間で済ませる
- 先出し資料: 利用候補表, 再解析条件メモ, 公開範囲メモ
- 確認論点: 利用可否, 注意点, ラベルの読み替え可否
- 会議後に残すもの: 利用条件メモと使わない条件の一覧

### 66.4 `activity_partner`

- 目的: 教材品質を落とさず実施範囲を決める
- 先出し資料: 教材目次, 追試導線図, 実施台本
- 確認論点: 実施1回分で十分か, 何を録画するか, 何を配布するか
- 会議後に残すもの: 実施版アジェンダと成果物分担

### 66.5 `pilot_partner`

- 目的: 小規模検証の請求単位と成果物単位を揃える
- 先出し資料: 比較条件メモ, 短い成果報告案, 費目対応表
- 確認論点: 検証の最小単位, 何を納品扱いにするか, どこで拡張を止めるか
- 会議後に残すもの: 小規模検証メモと次回までの判断条件

### 66.6 詳細版を引く場所

- 30分会議アジェンダの一覧は `MindUpload-EEGDATA-FundMap-collab-agenda.csv` を使う
- 列は `counterpart_type`, `goal`, `minute_0_5`, `minute_5_15`, `minute_15_25`, `minute_25_30`, `artifact_to_send_before`, `artifact_to_leave_after`, `avoid_point`

## 67. 25トピック別の最初の打診先候補メモ

### 67.1 基本ルール

- 最初の打診は `best_counterpart` にだけ送る
- 1通目では `first_artifact` を必ず先に出す
- `second_counterpart` は断られた後か、1週間以上反応が鈍いときに使う
- topic に対して `何を一緒にやらないか` も先に決めておく

### 67.2 最初に動きやすいテーマ

- `EEG信号品質の限界検証`: analysis_lab に `qc_benchmark_v1` を送る
- `ノイズ除去・信号分離手法の比較`: analysis_lab か pilot_partner に `preprocessing_comparison_table` を送る
- `デコーディング精度ベンチマーク`: analysis_lab に `decoding_benchmark_v1` を送る
- `リアルタイムデコーディング`: pilot_partner に `replay_latency_note` を送る
- `社会的認知`: activity_partner に `hyperscanning_pilot_note` を送る
- `mind-upload可能性の理論的枠組み`: activity_partner に `claim_ladder_memo` を送る

### 67.3 使い方

- `first_message_angle` はメールの1段落目にそのまま使う
- `meeting_goal` は 30分会議を設定するときの着地点に使う
- `do_not_lead_with` は 1通目で言わないこととして使う

### 67.4 詳細版を引く場所

- 初動打診メモの一覧は `MindUpload-EEGDATA-FundMap-topic-first-outreach.csv` を使う
- 列は `phase`, `topic`, `best_counterpart`, `second_counterpart`, `first_message_angle`, `first_artifact`, `meeting_goal`, `do_not_lead_with`

## 68. 制度タイプ別の月次レビュー表

### 68.1 共通ルール

- 月次レビューでは `進んだか` より `何を残せたか` を先に見る
- 毎月 `守る成果物`, `削るもの`, `次月の固定条件` を1行ずつ書く
- `反省` を増やしすぎず、比較表や notebook の更新単位に落とす
- 赤信号は `評価条件が揺れている`, `成果物が外に見えない`, `次段接続が空白` の3つで見る

### 68.2 `research_grant`

- 月次で見ること: 比較表が更新されたか, notebook が再実行可能か, 失敗条件が言語化されたか
- 残すもの: 比較表1版, 指標メモ, 次に切る条件一覧
- 削るもの: 補助比較, 過剰なデータ追加, 理論主張の拡張
- 次月へ渡すもの: 固定前処理と主要2条件のまま更新できる状態

### 68.3 `award_or_prize`

- 月次で見ること: 代表成果物が1から3点に保たれているか, 説明文が短くなっているか, 外から見える形に変換されたか
- 残すもの: 代表図表, 公開資料, 短い成果報告
- 削るもの: 周辺実績の列挙, 将来像の長文, 追加演出
- 次月へ渡すもの: 次段申請に貼れる説明文

### 68.4 `activity_grant`

- 月次で見ること: 教材と録画が整っているか, 追試導線が残っているか, 実施記録が申請材料に戻るか
- 残すもの: 教材版管理, 実施メモ, 追試件数メモ
- 削るもの: 開催回数の増加, 配布物の過剰化, 集客中心の改善
- 次月へ渡すもの: 1回分の教材パッケージ完成度

### 68.5 `loan_or_finance`

- 月次で見ること: 短期成果物が見えるか, 費目と成果物が対応しているか, 次段接続先が具体化したか
- 残すもの: 比較表, 費目対応表, 接続先メモ
- 削るもの: 外部発表の拡張, 新規検証の拡張, 説明しにくい費目
- 次月へ渡すもの: 申請骨子または共同研究費への接続材料

### 68.6 詳細版を引く場所

- 月次レビューの一覧は `MindUpload-EEGDATA-FundMap-monthly-review.csv` を使う
- 列は `support_type`, `review_goal`, `check_1`, `check_2`, `check_3`, `artifact_to_keep`, `cut_this_month`, `next_month_handoff`, `avoid_point`

## 69. 共同研究開始時の合意メモ雛形

### 69.1 共通ルール

- 最初の合意メモは契約書の代わりでなく、`何をやるか`, `何をやらないか`, `何を先に出すか` の確認に使う
- `成果物`, `データ条件`, `公開範囲`, `止め時` を必ず入れる
- 書き方は柔らかくても、分担と停止条件は曖昧にしない

### 69.2 共通の型

1. `目的`: 今回は何を小さく確認するか  
2. `範囲外`: 今回は何を扱わないか  
3. `こちらの役割`: 比較設計, 前処理, 初版成果物など  
4. `相手の役割`: 条件確認, データ解釈, 実施運営など  
5. `成果物`: 比較表, notebook, 教材, メモなど  
6. `公開条件`: 外に出せるものと出せないもの  
7. `止め時`: どこで拡張を止めるか  

### 69.3 相手タイプ別の強調点

- `analysis_lab`: 比較条件と追加比較軸の上限を明記する
- `dataset_curator`: 利用条件と公開範囲を先に明記する
- `activity_partner`: 教材と録画の残し方を先に明記する
- `pilot_partner`: 納品単位と請求単位を先に明記する

### 69.4 詳細版を引く場所

- 開始合意メモの一覧は `MindUpload-EEGDATA-FundMap-kickoff-memo.csv` を使う
- 列は `counterpart_type`, `purpose_line`, `out_of_scope_line`, `our_role_line`, `their_role_line`, `artifact_line`, `data_rule_line`, `stop_rule_line`, `avoid_point`

## 70. 25トピック別の first artifact 下書き一覧

### 70.1 使い方

- `artifact_opening` は そのままメモやメール添付の冒頭に使う
- `section_1` と `section_2` は まず埋めるべき見出しとして使う
- `next_action` は 1週間以内の具体タスクに変換する
- `avoid_point` は 最初の draft で言い過ぎないためのガードにする

### 70.2 first artifact の基本原則

- 1枚目で `比較条件`, `候補データ`, `残す指標` を見せる
- 2枚目以降に詳細を足し、最初から長文理論にしない
- `large vision` ではなく `small benchmark` の形にする

### 70.3 詳細版を引く場所

- first artifact 下書きの一覧は `MindUpload-EEGDATA-FundMap-topic-first-artifacts.csv` を使う
- 列は `phase`, `topic`, `artifact_name`, `artifact_format`, `artifact_opening`, `section_1`, `section_2`, `next_action`, `avoid_point`

## 71. 制度タイプ別の四半期レビュー表

### 71.1 共通ルール

- 四半期レビューでは `3か月で残ったもの` を最初に並べる
- `予定比` だけでなく `削って守った範囲` を書く
- 1期ごとに `継続`, `停止`, `次段接続` の3判断を明示する
- レビューの締めは反省でなく `次の四半期で固定する条件` にする

### 71.2 `research_grant`

- 見ること: benchmark の骨格が閉じたか, 比較表が外に出せる形か, 失敗条件が次段実験に繋がるか
- 残すもの: 比較表 stable 版, 再現 notebook, 手順書, 短報ドラフト
- 止めるもの: 補助比較, 増え続けるデータ条件, 理論主張の拡張
- 次四半期へ渡すもの: 更新可能な benchmark 基盤と次段申請材料

### 71.3 `award_or_prize`

- 見ること: 代表成果物が絞れているか, 見せ方が短くなったか, 次段申請へ貼れるか
- 残すもの: 代表図表, 公開資料, 100-300字説明文, 短い成果報告
- 止めるもの: 実績の追加列挙, 演出の増加, 将来像の長文化
- 次四半期へ渡すもの: 外部向け成果物一式と再利用可能な自己紹介文

### 71.4 `activity_grant`

- 見ること: 教材パッケージが残ったか, 追試導線が生きているか, 実施記録が研究材料へ戻るか
- 残すもの: 教材, 録画, CSV, wiki, 実施記録, 追試件数メモ
- 止めるもの: 開催回数の増加, 周辺イベント, 過剰な配布物
- 次四半期へ渡すもの: 再利用可能な教材一式と論点整理メモ

### 71.5 `loan_or_finance`

- 見ること: 短期成果物が見えるか, 費目と成果物が結びついているか, 次段資金の接続点があるか
- 残すもの: 比較表, 費目対応表, 申請骨子, 接続先メモ
- 止めるもの: 外部発表の拡張, 新規検証の拡張, 返済説明に使えない費目
- 次四半期へ渡すもの: 助成または共同研究費に変換できる成果物セット

### 71.6 詳細版を引く場所

- 四半期レビューの一覧は `MindUpload-EEGDATA-FundMap-quarterly-review.csv` を使う
- 列は `support_type`, `quarter_goal`, `review_1`, `review_2`, `review_3`, `artifact_to_keep`, `stop_now`, `next_quarter_focus`, `avoid_point`

## 72. 共同研究終了時のクローズメモ

### 72.1 共通ルール

- クローズメモは `終わった理由` より `何が残ったか` を先に書く
- `未完了` は失敗でなく、次に回す条件として整理する
- データ条件と公開範囲は終了時にもう一度明記する
- 関係を閉じるときも `次に連絡してよい条件` を1行残す

### 72.2 共通の型

1. `終了理由`: 今回ここで区切る理由  
2. `実施内容`: 何を比較し、何を確認したか  
3. `残った成果物`: 比較表, notebook, 教材, メモなど  
4. `未完了項目`: 次回以降に回す条件  
5. `公開条件`: 共有できるものとできないもの  
6. `次の接点`: 再開や再連絡の条件  

### 72.3 相手タイプ別の強調点

- `analysis_lab`: 比較条件の上限と、次に足す比較軸を明記する
- `dataset_curator`: 利用条件の確定範囲と、使わない条件を明記する
- `activity_partner`: 残る教材と録画の所在を明記する
- `pilot_partner`: 納品済み範囲と、次に有償化する単位を明記する

### 72.4 詳細版を引く場所

- クローズメモの一覧は `MindUpload-EEGDATA-FundMap-close-memo.csv` を使う
- 列は `counterpart_type`, `close_reason_line`, `done_line`, `artifact_line`, `remaining_line`, `data_rule_line`, `next_contact_line`, `avoid_point`

## 73. 25トピック別の short abstract 100字版一覧

### 73.1 使い方

- 100字版はフォームの短要約, メール冒頭, スライド1枚目に使う
- `core_claim` は 主張を広げすぎないための芯として使う
- `safe_ending` は 最後の一文の安全な閉じ方として使う

### 73.2 100字版で守ること

- `公開EEG`, `固定前処理`, `benchmark` など守りの語を最低1つ入れる
- `解明する`, `証明する`, `実現する` で閉じない
- 大きい理論より `比較`, `整理`, `整備`, `proxy` に寄せる

### 73.3 詳細版を引く場所

- 100字要約の一覧は `MindUpload-EEGDATA-FundMap-short-abstracts-100.csv` を使う
- 列は `phase`, `topic`, `short_abstract_100`, `core_claim`, `safe_ending`

## 74. 25トピック別の30秒ピッチ一覧

### 74.1 使い方

- 30秒ピッチは 面談冒頭 予備審査 口頭紹介の最初の1ターンに使う
- `opening_line` は 1文目として固定し `pitch_30s` で中身をつなぐ
- `closing_line` は `大きすぎる主張を締める` ための最後の1文として使う
- `avoid_point` は 話しながら逸脱しやすい論点のブレーキにする

### 74.2 30秒ピッチの基本原則

- 最初の10秒で `何を比べるか` を言う
- 次の10秒で `何を成果物として残すか` を言う
- 最後の10秒で `何を言い過ぎないか` を言う
- `世界を変える` ではなく `公開EEGで再現可能な比較条件を整える` に寄せる

### 74.3 詳細版を引く場所

- 30秒ピッチの一覧は `MindUpload-EEGDATA-FundMap-pitches-30s.csv` を使う
- 列は `phase`, `topic`, `pitch_30s`, `opening_line`, `closing_line`, `avoid_point`

## 75. 制度タイプ別の提出直前チェック1枚版

### 75.1 共通ルール

- 提出直前は `盛る作業` ではなく `削る作業` にする
- 1枚版では `今ある成果物` と `今回出さない主張` を並べて確認する
- 直前に直すのは `表現`, `整合`, `提出条件` までに止める
- 新しい分析や新しい相手先は締切直前に足さない

### 75.2 制度タイプ別の見る場所

- `research_grant`: 仮説より `比較条件と再現手順が揃っているか` を見る
- `award_or_prize`: 実績数より `代表成果物が一目で伝わるか` を見る
- `activity_grant`: 開催規模より `教材と再利用導線が残るか` を見る
- `loan_or_finance`: 将来像より `費目と短期成果物が結び付くか` を見る

### 75.3 直前に落としやすい赤信号

- 申請書本文と予算表で成果物の粒度がずれている
- `EEGで mind-upload を実現` のように claim level が急に跳ねている
- データ条件が `公開EEG` から `新規収集前提` にすり替わっている
- 締切当日にしか確認できない添付資料が残っている

### 75.4 詳細版を引く場所

- 提出直前チェックの一覧は `MindUpload-EEGDATA-FundMap-pre-submit-check.csv` を使う
- 列は `support_type`, `last_check_1`, `last_check_2`, `last_check_3`, `must_attach`, `must_cut`, `deadline_rule`, `red_flag`

## 76. 共同研究先タイプ別の first meeting メモ雛形

### 76.1 使い方

- 初回面談メモは `見せるもの2つ`, `聞くこと2つ`, `次の一手1つ` で固定する
- `meeting_goal` は 30分面談の出口として先に置く
- `show_1` と `show_2` は その場で画面共有できる単位に落とす
- `next_step` は 1週間以内に送れるものだけを書く

### 76.2 初回面談で守ること

- 相手に合わせて説明を変えても `今回やらない範囲` は固定する
- dataset 利用条件が絡む相手には 解析案より先に公開条件を確認する
- pilot 相手には 長い理論より `1回で見える deliverable` を先に出す
- 活動相手には 成果発表より `再利用できる教材単位` を先に示す

### 76.3 詳細版を引く場所

- 初回面談メモの一覧は `MindUpload-EEGDATA-FundMap-first-meeting-memo.csv` を使う
- 列は `counterpart_type`, `meeting_goal`, `show_1`, `show_2`, `ask_1`, `ask_2`, `next_step`, `avoid_point`

## 77. 25トピック別の1枚スライド骨子

### 77.1 使い方

- 1枚スライド骨子は 初回説明 申請添付 面談用の叩き台として使う
- `slide_title` は 研究テーマ名ではなく その1枚で見せる判断軸にする
- `top_line` は 1文で `何を測るか` を固定する
- `left_block` は 入力条件や比較条件 `right_block` は 出す図表や比較結果に寄せる
- `bottom_line` は 安全な結論だけに絞る

### 77.2 1枚に残す基本要素

- 上段は `公開EEG`, `固定前処理`, `比較条件` のどれかを必ず入れる
- 左側は `使うデータ`, `指標`, `条件固定` を置く
- 右側は `比較表`, `失敗条件`, `残る成果物` を置く
- 最下段は `過大主張を抑えた takeaway` で閉じる

### 77.3 詳細版を引く場所

- 1枚スライド骨子の一覧は `MindUpload-EEGDATA-FundMap-one-slide-skeletons.csv` を使う
- 列は `phase`, `topic`, `slide_title`, `top_line`, `left_block`, `right_block`, `bottom_line`, `avoid_point`

## 78. 制度タイプ別の提出当日オペレーション

### 78.1 共通ルール

- 提出当日は 内容改善ではなく `事故防止` に集中する
- PDF 化 添付確認 ファイル名確認を `締切前` に終える
- 送信後すぐに `何を出したか` と `次に使う版` を1行で残す
- 送信後に本文を書き換えたくなっても 当日はログ化だけして次版へ回す

### 78.2 制度タイプ別の重点

- `research_grant`: 比較条件と添付資料の整合を最優先に見る
- `award_or_prize`: 代表成果物の見え方が崩れていないかを見る
- `activity_grant`: 教材や公開導線のリンク切れがないかを見る
- `loan_or_finance`: 数字と費目対応が本文とずれていないかを見る

### 78.3 提出後すぐに残すもの

- 提出ファイル名
- 提出時刻
- 送信した版番号
- 次版で直す候補を3行以内で残したメモ

### 78.4 詳細版を引く場所

- 提出当日オペの一覧は `MindUpload-EEGDATA-FundMap-submit-day-ops.csv` を使う
- 列は `support_type`, `first_hour`, `final_10min`, `just_before_submit`, `right_after_submit`, `same_day_record`, `next_day_followup`, `avoid_point`

## 79. 共同研究先タイプ別の2回目面談アジェンダ

### 79.1 使い方

- 2回目面談は `紹介` ではなく `判定` の場として使う
- 初回で話した広い論点は持ち込まず `修正版 artifact` を中心に進める
- `decision_1` と `decision_2` に yes/no を置き 面談で決める項目を固定する
- `artifact_to_send` は 面談後3営業日以内に送れる単位にする

### 79.2 2回目面談で決めること

- 今回やる比較条件とやらない比較条件
- データ条件または公開条件の最終確認
- 次回までの責任分担
- 続けるか止めるかの判定条件

### 79.3 詳細版を引く場所

- 2回目面談アジェンダの一覧は `MindUpload-EEGDATA-FundMap-second-meeting-agenda.csv` を使う
- 列は `counterpart_type`, `meeting_goal`, `review_1`, `review_2`, `decision_1`, `decision_2`, `artifact_to_send`, `avoid_point`

## 80. 25トピック別の図表キャプション集

### 80.1 使い方

- `caption_short` は スライド直下や申請書内の短い図表注に使う
- `caption_mid` は wiki 本文 短報 共有メモの説明文として使う
- `what_this_figure_shows` は その図で何を判断できるかを固定するために使う
- `avoid_point` は 図の意味を広げすぎないためのブレーキにする

### 80.2 図表キャプションで守ること

- 図そのものより `比較条件` と `何を支持する図か` を先に書く
- `示した` と `証明した` を分ける
- 大きな理論名が入るときほど `proxy`, `候補`, `再現範囲` の語で締める
- 図1枚でテーマ全体を言い切らず `今回見せた範囲` を明記する

### 80.3 詳細版を引く場所

- 図表キャプションの一覧は `MindUpload-EEGDATA-FundMap-figure-captions.csv` を使う
- 列は `phase`, `topic`, `figure_title`, `caption_short`, `caption_mid`, `what_this_figure_shows`, `avoid_point`

## 81. 制度タイプ別の提出後フォロー運用

### 81.1 共通ルール

- 提出後24時間は `出した版を残す`, `次に直す点を3つ残す`, `無駄に追送しない` を守る
- 3営業日以内に 送った内容と面談用転用素材の差分を整理する
- 返信が来た場合は 新しい主張を足さず `提出済み内容の補足` に徹する
- 返信が来ない場合も 焦って追加資料を連投しない

### 81.2 制度タイプ別の重点

- `research_grant`: 比較条件一覧と候補データ表をすぐ出せる状態にしておく
- `award_or_prize`: 代表成果物3点と短い自己説明を面談用に転記しておく
- `activity_grant`: 教材見本と実施後に残る成果物一覧を即送できるようにする
- `loan_or_finance`: 費目対応表と短期成果物表の数字を再確認しておく

### 81.3 詳細版を引く場所

- 提出後フォロー運用の一覧は `MindUpload-EEGDATA-FundMap-post-submit-followup.csv` を使う
- 列は `support_type`, `first_24h`, `within_3d`, `within_7d`, `artifact_to_prepare`, `if_contacted`, `if_silent`, `avoid_point`

## 82. 共同研究先タイプ別の断り条件と継続条件一覧

### 82.1 使い方

- 連携判定は `相性が良いか` ではなく `小さく始めて成果物が残るか` で見る
- `continue_signal` は 次の1週間タスクに落とせる条件にする
- `stop_signal` は その場の温度感でなく 具体的な危険信号として書く
- `soft_no_line` は 関係を壊さず今回は見送るときの短文に使う

### 82.2 断り条件で先に見ること

- 公開条件が最後まで曖昧
- 比較条件より広報や大型構想が先に来る
- 小口の試行や小さい deliverable を受け入れない
- 次回までの責任分担が置けない

### 82.3 詳細版を引く場所

- 継続条件と断り条件の一覧は `MindUpload-EEGDATA-FundMap-collab-continue-stop.csv` を使う
- 列は `counterpart_type`, `continue_signal`, `stop_signal`, `checkpoint`, `soft_no_line`, `continue_next_step`, `avoid_point`

## 83. 25トピック別の審査員向け図1枚の読み上げ文

### 83.1 使い方

- `figure_talk_20s` は 面談や予備審査で図1枚を20秒前後で説明するときに使う
- `opening_line` は 何を比べる図かを最初に固定する
- `focus_line` は 審査員に見てほしい比較軸を1つに絞る
- `closing_line` は 過大主張を避けた締めの1文として使う

### 83.2 読み上げ文で守ること

- 最初に `この図は何を示すか` を言い 途中で `ここが差です` を言う
- 図の読み上げだけでテーマ全体を言い切らない
- `証明` より `比較` `整理` `再現範囲` の語を優先する
- 理論系 topic でも `候補指標` `状態差` `claim ladder` など観測可能な単位で閉じる

### 83.3 詳細版を引く場所

- 審査員向け図説明の一覧は `MindUpload-EEGDATA-FundMap-reviewer-figure-talk.csv` を使う
- 列は `phase`, `topic`, `figure_talk_20s`, `opening_line`, `focus_line`, `closing_line`, `avoid_point`

## 84. 制度タイプ別の不採択通知後48時間運用

### 84.1 共通ルール

- 通知当日は `感情の整理` と `記録固定` を先に行い 書き換えは急がない
- 最初の24時間では `落ちた理由の仮説` と `残す成果物` を分けて書く
- 48時間以内に `次版の縮小方針` と `残す図表1枚` を決める
- 不採択直後に 大きい理論やテーマをさらに足さない

### 84.2 制度タイプ別の重点

- `research_grant`: 範囲縮小と benchmark 化の余地を先に見る
- `award_or_prize`: 実績物の見せ順と代表成果物の絞り込みを先に見る
- `activity_grant`: 人数より教材と再利用物が残ったかを先に見る
- `loan_or_finance`: 使途と短期成果物の対応が弱かった点を先に見る

### 84.3 詳細版を引く場所

- 不採択後48時間運用の一覧は `MindUpload-EEGDATA-FundMap-rejection-48h.csv` を使う
- 列は `support_type`, `first_6h`, `first_24h`, `first_48h`, `record_to_keep`, `rewrite_start`, `avoid_point`

## 85. 共同研究先タイプ別の再開条件と保留条件メモ

### 85.1 使い方

- `hold_signal` は 今は止めるべき条件を短く固定する
- `resume_signal` は 再開してよい条件を具体的な形で置く
- `hold_line` は 関係を壊さず保留するときの短文に使う
- `resume_line` は 再開連絡の冒頭文として使う

### 85.2 保留と再開で見ること

- 利用条件や比較条件の曖昧さが解消したか
- 次回までの担当と deliverable が置けるか
- 小口で始める前提を相手が受け入れるか
- 前回止めた理由が文面で解消されたか

### 85.3 詳細版を引く場所

- 再開条件と保留条件の一覧は `MindUpload-EEGDATA-FundMap-collab-resume-hold.csv` を使う
- 列は `counterpart_type`, `hold_signal`, `resume_signal`, `hold_line`, `resume_line`, `artifact_to_keep`, `next_check`, `avoid_point`

## 86. 25トピック別の最初の査読コメント想定と返し1往復

### 86.1 使い方

- `reviewer_comment` は 最初に来そうな突っ込みを1文で固定したものとして使う
- `first_reply` は その場で返す短い返答として使う
- `next_fix` は 返答したあとに必ず直すべき最小修正点として使う
- `safe_claim` は それでも残してよい主張の下限として使う

### 86.2 最初の1往復で守ること

- 反論より先に `その懸念は妥当` を含む形で範囲を狭める
- その場で新しい約束を増やさず 既存の図表や比較条件へ寄せる
- 返答後は `何を直すか` を1個に絞る
- 通らない表現を残したまま長文化しない

### 86.3 詳細版を引く場所

- 査読コメント初動の一覧は `MindUpload-EEGDATA-FundMap-review-roundtrip.csv` を使う
- 列は `phase`, `topic`, `reviewer_comment`, `first_reply`, `next_fix`, `safe_claim`, `avoid_point`

## 87. 制度タイプ別の再応募1週間プラン

### 87.1 共通ルール

- 1日目は気持ちで書き換えず `落ちた仮説` と `残す成果物` を分ける
- 3日目までに `何を削るか` を決め 5日目までに `何を足すか` を決める
- 7日目までに 次版タイトルと図表1枚を固定する
- 次版の本文は 前回の弱点を潰す範囲で閉じる

### 87.2 再応募1週間で先に決めること

- 範囲を狭めるか 見せ方を変えるか
- 残す成果物は何か
- 今回増やす証拠は1点で足りるか
- 次に出す制度タイプを変える必要があるか

### 87.3 詳細版を引く場所

- 再応募1週間プランの一覧は `MindUpload-EEGDATA-FundMap-reapply-1week.csv` を使う
- 列は `support_type`, `day_1`, `day_2_3`, `day_4_5`, `day_6_7`, `artifact_to_finish`, `avoid_point`

## 88. 共同研究先タイプ別の失注後フォロー文面

### 88.1 使い方

- `subject_line` は 失注直後の短い follow-up 件名に使う
- `opening_line` は お礼と温度を下げるための1文として使う
- `reason_line` は 今回進めない理由を攻撃的でない形で固定する
- `keep_door_open_line` は 関係を切らずに終えるための1文に使う
- `next_asset_line` は 後で送り直せる成果物単位を明記するときに使う

### 88.2 失注後文面で守ること

- 相手の都合を責めない
- 失注理由を一般論でぼかしすぎず こちらの縮小方針に寄せる
- 大きい計画を再提示しない
- 次に送るなら `1枚` `1表` `短いメモ` にする

### 88.3 詳細版を引く場所

- 失注後フォロー文面の一覧は `MindUpload-EEGDATA-FundMap-lost-deal-followup.csv` を使う
- 列は `counterpart_type`, `subject_line`, `opening_line`, `reason_line`, `keep_door_open_line`, `next_asset_line`, `avoid_point`

## 89. 25トピック別の採択後最初の30日タスク

### 89.1 使い方

- `day_1_3` は 採択直後に固定する条件だけを書く
- `day_4_10` は 最初の比較表や候補データ確認など 早く閉じるべき基盤作業に使う
- `day_11_20` は 初版成果物を1つ出す期間として使う
- `day_21_30` は 月末に残す形へ閉じる期間として使う
- `first_artifact` は 30日以内に外へ見せられる最小成果物として使う

### 89.2 初月で守ること

- 新しい ambition を足さず 採択時に通した範囲を固定する
- `比較条件`, `候補データ`, `最初の図表` を月内に1回閉じる
- month 1 は 学術的完成より `再現可能な初版` を優先する
- `first_risk` は 30日で最も踏みやすい失敗として常に先に見る

### 89.3 詳細版を引く場所

- 採択後最初の30日タスクの一覧は `MindUpload-EEGDATA-FundMap-first-30days.csv` を使う
- 列は `phase`, `topic`, `day_1_3`, `day_4_10`, `day_11_20`, `day_21_30`, `first_artifact`, `first_risk`, `avoid_point`

## 90. 制度タイプ別の面談失敗からの立て直し

### 90.1 共通ルール

- 面談直後は `何を言い過ぎたか`, `何を言えなかったか`, `何を見せ忘れたか` を分けて書く
- 次回は 説明量を増やすのでなく `図1枚` と `結論1文` を減らして整える
- 失敗理由が不明でも まずは `広すぎた`, `成果物が見えない`, `数字が弱い` のどれかに仮置きする
- 次回面談までに直すのは 1つの弱点だけに絞る

### 90.2 面談失敗後に先に見ること

- 相手が止まったのはどの一文か
- 代表成果物がその場で見えたか
- 質問に対して claim level が跳ねたか
- 次回は口頭より図表で返すべきか

### 90.3 詳細版を引く場所

- 面談失敗からの立て直し一覧は `MindUpload-EEGDATA-FundMap-interview-recovery.csv` を使う
- 列は `support_type`, `failure_signal`, `same_day_fix`, `next_meeting_fix`, `one_slide_to_prepare`, `opening_to_change`, `avoid_point`

## 91. 共同研究先タイプ別の次回提案1ページ骨子

### 91.1 使い方

- `title_line` は 相手に合わせた次回提案の題名として使う
- `problem_line` は 今回は何を狭く解くかを固定する
- `our_offer_line` は こちらが先に出すものを短く示す
- `their_gain_line` は 相手が得るものを 研究寄りか運用寄りかで切り分けて示す
- `close_line` は 次の30分面談に繋げる最後の1文として使う

### 91.2 1ページ骨子で守ること

- vision より `次に出す1枚` を先に置く
- 相手の役割を増やしすぎない
- 初回の失敗理由がある場合は その修正点を1行で明示する
- `共同研究したいです` で終わらず `何を見てもらうか` で終える

### 91.3 詳細版を引く場所

- 次回提案1ページ骨子の一覧は `MindUpload-EEGDATA-FundMap-next-proposal-onepager.csv` を使う
- 列は `counterpart_type`, `title_line`, `problem_line`, `our_offer_line`, `their_gain_line`, `shared_artifact_line`, `close_line`, `avoid_point`

## 92. 25トピック別の月末レビュー観点

### 92.1 使い方

- `review_goal` は その月に守るべき芯として使う
- `check_1` から `check_3` は 月末に yes/no で確認する項目にする
- `keep_artifact` は 次月へ必ず残す成果物として使う
- `cut_next_month` は 来月やらないことを先に固定するために使う

### 92.2 月末レビューで守ること

- 進捗率より `比較条件が閉じたか` を優先して見る
- その月に増えたものより `残ったもの` を確認する
- 次月の追加 ambition を入れる前に `cut_next_month` を読む
- 25 topic すべてで `言い過ぎない線` を毎月確認する

### 92.3 詳細版を引く場所

- topic 別の月末レビュー一覧は `MindUpload-EEGDATA-FundMap-topic-month-end-review.csv` を使う
- 列は `phase`, `topic`, `review_goal`, `check_1`, `check_2`, `check_3`, `keep_artifact`, `cut_next_month`, `avoid_point`

## 93. 制度タイプ別の2回目面談テンプレ強化版

### 93.1 使い方

- 2回目面談の制度別版は `opening_30s` で入り `evidence_1` と `evidence_2` で絞って見せる
- `question_to_expect` は その制度で来やすい確認を先に潰すために使う
- `close_line` は 次に何を送るかを1文で締めるために使う
- `do_not_say` は 面談で claim level が跳ねるのを防ぐブレーキにする

### 93.2 強化版で守ること

- 最初の30秒で `制度に合う成果物` を言う
- 2枚目以降ではなく 1枚目で `今回残る物` を見せる
- 面談時間を埋めるための説明をしない
- 次回送付物は `1枚` `1表` `短いメモ` に留める

### 93.3 詳細版を引く場所

- 制度別の2回目面談テンプレ一覧は `MindUpload-EEGDATA-FundMap-second-meeting-plus.csv` を使う
- 列は `support_type`, `opening_30s`, `evidence_1`, `evidence_2`, `question_to_expect`, `close_line`, `do_not_say`

## 94. 共同研究先タイプ別のNDA前後で変える説明文

### 94.1 使い方

- `before_nda_line` は NDA 前の安全な説明として使う
- `after_nda_line` は NDA 後に具体度を上げる1文として使う
- `before_nda_focus` は NDA 前に何を見せるかを固定する
- `after_nda_focus` は NDA 後にどこまで具体化してよいかを固定する
- `stay_generic` は NDA 後でも一般論に留めるべき部分として使う

### 94.2 NDA 前後で守ること

- NDA 前は `比較条件`, `公開データ`, `成果物単位` までに留める
- NDA 後も 必要以上に全計画を開かない
- 相手タイプごとに 具体化してよい粒度を変える
- NDA を結んだことを理由に claim を大きくしない

### 94.3 詳細版を引く場所

- NDA 切替一覧は `MindUpload-EEGDATA-FundMap-nda-tone-switch.csv` を使う
- 列は `counterpart_type`, `before_nda_line`, `after_nda_line`, `before_nda_focus`, `after_nda_focus`, `stay_generic`, `avoid_point`

## 95. 25トピック別の四半期レビュー観点

### 95.1 使い方

- `quarter_goal` は 3か月で閉じるべき成果物の芯として使う
- `review_1` から `review_3` は 四半期末に yes/no で確認する項目として使う
- `keep_package` は 次四半期へ確実に渡す成果物束として使う
- `next_quarter_bridge` は 次の四半期で何に接続するかを1文で固定するために使う

### 95.2 四半期レビューで守ること

- 月ごとの進捗より `何が外に出せる形で閉じたか` を優先して見る
- 1四半期ごとに `増やす` のでなく `残す` を先に確定する
- 次四半期の接続先は 1本に絞る
- topic ごとの safe line を超える主張が混ざっていないかを最後に確認する

### 95.3 詳細版を引く場所

- topic 別の四半期レビュー一覧は `MindUpload-EEGDATA-FundMap-topic-quarterly-review.csv` を使う
- 列は `phase`, `topic`, `quarter_goal`, `review_1`, `review_2`, `review_3`, `keep_package`, `next_quarter_bridge`, `avoid_point`

## 96. 制度タイプ別の最終面談クロージング文

### 96.1 使い方

- `opening_line` は 終盤で何を持ち帰ってほしいかを固定する1文として使う
- `value_line` は 制度に合う価値を短く言い切る文として使う
- `evidence_line` は 面談中に見せた証拠を1つか2つに絞って回収する文として使う
- `next_line` は 次に送るものを1文で確定する文として使う
- `last_line` は 温度を保ったまま終える最後の1文として使う

### 96.2 クロージングで守ること

- 面談の最後で新しい話題を足さない
- 価値は制度に合わせて1本だけ言う
- 証拠は `図1枚` `表1枚` `短いメモ` の単位に戻す
- `do_not_say` に相当する危ない表現を最後に入れない

### 96.3 詳細版を引く場所

- 最終面談クロージング文の一覧は `MindUpload-EEGDATA-FundMap-final-meeting-close.csv` を使う
- 列は `support_type`, `opening_line`, `value_line`, `evidence_line`, `next_line`, `last_line`, `avoid_point`

## 97. 共同研究先タイプ別の first data share 前チェックリスト

### 97.1 使い方

- `check_1` から `check_3` は 共有前に必ず yes/no で確認する項目として使う
- `share_unit` は 最初に渡す単位を固定する
- `mask_rule` は 伏せるべき情報の粒度を固定する
- `note_line` は 送付メールの注意書き1文として使う

### 97.2 first data share 前に守ること

- 最初から全部渡さず `1枚` `1表` `最小サンプル` にする
- 公開EEG由来でも 相手との合意条件を超える整理をしない
- NDA の有無にかかわらず 不要な具体情報を外す
- 再送時に何を増やすかを最初の送付物に書かない

### 97.3 詳細版を引く場所

- first data share 前チェック一覧は `MindUpload-EEGDATA-FundMap-first-data-share-checklist.csv` を使う
- 列は `counterpart_type`, `check_1`, `check_2`, `check_3`, `share_unit`, `mask_rule`, `note_line`, `avoid_point`

## 98. 25トピック別の半年レビュー観点

### 98.1 使い方

- `halfyear_goal` は 半年で外に出す成果物の芯として使う
- `review_1` から `review_3` は 半年時点で yes/no で確認する項目として使う
- `keep_package` は 次の半年にも持ち越す成果物束として使う
- `next_halfyear_bridge` は 次の半年で何に接続するかを1文で固定するために使う

### 98.2 半年レビューで守ること

- 月次や四半期の積み上げより `外に見える形で残ったもの` を優先して見る
- 半年で増やしすぎた比較条件はここで止める
- 次の半年の接続先は `1本の benchmark 更新` か `1本の申請接続` に絞る
- topic ごとの安全域を越える主張が混ざっていないかを最後に確認する

### 98.3 詳細版を引く場所

- topic 別の半年レビュー一覧は `MindUpload-EEGDATA-FundMap-topic-halfyear-review.csv` を使う
- 列は `phase`, `topic`, `halfyear_goal`, `review_1`, `review_2`, `review_3`, `keep_package`, `next_halfyear_bridge`, `avoid_point`

## 99. 制度タイプ別の採択後キックオフ面談文

### 99.1 使い方

- `opening_line` は 採択後の最初の面談で scope を固定する1文として使う
- `scope_line` は 今回やることとやらないことを切る文として使う
- `deliverable_line` は 最初に残す成果物を言い切る文として使う
- `role_line` は こちらの担当と相手に期待する確認を短く言う文として使う
- `first_30d_line` は 初月で何を閉じるかを1文で示す文として使う

### 99.2 キックオフで守ること

- 採択直後ほど scope を広げない
- 初回面談では `最初の30日で何を残すか` を先に言う
- 制度に合う成果物を1つか2つに絞る
- 採択されたことを理由に強い主張へ寄せない

### 99.3 詳細版を引く場所

- 採択後キックオフ面談文の一覧は `MindUpload-EEGDATA-FundMap-post-award-kickoff.csv` を使う
- 列は `support_type`, `opening_line`, `scope_line`, `deliverable_line`, `role_line`, `first_30d_line`, `avoid_point`

## 100. 共同研究先タイプ別の成果公開前チェックリスト

### 100.1 使い方

- `check_1` から `check_3` は 公開直前に yes/no で確認する項目として使う
- `share_scope` は どこまで公開するかの粒度を固定する
- `approval_line` は 相手に確認するときの1文として使う
- `note_line` は 公開物に添える注意書きとして使う

### 100.2 成果公開前に守ること

- 公開する成果物は `図1枚` `表1枚` `短いメモ` の単位まで戻して確認する
- 公開範囲は NDA や利用条件より狭くすることはあっても広げない
- 相手タイプごとに確認したい論点を変える
- 公開前に新しい claim を足さない

### 100.3 詳細版を引く場所

- 成果公開前チェック一覧は `MindUpload-EEGDATA-FundMap-pre-publication-checklist.csv` を使う
- 列は `counterpart_type`, `check_1`, `check_2`, `check_3`, `share_scope`, `approval_line`, `note_line`, `avoid_point`

## 101. 25トピック別の年間レビュー観点

### 101.1 使い方

- `annual_goal` は 1年で外に残した成果物の芯として使う
- `review_1` から `review_3` は 年末に yes/no で確認する項目として使う
- `year_end_asset` は 翌年にも残す成果物束として使う
- `next_year_bridge` は 次年度に何へつなぐかを1文で固定するために使う

### 101.2 年間レビューで守ること

- 半年よりも `再利用された比較条件` と `外部に残った公共財` を優先して見る
- 年末に claim が広がっていたら package を小さく戻す
- 次年度接続は `benchmark 更新` `申請更新` `共同研究更新` のどれか1本に絞る
- mind-upload 実現論より `どこまで支えられたか` の評価軸を残す

### 101.3 詳細版を引く場所

- topic 別の年間レビュー一覧は `MindUpload-EEGDATA-FundMap-topic-annual-review.csv` を使う
- 列は `phase`, `topic`, `annual_goal`, `review_1`, `review_2`, `review_3`, `year_end_asset`, `next_year_bridge`, `avoid_point`

## 102. 制度タイプ別の成果報告会トークトラック

### 102.1 使い方

- `opening_line` は 最初の15秒で何を残したかを言う文として使う
- `core_line` は 今回やった範囲を切って示す文として使う
- `evidence_line` は 図表や成果物を1点だけ示す文として使う
- `reuse_line` は この成果が次にどう再利用されるかを示す文として使う
- `closing_line` は 最後の締めと次の小さな接続を言う文として使う

### 102.2 成果報告会で守ること

- 報告は ambition ではなく `残った成果物` から始める
- 図表は `1枚` `1表` `1 notebook` のどれかに絞る
- 次段の話は広げず `次に何へ接続するか` だけを短く言う
- 採択や受賞を理由に claim を強くしない

### 102.3 詳細版を引く場所

- 制度タイプ別の成果報告会トークトラックは `MindUpload-EEGDATA-FundMap-reportback-talk.csv` を使う
- 列は `support_type`, `opening_line`, `core_line`, `evidence_line`, `reuse_line`, `closing_line`, `avoid_point`

## 103. 共同研究先タイプ別の公開後フォロー文面

### 103.1 使い方

- `timing` は 公開後いつ連絡するかの目安として使う
- `opening_line` は URL と公開報告を添える最初の1文として使う
- `summary_line` は 相手に関係する要点だけを短く伝える文として使う
- `next_step_line` は 次に頼むことを最小単位で示す文として使う
- `keep_warm_line` は 関係を切らさず保つ短い文として使う

### 103.2 公開後フォローで守ること

- 公開後 `48時間から72時間` 以内に短く送る
- 相手の貢献を広く言いすぎず 公開済み範囲だけで謝意を示す
- 次のお願いは `10分確認` `1枚共有` `短い打合せ` の単位まで小さくする
- 公開直後に新しい大型提案へ飛ばない

### 103.3 詳細版を引く場所

- 共同研究先タイプ別の公開後フォロー文面は `MindUpload-EEGDATA-FundMap-post-publication-followup.csv` を使う
- 列は `counterpart_type`, `timing`, `opening_line`, `summary_line`, `next_step_line`, `keep_warm_line`, `avoid_point`

## 104. 25トピック別の翌年度開始メモ

### 104.1 使い方

- `opening_line` は 翌年度最初の打合せで言う冒頭1文として使う
- `checkpoint_1` と `checkpoint_2` は 初月に yes/no で閉じる確認項目として使う
- `first_asset` は 年度初めに最初に更新する成果物として使う
- `first_bridge` は その更新先を1本に絞る文として使う

### 104.2 翌年度開始で守ること

- 前年の成果物を作り直さず `更新版を1つ` だけ作る
- 年度初めに比較条件や課題数を増やしすぎない
- 最初の checkpoint は `2個` までに絞る
- 翌年度の接続先は `benchmark` `申請` `共同研究` のどれか1本に固定する

### 104.3 詳細版を引く場所

- topic 別の翌年度開始メモは `MindUpload-EEGDATA-FundMap-topic-next-year-start.csv` を使う
- 列は `phase`, `topic`, `opening_line`, `checkpoint_1`, `checkpoint_2`, `first_asset`, `first_bridge`, `avoid_point`

## 105. 制度タイプ別の最終成果物1枚要約

### 105.1 使い方

- `headline` は 1枚上部に置く題名として使う
- `summary_box` は 今回残った成果物の要点として使う
- `evidence_box` は 図表や notebook などの証拠枠として使う
- `reuse_box` は 次にどこで再利用されるかを示す枠として使う
- `footer_line` は 最後に添える締めの1文として使う

### 105.2 1枚要約で守ること

- 1枚要約は `やった作業` ではなく `残った成果物` から書く
- 証拠は `図1枚` `表1枚` `notebook 1本` のどれか1単位に絞る
- 次利用先は `1本` だけ書く
- 将来計画を足しすぎて最終成果の密度を薄めない

### 105.3 詳細版を引く場所

- 制度タイプ別の最終成果物1枚要約は `MindUpload-EEGDATA-FundMap-final-deliverable-onepager.csv` を使う
- 列は `support_type`, `headline`, `summary_box`, `evidence_box`, `reuse_box`, `footer_line`, `avoid_point`

## 106. 共同研究先タイプ別の再接続タイミング表

### 106.1 使い方

- `reconnect_timing` は 再接続の目安時期として使う
- `reconnect_trigger` は 連絡してよい条件を固定するために使う
- `opening_line` は 再接続時の最初の1文として使う
- `ask_unit` は 最初にお願いする最小単位として使う
- `keep_warm_line` は 今回動かなくても関係を保つ文として使う

### 106.2 再接続で守ること

- 再接続は `新しい1枚` `新しい判断点` `新しい短い成果物` が出たときだけにする
- 最初の依頼は `10分` `1枚` `1論点` の単位まで小さくする
- 止まっていた論点を一気に全部開かない
- 反応が弱いときは keep warm だけ残して次の節目まで待つ

### 106.3 詳細版を引く場所

- 共同研究先タイプ別の再接続タイミング表は `MindUpload-EEGDATA-FundMap-collab-reconnect-timing.csv` を使う
- 列は `counterpart_type`, `reconnect_timing`, `reconnect_trigger`, `opening_line`, `ask_unit`, `keep_warm_line`, `avoid_point`

## 107. 25トピック別の翌年度Q1タスク

### 107.1 使い方

- `q1_goal` は 翌年度Q1で閉じる目標として使う
- `task_1` から `task_3` は 最初の四半期で順に実行する3タスクとして使う
- `q1_deliverable` は Q1末に外へ出す成果物束として使う
- `avoid_point` は Q1で広げすぎないための制約として使う

### 107.2 Q1で守ること

- Q1は `更新版1本` `確認2点` `外部共有1回` の単位までに絞る
- `task_1` は 前年度資産の更新に使う
- `task_2` は failure mode や除外条件の確認に使う
- `task_3` は 外部共有可能な最小 package を作ることに使う

### 107.3 詳細版を引く場所

- topic 別の翌年度Q1タスクは `MindUpload-EEGDATA-FundMap-topic-next-year-q1.csv` を使う
- 列は `phase`, `topic`, `q1_goal`, `task_1`, `task_2`, `task_3`, `q1_deliverable`, `avoid_point`

## 108. 制度タイプ別の最終報告メール文面

### 108.1 使い方

- `subject_line` は 件名として使う
- `opening_line` は 送付目的と感謝をまとめる冒頭1文として使う
- `summary_line` は 今回残った成果物を短く言う文として使う
- `attachment_line` は 添付物やURLの説明として使う
- `next_line` は 今後の接続を最小単位で添える文として使う

### 108.2 最終報告メールで守ること

- メール本文は `感謝` `残った成果物` `添付物` `次の小さな接続` の順で書く
- 将来構想を長く書かない
- 添付は `1枚` `1表` `1リンク` 程度に絞る
- 制度の終了報告と次の営業提案を同じ文面で混ぜない

### 108.3 詳細版を引く場所

- 制度タイプ別の最終報告メール文面は `MindUpload-EEGDATA-FundMap-final-report-mail.csv` を使う
- 列は `support_type`, `subject_line`, `opening_line`, `summary_line`, `attachment_line`, `next_line`, `avoid_point`

## 109. 共同研究先タイプ別の再接続後初回面談メモ

### 109.1 使い方

- `meeting_goal` は その面談で閉じる目的として使う
- `agenda_1` と `agenda_2` は 先に置く2論点として使う
- `ask_line` は 最後に頼む最小単位の依頼文として使う
- `note_line` は 面談メモ末尾に残す1文として使う

### 109.2 初回面談で守ること

- 面談目的は `状況確認` `1論点の確認` `次の小さな共有` に絞る
- agenda は `2つ` までにする
- ask は `10分確認` `1枚レビュー` `短い再打合せ` の単位まで小さくする
- 再接続後の初回から大型計画へ飛ばない

### 109.3 詳細版を引く場所

- 共同研究先タイプ別の再接続後初回面談メモは `MindUpload-EEGDATA-FundMap-reconnect-first-meeting.csv` を使う
- 列は `counterpart_type`, `meeting_goal`, `agenda_1`, `agenda_2`, `ask_line`, `note_line`, `avoid_point`

## 110. 25トピック別の翌年度Q2タスク

### 110.1 使い方

- `q2_goal` は 翌年度Q2で閉じる目標として使う
- `task_1` から `task_3` は Q2で順に実行する3タスクとして使う
- `q2_deliverable` は Q2末に外へ出す成果物束として使う
- `avoid_point` は Q2で比較条件や claim を広げすぎないための制約として使う

### 110.2 Q2で守ること

- Q2は `更新版1本` `共有先1つ` `比較条件の固定` の単位に絞る
- `task_1` は Q1で作った更新版の安定化に使う
- `task_2` は 外部比較か共同確認の1回だけに使う
- `task_3` は 次の申請や共同作業に流せる最小 package を作ることに使う

### 110.3 詳細版を引く場所

- topic 別の翌年度Q2タスクは `MindUpload-EEGDATA-FundMap-topic-next-year-q2.csv` を使う
- 列は `phase`, `topic`, `q2_goal`, `task_1`, `task_2`, `task_3`, `q2_deliverable`, `avoid_point`

## 111. 制度タイプ別の最終成果物提出チェック

### 111.1 使い方

- `check_1` から `check_3` は 提出前に yes/no で確認する項目として使う
- `submit_unit` は 実際に提出する単位を固定するために使う
- `note_line` は 送付時の注意書き1文として使う
- `avoid_point` は 提出直前に起こりやすい過剰追加を止めるために使う

### 111.2 提出前に守ること

- 提出物は `1枚` `1表` `1リンク` `短い本文` の単位まで戻して確認する
- 報告用資料と営業用資料を混ぜない
- 感謝文と成果要約は短く分けて書く
- 提出直前に新しい claim や未確認の図表を足さない

### 111.3 詳細版を引く場所

- 制度タイプ別の最終成果物提出チェックは `MindUpload-EEGDATA-FundMap-final-deliverable-submit-check.csv` を使う
- 列は `support_type`, `check_1`, `check_2`, `check_3`, `submit_unit`, `note_line`, `avoid_point`

## 112. 共同研究先タイプ別の再接続後30日運用

### 112.1 使い方

- `day_7` `day_14` `day_30` は 再接続後30日でいつ何をするかの目安として使う
- `success_signal` は 継続してよい合図として使う
- `hold_signal` は いったん止める合図として使う
- `avoid_point` は 30日内に関係を壊しやすい動きを避けるために使う

### 112.2 30日運用で守ること

- 30日でやることは `共有` `確認` `次の小さな依頼` の3段階までに絞る
- `day_7` は 前回面談のメモ共有に使う
- `day_14` は 1論点の確認に使う
- `day_30` は 続けるか保留にするかを短く切るために使う

### 112.3 詳細版を引く場所

- 共同研究先タイプ別の再接続後30日運用は `MindUpload-EEGDATA-FundMap-reconnect-30days.csv` を使う
- 列は `counterpart_type`, `day_7`, `day_14`, `day_30`, `success_signal`, `hold_signal`, `avoid_point`

## 113. 25トピック別の翌年度Q3タスク

### 113.1 使い方

- `q3_goal` は 翌年度Q3で閉じる目標として使う
- `task_1` から `task_3` は Q3で順に実行する3タスクとして使う
- `q3_deliverable` は Q3末に外へ出す成果物束として使う
- `avoid_point` は Q3で scope と claim を広げすぎないための制約として使う

### 113.2 Q3で守ること

- Q3は `安定版1本` `再利用先1つ` `年末へつなぐ短いメモ` の単位に絞る
- `task_1` は Q2で安定化した成果物の最終確認に使う
- `task_2` は 再利用先か共同先への小さな受け渡しに使う
- `task_3` は 年末レビューへつなぐメモを残すことに使う

### 113.3 詳細版を引く場所

- topic 別の翌年度Q3タスクは `MindUpload-EEGDATA-FundMap-topic-next-year-q3.csv` を使う
- 列は `phase`, `topic`, `q3_goal`, `task_1`, `task_2`, `task_3`, `q3_deliverable`, `avoid_point`

## 114. 制度タイプ別の最終成果物アーカイブチェック

### 114.1 使い方

- `check_1` から `check_3` は 保存前に yes/no で確認する項目として使う
- `archive_unit` は 保存する単位を固定するために使う
- `note_line` は アーカイブ時の注意書き1文として使う
- `avoid_point` は 保存直前に起こりやすい混在や過剰追加を止めるために使う

### 114.2 アーカイブ前に守ること

- 保存物は `最終版` `公開版` `内部メモ` を分ける
- 送付用と保存用を同じフォルダ構造で混ぜない
- 将来計画や営業文面は成果物アーカイブに入れすぎない
- 保存直前に未確認ファイルを紛れ込ませない

### 114.3 詳細版を引く場所

- 制度タイプ別の最終成果物アーカイブチェックは `MindUpload-EEGDATA-FundMap-final-archive-check.csv` を使う
- 列は `support_type`, `check_1`, `check_2`, `check_3`, `archive_unit`, `note_line`, `avoid_point`

## 115. 共同研究先タイプ別の再接続後60日レビュー

### 115.1 使い方

- `day_45` は 45日前後で確認する動きとして使う
- `day_60` は 60日で切る判断として使う
- `review_point` は 60日レビューで見る論点として使う
- `continue_signal` は 続ける根拠として使う
- `stop_signal` は ここで止める根拠として使う

### 115.2 60日レビューで守ること

- 60日で見るのは `返答の質` `共有単位の維持` `次の小さな前進` の3点だけにする
- `day_45` は 前回合意の履行確認に使う
- `day_60` は 続けるか保留にするかを短く切るために使う
- 反応が弱いときに大型提案で押し込まない

### 115.3 詳細版を引く場所

- 共同研究先タイプ別の再接続後60日レビューは `MindUpload-EEGDATA-FundMap-reconnect-60days.csv` を使う
- 列は `counterpart_type`, `day_45`, `day_60`, `review_point`, `continue_signal`, `stop_signal`, `avoid_point`

## 116. 25トピック別の翌年度Q4タスク

### 116.1 使い方

- `q4_goal` は 翌年度Q4で閉じる目標として使う
- `task_1` から `task_3` は Q4で順に実行する3タスクとして使う
- `q4_deliverable` は Q4末に外へ出す成果物束として使う
- `avoid_point` は Q4で年末処理と claim を混ぜすぎないための制約として使う

### 116.2 Q4で守ること

- Q4は `年末前版1本` `年次レビュー接続1つ` `次年度へ残すメモ1つ` の単位に絞る
- `task_1` は Q3で閉じた成果物の年末前確認に使う
- `task_2` は 年次レビューや最終共有へつなぐ短い整理に使う
- `task_3` は 次年度へ残す最小メモを置くことに使う

### 116.3 詳細版を引く場所

- topic 別の翌年度Q4タスクは `MindUpload-EEGDATA-FundMap-topic-next-year-q4.csv` を使う
- 列は `phase`, `topic`, `q4_goal`, `task_1`, `task_2`, `task_3`, `q4_deliverable`, `avoid_point`

## 117. 制度タイプ別の最終成果物公開チェック

### 117.1 使い方

- `check_1` から `check_3` は 公開前に yes/no で確認する項目として使う
- `public_unit` は 実際に公開する単位を固定するために使う
- `note_line` は 公開時の注意書き1文として使う
- `avoid_point` は 公開直前に起こりやすい過剰説明や混在を止めるために使う

### 117.2 公開前に守ること

- 公開物は `図1枚` `表1枚` `短い本文` `リンク1本` の単位まで戻して確認する
- 保存版と公開版を同じ説明で出し分けない
- 感謝や制度説明は短くし 成果物の説明を中心に置く
- 公開直前に未確認の claim や内部メモを混ぜない

### 117.3 詳細版を引く場所

- 制度タイプ別の最終成果物公開チェックは `MindUpload-EEGDATA-FundMap-final-publication-check.csv` を使う
- 列は `support_type`, `check_1`, `check_2`, `check_3`, `public_unit`, `note_line`, `avoid_point`

## 118. 共同研究先タイプ別の再接続後90日レビュー

### 118.1 使い方

- `day_75` は 75日前後で確認する動きとして使う
- `day_90` は 90日で続けるか閉じるかを切る判断として使う
- `review_point` は 90日レビューで見る論点として使う
- `continue_signal` は 継続してよい根拠として使う
- `close_signal` は ここで関係を一度閉じる根拠として使う

### 118.2 90日レビューで守ること

- 90日で見るのは `前進の有無` `共有単位の維持` `次の接点の現実性` の3点だけにする
- `day_75` は 直近の共有や約束が保たれているかの確認に使う
- `day_90` は 続けるか一旦閉じるかを短く明確に切るために使う
- 反応が弱いときに長文提案や大型構想で延命しない

### 118.3 詳細版を引く場所

- 共同研究先タイプ別の再接続後90日レビューは `MindUpload-EEGDATA-FundMap-reconnect-90days.csv` を使う
- 列は `counterpart_type`, `day_75`, `day_90`, `review_point`, `continue_signal`, `close_signal`, `avoid_point`

## 119. 25トピック別の翌年度年末クローズメモ

### 119.1 使い方

- `closing_line` は 年末に topic をどう閉じるかの1文として使う
- `close_check_1` と `close_check_2` は 年末に yes/no で確認する項目として使う
- `carryover_asset` は 次年度に残す成果物束として使う
- `next_cycle_line` は 次の循環へどう接続するかを1文で固定するために使う

### 119.2 年末クローズで守ること

- 年末は `残った成果物` `切った論点` `次に残す最小単位` の3つだけに絞る
- 年末時点で広がった比較条件はここで止める
- carry over は `1枚` `1表` `1メモ` の単位まで小さくする
- mind-upload 実現論ではなく 評価軸と公共財が残ったかで閉じる

### 119.3 詳細版を引く場所

- topic 別の翌年度年末クローズメモは `MindUpload-EEGDATA-FundMap-topic-next-year-close.csv` を使う
- 列は `phase`, `topic`, `closing_line`, `close_check_1`, `close_check_2`, `carryover_asset`, `next_cycle_line`, `avoid_point`

## 120. 制度タイプ別の最終成果物公開後フォロー

### 120.1 使い方

- `timing` は 公開後いつ送るかの目安として使う
- `opening_line` は URL と公開報告を添える最初の1文として使う
- `summary_line` は 今回公開した成果物の芯を短く伝える文として使う
- `reuse_line` は 次にどこで再利用されるかを示す文として使う
- `next_line` は 今後の接続を最小単位で添える文として使う

### 120.2 公開後フォローで守ること

- 公開後 `48時間から72時間` 以内に短く送る
- 制度への感謝と成果物の説明を分けて書く
- 次の接続は `更新1回` `共有1回` `短い相談1回` の単位まで小さくする
- 公開直後に新しい大きな提案へ飛ばない

### 120.3 詳細版を引く場所

- 制度タイプ別の最終成果物公開後フォローは `MindUpload-EEGDATA-FundMap-final-publication-followup.csv` を使う
- 列は `support_type`, `timing`, `opening_line`, `summary_line`, `reuse_line`, `next_line`, `avoid_point`

## 121. 共同研究先タイプ別の再接続クローズ文面

### 121.1 使い方

- `timing` は クローズ連絡を送る時期として使う
- `opening_line` は これまでのやり取りへの感謝を添える最初の1文として使う
- `summary_line` は 今回ここで区切る理由を短く伝える文として使う
- `close_line` は 今回のやり取りを一度閉じる文として使う
- `keep_warm_line` は 将来の再接点を残す短い文として使う

### 121.2 クローズ文面で守ること

- close は `感謝` `現状の整理` `一旦閉じる` `将来の余地` の順で書く
- 相手の負担や非を匂わせない
- 次の連絡を強制せず 余地だけ残す
- 長文で正当化しない

### 121.3 詳細版を引く場所

- 共同研究先タイプ別の再接続クローズ文面は `MindUpload-EEGDATA-FundMap-collab-reconnect-close.csv` を使う
- 列は `counterpart_type`, `timing`, `opening_line`, `summary_line`, `close_line`, `keep_warm_line`, `avoid_point`

## 122. 25トピック別の次年度初動総括

### 122.1 使い方

- `summary_line` は 次年度の最初に何を残して始めるかの1文として使う
- `keep_point_1` と `keep_point_2` は 初動で崩してはいけない確認点として使う
- `restart_asset` は 次年度最初に触る成果物束として使う
- `first_direction` は 初動で向かう先を1本に固定するために使う

### 122.2 初動総括で守ること

- 初動は `残す資産` `維持する条件` `向かう先1本` の3点だけに絞る
- 前年度の作業棚卸しを長くやりすぎない
- restart asset は `1枚` `1表` `1メモ` の単位まで小さくする
- 強い主張ではなく `再利用可能な公共財` を起点にする

### 122.3 詳細版を引く場所

- topic 別の次年度初動総括は `MindUpload-EEGDATA-FundMap-topic-next-cycle-summary.csv` を使う
- 列は `phase`, `topic`, `summary_line`, `keep_point_1`, `keep_point_2`, `restart_asset`, `first_direction`, `avoid_point`

## 123. 制度タイプ別の公開後30日レビュー

### 123.1 使い方

- `day_7` は 公開後1週間で確認する動きとして使う
- `day_30` は 30日で切るレビュー動作として使う
- `review_point` は 30日レビューで見る論点として使う
- `good_signal` は 継続してよい合図として使う
- `next_line` は 次の小さな接続を添える文として使う

### 123.2 公開後30日で守ること

- 30日で見るのは `公開物の届き方` `再利用の芽` `次の小さな接続` の3点だけにする
- `day_7` は 到達確認と簡単な補足に使う
- `day_30` は 続けるなら何を1つ更新するかを切るために使う
- 公開直後の熱量で大きな追加提案へ飛ばない

### 123.3 詳細版を引く場所

- 制度タイプ別の公開後30日レビューは `MindUpload-EEGDATA-FundMap-publication-30days-review.csv` を使う
- 列は `support_type`, `day_7`, `day_30`, `review_point`, `good_signal`, `next_line`, `avoid_point`

## 124. 共同研究先タイプ別の再開文面

### 124.1 使い方

- `timing` は 再開連絡を送る時期として使う
- `opening_line` は 前回からの間を自然につなぐ最初の1文として使う
- `summary_line` は 今回再開する理由を短く伝える文として使う
- `reopen_line` は 再開したい内容を最小単位で示す文として使う
- `scope_line` は 今回広げない範囲を切る文として使う

### 124.2 再開文面で守ること

- reopen は `近況` `再開理由` `最小依頼` `広げない範囲` の順で書く
- 以前止まった理由を蒸し返さない
- ask は `10分確認` `1枚共有` `1論点` の単位まで小さくする
- いきなり大型共同研究の再始動にしない

### 124.3 詳細版を引く場所

- 共同研究先タイプ別の再開文面は `MindUpload-EEGDATA-FundMap-collab-reopen-lines.csv` を使う
- 列は `counterpart_type`, `timing`, `opening_line`, `summary_line`, `reopen_line`, `scope_line`, `avoid_point`

## 125. 25トピック別の次年度1ページ戦略メモ

### 125.1 使い方

- `headline` は 1ページ上部に置く題名として使う
- `why_now` は 次年度にその topic を動かす理由を短く置く文として使う
- `core_asset` は 起点にする成果物束として使う
- `first_move` は 最初にやる1動作として使う
- `success_line` は その1ページで最後に言い切る成功条件として使う

### 125.2 1ページ戦略で守ること

- 1ページには `なぜ今か` `何を起点にするか` `最初の1動作` だけを置く
- 前年度の履歴を全部載せない
- `core_asset` は `1枚` `1表` `1メモ` の束までに絞る
- success は 強い主張ではなく `再利用可能な更新` として書く

### 125.3 詳細版を引く場所

- topic 別の次年度1ページ戦略メモは `MindUpload-EEGDATA-FundMap-topic-strategy-onepager.csv` を使う
- 列は `phase`, `topic`, `headline`, `why_now`, `core_asset`, `first_move`, `success_line`, `avoid_point`

## 126. 制度タイプ別の公開後90日レビュー

### 126.1 使い方

- `day_30` は 中間確認としての動きに使う
- `day_90` は 90日で何を切るかの動きに使う
- `review_point` は 90日レビューで見る論点として使う
- `continue_signal` は 続けてよい合図として使う
- `reset_line` は 次の1件へ切り替える文として使う

### 126.2 公開後90日で守ること

- 90日で見るのは `届き方` `再利用の実在` `次の1更新` の3点だけにする
- `day_30` で反応を集めきれなくても 90日で1件に切る
- 反応の量より `次に何を1つ更新するか` を重視する
- 公開物が受けたことを理由に急に claim を強めない

### 126.3 詳細版を引く場所

- 制度タイプ別の公開後90日レビューは `MindUpload-EEGDATA-FundMap-publication-90days-review.csv` を使う
- 列は `support_type`, `day_30`, `day_90`, `review_point`, `continue_signal`, `reset_line`, `avoid_point`

## 127. 共同研究先タイプ別の再開後初回メール返信テンプレ

### 127.1 使い方

- `reply_trigger` は どんな返信が来た時に使うかの目安として使う
- `opening_line` は 返信の冒頭1文として使う
- `answer_line` は 相手への応答を短く返す文として使う
- `next_step_line` は 次の最小動作を置く文として使う
- `scope_line` は 今回広げない範囲を切る文として使う

### 127.2 返信テンプレで守ること

- 返信は `感謝` `応答` `次の小さな1歩` `広げない範囲` の順で書く
- 相手の返信量に合わせて短く返す
- next step は `10分` `1枚` `1論点` の単位まで小さくする
- 好反応でもいきなり大型再始動にしない

### 127.3 詳細版を引く場所

- 共同研究先タイプ別の再開後初回メール返信テンプレは `MindUpload-EEGDATA-FundMap-collab-reopen-reply.csv` を使う
- 列は `counterpart_type`, `reply_trigger`, `opening_line`, `answer_line`, `next_step_line`, `scope_line`, `avoid_point`

## 128. 25トピック別の次年度3か月戦略

### 128.1 使い方

- `quarter_goal` は 次年度最初の3か月で閉じる目標として使う
- `month_1` から `month_3` は 月ごとの最小動作として使う
- `quarter_deliverable` は 3か月後に外へ出す成果物束として使う
- `avoid_point` は 3か月で広げすぎないための制約として使う

### 128.2 3か月戦略で守ること

- 3か月は `更新1件` `確認1件` `共有1件` の束までに絞る
- `month_1` は 起点資産の更新に使う
- `month_2` は 条件や failure mode の確認に使う
- `month_3` は 外に出せる最小 package を作ることに使う

### 128.3 詳細版を引く場所

- topic 別の次年度3か月戦略は `MindUpload-EEGDATA-FundMap-topic-next-cycle-3month.csv` を使う
- 列は `phase`, `topic`, `quarter_goal`, `month_1`, `month_2`, `month_3`, `quarter_deliverable`, `avoid_point`

## 129. 制度タイプ別の公開後半年レビュー

### 129.1 使い方

- `day_90` は 中間確認の起点として使う
- `halfyear` は 半年で何を切るかのレビュー動作として使う
- `review_point` は 半年レビューで見る論点として使う
- `continue_signal` は 続けてよい合図として使う
- `reset_line` は 次の1件に切り替える文として使う

### 129.2 公開後半年で守ること

- 半年で見るのは `再利用の実在` `残った成果物` `次の1更新` の3点だけにする
- 反応が多くても update は `1件` に絞る
- 半年レビューは 実績整理であって大きな将来像の拡張ではない
- 公開後の反応を根拠に claim を強めない

### 129.3 詳細版を引く場所

- 制度タイプ別の公開後半年レビューは `MindUpload-EEGDATA-FundMap-publication-halfyear-review.csv` を使う
- 列は `support_type`, `day_90`, `halfyear`, `review_point`, `continue_signal`, `reset_line`, `avoid_point`

## 130. 共同研究先タイプ別の再開後2通目返信テンプレ

### 130.1 使い方

- `reply_trigger` は 2通目を送る場面の目安として使う
- `opening_line` は 返信の冒頭1文として使う
- `answer_line` は 1通目を受けた追加応答として使う
- `next_step_line` は 次の最小動作を再確認する文として使う
- `scope_line` は 今回広げない範囲を切る文として使う

### 130.2 2通目返信で守ること

- 2通目は `感謝` `追加応答` `次の1歩` `広げない範囲` の順で書く
- 1通目より短くする
- next step は なお `10分` `1枚` `1論点` の単位までに留める
- 好反応でも一気に論点を増やさない

### 130.3 詳細版を引く場所

- 共同研究先タイプ別の再開後2通目返信テンプレは `MindUpload-EEGDATA-FundMap-collab-reopen-second-reply.csv` を使う
- 列は `counterpart_type`, `reply_trigger`, `opening_line`, `answer_line`, `next_step_line`, `scope_line`, `avoid_point`

## 131. 25トピック別の次年度6か月戦略

### 131.1 使い方

- `halfyear_goal` は 次年度最初の6か月で閉じる目標として使う
- `month_1_2` `month_3_4` `month_5_6` は 2か月単位の最小動作として使う
- `halfyear_deliverable` は 6か月後に外へ出す成果物束として使う
- `avoid_point` は 6か月で scope を広げすぎないための制約として使う

### 131.2 6か月戦略で守ること

- 6か月は `更新1件` `比較確認1件` `共有先1つ` の束までに絞る
- `month_1_2` は 起点資産の更新に使う
- `month_3_4` は 条件と failure mode の安定化に使う
- `month_5_6` は 外へ出す安定版 package を作ることに使う

### 131.3 詳細版を引く場所

- topic 別の次年度6か月戦略は `MindUpload-EEGDATA-FundMap-topic-next-cycle-6month.csv` を使う
- 列は `phase`, `topic`, `halfyear_goal`, `month_1_2`, `month_3_4`, `month_5_6`, `halfyear_deliverable`, `avoid_point`

## 132. 制度タイプ別の公開後1年レビュー

### 132.1 使い方

- `halfyear` は 中間確認としての動きに使う
- `one_year` は 1年で何を切るかのレビュー動作として使う
- `review_point` は 1年レビューで見る論点として使う
- `continue_signal` は 続けてよい合図として使う
- `reset_line` は 次の1年で何を1件だけ続けるかを示す文として使う

### 132.2 公開後1年で守ること

- 1年で見るのは `残った成果物` `再利用の実在` `次の1更新` の3点だけにする
- 活動が多くても 次に続ける更新は `1件` に絞る
- 1年レビューは 価値が残った形を見る場であり 夢を膨らませる場ではない
- 公開後の反応を根拠に claim を強めない

### 132.3 詳細版を引く場所

- 制度タイプ別の公開後1年レビューは `MindUpload-EEGDATA-FundMap-publication-1year-review.csv` を使う
- 列は `support_type`, `halfyear`, `one_year`, `review_point`, `continue_signal`, `reset_line`, `avoid_point`

## 133. 共同研究先タイプ別の再開後3通目返信テンプレ

### 133.1 使い方

- `reply_trigger` は 3通目を送る場面の目安として使う
- `opening_line` は 返信の冒頭1文として使う
- `answer_line` は これまでの往復を受けた短い応答として使う
- `next_step_line` は 次の最小動作を最後に置く文として使う
- `scope_line` は 今回広げない範囲を切る文として使う

### 133.2 3通目返信で守ること

- 3通目は `感謝` `整理` `次の1歩` `広げない範囲` の順で書く
- 1通目と2通目よりさらに短くする
- next step は 引き続き `10分` `1枚` `1論点` の単位までに留める
- 往復が続いても大型再始動へ飛ばない

### 133.3 詳細版を引く場所

- 共同研究先タイプ別の再開後3通目返信テンプレは `MindUpload-EEGDATA-FundMap-collab-reopen-third-reply.csv` を使う
- 列は `counterpart_type`, `reply_trigger`, `opening_line`, `answer_line`, `next_step_line`, `scope_line`, `avoid_point`

## 134. 25トピック別の次年度年次戦略

### 134.1 使い方

- `annual_goal` は 次年度1年で閉じる目標として使う
- `quarter_1_2` と `quarter_3_4` は 上期/下期の最小動作として使う
- `year_deliverable` は 年末に外へ出す成果物束として使う
- `avoid_point` は 年次戦略で広げすぎないための制約として使う

### 134.2 年次戦略で守ること

- 1年は `更新1件` `共有先1つ` `年末版1束` の単位に絞る
- `quarter_1_2` は 起点資産の更新と安定化に使う
- `quarter_3_4` は 外へ出す年末版 package を作ることに使う
- 年次戦略は claim を足すより `再利用可能な更新` を残すことを優先する

### 134.3 詳細版を引く場所

- topic 別の次年度年次戦略は `MindUpload-EEGDATA-FundMap-topic-next-cycle-annual.csv` を使う
- 列は `phase`, `topic`, `annual_goal`, `quarter_1_2`, `quarter_3_4`, `year_deliverable`, `next_anchor`, `avoid_point`

## 135. 制度タイプ別の公開後クローズ判断

### 135.1 使い方

- `review_timing` は クローズ判断を置く時期として使う
- `close_condition` は ここで閉じてよい条件として使う
- `keep_condition` は まだ続ける条件として使う
- `close_line` は クローズ判断を短く伝える文として使う
- `reset_line` は 次に残す1件を示す文として使う

### 135.2 クローズ判断で守ること

- クローズ判断は `残った成果物` `再利用の実在` `次に残す1件` の3点だけで切る
- 活動量ではなく 再利用可能な形が残ったかを見る
- close しても次に残す更新は `1件` にする
- クローズ判断を将来像の拡張に使わない

### 135.3 詳細版を引く場所

- 制度タイプ別の公開後クローズ判断は `MindUpload-EEGDATA-FundMap-publication-close-decision.csv` を使う
- 列は `support_type`, `review_timing`, `close_condition`, `keep_condition`, `close_line`, `reset_line`, `avoid_point`

## 136. 共同研究先タイプ別の再開後クローズ返信テンプレ

### 136.1 使い方

- `reply_trigger` は クローズ返信を送る場面の目安として使う
- `opening_line` は 返信の冒頭1文として使う
- `answer_line` は ここまでの往復を踏まえた短い整理として使う
- `close_line` は 今回の往復をここで閉じる文として使う
- `scope_line` は 今回広げない範囲を切る文として使う

### 136.2 クローズ返信で守ること

- 返信は `感謝` `整理` `ここで閉じる` `広げない範囲` の順で書く
- 相手の反応不足を責めない
- 次に残す余地は書いても 再始動を強制しない
- 長文で弁明しない

### 136.3 詳細版を引く場所

- 共同研究先タイプ別の再開後クローズ返信テンプレは `MindUpload-EEGDATA-FundMap-collab-reopen-close-reply.csv` を使う
- 列は `counterpart_type`, `reply_trigger`, `opening_line`, `answer_line`, `close_line`, `scope_line`, `avoid_point`

## 137. 25トピック別の複数年ロードマップ要約

### 137.1 使い方

- `year_1_focus` は 直近1年で集中する軸として使う
- `year_2_focus` は 2年目に広げる軸として使う
- `year_3_focus` は 3年目に残す軸として使う
- `long_tail_asset` は 複数年をまたいで残す成果物束として使う
- `avoid_point` は 年数を伸ばした時に暴走しやすい論点を切るために使う

### 137.2 複数年ロードマップで守ること

- 複数年でも `年ごとに1本` の更新軸までに絞る
- year 1 は benchmark か比較表の更新に寄せる
- year 2 は 再利用条件か共有先の拡張に寄せる
- year 3 は 公共財として残る形の固定に寄せる

### 137.3 詳細版を引く場所

- topic 別の複数年ロードマップ要約は `MindUpload-EEGDATA-FundMap-topic-multiyear-roadmap.csv` を使う
- 列は `phase`, `topic`, `year_1_focus`, `year_2_focus`, `year_3_focus`, `long_tail_asset`, `avoid_point`

## 138. 制度タイプ別の公開後アーカイブ運用

### 138.1 使い方

- `archive_timing` は いつ保存系の整理をするかの目安として使う
- `archive_unit` は 保存する最小単位として使う
- `archive_check` は 保存時に必ず見る確認点として使う
- `revisit_trigger` は 再度アーカイブを開く条件として使う
- `note_line` は アーカイブ運用メモの1文として使う

### 138.2 公開後アーカイブ運用で守ること

- アーカイブは `公開版` `保存版` `内部メモ` を混ぜない
- reopen 条件は `更新1件` `利用1件` `確認1件` の単位までにする
- 保存量ではなく 再利用しやすい束になっているかを見る
- 保存運用を将来提案の棚にしない

### 138.3 詳細版を引く場所

- 制度タイプ別の公開後アーカイブ運用は `MindUpload-EEGDATA-FundMap-publication-archive-ops.csv` を使う
- 列は `support_type`, `archive_timing`, `archive_unit`, `archive_check`, `revisit_trigger`, `note_line`, `avoid_point`

## 139. 共同研究先タイプ別の再始動判断ルーブリック

### 139.1 使い方

- `go_signal` は 再始動してよい合図として使う
- `hold_signal` は まだ保留にすべき合図として使う
- `stop_signal` は 今回は止めるべき合図として使う
- `minimum_restart_unit` は 再始動する時の最小単位として使う
- `reason_line` は 判断理由を短く言う文として使う

### 139.2 再始動判断で守ること

- 判断は `go` `hold` `stop` の3択で切る
- 再始動しても `10分` `1枚` `1論点` の単位を超えない
- go の根拠は 温度感ではなく 具体的な更新や返答に置く
- stop の時も関係を壊す文面にしない

### 139.3 詳細版を引く場所

- 共同研究先タイプ別の再始動判断ルーブリックは `MindUpload-EEGDATA-FundMap-collab-restart-rubric.csv` を使う
- 列は `counterpart_type`, `go_signal`, `hold_signal`, `stop_signal`, `minimum_restart_unit`, `reason_line`, `avoid_point`

## 140. 25トピック別の複数年撤退条件

### 140.1 使い方

- `exit_trigger` は 複数年で一度止めるべき条件として使う
- `preserve_asset` は 止めても残す最小資産として使う
- `re_entry_condition` は 再開してよい条件として使う
- `note_line` は 撤退判断を短く共有する文として使う

### 140.2 撤退条件で守ること

- 撤退は `疲れたから止める` ではなく 条件で切る
- 止める時も `図1枚` `表1枚` `手順1本` は残す
- 今は止めることと 永久に不可能だと言うことを混同しない
- 高次主張ほど 早めに安全側へ畳む

### 140.3 詳細版を引く場所

- 25トピック別の複数年撤退条件は `MindUpload-EEGDATA-FundMap-topic-multiyear-exit.csv` を使う
- 列は `phase`, `topic`, `exit_trigger`, `preserve_asset`, `re_entry_condition`, `note_line`, `avoid_point`

## 141. 制度タイプ別の公開後波及効果メモ

### 141.1 使い方

- `spillover_window` は 波及効果を見に行く時期の目安として使う
- `primary_spillover` は 最優先で見たい波及先として使う
- `secondary_spillover` は 補助的に見る波及先として使う
- `signal_to_track` は 実際に追う指標として使う
- `note_line` は 制度側に共有する短文として使う

### 141.2 波及効果メモで守ること

- 波及効果は `引用数だけ` で見ない
- 使い回された単位が `図` `教材` `比較表` のどれかを明確にする
- 次の大型申請の期待値を 波及効果と混ぜない
- 小さい再利用1件でも 追えるなら価値として残す

### 141.3 詳細版を引く場所

- 制度タイプ別の公開後波及効果メモは `MindUpload-EEGDATA-FundMap-publication-spillover-notes.csv` を使う
- 列は `support_type`, `spillover_window`, `primary_spillover`, `secondary_spillover`, `signal_to_track`, `note_line`, `avoid_point`

## 142. 共同研究先タイプ別の再始動見送り文面

### 142.1 使い方

- `deferral_reason` は 今回見送る理由として使う
- `soft_line` は 角を立てずに返す短文として使う
- `next_check_timing` は 次に見直す時期として使う
- `reopen_trigger` は 再度連絡してよい条件として使う
- `note_line` は 内部メモ向けの一文として使う

### 142.2 見送り文面で守ること

- 見送りは `拒絶` ではなく `条件待ち` として書く
- 次に連絡する単位を `1図` `1条件` `1回分` まで落とす
- 相手の熱量を否定する文にしない
- 見送りの理由は 共有単位か条件不足に寄せる

### 142.3 詳細版を引く場所

- 共同研究先タイプ別の再始動見送り文面は `MindUpload-EEGDATA-FundMap-collab-restart-deferral.csv` を使う
- 列は `counterpart_type`, `deferral_reason`, `soft_line`, `next_check_timing`, `reopen_trigger`, `note_line`, `avoid_point`

## 143. 25トピック別の複数年復帰条件

### 143.1 使い方

- `re_entry_trigger` は 再開してよい条件として使う
- `first_return_unit` は 復帰時に最初にやる最小単位として使う
- `success_signal` は 復帰判断が正しかったかを見る合図として使う
- `note_line` は 復帰理由を短く共有する文として使う

### 143.2 復帰条件で守ること

- 復帰は `やっぱり気になる` ではなく 条件で切る
- 最初の復帰単位は `1表` `1図` `1手順` を超えない
- 復帰後に前の広い主張へすぐ戻らない
- 成功合図が出なければ すぐに再び縮退する

### 143.3 詳細版を引く場所

- 25トピック別の複数年復帰条件は `MindUpload-EEGDATA-FundMap-topic-multiyear-reentry.csv` を使う
- 列は `phase`, `topic`, `re_entry_trigger`, `first_return_unit`, `success_signal`, `note_line`, `avoid_point`

## 144. 制度タイプ別の公開後波及効果スコア表

### 144.1 使い方

- `score_1` は 最低限の波及として数える条件として使う
- `score_2` は 十分に意味がある波及として数える条件として使う
- `score_3` は 明確に強い波及として数える条件として使う
- `main_signal` は まず最初に追う指標として使う
- `note_line` は 制度側へ説明する短文として使う

### 144.2 波及効果スコアで守ること

- スコアは `件数` だけでなく `再利用単位` で切る
- score を上げる時は 同じ相手の反応を重複計上しない
- 制度タイプごとに 強い波及の意味が違うことを前提にする
- まだ起きていない期待を score に入れない

### 144.3 詳細版を引く場所

- 制度タイプ別の公開後波及効果スコア表は `MindUpload-EEGDATA-FundMap-publication-spillover-score.csv` を使う
- 列は `support_type`, `score_1`, `score_2`, `score_3`, `main_signal`, `note_line`, `avoid_point`

## 145. 共同研究先タイプ別の見送り後フォロー文面

### 145.1 使い方

- `followup_timing` は 見送り後に再度触る時期として使う
- `followup_line` は 実際に送る短文として使う
- `attachment_unit` は 添える最小資料として使う
- `reopen_check` は 再開前に見る確認点として使う
- `note_line` は 内部メモ向けの一文として使う

### 145.2 見送り後フォローで守ること

- フォローは `思い出し連絡` ではなく 更新共有として送る
- 添付は `図1枚` `資料1枚` `論点1件` の単位にする
- 返答がない時に 文面を長くして押し込まない
- 見送りの延長でも 関係を弱く保つ導線は残す

### 145.3 詳細版を引く場所

- 共同研究先タイプ別の見送り後フォロー文面は `MindUpload-EEGDATA-FundMap-collab-deferral-followup.csv` を使う
- 列は `counterpart_type`, `followup_timing`, `followup_line`, `attachment_unit`, `reopen_check`, `note_line`, `avoid_point`

## 146. 25トピック別の複数年復帰後90日プラン

### 146.1 使い方

- `day_0_to_30` は 復帰直後にやる最小作業として使う
- `day_31_to_60` は 比較表や図を作る中間作業として使う
- `day_61_to_90` は 90日以内に残す共有物として使う
- `success_marker` は 復帰が有効だったかを見る合図として使う

### 146.2 復帰後90日プランで守ること

- 最初の90日は `検証` に限定し `拡張` を入れない
- 60日までに 図表か比較表を1つは出す
- 90日以内に `続ける` `縮める` `再停止する` を決める
- 復帰直後から次年度大型計画に膨らませない

### 146.3 詳細版を引く場所

- 25トピック別の複数年復帰後90日プランは `MindUpload-EEGDATA-FundMap-topic-reentry-90days.csv` を使う
- 列は `phase`, `topic`, `day_0_to_30`, `day_31_to_60`, `day_61_to_90`, `success_marker`, `avoid_point`

## 147. 制度タイプ別の波及効果を示す証拠メモ

### 147.1 使い方

- `evidence_unit` は 証拠として束ねる最小単位として使う
- `weak_evidence` は 最低限の証拠として使う
- `strong_evidence` は 明確に強い証拠として使う
- `collection_timing` は 証拠を回収する時期として使う
- `note_line` は 制度側へ説明する一文として使う

### 147.2 波及効果の証拠で守ること

- 証拠は `件数` だけでなく `何が再利用されたか` を残す
- screenshot や URL を取れるものは 早めに保存する
- 私的な好反応は 証拠に昇格させない
- 強い証拠は 他者が再利用した痕跡に寄せる

### 147.3 詳細版を引く場所

- 制度タイプ別の波及効果を示す証拠メモは `MindUpload-EEGDATA-FundMap-publication-spillover-evidence.csv` を使う
- 列は `support_type`, `evidence_unit`, `weak_evidence`, `strong_evidence`, `collection_timing`, `note_line`, `avoid_point`

## 148. 共同研究先タイプ別の見送り後再打診テンプレ

### 148.1 使い方

- `reoutreach_timing` は 再打診する時期の目安として使う
- `opening_line` は 実際に送る出だしとして使う
- `shared_unit` は 添える最小共有物として使う
- `meeting_goal` は 再打診で狙う着地点として使う
- `note_line` は 内部メモ向けの一文として使う

### 148.2 見送り後再打診で守ること

- 再打診は `前より良くなった1点` を軸に送る
- meeting goal は `10分確認` `1条件確認` `1回分相談` を超えない
- 相手が前に止めた理由を無視して再送しない
- 共有物が増えても 本文は短く保つ

### 148.3 詳細版を引く場所

- 共同研究先タイプ別の見送り後再打診テンプレは `MindUpload-EEGDATA-FundMap-collab-deferral-reoutreach.csv` を使う
- 列は `counterpart_type`, `reoutreach_timing`, `opening_line`, `shared_unit`, `meeting_goal`, `note_line`, `avoid_point`

## 149. 25トピック別の復帰後180日プラン

### 149.1 使い方

- `day_0_to_60` は 復帰直後の再立ち上げとして使う
- `day_61_to_120` は 図表と比較軸を固める期間として使う
- `day_121_to_180` は 小さな共有物を外に出す期間として使う
- `deliverable_180d` は 180日以内に残す成果物として使う
- `decision_gate` は 180日時点で続けるか縮めるかを見る基準として使う

### 149.2 復帰後180日プランで守ること

- 180日で狙うのは `大きな前進` ではなく `継続価値の確認` に置く
- 120日までに 比較表か図表かメモのどれかを公開可能な形にする
- 180日時点で `続行` `縮小` `再停止` を条件で切る
- 復帰を長期テーマ復活の演出にしない

### 149.3 詳細版を引く場所

- 25トピック別の復帰後180日プランは `MindUpload-EEGDATA-FundMap-topic-reentry-180days.csv` を使う
- 列は `phase`, `topic`, `day_0_to_60`, `day_61_to_120`, `day_121_to_180`, `deliverable_180d`, `decision_gate`, `avoid_point`

## 150. 制度タイプ別の波及効果報告テンプレ

### 150.1 使い方

- `report_opening` は 報告文の冒頭として使う
- `metric_line` は 最低限入れる定量行として使う
- `evidence_line` は 証拠の見せ方として使う
- `next_line` は 今後の運用を短く伝える行として使う
- `note_line` は 内部で報告方針を共有する一文として使う

### 150.2 波及効果報告テンプレで守ること

- 報告は `成果自慢` ではなく `再利用の事実` に寄せる
- 定量は 1行で足りる形に圧縮する
- 画像やURLの証拠は 本文で語り過ぎず添付や脚注に逃がす
- 次の提案期待を 報告本文に混ぜない

### 150.3 詳細版を引く場所

- 制度タイプ別の波及効果報告テンプレは `MindUpload-EEGDATA-FundMap-publication-spillover-report.csv` を使う
- 列は `support_type`, `report_opening`, `metric_line`, `evidence_line`, `next_line`, `note_line`, `avoid_point`

## 151. 共同研究先タイプ別の再打診後初回面談メモ

### 151.1 使い方

- `first_goal` は 初回面談で決める最小ゴールとして使う
- `opening_question` は 最初に投げる確認質問として使う
- `share_unit` は 面談中に見せる最小共有物として使う
- `do_not_expand` は その場で広げない話題として使う
- `note_line` は 面談後メモに残す一文として使う

### 151.2 再打診後初回面談で守ること

- 初回面談は `関係再開` ではなく `条件再確認` の場にする
- 共有物は `図1枚` `条件1点` `要件1件` を超えない
- 相手が止めた理由を 先に確認してから次へ進む
- 面談中に大型提案へ膨らませない

### 151.3 詳細版を引く場所

- 共同研究先タイプ別の再打診後初回面談メモは `MindUpload-EEGDATA-FundMap-collab-reoutreach-first-meeting.csv` を使う
- 列は `counterpart_type`, `first_goal`, `opening_question`, `share_unit`, `do_not_expand`, `note_line`, `avoid_point`

## 152. 25トピック別の復帰後1年プラン

### 152.1 使い方

- `month_0_to_4` は 復帰直後の立ち上げとして使う
- `month_5_to_8` は 比較軸や利用範囲を固める期間として使う
- `month_9_to_12` は 1年の成果を小さく公開する期間として使う
- `deliverable_1y` は 1年で残す成果物として使う
- `decision_gate` は 1年後に続けるか閉じるかを見る基準として使う

### 152.2 復帰後1年プランで守ること

- 1年で狙うのは `大型復活` ではなく `限定条件の定着` に置く
- 年内に 比較表 図表 手順のどれかは外部共有できる形にする
- 1年後の判断は `継続価値` と `再利用価値` の2軸で切る
- 復帰したこと自体を成果に見せない

### 152.3 詳細版を引く場所

- 25トピック別の復帰後1年プランは `MindUpload-EEGDATA-FundMap-topic-reentry-1year.csv` を使う
- 列は `phase`, `topic`, `month_0_to_4`, `month_5_to_8`, `month_9_to_12`, `deliverable_1y`, `decision_gate`, `avoid_point`

## 153. 制度タイプ別の波及効果報告メール文面

### 153.1 使い方

- `subject_line` は 送信件名として使う
- `opening_line` は メール冒頭として使う
- `metric_line` は 1行で示す定量情報として使う
- `evidence_line` は 添付やURLの案内文として使う
- `closing_line` は 今後の運用を締める文として使う

### 153.2 波及効果報告メールで守ること

- メール本文は 5行前後で終える
- 数字は 1行 証拠は 1行に圧縮する
- 感想や展望で長くせず 再利用の事実を中心に書く
- 次の資金相談を 同じメールに混ぜない

### 153.3 詳細版を引く場所

- 制度タイプ別の波及効果報告メール文面は `MindUpload-EEGDATA-FundMap-publication-spillover-mail.csv` を使う
- 列は `support_type`, `subject_line`, `opening_line`, `metric_line`, `evidence_line`, `closing_line`, `avoid_point`

## 154. 共同研究先タイプ別の再打診後合意メモ

### 154.1 使い方

- `agreement_focus` は 今回合意する最小論点として使う
- `scope_line` は 対象範囲を短く固定する文として使う
- `next_step_line` は 次の実務を固定する文として使う
- `do_not_include` は 合意メモに入れない論点として使う
- `note_line` は 内部メモ向けの一文として使う

### 154.2 再打診後合意メモで守ること

- 合意は `広い提携` ではなく `次の1単位` に限定する
- scope は `図1枚` `条件1点` `1回分` を超えない
- 口頭で盛り上がった論点をそのまま書き足さない
- 未確定の予算や長期計画を合意済みのように書かない

### 154.3 詳細版を引く場所

- 共同研究先タイプ別の再打診後合意メモは `MindUpload-EEGDATA-FundMap-collab-reoutreach-agreement-memo.csv` を使う
- 列は `counterpart_type`, `agreement_focus`, `scope_line`, `next_step_line`, `do_not_include`, `note_line`, `avoid_point`

## 155. 25トピック別の復帰後クローズ判断表

### 155.1 使い方

- `continue_signal` は 復帰後も続けてよい合図として使う
- `shrink_signal` は 範囲を縮めて残すべき合図として使う
- `close_signal` は 今回は閉じるべき合図として使う
- `preserve_asset` は 閉じても残す最小成果物として使う
- `note_line` は 判断理由を短く共有する文として使う

### 155.2 復帰後クローズ判断で守ること

- 判断は `continue` `shrink` `close` の3択で切る
- 反応が弱い時ほど `close` ではなく まず `shrink` を検討する
- 閉じる時も `図1枚` `表1枚` `手順1本` のどれかは残す
- 復帰に投じた時間の大きさで継続を正当化しない

### 155.3 詳細版を引く場所

- 25トピック別の復帰後クローズ判断表は `MindUpload-EEGDATA-FundMap-topic-reentry-close.csv` を使う
- 列は `phase`, `topic`, `continue_signal`, `shrink_signal`, `close_signal`, `preserve_asset`, `note_line`, `avoid_point`

## 156. 制度タイプ別の波及効果報告1ページ版

### 156.1 使い方

- `headline` は 1ページの最上段見出しとして使う
- `metric_block` は 中央に置く数字ブロックとして使う
- `evidence_block` は 図やURLの置き方として使う
- `reuse_block` は 再利用の説明欄として使う
- `close_block` は 最後に置く締めの一文として使う

### 156.2 1ページ報告で守ること

- 1ページは `成果紹介` ではなく `再利用報告` に寄せる
- 数字ブロックは 3 個以内に絞る
- 証拠は `URL` `図` `引用` のうち一番強いものだけを置く
- 将来計画の余白で紙面を埋めない

### 156.3 詳細版を引く場所

- 制度タイプ別の波及効果報告1ページ版は `MindUpload-EEGDATA-FundMap-publication-spillover-onepager.csv` を使う
- 列は `support_type`, `headline`, `metric_block`, `evidence_block`, `reuse_block`, `close_block`, `avoid_point`

## 157. 共同研究先タイプ別の再打診後クローズ条件

### 157.1 使い方

- `close_trigger` は 今回の再打診を閉じる条件として使う
- `soft_close_line` は 実際に送る穏当な締め文として使う
- `preserve_relation_line` は 関係を弱く保つ一文として使う
- `recontact_window` は 次に再接触してよい時期として使う
- `note_line` は 内部メモ向けの一文として使う

### 157.2 再打診後クローズ条件で守ること

- close は `拒絶` ではなく `今回はここまで` として書く
- 文面は 相手の都合ではなく 単位不足や条件不足に寄せる
- 閉じた後の再接触時期を 先に決めておく
- 返答がないことを感情的に解釈しない

### 157.3 詳細版を引く場所

- 共同研究先タイプ別の再打診後クローズ条件は `MindUpload-EEGDATA-FundMap-collab-reoutreach-close-conditions.csv` を使う
- 列は `counterpart_type`, `close_trigger`, `soft_close_line`, `preserve_relation_line`, `recontact_window`, `note_line`, `avoid_point`

## 158. 25トピック別の復帰後再停止テンプレ

### 158.1 使い方

- `restop_trigger` は 復帰後に再び止める条件として使う
- `closing_line` は 止める時に残す短文として使う
- `keep_asset` は 再停止しても残す最小成果物として使う
- `revisit_window` は 次に見直す時期として使う
- `note_line` は 内部メモ向けの一文として使う

### 158.2 再停止テンプレで守ること

- 再停止は `失敗宣言` ではなく `条件待ち` として書く
- 止める時も `図1枚` `表1枚` `手順1本` のどれかは残す
- 復帰した事実に引っ張られて継続を延命しない
- 次に見る時期を決めずに終わらせない

### 158.3 詳細版を引く場所

- 25トピック別の復帰後再停止テンプレは `MindUpload-EEGDATA-FundMap-topic-reentry-restop.csv` を使う
- 列は `phase`, `topic`, `restop_trigger`, `closing_line`, `keep_asset`, `revisit_window`, `note_line`, `avoid_point`

## 159. 制度タイプ別の波及効果最終報告チェック

### 159.1 使い方

- `check_1` は 最初に確認する必須項目として使う
- `check_2` は 定量情報の確認として使う
- `check_3` は 添付や証拠の確認として使う
- `evidence_ready` は 送付前に満たす状態として使う
- `send_rule` は 実際に出す時の最小ルールとして使う

### 159.2 最終報告チェックで守ること

- 最終報告は `長さ` より `再利用の事実` を優先する
- 数字 証拠 次の運用の3点が揃わなければ送らない
- 同じ反応を重複計上しない
- 将来提案や未確定案件を最終報告に混ぜない

### 159.3 詳細版を引く場所

- 制度タイプ別の波及効果最終報告チェックは `MindUpload-EEGDATA-FundMap-publication-spillover-final-check.csv` を使う
- 列は `support_type`, `check_1`, `check_2`, `check_3`, `evidence_ready`, `send_rule`, `avoid_point`

## 160. 共同研究先タイプ別の再打診後アーカイブメモ

### 160.1 使い方

- `archive_unit` は 保存する最小単位として使う
- `archive_note` は アーカイブ時に残す短い説明として使う
- `resume_hint` は 再開できる条件メモとして使う
- `storage_rule` は どの束で保存するかのルールとして使う
- `note_line` は 内部メモ向けの一文として使う

### 160.2 再打診後アーカイブで守ること

- 保存は `やりとり全量` ではなく `次に使う最小束` にする
- メール本文 資料 面談メモ を混ぜない
- 再開条件は `1図` `1条件` `1回分` の単位まで落とす
- 相手の反応の解釈を書き過ぎない

### 160.3 詳細版を引く場所

- 共同研究先タイプ別の再打診後アーカイブメモは `MindUpload-EEGDATA-FundMap-collab-reoutreach-archive-memo.csv` を使う
- 列は `counterpart_type`, `archive_unit`, `archive_note`, `resume_hint`, `storage_rule`, `note_line`, `avoid_point`

## 161. 25トピック別の復帰後再挑戦条件

### 161.1 使い方

- `retry_trigger` は 再停止後にもう一度挑戦してよい条件として使う
- `first_retry_unit` は 再挑戦時の最小単位として使う
- `success_probe` は 再挑戦が有効だったかを早く見る確認点として使う
- `note_line` は 再挑戦理由を短く共有する文として使う

### 161.2 再挑戦条件で守ること

- 再挑戦は `惜しいから` ではなく 新条件の追加で切る
- 最初の単位は `図1枚` `表1枚` `手順1本` を超えない
- 2回目の再挑戦でも同じ失敗を繰り返すなら すぐ止める
- 前回の広い主張へ一気に戻らない

### 161.3 詳細版を引く場所

- 25トピック別の復帰後再挑戦条件は `MindUpload-EEGDATA-FundMap-topic-reentry-retry.csv` を使う
- 列は `phase`, `topic`, `retry_trigger`, `first_retry_unit`, `success_probe`, `note_line`, `avoid_point`

## 162. 制度タイプ別の最終報告送付後フォロー

### 162.1 使い方

- `followup_timing` は 最終報告送付後に触る時期として使う
- `followup_line` は 実際に送る短文として使う
- `resend_asset` は 再送してよい最小成果物として使う
- `stop_rule` は そこで止める条件として使う
- `note_line` は 内部で方針を共有する一文として使う

### 162.2 最終報告後フォローで守ること

- フォローは `催促` ではなく `確認と共有` に寄せる
- 再送するのは 図1枚 URL1本 比較表1枚までにする
- 返信がなくても追加で長文化しない
- 次の提案相談を ここでは混ぜない

### 162.3 詳細版を引く場所

- 制度タイプ別の最終報告送付後フォローは `MindUpload-EEGDATA-FundMap-publication-final-followup.csv` を使う
- 列は `support_type`, `followup_timing`, `followup_line`, `resend_asset`, `stop_rule`, `note_line`, `avoid_point`

## 163. 共同研究先タイプ別の再打診後再開条件メモ

### 163.1 使い方

- `resume_signal` は 再開してよい合図として使う
- `hold_signal` は まだ保留にすべき合図として使う
- `first_resume_unit` は 再開時の最小単位として使う
- `confirm_point` は 再開前に最後に確認する点として使う
- `note_line` は 内部メモ向けの一文として使う

### 163.2 再打診後再開条件で守ること

- 再開は `雰囲気が良い` ではなく 更新や返答で切る
- 最初の再開単位は `図1枚` `条件1点` `1回分` を超えない
- hold のままなら 無理に会議を増やさない
- 再開しても すぐ大型提案へ広げない

### 163.3 詳細版を引く場所

- 共同研究先タイプ別の再打診後再開条件メモは `MindUpload-EEGDATA-FundMap-collab-reoutreach-resume-conditions.csv` を使う
- 列は `counterpart_type`, `resume_signal`, `hold_signal`, `first_resume_unit`, `confirm_point`, `note_line`, `avoid_point`

## 164. 25トピック別の再挑戦後90日プラン

### 164.1 使い方

- `day_0_to_30` は 再挑戦直後の最小確認として使う
- `day_31_to_60` は 比較表や条件差分を作る期間として使う
- `day_61_to_90` は 残す共有物を固定する期間として使う
- `decision_gate` は 90日後に続けるか止めるかを見る基準として使う

### 164.2 再挑戦後90日プランで守ること

- 再挑戦直後は 前回との差分確認に限定する
- 60日までに 新条件の効き方を図表で1回は出す
- 90日後には `続行` `縮小` `再停止` を決める
- 再挑戦を大型復活の演出にしない

### 164.3 詳細版を引く場所

- 25トピック別の再挑戦後90日プランは `MindUpload-EEGDATA-FundMap-topic-retry-90days.csv` を使う
- 列は `phase`, `topic`, `day_0_to_30`, `day_31_to_60`, `day_61_to_90`, `decision_gate`, `avoid_point`

## 165. 制度タイプ別の最終報告後30日レビュー

### 165.1 使い方

- `review_focus` は 30日後に見る観点として使う
- `check_metric` は 最低限見直す数字として使う
- `signal_to_keep` は 続けてよい合図として使う
- `signal_to_close` は ここで止める合図として使う
- `note_line` は 内部レビュー向けの一文として使う

### 165.2 最終報告後30日レビューで守ること

- 30日レビューは 新しい期待ではなく 送付後の事実で切る
- 数字は 1つか2つに絞って再確認する
- keep signal が弱ければ 追加フォローを増やさない
- 次の提案相談を ここで始めない

### 165.3 詳細版を引く場所

- 制度タイプ別の最終報告後30日レビューは `MindUpload-EEGDATA-FundMap-publication-final-30days-review.csv` を使う
- 列は `support_type`, `review_focus`, `check_metric`, `signal_to_keep`, `signal_to_close`, `note_line`, `avoid_point`

## 166. 共同研究先タイプ別の再開後最初の30日メモ

### 166.1 使い方

- `day_0_to_10` は 再開直後に確認することとして使う
- `day_11_to_20` は 最初の共有物を固める期間として使う
- `day_21_to_30` は 次に続けるかを見る期間として使う
- `first_deliverable` は 30日で残す最小成果物として使う
- `note_line` は 内部メモ向けの一文として使う

### 166.2 再開後30日メモで守ること

- 最初の30日は 関係の再構築ではなく 条件の再確認に置く
- 共有物は `図1枚` `条件1点` `1回分` を超えない
- 30日で 大きな提案や契約の話に進めない
- 反応が弱ければ すぐ hold に戻す

### 166.3 詳細版を引く場所

- 共同研究先タイプ別の再開後最初の30日メモは `MindUpload-EEGDATA-FundMap-collab-resume-first-30days.csv` を使う
- 列は `counterpart_type`, `day_0_to_10`, `day_11_to_20`, `day_21_to_30`, `first_deliverable`, `note_line`, `avoid_point`

## 167. 25トピック別の再挑戦後180日プラン

### 167.1 使い方

- `day_0_to_60` は 再挑戦直後の立ち上げとして使う
- `day_61_to_120` は 差分の意味を固める期間として使う
- `day_121_to_180` は 小さな共有物として残す期間として使う
- `decision_gate` は 180日後に 続けるか閉じるかを見る基準として使う

### 167.2 再挑戦後180日プランで守ること

- 180日で狙うのは `再利用価値の回復` に置く
- 120日までに 新条件の効き方を図表か比較表で固定する
- 180日後には `続行` `縮小` `再停止` を条件で切る
- 再挑戦を長期復活の物語にしない

### 167.3 詳細版を引く場所

- 25トピック別の再挑戦後180日プランは `MindUpload-EEGDATA-FundMap-topic-retry-180days.csv` を使う
- 列は `phase`, `topic`, `day_0_to_60`, `day_61_to_120`, `day_121_to_180`, `decision_gate`, `avoid_point`

## 168. 制度タイプ別の最終報告後90日レビュー

### 168.1 使い方

- `review_focus` は 90日後に見る観点として使う
- `check_metric` は 最低限見直す数字として使う
- `signal_to_keep` は まだ追跡してよい合図として使う
- `signal_to_close` は ここで終える合図として使う
- `note_line` は 内部レビュー向けの一文として使う

### 168.2 最終報告後90日レビューで守ること

- 90日レビューは `余熱` ではなく `残った再利用` を見る
- 数字は 1つか2つに絞って再確認する
- keep signal がなければ ここで閉じる
- 次の提案や営業導線を このレビューに混ぜない

### 168.3 詳細版を引く場所

- 制度タイプ別の最終報告後90日レビューは `MindUpload-EEGDATA-FundMap-publication-final-90days-review.csv` を使う
- 列は `support_type`, `review_focus`, `check_metric`, `signal_to_keep`, `signal_to_close`, `note_line`, `avoid_point`

## 169. 共同研究先タイプ別の再開後60日メモ

### 169.1 使い方

- `day_0_to_20` は 再開直後の確認期間として使う
- `day_21_to_40` は 最初の共有物を安定化する期間として使う
- `day_41_to_60` は 次に続けるか hold に戻すかを見る期間として使う
- `deliverable_60d` は 60日で残す最小成果物として使う
- `note_line` は 内部メモ向けの一文として使う

### 169.2 再開後60日メモで守ること

- 60日間でも 共有単位は `図1枚` `条件1点` `1回分` を超えない
- 40日までに 共有物を1つは確定させる
- 60日で `継続` `hold` `close` のどれかを決める
- 良い空気だけで大型提案に進めない

### 169.3 詳細版を引く場所

- 共同研究先タイプ別の再開後60日メモは `MindUpload-EEGDATA-FundMap-collab-resume-60days.csv` を使う
- 列は `counterpart_type`, `day_0_to_20`, `day_21_to_40`, `day_41_to_60`, `deliverable_60d`, `note_line`, `avoid_point`

## 170. 25トピック別の再挑戦後1年プラン

### 170.1 使い方

- `month_0_to_4` は 再挑戦直後の立ち上げとして使う
- `month_5_to_8` は 差分の意味と利用範囲を固める期間として使う
- `month_9_to_12` は 小さな共有物として固定する期間として使う
- `decision_gate` は 1年後に 続けるか閉じるかを見る基準として使う

### 170.2 再挑戦後1年プランで守ること

- 1年で狙うのは `再利用価値の定着` に置く
- 年内に 図表 比較表 メモのどれかを外部共有できる形にする
- 1年後には `続行` `縮小` `再停止` を条件で切る
- 再挑戦を大型復活の物語にしない

### 170.3 詳細版を引く場所

- 25トピック別の再挑戦後1年プランは `MindUpload-EEGDATA-FundMap-topic-retry-1year.csv` を使う
- 列は `phase`, `topic`, `month_0_to_4`, `month_5_to_8`, `month_9_to_12`, `decision_gate`, `avoid_point`

## 171. 制度タイプ別の最終報告後クローズ判断

### 171.1 使い方

- `close_focus` は クローズ判断で最初に見る観点として使う
- `keep_signal` は まだ追跡してよい合図として使う
- `close_signal` は ここで閉じてよい合図として使う
- `last_asset` は 最後に残す最小成果物として使う
- `note_line` は 内部判断を共有する一文として使う

### 171.2 最終報告後クローズ判断で守ること

- クローズ判断は `反応の大きさ` ではなく `残った再利用` で切る
- keep signal がないなら 追跡を延命しない
- 閉じる時も URL か図1枚か比較表1枚は残す
- 次の提案や営業導線を クローズ判断に混ぜない

### 171.3 詳細版を引く場所

- 制度タイプ別の最終報告後クローズ判断は `MindUpload-EEGDATA-FundMap-publication-final-close.csv` を使う
- 列は `support_type`, `close_focus`, `keep_signal`, `close_signal`, `last_asset`, `note_line`, `avoid_point`

## 172. 共同研究先タイプ別の再開後90日メモ

### 172.1 使い方

- `day_0_to_30` は 再開直後の確認期間として使う
- `day_31_to_60` は 最初の共有物を安定版にする期間として使う
- `day_61_to_90` は 継続か hold か close かを見る期間として使う
- `deliverable_90d` は 90日で残す最小成果物として使う
- `note_line` は 内部メモ向けの一文として使う

### 172.2 再開後90日メモで守ること

- 90日でも 共有単位は `図1枚` `条件1点` `1回分` を超えない
- 60日までに 安定版の共有物を1つは作る
- 90日で `継続` `hold` `close` のどれかを決める
- 良い空気だけで大型提案に進めない

### 172.3 詳細版を引く場所

- 共同研究先タイプ別の再開後90日メモは `MindUpload-EEGDATA-FundMap-collab-resume-90days.csv` を使う
- 列は `counterpart_type`, `day_0_to_30`, `day_31_to_60`, `day_61_to_90`, `deliverable_90d`, `note_line`, `avoid_point`

## 173. 25トピック別の再挑戦後クローズ判断

### 173.1 使い方

- `close_focus` は 再挑戦を閉じるときに最初に見る論点として使う
- `keep_signal` は まだ小さく続けてよい合図として使う
- `close_signal` は ここで閉じてよい合図として使う
- `last_asset` は 閉じる前に残す最小成果物として使う
- `note_line` は 内部メモや handoff 向けの一文として使う

### 173.2 再挑戦後クローズ判断で守ること

- 再挑戦のクローズは `期待` ではなく `残った再利用` で切る
- keep signal がなければ `次で効くかもしれない` だけで延命しない
- 閉じる時も 図1枚 比較表1枚 条件表1枚のどれかは残す
- 高い理論主張へ戻るほど 早めに閉じる

### 173.3 詳細版を引く場所

- 25トピック別の再挑戦後クローズ判断は `MindUpload-EEGDATA-FundMap-topic-retry-close.csv` を使う
- 列は `phase`, `topic`, `close_focus`, `keep_signal`, `close_signal`, `last_asset`, `note_line`, `avoid_point`

## 174. 制度タイプ別の最終報告後アーカイブ運用

### 174.1 使い方

- `archive_focus` は 保存対象を絞る観点として使う
- `archive_unit` は 長期保存する最小単位として使う
- `retention_trigger` は まだ保持を続ける条件として使う
- `close_trigger` は 保持を縮小してよい条件として使う
- `final_archive` は 最後に残す具体物として使う
- `note_line` は 内部の保管メモや README 向けの一文として使う

### 174.2 最終報告後アーカイブ運用で守ること

- 保存対象は `次の人が再利用できる最小単位` まで削る
- 生データや重い派生物を全部残す前に `再説明に要るものだけ` を切り出す
- close trigger が立ったら 保管対象を増やさず固定する
- archive は 次の大型提案の倉庫にしない

### 174.3 詳細版を引く場所

- 制度タイプ別の最終報告後アーカイブ運用は `MindUpload-EEGDATA-FundMap-publication-final-archive-ops.csv` を使う
- 列は `support_type`, `archive_focus`, `archive_unit`, `retention_trigger`, `close_trigger`, `final_archive`, `note_line`, `avoid_point`

## 175. 共同研究先タイプ別の再開後クローズ条件

### 175.1 使い方

- `close_focus` は 再開案件を閉じるときに最初に見る論点として使う
- `keep_condition` は 次も小さく続けてよい条件として使う
- `hold_condition` は 一旦止めて様子を見る条件として使う
- `close_condition` は 閉じてよい条件として使う
- `last_asset` は 閉じる前に相手と共有して残す最小成果物として使う
- `note_line` は 面談メモや close mail の芯として使う

### 175.2 再開後クローズ条件で守ること

- 再開案件でも `次の1論点` が消えたら close を選ぶ
- hold は `曖昧な保留` ではなく 再開条件待ちの短期状態として使う
- close 時も 相手が後で再利用できる 1枚か1点は残す
- 雰囲気が良いだけで大型共同研究へ拡張しない

### 175.3 詳細版を引く場所

- 共同研究先タイプ別の再開後クローズ条件は `MindUpload-EEGDATA-FundMap-collab-resume-close-conditions.csv` を使う
- 列は `counterpart_type`, `close_focus`, `keep_condition`, `hold_condition`, `close_condition`, `last_asset`, `note_line`, `avoid_point`

## 176. 25トピック別の再挑戦後アーカイブメモ

### 176.1 使い方

- `archive_focus` は 何を残せば次に再利用できるかを見る観点として使う
- `keep_asset` は 長く残す最小成果物として使う
- `discard_asset` は ここで抱え込まないものとして使う
- `archive_trigger` は 保存版へ固定する条件として使う
- `note_line` は handoff や README 向けの短文として使う

### 176.2 再挑戦後アーカイブメモで守ること

- 再挑戦後に残すのは `次の比較に効く最小単位` に絞る
- keep asset は 1ページか1表か1図に寄せる
- discard asset を決めずに すべて保存しない
- archive は 再挑戦の未練を残す置き場にしない

### 176.3 詳細版を引く場所

- 25トピック別の再挑戦後アーカイブメモは `MindUpload-EEGDATA-FundMap-topic-retry-archive-memo.csv` を使う
- 列は `phase`, `topic`, `archive_focus`, `keep_asset`, `discard_asset`, `archive_trigger`, `note_line`, `avoid_point`

## 177. 制度タイプ別の最終報告後再公開条件

### 177.1 使い方

- `republish_focus` は 何を再公開してよいか判断する観点として使う
- `republish_condition` は 再公開してよい条件として使う
- `hold_condition` は いったん保留する条件として使う
- `do_not_republish` は 再公開しない条件として使う
- `republish_asset` は 再公開する最小成果物として使う
- `note_line` は 再公開判断の内部メモとして使う

### 177.2 最終報告後再公開条件で守ること

- 再公開は `反応があったから` ではなく `再利用価値が残ったから` で決める
- 再公開するなら 前回より短く狭く出す
- hold 条件のまま再公開しない
- 制度本文で禁じる範囲には踏み込まない

### 177.3 詳細版を引く場所

- 制度タイプ別の最終報告後再公開条件は `MindUpload-EEGDATA-FundMap-publication-final-republish-conditions.csv` を使う
- 列は `support_type`, `republish_focus`, `republish_condition`, `hold_condition`, `do_not_republish`, `republish_asset`, `note_line`, `avoid_point`

## 178. 共同研究先タイプ別の再開後再停止テンプレ

### 178.1 使い方

- `restop_focus` は 何が止まったので再停止するかを示す論点として使う
- `restop_trigger` は 再停止へ切る条件として使う
- `message_core` は 相手へ送る本文の芯として使う
- `leave_behind_asset` は 再停止時に残す最小成果物として使う
- `reopen_condition` は 将来また開ける条件として使う
- `note_line` は 内部の close note として使う

### 178.2 再開後再停止テンプレで守ること

- 再停止の理由は `作業量` より `次の1論点が消えたこと` で書く
- 相手責任に寄せず 条件が揃っていない事実だけを書く
- 再停止時も 1枚か1点は残して関係を荒らさない
- reopen condition がないのに 社交辞令だけ残さない

### 178.3 詳細版を引く場所

- 共同研究先タイプ別の再開後再停止テンプレは `MindUpload-EEGDATA-FundMap-collab-resume-restop-template.csv` を使う
- 列は `counterpart_type`, `restop_focus`, `restop_trigger`, `message_core`, `leave_behind_asset`, `reopen_condition`, `note_line`, `avoid_point`

## 179. 25トピック別の再挑戦後再公開条件

### 179.1 使い方

- `republish_focus` は 何を再公開の対象にしてよいかを見る観点として使う
- `republish_condition` は 再公開へ進めてよい条件として使う
- `hold_condition` は まだ様子を見る条件として使う
- `do_not_republish` は 再公開しないと決める条件として使う
- `republish_asset` は 出し直す最小成果物として使う
- `note_line` は 再公開判断を短く共有する一文として使う

### 179.2 再挑戦後再公開条件で守ること

- 再公開は `再挑戦した事実` ではなく `差分が伝わること` で決める
- republish asset は 1枚か1表か1ページに削る
- hold 条件のまま 外へ出し直さない
- 高い理論主張に読める topic ほど 再公開はさらに狭くする

### 179.3 詳細版を引く場所

- 25トピック別の再挑戦後再公開条件は `MindUpload-EEGDATA-FundMap-topic-retry-republish-conditions.csv` を使う
- 列は `phase`, `topic`, `republish_focus`, `republish_condition`, `hold_condition`, `do_not_republish`, `republish_asset`, `note_line`, `avoid_point`

## 180. 制度タイプ別の最終報告後二次利用許容メモ

### 180.1 使い方

- `secondary_use_focus` は 何の二次利用を見てよいかの観点として使う
- `allowed_unit` は 許容する最小単位として使う
- `allow_condition` は 二次利用を許容してよい条件として使う
- `hold_condition` は まだ確認が要る条件として使う
- `disallow_condition` は 二次利用を止める条件として使う
- `note_line` は 内部メモや README の一文として使う

### 180.2 最終報告後二次利用許容メモで守ること

- 二次利用は `何でも使ってよい` ではなく `最小単位で許容する` 形にする
- allowed unit は 再説明に必要なものだけに削る
- hold 条件がある間は 二次利用を急がない
- 制度文言と公開条件がぶつかる時は disallow を優先する

### 180.3 詳細版を引く場所

- 制度タイプ別の最終報告後二次利用許容メモは `MindUpload-EEGDATA-FundMap-publication-final-secondary-use.csv` を使う
- 列は `support_type`, `secondary_use_focus`, `allowed_unit`, `allow_condition`, `hold_condition`, `disallow_condition`, `note_line`, `avoid_point`

## 181. 共同研究先タイプ別の再停止後フォロー文面

### 181.1 使い方

- `followup_timing` は 再停止後に連絡するまでの待機期間として使う
- `followup_focus` は 何を軸に軽く戻るかの論点として使う
- `message_line` は 実際に送る短文の芯として使う
- `share_asset` は 添える最小成果物として使う
- `reopen_condition` は 次に開き直す条件として使う
- `note_line` は 内部の followup 方針メモとして使う

### 181.2 再停止後フォロー文面で守ること

- フォローは `再提案` ではなく `関係の再確認` に置く
- share asset は 1枚か1点から増やさない
- reopen condition がないなら 連絡だけ重ねない
- 以前止めた理由を曖昧に上書きしない

### 181.3 詳細版を引く場所

- 共同研究先タイプ別の再停止後フォロー文面は `MindUpload-EEGDATA-FundMap-collab-resume-restop-followup.csv` を使う
- 列は `counterpart_type`, `followup_timing`, `followup_focus`, `message_line`, `share_asset`, `reopen_condition`, `note_line`, `avoid_point`

## 182. 25トピック別の再挑戦後二次利用メモ

### 182.1 使い方

- `secondary_use_focus` は topic ごとに何の二次利用を見てよいかの観点として使う
- `allowed_unit` は 再利用を許容する最小成果物として使う
- `allow_condition` は 二次利用へ進めてよい条件として使う
- `hold_condition` は まだ確認が必要な条件として使う
- `disallow_condition` は 二次利用を止める条件として使う
- `note_line` は handoff や README 向けの短文として使う

### 182.2 再挑戦後二次利用メモで守ること

- 二次利用は `再挑戦したから使える` ではなく `限定条件が残ったから使える` で切る
- allowed unit は 1枚か1表か1ページに削る
- hold 条件がある間は 派生利用を広げない
- 高い理論主張に見えやすい topic は disallow を早めに選ぶ

### 182.3 詳細版を引く場所

- 25トピック別の再挑戦後二次利用メモは `MindUpload-EEGDATA-FundMap-topic-retry-secondary-use.csv` を使う
- 列は `phase`, `topic`, `secondary_use_focus`, `allowed_unit`, `allow_condition`, `hold_condition`, `disallow_condition`, `note_line`, `avoid_point`

## 183. 制度タイプ別の最終報告後派生共有条件

### 183.1 使い方

- `derived_share_focus` は 派生共有をどこまで許容するかの観点として使う
- `share_unit` は 派生共有する最小単位として使う
- `allow_condition` は 派生共有へ進めてよい条件として使う
- `hold_condition` は まだ様子を見る条件として使う
- `disallow_condition` は 派生共有を止める条件として使う
- `note_line` は 内部メモや README の一文として使う

### 183.2 最終報告後派生共有条件で守ること

- 派生共有は `元成果の再配布` ではなく `限定用途の再説明` に寄せる
- share unit は できるだけ元成果より小さくする
- hold 条件のまま 派生共有へ進まない
- 制度側の公開条件と相手側の期待がぶつかる時は disallow を優先する

### 183.3 詳細版を引く場所

- 制度タイプ別の最終報告後派生共有条件は `MindUpload-EEGDATA-FundMap-publication-final-derived-sharing.csv` を使う
- 列は `support_type`, `derived_share_focus`, `share_unit`, `allow_condition`, `hold_condition`, `disallow_condition`, `note_line`, `avoid_point`

## 184. 共同研究先タイプ別の再停止後再打診条件

### 184.1 使い方

- `reoutreach_focus` は 何が戻ったら再打診してよいかを見る観点として使う
- `reoutreach_trigger` は 再打診へ進めてよい条件として使う
- `hold_trigger` は まだ待つべき条件として使う
- `do_not_reoutreach` は 再打診しない条件として使う
- `first_asset` は 再打診時に添える最小成果物として使う
- `note_line` は 再打診判断の内部メモとして使う

### 184.2 再停止後再打診条件で守ること

- 再打診は `時間が経ったから` ではなく `次の1論点が戻ったから` で切る
- first asset は 1枚か1点から増やさない
- hold trigger が続く間は 連絡頻度を上げない
- do_not_reoutreach 条件がある時は 社交辞令で戻らない

### 184.3 詳細版を引く場所

- 共同研究先タイプ別の再停止後再打診条件は `MindUpload-EEGDATA-FundMap-collab-resume-restop-reoutreach-conditions.csv` を使う
- 列は `counterpart_type`, `reoutreach_focus`, `reoutreach_trigger`, `hold_trigger`, `do_not_reoutreach`, `first_asset`, `note_line`, `avoid_point`

## 185. 25トピック別の再挑戦後派生共有メモ

### 185.1 使い方

- `derived_share_focus` は topic ごとに何の派生共有を見てよいかの観点として使う
- `share_unit` は 外へ出す最小成果物として使う
- `allow_condition` は 派生共有へ進めてよい条件として使う
- `hold_condition` は まだ様子を見る条件として使う
- `disallow_condition` は 派生共有を止める条件として使う
- `note_line` は README や handoff 向けの短文として使う

### 185.2 再挑戦後派生共有メモで守ること

- 派生共有は `元成果の拡散` ではなく `限定条件つきの再説明` に寄せる
- share unit は 1枚か1表か1ページに削る
- hold 条件がある間は topic を広げない
- 高い理論主張へ読まれやすい topic は disallow を早めに選ぶ

### 185.3 詳細版を引く場所

- 25トピック別の再挑戦後派生共有メモは `MindUpload-EEGDATA-FundMap-topic-retry-derived-sharing.csv` を使う
- 列は `phase`, `topic`, `derived_share_focus`, `share_unit`, `allow_condition`, `hold_condition`, `disallow_condition`, `note_line`, `avoid_point`

## 186. 制度タイプ別の最終報告後再編集条件

### 186.1 使い方

- `reedit_focus` は 最終報告後に何を編集し直してよいかの観点として使う
- `reedit_trigger` は 再編集へ進めてよい条件として使う
- `hold_trigger` は まだ編集を待つ条件として使う
- `do_not_reedit` は 再編集しない条件として使う
- `edited_asset` は 編集し直す最小成果物として使う
- `note_line` は 内部メモや changelog 向けの一文として使う

### 186.2 最終報告後再編集条件で守ること

- 再編集は `反応があったから書き換える` ではなく `誤読を減らせるから書き換える` で決める
- edited asset は 元成果全体ではなく最小単位に絞る
- hold trigger の間は 版を増やさない
- 制度条件と公開履歴が衝突する時は do_not_reedit を優先する

### 186.3 詳細版を引く場所

- 制度タイプ別の最終報告後再編集条件は `MindUpload-EEGDATA-FundMap-publication-final-reedit-conditions.csv` を使う
- 列は `support_type`, `reedit_focus`, `reedit_trigger`, `hold_trigger`, `do_not_reedit`, `edited_asset`, `note_line`, `avoid_point`

## 187. 共同研究先タイプ別の再停止後保留解除条件

### 187.1 使い方

- `release_focus` は hold を外してよいかを見る観点として使う
- `release_trigger` は 保留解除へ進めてよい条件として使う
- `keep_hold_trigger` は まだ hold のままにする条件として使う
- `do_not_release` は 保留解除しない条件として使う
- `first_move` は 保留解除後の最初の動きとして使う
- `note_line` は 内部メモや連絡文の芯として使う

### 187.2 再停止後保留解除条件で守ること

- hold 解除は `時間経過` ではなく `次の1論点が具体化したこと` で切る
- first move は 1枚か1点の共有から始める
- keep hold の間は 関係を無理に温めない
- do_not_release 条件がある時は 社交辞令で再始動しない

### 187.3 詳細版を引く場所

- 共同研究先タイプ別の再停止後保留解除条件は `MindUpload-EEGDATA-FundMap-collab-resume-restop-hold-release.csv` を使う
- 列は `counterpart_type`, `release_focus`, `release_trigger`, `keep_hold_trigger`, `do_not_release`, `first_move`, `note_line`, `avoid_point`

## 188. 25トピック別の再挑戦後再編集メモ

### 188.1 使い方

- `reedit_focus` は topic ごとに何を直すと誤読が減るかの観点として使う
- `reedit_trigger` は 再編集へ進めてよい条件として使う
- `hold_trigger` は まだ編集を待つ条件として使う
- `do_not_reedit` は 再編集しない条件として使う
- `edited_asset` は 直す最小成果物として使う
- `note_line` は changelog や handoff 向けの短文として使う

### 188.2 再挑戦後再編集メモで守ること

- 再編集は `もっと良くしたい` ではなく `誤読を減らす必要がある` で決める
- edited asset は 1枚か1表か1ページに絞る
- hold trigger の間は 版を増やさない
- 高い理論主張へ読まれやすい topic は do_not_reedit を早めに選ぶ

### 188.3 詳細版を引く場所

- 25トピック別の再挑戦後再編集メモは `MindUpload-EEGDATA-FundMap-topic-retry-reedit-memo.csv` を使う
- 列は `phase`, `topic`, `reedit_focus`, `reedit_trigger`, `hold_trigger`, `do_not_reedit`, `edited_asset`, `note_line`, `avoid_point`

## 189. 制度タイプ別の最終報告後更新停止条件

### 189.1 使い方

- `update_stop_focus` は 何をもって更新を止めてよいかを見る観点として使う
- `stop_trigger` は 更新停止へ進めてよい条件として使う
- `keep_update_trigger` は まだ更新を続ける条件として使う
- `do_not_stop` は 停止しない方がよい条件として使う
- `frozen_asset` は 停止時に固定する最小成果物として使う
- `note_line` は README や内部メモの一文として使う

### 189.2 最終報告後更新停止条件で守ること

- 更新停止は `飽きたから止める` ではなく `再利用が止まったから止める` で切る
- frozen asset は 1枚か1本の URL に絞る
- keep update が立つ間は 更新理由を明記する
- do_not_stop 条件がある時は 無理に凍結しない

### 189.3 詳細版を引く場所

- 制度タイプ別の最終報告後更新停止条件は `MindUpload-EEGDATA-FundMap-publication-final-update-stop.csv` を使う
- 列は `support_type`, `update_stop_focus`, `stop_trigger`, `keep_update_trigger`, `do_not_stop`, `frozen_asset`, `note_line`, `avoid_point`

## 190. 共同研究先タイプ別の保留解除後初回連絡テンプレ

### 190.1 使い方

- `contact_focus` は 初回連絡で何を確認するかの論点として使う
- `opening_line` は 連絡文の最初の一文として使う
- `share_asset` は 添える最小成果物として使う
- `ask_line` は 相手に依頼する最小確認として使う
- `next_gate` は この連絡の次に進める条件として使う
- `note_line` は 内部メモや送信前チェックの一文として使う

### 190.2 保留解除後初回連絡テンプレで守ること

- 初回連絡は `再始動宣言` ではなく `1論点の確認依頼` に置く
- share asset は 1枚か1点から増やさない
- ask line は 短時間で返せる確認に削る
- next gate が曖昧なまま 長文を送らない

### 190.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後初回連絡テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-first-contact.csv` を使う
- 列は `counterpart_type`, `contact_focus`, `opening_line`, `share_asset`, `ask_line`, `next_gate`, `note_line`, `avoid_point`

## 191. 25トピック別の再挑戦後更新停止メモ

### 191.1 使い方

- `update_stop_focus` は topic ごとに何をもって更新停止してよいかを見る観点として使う
- `stop_trigger` は 更新停止へ進めてよい条件として使う
- `keep_update_trigger` は まだ更新を続ける条件として使う
- `do_not_stop` は 停止しない方がよい条件として使う
- `frozen_asset` は 停止時に固定する最小成果物として使う
- `note_line` は 内部メモや README の一文として使う

### 191.2 再挑戦後更新停止メモで守ること

- 更新停止は `もう十分やった` ではなく `再利用が止まった` で切る
- frozen asset は 1枚か1表か1ページに絞る
- keep update がある間は 更新理由を一文で残す
- 高い理論主張に読まれやすい topic は do_not_stop より早く凍結を選ぶ

### 191.3 詳細版を引く場所

- 25トピック別の再挑戦後更新停止メモは `MindUpload-EEGDATA-FundMap-topic-retry-update-stop.csv` を使う
- 列は `phase`, `topic`, `update_stop_focus`, `stop_trigger`, `keep_update_trigger`, `do_not_stop`, `frozen_asset`, `note_line`, `avoid_point`

## 192. 制度タイプ別の最終報告後凍結資産メモ

### 192.1 使い方

- `freeze_focus` は 制度タイプごとに何を凍結資産として残すかの観点として使う
- `frozen_unit` は 凍結して残す最小単位として使う
- `freeze_trigger` は 凍結へ進めてよい条件として使う
- `keep_live_trigger` は まだ live のまま更新した方がよい条件として使う
- `do_not_freeze` は 凍結しない方がよい条件として使う
- `note_line` は README や内部運用メモの一文として使う

### 192.2 最終報告後凍結資産メモで守ること

- 凍結資産は `全部保存` ではなく `後から参照される最小単位` にする
- frozen unit は URL1本か図1枚か表1枚まで削る
- keep live がある間は 凍結と live を混ぜない
- do_not_freeze 条件がある時は 中途半端な固定版を作らない

### 192.3 詳細版を引く場所

- 制度タイプ別の最終報告後凍結資産メモは `MindUpload-EEGDATA-FundMap-publication-final-frozen-assets.csv` を使う
- 列は `support_type`, `freeze_focus`, `frozen_unit`, `freeze_trigger`, `keep_live_trigger`, `do_not_freeze`, `note_line`, `avoid_point`

## 193. 共同研究先タイプ別の保留解除後2通目返信テンプレ

### 193.1 使い方

- `reply_focus` は 2通目で何を固定するかの論点として使う
- `opening_line` は 返信冒頭の一文として使う
- `share_asset` は 追加で添える最小成果物として使う
- `confirm_line` は 相手に確認する最小論点として使う
- `next_gate` は 2通目の後に進める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 193.2 保留解除後2通目返信テンプレで守ること

- 2通目は `関係を温める文` ではなく `1論点を固定する文` にする
- share asset は 初回より増やしても 1枚か1点までに抑える
- confirm line は yes/no か短文で返せる形にする
- next gate が曖昧なら 2通目を送らない

### 193.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後2通目返信テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-second-contact.csv` を使う
- 列は `counterpart_type`, `reply_focus`, `opening_line`, `share_asset`, `confirm_line`, `next_gate`, `note_line`, `avoid_point`

## 194. 25トピック別の再挑戦後凍結資産メモ

### 194.1 使い方

- `freeze_focus` は topic ごとに何を凍結資産として残すかの観点として使う
- `frozen_unit` は 凍結して残す最小単位として使う
- `freeze_trigger` は 凍結へ進めてよい条件として使う
- `keep_live_trigger` は まだ live のまま更新した方がよい条件として使う
- `do_not_freeze` は 凍結しない方がよい条件として使う
- `note_line` は handoff や README の一文として使う

### 194.2 再挑戦後凍結資産メモで守ること

- 凍結資産は `全部保存` ではなく `後から参照される最小単位` にする
- frozen unit は URL1本か図1枚か表1枚まで削る
- keep live がある間は 凍結版と live 版を混ぜない
- 高い理論主張へ誤読されやすい topic は 凍結しても注記を強める

### 194.3 詳細版を引く場所

- 25トピック別の再挑戦後凍結資産メモは `MindUpload-EEGDATA-FundMap-topic-retry-frozen-assets.csv` を使う
- 列は `phase`, `topic`, `freeze_focus`, `frozen_unit`, `freeze_trigger`, `keep_live_trigger`, `do_not_freeze`, `note_line`, `avoid_point`

## 195. 制度タイプ別の最終報告後再配布停止条件

### 195.1 使い方

- `redistribution_stop_focus` は 何をもって再配布を止めてよいかを見る観点として使う
- `stop_trigger` は 再配布停止へ進めてよい条件として使う
- `keep_sharing_trigger` は まだ共有を続ける条件として使う
- `do_not_stop` は 停止しない方がよい条件として使う
- `final_shared_asset` は 停止時に最後に残す最小共有物として使う
- `note_line` は README や内部メモの一文として使う

### 195.2 最終報告後再配布停止条件で守ること

- 再配布停止は `出回ったから終わり` ではなく `再利用が止まったから終わり` で切る
- final shared asset は 1枚か1本の URL に絞る
- keep sharing が立つ間は 配布理由を短く残す
- do_not_stop 条件がある時は 見かけの整理のために止めない

### 195.3 詳細版を引く場所

- 制度タイプ別の最終報告後再配布停止条件は `MindUpload-EEGDATA-FundMap-publication-final-redistribution-stop.csv` を使う
- 列は `support_type`, `redistribution_stop_focus`, `stop_trigger`, `keep_sharing_trigger`, `do_not_stop`, `final_shared_asset`, `note_line`, `avoid_point`

## 196. 共同研究先タイプ別の保留解除後3通目返信テンプレ

### 196.1 使い方

- `reply_focus` は 3通目で何を最終固定するかの論点として使う
- `opening_line` は 返信冒頭の一文として使う
- `share_asset` は 最後に添える最小成果物として使う
- `confirm_line` は 相手に確認する最終論点として使う
- `decision_gate` は この連絡の後に進退を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 196.2 保留解除後3通目返信テンプレで守ること

- 3通目は `関係維持の雑談` ではなく `継続 / hold / close を決める文` にする
- share asset は 追加しても 1枚か1点までに抑える
- confirm line は 最終判断に必要な 1 論点だけに削る
- decision gate が曖昧なら 3通目を送らない

### 196.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後3通目返信テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-third-contact.csv` を使う
- 列は `counterpart_type`, `reply_focus`, `opening_line`, `share_asset`, `confirm_line`, `decision_gate`, `note_line`, `avoid_point`

## 197. 25トピック別の再挑戦後最終共有ユニット

### 197.1 使い方

- `final_share_focus` は topic ごとに最終的に何を共有単位として残すかの観点として使う
- `final_unit` は 外部に残す最小共有物として使う
- `share_trigger` は その単位で共有してよい条件として使う
- `hold_trigger` は まだ共有を待つ条件として使う
- `do_not_share` は 共有しない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 197.2 再挑戦後最終共有ユニットで守ること

- 最終共有ユニットは `全部盛り` ではなく `あとで誤読されにくい最小単位` にする
- final unit は 1枚か1表か1ページに削る
- hold がある間は 派生共有を足さない
- 高い理論主張へ誤読されやすい topic は do_not_share を早めに選ぶ

### 197.3 詳細版を引く場所

- 25トピック別の再挑戦後最終共有ユニットは `MindUpload-EEGDATA-FundMap-topic-retry-final-share-unit.csv` を使う
- 列は `phase`, `topic`, `final_share_focus`, `final_unit`, `share_trigger`, `hold_trigger`, `do_not_share`, `note_line`, `avoid_point`

## 198. 制度タイプ別の最終報告後参照終了条件

### 198.1 使い方

- `reference_stop_focus` は 何をもって参照導線を閉じてよいかを見る観点として使う
- `stop_trigger` は 参照終了へ進めてよい条件として使う
- `keep_reference_trigger` は まだ参照を残す条件として使う
- `do_not_stop` は 参照終了しない方がよい条件として使う
- `last_reference` は 最後に残す最小参照物として使う
- `note_line` は README や内部メモの一文として使う

### 198.2 最終報告後参照終了条件で守ること

- 参照終了は `古くなった気がする` ではなく `再利用が止まった` で切る
- last reference は URL1本か図1枚まで削る
- keep reference がある間は 何のために残すかを明記する
- do_not_stop 条件がある時は 見かけだけ整えて閉じない

### 198.3 詳細版を引く場所

- 制度タイプ別の最終報告後参照終了条件は `MindUpload-EEGDATA-FundMap-publication-final-reference-stop.csv` を使う
- 列は `support_type`, `reference_stop_focus`, `stop_trigger`, `keep_reference_trigger`, `do_not_stop`, `last_reference`, `note_line`, `avoid_point`

## 199. 共同研究先タイプ別の保留解除後最終確認テンプレ

### 199.1 使い方

- `confirmation_focus` は 最終確認で何を確定するかの論点として使う
- `opening_line` は 確認文の最初の一文として使う
- `share_asset` は 最後に添える最小成果物として使う
- `confirmation_line` は 相手に確認する最終事項として使う
- `decision_gate` は この確認の後に継続 / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 199.2 保留解除後最終確認テンプレで守ること

- 最終確認は `関係維持の挨拶` ではなく `進退を切る確認` にする
- share asset は 1枚か1点から増やさない
- confirmation line は yes/no か短文で返せる形にする
- decision gate が曖昧なら 最終確認を送らない

### 199.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後最終確認テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-final-check.csv` を使う
- 列は `counterpart_type`, `confirmation_focus`, `opening_line`, `share_asset`, `confirmation_line`, `decision_gate`, `note_line`, `avoid_point`

## 200. 25トピック別の再挑戦後最終参照ユニット

### 200.1 使い方

- `reference_focus` は topic ごとに何を最終的な参照単位として残すかの観点として使う
- `reference_unit` は 後から参照しても誤読が広がりにくい最小単位として使う
- `keep_reference_trigger` は その単位の参照を残してよい条件として使う
- `replace_trigger` は より小さい単位か新しい単位へ差し替える条件として使う
- `do_not_reference` は 参照単位として残さない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 200.2 再挑戦後最終参照ユニットで守ること

- 最終参照ユニットは `全部への入口` ではなく `誤読されにくい最小参照点` にする
- reference unit は 1枚か1表か1ページに削る
- replace trigger が立ったら 古い参照単位を残し続けない
- 高い理論主張へ飛びやすい topic は do_not_reference を先に選ぶ

### 200.3 詳細版を引く場所

- 25トピック別の再挑戦後最終参照ユニットは `MindUpload-EEGDATA-FundMap-topic-retry-final-reference-unit.csv` を使う
- 列は `phase`, `topic`, `reference_focus`, `reference_unit`, `keep_reference_trigger`, `replace_trigger`, `do_not_reference`, `note_line`, `avoid_point`

## 201. 制度タイプ別の最終報告後問い合わせ窓口条件

### 201.1 使い方

- `contact_focus` は 最終報告後に何の問い合わせ窓口を残すかの観点として使う
- `open_trigger` は 窓口を開けておくべき条件として使う
- `close_trigger` は 窓口を閉じてよい条件として使う
- `do_not_open` は そもそも窓口を広く開けない方がよい条件として使う
- `min_contact_asset` は 窓口として残す最小導線として使う
- `note_line` は README や内部メモの一文として使う

### 201.2 最終報告後問い合わせ窓口条件で守ること

- 窓口は `何でも相談` ではなく `残課題に対応する最小導線` にする
- min contact asset は mailbox 1本か案内 1ページまでに削る
- close trigger が立ったら 返せない窓口を惰性で残さない
- do_not_open 条件がある時は 善意だけで問い合わせ先を増やさない

### 201.3 詳細版を引く場所

- 制度タイプ別の最終報告後問い合わせ窓口条件は `MindUpload-EEGDATA-FundMap-publication-final-contact-window.csv` を使う
- 列は `support_type`, `contact_focus`, `open_trigger`, `close_trigger`, `do_not_open`, `min_contact_asset`, `note_line`, `avoid_point`

## 202. 共同研究先タイプ別の保留解除後最終引き継ぎテンプレ

### 202.1 使い方

- `handoff_focus` は 保留解除後に最後に何を引き継ぐかの論点として使う
- `opening_line` は 引き継ぎ文の最初の一文として使う
- `share_asset` は 引き継ぎで添える最小成果物として使う
- `handoff_line` は 相手に渡す最終行動指示として使う
- `decision_gate` は この引き継ぎの後に継続 / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 202.2 保留解除後最終引き継ぎテンプレで守ること

- 最終引き継ぎは `説明の蒸し返し` ではなく `次の担当動作を確定する文` にする
- share asset は 1枚か1件から増やさない
- handoff line は 相手の次の1動作が見える形にする
- decision gate が曖昧なら 最終引き継ぎを送らない

### 202.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後最終引き継ぎテンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-final-handoff.csv` を使う
- 列は `counterpart_type`, `handoff_focus`, `opening_line`, `share_asset`, `handoff_line`, `decision_gate`, `note_line`, `avoid_point`

## 203. 25トピック別の再挑戦後最終問い合わせ導線

### 203.1 使い方

- `inquiry_focus` は topic ごとに最後にどの問い合わせだけ受けるかの観点として使う
- `inquiry_unit` は 外部に残す最小問い合わせ導線として使う
- `keep_open_trigger` は その導線を残してよい条件として使う
- `close_trigger` は その導線を閉じてよい条件として使う
- `do_not_open` は 問い合わせ導線として開かない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 203.2 再挑戦後最終問い合わせ導線で守ること

- 最終問い合わせ導線は `何でも聞いてよい窓口` ではなく `残る論点1つに返す導線` にする
- inquiry unit は mailbox 1本か FAQ 1枚に削る
- close trigger が立ったら 返せない問い合わせ導線を残さない
- 高い理論主張へ飛びやすい topic は do_not_open を先に選ぶ

### 203.3 詳細版を引く場所

- 25トピック別の再挑戦後最終問い合わせ導線は `MindUpload-EEGDATA-FundMap-topic-retry-final-inquiry-window.csv` を使う
- 列は `phase`, `topic`, `inquiry_focus`, `inquiry_unit`, `keep_open_trigger`, `close_trigger`, `do_not_open`, `note_line`, `avoid_point`

## 204. 制度タイプ別の最終報告後窓口終了条件

### 204.1 使い方

- `window_stop_focus` は 最終報告後に問い合わせ窓口をいつ閉じてよいかの観点として使う
- `stop_trigger` は 窓口終了へ進めてよい条件として使う
- `keep_window_trigger` は まだ窓口を残す条件として使う
- `do_not_stop` は その時点で窓口を閉じない方がよい条件として使う
- `last_window_asset` は 最後に残す最小窓口導線として使う
- `note_line` は README や内部メモの一文として使う

### 204.2 最終報告後窓口終了条件で守ること

- 窓口終了は `面倒だから閉じる` ではなく `返すべき問い合わせが止まった` で切る
- last window asset は mailbox 1本か説明ページ 1 本まで削る
- keep window が立つ間は 何に返す窓口かを明記する
- do_not_stop 条件がある時は 見かけの整理だけで閉じない

### 204.3 詳細版を引く場所

- 制度タイプ別の最終報告後窓口終了条件は `MindUpload-EEGDATA-FundMap-publication-final-contact-stop.csv` を使う
- 列は `support_type`, `window_stop_focus`, `stop_trigger`, `keep_window_trigger`, `do_not_stop`, `last_window_asset`, `note_line`, `avoid_point`

## 205. 共同研究先タイプ別の保留解除後最終責務確認テンプレ

### 205.1 使い方

- `responsibility_focus` は 保留解除後に最後に何の責務分界を確認するかの論点として使う
- `opening_line` は 確認文の最初の一文として使う
- `share_asset` は 責務確認で添える最小成果物として使う
- `responsibility_line` は 相手と自分の責務を切り分ける一文として使う
- `decision_gate` は この確認の後に継続 / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 205.2 保留解除後最終責務確認テンプレで守ること

- 最終責務確認は `関係整理の挨拶` ではなく `誰が何を持つかを固定する文` にする
- share asset は 1枚か1件から増やさない
- responsibility line は 相手担当と自分担当が1文で切れる形にする
- decision gate が曖昧なら 最終責務確認を送らない

### 205.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後最終責務確認テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-final-responsibility.csv` を使う
- 列は `counterpart_type`, `responsibility_focus`, `opening_line`, `share_asset`, `responsibility_line`, `decision_gate`, `note_line`, `avoid_point`

## 206. 25トピック別の再挑戦後最終FAQユニット

### 206.1 使い方

- `faq_focus` は topic ごとに最後にどの質問だけ FAQ 化するかの観点として使う
- `faq_unit` は 外部に残す最小 FAQ 単位として使う
- `keep_faq_trigger` は その FAQ を残してよい条件として使う
- `close_trigger` は その FAQ を閉じてよい条件として使う
- `do_not_faq` は FAQ 化しない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 206.2 再挑戦後最終FAQユニットで守ること

- 最終 FAQ は `全部の質問集` ではなく `繰り返し来る1論点への最小回答` にする
- faq unit は Q&A 1件か短いメモ 1 枚まで削る
- close trigger が立ったら 古い FAQ を惰性で残さない
- 高い理論主張へ飛びやすい topic は do_not_faq を先に選ぶ

### 206.3 詳細版を引く場所

- 25トピック別の再挑戦後最終FAQユニットは `MindUpload-EEGDATA-FundMap-topic-retry-final-faq-unit.csv` を使う
- 列は `phase`, `topic`, `faq_focus`, `faq_unit`, `keep_faq_trigger`, `close_trigger`, `do_not_faq`, `note_line`, `avoid_point`

## 207. 制度タイプ別の最終報告後自動応答条件

### 207.1 使い方

- `auto_reply_focus` は 最終報告後に何にだけ自動応答を返すかの観点として使う
- `enable_trigger` は 自動応答を有効にしてよい条件として使う
- `disable_trigger` は 自動応答を止めてよい条件として使う
- `do_not_enable` は 自動応答を使わない方がよい条件として使う
- `min_reply_asset` は 自動応答で残す最小導線として使う
- `note_line` は README や内部メモの一文として使う

### 207.2 最終報告後自動応答条件で守ること

- 自動応答は `対応した気になる装置` ではなく `返せる範囲を切る装置` にする
- min reply asset は URL 1 本か mailbox 1 本まで削る
- disable trigger が立ったら 古い自動応答を残さない
- do_not_enable 条件がある時は 不正確な案内を自動化しない

### 207.3 詳細版を引く場所

- 制度タイプ別の最終報告後自動応答条件は `MindUpload-EEGDATA-FundMap-publication-final-auto-reply.csv` を使う
- 列は `support_type`, `auto_reply_focus`, `enable_trigger`, `disable_trigger`, `do_not_enable`, `min_reply_asset`, `note_line`, `avoid_point`

## 208. 共同研究先タイプ別の保留解除後最終完了通知テンプレ

### 208.1 使い方

- `completion_focus` は 保留解除後に最後に何を完了として通知するかの論点として使う
- `opening_line` は 完了通知の最初の一文として使う
- `share_asset` は 完了通知で添える最小成果物として使う
- `completion_line` は 何が完了し何を残すかを伝える一文として使う
- `decision_gate` は この通知の後に継続 / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 208.2 保留解除後最終完了通知テンプレで守ること

- 最終完了通知は `長い振り返り` ではなく `今回どこまで完了したかを固定する文` にする
- share asset は 1枚か1件から増やさない
- completion line は 完了点と残タスクが1文で切れる形にする
- decision gate が曖昧なら 最終完了通知を送らない

### 208.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後最終完了通知テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-final-completion.csv` を使う
- 列は `counterpart_type`, `completion_focus`, `opening_line`, `share_asset`, `completion_line`, `decision_gate`, `note_line`, `avoid_point`

## 209. 25トピック別の再挑戦後最終参照リンク

### 209.1 使い方

- `reference_link_focus` は topic ごとに最後にどのリンクだけ残すかの観点として使う
- `reference_link` は 外部に残す最小の参照リンクとして使う
- `keep_link_trigger` は そのリンクを残してよい条件として使う
- `replace_trigger` は 別のより短いリンクや導線へ差し替える条件として使う
- `do_not_link` は 参照リンクとして残さない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 209.2 再挑戦後最終参照リンクで守ること

- 最終参照リンクは `全部への入口` ではなく `誤読を増やさない最小導線` にする
- reference link は URL 1 本に削る
- replace trigger が立ったら 古いリンクを惰性で残さない
- 高い理論主張へ飛びやすい topic は do_not_link を先に選ぶ

### 209.3 詳細版を引く場所

- 25トピック別の再挑戦後最終参照リンクは `MindUpload-EEGDATA-FundMap-topic-retry-final-reference-link.csv` を使う
- 列は `phase`, `topic`, `reference_link_focus`, `reference_link`, `keep_link_trigger`, `replace_trigger`, `do_not_link`, `note_line`, `avoid_point`

## 210. 制度タイプ別の自動応答停止後残置導線

### 210.1 使い方

- `residual_channel_focus` は 自動応答を止めた後に何だけ残すかの観点として使う
- `residual_channel` は 残す最小の導線として使う
- `keep_residual_trigger` は その導線を残してよい条件として使う
- `close_trigger` は その導線も閉じてよい条件として使う
- `do_not_leave` は 導線を残さない方がよい条件として使う
- `note_line` は README や内部メモの一文として使う

### 210.2 自動応答停止後残置導線で守ること

- 残置導線は `応答停止の穴埋め` ではなく `最低限の着地点` にする
- residual channel は URL 1 本か mailbox 1 本まで削る
- close trigger が立ったら 放置された導線を残さない
- do_not_leave 条件がある時は 止めた後に余計な入口を足さない

### 210.3 詳細版を引く場所

- 制度タイプ別の自動応答停止後残置導線は `MindUpload-EEGDATA-FundMap-publication-final-residual-channel.csv` を使う
- 列は `support_type`, `residual_channel_focus`, `residual_channel`, `keep_residual_trigger`, `close_trigger`, `do_not_leave`, `note_line`, `avoid_point`

## 211. 共同研究先タイプ別の保留解除後完了通知後再開条件テンプレ

### 211.1 使い方

- `restart_focus` は 完了通知の後に何が揃えば再開してよいかの論点として使う
- `opening_line` は 再開条件確認の最初の一文として使う
- `share_asset` は 再開条件確認で添える最小成果物として使う
- `restart_line` は 再開に必要な条件を伝える一文として使う
- `decision_gate` は この確認の後に reopen / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 211.2 保留解除後完了通知後再開条件テンプレで守ること

- 再開条件テンプレは `またいつかやりましょう` ではなく `何が揃えば再開かを固定する文` にする
- share asset は 1枚か1件から増やさない
- restart line は 再開条件を yes/no で返せる形にする
- decision gate が曖昧なら 再開条件確認を送らない

### 211.3 詳細版を引く場所

- 共同研究先タイプ別の保留解除後完了通知後再開条件テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-restart-conditions.csv` を使う
- 列は `counterpart_type`, `restart_focus`, `opening_line`, `share_asset`, `restart_line`, `decision_gate`, `note_line`, `avoid_point`

## 212. 25トピック別の再挑戦後最終案内文

### 212.1 使い方

- `guide_focus` は topic ごとに最後に何を案内文として残すかの観点として使う
- `guide_line` は 外部に残す最小の案内文として使う
- `keep_guide_trigger` は その案内文を残してよい条件として使う
- `rewrite_trigger` は より短い案内文へ書き換える条件として使う
- `do_not_guide` は 案内文として残さない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 212.2 再挑戦後最終案内文で守ること

- 最終案内文は `全部の説明文` ではなく `次の誤解を防ぐ最小の一文` にする
- guide line は 1文で切る
- rewrite trigger が立ったら 古い言い回しを残し続けない
- 高い理論主張へ飛びやすい topic は do_not_guide を先に選ぶ

### 212.3 詳細版を引く場所

- 25トピック別の再挑戦後最終案内文は `MindUpload-EEGDATA-FundMap-topic-retry-final-guide-line.csv` を使う
- 列は `phase`, `topic`, `guide_focus`, `guide_line`, `keep_guide_trigger`, `rewrite_trigger`, `do_not_guide`, `note_line`, `avoid_point`

## 213. 制度タイプ別の残置導線閉鎖条件

### 213.1 使い方

- `channel_close_focus` は 残置導線をいつ閉じてよいかの観点として使う
- `close_trigger` は 残置導線を閉鎖してよい条件として使う
- `keep_trigger` は まだ導線を残す条件として使う
- `do_not_close` は その時点で閉鎖しない方がよい条件として使う
- `last_channel_asset` は 最後に残す最小の導線として使う
- `note_line` は README や内部メモの一文として使う

### 213.2 残置導線閉鎖条件で守ること

- 導線閉鎖は `面倒だから閉じる` ではなく `着地役を終えた` で切る
- last channel asset は URL 1 本か mailbox 1 本まで削る
- keep trigger が立つ間は 何のために残すかを明記する
- do_not_close 条件がある時は 見かけだけ整えて閉じない

### 213.3 詳細版を引く場所

- 制度タイプ別の残置導線閉鎖条件は `MindUpload-EEGDATA-FundMap-publication-final-residual-close.csv` を使う
- 列は `support_type`, `channel_close_focus`, `close_trigger`, `keep_trigger`, `do_not_close`, `last_channel_asset`, `note_line`, `avoid_point`

## 214. 共同研究先タイプ別の再開条件成立後初回通知テンプレ

### 214.1 使い方

- `resume_notice_focus` は 再開条件が揃った後に最初に何を通知するかの論点として使う
- `opening_line` は 初回通知の最初の一文として使う
- `share_asset` は 初回通知で添える最小成果物として使う
- `resume_notice_line` は 再開の起点を伝える一文として使う
- `decision_gate` は この通知の後に reopen / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 214.2 再開条件成立後初回通知テンプレで守ること

- 初回通知は `再開しました` の一言ではなく `何が揃ってどこから始めるかを切る文` にする
- share asset は 1枚か1件から増やさない
- resume notice line は 次の1動作が見える形にする
- decision gate が曖昧なら 初回通知を送らない

### 214.3 詳細版を引く場所

- 共同研究先タイプ別の再開条件成立後初回通知テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-resume-notice.csv` を使う
- 列は `counterpart_type`, `resume_notice_focus`, `opening_line`, `share_asset`, `resume_notice_line`, `decision_gate`, `note_line`, `avoid_point`

## 215. 25トピック別の再挑戦後最終禁止表現

### 215.1 使い方

- `ban_focus` は topic ごとに最後まで避けるべき表現の観点として使う
- `avoid_phrase` は 実際に使わない表現として使う
- `replace_with` は 代わりに使う最小の言い換えとして使う
- `ban_trigger` は その表現を禁止してよい条件として使う
- `do_not_ban` は 一律禁止しない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 215.2 再挑戦後最終禁止表現で守ること

- 禁止表現は `厳しそうだから全部禁止` ではなく `誤読を増やす語だけ切る` で選ぶ
- replace with は 1文で代替できる形にする
- ban trigger が立ったら 古い強い言い回しを残さない
- do_not_ban 条件がある時は 文脈依存の必要語まで消さない

### 215.3 詳細版を引く場所

- 25トピック別の再挑戦後最終禁止表現は `MindUpload-EEGDATA-FundMap-topic-retry-final-ban-phrases.csv` を使う
- 列は `phase`, `topic`, `ban_focus`, `avoid_phrase`, `replace_with`, `ban_trigger`, `do_not_ban`, `note_line`, `avoid_point`

## 216. 制度タイプ別の残置導線閉鎖後最終参照先

### 216.1 使い方

- `post_close_focus` は 残置導線を閉じた後に何だけ参照先として残すかの観点として使う
- `final_reference` は 最後に残す最小の参照先として使う
- `keep_reference_trigger` は その参照先を残してよい条件として使う
- `remove_reference_trigger` は その参照先も外してよい条件として使う
- `do_not_leave_reference` は 参照先を残さない方がよい条件として使う
- `note_line` は README や内部メモの一文として使う

### 216.2 残置導線閉鎖後最終参照先で守ること

- 最終参照先は `閉じた後の代替窓口` ではなく `履歴確認の最小足場` にする
- final reference は URL 1 本まで削る
- remove reference trigger が立ったら 死んだ参照先を残さない
- do_not_leave_reference 条件がある時は 閉鎖後に無責任な参照先を足さない

### 216.3 詳細版を引く場所

- 制度タイプ別の残置導線閉鎖後最終参照先は `MindUpload-EEGDATA-FundMap-publication-final-post-close-reference.csv` を使う
- 列は `support_type`, `post_close_focus`, `final_reference`, `keep_reference_trigger`, `remove_reference_trigger`, `do_not_leave_reference`, `note_line`, `avoid_point`

## 217. 共同研究先タイプ別の再開条件成立後初回確認テンプレ

### 217.1 使い方

- `check_focus` は 再開条件が揃った後に最初に何を確認するかの論点として使う
- `opening_line` は 初回確認の最初の一文として使う
- `share_asset` は 初回確認で添える最小成果物として使う
- `check_line` は 再開後の最初の確認点を伝える一文として使う
- `decision_gate` は この確認の後に reopen / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 217.2 再開条件成立後初回確認テンプレで守ること

- 初回確認は `再開できそうですか` ではなく `最初に確認すべき一点を切る文` にする
- share asset は 1枚か1件から増やさない
- check line は yes/no か短文で返せる形にする
- decision gate が曖昧なら 初回確認を送らない

### 217.3 詳細版を引く場所

- 共同研究先タイプ別の再開条件成立後初回確認テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-resume-check.csv` を使う
- 列は `counterpart_type`, `check_focus`, `opening_line`, `share_asset`, `check_line`, `decision_gate`, `note_line`, `avoid_point`

## 218. 25トピック別の再挑戦後最終誤解防止メモ

### 218.1 使い方

- `misread_focus` は topic ごとに最後に何の誤解を防ぐかの観点として使う
- `guard_note` は 外部に残す最小の誤解防止メモとして使う
- `keep_note_trigger` は そのメモを残してよい条件として使う
- `rewrite_trigger` は より短い防止メモへ書き換える条件として使う
- `do_not_leave_note` は 防止メモを残さない方がよい条件として使う
- `note_line` は README や handoff 向けの一文として使う

### 218.2 再挑戦後最終誤解防止メモで守ること

- 誤解防止メモは `全部の注意事項` ではなく `最も起きやすい誤読を止める一文` にする
- guard note は 1文で切る
- rewrite trigger が立ったら 古い防止文を残し続けない
- do_not_leave_note 条件がある時は かえって誤読を増やす補足を足さない

### 218.3 詳細版を引く場所

- 25トピック別の再挑戦後最終誤解防止メモは `MindUpload-EEGDATA-FundMap-topic-retry-final-misread-guard.csv` を使う
- 列は `phase`, `topic`, `misread_focus`, `guard_note`, `keep_note_trigger`, `rewrite_trigger`, `do_not_leave_note`, `note_line`, `avoid_point`

## 219. 制度タイプ別の最終参照先削除条件

### 219.1 使い方

- `reference_delete_focus` は 最終参照先をいつ削除してよいかの観点として使う
- `delete_trigger` は 参照先を削除してよい条件として使う
- `keep_trigger` は まだ参照先を残す条件として使う
- `do_not_delete` は その時点で削除しない方がよい条件として使う
- `last_record_asset` は 削除前に残す最小の記録として使う
- `note_line` は README や内部メモの一文として使う

### 219.2 最終参照先削除条件で守ること

- 参照先削除は `見えなくしたい` ではなく `役割を終えた` で切る
- last record asset は URL 1 本か短い記録 1 本まで削る
- keep trigger が立つ間は 何のために残すかを明記する
- do_not_delete 条件がある時は 履歴確認の足場まで消さない

### 219.3 詳細版を引く場所

- 制度タイプ別の最終参照先削除条件は `MindUpload-EEGDATA-FundMap-publication-final-reference-delete.csv` を使う
- 列は `support_type`, `reference_delete_focus`, `delete_trigger`, `keep_trigger`, `do_not_delete`, `last_record_asset`, `note_line`, `avoid_point`

## 220. 共同研究先タイプ別の初回確認後次アクション通知テンプレ

### 220.1 使い方

- `next_action_focus` は 初回確認の後に何を次アクションとして通知するかの論点として使う
- `opening_line` は 通知の最初の一文として使う
- `share_asset` は 次アクション通知で添える最小成果物として使う
- `next_action_line` は 次の1動作を伝える一文として使う
- `decision_gate` は この通知の後に reopen / hold / close を決める条件として使う
- `note_line` は 送信前チェックや内部メモの一文として使う

### 220.2 初回確認後次アクション通知テンプレで守ること

- 次アクション通知は `では進めます` ではなく `次に何を誰がやるかを切る文` にする
- share asset は 1枚か1件から増やさない
- next action line は 期限か担当のどちらかが見える形にする
- decision gate が曖昧なら 次アクション通知を送らない

### 220.3 詳細版を引く場所

- 共同研究先タイプ別の初回確認後次アクション通知テンプレは `MindUpload-EEGDATA-FundMap-collab-hold-release-next-action-notice.csv` を使う
- 列は `counterpart_type`, `next_action_focus`, `opening_line`, `share_asset`, `next_action_line`, `decision_gate`, `note_line`, `avoid_point`
