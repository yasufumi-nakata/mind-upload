# Site Deepening Audit (2026-03-28, tech-roadmap phase-targeting front-door sync)

## 対象

- 主対象: `tech_roadmap.md`
- 派生同期: `summary_booklet.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1016/j.neuroimage.2020.116761`
- `https://doi.org/10.3389/fnhum.2021.691821`
- `https://doi.org/10.1523/ENEURO.0050-23.2023`
- `https://doi.org/10.1111/ejn.14931`
- `https://doi.org/10.1016/j.jneumeth.2021.109288`
- `https://doi.org/10.1523/JNEUROSCI.1913-18.2018`
- `https://doi.org/10.1016/j.brs.2025.09.019`

## 今回この箇所を選んだ理由

- `wiki/closed-loop-latency-jitter-and-safety-stops.md` と `verification.md` は、2026-03-28 時点で既に
  - `co-adaptation / credit assignment`
  - `phase-targeting estimability`
  - `functional effect versus targeting success`
  - `phase stability / adaptation policy`
  を明確に分けていました。
- しかし公開フロントドアである `tech_roadmap.md` の `M2` / `I1` は、なお
  - `phase-targeting では ms より phase error`
  という一段浅い整理に留まっていました。
- このままでは読者が
  - `phase error を出した`
  - `だから phase-targeting の主要技術負債はほぼ片付いた`
  と誤読しえます。
- Roadmap は入口ページですので、この圧縮を残すと、深層ページで止めた誤読を front door で再導入してしまいます。

## 根拠付き批判

### 1. 位相推定そのものが可観測条件に依存します

- [Zrenner et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116761) は、低 SNR と低振幅条件では non-causal benchmark 自体の精度も揺らぎ、causal estimator を強く読めないことを示しました。
- [Kim et al. (2023)](https://doi.org/10.1523/ENEURO.0050-23.2023) は、`11 public datasets`・`484 participants` で power と SNR が精度の主要因であり、特定の cognitive state を作るより high-power epoch を待つ方が重要だと示しました。

批判:

- したがって `phase error` を単独で置く設計は弱いです。
- front door でも `estimability gate` を独立項目として固定しなければ、band-pass 後の位相が自動的に意味を持つように見えてしまいます。

### 2. causal real-time estimate と post-hoc benchmark は同じではありません

- [Gordon et al. (2021)](https://doi.org/10.3389/fnhum.2021.691821) は、amplitude / stability constraints を入れた real-time prefrontal theta targeting と、gold-standard 的な post-hoc comparison を分離して評価しました。
- [Mansouri et al. (2018)](https://doi.org/10.3389/fnins.2018.00877) は real-time phase locking の proof-of-concept でしたが、効果一般を証明した論文ではありません。

批判:

- `phase-targeted` と書くだけでは、どの causal estimator をどの benchmark に対して読んでいるかが不明です。
- Roadmap のような入口ページこそ、`causal-versus-post-hoc benchmark` を明示すべきでした。

### 3. targeting success と functional effect は別です

- [Vigué-Guix et al. (2022)](https://doi.org/10.1111/ejn.14931) は、trial-to-trial alpha phase locking 自体は達成しつつ、reaction time への一貫した効果は group / individual の双方で支持されなかったと報告しました。

批判:

- `phase locking worked` を `phase-specific intervention worked` に繰り上げるのは誤りです。
- したがって front door では `targeting precision` と `downstream effect` を別箱にしなければなりません。

### 4. 位相精度の読み方も平均誤差だけでは足りません

- [Bruegger & Abegg (2021)](https://doi.org/10.1016/j.jneumeth.2021.109288) は mean phase offset, circular standard deviation, prediction latency を比較軸にしました。
- [Holt et al. (2019)](https://doi.org/10.1523/JNEUROSCI.1913-18.2018) は、patient-specific suppressing phase への consecutive stimulation と phase-bin width が effect size を変えることを示しました。

批判:

- `平均位相誤差` だけを front door に残すと、circular precision や phase policy の重要性が抜け落ちます。

### 5. 最適位相は固定ではありません

- [Hougland et al. (2025)](https://doi.org/10.1016/j.brs.2025.09.019) は、optimal mu phase が within-session に揺らぎ、inter-session test-retest reliability も低いことを示しました。

批判:

- `one preferred phase` を暗黙の default にしたままでは、fixed-phase policy と adaptive-phase policy の差が見えません。
- これは Roadmap の `I1` で止めるべき誤読でした。

## 今回実行した変更

- `tech_roadmap.md`
  - front matter の `page_highlights` と `known_points` に、phase-targeting を `estimability / benchmark / effect / stability` へ分解する site rule を追加しました。
  - `M2` の note-box を増補し、
    - oscillation estimability
    - causal-versus-post-hoc benchmark
    - downstream effect
    - phase stability / adaptation policy
    を front-door でも読めるよう改稿しました。
  - `M2` の bullet を、`phase error` 単独ではなく
    - target band / spatial filter
    - power / SNR gate
    - no-stim / phase-reset rejection
    - causal benchmark
    - circular spread
    - off-target comparator
    - fixed-versus-adaptive policy
    を要求する形へ更新しました。
  - `I1` の `Redefinition` と `Next` を更新し、phase-targeting の最小ログを `phase error` から multi-log stack へ引き上げました。
  - 参考文献に Zrenner 2020, Gordon 2021, Bruegger & Abegg 2021, Vigué-Guix 2022, Kim 2023, Holt 2019, Hougland 2025 を追加しました。

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成し、Roadmap front matter の更新を冊子へ反映しました。

## 今回止めた誤読

- `phase-targeting では ms より phase error` だけ読めば十分
- `phase error を出した = targeting burden の主要部分は解けた`
- `phase locking success = behavioral / physiological control success`
- `one preferred phase` を session 間でそのまま使える
- `phase-targeting` を一つの timing metric で比較できる

## 外部依存タスク

- なし
  - 今回の変更は公開本文、冊子再生成、監査記録、ローカル検証、commit、push まで repo 内で完結できます。

## 参考文献

1. Mansouri F, Fettes P, Schulze L, et al. A real-time phase-locking system for non-invasive brain stimulation. *Front Neurosci.* 2018.
   - https://doi.org/10.3389/fnins.2018.00877
2. Holt AB, Kormann E, Gulberti A, et al. Phase-Dependent Suppression of Beta Oscillations in Parkinson's Disease Patients. *J Neurosci.* 2019.
   - https://doi.org/10.1523/JNEUROSCI.1913-18.2018
3. Zrenner C, Galevska D, Nieminen JO, Baur D, Stefanou MI, Ziemann U. The shaky ground truth of real-time phase estimation. *NeuroImage.* 2020.
   - https://doi.org/10.1016/j.neuroimage.2020.116761
4. Gordon PC, Dörre S, Belardinelli P, Stenroos M, Zrenner B, Ziemann U, Zrenner C. Prefrontal Theta-Phase Synchronized Brain Stimulation With Real-Time EEG-Triggered TMS. *Front Hum Neurosci.* 2021.
   - https://doi.org/10.3389/fnhum.2021.691821
5. Bruegger D, Abegg M. Prediction of cortical theta oscillations in humans for phase-locked visual stimulation. *J Neurosci Methods.* 2021.
   - https://doi.org/10.1016/j.jneumeth.2021.109288
6. Vigué-Guix I, Morís Fernández L, Torralba Cuello M, Ruzzoli M, Soto-Faraco S. Can the occipital alpha-phase speed up visual detection through a real-time EEG-based brain-computer interface (BCI)? *Eur J Neurosci.* 2022.
   - https://doi.org/10.1111/ejn.14931
7. Kim B, Erickson BA, Fernandez-Nunez G, Rich R, Mentzelopoulos G, Vitale F, Medaglia JD. EEG Phase Can Be Predicted with Similar Accuracy across Cognitive States after Accounting for Power and Signal-to-Noise Ratio. *eNeuro.* 2023.
   - https://doi.org/10.1523/ENEURO.0050-23.2023
8. Hougland JR, Kirchhoff M, Vetter DE, Ahola O, Jooß A, Humaidan D, Ziemann U. Fluctuations in the optimal sensorimotor mu-rhythm phase associated with high corticospinal excitability during TMS-EEG. *Brain Stimul.* 2025.
   - https://doi.org/10.1016/j.brs.2025.09.019
