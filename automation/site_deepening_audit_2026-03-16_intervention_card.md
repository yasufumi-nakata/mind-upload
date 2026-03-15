# Site Deepening Audit (2026-03-16, Intervention Card / causal-closed-loop reporting)

## 対象

- 主対象: `verification.md`
- 副対象: `wiki/counterfactual-and-perturbation-verification.md`
- 補助対象: `wiki/baselines-prereg-and-model-cards.md`

## 今回の選定理由

- 2026-03-16 時点で、サイトは `Observability Budget`、`Fusion Card`、`Pretraining Card`、`latent-state error budget` まで整備されていました。
- その一方で、`adaptive stimulation`、`closed-loop BCI`、`state-dependent intervention`、`perturbation benchmark` を比較可能にするための **標準提出物** が欠けていました。
- この欠落は技術・自然科学の観点で優先度が高いです。なぜなら、現在の一次文献が示している前進は、単なる「高精度」ではなく、`trigger rule`、`timing audit`、`control/sham`、`recalibration burden`、`deployment horizon` の設計差に大きく依存するからです。

## 主要な批判点

### 1. 旧版は「因果証拠の段階」は示していましたが、「提出物として何を残すか」が固定されていませんでした

- 問題:
  - `verification.md` には causal/perturbation の 4 ゲートがありましたが、研究間比較に必要な提出物の最小欄がありませんでした。
  - そのため、同じ `adaptive` や `closed-loop` というラベルでも、`何を刺激したのか`、`何と比較したのか`、`どの条件で trigger したのか` を横並びに監査できませんでした。
- 根拠:
  - Zrenner et al. (2018) は、同じ rTMS でも EEG-defined brain state によって plasticity outcome が変わることを示しました。
  - Oehrn et al. (2024) は、adaptive DBS の有効性が state marker と comparator を固定した blinded randomized cross-over の設計に依存することを示しました。
- 修正:
  - `verification.md` に `Intervention Card` を新設し、`target / comparator`、`state estimate / trigger rule`、`timing audit`、`control / sham / artifact handling`、`safety / stop rule`、`online stability / recovery`、`claim ceiling` を標準欄として固定しました。

### 2. 旧版は timing と recalibration を評価指標としては持っていても、提出物仕様へ昇格していませんでした

- 問題:
  - サイト内には latency / jitter / recalibration burden の重要性が散在していましたが、モデルカード相当の必須提出物にはまだ接続されていませんでした。
  - この状態では、短いデモと長期運用を同じ `closed-loop success` と読めてしまいます。
- 根拠:
  - Littlejohn et al. (2025) は 80 ms increments の streaming brain-to-voice を示しました。
  - Wilson et al. (2025) は、accumulating neural change に対して frequent recalibration が必要であり、unsupervised recalibration が長期運用の主要課題であることを示しました。
- 修正:
  - `Intervention Card` に `timing audit` と `online stability / recovery` を独立欄として追加しました。
  - `wiki/baselines-prereg-and-model-cards.md` にも、因果・閉ループ結果では通常の model card に加えて `Intervention Card` が必要だと追記しました。

### 3. 旧版は control/sham と artifact handling が「必要なログ」止まりで、比較の主軸になっていませんでした

- 問題:
  - 旧 `counterfactual-and-perturbation-verification.md` には artifact 窓や control の重要性がありましたが、研究読解の中心に据える構造ではありませんでした。
  - これでは `刺激後に変化が見えた` をそのまま causal evidence と読みすぎます。
- 根拠:
  - Gordon et al. (2023) は optimized sham control を用いて、TMS-EEG 応答のうち sensory input 由来成分を切り分ける必要を示しました。
- 修正:
  - `wiki/counterfactual-and-perturbation-verification.md` に `Intervention Card` 節を追加し、`control / sham / artifact` を comparator・timing と並ぶ主要欄へ昇格しました。

## 今回実行した変更

- `verification.md`
  - page highlights に `Intervention Card` を追加
  - `Leaderboard & Model Cards` 節へ `Intervention Card` を接続
  - `2026-03 追補：L2 以上の介入・閉ループ結果には Intervention Card を添付する` 節を新設
  - 参考文献に Zrenner et al. (2018) と Gordon et al. (2023) を追加
- `wiki/baselines-prereg-and-model-cards.md`
  - `Intervention Card` を model card 運用の一部として追加
  - 因果・閉ループ結果向けの短い説明節を新設
- `wiki/counterfactual-and-perturbation-verification.md`
  - `Intervention Card` 節を新設
  - page highlights を更新
  - 参考文献に Zrenner et al. (2018) と Gordon et al. (2023) を追加
  - `last_updated` を `2026-03-16` に更新

## 外部依存で保留

- 実介入データの site-wide benchmark 実装
  - 担当者: maintainer / 実験系共同研究者
  - 前提条件: 公開可能な intervention log、timing log、artifact handling log、recalibration log を含むデータ
  - 完了条件: `target / comparator / trigger / timing / artifact / safety / recovery` を同一 schema で比較できる公開ベンチが整うこと

## 参考文献

- Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimul*. 2018.
  - https://doi.org/10.1016/j.brs.2017.11.016
- Gordon PC, Song YF, Jovellar DB, Rostami M, Belardinelli P, Ziemann U. Untangling TMS-EEG responses caused by TMS versus sensory input using optimized sham control and GABAergic challenge. *J Physiol*. 2023.
  - https://doi.org/10.1113/JP283986
- Oehrn CR, Cernera S, Hammer LH, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. *Nat Med*. 2024.
  - https://doi.org/10.1038/s41591-024-03196-z
- Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Forenzo D, Zhu H, Shanahan J, Lim J, He B. Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. *PNAS Nexus*. 2024.
  - https://doi.org/10.1093/pnasnexus/pgae145
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
