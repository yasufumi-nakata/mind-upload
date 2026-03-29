# Site Deepening Audit (2026-03-29, index / FAQ foundation-model benchmark-governance front door)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
- 同期対象:
  - `summary_booklet.md`
  - `scripts/build_summary_booklet.rb`
- 参照済みの既存深掘り:
  - `eeg_101.md`
  - `verification.md`
  - `wiki/eeg-foundation-models.md`
- 調査範囲: 技術 / 自然科学のみ
- 除外した論点: 哲学、法学、制度論

## web確認対象

- `https://proceedings.iclr.cc/paper_files/paper/2024/file/47393e8594c82ce8fd83adc672cf9872-Paper-Conference.pdf`
- `https://proceedings.mlr.press/v267/lee25a.html`
- `https://arxiv.org/abs/2510.21585`
- `https://arxiv.org/abs/2508.17742`
- `https://arxiv.org/abs/2601.17883`
- `https://arxiv.org/abs/2603.02268`
- `https://arxiv.org/abs/2506.19141`
- `https://eeg2025.github.io/`
- `https://eeg2025.github.io/data/`
- `https://eeg2025.github.io/rules/`
- `https://eeg2025.github.io/submission/`
- `https://eeg2025.github.io/leaderboard/`

## 今回この箇所を選んだ理由

- 深いページ群では、すでに EEG foundation model と benchmark governance をかなり厳密に読ませていました。
  - `eeg_101.md`
  - `verification.md#pretraining-card`
  - `wiki/eeg-foundation-models.md`
- しかし front door 側、とくに `index.md` と `faq.md` には、まだ次の停止線が十分に露出しておりませんでした。
  - `leaderboard result != general neural decoder`
  - `benchmark object != one common task object`
  - `benchmark governance / postmortem != administrative detail`
  - `large pretraining corpus != shortcut-resistant transfer`
- そのため、公開入口だけを読んだ読者が
  - `large model`
  - `strong leaderboard rank`
  - `cross-task challenge result`
  を、実際より強い `general EEG decoder` や `WBE-relevant state readout progress` と誤読する余地が残っておりました。

## 主要結論

- EEG foundation-model / leaderboard の front door 説明は、2026-03-29 時点の一次ソースに対してなお弱すぎました。
- 一次文献と公式 benchmark ページの現在地では、少なくとも入口でも次の 5 点を明示しなければなりません。
  - `pretraining corpus identity / overlap audit`
  - `benchmark object / supervision unit`
  - `adaptation regime`
  - `benchmark provenance / governance`
  - `shortcut resistance against subject / setup fingerprints`
- よって公開入口では、
  - `foundation-model result = benchmark-conditioned transfer evidence`
  - `leaderboard result = governance-conditioned score`
  と明示しない限り、技術的に正確とは申せませんでした。

## 根拠付き批判

### 1. 大規模 pretraining の存在だけでは、general EEG decoder を主張できません

- [Jiang et al. (2024)](https://proceedings.iclr.cc/paper_files/paper/2024/file/47393e8594c82ce8fd83adc672cf9872-Paper-Conference.pdf) は、LaBraM を提示しつつも、EEG 側の中心課題として
  - mismatched electrodes
  - unequal sample lengths
  - varied task designs
  - low signal-to-noise ratio
  を前景化しました。
- [El Ouahidi et al. (2025)](https://arxiv.org/abs/2510.21585) は 92 datasets, 25,000 subjects, 60,000+ hours という大規模 pretraining を提示しました。

批判:

- 旧 front door では、これらの論点は深いページに退避しており、入口では十分に止まっておりませんでした。
- しかし一次ソース自身が、`large-scale pretraining` の主張と同時に `setup heterogeneity` を中心問題として残しております。
- よって `large model exists` を `general decoder is close` と読ませる入口は不正確でございました。

### 2. モデル規模の大きさは、そのまま優越性や portability を保証しません

- [Lee et al. (2025)](https://proceedings.mlr.press/v267/lee25a.html) は、大規模 brainwave foundation models が従来 deep baselines に対して `about 0.5%` の marginal gain しか示さないケースを報告しました。
- [Liu et al. (2026)](https://arxiv.org/abs/2601.17883) は、
  - linear probing is frequently insufficient
  - specialist models trained from scratch remain competitive
  - larger foundation models do not necessarily yield better generalization
  を示しました。
- [Lahiri et al. (2026)](https://arxiv.org/abs/2603.02268) は、narrow-source pretraining と diverse-source pretraining の優劣が adaptation regime に依存しうることを示しました。

批判:

- したがって `bigger model`, `more datasets`, `higher pretraining scale` を one-dimensional frontier として入口で読ませるのは不正確でございます。
- 主張の ceiling は、少なくとも
  - linear probe か fine-tuning か
  - narrow-source か diverse-source か
  - specialist baseline を含めた比較か
  を固定して初めて読めます。

### 3. benchmark object は一つではなく、同じ benchmark family の中でも supervision unit が混在します

- [EEG Foundation Challenge paper (2025)](https://arxiv.org/abs/2506.19141) は、challenge を
  - new tasks / new subjects への transfer
  - psychopathology factor prediction
  の二系統で提示しました。
- 公式 [EEG Challenge data page](https://eeg2025.github.io/data/) は、`over 3,000 participants across six distinct cognitive tasks` と `four psychopathology dimensions` を同時に掲げています。

批判:

- 旧 front door は `leaderboard score` や `foundation-model result` を止めていても、`what exactly was predicted` の差を入口で十分に固定しておりませんでした。
- しかし trial-level decode, event-level readout, subject-level factor regression は同じ inferential object ではございません。
- したがって、`benchmark object / supervision unit` を入口で切り出さないのは、現行一次・公式ソースに対して弱すぎました。

### 4. benchmark governance は事務的 metadata ではなく、score の意味を変える一次条件です

- 公式 [EEG Challenge homepage](https://eeg2025.github.io/) は、proposal preprint が execution-phase changes に対してすでに outdated であり、current website と Starter Kit を authoritative source として使うべきだと明示しています。
- 公式 [rules page](https://eeg2025.github.io/rules/) は、
  - downsampled 100 Hz evaluation
  - extra pretraining datasets disclosure
  - pretrained-model and fine-tuning disclosure
  - single-GPU 20 GB inference-stage budget
  - code submission competition
  を要求しています。
- 公式 [submission page](https://eeg2025.github.io/submission/) は inference-stage code submission を固定しています。
- 公式 [leaderboard](https://eeg2025.github.io/leaderboard/) は、Challenge 2 sample が randomized されておらず contiguous-trial same-subject structure を exploit し得たことを開示し、challenge 1 / 2 を別 award にしました。

批判:

- これらは単なる大会運営メモではございません。
- `which data`, `which inference budget`, `which hidden grouping`, `which rules snapshot` で score が変わることを示す一次 evidence です。
- よって `benchmark provenance / governance` を front door で独立停止条件にしないのは不十分でございました。

### 5. benchmark inconsistency は model ranking 自体を反転させ得ます

- [Xiong et al. (2025)](https://arxiv.org/abs/2508.17742) は、inconsistent evaluation protocols が EEG foundation model の systematic comparison を unreliable にすると論じました。
- [Lahiri et al. (2026)](https://arxiv.org/abs/2603.02268) は、EEG-Bench と EEG-FM-Bench の systematic inconsistency により identical datasets 上でも ranking が `up to 24 pp` 反転しうることを示しました。

批判:

- これは `which model is best` の問題ではなく、`score itself is object- and protocol-dependent` という問題でございます。
- したがって front door は、`leaderboard` を capability frontier と読ませるのではなく、`governance-conditioned benchmark result` として止める必要がございました。

## 今回実行した変更

- `faq.md`
  - `page_highlights` を更新し、front door guardrails を 10 本に拡張しました。
  - `known_points` に、foundation-model / leaderboard score の読解停止線を追加しました。
  - 入口案内表に `Q1c2` を追加しました。
  - note box `Ten technical guards now fixed at the front door` に foundation-model / leaderboard stop rule を追加しました。
  - 新規節 `Q1c2` を追加し、foundation-model / leaderboard result を
    - benchmark-conditioned transfer evidence
    - governance-conditioned score
    として読む文面に改稿しました。

- `index.md`
  - `page_highlights` / `known_points` に foundation-model / leaderboard stop rule を追加しました。
  - new note box `If A Large EEG Model Or Leaderboard Rank Sounds Like A General Neural Decoder` を追加しました。
  - `faq.html#q1c2`、`eeg_101.html`、`verification.html#pretraining-card` への最短導線を front door に埋めました。

- `scripts/build_summary_booklet.rb`
  - 自動生成冊子の見出し
    - `入口で落としてはいけない技術的停止線`
    - `観測の上限`
    - `比較と解釈の上限`
    を英語化しました。
  - これは project rule `Any AI or automated update to public-facing content must be written in English.` に合わせるためでもございます。

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成し、front matter 由来の stop line と英語見出しを同期しました。

## 今回止めた誤読

- `leaderboard で上位 = general neural decoder がほぼ解けた`
- `large pretraining corpus = shortcut-resistant transfer がほぼ解けた`
- `challenge paper を読んだ = current benchmark operations まで把握した`
- `one benchmark family = one common supervision unit`
- `model ranking = pure model capability ranking`

## 外部依存タスク

- なし
  - 今回の変更は、一次ソース確認、repo 内公開ページ改稿、冊子再生成、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR*. 2024.
   - https://proceedings.iclr.cc/paper_files/paper/2024/file/47393e8594c82ce8fd83adc672cf9872-Paper-Conference.pdf
2. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *Proceedings of Machine Learning Research*. 2025.
   - https://proceedings.mlr.press/v267/lee25a.html
3. El Ouahidi Y, Lys J, Thölke P, Farrugia N, Pasdeloup B, Gripon V, Jerbi K, Lioi G. REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. *arXiv*. 2025.
   - https://arxiv.org/abs/2510.21585
4. Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
5. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
   - https://arxiv.org/abs/2601.17883
6. Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
   - https://arxiv.org/abs/2603.02268
7. Aristimunha B, Truong D, Guetschel P, et al. EEG Foundation Challenge: From Cross-Task to Cross-Subject EEG Decoding. *NeurIPS Competition Track*. 2025.
   - https://arxiv.org/abs/2506.19141
8. EEG Challenge (2025). Official homepage.
   - https://eeg2025.github.io/
9. EEG Challenge (2025). Data page.
   - https://eeg2025.github.io/data/
10. EEG Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
11. EEG Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
12. EEG Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
