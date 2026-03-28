# Site Deepening Audit (2026-03-29, front door effective-connectivity stop rule)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
- 同期先として確認したページ:
  - `verification.md`
  - `tech_roadmap.md`
  - `wiki/observation-to-estimation.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## web確認対象

- `https://doi.org/10.1016/j.neuroimage.2004.03.026`
- `https://doi.org/10.1016/j.jneumeth.2012.04.013`
- `https://doi.org/10.1016/j.neuroimage.2010.08.063`
- `https://doi.org/10.1016/j.jneumeth.2016.10.016`
- `https://doi.org/10.1007/s10548-020-00757-6`
- `https://doi.org/10.1098/rsif.2019.0043`
- `https://doi.org/10.1002/hbm.23061`
- `https://doi.org/10.1016/j.neuroimage.2020.117491`
- `https://doi.org/10.1002/hbm.26782`
- `https://doi.org/10.1016/j.neuroimage.2024.120954`
- `https://doi.org/10.1002/hbm.70285`
- `https://doi.org/10.1109/TPAMI.2026.3658839`

## 今回この箇所を選んだ理由

- `wiki/observation-to-estimation.md`、`verification.md`、`tech_roadmap.md` では、2026-03-29 時点で effective-connectivity の停止条件がかなり厳密化されておりました。
- しかし front door 側、とくに `faq.md` の `Q1e` と `index.md` の入口ノートには、まだ一段粗い圧縮が残っておりました。
- 旧 front door は主として
  - `candidate model space`
  - `validation`
  - `reliability`
  を挙げておりましたが、
  - `観測された部分系が本当に閉じているか`
  - `latent confounder / common drive をどこまで監査したか`
  - `ROI / node をどう定義したか`
  - `sampling / observation transform が方向推定をどこまで壊しうるか`
  を短い入口文としてはまだ固定しておりませんでした。
- そのため、公開入口だけを読んだ読者が
  - `DCM を回した`
  - `whole-brain effective connectivity を出した`
  - `reliability を見た`
  を、実際より強い causal-wiring claim と誤読する余地が残っておりました。

## 主要結論

- `effective connectivity` の公開入口説明は、`candidate model comparison` だけでは不十分でございました。
- 一次文献の現在地では、少なくとも front door でも
  - `observed-subsystem closure / latent-confound audit`
  - `node-definition policy`
  - `sampling / transformation sensitivity`
  を明示しなければ、`directed graph = causal wiring` の誤読を止め切れません。
- したがって、このサイトの公開入口では、effective-connectivity を
  - `model-conditioned causal hypothesis`
  と明示し、
  - `candidate model space`
  - `observed-subsystem closure / latent-confound audit`
  - `node-definition policy`
  - `sampling / transformation sensitivity`
  - `perturbation / external validation`
  - `reliability window`
  - `abstention boundary`
  を要求する文面へ更新する必要がございました。

## 根拠付き批判

### 1. 候補モデル比較だけでは、部分観測の問題を止め切れません

- [Penny et al. (2004)](https://doi.org/10.1016/j.neuroimage.2004.03.026) は、DCM 推論が比較したモデル集合に依存することを固定しました。
- [Rosa et al. (2012)](https://doi.org/10.1016/j.jneumeth.2012.04.013) は、post-hoc search により大きい model space を効率的に探索できることを示しました。
- しかし [Villaverde et al. (2019)](https://doi.org/10.1098/rsif.2019.0043) は、unknown inputs, states, and parameters を同時に評価する observability / identifiability 問題を前景化しました。

批判:

- 旧 FAQ は `candidate model space` を要求していても、`observed subsystem が閉じていたか` を独立欄として要求しておりませんでした。
- そのままでは `比較した候補の中で勝った = 外部にある latent driver もかなり片付いた` と誤読し得ます。

### 2. node / ROI 定義は implementation detail ではなく、方向推定の一次条件です

- [Smith et al. (2011)](https://doi.org/10.1016/j.neuroimage.2010.08.063) は、rich realistic simulated fMRI benchmark で `lag-based approaches perform very poorly` と述べたうえで、`functionally inaccurate ROIs` が network estimation に `extremely damaging` であることを示しました。

批判:

- 旧 front door wording では、node set 自体は暗に前提化されていても、`その node をどう定義したか` を停止条件として可視化しておりませんでした。
- atlas 切り、task-functional ROI、intervention-targeted node は同じ inferential object ではございません。

### 3. temporal-direction の弱点は、HRF caveat 一言では足りません

- [Barnett & Seth (2017)](https://doi.org/10.1016/j.jneumeth.2016.10.016) は、subsampling が detectability の `black spots` と `sweet spots` を作りうることを示しました。
- [Novelli et al. (2025)](https://doi.org/10.1002/hbm.70285) は、realistic HRF が広い範囲で minimum-phase になりうるため `HRF variability` だけで false positives が必然になるわけではない一方、`slow sampling of the BOLD signal` はなお `spurious GC inferences` を生みうることを示しました。

批判:

- したがって、`HRF assumptions matter` という一般論だけでは、どこが hemodynamic transform 依存で、どこが sampling 依存かを分けて読めません。
- 入口ページでも `sampling / transformation sensitivity` を独立条件として書く必要がございました。

### 4. resting connectivity は、介入伝播の近似として弱すぎます

- [Vink et al. (2020)](https://doi.org/10.1007/s10548-020-00757-6) は、resting-state EEG functional connectivity が TMS-evoked propagation variance の `less than 10%` しか説明しないことを示しました。

批判:

- したがって、resting connectivity, directed connectivity, causal propagation を滑らかにつなぐ入口文は危険でございます。
- `graph が整っている` と `intervention propagation を近似できる` は別問題である、と入口で止める必要がございました。

### 5. latent confounder 問題は、なお現役の研究課題です

- [Yan et al. (2026)](https://doi.org/10.1109/TPAMI.2026.3658839) は、biological system における causal interaction inference が `spurious causal interactions` に脆弱であり、`latent/unobserved confounders` 下での推定には依然として有効法が不足していると述べています。

批判:

- したがって、front door が `effective connectivity = promising causal map` 風に読める余地を残すのは不正確でございます。
- 入口説明でも `latent-confound audit` を必須欄として前面に出す必要がございました。

### 6. それでも reliability work は価値があり、その価値は限定条件つきで読むべきです

- [Frässle et al. (2016)](https://doi.org/10.1002/hbm.23061) は、face perception network の DCM で `negative free energy` の excellent reliability と、十分な effect-size 条件下での good parameter reliability を報告しました。
- [Jafarian et al. (2024)](https://doi.org/10.1002/hbm.26782) は、resting-state MEG DCM において 2 週間間隔データで reproducibility / reliability を評価しました。

批判:

- これは `DCM is worthless` という意味ではございません。
- むしろ、限定条件を明示すれば再現性は議論できる一方、それでも `unique causal wiring` には昇格しない、と入口文で整理する必要がございました。

## 今回実行した変更

- `faq.md`
  - `last_updated` を `2026-03-29` に更新しました。
  - front matter の `page_highlights` と `known_points` を更新し、effective-connectivity の入口 stop rule を
    - observed-subsystem closure / latent-confound audit
    - node-definition policy
    - sampling / transformation sensitivity
    を含む形に強化しました。
  - `Q1e` を改稿し、`candidate model space` だけでなく、上記 3 条件と perturbation / external validation を必須として明文化しました。
  - `Smith 2011`, `Barnett & Seth 2017`, `Vink 2020`, `Novelli 2025`, `Yan 2026`, `Villaverde 2019` を短答の中へ取り込みました。

- `index.md`
  - front matter の `page_highlights` / `known_points` に、DCM / effective-connectivity の新しい front-door stop rule を追加しました。
  - note box `If A Directed Graph Sounds Like Discovered Causal Wiring` を新設し、index だけ読んだ段階でも `DCM = discovered causal wiring` へ滑らないよう修正しました。

## 今回止めた誤読

- `candidate-model competition をした = causal wiring discovery にかなり近い`
- `whole-brain / faster DCM = identifiability もだいたい改善した`
- `ROI / node choice は実装細部であり、主張強度にはあまり効かない`
- `HRF caveat に一言触れた = temporal directionality の監査は済んだ`
- `resting-state FC が整っている = intervention propagation の近似に十分使える`
- `reliability が出た = unique causal circuit がかなり見えている`

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、repo 内公開ページ改稿、監査メモ作成、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004;22(3):1157-1172.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
2. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012;208(1):66-78.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
3. Smith SM, Miller KL, Salimi-Khorshidi G, et al. Network modelling methods for FMRI. *NeuroImage*. 2011;54(2):875-891.
   - https://doi.org/10.1016/j.neuroimage.2010.08.063
4. Barnett L, Seth AK. Detectability of Granger causality for subsampled continuous-time neurophysiological processes. *Journal of Neuroscience Methods*. 2017;275:93-121.
   - https://doi.org/10.1016/j.jneumeth.2016.10.016
5. Vink JJT, Klooster DCW, Ozdemir RA, Westover MB, Pascual-Leone A, Shafi MM. EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. *Brain Topography*. 2020;33(2):221-237.
   - https://doi.org/10.1007/s10548-020-00757-6
6. Villaverde AF, Tsiantis N, Banga JR. Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. *Journal of the Royal Society Interface*. 2019;16(156):20190043.
   - https://doi.org/10.1098/rsif.2019.0043
7. Frässle S, Harrison SJ, Heinzle J, et al. Test-retest reliability of effective connectivity in the face perception network. *Human Brain Mapping*. 2016;37(2):730-744.
   - https://doi.org/10.1002/hbm.23061
8. Frässle S, Manjaly ZM, Do CT, Kasper L, Pruessmann KP, Stephan KE. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021;225:117491.
   - https://doi.org/10.1016/j.neuroimage.2020.117491
9. Jafarian A, Karadag Assem M, Kocagoncu E, et al. Reliability of dynamic causal modelling of resting-state magnetoencephalography. *Human Brain Mapping*. 2024;45(10):e26782.
   - https://doi.org/10.1002/hbm.26782
10. Wu G, Han D, Wang H, et al. Improved regression dynamic causal modeling for whole-brain effective connectivity. *NeuroImage*. 2024;296:120954.
   - https://doi.org/10.1016/j.neuroimage.2024.120954
11. Novelli L, Barnett L, Seth AK, Razi A. Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. *Human Brain Mapping*. 2025;46(10):e70285.
   - https://doi.org/10.1002/hbm.70285
12. Yan J, Zhang S-W, Zhang C, Huang W, Shi J, Chen L. Dynamical Causality under Latent Confounders for Biological Network Reconstruction. *IEEE Transactions on Pattern Analysis and Machine Intelligence*. 2026.
   - https://doi.org/10.1109/TPAMI.2026.3658839
