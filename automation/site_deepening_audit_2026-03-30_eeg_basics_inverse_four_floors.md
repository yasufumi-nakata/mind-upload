# Site Deepening Audit (2026-03-30, EEG basics inverse / ESI four-floor split)

## 対象

- 主対象:
  - `wiki/eeg-basics.md`
- 同期先として確認したページ:
  - `eeg_101.md`
  - `wiki/measurement-and-modeling-terms.md`
  - `wiki/observation-to-estimation.md`
  - `wiki/verification-basics.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学
  - 法学
  - 制度論

## web確認対象

- `https://www.nature.com/articles/s41467-019-08725-w`
- `https://pubmed.ncbi.nlm.nih.gov/37307867/`
- `https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1335212/full`
- `https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1359753/full`
- `https://doi.org/10.1109/TMI.2024.3506596`
- `https://doi.org/10.1109/TMI.2025.3642620`
- `https://doi.org/10.1088/1741-2552/ae2f01`
- `https://doi.org/10.1093/braincomms/fcad023`
- `https://doi.org/10.1111/epi.18552`

## 今回この箇所を選んだ理由

- `wiki/eeg-basics.md` は、EEG を最初に学ぶ読者が通る技術系の beginner front door でございます。
- しかし 2026-03-30 時点では、この page は
  - `EEG is mixed`
  - `source imaging is hard`
  - `direct validation exists`
  までは書けていても、site-wide で既に厳密化されている
  - `field-formation visibility`
  - `forward-model / conductivity burden`
  - `solver-family uncertainty`
  - `validation class`
  の 4 分割が beginner layer ではまだ十分に固定されておりませんでした。
- そのままでは、初学者が
  - `better ESI`
  - `validated ESI`
  - `high-density EEG`
  を一つの progress bar に再圧縮して読む余地が残ります。

## 主要結論

- EEG source imaging は beginner page でも `one ladder` としてではなく、少なくとも次の 4 floor に分けて読む必要がございました。
  - `field-formation visibility`
  - `forward-model / conductivity burden`
  - `solver-family uncertainty`
  - `validation class`
- よって `wiki/eeg-basics.md` の safe ceiling は、
  - `EEG gives macro electrical observations`
  - `specific source-imaging improvements reduce named error terms`
  に留め、`better ESI` を generic progress word として置かないのが妥当でございます。
- 禁止すべき overread は次のとおりでございます。
  - `subcortical detectability = source imaging generally solved`
  - `conductivity estimation = inverse uncertainty mostly solved`
  - `posterior-aware solver = external correctness established`
  - `direct validation = all source regimes and target objects covered`

## 根拠付き批判

### 1. detectability と general recovery は同義ではございません

- [Seeber et al. (2019)](https://doi.org/10.1038/s41467-019-08725-w) は、`256-channel` scalp EEG と simultaneous DBS を用いて subcortical electrophysiological activity の detectability を示しました。

批判:

- これは `field-formation visibility` の前進であり、
  - `all source classes are visible`
  - `the inverse family is now unique`
  を意味しません。
- beginner page がここを `deep sources can now be read` とまとめてしまうのは粗すぎます。

### 2. conductivity burden は still a separate floor でございます

- [Vorwerk et al. (2024)](https://doi.org/10.3389/fnhum.2024.1335212) は、tissue conductivity uncertainty が EEG source analysis に global sensitivity を持つことを整理しました。
- [Vorwerk et al. (2026)](https://doi.org/10.1088/1741-2552/ae2f01) は、presurgical evaluation 文脈で skull conductivity estimation が source analysis をどう改善しうるかを検討しました。

批判:

- したがって `individual MRI` や `better head model` を書くだけでは足りず、
  - `which conductivity burden was reduced`
  - `how much spread remained`
  を別 floor として保持する必要がございます。
- beginner page でこれを source-imaging 一般論へ吸収すると、forward-model 側の失敗様式が見えなくなります。

### 3. uncertainty-aware solver は validation の代わりではございません

- [Luria et al. (2024)](https://doi.org/10.3389/fnhum.2024.1359753) は、SESAMEEG が ambiguous data に対して alternative scenarios と confidence information を返しうることを示しました。
- [Tong et al. (2025)](https://doi.org/10.1109/TMI.2024.3506596) は、spatial-temporal EEG/MEG source imaging に対する debiased inference を提示しました。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は、extended E/MEG source activation に対する empirical-Bayesian uncertainty quantification を主題化しました。

批判:

- これらは重要な進歩ですが、いずれも主に
  - `how the candidate set is exposed`
  - `how uncertainty is reported`
  を改善する文献でございます。
- よって `uncertainty-aware solver exists` を
  - `the reported source is externally correct`
  と読み替えることはできません。

### 4. direct validation も one solved rung ではございません

- [Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219) は、focal sources に対する ESI methods の systematic comparison を行いました。
- [Unnwongse et al. (2023)](https://doi.org/10.1093/braincomms/fcad023) は、intracranial electric stimulation を用いた direct validation で、depth と conductivity dependence が localization error を動かすことを示しました。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は、simultaneous HD-EEG / SEEG で ictal と interictal の差、source depth、spike power 依存を示しました。

批判:

- したがって `direct validation exists` と書くだけでは、
  - focal centre
  - depth-dependent localization error
  - simultaneous invasive recording regime
  - source extent / overlap
  の違いが消えてしまいます。
- beginner page でも `validation class` は独立 floor として提示すべきでございました。

## 今回実行した変更

- `wiki/eeg-basics.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter の `page_highlights` と `known_points` に、EEG source imaging を 4 floor で読む rule を追加しました。
  - 新規 note-box
    - `2026-03-30 re-audit: better EEG source imaging is still four different advances`
    を追加しました。
  - 新規 table
    - `Four-floor split for EEG source imaging`
    を追加し、visibility / conductivity / solver uncertainty / validation class を beginner layer で固定しました。
  - `How to connect with WBE` の paragraph を更新し、WBE 側へ上げる前に disclose すべき source-imaging floor を明文化しました。
  - 参考文献と sidebar reference に
    - Pascarella 2023
    - Vorwerk 2024
    - Luria 2024
    - Tong 2025
    - Feng 2025
    - Vorwerk 2026
    を追加しました。

## 今回止めた誤読

- `subcortical detectability = deep source recovery generally solved`
- `better conductivity model = inverse ambiguity mostly gone`
- `posterior-aware inverse solver = external truth established`
- `one direct-validation paper = all source regimes validated`
- `better ESI = one monotonic progress bar`

## 外部依存タスク

- なし
  - 今回の作業は、web 上の一次資料確認、repo 内ページ改稿、wiki export 更新、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. *Nature Communications*. 2019;10:753.
   - https://doi.org/10.1038/s41467-019-08725-w
2. Pascarella A, Mikulan E, Sciacchitano F, et al. An in-vivo validation of ESI methods with focal sources. *NeuroImage*. 2023;277:120219.
   - https://doi.org/10.1016/j.neuroimage.2023.120219
3. Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Communications*. 2023;5(2):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
4. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024;18:1335212.
   - https://doi.org/10.3389/fnhum.2024.1335212
5. Luria G, Viani S, Pascarella A, et al. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Frontiers in Human Neuroscience*. 2024;18:1359753.
   - https://doi.org/10.3389/fnhum.2024.1359753
6. Tong PF, Yang H, Ding X, et al. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2024.3506596
7. Feng Z, Mishne G, Hashemi A, et al. Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2025.3642620
8. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
   - https://doi.org/10.1111/epi.18552
9. Vorwerk J, Köhler T, Güllmar D, et al. Potential of EEG and EEG/MEG skull conductivity estimation to improve source analysis in presurgical evaluation of epilepsy. *Journal of Neural Engineering*. 2026;23(1):016007.
   - https://doi.org/10.1088/1741-2552/ae2f01
