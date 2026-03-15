# Site Deepening Audit (2026-03-15, Extracellular Recording / Unit Identity Ceiling)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `wiki/state-trait-and-drift.md`
- 関連公開ページ: `tech_roadmap.md`, `verification.md`

## 今回の選定理由

- 2026-03-15 時点の公開サイトは、EEG / fMRI / atlas / connectomics / glia imaging の claim ceiling をかなり整理できていましたが、`high-density extracellular probe` を独立した measurement stack として前面化できていませんでした。
- その結果、Neuropixels や Utah array の前進を、`local population readout` ではなく `stable single-unit ground truth` に近く誤読する余地が残っていました。
- これは技術・自然科学の観点で弱点です。なぜなら、侵襲記録は確かに強い local readout を与えますが、慢性縦断では `same neuron across days` 自体が sorting / drift correction / unit matching / tissue response の監査対象であり、観測事実として自動では与えられないからです。

## 主要な批判点

### 1. 旧 measurement-stack 整理は extracellular probe を ECoG / SEEG や一般的な侵襲記録の影に置きすぎていました

- 問題:
  - ECoG / SEEG と extracellular spiking は、直接観測量も latent state も違います。
  - 前者は局所 field potential と刺激応答、後者は implant 近傍の spike waveform / threshold crossing / multiunit を与えます。
  - これを同列に扱うと、sorted spike train を stable neuron identity と読み替えやすくなります。
- 根拠:
  - Steinmetz et al. (2021) は Neuropixels 2.0 により stable long-term recordings を前進させましたが、motion stabilization を前提にしています。
  - Pachitariu et al. (2024) は Kilosort4 を drift、low-norm units、split / merge benchmark を中心に更新しました。
  - van Beest et al. (2024) は cross-day matching を probabilistic unit identification として扱いました。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` に `high-density extracellular probe` 行を新設しました。
  - claim ceiling を `implant-region の local population window と stated validity horizon まで` に固定しました。

### 2. 旧 state/trait/drift 整理は unit-level drift と sorting / matching 不確実性の切り分けが弱かった

- 問題:
  - 既存ページは biological drift と decoder drift を分けていましたが、慢性 invasive 記録に特有の `probe drift`、`unit matching error`、`tissue response` を独立監査項目としては固定していませんでした。
  - このままでは `single-unit instability` をすべて生体由来の representational drift と誤解するか、逆に `same neuron` を過信するかの両方向の誤読が起きます。
- 根拠:
  - Trautmann et al. (2019) は dense array で population dynamics を spike sorting なしでもかなり回収できると示し、unit identity 依存の結論と population-level backbone 依存の結論を分ける必要を示しました。
  - Gregory et al. (2023) は array 周辺 neuron の structural / functional change を示し、implant 自体が測定だけでなく局所 perturbation でもあることを示しました。
- 修正:
  - `wiki/state-trait-and-drift.md` に `unit identity audit` を追加しました。
  - sorting version、drift correction、unit-match probability、dropout / new-unit rate、implant age、tissue-response proxy を必須監査欄として追記しました。

### 3. 旧 Verification は chronic extracellular recording の observability budget を十分 operational にしていませんでした

- 問題:
  - Observability Budget は measurement stack と latent state を固定していましたが、chronic probe 系の `same neuron across days` を止める専用欄がありませんでした。
- 修正:
  - `verification.md` の Observability Budget に `unit identity audit` 行を追加しました。
  - unit identity audit が無い chronic probe 結果は、single-unit longitudinal claim を受理しないと明記しました。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - `high-density extracellular probe` を独立 stack として追加
  - `local population window` と `stable unit identity` を分離
  - sorting / matching / drift audit を site rule へ反映
  - 関連一次文献を参考文献へ追加
- `wiki/state-trait-and-drift.md`
  - `last_updated` を 2026-03-15 に更新
  - chronic extracellular recording の drift 監査を追記
  - `unit identity audit` を新設
  - 関連一次文献を参考文献へ追加
- `tech_roadmap.md`
  - M1 に `high-density extracellular probe` 行を追加
  - M7 に chronic unit identity audit の注記を追加
  - 参考文献へ関連一次文献を追加
- `verification.md`
  - Observability Budget に chronic extracellular recording の `unit identity audit` を追加
  - `high-density extracellular probe` の default ceiling を明記
  - 参考文献へ関連一次文献を追加

## 外部依存で保留

- chronic probe benchmark の標準カード化
  - 担当者: AI / maintainer
  - 前提条件: `sorting version`, `drift correction`, `unit matching`, `dropout/new-unit rate`, `implant age`, `tissue-response proxy` の最小 schema をベンチ共通欄として確定すること
  - 完了条件: chronic invasive dataset / paper を読むときに、single-unit claim と population-window claim を同じ card 形式で監査できること

## 参考文献

- Steinmetz NA, Aydin C, Lebedeva A, et al. Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. *Science*. 2021;372(6539):eabf4588.
  - https://doi.org/10.1126/science.abf4588
- Pachitariu M, et al. Spike sorting with Kilosort4. *Nat Methods*. 2024;21:914-921.
  - https://doi.org/10.1038/s41592-024-02595-5
- Trautmann EM, Stavisky SD, Lahiri S, et al. Accurate estimation of neural population dynamics without spike sorting. *Neuron*. 2019;103(2):292-308.e4.
  - https://doi.org/10.1016/j.neuron.2019.05.003
- van Beest EH, Jia X, Deng X, et al. Tracking neurons across days with high-density probes. *Nat Methods*. 2024.
  - https://doi.org/10.1038/s41592-024-02440-1
- Gregory NS, et al. Structural and functional changes of deep layer pyramidal neurons surrounding implanted microelectrode arrays in rat motor cortex. *J Neural Eng*. 2023;20(4):046022.
  - https://doi.org/10.1088/1741-2552/ace8ac
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
