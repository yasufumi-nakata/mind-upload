# Site Deepening Audit (2026-03-15, Event Fidelity / Semantics / Synchronization)

## 対象

- 主対象: `wiki/event-sync-and-measurement-logs.md`
- 副対象: `datasets.md`
- 補助対象: `wiki/standards-repositories-validators-and-benchmarks.md`

## 今回の選定理由

- 技術・自然科学の観点で、現行サイトの次の弱点は `event sync / annotation fidelity` だと判断しました。
- 理由は、現行本文が「イベントと同期が重要」とは正しく述べていても、`時刻の器`、`イベント意味論`、`clock alignment`、`device-side delay` をまだ十分に分離できていなかったためです。
- この弱点は入口実務に直結します。波形とラベルが公開されていても、イベント意味論と時計系が曖昧なら、EEG の強みである時間忠実度そのものが崩れるからです。

## 主要な批判点

### 1. 旧ページは `events.tsv` を event fidelity 全体と近いものとして読ませる余地がありました

- 問題:
  - 現行の `wiki/event-sync-and-measurement-logs.md` は event marker と label provenance の重要性を正しく述べていましたが、`BIDS task events` が与えるのは主に時刻と列の器であり、cross-study 比較に必要な意味論そのものではないことを十分に前面化できていませんでした。
  - そのため、`events.tsv` があるだけで event semantics まで固定されたと誤読する余地が残っていました。
- 根拠:
  - BIDS の task events 仕様は `events.tsv` と sidecar JSON による記述枠を与えます。
  - Robbins et al. (2021) は、既存の時系列データ標準だけでは event description に重要な details が欠けやすく、HED が FAIR な event annotation を補うと示しました。
  - Hermes et al. (2025) は、HED library schema により EEG data annotation を machine-actionable に整理できることを示しました。
- 修正:
  - `wiki/event-sync-and-measurement-logs.md` に `イベント忠実度は 3 層で監査します` 節を追加し、`時間アンカー / イベント意味論 / 同期と輸送` を分離しました。
  - 同ページの EEG-BIDS 節に `events.json と HED` を追加しました。

### 2. 旧ページは LSL の有効範囲を十分に切り分けていませんでした

- 問題:
  - 現行ページは遅延・ジッタ・ドリフトを説明していましたが、LSL のような同期ミドルウェアが何を解決し、何を解決しないかが十分に書かれていませんでした。
  - そのため、LSL や trigger があるだけで hardware delay まで ground-truth 化されたように読める構造が残っていました。
- 根拠:
  - Kothe et al. (2025) は、LSL がネットワーク遅延・ジッタを扱い millisecond precision の recording を支える一方、input device の throughput delay や on-device processing delay は software timestamps だけでは推定・補正できないことを明記しました。
- 修正:
  - `wiki/event-sync-and-measurement-logs.md` に `LSL は有力ですが、hardware ground truth ではありません` 節を追加しました。
  - `timestamp domain`、`device-side delay`、`drift / resync policy`、`validation method` を別ログとして残す site rule を明記しました。
  - `wiki/standards-repositories-validators-and-benchmarks.md` にも、LSL は同期ミドルウェアであって BIDS や benchmark の代替ではないことを追加しました。

### 3. 旧 datasets 導線は annotation provenance を重視していましたが、event semantics と sync evidence を dataset card の必須欄として固定していませんでした

- 問題:
  - `datasets.md` はラベル provenance と時間粒度をかなり明確にしていましたが、dataset card の最小提出物として `clock domain`、`delay / jitter audit`、`event semantics` をまだ必須欄にしていませんでした。
  - これでは、dataset 名とラベル由来だけを揃えても、時間忠実度の監査が抜ける余地がありました。
- 根拠:
  - BIDS EEG と EEG-BIDS は共有可能な metadata の床を与えますが、event semantics と clock audit を追加しなければ time-aligned benchmark には不十分です。
  - Motion-BIDS (Jeung et al., 2024) は、追加モダリティでは metadata と coordinate frame が解釈の中核であることを示しました。
- 修正:
  - `datasets.md` に `Event Fidelity Card` 注記を追加しました。
  - dataset card の site rule を `provenance / time grain / clock domain と sync evidence / event semantics / split unit / stop claim` の 6 項目へ拡張しました。

### 4. 旧 standards ページは BIDS・repository・validator・benchmark の区別はできていましたが、`event semantics` と `synchronization middleware` の層が抜けていました

- 問題:
  - `wiki/standards-repositories-validators-and-benchmarks.md` は 5 層整理として有用でしたが、2026-03 時点の実務では、BIDS の器、HED / Motion-BIDS の意味論、LSL の同期を別層として扱う必要があります。
- 修正:
  - 同ページの operational stack を 7 層へ更新しました。
  - `HED / Motion-BIDS` を `イベント意味論 / 拡張 schema`、`LSL` を `同期ミドルウェア` として追加しました。
  - `ありがちな混同` 表へ、`events.tsv があるので semantics まで固定された` と `LSL を使ったので hardware 遅延まで解決した` を追記しました。

## 今回実行した変更

- `wiki/event-sync-and-measurement-logs.md`
  - イベント忠実度を 3 層に分ける節を追加
  - LSL の有効範囲と限界を説明する節を追加
  - EEG-BIDS 節に `events.json + HED`、`clock / sync log`、`*_coordsystem.json` を追加
  - `Event Fidelity Card` を site rule として追加
  - 参考文献を BIDS / HED / LSL / Motion-BIDS まで拡張
- `datasets.md`
  - `raw EEG があるだけでは足りない` 節を更新
  - `Event Fidelity Card` 注記を追加
  - dataset card の必須欄を 6 項目へ拡張
  - 参考文献に BIDS task events、HED、LSL、Motion-BIDS を追加
- `wiki/standards-repositories-validators-and-benchmarks.md`
  - 5 層整理を 7 層整理へ更新
  - HED / Motion-BIDS / LSL を別層として追加
  - ありがちな混同表へ 2 行を追加

## 外部依存で保留

- hardware delay を含む site-wide event fidelity template の実測運用
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: photodiode、loopback、TTL などの測定経路を実機で運用できること
  - 完了条件: EEG + stimulus + motion の各実験 run について、clock domain、device-side delay、validation method を同一テンプレートで残せること

## 参考文献

- BIDS Specification. Task events.
  - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html
- BIDS Specification. Electroencephalography.
  - https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Sci Data*. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Robbins KA, Truong D, Jones P, et al. Building FAIR functionality: annotating events in time series data using Hierarchical Event Descriptors (HED). *Neuroinformatics*. 2021.
  - https://doi.org/10.1007/s12021-021-09513-7
- Hermes D, et al. HED library schema for EEG data annotation. *Sci Data*. 2025.
  - https://doi.org/10.1038/s41597-025-05791-2
- Kothe CA, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
  - https://doi.org/10.1162/imag_a_00136
- Jeung S, et al. Motion-BIDS, an extension to the brain imaging data structure for motion data. *Sci Data*. 2024.
  - https://doi.org/10.1038/s41597-024-03559-8
