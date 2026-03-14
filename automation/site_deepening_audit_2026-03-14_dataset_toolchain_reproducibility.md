# Site Deepening Audit (2026-03-14, Dataset Toolchain / Benchmark Reproducibility)

## 対象

- 主対象: `datasets.md`
- 副対象: `wiki/standards-repositories-validators-and-benchmarks.md`
- 副対象: `wiki/l0-minimum-artifact-pack.md`

## 今回の選定理由

- 公開サイトはすでに `BIDS は規格、OpenNeuro は置き場、Benchmark は比較ルール` という大枠までは整理できていました。
- しかし、2026-03-14 時点の実務導線には、`同じ dataset 名でも別 snapshot / version なら別入力になる` こと、`MNE-BIDS のようなローダ / 変換器` と `MOABB のような benchmark harness` が別物であることが十分に固定されていませんでした。
- この欠落は技術・自然科学の観点で弱点です。なぜなら、L0 の再現可能解析では高性能モデル以前に `どの版の入力を、どの評価族で比べたか` を固定しない限り、比較可能性そのものが成立しないからです。

## 主要な批判点

### 1. 現行サイトは `規格 / 置き場 / benchmark` を概念的に分けていたが、`版固定` が不足していました

- 問題:
  - 旧版は `OpenNeuro` や `PhysioNet` を置き場として紹介していましたが、dataset 名だけで同一入力を特定したかのように読める余地がありました。
  - しかし、公開 repository 上では同じ dataset 名でも snapshot / version が変わりえます。
- 根拠:
  - OpenNeuro の公式 docs は、snapshot を semantic version の git tag として扱うことを明示しています。
  - PhysioNet の project pages と citation guidance は、resource ごとに version を示し、その版を引用する運用を取っています。
- 修正:
  - `datasets.md` と `wiki/l0-minimum-artifact-pack.md` に、dataset 名ではなく `snapshot / version / DOI / 取得日` を最低成果物へ含める site rule を追加しました。
  - `wiki/standards-repositories-validators-and-benchmarks.md` に `Input ID` として版固定を独立論点化しました。

### 2. 現行サイトは `読めること` と `公平比較できること` を十分に分離していませんでした

- 問題:
  - 旧版では `BIDS に揃える`, `Validator を通す`, `Benchmark で比べる` までは書かれていましたが、その中間にある `MNE-BIDS のような入出力経路` と `MOABB のような evaluation engine` が抜けていました。
  - その結果、読者が `MNE-BIDS で読めた = benchmark まで済んだ` と誤読しうる構造が残っていました。
- 根拠:
  - Appelhoff et al. (2019) の MNE-BIDS は、BIDS datasets の整理・metadata 抽出・MNE への読込経路を提供するソフトウェアです。
  - MNE-BIDS の current docs は、`write_raw_bids()` について `BIDS was originally designed for unprocessed or minimally processed data` と注意し、modified/preloaded data の書き戻しを例外的扱いにしています。
  - Jayaram & Barachant (2018) の MOABB は、EEG-based BCI に対する trustworthy algorithm benchmarking を目的とし、paradigm と evaluation を固定する枠組みです。
  - MOABB の公式 docs も、within-session / cross-session / cross-subject を別 evaluation family として整理しています。
- 修正:
  - `wiki/standards-repositories-validators-and-benchmarks.md` に `5 層` の表を追加し、規格、公開版、変換・読込、benchmark harness、学習器を分離しました。
  - `datasets.md` に `置き場の次に固定する実行鎖` と `Step 2.5: loader と benchmark を分けて固定する` を追加しました。

### 3. 現行 L0 成果物パックには `evaluation family` と `dataset version` が明示されていませんでした

- 問題:
  - 旧 `wiki/l0-minimum-artifact-pack.md` は、BIDS、QC、分割、ベースライン、実行手順、失敗例を挙げていましたが、`どの版のデータか` と `within-session / cross-session / cross-subject のどれか` を独立成果物として扱っていませんでした。
  - これでは、同じ score でも意味が変わるケースを防ぎきれません。
- 根拠:
  - MOABB docs は paradigm と evaluation family を独立に定義しており、同じ pipeline でも評価族が変われば比較意味が変わります。
  - OpenNeuro / PhysioNet は dataset versioning を明示しており、dataset 名だけでは不十分です。
- 修正:
  - `wiki/l0-minimum-artifact-pack.md` を `7 点` から `8 点` へ更新し、先頭に `データ版` を追加しました。
  - 分割ルールにも evaluation family を明記し、`他の人が同じ版の入力を持てますか` を最初の完了判定に変更しました。

## 今回実行した変更

- `datasets.md`
  - repository / BIDS / loader / benchmark の実務鎖を追加
  - `version pin` と `evaluation family` を L0 checklist と確認表に追加
  - OpenNeuro、PhysioNet、MNE-BIDS、MOABB の一次ソースを参考文献へ追加
- `wiki/standards-repositories-validators-and-benchmarks.md`
  - `4 つ` の概念説明を、`5 層` の運用表へ拡張
  - `dataset 名だけでは足りない`, `MNE-BIDS ≠ benchmark`, `MOABB score は evaluation family 依存` を明文化
  - `4 つの ID` と `5 問` を追加
- `wiki/l0-minimum-artifact-pack.md`
  - `7 点` を `8 点` に更新し、`データ版` を追加
  - 完了判定を `同じ版の入力` 基準へ更新

## 外部依存で保留

- site-wide な benchmark schema の統一
  - 担当者: AI / maintainer
  - 前提条件: `within-session / cross-session / cross-subject` を公開ページ全体でどこまで標準語として使うかを決めること
  - 完了条件: `datasets.md`、`verification.md`、関連 wiki の間で evaluation family 名と最低提出物が一貫すること

## 参考文献

- BIDS Specification: Electroencephalography
  - https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Scientific Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- OpenNeuro Docs: Git access and snapshots
  - https://docs.openneuro.org/git.html
- OpenNeuro Docs: User guide
  - https://docs.openneuro.org/user_guide.html
- PhysioNet: About
  - https://physionet.org/about/
- PhysioNet: Resources
  - https://physionet.org/about/content/
- Appelhoff S, Sanderson M, Brooks TL, et al. MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis. J Open Source Softw. 2019.
  - https://doi.org/10.21105/joss.01896
- MNE-BIDS Docs: write_raw_bids
  - https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html
- Jayaram V, Barachant A. MOABB: trustworthy algorithm benchmarking for BCIs. Journal of Neural Engineering. 2018.
  - https://doi.org/10.1088/1741-2552/aadea0
- MOABB Docs
  - https://moabb.neurotechx.com/docs/index.html
- MOABB Docs: paradigm and evaluation examples
  - https://moabb.neurotechx.com/docs/auto_examples/paradigm_examples/index.html
