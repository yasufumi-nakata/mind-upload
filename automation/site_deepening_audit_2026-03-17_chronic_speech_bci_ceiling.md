# Site Deepening Audit (2026-03-17, Chronic Speech BCI Ceiling / decode ≠ chronic emulate)

## 対象

- 主対象: `perspective.md`
- 主対象: `wiki/decode-vs-emulate.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`decode ≠ emulate`、`multimodal ≠ state-complete`、`same-day fit ≠ cross-day maintenance` をかなり明確に区別できていました。
- その一方で、2025 年の speech neuroprosthesis 前線を読むときに重要になる `same-session streaming success ≠ chronic deployability ≠ stable mechanism readout` の 3 段階が、主要本文ではまだ十分 operational ではありませんでした。
- とくに `Perspective` の `Research Program` は、技術的提出物よりも抽象的な終点へ寄っており、`decode 側の前進をどの evidence gate で止めるか` が supporting wiki ほど明示されていませんでした。

## 主要な批判点

### 1. 旧サイトは、speech BCI の `same-session streaming` と `longitudinal deployment` の境界を主要本文で十分に固定していませんでした

- 問題:
  - `wiki/decode-vs-emulate.md` と `perspective.md` は、language prior、tail latency、cross-day 一般化の重要性を正しく書いていました。
  - しかし、2025 年の streaming / voice-synthesis neuroprosthesis が押し上げたのは主に `communication subsystem` であり、その次の壁が `fixed decoder longevity` と `recalibration burden` であることは、主要本文ではまだ弱く、支援ページへ分散していました。
- 根拠:
  - Littlejohn et al. (2025) は、speech synthesis を 80 ms increments で online large-vocabulary に前進させました。
  - Wairagkar et al. (2025) は、instantaneous voice synthesis と silence fallback を示しましたが、fixed decoder を post-implant day 165 で固定した評価では、およそ 15 日以降に目立つ性能低下も示しています。
  - Wilson et al. (2025) は、cursor iBCI において one-month の unsupervised recalibration を検証し、accumulating neural changes を補償しない fixed decoder が長期使用で崩れることを示しました。
- 批判:
  - したがって、`streaming に動いた`、`音声になった`、`無音時に silence fallback できた` を、そのまま `recalibration-light で chronic deployable` と読むことはできません。
  - speech BCI の主張を上げるには、`fixed decoder interval`、`time since last supervised calibration`、`recovery time`、`recalibration burden` を主要提出物へ上げる必要があります。

### 2. 旧サイトは、microelectrode 系の `same neuron across days` を decode/emulate 境界の核心へ十分に接続していませんでした

- 問題:
  - サイト全体では chronic unit identity の話題がすでに存在しましたが、`decode-vs-emulate` と `Perspective` の speech BCI 説明では、same-neuron claim が観測事実ではなく、motion correction・spike sorting・probabilistic matching を介した推定であることが前面に出ていませんでした。
- 根拠:
  - Steinmetz et al. (2021) は、stable long-term recording を前進させた一方で、automatic post hoc correction for brain movements を必要条件として示しました。
  - Pachitariu et al. (2024) は、drift、split / merge error を spike sorting の中心課題として扱いました。
  - van Beest et al. (2025) は、UnitMatch により cross-day matching を probability 付きで扱い、days between recordings で tracking probability が下がることを示しました。
  - Pun et al. (2024) は、human intracortical recordings で instability が closed-loop performance 低下と高相関することを示しました。
- 批判:
  - したがって、chronically implanted microelectrode array の成功を `stable single-neuron mechanism was read out` と書くのは過大でございます。
  - 少なくとも、`sorting version`、`drift correction`、`unit-match probability`、`dropout / new-unit rate` を hidden にしてはいけません。

### 3. 旧 `Perspective` の研究計画は、技術・自然科学の提出物より抽象的な終点へ寄りすぎていました

- 問題:
  - `Research Program` は、サイト全体の最近の監査水準に比べると、まだ `何を出せば次の主張に進めるか` が甘く、`communication subsystem → longitudinal benchmark → perturbation / maintenance-state benchmark` の順番が見えにくい構造でした。
- 批判:
  - 技術・自然科学の観点からは、ここで先に固定すべきなのは `本人性維持` のような抽象名詞ではなく、`subsystem scope`、`fixed decoder interval`、`recalibration burden`、`chronic identity audit`、`perturbation consistency` でございます。
  - 研究計画は、`大きな終点` ではなく `提出物と棄権条件` を先に並べる方が一次文献に整合的です。

## 今回実行する変更

- `perspective.md`
  - `last_updated` を `2026-03-17` に更新
  - page highlight / known point に `streaming success ≠ chronic deployability` を追加
  - `Research Program` を、communication subsystem benchmark → chronic stability audit → perturbation / maintenance-state benchmark の順へ改稿
  - `Brain-to-Text` 節に chronic speech BCI ceiling の監査表を追加
  - `fixed decoder interval`、`time since last supervised calibration`、`microelectrode 系の unit identity audit` を必須提出物へ追加
- `wiki/decode-vs-emulate.md`
  - `last_updated` を `2026-03-17` に更新
  - chronic communication ceiling の節を追加
  - same-session streaming、recalibration burden、same-neuron tracking uncertainty を分けて監査する rule を追加
  - site rules と gate を、speech BCI の chronic deployability 条件まで拡張

## 外部依存で保留

- なし
  - 今回の変更は、公開ページ本文と監査ルールの更新で完結します。

## 参考文献

1. Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025;28:902-912.
   - https://doi.org/10.1038/s41593-025-01905-6
2. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025;644:145-152.
   - https://doi.org/10.1038/s41586-025-09127-3
3. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
4. Pun TK, Khoshnevis M, Hosman T, et al. Measuring instability in chronic human intracortical neural recordings towards stable, long-term brain-computer interfaces. *Communications Biology*. 2024;7:1363.
   - https://doi.org/10.1038/s42003-024-06784-4
5. Steinmetz NA, Aydin C, Lebedeva A, et al. Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. *Science*. 2021;372:eabf4588.
   - https://doi.org/10.1126/science.abf4588
6. Pachitariu M, Sridhar S, Pennington J, Stringer C. Spike sorting with Kilosort4. *Nature Methods*. 2024;21:914-921.
   - https://doi.org/10.1038/s41592-024-02595-5
7. van Beest EH, Bimbard C, Fabre JMJ, et al. Tracking neurons across days with high-density probes. *Nature Methods*. 2025;22:778-787.
   - https://doi.org/10.1038/s41592-024-02440-1
