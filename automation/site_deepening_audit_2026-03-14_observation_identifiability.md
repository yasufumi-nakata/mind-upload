# Site Deepening Audit (2026-03-14, Observation / Estimation / Identifiability)

## 対象

- 主対象: `wiki/observation-to-estimation.md`
- 副対象: `tech_roadmap.md`
- 副対象: `wiki/measurement-and-modeling-terms.md`

## 今回の選定理由

- 2026-03-14 時点で、公開サイトの `閉ループ`、`因果摂動`、`multimodal integration`、`decode vs emulate` はかなり具体化されていました。
- その一方で、`観測から推定へ` 周辺は、概念整理としては正しいものの、`どこで主張が止まるか` と `何を追加すれば一段強く言えるか` が一次文献ベースの監査項目になっていませんでした。
- この弱さは局所ページに留まりません。`tech_roadmap.md` の R1 / R4 / R7 は、サイト全体の「どこまで言えるか」を定める基準点であり、ここが甘いと ESI、DCM、SCM、因果同値類の読み方が全ページで楽観化します。

## 主要な批判点

### 1. 旧 `R1` は「ベイズを標準解」と読める書き方で、監査項目より solver 名が先に出ていました

- 問題:
  - 旧 `tech_roadmap.md` の R1 は、逆問題が不良設定であること自体は正しく書いていました。
  - しかし結論が `ベイズ的アプローチを原則とする` で閉じており、読者に「solver family を決めれば問題がかなり解ける」という印象を与えうる構造でした。
- 根拠:
  - Wipf & Nagarajan (2009) は unified Bayesian framework を提示しましたが、これは Bayesian route の有力さを示すのであって、単独で一意復元を保証する研究ではありません。
  - Aydin et al. (2019) は、頭部組織導電率の不確かさが dipole reconstruction を大きく動かすことを示しました。
  - Unnwongse et al. (2023) と Hao et al. (2025) は、頭蓋内刺激や同時 SEEG を ground truth にした直接妥当化で、source depth、geometry、forward model、solver が誤差に強く効くことを示しています。
- 修正:
  - `ベイズを原則` を撤回し、`不確実性表現 + 幾何/導電率感度分析 + 外部妥当化` を受理条件として前面化しました。
  - Bayesian / empirical Bayes は「有力候補」へ位置づけ直しました。

### 2. 旧 `R4` は、Active Inference と multiscale simulation を既定路線のように読ませていました

- 問題:
  - 旧版は `Active Inference` と `Blue Brain Project 等のマルチスケール因果モデリング` を強い方針として前面に出していました。
  - しかし、2026-03 時点で一次文献が強く支えるのは、`観測適合だけでは因果は同定できない`、`候補モデル空間と介入データが必要`、`理論は競争させるべき` という点です。
- 根拠:
  - Friston et al. (2003) と Penny et al. (2004) は、DCM が候補モデル比較であることを明確にしています。
  - Hauser & Buhlmann (2012) は、介入データが Markov equivalence class を狭めることを示しました。
  - Vink et al. (2020) は、functional connectome が causal activity flow の弱い予測子に留まることを示しています。
  - Lee et al. (2017) は、麻酔で誘導された変化を使った DCM 妥当化を示しており、観測適合だけではなく intervention-like な条件差が重要であることを示します。
- 修正:
  - `Active Inference / DCM / SCM / state-space / mechanistic circuit` を競争させる候補集合として書き換えました。
  - `候補モデル空間の明示`、`family comparison`、`model recovery`、`held-out perturbation` を必須要件として固定しました。
  - multiscale route は `有力な拡張ルート` へ下げ、既定路線から外しました。

### 3. 旧 `wiki/observation-to-estimation.md` は、概念説明にとどまり、監査ゲートがありませんでした

- 問題:
  - 順問題、逆問題、ESI、DCM、SCM、因果同値類の定義はありましたが、どの条件がなければ主張が止まるかが表になっていませんでした。
  - その結果、`観測に合う` → `内部状態が分かった` → `因果が分かった` の段差が弱く読まれる余地がありました。
- 根拠:
  - Mikulan et al. (2020)、Unnwongse et al. (2023)、Hao et al. (2025) は、source imaging の強さが external validation route に依存することを示しています。
  - Feng et al. (2025) は empirical Bayesian uncertainty quantification を提示しましたが、これは `solver 名` ではなく `不確実性をどう出すか` が本体です。
  - Hauser & Buhlmann (2012) は、観測のみと介入ありで、得られる因果情報の強さが変わることを明示しています。
- 修正:
  - 新版では `4つの監査ゲート`（幾何、幅の可視化、候補モデル集合、外部妥当化/介入）へ全面再編しました。
  - `solver 名より監査`、`DCM は自動発見器ではない`、`SCM は介入の言語であり観測だけでは同値類が残る` という3本柱に置き換えました。

### 4. `measurement-and-modeling-terms.md` も、補助ページとしては十分でしたが、同値類と candidate set の話が抜けていました

- 問題:
  - 旧版は `観測→整理→推定→検証` の流れを理解するには有用でした。
  - しかし、`推定段階では候補モデル依存性がある`、`観測だけでは causal direction が残る` という補足がなく、`observation-to-estimation` と比べて一段弱い説明でした。
- 修正:
  - `推定は推定であり、不確実性と候補モデル依存性が残る` へ書き換えました。
  - `2026-03 の補足` として、DCM / SCM / 同値類の役割差を追加しました。

## 今回実行した変更

- `wiki/observation-to-estimation.md`
  - front matter を技術・自然科学中心に更新
  - `4つの監査ゲート`、`ESI の妥当化ラダー`、`DCM の候補モデル依存性`、`SCM と介入の役割`、`site rule`、`参考文献` を新設
- `tech_roadmap.md`
  - R1 の `ベイズ原則` を撤回し、`不確実性 + 感度分析 + 外部妥当化` へ変更
  - R4 を `特定理論の採用` から `model competition + intervention benchmark` へ変更
  - R7 に `family / sensitivity / calibration / abstention` を追加
  - 参考文献に source validation と causal identifiability 文献を追加
- `wiki/measurement-and-modeling-terms.md`
  - `候補モデル依存性` と `因果同値類` を補う最小限の同期修正を追加

## 外部依存で保留

- `perspective.md` と `tech_roadmap.md` に残る theory-heavy citation の site-wide 再監査
  - 担当者: AI / maintainer
  - 前提条件: 全ページの future-looking / theory-specific 引用を棚卸しすること
  - 完了条件: `既定路線` と読める理論依存記述が、公開一次文献の強さに合わせて整理されること

## 参考文献

- Wipf D, Nagarajan S. A unified Bayesian framework for MEG/EEG source imaging. NeuroImage. 2009.
  - https://doi.org/10.1016/j.neuroimage.2008.02.059
- Aydin U, Vorwerk J, Kupper P, et al. Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. Front Neurosci. 2019.
  - https://doi.org/10.3389/fnins.2019.00531
- Mikulan E, Russo S, Bares M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. Sci Data. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, Alhilani M, Asano E, et al. High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Feng Z, Mishne G, Hashemi A, et al. Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. IEEE Trans Med Imaging. 2025.
  - https://doi.org/10.1109/TMI.2025.3642620
- Friston KJ, Harrison L, Penny W. Dynamic causal modelling. NeuroImage. 2003.
  - https://doi.org/10.1016/S1053-8119(03)00202-7
- Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. NeuroImage. 2004.
  - https://doi.org/10.1016/j.neuroimage.2004.03.026
- Lee HL, Zahneisen B, Hugger T, et al. Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. NeuroImage. 2017.
  - https://doi.org/10.1016/j.neuroimage.2017.02.012
- Hauser A, Buhlmann P. Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. JMLR. 2012.
  - https://jmlr.org/papers/v13/hauser12a.html
- Vink JJ, Ramos-Nunez AI, Bellesi A, et al. The brain's functional connectome is a poor predictor of the brain's causal activity flow. PLoS Comput Biol. 2020.
  - https://doi.org/10.1371/journal.pcbi.1007866
