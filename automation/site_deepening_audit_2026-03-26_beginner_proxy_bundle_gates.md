# 2026-03-26 サイト深掘り監査: beginner ページの human-proxy bundle 三軸・三ゲート不足

- 対象ページ: `faq.md`, `wiki/verification-basics.md`
- 同期参照: `verification.md`, `wiki/human-proxy-composition.md`, `wiki/measurement-stack-and-claim-ceiling.md`
- web 確認対象: `https://mind-upload.com/faq.html#q2d`, `https://mind-upload.com/wiki/verification-basics.html`

## 1. 今回このページ群を選んだ理由

- サイト本体では、living-human proxy bundle を `proxy class / operational maturity / calibrator role` の三軸で読み、さらに `robustness / common-driver・quantity-bridge / increment` の三ゲートで昇格判定する規則が、すでに `verification.md` と `wiki/human-proxy-composition.md` に実装されております。
- しかし beginner 導線である `faq.md` と `wiki/verification-basics.md` では、その rule がまだ十分に前面化されていませんでした。
- 特に `faq.md` は Q2d で human route の読み方をなお `two-dimensional` と表現しており、`calibrator role` が抜けていました。
- また `wiki/verification-basics.md` は `proxy bundle と bridge が重要` までは述べていましたが、proxy bundle の内部にある `三軸` と `三ゲート` が beginner level では見えないため、読者が `row を並べれば state closure に近い` と誤読しうる余地が残っていました。

## 2. 主批判

### 2-1. `proxy class` と `operational maturity` だけでは、何を較正できるかが固定されません

- `Johansen et al. (2024)` は healthy-human SV2A atlas であり、regional synaptic-density proxy を押し上げますが、momentary synaptic efficacy を直接固定しません。
- `Lucchetti et al. (2025)` は five-metabolite MRSI similarity graph であり、parcel-level biochemical scaffold です。kinetic rate imaging や local controller readout ではありません。
- `Li et al. (2025)` は 7 T dynamic DMRSI + kinetic model による macro energetic-rate route であり、branch-local ATP reserve や mitochondrial positioning を直接与えません。
- `Baadsvik et al. (2024)` は myelin bilayer mapping の proof-of-principle ですが、per-axon timing controller を固定しません。
- `Hirschler et al. (2025)` と `Dagum et al. (2026)` は support-state / clearance-side route を押し上げますが、cell-specific immune controller や synapse-level maintenance logic ではありません。
- したがって beginner ページでも `calibrator role` を独立軸として書かなければ、`real human route` が `maintenance-state の広い較正` にすり替わります。

### 2-2. bundle の問題は taxonomy だけではなく、robustness と composition の問題でもあります

- `Finnema et al. (2018)` は route-specific SV2A PET でも regional V_T の mean absolute test-retest reproducibility が `3-9%` であることを示しました。つまり `存在する route` と `安定した route` は同じではありません。
- `Holiga et al. (2018)` は common task-fMRI / resting-fMRI measures の reliability が `poor to excellent` まで広く散ることを示しました。fMRI という modality label だけでは reliability は固定されません。
- `Wirsich et al. (2021)` は simultaneous EEG-fMRI connectome relationship が `72 subjects / 4 centres / 1.5T-7T` で reproducible であることを示しましたが、これは逆に `cross-centre robustness は示す必要があるが自動ではない` ことを意味します。
- `Amiri et al. (2023)` は acute DoC cohort で `87 enrolled patients` のうち `63` だけが EEG+fMRI を持ち、direct same-feature comparison は `48 patients` に縮むことを示しました。bundle は complete-case slice を隠せません。
- `Manasova et al. (2026)` は multimodal multicentre validation で modality 増加に伴う performance gain を示しつつ、clinically important groups で higher inter-modality disagreement も示しました。bundle は `more rows = solved` ではありません。
- `Vafaii et al. (2024)` は simultaneous Ca2+ / BOLD で `common and divergent` organization を示し、`Epp et al. (2025)` は task BOLD と oxygen metabolism が opposite sign を取りうることを示しました。cross-row agreement は shared factor や quantity mismatch を含みえます。
- したがって beginner ページでも `robustness / common-driver・quantity-bridge / increment` の三ゲートを見せないと、Human Proxy Composition Card が単なる taxonomy 表になってしまいます。

## 3. 今回実行した変更

### 3-1. `faq.md`

- front matter の `page_highlights` に `three axes` を追加しました。
- `known_points` に `proxy class / operational maturity / calibrator role` の分離を追加しました。
- Q2d の `two-dimensional` という表現を廃止し、`three-axis` へ改稿しました。
- 同節で bundle 昇格条件を `robustness / common-driver・quantity-bridge / increment` の三ゲートとして明文化しました。
- note-box を `Seven quick checks behind the three-gate rule` へ改稿し、`Finnema / Holiga / Wirsich` に基づく repeatability / transfer check と、`Vafaii / Manasova` に基づく composition / increment check を追加しました。
- 参考文献に `Finnema`, `Holiga`, `Wirsich`, `Vafaii`, `Amiri`, `Bolt`, `Manasova` を追加しました。

### 3-2. `wiki/verification-basics.md`

- `last_updated` を `2026-03-26` に更新しました。
- front matter の `page_highlights` と `known_points` に、三軸・三ゲートを追加しました。
- 冒頭 note-box に `2026-03-26 beginner tightening: proxy bundles now need three axes and three gates` を新設しました。
- 新節 `Human proxy bundles now need three axes and three gates` を追加し、
  - `proxy class`
  - `operational maturity`
  - `calibrator role`
  の三軸 table と、
  - `robustness`
  - `common-driver / quantity-bridge`
  - `increment over the strongest single row`
  の三ゲート table を導入しました。
- `Living-human proxy bundle` row の説明を、`quantity type` だけでなく `safe calibrator role` と `three-gate disclosure` まで含むように改稿しました。
- `Representative primary-literature reasons` を拡張し、beginner page でも human-proxy bundle の failure mode を文献根拠つきで追えるようにしました。
- 参考文献に `Finnema`, `Holiga`, `Wirsich`, `Amiri`, `Vafaii`, `Epp`, `Manasova` を追加しました。

## 4. 今回の変更で止めた誤読

- `human route が複数ある = それらは同じ hidden-state family を較正している`
- `route が real = deployable and robust route`
- `same-subject bundle = same-state bundle`
- `row diversity = state closure`
- `Human Proxy Composition Card = ただの taxonomy 表`

## 5. 外部依存タスク

- なし。今回の修正はこのセッションで repo 内完結で実行可能でした。

## 6. 参考文献

1. Finnema SJ, Nabulsi NB, Mercier J, et al. Kinetic evaluation and test-retest reproducibility of [11C]UCB-J, a novel radioligand for positron emission tomography imaging of synaptic vesicle glycoprotein 2A in humans. *J Cereb Blood Flow Metab*. 2018;38(11):2041-2052. https://doi.org/10.1177/0271678X17724947
2. Holiga S, Sambataro F, Luzy C, et al. Test-retest reliability of task-based and resting-state blood oxygen level dependence and cerebral blood flow measures. *PLOS ONE*. 2018;13(11):e0206583. https://doi.org/10.1371/journal.pone.0206583
3. Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. *NeuroImage*. 2021;231:117864. https://doi.org/10.1016/j.neuroimage.2021.117864
4. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *J Neurosci*. 2024;44(33):e1750232024. https://doi.org/10.1523/JNEUROSCI.1750-23.2024
5. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nat Commun*. 2025;16:11344. https://doi.org/10.1038/s41467-025-66124-w
6. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
7. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magn Reson Med*. 2024;91(6):2332-2344. https://doi.org/10.1002/mrm.29998
8. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nat Neurosci*. 2025;28(11):2392-2401. https://doi.org/10.1038/s41593-025-02073-3
9. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nat Commun*. 2026;17:715. https://doi.org/10.1038/s41467-026-68374-8
10. Amiri M, Fisher PM, Raimondo F, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023;146(1):50-64. https://doi.org/10.1093/brain/awac335
11. Manasova V, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026. https://doi.org/10.1093/brain/awaf412
12. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nat Commun*. 2024;15:229. https://doi.org/10.1038/s41467-023-44363-z
13. Bolt T, Wang S, Nomi JS, et al. Autonomic physiological coupling of the global fMRI signal. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-01945-y
14. Epp SM, Halani S, Paquette M, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-02132-9
