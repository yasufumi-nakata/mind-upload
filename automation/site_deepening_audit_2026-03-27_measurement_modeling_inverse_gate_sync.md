# Site Deepening Audit (2026-03-27, measurement / modeling inverse-gate sync)

## 対象

- 主対象: `wiki/measurement-and-modeling-terms.md`
- 同期対象: `github-wiki-export/measurement-and-modeling-terms.md`
- web確認対象:
  - `https://mind-upload.com/wiki/measurement-and-modeling-terms.html`
  - `https://doi.org/10.1007/s10548-010-0154-x`
  - `https://doi.org/10.1002/hbm.20571`
  - `https://doi.org/10.1002/hbm.25272`
  - `https://doi.org/10.3389/fnhum.2024.1335212`
  - `https://doi.org/10.3389/fnhum.2024.1359753`
  - `https://doi.org/10.1109/TMI.2024.3506596`
  - `https://doi.org/10.1109/TMI.2025.3642620`
  - `https://doi.org/10.1038/s41597-020-0467-x`
  - `https://doi.org/10.1016/j.neuroimage.2023.120219`
  - `https://doi.org/10.1093/braincomms/fcad023`
  - `https://doi.org/10.1111/epi.18552`
  - `https://doi.org/10.1088/1741-2552/ae2f01`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `wiki/measurement-and-modeling-terms.md` は初学者導線として重要ですが、2026-03-27 時点の core page 群よりもなお一段粗く、`inverse problem` をほぼ一つの推定語として読ませる余地を残していました。
- しかし site 全体ではすでに
  - `field-formation visibility`
  - `forward-model / conductivity burden`
  - `solver-family / posterior uncertainty`
  - `validation class / source regime`
  を分けて読む規律が前面化されています。
- beginner page がここで粗いままだと、`better ESI` や `validated ESI` という語で、複数の異なる前進を一つの progress bar に再圧縮してしまいます。

## 根拠付き批判

### 1. inverse problem の上流にある `field-formation visibility` と downstream の solver 改良は同じ進歩ではありません

- [Ahlfors et al. (2010)](https://doi.org/10.1007/s10548-010-0154-x) は、EEG / MEG 感度が source orientation に強く依存することを示しました。
- [Goldenholz et al. (2009)](https://doi.org/10.1002/hbm.20571) は、source extent と anatomy が cortical SNR を大きく変えることを示しました。
- [Piastra et al. (2021)](https://doi.org/10.1002/hbm.25272) は、CSF を含む head-model detail が cortical / subcortical sensitivity を大きく動かすことを示しました。

批判:

- これらは「何がそもそもセンサへ届くか」という上流の壁です。
- 一方で posterior-aware solver や debiased inference は、その後段で candidate set をどう表すかという問題です。
- したがって `solver が良くなった` と `見える source class が増えた` は同じ問いではありません。

### 2. conductivity sensitivity と posterior-aware solver は別の failure mode を扱っています

- [Vorwerk et al. (2024)](https://doi.org/10.3389/fnhum.2024.1335212) は tissue conductivity uncertainty が EEG source analysis をどう動かすかを global sensitivity として整理しました。
- [Vorwerk et al. (2026)](https://doi.org/10.1088/1741-2552/ae2f01) は skull conductivity estimation が presurgical source analysis の不確実性をどこまで縮めるかを示しました。
- [Luria et al. (2024)](https://doi.org/10.3389/fnhum.2024.1359753) は posterior distribution と alternative configurations を出せる probabilistic route を整備しました。
- [Tong et al. (2025)](https://doi.org/10.1109/TMI.2024.3506596) は regularization bias を補正し、variance と hypothesis testing を扱う debiased inference を導入しました。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は extended source 向けの empirical-Bayesian uncertainty quantification を前面化しました。

批判:

- conductivity sensitivity は forward-model 側の burden です。
- probabilistic / debiased / empirical-Bayesian route は solver-family 側の burden です。
- 片方の前進をもう片方の解決として読ませるのは、技術的に誤りです。

### 3. validation class の違いを beginner page で隠すと、direct validation の意味がずれます

- [Mikulan et al. (2020)](https://doi.org/10.1038/s41597-020-0467-x) は known stimulation site を持つ human ground-truth dataset を与えました。
- [Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219) は focal-source in-vivo benchmark で method 差と parameter sensitivity を比較しました。
- [Unnwongse et al. (2023)](https://doi.org/10.1093/braincomms/fcad023) は多数の intracranial stimulation location を用いて depth と conductivity 依存の localization error を示しました。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は simultaneous HD-EEG / SEEG で ictal / interictal の accuracy 差を示しました。

批判:

- known-site stimulation、focal-source board、simultaneous invasive concordance、clinical ictal localization は同じ error question を答えていません。
- それなのに beginner page が `ESI was validated` の一言で済ませると、読者は validation class を一つの ladder と誤解します。

### 4. core page で厳しくした stop line が beginner page で再び緩むのは site-wide governance 上の穴です

- `wiki/observation-to-estimation.md` や `research_harvest_50.md` は既に inverse route を細分化していました。
- しかし beginner page 側で `inverse problem` を一語のまま置くと、入口で再び
  - `better solver`
  - `better conductivity model`
  - `better benchmark result`
  を合算して `inverse identifiability がかなり進んだ` と読めてしまいます。

批判:

- これは site 全体の stop line を入口ページで崩す構造です。
- よって、今回の優先修正対象として妥当でした。

## 今回実行した変更

- `wiki/measurement-and-modeling-terms.md`
  - `last_updated` を `2026-03-27` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` を、inverse problem を 4 ゲートで読む規律へ同期しました。
  - `2026-03-27 correction to the inverse-problem route` を追加し、field visibility, conductivity burden, solver uncertainty, validation class を別問題として明示しました。
  - `Inverse problem` と `ESI` の表記を改稿し、`one polished map` を禁止する site rule を beginner page に埋め込みました。
  - `Inverse-problem gate` table を追加し、
    - field-formation visibility
    - forward-model / conductivity burden
    - solver-family / posterior uncertainty
    - validation class / source regime
    の 4 分割を beginner page でも読めるようにしました。
  - `Read ESI by validation class, not solver name` を `Read ESI by four gates, not solver name` に更新しました。
  - 参考文献へ Ahlfors 2010, Goldenholz 2009, Piastra 2021, Pascarella 2023, Vorwerk 2024, Luria 2024, Tong 2025, Feng 2025, Vorwerk 2026 を追加しました。

- `github-wiki-export/measurement-and-modeling-terms.md`
  - 公開 wiki 側と同じ inverse-gate rule を同期しました。
  - GitHub Wiki 導線でも `inverse problem = one progress bar` を読めないようにしました。

## 今回止めた誤読

- `better ESI = inverse problem 全体が一段解決した`
- `posterior-aware solver = field visibility や forward-model uncertainty も実質解決した`
- `conductivity estimation が改善した = validation class の違いも吸収できる`
- `validated ESI = focal / extended / spontaneous / deep regime をまとめて通過した`

## 外部依存タスク

- なし
  - 今回の作業は repo 内の公開本文、wiki export、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Ahlfors SP, Han J, Belliveau JW, Hämäläinen MS. Sensitivity of MEG and EEG to source orientation. *Brain Topography*. 2010;23(3):227-232.
   - https://doi.org/10.1007/s10548-010-0154-x
2. Goldenholz DM, Ahlfors SP, Hämäläinen MS, Sharon D, Ishitobi M, Vaina LM, Stufflebeam SM. Mapping the signal-to-noise-ratios of cortical sources in magnetoencephalography and electroencephalography. *Human Brain Mapping*. 2009;30(4):1077-1086.
   - https://doi.org/10.1002/hbm.20571
3. Piastra MC, Nüßing A, Vorwerk J, Clerc M, Engwer C, Wolters CH. A comprehensive study on electroencephalography and magnetoencephalography sensitivity to cortical and subcortical sources. *Human Brain Mapping*. 2021;42(4):978-992.
   - https://doi.org/10.1002/hbm.25272
4. Michel CM, Brunet D. EEG source imaging: a practical review of the analysis steps. *Frontiers in Neurology*. 2019;10:325.
   - https://doi.org/10.3389/fneur.2019.00325
5. Mikulan E, Russo S, Bares M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020;7:127.
   - https://doi.org/10.1038/s41597-020-0467-x
6. Pascarella A, Mikulan E, Sciacchitano F, et al. An in-vivo validation of ESI methods with focal sources. *NeuroImage*. 2023;277:120219.
   - https://doi.org/10.1016/j.neuroimage.2023.120219
7. Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Communications*. 2023;5(2):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
8. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024;18:1335212.
   - https://doi.org/10.3389/fnhum.2024.1335212
9. Luria G, Viani S, Pascarella A, et al. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Frontiers in Human Neuroscience*. 2024;18:1359753.
   - https://doi.org/10.3389/fnhum.2024.1359753
10. Tong PF, Yang H, Ding X, et al. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2024.3506596
11. Feng Z, Mishne G, Hashemi A, et al. Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2025.3642620
12. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
   - https://doi.org/10.1111/epi.18552
13. Vorwerk J, Köhler T, Güllmar D, et al. Potential of EEG and EEG/MEG skull conductivity estimation to improve source analysis in presurgical evaluation of epilepsy. *Journal of Neural Engineering*. 2026;23(1):016007.
   - https://doi.org/10.1088/1741-2552/ae2f01
