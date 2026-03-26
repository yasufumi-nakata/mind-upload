# Site Deepening Audit (2026-03-27, Beginner Human Proxy Quantity-Type Split)

## 対象

- 主対象: `wiki/mind-upload-basics.md`
- 参照同期: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 参照同期: `verification.md`
- 参照同期: `wbe_101.md`

## 今回の選定理由

- 現行サイトの主幹ページでは、human proxy を `proxy class`, `operational maturity`, `calibrator role` で読む規律がかなり整備されていました。
- しかし初心者向け入口である `wiki/mind-upload-basics.md` には、なお `myelin mapping`, `BBB permeability / exchange imaging` のような粗い一括語が残っていました。
- 入口で quantity type を曖昧にすると、その後の読解でも `human proxy exists` を `human hidden-state is almost visible` に読み替える誤読が固定されやすくなります。
- 技術・自然科学の観点では、この入口の補正を優先する価値があります。理由は、同じ modality 名でも `何をどの measurement model で推定したか` が違えば、可視化 ceiling も calibrator role も変わるからです。

## 根拠付き批判

### 1. Beginner page がなお `human myelin MRI` を一つの meter として読ませる余地を残していました

- 問題:
  - 旧本文では `myelin-bilayer MRI` を human observability ladder の一部として紹介していましたが、myelin MRI の内部で quantity type が分かれていませんでした。
  - そのため、`myelin-water`, `MT-family contrast`, `bilayer-sensitive mapping`, `qT1 remyelination-sensitive contrast` がほぼ同じ inferential object であるかのように読める状態でした。
- 根拠:
  - [Arshad et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/) は、calibrated `T1w/T2w` が高い再検査信頼性を持っても、`MWF` に対する criterion validity は低いと報告しました。
  - [Koshino et al. (2018)](https://doi.org/10.1038/s41598-018-28852-6) は、white matter で `SyMRI` と `MTsat` は強く相関する一方、`T1w/T2w` は両者より弱い相関しか示さないと報告しました。
  - [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は、`myelin lipid-protein bilayer` を狙う別系統の route を in vivo human で提示しましたが、`2 healthy volunteers` と `high-performance RF and gradient hardware` という限定条件でした。
  - [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) は、postmortem MS cortex で `qT1` が remyelination-sensitive だった一方、`MWF` と `MTR` は demyelinated と remyelinated cortex を区別しなかったと報告しました。
- 批判:
  - したがって、beginner page で `human myelin MRI` を一括で置くのは粗いです。
  - `healthy white-matter myelin amount`, `bilayer-sensitive contrast`, `remyelination-sensitive cortical contrast` は同じ claim family ではありません。

### 2. Beginner page がなお `human BBB imaging` を一つの permeability meter として読ませる余地を残していました

- 問題:
  - 旧本文では `BBB permeability / exchange imaging` というまとめ方をしていました。
  - しかしこの書き方では `water-exchange ASL` と `tracer-specific PET permeability-surface-area` が同じ quantity type であるかのように見えます。
- 根拠:
  - [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は、同一 cohort で `DP-ASL` と `ME-ASL` を比較し、`Kw` の量的推定値と年齢依存の見え方が method-dependent であることを示しました。
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は、multi-echo ASL で `Tex` を評価し、`194 healthy adults` の reference range を提示しました。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は、high-temporal-resolution total-body PET と kinetic modeling により、`three radiotracers` にわたる tracer-specific `PS` を推定しましたが、同時に `lack of ground truth values in humans` を major limitation と明記しました。
- 批判:
  - したがって、`human BBB imaging` を beginner page で一括語にすると、quantity type と model burden が消えます。
  - `water-exchange time/rate` と `molecule-specific transport-model PS` は同じ inferential object ではありません。

### 3. Beginner page が `human astrocyte evidence` を十分に切り分けていませんでした

- 問題:
  - 旧 human observability ladder では、astrocyte-related human route が表に独立しておらず、初心者が rodent astrocyte causality と human PET proxy を同一 ladder で読んでしまう余地がありました。
- 根拠:
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) は、`18F-SMBT-1` が `MAO-B` route であり、`selegiline` により全脳で `>85% blockade` を示すと報告しました。
  - [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は、`11C-BU99008` が `I2BS` route であり、`idazoxan` では dose-dependent に block される一方、`isocarboxazid` では block されないと報告しました。
  - [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) は、`11C-BU99008` uptake が disease stage と region で単調ではなく、Aβ-positive MCI と AD で異なる regional pattern を示すと報告しました。
  - [Jaisa-Aad et al. (2024)](https://doi.org/10.1007/s00401-024-02712-2) は、MAO-B が主に astrocytic であることを支持しつつ、AD/ADRD class ごとに expression pattern が異なると報告しました。
- 批判:
  - したがって、beginner page でも human astrocyte PET は `target-defined MAO-B or I2BS proxy` として明示すべきです。
  - そうしないと、`rodent astrocyte ensemble causality -> human astrocyte PET -> near-direct human astrocyte-state visibility` という不当な昇格が起こります。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `last_updated` を `2026-03-27` に更新
  - `page_highlights` と `known_points` に `quantity type` の明示ルールを追加
  - beginner update note-box を `quantity type now belongs at the beginner front door` へ改稿
  - human observability ladder の表で `energetic` と `myelin` を分離
  - myelin row を `Arshad / Koshino / Baadsvik / Galbusera` で quantity-defined family として再構成
  - BBB row を `Morgan / Padrela / Chung` で `Tex/Kw` と tracer-specific `PS` の split へ改稿
  - astrocyte row を新設し、`MAO-B` と `I2BS` の target-defined PET route を beginner page に追加
  - `Quantity type is part of the claim` note-box を新設し、上記三系統の圧縮不能性を一次文献で明示
  - references に `Arshad 2017`, `Koshino 2018`, `Galbusera 2025`, `Morgan 2024`, `Villemagne 2022`, `Tyacke 2018`, `Livingston 2022`, `Jaisa-Aad 2024` を追加

## 今回の修正で止めた誤読

- `human myelin MRI = one generic myelin meter`
- `BBB permeability / exchange imaging = one stable permeability quantity`
- `human astrocyte evidence = one generic astrocyte-state PET scalar`
- `beginner page だから modality 名だけで十分`
- `human proxy exists = same hidden-state family is already visible`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文と監査記録の更新のみで完結しています。

## 参考文献

1. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017;38(4):1780-1790.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
2. Koshino S, Hagiwara A, Okuda S, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018;8:10554.
   - https://doi.org/10.1038/s41598-018-28852-6
3. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
4. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025;35(5):e70010.
   - https://doi.org/10.1111/bpa.70010
5. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024;37(12):e5256.
   - https://doi.org/10.1002/nbm.5256
6. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025;147:176-186.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
7. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
8. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263255
9. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018;59(10):1597-1602.
   - https://doi.org/10.2967/jnumed.118.208009
10. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022;27(4):2019-2029.
   - https://doi.org/10.1038/s41380-021-01429-y
11. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024;147(1):66.
   - https://doi.org/10.1007/s00401-024-02712-2
