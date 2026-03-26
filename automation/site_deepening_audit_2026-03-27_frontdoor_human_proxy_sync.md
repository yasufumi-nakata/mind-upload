# Site Deepening Audit (2026-03-27, Front-Door Human Proxy Synchronization)

## 対象

- 主対象: `index.md`
- 主対象: `wbe_101.md`
- 主対象: `verification.md`
- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 派生同期: `summary_booklet.md`

## 今回の選定理由

- 2026-03-27 の一連の監査で、site 本体はすでに `quantity-defined` や `target-defined` の規律をかなり導入していました。
- しかし front door と summary layer には、なお `macro biochemical / energetic / ionic / thermal / myelin / clearance proxies` や `BBB permeability MRI / PET` のような古い総称が残っていました。
- そのため、詳細ページでは分けている inferential object が、入口ページでは再び一つに圧縮され、`human proxy exists` が `human hidden-state is almost directly visible` に滑りやすい状態でした。
- 技術・自然科学の観点では、ここを先に直す価値があります。理由は、入口の一文がその後の読解 ceiling を規定するからです。

## 根拠付き批判

### 1. Front door が human route の quantity type を消していました

- 問題:
  - `index.md` と `wbe_101.md` では、human evidence をなお `macro ... proxies` の束として読める箇所が残っていました。
  - これでは、`sodium MRI`, `myelin MRI`, `BBB MRI / PET`, `astrocyte PET` の内部で異なる quantity / target / transport regime が見えません。
- 根拠:
  - [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は、同一 cohort でも `DP-ASL` と `ME-ASL` で BBB water-exchange 推定値と年齢依存が一致しないことを示しました。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は、human BBB PET が `tracer-specific permeability-surface-area product` を kinetic model の下で扱う route であり、generic leakiness scalar ではないことを示しました。
  - [Arshad et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/) と [Koshino et al. (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6043493/) は、human myelin MRI 指標が interchangeable ではないことを示しました。
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) と [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は、human astrocyte PET が `MAO-B` と `I2BS` で別 target class であることを示しました。
- 批判:
  - したがって、入口で `macro proxy` と総称するだけでは粗すぎます。
  - Front door でも `quantity-defined myelin`, `quantity-defined ionic`, `BBB water-exchange / tracer-specific transport`, `target-defined astrocyte PET` と書き分ける必要があります。

### 2. Detailed page と front door の claim ceiling がずれていました

- 問題:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` の本文深部では、すでに `quantity-defined macro-myelin proxy family`, `human BBB water-exchange or tracer-specific transport proxy route`, `target-defined human astrocyte-related proxy route` が導入済みでした。
  - それにもかかわらず front matter や addendum の一部には、なお `macro ionic proxy`, `macro-myelin proxy`, `macro BBB permeability routes` のような旧い圧縮表現が残っていました。
- 根拠:
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012), [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256), [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) を並べるだけでは、`water exchange` と `tracer-specific transport` の違いは消えます。
  - [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) と [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) を同じ `myelin proxy` とだけ書くと、`bilayer-sensitive route` と `qT1 remyelination-sensitive route` の違いが消えます。
- 批判:
  - 入口と詳細本文で ceiling language がずれていると、site 全体としては reader-facing rule が不安定になります。
  - よって、front matter と addendum の分類語も詳細本文と同じ粒度へ同期させる必要がありました。

### 3. Summary booklet が古い front matter をそのまま再拡散していました

- 問題:
  - `summary_booklet.md` は自動生成物であり、front matter の古い bullet を再掲載していました。
- 根拠:
  - 旧 summary には `macro biochemical / energetic / ionic / thermal / myelin / clearance proxies` という圧縮表現が残っていました。
- 批判:
  - つまり、front door の粗さは一ページの問題ではなく、派生 summary にも再注入されていました。
  - このため、本文修正後に summary booklet も再生成しなければ同期は完了しません。

## 今回実行した変更

- `index.md`
  - human evidence summary を `quantity-defined ionic / myelin proxy families`, `BBB water-exchange or tracer-specific transport proxies`, `target-defined astrocyte PET` へ更新
  - front-door note-box の human route 列挙を詳細ページの分類語に同期

- `wbe_101.md`
  - page highlights の myelin / BBB / layered human evidence を quantity-type language へ更新
  - human observability ladder の BBB row を `Human BBB water-exchange / tracer-specific transport proxy` へ改稿
  - myelin row を `one quantity-defined macro myelin route` に更新
  - myelin / BBB note-box を `myelin-water / MT-family / bilayer / qT1` および `Padrela / Morgan / Chung` の split に同期

- `verification.md`
  - `human maintenance evidence must be class-labeled` addendum の human class list を、receptor/transporter atlas, occupancy, displacement, quantity-defined ionic/myelin, BBB water-exchange / tracer-specific transport, astrocyte target class まで含む形へ更新

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - front matter の highlights / known points / unknown points を quantity-defined / target-defined language に同期
  - human observability ceiling の class list を `quantity-defined macro ionic`, `quantity-defined macro-myelin`, `macro BBB water-exchange / tracer-specific transport`, `target-defined astrocyte-related proxy` へ更新
  - practical interpretation と calibrator-role paragraph に `Morgan et al. (2024)` を加え、BBB family の quantity type を明記

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` による再生成対象として同期

## 今回の修正で止めた誤読

- `human evidence is layered` だからと言って、その layer が one generic macro proxy stack だと読むこと
- `human BBB MRI / PET` を一つの permeability meter と読むこと
- `human myelin MRI` を一つの interchangeable myelin meter と読むこと
- `human astrocyte PET` を一つの generic astrocyte-state scalar と読むこと
- detailed page では split しているのに、front door だけ旧い総称で読むこと

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文、派生 summary、監査記録の更新で完結しています。

## 参考文献

1. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024;37(12):e5256.
   - https://doi.org/10.1002/nbm.5256
2. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025;147:176-186.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
3. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
4. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017;38(4):1780-1790.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
5. Koshino S, Hagiwara A, Okuda S, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018;8:10554.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC6043493/
6. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
7. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025;35(5):e70010.
   - https://doi.org/10.1111/bpa.70010
8. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263255
9. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018;59(10):1597-1602.
   - https://doi.org/10.2967/jnumed.118.208009
10. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022;27(4):2019-2029.
   - https://doi.org/10.1038/s41380-021-01429-y
11. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024;147(1):66.
   - https://doi.org/10.1007/s00401-024-02712-2
