# Site Deepening Audit (2026-03-17, Dendritic Integration Ceiling / connectome ≠ point-neuron-complete)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-17 時点で、公開サイトは `connectome-complete ≠ emulation-complete`、`same-day fit ≠ cross-day maintenance`、`structural synapse metric ≠ current weight` をかなり強く整理できていました。
- その一方で、単一ニューロン内部の計算をなお暗黙に `point neuron` へ圧縮しやすく、`cell type + synaptic state + somatic output が分かれば、single-neuron transfer function もかなり固定された` と誤読できる余地が残っていました。
- この弱点は技術・自然科学の観点で重要です。現在の一次文献が比較的一貫して示しているのは、樹状突起 branch が単なる入力配線ではなく、`NMDA spike`、`plateau`、`dendritic action potential`、`branch-specific plasticity` を持つ非線形 subunit であり、感覚選択性、知覚、記憶リンクにまで関与するという点だからです。

## 根拠付き批判

### 1. 旧サイトは `synaptic state` と `single-neuron computation` の間にある樹状突起統合状態を独立軸として扱っていませんでした

- 問題:
  - 既存サイトは `current synaptic efficacy`、`intrinsic excitability`、`AIS`、`homeostasis` をかなり丁寧に分けていました。
  - しかし、そこから先の `branch-specific integration state` が独立欄でなかったため、読者が `current weight と gain を押さえれば、あとは point neuron 近似でほぼ足りる` と誤読しうる構造が残っていました。
- 根拠:
  - Schiller et al. (2000) は neocortical pyramidal neuron の basal dendrite で NMDA spike を示しました。
  - Polsky et al. (2004) は thin dendrite が computational subunit として振る舞うことを示しました。
  - Smith et al. (2013) は in vivo で dendritic spike が感覚選択性を高めることを示しました。
- 批判:
  - したがって、`connectome + synaptic state + soma output` をそのまま `single-neuron mechanism` と読むことはできません。
  - 少なくとも site rule 上は、`dendritic integration` を `synaptic efficacy` と `intrinsic excitability` の中間にある独立の hidden-state ceiling として出す必要があります。

### 2. 旧 measurement / verification 仕様では、`dendritic direct evidence` と `soma / morphology proxy` の境界が十分 operational ではありませんでした

- 問題:
  - 従来の公開ページは `EM / same-brain function / Patch-seq / extracellular probe` の主張上限をよく整理していました。
  - ただし、`somatic spike train`、`receptive-field tuning`、`樹状突起形態`、`branch geometry` が、`branch-specific NMDA spike / plateau / dendritic AP` の direct evidence ではないことは、提出物仕様にまだ十分落ちていませんでした。
- 根拠:
  - Cichon & Gan (2015) は branch-specific dendritic Ca2+ spike が持続 plasticity を引き起こすことを示しました。
  - Takahashi et al. (2016) は active cortical dendrite の介入が perception を動かすことを示しました。
  - Sehgal et al. (2025) は branch-specific plasticity が近接時刻の contextual memory linking に関与することを示しました。
- 批判:
  - したがって、`soma-level fit` や `point-neuron model` の成功を、そのまま `single-neuron transfer-function equivalence` と書いてはいけません。
  - Verification では `dendritic-state audit` を `synaptic efficacy audit` から独立させ、`point-neuron / soma-only` 条件と `dendrite-aware` 条件の比較を要求する必要があります。

### 3. 旧 human observability 導線は、`human local ex vivo dendrite evidence` と `whole-brain in vivo ceiling` を十分に分けていませんでした

- 問題:
  - human 側では EM fragment、MRSI、myelin proxy、TMS/EEG plasticity proxy、CSF/glymphatic proxy がかなり整理されていました。
  - しかし、human の dendritic evidence が `局所 ex vivo microcircuit` で前進していることと、`whole-brain in vivo branch-state direct readout は依然ない` ことの両方が、入門と observability page では十分に並びませんでした。
- 根拠:
  - Beaulieu-Laroche et al. (2018) は human cortical neuron の enhanced dendritic compartmentalization を示しました。
  - Gidon et al. (2020) は human layer 2/3 cortical neurons の dendritic action potentials と計算特性を示しました。
- 批判:
  - この 2 本が押し上げるのは `human local dendritic mechanism` の存在であって、`human whole-brain dendritic-state observability` ではありません。
  - したがって、human evidence の表では `local ex vivo` と `whole-brain in vivo` を別 tiers として扱う必要があります。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `7つの状態クラス` を `8つの状態クラス` へ改稿
  - `樹状突起統合状態` を bottom-line table と timescale matrix に追加
  - `樹状突起は point neuron の自動補完先ではありません` 節を新設
  - augmentation / ablation と site rules に `dendritic branch readout / perturbation` と `soma-only fit ≠ branch-state complete` を追加
- `wiki/measurement-stack-and-claim-ceiling.md`
  - state-variable matrix に `dendritic integration / branch-specific nonlinear subunits` 行を追加
  - `whole-brain stack ではほぼ latent` という claim ceiling を明文化
  - 参考文献に dendritic subunit / human dendrite 文献を追加
- `verification.md`
  - `latent-state error budget` に `dendritic integration / local nonlinear subunits` 行を追加
  - `somatic agreement は dendritic-state agreement ではありません` note を追加
  - 参考文献に branch-specific plasticity / human dendrite 文献を追加
- `wbe_101.md`
  - hidden-state の evidence table に `dendritic integration / branch-specific plasticity` 行を追加
  - `point-neuron 化は既定値ではありません` note を追加
  - human observability paragraph に `local ex vivo dendrite evidence` と `whole-brain in vivo ceiling` の差を追記
- `tech_roadmap.md`
  - R 系列の state-variable 列挙へ `樹状突起の branch-specific 統合状態` を追加

## 外部依存で保留

- なし
  - 今回の修正は、公開本文と提出物仕様の更新で完結しています。

## 参考文献

1. Schiller J, Major G, Koester HJ, Schiller Y. NMDA spikes in basal dendrites of cortical pyramidal neurons. *Nature*. 2000;404:285-289.
   - https://doi.org/10.1038/35005094
2. Polsky A, Mel BW, Schiller J. Computational subunits in thin dendrites of pyramidal cells. *Nature Neuroscience*. 2004;7:621-627.
   - https://doi.org/10.1038/nn1253
3. Smith SL, Smith IT, Branco T, Häusser M. Dendritic spikes enhance stimulus selectivity in cortical neurons in vivo. *Nature*. 2013;503:115-120.
   - https://doi.org/10.1038/nature12600
4. Cichon J, Gan WB. Branch-specific dendritic Ca2+ spikes cause persistent synaptic plasticity. *Nature*. 2015;520:180-185.
   - https://doi.org/10.1038/nature14251
5. Takahashi N, Oertner TG, Hegemann P, Larkum ME. Active cortical dendrites modulate perception. *Science*. 2016;354:1587-1590.
   - https://doi.org/10.1126/science.aah6066
6. Beaulieu-Laroche L, Toloza EHS, van der Goes MS, et al. Enhanced Dendritic Compartmentalization in Human Cortical Neurons. *Cell*. 2018;175:643-651.e14.
   - https://doi.org/10.1016/j.cell.2018.08.045
7. Gidon A, Zolnik TA, Fidzinski P, et al. Dendritic action potentials and computation in human layer 2/3 cortical neurons. *Science*. 2020;367:83-87.
   - https://doi.org/10.1126/science.aax6239
8. Sehgal M, et al. Compartmentalized dendritic plasticity in the mouse retrosplenial cortex links contextual memories formed close in time. *Nature Neuroscience*. 2025;28:602-615.
   - https://doi.org/10.1038/s41593-025-01876-8
