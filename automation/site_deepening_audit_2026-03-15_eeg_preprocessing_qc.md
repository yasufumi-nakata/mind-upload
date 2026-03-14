# Site Deepening Audit (2026-03-15, EEG Preprocessing / QC Acceptance Gates)

## 対象

- 主対象: `wiki/eeg-preprocessing-and-qc.md`
- 副対象: `eeg_101.md`

## 今回の選定理由

- 2026-03-15 時点で公開サイトは、EEG が魔法の読心術ではないこと、source imaging の ceiling、multimodal 統合の限界まではかなり整理できていました。
- その一方で、`EEG前処理とQC` 周辺はなお「重要です」という一般論に寄っており、`どの処理差がどの種類の主張を止めるか` が一次文献ベースの監査ゲートになっていませんでした。
- この弱さは局所ページに留まりません。EEG を使う L0、L1、意識指標、source imaging、閉ループのどれも、前処理と QC の床が曖昧だと、上流の慎重な議論まで過大化して読まれます。

## 主要な批判点

### 1. 旧 `EEG前処理とQC` は 4 論点の列挙に留まり、受理条件になっていませんでした

- 問題:
  - 旧版は `参照法`、`フィルタ`、`アーティファクト処理`、`除外基準` を挙げていました。
  - しかし、それぞれが `何の主張を止める gate なのか`、`何を残さないと再現可能成果物にならないのか` が表になっていませんでした。
- 根拠:
  - EEG-BIDS と BIDS EEG specification は、reference、ground、filters、bad channels、電極座標、event 情報などを具体的な metadata として要求します。
  - COBIDAS-MEEG は、取得条件、filters、artifact handling、bad channel / epoch 処理、除外規則を透明に報告することを求めています。
- 修正:
  - `wiki/eeg-preprocessing-and-qc.md` を全面改稿し、`metadata`、`reference`、`filter`、`artifact`、`保持率 / 高周波` の 5 監査ゲートで再構成しました。
  - それぞれについて、`一次文献が今支持すること` と `通っていないときに止める主張` を表で固定しました。

### 2. 旧版は `報告の床` と `アルゴリズム選択` を十分に分離していませんでした

- 問題:
  - 旧版では `ICA などを使ったか` という記述はありましたが、BIDS / COBIDAS が求める床と、PREP / Autoreject / ICLabel のような候補手法が混ざっていました。
  - その結果、読者が `有名な pipeline 名を書いた = 再現性が確保された` と誤読しうる構造が残っていました。
- 根拠:
  - PREP pipeline は robust rereference の前に bad channel を扱う必要を示しましたが、これは `万能の完成パイプライン` ではなく、reporting floor の代替でもありません。
  - Autoreject と ICLabel は有用な automation ですが、どちらも signal preservation を自動保証するものではありません。
- 修正:
  - `報告の床は algorithm 名ではなく metadata` という節を新設しました。
  - `候補手法` の表を追加し、PREP / Autoreject / ICA+ICLabel を `有力な道具` として位置づけつつ、`自動的に標準解へ昇格しない理由` を並記しました。

### 3. 旧版は `artifact を多く消した = よい前処理` と読める余地がありました

- 問題:
  - 旧版は artifact 除去の必要性を述べていましたが、`何を削るほど signal も削りうるか`、`accuracy が下がるのは必ずしも悪ではない` という点が弱かったです。
  - これは decoding 系ページで特に危険です。artifact-related confound を拾った高精度を、neural information の向上と誤読しやすいからです。
- 根拠:
  - Kessler et al. (2025) は preprocessing の選択が decoding performance を大きく動かすことを示しました。
  - 2025 年の NeuroImage 論文 `Assessing the impact of artifact correction and artifact rejection on the performance of SVM- and LDA-based decoding of EEG signals` は、artifact correction が decoding 精度を必ずしも改善しないことを示しました。
- 修正:
  - `artifact suppression は常に改善とは限りません` という節を新設しました。
  - `最も高い decoding 精度を出した pipeline を無条件で最良としない` を site rule として明文化し、`raw-clean delta`、`保持率`、`代替 pipeline との感度分析` を最低提出物に追加しました。

### 4. 旧版は高周波数帯の筋電汚染を弱くしか扱っていませんでした

- 問題:
  - 旧版は筋電を artifact の一例として挙げるに留まり、high beta / gamma claim をどの条件で止めるかが明確ではありませんでした。
  - そのため、`高周波 power が上がった = neural gain` と読める余地がありました。
- 根拠:
  - Muthukumaraswamy (2013) は、muscle artifact が 20-300 Hz に広く重なり、高周波数帯の neural 解釈を難しくすることを整理しています。
- 修正:
  - `高 beta / gamma は筋電監査なしに強く書きません` という独立節を追加しました。
  - `high-frequency exception note` を最低提出物に追加し、EMG / topography / residual check を通さない限り gamma claim を上げない運用へ変えました。

### 5. 旧 `eeg_101.md` は前処理の重要性を述べていましたが、受理条件としては薄かったです

- 問題:
  - 公開入門ページでは `前処理や参照で結果が変わる` と説明されていましたが、読者が `細かい実装差` として読み流せる程度の重さに留まっていました。
- 修正:
  - `eeg_101.md` に `2026-03 文献監査：前処理は見栄えではなく受理条件です` を追加しました。
  - 公開ページ側では詳細に入りすぎず、5 つの acceptance gate と site rule を圧縮して示し、詳細は wiki へ送る構成にしました。

## 今回実行した変更

- `wiki/eeg-preprocessing-and-qc.md`
  - front matter を更新
  - 旧版を全面改稿し、5 監査ゲート、候補手法の位置づけ、最低提出物、止めるべき誤読、参考文献を追加
- `eeg_101.md`
  - `last_updated` を 2026-03-15 に更新
  - front matter の highlights / known / unknown を更新
  - `前処理は見栄えではなく受理条件` の節を追加
  - 参考リンクへ PREP、Widmann、Muthukumaraswamy、Kessler を追加
- `github-wiki-export/eeg-preprocessing-and-qc.md`
  - export 再生成で公開用 wiki HTML を同期

## 外部依存で保留

- raw / clean paired benchmark の site-wide 整備
  - 担当者: AI / maintainer
  - 前提条件: 同一 raw EEG に対して複数 preprocessing family を比較できる公開 benchmark と、task-relevant signal preservation 指標の合意
  - 完了条件: `accuracy` だけでなく `artifact suppression`、`retention`、`signal preservation` を同一 schema で比較できること

## 参考文献

- BIDS Specification: Electroencephalography
  - https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Scientific Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. Nature Neuroscience. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M, Robbins KA. The PREP pipeline: standardized preprocessing for large-scale EEG analysis. Journal of Neuroscience Methods. 2015.
  - https://doi.org/10.1016/j.jneumeth.2015.06.014
- Widmann A, Schröger E, Maess B. Digital filter design for electrophysiological data: a practical approach. Journal of Neuroscience Methods. 2015.
  - https://doi.org/10.1016/j.jneumeth.2014.08.002
- Muthukumaraswamy SD. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. Frontiers in Human Neuroscience. 2013.
  - https://doi.org/10.3389/fnhum.2013.00138
- Cao Y, et al. How Different EEG References Influence Sensor Level Functional Connectivity Graphs. Frontiers in Neuroscience. 2017.
  - https://doi.org/10.3389/fnins.2017.00368
- Jas M, Engemann DA, Bekhti Y, Raimondo F, Gramfort A. Autoreject: automated artifact rejection for MEG and EEG data. NeuroImage. 2017.
  - https://doi.org/10.1016/j.neuroimage.2017.08.030
- Pion-Tonachini L, Kreutz-Delgado K, Makeig S. ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. NeuroImage. 2019.
  - https://doi.org/10.1016/j.neuroimage.2019.05.026
- Kessler V, et al. How EEG preprocessing shapes decoding performance. Communications Biology. 2025.
  - https://doi.org/10.1038/s42003-025-08464-3
- Assessing the impact of artifact correction and artifact rejection on the performance of SVM- and LDA-based decoding of EEG signals. NeuroImage. 2025.
  - https://www.sciencedirect.com/science/article/pii/S1053811925003076
