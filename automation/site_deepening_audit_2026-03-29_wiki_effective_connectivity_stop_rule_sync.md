# Site Deepening Audit (2026-03-29, wiki effective-connectivity stop-rule sync)

## 対象

- 主対象:
  - `wiki/mind-upload-basics.md`
  - `wiki/verification-basics.md`
  - `wiki/claims-and-evidence.md`
- 同期元として確認したページ:
  - `wiki/observation-to-estimation.md`
  - `verification.md`
  - `faq.md`
  - `index.md`
  - `perspective.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- 2026-03-29 時点で、front door 側と route-card 本体では effective-connectivity の停止条件がすでにかなり厳密化されておりました。
- 具体的には `index.md`、`faq.md`、`verification.md`、`perspective.md`、`wiki/observation-to-estimation.md` が、
  - `candidate model space`
  - `observed-subsystem closure / latent-confound audit`
  - `node-definition policy`
  - `sampling / transformation sensitivity`
  - `validation / reliability / abstention`
  を分けて要求する水準まで到達しておりました。
- しかし初学者向けの `wiki/mind-upload-basics.md`、`wiki/verification-basics.md`、`wiki/claims-and-evidence.md` には、なお
  - `candidate model space`
  - `recovery`
  - `validation`
  - `reliability`
  を中心とした旧来の要約が残っておりました。
- このズレを放置すると、入口を読み終えた読者が beginner wiki に移った段階で、再び
  - `DCM を回した`
  - `大きいモデル空間を比較した`
  - `reliability がそこそこ出た`
  を `causal wiring discovery` に近いものとして読み直してしまいます。

## web確認対象

- `https://pubmed.ncbi.nlm.nih.gov/20817103/`
- `https://pubmed.ncbi.nlm.nih.gov/27826091/`
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC7191224/`
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC6685009/`
- `https://arxiv.org/abs/2312.01833`
- `https://pubmed.ncbi.nlm.nih.gov/41605165/`

## 主要結論

- beginner wiki 側でも、effective-connectivity は `candidate model comparison` だけで説明してはいけません。
- 一次文献の現在地では、少なくとも
  - `observed-subsystem closure / latent-confound audit`
  - `node-definition policy`
  - `sampling / transformation sensitivity`
  - `validation / reliability window / abstention`
  を beginner 向け文面でも固定する必要がございます。
- したがって、今回の 3 ページは `effective connectivity = model-conditioned causal hypothesis` という site-wide rule に明示的に同期させるべきでございました。

## 根拠付き批判

### 1. 候補モデル比較だけでは、部分観測と latent confounder を止め切れません

- [Penny et al. (2004)](https://doi.org/10.1016/j.neuroimage.2004.03.026) は DCM 推論が比較した model structure に依存することを固定しました。
- [Rosa et al. (2012)](https://doi.org/10.1016/j.jneumeth.2012.04.013) は大きな candidate space を効率的に探索できることを示しました。
- しかし [Villaverde et al. (2019)](https://doi.org/10.1098/rsif.2019.0043) は、unknown inputs, states, and parameters を同時に含む full observability / estimation 問題を前景化しました。
- さらに [Yan et al. (2026)](https://doi.org/10.1109/TPAMI.2026.3658839) は、biological network reconstruction において latent/unobserved confounders がなお活発な method-development 問題であることを示しました。

批判:

- 旧 beginner wiki は `candidate model space` を書いていても、`observed subsystem が閉じていたか` と `latent confounder をどう監査したか` を独立条件として固定しておりませんでした。
- そのため、`比較した候補の中で勝った = 外側の hidden driver もかなり片付いた` と誤読しやすい状態でございました。

### 2. node / ROI 定義は実装細部ではなく、方向推定の一次条件でございます

- [Smith et al. (2011)](https://doi.org/10.1016/j.neuroimage.2010.08.063) は、rich realistic simulated fMRI benchmark により `lag-based approaches perform very poorly` とし、`functionally inaccurate ROIs` が network estimation に `extremely damaging` であることを示しました。

批判:

- 旧 beginner wording は、node set をほぼ暗黙の前提にしており、`その node をどう定義したか` を causal-claim stop rule として正面から扱っておりませんでした。
- atlas parcellation、task-functional ROI、intervention-targeted node は同じ inferential object ではございません。

### 3. sampling / observation-transform failure mode は、一般的な注意書きだけでは足りません

- [Barnett & Seth (2017)](https://doi.org/10.1016/j.jneumeth.2016.10.016) は、subsampling が detectability の `black spots` と `sweet spots` を作りうることを示しました。
- [Novelli et al. (2025)](https://doi.org/10.1002/hbm.70285) は、realistic HRF が minimum-phase である範囲が広い一方、`slow BOLD sampling` はなお `spurious GC` を生みうることを示しました。

批判:

- 旧 beginner wiki では `observation assumptions` や `priors` という抽象語で止まり、どこが HRF variability の問題で、どこが sampling aliasing / transform sensitivity の問題かが分離されておりませんでした。
- その結果、`hemodynamic caveat に一言触れた = temporal directionality の監査は済んだ` という危険な読みを止め切れておりませんでした。

### 4. resting-state FC は causal propagation の代用として弱すぎます

- [Vink et al. (2020)](https://doi.org/10.1007/s10548-020-00757-6) は、resting-state EEG functional connectivity が TMS-evoked propagation variance の `less than 10%` しか説明しないことを示しました。

批判:

- したがって、`resting connectivity`、`directed connectivity`、`causal circuit` を beginner 説明で滑らかにつなぐことは技術的に不正確でございます。
- route card には perturbation or external validation を残し、観測ベース graph と intervention propagation を分けて書く必要がございました。

### 5. reliability work は価値がありますが、その価値は限定条件つきで読むべきでございます

- [Jafarian et al. (2024)](https://doi.org/10.1002/hbm.26782) は、resting-state MEG DCM において 2 週間間隔でも、近い acquisition condition の下で高い再現性を示しました。

批判:

- これは `effective connectivity is solved` の根拠ではございません。
- むしろ、`reliability window` を明示すれば価値がある一方、それでも `unique causal wiring discovery` へは昇格しないと beginner ページで書く必要がございました。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `page_highlights` と `known_points` に effective-connectivity stop rule を追加しました。
  - `2026-03-29 technical correction` note-box を追加し、Smith 2011 / Barnett & Seth 2017 / Vink 2020 / Villaverde 2019 / Novelli 2025 / Jafarian 2024 / Yan 2026 に基づいて beginner 向け stop rule を明文化しました。
  - `Representative reasons, from current primary literature` を更新し、effective-connectivity を `candidate-model disclosure` だけで済ませない文面に修正しました。
  - 参考文献を追加しました。

- `wiki/verification-basics.md`
  - `last_updated` を `2026-03-29` に更新しました。
  - `page_highlights` / `known_points` に effective-connectivity route-card 要件を同期しました。
  - `2026-03-29 correction` note-box を追加しました。
  - claim-family table の effective-connectivity 行を、closure / node-definition / sampling を含む形へ更新しました。
  - `Representative primary-literature reasons` を更新し、verification beginner page でも同じ stop rule を保持するよう修正しました。
  - 参考文献を追加しました。

- `wiki/claims-and-evidence.md`
  - `last_updated` を `2026-03-29` に更新しました。
  - `page_highlights` の effective-connectivity bullet を site-wide rule に合わせて強化しました。
  - `2026-03-29 deepening` note-box を追加しました。
  - headline-reading table の `Found causal wiring / effective connectivity` 行を更新し、closure / node-definition / sampling を質問項目に加えました。
  - `Model-conditioned graphs are not discovered causal wiring` 節を全面改稿し、候補モデル比較だけでなく closure / confound / sampling / reliability-window まで要求する説明へ更新しました。
  - route-card table と参考文献を更新しました。

## 今回止めた誤読

- `candidate-model comparison をした = causal wiring discovery にかなり近い`
- `ROI / node choice は細部であり、main claim にはあまり効かない`
- `HRF caveat に一言触れた = sampling / transform failure mode は十分説明した`
- `resting-state FC と directed graph がある = intervention propagation にもかなり近い`
- `reliability が高い = unique causal circuit が見えた`
- `front door では厳密、beginner wiki では少し粗くてよい`

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、repo 内本文改稿、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
2. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
3. Smith SM, Miller KL, Salimi-Khorshidi G, et al. Network modelling methods for FMRI. *NeuroImage*. 2011.
   - https://doi.org/10.1016/j.neuroimage.2010.08.063
4. Barnett L, Seth AK. Detectability of Granger causality for subsampled continuous-time neurophysiological processes. *Journal of Neuroscience Methods*. 2017.
   - https://doi.org/10.1016/j.jneumeth.2016.10.016
5. Villaverde AF, Tsiantis N, Banga JR. Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. *Journal of the Royal Society Interface*. 2019.
   - https://doi.org/10.1098/rsif.2019.0043
6. Vink JJT, Klooster DCW, Ozdemir RA, Westover MB, Pascual-Leone A, Shafi MM. EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. *Brain Topography*. 2020.
   - https://doi.org/10.1007/s10548-020-00757-6
7. Jafarian A, Karadag Assem M, Kocagoncu E, et al. Reliability of dynamic causal modelling of resting-state magnetoencephalography. *Human Brain Mapping*. 2024.
   - https://doi.org/10.1002/hbm.26782
8. Novelli L, Barnett L, Seth AK, Razi A. Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. *Human Brain Mapping*. 2025.
   - https://doi.org/10.1002/hbm.70285
9. Yan J, Zhang S-W, Zhang C, Huang W, Shi J, Chen L. Dynamical Causality under Latent Confounders for Biological Network Reconstruction. *IEEE Transactions on Pattern Analysis and Machine Intelligence*. 2026.
   - https://doi.org/10.1109/TPAMI.2026.3658839
