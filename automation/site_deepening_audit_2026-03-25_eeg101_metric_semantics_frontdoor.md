# Site Deepening Audit (2026-03-25, EEG 101 metric-semantics front door)

## 対象

- 主対象: `eeg_101.md`
- 同期対象: `summary_booklet.md`
- 範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `datasets.md` と `wiki/dataset-splits-and-leakage.md` では、2026-03-25 時点ですでに
  - `metric semantics are part of the benchmark`
  - `task-matched metric bundle`
  - `seizure = sensitivity + false alarms + overlap`
  - `sleep staging = macro/per-stage agreement`
  という stop line がかなり明確でした。
- しかし入口ページである `eeg_101.md` は、なお
  - `same score can mean different things`
  - `features and metrics`
  という一般論に留まり、`accuracy` や `AUROC` をどこで止めるのかを front door では固定していませんでした。
- これは public-spec inconsistency です。最初に読まれる EEG primer が metric semantics を固定しないと、読者は `high accuracy` をそのまま `strong EEG evidence` と読めてしまい、実務ページで止めている規律が入口で緩みます。

## 根拠付き批判

### 1. class imbalance 下で ROC や accuracy だけでは性能解釈が固定できません

- [Saito & Rehmsmeier (2015)](https://doi.org/10.1371/journal.pone.0118432) は、強い不均衡では precision-recall の方が ROC より informative であることを示しました。

批判:

- したがって EEG primer が `score` を一般語のままにしておくのは弱いです。
- rare-event EEG task で `AUROC が高い` だけを読むと、precision 崩壊や false-alarm burden を見落としたまま強い結果に見えてしまいます。

### 2. seizure task は event sensitivity と false alarms を束で読まなければなりません

- [Roy et al. (2021)](https://doi.org/10.1016/j.ebiom.2021.103275) は scalp EEG seizure detection を `high sensitivity and low false alarm rates` の trade-off として評価しました。
- [Scheuer et al. (2021)](https://doi.org/10.1097/WNP.0000000000000709) は large dataset で seizure marking を比較し、`pairwise sensitivity` と `false-positive rate` を event overlap 付きで評価しました。
- [Segal et al. (2023)](https://doi.org/10.3389/fnins.2023.1184990) は seizure prediction で false-alarm control 自体が設計対象になることを示しました。

批判:

- よって seizure detection / forecasting を `accuracy` や `AUROC` の headline だけで読むのは技術的に甘いです。
- EEG primer がこの stop line を持たないと、臨床寄りタスクで最も危険な誤読を入口で止められません。

### 3. sleep staging は pooled accuracy だけでは stage failure と bias を隠します

- [Sun et al. (2017)](https://doi.org/10.1093/sleep/zsx139) は large-scale automated sleep staging で Cohen's kappa を主要指標に置き、stage proportion imbalance が性能推定に効くことを示しました。
- [Vallat & Walker (2021)](https://doi.org/10.7554/eLife.70092) は N1 と stage transitions が accuracy を下げやすいことを示しました。
- [Dei Rossi et al. (2026)](https://doi.org/10.1038/s41746-025-02237-2) は、sleep staging で macro-F1、consensus agreement、out-of-domain generalization、demographic / clinical bias を同時に監査し、global accuracy 改善だけでは bias が消えないことを示しました。

批判:

- したがって sleep staging を単一 accuracy で読むのは不十分です。
- EEG primer に `Cohen's kappa / macro-F1 / per-stage / subgroup slices` が見えないままだと、N1 failure や clinical-subgroup bias を hidden error のまま放置します。

## 今回実行した変更

- `eeg_101.md`
  - `last_updated` を `2026-03-25` に更新しました。
  - front matter の `page_highlights` と `known_points` に、metric semantics を独立 stop line として追加しました。
  - 冒頭に `Metric semantics are part of the EEG claim` note-box を追加し、
    - class imbalance
    - seizure evaluation
    - sleep-staging stage / bias evaluation
    を一次文献つきで front door に固定しました。
  - primer 向けの `task family -> minimum metric bundle -> overreading stopped` table を追加しました。
  - pipeline の `Features and metrics` を `Features and metric bundle` に変更し、単一 headline score を避ける site rule を明文化しました。
  - references に Saito, Roy, Scheuer, Segal, Sun, Vallat & Walker, Dei Rossi を追加しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成し、EEG 101 の front-matter 更新を冊子へ同期します。

## 今回修正しないもの

- 哲学 / 法学 / personhood
  - ユーザー指示どおり対象外です。
- `issue.md`
  - ユーザー指示どおり確認していません。
- glossary の全面整理
  - 今回の主問題は entry EEG page の stop line 欠落であり、用語集全体の再編までは不要と判断しました。

## 外部依存で保留

- なし
  - 今回の作業は repo 内の公開本文修正、冊子再生成、build、commit、push までで完結できます。

## 参考文献

1. Saito T, Rehmsmeier M. The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets. *PLOS ONE*. 2015.
   - https://doi.org/10.1371/journal.pone.0118432
2. Roy Y, Banville H, Albuquerque I, et al. Evaluation of artificial intelligence systems for assisting neurologists with fast and accurate annotations of scalp electroencephalography data. *eBioMedicine*. 2021.
   - https://doi.org/10.1016/j.ebiom.2021.103275
3. Scheuer ML, Wilson SB, Antony A, et al. Seizure Detection: Interreader Agreement and Detection Algorithm Assessments Using a Large Dataset. *Journal of Clinical Neurophysiology*. 2021.
   - https://doi.org/10.1097/WNP.0000000000000709
4. Segal E, Goldental A, Gadot Y, et al. Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. *Frontiers in Neuroscience*. 2023.
   - https://doi.org/10.3389/fnins.2023.1184990
5. Sun H, Jia J, Goparaju B, et al. Large-Scale Automated Sleep Staging. *Sleep*. 2017.
   - https://doi.org/10.1093/sleep/zsx139
6. Vallat R, Walker MP. An open-source, high-performance tool for automated sleep staging. *eLife*. 2021.
   - https://doi.org/10.7554/eLife.70092
7. Dei Rossi A, Metaldi M, Bechny M, et al. SLEEPYLAND: trust begins with fair evaluation of automatic sleep staging models. *npj Digital Medicine*. 2026.
   - https://doi.org/10.1038/s41746-025-02237-2
