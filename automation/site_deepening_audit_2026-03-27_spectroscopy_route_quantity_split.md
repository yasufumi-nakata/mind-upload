# Site Deepening Audit (2026-03-27, Spectroscopy Route Quantity-Type Split)

## 対象

- 主対象: `index.md`
- 主対象: `wbe_101.md`
- 主対象: `wiki/mind-upload-basics.md`
- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 主対象: `verification.md`
- 派生同期: `summary_booklet.md`

## 今回の選定理由

- 現行サイトはすでに human proxy を `macro biochemical scaffold` や `macro energetic proxy` として慎重に扱っていましたが、なお `spectroscopy-derived human route` を一段粗い粒度で読める箇所が残っていました。
- とくに front door と claim-ceiling 側では、`1H-MRSI metabolic similarity`, `31P-MRS energetic balance`, `deuterium metabolite / kinetic-rate imaging` が同じ inferential object の variation であるかのように見える余地がありました。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、human observability を議論する際に `spectroscopy evidence exists` だけでまとめると、実際には異なる quantity type, cohort burden, hardware burden, model burden を持つ route を同じ calibrator role と誤読しやすいからです。

## 根拠付き批判

### 1. 1H-MRSI similarity, 31P energetic balance, deuterium rate imaging は同じ quantity ではありません

- 問題:
  - 旧サイトは MRSI metabolic connectome を `similarity scaffold` として止めていましたが、サイト全体ではなお `biochemical / energetic` の二分で読める箇所が残っていました。
- 根拠:
  - [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は、gray-matter parcel 間の five-metabolite correlation から human metabolic connectome を構成しました。これは `parcel-level similarity structure` です。
  - [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は、healthy human brain で `ATP synthesis`, phosphorus-metabolite concentrations, pH, T1 relaxation times を 31P-MRS で評価しました。これは `energetic balance / phosphorus metabolism` の route です。
  - [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は dynamic deuterium MRSI により `CMRGlc`, `CMRLac`, `VTCA`, `Tmax` を人で推定しました。これは `kinetic glucose-rate imaging` です。
  - [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は 7 T dynamic deuterium metabolic imaging から `HDO / Glc / Glx / Lac` の absolute concentration と rate を定量しました。これは `absolute metabolite distribution + rate imaging` の route です。
- 批判:
  - したがって、`human spectroscopy` を一括語で扱うと quantity type が消えます。
  - `similarity`, `energetic balance`, `absolute metabolite distribution`, `kinetic rate imaging` は同じ inferential object ではありません。

### 2. 同じ 1H-MRSI でも map formation 自体に別の measurement-model burden があります

- 問題:
  - modality 名だけで route を固定すると、読者が `MRSI map = one stable biochemical picture` と読めてしまいます。
- 根拠:
  - [Bhogal et al. (2020)](https://doi.org/10.1002/brb3.1852) は 7 T 2D 1H-MRSI で lipid suppression と tissue-fraction correction を前提に metabolic distribution を扱いました。
  - [Wright et al. (2022)](https://doi.org/10.1016/j.neuroimage.2022.119574) は 9.4 T で voxel-specific T1-relaxation correction を伴う 12-metabolite mapping を行いました。
  - [Baboli et al. (2024)](https://doi.org/10.1148/radiol.232401) は whole-brain 3D MRSI で water normalization と absolute quantification burden を伴う route を提示しました。
  - [Guo et al. (2025)](https://doi.org/10.1109/TBME.2025.3572448) は high-resolution whole-brain metabolic imaging で ghosting, aliasing, low-SNR を抑える reconstruction burden を明示しました。
- 批判:
  - したがって、`1H-MRSI evidence exists` だけでは不十分です。
  - 少なくとも `metabolite set`, `parceling or voxel unit`, `correction model`, `artifact / QC burden`, `static similarity か rate imaging か` を disclosure しない限り、claim ceiling は上げられません。

### 3. 31P と deuterium を一括りにすると calibrator role が曖昧になります

- 問題:
  - `energetic imaging` という表現は、phosphorus metabolite balance と deuterated glucose / lactate kinetics を同じ proxy class として読ませやすいです。
- 根拠:
  - [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は resting healthy participants 12 名の 31P-MRS で ATP synthesis と pH を扱っており、局所 branch-level mitochondrial controller ではありません。
  - [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は healthy participants 5 名・7 T・custom dual-frequency coil・blood-input modeling を伴う小規模高負荷 route です。
  - [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) も 7 T dynamic DMI による absolute concentration / rate estimation であり、routine whole-brain maintenance-state assay ではありません。
- 批判:
  - したがって、`macro energetic proxy` の一語では calibrator role が粗すぎます。
  - safe reading は `31P energetic-balance proxy` と `deuterium metabolite / energetic-rate proxy` を分けたうえで、それぞれ bounded calibrator として止めることです。

### 4. 分光 route の存在は branch-local mitochondrial state を与えません

- 問題:
  - quantity split を入れたあとでも、human spectroscopy が local mitochondrial controller に近づいたと誤読される危険があります。
- 根拠:
  - 本サイトが maintenance-state 側で参照している causal literature は、ATP-linked presynaptic function, dendritic mitochondrial positioning / fission, ATP-synthase nano-organization, Ca2+-efflux tuning のような局所 object を問題にしています。
  - 上記の human spectroscopy papers は、そうした branch-local controller を直接測定していません。
- 批判:
  - したがって、今回の修正は `human spectroscopy is now near-direct maintenance-state readout` を支持しません。
  - むしろ `どの bounded hidden-state familyをどこまで calibrate できるか` を明示するための修正です。

## 今回実行した変更

- `index.md`
  - front-door の human evidence bullet を `1H-MRSI similarity / 31P energetic balance / deuterium metabolite-rate` に分割
  - note-box を spectroscopy quantity-type split に合わせて改稿

- `wbe_101.md`
  - human observability ladder を `1H-MRSI`, `31P-MRS`, `deuterium imaging` の 3 row に分解
  - spectroscopy route-card note を追加し、quantity type と burden を明示

- `wiki/mind-upload-basics.md`
  - beginner front door を `five-metabolite parcel-similarity scaffold / 31P energetic-balance route / deuterium metabolite-rate imaging` に更新
  - beginner ladder と measurement-model caution を分光 split に同期
  - references を追加

- `wiki/measurement-stack-and-claim-ceiling.md`
  - human-side description / highlights / known points を spectroscopy quantity-type split に更新
  - claim-ceiling 表を `1H-MRSI similarity`, `31P energetic-balance`, `deuterium metabolite / rate imaging` に分割
  - `proxy class / operational maturity / calibrator role` note を分光 split に合わせて改稿
  - `spectroscopy rows also split by quantity type and model burden` note を追加
  - references を追加

- `verification.md`
  - page highlight と known points に spectroscopy split rule を追加
  - `human maintenance evidence must be class-labeled` addendum を 1H-MRSI / 31P / deuterium の class 名へ更新
  - `spectroscopy-derived human routes are not one proxy row` addendum を追加
  - bioenergetic route-card 文言を `31P energetic-balance / deuterium metabolite-rate proxy` に同期
  - references を追加

- `summary_booklet.md`
  - 再生成対象に含めました

## 今回の修正で止めた誤読

- `human spectroscopy evidence exists = one near-direct maintenance-state route exists`
- `1H-MRSI similarity, 31P energetic balance, deuterium rate imaging はほぼ同じ proxy`
- `energetic imaging exists = branch-local mitochondrial fragility is now observable in humans`
- `MRSI map がある = quantity type と model burden は省略できる`

## 外部依存タスク

- なし
  - 今回の作業は repo 内の本文、監査メモ、要約同期で完結しています。

## 参考文献

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
2. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
3. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
4. Karkouri J, Deelchand DK, Van de Moortele P-F, et al. Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
5. Bhogal AA, Broeders TAA, Morsinkhof L, et al. Lipid-suppressed and tissue-fraction corrected metabolic distributions in human central brain structures using 2D 1H magnetic resonance spectroscopic imaging at 7 T. *Brain and Behavior*. 2020;10(10):e01852.
   - https://doi.org/10.1002/brb3.1852
6. Wright AM, Murali-Manohar S, Henning A. Quantitative T1-relaxation corrected metabolite mapping of 12 metabolites in the human brain at 9.4 T. *NeuroImage*. 2022;261:119574.
   - https://doi.org/10.1016/j.neuroimage.2022.119574
7. Baboli M, Wang F, Dong Z, et al. Absolute Metabolite Quantification in Individuals with Glioma and Healthy Individuals Using Whole-Brain Three-dimensional MR Spectroscopic and Echo-planar Time-resolved Imaging. *Radiology*. 2024;311(3):e232401.
   - https://doi.org/10.1148/radiol.232401
8. Guo R, Bogner W, Heckova E, et al. High-resolution whole-brain metabolic imaging using accelerated free induction decay MR spectroscopic imaging and a dual-branch super-resolution network. *IEEE Transactions on Biomedical Engineering*. 2025.
   - https://doi.org/10.1109/TBME.2025.3572448
