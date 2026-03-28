# Site Deepening Audit (2026-03-29, FAQ / Perspective spectroscopy proxy split)

## 対象

- 主対象:
  - `faq.md`
  - `perspective.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- サイト全体では既に spectroscopy taxonomy の細分化がかなり進んでおりましたが、`faq.md` の `Q2d` と `perspective.md` の human-route table には、なお `31P / deuterium energetic imaging` を一段で圧縮する箇所が残っておりました。
- この圧縮は、サイト自身が採用している
  - `proxy class`
  - `quantity type`
  - `operational maturity`
  - `calibrator role`
  を分けて書く方針と整合しません。
- とくに `31P` 側は、一次文献の時点で少なくとも
  - resting energetic balance
  - model-conditioned MT exchange flux
  - whole-brain intracellular NAD-content mapping
  - localized task-evoked functional NAD dynamics
  という別 row に分かれております。
- それにもかかわらず front door と perspective で `31P energetic imaging` を一つのルートのように書くと、読者が
  - `31P で何か見えた`
  - `だから energetic state はだいたい一段見えるようになった`
  - `static map` と `task-locked local dynamics` は似た種類の進歩だ
  と誤読しやすくなります。

## web確認対象

- https://pubmed.ncbi.nlm.nih.gov/26404723/
- https://pubmed.ncbi.nlm.nih.gov/27868234/
- https://pubmed.ncbi.nlm.nih.gov/27670385/
- https://pubmed.ncbi.nlm.nih.gov/31329342/
- https://pubmed.ncbi.nlm.nih.gov/38911598/
- https://pubmed.ncbi.nlm.nih.gov/41816808/
- https://pubmed.ncbi.nlm.nih.gov/40109558/
- https://www.nature.com/articles/s41467-025-66124-w.pdf

## 主要結論

- `31P route` は一つの inferential object ではございません。
- [Ren et al. (2015)](https://pubmed.ncbi.nlm.nih.gov/26404723/) は resting ATP synthesis / metabolites / pH / T1 の energetic-balance route であり、[Ren et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/27868234/) は 5-pool model を伴う MT exchange-flux route でございます。
- [Guo et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/38911598/) は 7 T での whole-brain intracellular NAD-content map であり、[Kaiser et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/41816808/) は prior fMRI で局在化した occipital voxel における task-evoked NAD+ dynamics でございます。
- [Li et al. (2025)](https://pubmed.ncbi.nlm.nih.gov/40109558/) は dynamic DMRSI と kinetic modeling による whole-brain glucose transport / metabolic-rate route であり、これも `31P balance` や `31P NAD route` の単純な延長ではございません。
- したがって、`faq.md` と `perspective.md` では `31P energetic imaging` を一行で書くのではなく、少なくとも
  - `31P energetic balance`
  - `31P MT exchange-flux`
  - `31P NAD-content mapping`
  - `localized functional 31P NAD dynamics`
  - `dynamic deuterium rate imaging`
  の別 row に分ける必要がございました。

## 根拠付き批判

### 1. `31P NAD` 自体が既に dedicated assay であり generic balance scalar ではございません

- [de Graaf et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/27670385/) は human 7 T で NAD+ detection を行い、`31P-MRS` 側は `NADH` と `UDPG` の spectral overlap が問題になることを示しました。

批判:

- したがって `31P` は modality 名だけで一つの row にまとめてよいものではございません。
- とくに NAD route は `ATP / pH` 近傍の generic energetic balance として潰せません。

### 2. static NAD map と functional NAD dynamics は同じ量ではございません

- [Guo et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/38911598/) は `whole-brain intracellular NAD content` を 7 T `31P-MRSI` でマッピングし、`2.3 cc` nominal resolution と repeat-scan reproducibility を示しました。
- [Kaiser et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/41816808/) は prior `fMRI` で局在化した visual-cortex voxel から `31P fMRS` を取得し、`25 healthy volunteers` における task-evoked `NAD+` dynamics を示しました。

批判:

- 前者は `whole-brain static content map`、後者は `localized task-locked dynamics` でございます。
- `spatial support`、`time axis`、`localization burden`、`calibrator role` が違うため、一つの `31P NAD route` として書くのは不正確でございます。

### 3. functional 31P route は whole-brain map の上位互換ではございません

- [Hendriks et al. (2019)](https://pubmed.ncbi.nlm.nih.gov/31329342/) は visual stimulation に対する `31P functional MRS` を成立させるために、close-fitting coil, 7 T, large visual angle, large spectroscopy volume など高 SNR 前提を組み合わせました。
- [Kaiser et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/41816808/) でも測定対象は `functionally localized visual cortex voxel` でございました。

批判:

- よって functional `31P` は `whole-brain state map` を強くした route ではなく、bounded task design に依存した localized dynamics route でございます。

### 4. deuterium kinetic imaging も `31P` の延長表現ではございません

- [Li et al. (2025)](https://pubmed.ncbi.nlm.nih.gov/40109558/) は dynamic DMRSI と kinetic model により `0.7 cc nominal voxel`、`2.5 min/image`、whole-brain coverage で `CMR_Glc`, `CMR_Lac`, `V_TCA`, `T_max` を推定しました。

批判:

- これは `energetic balance` でも `NAD content` でも `functional NAD dynamics` でもございません。
- `kinetic rate imaging` は独立した quantity type として書く必要がございます。

### 5. `1H-MRSI similarity` との境界整理にもこの split は必要でございます

- [Lucchetti et al. (2025)](https://www.nature.com/articles/s41467-025-66124-w.pdf) は five-metabolite `1H-MRSI` から parcel-level metabolic similarity scaffold を構築し、`51` 例本体と `13` 例独立 replicate を示しました。

批判:

- `similarity scaffold`、`31P energetic balance`、`31P exchange flux`、`31P NAD content map`、`localized functional NAD dynamics`、`deuterium kinetic rate imaging` は別 object でございます。
- ここを分けない限り、site の observability / identifiability の説明が front door で粗くなります。

## 今回実行した変更

- `faq.md`
  - front matter の `known_points` を更新し、spectroscopy row を `31P energetic balance / MT exchange-flux / NAD-content mapping / localized functional NAD-dynamics / deuterium rate imaging` に分離しました。
  - `Q2c` の hidden-state paragraph を更新し、human energetic routes の split を明文化しました。
  - `Q2d` の導入 paragraph を更新し、Ren 2015 / Ren 2017 / Guo 2024 / Kaiser 2026 / Li 2025 を別 quantity type として説明しました。
  - `Q2d` table を更新し、31P/deuterium row を 5 行へ分解しました。
  - `Route name alone is too coarse` と `Same quantity?` の説明を更新し、`31P route` を一段で読ませないよう修正しました。
  - 参考文献リストへ Ren 2017 / Guo 2024 / Kaiser 2026 を追加しました。

- `perspective.md`
  - human-route table の `Human energetic imaging (31P-MRS / dynamic DMRSI)` を削除し、`31P energetic-balance`, `31P MT exchange-flux`, `31P NAD-content mapping`, `localized functional 31P NAD-dynamics`, `dynamic deuterium rate imaging` の 5 行へ分解しました。
  - `31P route names need their own quantity split` note-box を追加し、de Graaf 2017 / Hendriks 2019 / Guo 2024 / Kaiser 2026 に基づく stop rule を front door に近い位置へ挿入しました。
  - `Proxy class, operational maturity, and calibrator role are different axes` の note を更新し、spectroscopy rows の quantity-type split を反映しました。
  - `Quantity-type collapse` 行を更新し、spectroscopy row をより正確に分解しました。

## 今回止めた誤読

- `31P で見えた` = `human energetic state の汎用 meter が一段強くなった`
- `whole-brain NAD-content map` = `task-evoked local NAD dynamics`
- `31P energetic balance` = `31P exchange-flux` = `31P NAD map`
- `dynamic deuterium rate imaging` を `31P route` の別名として読める
- `spectroscopy improved` の一言で similarity / balance / flux / static content / local dynamics / kinetic rate をまとめてよい

## 外部依存タスク

- なし
  - 今回の作業は web 上の一次文献確認、repo 内公開ページ改稿、監査メモ作成、検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Ren J, Sherry AD, Malloy CR. (2015). 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times.
   - https://doi.org/10.1002/nbm.3384
2. Ren J, Sherry AD, Malloy CR. (2017). Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T.
   - https://doi.org/10.1002/mrm.26560
3. de Graaf RA, De Feyter HM, Brown PB, et al. (2017). Detection of cerebral NAD+ in humans at 7T.
   - https://doi.org/10.1002/mrm.26465
4. Hendriks AD, van der Kemp WJM, Luijten PR, Petridou N, Klomp DWJ. (2019). SNR optimized 31P functional MRS to detect mitochondrial and extracellular pH change during visual stimulation.
   - https://doi.org/10.1002/nbm.4137
5. Guo R, Yang S, Wiesner HM, et al. (2024). Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla.
   - https://doi.org/10.3389/fnins.2024.1389111
6. Li X, Zhu X-H, Li Y, et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging.
   - https://doi.org/10.1093/pnasnexus/pgaf072
7. Kaiser A, Vind FA, Duarte JMN, et al. (2026). Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation.
   - https://doi.org/10.1177/0271678X261415784
8. Lucchetti F, Céléreau E, Steullet P, et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization.
   - https://doi.org/10.1038/s41467-025-66124-w
