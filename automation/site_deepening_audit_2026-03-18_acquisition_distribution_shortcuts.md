# Site Deepening Audit (2026-03-18, Acquisition-Distribution Shortcuts in EEG)

## 対象

- 主対象: `datasets.md`
- 副対象: `eeg_101.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`subject/session fingerprint`、`movement / EOG / EMG`、`feedback route` の整理をかなり強くできていました。
- その一方で、実務入口である `datasets.md` と `eeg_101.md` では、`site / device / reference system / electrode layout / protocol distribution` が独立の shortcut family としてはまだ弱く、`dataset metadata` の話に吸収されやすい状態でした。
- これは技術・自然科学の観点で重要です。なぜなら EEG では、同じ課題ラベルでも、参照法・電極配置・アンプ・サンプリング・フィルタ・施設差によって観測される波形そのものが変わりうるからです。そのため、`高スコア` を `target neural variable を読めた` と言う前に、`recording distribution を読んだだけではないか` を止める必要があります。

## 主要な批判点

### 1. 旧 site は `subject/session fingerprint` を前景化した一方、`acquisition-distribution shortcut` を入口で独立扱いしていませんでした

- 問題:
  - `verification.md` の深い箇所では `subject / session / site / device` が既に出ていました。
  - しかし `datasets.md` と `eeg_101.md` の入口説明では、読者が依然として `device や reference は背景条件` と読める状態でした。
- 根拠:
  - Hu et al. (2018) は reference montage と electrode setup が scalp EEG potentials 自体を変えることを示しました。
  - Melnik et al. (2017) は EEG differences に system / subject / session がそれぞれ寄与することを示しました。
- 批判:
  - したがって、`who/when` だけでなく `how/where/with-what-setup` も shortcut family として切り出さなければ、入口の科学的防波堤として不十分でした。

### 2. 旧 `Datasets` の一般化説明は `within/cross-session/cross-subject/adaptation` を分けていても、`acquisition distribution` の hold-out を十分要求していませんでした

- 問題:
  - `datasets.md` は generalization family を丁寧に整理していました。
  - しかし site / device / reference system / electrode layout / protocol をまたいだ disjointness や harmonization log は必須提出物として固定されていませんでした。
- 根拠:
  - Xu et al. (2020) は cross-dataset EEG decoding における environmental variability として amplifier, cap, sampling rate, filtering, experiment context を挙げています。
  - Ceballos-Villegas et al. (2022) は 9 か国・14 研究・12 デバイスに跨る qEEG batch effects を調和させるための統計的補正を提示しました。
- 批判:
  - これは `different people` と `different recording distributions` が別の一般化障壁であることを意味します。
  - したがって、cross-subject のみを言っても `cross-device` や `cross-reference` を自動では保証しませんでした。

### 3. 旧 site は `harmonization` を foundation-model 側では触れていても、starter dataset 側の最低運用ルールに落とし切れていませんでした

- 問題:
  - `wiki/eeg-foundation-models.md` には channel/reference/sample-rate harmonization の規律がありました。
  - しかし public 実務ページである `datasets.md` の dataset card には、そのルールがまだ完全には降りていませんでした。
- 根拠:
  - Dong et al. (2024) は different channel locations を持つ scalp EEG を comparative study のために変換する処理自体が必要だと示しました。
  - Engemann et al. (2022) は複数国・複数文脈の M/EEG cohort を跨いだ benchmark を提示し、cross-context comparability を benchmark design の一部にしています。
- 批判:
  - つまり `foundation model だけ harmonization が必要` なのではなく、starter dataset の比較段階から harmonization log が必要でした。

### 4. 旧 `Verification` と `Roadmap` は `site/device` を示していても、`reference system / electrode layout / protocol` を fingerprint audit の中心項目に据えていませんでした

- 問題:
  - `verification.md` の Specificity & Shortcut Card は有用でしたが、読者が `reference system` や `electrode layout` を `nuisance log` ではなく `前処理メモ` と誤読する余地がありました。
  - `tech_roadmap.md` の R6 も、主に `subject/session fingerprint` に焦点が当たっていました。
- 根拠:
  - Hu et al. (2018)、Melnik et al. (2017)、Xu et al. (2020)。
- 批判:
  - そのため site-wide ルールとしては、`fingerprint audit` を `fingerprint / acquisition-distribution audit` に広げる必要がありました。

## 今回実行した変更

- `datasets.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points を `acquisition-distribution shortcut` まで拡張
  - `generalization-families` 節に acquisition-distribution shortcut の addendum を追加
  - dataset card の site rule に `site / device / reference-system / electrode-layout disjointness` と harmonization log を追加
  - starter dataset card の必須項目へ `acquisition-distribution summary plus harmonization policy` を追加
  - BIDS note に `BIDS does not auto-harmonize cross-cohort setup differences` を明記
- `eeg_101.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points を `site / device / reference / electrode layout / protocol` まで拡張
  - 入口 note と本文を改稿し、setup differences を measurement condition の一部として扱う site rule を追加
- `verification.md`
  - page highlights / known points を `acquisition-distribution shortcut` まで更新
  - Specificity & Shortcut Card を `fingerprint / acquisition-distribution audit` に拡張
  - `reference system / electrode layout / protocol` を card の独立必須項目として追加
  - acquisition-distribution shortcut の addendum を追加
- `tech_roadmap.md`
  - page highlights / known points に `setup shortcut` を追加
  - `R6` の addendum と deliverables を `site / device / reference-system / electrode-layout` まで拡張

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・監査規則・ロードマップ記述の改稿で完結しています。

## 参考文献

1. Hu S, Stead M, Dai Q, Worrell GA. How do reference montage and electrodes setup affect the measured scalp EEG potentials? *Journal of Neural Engineering*. 2018.
   - https://doi.org/10.1088/1741-2552/aacfe4
2. Melnik A, Legkov P, Izdebski K, et al. Systems, Subjects, Sessions: To What Extent Do These Factors Influence EEG Data? *Frontiers in Human Neuroscience*. 2017;11:150.
   - https://doi.org/10.3389/fnhum.2017.00150
3. Xu M, Fanton S, Jahanbekam A, et al. The Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. *Frontiers in Human Neuroscience*. 2020;14:103.
   - https://doi.org/10.3389/fnhum.2020.00103
4. Ceballos-Villegas JA, Bosch-Bayard J, Galan-Garcia L, et al. Harmonized multinational qEEG norms (HarMNqEEG): A multinational qEEG normative database with harmonized EEG norms. *Brain and Behavior*. 2022;12(11):e2789.
   - https://doi.org/10.1002/brb3.2789
5. Engemann DA, Kozynets O, Sabbagh D, et al. A reusable benchmark of brain-age prediction from M/EEG resting-state signals. *NeuroImage*. 2022;262:119521.
   - https://doi.org/10.1016/j.neuroimage.2022.119521
6. Dong Z, Chen J, Zhang C, et al. Transforming scalp EEGs with different channel locations by REST for comparative study. *Brain Research Bulletin*. 2024;210:110906.
   - https://doi.org/10.1016/j.brainresbull.2024.110906
