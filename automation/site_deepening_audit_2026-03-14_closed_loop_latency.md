# Site Deepening Audit (2026-03-14, Closed-Loop Timing / Safety)

## 対象

- 主対象: `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 前回監査で EEG・decode/emulate・multimodal integration はかなり具体化されましたが、`閉ループ` 周辺はまだ一般論と強い閾値主張が混在していました。
- 特に `tech_roadmap.md` の M2 節は、ガンマ同期から `1 ms 以下` や `microsecond 級同期` をほぼ共通要件のように読める構造でした。
- しかし、2026-03 時点の一次文献が支持するのは、`閉ループの時間要件はループ種別ごとに異なる` という整理であり、単一閾値の site-wide 適用ではありません。

## 主要な批判点

### 1. 現行 Roadmap は「単一の timing 閾値」で閉ループ全体を語っていました

- 問題:
  - `tech_roadmap.md` は、phase synchronization の難しさから `1 ms 以下のジッタ許容` と `microsecond 単位の計測同期` を強く打ち出していました。
  - しかし、それは phase-targeted loop の一部では重要でも、slow neurofeedback や adaptive DBS にそのまま一般化できません。
- 根拠:
  - Wilson et al. (2010) は、BCI timing を input / processing / output で分けて hardware 実測する必要を示しました。
  - Belinskaia et al. (2020) は、alpha neurofeedback で追加 250 / 500 ms 遅延が学習を悪化させることを示しました。ここで重要なのは `短い方がよい` であって、site-wide に `1 ms` を要求することではありません。
  - Mansouri et al. (2018) と Zrenner et al. (2018) は、phase-targeting 系では delay を `位相誤差` に写像して評価すべきことを示しました。
  - Little et al. (2013) と Tinkhauser et al. (2017) の adaptive DBS 文脈では、支配時定数は beta burst であり、phase-locked stimulation より遅い帯域です。
- 修正:
  - M2 の note を全面差し替え、`loop class ごとに end-to-end 実測を残す` 形へ変更しました。
  - I1 も `state feedback / ERP-command / phase-locked / burst-driven` の 4 区分で読む構造へ修正しました。

### 2. 現行 wiki は概念説明としては正しいが、一次文献と監査項目が不足していました

- 問題:
  - 旧 `wiki/closed-loop-latency-jitter-and-safety-stops.md` は「遅延」「ジッタ」「ドリフト」「安全停止」の用語整理としては有用でした。
  - ただし、`なぜ固定閾値が危険か`、`どの loop class で何を測るべきか`、`marker と end-to-end をどう分けるか` が一次文献で支えられていませんでした。
- 根拠:
  - Thompson et al. (2013) と Mowla et al. (2017) は、ERP 系 BCI で latency jitter が性能に効くことを示しました。
  - Appelhoff & Stenner (2021) は USB marker で sub-ms event marking を示しましたが、これは marker path の精度であって loop 全体の保証ではありません。
  - Kothe et al. (2025) は LSL の synchronized multimodal recording を整理しましたが、software-based synchronization と physical actuation onset は分けて扱う必要があります。
- 修正:
  - wiki を `4 つの loop class` と `4 つの監査層`（end-to-end、marker/sync、phase/burst 指標、停止規則）で全面改稿しました。
  - 参考文献を一次文献中心で追加しました。

### 3. 現行記述は「同期」と「出力実測」と「安全停止」を混ぜていました

- 問題:
  - LSL、TTL marker、photodiode、phase estimator、安全停止は、似て見えて別の層です。
  - 旧ページではこの差が十分に明示されておらず、`LSL があるから timing は十分` と誤読される余地がありました。
- 根拠:
  - Kothe et al. (2025) は LSL を software-based synchronization として示しています。
  - Wilson et al. (2010) は output path を別に測る必要を示しています。
  - Appelhoff & Stenner (2021) は marker path の高速化を示していますが、display/stimulator path とは別問題です。
- 修正:
  - `LSL が保証すること / しないこと` を独立節に分離しました。
  - `棄権 / freeze / 安全停止` を trigger と log の違いまで表で固定しました。

## 今回実行した変更

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - 2026-03-06 版の一般説明を、一次文献ベースの evidence refresh 版へ全面改稿
  - `固定閾値が危険な理由`、`4つの loop class`、`LSL と marker の役割差`、`最低限残すログ`、`参考文献` を追加
- `tech_roadmap.md`
  - M2 の `1 ms / microsecond` 前提を撤回し、loop class ごとの監査へ差し替え
  - I1 の `閉ループ` を loop class と end-to-end 指標で再定義
  - timing/synchronization 文献の参照セットを更新

## 外部依存で保留

- ヒトでの phase-specific stimulation と adaptive DBS を同一ベンチへ入れる共通評価系の構築
  - 担当者: AI / maintainer / 実験系 collaborators
  - 前提条件: IRB、刺激機材、closed-loop 実験環境
  - 完了条件: 共通の end-to-end latency / phase error / stop-rule schema で比較できる実験系が整うこと

## 参考文献

- Wilson JA, Mellinger J, Schalk G, Williams JC. A procedure for measuring latencies in brain-computer interfaces. IEEE Trans Biomed Eng. 2010.
  - https://doi.org/10.1109/TBME.2010.2047259
- Thompson DE, Warschausky SA, Huggins JE. Classifier-based latency estimation: a novel way to estimate and predict BCI accuracy. J Neural Eng. 2013.
  - https://doi.org/10.1088/1741-2560/10/1/016006
- Mowla MR, Huggins JE, Thompson DE. Enhancing P300-BCI performance using latency estimation. Brain Comput Interfaces. 2017.
  - https://doi.org/10.1080/2326263X.2017.1338010
- Belinskaia A, Smetanin N, Lebedev M, Ossadtchi A. Short-delay neurofeedback facilitates training of the parietal alpha rhythm. J Neural Eng. 2020.
  - https://doi.org/10.1088/1741-2552/abc8d7
- Mansouri F, Fettes P, Schulze L, et al. A real-time phase-locking system for non-invasive brain stimulation. Front Neurosci. 2018.
  - https://doi.org/10.3389/fnins.2018.00877
- Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. Brain Stimul. 2018.
  - https://doi.org/10.1016/j.brs.2017.11.016
- Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. Ann Neurol. 2013.
  - https://doi.org/10.1002/ana.23951
- Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. Brain. 2017.
  - https://doi.org/10.1093/brain/awx010
- Appelhoff S, Stenner T. In COM we trust: Feasibility of USB-based event marking. Behav Res Methods. 2021.
  - https://doi.org/10.3758/s13428-021-01571-z
- Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. Imaging Neurosci. 2025.
  - https://doi.org/10.1162/IMAG.a.136
