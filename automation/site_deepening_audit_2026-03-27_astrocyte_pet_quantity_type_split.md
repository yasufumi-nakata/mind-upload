# Site Deepening Audit (2026-03-27, Human Astrocyte PET Quantity-Type Split)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `index.md`
- 副対象: `wbe_101.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-21 の監査で、site はすでに `astrocyte / glial-state` を generic support background から切り離し、rodent causal rows と human PET proxy を分けていました。
- しかし、その次の段階でまだ弱い点が残っていました。human 側がなお `reactive-astrogliosis PET` や `astrocyte PET proxy` という一括語で読めてしまい、`MAO-B` と `I2BS` が同じ quantity type であるかのように見える余地がありました。
- これは技術・自然科学の観点で優先度が高いです。human observability ceiling を議論する際には、`astrocyte-related proxy exists` だけでなく、`何を標的にし、どの競合/遮断・病期・モデル条件で読んだのか` を固定しないと、human astrocyte state の見え方を過大評価しやすいからです。

## 根拠付き批判

### 1. Human astrocyte PET は一つの astrocyte meter ではありません

- 問題:
  - 既存サイトは `human reactive-astrogliosis PET` を正しく proxy として扱っていましたが、その内部で `MAO-B` と `I2BS` がまだ分かれていませんでした。
- 根拠:
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) は `18F-SMBT-1` を MAO-B selective tracer として評価し、selegiline による強い blockade を報告しました。
  - [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は `11C-BU99008` を I2BS ligand として評価し、idazoxan 競合はある一方で monoamine oxidase inhibitor `isocarboxazid` では block されないことを示しました。
- 批判:
  - したがって、`human astrocyte PET` を一括語で扱うと target class が消えます。
  - `MAO-B route` と `I2BS route` は同じ molecular object ではなく、同じ inferential object として読むのは粗いです。

### 2. Human astrocyte PET の読みは病期・領域で単調ではありません

- 問題:
  - 既存サイトは human astrocyte PET を proxy class として止めていましたが、なお `one astrocyte scalar in humans` と誤読できる余地がありました。
- 根拠:
  - [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) は `11C-BU99008` で、Aβ-positive MCI が AD より高い uptake を示す領域があり、regional pattern も一様ではないことを報告しました。
  - [Jaisa-Aad et al. (2024)](https://doi.org/10.1007/s00401-024-02712-2) は postmortem で cortical MAO-B が主に astrocytic であることを支持しつつ、AD/ADRD class ごとに expression pattern が異なることを示しました。
- 批判:
  - したがって、human astrocyte PET を `astrocyte reactivity can now be read generically` に昇格させるのは不適切です。
  - 少なくとも `target`, `competition/blockade`, `disease regime`, `quantification route` を disclosure 項目にしなければなりません。

### 3. Human astrocyte PET を rodent ensemble evidence と連続 ladder に置くと誤読が起きます

- 問題:
  - 既存サイトは rodent causal astrocyte evidence を強く扱えていましたが、human PET 側の target split が弱いままだと、`rodent ensemble causality -> human astrocyte PET -> near-direct human astrocyte-state` という滑りが起きます。
- 根拠:
  - [Williamson et al. (2025)](https://doi.org/10.1038/s41586-024-08170-w), [Dewa et al. (2025)](https://doi.org/10.1038/s41586-025-09619-2), [Bukalo et al. (2026)](https://doi.org/10.1038/s41586-025-10068-0) は rodent local circuit / ensemble causal rows です。
  - これに対し Villemagne / Tyacke / Livingston は tracer-defined human PET routes であり、direct observable も causal leverage も spatial unit も違います。
- 批判:
  - したがって、human PET row は `human astrocyte ensemble identity` ではなく、`target-defined astrocyte-related proxy` として止める必要があります。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - astrocyte family の highlights / known points を `MAO-B / I2BS` split に更新
  - `How this site reads current human astrocyte evidence` を改稿し、`SMBT-1`, `BU99008`, `Livingston 2022`, `Jaisa-Aad 2024` を追加
  - astrocyte route card の human field を `Human target / quantity type / tracer burden` に更新
  - human observability table の astrocyte row を `MAO-B / I2BS routes` へ更新
  - human proxy / calibrator 記述を target-defined proxy として同期

- `verification.md`
  - page highlight の astrocyte route-card rule を `human target / quantity type / tracer burden` へ更新
  - astrocyte addendum に `Tyacke 2018`, `Livingston 2022`, `Jaisa-Aad 2024` を追加

- `index.md`
  - landing-page highlight と astrocyte note を `MAO-B / I2BS` split に同期
  - `human astrocyte-related PET` を `target-defined, bounded proxy class` として明示

- `wbe_101.md`
  - `last_updated` を `2026-03-27` に更新
  - entry-level astrocyte note を `MAO-B / I2BS` split に同期
  - human observability table の astrocyte row を `target-defined MAO-B or I2BS route` に更新

- `glossary.md`
  - `Astrocyte / glial-state` 定義に、human astrocyte PET は `MAO-B / I2BS` の target-defined proxy class だと追記

## 今回の修正で止めた誤読

- `human astrocyte PET = one generic astrocyte-state meter`
- `MAO-B PET と I2BS PET はほぼ同じ inferential object`
- `human astrocyte-related proxy exists = human astrocyte ensemble identity is near-directly visible`
- `rodent astrocyte ensemble causality` と `human tracer-defined astrocyte PET` をそのまま一段の ladder に置ける

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文と監査記録の更新のみで完結しています。

## 参考文献

1. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263255
2. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018;59(10):1597-1602.
   - https://doi.org/10.2967/jnumed.118.208009
3. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022;27(4):2019-2029.
   - https://doi.org/10.1038/s41380-021-01429-y
4. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024;147(1):66.
   - https://doi.org/10.1007/s00401-024-02712-2
5. Suzuki A, Stern SA, Bozdagi O, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011;144(5):810-823.
   - https://doi.org/10.1016/j.cell.2011.02.018
6. Cahill MK, Berrios J, Schaid MD, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024;629:146-153.
   - https://doi.org/10.1038/s41586-024-07311-5
7. Williamson NR, Ferreira AN, Watanabe AT, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025;636:445-454.
   - https://doi.org/10.1038/s41586-024-08170-w
8. Dewa K, Kwon O-B, Zheng X, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025;648:99-107.
   - https://doi.org/10.1038/s41586-025-09619-2
9. Bukalo O, Vainchtein ID, Forli A, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
