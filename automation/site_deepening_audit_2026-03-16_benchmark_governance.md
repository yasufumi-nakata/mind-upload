# Site Deepening Audit (2026-03-16, Benchmark Governance / Leaderboard Evidence)

## 対象

- 主対象: `datasets.md`
- 主対象: `verification.md`

## 今回の選定理由

- 2026-03-16 時点で、公開サイトは `dataset version`、`BIDS`、`event fidelity`、`evaluation family`、`benchmark provenance` をかなり整理できていました。
- しかし、`その score がどんな運用条件で露出したか` という benchmark governance は、まだ公開ルールとして十分に固定されていませんでした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、同じ `cross-subject accuracy` でも、`public leaderboard で何十回も擦った score` と、`hidden final test + code submission + fixed checkpoint policy` で得た score は、統計的な意味が違うからです。

## 主要な批判点

### 1. 旧 `datasets.md` は benchmark provenance を重視していましたが、benchmark governance を別の提出物として扱えていませんでした

- 問題:
  - 旧版は `benchmark 名`、`version`、`split construction`、`checkpoint selection` の重要性を foundation model 文脈ではかなり明確に書いていました。
  - しかし、`public leaderboard か hidden/private test か`、`prediction upload か code submission か`、`submission cap があるか`、`final ranking が separate hold-out か` といった運用条件は dataset 導線では前面化されていませんでした。
- 根拠:
  - Jayaram & Barachant (2018) と MOABB docs は、within-session / cross-session / cross-subject を standardized evaluation family として整えました。
  - ただし Blum & Hardt (2015) は、leaderboard が repeated submission により adaptive hold-out になりうることを示しました。
  - 一方で Roelofs et al. (2019) は、separate final test を持つ Kaggle competition 群では public leaderboard overfitting が必ずしも大きくないことを示しました。
- 修正:
  - `datasets.md` に `2.7) benchmark governance を出さない leaderboard は比較可能な証拠になりません` を追加しました。
  - `Benchmark Governance Card` を新設し、benchmark object、evaluation surface、submission budget、model-selection policy、external data / pretraining disclosure、runtime envelope、post-benchmark audit を最低提出項目へ昇格しました。

### 2. 旧 `verification.md` は model card と intervention card を整備していましたが、benchmark 側の責任分界が弱いままでした

- 問題:
  - 旧版は `Observability Budget`、`Fusion Card`、`Temporal Validity Card`、`latent-state error budget`、`Intervention Card` を整備していました。
  - しかし、`モデルが何をしたか` と `benchmark がどんな露出条件で score を返したか` を分ける card が無く、leaderboard / challenge 結果の読み方が model card 側へ押し込まれていました。
- 根拠:
  - BCI Competition IV 公式サイトは、labeled calibration + unlabeled evaluation data を採り、`one researcher may NOT submit multiple results to one data set` と明記しています。
  - EEG Challenge 2025 Rules / Submission は、code submission、single GPU 20 GB 制約、extra dataset / pre-trained model の明示、daily submission limit を要求しています。
  - Xiong et al. (2025) は standardized evaluation の欠如が cross-model comparison を unreliable にすると明記し、Lahiri et al. (2026) は split construction、checkpoint selection、segment length、normalization を含む 6 要因の不整合で ranking が最大 24 pp 反転しうると報告しました。
- 修正:
  - `verification.md` に `Benchmark Governance Card` 節を追加しました。
  - `Benchmark Governance Card` を Model Card / Pretraining Card / Observability Budget / Intervention Card と分離し、`score を比較可能にする評価面` を固定する提出物として定義しました。

### 3. 旧 site は leaderboard を「悪」と「善」の二択で読ませる余地がありました

- 問題:
  - benchmark governance を明示しないままだと、読者は `leaderboard は全部 unsafe` か `challenge だから自動で公平` かの二択で理解しがちでした。
- 根拠:
  - Blum & Hardt (2015) は adaptive hold-out 問題を理論化しました。
  - しかし Roelofs et al. (2019) は、separate final test を持つ competition 群では substantial overfitting の証拠が乏しいと示しました。
- 修正:
  - 両ページで site rule を「leaderboard 全否定」ではなく、「hidden evaluation、submission budget、checkpoint policy、extra data disclosure を出さない score は限定つきで読む」へ修正しました。

## 今回実行した変更

- `datasets.md`
  - `2.7) benchmark governance` 節を追加
  - `Benchmark Governance Card` を定義
  - site rule と references を更新
- `verification.md`
  - stage 4 の `Leaderboard & Model Cards` 説明へ `Benchmark Governance Card` を追加
  - `Benchmark Governance Card` 節を新設
  - 参考文献へ leaderboard / challenge / benchmark governance 関連の一次資料を追加

## 外部依存で保留

- なし
  - 今回の変更は、このリポジトリ内の公開ルール整備と参考文献追加で完結しています。

## 参考文献

- Jayaram V, Barachant A. MOABB: trustworthy algorithm benchmarking for BCIs. *J Neural Eng*. 2018.
  - https://doi.org/10.1088/1741-2552/aadea0
- MOABB Documentation.
  - https://moabb.neurotechx.com/docs/index.html
- Blum A, Hardt M. The Ladder: A Reliable Leaderboard for Machine Learning Competitions. *ICML / PMLR 37*. 2015.
  - https://proceedings.mlr.press/v37/blum15.html
- Roelofs R, Shankar V, Recht B, Fridovich-Keil S, Hardt M, Miller J, Schmidt L. A Meta-Analysis of Overfitting in Machine Learning. *NeurIPS*. 2019.
  - https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html
- BCI Competition IV.
  - https://www.bbci.de/competition/iv/
- EEG Challenge (2025): Rules.
  - https://eeg2025.github.io/rules/
- EEG Challenge (2025): Submission.
  - https://eeg2025.github.io/submission/
- Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. 2025.
  - https://arxiv.org/abs/2508.17742
- Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. 2026.
  - https://arxiv.org/abs/2603.02268
