# 2026-03-31 site deepening audit: datasets U3 component-ablation ladder

## 対象として選んだ箇所

- `datasets.md`

## 今回ここを優先した理由

- 2026-03-31 時点の公開サイトは、`index.md`、`wbe_101.md`、`research_harvest_50.md`、`verification.md` で、maintenance-state family が one support bucket ではないことをかなり強く打ち出しておりました。
- しかし、実務入口である `datasets.md` には、`それをどうデータ設計に落とすか` がまだ不足しておりました。
- 現状の `datasets.md` は
  - BIDS / QC / split / benchmark governance
  - EEG-first baseline
  - source-imaging benchmark disclosure
  には強い一方で、
  - neuron-first baseline に対して support-state rows をどう 1 本ずつ足すのか
  - strongest-single-row と full bundle をどう比較するのか
  - どこで主張を止めるのか
  が public page として未固定でございました。

## 根拠付き批判

### 1. 現状の `datasets.md` は `reproducible baseline` までは強いですが、`maintenance-state family の追加価値をどう測るか` を固定していませんでした

- これは practical page として弱点でございます。
- サイト全体ではすでに
  - astrocyte-state
  - neurovascular / BBB / pericyte support
  - clearance / immune support
  - other maintenance-state families
  を分離しているにもかかわらず、`datasets.md` だけがなお `later add more modalities` に近い読み方を許しておりました。
- そのままでは読者が
  - `support variables matter`
  - `therefore any multimodal addition is progress`
  と飛躍できます。

### 2. 一次文献は `support-state` を one family として扱っておりません

- <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a> は、learning-associated astrocyte ensembles が memory recall を制御する route を示しております。
- <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a> は、astrocytic ensemble が repeated experience 後の <strong>multiday trace</strong> として memory stabilization に関わる route を示しております。
- <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> は、amygdala astrocytes が fear-state representation と retrieval / extinction を支える route を示しております。
- <a href="https://doi.org/10.1038/s41467-025-61312-0" target="_blank">Mai-Morente et al. (2025)</a> は、pericyte pannexin1 が capillary diameter と memory function を支える neurovascular-support route を示しております。
- <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a> は、meningeal lymphatics-microglia axis が synaptic physiology を調整する route を示しております。
- <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> は、living humans における CSF mobility を高解像度 MRI で可視化した bounded clearance-side observability route を示しております。
- <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> は、39 participants の randomized crossover trial と multicompartment model により、sleep-active glymphatic clearance と plasma Aβ / tau dynamics を結ぶ route を示しております。
- <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025)</a> は、human BBB permeability-surface-area を tracer-specific PET で定量化する route を提示しつつ、ground truth / test-retest が future work であることも明示しております。

批判:

- これらは
  - species
  - spatial unit
  - time window
  - direct observable
  - route burden
  - human transfer ceiling
  が違います。
- よって practical page でも `one multimodal support bundle` として扱うのは不正確でございました。

### 3. `datasets.md` に ablation ladder が無いと、最小構成の判定が data-driven になりません

- `minimum required configuration` を data-driven に決めるには、
  - neuron-first baseline
  - one-family-at-a-time augmentation
  - strongest-single-row versus full bundle
  - missingness / common-driver audit
  が要ります。
- これが無いと、
  - `all-in bundle beat baseline`
  だけで
  - `minimum biological configuration was identified`
  と誤読されます。
- 一次文献はその飛躍を支持しておりません。astrocyte causality, pericyte support, lymphatic-microglial regulation, CSF mobility, glymphatic efflux, BBB transport quantification は、同じ inferential object を返していないためでございます。

### 4. starter EEG datasets は U3 の検証 board ではなく、baseline arm であることを practical page で明示すべきでした

- `datasets.md` の現行構成では、EEG Motor Movement/Imagery, CHB-MIT, Sleep-EDF, TUH が practical starting point として適切であることは明確でした。
- ただし、それらは
  - astrocyte-state
  - pericyte / BBB support
  - clearance transport
  - meningeal-lymphatic / microglial routes
  を単独では閉じません。
- この stop rule を `datasets.md` に置かないと、public starter datasets が U3 closure board であるかのような誤読が残ります。

## web で確認した主な一次資料

- <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a>
  - learning-associated astrocyte ensembles が memory recall を調整
- <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a>
  - astrocytic ensemble が repeated experience 後の multiday trace として memory stabilization を支える
- <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a>
  - amygdala astrocytes が fear-state-related neural representations を支える
- <a href="https://doi.org/10.1038/s41467-025-61312-0" target="_blank">Mai-Morente et al. (2025)</a>
  - pericyte Panx1 が capillary diameter と memory function を支える
- <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a>
  - meningeal lymphatics-microglia axis が synaptic physiology を調整
- <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a>
  - high-resolution MRI による human CSF mobility route
- <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a>
  - randomized crossover + multicompartment model による sleep-active glymphatic clearance route
- <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025)</a>
  - tracer-specific BBB permeability-surface-area quantification route

## 今回実行した変更

### `datasets.md`

- front matter の `page_highlights` に、maintenance-state routes の component-addition / ablation ladder を追加しました。
- `known_points` に、starter EEG datasets は neuron-first baseline であり、support-state claims には one-family-at-a-time augmentation と strongest-single-row versus bundle comparison が必要であることを追加しました。
- `unknown_points` に、public dataset bundle として shared missingness / common-driver audit を備えた U3 ladder が未確立であることを追加しました。
- `Plan for future expansion` 直後に、
  - なぜ `support-variable` を one bucket と読んではいけないか
  - どの primary papers が astrocyte / pericyte-BBB / clearance を split しているか
  を示す note-box を追加しました。
- 新しい section `A practical component-addition / ablation ladder for maintenance-state routes` を追加し、
  - astrocyte / glial route
  - neurovascular / BBB / pericyte support route
  - clearance / immune / lymphatic route
  - bundle comparison rule
  を table で固定しました。
- 同 section に、minimum loop として
  - neuron-first baseline freeze
  - one-family-at-a-time augmentation
  - direct observable / time window / spatial unit / route class disclosure
  - strongest-single-row vs full bundle comparison
  - stop-at-incremental-gain rule
  を ordered list として追加しました。
- starter EEG datasets は baseline arm にすぎないことを明示する note-box を追加しました。
- references に今回前面化した U3 primary papers を追加しました。

## 今回止めた誤読

- `support variables matter` = `any multimodal addition counts as progress`
- `astrocyte`, `BBB`, `glymphatic`, `pericyte`, `microglia` は one support bucket
- `all-in bundle beats baseline` = `minimum required biological configuration identified`
- starter EEG datasets はそのまま U3 closure board である
- bounded human proxy gain = local controller identified

## 検証

- `bundle exec jekyll build`
- `git diff --stat`
- `git diff --check`

## external dependency tasks

- なし
  - 今回の主作業は、web 上の一次資料確認、repo 内 public page 修正、監査メモ追加、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Williamson MR, Kwon W, Woo J, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025. https://doi.org/10.1038/s41586-024-08170-w
2. Dewa K, Kaseda K, Kuwahara A, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025. https://doi.org/10.1038/s41586-025-09619-2
3. Bukalo O, O'Sullivan R, Tanisumi Y, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026. https://doi.org/10.1038/s41586-025-10068-0
4. Mai-Morente S, Isasi E, Rafael A, et al. Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. *Nature Communications*. 2025;16:6128. https://doi.org/10.1038/s41467-025-61312-0
5. Kim K, Abramishvili D, Du S, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025;188(10):2705-2719.e23. https://doi.org/10.1016/j.cell.2025.02.022
6. Hirschler L, Runderkamp BA, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28:2392-2401. https://doi.org/10.1038/s41593-025-02073-3
7. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076. https://doi.org/10.1038/s41467-025-58356-7
8. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715. https://doi.org/10.1038/s41467-026-68374-8
