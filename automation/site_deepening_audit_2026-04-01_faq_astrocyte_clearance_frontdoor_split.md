# Site Deepening Audit (2026-04-01, FAQ astrocyte / clearance front-door split)

## 対象

- 主対象:
  - `faq.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学
  - 制度論

## 今回この箇所を選んだ理由

- `faq.md` は site の最短 front door であり、最初に読まれる要約ページでございます。
- しかし 2026-04-01 時点でも、central rule pages と `wbe_101.md` がすでに分解している
  - astrocyte PET family
  - human clearance-transport family
  を、FAQ の header bullet と `Q2d` の human-route table ではなお部分的に再圧縮しておりました。
- 入口で family label を粗く戻すと、deep page 側で止めた誤読が最初の導線で再導入されます。
- したがって、今回もっとも改善効果が大きいのは、新しい論文を追加で並べることではなく、FAQ front door 自体を central taxonomy と同期させることだと判断いたしました。

## web で確認した主な一次資料

- `https://doi.org/10.2967/jnumed.121.263254`
- `https://doi.org/10.2967/jnumed.121.263255`
- `https://doi.org/10.1007/s12149-025-02083-y`
- `https://doi.org/10.1007/s12149-025-02144-2`
- `https://doi.org/10.2967/jnumed.118.208009`
- `https://doi.org/10.1038/s41380-021-01429-y`
- `https://doi.org/10.1038/s41380-025-03355-9`
- `https://doi.org/10.1126/science.aax5440`
- `https://doi.org/10.1016/j.neuroimage.2025.121142`
- `https://doi.org/10.1038/s41467-023-37685-5`
- `https://doi.org/10.1038/s41593-025-02073-3`
- `https://doi.org/10.1038/s41467-026-68374-8`

## 根拠付き批判

### 1. FAQ の人間側 front door は astrocyte PET をまだ 1 本の brain-route family に戻しておりました

- 旧 `Q2d` table は
  - `Brain astrocyte-related PET routes`
  - `Whole-body SMBT-1 biodistribution`
  の二行で止まっておりました。
- しかし一次文献は、この圧縮を支持いたしません。
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) は `first-in-human MAO-B target-validation` route であり、selegiline blockade と reversible kinetics を主に支える論文でございます。
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) は `AD-spectrum disease-context` route であり、Aβ burden との関係をみる病理コンテクスト論文でございます。
  - [Hiraoka et al. (2025)](https://doi.org/10.1007/s12149-025-02083-y) はタイトル自体が示す通り `kinetic and quantitative analysis` の論文であり、brain-quantification route でございます。
  - [Mesfin et al. (2026)](https://doi.org/10.1007/s12149-025-02144-2) は `whole-body biodistribution` を扱う tracer-burden route でございます。
  - [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) と [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) は `I2BS` target class であり、MAO-B family と同じ row に戻してはなりません。
  - [Best et al. (2026)](https://doi.org/10.1038/s41380-025-03355-9) は MAO-B binding の解釈が severity / smoking にも動くことを示しました。

批判:

- したがって FAQ front door で `brain astrocyte-related PET` とだけ書くと、
  - target validation
  - disease context
  - brain quantification
  - whole-body tracer burden
  - cross-target interpretation
  の差が消えます。
- これは site-wide の route-role split と矛盾しておりました。

### 2. FAQ の clearance row も、なお `CSF mobility + efflux` へ圧縮されておりました

- 旧 table は human clearance family を
  - `CSF-mobility and sleep-linked clearance routes`
  に近い読みでまとめておりました。
- 一次文献はこの圧縮も支持いたしません。
  - [Fultz et al. (2019)](https://doi.org/10.1126/science.aax5440) は `macroscopic sleep-linked CSF oscillation` route でございます。
  - [Kim, Huang, & Liu (2025)](https://doi.org/10.1016/j.neuroimage.2025.121142) は `parenchyma-CSF water exchange` route でございます。
  - [Eide et al. (2023)](https://doi.org/10.1038/s41467-023-37685-5) は intrathecal gadobutrol と PK-based `CSF-to-blood clearance capacity` route でございます。
  - [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) は `CSF mobility MRI` route でございます。
  - [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は randomized crossover と multicompartment model を用いた `model-based overnight biomarker efflux` route でございます。

批判:

- これらは direct observable, carrier class, crossed boundary, model burden, time window が違います。
- したがって FAQ で `human clearance routes` とだけ書くと、oscillation / water exchange / intrathecal retention / mobility / biomarker efflux がひとつの measurable object に見えてしまいます。

### 3. front door の再圧縮は central rule page の厳密化を打ち消します

- 2026-04-01 時点で、`wiki/human-proxy-composition.md`、`wiki/measurement-stack-and-claim-ceiling.md`、`wiki/homeostatic-plasticity-and-maintenance-state.md`、`wbe_101.md` は、これらの family をすでに分解しておりました。
- それにもかかわらず FAQ の最初の表と要約 bullet が粗いままだと、読者は最初の導線で旧来の family label へ戻ります。

批判:

- FAQ は「短いから粗くてよい」ページではございません。
- むしろ最短 front door だからこそ、最低限の route-family split を visible にする必要がございました。

## 今回実行した変更

### `faq.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` と `known_points` を更新し、astrocyte / clearance family の front-door split を header block でも visible にしました。
- `Q2c` の clearance paragraph を改稿し、
  - macroscopic CSF oscillation
  - parenchyma-CSF water exchange
  - intrathecal tracer / CSF-to-blood clearance
  - CSF mobility
  - model-based biomarker efflux
  が別 route であることを前倒しで明示しました。
- `Q2d` 導入 paragraph を更新し、human clearance family を 5 route に分解して言及しました。
- `Q2d` の human-route table を更新し、astrocyte / clearance row を
  - SMBT-1 MAO-B target validation
  - SMBT-1 AD-spectrum disease context
  - SMBT-1 brain quantification
  - I2BS brain astrocyte PET
  - whole-body SMBT-1 biodistribution
  - macroscopic sleep-linked CSF oscillation
  - parenchyma-CSF water exchange
  - intrathecal tracer / CSF-to-blood clearance
  - CSF mobility MRI
  - sleep-linked biomarker-efflux model
  へ分解しました。
- 新しい note-box `Human clearance-transport also needs a family split at the FAQ front door` を追加しました。
- `Route name alone is too coarse` note を更新し、astrocyte / clearance family の route names を列挙しました。
- 後半の crosswalk table も、
  - MAO-B family
  - I2BS route
  - whole-body biodistribution
  - clearance-transport family
  を分けて読める形へ更新しました。
- references に
  - Fultz et al. (2019)
  - Kim, Huang, & Liu (2025)
  - Eide et al. (2023)
  を追加しました。

## 今回止めた誤読

- `brain astrocyte PET exists` = one reusable astrocyte-state row
- `MAO-B PET` = target validation + disease context + quantification + biodistribution
- `I2BS PET` = MAO-B family の別 quantification option
- `human clearance route exists` = one common measurable glymphatic object
- `CSF oscillation` = `water exchange` = `intrathecal clearance capacity` = `CSF mobility` = `biomarker efflux`
- `FAQ だから route family は粗くてよい`

## external dependency tasks

- なし
  - 今回の作業は一次文献確認、repo 内改稿、ローカル検証、Git 操作で完結できます。

## 参考文献

1. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263254
2. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263255
3. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025.
   - https://doi.org/10.1007/s12149-025-02083-y
4. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
5. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
6. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
7. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
8. Fultz NE, Bonmassar G, Setsompop K, et al. Coupled electrophysiological, hemodynamic, and cerebrospinal fluid oscillations in human sleep. *Science*. 2019.
   - https://doi.org/10.1126/science.aax5440
9. Kim D, Huang Y, Liu J. Non-invasive MRI measurements of age-dependent in vivo human glymphatic exchange using magnetization transfer spin labeling. *NeuroImage*. 2025.
   - https://doi.org/10.1016/j.neuroimage.2025.121142
10. Eide PK, Lashkarivand A, Pripp A, et al. Plasma neurodegeneration biomarker concentrations associate with glymphatic and meningeal lymphatic measures in neurological disorders. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-37685-5
11. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
12. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
