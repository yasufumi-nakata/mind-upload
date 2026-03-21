# Site Deepening Audit (2026-03-21, Astrocyte Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 運用ルール反映: `verification.md`
- 入口反映: `wbe_101.md`, `index.md`

## 今回の選定理由

- 2026-03-21 時点で、サイトはすでに `astrocyte / glial-state` を generic support background から切り離していました。
- その一方で、myelin / bioenergetic / clearance と違って、`astrocyte evidence` 自体を分解する route card はまだありませんでした。
- このため、技術・自然科学の観点で読者が少なくとも以下を一つの証拠クラスに圧縮しやすい状態でした。
  - lactate-shuttle support
  - minute-scale cortical astrocyte-network encoding
  - learning-associated hippocampal recall ensemble
  - multiday stabilization ensemble
  - amygdala fear-state representation
  - human MAO-B / reactive-astrogliosis PET

## 根拠付き批判

### 1. 代謝支援と ensemble readout は同じ claim family ではありません

- 問題:
  - 既存サイトは astrocytes が重要だと示していましたが、`何が直接観測されたのか` の欄がなく、metabolic support と ensemble-level memory state が同じラベルに落ちやすい状態でした。
- 根拠:
  - Suzuki et al. (2011) は astrocyte-neuron lactate transport を long-term memory formation の条件として示しました。
  - Cahill et al. (2024) は local neurotransmitter input が minutes-scale の cortical astrocyte network state に写ることを示しました。
- 批判:
  - したがって `astrocytes matter` だけでは粗すぎます。lactate-shuttle support と cortical network encoding は別の inferential object です。

### 2. Recall, multiday stabilization, fear-state representation も同じ object ではありません

- 問題:
  - front door では astrocyte-state の重要性を前面化できていましたが、recall / stabilization / fear-state representation を submission rule 上で分ける欄がありませんでした。
- 根拠:
  - Williamson et al. (2025) は learning-associated astrocyte ensembles と recall を結びました。
  - Dewa et al. (2025) は emotional memory の multiday stabilization を示しました。
  - Bukalo et al. (2026) は basolateral amygdala astrocyte Ca2+ signalling が fear-memory representations を支えることを示しました。
- 批判:
  - したがって `rodent astrocyte causal evidence exists` を一文で済ませると、対象行動・回路・時間幅の差が消えます。

### 3. Human astrocyte PET は human astrocyte-ensemble readout ではありません

- 問題:
  - 既存サイトは human observability ceiling を丁寧に整理していましたが、astrocyte 側の human proxy class がまだ明示されていませんでした。
- 根拠:
  - Villemagne et al. (2022) は `18F-SMBT-1` を MAO-B selective reactive-astrogliosis PET tracer として first-in-human characterization しました。
- 批判:
  - これは `human astrocyte-related proxy exists` を支持しますが、learning-associated ensemble, recall-state astrocyte, arbitrary memory content, whole-brain astrocyte-state identity の ground truth ではありません。

### 4. Verification 側に route card がなければ実務上は抜けます

- 問題:
  - hidden-state の本文だけで astrocyte を独立扱いしても、`verification.md` 側に mandatory fields がなければ投稿物審査では generic glial sentence に戻りえます。
- 批判:
  - `state variable` と `submission rule` が一致していない状態は site operation 上の弱点です。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights`, `known_points`, `unknown_points` を astrocyte route-card 方針に同期しました。
  - astrocyte section に `How this site reads current human astrocyte evidence` note を追加し、`18F-SMBT-1 / MAO-B / reactive-astrogliosis PET` を human astrocyte-related proxy として位置づけました。
  - `#astrocyte-route-card` を新設し、以下の field を固定しました。
    - claim family
    - biological regime
    - direct astrocyte observable
    - driver / perturbation route
    - functional target
    - human proxy class / tracer burden
    - abstention boundary
  - human observability table に `human astrocyte PET / reactive-astrogliosis proxy` row を追加しました。
- `verification.md`
  - `page_highlights` に astrocyte route-card rule を追加しました。
  - maintenance-state error budget の `Glial / astrocyte support` 行を route-card 粒度へ更新しました。
  - `astrocyte evidence also needs a route card` addendum を追加しました。
- `wbe_101.md`
  - `page_highlights` を astrocyte evidence is not one class に同期しました。
  - entry-level note を `astrocyte evidence now gets its own route card` に更新しました。
- `index.md`
  - landing-page highlight を astrocyte evidence is not one class に更新しました。
  - astrocyte note を route-card への導線つきで更新しました。

## 外部依存で保留

- same-subject human astrocyte-state benchmark
  - 担当者: external human neuroimaging / glia-measurement researchers
  - 前提条件: human astrocyte-related proxy, perturbation, and external biological calibration を同一被験者で比較できる公開設計
  - 完了条件: human astrocyte PET or other proxy がどの maintenance-state uncertainty term をどこまで減らすかを比較できる benchmark が公開されること

## 参考文献

1. Suzuki A, Stern SA, Bozdagi O, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011;144(5):810-823.
   - https://doi.org/10.1016/j.cell.2011.02.018
2. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263254
3. Cahill MK, Berrios J, Schaid MD, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024;629:146-153.
   - https://doi.org/10.1038/s41586-024-07311-5
4. Williamson NR, Ferreira AN, Watanabe AT, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025;636:445-454.
   - https://doi.org/10.1038/s41586-024-08170-w
5. Dewa K, Kwon O-B, Zheng X, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025;648:99-107.
   - https://doi.org/10.1038/s41586-025-09619-2
6. Bukalo O, Vainchtein ID, Forli A, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
