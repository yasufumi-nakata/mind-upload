# Site Deepening Audit (2026-03-14, State / Trait / Drift)

## 対象

- 主対象: `wiki/state-trait-and-drift.md`
- 副対象: `wiki/index.md`
- 副対象: `verification.md`
- 副対象: `eeg_101.md`

## 今回の選定理由

- 本日までに `uncertainty`、`closed-loop`、`verification`、`decode/emulate` 周辺はかなり更新されましたが、それらの前提になる `state・trait・drift` の補助ページは 2026-03-06 版のままでした。
- 現行ページは概念の入口としては有用でしたが、技術・自然科学の観点では、`その場の状態変動`、`比較的安定な骨格`、`生体側の representational drift`、`interface / decoder drift` を同じ箱に入れていました。
- この混線は、最近追加した `recalibration burden`、`abstention/silence`、`population-level stability` の議論を弱くします。特に、fixed decoder 劣化を脳の本質的変化と読み違える余地が残っていました。

## 主要な批判点

### 1. 旧版は drift を 1 種類として扱いすぎていました

- 問題:
  - 旧版では drift を「時間とともに起きる変化」とだけ説明しており、生体側の表現ドリフトと、電極・前処理・decoder の nonstationarity が分離されていませんでした。
  - しかし BCI の長期運用では、この 2 つを混ぜると原因同定ができません。
- 根拠:
  - Wilson et al. (2025) は intracortical cursor BCI が accumulating neural nonstationarities により frequent recalibration を要することを示しました。
  - Wairagkar et al. (2025) は brain-to-voice decoder の fixed 運用性能が約 15 日で目立って低下することを示しました。
- 修正:
  - `biological drift` と `interface / decoder drift` を独立行として追加しました。
  - fixed decoder interval、recalibration burden、recovery time を最低提出物へ入れました。

### 2. 旧版は trait を verbal な「長く安定する特徴」としか書いておらず、何を安定骨格とみなすかが弱すぎました

- 問題:
  - 旧版は trait を説明していましたが、単一 neuron / voxel の不変性と誤読されうる構造でした。
  - しかし一次文献が示すのは、しばしば個々のユニットは動く一方、latent dynamics や representational geometry の方がより安定である、という構図です。
- 根拠:
  - Gallego et al. (2020) は neuron turnover があっても low-dimensional latent dynamics が安定し、aligned latent dynamics に基づく decoding は長期間維持できると示しました。
  - Finn et al. (2015) は functional connectivity profile が cross-session かつ task/rest をまたいでも個人識別に使えることを示しました。
  - Noda et al. (2025) は single-neuron tuning volatility があっても population-level representational map が保たれることを示しました。
- 修正:
  - trait を `trait-like backbone` として再定義し、latent dynamics、representational geometry、functional fingerprint を例示しました。
  - `trait は単一 unit の静止画ではない` という site rule を明文化しました。

### 3. 旧版は state fluctuation を「短期の揺れ」としか書かず、実際には何がどれだけ効くかを示していませんでした

- 問題:
  - 旧版は疲労や集中を例示するだけで、state fluctuation が neural variance の本体になりうることを示していませんでした。
- 根拠:
  - Musall et al. (2019) は uninstructed movements が cortex-wide activity を強く規定することを示しました。
  - Benisty et al. (2024) は spontaneous behavior が magnitude だけでなく functional connectivity の correlational structure を高速に変えることを示しました。
- 修正:
  - `state fluctuation` を単なるノイズではなく、within-session で監査すべき層として独立させました。
  - 行動・生理の同時計測と state 別性能差を最低限の評価へ入れました。

### 4. 旧版には一次文献も longitudinal benchmark もありませんでした

- 問題:
  - 参考文献節が無く、読者が何を根拠に state / trait / drift を分けるのかを追えませんでした。
  - また、どんなログがあれば縦断評価を読めるのかが固定されていませんでした。
- 修正:
  - state fluctuation、trait-like backbone、representational drift、decoder drift を支える一次文献を 8 本追加しました。
  - `state sensitivity / fixed-model stability / population backbone / recalibration burden` の 4 監査項目を表で固定しました。

## 今回実行した変更

- `wiki/state-trait-and-drift.md`
  - front matter を技術・自然科学中心へ更新
  - `4 つの層`、`旧来の 3 分類だけでは足りない理由`、`一次文献が示す現実`、`最低限分けて残すもの`、`降格ルール`、`参考文献` を新設
  - trait を `trait-like backbone` として再定義
  - fixed decoder interval と recalibration burden を明示
- site-wide label consistency
  - `不確実性・信頼区間・棄権` の旧リンク文言を、改題済みの `不確実性・校正・棄権` へ合わせて更新

## 外部依存で保留

- cross-modal longitudinal benchmark の実装
  - 担当者: AI / maintainer / 実験系 collaborators
  - 前提条件: 同一被験者で state 操作、長期再計測、fixed decoder hold、recalibration log を含む公開データ
  - 完了条件: EEG / 侵襲 BCI / fMRI の少なくとも 2 系統で、同一 schema の `state sensitivity / trait backbone / drift / recalibration burden` 比較が可能になること

## 参考文献

- Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. Nat Neurosci. 2019.
  - https://doi.org/10.1038/s41593-019-0502-4
- Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. Nat Neurosci. 2024.
  - https://doi.org/10.1038/s41593-023-01498-y
- Gallego JA, Perich MG, Chowdhury RH, Solla SA, Miller LE. Long-term stability of cortical population dynamics underlying consistent behavior. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-019-0555-4
- Finn ES, Shen X, Scheinost D, et al. Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity. Nat Neurosci. 2015.
  - https://doi.org/10.1038/nn.4135
- Roth ZN, Merriam EP. Representations in human primary visual cortex drift over time. Nat Commun. 2023.
  - https://doi.org/10.1038/s41467-023-40144-w
- Noda T, Kienle E, Eppler J-B, et al. Homeostasis of a representational map in the neocortex. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01982-7
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
