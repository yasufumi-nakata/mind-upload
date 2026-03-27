# Site Deepening Audit (2026-03-27, research harvest U1 inverse-route split)

## 対象

- 主対象: `research_harvest_50.md`
- 対象節: `U1: Inverse problem identifiability`
- 範囲: 技術・自然科学のみ

## 今回この箇所を選んだ理由

- 公開サイトの中核ページである `verification.md`、`datasets.md`、`tech_roadmap.md`、`wiki/observation-to-estimation.md` では、すでに
  - `field-formation visibility`
  - `conductivity / forward-model sensitivity`
  - `solver disagreement / posterior width`
  - `validation class`
  を別々に読む規律が導入されていました。
- しかし文献ハブである `research_harvest_50.md` の U1 は、なお
  - Bayesian / Champagne 系の推定法
  - conductivity uncertainty / conductivity estimation
  - focal-source / simultaneous-SEEG の direct validation
  をほぼ一つの「inverse problem の前進」としてまとめていました。
- この圧縮は技術・自然科学の観点で弱点です。なぜなら、読者が
  - `posterior-aware method がある`
  - `conductivity estimation が改善した`
  - `focal-source benchmark で良かった`
  を足し合わせて、`inverse identifiability がかなり解決した`
  と過読しやすいからです。

## 根拠付き批判

### 1. solver-family progress と forward-model uncertainty は同じ問いではありません

- [Luria et al. (2024)](https://doi.org/10.3389/fnhum.2024.1359753) の SESAMEEG は、単一の best map ではなく posterior distribution と alternative source configurations を出せることを前面化しています。
- [Tong et al. (2025)](https://doi.org/10.1109/TMI.2024.3506596) は、regularization による amplitude / orientation / depth bias を補正し、variance と hypothesis testing を扱う debiased inference を導入しました。
- 一方で [Rimpiläinen et al. (2019)](https://doi.org/10.1016/j.neuroimage.2018.11.058)、[Vorwerk et al. (2024)](https://doi.org/10.3389/fnhum.2024.1335212)、[Vorwerk et al. (2026)](https://doi.org/10.1088/1741-2552/ae2f01) が扱っているのは、head conductivity uncertainty や conductivity estimation が localization error をどれだけ動かすかという forward-model 側の問題です。
- したがって、`uncertainty-aware solver がある` と `conductivity uncertainty を扱える` は同じ進歩量ではありません。前者は candidate-set representation の前進であり、後者は forward-model burden の縮小です。

### 2. focal-source benchmark と extended-source reconstruction は同じ leaderboard に置けません

- [Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219) は in-vivo focal-source benchmark で method 間差と regularization / montage dependence を比較しました。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) の Block-Champagne は、extended E/MEG source activation に対する empirical-Bayesian uncertainty quantification を主題にしています。
- ここで benchmark object 自体が違います。focal-source validation で良い method が、そのまま extended-source reconstruction の universal winner になるわけではありません。
- したがって、旧 U1 のように `MNE / beamformer / Champagne` を一続きに並べるだけでは不十分で、少なくとも `source regime` を分離しなければなりません。

### 3. named validation class が無いと direct validation の意味がずれます

- [Mikulan et al. (2020)](https://doi.org/10.1038/s41597-020-0467-x) は、living human で precisely known stimulation locations を持つ open dataset を提示しました。
- [Unnwongse et al. (2023)](https://doi.org/10.1093/braincomms/fcad023) は、3619 stimulation locations を用い、mean localization error が source depth と skull conductivity に依存して 10.3-26 mm に広がることを示しました。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は、29 simultaneous HD-EEG/SEEG cases で ictal ESI が interictal ESI より良い一方、accuracy が source depth と spike power に依存することを示しました。
- これらはどれも重要ですが、`known stimulation site`, `simultaneous invasive concordance`, `clinical seizure-onset localization` は同じ error question を答えていません。
- よって U1 の literature hub で validation class を明示しないのは、自然科学的には粗すぎます。

### 4. 文献ハブの front door に弱い参照を残すと、core page の厳しさが再び緩みます

- 旧 U1 では、review、book chapter、arXiv、OpenAlex item が前面に残っており、direct validation や recent primary sources より目立つ構造でした。
- 文献ハブは「量が多いから何でも置く場所」ではなく、読者が次に何を一次ソースとして読むべきかを固定するページです。
- したがって、public evidence bank の U1 は、少なくとも
  - `Mahjoory 2017`
  - `Mikulan 2020`
  - `Pascarella 2023`
  - `Unnwongse 2023`
  - `Vorwerk 2024/2025/2026`
  - `Tong 2025`
  - `Feng 2025`
  - `Hao 2025`
  のような primary route を中心に再構成するべきでした。

## 今回実行した変更

- `research_harvest_50.md`
  - `last_updated` を `2026-03-27` に更新しました。
  - front matter の `page_highlights` / `known_points` を、U1 が `field-formation visibility` だけでなく `posterior / solver-family uncertainty`, `conductivity / forward-model sensitivity`, `named validation class`, `source regime` を分けて読むことが分かる文言へ更新しました。
  - U1 冒頭に `2026-03-27 addendum: U1 is three coupled subroutes, not one progress bar` を追加しました。
  - U1 に `Posterior / solver-family route`, `Forward-model / conductivity route`, `Validation-class / source-regime route` の 3 分割 table を追加しました。
  - U1 の `Research question breakdown` を、単なる solver 名比較ではなく `abstention / claim downgrading rule` まで問う形へ改稿しました。
  - U1 の `What has some traction now` と `What still needs research` を、recent primary literature に同期して全面改稿しました。
  - U1 の `Major previous studies` を 13 本の primary-source 中心リストへ入れ替え、review / arXiv / OpenAlex front-door 依存を外しました。

## 今回止めた誤読

- `uncertainty-aware inverse solver が出た = forward-model uncertainty もほぼ処理できた`
- `focal-source benchmark で良かった method = extended-source でも普遍的に良い`
- `simultaneous SEEG concordance = known-site stimulation ground truth`
- `inverse problem literature が厚い = inverse identifiability がほぼ閉じた`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の文書更新・検証・commit・push で完結できます。

## 参考文献

1. Mahjoory K, Nikulin VV, Botrel L, Linkenkaer-Hansen K, Fato MM, Haufe S. Consistency of EEG source localization and connectivity estimates. *NeuroImage*. 2017.
   - https://doi.org/10.1016/j.neuroimage.2017.02.076
2. Rimpiläinen V, Koulouri A, Lucka F, Kaipio JP, Wolters CH. Improved EEG source localization with Bayesian uncertainty modelling of unknown skull conductivity. *NeuroImage*. 2019.
   - https://doi.org/10.1016/j.neuroimage.2018.11.058
3. Mikulan E, Russo S, Parmigiani S, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020.
   - https://doi.org/10.1038/s41597-020-0467-x
4. Pascarella A, Mikulan E, Sciacchitano F, et al. An in-vivo validation of ESI methods with focal sources. *NeuroImage*. 2023.
   - https://doi.org/10.1016/j.neuroimage.2023.120219
5. Unnwongse K, Rampp S, Wehner T, et al. Validating EEG source imaging using intracranial electrical stimulation. *Brain Communications*. 2023.
   - https://doi.org/10.1093/braincomms/fcad023
6. Luria G, Viani S, Pascarella A, et al. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Frontiers in Human Neuroscience*. 2024.
   - https://doi.org/10.3389/fnhum.2024.1359753
7. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024.
   - https://doi.org/10.3389/fnhum.2024.1335212
8. Leone F, Caporali A, Pascarella A, et al. Investigating the impact of the regularization parameter on EEG resting-state source reconstruction and functional connectivity using real and simulated data. *NeuroImage*. 2024.
   - https://doi.org/10.1016/j.neuroimage.2024.120896
9. Tong PF, Yang H, Ding X, et al. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2024.3506596
10. Feng Z, Mishne G, Hashemi A, et al. Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2025.3642620
11. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
   - https://doi.org/10.1111/epi.18552
12. Vorwerk J, Höltershinken MB, Wolters CH, Baumgarten D. Global sensitivity of MEG source analysis to tissue conductivity uncertainties. *NeuroImage*. 2025.
   - https://doi.org/10.1016/j.neuroimage.2025.121618
13. Vorwerk J, Köhler T, Güllmar D, et al. Potential of EEG and EEG/MEG skull conductivity estimation to improve source analysis in presurgical evaluation of epilepsy. *Journal of Neural Engineering*. 2026.
   - https://doi.org/10.1088/1741-2552/ae2f01
