# Site Deepening Audit (2026-03-30, artifact-stack route-card sync)

## 対象

- 主対象:
  - `wiki/baselines-prereg-and-model-cards.md`
- 整合対象:
  - `verification.md`
  - `wiki/verification-basics.md`
  - `wiki/observation-to-estimation.md`
  - `wiki/uncertainty-confidence-and-abstention.md`
  - `wiki/thermodynamic-grounding-basics.md`
  - `wiki/state-continuity-bridge.md`
  - `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学
  - 法学
  - 制度論

## 今回この箇所を選んだ理由

- 2026-03-30 時点の site-wide rule では、`Verification` とその周辺 wiki はすでに
  - `Neural Contribution Card`
  - `Temporal Validity Card`
  - `Calibration & Abstention Card`
  - `Inverse-Solver Agreement Log`
  - `Tractography route card`
  - `Effective-connectivity route card`
  - `Irreversibility / thermodynamic route card`
  - `Intervention Card`
  - `Body / Environment Boundary Card`
  を個別に要求しておりました。
- しかし `wiki/baselines-prereg-and-model-cards.md` はまだ旧来の
  - `Specificity & Shortcut`
  - `Fusion`
  - `Pretraining`
  - `Human Proxy Composition`
  - `State-Continuity Bridge`
  の中心で止まっており、artifact stack の説明が site 全体より一段古いままでございました。
- その結果、このページだけを読んだ読者が
  - `generic companion card があれば十分`
  - `model card + benchmark + いくつかの補助 card`
  で strong claim を比較できるかのように誤読する余地が残っておりました。

## 主要結論

- 現在の site rule では、artifact stack はもはや
  - `generic companion cards`
  だけでは不十分でございます。
- 少なくとも次の claim family は、別々の failure mode を持つため、別々の card / log を要求すべきでございました。
  - `language-facing text / speech decode`
  - `EEG source imaging / inverse reconstruction`
  - `tractography / structural connectome`
  - `effective connectivity / DCM`
  - `thermodynamic irreversibility`
  - `intervention / closed loop / embodiment`
  - `cross-day or longitudinal generalization`
  - `confidence / interval / abstention-bearing outputs`
- よって、このページの safe reading は
  - `artifact stack = generic companion cards + route-specific cards/logs`
  に更新する必要がございました。

## 根拠付き批判

### 1. language-facing outputs は generic shortcut audit だけでは足りません

- [Tang et al. (2023)](https://doi.org/10.1038/s41593-023-01304-9) は、semantic reconstruction が fMRI と autoregressive context の両方に依存することを示しました。
- [Défossez et al. (2023)](https://doi.org/10.1038/s42256-023-00714-5) は、fixed 3-second speech segment retrieval を報告しました。
- [d'Ascoli et al. (2025)](https://doi.org/10.1038/s41467-025-65499-0) は、known word onset と fixed retrieval set に依存した word decoding を示しました。
- [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は、同日学習済み limited vocabulary と closed-loop voice synthesis を示しました。

批判:

- これらはすべて `brain-to-text` や `speech decode` と一括りにできますが、
  - candidate set
  - onset rule
  - language prior
  - prompt / vocoder scaffold
  - same-session dependence
  を分けて読まなければなりません。
- したがって `Specificity & Shortcut Card` だけでは不十分で、`Neural Contribution Card`、さらに時間一般化や confidence を含む場合は `Temporal Validity Card` と `Calibration & Abstention Card` が必要でございました。

### 2. ESI は one localization score では読めません

- [Horrillo-Maysonnial et al. (2023)](https://doi.org/10.1016/j.clinph.2023.08.009) は、targeted montage が high-density へ高い concordance を持ちうる一方で tangential generator では劣化することを示しました。
- [Rong et al. (2025)](https://doi.org/10.1016/j.clinph.2025.04.009) は、DeepSIF が electrode reduction に対して相対的に頑健でも route dependence を消さないことを示しました。
- [Unnwongse et al. (2023)](https://doi.org/10.1093/braincomms/fcad023)、[Hao et al. (2025)](https://doi.org/10.1111/epi.18552)、[Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219)、[Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は、それぞれ validation class、source regime、benchmark object、extended-source uncertainty が別問題であることを示しました。

批判:

- したがって `ESI improved` や `external validation exists` だけでは claim は読めません。
- `Inverse-Solver Agreement Log` と、validation class / source regime / benchmark object disclosure を stack に入れる必要がございました。

### 3. tractography は modality 名ではなく object typing が必要です

- [Gajwani et al. (2023)](https://doi.org/10.1162/netn_a_00324) は hub location の pipeline dependence を示しました。
- [He et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120904) は tractogram filtering により laterality が変わりうることを示しました。
- [McMaster et al. (2025)](https://doi.org/10.1016/j.mri.2025.110424)、[Bramati et al. (2026)](https://doi.org/10.3389/fnimg.2026.1670604) は acquisition / voxel size / q-space dependence を示しました。
- [Manzano-Patrón et al. (2025)](https://doi.org/10.1016/j.media.2025.103580)、[Zhu et al. (2025)](https://doi.org/10.1016/j.media.2025.103498) は uncertainty propagation と MRI-microscopy hybrid calibration が tractography chain の一部しか解決しないことを示しました。

批判:

- したがって `tractography result` は one graph headline では読めず、
  - acquisition / harmonization
  - endpoint assignment
  - graph construction
  - uncertainty
  - external calibration
  を分ける `Tractography route card` が必要でございました。

### 4. effective connectivity は candidate model disclosure だけでは足りません

- [Smith et al. (2011)](https://doi.org/10.1016/j.neuroimage.2010.08.063) は lag-based fMRI approaches の弱さを示しました。
- [Barnett & Seth (2017)](https://doi.org/10.1016/j.jneumeth.2016.10.016) は subsampling による detectability black spot / sweet spot を示しました。
- [Villaverde et al. (2019)](https://doi.org/10.1098/rsif.2019.0043) は full input-state-parameter observability を前景化しました。
- [Novelli et al. (2025)](https://doi.org/10.1002/hbm.70285)、[Jafarian et al. (2024)](https://doi.org/10.1002/hbm.26782)、[Yan et al. (2026)](https://doi.org/10.1109/TPAMI.2026.3658839) は sampling sensitivity、reliability-window dependency、latent confounders を示しました。

批判:

- したがって directed graph を `causal wiring` として読む前に、
  - observed-subsystem closure / latent-confound audit
  - node-definition policy
  - sampling / transformation sensitivity
  - validation
  - reliability window
  - abstention
  を要求する `Effective-connectivity route card` が必要でございました。

### 5. thermodynamic language は one quantity ではありません

- [Lynn et al. (2021)](https://doi.org/10.1073/pnas.2109889118) は coarse-grained BOLD state transitions から entropy-production lower bounds を推定しました。
- [Ishihara & Shimazaki (2025)](https://doi.org/10.1038/s41467-025-66669-w) は spike-train から model-based entropy flow を推定しました。

批判:

- これらはともに thermodynamic language を使いますが、
  - signal route
  - coarse-graining
  - estimator family
  - quantity type
  - closure assumption
  が異なります。
- よって `thermodynamic result` を generic model card の脚注で扱うのは弱く、`Irreversibility / thermodynamic route card` が必要でございました。

## 今回実行した変更

- `wiki/baselines-prereg-and-model-cards.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter の `description` / `page_intro` / `page_highlights` / `known_points` を、generic companion cards から route-specific cards / logs まで含む現在の site rule に合わせて更新しました。
  - `wiki_links` に
    - `observation-to-estimation`
    - `uncertainty-confidence-and-abstention`
    - `thermodynamic-grounding-basics`
    - `closed-loop-latency-jitter-and-safety-stops`
    を追加しました。
  - 新規 note box
    - `2026-03-30 addendum: generic companion cards are no longer enough for the current site rule`
    を追加しました。
  - roles table を拡張し、
    - `Neural Contribution Card`
    - `Route-specific cards / logs`
    - `Temporal Validity Card`
    - `Calibration & Abstention Card`
    を追加しました。
  - `Which extra artifacts are triggered by the claim` table を site-wide rule に合わせて全面更新し、
    - language-facing decode
    - ESI / inverse reconstruction
    - tractography
    - effective connectivity
    - thermodynamics
    - intervention / closed loop
    - probabilities / abstention
    を追加しました。
  - 新規 section
    - `Why route-specific cards had to be added`
    を追加し、claim family ごとの distinct failure mode を表で整理しました。
  - `Minimum checks when reading public pages` checklist に
    - `Neural Contribution`
    - `route-specific card/log`
    - `Intervention / Body / Environment`
    - `Temporal Validity / Calibration`
    を追加しました。
  - 参考文献と sidebar link を current site rule に合わせて拡張しました。

## 今回止めた誤読

- `artifact stack = benchmark + model card + generic companion cards`
- `language-facing output = generic decode`
- `ESI = one localization score`
- `tractography = one connectome object`
- `effective connectivity = discovered causal wiring`
- `thermodynamic headline = one stable quantity`
- `same-subject bridge = same-state`
- `confidence score = calibrated risk control`

## 検証結果

- `git diff --check`
  - pass
- `bundle exec jekyll build`
  - pass
  - build completed successfully at `2026-03-30` in the local workspace

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、公開ページ改稿、ローカル build 検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Tang J, LeBel A, Jain S, Huth AG. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nature Neuroscience*. 2023;26:858-866.
   - https://doi.org/10.1038/s41593-023-01304-9
2. d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. *Nature Communications*. 2025;16:10521.
   - https://doi.org/10.1038/s41467-025-65499-0
3. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025;644:145-152.
   - https://doi.org/10.1038/s41586-025-09127-3
4. Horrillo-Maysonnial A, Avigdor T, Abdallah C, et al. Targeted density electrode placement achieves high concordance with traditional high-density EEG for electrical source imaging in epilepsy. *Clinical Neurophysiology*. 2023;156:262-271.
   - https://doi.org/10.1016/j.clinph.2023.08.009
5. Rong J, Sun R, Joseph B, Worrell G, He B. Deep learning-based EEG source imaging is robust under varying electrode configurations. *Clinical Neurophysiology*. 2025;175:2010730.
   - https://doi.org/10.1016/j.clinph.2025.04.009
6. Gajwani M, Oldham S, Pang JC, et al. Can hubs of the human connectome be identified consistently with diffusion MRI? *Network Neuroscience*. 2023;7(4):1277-1304.
   - https://doi.org/10.1162/netn_a_00324
7. He Y, Hong Y, Wu Y, et al. Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. *NeuroImage*. 2024;297:120904.
   - https://doi.org/10.1016/j.neuroimage.2024.120904
8. Manzano-Patrón JP, Deistler M, Schröder C, et al. Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. *Medical Image Analysis*. 2025;103:103580.
   - https://doi.org/10.1016/j.media.2025.103580
9. Smith SM, Miller KL, Salimi-Khorshidi G, et al. Network modelling methods for FMRI. *NeuroImage*. 2011;54(2):875-891.
   - https://doi.org/10.1016/j.neuroimage.2010.08.063
10. Barnett L, Seth AK. Detectability of Granger causality for subsampled continuous-time neurophysiological processes. *Journal of Neuroscience Methods*. 2017;275:93-121.
   - https://doi.org/10.1016/j.jneumeth.2016.10.016
11. Villaverde AF, Tsiantis N, Banga JR. Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. *Journal of the Royal Society Interface*. 2019;16(156):20190043.
   - https://doi.org/10.1098/rsif.2019.0043
12. Novelli L, Barnett L, Seth AK, Razi A. Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. *Human Brain Mapping*. 2025;46(10):e70285.
   - https://doi.org/10.1002/hbm.70285
13. Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021;118(47):e2109889118.
   - https://doi.org/10.1073/pnas.2109889118
14. Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*. 2025;16:10852.
   - https://doi.org/10.1038/s41467-025-66669-w
