---
layout: default
title: 'Wiki: Issue #267-#280 対応監査'
description: 2026年5月3日時点で未完了だった GitHub Issues #267-#280 を、公開ページ・Wiki・外部依存タスクへ対応付ける監査台帳。
article_type: ウィキ
subtitle: クローズ対象 issue の要求、反映先、残る外部依存を 1 つずつ確認します。
author: マインドアップロード研究プロジェクト
last_updated: '2026-05-03'
note: Issue #267-#280 クローズ用対応監査
audience: issue がどの公開アーティファクトに反映されたか、何がまだ外部依存かを確認したい人。
reading_time: 15～25分
page_intro: このページは、2026年5月3日に未完了だった #267 から #280 までの GitHub Issues を、実際の公開ページ、Wiki ページ、検証カード、外部依存タスクへ対応付ける監査台帳です。
accuracy_note: ここでの「対応済み」は、issue の論点を公開アーティファクトに反映し、主張上限と停止条件を明示したことを意味します。参加者実験、IRB、外部 repo の実装、長期データ収集、法的判断が完了したという意味ではありません。
page_highlights:
- #267-#279 の EEG/ESI/DCM/維持状態/熱力学/マルチモーダル批判は、既存の検証カードと測定スタックページへ対応付けました。
- #275-#277 は同一本文の重複 issue として、同じ構造・熱力学・遅い計算層の監査に束ねました。
- #280 は BioData latent から mind-state substrate への橋渡し課題として、専用の Omoikane bridge ギャップ登録ページに分離しました。
- このページは、実行済み変更と外部依存タスクを混同しないためのクローズ根拠です。
known_points:
- EEG/ESI の改善は、深部状態や一意の内部状態復元を自動的に意味しません。
- DCM や有効接続性は、モデル空間、観察閉包、摂動または外部検証、棄権境界がない限り、モデル条件付き仮説に留まります。
- 維持状態、グリア、ECM、神経調節、代謝、熱状態は、背景ではなく主張上限を決める状態ファミリーとして扱う必要があります。
- 熱力学ラベルは、現時点では探索補助ログであり、意識再現や本人性の合格条件ではありません。
unknown_points:
- どの測定粒度と介入設計が L4 以上の本人性主張に十分かは未解決です。
- Omoikane 側の BioData bridge 実装そのものは、この repo の公開文書更新だけでは変更されません。
wiki_links:
- label: 'Wiki: Omoikane BioData bridge ギャップ登録'
  url: /wiki/omoikane-biodata-mind-state-bridge-gap-register.html
  description: #280 の BioData latent から意識再現までの研究ギャップを、測定対象、データセット、評価指標、反証条件、倫理 gate へ分解します。
- label: 'Wiki: 観測から推定まで'
  url: /wiki/observation-to-estimation.html
  description: ESI、DCM、SCM、因果等価クラス、識別可能性を整理します。
- label: 'Wiki: 測定スタックごとの可観測性とクレーム上限'
  url: /wiki/measurement-stack-and-claim-ceiling.html
  description: 各モダリティが直接観察するものと、残る claim ceiling を確認します。
recommended_pages:
- label: 検証
  url: /verification.html
- label: 技術ロードマップ
  url: /tech_roadmap.html
- label: GitHub Issues インベントリ
  url: /wiki/github-issues-inventory.html
---

# Issue #267-#280 対応監査

このページは、クローズ対象 issue の本文を、そのまま「解決済みの科学的主張」に変換するためのページではありません。目的は、各 issue が指摘した弱点を、公開アーティファクト内の読み取り規則、検証カード、停止条件、または外部依存タスクへ落とし込むことです。

## 対応方針

今回の対応は 3 層に分けます。

1. **このセッションで実行した変更**: issue 対応監査ページ、この Omoikane bridge ギャップ登録ページ、入口リンク、Wiki サイドバー、GitHub Issues インベントリの更新。
2. **既存公開アーティファクトで確認済みの対応**: `verification.md`、`tech_roadmap.md`、`eeg_101.md`、`wiki/observation-to-estimation.md`、`wiki/measurement-stack-and-claim-ceiling.md`、`wiki/thermodynamic-grounding-basics.md` などにすでに存在する検証カードと停止条件。
3. **external dependency tasks**: 参加者データ収集、IRB、Omoikane/eegflow 側の別 repo 実装、実験プロトコル承認、長期縦断データ、法的・倫理的判断。

## Issue 別対応表

| issue | 主な要求 | 反映・確認したアーティファクト | 残る外部依存 |
|---:|---|---|---|
| #267 | EEG 逆問題の物理限界、定量的棄権条件、外部 ground truth を必須化する。 | `eeg_101.md` の ESI 検証ラダー、`tech_roadmap.md#qa-r1` / `#qa-r2`、`verification.md#observability-budget`、`verification.md#identifiability-card`、`wiki/observation-to-estimation.html`。 | 同時侵襲記録、頭蓋内刺激、ファントムなどの新規検証データ取得。 |
| #268 | L1/L2 の claim ceiling、マルチモーダル可観測性、恒常性を制御制約として扱う。 | `verification.md#observability-budget`、`verification.md#maintenance-state-error-budget`、`verification.md#fusion-card`、`wiki/measurement-stack-and-claim-ceiling.html`。 | L2 以上を主張できる同一対象の外部検証付きデータセット。 |
| #269 | ESI 誤差、コネクトーム縮退、閉ループ熱力学、Neural Contribution baseline、文献鮮度を反映する。 | `verification.md#neural-contribution-card`、`verification.md#specificity-shortcut-card`、`tech_roadmap.md#qa-i9`、`wiki/thermodynamic-grounding-basics.html`、`wiki/connectome-is-not-enough.html`。 | issue が挙げた未検証の新規文献名は、一次ソース確認後に文献ページへ個別追加。 |
| #270 | EEGflow 的な前処理、ソース推定、因果モデル、再現性、最新研究との整合性を整理する。 | `datasets.md` / `verification.md` の L0・再現性ルール、`tech_roadmap.md#qa-r4`、`wiki/eeg-preprocessing-and-qc.html`、`wiki/observation-to-estimation.html`。 | `yasufumi-nakata/eegflow` 側のコード実装、公開データセットでの end-to-end 実行例。 |
| #271 | 個別頭部モデル、導電率校正、DCM の限界、状態変数感度、神経/生理アーティファクト分離を要求する。 | `verification.md#identifiability-card`、`verification.md#specificity-shortcut-card`、`verification.md#neural-contribution-card`、`wiki/measurement-stack-and-claim-ceiling.html#hemodynamic-transfer-wall`。 | EIT や同時計測を含む実測校正、NPASR の実データ標準化。 |
| #272 | マクロ観察からエミュレーションへの飛躍、潜在状態縮退、DCM 同定可能性、維持状態の多時間スケール結合を扱う。 | `wiki/observation-to-estimation.html#effective-connectivity-route-card`、`tech_roadmap.md#qa-r7`、`verification.md#maintenance-state-error-budget`。 | 省略メカニズムを露出させる新規摂動設計と同一対象データ。 |
| #273 | 維持状態を単なる背景ではなく統合された動的システムとして扱い、EEG の情報理論的限界を明示する。 | `tech_roadmap.md#qa-r0` / `#qa-r3` / `#qa-r5`、`wiki/homeostatic-plasticity-and-maintenance-state.html`、`wiki/observation-to-estimation.html`。 | Cramer-Rao 型境界や侵襲記録との cross-validation を実データで標準化する作業。 |
| #274 | 定量的状態変数、熱力学監査、潜在状態誤差予算、マルチモーダル統合を強化する。 | `verification.md#maintenance-state-error-budget`、`verification.md#thermodynamic-verification`、`verification.md#fusion-card`、`tech_roadmap.md#qa-i9`。 | 状態変数ごとの感度分析表と、外部校正付きプロキシ bundle の実データ構築。 |
| #275 | 熱力学、アストロサイト/ECM の遅い計算層、hidden state 解像度、ベイズ的マルチモーダル統合を追加する。 | #275-#277 は同一本文の重複として、`tech_roadmap.md#qa-i9`、`verification.md#maintenance-state-error-budget`、`verification.md#fusion-card`、`wiki/thermodynamic-grounding-basics.html` に束ねて対応。 | 同一対象での slow-scale computational layer 測定と縦断校正。 |
| #276 | #275 と同一。 | #275 と同じ対応。 | #275 と同じ外部依存。 |
| #277 | #275 と同一。 | #275 と同じ対応。 | #275 と同じ外部依存。 |
| #278 | ESI 過小評価、維持状態の非線形結合、Landauer の飛躍、Deployability 表現の抑制を要求する。 | `eeg_101.md`、`verification.md#thermodynamic-verification`、`verification.md#human-proxy-composition-card`、`wiki/measurement-stack-and-claim-ceiling.html`。 | 臨床パネルを WBE の状態完全読み出しと誤読しないための実データ同一対象比較。 |
| #279 | EEG 深部不可視性、DCM 計算爆発、湿った演算、神経修飾・グリア・代謝の統合を要求する。 | `wiki/measurement-stack-and-claim-ceiling.html#eeg-meg-validation-wall`、`wiki/observation-to-estimation.html#effective-connectivity-route-card`、`wiki/connectome-is-not-enough.html`。 | PET/MRSI/神経修飾/代謝を同一 identity の状態推定へ接続する longitudinal dataset。 |
| #280 | Omoikane BioData bridge から意識再現までの研究ギャップ、測定対象、dataset、指標、反証条件、倫理 gate、downgrade rule を定義する。 | 新規ページ `wiki/omoikane-biodata-mind-state-bridge-gap-register.md`。 | Omoikane 別 repo の実装変更、BioData/神経/行動/主観報告の同一対象縦断データ、IRB/同意/撤回/rollback 運用。 |

## 横断チェックリスト

| 明示要求 | 具体的な証拠 | カバー範囲 |
|---|---|---|
| EEG/ESI の物理限界を、単なる「ぼやけ」ではなく claim ceiling として扱う。 | `eeg_101.md`、`wiki/measurement-stack-and-claim-ceiling.html#eeg-meg-validation-wall`、`wiki/observation-to-estimation.html`。 | #267、#268、#269、#271、#272、#273、#278、#279 |
| 棄権条件と不確実性伝播をカード化する。 | `verification.md#observability-budget`、`verification.md#identifiability-card`、`wiki/uncertainty-confidence-and-abstention.html`。 | #267、#268、#271、#272、#274 |
| DCM / effective connectivity を因果構造発見として過読しない。 | `verification.md` の有効接続性 note、`wiki/observation-to-estimation.html#effective-connectivity-route-card`、`tech_roadmap.md#qa-r4`。 | #268、#270、#271、#272、#279 |
| コネクトーム不足、グリア、ECM、代謝、神経調節、維持状態を別ファミリーとして扱う。 | `verification.md#maintenance-state-error-budget`、`wiki/connectome-is-not-enough.html`、`wiki/homeostatic-plasticity-and-maintenance-state.html`。 | #268、#271、#272、#273、#274、#275、#276、#277、#279 |
| 熱力学/Landauer/NESS/EPR を合格条件ではなく探索補助ログとして分離する。 | `tech_roadmap.md#qa-i9`、`verification.md#thermodynamic-verification`、`wiki/thermodynamic-grounding-basics.html#irreversibility-route-card`。 | #269、#274、#275、#276、#277、#278 |
| マルチモーダルを状態完全性と読まない。 | `verification.md#fusion-card`、`verification.md#human-proxy-composition-card`、`wiki/measurement-stack-and-claim-ceiling.html`。 | #268、#274、#275、#276、#277、#278、#280 |
| Brain-to-text / 音声 decoding で神経寄与を LM-only や shuffle baseline から分離する。 | `verification.md#neural-contribution-card`、`verification.md#specificity-shortcut-card`、`tech_roadmap.md` の侵襲言語 BCI ルート。 | #269、#271 |
| BioData latent から qualia / self model / episodic stream への bridge を、semantic thought content や consciousness reproduction と混同しない。 | `wiki/omoikane-biodata-mind-state-bridge-gap-register.md`。 | #280 |

## このセッションで実行した変更

- `wiki/open-issues-267-280-resolution.md` を追加し、#267-#280 の対応先と外部依存を issue 別に固定しました。
- `wiki/omoikane-biodata-mind-state-bridge-gap-register.md` を追加し、#280 の研究ギャップを測定対象、必要データセット、評価指標、反証条件、倫理 gate、downgrade rule に分解しました。
- `wiki/index.md`、`issue.md`、`content_hub.md`、`verification.md`、`scripts/export_github_wiki.rb` から新規ページへ到達できるようにしました。
- GitHub Issue を閉じた後、`scripts/sync_github_issues_inventory.py` で `wiki/github-issues-inventory.md` を再生成し、未完了 issue が残っていない状態を反映します。

## external dependency tasks

| task | owner | 前提条件 | 完了条件 |
|---|---|---|---|
| `yasufumi-nakata/eegflow` 側で BIDS 公開データを使った end-to-end 前処理、ESI、因果モデル例を整備する。 | eegflow maintainer | 対象 repo の編集権限、対象公開データセット、依存環境。 | 第三者が同じ commit と dataset で再実行できる L0 artifact pack が公開される。 |
| 同時 EEG-iEEG / SEEG / 頭蓋内刺激 / ファントムを用いた ESI 外部検証を増やす。 | 研究 PI / 臨床共同研究者 | IRB、参加者同意、臨床または実験ハードウェア、データ共有契約。 | 検証クラス、誤差分布、不確実性、棄権境界が公開 artifact として登録される。 |
| Omoikane 側の BioData bridge schema / transmitter 実装を、mind-upload 側の bridge gap register と同期する。 | Omoikane maintainer | Omoikane repo の編集権限、schema compatibility 方針、digest-only 境界の維持。 | Omoikane 側に claim ceiling、downgrade rule、bridge input/output contract が実装または docs 化される。 |
| BioData / 神経 / 行動 / 主観報告 / 記憶再認の同一対象 longitudinal dataset を設計・取得する。 | 研究 PI / データ管理者 | IRB、同意、撤回、プライバシー、機器、長期運用資金。 | dataset card、calibration protocol、missing modality policy、subject-level split、negative controls が公開または審査可能になる。 |
| identity continuity の witness / consent / revocation / rollback protocol を実運用化する。 | 倫理・法務・研究運用責任者 | 法的判断、倫理審査、参加者説明、監査ログ基盤。 | witness、撤回、rollback、branch handling、監査ログの責任境界が承認済み protocol になる。 |
