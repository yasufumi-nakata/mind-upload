# Site Deepening Audit (2026-03-16, Mechanistic Boundary / Hidden-State Evidence Class)

## 対象

- 主対象: `mind_uploading_papers.md`
- 主対象: `research_harvest_50.md`
- 副対象: `wiki/paper-source-types-and-evidence-status.md`
- 副対象: `wiki/literature-and-evidence-reading.md`

## 今回の選定理由

- 2026-03-16 時点で、公開サイトは `direct validation`、`task-limited demo`、`dataset / benchmark / standard` をかなり明確に分けられていました。
- ただし、技術・自然科学の議論で極めて重要な `何がまだ十分でないかを示す一次研究` が、まだ独立クラスとして固定されていませんでした。
- この弱点は深刻です。なぜなら、WBE や brain-to-text の高 score を過大解釈しやすい箇所では、しばしば
  - `何ができたか` を示す demo 論文
  - `何を直接妥当化したか` を示す validator 論文
  - `何がまだ latent state / omitted mechanism として残るか` を示す mechanistic boundary 論文
  が混ざって読まれるからです。

## 主要な批判点

### 1. 旧サイトは `高性能 demo` と `十分性を止める mechanistic paper` を同じ evidence class で運用していました

- 問題:
  - `mind_uploading_papers.md` と `research_harvest_50.md` は、非侵襲 decode、speech neuroprosthesis、ESI direct validation を強く整理できていました。
  - しかし、`connectome + cell type + high score demo` ではまだ十分でないことを示す一次研究が、入口の evidence class としては独立していませんでした。
- 根拠:
  - <https://doi.org/10.1038/s41586-020-2907-3> の Gouwens et al. (2021) は、transcriptomic type の内部にも morpho-electric variation が残ることを示しました。
  - <https://doi.org/10.1016/j.cell.2016.01.046> の Hengen et al. (2016)、<https://doi.org/10.1038/s41593-023-01536-9> の Xu et al. (2024) は、sleep / wake をまたぐ firing-rate homeostasis と network regime recovery を示しました。
  - <https://doi.org/10.1038/s41593-023-01558-3> の Looser et al. (2024) は、oligodendrocyte-axon metabolic coupling が timing と axonal health に効くことを示しました。
  - <https://doi.org/10.1038/s41586-024-07311-5> の Cahill et al. (2024)、<https://doi.org/10.1038/s41586-024-08170-w> の Williamson et al. (2025) は、astrocyte network / ensemble が recall や local transmitter integration に関わることを示しました。
  - <https://doi.org/10.1038/s41593-025-02080-4> の Beiran & Litwin-Kumar (2025) は、connectome 制約を入れても未測定 biophysical parameter のために recurrent dynamics の縮退が残ることを示しました。
- 修正:
  - 4 ページすべてで `mechanistic boundary / hidden-state evidence` を独立クラスとして追加しました。

### 2. 旧サイトは `何ができたか` と `何がまだ足りないか` の論文を、読む順番として固定できていませんでした

- 問題:
  - 高 score の demo 論文を見た読者が、そのまま強い主張へ上げやすい構造が残っていました。
- 根拠:
  - <https://doi.org/10.1038/s41593-023-01304-9> の Tang et al. (2023)、<https://doi.org/10.1038/s41467-025-65499-0> の d'Ascoli et al. (2025)、<https://doi.org/10.1038/s41586-023-06377-x> の Willett et al. (2023)、<https://doi.org/10.1038/s41593-025-01905-6> の Littlejohn et al. (2025)、<https://doi.org/10.1038/s41586-025-09127-3> の Wairagkar et al. (2025) は、課題限定の decode / communication performance を強くします。
  - しかし上記の mechanistic boundary 論文群は、同じ成果から whole-brain sufficiency へは上げられない理由を別の軸で与えます。
- 修正:
  - `mind_uploading_papers.md` に、demo 論文を mechanistic boundary paper と対で読む site rule を追加しました。
  - `research_harvest_50.md` にも、高 score 論文のあとに boundary paper を 1 本挟む rule を追加しました。

### 3. 旧 evidence class は `reproducibility / governance` と `mechanistic ceiling` を十分に分離していませんでした

- 問題:
  - `dataset / benchmark / standard` は比較条件を整える重要なクラスですが、何が biological sufficiency を止めるかとは別問題です。
  - 旧サイトでは、この 2 種類の「補助的に見える論文」が、まだ十分に分け切れていませんでした。
- 根拠:
  - <https://doi.org/10.1038/s41597-019-0104-8> の Pernet et al. (2019)、<https://doi.org/10.1038/s41597-024-03559-8> の Burns et al. (2024)、<https://doi.org/10.1162/imag.a.136> の Kothe et al. (2025)、<https://doi.org/10.1088/1741-2552/aadea0> の Jayaram & Barachant (2018)、<https://proceedings.mlr.press/v37/blum15.html> の Blum & Hardt (2015)、<https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html> の Roelofs et al. (2019) は、再解析可能性、同期、leaderboard governance を押し上げます。
  - しかし、Gouwens / Hengen / Xu / Looser / Cahill / Williamson / Beiran & Litwin-Kumar は、未観測 state と omitted mechanism の一覧を押し上げます。
- 修正:
  - `dataset / benchmark / standard` は比較条件を整えるクラス、`mechanistic boundary / hidden-state evidence` は sufficiency ceiling を明示するクラス、として明確に分けました。

### 4. 旧 wiki は `evidence class` の読み方を持っていても、`demo と boundary の混同` まで前景化していませんでした

- 問題:
  - `wiki/paper-source-types-and-evidence-status.md` と `wiki/literature-and-evidence-reading.md` は、Badge / source_logged / curated の読み方としては十分に機能していました。
  - しかし、技術読者に最も重要な `demo のあとに boundary paper を挟む` という読み順が、まだ明示的ではありませんでした。
- 修正:
  - 2 つの wiki で `mechanistic boundary / hidden-state evidence` を evidence class に追加しました。
  - `論文集 → 文献地図` を読むとき、demo / validator / boundary を混同しない rule を明示しました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `maintenance-state / mechanistic boundary` を優先ルートへ昇格
  - `mechanistic boundary / hidden-state evidence` を evidence class 表へ追加
  - demo 論文のあとに boundary paper を併読する site rule を追加
- `research_harvest_50.md`
  - 技術・自然科学の優先ルートを `maintenance-state / mechanistic boundary` へ更新
  - evidence class 表へ mechanistic boundary 行を追加
  - 高 score 論文の直後に boundary paper を挟む運用 rule を追加
- `wiki/paper-source-types-and-evidence-status.md`
  - page highlights と evidence class 表へ mechanistic boundary を追加
  - `何ができたか` と `何がまだ足りないか` を別クラスとして固定
- `wiki/literature-and-evidence-reading.md`
  - demo と mechanistic boundary を混同しない読み方へ更新
  - 論文集 / 文献地図の役割差説明に、この新クラスを反映

## 外部依存で保留

- 論文カード単位での `mechanistic boundary / hidden-state evidence` タグ付与
  - 担当者: AI / maintainer
  - 前提条件: 各カードに付ける class 規約を安定化すること
  - 完了条件: `mind_uploading_papers.md` と `research_harvest_50.md` のカード群を class で絞り込めること

## 参考文献

- Gouwens NW, et al. Phenotypic variation of transcriptomic cell types in mouse motor cortex. *Nature*. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nature Neuroscience*. 2024.
  - https://doi.org/10.1038/s41593-023-01536-9
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nature Neuroscience*. 2024.
  - https://doi.org/10.1038/s41593-023-01558-3
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-024-08170-w
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Tang J, LeBel A, Jain S, Huth AG. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nature Neuroscience*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Ferrante O, Kamieniak I, et al. Towards decoding individual words from non-invasive brain recordings. *Nature Communications*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Communications*. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, et al. Direct validation of HD-EEG source imaging with simultaneous stereoelectroencephalography in focal epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS. *Scientific Data*. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Burns M, Nii L, Williams AN, et al. Motion-BIDS. *Scientific Data*. 2024.
  - https://doi.org/10.1038/s41597-024-03559-8
- Kothe C, Appelhoff S, Bullock T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
  - https://doi.org/10.1162/imag.a.136
- Jayaram V, Barachant A. MOABB. *Journal of Neural Engineering*. 2018.
  - https://doi.org/10.1088/1741-2552/aadea0
- Blum A, Hardt M. The Ladder: A Reliable Leaderboard for Machine Learning Competitions. *PMLR*. 2015.
  - https://proceedings.mlr.press/v37/blum15.html
- Roelofs R, Shankar V, Recht B, Fridovich-Keil S, Hardt M, Miller J. A Meta-Analysis of Overfitting in Machine Learning. *NeurIPS*. 2019.
  - https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html
