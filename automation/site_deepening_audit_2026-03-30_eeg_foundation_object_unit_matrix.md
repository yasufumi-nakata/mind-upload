# Site Deepening Audit (2026-03-30, EEG foundation benchmark object / unit matrix)

## 対象

- 主対象: `wiki/eeg-foundation-models.md`
- 副対象: `eeg_101.md`
- 参照整合性修正: `verification.md`

## 今回この箇所を選んだ理由

- 2026-03-30 時点で、サイトはすでに EEG foundation model の `source type`、`pretraining corpus`、`harmonization`、`adaptation regime`、`benchmark provenance` をかなり厳密に整理できておりました。
- しかし、なお 1 つ弱い圧縮が残っておりました。`benchmark object / supervision unit` は書かれていても、読者が
  - `何を予測しているのか`
  - `何を独立予測単位と数えるのか`
  - `何を hold-out unit と数えるのか`
  - `どの運用制約下で leaderboard が作られたのか`
  を benchmark 名だけで自動的に埋めてしまえる余地がありました。
- これは技術・自然科学の観点で弱点でございます。理由は、近年の EEG FM benchmark / competition / transfer 論文群そのものが、まさにこの 4 軸の不一致で比較解釈が揺れることを示しているからです。

## web確認対象

- `https://eeg2025.github.io/`
- `https://eeg2025.github.io/rules/`
- `https://eeg2025.github.io/submission/`
- `https://eeg2025.github.io/leaderboard/`
- `https://proceedings.mlr.press/v267/lee25a.html`
- `https://arxiv.org/abs/2601.17883`
- `https://arxiv.org/abs/2603.02268`
- `https://arxiv.org/abs/2510.21585`

## 根拠付き批判

### 1. benchmark object だけでは、score の意味を固定できませんでした

- 根拠:
  - EEG Challenge 2025 の公式 homepage は、Challenge 1 を `CCD trial から response time を回帰する課題`、Challenge 2 を `複数 paradigm の EEG から externalizing score を予測する課題` と分けております。
  - つまり、同じ competition 名の中で既に `trial-level regression` と `subject-level regression` が混在しております。
  - Lee et al. (2025) は memory tasks と sleep stage classification を同じ fine-tuning audit の中で比較しております。
- 批判:
  - したがって、`benchmark object / supervision unit` という語だけではまだ粗く、少なくとも `predicted object` と `independent prediction unit` を分けて front door で見せる必要がございました。

### 2. hold-out unit と grouped ancestry が、benchmark provenance に埋もれておりました

- 根拠:
  - Liu et al. (2026) は `leave-one-subject-out cross-subject generalization` と `within-subject few-shot calibration` を並列に評価しております。
  - Lahiri et al. (2026) は benchmark inconsistency が同一 dataset 上でも ranking を最大 24 percentage points 逆転させうると述べ、split construction, checkpoint selection, segment length, normalization など 6 要因を具体化しております。
  - EEG Challenge 2025 leaderboard は Challenge 2 sample が randomized されておらず、contiguous-trial same-subject structure を利用できたと organizers 自身が開示しております。
- 批判:
  - よって、`split rule was reported` だけでは不十分で、`何を独立 hold-out と見なしたのか`、`同一 raw recording / subject 由来 grouping が残っていないか` を別欄として見えるようにしないと、benchmark provenance の箱がまだ広すぎます。

### 3. leaderboard は model comparison だけでなく operations budget の比較でもあります

- 根拠:
  - EEG Challenge 2025 rules / submission は
    - inference-only code competition
    - no training allowed at submission
    - single GPU with 20 GB memory
    を明記しております。
- 批判:
  - したがって leaderboard は単なる model score 比較ではなく、`fixed operations budget 下の score` でもございます。
  - この条件を benchmark provenance の一部として曖昧に保持するより、`operations budget` として front door で独立に見せる方が、技術的に正確でございます。

### 4. 既存ページは benchmark name を過度に代表させておりました

- 根拠:
  - REVE は setup heterogeneity への positional encoding を前面に出しております。
  - Lee (2025) は fine-tuning / LoRA の効率性を示しております。
  - Liu (2026) は transfer regime comparison を前面に出しております。
  - PRISM (2026) は clinical mimicker diagnosis と benchmark inconsistency を前面に出しております。
- 批判:
  - これらは `EEG foundation model progress` という 1 行に圧縮できる種類の進歩ではありません。
  - model family, evaluation family, object family, and operations family が別々に動いているため、その split を明文化する必要がございました。

## 今回実行した変更

- `wiki/eeg-foundation-models.md`
  - `last_updated` を `2026-03-30` に更新
  - front matter に `benchmark object / independent prediction unit / grouped hold-out unit / inference-stage budget` を separate field とする rule を追加
  - note box を改稿し、EEG Challenge 1 / 2、Lee (2025)、Liu (2026)、Lahiri (2026) を使って
    - predicted object
    - independent prediction unit
    - grouped hold-out unit
    - operations budget
    を分離
  - 新規 section `2026-03-30 correction: benchmark object still needs an explicit matrix` を追加
  - G5 / G6 をそれぞれ `independent prediction unit` と `operations budget` を含む形へ改稿
  - Pretraining Card の benchmark rows を改稿し、grouped ancestry と inference-stage restrictions をより明示
  - Lee (2025) の reference を OpenReview ベースから PMLR proceedings ベースへ更新
- `eeg_101.md`
  - `last_updated` を `2026-03-30` に更新
  - page highlights / known points に foundation-model benchmark の 4 軸分離を追加
  - foundation-model benchmark note を改稿し、Challenge 1 / 2, Lee (2025), Liu (2026), Lahiri (2026) を用いて
    - predicted object
    - independent prediction unit
    - grouped hold-out unit
    - adaptation regime
    - operations budget
    を front door で見えるようにしました
- `verification.md`
  - Lee (2025) への参照を OpenReview から PMLR proceedings へ修正

## 今回止めた誤読

- `EEG foundation benchmark = one shared prediction object`
- `benchmark name が同じなら独立予測単位も同じ`
- `split rule があれば grouped ancestry 問題は十分に開示された`
- `leaderboard は model quality comparison だけであり operations budget は副次的`
- `cross-task transfer` と `subject-level clinical factor prediction` と `few-shot calibration` を one transfer story に圧縮してよい

## 検証結果

- `env VERIFY_GITHUB_WIKI_BUILD=1 ./scripts/verify_github_wiki_toolchain.sh`
  - syntax / boundary / ops-reference / noise-cleanup / export は pass
  - 最終 export validator は `uncommitted export drift` で停止
  - これは今回 source を更新した直後で export 差分が未コミットだったためであり、想定内でございました
- `env GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - pass
- `git diff --check`
  - pass
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - pass

## 外部依存タスク

- なし
  - 今回の変更は web 上の一次ソース確認、repo 内公開文面改稿、export/build 検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. EEG Challenge (2025). Official homepage.
   - https://eeg2025.github.io/
2. EEG Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
3. EEG Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
4. EEG Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
5. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *Proceedings of the 42nd International Conference on Machine Learning*. 2025.
   - https://proceedings.mlr.press/v267/lee25a.html
6. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
   - https://arxiv.org/abs/2601.17883
7. Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
   - https://arxiv.org/abs/2603.02268
8. El Ouahidi Y, Lys J, Tholke P, Farrugia N, Pasdeloup B, Gripon V, Jerbi K, Lioi G. REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. *arXiv*. 2025.
   - https://arxiv.org/abs/2510.21585
9. Xiong W, Li J, Li J, Zhu K. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
