# Site Deepening Audit (2026-03-25, datasets benchmark governance)

## 対象

- 主対象: `datasets.md`
- 範囲: 技術・自然科学のみ

## 今回この箇所を選んだ理由

- `eeg_101.md`、`wiki/eeg-foundation-models.md`、`verification.md` では、すでに
  - `foundation-model headline != solved generalization`
  - `benchmark provenance is part of the evidence`
  - `official challenge postmortem can change what the score means`
  という規律が強化されていました。
- しかし `datasets.md` は実務入口であるにもかかわらず、主に
  - split / leakage
  - harmonization
  - temporal validity
  - inverse-problem validation class
  に重心があり、`benchmark governance / hidden grouping / inference-stage budget / organizer postmortem` が独立 stop line としてはまだ弱い状態でした。
- これは技術・自然科学の観点で弱点です。なぜなら、実務入口で benchmark 名だけが残ると、読者は `official leaderboard` を `stable measurement of generalization` に過読しやすいからです。

## 根拠付き批判

### 1. benchmark 名だけでは、何を測ったスコアなのか固定できません

- 根拠:
  - EEG Challenge (2025) の公式トップページは、challenge preprint が execution phase の変更を反映していないため、現行 website と starter kit を参照するよう明記しています。
  - 公式 rules は、追加 pretraining data、使用 pretrained model、fine-tuning 方法の開示、`inference-stage code submission`、`single GPU with 20 GB memory` を要求しています。
- 批判:
  - したがって benchmark 名だけではなく、`current rules` と `submission constraints` も benchmark object の一部です。
  - これを dataset / benchmark 実務ページで固定しないのは弱いです。

### 2. official leaderboard 自体が postmortem を含みうる以上、postmortem は周辺情報ではありません

- 根拠:
  - EEG Challenge (2025) の最終 leaderboard は、Challenge 2 sample が randomize されておらず contiguous-trial same-subject structure を利用できたため、賞の扱いを変更したと公開しています。
- 批判:
  - これは「後から付いた補足」ではなく、`leaderboard が何を測っていたのか` を変更する情報です。
  - したがって postmortem は benchmark reproducibility の一部であり、実務ページの checklist に出ていなければなりません。

### 3. benchmark governance の弱さは、近年の EEG-FM benchmark papers 自身が警告しています

- 根拠:
  - Xiong et al. (2025) は、inconsistent protocols により cross-model comparison が unreliable になると述べています。
  - Liu et al. (2026) は 12 open-source EEG foundation models と specialist baselines を 13 datasets で比較し、linear probing と fine-tuning の違い、model scale、benchmarking choice によって読みが変わることを示しました。
- 批判:
  - よって `benchmark governance` は site 内部の作法ではなく、一次ソース側から要請されている stop line です。
  - `datasets.md` がこの stop line を前景化していないのは、site-wide rule との整合性の点でも弱かったと言えます。

## 今回実行した変更

- `datasets.md`
  - `last_updated` を `2026-03-25` に更新しました。
  - front matter の `page_highlights` と `known_points` に、benchmark provenance / postmortem を独立論点として追加しました。
  - `wiki_links` に `Wiki: EEG foundation models and pretraining` を追加しました。
  - generalization / shortcut section に `2026-03-25 addendum: benchmark governance is part of the benchmark` note-box を新設しました。
  - 同 section の site rule を拡張し、leaderboard / challenge claim には benchmark version, split/randomization, hidden grouping, extra-data/checkpoint policy, inference-stage restrictions, postmortem disclosure を必須化しました。
  - `benchmark-mindset` checklist に `Benchmark provenance` 項目を追加しました。
  - benchmark 実務の follow-up として `Pretraining Card` と foundation-model wiki への導線を追加しました。

## 外部依存で保留

- なし
  - 今回の変更は repo 内の文書修正・検証・push までで完結できます。

## 参考文献 / 公式ソース

1. EEG Challenge (2025) official homepage.
   - https://eeg2025.github.io/
2. EEG Challenge (2025) official rules.
   - https://eeg2025.github.io/rules/
3. EEG Challenge (2025) official submission page.
   - https://eeg2025.github.io/submission/
4. EEG Challenge (2025) official leaderboard / postmortem.
   - https://eeg2025.github.io/leaderboard/
5. Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025/2026.
   - https://arxiv.org/abs/2508.17742
6. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
   - https://arxiv.org/abs/2601.17883
