# Site Deepening Audit (2026-03-31, front-door sleep replay route-family sync)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
- 調査範囲:
  - 技術
  - 自然科学
- 除外:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
- `verification.md`
- `wbe_101.md`

では既に `sleep replay route card` が入っており，`sleep history` と `sleep architecture / replay-coupling` の分離も成立しておりました．

- しかし front door に当たる `index.md` には，睡眠再活性化系を独立の route-family として止める note がまだございませんでした。
- `faq.md` の `Q2c` でも，sleep/homeostasis は出てくる一方で，
  - phase-locked auditory stimulation
  - endogenous scalp decoding
  - intracranial closed-loop synchrony intervention
  - spindle-locked ripple evidence
  - spindle-phase-sensitive cueing
  - item-selective / difficulty-selective TMR effects
  の分離が front-door waterline で明示されておりませんでした。

このままですと読者は

- `sleep happened`
- `a cue was delivered`
- `overnight memory changed`
- `replay-coupling matched`

を近いものとして読めます．これは現在の一次文献が支持する読み方ではございません。

## web確認対象

- https://doi.org/10.1016/j.neuron.2013.03.006
- https://doi.org/10.1038/s41467-021-23520-2
- https://doi.org/10.1038/s41593-023-01324-5
- https://doi.org/10.1038/s41467-024-49572-8
- https://doi.org/10.1016/j.neuroimage.2025.121530
- https://doi.org/10.1038/s41467-025-57766-x
- https://doi.org/10.1038/s41539-025-00340-3

## 根拠付き批判

### 1. front-door では sleep replay 系がまだ一段圧縮されておりました

- 既存の深いページでは，sleep replay 系はすでに route-card 化されております。
- それにもかかわらず `index.md` と `faq.md` では，sleep/homeostasis は見えても，
  - 何を直接見た研究なのか
  - timing policy がどこまで causal に効いたのか
  - item selection がどうなっているのか
  - overnight gain が何を意味するのか
  が front door で固定されておりませんでした。

批判:

- この構造では，読者が `sleep replay evidence` を一つの mechanistic rung と誤読できます。
- 中核 rule が深いページだけにあり，入口で停止線が立っていないのは site-wide policy と不整合でございます。

### 2. 現在の一次文献は timing policy を route-family の一部として扱うべきことを示しております

- [Ngo et al. (2013)](https://doi.org/10.1016/j.neuron.2013.03.006) は，ヒトで `auditory closed-loop stimulation` が slow oscillation の位相に依存して記憶改善を示す route でございます。
- [Geva-Sagiv et al. (2023)](https://doi.org/10.1038/s41593-023-01324-5) は，ヒト睡眠中の real-time intracranial closed-loop DBS において，precise timing を外すと electrophysiological / behavioral effect が消失ないし悪化しうることを示しました。
- [Jourde et al. (2025)](https://doi.org/10.1016/j.neuroimage.2025.121530) は，auditory stimulation efficacy 自体が thalamocortical spindle phase に依存することを示しました。

批判:

- したがって `sleep stimulation worked` は，
  - `phase-locked intervention worked`
  - `the relevant replay timing variable was matched`
  と同義ではございません。
- timing policy を書かずに cueing result を mechanistic replay evidence に繰り上げるのは不正確でございます。

### 3. observational / perturbational / ripple-linked evidence は同じ object を返しません

- [Schreiner et al. (2021)](https://doi.org/10.1038/s41467-021-23520-2) は endogenous scalp-EEG decoding around aggregated SO-spindle complexes の route でございます。
- [Schreiner et al. (2024)](https://doi.org/10.1038/s41467-024-49572-8) は human NREM における spindle-locked ripples と reactivation の関係を示す route でございます。
- [Geva-Sagiv et al. (2023)](https://doi.org/10.1038/s41593-023-01324-5) は intracranial closed-loop synchrony intervention でございます。

批判:

- scalp decoding, spindle-ripple evidence, intracranial stimulation は direct observable も spatial access も causal leverage も異なります。
- これらを一括して `sleep replay evidence` とだけ呼ぶと，claim ceiling が不当に高く見えます。

### 4. TMR benefit 自体も one-sign outcome ではございません

- [Duan et al. (2025)](https://doi.org/10.1038/s41467-025-57766-x) は，同一の human TMR session 内でも strengthening items と decaying items が混在しうることを示しました。
- [Shin et al. (2025)](https://doi.org/10.1038/s41539-025-00340-3) は，benefit が difficult / challenging memories に集中しうることを示しました。

批判:

- したがって `overnight gain` や `TMR improved memory` を generic replay-success row にしてはいけません。
- memory target / selection regime を切り分けない限り，平均効果は mechanism を代表しません。

## 今回実行した変更

### `index.md`

- `page_highlights` に，sleep replay evidence が
  - phase-locked auditory stimulation
  - endogenous scalp decoding
  - intracranial closed-loop synchrony
  - spindle-locked ripple evidence
  - spindle-phase-sensitive cueing
  - item-selective / difficulty-selective TMR
  に分かれることを明示する bullet を追加しました。
- `If You Are Treating Sleep Replay Evidence As One Solved Row` note-box を新設しました。
- front door の safe reading を
  - `a cue was delivered during sleep`
  - `overnight memory changed`
  - `replay-coupling matched`
  は別 claim である
  と読める文言へ更新しました。

### `faq.md`

- `page_highlights` に sleep replay route-family split を追加しました。
- `known_points` に，sleep history と sleep architecture / replay-coupling が別変数であり，sleep replay 内部も別 route-family であることを追加しました。
- `Q2c` に，新しい sleep replay paragraph を追加しました。
  - Ngo 2013
  - Schreiner 2021
  - Geva-Sagiv 2023
  - Schreiner 2024
  - Jourde 2025
  - Duan 2025
  - Shin 2025
  を使い，front-door で mechanistic overread を止める文面へ改稿しました。
- 参考文献一覧に上記 7 本を追加しました。

## 今回止めた誤読

- `sleep happened` = `replay-coupling matched`
- `a cue was delivered during sleep` = `phase-specific replay intervention succeeded`
- `overnight gain` = `the same mechanism improved all items`
- `one TMR effect` = `one common mechanistic object`
- `intracranial closed-loop success` = `scalp-observed replay evidence is already equivalent`

## 検証

- `bundle exec jekyll build`
- `git diff --check`
- `git diff --stat`

## external dependency tasks

- なし
  - 今回の作業は，文献確認，front-door 改稿，検証，commit，push までこのセッションで完結できます。

## 参考文献

1. Ngo HVV, Martinetz T, Born J, Mölle M. Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. *Neuron*. 2013. https://doi.org/10.1016/j.neuron.2013.03.006
2. Schreiner T, Petzka M, Staudigl T, Staresina BP. Endogenous memory reactivation during sleep in humans is clocked by slow oscillation-spindle complexes. *Nature Communications*. 2021. https://doi.org/10.1038/s41467-021-23520-2
3. Geva-Sagiv M, Mankin EA, Eliashiv D, et al. Augmenting hippocampal-prefrontal neuronal synchrony during sleep enhances memory consolidation in humans. *Nature Neuroscience*. 2023. https://doi.org/10.1038/s41593-023-01324-5
4. Schreiner T, Griffiths BJ, Kutlu M, et al. Spindle-locked ripples mediate memory reactivation during human NREM sleep. *Nature Communications*. 2024. https://doi.org/10.1038/s41467-024-49572-8
5. Jourde N, Fattinger S, Teague M, et al. The effectiveness of auditory stimulation in sleep varies with thalamocortical spindle phase. *NeuroImage*. 2025. https://doi.org/10.1016/j.neuroimage.2025.121530
6. Duan W, Xu Z, Chen D, et al. Electrophysiological signatures underlying variability in human memory consolidation. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57766-x
7. Shin G-H, Kweon Y-S, Oh S, et al. Personalized targeted memory reactivation enhances consolidation of challenging memories via slow wave and spindle dynamics. *npj Science of Learning*. 2025. https://doi.org/10.1038/s41539-025-00340-3
