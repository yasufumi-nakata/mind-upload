# Site Deepening Audit (2026-03-27, tech_roadmap human route taxonomy sync)

## 対象

- 主対象: `tech_roadmap.md`
- 再生成対象: `summary_booklet.md`
- web確認対象:
  - `https://doi.org/10.1038/s41467-025-66124-w`
  - `https://doi.org/10.1002/nbm.3384`
  - `https://doi.org/10.1093/pnasnexus/pgaf072`
  - `https://doi.org/10.1002/mrm.70308`
  - `https://doi.org/10.1038/s41598-018-28852-6`
  - `https://doi.org/10.1002/mrm.29998`
  - `https://doi.org/10.1111/bpa.70010`
  - `https://doi.org/10.1002/nbm.5256`
  - `https://doi.org/10.1016/j.neurobiolaging.2024.12.012`
  - `https://doi.org/10.1038/s41467-025-58356-7`
  - `https://doi.org/10.2967/jnumed.121.263255`
  - `https://doi.org/10.2967/jnumed.118.208009`

## 今回この箇所を選んだ理由

- `tech_roadmap.md` は site の依存関係を最初に固定する主ページですが、2026-03-27 時点でも M3 の human in vivo ladder だけは一段粗い状態でした。
- 他ページではすでに
  - `1H-MRSI similarity`
  - `31P energetic balance`
  - `deuterium metabolite / rate`
  - `quantity-defined myelin family`
  - `BBB water-exchange`
  - `tracer-specific BBB transport`
  - `target-defined astrocyte PET`
  を分けて読ませている一方、Roadmap ではなお
  - `Dynamic DMRSI`
  - `Myelin bilayer MRI`
  - `Human astrocyte-related PET`
  のような粗い family name が残っていました。
- これは技術・自然科学の観点で重要です。Roadmap でこの圧縮を許すと、他ページで止めている `human observability is converging` の過読が再導入されるからです。

## 根拠付き批判

### 1. spectroscopy は one row ではありません

- [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は `five-metabolite parcel-similarity scaffold` です。
- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は `ATP synthesis / phosphorus metabolites / intra-extracellular pH` の `31P energetic-balance route` です。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) と [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は `deuterium metabolite / rate imaging` です。

批判:

- したがって `human spectroscopy` を一行で置くと、similarity / energetic balance / kinetic-rate の違いが消えます。
- これは quantity type の圧縮であり、calibrator role の過大評価につながります。

### 2. myelin も one meter ではありません

- [Koshino et al. (2018)](https://doi.org/10.1038/s41598-018-28852-6) は SyMRI, MTsat, T1w/T2w ratio の一致度差を示しました。
- [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は bilayer-sensitive route を示しましたが、healthy volunteers 2 名の proof-of-principle です。
- [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) は postmortem MS cortex で `qT1` が remyelination-sensitive である一方、`MWF` と `MTR` は demyelination と remyelination を分けなかったと報告しました。

批判:

- よって `myelin MRI` は一つの interchangeable meter ではありません。
- quantity-defined family として固定しない限り、per-axon timing support や remyelination sensitivity を同じ強さで読んでしまいます。

### 3. BBB も one permeability row ではありません

- [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は DP-ASL と ME-ASL で `Kw` が `106.6 ± 19.7` と `306.8 ± 71.7 min^-1` に分かれることを示しました。
- [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は multi-echo ASL で adult lifespan の BBB water permeability を扱いました。
- [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は `molecule-specific transport mechanism` を通る `tracer-specific BBB permeability-surface-area product` を dynamic PET で定量しました。

批判:

- `BBB proxy` を一行で置くと、water exchange と tracer-specific transport が同じ inferential object であるかのように読めます。
- 実際には quantity type と transport regime が違うため、同じ ceiling を与えるのは不適切です。

### 4. astrocyte PET も target-defined route の集合です

- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) は MAO-B linked reactive astrogliosis burden を扱いました。
- [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は I2BS PET ligand の first-in-human route を評価しました。

批判:

- したがって `human astrocyte-related PET` を generic astrocyte-state meter のように置くのは粗いです。
- target-defined route であることを明示しない限り、MAO-B と I2BS が同じ target class を測ったかのように誤読されます。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を `2026-03-27` に更新しました。
  - front matter の `page_highlights` / `known_points` に、human route family を quantity / target / transport 単位へ割り戻す rule を追加しました。
  - M3 の addendum title を更新し、`quantity / target / transport split` を前面化しました。
  - M3 本文で
    - `1H-MRSI similarity`
    - `31P energetic balance`
    - `deuterium metabolite / rate`
    - `quantity-defined myelin family`
    - `BBB water-exchange`
    - `tracer-specific BBB PET transport`
    - `target-defined astrocyte PET`
    を別 object として明示しました。
  - M3 table を拡張し、上記 rows を別 ceiling で記述しました。
  - bundle-level paragraph も更新し、within-family split を fix した後でしか cohort / robustness gate に進めないことを明示しました。

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` による再生成対象です。

## 今回止めた誤読

- `human spectroscopy` が一つの human route である
- `myelin MRI` が一つの interchangeable meter である
- `BBB proxy` が一つの generic permeability scalar である
- `human astrocyte-related PET` が generic astrocyte-state meter である
- `proxy class / maturity / calibrator role` さえ書けば family-internal split は省略できる

## 外部依存タスク

- なし
  - 今回の作業は repo 内本文、監査メモ、要約再生成、build 検証、push までで完結できます。

## 参考文献

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-66124-w
2. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015. https://doi.org/10.1002/nbm.3384
3. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
4. Karkouri J, Novoselova M, Rodgers CT, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. *Magnetic Resonance in Medicine*. 2026. https://doi.org/10.1002/mrm.70308
5. Koshino S, Hagiwara A, Okuda S, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018. https://doi.org/10.1038/s41598-018-28852-6
6. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024. https://doi.org/10.1002/mrm.29998
7. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025. https://doi.org/10.1111/bpa.70010
8. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024. https://doi.org/10.1002/nbm.5256
9. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025. https://doi.org/10.1016/j.neurobiolaging.2024.12.012
10. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-58356-7
11. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022. https://doi.org/10.2967/jnumed.121.263255
12. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018. https://doi.org/10.2967/jnumed.118.208009
