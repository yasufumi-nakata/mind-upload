# Site Deepening Audit (2026-03-15, Glossary / Modeling Claim Boundaries)

## 対象

- 主対象: `glossary.md`
- 副対象: `wiki/measurement-and-modeling-terms.md`

## 今回の選定理由

- 2026-03-15 時点で、公開ページ本体では `observability`、`identifiability`、`maintenance-state`、`decode / emulate`、`calibration / abstention` の境界がかなり整理されていました。
- その一方で、用語層である `glossary.md` と `wiki/measurement-and-modeling-terms.md` はまだ一段粗く、`detectable` と `localized`、`localized` と `identified`、`fit` と `validated`、`accurate` と `deployable` が同じ箱に入って読まれうる構造を残していました。
- これは技術・自然科学の観点で弱点でございます。なぜなら、本サイトの中心原理は「レベル間のすり替えを防ぐこと」であり、入口の用語定義が粗いと、本文で厳密化した境界が再び崩れるからです。

## 主要な批判点

### 1. 旧 glossary は `observability / identifiability` を正しく書いていた一方、主張階段が粗すぎました

- 問題:
  - 旧 `glossary.md` は `観測可能性 / 同定可能性` の短い区別を持っていました。
  - しかし、実務上もっと事故が起きやすい `detectability`、`localization`、`direct validation` が抜けていたため、読者が `見えた` を `局在した` に、`局在した` を `一意に分かった` に読み替えやすい構造でした。
- 根拠:
  - Seeber et al. (2019) は deep activity の **detectability** を前進させましたが、一般的一意復元を主張していません。
  - Aydin et al. (2019) は頭部導電率不確かさが dipole reconstruction を大きく動かすことを示しました。
  - Unnwongse et al. (2023) と Hao et al. (2025) が押し上げたのは **direct validation route** であり、state-complete reconstruction ではありません。
- 修正:
  - `glossary.md` に `検出可能性 / 局在化 / 同定可能性 / 直接妥当化` を追加し、`observability budget` と `claim ceiling` も用語として固定しました。

### 2. 旧 `measurement-and-modeling-terms` は「検証」までで止まり、`deployability` の壁を見せられていませんでした

- 問題:
  - 旧 wiki は `観測 -> 整理 -> 推定 -> 検証` の 4 段階で整理していました。
  - しかし、closed-loop BCI や seizure prediction の文脈では、`高い accuracy` と `長期に使える` は別です。ここを用語段階で切り分けられていませんでした。
- 根拠:
  - Segal et al. (2023) は seizure prediction で calibration により false alarm rate を制御できることを示しました。
  - Wilson et al. (2025) は intracortical BCI で long-term unsupervised recalibration を主要課題として示しました。
- 修正:
  - `wiki/measurement-and-modeling-terms.md` を `観測 -> 整理 -> 推定 -> 妥当化 -> 運用` の 5 段階へ改稿しました。
  - `calibration`、`coverage`、`abstention`、`tail latency`、`recalibration burden` を独立した運用語として追加しました。

### 3. 旧用語ページは `connectivity` を `localization` の延長として読み替える余地を残していました

- 問題:
  - 旧 `measurement-and-modeling-terms` では `ESI / DCM / SCM` の列はありましたが、`connectivity claim は localization の次の段であり、別仮定が要る` という site rule が見えにくい構造でした。
- 根拠:
  - Haufe et al. (2013) は connectivity 指標間の結論が source mixing 条件で食い違いうることを示しました。
  - Palva et al. (2018) は source reconstruction 後にも ghost interaction が残りうると警告しました。
  - Penny et al. (2004) は DCM が候補構造の比較であることを示し、Vink et al. (2020) は EEG functional connectivity が causal interaction の弱い予測子にとどまることを報告しました。
  - Hauser & Bühlmann (2012) は介入が identifiability を細かくすることを理論的に示しました。
- 修正:
  - `wiki/measurement-and-modeling-terms.md` に `Detectability / Localization / Connectivity / Identifiability` の階段表を追加しました。
  - `Family Comparison`、`Held-out Perturbation`、`Ghost Interaction` を用語として明示し、`fit = validated` と読まない site rule を追加しました。

### 4. 旧用語層は `parameter degeneracy` を欠き、出力一致を唯一機序と誤読しやすい状態でした

- 問題:
  - 旧 glossary / wiki は、逆問題の非一意性は述べていたものの、`異なる内部パラメータで同じ出力が出る` という縮退の直感が不足していました。
- 根拠:
  - Prinz et al. (2004) は disparate circuit parameters から similar network activity が得られることを示しました。
- 修正:
  - `glossary.md` と `wiki/measurement-and-modeling-terms.md` に `Parameter Degeneracy` を追加し、`出力一致 ≠ 唯一の内部機序` を用語層でも固定しました。

## 今回実行した変更

- `glossary.md`
  - `last_updated` を 2026-03-15 に更新
  - `page_highlights / known / unknown` を recent terminology audit に合わせて更新
  - `よく混同する言葉` に `検出可能性 / 局在化`、`局在化 / 同定可能性`、`同定可能性 / 直接妥当化`、`confidence / calibration`、`calibration / deployability`、`lagged connectivity / leakage control` を追加
  - `計測` 節に `Observability Budget` と `Claim Ceiling` を追加
  - `モデル化` 節に `Detectability`、`Localization`、`Ghost Interaction`、`Family Comparison`、`Parameter Degeneracy` を追加
  - `不確実性と運用` 節を新設し、`Calibration`、`Coverage`、`Abstention`、`Tail Latency`、`Recalibration Burden` を追加
  - 参考文献を一次文献中心に増補
- `wiki/measurement-and-modeling-terms.md`
  - 4 段階整理を 5 段階整理へ全面改稿
  - `observability budget`、`claim ceiling`、`annotation provenance`、`latency / jitter` を整理段階まで含めて明示
  - `Detectability / Localization / Connectivity / Identifiability` の階段表を追加
  - `Direct Validation`、`Family Comparison`、`Held-out Perturbation` を妥当化段に明示
  - `Calibration / Coverage / Abstention / Tail Latency / Recalibration Burden` を運用段に新設
  - `site rule` と参考文献節を追加

## 検証

- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功。`_site` 生成まで完了。

## 外部依存で保留

- なし

## 参考文献

- Seeber M, Cantonas LM, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. *Nature Communications*. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Aydin U, Vorwerk J, Küpper P, et al. Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. *Frontiers in Neuroscience*. 2019.
  - https://doi.org/10.3389/fnins.2019.00531
- Mikulan E, Russo S, Parmigiani S, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. *Brain Communications*. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
- Haufe S, Nikulin VV, Müller KR, Nolte G. A critical assessment of connectivity measures for EEG data: a simulation study. *NeuroImage*. 2013.
  - https://doi.org/10.1016/j.neuroimage.2012.09.036
- Palva JM, Wang SH, Palva S, et al. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. *NeuroImage*. 2018.
  - https://doi.org/10.1016/j.neuroimage.2018.02.032
- Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004.
  - https://doi.org/10.1016/j.neuroimage.2004.03.026
- Hauser A, Bühlmann P. Characterization and Greedy Learning of Interventional Markov Equivalence Classes of Directed Acyclic Graphs. *JMLR*. 2012.
  - https://jmlr.csail.mit.edu/papers/v13/hauser12a.html
- Vink JJT, Klooster DCW, Ozdemir RA, et al. EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. *Brain Topography*. 2020.
  - https://doi.org/10.1007/s10548-020-00757-6
- Segal G, Keidar N, Lotan RM, et al. Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. *Frontiers in Neuroscience*. 2023.
  - https://doi.org/10.3389/fnins.2023.1184990
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Prinz AA, Bucher D, Marder E. Similar network activity from disparate circuit parameters. *Nature Neuroscience*. 2004.
  - https://doi.org/10.1038/nn1352
