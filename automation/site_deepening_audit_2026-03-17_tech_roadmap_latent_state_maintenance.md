# Site Deepening Audit (2026-03-17, Tech Roadmap / latent-state and maintenance-state route)

## 対象

- 主対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-17 時点で、公開サイト全体としては `connectome-complete ≠ emulation-complete`、`predictability ≠ identifiability`、`same-day success ≠ cross-day deployability` の区別がかなり整っていました。
- その一方で、公開導線の中核である `tech_roadmap.md` の `R3（潜在状態）` と `R5（可塑性）` は、なお抽象度が高く、`latent state` をほぼ 1 本の変数として読ませる構造が残っていました。
- この弱点は技術・自然科学の観点で優先度が高いです。なぜなら、現在の一次文献が比較的強く支持しているのは、`潜在状態の有無` ではなく、`どの latent state が、どの時間スケールで、どの claim を止めるか` だからです。

## 主要な批判点

### 1. 旧 `R3` は latent state を抽象名詞としては正しく置いていましたが、証拠階級と時間スケールを落としていました

- 問題:
  - 旧 `R3` は「観測ノイズと真の状態を分離し、状態が予測に効いていることを示せるか」という方向性自体は正しかったです。
  - しかし、実際に何が latent state として残るのかが見えず、読者が `held-out prediction が上がった` ことを、そのまま `hidden state もかなり回収できた` と読み替えやすい状態でした。
- 根拠:
  - Beiran & Litwin-Kumar (2025) は、connectome 制約があっても biophysical parameter の違いで recurrent dynamics が大きく縮退しうることを示しました。
  - MICrONS Consortium (2025) は、same-brain structure と function の結合を大きく前進させましたが、これは local conditional prediction を強くしたのであって、全脳 state-complete reconstruction ではありません。
  - Gouwens et al. (2021) は、同じ transcriptomic type の内部にも morpho-electric heterogeneity が残ることを示しました。
  - Hengen et al. (2016)、Torrado Pacheco et al. (2021)、Xu et al. (2024) は、sleep / wake をまたぐ firing-rate homeostasis と cortical regime recovery を示しました。
  - Looser et al. (2024) は、oligodendrocyte-axon metabolic coupling が activity-dependent かつ axonal health に重要であることを示しました。
  - Cahill et al. (2024)、Williamson et al. (2025)、Dewa et al. (2025) は、astrocyte ensemble と slow-state が minutes-to-days の回路状態と memory stabilization に関与することを示しました。
  - Hadzibegovic et al. (2026) は、neocortical engram neurons の intrinsic excitability plasticity が early consolidation window に時間制限つきで必要であることを示しました。
- 修正:
  - `R3` に `latent-state を evidence tier × dominant timescale で分ける` table を追加しました。
  - morpho-electric / intrinsic excitability、sleep-homeostasis、delay / myelin / metabolic support、astrocyte / slow-state、connectome-constrained degeneracy を別々の latent-state class として明示しました。

### 2. 旧 `R5` は plasticity を「入れる / 入れない」の二択に寄せすぎており、maintenance-state の壁を見せていませんでした

- 問題:
  - 旧 `R5` は、長期主張では学習則が必要になりうること自体は述べていました。
  - しかし、一次文献が示す本当の境界は `learning rule を書いたかどうか` ではなく、`same-day / cross-day / remote-memory` のどこまでを claim するかです。
  - このままでは、same-day fit と multiday stabilization を同じ「plasticity の話」として扱ってしまいます。
- 根拠:
  - Hengen et al. (2016)、Torrado Pacheco et al. (2021)、Xu et al. (2024) は、sleep-dependent recovery をまたぐなら maintenance-state を無視できないことを示しました。
  - Dewa et al. (2025) は、astrocytic ensemble が memory stabilization の multiday trace として働くことを示しました。
  - Hadzibegovic et al. (2026) は、intrinsic excitability plasticity が early consolidation window の permissive mechanism であり、late phase にはそのまま残らないことを示しました。
- 修正:
  - `R5` を `固定モデル`、`固定パラメータ + maintenance log`、`明示的 plasticity / maintenance model` の 3 ルートに分解しました。
  - same-day decode、cross-day stability、remote-memory / consolidation claim で必要提出物を変える site rule を追加しました。

### 3. 旧ロードマップは R 系列と Verification 側の提出物規格の接続が弱く、実務へ落ちにくい状態でした

- 問題:
  - hidden-state の危険性は他ページで説明されていましたが、ロードマップだけ読むと `では何を出せば次の claim に進めるか` が見えにくい状態でした。
- 修正:
  - `R3` に `latent-state error budget` と `connectome-only baseline vs augmentation` を要求する提出物を追記しました。
  - `R5` に `Temporal Validity Card`、`state annotation`、`recalibration burden`、`sleep / maintenance log` への接続を明示しました。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を `2026-03-17` に更新
  - page highlights / known points に latent-state / maintenance-state の読み分けを追加
  - 冒頭監査節を `計測・潜在状態・同定・介入の4つの壁` に更新
  - `R3` を evidence tier × timescale table と提出物 rule つきへ改稿
  - `R5` を claim timescale と maintenance-state 基準つきへ改稿

## 外部依存で保留

- なし

## 参考文献

- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- MICrONS Consortium. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Gouwens NW, et al. Phenotypic variation within transcriptomic cell types in mouse motor cortex. *Nature*. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Torrado Pacheco A, et al. Sleep promotes downward firing rate homeostasis. *Neuron*. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nature Neuroscience*. 2024.
  - https://doi.org/10.1038/s41593-023-01536-9
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nature Neuroscience*. 2024.
  - https://doi.org/10.1038/s41593-023-01558-3
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-024-08170-w
- Dewa KI, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09619-2
- Hadzibegovic S, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2026.
  - https://doi.org/10.1038/s41467-025-66975-3
