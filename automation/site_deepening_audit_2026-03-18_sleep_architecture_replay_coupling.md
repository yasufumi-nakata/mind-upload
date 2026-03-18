# Site Deepening Audit (2026-03-18, Sleep Architecture / Replay-Coupling)

## 対象

- 主対象: `verification.md`
- 副対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `index.md`

## 今回の選定理由

- 既存サイトは、`sleep / wake history` や `sleep-dependent homeostasis` を maintenance-state の一部としてすでに正しく扱っていました。
- しかし現状のままだと、`睡眠があった` ことと、`slow oscillation / spindle / ripple の位相結合や replay window が consolidation-permissive だった` ことが近すぎます。
- 技術・自然科学の観点では、ここを分けないと `same-day fit は違うが overnight なら近い` という読みを止める力が弱く、cross-day claim の ceiling が甘くなります。

## 主要な批判点

### 1. `sleep / wake history` は必要条件でも、固定化機構の記述としては粗すぎました

- 問題:
  - 旧版の maintenance-state error budget は `sleep / wake history` を持っていましたが、`どの NREM window で consolidation が進んだか` や `slow oscillation / spindle / ripple の協調があったか` を独立 field にしていませんでした。
  - この構造だと読者が `寝た/寝ていない` を、そのまま `記憶固定化機構が揃っていた/いなかった` へ読み替えやすいままでした。
- 根拠:
  - Ngo et al. (2013) は、ヒトで slow oscillation up-state に位相を合わせた closed-loop auditory stimulation だけが memory と spindle coupling を改善し、位相外刺激は効かないことを示しました。
  - Maingret et al. (2016) は、ラットで hippocampal sharp-wave ripples と cortical delta / spindle の時間協調を強めたときにだけ翌日の成績が改善することを示しました。
  - Latchoumane et al. (2017) は、マウスで thalamic spindle を slow oscillation up-state に合わせて誘導したときだけ、triple coupling と hippocampus-dependent memory が改善することを示しました。
- 修正:
  - `verification.md` に `Sleep architecture / replay-coupling state` を新設し、`sleep / wake history` とは別の提出物にしました。

### 2. 人で見えている sleep evidence の層差が十分に出ていませんでした

- 問題:
  - 旧版は `sleep history` や `overnight recovery` を書けば、human-side evidence がある程度揃ったように読める余地を残していました。
  - しかし実際には、scalp で見える stage composition / SO-spindle coupling、iEEG で見える ripple coupling、closed-loop DBS や phase-locked stimulation の causal evidence は同じ層ではありません。
- 根拠:
  - Schreiner et al. (2021) は、ヒト nap EEG で endogenous memory reactivation が SO-spindle complexes に clocked され、その coupling precision が reactivation strength と consolidation を予測することを示しました。
  - Geva-Sagiv et al. (2023) は、ヒト intracranial closed-loop DBS により hippocampal-prefrontal synchrony を増強すると overnight memory が改善することを示しました。
  - Schreiner et al. (2024) は、ヒト NREM で spindle-locked ripples が memory reactivation に結びつくことを示しました。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` に、sleep history と sleep architecture / replay-coupling を分ける addendum を追加し、human では scalp proxy と intracranial evidence を同列に扱わないことを明記しました。

### 3. `cross-day score` と `consolidation-consistent mechanism` の距離がまだ十分に見えていませんでした

- 問題:
  - 旧版でも `same-day fit != cross-day maintenance` は書かれていましたが、`cross-day hold != replay-coupling-matched consolidation` という stop rule が弱いままでした。
  - そのため、night interval をまたいだ score 保持が、そのまま mechanistic support に読まれる危険がありました。
- 根拠:
  - Deng et al. (2025) は NREM 中の cAMP oscillation が memory consolidation の時間窓を規定することを示し、`sleep があった` だけでなく `いつ / どの window か` が重要であることを示しました。
- 修正:
  - `wbe_101.md` と `index.md` に、`sleep duration or recovery label alone is not consolidation-mechanism evidence` という入口側の読み方を追加しました。

## 今回実行した変更

- `verification.md`
  - maintenance-state error budget に `Sleep architecture / replay-coupling state` を追加
  - `sleep history` と `sleep architecture` を別々に扱う addendum を追加
  - front matter の highlights / known points を更新
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `13 maintenance-states` に更新
  - maintenance-state table に `Sleep architecture / replay-coupling state` を追加
  - sleep section に `Sleep history is not sleep architecture` addendum を追加
  - practical rule を追加し、front matter を更新
- `wbe_101.md`
  - hidden-state の導入文に sleep architecture / replay-coupling の一次文献を追加
  - hidden-state table に `Sleep architecture / replay-coupling state` を追加
  - front matter を更新
- `index.md`
  - landing page の maintenance-state note と front matter を更新

## 外部依存で保留

- human whole-brain replay-coupling ground truth
  - 担当者: 睡眠計測・iEEG・神経刺激系の実験研究者
  - 前提条件: hippocampal ripple, cortical slow oscillation, spindle coupling を large-scale human setting で同時に観測または強く外部較正できる計測系
  - 完了条件: `overnight retention` と `sleep architecture / replay-coupling state` を同一 protocol 上で比較できる公開 benchmark が整備されること

## 参考文献

1. Ngo H-VV, Martinetz T, Born J, Mölle M. Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. *Neuron*. 2013;78(3):545-553.
   - https://doi.org/10.1016/j.neuron.2013.03.006
2. Maingret N, Girardeau G, Todorova R, Goutierre M, Zugaro M. Hippocampo-cortical coupling mediates memory consolidation during sleep. *Nature Neuroscience*. 2016;19:959-964.
   - https://doi.org/10.1038/nn.4304
3. Latchoumane C-FV, Ngo H-VV, Born J, Shin H-S. Thalamic Spindles Promote Memory Formation during Sleep through Triple Phase-Locking of Cortical, Thalamic, and Hippocampal Rhythms. *Neuron*. 2017;95(2):424-435.e6.
   - https://doi.org/10.1016/j.neuron.2017.06.025
4. Schreiner T, Petzka M, Staudigl T, Staresina BP. Endogenous memory reactivation during sleep in humans is clocked by slow oscillation-spindle complexes. *Nature Communications*. 2021;12:3112.
   - https://doi.org/10.1038/s41467-021-23520-2
5. Geva-Sagiv M, Mankin EA, Eliashiv D, et al. Augmenting hippocampal-prefrontal neuronal synchrony during sleep enhances memory consolidation in humans. *Nature Neuroscience*. 2023;26:1100-1110.
   - https://doi.org/10.1038/s41593-023-01324-5
6. Schreiner T, Petzka M, Staudigl T, et al. Spindle-locked ripples mediate memory reactivation during human NREM sleep. *Nature Communications*. 2024;15:5367.
   - https://doi.org/10.1038/s41467-024-49572-8
7. Deng Z, Fei X, Zhang S, Xu M. A time window for memory consolidation during NREM sleep revealed by cAMP oscillation. *Neuron*. 2025;113(12):1983-1997.e7.
   - https://doi.org/10.1016/j.neuron.2025.03.020
