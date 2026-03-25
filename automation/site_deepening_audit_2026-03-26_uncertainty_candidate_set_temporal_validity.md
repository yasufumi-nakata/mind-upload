# Site Deepening Audit (2026-03-26, Uncertainty / Candidate Scaffold / Temporal Validity)

## 対象

- 主対象: `wiki/uncertainty-confidence-and-abstention.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 直近の更新で、このサイトは `candidate set`、`prompt scaffold`、`Temporal Validity Card`、`Neural Contribution Card` を別ページではかなり明確に扱えていました。
- その一方で、`wiki/uncertainty-confidence-and-abstention.md` はまだ主に一般的な calibration / abstention ページとして読めてしまい、言語デコード系の `confidence` が **何に条件づけられた confidence なのか** を十分に固定していませんでした。
- これは技術・自然科学の観点で重要でございます。なぜなら、同じ `top-k` や confidence でも、
  - 固定候補バンクからの retrieval なのか
  - 既知 onset つきの単語デコードなのか
  - prompt-conditioned generation なのか
  - autoregressive context を使う subject-specific reconstruction なのか
  によって、確率や不確実性の意味が変わるからでございます。

## 主要な批判点

### 1. 旧ページは `confidence != calibration` を教えられていましたが、`confidence is conditional on the declared output scaffold` をまだ前景化できていませんでした

- 問題:
  - 旧 `wiki/uncertainty-confidence-and-abstention.md` は split、coverage、abstention の重要性を整理できていました。
  - しかし、言語デコード系の score が `candidate bank`、`known onset`、`prompt`、`LM prior` に条件づけられていることを、独立した stop line としては示せていませんでした。
- 根拠:
  - Tang et al. (2023) は fMRI と autoregressive context の双方に依存する semantic reconstruction を示し、encoding model と language model の寄与を分けるために distractor-based 評価も行っています。
  - Défossez et al. (2023) は 3 秒音声セグメントに対する top-k retrieval を示しており、open-world generation ではありません。
  - d'Ascoli et al. (2025) は prior retrieval work が test 時に ground-truth speech segments を必要とする点を明示し、自身の結果も known-word-onset と fixed retrieval set の下で報告しています。
  - Ye et al. (2025) は brain embedding と text prompt embedding を連結して LLM generation を行っており、prompt scaffold が出力空間の一部です。
- 修正:
  - `wiki/uncertainty-confidence-and-abstention.md` に `Candidate-bank and prompt-conditioned confidence are not open-world uncertainty` 節を追加しました。
  - 同ページの highlights / known points / note に、言語デコード系 score の条件づけ対象を明示しました。

### 2. 旧ページは calibration を temporal shift まで拡張する caution はありましたが、`candidate scaffold` と `temporal validity` の接続が弱いままでした

- 問題:
  - 旧版は `within-session != cross-day` を述べていましたが、言語デコード系 task でこれをどう読むべきかが明確ではありませんでした。
  - 特に、同一 subject・同一 protocol・同一 onset rule での calibration を、そのまま deployment 的 reliability に近づけて読める余地が残っていました。
- 根拠:
  - Ovadia et al. (2019) は dataset shift 下で uncertainty estimate が大きく劣化しうることを示しました。
  - Han, Huang, Wang (2024) は temporal distribution shift 下で assessment / selection 自体を時間軸に整列させる必要を示しました。
  - Tibshirani et al. (2019) は exchangeability が崩れる covariate shift では conformal route 自体を修正する必要を示しました。
- 修正:
  - `wiki/uncertainty-confidence-and-abstention.md` に、言語デコード系出力は `Neural Contribution Card` と `Temporal Validity Card` を重ねて読むルールを追記しました。
  - 参考文献の Han 論文について、著者表記と PMLR リンクを一次ソースに合わせて修正しました。

### 3. 旧ページは task-specific reporting に言語デコード系が欠けており、`何を出せば最低限読めるのか` が曖昧でした

- 問題:
  - source imaging、offline EEG classification、rare event prediction、online BCI は個別欄がありました。
  - しかし、speech / brain-to-text decode は候補集合・prompt・onset・no-brain/no-LM baseline が本質なのに、その reporting row がありませんでした。
- 修正:
  - `speech / brain-to-text decode` 行を追加しました。
  - 要求項目として `Neural Contribution Card` fields、candidate bank / retrieval-set size、prompt / LM scaffold、onset regime、no-brain / no-LM / shuffle controls、calibration / abstention slices、Temporal Validity Card を明記しました。

### 4. 旧ページの references には temporal-shift 文献の誤リンクがあり、一次文献監査として不十分でした

- 問題:
  - Han et al. (2024) のリンクが `han24d` になっており、正しくは `han24b` でした。
  - 著者表記も `Han, J.` になっていましたが、正しくは `Han, E.` です。
- 修正:
  - 対象ページの reference を修正しました。
  - あわせて Tang / Défossez / d'Ascoli / Ye / Tibshirani を追加し、今回の批判点に対応する一次文献束を揃えました。

## 今回実行した変更

- `wiki/uncertainty-confidence-and-abstention.md`
  - `last_updated` を `2026-03-26` に更新
  - scope / highlights / known points / weaknesses note を更新
  - `candidate-bank and prompt-conditioned confidence` 節を新設
  - `speech / brain-to-text decode` の task-specific reporting 行を追加
  - site rules に `Language-facing scores must disclose their scaffold` と `Stack the Neural Contribution Card` を追加
  - Han reference の誤りを修正し、一次文献を追加
- `glossary.md`
  - calibration の定義を、language decode では declared scaffold に条件づけられる旨が読めるよう更新

## 外部依存で保留

- なし
  - 今回の変更は本文、参照、用語の同期で完結しています。

## 参考文献

- Tang J, LeBel A, Jain S, Huth AG. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- Défossez A, Caucheteux C, Rapin J, et al. Decoding speech perception from non-invasive brain recordings. Nat Mach Intell. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Ye X, Liu X, Wang Y, et al. Generative language reconstruction from brain recordings. Commun Biol. 2025.
  - https://doi.org/10.1038/s42003-025-07731-7
- Ovadia Y, Fertig E, Ren J, et al. Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift. NeurIPS. 2019.
  - https://papers.nips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html
- Han E, Huang C, Wang K. Model Assessment and Selection under Temporal Distribution Shift. ICML / PMLR. 2024.
  - https://proceedings.mlr.press/v235/han24b.html
- Tibshirani RJ, Barber RF, Candès EJ, Ramdas A. Conformal Prediction Under Covariate Shift. NeurIPS. 2019.
  - https://papers.nips.cc/paper/8522-conformal-prediction-under-covariate-shift
