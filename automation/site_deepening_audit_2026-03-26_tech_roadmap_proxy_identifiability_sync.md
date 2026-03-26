# Site Deepening Audit (2026-03-26, `tech_roadmap.md` proxy / identifiability sync)

## 対象

- 主対象: `tech_roadmap.md`
- 再生成対象: `summary_booklet.md`
- web確認対象:
  - `https://doi.org/10.1038/s41467-025-66124-w`
  - `https://doi.org/10.1038/s41593-025-02073-3`
  - `https://doi.org/10.1038/s41467-026-68374-8`
  - `https://doi.org/10.2967/jnumed.121.263255`
  - `https://doi.org/10.1371/journal.pone.0206583`
  - `https://doi.org/10.1016/j.neuroimage.2021.117864`
  - `https://doi.org/10.1093/brain/awac335`
  - `https://doi.org/10.1093/brain/awaf412`
  - `https://doi.org/10.1038/s41467-023-44363-z`
  - `https://doi.org/10.1038/s41467-025-64414-x`
  - `https://doi.org/10.1038/s41593-025-02080-4`
  - `https://doi.org/10.1016/j.crmeth.2023.100520`
  - `https://doi.org/10.1038/s41586-025-08790-w`
  - `https://doi.org/10.1038/s41598-024-70609-x`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `tech_roadmap.md` はサイトの主要な依存関係マップですが、`last_updated` が `2026-03-25` のままで、3月26日に site-wide で強化された
  - human proxy の `cohort / regime`
  - bundle `robustness / availability`
  - multimodal / same-brain / connectome-constrained の candidate-set audit
  との同期がまだ弱い状態でした。
- そのため、roadmap 本体だけを読む読者は、他ページで既に停止線へ昇格した論点を見落としうる状態でした。

## 根拠付き批判

### 1. M3 は `proxy class / maturity / calibrator role` だけでは bundle promotion を止め切れていませんでした

- 一次文献が押し上げている human proxy rows は、同じ cohort / physiological regime から来ていません。
  - [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は adolescents を主 cohort に持ちます。
  - [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) は healthy younger adults の 7T route です。
  - [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は healthy older adults の sleep-deprivation crossover です。
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) は AD continuum の reactive-astrogliosis PET です。
- したがって、`human routes are converging` を one matched human baseline のように読むのは不適切です。

### 2. bundle の強さは row diversity だけで決まりません

- [Holiga et al. (2018)](https://doi.org/10.1371/journal.pone.0206583) は MRI-derived metrics の test-retest reliability が `poor to excellent` まで分散することを示しました。
- [Wirsich et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.117864) は simultaneous EEG-fMRI connectomes の cross-setup reproducibility を示しましたが、これは `robustness can be demonstrated` という意味であり、未検証 bundle に自動付与される性質ではありません。
- [Amiri et al. (2023)](https://doi.org/10.1093/brain/awac335) では same-sample multimodal comparison が `n = 48` の full-feature subset に依存しました。
- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は missing values を `-1` で扱う multicentre multimodal prediction を採用しつつ、MCS / improved patients で pairwise disagreement が高いことを示しました。
- したがって `more rows`、`same session`、`multicentre` を bundle stability や same-state closure に読み替えるのは弱いです。

### 3. R7 は observability / identifiability を分けていても、multimodal / connectome-constrained / same-brain sequential を別監査として止め切れていませんでした

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は simultaneous multimodal data に共通成分と相違成分の両方が残ることを示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI に tight coupling と distinct network patterns の両方があることを示しました。
- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は connectome-constrained network でも追加録音なしには dynamics の縮退が残ることを示しました。
- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520) と [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) は same-brain sequential pipeline に preservation / stage gap があることを示します。
- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) は 10-hour EEG dynamics が decode condition を動かすことを示しました。
- よって `multimodal`, `connectome-constrained`, `same-brain` は、それぞれ
  - observability gain
  - conditional model restriction
  - specimen identity
  を前進させますが、候補集合の collapse や same-state continuity を自動では与えません。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter の `page_highlights` / `known_points` に
    - `cohort / physiological regime`
    - `row robustness / availability`
    - `bridge / composition validity`
    を追加
  - M3 の入口 note を更新し、three-axis ladder の上に bundle-level gate があることを前面化
  - M3 に
    - mixed cohort / regime
    - route-local repeatability
    - cross-centre transfer
    - complete-case / missing-row policy
    の停止線を追記
  - M3 の bundle promotion rule を
    - same-subject / same-session
    - cohort / regime compatibility
    - row-level repeatability
    - availability disclosure
    - external calibration
    - Human Proxy Composition Card
    へ拡張
  - R7 の supplement を更新し、audit を
    - observability budget
    - structural identifiability
    - practical identifiability
    - bridge / composition validity
    - external validation / abstention
    の 5 段へ拡張
  - R7 に table を追加し、
    - same-session multimodal bundle
    - connectome-constrained predictor
    - same-brain / same-subject sequential pipeline
    を別々の audit object として固定

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成予定

## 今回止めた誤読

- `three-axis ladder を満たせば human bundle は十分強い`
- `adolescent scaffold + younger-adult CSF mobility + older-adult clearance = one matched baseline`
- `same-session multimodal = candidate-set closure`
- `connectome-constrained = unique recovery`
- `same-brain sequential = same-state evidence`

## 外部依存タスク

- なし
  - 今回の作業は repo 内文書更新、要約再生成、build 検証、push までこのセッションで完結可能です。

## 参考文献

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-66124-w
2. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-02073-3
3. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026. https://doi.org/10.1038/s41467-026-68374-8
4. Villemagne VL, Rowe CC, Burnham S, et al. Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022. https://doi.org/10.2967/jnumed.121.263255
5. Holiga Š, Sambataro F, Luzy C, et al. Test-retest reliability of task-based and resting-state blood oxygen level dependence and cerebral blood flow measures. *PLoS One*. 2018. https://doi.org/10.1371/journal.pone.0206583
6. Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.117864
7. Amiri M, Andelic N, Westhall E, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023. https://doi.org/10.1093/brain/awac335
8. Manasova D, Hermann B, Calligaris C, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026. https://doi.org/10.1093/brain/awaf412
9. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024. https://doi.org/10.1038/s41467-023-44363-z
10. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-64414-x
11. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-02080-4
12. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023. https://doi.org/10.1016/j.crmeth.2023.100520
13. MICrONS Consortium, Bae JA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025. https://doi.org/10.1038/s41586-025-08790-w
14. Egger J, Kostoglou K, Müller-Putz GR. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024. https://doi.org/10.1038/s41598-024-70609-x
