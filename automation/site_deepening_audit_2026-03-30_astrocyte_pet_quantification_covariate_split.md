# Site Deepening Audit (2026-03-30, astrocyte PET quantification / covariate split)

## 対象

- 主対象:
  - `wbe_101.md`
  - `faq.md`
  - `mind_uploading_papers.md`
  - `verification.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## web確認対象

- `https://doi.org/10.2967/jnumed.121.263254`
- `https://doi.org/10.1007/s12149-025-02083-y`
- `https://doi.org/10.2967/jnumed.118.208009`
- `https://doi.org/10.1038/s41380-021-01429-y`
- `https://doi.org/10.1038/s41380-025-03355-9`
- `https://doi.org/10.1007/s00401-024-02712-2`

## 今回この箇所を選んだ理由

- 2026-03-30 時点で、このサイトはすでに `astrocyte evidence is not one class` という一次停止条件をかなり強く実装しておりました。
- ただし front door 側では、human astrocyte PET の stop rule が実質的に
  - `MAO-B`
  - `I2BS`
  の target split に強く依存しており、
  - `same target inside MAO-B`
  - `quantification route`
  - `scan window / reference region / kinetic model`
  - `disease stage / severity`
  - `smoking-related covariates`
  までを短い入口文で十分に止め切れておりませんでした。
- そのため、入口だけ読んだ読者が
  - `human astrocyte PET exists`
  - `MAO-B PET exists`
  を
  - `one generic astrocyte-state meter`
  のように過読する余地が残っておりました。

## 主要結論

- 現在の human astrocyte PET は、少なくとも次の 4 軸で止める必要がございました。
  - `molecular target`
  - `quantification route`
  - `disease / cohort regime`
  - `material covariates`
- よって safe reading は
  - `target-defined astrocyte-related proxy`
  だけでは不十分で、
  - `target-defined`
  - `quantification-defined`
  - `disease- / covariate-conditioned`
  astrocyte-related proxy に留めるのが妥当でございます。
- 以下の overread は front door でも禁止すべきでございます。
  - `astrocyte PET = one generic astrocyte scalar`
  - `MAO-B PET = route-free astrocyte-state meter`
  - `astrocyte PET = content-specific astrocyte-ensemble identity`
  - `target split only = sufficient interpretation`

## 根拠付き批判

### 1. MAO-B と I2BS の分離は必要ですが、それだけでは不十分でございます

- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) は `18F-SMBT-1` を MAO-B-selective reactive-astrogliosis proxy として first-in-human で示しました。
- [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は `11C-BU99008` を I2BS route として示し、isocarboxazid で block されないことから MAO-B PET と別 target であることを示しました。

批判:

- したがって `astrocyte PET` を一行で読むことはできません。
- しかし同時に、`MAO-B` と `I2BS` に分ければ終わりでもございません。
- 同じ `MAO-B` target 内でも、何を quantity として読んでいるのかがさらに分かれます。

### 2. 同じ MAO-B route の内部でも quantification route が固定されておりません

- [Hiraoka et al. (2025)](https://doi.org/10.1007/s12149-025-02083-y) は `18F-SMBT-1` PET について、kinetic modeling に対して `SUV` / `SUVR-1` の scan window と reference-region choice を明示的に比較しました。
- 同論文の要点は、`MAO-B PET` というラベルだけでは quantity が定まらず、
  - `50-70 min`
  - `70-90 min`
  - `SUVR-1`
  - `reference region`
  - `kinetic model`
  の route burden を明示しなければ読めないということでございます。

批判:

- したがって `MAO-B PET was measured` だけでは、まだ route が固定されておりません。
- `same target` でも `same quantity` とは限りません。

### 3. human astrocyte PET は disease stage / severity に対して単調スカラーではございません

- [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) は `11C-BU99008` uptake が region と impairment stage に依存し、Aβ-positive MCI と AD で同じ方向の一様変化にならないことを示しました。
- [Best et al. (2026)](https://doi.org/10.1038/s41380-025-03355-9) は `11C-SL25.1188` による human MAO-B PET で、AUD 群全体として mean binding が有意に上がるわけではなく、severity と daily cigarette use で binding が動くことを示しました。

批判:

- したがって human astrocyte PET は
  - `more disease = more signal`
  のような単調な scalar として読めません。
- さらに `disease regime` が違えば signal direction の読みも変わり得ます。

### 4. postmortem 側でも MAO-B 自体が disease class で変わります

- [Jaisa-Aad et al. (2024)](https://doi.org/10.1007/s00401-024-02712-2) は、MAO-B が主に astrocytic であることを支持しつつも、AD/ADRD class によって expression pattern が異なることを示しました。

批判:

- したがって `MAO-B = one stable astrocyte biomarker` と読むのは過読でございます。
- PET side の quantification burden と pathology-class burden は別々に残ります。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - `How this site reads current human astrocyte evidence` を強化し、
    - `target split`
    - `quantification route`
    - `disease / cohort regime`
    - `covariate regime`
    の 4 軸で読む stop rule を入れました。
  - astrocyte route-card の `Human target / quantity type / tracer burden` を拡張し、
    - `validated scan window / reference region or kinetic model`
    - `smoking or recent substance exposure`
    を明示しました。
  - Hiraoka 2025 / Best 2026 を参考文献へ追加しました。
- `wbe_101.md`
  - 誤 DOI `10.2967/jnumed.121.263255` を正 DOI `10.2967/jnumed.121.263254` に修正しました。
  - astrocyte front-door note を `target-defined and quantification-/regime-conditioned proxy class` に更新しました。
  - human astrocyte PET row を `quantification-conditioned` まで明記する形へ更新しました。
- `faq.md`
  - human astrocyte PET row を `named quantification route and cohort / covariate regime` まで明記する形へ更新しました。
  - 新しい note box
    - `Human astrocyte PET needs a second split inside the tracer label`
    を追加しました。
  - Hiraoka 2025 / Best 2026 を参考文献へ追加しました。
- `mind_uploading_papers.md`
  - paper-front door の technical addendum に、
    - MAO-B vs I2BS split だけでなく
    - MAO-B 内部の quantification route / severity / smoking burden
    も必要だと明示しました。
  - 誤 DOI `10.2967/jnumed.121.263255` を全て `10.2967/jnumed.121.263254` へ修正しました。
- `verification.md`
  - astrocyte support の submission burden に
    - `quantification route`
    - `disease / cohort regime`
    - `material covariates`
    を追加し、公開ルールと同期しました。

## 今回止めた誤読

- `MAO-B vs I2BS が分かれていれば astrocyte PET は十分に読める`
- `MAO-B PET = one route-free astrocyte scalar`
- `human astrocyte PET = generic astrocyte-state meter`
- `astrocyte PET = content-specific astrocyte ensemble`
- `different cohort regimes can be averaged into one baseline`

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、公開ページ改稿、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263254
2. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025;39(11):1249-1257.
   - https://doi.org/10.1007/s12149-025-02083-y
3. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018;59(10):1597-1602.
   - https://doi.org/10.2967/jnumed.118.208009
4. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022;27(4):2019-2029.
   - https://doi.org/10.1038/s41380-021-01429-y
5. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026;31:2191-2201.
   - https://doi.org/10.1038/s41380-025-03355-9
6. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024;147(1):66.
   - https://doi.org/10.1007/s00401-024-02712-2
