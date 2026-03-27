# Site Deepening Audit (2026-03-28, phase-targeting estimability / effect / stability split)

## 対象

- 主対象: `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- 同期対象:
  - `github-wiki-export/closed-loop-latency-jitter-and-safety-stops.md`
  - `verification.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.3389/fnins.2018.00877`
- `https://doi.org/10.1016/j.brs.2017.11.016`
- `https://doi.org/10.1523/JNEUROSCI.1913-18.2018`
- `https://doi.org/10.1016/j.neuroimage.2020.116761`
- `https://doi.org/10.3389/fnhum.2021.691821`
- `https://doi.org/10.1016/j.jneumeth.2021.109288`
- `https://doi.org/10.1111/ejn.14931`
- `https://doi.org/10.1523/ENEURO.0050-23.2023`
- `https://doi.org/10.1016/j.brs.2025.09.019`

## 今回この箇所を選んだ理由

- `closed-loop` ページはすでに
  - latency / jitter
  - body/environment boundary
  - co-adaptation / credit assignment
  - fixed-decoder durability
  - rescue burden
  をかなり厳密に切り分けていました。
- しかし `phase-locked stimulation` だけは、なお
  - `phase error を出した`
  - `missed trigger を出した`
  というログで主要な技術負債が片付くように読める余地が残っていました。
- これは現在の一次文献の水準とずれています。位相同期刺激の失敗要因は、もはや単なる遅延ではなく、
  - その時点で対象振動が本当に推定可能だったか
  - causal estimator が post-hoc benchmark と整合していたか
  - 位相合わせに成功したことと downstream effect が切り分けられているか
  - 最適位相が session 内外で安定だったか
  を別々に見なければなりません。

## 根拠付き批判

### 1. `band-pass した位相` は、そのままでは意味を持ちません

- [Zrenner et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116761) は、phase estimation error が対象振動の instantaneous amplitude と SNR に強く依存し、低 SNR 条件では「ground truth phase」自体の精度が揺らぐことを示しました。
- [Kim et al. (2023)](https://doi.org/10.1523/ENEURO.0050-23.2023) は 11 公開データセット・484 参加者を用いて、power と SNR をそろえると cognitive state 間の位相予測精度差は小さくなり、むしろ高 power / 高 SNR epoch を待つ方が重要だと示しました。

批判:

- したがって `phase-targeted loop` を読む入口で、対象振動の `estimability gate` を固定しないのは弱いです。
- `8-12 Hz を見た` だけでは足りず、少なくとも `spectral peak / power / SNR / no-stim rate` を出すべきでした。

### 2. causal targeting と post-hoc phase は別物であり、benchmark が必要です

- [Mansouri et al. (2018)](https://doi.org/10.3389/fnins.2018.00877) と [Zrenner et al. (2018)](https://doi.org/10.1016/j.brs.2017.11.016) は real-time phase-targeting の実装可能性を示しました。
- しかし [Zrenner et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116761) は、刺激時点の standard instantaneous phase は刺激アーチファクトで future signal を失うため、causal estimator は non-causal estimator への近似として benchmark されるべきだと明示しました。
- [Gordon et al. (2021)](https://doi.org/10.3389/fnhum.2021.691821) は prefrontal theta で、実刺激を含まない matched epochs を用いて post-hoc gold-standard comparator を作り、low-amplitude / phase-reset epoch を除くことで精度が上がることを示しました。

批判:

- `phase error distribution` だけを載せても、その誤差が何に対する誤差かを固定しなければ技術的意味が弱いです。
- よって、このページは `causal estimator family` と `post-hoc benchmark procedure` を分離して要求すべきでした。

### 3. phase-locking に成功しても、機能効果は別問題です

- [Vigué-Guix et al. (2022)](https://doi.org/10.1111/ejn.14931) は real-time EEG-based BCI で occipital alpha への reliable trial-to-trial phase locking を達成しました。
- それにもかかわらず、reaction time の一貫した phase dependence は group でも individual でも確認できませんでした。

批判:

- したがって `phase locking worked` を `behavioral/physiological control worked` に繰り上げて読むのは誤りです。
- この区別をサイトルールにしないと、`位相合わせ成功 = phase-specific intervention success` という誤読を再注入します。

### 4. phase precision 自体が effect size を変えます

- [Bruegger & Abegg (2021)](https://doi.org/10.1016/j.jneumeth.2021.109288) は mean phase offset, circular standard deviation, prediction latency を比較軸として phase-locked visual stimulation 法を評価しました。
- [Holt et al. (2019)](https://doi.org/10.1523/JNEUROSCI.1913-18.2018) は Parkinson 症例の beta phase-dependent stimulation で、phase bin を狭くすると modulation が強まり、連続して suppressing phase に入る pulse 数が効果を左右することを示しました。

批判:

- よって `平均位相誤差` だけでは足りません。
- `circular spread`、`phase-bin width`、`consecutive-cycle policy` を出さなければ、phase-targeting の強さを比較できません。

### 5. 最適位相は固定ではなく、session 内外で揺れます

- [Hougland et al. (2025)](https://doi.org/10.1016/j.brs.2025.09.019) は、high corticospinal excitability に対応する sensorimotor mu phase が within-session に揺らぎ、inter-session では low test-retest reliability を示すことを報告しました。

批判:

- したがって `one fixed preferred phase` を自然な default として読むのは危険です。
- `fixed-phase result` と `adaptive-phase result` を分けない限り、同じ success label でも意味が変わってしまいます。

## 今回実行した変更

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - front matter の `accuracy_note` / `page_highlights` / `known_points` / `unknown_points` に phase-targeting の制約を追加しました。
  - `2026-03-28 second re-audit: phase-targeting needs an estimability wall` を追加しました。
  - `phase-locked stimulation` 行を、latency だけでなく
    - target band / spatial filter
    - power/SNR gate
    - causal-versus-post-hoc benchmark
    - circular precision
    - fixed-versus-adaptive phase policy
    を要求する内容へ改稿しました。
  - 新セクション `Phase-targeting is estimability-limited, not latency-limited` を追加し、
    - oscillation gate / estimability
    - causal estimator benchmark
    - targeting precision
    - functional effect versus targeting success
    - phase stability and adaptation policy
    を別々の監査層として固定しました。
  - minimum log の phase 系項目を分割し、burst 系ログと混ぜない形にしました。
  - 読解質問を `12` から `14` に更新し、phase-targeting 特有の 2 問を追加しました。
  - 参考文献を追加しました。

- `github-wiki-export/closed-loop-latency-jitter-and-safety-stops.md`
  - GitHub Wiki 側へ同じ phase-targeting rule を同期しました。

- `verification.md`
  - `Additional audit logs` に `Phase-Targeting Log` を追加しました。
  - これにより、phase-triggered observation / stimulation を generic `Perturbation log` の下位に埋めず、独立ログとして扱う site-wide rule を明文化しました。

## 今回止めた誤読

- `phase error を出した = phase-targeting の主要技術負債は解けた`
- `band-pass した位相 = その epoch の意味ある target phase`
- `trial-to-trial phase locking 成功 = behavior / physiology も phase specific に変わった`
- `one preferred phase` を、そのまま session 横断で使える
- `phase/burst systems` を 1 つの補助指標欄で足りる

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査メモ、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Mansouri F, Fettes P, Schulze L, et al. A Real-Time Phase-Locking System for Non-invasive Brain Stimulation. *Front Neurosci.* 2018;12:877.
   - https://doi.org/10.3389/fnins.2018.00877
2. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimul.* 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
3. Holt AB, Kormann E, Gulberti A, et al. Phase-Dependent Suppression of Beta Oscillations in Parkinson's Disease Patients. *J Neurosci.* 2019;39(6):1119-1134.
   - https://doi.org/10.1523/JNEUROSCI.1913-18.2018
4. Zrenner C, Galevska D, Nieminen JO, Baur D, Stefanou MI, Ziemann U. The shaky ground truth of real-time phase estimation. *Neuroimage.* 2020;214:116761.
   - https://doi.org/10.1016/j.neuroimage.2020.116761
5. Gordon PC, Dörre S, Belardinelli P, Stenroos M, Zrenner B, Ziemann U, Zrenner C. Prefrontal Theta-Phase Synchronized Brain Stimulation With Real-Time EEG-Triggered TMS. *Front Hum Neurosci.* 2021;15:691821.
   - https://doi.org/10.3389/fnhum.2021.691821
6. Bruegger D, Abegg M. Prediction of cortical theta oscillations in humans for phase-locked visual stimulation. *J Neurosci Methods.* 2021;361:109288.
   - https://doi.org/10.1016/j.jneumeth.2021.109288
7. Vigué-Guix I, Morís Fernández L, Torralba Cuello M, Ruzzoli M, Soto-Faraco S. Can the occipital alpha-phase speed up visual detection through a real-time EEG-based brain-computer interface (BCI)? *Eur J Neurosci.* 2022;55(11-12):3224-3240.
   - https://doi.org/10.1111/ejn.14931
8. Kim B, Erickson BA, Fernandez-Nunez G, Rich R, Mentzelopoulos G, Vitale F, Medaglia JD. EEG Phase Can Be Predicted with Similar Accuracy across Cognitive States after Accounting for Power and Signal-to-Noise Ratio. *eNeuro.* 2023;10(9):ENEURO.0050-23.2023.
   - https://doi.org/10.1523/ENEURO.0050-23.2023
9. Hougland JR, Kirchhoff M, Vetter DE, Ahola O, Jooß A, Humaidan D, Ziemann U. Fluctuations in the optimal sensorimotor mu-rhythm phase associated with high corticospinal excitability during TMS-EEG. *Brain Stimul.* 2025;18(6):1843-1851.
   - https://doi.org/10.1016/j.brs.2025.09.019
