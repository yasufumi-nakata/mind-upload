# Site Deepening Audit (2026-03-27, human proxy composition taxonomy sync)

## 対象

- 主対象: `wiki/human-proxy-composition.md`
- 同期対象: `wiki/verification-basics.md`
- 派生同期: `summary_booklet.md`
- web確認対象:
  - `https://mind-upload.com/wiki/human-proxy-composition.html`
  - `https://mind-upload.com/wiki/verification-basics.html`
  - `https://doi.org/10.1002/nbm.3384`
  - `https://doi.org/10.1093/pnasnexus/pgaf072`
  - `https://doi.org/10.1002/mrm.70308`
  - `https://doi.org/10.1038/s41598-018-28852-6`
  - `https://doi.org/10.1002/mrm.29998`
  - `https://doi.org/10.1111/bpa.70010`
  - `https://doi.org/10.1016/j.neurobiolaging.2024.12.012`
  - `https://doi.org/10.1002/nbm.5256`
  - `https://doi.org/10.1038/s41467-025-58356-7`
  - `https://doi.org/10.2967/jnumed.121.263255`
  - `https://doi.org/10.2967/jnumed.118.208009`
  - `https://doi.org/10.1038/s41380-021-01429-y`
  - `https://doi.org/10.1007/s00401-024-02712-2`
  - `https://doi.org/10.1038/s41593-025-02073-3`
  - `https://doi.org/10.1038/s41467-026-68374-8`

## 今回この箇所を選んだ理由

- 2026-03-27 の front door 系更新によって、site 本体はすでに
  - `1H-MRSI similarity`
  - `31P energetic balance`
  - `deuterium metabolite / rate`
  - `quantity-defined myelin family`
  - `BBB water-exchange`
  - `tracer-specific BBB transport`
  - `target-defined astrocyte PET`
  - `CSF mobility`
  - `model-based biomarker efflux`
  を分けて読ませる規律へ進んでいました。
- しかし公開中の `wiki/human-proxy-composition.html` は、なお
  - `MRSI`
  - `myelin bilayer MRI`
  - `clearance routes`
  などの旧い粗さを残しており、composition の中核ページが site-wide taxonomy に遅れていました。
- 同時に `wiki/verification-basics.html` には、front matter の unquoted colon による表示崩れまで入り、beginner 入口で
  - `Human proxy bundles now need three axes first`
  の行が実際には壊れた hash 表示になっていました。
- これは単なる文言揺れではありません。reader-facing rule の中核ページが粗いままだと、front door で止めたはずの誤読が composition page で再注入されるからです。

## 根拠付き批判

### 1. composition page 自体がまだ `family name = inferential object` を許していました

- `Lucchetti et al. (2025)` は five-metabolite の `parcel-level similarity scaffold` です。
- `Ren et al. (2015)` は `ATP synthesis / phosphorus metabolite / pH balance` の `31P energetic-balance route` です。
- `Li et al. (2025)` と `Karkouri et al. (2026)` は `deuterated metabolite distributions / kinetic-rate maps` の route です。
- `Koshino et al. (2018)`、`Baadsvik et al. (2024)`、`Galbusera et al. (2025)` は、myelin-family が
  - `MT-family / SyMRI`
  - `bilayer-sensitive mapping`
  - `qT1 remyelination-sensitive contrast`
  に割れていることを示します。
- `Morgan et al. (2024)` と `Padrela et al. (2025)` は `BBB water exchange` です。
- `Chung et al. (2025)` は `tracer-specific BBB permeability-surface-area product` です。
- `Villemagne et al. (2022)` は `MAO-B` route、`Tyacke et al. (2018)` は `I2BS` route であり、同じ astrocyte PET ではありません。

批判:

- したがって、composition の中核ページが `MRSI`、`myelin`、`BBB`、`astrocyte` とだけ置くのは、2026-03-27 時点では粗すぎます。
- quantity type, target class, transport regime が違うなら、bundle composition の条件そのものが変わります。
- この split を欠いた composition page は、site 全体の厳しさを一段階甘く読み替えさせます。

### 2. same bundle の中で cohort / regime が一致していないことを十分に前面化できていませんでした

- `Lucchetti et al. (2025)` の主 cohort は `13-15 years` の adolescents です。
- `Padrela et al. (2025)` は `194 healthy adults` の lifespan reference range です。
- `Hirschler et al. (2025)` は healthy younger adults と CAA cohort を分けています。
- `Dagum et al. (2026)` は `49-66 years` の healthy older adults の crossover です。
- `Villemagne et al. (2022)` は `76 ± 5.5 years` の AD continuum です。
- `Galbusera et al. (2025)` は postmortem MS cortex です。

批判:

- よって、bundle の中で row が増えても、それが one matched human baseline を形成するわけではありません。
- composition rule は quantity split だけでなく、cohort / regime compatibility を front-facing に要求しなければ不十分です。

### 3. beginner verification page が粗い proxy-class 言語を残していました

- `wiki/verification-basics.md` の proxy-class row は、
  - `density proxy`
  - `biochemical similarity scaffold`
  - `kinetic rate map`
  - `myelin proxy`
  - `support-state proxy`
  という旧い表現でした。
- しかし site の現行規律では
  - `31P energetic balance`
  - `deuterium metabolite / rate`
  - `quantity-defined myelin`
  - `BBB water-exchange`
  - `tracer-specific BBB transport`
  - `target-defined astrocyte PET`
  - `CSF mobility`
  - `model-based efflux`
  を beginner page でも最低限分ける必要があります。

批判:

- beginner page で proxy class を粗く置くと、読者は最初の理解段階で `bundle diversity = one shared state meter nearing completion` と誤読します。
- `verification-basics.html` の broken bullet も含め、入口ページとしての品質が current site rule を下回っていました。

## 今回実行した変更

- `wiki/human-proxy-composition.md`
  - `last_updated` を `2026-03-27` に更新しました。
  - front matter の `description` / `page_intro` / `page_highlights` / `known_points` を、`quantity / target / transport` language に同期しました。
  - `What this page fixes` を改稿し、このページ自身が site-wide taxonomy に遅れていたことを明示しました。
  - route matrix を拡張し、
    - `31P energetic-balance route`
    - `dynamic deuterium metabolite / rate imaging`
    - `quantity-defined myelin MRI family`
    - `BBB water-exchange MRI`
    - `tracer-specific BBB PET transport`
    - `target-defined astrocyte PET`
    を composition table に追加しました。
  - `Spectroscopy is not one route` note-box を追加し、`Lucchetti / Ren / Li / Karkouri` を分離しました。
  - `Myelin, BBB, and astrocyte are still family names, not single meters` note-box を追加し、family-internal split が composition 条件に属することを明示しました。
  - `Eight collapse errors` の最上段を `Quantity / target / transport collapse` に改稿し、density / similarity / energetic balance / rate / water exchange / transport / target-defined binding / mobility / efflux を別物として列挙しました。
  - `three axes` table を拡張し、proxy class / operational maturity / calibrator role を新 taxonomy で具体化しました。
  - `promotion-rule` table の proxy-class / direct-observable / calibrator-role 記述を新 taxonomy に同期しました。
  - references に `Ren 2015`, `Karkouri 2026`, `Arshad 2017`, `Koshino 2018`, `Galbusera 2025`, `Morgan 2024`, `Padrela 2025`, `Chung 2025`, `Villemagne 2022`, `Tyacke 2018`, `Livingston 2022`, `Jaisa-Aad 2024` を追加しました。

- `wiki/verification-basics.md`
  - `last_updated` を `2026-03-27` に更新しました。
  - broken display の原因だった `page_highlights` の unquoted colon 行を修正しました。
  - `2026-03-27 correction: route-family names were still too coarse` note-box を追加しました。
  - `proxy-bundle-rules` 導入文に `Ren / Karkouri / Padrela / Chung / Villemagne / Tyacke` を追加し、bundle 内部差を beginner page でも読めるようにしました。
  - proxy-class table を `energetic-balance / deuterium / quantity-defined myelin / BBB water-exchange / tracer-specific transport / target-defined astrocyte / model-based efflux` まで拡張しました。
  - claim-family table の `Living-human proxy bundle` row を新 taxonomy に同期しました。
  - references に上記追加文献を追記しました。

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` による再生成対象としました。

## 今回止めた誤読

- `human spectroscopy` が一つの proxy class である
- `myelin MRI` が一つの interchangeable meter である
- `human BBB proxy` が一つの generic permeability meter である
- `human astrocyte PET` が一つの generic astrocyte-state scalar である
- `composition page は central rule だが front door より粗くてもよい`
- `beginner verification page の proxy class は粗くてよい`

## 外部依存タスク

- なし
  - 今回の作業は repo 内の公開本文、派生 summary、export、build、push までで完結できます。

## 参考文献

1. Ren J, Sherry AD, Malloy CR. <sup>31</sup>P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
2. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
3. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
4. Karkouri J, Novoselova M, Rodgers CT, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
5. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
6. Koshino S, Hagiwara A, Okuda S, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018.
   - https://doi.org/10.1038/s41598-018-28852-6
7. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
8. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025.
   - https://doi.org/10.1111/bpa.70010
9. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024.
   - https://doi.org/10.1002/nbm.5256
10. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
11. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-58356-7
12. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with <sup>18</sup>F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263255
13. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of <sup>11</sup>C-BU99008, a PET Ligand for the Imidazoline<sub>2</sub> Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
14. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel <sup>11</sup>C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
15. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer’s disease and related dementias. *Acta Neuropathologica*. 2024.
   - https://doi.org/10.1007/s00401-024-02712-2
16. Hirschler L, Runderkamp BA, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
17. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
