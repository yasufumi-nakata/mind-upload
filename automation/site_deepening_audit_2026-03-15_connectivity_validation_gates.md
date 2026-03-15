# Site Deepening Audit (2026-03-15, EEG Connectivity / Validation Gates and Reference Integrity)

## 対象

- 主対象: `perspective.md`
- 副対象: `wiki/observation-to-estimation.md`
- 関連修正: `wiki/eeg-preprocessing-and-qc.md`, `wiki/eeg-basics.md`, `tech_roadmap.md`

## 今回の選定理由

- 2026-03-15 時点で、公開サイトの `measurement ceiling`、`observability`、`maintenance-state`、`decode/emulate` はかなり整理されていました。
- その一方で、`perspective.md` の Issue #47 はなお `ASR + ZapLine + wPLI / STE` が事実上の既定解のように読める構造を残していました。
- これは技術・自然科学の観点で弱点です。なぜなら、artifact suppression、lagged connectivity、directed connectivity、direct validation は同じ階層の達成ではないからです。
- とくに `wPLI を使えば volume conduction を処理できた`、`directed metric を使えば causality に一歩近づいた` という読まれ方は、一次文献が支持する強さを越えます。

## 主要な批判点

### 1. 旧 Issue #47 は、手法名を evidence gate より前に置いていました

- 問題:
  - 旧 `perspective.md` は、ASR、ZapLine、wPLI、STE を 1 つの推奨パッケージのように並べていました。
  - そのため、読者が `どの条件でその metric が使えるのか` より先に、`その metric を選べばよい` と誤読しやすい構造でした。
- 根拠:
  - Vinck et al. (2011) が示したのは、wPLI が volume-conduction、noise、sample-size bias を**減らす候補**だという点です。完全解決ではありません。
  - Haufe et al. (2013) の simulation study は、directed connectivity measures が source mixing 条件で食い違いうることを示しました。
- 修正:
  - `perspective.md` の Issue #47 を、`method package` ではなく `connectivity validation gate` として再構成しました。
  - `ASR / ZapLine は候補`, `wPLI は候補`, `STE / Granger / DTF / model-based connectivity は候補` であり、採否は別監査で決めると明記しました。

### 2. lagged metric を leakage immunity のように読める余地が残っていました

- 問題:
  - 旧記述では、wPLI が `体積伝導の問題に対処する` と直線的に読めました。
- 根拠:
  - Zhang et al. (2020) は、scalp EEG functional network analysis が reference choice で変わることを示しました。
  - Palva et al. (2018) は、source reconstruction 後にも ghost interaction が残りうると警告しました。
- 修正:
  - `perspective.md` と `wiki/eeg-preprocessing-and-qc.md` に、`lagged metric を使っても reference 依存性と ghost interaction は別問題として残る` と明記しました。
  - `wiki/observation-to-estimation.md` に `connectivity は localization の次の段です` 節を追加し、sensor-space / source-space / directed connectivity を分離しました。

### 3. directed connectivity を localization の延長で読ませていました

- 問題:
  - 旧 site では、ESI の次に directed metric を足すと、そのまま causal mechanism に近づいたように見える余地がありました。
- 根拠:
  - Haufe et al. (2013) は、measure ごとの結論が source mixing で不安定になりうることを示しました。
  - Papadopoulou et al. (2019) は、同時 cortical recording と reconstructed source の controlled comparison で qualitative な一致を示しましたが、これは tightly controlled な 1 系での construct validation です。
  - Hao et al. (2025) は simultaneous SEEG/HD-EEG で validation route を前進させましたが、drug-resistant epilepsy cohort であり、depth / power 依存性も残ります。
- 修正:
  - `wiki/observation-to-estimation.md` に、directed connectivity は `source localization より 1 段上の主張` であると明示しました。
  - `surrogate / null`, `family comparison`, `同時侵襲記録`, `held-out perturbation` のいずれかを通さない directed claim は exploratory に留める方針へ改めました。

### 4. Hao et al. (2025) の書誌情報が公開ページ内で一致していませんでした

- 問題:
  - 公開ページの一部で、DOI `10.1111/epi.18552` に対して旧題に近い `High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography` が残っていました。
- 根拠:
  - Crossref metadata と PubMed 掲載題名は `HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy` です。
- 修正:
  - `wiki/observation-to-estimation.md`
  - `wiki/eeg-basics.md`
  - `tech_roadmap.md`
  の公開ページで、題名と著者先頭表記を Crossref metadata に合わせて修正しました。

## 今回実行した変更

- `perspective.md`
  - Issue #47 を `前処理再現性と connectivity validation gate` へ改稿
  - `ASR / ZapLine / wPLI / directed metrics` を既定解ではなく候補群へ格下げ
  - reference / leakage / metric assumptions / external validation を別ゲートとして明記
  - 参考文献に Zhang (2020), Palva (2018), Haufe (2013), Papadopoulou (2019), Hao (2025) を追加
- `wiki/observation-to-estimation.md`
  - `last_updated` を 2026-03-15 に更新
  - page highlights / known / unknown を connectivity validation 寄りに更新
  - `connectivity は localization の次の段です` 節を新設
  - site rule に `connectivity を localization の延長と書かない` と `lagged / directed 指標を免罪符にしない` を追加
  - Hao (2025) の書誌情報を修正し、新規一次文献を追加
- `wiki/eeg-preprocessing-and-qc.md`
  - `lagged 指標でも読み替え禁止です` の note-box を追加
  - `connectivity claim card` を最低提出物へ追加
  - 誤読表へ `wPLI / directed metric を使ったので解決` を追加
  - Vinck (2011), Zhang (2020), Palva (2018), Haufe (2013) を参考文献へ追加
- `wiki/eeg-basics.md`
  - `last_updated` を 2026-03-15 に更新
  - Hao (2025) の参考文献題名と著者表記を修正
- `tech_roadmap.md`
  - Hao (2025) の参考文献題名と著者表記を修正

## 外部依存で保留

- source-space connectivity / directed connectivity の公開 benchmark 固定
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: 同時侵襲・非侵襲記録、source reconstruction 条件、parcellation、null/surrogate、perturbation log を同一 schema で比較できること
  - 完了条件: `sensor-space summary`、`source-space connectivity`、`directed/effective connectivity` を別評価軸で公開比較できる benchmark が整うこと

## 参考文献

- Vinck M, Oostenveld R, van Wingerden M, et al. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. *NeuroImage*. 2011.
  - https://doi.org/10.1016/j.neuroimage.2011.01.055
- Zhang L, Wang P, Zhang R, et al. The Influence of Different EEG References on Scalp EEG Functional Network Analysis During Hand Movement Tasks. *Front Hum Neurosci*. 2020.
  - https://doi.org/10.3389/fnhum.2020.00367
- Palva JM, Wang SH, Palva S, et al. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. *NeuroImage*. 2018.
  - https://doi.org/10.1016/j.neuroimage.2018.02.032
- Haufe S, Nikulin VV, Muller KR, Nolte G. A critical assessment of connectivity measures for EEG data: A simulation study. *NeuroImage*. 2013.
  - https://doi.org/10.1016/j.neuroimage.2012.09.036
- Papadopoulou M, Friston K, Marinazzo D. Estimating Directed Connectivity from Cortical Recordings and Reconstructed Sources. *Brain Topogr*. 2019.
  - https://doi.org/10.1007/s10548-015-0450-6
- Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
