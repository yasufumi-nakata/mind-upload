# Site Deepening Audit (2026-03-17, Measurement / Modeling Guide and Card Alignment)

## 対象

- 主対象: `wiki/measurement-and-modeling-terms.md`
- 副対象: `wiki/verification-basics.md`

## 今回の選定理由

- 2026-03-17 時点で公開サイト本体は、`multimodal ≠ state-complete`、`same-day success ≠ cross-day validity`、`high confidence ≠ safe deployment` をかなり強く区別できていました。
- その一方で、学習導線の中核である `wiki/measurement-and-modeling-terms.md` と `wiki/verification-basics.md` では、これらの境界がなお `5段階の学習フロー` や `監査` という大きな箱へ圧縮されていました。
- この弱点は技術・自然科学の観点で重要です。なぜなら、観測・proxy・model-dependent inference・運用証拠を同じ `見えた / 分かった / 使えた` で読むと、主張の昇格が一段ずつではなく一気に起こるからです。

## 主要な批判点

### 1. 旧 `measurement-and-modeling-terms` は `5段階` の説明はできていましたが、site-wide の提出物仕様へ十分につながっていませんでした

- 問題:
  - 旧ページは `観測→整理→推定→妥当化→運用` の流れ自体は明瞭でした。
  - しかし、最近 Verification に追加された `Observability Budget`、`Fusion Card`、`latent-state error budget`、`Temporal Validity Card`、`Calibration & Abstention Card` がどの段階の failure mode を止めるのかが見えにくく、学習ガイドと実際の運用ルールが少しずれていました。
- 批判:
  - これでは読者が、`段階の理解` と `提出物の理解` を別々に覚える必要があり、site-wide の一貫性が落ちます。
  - さらに `proxy を明示する card`、`hidden state を明示する card`、`何日持つかを明示する card`、`confidence semantics を明示する card` が別物だと分からないまま、1 枚の audit で全部済むように誤読しやすくなります。
- 修正:
  - `5段階` と `site-wide card` の対応表を追加しました。
  - `観測 = Observability Budget`、`推定 = latent-state error budget / Fusion Card`、`妥当化 = Intervention Card`、`運用 = Temporal Validity Card / Calibration & Abstention Card` を接続しました。

### 2. 旧学習ガイドは `direct`、`proxy`、`inferred`、`deployable` を十分に分けていませんでした

- 問題:
  - 旧 `measurement-and-modeling-terms` は detectability / localization / identifiability / direct validation / deployability を区別していました。
  - しかし `見えた` の中に、`sensor signal を直接測った`、`proxy を得た`、`モデル依存で internal state を推定した`、`長期運用できた` が同時に入っており、measurement class ごとの差がやや曖昧でした。
- 根拠:
  - Seeber et al. (2019) は deep activity の detectability を前進させましたが、Aydin et al. (2019) が示すように conductivity uncertainty だけでも localization は動きます。
  - Murphy et al. (2011) と Williams et al. (2023) は、BOLD difference が neural state だけでなく vascular transfer state / CVR にも支配されることを示しました。
  - Finnema et al. (2016)、Naganawa et al. (2021)、Johansen et al. (2024) が押し上げたのは human in vivo の `regional synaptic-density proxy` であって、current synaptic efficacy の direct readout ではありません。
  - Wilson et al. (2025) は、長期 intracortical BCI で deployability が recalibration burden に大きく依存することを示しました。
- 批判:
  - したがって、`direct signal`、`proxy`、`model-based inference`、`operational evidence` は、site の学習入口でも明示的に分ける必要があります。
- 修正:
  - `EEG / MEG`、`fMRI / BOLD`、`SV2A PET`、`chronic extracellular probe` を例に、何が direct で何が proxy / inferred かを整理する表を追加しました。

### 3. 旧 `verification-basics` は `監査` を 1 箱にまとめすぎていました

- 問題:
  - 旧 `verification-basics` は、標準、ベンチ、事前登録、監査の 4 部品を初歩向けに説明する点では成功していました。
  - しかし `監査` の内部で、`何を直接見たか`、`何をどう結び付けたか`、`どの latent state が残るか`、`何日持つか`、`低信頼時にどう止まるか` の差が見えませんでした。
- 批判:
  - 初学者がここで `audit = 1 枚の成績表` と理解すると、Verification 本文に入った時点で card 群が増えすぎたように見え、逆に学習コストが上がります。
- 修正:
  - `verification-basics` に `監査は 1 枚では足りません` 節を新設し、Observability / Fusion / latent-state / Intervention / Temporal Validity / Calibration & Abstention の役割差を表にしました。

## 今回実行した変更

- `wiki/measurement-and-modeling-terms.md`
  - `last_updated` を `2026-03-17` に更新
  - front matter と highlights / known points を、`direct / proxy / inferred / deployable` と site-wide card 対応が分かる内容へ更新
  - `5段階と site-wide 提出物の対応` 節を追加
  - `direct / proxy / inferred / deployable を同じ『見えた』にしない` 節を追加
  - deployment 節に `Temporal Validity Card` と `Calibration & Abstention Card` の役割差を追加
  - site rule を 5 本から 7 本へ拡張
  - 参考文献に Murphy (2011), Williams (2023), Finnema (2016), Naganawa (2021), Johansen (2024) を追加
- `wiki/verification-basics.md`
  - `last_updated` を `2026-03-17` に更新
  - front matter と highlights / known points を更新
  - `監査は 1 枚では足りません` 節を追加
  - `measurement-and-modeling-terms` への導線を追記

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と学習導線の改稿で完結しています。

## 参考文献

1. Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. *Nature Communications*. 2019.
   - https://doi.org/10.1038/s41467-019-08725-w
2. Aydin U, Vorwerk J, Küpper P, et al. Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. *Frontiers in Neuroscience*. 2019.
   - https://doi.org/10.3389/fnins.2019.00531
3. Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. *Brain Communications*. 2023.
   - https://doi.org/10.1093/braincomms/fcad023
4. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
   - https://doi.org/10.1111/epi.18552
5. Murphy K, Harris AD, Wise RG. Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. *NeuroImage*. 2011.
   - https://doi.org/10.1016/j.neuroimage.2010.07.059
6. Williams RJ, Specht JL, Mazerolle EL, Lebel RM, MacDonald ME, Pike GB. Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. *Frontiers in Physiology*. 2023.
   - https://doi.org/10.3389/fphys.2023.1167148
7. Finnema SJ, Nabulsi NB, Eid T, et al. Imaging synaptic density in the living human brain. *Science Translational Medicine*. 2016.
   - https://doi.org/10.1126/scitranslmed.aaf6667
8. Naganawa M, Nabulsi N, Lin S-F, et al. First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. *Journal of Nuclear Medicine*. 2021.
   - https://doi.org/10.2967/jnumed.120.249144
9. Johansen A, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
10. Haufe S, Nikulin VV, Müller K-R, Nolte G. A critical assessment of connectivity measures for EEG data: a simulation study. *NeuroImage*. 2013.
   - https://doi.org/10.1016/j.neuroimage.2012.09.036
11. Palva JM, Wang SH, Palva S, et al. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. *NeuroImage*. 2018.
   - https://doi.org/10.1016/j.neuroimage.2018.02.032
12. Vink JJT, Klooster DCW, Ozdemir RA, et al. EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. *Brain Topography*. 2020.
   - https://doi.org/10.1007/s10548-020-00757-6
13. Segal G, Keidar N, Lotan RM, et al. Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. *Frontiers in Neuroscience*. 2023.
   - https://doi.org/10.3389/fnins.2023.1184990
14. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
