# Site Deepening Audit (2026-03-21, Multimodal Shared-vs-Specific Signal Gate)

## 対象

- 主対象: `wiki/multimodal-integration-basics.md`
- 運用ルール反映: `verification.md`
- 入口反映: `wbe_101.md`, `index.md`
- 参照整合修正: `wiki/baselines-prereg-and-model-cards.md`, `wiki/measurement-stack-and-claim-ceiling.md`

## 今回の選定理由

- サイトはすでに `Fusion Card` を導入しており、`multimodal = 自動的に強い` という誤読はかなり止められていました。
- しかし 2026-03-21 時点でも、`共有タイムスタンプを持った`、`共通 cross-modal component が見えた`、`同じ生物学的状態変数を捉えた` の 3 段階が front door で十分には分離されていませんでした。
- このままでは、技術・自然科学の観点で読者が `simultaneous`, `coupled`, `shared factor` を見ただけで、融合がターゲット変数の特定まで進んだと誤読しやすい状態でした。

## 根拠付き批判

### 1. 同期と biological equivalence は同じではありません

- 問題:
  - 既存サイトは `same-session` や `simultaneous` の危険性を指摘していましたが、なお `共有クロック` と `共有状態変数` の差が実務ルールとしては弱めでした。
- 根拠:
  - Kothe et al. (2025) は LSL を同期インフラとして整理していますが、これは stream alignment の話であり、device-side delay truth や biological equivalence の証明ではありません。
  - Wei et al. (2020) は EEG-fMRI fusion を model-conditioned inference として扱っており、融合自体が latent variable の一意性を保証するわけではありません。
- 批判:
  - したがって `同期できた` ことを `同じものを測った` ことへ昇格させるのは不適切です。

### 2. 共通成分が見えても、modality-specific residual は残ります

- 問題:
  - 既存本文は `common and divergent structure` を言及していましたが、論文読解時に `主張が shared component に乗っているのか、residual 側に残っているのか` を開示する site rule が明示的ではありませんでした。
- 根拠:
  - Vafaii et al. (2024) は multimodal spontaneous activity から common pattern と divergent pattern の両方を示しました。
  - Chen et al. (2025) は simultaneous EEG-PET-MRI で coupled global dynamics を示す一方、network-specific structure も残ることを示しました。
- 批判:
  - よって `共通因子がある` からといって、`対象状態変数が modality 間で一意に同定された` とは読めません。
  - この差を card field にしない限り、Fusion Card はまだ弱いです。

### 3. 共有成分は target neural variable ではなく shared physiology かもしれません

- 問題:
  - 既存サイトは vascular-state / CVR をかなり丁寧に分離していましたが、`cross-modal common factor` 自体が autonomic / arousal physiology を強く含みうる点は front door でまだ弱めでした。
- 根拠:
  - Bolt et al. (2025) は global fMRI signal の低周波変動が EEG と複数の autonomic 指標に結びつく distributed arousal response を示しました。
  - Özbay et al. (2019) は EEG で捉えた arousal event と sympathetic activity が fMRI signal に寄与することを示しました。
- 批判:
  - したがって `shared low-frequency factor` は、即 `shared neural state` ではありません。
  - `shared neural candidate` / `physiology-linked global factor` / `mixed unresolved factor` を分けずに multimodal を強く読むのは不適切です。

### 4. 参照整合にも修正が必要でした

- 問題:
  - Chen et al. (2025) の参考文献表記が一部ページで誤って `Chen, Z.` になっていました。
- 根拠:
  - 一次ソースの著者表記は `Chen, J. E.` です。
- 批判:
  - 文献整合が崩れていると site-wide の批判の信頼性自体が落ちるため、今回の主題と合わせて是正が必要でした。

## 今回実行した変更

- `wiki/multimodal-integration-basics.md`
  - `last_updated` を `2026-03-21` に更新しました。
  - `7 audit gates` を `8 audit gates` に改め、`Shared-vs-specific component gate` を追加しました。
  - `shared timestamps` / `shared component` / `target biological variable` を分ける note を追加しました。
  - Bolt / Özbay を加え、`shared factor` が autonomic / arousal physiology を含みうる点を前面化しました。
  - tri-modal EEG-PET-MRI の節を、`coupled global dynamics` と `target-variable specificity` を分ける方向に更新しました。
- `verification.md`
  - `Fusion Card` に `Shared-vs-specific component disclosure` 行を追加しました。
  - `common factor` だけでは one shared biological state variable と読まない stop rule を明文化しました。
  - Bolt / Özbay の references を追加しました。
- `wbe_101.md`
  - entry-level note と highlights を更新し、same-session multimodal evidence でも `shared factor ≠ solved state variable` を front door で読めるようにしました。
  - `Fusion Card` の説明に `shared-vs-specific component disclosure` を組み込みました。
  - Bolt / Özbay を references に追加しました。
- `index.md`
  - 入口に `shared multimodal factor` の過大解釈を止める note を追加しました。
- 参照整合修正
  - `verification.md`, `wbe_101.md`, `wiki/baselines-prereg-and-model-cards.md`, `wiki/measurement-stack-and-claim-ceiling.md` の Chen et al. (2025) 参考文献表記を一次ソースに合わせて訂正しました。

## 外部依存で保留

- same-subject / same-session / same-perturbation で shared-vs-specific decomposition を externally calibrate できる benchmark package
  - 担当者: multimodal 計測系研究者 / benchmark 設計者 / maintainer
  - 前提条件: EEG, fMRI, PET, autonomic physiology を同一被験者・同一 regime で取得し、shared component と physiology-linked global factor を識別できる公開データ
  - 完了条件: `shared neural candidate` / `physiology-linked factor` / `modality-specific residual` を card-level に比較できる公開 benchmark が整備されること

## 参考文献

1. Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025;3:IMAG.a.136.
   - https://doi.org/10.1162/IMAG.a.136
2. Wei H, Jafarian A, Zeidman P, Litvak V, Razi A, Garrido M, Friston K, Daunizeau J. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020;211:116595.
   - https://doi.org/10.1016/j.neuroimage.2020.116595
3. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024;15:229.
   - https://doi.org/10.1038/s41467-023-44363-z
4. Chen JE, Lewis LD, Coursey SE, Catana C, Polimeni JR, Fan J, Droppa KS, Patel R, Wey H-Y, Chang C, Manoach DS, Price JC, Sander CY, Rosen BR. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025;16:8887.
   - https://doi.org/10.1038/s41467-025-64414-x
5. Bolt TS, van den Brink RL, Song C, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025;28:1266-1278.
   - https://doi.org/10.1038/s41593-025-01945-y
6. Özbay PS, Chang C, Picchioni D, et al. Sympathetic activity contributes to the fMRI signal. *Communications Biology*. 2019;2:421.
   - https://doi.org/10.1038/s42003-019-0659-0
