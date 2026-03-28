# Site Deepening Audit (2026-03-29, 31P NAD static-vs-functional split)

## 対象

- 主対象:
  - `index.md`
  - `wbe_101.md`
  - `verification.md`
  - `tech_roadmap.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wiki/human-proxy-composition.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `wiki/mind-upload-basics.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- サイト全体の human proxy taxonomy は既にかなり厳密でしたが、`31P NAD` 周りだけはまだ `NAD-content / functional routes` のような圧縮が残っておりました。
- しかし一次文献を辿ると、少なくとも human-side の `31P NAD` には次の別物がございます。
  - `whole-brain intracellular NAD content mapping`
  - `task-evoked localized NAD+ dynamics`
- この二つは同じ `31P NAD route` ではございません。量の型、空間支持、時間窓、必要なローカライゼーション、モデル依存、妥当な calibrator role が異なります。
- この圧縮を残すと、読者が
  - `31P で NAD が見えた`
  - `human energetic state の route が 1 本太くなった`
  - `whole-brain content map` と `task-locked local dynamics` はだいたい同じ
  と誤読しやすくなります。

## 主要結論

- `31P NAD-content mapping` と `31P functional NAD-dynamics` は、同じ modality を共有していても同じ inferential object ではございません。
- 前者は `whole-brain intracellular NAD content` を狙う静的マッピング系、後者は `functionally localized voxel` での `task-evoked NAD+ dynamics` を狙う局所・時間依存系です。
- 従って site の taxonomy では、
  - `macro 31P NAD-content map proxy`
  - `localized functional 31P NAD-dynamics proxy`
  の 2 行に分ける必要がございました。
- この split を入れない限り、site 自身が採用している `quantity type / proxy class / calibrator role を分けて書く` という基準と整合しません。

## 根拠付き批判

### 1. `31P NAD` は最初から generic energetic-balance scalar ではありません

- [Zhu et al. (2015)](https://doi.org/10.1073/pnas.1417921112) は healthy human brain における in vivo `31P` NAD assay を用い、`intracellular NAD contents` と `redox state` を扱いました。
- [de Graaf et al. (2017)](https://doi.org/10.1002/mrm.26465) は human brain 7 T で cerebral `NAD+` detection を行い、`31P-MRS` 側では `NADH` や `UDPG` との spectral overlap が問題になることを明示しました。

批判:

- したがって `31P NAD` は、`ATP / PCr / pH` の近くにあるからといって、そのまま generic `energetic-balance` の下位項として潰してよい量ではございません。
- 一次文献の時点で既に、`NAD` は dedicated assay / fitting / overlap handling を要する別 quantity class として立っております。

### 2. `whole-brain NAD content map` と `functional local NAD dynamics` は同じ量ではありません

- [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111) は 7 T `31P-MRSI` と probabilistic subspace-based processing を用いて、`entire human brain` の `intracellular NAD content` マッピングの feasibility を示しました。
- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) は 25 healthy volunteers を対象に、prior `fMRI` で機能局在化した occipital voxel から `31P fMRS` を取得し、visual stimulation block 中の `NAD+` dynamics を報告しました。

批判:

- 前者は `whole-brain content mapping`、後者は `task-locked local dynamics` でございます。
- これは `quantity type` だけでなく、`spatial support`、`time axis`、`localization burden` まで違います。
- それにもかかわらず両者を `31P NAD-content / functional routes` という一段に押し込むと、site の claim ceiling 読みが粗くなります。

### 3. functional 31P route は局所・刺激依存・高設計負荷であり、whole-brain map の代替ではありません

- [Hendriks et al. (2019)](https://doi.org/10.1002/nbm.4137) は visual stimulation 下の human `31P functional MRS` で mitochondrial / extracellular pH-related change を見るために、large visual angle、7 T、close-fitting RF coil、high-SNR acquisition を組み合わせました。
- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) でも、測定対象は `functionally localized` な occipital voxel であり、block design と prior `fMRI` に依存しております。

批判:

- したがって functional `31P` route は、generic `macro energetic state meter` ではございません。
- これは `same-subject whole-brain NAD map` の上位互換でもなく、`task-general controller identity` を読める route でもございません。
- 妥当な calibrator role は、せいぜい `bounded task-locked local NAD-dynamics proxy` まででございます。

### 4. `31P energetic balance`、`31P MT exchange-flux`、`31P NAD map`、`31P functional NAD dynamics` は 31P 内部でも別行であるべきです

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は `ATP synthesis`, phosphorus metabolites, intra-/extracellular pH, T1 relaxation を測りました。
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) は 7 T band-inversion / MT 5-pool model で `PCr->ATP` と `Pi->ATP` exchange flux を推定しました。
- [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111) は `NAD content map`、[Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) は `functional NAD dynamics` を示しました。

批判:

- つまり human `31P` だけを見ても、
  - resting metabolite / pH balance
  - model-conditioned MT exchange flux
  - whole-brain NAD-content mapping
  - localized functional NAD dynamics
  という別 row がございます。
- これを一つの `31P route` として扱うのは、一次文献の quantity split を site 側で再び潰してしまうことになります。

### 5. この split は deuterium や 1H-MRSI との境界整理にも必要です

- [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は five-metabolite `1H-MRSI` から parcel-similarity scaffold を作りました。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は dynamic deuterium MRSI と kinetic modeling で glucose-metabolic rate terms を whole-brain map として推定しました。
- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は specialized 7 T deuterium route で absolute HDO / Glc / Glx / Lac maps と rate maps を作りました。

批判:

- `31P` 内部の split が曖昧なままですと、site の spectroscopy taxonomy 全体も曖昧になります。
- `1H-MRSI similarity scaffold`、`31P energetic balance`、`31P NAD-content map`、`31P functional NAD dynamics`、`deuterium absolute metabolite map`、`deuterium kinetic-rate imaging` は、それぞれ別の inferential object として並べるべきでございます。

## 今回実行した変更

- `index.md`
  - front-door bullet と spectroscopy note を更新し、`31P NAD-content mapping` と `31P functional NAD-dynamics` を分離しました。
- `wbe_101.md`
  - human observability ladder で `Human 31P NAD-content mapping route` と `Human 31P functional NAD-dynamics route` を別 row にしました。
- `verification.md`
  - observability / composition 側の rule を更新し、`macro 31P NAD-content map proxy` と `localized functional 31P NAD-dynamics proxy` を別 proxy class として明示しました。
- `tech_roadmap.md`
  - roadmap の human proxy family summary と M3 addendum を更新し、`Guo 2024` と `Kaiser 2026` を別 route として書き分けました。
- `wiki/measurement-stack-and-claim-ceiling.md`
  - spectroscopy stack table と proxy-class summary を更新し、`NAD content map` と `functional NAD dynamics` の claim ceiling を分離しました。
- `wiki/human-proxy-composition.md`
  - composition rule を更新し、`31P NAD` を単一 row として合成させないようにしました。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - macro energetic proxy family の説明と route-card 項目を更新しました。
- `wiki/mind-upload-basics.md`
  - beginner front door でも `31P NAD-content mapping` と `31P functional NAD-dynamics` を別 route として説明するよう修正しました。

## 今回止めた誤読

- `31P で NAD が見えた` = `human energetic state の near-direct meter が一段成立した`
- `whole-brain intracellular NAD content map` = `task-evoked local NAD+ dynamics`
- `31P energetic balance` = `31P MT exchange-flux` = `31P NAD map` = `31P functional NAD dynamics`
- `functional voxel assay` を `whole-brain state map` の近似として読める
- `31P` と `deuterium` と `1H-MRSI` をまとめて `spectroscopy improved` の一言で済ませてよい

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、repo 内本文修正、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Zhu X.-H., Lu M., Lee B.-Y., et al. In vivo NAD assay reveals the intracellular NAD contents and redox state in healthy human brain and their age dependences. *Proceedings of the National Academy of Sciences*. 2015;112(9):2876-2881.
   - https://doi.org/10.1073/pnas.1417921112
2. de Graaf R. A., De Feyter H. M., Brown P. B., et al. Detection of cerebral NAD+ in humans at 7T. *Magnetic Resonance in Medicine*. 2017;78(3):828-835.
   - https://doi.org/10.1002/mrm.26465
3. Ren J., Sherry A. D., Malloy C. R. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
4. Ren J., Sherry A. D., Malloy C. R. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017;77(3):901-910.
   - https://doi.org/10.1002/mrm.26560
5. Hendriks A. D., van der Kemp W. J. M., Luijten P. R., Petridou N., Klomp D. W. J. SNR optimized 31P functional MRS to detect mitochondrial and extracellular pH change during visual stimulation. *NMR in Biomedicine*. 2019;32(11):e4137.
   - https://doi.org/10.1002/nbm.4137
6. Guo R., Yang S., Wiesner H. M., et al. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. *Frontiers in Neuroscience*. 2024;18:1389111.
   - https://doi.org/10.3389/fnins.2024.1389111
7. Li X., Zhu X.-H., Li Y., et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
8. Lucchetti F., Celereau E., Steullet P., et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
9. Kaiser A., Vind F. A., Duarte J. M. N., et al. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
10. Karkouri F., Shah N. J., Deelchand D. K. Absolute deuterium metabolic imaging and concentration mapping in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
