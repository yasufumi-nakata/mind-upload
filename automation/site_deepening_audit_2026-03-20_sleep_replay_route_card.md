# Site Deepening Audit (2026-03-20, Sleep Replay Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 既存サイトはすでに `sleep / wake history` と `sleep architecture / replay-coupling state` を分離しており、この点は正しかったです。
- しかし現状のままだと、`phase-locked auditory stimulation`、`scalp EEG decoding around SO-spindle complexes`、`intracranial closed-loop synchrony intervention`、`item-level strengthening / decay under TMR`、`difficulty-selective benefit` が、まだ同じ `sleep replay evidence` として読めてしまいました。
- これは技術・自然科学の観点では粗すぎます。なぜなら、観測窓・空間アクセス・介入の因果強度・対象記憶の選び方が違えば、主張できる ceiling が変わるからです。

## 主要な批判点

### 1. `sleep replay evidence` が単一の証拠クラスのように見えていました

- 問題:
  - 旧版でも睡眠アーキテクチャの重要性は書かれていましたが、`何を直接見た研究か` がまだ十分に分解されていませんでした。
  - この構造だと、読者が `NREMで coupling があった`、`cue を入れた`、`翌朝スコアが上がった` を近いものとして読んでしまいます。
- 根拠:
  - Ngo et al. (2013) は、健常ヒトで slow oscillation 位相に合わせた auditory stimulation だけが memory と spindle coupling を改善することを示しました。
  - Schreiner et al. (2021) は、健常ヒト scalp EEG で endogenous reactivation を SO-spindle complexes 近傍で復号しましたが、同論文自身が aggregated events・modest decoding・scalp では ripple ground truth に不可知であることを明記しています。
  - Geva-Sagiv et al. (2023) は、ヒト iEEG / intracranial closed-loop DBS による synchrony 増強を示しており、観測・介入の層がまったく異なります。
  - Schreiner et al. (2024) は、ヒト NREM で spindle-locked ripples が memory reactivation と結びつくことを示しました。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` に `sleep replay route card` を新設し、claim family / preparation / event definition / timing policy / memory target / abstention boundary を分離しました。

### 2. `average overnight gain` が mechanistic replay evidence に寄りすぎていました

- 問題:
  - 旧版の safe-reading は `sleep duration` と `architecture` の違いまでは押さえていましたが、`平均的な overnight 改善` と `replay-consistent mechanism` の距離がまだ甘く見えました。
  - 特に TMR 系では、同じ夜でも item ごとの差や難易度依存が大きく、平均 gain だけでは mechanism を固定できません。
- 根拠:
  - Duan et al. (2025) は、ヒト intracranial EEG を用いた TMR で、同一セッション内でも strengthening items と decaying items が混在し、hippocampal-cortical coupling と cortical spindle dynamics の位相が異なることを示しました。
  - Shin et al. (2025) は、personalized TMR の benefit が特に difficult / challenging memories に集中し、slow-wave / spindle coupling との相関もその regime で立つことを示しました。
- 修正:
  - `wbe_101.md` と `verification.md` で `average overnight gain` や `a delivered cue` を、単独では replay-consistent evidence に昇格させない表現へ更新しました。

### 3. `何が latent のまま残るか` が sleep replay だけはまだ曖昧でした

- 問題:
  - 他の hidden-state には route card が増えてきた一方で、sleep replay は `何がまだ見えていないのか` が一段弱く、scalp / iEEG / rodent causal timing をまたいだ overread を止めにくい状態でした。
- 根拠:
  - Schreiner et al. (2021) は scalp EEG では ripple ground truth に不可知であり、個々の SO-spindle event ごとに reactivation が起きたかまでは未確定と述べています。
  - Deng et al. (2025) は、同じ NREM でも consolidation permissive な intracellular window が時間構造を持つことを示しました。
- 修正:
  - `sleep replay route card` に `abstention boundary` を追加し、`scalp では ripple ground truth は未確定` `patient iEEG の一般化は限定的` `cue efficacy と endogenous mechanism は別` を明記する構造にしました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `sleep replay route card` を新設
  - `Sleep architecture / replay-coupling state` の safe-reading を強化
  - `page_highlights` / `unknown_points` を更新
  - Duan et al. (2025), Shin et al. (2025) を参考文献に追加
- `verification.md`
  - maintenance-state budget に sleep replay route card の運用ルールを追加
  - `Sleep architecture / replay-coupling state` 行の提出要件を強化
  - Duan et al. (2025), Shin et al. (2025) を参考文献に追加
- `wbe_101.md`
  - entry page に `Sleep replay evidence now gets its own route card` note を追加
  - hidden-state table の safe-reading を強化
  - Duan et al. (2025), Shin et al. (2025) を参考文献に追加

## 外部依存で保留

- healthy-human whole-brain replay ground truth
  - 担当者: 睡眠 iEEG / multimodal imaging / neurostimulation の実験研究者
  - 前提条件: hippocampal ripple・cortical SO / spindle・behavioral retention を同一 protocol で高密度かつ広域に比較できる計測系
  - 完了条件: scalp proxy・patient iEEG・causal intervention の各 route を同一評価表で比較できる公開 benchmark が整備されること

## 参考文献

1. Ngo H-VV, Martinetz T, Born J, Mölle M. Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. *Neuron*. 2013;78(3):545-553.
   - https://doi.org/10.1016/j.neuron.2013.03.006
2. Maingret N, Girardeau G, Todorova R, Goutierre M, Zugaro M. Hippocampo-cortical coupling mediates memory consolidation during sleep. *Nature Neuroscience*. 2016;19:959-964.
   - https://doi.org/10.1038/nn.4304
3. Latchoumane C-FV, Ngo H-VV, Born J, Shin H-S. Thalamic Spindles Promote Memory Formation during Sleep through Triple Phase-Locking of Cortical, Thalamic, and Hippocampal Rhythms. *Neuron*. 2017;95(2):424-435.e6.
   - https://doi.org/10.1016/j.neuron.2017.06.025
4. Schreiner T, Petzka M, Staudigl T, Staresina BP. Endogenous memory reactivation during sleep in humans is clocked by slow oscillation-spindle complexes. *Nature Communications*. 2021;12:3112.
   - https://doi.org/10.1038/s41467-021-23520-2
5. Geva-Sagiv M, Mankin EA, Eliashiv D, et al. Augmenting hippocampal-prefrontal neuronal synchrony during sleep enhances memory consolidation in humans. *Nature Neuroscience*. 2023;26:1100-1110.
   - https://doi.org/10.1038/s41593-023-01324-5
6. Schreiner T, Petzka M, Staudigl T, et al. Spindle-locked ripples mediate memory reactivation during human NREM sleep. *Nature Communications*. 2024;15:5367.
   - https://doi.org/10.1038/s41467-024-49572-8
7. Deng Z, Fei X, Zhang S, Xu M. A time window for memory consolidation during NREM sleep revealed by cAMP oscillation. *Neuron*. 2025;113(12):1983-1997.e7.
   - https://doi.org/10.1016/j.neuron.2025.03.020
8. Duan W, Xu Z, Chen D, et al. Electrophysiological signatures underlying variability in human memory consolidation. *Nature Communications*. 2025;16:2472.
   - https://doi.org/10.1038/s41467-025-57766-x
9. Shin G-H, Kweon Y-S, Oh S, et al. Personalized targeted memory reactivation enhances consolidation of challenging memories via slow wave and spindle dynamics. *npj Science of Learning*. 2025;10:47.
   - https://doi.org/10.1038/s41539-025-00340-3
