# Site Deepening Audit (2026-03-16, Calibration / Abstention Card)

## 対象

- 主対象: `verification.md`
- 主対象: `wiki/uncertainty-confidence-and-abstention.md`
- 副対象: `wiki/baselines-prereg-and-model-cards.md`
- 副対象: `eeg_101.md`

## 今回の選定理由

- 2026-03-16 時点で、このサイトは Observability Budget、Fusion Card、Temporal Validity Card、Intervention Card、Benchmark Governance Card まで整備できていました。
- その一方で、`confidence`、`posterior`、`prediction set`、`abstention` は各ページで注意書きとして散在しており、他の論点のような **独立した提出物仕様** にはなっていませんでした。
- この欠落は技術・自然科学の観点で重大でございます。なぜなら、同じ `ECE` や `coverage` でも
  - `fit / calibration / test` をどう分けたか
  - `within-session / cross-session / cross-subject / temporal shift` のどれで測ったか
  - `prediction set` なのか `scalar confidence` なのか
  - `abstention` が何へ分岐するのか
  を固定しない限り、確率や棄権の意味そのものが変わるからです。

## 主要な批判点

### 1. 旧サイトは `confidence != calibration` と言っていましたが、提出物仕様としては未固定でした

- 問題:
  - `wiki/uncertainty-confidence-and-abstention.md` は `confidence` と `calibration` を分ける補助ページとしては機能していました。
  - しかし Verification 本体には、それを他のカード類のように再利用できる schema がありませんでした。
- 根拠:
  - Ovadia et al. (2019) は predictive uncertainty methods が dataset shift 下で広く劣化しうることを示しました。
  - Han et al. (2024) は temporal distribution shift で model assessment / selection 自体を時間軸に合わせる必要を示しました。
- 修正:
  - `verification.md` に `Calibration & Abstention Card` を新設しました。
  - `fit / calibration / test separation`、`evaluation family / shift slices`、`metrics / validity statement`、`fallback policy`、`recalibration policy`、`claim ceiling` を最低提出項目に昇格しました。

### 2. 旧サイトは calibration を主に `1数値の良し悪し` として読ませやすく、split 依存性が弱かった

- 問題:
  - 旧 `wiki/uncertainty-confidence-and-abstention.md` は ECE / Brier / NLL を出すべきだと述べていました。
  - しかし `どの split でその calibration を得たか`、`test を見ながら threshold を触っていないか`、`same-day と cross-day が別物であるか` を十分に前景化していませんでした。
- 根拠:
  - Shafiezadeh et al. (2023) は patient-independent seizure prediction で evaluation split の作り方自体が結果を大きく動かすことを示しました。
  - Shafiezadeh et al. (2024) は calibration 改善が threshold 設計を変えることを示しました。
- 修正:
  - `wiki/uncertainty-confidence-and-abstention.md` に `校正は fit / calibration / test を分けて管理します` 節を追加しました。
  - 同ページに `同じ calibration でも evaluation family が違えば意味が変わります` 節を追加し、within-session / cross-session / cross-subject / temporal shift を分けました。

### 3. 旧サイトは `prediction set`、`interval`、`abstention` を同じ「不確実性」でまとめていました

- 問題:
  - 旧版では scalar confidence、interval、set-valued prediction、abstention の違いが十分に構造化されていませんでした。
  - そのため、読者が `confidence を出した`、`set を返した`、`答えないことがある` を、いずれも同じ「安全性」と誤読する余地が残っていました。
- 根拠:
  - Lei et al. (2018) は split conformal による distribution-free predictive inference を示しました。
  - Chernozhukov et al. (2021) は distributional conformal prediction を提示しました。
  - Eliades & Papadopoulos (2019) は conformal prediction を exoskeleton control に適用し、set-valued output 自体が safety design の一部になりうることを示しました。
- 修正:
  - `wiki/uncertainty-confidence-and-abstention.md` に `確率・区間・予測集合・棄権は別の出力です` 節を追加しました。
  - `metrics / validity statement` に marginal / conditional / temporal validity と set size を明示するルールを追加しました。

### 4. 旧サイトは public entry から新カードへ辿る導線が弱かった

- 問題:
  - card を Verification にだけ追加しても、公開ページや学習ページから辿れなければ運用上は死にます。
- 修正:
  - `wiki/baselines-prereg-and-model-cards.md` に `Calibration & Abstention Card` の位置づけを追加しました。
  - `eeg_101.md` の不確実性 note から `verification.html#calibration-abstention-card` へ導線を追加しました。

## 今回実行した変更

- `verification.md`
  - `page_highlights` に Calibration & Abstention Card を追加
  - `Leaderboard & Model Cards` 説明へ新カードを統合
  - `calibration-abstention-card` 節を新設
  - 参考文献に Ovadia / Han / Shafiezadeh / Lei / Chernozhukov / Segal / Eliades を追加
- `wiki/uncertainty-confidence-and-abstention.md`
  - `last_updated` を 2026-03-16 に更新
  - front matter の highlights / known / unknown / wiki_links を更新
  - `fit / calibration / test`、`evaluation family / shift slices`、`output object` の節を追加
  - site rule を Calibration & Abstention Card ベースへ改稿
  - 参考文献を拡張
- `wiki/baselines-prereg-and-model-cards.md`
  - page highlights に新カードを追加
  - 2026-03 追補と roles / checklist を更新
  - `確率や棄権を出す結果で追加するもの` 節を新設
- `eeg_101.md`
  - 不確実性 note と highlights に新カードへの導線を追加

## 外部依存で保留

- なし
  - 今回の作業はこのリポジトリ内の本文更新、導線修正、参考文献追加で完結しています。

## 参考文献

- Ovadia Y, Fertig E, Ren J, et al. Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift. NeurIPS. 2019.
  - https://papers.nips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html
- Han E, Huang C, Wang K. Model Assessment and Selection under Temporal Distribution Shift. ICML / PMLR. 2024.
  - https://proceedings.mlr.press/v235/han24b.html
- Shafiezadeh S, Mento G, Testolin A. Methodological Issues in Evaluating Machine Learning Models for Patient-Independent Epileptic Seizure Prediction. Mathematics. 2023.
  - https://doi.org/10.3390/math11071650
- Shafiezadeh S, Duma GM, Mento G, et al. Calibrating Deep Learning Classifiers for Patient-Independent Electroencephalogram Seizure Forecasting. Sensors. 2024.
  - https://doi.org/10.3390/s24092863
- Lei J, G'Sell M, Rinaldo A, Tibshirani RJ, Wasserman L. Distribution-Free Predictive Inference for Regression. JASA. 2018.
  - https://doi.org/10.1080/01621459.2017.1307116
- Chernozhukov V, Wüthrich K, Zhu Y. Distributional conformal prediction. PNAS. 2021.
  - https://doi.org/10.1073/pnas.2107794118
- Segal G, Keidar N, Lotan RM, et al. Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. Front Neurosci. 2023.
  - https://doi.org/10.3389/fnins.2023.1184990
- Eliades G, Papadopoulos H. Applying conformal prediction to control an exoskeleton. PMLR. 2019.
  - https://proceedings.mlr.press/v105/eliades19a.html
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
