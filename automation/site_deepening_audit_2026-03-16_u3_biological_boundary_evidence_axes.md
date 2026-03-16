# Site Deepening Audit (2026-03-16, U3 Biological Boundary / Evidence Axes)

## 対象

- 主対象: `research_harvest_50.md`
- 副対象: `wiki/u-number-guide.md`

## 今回の選定理由

- `research_harvest_50.md` の `U3: 生物学的境界` は、現在のサイト全体の中では相対的に古く、`connectome の前進`、`sleep / homeostasis`、`髄鞘 / 代謝支持`、`glia / clearance / immune support`、`身体・環境ループ` を近い強さで並べていました。
- その結果、技術・自然科学の読者が `connectome が進んだ` ことを `長期維持に必要な support-state までかなり解けた` と誤読する余地、あるいは逆に `ニューロン外のものは全部 speculative` と誤読する余地が残っていました。
- さらに旧 `根拠例` には、直接性の弱い章論文や general review が混じっており、現在の site rule が他ページで要求している `一次文献の直接性 / 時定数 / claim ceiling` の切り分けに届いていませんでした。

## 根拠付き批判

### 1. 旧 U3 は「何が structural scaffold で、何が maintenance-state か」を分け切れていませんでした

- 問題:
  - 旧版は `connectome 再構成が進んでいる` と `astrocyte-neuron 相互作用が増えている` を同列で置いていました。
  - しかし、この 2 群は同じ証拠型ではありません。前者は主に `構造 scaffold / cell-type bridge` を押し上げ、後者は `support-state` や `cross-day stability` に関わるからです。
- 根拠:
  - Schlegel et al. (2024) は、adult fly の whole-brain annotation と multi-connectome cell typing を提示し、構造 scaffold を強く押し上げました。
  - MICrONS Consortium et al. (2025) は、same-brain で structure-function link を押し上げましたが、扱うのは multi-area visual cortex の local functional connectomics であり、human whole-brain state completeness ではありません。
  - Beiran & Litwin-Kumar (2025) は、connectome-constrained recurrent networks でも neural activity prediction に縮退が残ることを示しました。
- 修正:
  - `U3` を `構造 scaffold / cell-type bridge`、`sleep / homeostatic regime`、`axon-myelin / glial support`、`clearance / immune support` の 4 軸へ再編しました。

### 2. 旧 U3 は sleep / homeostasis と glial / metabolic support の因果的重みを十分に前面化していませんでした

- 問題:
  - 旧版は `グリア/体液性調節を追加したときの改善量` を問いとしては置いていましたが、どの文献が `same-day fit` と `cross-day maintenance` の差を直接示すのかが曖昧でした。
- 根拠:
  - Hengen et al. (2016) は、firing-rate homeostasis が sleep / wake に依存して抑制・促進されることを示しました。
  - Xu et al. (2024) は、sleep が cortical networks の computational regime を回復させることを示しました。
  - Looser et al. (2024) は、oligodendrocyte-axon metabolic coupling が axonal health に関わることを示しました。
  - Cahill et al. (2024) は、local neurotransmitter input が cortical astrocyte network に符号化されることを示しました。
  - Williamson et al. (2025) は、learning-associated astrocyte ensembles が memory recall を制御することを示しました。
- 修正:
  - `今、解かれているもの` と `主要先行研究` を、sleep/homeostasis・髄鞘/代謝支持・astrocyte memory を中心に再構成しました。

### 3. 旧 U3 は clearance / immune support と body/environment loop を、既定 core と同じ強さで読ませる余地がありました

- 問題:
  - 旧版は glymphatic / meningeal lymphatic / immune surveillance と embodied cognition を近く置いていました。
  - しかし、前者は近年ようやく synaptic physiology や human CSF mobility と結び付く primary evidence が出てきた領域であり、後者は task-specific omission test より一般論が先行しやすい領域です。
- 根拠:
  - Kim et al. (2025) は、meningeal lymphatics-microglia axis が synaptic physiology を調整することを示しました。
  - *Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans* (2025) は、MRI により humans で CSF mobility の局在的 driver を示しました。
  - *The glymphatic system clears amyloid-beta and tau from brain to plasma in humans* (2026) は、human で glymphatic route に沿った amyloid-beta / tau clearance を示しました。
  - ただし、これらは `support-state` を measurable にした前進であり、moment-to-moment neural truth や universal minimal core を直接与えたわけではありません。
- 修正:
  - `clearance / immune support` を独立軸として残しつつ、`momentary neural truth` や `universal minimal core` へは上げないと明記しました。
  - `身体・環境ループ` は重要候補だが、現時点では `same-task ablation / transfer test` が薄く、4 軸と同じ primary evidence class には置かないという site rule を追加しました。

## 今回実行した変更

- `research_harvest_50.md`
  - `U3` の厳密定義を更新
  - `2026-03 U3 再監査` 節を追加し、4 つの evidence axis を明示
  - `リサーチクエスチョン分解` を timescale / omission test ベースへ差し替え
  - `今、解かれているもの` と `未解決` を primary evidence に合わせて再構成
  - `主要先行研究` を 15 件の一次文献へ更新
  - U3 の summary row / representative findings も新しい読み方へ更新
- `wiki/u-number-guide.md`
  - `last_updated` を 2026-03-16 に更新
  - U3 の入口説明を `maintenance-state と支持系` へ更新

## 外部依存で保留

- なし
  - 今回の変更は、このリポジトリ内の公開文面更新で完結しています。

## 参考文献

- Schlegel P, et al. Whole-brain annotation and multi-connectome cell typing of Drosophila. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07686-5
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Gamlin C, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08805-6
- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal Firing Rate Homeostasis Is Inhibited by Sleep and Promoted by Wake. *Cell*. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nature Neuroscience*. 2024.
  - https://doi.org/10.1038/s41593-023-01536-9
- Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. *Science*. 2014.
  - https://doi.org/10.1126/science.1252304
- McKenzie IA, et al. Motor skill learning requires active central myelination. *Science*. 2014.
  - https://doi.org/10.1126/science.1254960
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nature Neuroscience*. 2024.
  - https://doi.org/10.1038/s41593-023-01558-3
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-024-08170-w
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *PNAS*. 2022.
  - https://doi.org/10.1073/pnas.2211572119
- Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
  - https://doi.org/10.1016/j.cell.2025.02.022
- Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
  - https://doi.org/10.1038/s41593-025-02073-3
- The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
  - https://doi.org/10.1038/s41467-026-68374-8
