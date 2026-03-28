# Site Deepening Audit (2026-03-29, perspective / causal-model boundary and effective-connectivity stop rule)

## 対象

- 主対象: `perspective.md`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `perspective.md` は公開サイトの中でも「立場表明」として最も広く読まれやすいページです。
- ただし 2026-03-29 時点でも、因果モデリング節には一段弱い点が残っていました。既に `wiki/observation-to-estimation.md`、`verification.md`、`tech_roadmap.md` では、
  - observed-subsystem closure / latent-confound audit
  - node-definition policy
  - sampling / transformation sensitivity
  を effective-connectivity の必須停止条件として固定していましたが、`perspective.md` 側はなお
  - `candidate model comparison`
  - `perturbation`
  - `abstention`
  の抽象度で止まっており、 directed graph が実際より強く読まれる余地がありました。
- これは技術的に重大でございます。WBE 文脈で必要なのは、きれいな directed graph ではなく、介入に耐える causal structure だからです。部分観測と観測変換で壊れうる graph を、そのまま「因果の発見」に寄せて読ませるのは不正確です。

## web確認対象

- `https://doi.org/10.1016/j.neuroimage.2010.08.063`
- `https://doi.org/10.1016/j.jneumeth.2016.10.016`
- `https://doi.org/10.1007/s10548-020-00757-6`
- `https://doi.org/10.1002/hbm.70285`
- `https://doi.org/10.1098/rsif.2019.0043`
- `https://doi.org/10.1109/TPAMI.2026.3658839`

## 根拠付き批判

### 1. 候補モデル比較だけでは、部分観測と latent confounder を止め切れません

- [Villaverde et al. (2019)](https://doi.org/10.1098/rsif.2019.0043) は、unknown inputs, states, and parameters をしばしば同時に扱う必要を示しました。
- [Yan et al. (2026)](https://doi.org/10.1109/TPAMI.2026.3658839) は、生物ネットワーク再構成において latent confounders が spurious causal interaction の主要因であり続けることを示しました。

批判:

- 旧 `perspective.md` では `DCM is a candidate in model competition` とは書いてありましたが、`観測された部分系が本当に閉じているか` を独立欄として要求していませんでした。
- そのままでは、読者が `candidate-model competition をした = causal graph の妥当性もかなり見た` と誤読し得ます。

### 2. node / ROI 定義は implementation detail ではなく、方向推定の一次条件です

- [Smith et al. (2011)](https://doi.org/10.1016/j.neuroimage.2010.08.063) は、大規模 simulation benchmark により、lag-based approaches が poor であり、functionally inaccurate ROIs が network estimation に極めて有害であることを示しました。

批判:

- 旧版は `use DCM and compare models` と書いていましたが、`その node をどう定義したか` を route-card 的に固定していませんでした。
- atlas で切った node, functionally grounded node, intervention-targeted node は同じ inferential object ではございません。

### 3. hemodynamic caveat を一言書くだけでは、sampling / transform failure mode は止まりません

- [Barnett & Seth (2017)](https://doi.org/10.1016/j.jneumeth.2016.10.016) は、subsampling によって Granger-causal detectability に black spots が生じうることを示しました。
- [Novelli et al. (2025)](https://doi.org/10.1002/hbm.70285) は、HRF variability だけで必ず false positive が出るわけではない一方、slow BOLD sampling はなお spurious GC inference を招きうることを示しました。

批判:

- `HRF assumptions matter` という一般論だけでは、どこが HRF 依存で、どこが sampling aliasing / transform sensitivity 依存なのかが曖昧です。
- よって site 側は `observation model` と `sampling / transformation sensitivity` を切り分けて要求する必要がありました。

### 4. resting-state connectivity は、因果伝播の代用には弱すぎます

- [Vink et al. (2020)](https://doi.org/10.1007/s10548-020-00757-6) は、resting-state EEG functional connectivity が TMS-evoked propagation variance の 10% 未満しか説明しないことを示しました。

批判:

- `resting connectivity`, `effective connectivity`, `causal structure` を滑らかにつなぐ書き方は、この水準の一次文献とは整合しません。
- directed graph の可視化は情報価値がありますが、そのまま intervention propagation の近似として読むのは過大解釈です。

## 今回実行した変更

- `perspective.md`
  - `last_updated` を `2026-03-29` に更新しました。
  - front matter の `page_highlights` / `known_points` / `wiki_links` に effective-connectivity の新しい停止条件を同期しました。
  - `Decoding: Introducing active inference and counterfactual virtual equivalence` 節に 2026-03-29 addendum を追加し、Smith 2011 / Barnett & Seth 2017 / Vink 2020 / Novelli 2025 / Yan 2026 に基づく stop-rule を明記しました。
  - `Demonstration plan` の最小要件に `node-definition / parcellation policy`、`observed-subsystem closure`、`latent confounder audit` を追加しました。
  - 5-wall table の `Wall of identity` を技術的に正しい `Wall of identifiability` に修正しました。
  - 同 table の identifiability 行を、`family comparison` だけでなく `observed-subsystem closure / latent-confound audit`、`node-definition policy`、`sampling / transformation sensitivity` を要求する形に更新しました。
  - `scalable directed graphs still need an audit trail` note-box を追加しました。
  - 参考文献 [141]-[146] を追加しました。

## 今回止めた誤読

- `whole-brain DCM = discovered causal wiring`
- `candidate-model competition をした = latent confounder 問題もかなり片付いた`
- `HRF に注意した = temporal directionality の監査は済んだ`
- `resting-state connectivity が整っている = intervention propagation の近似にも使える`
- `denser / scalable graph = identifiability が改善した`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開文書改稿、監査メモ、検証、commit、push までこのセッションで完結可能です。

## 参考文献

1. Smith SM, Miller KL, Salimi-Khorshidi G, et al. (2011). Network modelling methods for FMRI. *NeuroImage*, 54(2), 875-891.
   - https://doi.org/10.1016/j.neuroimage.2010.08.063
2. Barnett L, Seth AK. (2017). Detectability of Granger causality for subsampled continuous-time neurophysiological processes. *Journal of Neuroscience Methods*, 275, 93-121.
   - https://doi.org/10.1016/j.jneumeth.2016.10.016
3. Vink JJT, Klooster DCW, Ozdemir RA, Westover MB, Pascual-Leone A, Shafi MM. (2020). EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. *Brain Topography*, 33(2), 221-237.
   - https://doi.org/10.1007/s10548-020-00757-6
4. Novelli L, Barnett L, Seth AK, Razi A. (2025). Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. *Human Brain Mapping*, 46(10), e70285.
   - https://doi.org/10.1002/hbm.70285
5. Villaverde AF, Tsiantis N, Banga JR. (2019). Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. *Journal of the Royal Society Interface*, 16(156), 20190043.
   - https://doi.org/10.1098/rsif.2019.0043
6. Yan J, Zhang S-W, Zhang C, Huang W, Shi J, Chen L. (2026). Dynamical Causality under Latent Confounders for Biological Network Reconstruction. *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
   - https://doi.org/10.1109/TPAMI.2026.3658839
