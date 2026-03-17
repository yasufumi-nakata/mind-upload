# Site Deepening Audit (2026-03-17, Shared Extracellular / Electrical State / chemical connectome ≠ electrical-ionic completeness)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `wbe_101.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`connectome-complete ≠ emulation-complete`、`same-day fit ≠ cross-day maintenance`、`decode ≠ emulate` をかなり強く整理できていました。
- その一方で、connectome の外に残る hidden state の整理は、なお `chemical synapse`、`dendrite`、`myelin`、`neuromodulation`、`glia`、`clearance` に厚く寄っており、`shared extracellular / electrical state` を独立クラスとしてほぼ扱っていませんでした。
- この欠落は技術・自然科学の観点で重要です。なぜなら、同じ chemical wiring と同じ cell type でも、`gap junction`、`endogenous electric field`、`interstitial ion / chloride state` が違えば、`inhibition sign / gain`、`fast synchrony`、`state-switch threshold`、`plasticity gate` が変わりうるからです。

## 根拠付き批判

### 1. 旧サイトは chemical connectome の外にある electrical / ionic state を、他の hidden-state 行へ埋め込みすぎていました

- 問題:
  - 既存サイトは `electrical synapses` を Lappalainen らの model omission として短く触れていましたが、読者が `chemical connectome がかなり取れれば、残る hidden state は主に synapse / dendrite / glia だ` と読める余地が残っていました。
  - しかし実際には、shared extracellular / electrical state はそれ自体で別の claim ceiling を作ります。
- 根拠:
  - Galarreta & Hestrin (1999) は neocortical fast-spiking interneuron 間の electrical coupling を示しました。
  - Anastassiou et al. (2011) は endogenous electric field が cortical neuron の spike timing を偏らせうることを示しました。
  - Ding et al. (2016) は brain interstitial ion composition を変えるだけで sleep-like / wake-like activity pattern を切り替えうることを示しました。
- 批判:
  - したがって、`chemical synapse graph` と `electrical / ionic state` は同じ箱ではありません。
  - `connectome-complete` を `electrical / ionic completeness` へ読み替えるのは過大でございます。

### 2. 旧サイトは inhibition の効き方を synapse / cell type 側へ寄せて読みやすく、chloride-dependent state を独立監査していませんでした

- 問題:
  - 既存サイトは inhibitory circuit の重要性自体は十分に書けていました。
  - しかし、`GABA がどれだけ抑制的に働くか` を local chloride state と activity history が左右する点は、主要本文ではほぼ独立扱いされていませんでした。
- 根拠:
  - Burman et al. (2023) は active cortical networks が in vivo で fast synaptic inhibition を shunting mode に寄せることを示しました。
  - Alfonsa et al. (2025) は sleep-wake-related な intracellular chloride 変化が glutamatergic cortical synapse の plasticity を調節することを示しました。
- 批判:
  - したがって、同じ connectome と同じ cell type が分かっていても、`inhibition sign / gain` や `plasticity gate` は固定されません。
  - `inhibitory edge がある` ことを、そのまま `その時点の inhibitory effect が分かる` と読むことはできません。

### 3. 旧 Verification 規格では electrical / ionic ceiling が提出物の不合格条件へ十分に落ちていませんでした

- 問題:
  - 状態変数の完全性ゲートは存在しましたが、`local ion / field / gap-junction state を持たない結果` が、どこまでしか言えないかは明示されていませんでした。
- 批判:
  - これでは `connectome + cell type + synaptic model` を持つ結果が、phase locking や state switching まで暗黙に持ち上がりやすくなります。
  - 技術サイトとしては、`何を直接見ていないなら何を主張してはいけないか` を card / gate に書く必要があります。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `shared extracellular / electrical state` を front matter、要約、bottom-line table、timescale matrix に追加
  - `9つの状態クラス` へ更新
  - `gap junction / ephaptic field / interstitial ion & chloride state` を独立節として追加
  - `augmentation / ablation` の説明にもこの state class を反映
  - 参考文献へ Galarreta & Hestrin (1999), Anastassiou et al. (2011), Ding et al. (2016), Burman et al. (2023), Alfonsa et al. (2025) を追加
- `wbe_101.md`
  - page highlights / known points に `shared extracellular / electrical state` を追加
  - hidden-state table に `shared extracellular / electrical state` の evidence row を追加
  - 短い hidden-state summary table にも同クラスを追加
  - 参考文献へ同上 5 本を追加
- `verification.md`
  - `状態変数の完全性ゲート` を `少なくとも7種類` に更新
  - `shared extracellular / electrical state` の gate row を追加
  - `chemical connectome は electrical / ionic completeness を自動では与えない` という運用 note を追加

## 外部依存で保留

- なし
  - 今回の作業は、一次文献に基づく公開本文と検証規格の更新で完結しています。

## 参考文献

1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/99496
2. Anastassiou CA, Perin R, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nature Neuroscience*. 2011;14:217-223.
   - https://doi.org/10.1038/nn.2727
3. Ding F, O'Donnell J, Xu Q, Kang N, Goldman N, Nedergaard M. Changes in the composition of brain interstitial ions control the sleep-wake cycle. *Science*. 2016;352(6285):550-555.
   - https://doi.org/10.1126/science.aaf3736
4. Burman RJ, et al. Active cortical networks promote shunting fast synaptic inhibition in vivo. *Neuron*. 2023;111(22):3633-3648.e8.
   - https://doi.org/10.1016/j.neuron.2023.07.013
5. Alfonsa H, et al. Sleep-wake-related changes in intracellular chloride regulate plasticity at glutamatergic cortical synapses. *Current Biology*. 2025.
   - https://doi.org/10.1016/j.cub.2025.01.050
