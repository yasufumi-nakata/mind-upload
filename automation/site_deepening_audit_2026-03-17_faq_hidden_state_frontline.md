# Site Deepening Audit (2026-03-17, FAQ Hidden-State Frontline / Public-Facing Compression Risk)

## 対象

- 主対象: `faq.md`
- 副対象: `summary_booklet.md`

## 今回の選定理由

- 2026-03-17 時点の深い本文と wiki では、`connectome-complete ≠ emulation-complete`、`multimodal ≠ state-complete`、`same-day fit ≠ cross-day maintenance` がかなり明確に整理されていました。
- しかし入口の `faq.md` は、`Q2c` でなお `sleep / myelin / glia` への圧縮が強く、2026-03 に追加済みの `current synaptic state`、`dendritic integration`、`AIS / excitability`、`clearance / immune support`、`human proxy ceiling` が一般読者に届き切っていませんでした。
- web で公開側を確認すると、トップページに比べて FAQ は live 反映も弱く、入口としての更新優先度が高いと判断しました。

## 根拠付き批判

### 1. 旧 FAQ は hidden state を `maintenance-state` 側へ寄せすぎており、fast / controller / slow の層差が消えていました

- 問題:
  - 旧 `Q2c` は `sleep / myelin / glia` を中心に正しく注意喚起していました。
  - その一方で、`current synaptic efficacy / release state`、`branch-specific dendritic integration`、`AIS / excitability / recovery controller` が FAQ 上では十分前面化されていませんでした。
- 根拠:
  - Gouwens et al. (2021) は同じ transcriptomic type の内部に morpho-electric phenotype の幅が残ることを示しました。
  - Mittermaier et al. (2024) は human neocortical tissue で membrane-state sequence が synaptic efficacy と consolidation を短時間で動かすことを示しました。
  - Gidon et al. (2020) は human layer 2/3 neuron の dendritic action potential と計算特性を示しました。
  - Benoit et al. (2025) と Hadzibegovic et al. (2026) は excitability / AIS / memory allocation / recovery window が別 state class であることを示しました。
- 批判:
  - したがって FAQ が `maintenance-state が残る` だけで止まると、読者は `fast execution state` と `controller state` を見落としやすく、`connectome + cell type + 少しの補正` という誤読へ戻ります。

### 2. 旧 FAQ は `same-brain structure-function link` と `state-complete reconstruction` の境界を入口で十分に固定していませんでした

- 問題:
  - 深い本文では MICrONS や connectome-constrained modelling の ceiling を整理できていましたが、FAQ はその結果をまだ十分に圧縮して返せていませんでした。
- 根拠:
  - MICrONS Consortium et al. (2025) が直接押し上げたのは same-brain の local structure-function link です。
  - Beiran & Litwin-Kumar (2025) は connectome 制約を入れても dynamics の縮退が残ることを示しました。
- 批判:
  - 入口でこの境界が弱いと、読者は `same-brain connectomics まで来た = current state もかなり埋まった` と読みやすくなります。

### 3. 旧 FAQ は human observability ceiling を `human でも見え始めた` に寄せすぎていました

- 問題:
  - 深い wiki では `local ex vivo dendrite evidence`、`macro-biochemical scaffold`、`myelin proxy`、`perturbation proxy`、`CSF / glymphatic proxy` を分けていましたが、FAQ にはその層差が十分に入っていませんでした。
- 根拠:
  - Lucchetti et al. (2025) は parcel-level の metabolic connectome を示しました。
  - Baadsvik et al. (2024) は human myelin bilayer map を示しました。
  - Zrenner et al. (2018) は EEG-defined excitability proxy が TMS plasticity efficacy を左右することを示しました。
  - Dagum et al. (2026) は human で glymphatic route に沿った biomarker transport を示しました。
- 批判:
  - これらが押し上げるのは `macro scaffold / proxy` であり、whole-brain in vivo の `state-complete readout` ではありません。FAQ でもこの ceiling を明示しないと、`human でもかなり直接見え始めた` という誤読を止め切れません。

## 今回実行した変更

- `faq.md`
  - `page_highlights` と `known_points` を、`current synaptic state / dendritic integration / AIS / maintenance-state` を見える形へ更新
  - 入口案内テーブルの `Q2c` 説明を `sleep / myelin / glia` から、`synaptic state / dendrite / AIS / maintenance-state` へ更新
  - `Q2c` を全面改稿し、`fast execution state`、`controller state`、`slow maintenance-state`、`human observability ceiling` の 4 層へ再分解
  - MICrONS / Beiran-Litwin-Kumar / Mittermaier / Gidon / Benoit / Hadzibegovic / Williamson / Kim / Lucchetti / Baadsvik / Zrenner / Dagum を追記

## 外部依存で保留

- なし
  - 今回の修正は、公開 FAQ の改稿で完結しています。

## 参考文献

1. Gouwens NW, et al. Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. *Nature*. 2021.
   - https://doi.org/10.1038/s41586-020-2907-3
2. MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
3. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02080-4
4. Mittermaier V, Kononenko NL, Jin Y, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-024-53901-2
5. Gidon A, et al. Dendritic action potentials and computation in human layer 2/3 cortical neurons. *Science*. 2020.
   - https://doi.org/10.1126/science.aax6239
6. Benoit CM, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02152-5
7. Hadzibegovic N, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-025-66975-3
8. Hengen KB, et al. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016.
   - https://doi.org/10.1016/j.cell.2016.01.046
9. Torrado Pacheco A, et al. Sleep promotes downward firing rate homeostasis. *Neuron*. 2021.
   - https://doi.org/10.1016/j.neuron.2021.04.004
10. Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-023-01536-9
11. Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-023-01558-3
12. Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
   - https://doi.org/10.1038/s41586-024-07311-5
13. Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-024-08170-w
14. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
   - https://doi.org/10.1016/j.cell.2025.02.022
15. Lucchetti F, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
16. Baadsvik EL, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
17. Zrenner C, et al. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018.
   - https://doi.org/10.1016/j.brs.2017.11.016
18. Dagum P, et al. The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
