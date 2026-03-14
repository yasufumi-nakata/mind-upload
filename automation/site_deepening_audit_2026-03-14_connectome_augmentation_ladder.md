# Site Deepening Audit (2026-03-14, Connectome / Augmentation Ladder)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-14 時点の公開サイトは、`connectome-complete ≠ emulation-complete` という批判自体はかなり整理できていました。
- しかし、現状の説明はなお `欠ける状態変数の列挙` に寄っており、読者が「では何を足したら、一段強い予測 claim に進めるのか」を比較可能な形で読み取りにくい状態でした。
- この欠落は技術・自然科学の側面で弱点です。なぜなら、state variable を無限に追加列挙するだけでは、研究設計が `何を取るべきか` ではなく `何でも足りない` に見えてしまい、実証可能性が落ちるからです。

## 主要な批判点

### 1. 現行サイトは `何が足りないか` を言えていたが、`何を足すと何が改善したと読めるか` が前面に出ていませんでした

- 問題:
  - `wiki/connectome-is-not-enough.md` は、細胞型、内在興奮性、シナプス、遅延、神経修飾、グリアが欠けることを一次文献で示していました。
  - しかし、state variable の増分価値を `augmentation / ablation` として比較する表が無く、読者が「どの追加測定がどの誤差項を減らすのか」を追いにくい構造でした。
- 根拠:
  - Lappalainen et al. (2024) は connectome-constrained network で広い活動予測を示しましたが、electrical synapses、nonlinear chemical synapses、neuromodulation などを説明外に置いています。
  - Beiran & Litwin-Kumar (2025) は、connectome を与えても未測定 biophysical parameter が違うと recurrent dynamics が大きく縮退しうることを示しました。
  - MICrONS Consortium et al. (2025) は、同一個体で dense neural activity、EM connectome、pupil diameter、locomotion を結び、`same-brain structure + function + behavior` の増分価値を具体化しました。
- 修正:
  - `wiki/connectome-is-not-enough.md` に `augmentation / ablation` 節を追加しました。
  - `connectome-only baseline`、`+ same-brain function / behavior`、`+ transcriptomic / cell-type label`、`+ local transmitter dynamics`、`+ glial / slow-state`、`+ perturbation / recovery of excitability-homeostasis` を段階表で固定しました。

### 2. 神経修飾とグリアについて、`重要である` 以上の運用ルールが弱かった

- 問題:
  - 既存サイトは `pupil / HRV は coarse proxy`、`glia は support tissue ではない` までは言えていました。
  - ただし、どの条件で `covariate` から `predictive gain を与えた state variable` へ昇格させるかが曖昧でした。
- 根拠:
  - Neyhart et al. (2024) は cortical ACh dynamics が cholinergic axon activity と behavioral state からかなり予測できる一方、距離と clearance kinetics に依存する局所性が残ることを示しました。
  - Cahill et al. (2024) は local, transient neurotransmitter inputs が broad cortical astrocyte network に minutes-long に符号化されることを示しました。
  - Vadisiute et al. (2024) は acute chemogenetic manipulation 後に astrocyte、microglia、synaptic density が急速に変化することを示しました。
- 修正:
  - `connectome-only baseline を置かずに、追加した state variable が効いたとは書かない` という site rule を追加しました。
  - `proxy specificity`、`family / uncertainty`、`abstention` を同時提出物へ含める運用へ更新しました。

### 3. 状態変数の完全性ゲートが、Verification 側ではなお `欠測リスト` 寄りでした

- 問題:
  - `verification.md` の `状態変数の完全性ゲート` は、何が欠けるかを示す表としては有用でしたが、研究者が次に出すべき提出物が一覧しにくい構造でした。
  - そのため、読者が `状態変数が足りない` を理解しても、`何を baseline に何と比較するのか` が読み取りにくい状態でした。
- 根拠:
  - MICrONS、Gamlin、Neyhart、Cahill、Hadzibegovic らの一次文献は、追加情報の価値が `どの状態変化・回復・課題条件で効くか` を分解して読むべきことを示しています。
- 修正:
  - `verification.md` に `augmentation claim` の比較表を追加しました。
  - `+ same-brain function / behavior`、`+ transcriptomic / cell-type label`、`+ neuromodulatory proxy`、`+ glial / slow-state`、`+ excitability / homeostatic recovery log` について、最低限ほしい比較と不合格時の読み替えを固定しました。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `augmentation / ablation` 節を追加
  - `connectome-only baseline` を明示
  - `state-variable augmentation claim` の最低提出物を表へ追加
  - Vadisiute (2024)、Hadzibegovic (2026) を参考文献へ追加
- `verification.md`
  - `状態変数の完全性ゲート` に augmentation claim の比較表を追加
  - connectome / same-brain function / transcriptomic label / neuromodulatory proxy / glial state / recovery log を比較可能な提出物へ変換
  - 関連する primary papers を参考文献へ追加

## 外部依存で保留

- same-brain augmentation benchmark の実データ整備
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: connectome-only baseline と augmentation 条件を同一 split で比較できる公開データ
  - 完了条件: cross-state / cross-day / perturbation / recovery を含む predictive gain を site-wide に再利用できる schema で公開すること

## 参考文献

- Lappalainen JK, Tschopp FD, Prakhya S, et al. Connectome-constrained networks predict neural activity across the fly visual system. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07939-3
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08805-6
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. Nature Neuroscience. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. Cell Reports. 2024.
  - https://doi.org/10.1016/j.celrep.2024.114808
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Vadisiute A, Meijer E, Therpurakal RN, et al. Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. Communications Biology. 2024.
  - https://doi.org/10.1038/s42003-024-06994-w
- Hadzibegovic N, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. Nature Communications. 2026.
  - https://doi.org/10.1038/s41467-025-66975-3
