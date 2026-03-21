# Site Deepening Audit (2026-03-21, Post-Transcriptional RNA Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 運用ルール反映: `verification.md`
- 入口反映: `wbe_101.md`, `index.md`

## 今回の選定理由

- 2026-03-21 時点で、サイトはすでに `post-transcriptional RNA-state` を hidden-state として前面化していました。
- しかし、`transcription / chromatin`、`phospho-signaling`、`proteostasis`、`sleep replay`、`myelin`、`ionic` などには route card がある一方で、`post-transcriptional RNA-state` だけはまだ `重要だが一段落ちた説明` に留まっていました。
- この不均衡は技術・自然科学の観点で重要です。理由は、RNA 系の一次文献が実際には
  - alternative-splice isoform
  - m6A-dependent translation
  - m6A-dependent degradation
  - RNA editing
  - long-read atlas / observability ceiling
  のように異なる inferential object を持つのに、現状サイトではそれらが `gene-level abundance ではない` という一つの停止線に圧縮されやすかったからです。

## 根拠付き批判

### 1. 既存サイトは `gene-level abundance ではない` ことは言えていましたが、`何の RNA 制御か` をまだ十分に固定していませんでした

- 問題:
  - 既存本文は、gene-level transcript count が isoform / m6A / editing を決めないことを明記していました。
  - しかし、`alternative splicing`、`m6A-dependent translation`、`m6A-dependent degradation`、`RNA editing` が互いに異なる claim family であることを、route-card field としては固定していませんでした。
- 根拠:
  - Wang et al. (2015) は neuron-specific LSD1 splice isoform であり、下流 object は chromatin / transcriptional elongation です。
  - Dai et al. (2019) は presynaptic neurexin alternative splicing による postsynaptic receptor-balance control です。
  - Shi et al. (2018) は YTHDF1 を介した neuronal-stimulus-dependent translation です。
  - Li et al. (2025) は YTHDF2 を介した m6A mRNA degradation です。
  - Peterson et al. (2025) は ADAR2-mediated GluA2 editing による homeostatic scaling control です。
- 批判:
  - したがって、`RNA-state evidence` という一語のままでは粗すぎます。
  - 少なくとも `claim family` と `RNA control axis` を固定しない限り、読者は mechanistic object を取り違えます。

### 2. RNA-side controller と downstream object の区別が弱く、hybrid paper を誤読しやすい状態でした

- 問題:
  - 既存サイトは RNA-side control を強調していましたが、`その RNA 制御が最終的に何を変えたのか` を field として固定していませんでした。
- 根拠:
  - Wang et al. (2015) は alternative splicing paper ですが、直接の downstream object は histone mark / transcriptional elongation です。
  - Dai et al. (2019) は splice paperですが、downstream object は postsynaptic NMDA/AMPA balance です。
  - Peterson et al. (2025) は editing paperですが、downstream object は Ca2+-permeable AMPAR-dependent homeostatic upscaling です。
- 批判:
  - したがって、`RNA controller` と `downstream functional object` を別欄にしないと、
    - RNA-state を transcription-state と混同する
    - RNA-state を receptor-composition control と混同する
    - RNA-state を generic memory-support と混同する
    という 3 種類のすり替えが起きます。

### 3. atlas / observability ceiling を mechanistic controller と同列に読めてしまう弱点がありました

- 問題:
  - 既存ページは Joglekar et al. (2024) を human observability ceiling として引用していましたが、`atlas route` と `current living-human state readout` の差を route-card の停止線としてはまだ十分に固定していませんでした。
- 根拠:
  - Joglekar et al. (2024) は single-cell long-read atlas であり、cell type / region / development / species にまたがる isoform variability を示しています。
  - 一方で、human data は hippocampus を含む ex vivo / atlas-building route であり、living-human whole-brain in vivo readout ではありません。
- 批判:
  - したがって、atlas paper の存在を `current human RNA-state observability が近い` へ昇格させるのは不適切です。
  - `human observability ceiling` を独立欄にしなければ、この誤読は止まりません。

### 4. current site text には `abstention boundary` がまだ弱く、何が依然 latent かを一文で止めにくかったです

- 問題:
  - 既存本文は human ceiling を述べていましたが、submission rule として `same-subject whole-brain continuity`、`compartment-specific RNA localization`、`non-destructive live readout` を一文で止める欄がありませんでした。
- 根拠:
  - Shi et al. (2018), Li et al. (2025), Peterson et al. (2025) はいずれも強い causal papers ですが、living-human whole-brain current RNA-state を直接読む route ではありません。
- 批判:
  - したがって、強い rodent mechanistic paper と human atlas clue を同じ段で語るなら、最後に `何がまだ latent か` を明示する欄が必須です。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights` と `known_points` に、post-transcriptional RNA evidence が one class ではないことを追加しました。
  - `unknown_points` を更新し、`どう audit するか` という抽象論から、`どの route-card fields が必要か` と `どの calibrator が不足か` へ具体化しました。
  - `2026-03-21 addendum: post-transcriptional RNA evidence now needs a route card` を新設しました。
  - 新規 route-card table を追加し、以下を独立欄として固定しました。
    - claim family
    - RNA control axis
    - biological regime
    - time axis / state dependence
    - assay and direct observable
    - downstream functional object
    - causal leverage
    - human observability ceiling
    - abstention boundary
  - `Why this route card is necessary here` を追加し、Wang / Dai / Shi / Li / Peterson / Joglekar を異なる evidence class として読み分ける規則を明文化しました。
- `verification.md`
  - `page_highlights` に post-transcriptional RNA route card を追加しました。
  - `2026-03-21 addendum: post-transcriptional RNA evidence now needs a route card` を追加しました。
  - maintenance-state table の post-transcriptional row に `downstream object` の開示を追加しました。
  - hidden-state table の post-transcriptional row に `downstream transcriptional control` を明示し、Wang et al. (2015) 型の hybrid route を読めるようにしました。
- `wbe_101.md`
  - `page_highlights` に post-transcriptional evidence-class split を追加しました。
  - entry-level note を route-card 連動の形へ更新し、`RNA controller` と `atlas ceiling` を同列にしない停止線を追加しました。
- `index.md`
  - `page_highlights` に post-transcriptional evidence-class split を追加しました。
  - front-door note `If You Are Treating Post-Transcriptional RNA Evidence As One Solved Row` を追加しました。

## 外部依存で保留

- living-human whole-brain post-transcriptional calibration route
  - 担当者: long-read / chemical biology / imaging / human neuroscience の共同研究者
  - 前提条件: living-human-compatible な isoform / editing / m6A 読み出し、または external calibrator として比較可能な same-subject bridge data
  - 完了条件: atlas / ex vivo route を超えて、同一個体の current post-transcriptional RNA-state を living-human condition で比較可能に制約できる公開 benchmark が整備されること

## 参考文献

1. Wang J, Telese F, Tan Y, et al. LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. *Nature Neuroscience*. 2015.
   - https://doi.org/10.1038/nn.4069
2. Dai J, Aoto J, Südhof TC. Alternative Splicing of Presynaptic Neurexins Differentially Controls Postsynaptic NMDA and AMPA Receptor Responses. *Neuron*. 2019.
   - https://doi.org/10.1016/j.neuron.2019.03.032
3. Shi H, Zhang X, Weng Y-L, et al. m6A facilitates hippocampus-dependent learning and memory through YTHDF1. *Nature*. 2018.
   - https://doi.org/10.1038/s41586-018-0666-1
4. Li K, Guo C, Wu X, et al. Enhanced Protein Synthesis and Hippocampus-Dependent Memory via Inhibition of YTHDF2-Mediated m6A mRNA Degradation. *Advanced Science*. 2025.
   - https://doi.org/10.1002/advs.202514926
5. Peterson L, Coca R, Parikh S, et al. ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. *Science Signaling*. 2025.
   - https://doi.org/10.1126/scisignal.adr1442
6. Joglekar A, Prjibelski A, Mahfouz A, et al. Single-cell long-read sequencing-based mapping reveals specialized splicing patterns in developing and adult mouse and human brain. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-024-01616-4
