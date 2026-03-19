# Site Deepening Audit (2026-03-19, MRSI Metabolic Connectome Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03 時点の公開サイトは、human-side observability を `structural scaffold / synaptic-density proxy / macro biochemical / energetic / ionic / thermal / myelin / support proxy / perturbation-conditioned proxy` にかなり丁寧に分解できております。
- しかし `human metabolic connectome` という語は、読者に `別種の connectome が脳全体で見えた`、あるいは `brain-wide metabolic flux network が直接測れた` という印象を残しやすい状態でした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、`connectome` という語が structural connectome と同じ inferential weight を帯びやすく、さらに `metabolic` という語が glucose-flux / ATP-turnover / energetic-state imaging と混線しやすいからです。

## 根拠付き批判

### 1. `metabolic connectome` は axonal graph ではなく、五つの代謝物に基づく parcel-similarity graph でした

- 問題:
  - 旧公開本文は `human metabolic connectome` を `macro-biochemical scaffold` としては置いていましたが、その object が何であるかを十分に operational に書いていませんでした。
- 根拠:
  - Lucchetti et al. (2025) は、この object を `pairwise correlations among five metabolites (tCr, tNAA, Glx, Ins, Cho) across gray-matter parcels` と定義しました。
  - 同論文は、overall metabolic similarity が tractography-based structural connectivity とは weak にしか整合せず、むしろ cytoarchitectonic similarity と gene co-expression により近いと報告しました。
- 批判:
  - したがって `metabolic connectome` を structural connectome と同じ意味で読むのは誤りです。
  - 安全な読解は、`gray-matter parcel-level biochemical similarity graph` です。

### 2. この object は static 1H-MRSI similarity scaffold であり、metabolic-rate imaging ではありませんでした

- 問題:
  - `metabolic` という語だけで、読者が glucose transport, ATP turnover, oxidative / nonoxidative flux まで直接見えたかのように読める余地が残っていました。
- 根拠:
  - Lucchetti et al. (2025) の主 object は `1H-MRSI metabolite profile similarity` です。
  - これに対して Li et al. (2025) は dynamic deuterium MRSI と kinetic model を用いて、CMRGlc, CMRLac, VTCA, Tmax を whole-brain で定量しました。
- 批判:
  - つまり `static metabolite similarity` と `dynamic metabolic rate imaging` は別 object です。
  - `metabolic connectome` が存在することから、現在の glucose flux や ATP-related turnover が直接見えたと読むのは overread です。

### 3. MRSI route は measurement model を強く持つため、route card が必要でした

- 問題:
  - 旧公開本文は PET については tracer / quantification route を強く要求していましたが、MRSI row には同じレベルの route-card 要件がありませんでした。
- 根拠:
  - Bhogal et al. (2020) は、in vivo MRSI に low SNR, partial-volume effects, extracranial lipid artifacts, scan-time constraints があると明示し、1 mm^3 tissue-fraction correction と QC threshold が必要だと示しました。
  - Wright et al. (2022) は、voxel-specific T1 correction を averaged T1 で置き換えると GM/WM 差が大きい代謝物地図に bias が入ると示しました。
  - Baboli et al. (2024) は、whole-brain MRSI absolute quantification が tissue-water / relaxation correction の取り方でずれうることを示しました。
  - Lucchetti et al. (2025) 自身も、5 mm isotropic MRSI に対して RBV + PSF deconvolution による partial-volume correction を行っています。
- 批判:
  - したがって MRSI row も `modality name` だけでは読めません。
  - `metabolite set`, `parceling unit`, `resolution / PSF / partial-volume correction`, `lipid / water handling`, `spectral QC`, `abstention boundary`, `static similarity vs kinetic rate imaging` を route card 化する必要がありました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `human metabolic connectome` row を `five-metabolite parcel-similarity graph` として改稿しました。
  - `metabolic-connectome route card` note を新設し、structural graph / flux map / local controller への overread を止めました。
  - dangerous-reading table に `connectome / flux` 誤読を止める行を追加しました。
  - 参考文献へ Bhogal (2020), Wright (2022), Baboli (2024) を追加しました。
- `wbe_101.md`
  - front-door highlights / known points に MRSI metabolic-connectome ceiling を追加しました。
  - human observability ladder の row を `similarity scaffold` として改稿しました。
  - `The MRSI metabolic-connectome row also needs a route card` note を追加しました。
  - 参考文献へ Bhogal (2020), Wright (2022), Baboli (2024) を追加しました。
- `verification.md`
  - page highlights / known points に MRSI metabolic-connectome route-card requirement を追加しました。
  - Observability Budget の `Human evidence class / observability ceiling` に MRSI-specific disclosure 要件を追加しました。
  - `MRSI metabolic connectome is a similarity graph, not a flux map` note を追加しました。
  - 参考文献へ Lucchetti (2025), Bhogal (2020), Wright (2022), Baboli (2024) を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・運用要件・参考文献の改稿で完結しております。

## 参考文献

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
2. Bhogal AA, Broeders TAA, Morsinkhof L, et al. Lipid-suppressed and tissue-fraction corrected metabolic distributions in human central brain structures using 2D 1H magnetic resonance spectroscopic imaging at 7 T. *Brain and Behavior*. 2020;10(12):e01852.
   - https://doi.org/10.1002/brb3.1852
3. Wright AM, Murali-Manohar S, Henning A. Quantitative T1-relaxation corrected metabolite mapping of 12 metabolites in the human brain at 9.4 T. *NeuroImage*. 2022;263:119574.
   - https://doi.org/10.1016/j.neuroimage.2022.119574
4. Baboli M, Wang F, Dong Z, et al. Absolute Metabolite Quantification in Individuals with Glioma and Healthy Individuals Using Whole-Brain Three-dimensional MR Spectroscopic and Echo-planar Time-resolved Imaging. *Radiology*. 2024;312(3):e232401.
   - https://doi.org/10.1148/radiol.232401
5. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
