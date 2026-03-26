# Site Deepening Audit (2026-03-26, Connectome Maintenance-State Family Completion)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 同期対象: `github-wiki-export/connectome-is-not-enough.md`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- 2026-03-26 時点で、サイト全体の front door と maintenance-side pages はすでに
  - `thermal-state`
  - `bioenergetic / mitochondrial state`
  - `neurovascular-unit / BBB / pericyte state`
  - `astrocyte-state`
  - `clearance / immune support`
  を独立 family として扱っていました。
- その一方で `wiki/connectome-is-not-enough.md` は、依然として
  - `generic glia`
  - `vascular nuisance`
  - `slow support`
  のような粗い束ね方が残っており、site-wide taxonomy に追いついていませんでした。
- これは技術・自然科学の観点で重要です。connectome insufficiency を説明するページが maintenance-side family を粗く束ねたままだと、読者が `graph + weights + a few support words` を state-complete に近いものとして過読しやすくなるからです。

## 根拠付き批判

### 1. `connectome-is-not-enough` が current site rule より maintenance-side family を粗く圧縮していました

- 問題:
  - 当該ページは `14 state classes and 1 wall` のままでした。
  - しかし site-wide では、connectome 外に残る maintenance-side family はもっと細かく分けられていました。
- 批判:
  - 中核ページだけ taxonomy が古いままだと、front door では止めている過読をこのページで再導入してしまいます。
  - 特に `glia`, `vascular`, `slow support` のような一語は、現在の一次文献に照らすと粗すぎます。

### 2. Thermal-state は timing-state や recording nuisance に吸収してはいけません

- 根拠:
  - [Hardingham & Larkman (1998)](https://doi.org/10.1111/j.1469-7793.1998.249bu.x) は synaptic reliability の温度依存性を示しました。
  - [Long & Fee (2008)](https://doi.org/10.1038/nature07448) は局所 cooling による sequence timing の伸張を示しました。
  - [Owen et al. (2019)](https://doi.org/10.1038/s41593-019-0422-3) は optogenetic manipulation 自体が tissue heating artifact を持ちうることを示しました。
- 批判:
  - `timing changed` と `the device heated tissue` は同じ inferential object ではありません。
  - よって thermal-state は connectome insufficiency の独立 family として明示する必要がありました。

### 3. Bioenergetic / mitochondrial state は activity fit や macro energetic imaging に吸収してはいけません

- 根拠:
  - [Rangaraju et al. (2014)](https://doi.org/10.1016/j.cell.2013.12.042) は local ATP synthesis と synaptic function を結びました。
  - [Divakaruni et al. (2018)](https://doi.org/10.1016/j.neuron.2018.09.025) は dendritic mitochondrial fission を LTP induction に結びました。
  - [Vishwanath et al. (2026)](https://doi.org/10.1038/s42255-026-01451-w) は mitochondrial Ca2+ efflux tuning と long-term memory across species を結びました。
  - [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は human dynamic DMRSI を示しましたが、なお macro energetic proxy です。
- 批判:
  - presynaptic ATP support, dendritic mitochondrial controller, nano-organization, human macro rate map は同じ quantity type ではありません。
  - したがって connectome page でも独立 family と proxy ceiling の両方を明示すべきでした。

### 4. Neurovascular / BBB / pericyte state は hemodynamic confound audit に吸収してはいけません

- 根拠:
  - [Bell et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.043) は pericyte deficiency と neurovascular / BBB dysfunction を示しました。
  - [Kisler et al. (2020)](https://doi.org/10.3389/fncel.2020.00027) は rapid neurovascular uncoupling を示しました。
  - [Pandey et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.030) は pericyte-derived IGF2 と memory formation を示しました。
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) と [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は human BBB proxy routes を押し上げました。
- 批判:
  - `vascular nuisance was audited` と `neurovascular controller state was identified` は別です。
  - human BBB route があることも、そのまま local controller readout を意味しません。

### 5. Astrocyte-state と clearance / immune support は generic glia に戻してはいけません

- 根拠:
  - [Suzuki et al. (2011)](https://doi.org/10.1016/j.cell.2011.02.018), [Cahill et al. (2024)](https://doi.org/10.1038/s41586-024-07311-5), [Williamson et al. (2025)](https://doi.org/10.1038/s41586-024-08170-w), [Dewa et al. (2025)](https://doi.org/10.1038/s41586-025-09619-2) は astrocyte-side family が support, encoding, recall, stabilization を別々に規定することを示しました。
  - [Louveau et al. (2015)](https://doi.org/10.1038/nature14432), [Ahn et al. (2019)](https://doi.org/10.1038/s41586-019-1419-5), [Kim et al. (2025)](https://doi.org/10.1016/j.cell.2025.02.022), [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は clearance / immune support が独立した support-state family であることを示しました。
- 批判:
  - astrocyte-state と clearance / immune support を generic glia に戻すと、support, ensemble, drainage, microglia-linked synaptic physiology, human proxy ceiling の差が消えます。
  - connectome insufficiency のページこそ、この差を最初から見せる必要がありました。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - front matter の description / highlights / known points を site-wide taxonomy に同期しました。
  - conclusion と bottom-line table を `18 state classes and 1 putative wall` に更新しました。
  - thermal / bioenergetic / neurovascular-BBB / astrocyte / clearance rows を追加しました。
  - `Why these classes are easy to skip` 節に上記 family の独立解説と human proxy ceiling note を追加しました。
  - augmentation-ablation table に thermal, bioenergetic, neurovascular, astrocyte, clearance rows を追加しました。
  - minimum submission rules に新 family の latent-state disclosure を追加しました。
  - references に一次文献束を追加しました。

- `github-wiki-export/connectome-is-not-enough.md`
  - export 再生成で同期対象に含めました。

## 今回止めた過読

- `connectome + generic glia = maintenance-side mostly covered`
- `timing-state already covers thermal-state`
- `macro energetic imaging = local mitochondrial controller`
- `vascular confound audit = neurovascular-unit / BBB state`
- `human BBB proxy = pericyte / endothelial controller readout`
- `reactive astrogliosis PET = astrocyte ensemble state`
- `human glymphatic / CSF route = local immune-controller readout`

## 外部依存タスク

- same-subject human calibration for maintenance-side family proxies
  - 担当者: external human neuroimaging / cellular-calibration researchers
  - 前提条件: same-subject design linking macro thermal / energetic / BBB / astrocyte / clearance proxies to externally validated local targets
  - 完了条件: 各 proxy がどの hidden-state uncertainty term をどこまで減らすか比較可能な benchmark が公開されること

## 参考文献

1. Hardingham NR, Larkman AU. The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. *J Physiol*. 1998. https://doi.org/10.1111/j.1469-7793.1998.249bu.x
2. Long MA, Fee MS. Using temperature to analyse temporal dynamics in the songbird motor pathway. *Nature*. 2008. https://doi.org/10.1038/nature07448
3. Owen SF, Liu MH, Kreitzer AC. Thermal constraints on in vivo optogenetic manipulations. *Nat Neurosci*. 2019. https://doi.org/10.1038/s41593-019-0422-3
4. Rangaraju V, Calloway N, Ryan TA. Activity-driven local ATP synthesis is required for synaptic function. *Cell*. 2014. https://doi.org/10.1016/j.cell.2013.12.042
5. Divakaruni SS, Van Dyke AM, Chandra R, et al. Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. *Neuron*. 2018. https://doi.org/10.1016/j.neuron.2018.09.025
6. Vishwanath AA, Comyn T, Mira RG, et al. Mitochondrial Ca2+ efflux controls neuronal metabolism and long-term memory across species. *Nat Metab*. 2026. https://doi.org/10.1038/s42255-026-01451-w
7. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
8. Bell RD, Winkler EA, Sagare AP, et al. Pericytes control key neurovascular functions and neuronal phenotype in the adult brain and during brain aging. *Neuron*. 2010. https://doi.org/10.1016/j.neuron.2010.09.043
9. Kisler K, Nikolakopoulou AM, Sweeney MD, et al. Acute ablation of cortical pericytes leads to rapid neurovascular uncoupling. *Front Cell Neurosci*. 2020. https://doi.org/10.3389/fncel.2020.00027
10. Pandey K, Bessières B, Sheng SL, et al. Neuronal activity drives IGF2 expression from pericytes to form long-term memory. *Neuron*. 2023. https://doi.org/10.1016/j.neuron.2023.08.030
11. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiol Aging*. 2025. https://doi.org/10.1016/j.neurobiolaging.2024.12.012
12. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-58356-7
13. Suzuki A, Stern SA, Bozdagi O, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011. https://doi.org/10.1016/j.cell.2011.02.018
14. Cahill MK, Berrios J, Schaid MD, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024. https://doi.org/10.1038/s41586-024-07311-5
15. Williamson NR, Ferreira AN, Watanabe AT, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025. https://doi.org/10.1038/s41586-024-08170-w
16. Dewa K, Kwon O-B, Zheng X, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025. https://doi.org/10.1038/s41586-025-09619-2
17. Louveau A, Smirnov I, Keyes TJ, et al. Structural and functional features of central nervous system lymphatic vessels. *Nature*. 2015. https://doi.org/10.1038/nature14432
18. Ahn JH, Cho H, Kim J-H, et al. Meningeal lymphatic vessels at the skull base drain cerebrospinal fluid. *Nature*. 2019. https://doi.org/10.1038/s41586-019-1419-5
19. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025. https://doi.org/10.1016/j.cell.2025.02.022
20. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nat Commun*. 2026. https://doi.org/10.1038/s41467-026-68374-8
