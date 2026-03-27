# Site Deepening Audit (2026-03-28, EEG foundation-model benchmark object / supervision-unit split)

## 対象

- 主対象: `wiki/eeg-foundation-models.md`
- 同期対象:
  - `github-wiki-export/eeg-foundation-models.md`
  - `verification.md`
  - `eeg_101.md`
- web確認対象:
  - `https://eeg2025.github.io/data/`
  - `https://eeg2025.github.io/submission/`
  - `https://eeg2025.github.io/leaderboard/`
  - `https://openreview.net/forum?id=J5SbLoq7Uv`
  - `https://arxiv.org/abs/2508.17742`
  - `https://arxiv.org/abs/2601.17883`
  - `https://arxiv.org/abs/2603.02268`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `EEG foundation models` 系の公開ページは、2026-03-28 時点で
  - source type
  - corpus overlap
  - setup diversity
  - harmonization
  - adaptation regime
  - benchmark provenance
  - shortcut resistance
  をかなり強く分離していました。
- しかしなお一つ、重要な混線源が残っていました。`benchmark name` や `cross-task transfer` という言い方だけだと、
  - per-window / per-trial decode
  - event detection
  - sequence labeling
  - subject-level regression / diagnosis
  を同じ `generalization advance` に圧縮して読めてしまいます。
- これは site-wide に危険です。foundation model の話題は「多タスクで強い」ほど強い結論に読まれやすい一方、実際の supervision unit と metric family が違えば、同じ frontier score ではありません。

## 根拠付き批判

### 1. 公式 challenge 自体が、単一の prediction object を固定していません

- 根拠:
  - [EEG Challenge data page](https://eeg2025.github.io/data/) は、competition dataset が `over 3,000 participants across six distinct cognitive tasks` であることを明記しています。
  - 同ページは、各 participant に `four psychopathology dimensions` が付与されることも明記しています。
  - [EEG Challenge leaderboard](https://eeg2025.github.io/leaderboard/) は、Challenge 2 の non-randomized contiguous-trial 問題を公開し、Challenge 1 と 2 を分離して表彰しています。
- 批判:
  - これは、同じ official benchmark family の中でも、trial-level task prediction と subject-level target prediction が混在しうることを意味します。
  - したがって `EEG Challenge で強い` だけでは、何を1予測単位として勝ったのかが分かりません。
  - `benchmark provenance` だけでなく、`benchmark object / supervision unit` を独立項目にしないと、site rule としてまだ粗いままでした。

### 2. accepted foundation-model fine-tuning papers ですら、task family を跨いでいます

- 根拠:
  - [Lee et al. (2025)](https://openreview.net/forum?id=J5SbLoq7Uv) は、`multiple BCI benchmark tasks, including memory tasks and sleep stage classification` にわたる systematic fine-tuning を行っています。
  - 同論文は、large brainwave foundation models が従来 deep baselines を `0.5%` 程度しか上回らない一方、LoRA による parameter-efficient adaptation が有効であることも示しています。
- 批判:
  - memory task と sleep stage classification は、label provenance, temporal granularity, metric semantics, independent prediction unit が違います。
  - したがって `fine-tuning で複数 task に効いた` を、そのまま `one general transferable representation` と書くのは過剰です。

### 3. 最新 benchmark 論文も、object-family をまたぐ比較の不安定さを示しています

- 根拠:
  - [Xiong et al. (2025)](https://arxiv.org/abs/2508.17742) は、`14 datasets across 10 paradigms` を統合し、現状の比較が fragmented で unreliable だと述べています。
  - [Liu et al. (2026)](https://arxiv.org/abs/2601.17883) は、`12 open-source foundation models` と specialist baselines を `13 datasets` で比較し、linear probing insufficiency と ranking instability を報告しています。
  - [Lahiri et al. (2026)](https://arxiv.org/abs/2603.02268) は、clinical differential diagnosis という subject-level object で、narrow-source と diverse-source pretraining の優位が regime により入れ替わることを示しています。
- 批判:
  - これらは benchmark name や dataset count を増やしても、prediction object の違いを消せないことを示しています。
  - `many datasets / many paradigms` は benchmark-object split を省略する理由ではなく、むしろ必要性を強めます。

## 今回実行した変更

- `wiki/eeg-foundation-models.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `page_intro` / `page_highlights` / `known_points` / `unknown_points` を、`benchmark object / supervision unit` の独立軸に同期しました。
  - `Benchmark object and supervision unit are not one box either` note を追加しました。
  - `The 9 gates` を `The 10 gates` に更新し、`G5: benchmark object / supervision unit` を追加しました。
  - `Pretraining Card` に `Benchmark Object / Supervision Unit` 行を追加しました。
  - `Operating rules` に、window classification / sequence labeling / subject-level regression を同列 frontier score に圧縮しない site rule を追加しました。
  - 参考文献に `EEG Challenge (2025). Data.` を追加しました。

- `github-wiki-export/eeg-foundation-models.md`
  - 公開ページと同じ rule を GitHub Wiki 側へ同期しました。

- `verification.md`
  - `page_highlights` の Pretraining Card 説明へ `benchmark object / supervision unit` を追加しました。
  - Pretraining Card 導入段落に、challenge data page が task-level と subject-level object を混在させることを追記しました。
  - Pretraining Card table に `benchmark object / supervision unit` 行を追加しました。
  - `Minimum operating rules` と `How this differs from the existing cards` を同期しました。
  - 参考文献に `EEG Challenge (2025). Data.` を追加しました。

- `eeg_101.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - foundation-model 関連 highlight / known point を `benchmark object / supervision unit` まで含む形に更新しました。
  - `Foundation-model benchmarks are not all scoring the same object` note を追加しました。
  - 参考文献に `EEG Challenge (2025), data` を追加しました。

## 今回の修正で止めた誤読

- `cross-task transfer` = どの task family でも同じ意味の generalization
- `EEG Challenge で強い` = one benchmark object で portable に強い
- `memory task と sleep staging の両方で改善` = one shared downstream object が改善
- `many datasets / many paradigms` = benchmark object の違いはもう重要ではない
- `foundation model benchmark win` = per-window decode, event detection, subject regression をまとめて frontier evidence として読める

## 外部依存タスク

- なし
  - 今回の変更は repo 内本文、監査記録、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. EEG Challenge (2025). Data.
   - https://eeg2025.github.io/data/
2. EEG Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
3. EEG Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
4. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML 2025 poster*.
   - https://openreview.net/forum?id=J5SbLoq7Uv
5. Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
6. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
   - https://arxiv.org/abs/2601.17883
7. Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
   - https://arxiv.org/abs/2603.02268
