# Site Deepening Audit (2026-03-29, effective-connectivity partial-observation / sampling audit)

## 対象

- 主対象: `wiki/observation-to-estimation.md`
- 同期対象:
  - `verification.md`
  - `tech_roadmap.md`
  - `wiki/measurement-and-modeling-terms.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1016/j.neuroimage.2010.08.063`
- `https://doi.org/10.1016/j.jneumeth.2016.10.016`
- `https://doi.org/10.1007/s10548-020-00757-6`
- `https://doi.org/10.1002/hbm.70285`
- `https://doi.org/10.1109/TPAMI.2026.3658839`
- `https://doi.org/10.1098/rsif.2019.0043`

## 今回この箇所を選んだ理由

- サイト全体はすでに `effective connectivity` を `candidate model space` 依存の主張としてかなり厳しく読ませる構造になっていました。
- しかし、その止め方にはまだ一段弱い点が残っていました。現行サイトの route card は
  - compared model space
  - observation assumptions
  - validation
  - reliability
  - abstention
  を要求していましたが、
  - `観測された部分系が本当に閉じているか`
  - `隠れノード / 共通入力 / latent confounder をどこまで監査したか`
  - `ROI / node 定義を変えると向き付きグラフがどこまで崩れるか`
  - `sampling / filtering / HRF 変換に対して方向推定がどこまで頑健か`
  を運用上の必須欄としてはまだ固定していませんでした。
- これは WBE 文脈では弱点でございます。理由は、WBE 周辺で議論したいのは単なる「予測可能な directed graph」ではなく、介入応答に耐える causal structure だからです。向き付きグラフ自体が部分観測と観測変換で壊れうるなら、candidate-model disclosure だけでは停止条件として不十分でございます。

## 根拠付き批判

### 1. `candidate model space` の開示だけでは、部分観測による擬似的な方向性を止め切れません

- [Villaverde et al. (2019)](https://doi.org/10.1098/rsif.2019.0043) は、unknown inputs, states, and parameters を同時に扱う必要を示しました。
- [Yan et al. (2026)](https://doi.org/10.1109/TPAMI.2026.3658839) は、生物ネットワーク再構成において latent confounders が依然として spurious causal interaction の主要因であり、その補正自体が現役の研究課題であることを示しました。

批判:

- 現行の route card では `omitted alternatives` は要求されていましたが、`unobserved part of the system` が作る交絡を独立した監査対象として固定していませんでした。
- そのままでは、読者が `candidate model set を出している = causal graph の外部妥当性も見ている` と誤読し得ます。
- 実際には、比較した候補集合の内部で勝ったことと、観測外ノードや共通入力に対して頑健であることは別問題でございます。

### 2. node / ROI 定義は implementation detail ではなく、方向推定を壊しうる一次条件です

- [Smith et al. (2011)](https://doi.org/10.1016/j.neuroimage.2010.08.063) は、豊富な simulated fMRI benchmark により、lag-based methods が poor であり、特に functionally inaccurate ROI が network estimation に極めて有害であることを示しました。

批判:

- 現行サイトは `node set` 自体は要求していましたが、`その node をどう定義したか` を独立欄としては固定していませんでした。
- しかし一次文献の水準では、atlas 由来の便宜的 parcellation と functionally grounded node definition は同じではありません。
- よって、`whole-brain directed graph` や `atlas-wide DCM` という見た目だけで causal wiring に近づいたように読ませないためには、node-definition policy を route card に切り出す必要がございました。

### 3. hemodynamic / temporal の弱点は一つの `HRF confound` ではなく、`observation transform` と `sampling` を分けて読む必要があります

- [Barnett & Seth (2017)](https://doi.org/10.1016/j.jneumeth.2016.10.016) は、continuous-time neurophysiological process を subsample すると Granger-causal detectability に black spot が生じうることを示しました。
- [Novelli et al. (2025)](https://doi.org/10.1002/hbm.70285) は、HRF が minimum-phase であれば HRF variability だけで直ちに false positive が必然化するわけではない一方、BOLD の slow sampling はなお spurious GC inference を導きうることを示しました。

批判:

- これまでの site wording だと、`neural / hemodynamic assumptions` は要求していても、sampling / filtering / transform sensitivity を独立の停止条件としては固定していませんでした。
- その結果、`HRF に注意` という一般論に吸収され、どこが HRF 依存で、どこが sampling aliasing 依存なのかが曖昧でございました。
- よって site rule は、`observation model` と `sampling / transformation sensitivity` を切り分ける必要がありました。

### 4. resting-state connectivity の整った図は causal propagation の強い証拠ではありません

- [Vink et al. (2020)](https://doi.org/10.1007/s10548-020-00757-6) は、EEG resting-state functional connectivity が TMS-evoked propagation variance の 10% 未満しか説明せず、刺激部位・被験者間で大きく変動することを示しました。

批判:

- したがって、resting-state FC, source-space FC, activity-flow-compatible diagram, dense effective-connectivity graph の間を滑らかにつなぐ書き方は依然として危険でございます。
- 現行サイトでも `model-conditioned hypothesis` とは書いていましたが、`supporting connectivity evidence` の弱さを directed-graph 読解に直接結びつける文言がまだ不足していました。

## 今回実行した変更

- `automation/site_deepening_audit_2026-03-29_effective_connectivity_partial_observation.md`
  - 本監査記録を追加しました。
- `wiki/observation-to-estimation.md`
  - `last_updated` を `2026-03-29` に更新しました。
  - `page_highlights` / `known_points` に、effective-connectivity の新しい停止条件として
    - observed-subsystem closure / latent-confound audit
    - node-definition policy
    - sampling / transformation sensitivity
    を追加しました。
  - `2026-03-29 deepening` note を追加し、Smith 2011, Barnett & Seth 2017, Vink 2020, Novelli 2025, Yan 2026 を使って、`directed graph` の過読停止条件を強化しました。
  - `effective-connectivity route card` に
    - observed subsystem / latent-confound audit
    - node-definition policy
    - sampling / transformation sensitivity
    の行を追加しました。
  - 参考文献を追加しました。
- `verification.md`
  - effective-connectivity の要約ルールを更新し、partial observation / node policy / sampling sensitivity を短い運用文として同期しました。
- `tech_roadmap.md`
  - front-matter と R4 の route-card 要件を更新し、roadmap 側でも同じ停止条件を要求するようにしました。
- `wiki/measurement-and-modeling-terms.md`
  - beginner route 側の DCM 説明にも同じ要件を同期しました。

## 今回止めた誤読

- `candidate model set を出した = directed graph の causal 妥当性もかなり見えている`
- `whole-brain / atlas-wide graph = node-definition に依らない causal object`
- `hemodynamic caveat に一言触れた = temporal-direction の監査は済んだ`
- `resting-state FC や source FC が整っている = intervention propagation の近似にも十分使える`
- `dense / scalable / predictive effective-connectivity estimate = discovered wiring`

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査記録、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Smith SM, Miller KL, Salimi-Khorshidi G, et al. Network modelling methods for FMRI. *NeuroImage*. 2011;54(2):875-891.
   - https://doi.org/10.1016/j.neuroimage.2010.08.063
2. Barnett L, Seth AK. Detectability of Granger causality for subsampled continuous-time neurophysiological processes. *Journal of Neuroscience Methods*. 2017;275:93-121.
   - https://doi.org/10.1016/j.jneumeth.2016.10.016
3. Vink JJT, Klooster DCW, Ozdemir RA, Westover MB, Pascual-Leone A, Shafi MM. EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. *Brain Topography*. 2020;33(2):221-237.
   - https://doi.org/10.1007/s10548-020-00757-6
4. Novelli L, Barnett L, Seth AK, Razi A. Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. *Human Brain Mapping*. 2025;46(10):e70285.
   - https://doi.org/10.1002/hbm.70285
5. Yan J, Zhang SW, Zhang C, Huang W, Shi J, Chen L. Dynamical Causality under Latent Confounders for Biological Network Reconstruction. *IEEE Transactions on Pattern Analysis and Machine Intelligence*. 2026.
   - https://doi.org/10.1109/TPAMI.2026.3658839
6. Villaverde AF, Tsiantis N, Banga JR. Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. *Journal of the Royal Society Interface*. 2019;16(156):20190043.
   - https://doi.org/10.1098/rsif.2019.0043
