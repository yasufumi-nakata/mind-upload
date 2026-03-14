# Site Deepening Audit (2026-03-15, Dataset Annotation Fidelity / Leakage Units)

## 対象

- 主対象: `datasets.md`
- 副対象: `wiki/event-sync-and-measurement-logs.md`
- 副対象: `wiki/dataset-splits-and-leakage.md`

## 今回の選定理由

- `datasets.md` は 2026-03-14 時点で、version pin、BIDS、loader、benchmark harness の分離まではかなり整理できていました。
- しかし、スターターデータ 4 件の説明はなお `使いやすさ` と `一般的な注意点` に重心があり、`ラベルがどこから来たか`、`どの時間粒度で付いたか`、`何を独立な split 単位とみなすべきか` が十分に固定されていませんでした。
- この弱点は技術・自然科学の観点で重大です。なぜなら、同じ `EEG dataset` でも、cue-locked event、expert interval annotation、manual hypnogram、report-derived label は情報論的に別物であり、ここを曖昧にしたまま score を比べると benchmark の意味が壊れるからです。

## 主要な批判点

### 1. 旧 `datasets.md` は dataset 名を並べていましたが、annotation provenance を実務の主軸に置けていませんでした

- 問題:
  - 旧版は `EEG Motor Movement/Imagery`、`CHB-MIT`、`Sleep-EDF`、`TUH EEG` の向き不向きは説明していました。
  - しかし、`cue-locked annotation channel`、`expert seizure interval`、`manual hypnogram`、`report-derived clinical label` の違いが表で固定されていませんでした。
- 根拠:
  - EEG Motor Movement/Imagery は、annotation channel / `.event` に T0/T1/T2 を持つ cue-locked task です。
  - CHB-MIT は、summary / `.seizure` による long-recording seizure annotation を持ち、さらに `chb21` が `chb01` と同一被験者です。
  - Sleep-EDF Expanded は、well-trained technicians による Rechtschaffen & Kales hypnogram と 1 Hz event marker を持ちます。
  - TUH EEG Corpus は patient / session hierarchy と de-identified clinician report `.txt` を持ち、TUSZ は report keyword search と algorithmic triage を用いた selection を含みます。
- 修正:
  - `datasets.md` に `ラベル / イベントの出どころ` と `時間忠実度` を独立列に持つ表を追加しました。
  - 併せて、各行に `ここで止める主張` と `最低限の運用ルール` を付け、本サイトの claim ceiling を固定しました。

### 2. 旧サイトは `観測ログ` を event marker や timing に寄せすぎており、label provenance を log として扱っていませんでした

- 問題:
  - `wiki/event-sync-and-measurement-logs.md` は raw EEG だけでは足りないことを説明していましたが、主として marker / sync / bad segment の話でした。
  - そのため、`manual scoring` や `report-derived label` を、後から復元不能な観測ログとして扱えていませんでした。
- 根拠:
  - Sleep-EDF では sleep stage 自体が manual hypnogram であり、scoring manual を失うと label の意味が変わります。
  - TUH / TUSZ では report text と report-derived triage が付属し、signal-only benchmark と multimodal benchmark を分離しなければ leakage risk が残ります。
- 修正:
  - `wiki/event-sync-and-measurement-logs.md` に `ラベルの出どころは 4 種類に分けて読む` 節を追加しました。
  - `annotation channel / expert interval / manual hypnogram / report-derived label` を並べ、それぞれに必要な補助ログを対応づけました。

### 3. 旧 `dataset-splits-and-leakage` は一般論としては正しいが、dataset 固有の独立単位を固定できていませんでした

- 問題:
  - 旧版は subject / session / time split の原則を説明していましたが、各スターターデータで `本当の独立単位` が何かを明示していませんでした。
  - このため、例えば `CHB-MIT は file 単位で十分`、`Sleep-EDF は epoch をシャッフルしてよい`、`TUH は segment split でよい` と読める余地が残っていました。
- 根拠:
  - CHB-MIT は `chb21` = `chb01` の同一被験者という例外を含みます。
  - Sleep-EDF は subject-night 構造を持ち、same-night hypnogram continuity が強い情報を持ちます。
  - TUH EEG / TUSZ は patient / session hierarchy を持ち、report text が session-level covariate になりえます。
- 修正:
  - `wiki/dataset-splits-and-leakage.md` に、4 datasets の `独立単位`、`ありがちな誤分割`、`なぜ漏れるか`、`安全側の分け方` を追加しました。
  - 併せて、`独立 ID`、`report 使用`、`label manual` を最低報告項目へ追加しました。

### 4. Sleep-EDF の manual scoring を、現代の sleep benchmark と同列に読める余地がありました

- 問題:
  - 旧版は Sleep-EDF を状態遷移学習の良い入口として紹介していましたが、R&K scoring と AASM scoring の差を運用上の gate にしていませんでした。
- 根拠:
  - Sleep-EDF Expanded は R&K に基づく manual scoring です。
  - Moser et al. (2009) は、AASM と R&K の sleep classification が一致しない部分を示しました。
- 修正:
  - `datasets.md` と 2 本の wiki に、`R&K -> AASM mapping rule を書かずに cross-dataset 比較しない` site rule を追加しました。

## 今回実行した変更

- `datasets.md`
  - `last_updated` を 2026-03-15 に更新
  - `annotation provenance` を front matter と本文へ追加
  - `ラベル / イベントの出どころ`、`時間忠実度`、`止める主張`、`最低限の運用ルール` の表を追加
  - checklist に `注釈 provenance` を追加
- `wiki/event-sync-and-measurement-logs.md`
  - `last_updated` と front matter を更新
  - `label provenance` を event log と同格に扱う方針へ改稿
  - 4 種の label type とスターターデータ別 logging rule を追加
  - 参考文献節を追加
- `wiki/dataset-splits-and-leakage.md`
  - `last_updated` と front matter を更新
  - dataset 固有の独立単位表を追加
  - `report usage` と `label manual` を最低報告項目へ追加
  - 参考文献節を追加

## 外部依存で保留

- site-wide な dataset card schema の統一
  - 担当者: AI / maintainer
  - 前提条件: ほかの dataset / benchmark ページでも `annotation provenance` `time fidelity` `split unit` `claim ceiling` を共通属性として扱うこと
  - 完了条件: 公開データ紹介ページで、dataset 名だけでなく上記 4 属性が常に前面に出ること

## 参考文献

- PhysioNet: EEG Motor Movement/Imagery Dataset
  - https://physionet.org/content/eegmmidb/1.0.0/
- PhysioNet: CHB-MIT Scalp EEG Database
  - https://physionet.org/content/chbmit/1.0.0/
- PhysioNet: Sleep-EDF Database Expanded
  - https://physionet.org/content/sleep-edfx/1.0.0/
- Obeid I, Picone J. The Temple University Hospital EEG Data Corpus. *Front Neurosci*. 2016.
  - https://doi.org/10.3389/fnins.2016.00196
- Shah V, von Weltin E, Lopez S, et al. The Temple University Hospital Seizure Detection Corpus. *Front Neuroinform*. 2018.
  - https://doi.org/10.3389/fninf.2018.00083
- Moser D, Anderer P, Gruber G, et al. Sleep classification according to AASM and Rechtschaffen & Kales: effects on sleep scoring parameters. *Sleep*. 2009.
  - https://pubmed.ncbi.nlm.nih.gov/19238800/
