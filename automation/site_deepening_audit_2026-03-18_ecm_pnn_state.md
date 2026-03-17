# Site Deepening Audit (2026-03-18, ECM / PNN State Is Not Just Synapse Packaging)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`cell type`、`intrinsic excitability`、`synaptic state`、`timing-state`、`neuromodulation`、`glia` をかなり強く分解できておりました。
- その一方で、`perisynaptic extracellular matrix / perineuronal nets (ECM / PNN)` は、可塑性や記憶安定化の前提条件としてほぼ独立記述されておらず、読者が `synapse count / weight を書けば plasticity gate もほぼ含まれる` と誤読しうる構造が残っておりました。
- この欠落は技術・自然科学の観点で重要です。なぜなら、同じ connectome と同じ synapse graph でも、ECM / PNN 状態が違えば `AMPA receptor mobility`、`adult plasticity window`、`GABAergic inhibitory plasticity`、`memory erasure resistance` が変わりうるからです。

## 主要な批判点

### 1. 旧 site は `synaptic state` と `glial / slow-state` を分けていたが、ECM / PNN を独立 state class にしていませんでした

- 問題:
  - `verification.md` と `wiki/connectome-is-not-enough.md` は、配線だけでは足りないという主張自体は正しく置けていました。
  - しかし、`synapse` と `glia` のあいだにある ECM / PNN を独立の監査対象にしていなかったため、`weights を推定した` を `plasticity gate もかなり分かった` と誤読できる余地が残っていました。
- 根拠:
  - Pizzorusso et al. (2002) は、chondroitinase により adult visual cortex の ocular-dominance plasticity を再活性化できることを示しました。
  - Frischknecht et al. (2009) は、brain ECM が AMPA receptor lateral mobility と short-term synaptic plasticity を制約することを示しました。
  - Gogolla et al. (2009) は、perineuronal nets が fear memory の erasure を防ぐことを示しました。
- 批判:
  - したがって、`synapse graph` を書くだけでは、`その回路が今どの可塑性窓にいるか` までは固定できません。
  - ECM / PNN は `synapse detail の脚注` ではなく、独立の state class として書くべきでした。

### 2. 旧 `maintenance-state` は bioenergetics, astrocytes, clearance を厚く扱っていたが、matrix-dependent plasticity gate を落としていました

- 問題:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` は maintenance-state を豊かに整理していました。
  - しかし、`adult plasticity gate`、`inhibitory stabilization`、`memory-update resistance` を ECM / PNN 状態としては独立列挙していませんでした。
- 根拠:
  - Chelini et al. (2024) は、peri-synaptic matrix cluster が activity-dependent plasticity と memory に寄与することを示しました。
  - Jabłońska et al. (2024) は、ECM integrity が hippocampus の GABAergic plasticity を調節することを示しました。
- 批判:
  - これらは、ECM / PNN が単なる構造材ではなく、回路の更新則そのものに関わることを示しています。
  - したがって、maintenance-state のリストから ECM / PNN を落とすと、`stability` と `plasticity` の境界条件を 1 段欠いた説明になります。

### 3. 旧 entry page は `hidden state` を示していたが、ECM / PNN による plasticity ceiling を入口で止めていませんでした

- 問題:
  - `wbe_101.md` は初心者向けに hidden state を非常に良く整理していましたが、ECM / PNN が抜けていたため、`synapse count + myelin + glia` を見ればかなり十分、という読みがまだ残りました。
- 根拠:
  - Pizzorusso et al. (2002)、Frischknecht et al. (2009)、Gogolla et al. (2009)、Jabłońska et al. (2024)。
- 批判:
  - 入口でこの層を止めないと、`構造再現` と `可塑性・再固定化の条件再現` が混ざります。
  - WBE entry としては、ECM / PNN を hidden state に含めないのは甘すぎました。

### 4. human observability ceiling にも `ECM / PNN はまだ in vivo whole-brain readout が乏しい` という線引きがありませんでした

- 問題:
  - human 側の observability は、SV2A PET、MRSI、myelin bilayer、sleep / TMS proxy、CSF / glymphatic proxy までかなり整理されていました。
  - しかし、ECM / PNN は `今どこまで human で直接見えているのか` が本文に固定されていませんでした。
- 根拠:
  - Boonen et al. (2022) は human hippocampal sclerosis tissue における ECM 再編成を示しましたが、これは ex vivo pathology です。
- 批判:
  - したがって、human ECM evidence は `another biological layer exists` を支持しても、`current in vivo ECM gate` の ground truth ではありません。
  - site-wide rule として、human ECM evidence はまず `ex vivo/pathology support` と書くべきでした。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `last_updated` を `2026-03-18` に更新
  - maintenance-state の全体像を `9 maintenance-states` へ拡張
  - `Perisynaptic ECM / PNN state` を表に追加
  - ECM / PNN 専用節を新設し、plasticity gate・receptor mobility・memory erasure resistance・GABAergic plasticity を独立説明
  - human observability に `ECM / PNN は主として ex vivo/pathology layer` という ceiling を追加
- `wiki/connectome-is-not-enough.md`
  - `6 state classes` を `7 state classes` へ更新
  - state-class table に `Perisynaptic ECM / PNN state` 行を追加
  - `Why are these 7 classes easy to skip` に ECM / PNN の独立節を追加
  - augmentation / ablation table に `+ ECM / PNN state audit` 行を追加
  - site rule に `ECM / PNN は synapse count や glial support に潰さない` という運用規則を追加
- `verification.md`
  - Observability Budget の `remaining latent state` に ECM / PNN を追加
  - `State variable integrity gate` を 7 class 構成へ更新
  - ECM / PNN 専用 addendum を追加
  - augmentation table に `+ ECM / PNN state audit` を追加
- `wbe_101.md`
  - `last_updated` を `2026-03-18` に更新
  - hidden-state の入口説明に ECM / PNN を追加
  - entry-level hidden-state table に `Perisynaptic ECM / PNN state` を追加
  - 併せて Looser et al. (2024) の DOI 誤記を修正

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・検証ルール・エントリ説明・内部監査メモの改稿で完結しております。

## 参考文献

1. Pizzorusso T, Medini P, Berardi N, Chierzi S, Fawcett JW, Maffei L. Reactivation of ocular dominance plasticity in the adult visual cortex. *Science*. 2002.
   - https://doi.org/10.1126/science.1072699
2. Frischknecht R, Heine M, Perrais D, Seidenbecher CI, Choquet D, Gundelfinger ED. Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. *Nature Neuroscience*. 2009.
   - https://doi.org/10.1038/nn.2338
3. Gogolla N, Caroni P, Lüthi A, Herry C. Perineuronal nets protect fear memories from erasure. *Science*. 2009.
   - https://doi.org/10.1126/science.1174146
4. Chelini G, Pantazopoulos H, Durning P, et al. Focal clusters of peri-synaptic matrix contribute to activity-dependent plasticity and memory in mice. *Cell Reports*. 2024.
   - https://doi.org/10.1016/j.celrep.2024.114112
5. Jabłońska K, Kaczor K, Kółeczko M, et al. Extracellular matrix integrity regulates GABAergic plasticity in the hippocampus. *Matrix Biology*. 2024.
   - https://doi.org/10.1016/j.matbio.2024.11.001
6. Boonen M, Hellings N, Hoedemaekers T, et al. Reorganization of the brain extracellular matrix in hippocampal sclerosis. *International Journal of Molecular Sciences*. 2022.
   - https://doi.org/10.3390/ijms23158197
