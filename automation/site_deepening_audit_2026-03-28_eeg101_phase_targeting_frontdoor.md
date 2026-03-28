# Site Deepening Audit (2026-03-28, eeg_101 phase-targeting frontdoor)

## 対象

- 主対象:
  - `eeg_101.md`
- 同期対象:
  - `summary_booklet.md` (`ruby scripts/build_summary_booklet.rb` で再生成)
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://mind-upload.com/eeg_101.html`
- `https://mind-upload.com/wiki/closed-loop-latency-jitter-and-safety-stops.html#phase-targeting-wall`
- `https://doi.org/10.3389/fnins.2018.00877`
- `https://doi.org/10.1016/j.brs.2017.11.016`
- `https://doi.org/10.1016/j.neuroimage.2020.116761`
- `https://doi.org/10.3389/fnhum.2021.691821`
- `https://doi.org/10.1111/ejn.14931`
- `https://doi.org/10.1523/ENEURO.0050-23.2023`
- `https://doi.org/10.1016/j.brs.2025.09.019`

## 今回この箇所を選んだ理由

- `eeg_101.md` は EEG を入口から読む読者の主要 frontdoor であり、ここで止められない誤読は後段の wiki で再流入しやすい箇所でございます。
- 2026-03-28 時点の live page `https://mind-upload.com/eeg_101.html` は、closed-loop を `latency / jitter / safe-stop` までは案内しておりましたが、phase-targeting については site 内の深いページほどには stop line が見えておりませんでした。
- そのため、読者が
  - `EEG が速い` = `phase-targeted control の主要技術課題はほぼ解決`
  - `mean phase error が小さい` = `phase-specific physiological control も確認済み`
  - `phase locking に成功` = `機能効果も再現されている`
  - `一度見つかった preferred phase` = `別セッションでも固定的に使える`
  と読んでしまう余地が残っておりました。

## 根拠付き批判

### 1. phase-targeting を generic closed-loop timing に埋め込むと、estimability の壁が見えません

- 根拠:
  - live page `https://mind-upload.com/eeg_101.html` では、closed-loop について `latency / jitter / safe-stop` は案内されていた一方、`oscillation estimability`、`power/SNR gate`、`no-stim rate` は入口ページで明示されておりませんでした。
  - [Zrenner et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116761) は、real-time phase estimation の ground truth 自体が oscillatory amplitude と SNR に強く依存することを示しました。
  - [Kim et al. (2023)](https://doi.org/10.1523/ENEURO.0050-23.2023) は、11 公開 dataset・484 participants で、phase prediction accuracy が cognitive state 一般より power / SNR 条件に大きく依存することを示しました。
- 批判:
  - したがって、EEG intro が phase-targeting を generic realtime use の一部としてしか語らないと、読者は `速さ` を `位相推定可能性` と取り違えます。
  - 入口ページでも `estimability` を first gate として見せる必要がございました。

### 2. targeting accuracy と downstream effect は別 object です

- 根拠:
  - [Mansouri et al. (2018)](https://doi.org/10.3389/fnins.2018.00877) と [Zrenner et al. (2018)](https://doi.org/10.1016/j.brs.2017.11.016) は、real-time phase-triggering feasibility を示しました。
  - しかし [Vigué-Guix et al. (2022)](https://doi.org/10.1111/ejn.14931) は、real-time EEG-based BCI で reliable trial-to-trial alpha phase locking を達成しつつ、一貫した behavioral benefit は得られないことを示しました。
- 批判:
  - したがって `phase locking が成立した` を `機能的制御が成立した` と読むのは不適切でございます。
  - 入口ページにも `targeting success != downstream effect` の停止線が必要でございました。

### 3. causal estimator benchmark がなければ、phase error 自体の意味が不安定です

- 根拠:
  - [Gordon et al. (2021)](https://doi.org/10.3389/fnhum.2021.691821) は、prefrontal theta targeting で low-theta epoch と phase-reset epoch を除外し、post-hoc benchmark と比較して初めて読める形にしました。
  - [Zrenner et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116761) も、real-time phase estimation の "ground truth" が method-dependent であることを問題化しました。
- 批判:
  - つまり `mean phase offset` 単独では、因果的に使った estimator が post-hoc reconstruction とどの程度整合したのか不明でございます。
  - 入口ページで `phase error` だけを想起させると、benchmark 不在のまま数値だけが独り歩きいたします。

### 4. preferred phase は固定 object ではなく、安定性監査が必要です

- 根拠:
  - [Hougland et al. (2025)](https://doi.org/10.1016/j.brs.2025.09.019) は、high corticospinal excitability と関連する optimal sensorimotor mu-phase が within-session でも揺らぎ、test-retest reliability が低いことを示しました。
- 批判:
  - したがって `one preferred phase` を普遍的制御点として frontdoor で暗黙視させるのは危険でございます。
  - 入口ページでも `phase stability / adaptation policy` を独立ログとして固定する必要がございました。

## 今回実行した変更

- `eeg_101.md`
  - `page_highlights` に、phase-targeted EEG loops では `low latency / mean phase error` だけでは足りず、`estimability / causal benchmark / downstream effect / phase stability` を分ける必要がある旨を追加しました。
  - `known_points` に、target-band power / SNR gate、no-stim rate、comparator、preferred-phase stability が別監査項目である旨を追加しました。
  - `Minimum QC` 節の closed-loop note を拡張し、phase-targeting では timing number だけでは読めないことを frontdoor で明示しました。
  - 新しい note-box `Phase-targeted EEG loops need four separate logs at the entry page` を追加し、entry-level で
    - estimability
    - targeting accuracy
    - downstream effect
    - phase stability
    の4ログを固定しました。
  - `four gates` table の deployability 行に、phase-locked control を主張する場合は phase-targeting logs を追加で求めるよう反映しました。
  - `generalization families` table の `longitudinal / closed loop` 行にも、phase-targeting logs を含めるよう反映しました。

## 今回止めた過読

- `low latency` = `phase-targeted EEG control の主要技術課題はほぼ解決`
- `small mean phase error` = `causal phase targeting が妥当`
- `phase locking` = `physiological / behavioral effect も確認済み`
- `preferred phase` = `cross-session で安定した固定 control point`

## 外部依存タスク

- なし
  - 今回の作業は repo 内文書、監査記録、生成物更新、検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Mansouri F, Fettes P, Schulze L, et al. A real-time phase-locking system for non-invasive brain stimulation. *Frontiers in Neuroscience*. 2018;12:877.
   - https://doi.org/10.3389/fnins.2018.00877
2. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
3. Zrenner C, Galevska D, Nieminen JO, Baur D, Stefanou MI, Ziemann U. The shaky ground truth of real-time phase estimation. *NeuroImage*. 2020;214:116761.
   - https://doi.org/10.1016/j.neuroimage.2020.116761
4. Gordon PC, Dörre S, Belardinelli P, Stenroos M, Zrenner B, Ziemann U, Zrenner C. Prefrontal Theta-Phase Synchronized Brain Stimulation With Real-Time EEG-Triggered TMS. *Frontiers in Human Neuroscience*. 2021;15:691821.
   - https://doi.org/10.3389/fnhum.2021.691821
5. Vigué-Guix I, Morís Fernández L, Torralba Cuello M, Ruzzoli M, Soto-Faraco S. Can the occipital alpha-phase speed up visual detection through a real-time EEG-based brain-computer interface (BCI)? *European Journal of Neuroscience*. 2022;55(11-12):3224-3240.
   - https://doi.org/10.1111/ejn.14931
6. Kim B, Erickson BA, Fernandez-Nunez G, Rich R, Mentzelopoulos G, Vitale F, Medaglia JD. EEG Phase Can Be Predicted with Similar Accuracy across Cognitive States after Accounting for Power and Signal-to-Noise Ratio. *eNeuro*. 2023;10(9):ENEURO.0050-23.2023.
   - https://doi.org/10.1523/ENEURO.0050-23.2023
7. Hougland JR, Kirchhoff M, Vetter DE, Ahola O, Jooß A, Humaidan D, Ziemann U. Fluctuations in the optimal sensorimotor mu-rhythm phase associated with high corticospinal excitability during TMS-EEG. *Brain Stimulation*. 2025;18(6):1843-1851.
   - https://doi.org/10.1016/j.brs.2025.09.019
