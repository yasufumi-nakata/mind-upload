# Site Deepening Audit (2026-03-15, Research Harvest / Technical-Natural-Science Priority Route)

## 対象

- 主対象: `research_harvest_50.md`
- 副対象: `wiki/u-number-guide.md`

## 今回の選定理由

- `research_harvest_50.md` は未解決問題ごとの地図として有用ですが、2026-03-15 時点では、技術・自然科学の読者が最初に辿るべき導線が入口で固定されていませんでした。
- 実際、ページ前半には `source_logged` の受理ログや、U0/U12/U15 のような形而上学・制度寄りの群が近い位置に並び、計測・直接妥当化・長期閉ループ安定性・maintenance-state より先に目へ入りやすい構造が残っていました。
- これは技術・自然科学の観点で弱点です。なぜなら、現在の一次証拠が比較的厚い front は、本人性や制度論ではなく、`何が測れるか`、`どこまで直接妥当化できるか`、`decode と emulation をどう分けるか`、`長期運用で何が壊れるか` にあるからです。

## 主要な批判点

### 1. 旧入口は intake queue と evidence frontier を視覚的に近づけすぎていました

- 問題:
  - `最新追加入力` は運用上必要ですが、Media / Review / arXiv の `source_logged` 項目が入口前半にあるため、技術読者が「いま最も重要な一次証拠群」と誤読する余地がありました。
  - とくに decode、speech neuroprosthesis、HD-EEG direct validation、maintenance-state の front を探したい読者に対し、既定の読む順序が固定されていませんでした。
- 根拠:
  - Tang et al. (2023) と d'Ascoli et al. (2025) は、非侵襲 decode がどこまで進んだかを直接示す一次文献です。
  - Willett et al. (2023)、Littlejohn et al. (2025)、Wairagkar et al. (2025) は、侵襲 speech neuroprosthesis の front を示します。
  - Unnwongse et al. (2023) と Hao et al. (2025) は、EEG source imaging を intracranial / SEEG で直接妥当化する系です。
- 修正:
  - `research_harvest_50.md` に `2026-03 技術・自然科学の優先ルート` を新設しました。
  - `最新追加入力` 節には、frontier ranking ではなく intake queue であることを明記しました。

### 2. 旧 U 導線は、技術読者が先に見るべき U 群を十分に絞れていませんでした

- 問題:
  - 既存の入口表は一般向けには有用でしたが、U11、U0/U12、U14/U15 が早い段階で並ぶため、技術・自然科学の既定ルートとしては焦点が広すぎました。
  - これでは `decode の成功`、`閉ループの局所成功`、`connectome の前進` を、WBE の核心条件へ読み替えやすい構造が残ります。
- 根拠:
  - Littlejohn et al. (2025) と Wilson et al. (2025) は、長期運用では streaming success と recalibration burden を分けて扱う必要があることを示しました。
  - Xu et al. (2024)、Looser et al. (2024)、Lee et al. (2022)、Gouwens et al. (2021) は、connectome と cell type の外に maintenance-state が残ることを支持します。
  - LSL 論文 (Kothe et al., 2025) と Motion-BIDS (2024) は、時刻同期と multimodal metadata を固定しないと比較不能になることを示します。
- 修正:
  - `research_harvest_50.md` の関心別入口を、`U1/U7 → U4/U13 → U8 → U3 → U10` の技術優先順へ差し替えました。
  - `wiki/u-number-guide.md` にも同じ技術ルートを追加しました。

### 3. 旧導線は「今回は主導線に置かない群」を明示していませんでした

- 問題:
  - U0/U12/U15 は重要ですが、今回のユーザ要求どおり技術・自然科学だけに焦点を絞るなら、既定入口から意図的に外す必要があります。
  - これを明示しないと、「重要だから先に読む」と「重要だが今回の主導線ではない」が混ざります。
- 修正:
  - `research_harvest_50.md` と `wiki/u-number-guide.md` の両方に、`U0 / U12 / U15 は主導線から外す` 注記を追加しました。
  - 理由は、哲学・法学ではなく、まず計測・直接妥当化・長期安定・hidden state を固定すべきだからだと本文へ明記しました。

## 今回実行した変更

- `research_harvest_50.md`
  - `last_updated` を 2026-03-15 に更新
  - front matter に技術・自然科学の既定入口を追加
  - `2026-03 技術・自然科学の優先ルート` 節を新設
  - `最新追加入力` が frontier ranking ではないことを追記
  - U 導線を `U1/U7 → U4/U13 → U8 → U3 → U10` の順へ更新
- `wiki/u-number-guide.md`
  - `last_updated` を 2026-03-15 に更新
  - front matter に技術ルートを追記
  - `技術・自然科学で先に見る順` 節を新設
  - `U0 / U12 / U15` を主導線から外す理由を追記

## 外部依存で保留

- 文献地図全引用の evidence-rank タグ再付与
  - 担当者: AI / maintainer
  - 前提条件: `primary-experimental / primary-dataset / review / media / philosophy-law / operations` の分類規約を決めること
  - 完了条件: 文献地図の全引用が `状態` だけでなく `証拠型` と `優先度` でも絞り込めること

## 参考文献

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nat Neurosci*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Unnwongse K, Elger CE, Pawley AD, Surges R, Avigdor T. Validating EEG source imaging using intracranial electrical stimulation in stereotyped seizure-onset patients. *Brain Commun*. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, et al. Direct validation of HD-EEG source imaging with simultaneous stereoelectroencephalography in focal epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
- Kothe CA, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
  - https://doi.org/10.1162/imag.a.136
- Motion-BIDS Consortium. Motion-BIDS, an extension to the brain imaging data structure for motion data. *Sci Data*. 2024.
  - https://doi.org/10.1038/s41597-024-03559-8
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Gouwens NW, et al. Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. *Nature*. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nat Commun*. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nat Neurosci*. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *Proc Natl Acad Sci U S A*. 2022.
  - https://doi.org/10.1073/pnas.2211572119
