# Site Deepening Audit (2026-03-14, Connectome / State Completeness)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`

## 今回の選定理由

- 公開サイトにはすでに `connectome-complete は emulation-complete ではない` という正しい方向性がありましたが、2026-03-14 時点の本文は主として `欠ける状態変数の列挙` に留まっていました。
- しかし、2024-2025 の一次文献が示している重要点は 2 段あります。
  1. 配線図から落ちる state variable が複数あること。
  2. たとえ connectome-constrained にしても、未測定の細胞・シナプス・修飾パラメータが残ると dynamics 自体が縮退しうること。
- 旧版は前者は押さえていましたが、後者の `identifiability wall` が弱く、読者が `connectome + 少し activity が合う = 内部状態がかなり分かった` と誤読する余地がありました。

## 主要な批判点

### 1. 旧版は「欠ける state variable」を説明していたが、「connectome-constrained でも残る縮退」を独立論点として扱っていませんでした

- 問題:
  - 旧版は `細胞型 / シナプス / 遅延 / 神経修飾 / グリア` を正しく挙げていました。
  - しかし、connectome を既知にしても内部 dynamics がしばしば一意にならない、という推定論上の壁を本文で明示していませんでした。
- 根拠:
  - Beiran & Litwin-Kumar (2025) は、connectome-constrained recurrent network でも biophysical parameter の違いで未観測ニューロンの dynamics が大きく変わりうることを示しました。
  - Lappalainen et al. (2024) は fly visual system で connectome-constrained model を前進させましたが、著者自身が electrical synapses、nonlinear chemical synapses、neuromodulation を reductionist model の説明外に置いています。
- 修正:
  - `5 つの状態クラス` に加えて `1 つの推定上の壁（パラメータ縮退）` を追加しました。
  - `connectome-constrained model` を unique internal state ではなく `hypothesis engine / conditional model` として読む site rule を明記しました。

### 2. 旧版は state class ごとの「危険な誤読」と「claim downgrade」を固定していませんでした

- 問題:
  - 旧版は各 state class を紹介していましたが、`何を過大主張とみなすか`、`欠けたままならどの claim を止めるべきか` が表で固定されていませんでした。
  - このため、unlabeled graph、edge count、pupil/HRV などを、読者がそのまま機能的十分条件や transmitter ground truth と誤読しうる構造でした。
- 根拠:
  - MICrONS Consortium (2025) は、哺乳類皮質では同じ cell type 内にも異なる tuning preference をもつニューロンがあり、same-brain connectivity と function を結んで読む必要があることを示しました。
  - Gamlin et al. (2025) は、予測された Sst transcriptomic types ごとに結合・シナプス特性・髄鞘化が異なることを示しました。
  - Holler et al. (2021) と Matsuzaki et al. (2004) は、synapse が binary edge ではなく ultrastructure / weight / plastic history を持つことを示しました。
  - Vardalaki et al. (2022) は、成体新皮質でも filopodia が silent synapse の構造基盤になりうることを示しました。
  - Reimer et al. (2016) と Neyhart et al. (2024) は、瞳孔や行動状態が cholinergic / adrenergic dynamics を反映しても、局所 release / clearance や transmitter specificity を置き換えないことを示しました。
- 修正:
  - 冒頭表を `何が欠けるか / 危険な誤読 / 現時点での扱い` の 4 列へ再構成しました。
  - `weights / delays が無いときは位相・介入・閉ループ claim を降格する` など、site-wide に使える運用ルールを明文化しました。

### 3. 旧版は「この議論から何を提出物として要求するか」が弱く、実務へ落ちにくかった

- 問題:
  - 旧版は概念としては妥当でしたが、読者や将来の編集者が `では何を出せば L1 / L2 / L3 に近い claim をしてよいのか` を判断しにくい構造でした。
- 根拠:
  - state completeness の議論は、単なる caution note で終わると運用に効きません。
  - 実際には、構造 atlas、条件付き dynamical claim、介入・閉ループ claim で必要提出物が異なります。
- 修正:
  - `このサイトで採用する読み替えルールと最低提出物` 節を新設しました。
  - `構造 atlas / scaffold`、`条件付き dynamical claim`、`介入・閉ループ claim` の 3 段で最低提出物を表にしました。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - front matter を `state variable の欠落 + connectome-constrained 推定の限界` へ更新
  - 冒頭表を `5 state classes + 1 inferential wall` へ拡張
  - `見落としやすい第0の問題：配線が分かっても dynamics はまだ縮退します` 節を追加
  - `危険な誤読` と `現時点での扱い` を表で固定
  - `最低提出物` の表を追加
  - 2022-2025 の一次文献を追加

## 外部依存で保留

- same-brain multimodal / perturbation を用いた `state completeness benchmark` の実装
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: 公開可能な connectomics + same-brain physiology + perturbation データ、またはそれに準じる benchmark
  - 完了条件: `欠測 state variable` と `残存 family` を同じ schema で比較できる公開評価系が整うこと

## 参考文献

- Dorkenwald S, McKellar CE, Macrina T, et al. Neuronal wiring diagram of an adult brain. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Lappalainen JK, Tschopp FD, Prakhya S, et al. Connectome-constrained networks predict neural activity across the fly visual system. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07939-3
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08805-6
- Holler S, et al. Structure and function of a neocortical synapse. Nature. 2021.
  - https://doi.org/10.1038/s41586-020-03134-2
- Matsuzaki M, Honkura N, Ellis-Davies GCR, Kasai H. Structural basis of long-term potentiation in single dendritic spines. Nature. 2004.
  - https://doi.org/10.1038/nature02617
- Vardalaki D, Chung K, Harnett MT. Filopodia are a structural substrate for silent synapses in adult neocortex. Nature. 2022.
  - https://doi.org/10.1038/s41586-022-05483-6
- Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. Science. 2014.
  - https://doi.org/10.1126/science.1252304
- McKenzie IA, et al. Motor skill learning requires active central myelination. Science. 2014.
  - https://doi.org/10.1126/science.1254960
- Micheva KD, Kiraly M, Perez MM, Madison DV. Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. Cereb Cortex. 2021.
  - https://doi.org/10.1093/cercor/bhab018
- Reimer J, et al. Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. Nat Commun. 2016.
  - https://doi.org/10.1038/ncomms13289
- Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. Cell Reports. 2024.
  - https://doi.org/10.1016/j.celrep.2024.114808
- Adamsky A, et al. Astrocytic activation generates de novo neuronal potentiation and memory enhancement. Nat Neurosci. 2018.
  - https://doi.org/10.1038/s41593-018-0253-6
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
