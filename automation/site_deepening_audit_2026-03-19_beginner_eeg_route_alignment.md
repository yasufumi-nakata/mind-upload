# Site Deepening Audit (2026-03-19, Beginner EEG Route Alignment)

## 対象

- 主対象: `wiki/eeg-basics.md`
- 副対象: `wiki/measurement-and-modeling-terms.md`
- 副対象: `wiki/eeg-preprocessing-and-qc.md`

## 今回の選定理由

- 2026-03-19 時点で、公開 front door 側の `eeg_101.md`、`verification.md`、`wiki/observation-to-estimation.md` はかなり厳密になっておりました。
- その一方で、初学者が最初に辿りやすい `wiki/eeg-basics.md`、`wiki/measurement-and-modeling-terms.md`、`wiki/eeg-preprocessing-and-qc.md` は、公開サイト上でも更新日が 2026-03-14 / 2026-03-15 のままで、2026-03 の厳密化を十分に反映しておりませんでした。
- これは技術・自然科学の観点で重要です。なぜなら、この 3 ページは「最初に読む補助ページ」であり、ここで
  - `measurement condition` を単なる実装差と読む
  - `cleanup` を `network / causal claim` まで押し上げる
  - `ESI / DCM / SCM` を同じ強さの「モデル化用語」と読む
  余地が残ると、後段の厳密な route card 規律が入口で薄まるからです。

## 根拠付き批判

### 1. beginner EEG route は `measurement condition` を observation model として十分に固定していませんでした

- 問題:
  - `wiki/eeg-basics.md` と `wiki/eeg-preprocessing-and-qc.md` は reference・filter・artifact の重要性は説明していました。
  - しかし、`site / device / reference system / electrode layout / protocol` が measurement condition そのものであり、cross-dataset score や same-task comparison を大きく動かしうることを beginner front door で十分に明示しておりませんでした。
- 根拠:
  - Pernet et al. (2019) と Pernet et al. (2020) は、再現可能 EEG 研究の最低条件として metadata / reporting floor をかなり具体的に固定しました。
  - Xu et al. (2020) は、amplifier、cap、sampling rate、filtering の環境差が cross-dataset deep-learning 結果を大きく動かすことを示しました。
  - Dong et al. (2024) は、channel location の違い自体が BCI 比較で harmonization を要することを示しました。
- 批判:
  - したがって、measurement condition を「前処理メモ」扱いするのは弱すぎます。
  - EEG では `what was measured` と `how it was acquired / referenced / laid out` を切り離せません。これは cleanup 以前の observation model です。

### 2. beginner route は `cleanup` と `connectivity / causality ceiling` をまだ分離し切れていませんでした

- 問題:
  - `wiki/eeg-preprocessing-and-qc.md` は artifact suppression の重要性を説明していましたが、cleanup が source leakage や directionality identifiability を自動的に解決しないことを front-door で十分に止めていませんでした。
  - `wiki/eeg-basics.md` も、source imaging の限界は説明していた一方で、network map や directed graph がさらに一段強い主張であることを強く書いておりませんでした。
- 根拠:
  - Vinck et al. (2011) は wPLI を zero-lag mixing に対してより保守的な phase metric として提示しましたが、leak-proof を主張しておりません。
  - Haufe et al. (2013) は、sensor-space connectivity が volume conduction で強く制限され、source reconstruction 後でも spurious connectivity が残りうることを示しました。
  - Palva et al. (2018) は、leakage-insensitive source-space measures でも ghost interactions が起こりうることを示しました。
  - Miljevic et al. (2025) は、sensor-space EEG connectivity が rereferencing、epoch length、epoch number、metric choice に強く依存することを示しました。
- 批判:
  - したがって、artifact-cleaned signal を得たことをもって、network claim の ceiling が上がったとは読めません。
  - `cleaner waveform` と `more identifiable interaction structure` は別問題です。初心者導線でこの分離が弱いのは危険です。

### 3. `ESI / DCM / SCM` を一段で並べると、validation class と candidate-model dependence が薄まりました

- 問題:
  - `wiki/measurement-and-modeling-terms.md` は flow 自体は分かりやすかった一方、ESI、DCM、SCM を「推定」の 1 かごに入れすぎていました。
  - その結果、読者が `ESI = solver issue`、`DCM = causal connection detector`、`SCM = 因果を言うための最終言語` と短絡できる余地が残っていました。
- 根拠:
  - Michel & Brunet (2019) は、ESI を実務上の multi-step pipeline として整理し、forward model、regularization、validation の依存を明示しました。
  - Mikulan et al. (2020), Unnwongse et al. (2023), Hao et al. (2025) は、intracranial stimulation / simultaneous SEEG といった direct-validation class が source error を異なる形で制約することを示しました。
  - Penny et al. (2004) と Rosa et al. (2012) は DCM inference が candidate model space に依存することを固定しました。
  - Frässle et al. (2021) と Wu et al. (2024) は DCM の whole-brain 化・高速化を進めましたが、それは tractability の改善であり identifiability の完成ではありません。
- 批判:
  - したがって beginner page でも、ESI は `validation ladder`、DCM は `candidate-model route card`、SCM は `intervention language / equivalence-class narrowing` として切り分ける必要がありました。

## 今回実行した変更

- `wiki/eeg-basics.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - measurement condition を observation model の一部として明示しました。
  - connectivity / directed-connectivity claim が source imaging よりさらに強い主張であることを beginner page で明文化しました。
  - 参考文献へ Pernet (2020), Xu (2020), Vinck (2011), Haufe (2013), Palva (2018), Miljevic (2025) を追加しました。
- `wiki/measurement-and-modeling-terms.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - ESI / DCM / SCM を 1 つの「推定」語としてではなく、別々の stop rule を持つ語として再整理しました。
  - `Route card` を verification vocabulary に追加しました。
  - ESI validation ladder と DCM candidate-model rule を beginner page に埋め込みました。
  - 参考文献セクションを新設しました。
- `wiki/eeg-preprocessing-and-qc.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - `setup-distribution / harmonization gate` と `connectivity ceiling gate` を追加し、gate を 5 から 7 に拡張しました。
  - cleanup tools を connectivity / causality validation と誤読しない rule を追加しました。
  - minimum deliverables に `setup / harmonization log` と `connectivity-ceiling note` を追加しました。
  - 参考文献へ Xu (2020), Dong (2024), Chang (2018), de Cheveigné (2020), Vinck (2011), Haufe (2013), Palva (2018), Miljevic (2025) を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文と参考文献導線の改稿で完結しております。

## 参考文献

1. Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Scientific Data*. 2019;6:103.
   - https://doi.org/10.1038/s41597-019-0104-8
2. Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. *Nature Neuroscience*. 2020;23:1473-1483.
   - https://doi.org/10.1038/s41593-020-00709-0
3. Michel CM, Brunet D. EEG source imaging: a practical review of the analysis steps. *Frontiers in Neurology*. 2019;10:325.
   - https://doi.org/10.3389/fneur.2019.00325
4. Mikulan E, Russo S, Bares M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020;7:127.
   - https://doi.org/10.1038/s41597-020-0467-x
5. Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Communications*. 2023;5(2):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
6. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
   - https://doi.org/10.1111/epi.18552
7. Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. *Frontiers in Human Neuroscience*. 2020;14:103.
   - https://doi.org/10.3389/fnhum.2020.00103
8. Dong C, Jia T, Wang S, et al. Benchmarking of different channel locations for motor imagery based BCI. *Brain Research Bulletin*. 2024;210:110906.
   - https://doi.org/10.1016/j.brainresbull.2024.110906
9. Chang C-Y, Hsu S-H, Pion-Tonachini L, Jung T-P. Evaluation of Artifact Subspace Reconstruction for automatic EEG artifact removal. *Proc IEEE EMBC*. 2018.
   - https://doi.org/10.1109/EMBC.2018.8512547
10. de Cheveigné A. ZapLine: A simple and effective method to remove power line artifacts. *NeuroImage*. 2020;207:116356.
   - https://doi.org/10.1016/j.neuroimage.2019.116356
11. Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CMA. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. *NeuroImage*. 2011;55(4):1548-1565.
   - https://doi.org/10.1016/j.neuroimage.2011.01.055
12. Haufe S, Nikulin VV, Müller K-R, Nolte G. A critical assessment of connectivity measures for EEG data: A simulation study. *NeuroImage*. 2013;64:120-133.
   - https://doi.org/10.1016/j.neuroimage.2012.09.036
13. Palva JM, Wang SH, Palva S, et al. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. *NeuroImage*. 2018;173:632-643.
   - https://doi.org/10.1016/j.neuroimage.2018.02.032
14. Miljevic A, Murphy OW, Fitzgerald PB, Bailey NW. Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. *Clinical Neurophysiology*. 2025;174:73-83.
   - https://doi.org/10.1016/j.clinph.2025.03.043
15. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004;22(3):1157-1172.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
16. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012;208(1):66-78.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
17. Frässle S, Paulus FM, Krach S, Jansen A. Test-retest reliability of effective connectivity in the face perception network. *Human Brain Mapping*. 2016;37(2):730-744.
   - https://doi.org/10.1002/hbm.23061
18. Frässle S, Manjaly ZM, Do CT, Kasper L, Pruessmann KP, Stephan KE. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021;225:117491.
   - https://doi.org/10.1016/j.neuroimage.2020.117491
19. Wu H, Hu X, Zeng Y. A fast dynamic causal modeling regression method for fMRI. *NeuroImage*. 2024;304:120954.
   - https://doi.org/10.1016/j.neuroimage.2024.120954
