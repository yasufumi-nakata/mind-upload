# Site Deepening Audit (2026-03-15, L0 Artifact Pack / Provenance and Derivative Lineage)

## 対象

- 主対象: `wiki/l0-minimum-artifact-pack.md`
- 副対象: `wiki/eeg-to-l0-route.md`

## 今回の選定理由

- 2026-03-15 時点で、公開サイトは `annotation provenance`、`time fidelity`、`measurement stack`、`maintenance-state`、`direct validation` の整理がかなり進んでいました。
- その一方で、L0 実務導線はなお `dataset version + BIDS + QC + split + baseline + runbook` を中心とする説明に留まり、`raw と derivative の境界`、`machine-readable lineage`、`split manifest`、`実行環境 pin` が十分に前面化していませんでした。
- これは技術・自然科学の観点で弱点でございます。なぜなら、現行の一次文献と公式仕様がかなり明確に支持しているのは、「再利用可能な raw 入力」と「監査可能な processing lineage」を分けること、そして acquisition / preprocessing / reporting / sharing を曖昧にしないことだからです。

## 主要な批判点

### 1. 旧 `l0-minimum-artifact-pack` は runbook を重視していましたが、derivative lineage を成果物の中核に置けていませんでした

- 問題:
  - 旧ページは `実行手順` を要求していましたが、cleaned EEG、epochs、feature table、QC report がどの raw 入力とどの pipeline から出たかを、機械可読に追う要件が弱いままでした。
  - そのため、`runbook はあるが output lineage が無い` 状態でも、L0 完了に近く読める余地がありました。
- 根拠:
  - Gorgolewski et al. (2016) は BIDS を、入力実験データの構造化された共有形式として確立しました。
  - Pernet et al. (2019) は EEG-BIDS を通じて、EEG の raw data と metadata を再利用可能な形で残す床を示しました。
  - BIDS Specification の derivatives 節は、processing outputs を `DatasetType=derivative` の dataset として扱い、`GeneratedBy` と `SourceDatasets` を持たせる方針を明示しています。
- 修正:
  - `wiki/l0-minimum-artifact-pack.md` で `raw dataset identity` と `derivative lineage` を分離し、`GeneratedBy` / `SourceDatasets` / file-level lineage を L0 成果物へ昇格しました。
  - provenance 例として最小の `dataset_description.json` 例を追加しました。

### 2. 旧ページは `raw identity` と `run identity` を混ぜていました

- 問題:
  - 旧版は `dataset version` と `実行手順` を挙げていましたが、`どの raw 入力か` と `どの split / seed / command / environment で走らせたか` を独立の artifact として整理していませんでした。
  - これでは「同じデータを使った」と「同じ実験条件で評価した」が混ざります。
- 根拠:
  - COBIDAS-MEEG (Pernet et al., 2020) は acquisition、analysis、reporting、sharing を明示的に分けて残す必要を示しています。
  - BIDS Apps (Gorgolewski et al., 2017) は containerized neuroimaging pipelines により、実行環境の再現性を改善する設計を示しました。
- 修正:
  - `wiki/eeg-to-l0-route.md` に `raw identity`、`derivative identity`、`run identity` の 3 区分を追加しました。
  - ここで `container tag ないし lockfile`、`git commit`、`seed` を必須化した判断は、上記文献と仕様からの **推論** です。すなわち、仕様が単一の field 名として常に強制するわけではありませんが、L0 比較可能性の床としては必要だと本サイトは判断しました。

### 3. 旧 `EEGからL0までの一本道` は step 4 と step 5 の境界がまだ粗く、観測ログと lineage を分け切れていませんでした

- 問題:
  - 旧 route は `イベント同期と観測ログ` のあと `Hands-on` へ進む一本道を与えていましたが、そこで何を raw 側へ残し、何を derivative 側へ残すかが本文だけでは十分に固定されていませんでした。
  - そのため、`event semantics` と `processing provenance` が同じ箱の「付随情報」に見える構造でした。
- 根拠:
  - Robbins et al. (2021) と Hermes et al. (2025) は、event semantics を HED のような機械可読な形で残す重要性を示しました。
  - 一方で derivatives specification は、processing outputs の lineage を別の層で扱います。
- 修正:
  - `wiki/eeg-to-l0-route.md` の step 4 を `event semantics / label provenance / clock domain` に寄せ、step 5 を `derivative lineage / command provenance / environment pin` に寄せて分離しました。
  - これにより、`同じ label の意味を復元する` ことと `同じ output を再生成する` ことを別ゲートとして扱うよう改めました。

### 4. 旧 site は split manifest を第一級 artifact として押し上げていませんでした

- 問題:
  - 旧版には `分割規則` がありましたが、manifest や hash のような再現可能な単位が本文の主語になっていませんでした。
  - これでは score を出した後に分割が動いた場合の監査が弱くなります。
- 根拠:
  - COBIDAS-MEEG が求める透明な analysis / reporting と、本サイト既存の leakage rule を合わせると、単なる説明文ではなく再利用可能な split artifact が必要になります。これは COBIDAS-MEEG と本サイトの benchmark comparability rule からの **推論** です。
- 修正:
  - 両ページで `split manifest` と `test frozen rule` を明示し、score と同格の artifact として扱うよう更新しました。

## 今回実行した変更

- `wiki/l0-minimum-artifact-pack.md`
  - `last_updated` を 2026-03-15 に更新
  - `10 点 artifact pack` へ拡張
  - `raw / derivative / run provenance` を分離
  - `dataset_description.json` の provenance 例を追加
  - 参考文献節を新設
- `wiki/eeg-to-l0-route.md`
  - `last_updated` を 2026-03-15 に更新
  - step 4 を `event semantics / label provenance / clock domain` に更新
  - step 5 を `derivative lineage / command provenance / environment pin` に更新
  - `raw identity / derivative identity / run identity` の 3 区分を追加
  - 参考文献節を新設

## 外部依存で保留

- site-wide provenance schema の共通化
  - 担当者: AI / maintainer
  - 前提条件: `split manifest`、`GeneratedBy`、`SourceDatasets`、`container tag or lockfile`、`failure registry` を datasets / verification / hands-on 導線でも共通欄名にそろえること
  - 完了条件: L0 系ページならどこを読んでも、raw identity / derivative identity / run identity の 3 層で artifact を監査できること

## 参考文献

- Gorgolewski KJ, Auer T, Calhoun VD, et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. *Sci Data*. 2016.
  - https://doi.org/10.1038/sdata.2016.44
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Sci Data*. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. *Nat Neurosci*. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Gorgolewski KJ, Esteban O, Ellis DG, et al. BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods. *PLoS Comput Biol*. 2017.
  - https://doi.org/10.1371/journal.pcbi.1005209
- BIDS Specification (stable). Derived dataset and pipeline description.
  - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html
- Robbins KA, Touryan J, Mullen T, et al. Building FAIR functionality: Annotating events in time series data using Hierarchical Event Descriptors. *Neuroinformatics*. 2021.
  - https://doi.org/10.1007/s12021-021-09513-7
- Hermes D, Bigdely-Shamlo N, Niso G, et al. HED library schema for EEG data annotation. *Sci Data*. 2025.
  - https://doi.org/10.1038/s41597-025-05791-2
