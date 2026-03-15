# Site Deepening Audit (2026-03-15, Closed-Loop Longitudinal Deployment / Recalibration Burden)

## 対象

- 主対象: `wiki/closed-loop-latency-jitter-and-safety-stops.md`

## 今回の選定理由

- 現行の `閉ループ・遅延・ジッタ・安全停止` は、2010-2021 年の timing / synchronization / phase-locking 文献を整理する入門としては有用でした。
- しかし 2026-03-15 時点では、2024-2026 年の一次文献が示した `長期運用` `speech streaming` `在宅 deployability` の壁が十分に反映されていませんでした。
- とくに公開ページは、閉ループを `loop が 1 回速く動くか` の問題として読む構造が残っており、`tail latency` `recalibration burden` `programming burden` を timing とは別の主変数として扱えていませんでした。
- これは技術・自然科学の観点で弱点です。なぜなら、現在の強い一次証拠は `固定閾値` よりも、`どの loop class か`、`どこが律速か`、`何日ごとに人手再較正が要るか`、`clinic から home へ持ち出せるか` の方にあります。

## 主要な批判点

### 1. 旧ページは `speech neuroprosthesis` を独立ループ型として扱っていませんでした

- 問題:
  - 旧版の 4 類型は `state feedback` `ERP/command` `phase-locked stimulation` `adaptive DBS` でした。
  - しかし、streaming brain-to-voice / voice-synthesis BCI は、phase loop でも burst loop でもなく、`tail latency` `audio output path` `silence fallback` `false speech suppression` が主指標になる別系統です。
- 根拠:
  - Littlejohn et al. (2025) は 80 ms increments の streaming brain-to-voice を示し、go cue から音声生成までの分布を別に出しました。
  - Wairagkar et al. (2025) は 10 ms 未満の neural-to-voice synthesis を示しつつ、closed-loop feedback は audio driver に律速されうること、さらに non-speech / overlapping speech では silence を返す設計を示しました。
- 修正:
  - `wiki/closed-loop-latency-jitter-and-safety-stops.md` に `streaming communication / speech neuroprosthesis` を第 3 の loop class として追加しました。
  - 併せて、`per-step inference latency` `cue-to-output latency` `audio driver latency` `silence / false-speech rate` `recalibration event` を主要ログへ追加しました。

### 2. 旧ページは `recalibration burden` を drift の一般論に埋め込みすぎていました

- 問題:
  - 旧版の `drift` と `freeze` の説明は概念として正しかった一方、`daily supervised recalibration がどれだけ実用障害になるか` を実証レベルで前面化していませんでした。
  - その結果、within-session の低遅延ループが、そのまま日常利用へ伸びるように読める余地が残っていました。
- 根拠:
  - Wilson et al. (2025) は、frequent daily supervised recalibration が日常利用の主要な障害であると明示し、multiple timescales の drift を扱う unsupervised recalibration を 1 か月の closed-loop で評価しました。
- 修正:
  - 新たに `2026-03 文献監査：長期運用で増える 3 つの壁` 節を追加し、`recalibration burden / drift` を独立壁として切り出しました。
  - `time since last supervised calibration` `unsupervised adaptation` `performance decay curve` `recovery time` `human intervention time` を主要ログへ引き上げました。

### 3. 旧ページは `deployability` を loop quality と混ぜていました

- 問題:
  - 旧版は adaptive DBS を burst 検出遅延や停止規則として整理していましたが、`clinic / home 転移` や `programming burden` を別の審査軸として扱っていませんでした。
  - これでは、ラボや病院内で制御が成立したことを、そのまま chronic deployment の成立に読み替えやすくなります。
- 根拠:
  - Oehrn et al. (2024) は chronic aDBS を in-clinic / at-home の両方で評価しました。
  - Cascino et al. (2026) は chronic cDBS の連続症例 20 例中 9 例が aDBS 適格、2025 年 7 月時点で 5 例継続と報告し、technical / programming constraints が adoption を制限することを示しました。
- 修正:
  - `naturalistic deployment / programming burden` を第 3 の別壁として追加しました。
  - `clinic/home performance gap` `eligibility` `continuation` `programming change` `stimulation duty cycle` を deployment 側のログとして要求しました。

### 4. 旧ページは `silence / hold-last-output` を棄権・停止と分離できていませんでした

- 問題:
  - 旧版の停止表は `棄権` `freeze` `安全停止` の 3 類型でした。
  - しかし speech / streaming 系では、`短い不確実性や非発話区間を silence で返す` 動作は、棄権や hard stop と運用目的が異なります。
- 根拠:
  - Wairagkar et al. (2025) は non-speech / overlapping speech 区間で silence を返す設計を明示しました。
- 修正:
  - `hold-last-output / silence fallback` を独立行として追加しました。
  - `発動率` `最大継続時間` `false speech suppression` `解除遅延` を最低ログへ追加しました。

## 今回実行した変更

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - `last_updated` を 2026-03-15 に更新
  - front matter の highlights / known / unknown を 2024-2026 文献に合わせて更新
  - `streaming communication / speech neuroprosthesis` を loop class 表へ追加
  - `2026-03 文献監査：長期運用で増える 3 つの壁` 節を新設
  - `hold-last-output / silence fallback` を停止表へ追加
  - checklist を `module-wise latency` `speech-specific logs` `recalibration burden` `naturalistic deployment` へ拡張
  - `L3 の主張を読むときの 6 問` に更新
  - 参考文献へ Littlejohn (2025), Wairagkar (2025), Wilson (2025), Oehrn (2024), Cascino (2026) を追加

## 外部依存で保留

- speech BCI と chronic aDBS を横断する共通 deployment benchmark
  - 担当者: AI / maintainer / 実験系 collaborators
  - 前提条件: `tail latency` `silence fallback` `recalibration burden` `clinic/home transfer` `programming burden` を共通 schema で記録する公開運用ログがあること
  - 完了条件: `閉ループが速い` と `閉ループが長期に使える` を別の score として公開比較できること

## 参考文献

- Wilson JA, Mellinger J, Schalk G, Williams JC. A procedure for measuring latencies in brain-computer interfaces. *IEEE Trans Biomed Eng*. 2010.
  - https://doi.org/10.1109/TBME.2010.2047259
- Mowla MR, Huggins JE, Thompson DE. Enhancing P300-BCI performance using latency estimation. *Brain Comput Interfaces*. 2017.
  - https://doi.org/10.1080/2326263X.2017.1338010
- Belinskaia A, Smetanin N, Lebedev M, Ossadtchi A. Short-delay neurofeedback facilitates training of the parietal alpha rhythm. *J Neural Eng*. 2020.
  - https://doi.org/10.1088/1741-2552/abc8d7
- Mansouri F, Fettes P, Schulze L, et al. A Real-Time Phase-Locking System for Non-invasive Brain Stimulation. *Front Neurosci*. 2018.
  - https://doi.org/10.3389/fnins.2018.00877
- Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimul*. 2018.
  - https://doi.org/10.1016/j.brs.2017.11.016
- Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. *Ann Neurol*. 2013.
  - https://doi.org/10.1002/ana.23951
- Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. *Brain*. 2017.
  - https://doi.org/10.1093/brain/awx010
- Appelhoff S, Stenner T. In COM we trust: Feasibility of USB-based event marking. *Behav Res Methods*. 2021.
  - https://doi.org/10.3758/s13428-021-01571-z
- Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neurosci*. 2025.
  - https://doi.org/10.1162/IMAG.a.136
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. *Nat Med*. 2024.
  - https://doi.org/10.1038/s41591-024-03196-z
- Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. *npj Parkinsons Dis*. 2026.
  - https://doi.org/10.1038/s41531-026-01269-z
