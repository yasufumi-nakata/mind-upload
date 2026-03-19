# Site Deepening Audit (2026-03-20, EEG Foundation Models / Benchmark Governance)

## 対象

- 主対象: `mind_uploading_papers.md`
- 主対象: `wiki/eeg-foundation-models.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-20 時点で，サイトは EEG foundation model の読み方自体はすでに持っていました。
- ただし，その論点が `paper archive の技術フロンティア入口` と `Verification の提出ルール` にまだ十分統合されていませんでした。
- このままでは，読者が `large model の高スコア = portable transfer solved`，`leaderboard 上位 = subject-invariant decoding solved` と誤読しやすい状態でした。
- とくに 2025 年 EEG Challenge の公式 postmortem は，`benchmark provenance` が抽象論ではなく，実際にランキングと賞の解釈を変える運営上の論点であることを示しています。

## 主要な批判点

### 1. 公開アーカイブの技術入口に foundation-model ルートが欠けていました

- 問題:
  - `mind_uploading_papers.md` は decode / neuroprosthesis / ESI / observability / maintenance-state を優先導線として整理していました。
  - しかし，2024-2026 に技術的に重要度が上がった `EEG foundation model / pretraining` が front-door route として未統合でした。
  - そのため，foundation-model 論文を law / philosophy 混在の年次順から拾うしかなく，技術・自然科学の読み筋が弱いままでした。
- 根拠:
  - Kostas et al. (2021) は transfer を中心課題として置いています。
  - Jiang et al. (2024) は electrode mismatch，unequal length，varied task design，low SNR を主要障壁として明示しています。
  - Lee et al. (2025) は大規模 brainwave FM の fine-tuning 利得が小さいことと，PEFT の重要性を示しています。
- 今回実行した変更:
  - `mind_uploading_papers.md` に `EEG foundation models / pretraining governance` 行を追加しました。
  - 同ページに foundation-model 専用の読み方 note と evidence class を追加しました。
  - `I want to read EEG foundation models / pretraining safely` という読者向け導線も追加しました。

### 2. ベンチマーク運営上の失敗が，公開ルール側でまだ一級の証拠として扱われていませんでした

- 問題:
  - サイトは `benchmark provenance` の必要性をすでに述べていました。
  - しかし，公式 competition が実際に `split construction` と `sample order` の問題で解釈を変更した事例は，十分に front door へ反映されていませんでした。
- 根拠:
  - EEG Challenge 2025 submission page は `inference-only code competition` を明記しています。
  - EEG Challenge 2025 leaderboard は，Challenge 2 で sample randomization をしていなかったため contiguous trials から same-subject structure を利用できたと organizers 自身が開示し，最終的に Challenge 1 / 2 を別賞にしました。
- 今回実行した変更:
  - `wiki/eeg-foundation-models.md` に official leaderboard / postmortem を独立した source row として追加しました。
  - 同ページで `benchmark provenance` の定義に `sample-randomization / hidden-grouping policy / inference-stage restrictions` を追加しました。
  - `verification.md` の Pretraining Card にも同じ観点を入れ，提出ルールへ昇格しました。

### 3. verification 側の Pretraining Card が，split randomness と hidden grouping をまだ明示していませんでした

- 問題:
  - 旧 Pretraining Card は corpus, harmonization, adaptation, benchmark provenance を要求していました。
  - ただし benchmark provenance の中身がまだ粗く，`sample randomization` と `hidden grouping` が独立項目として見えませんでした。
- 根拠:
  - 公式 challenge postmortem が，この二点だけで leaderboard interpretation を変えることを示しました。
  - したがって `benchmark name / version / split rule` だけでは不十分です。
- 今回実行した変更:
  - `verification.md` で page highlight / known point / Pretraining Card 本文を更新しました。
  - `benchmark provenance` 欄に `sample-randomization / hidden-grouping policy` と `inference-stage compute or training restrictions` を追加しました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - foundation-model / pretraining governance を技術フロンティア入口に追加
  - foundation-model 専用 note を追加
  - evidence class と読者導線を追加
- `wiki/eeg-foundation-models.md`
  - `last_updated` を更新
  - official leaderboard / postmortem を source row と reference に追加
  - G5 benchmark provenance を厳格化
  - benchmark postmortem を site rule に追加
- `verification.md`
  - Pretraining Card の benchmark provenance を厳格化
  - official challenge operations を根拠として本文へ統合

## 検証結果

- `git diff --check` : pass
- `bundle exec jekyll build` : pass

## 外部依存で保留

- なし
  - 今回の変更はすべてこのリポジトリ内で完結しています。

## 参考文献

- Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Front Hum Neurosci*. 2021;15:653659.
  - https://doi.org/10.3389/fnhum.2021.653659
- Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR*. 2024.
  - https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html
- Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML 2025 poster*.
  - https://openreview.net/forum?id=J5SbLoq7Uv
- EEG Foundation Challenge (2025). Submission.
  - https://eeg2025.github.io/submission/
- EEG Foundation Challenge (2025). Leaderboard.
  - https://eeg2025.github.io/leaderboard/
- Xiong W, Li J, Li J, Zhu K. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
  - https://arxiv.org/abs/2508.17742
- Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
  - https://arxiv.org/abs/2603.02268
