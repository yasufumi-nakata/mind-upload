# Site Deepening Audit (2026-03-20, Cargo-Transport / Cytoskeletal Trafficking State)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 入口・運用反映: `wbe_101.md`, `faq.md`, `verification.md`, `glossary.md`

## 今回の選定理由

- 既存サイトは `connectome ≠ current state`、`cell type ≠ excitability-complete`、`proteostasis ≠ late stabilization complete`、`bioenergetics ≠ local mechanism complete` をかなり丁寧に分離できていました。
- しかしその一方で、`どの receptor / endosome / RNA cargo / organelle / presynaptic component が、必要な時間幅で、必要な branch / spine / bouton に到達しているか` という輸送層は、なお `proteostasis` や `ATP support` の影に隠れていました。
- このままでは読者が `weight, local translation, ATP がだいたい分かれば、局所 delivery もほぼ固定できる` と誤読しやすく、技術・自然科学の観点ではここが未補強の弱点でした。

## 主要な批判点

### 1. 旧サイトは `何が作られるか` と `何が届くか` を十分に分離できていませんでした

- 問題:
  - 既存本文は local proteostasis と bioenergetic support を独立 state としてかなり前進させていました。
  - しかし、同じ translation capacity や ATP reserve があっても、receptor, recycling endosome, RNA cargo, mitochondria, presynaptic material の delivery route が違えば、compartment-specific plasticity outcome はまだ変わりえます。
- 根拠:
  - Park et al. (2006) は recycling-endosome exocytosis が LTP-associated spine growth に必要であることを示しました。
  - Maas et al. (2009) は synaptic activation により postsynaptic cargo transport を支える microtubule が再編されることを示しました。
  - Yin et al. (2011) は KIF17 が NR2A/2B balance と memory を支えることを示しました。
- 批判:
  - したがって、`局所翻訳がある` と `必要な cargo が正しい場所へ到達している` は同義ではありません。

### 2. 旧サイトは `postsynaptic stabilization` と `presynaptic delivery` を同じ粗さで読ませていました

- 問題:
  - 既存の hidden-state 説明は postsynaptic 側の state を厚くしていた一方で、presynaptic cargo delivery と bouton-specific retention の独立性が薄く残っていました。
- 根拠:
  - Zhao et al. (2020) は KIF5B depletion により dendritic transport, synaptic plasticity, memory が障害されることを示しました。
  - Swarnkar et al. (2021) は KIF5C-mediated transport が structural plasticity と long-term memory を制約することを示しました。
  - Aiken & Holzbaur (2024) は axonal microtubule patterning が presynaptic cargo delivery を制御することを示しました。
- 批判:
  - したがって、`synaptic state` を論じるときに presynaptic delivery route を別列に立てないのは粗すぎました。

### 3. 旧サイトは human observability ceiling に `cargo routing` の不可視性を十分反映していませんでした

- 問題:
  - human 側の前進として tractography, PET, MRSI, sodium MRI, thermometry, myelin proxy, clearance proxy はよく整理されていました。
  - しかし、それらが `branch- or bouton-specific cargo pausing, motor engagement, microtubule traffic state` を直接見ていない点は、本文前面ではまだ弱く、読者が proxy bundle を local transport ground truth へ過剰昇格させる余地がありました。
- 批判:
  - 技術・自然科学の観点では、`何が見えていないか` を書かない限り、observability ladder は完成しません。
- 修正方針:
  - human in vivo route は、cargo transport についてはなお `local hidden state` として扱うことを明文化しました。

### 4. verification 側で監査列がなければ、実務上は見落とされます

- 問題:
  - hidden state として本文に書いても、`verification.md` の error budget と augmentation table に入っていなければ、投稿物審査では落ちやすい論点のままです。
- 批判:
  - `state variable` と `submission rule` が一致していなければ、サイト運用上は独立 class として機能しません。
- 修正:
  - latent-state error budget と maintenance-state error budget の双方に `cargo-transport / cytoskeletal trafficking` を追加し、`weight / proteostasis / ATP` のどれにも畳み込まない site rule を明記しました。

## 今回実行した変更

- `wbe_101.md`
  - hidden-state の導入と table に `Cargo-transport / cytoskeletal trafficking state` を追加
  - connectome / maintenance-state 説明へ cargo-delivery route の不可欠性を反映
  - 参考文献を追加
- `faq.md`
  - `connectome and cell type` だけでは足りない理由に cargo-delivery layer を追加
  - human evidence ladder の不可視項目に branch/bouton-specific cargo routing を追加
  - 参考文献を追加
- `verification.md`
  - latent-state error budget と maintenance-state error budget に transport 行を追加
  - `Do not collapse cargo delivery into proteostasis or ATP` note を追加
  - state variable integrity gate と minimum operating rules に transport state を反映
  - 参考文献を追加
- `glossary.md`
  - `Maintenance-state` の定義を更新
  - `Cargo-transport / cytoskeletal trafficking state` 項目を追加
- `wiki/connectome-is-not-enough.md`
  - missing hidden-state class に cargo-transport を追加
  - augmentation / ablation ladder と site rule に transport audit を追加
  - `weight / transcriptomic clue / macro energetic proxy` では compartment-specific delivery の ground truth にならないことを明記
  - 参考文献を追加
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - maintenance-state count を更新
  - `Cargo-transport / cytoskeletal trafficking is not implied by proteostasis or ATP` 節を新設
  - human observability ceiling に cargo-routing 不可視性を追加
  - site rule に transport state を追加
  - 参考文献を追加

## 外部依存で保留

- human in vivo での branch/spine/bouton-specific cargo-transport ground truth
  - 担当者: 実験系共同研究者 / 高分解能計測系研究者
  - 前提条件: cargo pausing, motor engagement, microtubule traffic state, bouton retention を人で直接または強く外部較正できる計測系
  - 完了条件: human longitudinal setting で compartment-specific delivery route を比較可能にする公開 benchmark または因果介入系が整備されること

## 参考文献

1. Park M, Salgado JM, Ostroff L, Helton TD, Robinson CG, Harris KM, Ehlers MD. Plasticity-induced growth of dendritic spines by exocytic trafficking from recycling endosomes. *Neuron*. 2006;52(5):817-830.
   - https://doi.org/10.1016/j.neuron.2006.09.040
2. Maas C, Belgardt D, Lee HK, Heisler FF, Lappe-Siefke C, Magiera MM, van Dijk J, Hausrat TJ, Janke C, Kneussel M. Synaptic activation modifies microtubules underlying transport of postsynaptic cargo. *Proceedings of the National Academy of Sciences of the United States of America*. 2009;106(21):8731-8736.
   - https://doi.org/10.1073/pnas.0902304106
3. Yin X, Takei Y, Kido MA, Hirokawa N. Molecular motor KIF17 is fundamental for memory and learning via differential support of synaptic NR2A/2B levels. *Neuron*. 2011;70(2):310-325.
   - https://doi.org/10.1016/j.neuron.2011.03.026
4. Zhao J, Fok AHK, Fan R, Kwan P-Y, Chan H-L, Lo LHY, Chan Y-S, Yung W-H, Huang J, Lai CSW, Lai K-O. Specific depletion of the motor protein KIF5B leads to deficits in dendritic transport, synaptic plasticity and memory. *eLife*. 2020;9:e53456.
   - https://doi.org/10.7554/eLife.53456
5. Swarnkar S, Avchalumov Y, Espadas I, Grinman E, Liu X-A, Raveendra BL, Zucca A, Mediouni S, Sadhu A, Valente S, Page D, Miller K, Puthanveettil SV. Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. *Cell Reports*. 2021;36(2):109369.
   - https://doi.org/10.1016/j.celrep.2021.109369
6. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Current Biology*. 2024;34(8):1687-1704.e8.
   - https://doi.org/10.1016/j.cub.2024.03.010
