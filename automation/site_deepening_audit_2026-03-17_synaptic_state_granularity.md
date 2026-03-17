# Site Deepening Audit (2026-03-17, Synaptic State Granularity / Structural Prior ≠ Current Weight)

## 対象

- 主対象: `wbe_101.md`
- 副対象: `faq.md`
- 副対象: `verification.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`connectome-complete ≠ emulation-complete`、`same-brain function ≠ current weight readout` をかなり強く区別できていました。
- その一方で、入口ページでは `synaptic state` がなお 1 行に圧縮されやすく、`presynaptic release probability`、`postsynaptic AMPAR / silent-synapse state`、`membrane-state-gated consolidation` が十分に分離されていませんでした。
- 加えて、Mittermaier 論文は public pages 間で筆頭著者名と DOI が崩れており、読者が原著へ戻る導線を壊していました。

## 主要な批判点

### 1. `WBE 101` の evidence table に synaptic-state 行がなく、入口ページで相対的に弱く見えていました

- 問題:
  - hidden-state の総論では `current synaptic efficacy / release state` に触れていた一方、table 上では dendrite や excitability と違って独立した evidence row がありませんでした。
  - そのため、読者が `synaptic state` を補助的な caveat と読み、WBE の mechanistic boundary として相対的に軽く扱いやすい構造が残っていました。
- 根拠:
  - Holler et al. (2021) は PSD 面積と平均 EPSP の対応を前進させつつ、trial-to-trial 対応の弱さも示しました。
  - Dürst et al. (2022) は bouton potency が主として vesicular release probability に依存することを示しました。
  - Matsuzaki et al. (2004), Vardalaki et al. (2022), Li et al. (2025) は postsynaptic AMPAR / silent-synapse 側の状態変数を押し上げました。
  - Mittermaier et al. (2024) は human neocortical tissue で membrane-state sequence が transmission / consolidation を短時間で動かすことを示しました。
- 修正:
  - `wbe_101.md` に `synaptic efficacy / release state / receptor occupancy` の独立 row を追加しました。
  - あわせて `synaptic state は 1 個の数字ではありません` という note を追加し、structural prior と current weight を分離しました。

### 2. `FAQ` は synaptic-state line をほぼ 1 本の human paper で代表させており、粒度が不足していました

- 問題:
  - `faq.md` の Q2c では fast execution state の代表として、Mittermaier 論文の旧誤表記に依存した参照が中心で、presynaptic / postsynaptic / state-gated consolidation の 3 層が潰れていました。
  - しかも筆頭著者名と DOI が誤っており、原著導線として不正確でした。
- 根拠:
  - presynaptic 側は Dürst et al. (2022) の `p_ves` が直接的です。
  - postsynaptic 側は Matsuzaki (2004), Vardalaki (2022), Li (2025) が補完します。
  - human tissue 側は Mittermaier et al. (2024) が short-timescale の state gating を与えます。
- 修正:
  - `faq.md` の Q2c を、`structural prior`、`presynaptic release probability`、`postsynaptic AMPAR / silent-synapse state`、`membrane-state-gated consolidation` に分解しました。
  - Mittermaier 論文の筆頭著者名と DOI を修正しました。

### 3. Verification 側は `current weight` を止める規則はあったものの、何が presynaptic で何が postsynaptic かは曖昧でした

- 問題:
  - `verification.md` の latent-state error budget では、`synaptic efficacy / plastic history` 行が存在していましたが、提出物レベルで `presynaptic release probability` と `postsynaptic receptor-state` を明示する粒度にはなっていませんでした。
- 根拠:
  - current synaptic state を支配する量は 1 本ではなく、Holler, Dürst, Matsuzaki, Vardalaki, Li, Mittermaier が別々の層を押し上げています。
- 修正:
  - `verification.md` の row を `presynaptic release-probability / postsynaptic receptor-state / plasticity` の監査に拡張しました。
  - note と reference list も整え、`structural prior ≠ current effective weight` をより operational にしました。

### 4. same-brain connectomics を `structural hallmark` と `momentary state` に切り分ける文章がまだ甘い箇所がありました

- 問題:
  - `wiki/connectome-is-not-enough.md` と `wiki/measurement-stack-and-claim-ceiling.md` は既に構造対状態の区別を強く書いていましたが、2025 年の engram / AMPAR 文献を踏まえると、`structural hallmark` と `momentary synaptic state` の差をさらに明示できました。
- 根拠:
  - Li et al. (2025) は memory-related ensemble への AMPAR redistribution を示しました。
  - Uytiepo et al. (2025) は memory engram の structural hallmark を示しました。
  - これらは重要な前進ですが、それでも `momentary current weight` の全脳 readout ではありません。
- 修正:
  - `wiki/connectome-is-not-enough.md` に Li / Uytiepo を追加し、`engram-scale structural hallmark` を `structural prior / state-averaged constraint` として扱う規則を明示しました。
  - `wiki/measurement-stack-and-claim-ceiling.md` も synaptic-state line を同じ粒度へ揃えました。

## 今回実行した変更

- `wbe_101.md`
  - synaptic-state の独立 evidence row を追加
  - synaptic state の 3 分解（presynaptic / postsynaptic / state-gated consolidation）を note で明示
  - 参考文献に Holler, Dürst (2022), Matsuzaki, Vardalaki, Li, Mittermaier を追加
- `faq.md`
  - Q2c の fast execution state を presynaptic / postsynaptic / human state-gating へ分解
  - Mittermaier 論文の筆頭著者名と DOI を修正
  - 参考文献を追加
- `verification.md`
  - latent-state error budget の synaptic 行を presynaptic / postsynaptic の粒度へ拡張
  - note を更新し、reference list を修正
- `wiki/connectome-is-not-enough.md`
  - Li / Uytiepo を追加
  - `engram-scale structural hallmark` を structural prior として扱う規則を追加
  - Mittermaier 論文の表記を修正
- `wiki/measurement-stack-and-claim-ceiling.md`
  - same-brain connectomics の synaptic-state 説明を更新
  - reference list を修正

## 外部依存で保留

- なし
  - 今回の修正は、公開本文・wiki・検証規則の改稿で完結しています。

## 参考文献

1. Holler S, et al. Structure and function of a neocortical synapse. *Nature*. 2021.
   - https://doi.org/10.1038/s41586-020-03134-2
2. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-33565-6
3. Matsuzaki M, Honkura N, Ellis-Davies GCR, Kasai H. Structural basis of long-term potentiation in single dendritic spines. *Nature*. 2004.
   - https://doi.org/10.1038/nature02617
4. Vardalaki D, Chung K, Harnett MT. Filopodia are a structural substrate for silent synapses in adult neocortex. *Nature*. 2022.
   - https://doi.org/10.1038/s41586-022-05483-6
5. Mittermaier V, Kononenko NL, Jin Y, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-024-53901-2
6. Li J, et al. Dynamic redistribution of AMPA receptors toward memory-related neuronal ensembles in mice barrel cortex during sensory learning. *Neuron*. 2025.
   - https://doi.org/10.1016/j.neuron.2025.06.002
7. Uytiepo M, et al. Synaptic architecture of a memory engram in the mouse hippocampus. *Science*. 2025.
   - https://doi.org/10.1126/science.ado8316
