# Site Deepening Audit (2026-03-18, EEG Source-Validation Evidence Classes)

## 対象

- 主対象: `eeg_101.md`
- 副対象: `datasets.md`
- 副対象: `verification.md`
- 副対象: `faq.md`
- 副対象: `wiki/eeg-basics.md`
- 副対象: `wiki/observation-to-estimation.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`EEG inverse problem`、`head model / conductivity`、`外部検証が必要` という大筋は既にかなり強く書けていました。
- その一方で、`external validation` がなお 1 つの箱として読める箇所が残っていました。とくに `simulation / phantom`、`intracranial stimulation`、`simultaneous HD-EEG/SEEG`、`postsurgical outcome` は、同じ検証強度ではありません。
- これは技術・自然科学の観点で重要です。なぜなら、どの validation class を通ったかで答えられる誤差質問が違うからです。solver の挙動監査、既知刺激位置に対する localization error、同時 invasive 記録との concordance、臨床的な resection concordance は、いずれも別の evidence class です。

## 根拠付き批判

### 1. 旧 public pages は `external validation` を要求していても、validation class の違いを front door で十分に固定していませんでした

- 問題:
  - `eeg_101.md` と `verification.md` では、source imaging claim に external validation が必要であること自体は書かれていました。
  - しかし、`simulation / phantom`、`intracranial stimulation`、`simultaneous SEEG`、`postsurgical outcome` が何を検証し、何をまだ検証していないかが入口で分かりにくい構造でした。
- 根拠:
  - Mikulan et al. (2020) は intracerebral stimulation と 256ch HD-EEG を同時公開し、既知刺激位置を基準に source localization method を監査できる ground-truth dataset を提示しました。
  - Unnwongse et al. (2023) は human intracranial electrical stimulation を ground truth に使い、localization error が source depth と skull conductivity に依存することを示しました。
  - Hao et al. (2025) は simultaneous HD-EEG/SEEG で、ictal / interictal ESI の局在精度が source depth と source power に依存することを示しました。
  - Birot et al. (2014) は 38 例の高密度 EEG / intracranial EEG / 術後転帰を用い、ESI-max と irritative zone の距離や resection concordance を評価しました。
- 批判:
  - したがって、`validated` を 1 語で済ませると、`known stimulation site に対する誤差` と `clinical concordance` と `同時 invasive reference` の差が消えます。
  - site-wide rule として、`validation class` を申告しない source-imaging claim は弱すぎました。

### 2. 旧 `Datasets` の validation ladder では C 段がなお heterogeneous でした

- 問題:
  - `datasets.md` は A/B/C の 3 段で source-imaging data を整理していました。
  - しかし C 段の中で、stimulation ground truth・simultaneous SEEG・postsurgical outcome がまとめて扱われていました。
- 根拠:
  - Mikulan et al. (2020) は `known stimulation location / time` を与えます。
  - Hao et al. (2025) は concurrent SEEG を reference としますが、病的活動と cohort 条件に依存します。
  - Birot et al. (2014) は術後転帰と intracranial EEG を用いた clinical concordance を与えますが、source ground truth そのものではありません。
- 批判:
  - これらは全部 `C: direct validation` ではあるものの、同じ質問に答えていません。
  - したがって、利用者が `C stage を 1 つ通れば source imaging は十分に validated` と誤読する余地が残っていました。

### 3. 旧 `Verification` は external calibration route を要求していても、提出物として `何の誤差をどの benchmark で監査したのか` まで要求していませんでした

- 問題:
  - `verification.md` は Observability Budget で `external calibration route` を求めていました。
  - しかし提出フォーマットとして、`validation class`、`target error`、`safe claim ceiling` を分けて書かせていませんでした。
- 根拠:
  - Unnwongse et al. (2023) は depth / conductivity dependence を直接示しました。
  - Hao et al. (2025) は simultaneous SEEG reference でも depth / source power dependence が残ることを示しました。
  - Seeber et al. (2019) は 256ch HD-EEG と同時 DBS から subcortical detectability を示しましたが、general unique reconstruction を主張していません。
- 批判:
  - したがって submission 側では、`どの validation class を通ったから何を言えるのか` を明記しないと、predictability 改善や concordance 改善を `unique restoration` にすり替えやすいままでした。

### 4. 引用不整合が残っており、証跡追跡性を下げていました

- 問題:
  - `verification.md` の一部では、Hao et al. (2025) に対して `10.1007/s00415-025-12886-9` と別タイトルが残っていました。
  - `wiki/eeg-basics.md` と `wiki/observation-to-estimation.md` などには、`10.1111/epi.18552` に対して旧題・旧著者表記が残っていました。
- 根拠:
  - PubMed の一次情報では、該当論文は `Shenglin Hao et al.` による *HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy*、DOI `10.1111/epi.18552` です。
- 批判:
  - この種の引用 drift は、validation class の読み分け以前の基礎証跡を崩します。
  - 科学的な front door では、タイトル・著者・DOI の一致を優先して直す必要がありました。

## 今回実行した変更

- `eeg_101.md`
  - `external validation` を 1 つの箱にしない page highlight / known point を追加
  - ESI 節に `validation class` の比較表を追加
  - `simulation / phantom`、`stimulation ground truth`、`simultaneous invasive recording`、`postsurgical outcome` の safe reading を分離
  - 参考文献を増補し、`Michel & Brunet` の誤 DOI も修正
- `datasets.md`
  - stage C をさらに `stimulation / simultaneous invasive / postsurgical outcome` の evidence class に分解
  - `C stage is not one box` という読解ルールを note box で明記
  - Birot et al. (2014) を参考文献へ追加
- `verification.md`
  - page highlight / known point に `validation class` の分離を追加
  - Observability Budget の `external calibration route` を `validation class` まで書かせる形式に改稿
  - Verification Rigor に `ESI validation is a ladder, not one checkbox` の表を追加
  - Hao et al. (2025) の DOI / title / author drift を修正し、Mikulan / Birot を追加
- `faq.md`
  - EEG の短答に、`external validation` を 1 つの checkbox として読まない site rule を追加
- `wiki/eeg-basics.md`
  - Hao et al. (2025) のタイトル / 著者表記を修正
- `wiki/observation-to-estimation.md`
  - Gate 4 を `validation class` の明示まで要求する形に改稿
  - Hao et al. (2025) の参考文献表記を修正
- `github-wiki-export/eeg-basics.md`
  - wiki export 側の Hao et al. (2025) 引用を同期修正
- `github-wiki-export/observation-to-estimation.md`
  - wiki export 側の Gate 4 / 引用を同期修正
- `tech_roadmap.md`
  - 参考文献表記の Hao et al. (2025) を一次情報に合わせて修正

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・wiki・引用整合の改稿で完結しています。

## 参考文献

1. Birot G, Spinelli L, Vulliemoz S, et al. Head model and electrical source imaging: a study of 38 epileptic patients. *NeuroImage: Clinical*. 2014;5:77-83.
   - https://doi.org/10.1016/j.nicl.2014.06.005
2. Mikulan E, Russo S, Parmigiani S, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020;7:127.
   - https://doi.org/10.1038/s41597-020-0467-x
3. Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. *Nature Communications*. 2019;10:753.
   - https://doi.org/10.1038/s41467-019-08725-w
4. Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. *Brain Communications*. 2023;5(2):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
5. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
   - https://doi.org/10.1111/epi.18552
6. Aydin U, Vorwerk J, Kupper P, et al. Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. *Frontiers in Neuroscience*. 2019;13:531.
   - https://doi.org/10.3389/fnins.2019.00531
7. Lantz G, Grave de Peralta R, Spinelli L, Seeck M, Michel CM. Epileptic source localization with high density EEG: how many electrodes are needed? *Clinical Neurophysiology*. 2003;114(1):63-69.
   - https://doi.org/10.1016/S1388-2457(02)00337-1
8. Song J, Davey C, Poulsen C, et al. EEG source localization: Sensor density and head surface coverage. *Journal of Neuroscience Methods*. 2015;256:9-21.
   - https://doi.org/10.1016/j.jneumeth.2015.08.015
