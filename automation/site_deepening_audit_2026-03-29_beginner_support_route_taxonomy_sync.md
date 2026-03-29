# Site Deepening Audit (2026-03-29, beginner support-route taxonomy sync)

## 対象

- 主対象:
  - `wiki/mind-upload-basics.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- site 全体では human support-state / maintenance-state route を proxy class ごとに読む規則がかなり整ってきておりました。
- しかし beginner / supporting wiki 層ではなお、
  - `BBB permeability / transport`
  - `astrocyte PET`
  - `CSF mobility / sleep-linked clearance`
  のような圧縮が残っておりました。
- これは wording の問題ではございません。direct observable、model burden、safe calibrator role が違う route を一つの human support-state row に戻してしまうため、front door 側で導入済みの route-card discipline と矛盾いたします。

## 主要結論

- `human BBB evidence` は一つの inferential object ではございません。
  - [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) と [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は `BBB water exchange` route でございます。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は `tracer-specific BBB transport` route でございます。
- `human astrocyte PET` も一つの scalar ではございません。
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) と [Jaisa-Aad et al. (2024)](https://doi.org/10.1007/s00401-024-02712-2) は `MAO-B-related astrocyte` route でございます。
  - [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) と [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) は `I2BS-related astrocyte` route でございます。
- `human clearance evidence` も一つの route ではございません。
  - [Fultz et al. (2019)](https://doi.org/10.1126/science.aax5440): macroscopic CSF oscillation
  - [Kim, Huang, & Liu (2025)](https://doi.org/10.1016/j.neuroimage.2025.121142): parenchyma-CSF water exchange
  - [Eide et al. (2023)](https://doi.org/10.1038/s41467-023-37685-5): intrathecal tracer / CSF-to-blood clearance capacity
  - [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3): CSF mobility
  - [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8): model-based overnight biomarker efflux

## 根拠付き批判

### 1. BBB water exchange と tracer-specific BBB transport は同じ量ではございません

- [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は diffusion-prepared / multi-echo ASL による blood-brain barrier water exchange rate を扱っております。
- [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) も multi-echo ASL による water permeability を adult lifespan で比較しております。
- [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は total-body PET と kinetic modeling により molecular blood-brain barrier permeability を tracer-specific transport object として扱っております。

批判:

- `BBB permeability / transport` の一語では water-exchange と tracer-specific transport が潰れます。
- 一方は ASL fitting burden を伴う water-exchange proxy、他方は tracer choice と kinetic model に依存する transport proxy でございます。
- したがって beginner page でも `generic BBB leakiness meter` のように読める表現は不適切でございます。

### 2. MAO-B PET と I2BS PET を一つの astrocyte row にしてはいけません

- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) は `18F-SMBT-1` による MAO-B tracer evaluation でございます。
- [Jaisa-Aad et al. (2024)](https://doi.org/10.1007/s00401-024-02712-2) は MAO-B を reactive astrogliosis biomarker として整理しております。
- [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は `11C-BU99008` による imidazoline2 binding site route でございます。
- [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) は `11C-BU99008 PET` と糖代謝・灰白質容積・アミロイド負荷の関係を扱っております。

批判:

- `human astrocyte PET` という一行は、target dependence を消してしまいます。
- MAO-B-related burden と I2BS-related burden は interchangeable ではございません。
- したがって astrocyte proxy は `route-free astrocyte-state scalar` として書いてはならず、target-defined proxy として明示すべきでございます。

### 3. clearance route は少なくとも 5 つの proxy class に分かれます

- [Fultz et al. (2019)](https://doi.org/10.1126/science.aax5440) は sleep-linked macroscopic CSF oscillation でございます。
- [Kim, Huang, & Liu (2025)](https://doi.org/10.1016/j.neuroimage.2025.121142) は parenchyma-CSF water exchange でございます。
- [Eide et al. (2023)](https://doi.org/10.1038/s41467-023-37685-5) は intrathecal gadobutrol retention と PK-based CSF-to-blood clearance variables を扱っております。
- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) は MRI-based CSF mobility を扱っております。
- [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は multicompartment model 付き overnight amyloid-beta / tau efflux を扱っております。

批判:

- `CSF mobility / sleep-linked clearance` では oscillation、water exchange、intrathecal tracer retention、mobility、biomarker efflux が同じ row に圧縮されます。
- これにより net molecular flux、protein-specific efflux、CSF-to-blood clearance capacity、macro mobility という別々の inferential object が混線いたします。
- beginner 層でこの圧縮を残すと、front door で止めた誤読が support page で再導入されます。

### 4. beginner page だから coarse taxonomy でよい、という運用は成立しません

- `wiki/mind-upload-basics.md` は site の入門導線でございます。
- `wiki/measurement-stack-and-claim-ceiling.md` は claim ceiling の読み方を教育する central supporting page でございます。

批判:

- この 2 ページで coarse wording を許すと、読者は最も重要な導線で `one modality family = one measurable state` と誤読いたします。
- したがって beginner page ほど `what the route directly constrains` を明示する必要がございます。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `Human BBB water-exchange MRI` と `Human tracer-specific BBB transport PET` を分離しました。
  - `Human MAO-B astrocyte PET` と `Human I2BS astrocyte PET` を分離しました。
  - clearance 系を
    - `Human macroscopic CSF-oscillation proxy`
    - `Human parenchyma-CSF water-exchange proxy`
    - `Human intrathecal tracer / CSF-to-blood clearance proxy`
    - `Human CSF-mobility MRI`
    - `Human model-based overnight biomarker efflux`
    に分離しました。
  - beginner note を更新し、quantity type が claim の一部であることを明示しました。

- `wiki/measurement-stack-and-claim-ceiling.md`
  - section 7 の introductory paragraph を route-family 単位へ改稿しました。
  - ladder table に BBB、astrocyte、clearance の分離 rows を追加しました。
  - `Proxy class / operational maturity / calibrator role` note を route split に整合させました。
  - `Site rule for human proxy classes` を更新し、human support-state routes を coarse label で済ませない規則を本文に固定しました。

## 今回止めた誤読

- `BBB water exchange` = `tracer-specific BBB transport`
- `astrocyte PET` = one route-free astrocyte scalar
- `CSF mobility MRI` = direct clearance truth
- `sleep-linked CSF oscillation` = protein-efflux proof
- `intrathecal tracer retention` = natural-sleep whole-brain clearance truth
- beginner page では route naming を粗くしてよい

## 外部依存タスク

- なし
  - 今回の変更は一次文献の web 確認、repo 内改稿、検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024.
   - https://doi.org/10.1002/nbm.5256
2. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
3. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-58356-7
4. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263254
5. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024.
   - https://doi.org/10.1007/s00401-024-02712-2
6. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
7. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
8. Fultz NE, Bonmassar G, Setsompop K, et al. Coupled electrophysiological, hemodynamic, and cerebrospinal fluid oscillations in human sleep. *Science*. 2019.
   - https://doi.org/10.1126/science.aax5440
9. Kim D, Huang Y, Liu J. Non-invasive MRI measurements of age-dependent in vivo human glymphatic exchange using magnetization transfer spin labeling. *NeuroImage*. 2025.
   - https://doi.org/10.1016/j.neuroimage.2025.121142
10. Eide PK, Lashkarivand A, Pripp AH, et al. Plasma neurodegeneration biomarker concentrations associate with glymphatic and meningeal lymphatic measures in neurological disorders. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-37685-5
11. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
12. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
