# Site Deepening Audit (2026-03-15, Claims / Evidence / Measurement Boundaries)

## 対象

- 主対象: `wiki/claims-and-evidence.md`
- 関連ページ: `wiki/measurement-stack-and-claim-ceiling.md`
- 関連ページ: `wiki/observation-to-estimation.md`
- 関連ページ: `wiki/connectome-is-not-enough.md`
- 関連ページ: `wiki/state-trait-and-drift.md`

## 今回の選定理由

- 2026-03-15 時点で、公開サイト本体では `measurement ceiling`、`direct validation`、`maintenance-state`、`chronic unit identity audit` の整理がかなり前進していました。
- その一方で、`wiki/claims-and-evidence.md` は 2026-03-06 時点の一般論に留まり、`高 score` と `強い主張` の間にある技術的な境界をまだ十分に固定できていませんでした。
- ここが弱いと、個別ページで慎重に書いた制約が読者の頭の中で再び潰れてしまいます。つまり、サイト内でいちばん広く参照される「読み方ガイド」が、現在の科学的な厳しさに追いついていませんでした。

## 主要な批判点

### 1. 旧ページは L0〜L5 を主張の強さとして整理していましたが、measurement stack ごとの claim ceiling を落としていました

- 問題:
  - 旧 `wiki/claims-and-evidence.md` は、`再現`、`予測`、`閉ループ`、`本人性` を順に並べる入門としては有用でした。
  - しかし、同じ L1 や L2 でも、`scalp EEG`、`simultaneous SEEG/HD-EEG bridge`、`high-density extracellular probe`、`connectome + cell type atlas` では、直接観測量と latent state がまったく異なります。
  - この差を書かないと、読者は `予測精度が高い = localization / causality / state-complete reconstruction に近い` と誤読しやすくなります。
- 根拠:
  - Hao et al. (2025) は simultaneous SEEG/HD-EEG による source imaging validation route を前進させましたが、drug-resistant epilepsy cohort と depth / power dependence という制約が残ります。
  - Steinmetz et al. (2021) は Neuropixels 2.0 の stable long-term recording を示しましたが、motion stabilization と recording condition が前提です。
  - van Beest et al. (2024) は cross-day neuron tracking を probabilistic unit matching として扱っており、`same neuron` は自動的な観測事実ではないことを示しました。
  - Gouwens et al. (2021)、Torrado Pacheco et al. (2021)、Looser et al. (2024)、Cahill et al. (2024) は、cell type や connectome の外に maintenance-state が残ることを支持します。
- 修正:
  - `wiki/claims-and-evidence.md` に `同じ L1 でも、計測スタックが違えば claim ceiling も違います` 節を追加しました。
  - `直接見えているもの / まだ latent のもの / 安全側の上限 / 1 段上げるために必要な証拠` を 1 表で整理しました。

### 2. 旧ページは「高 score」を upgrade gate なしに強い主張へ読み替える危険を十分に止めていませんでした

- 問題:
  - 旧ページは `追加で確認したいこと` を書いていましたが、upgrade gate が一般論に留まっていました。
  - とくに `localization`、`directed connectivity`、`stable single-unit identity`、`connectome-complete` は、見出しだけ読むと 1 段強い主張へ飛びやすい類型です。
- 根拠:
  - Vinck et al. (2011) は wPLI を volume-conduction / noise / sample-size bias を減らす指標として示しましたが、完全免疫を主張したわけではありません。
  - Haufe et al. (2013) は connectivity measures が source mixing 条件で食い違いうることを示しました。
  - Palva et al. (2018) は source-space でも ghost interaction が残りうると警告しました。
- 修正:
  - `主張を 1 段上げる前の 3 ゲート` として、`direct validation`、`perturbation / counterfactual`、`longitudinal maintenance audit` を独立に追加しました。
  - `lagged metric を使った`、`source imaging をした`、`chronic probe で追った`、`connectome を作った` を、そのまま upgrade 理由にしない site rule を明記しました。

### 3. 旧ページは connectome 系の主張を structural scaffold と state-complete reconstruction で十分に分離していませんでした

- 問題:
  - 旧 `wiki/claims-and-evidence.md` には `出力一致と内部の仕組みは別` という重要な一般原則はありました。
  - しかし、WBE 文脈で最も誤読されやすい `connectome-complete` について、何がまだ hidden state として残るかの具体が不足していました。
- 根拠:
  - Gouwens et al. (2021) は transcriptomic type 内の morpho-electric variation を示しました。
  - Torrado Pacheco et al. (2021) は sleep-dependent firing-rate homeostasis を示しました。
  - Looser et al. (2024) は oligodendrocyte-axon metabolic coupling を示しました。
  - Cahill et al. (2024) は local neurotransmitter input が astrocyte network state として広域・遅い時間スケールに展開されることを示しました。
- 修正:
  - 見出し翻訳表に `コネクトームが完成した` を追加し、`structural scaffold の前進` と `emulation-complete` を明確に分離しました。
  - この判断は上記一次文献からの **推論** であり、直接観測された state-complete reconstruction を意味しないことも本文に残しました。

## 今回実行した変更

- `wiki/claims-and-evidence.md`
  - `last_updated` を 2026-03-15 に更新
  - `page_highlights` / `known_points` / `unknown_points` を measurement-boundary 寄りに更新
  - `同じ L1 でも、計測スタックが違えば claim ceiling も違います` 節を新設
  - `見出しを technical route に翻訳する` 表へ `EEG source imaging`、`Neuropixels`、`connectome-complete` を追加
  - `主張を 1 段上げる前の 3 ゲート` を追加
  - 参考文献を一次文献ベースで追加

## 外部依存で保留

- measurement-claim card の site-wide テンプレート化
  - 担当者: AI / maintainer
  - 前提条件: `measurement stack`, `direct observation`, `latent state`, `validation route`, `longitudinal audit` を全ページで同じ欄名にそろえること
  - 完了条件: ニュース、論文集、公開ページのいずれを読んでも、同じ card 形式で claim ceiling を監査できること

## 参考文献

- Vinck M, Oostenveld R, van Wingerden M, et al. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. *NeuroImage*. 2011.
  - https://doi.org/10.1016/j.neuroimage.2011.01.055
- Haufe S, Nikulin VV, Müller K-R, Nolte G. A critical assessment of connectivity measures for EEG data: A simulation study. *NeuroImage*. 2013.
  - https://doi.org/10.1016/j.neuroimage.2012.09.036
- Palva JM, Wang SH, Palva S, et al. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. *NeuroImage*. 2018.
  - https://doi.org/10.1016/j.neuroimage.2018.02.032
- Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
  - https://pubmed.ncbi.nlm.nih.gov/40674110/
- Steinmetz NA, Aydin C, Lebedeva A, et al. Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. *Science*. 2021.
  - https://doi.org/10.1126/science.abf4588
- van Beest EH, Bimbard C, Fabre JMJ, et al. Tracking neurons across days with high-density probes. *Nature Methods*. 2024.
  - https://doi.org/10.1038/s41592-024-02440-1
- Gouwens NW, et al. Phenotypic variation of transcriptomic cell types in mouse motor cortex. *Nature*. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Torrado Pacheco A, et al. Sleep Promotes Downward Firing Rate Homeostasis. *Neuron*. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nature Neuroscience*. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
