# Site Deepening Audit (2026-03-15, Maintenance State / Sleep / Myelin / Metabolic Support)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-14 時点で公開サイトは、connectome と cell type だけでは不十分であることをかなり明確にしていました。
- ただし、`Wiki: 恒常性可塑性と維持状態` はなお `内在興奮性 / 発火率 set point / 分子ターンオーバー` の 3 点に重心があり、睡眠依存の再正規化、髄鞘 / オリゴデンドロサイト、グリア代謝支援を maintenance-state の本体として十分に固定していませんでした。
- これは技術・自然科学の観点で弱点です。なぜなら、長期ダイナミクス、cross-day stability、学習後の再平衡、timing-sensitive closed loop を読む際に、`昼間の活動が似た` ことを `維持機構まで同じ` と誤読しやすい構造だったからです。

## 主要な批判点

### 1. 現行ページは maintenance-state を狭く取りすぎており、sleep を controller の時間軸として扱えていませんでした

- 問題:
  - 旧版は firing-rate set point と molecular turnover を押さえていましたが、sleep / wake cycle 自体が synaptic scaling と homeostatic recovery の実行相であることを前面に出していませんでした。
  - そのため、same-day の活動一致や短期 decode 成績が、cross-day stability や長期維持に近い証拠であるかのように読める余地が残っていました。
- 根拠:
  - Hengen et al. (2016) は firing-rate homeostasis が sleep / wake で非対称に進むことを示しました。
  - Torrado Pacheco et al. (2021) は sleep が downward firing-rate homeostasis を進めることを示しました。
  - de Vivo et al. (2017)、Diering et al. (2017)、Noya et al. (2019)、Xu et al. (2024) は、sleep 中に ultrastructure、synaptic scaling、proteome、network regime が系統的に更新されることを示しました。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` を `3 つ` から `6 つ` の maintenance-state へ再編しました。
  - `sleep / wake 依存の再正規化` を独立クラスとして追加し、same-day fit と overnight maintenance を分離しました。

### 2. 旧版は myelin / oligodendrocyte state を maintenance-state に十分に含めていませんでした

- 問題:
  - 旧版は遅延や髄鞘の話を他ページ側へ逃がしており、このページ単体では `維持状態` が neuron-centric に見えました。
  - しかし timing-sensitive claim では、myelin は単なる固定遅延ではなく、activity-dependent に変化する状態変数です。
- 根拠:
  - Gibson et al. (2014) は neuronal activity が oligodendrogenesis と adaptive myelination を促進することを示しました。
  - McKenzie et al. (2014) は motor skill learning に active central myelination が必要であることを示しました。
  - Looser et al. (2024) は oligodendrocyte-axon metabolic coupling が axonal health の維持に関わることを示しました。
- 修正:
  - `髄鞘 / オリゴデンドロサイト support` を独立クラスとして追加しました。
  - delay を固定定数で吸収した場合は、それで何を捨てたかを本文に残す運用ルールへ更新しました。

### 3. 旧版は glial / metabolic support を `分子ターンオーバーの背景` に近く扱っており、記憶固定化の主変数として弱かった

- 問題:
  - 旧版は active maintenance を分子状態の持続として述べていましたが、astrocyte-neuron lactate transport や astrocyte network state のような support mechanism を十分に分離していませんでした。
  - その結果、memory persistence が `神経側の内部状態だけ` の問題として読める構造が残っていました。
- 根拠:
  - Suzuki et al. (2011) は astrocyte-neuron lactate transport が long-term memory formation に必要であることを示しました。
  - Cahill et al. (2024) は local neurotransmitter input が astrocyte network state に minutes-long に符号化されることを示しました。
  - Lee et al. (2022) は molecular turnover の下でも記憶が active maintenance で残りうることを示しました。
- 修正:
  - `グリア代謝 / substrate routing` と `分子ターンオーバー下の再固定化` を分離しました。
  - 記憶維持を `static storage` ではなく `再正規化と再固定化の連鎖` として読む文面へ改稿しました。

### 4. Verification 側の state-completeness gate も、maintenance-state の広がりをまだ十分に反映していませんでした

- 問題:
  - `verification.md` の表は有用ですが、`内在興奮性・恒常性 set point` の説明が excitability に寄りすぎており、sleep-dependent renormalization や recovery controller を明示していませんでした。
- 修正:
  - `verification.md` の該当行を更新し、sleep / wake に依存した renormalization と recovery controller を含む表現に改めました。
  - 実務ルールの注記も `恒常性 / 維持状態` として言い換えました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - front matter と要約を更新
  - `6 つの maintenance-state` 表へ全面改稿
  - sleep-dependent renormalization、adaptive myelination、oligodendrocyte metabolic coupling、astrocyte metabolic support の節を追加
  - 誤読テーブルと実務ルールを、cross-day / overnight / timing-sensitive claim へ対応させて更新
  - 参考文献を 18 本へ拡張
- `verification.md`
  - `状態変数の完全性ゲート` の `内在興奮性・恒常性 set point` 行を更新
  - 注記の `恒常性 / 維持状態` 表現へ同期

## 外部依存で保留

- sleep / myelin / glial maintenance を含む公開 benchmark の整備
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: sleep state、cross-day recovery、myelin proxy、glial / metabolic proxy を同一個体で追える公開データ
  - 完了条件: `same-day fit`、`overnight recovery`、`timing-sensitive stability` を同一 schema で比較できる benchmark を site-wide に再利用できること

## 参考文献

- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. Cell. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Torrado Pacheco A, et al. Sleep Promotes Downward Firing Rate Homeostasis. Neuron. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- de Vivo L, et al. Ultrastructural evidence for synaptic scaling across the wake/sleep cycle. Science. 2017.
  - https://doi.org/10.1126/science.aah5982
- Diering GH, et al. Homer1a drives homeostatic scaling-down of excitatory synapses during sleep. Science. 2017.
  - https://doi.org/10.1126/science.aai8355
- Noya SB, et al. The forebrain synaptic transcriptome is organized by clocks but its proteome is driven by sleep. Science. 2019.
  - https://doi.org/10.1126/science.aav2642
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. Nature Communications. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. Science. 2014.
  - https://doi.org/10.1126/science.1252304
- McKenzie IA, et al. Motor skill learning requires active central myelination. Science. 2014.
  - https://doi.org/10.1126/science.1254960
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. Nature Neuroscience. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Suzuki A, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. Cell. 2011.
  - https://doi.org/10.1016/j.cell.2011.02.018
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. PNAS. 2022.
  - https://doi.org/10.1073/pnas.2211572119
