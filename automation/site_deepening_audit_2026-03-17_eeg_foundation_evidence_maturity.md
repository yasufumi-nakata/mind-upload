# Site Deepening Audit (2026-03-17, EEG Foundation Models / Evidence Maturity and Benchmark Authority)

## 対象

- 主対象: `wiki/eeg-foundation-models.md`
- 副対象: `datasets.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-17 時点で、サイトは EEG foundation model の `corpus overlap`、`harmonization`、`adaptation regime`、`benchmark provenance` をかなり強く整理できていました。
- その一方で、公開本文ではなお、`accepted model paper`、`official challenge website / rules`、`arXiv benchmark preprint`、`under-review manuscript` が同じ強さの evidence として読める余地が残っていました。
- この弱点は技術・自然科学の観点で重要です。なぜなら、accepted paper が比較的強く支えるのは `ある設定での representation learning / transfer の前進` であり、official rules が支えるのは `score の露出条件` であり、preprint benchmark audit が支えるのは `比較の不安定性に関する警告` だからです。ここを混ぜると、`model capability` と `benchmark governance warning` と `moving target な運用条件` を 1 本の frontier ranking に圧縮してしまいます。

## 主要な批判点

### 1. 旧 foundation ページは source type を表の前面に出しておらず、accepted paper と benchmark-warning preprint を同列に読みやすかった

- 問題:
  - `wiki/eeg-foundation-models.md` は個々の研究の論点自体はよく整理していました。
  - しかし `accepted conference paper`、`official competition docs`、`arXiv preprint`、`under-review manuscript` の違いが table 上で即座に見えませんでした。
- 根拠:
  - BENDR は *Frontiers in Human Neuroscience* 2021 の査読済み journal paper です。
  - BIOT は NeurIPS 2023 の accepted conference paper です。
  - LaBraM は ICLR 2024 の accepted conference paper です。
  - EEGPT は NeurIPS 2024 の accepted conference presentation です。
  - EEG-FM-Bench、NeuroTTT、PRISM は arXiv preprint です。
  - DIVER-1 は under-review source として流通しています。
- 批判:
  - したがって、これらを同じ `最新研究` の 1 列で読むと、accepted capability evidence と exploratory benchmark warning が混ざります。
  - とくに ranking reversal や scaling-law の主張は重要ですが、`accepted benchmark consensus` ではなく、まず `warning / hypothesis / audit signal` として読むべきです。

### 2. 旧 site rule では moving target な challenge rule の authority source が固定されていなかった

- 問題:
  - `datasets.md` と `verification.md` は Benchmark Governance Card をかなり整備していましたが、`どのページを current authority と見なしたか` と `いつ確認したか` が card の欄にありませんでした。
- 根拠:
  - EEG Foundation Challenge の公式サイトは 2025-11-17 時点の本文で、challenge paper preprint が execution phase の変更を反映しておらず、`website` と `starter kit` を参照するよう明記しています。
  - つまり proposal / companion paper だけでは、current rule を固定できません。
- 批判:
  - `official website / rules / submission page` と `proposal preprint` を区別しない benchmark card は、運用中 challenge の解釈を取り違えます。
  - したがって Benchmark Governance Card には、`authority source / last verified` が必要です。

### 3. 旧 Pretraining Card は dataset / protocol を監査できていましたが、source maturity を監査していませんでした

- 問題:
  - 現行 Pretraining Card は `corpus identity`、`population / setup diversity`、`harmonization`、`objective / adaptation regime`、`benchmark provenance`、`scale / efficiency` を固定していました。
  - しかし、`この主張が accepted paper から来たのか、official rules から来たのか、preprint / under-review から来たのか` は card に入りませんでした。
- 批判:
  - これでは、accepted model result、competition operation、benchmark criticism が同じ evidential weight で流通します。
  - EEG foundation model のような moving field では、`source type / evidence maturity` を card に入れないと、score の意味だけでなく claim の重さ自体が曖昧になります。

## 今回実行した変更

- `wiki/eeg-foundation-models.md`
  - `last_updated` を `2026-03-17` に更新
  - page highlights に `source type を同じ証拠階級として扱わない` ルールを追加
  - `2026-03-17 時点で先に固定する source type` note を追加
  - `一次資料を evidence tier ごとに分けて読む` table を新設し、`source type / 2026-03-17 時点` 列を追加
  - `foundation model を読む前の 8 つの gate` に `G0: source type / maturity` を追加
  - Pretraining Card に `Source Type / Maturity` 行を追加
  - site rules に `official challenge docs を優先する` と `preprint benchmark warning を frontier verdict にしない` を追加
- `datasets.md`
  - `last_updated` を `2026-03-17` に更新
  - Pretraining Card に `source type / evidence maturity` 行を追加
  - foundation model 節に `2026-03-17 の追加 site rule` note を追加
  - Benchmark Governance Card に `authority source / last verified` 行を追加
  - benchmark governance 節に `2026-03-17 の authority rule` note を追加
- `verification.md`
  - Benchmark Governance Card に `authority source / last verified` 行を追加
  - `moving target benchmark` に関する note を追加

## 外部依存で保留

- なし
  - 今回の変更は、公開ページと card 仕様の改稿で完結しています。

## 参考文献・確認元

1. Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Front Hum Neurosci*. 2021;15:653659.
   - https://doi.org/10.3389/fnhum.2021.653659
2. Wang H, Lu C, Xie B, et al. BIOT: Biosignal Transformer for Cross-data Learning in the Wild. *NeurIPS 2023*.
   - https://papers.nips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf
3. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR 2024*.
   - https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html
4. Wang G, Liu W, He Y, et al. EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals. *NeurIPS 2024*.
   - https://neurips.cc/virtual/2024/poster/93793
5. Lee N, Barmpas K, Panagakis Y, et al. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML 2025 poster*.
   - https://openreview.net/forum?id=J5SbLoq7Uv
6. EEG Foundation Challenge official website.
   - https://eeg2025.github.io/
7. EEG Foundation Challenge rules.
   - https://eeg2025.github.io/rules/
8. EEG Foundation Challenge submission instructions.
   - https://eeg2025.github.io/submission/
9. Xiong W, Li J, Li J, Zhu K. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
10. El Ouahidi Y, Lys J, Thölke P, et al. REVE: A Foundation Model for EEG. *arXiv*. 2025.
   - https://arxiv.org/abs/2510.21585
11. Han DD, Gwon Y, Lee AL, et al. DIVER-1: Deep Integration of Vast Electrophysiological Recordings at Scale. *arXiv*. 2025.
   - https://arxiv.org/abs/2512.19097
12. Wang S, Deng Y, Bao Z, Zhan X, Duan Y. NeuroTTT: Bridging Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training. *arXiv*. 2025.
   - https://arxiv.org/abs/2509.26301
13. Lahiri JB, Runwal P, Kulkarni A, et al. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
   - https://arxiv.org/abs/2603.02268
14. Blum A, Hardt M. The Ladder: A Reliable Leaderboard for Machine Learning Competitions. *ICML 2015*.
   - https://proceedings.mlr.press/v37/blum15.html
15. Roelofs R, Cain N, Shlens J, Mozer MC. A Meta-Analysis of Overfitting in Machine Learning. *NeurIPS 2019*.
   - https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html
