# Site Deepening Audit (2026-03-28, L0 artifact pack benchmark-meaning / temporal-validity sync)

## 対象

- 主対象: `wiki/l0-minimum-artifact-pack.md`
- 同期対象:
  - `github-wiki-export/l0-minimum-artifact-pack.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html`
- `https://eeg2025.github.io/`
- `https://eeg2025.github.io/rules/`
- `https://eeg2025.github.io/leaderboard/`
- `https://eeg2025.github.io/faq/`
- `https://doi.org/10.1038/s41598-024-70609-x`
- `https://doi.org/10.1038/s41551-025-01536-z`
- `https://doi.org/10.1371/journal.pone.0118432`
- `https://doi.org/10.7554/eLife.70092`

## 今回この箇所を選んだ理由

- `wiki/l0-minimum-artifact-pack.md` は practical front door であり、初学者が「L0 の最小十分条件」をここで覚えます。
- しかし 2026-03-28 時点の本文は、`event fidelity`、`label provenance`、`acquisition-distribution summary`、`derivative lineage` まではかなり改善されていた一方で、なお
  - `benchmark object / metric bundle`
  - `benchmark provenance / governance`
  - `temporal-validity addendum`
  を pack 本体に固定していませんでした。
- これは site-wide の現行 rule と不整合でございます。`datasets.md` や `verification.md` がすでに止めている誤読を、この補助ページだけが再導入しうるためでございます。

## 根拠付き批判

### 1. `BIDS + split + score` だけでは、score object を固定できません

- [BIDS Events specification](https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html) は、`onset` が「対応 task data file の first stored data point からの時刻」であることを明示しており、BIDS が timing/annotation の traceability を与えても、それだけで benchmark meaning 全体を固定するわけではないことを示します。
- さらに [EEG Challenge (2025) homepage](https://eeg2025.github.io/) は、同じ official benchmark family の中で
  - Challenge 1: `response time` の regression
  - Challenge 2: `psychopathology scores` の subject-level regression
  を並置しています。

批判:

- したがって `benchmark name` や `EEG decoding score` だけでは、何を 1 prediction unit として学習・評価したのかが確定しません。
- `L0 artifact pack` が `benchmark object + metric bundle` を必須化しないのは、いまの site rule として弱すぎました。

### 2. official challenge / leaderboard の意味は execution 中に動きます

- [EEG Challenge (2025) homepage](https://eeg2025.github.io/) は、challenge preprint が execution phase の変更により outdated になり、website と Starter Kit を current source として扱うべきと明記しています。
- [EEG Challenge FAQ](https://eeg2025.github.io/faq/) は、
  - single GPU `20 GB` memory
  - external dataset disclosure
  - pretrained-model and fine-tuning disclosure
  を current operational rule として明示しています。
- [EEG Challenge leaderboard](https://eeg2025.github.io/leaderboard/) は、Challenge 2 の sample-randomization 問題を開示し、評価の読み方を修正しています。

批判:

- したがって leaderboard や challenge name を artifact に載せるだけでは不十分です。
- `current rules snapshot`、`extra-data policy`、`inference-stage restriction`、`postmortem / correction status` を pack 本体に入れない限り、第三者は同じ benchmark meaning を再構成できません。

### 3. `cross-session` や `adaptation` は、それだけでは temporal validity ではありません

- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) は、`10-hour` EEG recording で decoder-relevant dynamics が動き、adaptive decoder の必要性が生じることを示しました。
- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は、cursor iBCI で unsupervised recalibration を反復しつつ `one month` 規模の運用を報告しており、長期安定性と recalibration burden を別に読む必要を示しています。

批判:

- したがって `cross-session`, `adaptation`, `longitudinal` という family label だけでは、何が固定され、どれだけ再較正が必要で、どこまで transfer できたかが分かりません。
- `state annotation`、`fixed decoder interval`、`recalibration amount / timing`、`transfer ceiling` を含む `Temporal-Validity addendum` を pack に入れないのは、実務上の stop line として不十分でした。

### 4. metric semantics は score の脚注ではなく benchmark の一部です

- [Saito & Rehmsmeier (2015)](https://doi.org/10.1371/journal.pone.0118432) は、imbalanced data では ROC / accuracy が performance difference を隠しうる一方、precision-recall がそれを可視化しうることを示しました。
- [Vallat & Walker (2021)](https://doi.org/10.7554/eLife.70092) は、自動 sleep staging で N1 が最も agreement / confidence の低い stage であることを示しており、pooled score だけでは stage-specific weakness が隠れることを示します。

批判:

- したがって `accuracy is there` を L0 pack の十分条件に近く読ませるのは誤りです。
- `task-matched metric bundle` を必須化しない限り、同じ numeric score を task 間で同列に読んでしまう危険が残ります。

## 今回実行した変更

- `wiki/l0-minimum-artifact-pack.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `description` / `subtitle` / `page_intro` / `page_highlights` / `known_points` / `unknown_points` を、現行 site-wide rule に同期しました。
  - `2026-03-28 addendum: the 11-point pack was still under-specified` を追加しました。
  - `Minimum 11 items` を `Minimum 14 items` に更新し、
    - `Benchmark object + metric bundle`
    - `Benchmark provenance + governance`
    - `Temporal-Validity addendum`
    を pack 本体へ追加しました。
  - `Why the old 8-point pack is now too weak` を拡張し、
    - benchmark object
    - governance snapshot
    - temporal-validity
    を独立 failure mode として追加しました。
  - `Five bundles` の evaluation bundle を更新し、prediction object / metric bundle / current benchmark rules / temporal scope を明記しました。
  - `Common omissions` と `A stricter L0 completion check` を更新し、
    - leaderboard / challenge governance
    - cross-session / adaptation temporal scope
    を front-door で確認できるようにしました。
  - references に official challenge docs と temporal-validity / metric-semantics 文献を追加しました。

- `github-wiki-export/l0-minimum-artifact-pack.md`
  - 公開ページと同じ stricter L0 pack rule を GitHub Wiki 側へ同期しました。

## 今回止めた誤読

- `BIDS + split + score` があれば L0 の再現性要件はほぼ満たした
- `EEG Challenge` や leaderboard 名さえ書けば benchmark meaning は固定できた
- `cross-session` や `adaptation` は、そのまま durability claim に読める
- `accuracy` や 1 つの pooled score を task-matched metric bundle の代わりに使える
- `same benchmark family` の中で prediction object が違っても、同じ generalization advance としてまとめてよい

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、GitHub Wiki export、監査記録、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Brain Imaging Data Structure. Events.
   - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html
2. EEG Challenge (2025). Homepage.
   - https://eeg2025.github.io/
3. EEG Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
4. EEG Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
5. EEG Challenge (2025). FAQ.
   - https://eeg2025.github.io/faq/
6. Egger J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
7. Wilson GH, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
8. Saito T, Rehmsmeier M. The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets. *PLOS One*. 2015.
   - https://doi.org/10.1371/journal.pone.0118432
9. Vallat R, Walker MP. An open-source, high-performance tool for automated sleep staging. *eLife*. 2021.
   - https://doi.org/10.7554/eLife.70092
