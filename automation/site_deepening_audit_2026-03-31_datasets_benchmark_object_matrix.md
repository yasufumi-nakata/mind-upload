# 2026-03-31 site deepening audit: datasets benchmark-object matrix

## 対象として選んだ箇所

- `datasets.md`
- `wiki/l0-minimum-artifact-pack.md`

今回ここを優先した理由は、公開サイトの理論ページ群はすでにかなり厳密なのに対し、実務入口である `Datasets` 系は、読者が `dataset name`、`benchmark name`、`leaderboard result` をそのまま `one stable score object` と読みやすい位置にあるためです。ここが粗いと、どれだけ他ページで慎重な claim ceiling を定義していても、L0 / L1 の入口で `same score = same achievement` という誤読が復活します。

## 根拠付き批判

### 1. 現行ページは benchmark governance をかなり強く止めていましたが、`benchmark name = benchmark object` の誤読をまだ残していました

- 既存の `datasets.md` は、`rules snapshot`、`hidden grouping`、`extra-data policy`、`postmortem` をすでに要求していました。
- しかし、この書き方だけでは、読者がなお
  - `何を予測しているのか`
  - `何を独立 prediction unit とするのか`
  - `何を hold-out unit とするのか`
  - `target-session data を使ったか`
  - `どの operations budget で比較しているか`
  を benchmark 名の中へ吸収してしまいます。
- これは一次情報の読み方としてまだ弱いです。

### 2. EEG Challenge (2025) の公式情報自体が、「benchmark governance」と「benchmark object」が別だと示しています

- 公式 homepage は、`Challenge 1` を **response-time regression**、`Challenge 2` を **externalizing prediction across paradigms** として分けています。
- 公式 rules / submission page は、これに加えて
  - inference-only code submission
  - single-GPU 20 GB budget
  - additional pretraining disclosure
  を課しています。
- さらに公式 leaderboard は `Challenge 2 samples had not been randomized` と後から明かしており、contiguous-trial same-subject structure が benchmark meaning 自体を動かしうることを示しました。
- したがって、`benchmark object` と `benchmark governance` は別の disclosure field として固定する必要があります。

### 3. 同じ dataset でも evaluation family と adaptation regime で score object は変わります

- [Ma et al. (2022)](https://doi.org/10.1038/s41597-022-01647-1) は、同じ 5-session motor-imagery dataset から
  - within-session
  - cross-session
  - cross-session adaptation
  を分けて報告しています。
- この事実だけでも、dataset 名だけでは `fixed decoder` か `adapted decoder` か、また `pre-adaptation ceiling` がどこにあるかは決まりません。
- したがって `evaluation family` と `target-session usage` は dataset card 側で別明記されるべきです。

### 4. 最新 benchmark papers は、transfer regime と protocol inconsistency で ranking が反転すると示しています

- [Liu et al. (2026)](https://arxiv.org/abs/2601.17883) は、**12 open-source foundation models** を **13 datasets** にわたり比較し、`leave-one-subject-out cross-subject` と `within-subject few-shot calibration` を分けて評価しています。
- [Lahiri et al. (2026)](https://arxiv.org/abs/2603.02268) は、同一 dataset 上でも benchmark inconsistency が ranking を **up to 24 percentage points** 動かしうると示し、その source を split construction, checkpoint selection, segment length, normalization など **6 concrete sources** に分解しました。
- したがって practical page では `benchmark provenance` だけでなく、`object / unit / adaptation / budget matrix` を前面に置く方が科学的に正確です。

### 5. この修正は理論ページより `Datasets` と `L0 artifact pack` に入れるのが合理的でした

- 理論ページ群は already cautious です。
- しかし、実務入口で `benchmark object` の切り分けが弱いと、reader は最終的に `score interpretation` を practical route で粗く学んでしまいます。
- したがって今回は `Datasets` を front door、`L0 artifact pack` を submission schema として同期させる方が実効性が高いと判断しました。

## 今回実行した変更

### `datasets.md`

- front matter の `page_highlights` / `known_points` に、`benchmark name` が `predicted object / independent unit / grouped hold-out unit / adaptation regime / operations budget` を自動では固定しないことを追記しました。
- `2026-03-31 addendum: benchmark name is not yet the benchmark object` を追加しました。
- 同 addendum 直下に table を追加し、以下を別々の case として固定しました。
  - `EEG Challenge 1`
  - `EEG Challenge 2`
  - `Ma et al. (2022)` five-session motor-imagery dataset
  - `Liu et al. (2026)` foundation-model benchmark matrix
- `Site rule from this section` を更新し、dataset / benchmark card の必須項目に
  - `benchmark object + independent prediction unit`
  - `operations budget`
  を明示的に追加しました。
- その結果、score は `benchmark-object-unresolved` / `benchmark-governance-unresolved` として止められるようになりました。

### `wiki/l0-minimum-artifact-pack.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `page_highlights` / `known_points` に、benchmark 名の粗さと object / unit / budget disclosure の必要性を追記しました。
- `2026-03-31 addendum: benchmark name is not yet the benchmark object` を追加しました。
- item 7 を `predicted object` と `grouped hold-out unit` を含む定義へ更新しました。
- item 8 を `inference-stage restrictions / operations budget` を明示する定義へ更新しました。

## 今回止めた誤読

- `same benchmark name = same score object`
- `leaderboard governance を出した = prediction object も十分開示した`
- `cross-session dataset = fixed decoder durability benchmark`
- `few-shot calibration result = cross-subject portability result`
- `same dataset and same models = ranking is stable unless model changes`

## 検証

- `bundle exec jekyll build` を実行して、site build が通ることを確認します。
- `git diff --stat` と主要差分で、`Datasets` と `L0 artifact pack` の rule sync を確認します。

## external dependency tasks

- 今回の主作業に関して、外部依存で止めた項目はありません。

## 参考文献

1. [EEG Challenge (2025) official homepage](https://eeg2025.github.io/)
2. [EEG Challenge (2025) official rules](https://eeg2025.github.io/rules/)
3. [EEG Challenge (2025) official submission page](https://eeg2025.github.io/submission/)
4. [EEG Challenge (2025) official leaderboard / organizer postmortem](https://eeg2025.github.io/leaderboard/)
5. Xiong X, Jiang B, Jin Y, et al. EEG-FM-Bench: Benchmarking EEG Foundation Models with Comprehensive Evaluation Pipelines. arXiv. 2025. [https://arxiv.org/abs/2508.17742](https://arxiv.org/abs/2508.17742)
6. Liu D, Chen Y, Chen Z, et al. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. arXiv. 2026. [https://arxiv.org/abs/2601.17883](https://arxiv.org/abs/2601.17883)
7. Lahiri JB, Runwal P, Kulkarni A, et al. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. arXiv. 2026. [https://arxiv.org/abs/2603.02268](https://arxiv.org/abs/2603.02268)
8. Ma J, Yang B, Qiu W, et al. A large EEG dataset for studying cross-session variability in motor imagery brain-computer interface. *Scientific Data*. 2022. [https://doi.org/10.1038/s41597-022-01647-1](https://doi.org/10.1038/s41597-022-01647-1)
9. MOABB documentation. Mother of All BCI Benchmarks. [https://moabb.neurotechx.com/docs/index.html](https://moabb.neurotechx.com/docs/index.html)
10. Egger P, De Vos M, Suykens JAK, et al. Decoding movement-related cortical potentials over ten hours of continuous recording reveals adaptive BCI needs. *Scientific Reports*. 2024. [https://doi.org/10.1038/s41598-024-70609-x](https://doi.org/10.1038/s41598-024-70609-x)
11. Wilson GH, Stavisky SD, Willett FR, et al. Long-term unsupervised recalibration in intracortical BCI control. *Nature Biomedical Engineering*. 2025. [https://doi.org/10.1038/s41551-025-01536-z](https://doi.org/10.1038/s41551-025-01536-z)
12. Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLOS ONE*. 2015. [https://doi.org/10.1371/journal.pone.0118432](https://doi.org/10.1371/journal.pone.0118432)
13. Vallat R, Walker MP. An open-source, high-performance tool for automated sleep staging. *eLife*. 2021. [https://doi.org/10.7554/eLife.70092](https://doi.org/10.7554/eLife.70092)
