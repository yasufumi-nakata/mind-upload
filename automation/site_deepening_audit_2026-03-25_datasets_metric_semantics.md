# Site Deepening Audit (2026-03-25, datasets metric semantics)

## 対象

- 主対象: `datasets.md`
- 関連対象: `wiki/dataset-splits-and-leakage.md`
- 範囲: 技術・自然科学のみ

## 今回この箇所を選んだ理由

- `datasets.md` と `wiki/dataset-splits-and-leakage.md` は、2026-03-25 時点で既に
  - split / leakage
  - acquisition-distribution shortcut
  - benchmark provenance / postmortem
  をかなり明確に止められる状態でした。
- しかし、なお残っていた弱点は `metric semantics` です。
  - 読者が rare-event task や class-imbalanced task を、依然として `accuracy` や `AUROC` のような単一 headline score で読んでしまう余地がありました。
  - これは seizure detection / seizure forecasting / sleep staging のような主要 EEG 実務で、そのまま性能解釈の誤読に直結します。
- したがって、次に深掘りすべき箇所は split でも benchmark provenance でもなく、`何をもって性能と読むのか` を固定する metric-layer でした。

## 根拠付き批判

### 1. 強い不均衡下では ROC や accuracy だけでは性能解釈が固定できません

- [Saito & Rehmsmeier (2015)](https://doi.org/10.1371/journal.pone.0118432) は、強い class imbalance では precision-recall plot の方が ROC plot より informative であることを示しました。

批判:

- したがって、rare-event EEG task を `AUROC が高い` だけで読むのは不十分です。
- 正例が稀な課題で ROC が見せる見かけ上の良さは、実運用で重要な precision / false alarms / minority-class collapse を隠しえます。

### 2. seizure task では「イベントを拾えたか」と「どれだけ誤警報を出したか」を同時に読まなければなりません

- [Roy et al. (2021)](https://doi.org/10.1016/j.ebiom.2021.103275) は、scalp EEG annotation 支援系の評価で sensitivity と false detections の両方を扱っています。
- [Scheuer et al. (2021)](https://doi.org/10.1097/WNP.0000000000000709) は、large seizure dataset 上で inter-reader agreement と algorithm assessment を比較し、event overlap と detection behavior の読みに単一 score では足りないことを示しています。
- [Segal et al. (2023)](https://doi.org/10.3389/fnins.2023.1184990) は、seizure prediction において false alarm rate 制御そのものが設計課題であることを示しました。

批判:

- よって seizure detection / forecasting を `accuracy` や `AUROC` の headline だけで記述するのは、技術的に甘いです。
- 最低でも `event sensitivity / recall`、`false alarms per hour or day`、`event-overlap rule`、必要なら `latency` と `calibration` を束として示さなければ、モデルの価値を誤読します。

### 3. sleep staging では pooled score が minority-stage failure を隠します

- [Sun et al. (2017)](https://doi.org/10.1093/sleep/zsx139) は large-scale automated sleep staging で Cohen's kappa を主要指標に置き、class imbalance が推定に効くことを明示しています。
- [Vallat & Walker (2021)](https://doi.org/10.7554/eLife.70092) は、自動 sleep staging の中でも N1-stage が弱点になりやすいことを示しています。

批判:

- したがって sleep staging を単一 accuracy で読むのは危険です。
- `Cohen's kappa` や `macro-F1`、さらに `per-stage recall / F1` と confusion matrix を出さなければ、特に N1 のような弱い stage failure を隠したまま「高性能」と読めてしまいます。

## 今回実行した変更

- `datasets.md`
  - front matter の `page_highlights` と `known_points` に、metric semantics を独立 stop line として追加しました。
  - `2026-03-25 addendum: metric semantics are part of the benchmark` note-box を追加しました。
  - task family ごとの minimum metric bundle table を追加し、
    - cue-locked classification / decoding
    - seizure detection / forecasting
    - sleep staging
    それぞれで最低限読むべき指標束を固定しました。
  - `benchmark-mindset` checklist に `Metric bundle` 項目を追加しました。
  - 参考文献に metric-semantics 系の一次ソースを追加しました。
- `wiki/dataset-splits-and-leakage.md`
  - `Metric semantics are also part of leak-resistant reporting` note-box を追加しました。
  - report checklist に `Metric bundle` 項目を追加しました。
  - 参考文献に同論点の一次ソースを追加し、本文と references を整合させました。

## 今回修正しないもの

- 哲学 / 法学 / personhood 論点
  - ユーザー指示どおり対象外です。
- `issue.md`
  - ユーザー指示どおり確認していません。

## 外部依存で保留

- なし
  - 今回の作業は repo 内文書更新、検証、commit、push までで完結できます。

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
7. Wong JCH, O'Mara B, Yee NW, et al. A review of machine learning applications for the classification and detection of epileptic seizures in electroencephalography. *Epilepsia Open*. 2023.
   - https://doi.org/10.1002/epi4.12704
