# Site Deepening Audit (2026-03-26, Standards / Repositories / Validators / Benchmarks Page)

## 対象

- 主対象: `wiki/standards-repositories-validators-and-benchmarks.md`

## 今回の選定理由

- 2026-03-26 時点で、`datasets.md`、`verification.md`、`wiki/baselines-prereg-and-model-cards.md`、`wiki/eeg-foundation-models.md` はすでに `benchmark provenance` を強く扱っていました。
- しかし、実務導線の根元にある `wiki/standards-repositories-validators-and-benchmarks.md` だけは、なお `benchmark = harness name + evaluation family` に近い整理で止まっていました。
- そのため、サイト内部で `MOABB のような harness` と `official challenge rules / submission constraints / leaderboard postmortem` の意味づけがずれており、読者が `benchmark 名を知っている = score の意味も確定している` と過読しうる状態でした。
- これは技術・自然科学の観点で弱点です。理由は、比較結果の意味はデータだけでなく、split construction、hidden grouping、extra-data policy、execution constraint、postmortem correction に依存するからです。

## 根拠付き批判

### 1. 旧ページは `benchmark harness` と `benchmark provenance / governance` を分けていませんでした

- 問題:
  - 旧ページは `BIDS / OpenNeuro / Validator / MOABB` の役割差は整理していました。
  - しかし、`MOABB のような harness が評価 family を固定すること` と、`challenge 運用が score の意味をさらに固定すること` を別に書いていませんでした。
- 根拠:
  - [MOABB docs](https://moabb.neurotechx.com/docs/index.html) は within-session / cross-session / cross-subject などの evaluation family を前面に出しています。
  - 一方、[EEG Challenge 2025 homepage](https://eeg2025.github.io/) は proposal preprint が execution 中に outdated になり、website を current source とみなすべきだと明記しています。
  - [EEG Challenge 2025 rules](https://eeg2025.github.io/rules/) は filter / downsample route、additional data disclosure、pretrained-model disclosure、single-GPU 20 GB inference budget を固定しています。
  - [EEG Challenge 2025 submission](https://eeg2025.github.io/submission/) は inference-only code submission であることを固定しています。
  - [EEG Challenge 2025 leaderboard](https://eeg2025.github.io/leaderboard/) は Challenge 2 の sample randomization error を公開し、最終的な読み方を修正しています。
- 批判:
  - したがって `benchmark = MOABB` や `benchmark = challenge 名` という整理は弱すぎます。
  - 実際の score の意味は、harness 名だけではなく、execution-phase の governance document 群で決まります。

### 2. 旧ページの ID 設計では benchmark meaning を固定しきれませんでした

- 問題:
  - 旧ページの `Minimum 4 IDs` は Input / Schema / Evaluation / Pipeline で終わっていました。
  - しかしこれだけでは、同じ benchmark 名でも `どの rules snapshot で、どの extra-data policy で、どの postmortem を含むか` を固定できませんでした。
- 根拠:
  - [OpenNeuro user guide](https://docs.openneuro.org/user_guide.html) は dataset snapshot と git hash を dataset page で確認できると明記しています。
  - [PhysioNet resources guidance](https://physionet.org/about/content/) は versioned resource / citation culture を前提にしています。
  - [Liu et al. (2026)](https://doi.org/10.48550/arXiv.2601.17883) は 12 open-source EEG foundation models と 13 datasets を比較し、protocol choice により transfer の読みが動くことを示しました。
- 批判:
  - 入力 version だけ固定しても benchmark governance が未固定なら、再現されるのは同じ score object ではなく、ただ同じ raw data を使った run にすぎません。
  - よって `Benchmark Governance ID` を独立に要求する必要がありました。

### 3. 旧ページは official postmortem を administrative footnote と読める構造でした

- 問題:
  - 旧版は `benchmark` を静的な comparison rule として説明しており、後から出る organizer correction や leaderboard note の重要性を明示していませんでした。
- 根拠:
  - [Xiong et al. (2025/2026)](https://doi.org/10.48550/arXiv.2508.17742) は EEG foundation model 比較で evaluation protocol inconsistency が信頼できる cross-model comparison を壊すと論じています。
  - [EEG Challenge 2025 leaderboard](https://eeg2025.github.io/leaderboard/) は Challenge 2 split の問題を明示し、賞の扱いを修正しています。
- 批判:
  - したがって organizer postmortem は脚注ではなく benchmark meaning そのものの更新です。
  - この点を practical wiki の入口ページで固定しないと、他ページの benchmark governance ルールと噛み合いません。

## 今回実行した変更

- `wiki/standards-repositories-validators-and-benchmarks.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - front matter を更新し、`benchmark provenance / governance` を page intro / highlights / known points に追加しました。
  - 冒頭に `2026-03-26 correction: benchmark provenance is part of the benchmark` note を新設しました。
  - 用語表に `benchmark provenance / governance` を追加しました。
  - `4 labels -> 8 layers` に更新し、`Benchmark provenance / governance` を独立 layer として追加しました。
  - `Benchmark provenance is part of reproducibility` の新規 section を追加し、
    - current rule snapshot
    - split / randomization / hidden grouping
    - extra-data / pretrained-model policy
    - inference-stage execution constraints
    - postmortem / correction status
    を benchmark object の構成要素として table 化しました。
  - EEG 実務例に `Freeze benchmark provenance` を追加しました。
  - `Common confusion` に
    - benchmark name alone
    - challenge proposal paper alone
    を追加しました。
  - `Minimum 5 IDs` に改め、`Benchmark Governance ID` を追加しました。
  - `7 questions when reading strong arguments` に改め、`What benchmark provenance was in force?` を追加しました。
  - 参考文献に EEG Challenge 2025 の homepage / rules / submission / leaderboard と Xiong / Liu を追加しました。

## 外部依存で保留

- なし
  - 今回の変更は公開本文と export 更新で完結します。

## 参考文献

1. EEG Challenge (2025). Homepage.
   - https://eeg2025.github.io/
2. EEG Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
3. EEG Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
4. EEG Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
5. Jayaram V, Barachant A. MOABB: trustworthy algorithm benchmarking for BCIs. *J Neural Eng*. 2018.
   - https://doi.org/10.1088/1741-2552/aadea0
6. Xiong Z, et al. EEG-FM-Bench. arXiv. 2025/2026.
   - https://doi.org/10.48550/arXiv.2508.17742
7. Liu D, Chen Y, Chen Z, et al. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. arXiv. 2026.
   - https://doi.org/10.48550/arXiv.2601.17883
8. OpenNeuro documentation: User Guide.
   - https://docs.openneuro.org/user_guide.html
9. PhysioNet: Resources.
   - https://physionet.org/about/content/
