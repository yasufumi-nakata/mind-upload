# Site Deepening Audit (2026-03-26, EEG to L0 / Benchmark Object and Temporal Route)

## 対象

- 主対象: `wiki/eeg-to-l0-route.md`

## 今回の選定理由

- 2026-03-26 時点で、`dataset-splits-and-leakage`、`state-trait-and-drift`、`event-sync-and-measurement-logs`、`baselines-prereg-and-model-cards` などの補助ページはかなり深くなっていました。
- その一方で、`wiki/eeg-to-l0-route.md` は入口ページとして重要であるにもかかわらず、`dataset selection`、`split hygiene`、`temporal validity`、`event semantics`、`artifact lineage` をまだ粗く一列に流していました。
- これは技術・自然科学の観点で弱点でございます。なぜなら、現行の一次文献と公式仕様が支持しているのは、`何を測ったか`、`何を比較したか`、`どの時間範囲に一般化できるか`、`どの観測ログが残っているか`、`どの raw からどの derivative が生成されたか` を分けて監査することだからです。

## 主要な批判点

### 1. 旧 route は `dataset choice` を benchmark object ではなく、ほぼ `ファイル選択` として扱っていました

- 問題:
  - 旧版は `どの public data を選ぶか` を主軸にしていましたが、`task`、`target`、`metric bundle`、`extra-data policy`、`benchmark version`、`organizer postmortem` まで含めた benchmark object を前面化できていませんでした。
  - そのため、同じ dataset 名の下で benchmark の意味が変わっても、入口ページだけ読むと `同じ benchmark の改善` に見えてしまう余地がありました。
- 根拠:
  - Saito & Rehmsmeier (2015) は、評価指標の選び方だけで二値分類の読み方が変わることを示しました。
  - EEG Challenge (2025) 公式サイト・rules・leaderboard は、実行中のルール更新や最終 postmortem により benchmark の意味が動くことを示しています。
- 修正:
  - `wiki/eeg-to-l0-route.md` の step 2 を `Datasets` 単独ではなく、`Datasets + Baseline / Benchmark / Pre-registration / Model Card` の組として再設計しました。
  - `dataset/version, task, target, hold-out unit, metric bundle, benchmark-governance status` を benchmark object の必須要素として明示しました。

### 2. 旧 route は `clean split` と `temporal validity` を分け切れていませんでした

- 問題:
  - 旧版では split を決めれば次へ進めるように読めましたが、`same-session`、`same-day`、`cross-day`、`fixed decoder`、`recalibrated decoder` の違いが route の入口で固定されていませんでした。
  - これでは、同じ subject/session split を守っていても、同日内の短時間成功を跨日耐久性へ昇格させる危険が残ります。
- 根拠:
  - Chaibub Neto et al. (2019)、Melnik et al. (2017)、Xu et al. (2020)、Di et al. (2021) は、subject/session や acquisition-distribution の構造が高い予測性を持ちうることを示しました。
  - Egger et al. (2024) は、約 10 時間スケールでも EEG decode 条件が変動し、adaptive decoder が必要になることを示しました。
- 修正:
  - step 3 を `dataset-splits-and-leakage + state-trait-and-drift` の組に変更しました。
  - `split manifest` と `temporal-validity note` を別 artifact として導入し、`same-session / same-day / cross-day / longer-horizon` と `fixed / recalibrated` を先に固定する形へ改めました。

### 3. 旧 route は `events in BIDS` を `semantics and timing solved` のように読ませる余地がありました

- 問題:
  - 旧版では event sync を 1 step で扱っていましたが、`time anchor`、`event semantics`、`clock alignment`、`report-derived label provenance` の違いが十分に前景化されていませんでした。
  - そのため、`events.tsv がある`、`LSL を使った`、`label がある` が同じ強さの証拠に見えてしまいます。
- 根拠:
  - BIDS specification は event と derivative provenance の役割を分けています。
  - Hermes et al. (2025) は EEG annotation の機械可読 semantics を強化しています。
  - Kothe et al. (2025) は、LSL がネットワーク同期に有効でも device-side delay を自動で測るわけではないと明示しています。
- 修正:
  - step 4 を `observation contract` として再定義し、`event times / semantics / label provenance / clock domain / delay-jitter-drift notes` を列挙しました。
  - 本文中でも `time anchor`、`event semantics`、`clock/synchronization audit` を別の層として明示しました。

### 4. 旧 route は `pipeline ran` と `L0 complete` を近接させすぎていました

- 問題:
  - 旧版の artifact pack への接続はありましたが、`raw identity`、`derivative identity`、`run identity`、`failure registry`、`stopped claim` が入口で同格に並んでいませんでした。
  - これでは、score だけ出せば route を最後まで通過したように読めます。
- 根拠:
  - Gorgolewski et al. (2016)、Pernet et al. (2019)、Pernet et al. (2020)、BIDS specification は、raw / derivative / provenance を分けて残す方向を支持しています。
  - ただし `split manifest` や `stopped claim` は単一仕様の mandatory key ではありません。これは current standards と benchmark practice を踏まえた本サイトの **運用推論** でございます。
- 修正:
  - step 5 とその後続節で `benchmark object`、`split manifest`、`temporal-validity note`、`observation log`、`derivative lineage`、`stopped claim` を最小 artifact bundle として明示しました。
  - `Five accidents this route now tries to stop early` 節を追加し、入口で止めるべき誤読を明文化しました。

## 今回実行した変更

- `wiki/eeg-to-l0-route.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter を全面更新し、route の焦点を `benchmark object / temporal regime / observation contract / lineage` に変更
  - `Six gates from EEG to L0` を新設
  - `Why these gates must stay separate` を新設
  - `Minimum artifact bundle before one score matters` を新設
  - `Five accidents this route now tries to stop early` を新設
  - 参考文献を新設し、一次文献・公式仕様・公式 benchmark サイトを追加

## 外部依存で保留

- なし
  - 今回の作業は、公開本文の改稿・参考文献の追加・後続の export/build 検証で完結可能でございます。

## 参考文献

- Gorgolewski KJ, Auer T, Calhoun VD, et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. *Sci Data*. 2016.
  - https://doi.org/10.1038/sdata.2016.44
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Sci Data*. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. *Nat Neurosci*. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Brain Imaging Data Structure (stable), dataset description / derived dataset and pipeline description.
  - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html
- Hermes D, Bigdely-Shamlo N, Niso G, et al. HED library schema for EEG data annotation. *Sci Data*. 2025.
  - https://doi.org/10.1038/s41597-025-05791-2
- Kothe C, Grivich M, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neurosci*. 2025.
  - https://doi.org/10.1162/IMAG.a.136
- Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digit Med*. 2019.
  - https://doi.org/10.1038/s41746-019-0178-x
- Melnik A, Legkov P, Izdebski K, et al. Systems, subjects, sessions: to what extent do these factors influence EEG data? *Front Hum Neurosci*. 2017.
  - https://doi.org/10.3389/fnhum.2017.00150
- Xu M, Han J, Wang Y, et al. Cross-dataset variability problem in EEG decoding with deep learning. *Front Hum Neurosci*. 2020.
  - https://doi.org/10.3389/fnhum.2020.00103
- Di M, Han J, Wang Y, et al. The time-robustness analysis of individual identification based on resting-state EEG. *Front Hum Neurosci*. 2021.
  - https://doi.org/10.3389/fnhum.2021.672946
- Egger M, Haden B, Bernarding J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Sci Rep*. 2024.
  - https://doi.org/10.1038/s41598-024-70609-x
- Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLoS One*. 2015.
  - https://doi.org/10.1371/journal.pone.0118432
- EEG Challenge (2025) official website / rules / leaderboard.
  - https://eeg2025.github.io/
  - https://eeg2025.github.io/rules/
  - https://eeg2025.github.io/leaderboard/
