# Site Deepening Audit (2026-03-14, Homeostatic Maintenance States)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`
- 副対象: `tech_roadmap.md`
- 副対象: `perspective.md`
- 副対象: `wiki/index.md`

## 今回の選定理由

- 本日の自動深掘りでは、`connectome は scaffold であって state-complete ではない` という大枠はすでに強化されていました。
- しかし現行サイトの主な state-completeness 議論は、`細胞型 / シナプス / 遅延 / 神経修飾 / グリア` を中心にしており、`内在興奮性 / firing-rate set point / 分子ターンオーバー下の維持機構` が独立クラスとして前面に出ていませんでした。
- この欠落は、`同じ connectome + 同じ cell type なら長期ダイナミクスもかなり決まる` という誤読を許します。技術・自然科学の観点では、これはまだ過大主張です。

## 主要な批判点

### 1. 旧版は `cell type` を立てた後の `内在興奮性` を過小評価していました

- 問題:
  - 旧版は transcriptomic type や same-brain function を重視していましたが、同じ type の内部にも morpho-electric phenotype と ion-channel expression の幅が残る点を、独立の不足変数として扱っていませんでした。
  - そのため、`cell-type ラベルを付ければ threshold / gain / recovery もだいたい決まる` という誤読が残っていました。
- 根拠:
  - Gouwens et al. (2021) は、mouse cortex の transcriptomic type が morpho-electric space で連続的な変動を持つことを示しました。
  - Schulz et al. (2006) は、同定済みニューロンでも ion-channel mRNA と電流量に大きな個体差があることを示しました。
- 修正:
  - `wiki/connectome-is-not-enough.md` と `verification.md` の state-completeness 記述を `5 クラス` から `6 クラス` へ更新しました。
  - 新たに `内在興奮性・恒常性 set point` 行を追加しました。

### 2. 旧版は `今の活動値` と `どこへ戻るか` を分けていませんでした

- 問題:
  - 旧版は short-term state と synaptic state を論じていましたが、homeostatic controller と firing-rate set point を独立の技術論点として扱っていませんでした。
  - その結果、`短時間の活動一致` と `長期安定性` が近いものとして読めてしまいました。
- 根拠:
  - Turrigiano et al. (1998) は homeostatic synaptic scaling を示しました。
  - O'Leary et al. (2014) は activity-dependent channel expression から set point と compensation が生まれることを示しました。
  - Hengen et al. (2016) は in vivo で individual neuron の precise firing-rate set point を示しました。
- 修正:
  - 新設した wiki で `発火率 set point / homeostatic controller` を独立の maintenance-state として整理しました。
  - `verification.md`、`tech_roadmap.md`、`perspective.md` にも long-term claim を弱める条件として反映しました。

### 3. 旧版は `記憶が残る` ことを `静的な保存で十分` と読み違えうる構造でした

- 問題:
  - 旧版は可塑性やシナプス状態を扱っていましたが、分子ターンオーバーをまたいで記憶が維持されるとき、それが active maintenance を意味する点が正面から出ていませんでした。
- 根拠:
  - Yiu et al. (2014) は relative excitability が memory allocation を左右することを示しました。
  - Lee et al. (2022) は synaptic memory が molecular turnover の下でも active な state transfer により維持されうることを示しました。
- 修正:
  - 新規 wiki で `分子ターンオーバー下の維持機構` を第3の maintenance-state として追加しました。
  - `memory persistence = static molecular storage` と読まない rule を明記しました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - 新規追加
  - `内在興奮性 / ion-channel 構成`、`発火率 set point / homeostatic controller`、`分子ターンオーバー下の維持機構` を 3 つの maintenance-state として整理
  - 一次文献 8 本を付け、危険な誤読と site rule を明文化
- `wiki/connectome-is-not-enough.md`
  - `5 クラス` を `6 クラス` へ更新
  - `内在興奮性・恒常性 set point` を独立行として追加
  - 詳細説明と新 wiki への導線を追加
- `verification.md`
  - 状態変数の完全性ゲートを `6 クラス` へ更新
  - 新規 wiki への導線を追加
- `wbe_101.md`
  - 入門ページから新規 wiki への導線を追加
- `tech_roadmap.md`
  - R 系列と M3 に `intrinsic excitability / homeostatic set point` を追加
- `perspective.md`
  - 中核説明の `5 状態クラス` を `6 状態クラス` へ更新
- `wiki/index.md`
  - 新規 wiki の導線を追加

## 外部依存で保留

- human での直接的な excitability-homeostasis benchmark
  - 担当者: 実験系 collaborators / maintainer
  - 前提条件: 長期反復計測、perturbation、細胞内または侵襲系 ground truth、cross-day 追跡
  - 完了条件: connectome / cell type / excitability / recovery を同一 schema で比較できる benchmark が公開されること

## 参考文献

- Gouwens NW, et al. Phenotypic variation of transcriptomic cell types in mouse motor cortex. Nature. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Schulz DJ, Goaillard J-M, Marder E. Variable channel expression in identified single and electrically coupled neurons in different animals. Nat Neurosci. 2006.
  - https://doi.org/10.1038/nn1639
- Turrigiano GG, Leslie KR, Desai NS, Rutherford LC, Nelson SB. Activity-dependent scaling of quantal amplitude in neocortical neurons. Nature. 1998.
  - https://doi.org/10.1038/36103
- O'Leary T, Williams AH, Franci A, Marder E. Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. Neuron. 2014.
  - https://doi.org/10.1016/j.neuron.2014.04.002
- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. Cell. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Yiu AP, et al. Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. Neuron. 2014.
  - https://doi.org/10.1016/j.neuron.2014.07.017
- Hadzibegovic N, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. Nat Commun. 2026.
  - https://doi.org/10.1038/s41467-025-66975-3
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. Proc Natl Acad Sci U S A. 2022.
  - https://doi.org/10.1073/pnas.2211572119
