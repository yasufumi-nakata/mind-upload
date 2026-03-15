# Site Deepening Audit (2026-03-15, EEG Generalization Ladder / Recalibration Burden)

## 対象

- 主対象: `datasets.md`
- 副対象: `eeg_101.md`

## 今回の選定理由

- 公開サイトは 2026-03-15 時点で、annotation provenance、split unit、QC、observability ceiling まではかなり整理できていました。
- その一方で、公開ページの入口ではなお `高い score` が `どの汎化条件で出た score なのか` を読み分ける導線が弱く、`within-session の成功` が `cross-day robustness` や `deployable loop` に見えてしまう余地が残っていました。
- この弱点は技術・自然科学の観点で重大です。なぜなら、EEG/BCI の現実の壁は、単純な分類能だけではなく、state fluctuation、session drift、subject variability、recalibration burden が別々に効くことだからです。

## 主要な批判点

### 1. 旧 `datasets.md` は split unit を説明していたが、evaluation family を読解ルールとして前面化できていませんでした

- 問題:
  - 旧版には `within-session / cross-session / cross-subject` という語はありました。
  - しかし、それぞれが `別の科学的問い` であり、同じ accuracy として横並びにできないことが、本文の主節として固定されていませんでした。
- 根拠:
  - MOABB の公式 docs は `WithinSessionEvaluation`、`CrossSessionEvaluation`、`CrossSubjectEvaluation` を別クラスとして実装しています。
  - `WithinSessionEvaluation` は同一 session 内の k-fold です。
  - `CrossSessionEvaluation` は同一 subject の別 session をまたぐ評価です。
  - `CrossSubjectEvaluation` は 1 subject を hold-out し、残りの subject で学習する評価です。
- 修正:
  - `datasets.md` に `2.5) 同じ score でも、汎化の階段が違えば意味が変わります` を追加しました。
  - `evaluation family / hold-out 単位 / 言えること / 止める誤読` の 4 列で表を新設し、score 単独の誤読を止める形にしました。

### 2. 旧サイトは same-day score と cross-day 劣化の距離を、一次文献の数字で示していませんでした

- 問題:
  - 旧版では `cross-session は難しい` という方向性は出ていましたが、どの程度落ちるのかが入口ページでは定量化されていませんでした。
- 根拠:
  - Ma et al. (2022) は、5 日間・25 subject の motor imagery dataset で、subject-specific の平均 accuracy が `within-session 68.8%` から `cross-session 53.7%` へ落ちることを示しました。
  - 同論文では、少量の target-session data を使う cross-session adaptation で `78.9%` まで回復することも示しています。
  - ここから直接言えるのは、`same-day separation`、`別日耐性`、`再較正込みの運用` は別の評価である、ということです。
- 修正:
  - `datasets.md` と `eeg_101.md` に上記の数値を追加し、`高 score` を見る際に `hold-out 条件` と `adaptation の有無` を同時に読む site rule を明文化しました。

### 3. 旧 `eeg_101.md` は artifact と inverse problem を丁寧に扱っていたが、state confound と long-term nonstationarity を入口では弱くしか扱っていませんでした

- 問題:
  - 旧版は source imaging ceiling と preprocessing gate をかなり厳密に扱っていました。
  - しかし、same-day score がその日の state や movement を拾っている可能性、あるいは別日で崩れる可能性を、独立節として前面化していませんでした。
- 根拠:
  - Musall et al. (2019) は、cortex-wide activity が uninstructed movements に強く支配されうることを示しました。
  - Wilson et al. (2025) は、intracortical BCI において accumulated neural nonstationarity のため frequent recalibration が必要になることを示しました。
  - modality は違っても、`same-day decoding success` と `long-term operational stability` が別問題である点は、EEG を読む側にも重要な lesson です。
- 修正:
  - `eeg_101.md` に `同じ decoding score でも、読んでよい範囲は違います` 節を追加しました。
  - `within-session / cross-session / cross-subject / longitudinal closed-loop` を 4 行の表で固定し、各行に `ここで主に見ているもの` と `まだ言えないこと` を明示しました。

### 4. 旧公開ページは recalibration を「改善策」としては示していたが、「性能の一部」としては十分固定していませんでした

- 問題:
  - 旧版には drift や recalibration burden の論点が wiki や FAQ にはありましたが、EEG 入口ページと datasets 入口ページでは補助的な位置づけに留まっていました。
- 根拠:
  - Wilson et al. (2025) は、frequent recalibration が必要になること自体が運用上の壁であることを示しました。
  - したがって `adaptation で戻る` は朗報である一方、`最初から stable だった` ことは意味しません。
- 修正:
  - `datasets.md` では `cross-session adaptation` を独立行として追加し、`target session の少量データを使ったか` を最低報告項目へ昇格しました。
  - `eeg_101.md` では、`fixed decoder を何日 hold したか` と `recalibration burden` を確認項目へ追加しました。

## 今回実行した変更

- `datasets.md`
  - front matter の highlights / known points / wiki links を更新
  - `同じ score でも、汎化条件が違えば意味は変わります` の note を追加
  - `2.5) 同じ score でも、汎化の階段が違えば意味が変わります` 節を新設
  - MOABB docs、Ma et al. (2022)、Musall et al. (2019)、Wilson et al. (2025) を参考文献へ追加
- `eeg_101.md`
  - front matter の highlights / known / unknown / wiki links を更新
  - `高い score を見たとき、まず何を hold-out したかを見たいとき` の note を追加
  - `同じ decoding score でも、読んでよい範囲は違います` 節を新設
  - `よくある誤解` に `高い accuracy が出たので、別日や別人でも十分だ` を追加
  - MOABB docs、Ma et al. (2022)、Musall et al. (2019)、Wilson et al. (2025) を参考文献へ追加

## 外部依存で保留

- site-wide な score card schema の統一
  - 担当者: AI / maintainer
  - 前提条件: `evaluation family`、`hold-out unit`、`adaptation budget`、`recalibration burden` を datasets / verification / papers / FAQ で共通属性にすること
  - 完了条件: score が公開される全ページで、少なくとも上記 4 属性が必ず併記されること

## 参考文献

- Jayaram V, Barachant A. MOABB: trustworthy algorithm benchmarking for BCIs. *Journal of Neural Engineering*. 2018.
  - https://doi.org/10.1088/1741-2552/aadea0
- MOABB Docs: WithinSessionEvaluation
  - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.WithinSessionEvaluation.html
- MOABB Docs: CrossSessionEvaluation
  - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSessionEvaluation.html
- MOABB Docs: CrossSubjectEvaluation
  - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSubjectEvaluation.html
- Ma J, Yang B, Qiu W, et al. A large EEG dataset for studying cross-session variability in motor imagery brain-computer interface. *Scientific Data*. 2022.
  - https://doi.org/10.1038/s41597-022-01647-1
- Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
  - https://doi.org/10.1038/s41593-019-0502-4
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
