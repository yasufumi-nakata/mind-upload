# Site Deepening Audit (2026-03-25, verification state-integrity taxonomy sync)

## 対象

- 主対象: `verification.md`
- 同期対象: `summary_booklet.md`（必要なら再生成）
- 範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `verification.md` は公開サイトの中核ページであり、ここに残る圧縮は site-wide rule 全体の圧縮として読まれます。
- 2026-03-25 時点の live `State variable integrity gate` には、`Intrinsic excitability/homeostasis/maintenance state` や `Neural modification field` のような古い束ね方が残っていました。
- しかし同時に、`wbe_101.md`, `perspective.md`, `wiki/homeostatic-plasticity-and-maintenance-state.md` では、すでに
  - `relative excitability`
  - `AIS / ion-channel configuration`
  - `firing-rate set point / recovery controller`
  - `sleep / wake renormalization`
  - `sleep architecture / replay-coupling`
  - `myelin / oligodendrocyte timing support`
  - `thermal-state`
  - `neuromodulatory specificity / transmitter context`
  - `bioenergetic / mitochondrial state`
  - `astrocyte-state`
  - `clearance / immune support`
  を別々の inferential object として扱っていました。
- つまり、最も重要な verification page が、奥の route-card 規則より粗い taxonomy を public front door に残していた、というのが今回の主要な弱点です。

## 観察した問題

### 1. `verification.md` の gate が現在の route-card 体系より粗いままでした

- 旧本文は `at least thirteen loose state classes` という書き方のまま残っていました。
- table でも、`intrinsic excitability` と `firing-rate recovery`、`sleep history` と `sleep replay`、`myelin support` と `delay`、`neuromodulatory specificity` と `mixed arousal proxy`、`astrocyte-state` と `clearance / immune support` が十分に切り分けられていませんでした。
- この状態だと、読者は `connectome + 少数の補助状態` が現在の site rule よりも state-complete に近いかのような印象を受けます。

### 2. `Neural modification field` という行は、科学的に何を指すのかが不安定でした

- mixed arousal proxy、local transmitter sensor、receptor / transporter atlas prior、occupancy PET、challenge-linked displacement PET は、同じ direct observable でも同じ quantity type でもありません。
- それにもかかわらず verification gate では一つの umbrella row のように読める状態でした。
- これは `human-proxy composition` と `maintenance-state route card` の現在の運用に反します。

### 3. augmentation table にも古い圧縮が残っていました

- 後段の augmentation table に `+ glial / slow-state` という行が残っており、
  - `bioenergetic / mitochondrial`
  - `astrocyte / glial-state`
  - `clearance / immune support`
  の違いが見えませんでした。
- これでは gate 側で family split を強めても、「何を追加したらどの error term が減るのか」が再び曖昧になります。

## 根拠付き批判

### 1. excitability は単一行ではありません

- `relative excitability / allocation bias` と `firing-rate set point / recovery controller` は別物です。
- [Hengen et al. (2016)](https://doi.org/10.1016/j.cell.2016.01.046) は sleep / wake をまたぐ firing-rate homeostasis を示し、allocation bias とは別の controller を固定しました。
- したがって `intrinsic excitability/homeostasis/maintenance state` という一行では粗すぎます。

### 2. sleep history と replay-coupling は別物です

- [Schreiner et al. (2021)](https://doi.org/10.1038/s41467-021-23520-2) は SO-spindle coupling precision と endogenous reactivation を結びつけました。
- [Schreiner et al. (2024)](https://doi.org/10.1038/s41467-024-49572-8) は spindle-locked ripples を示しました。
- [Deng et al. (2025)](https://doi.org/10.1016/j.neuron.2025.03.020) は NREM consolidation に intracellular time window があることを示しました。
- したがって `sleep occurred` と `replay-consistent maintenance` の間には、別の route card が必要です。

### 3. timing support を scalar delay に潰すのは過大です

- [Seidl et al. (2015)](https://doi.org/10.1038/ncomms9073) は node / internode geometry による timing tuning を示しました。
- [Cohen et al. (2020)](https://doi.org/10.1016/j.cell.2019.11.039) は periaxonal nanocircuit を示しました。
- よって `delay` は device latency の数値ではなく、別の tissue-side state family として読む必要があります。

### 4. neuromodulation は one scalar ではありません

- [Reimer et al. (2016)](https://doi.org/10.1038/ncomms13289) は pupil-linked fluctuations が adrenergic / cholinergic activity の mixed proxy であることを示しました。
- [Hansen et al. (2022)](https://doi.org/10.1038/s41593-022-01186-3) は human receptor / transporter atlas という別の inferential object を与えました。
- したがって mixed arousal covariate と transmitter-specific prior / occupancy / release proxy は同じ行に入れるべきではありません。

### 5. thermal-state は generic timing covariate ではありません

- [Rzechorzek et al. (2022)](https://doi.org/10.1093/brain/awab466) は human brain thermometry を独立の observable class として押し上げました。
- したがって timing proxy や vascular nuisance の従属変数としてのみ扱うと、thermal-state の独立 ceiling が見えなくなります。

### 6. astrocyte-state と clearance / immune support は別物です

- [Louveau et al. (2015)](https://doi.org/10.1038/nature14432) は CNS lymphatic vessels を示しました。
- [Kim et al. (2025)](https://doi.org/10.1016/j.cell.2025.02.022) は meningeal-lymphatics-microglia axis による synaptic physiology 制御を示しました。
- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) と [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は human clearance-side proxy classes を押し上げました。
- 一方で astrocyte-state は transmitter integration や recall ensemble 側の問題です。したがって両者を `glial / slow-state` 一行に戻すと、controller と support proxy が再び混ざります。

## 今回実行した変更

- `verification.md`
  - `State variable integrity gate` の導入段落を、古い `13 loose state classes` 言語から、現行 site rule に沿った説明へ差し替えました。
  - table を 3 列から 4 列に改め、
    - `What remains variable`
    - `Shortcut to block`
    - `Ceiling if unmeasured`
    を明示しました。
  - gate 内で以下を独立行として可視化しました。
    - `relative excitability / allocation bias`
    - `AIS / ion-channel configuration`
    - `firing-rate set point / recovery controller`
    - `sleep / wake renormalization`
    - `sleep architecture / replay-coupling state`
    - `myelin / oligodendrocyte timing support`
    - `thermal-state / tissue operating temperature`
    - `neuromodulatory specificity / transmitter context`
    - `bioenergetic / mitochondrial state`
    - `astrocyte / glial-state`
    - `clearance / immune support`
  - `Practical rules here` を、現行 route-card 群への導線として書き換えました。
  - family-specific split を支える一次文献をまとめた `2026-03-25 addendum` を追加しました。
  - augmentation table の `+ glial / slow-state` を廃止し、
    - `+ sleep / wake renormalization audit`
    - `+ sleep architecture / replay audit`
    - `+ thermal-state audit`
    - `+ bioenergetic / mitochondrial audit`
    - `+ astrocyte / glial-state audit`
    - `+ clearance / immune-support audit`
    に分割しました。
- `summary_booklet.md`
  - verification 更新の反映確認のため、再生成対象として扱います。

## 外部依存で保留

- なし
  - 今回の作業は公開本文、監査記録、冊子再生成、ビルド、`push` までこのセッションで完結できます。

## 参考文献

1. Hengen KB, et al. Neural firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016.
   - https://doi.org/10.1016/j.cell.2016.01.046
2. Schreiner T, Petzka M, Staudigl T, Staresina BP. Endogenous memory reactivation during sleep in humans is clocked by slow oscillation-spindle complexes. *Nature Communications*. 2021.
   - https://doi.org/10.1038/s41467-021-23520-2
3. Schreiner T, Petzka M, Staudigl T, et al. Spindle-locked ripples mediate memory reactivation during human NREM sleep. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-024-49572-8
4. Deng Z, Fei X, Zhang S, Xu M. A time window for memory consolidation during NREM sleep revealed by cAMP oscillation. *Neuron*. 2025.
   - https://doi.org/10.1016/j.neuron.2025.03.020
5. Seidl AH, Rubel EW, Barría A. Differential conduction velocity regulation in ipsi- and contralateral collaterals innervating the chick nucleus laminaris. *Nature Communications*. 2015.
   - https://doi.org/10.1038/ncomms9073
6. Cohen CCH, et al. Saltatory conduction along myelinated axons involves a periaxonal nanocircuit. *Cell*. 2020.
   - https://doi.org/10.1016/j.cell.2019.11.039
7. Reimer J, et al. Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. *Nature Communications*. 2016.
   - https://doi.org/10.1038/ncomms13289
8. Hansen JY, et al. A neurotransmitter receptor atlas of the human brain. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01186-3
9. Rzechorzek NM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022.
   - https://doi.org/10.1093/brain/awab466
10. Rangaraju V, Lauterbach M, Schuman EM. Spatially stable mitochondrial compartments fuel local translation during plasticity. *Cell*. 2019.
   - https://doi.org/10.1016/j.cell.2018.12.013
11. Louveau A, et al. Structural and functional features of central nervous system lymphatic vessels. *Nature*. 2015.
   - https://doi.org/10.1038/nature14432
12. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
   - https://doi.org/10.1016/j.cell.2025.02.022
13. Hirschler L, et al. Imaging CSF mobility in the human brain. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
14. Dagum P, et al. The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
