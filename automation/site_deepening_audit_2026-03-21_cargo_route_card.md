# Site Deepening Audit (2026-03-21, Cargo Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `verification.md`

## 今回の選定理由

- 既存サイトは `cargo-transport / cytoskeletal trafficking` を hidden state としてはすでに独立化できていました。
- しかし現状のままだと、`postsynaptic receptor delivery`、`activity-dependent vesicle confinement`、`learning-phase microtubule-state gating`、`axonal RNA localization`、`presynaptic cargo retention` が、まだ同じ `cargo evidence` として読めてしまいました。
- これは技術・自然科学の観点では粗すぎます。なぜなら、どの cargo を、どの compartment で、どの transport phase について、どの timescale で、どの causal leverage で見たかが違えば、主張できる ceiling が大きく変わるからです。

## 主要な批判点

### 1. 旧サイトは `何が届いたか` と `どこで足止めされたか` と `何が長期記憶に必要か` を十分に分離できていませんでした

- 問題:
  - 既存本文は `proteostasis` と `bioenergetics` から cargo routing を独立 state として切り出していました。
  - しかし cargo 側の中でも、`postsynaptic receptor delivery`, `local confinement near a stimulated shaft`, `axonal RNA localization`, `presynaptic cargo pausing / retention` は別の inferential object です。
- 根拠:
  - Park et al. (2006) は recycling-endosome exocytosis が LTP-associated spine growth に必要であることを示しました。
  - Correia et al. (2008) は myosin-Va-dependent AMPAR transport into spines during LTP を示しました。
  - Wong et al. (2024) は endogenous GluA1 vesicles が stimulated dendritic region の近傍で confinement され reservoir を増やすことを示しましたが、同時に `direct spine exocytosis solved` とは読めません。
  - de Queiroz et al. (2025) は mature in vivo memory circuit で axonal RNA localization が long-term memory に必要で short-term memory には不要であることを示しました。
- 批判:
  - したがって、`transport evidence exists` を `cargo route is broadly solved` と読むのは過剰です。

### 2. 旧サイトは `transport-path state` と `cargo object` と `transport phase` を監査項目として固定していませんでした

- 問題:
  - 既存の `verification.md` には cargo 行がありましたが、`claim family` と `transport phase / state variable` がまだ明示されていませんでした。
  - この構造だと、読者や投稿者が `delivery`, `pausing`, `retention`, `RNA localization`, `exocytosis` を一括で申告しても通ってしまいます。
- 根拠:
  - Uchida et al. (2014) は learning-phase microtubule stability と KIF5-mediated GluA2 localization を通じた memory control を示しました。
  - Aiken & Holzbaur (2024) は local axonal microtubule dynamics が presynaptic cargo delivery and pausing を pattern することを示しました。
- 批判:
  - したがって、`cargo` という語だけでは route audit として不十分です。少なくとも `claim family / cargo object / compartment scope / transport phase / trigger / direct observable / causal leverage / human ceiling` を固定する必要があります。

### 3. 旧サイトは `human-related evidence` の ceiling を cargo 論点ではまだ弱く止めていました

- 問題:
  - 既存本文は living human in vivo で branch- or bouton-specific cargo traffic を見ていないと書いていました。
  - しかし `human neuron preparation` と `living-human whole-brain route` の差が front-facing rule としてはまだ弱く、culture evidence を human observability progress に過剰接続する余地が残っていました。
- 根拠:
  - Aiken & Holzbaur (2024) は human induced-neuron axon preparation を使った mechanistic advance です。
  - これは重要ですが、living-human whole-brain cargo-state ground truth ではありません。
- 批判:
  - `human-derived preparation exists` を `human in vivo observability improved` と読み替えるのは、このサイトが止めるべき shortcut です。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights` と `known_points` に cargo route-card 必要性を追加
  - `unknown_points` に cargo route-card fields 未確定という論点を追加
  - cargo section を再記述し、`delivery / confinement / microtubule-state / RNA localization / presynaptic retention` を分離
  - `cargo-route-card` を新設し、必要監査項目を table 化
  - Correia et al. (2008), Uchida et al. (2014), Wong et al. (2024), de Queiroz et al. (2025) を参考文献へ追加
- `wbe_101.md`
  - 入口ページに `Cargo-transport evidence now gets its own route card` note を追加
  - entry point でも cargo evidence class の分離を明文化
  - 新規参考文献を追加
- `verification.md`
  - `Cargo-transport / cytoskeletal trafficking route` 行を route-card 前提の監査項目へ拡張
  - `Cargo-transport / cytoskeletal trafficking support` 行を route-card 前提へ更新
  - `cargo evidence also needs a route card` note を追加
  - minimum operating rules に cargo support 欠落時の ceiling を追加
  - 新規参考文献を追加

## 外部依存で保留

- living-human whole-brain での branch / spine / bouton-specific cargo-state ground truth
  - 担当者: 高分解能 live imaging・molecular transport・human-compatible neurotechnology の実験研究者
  - 前提条件: cargo object, motor engagement, pausing / docking / retention, and local functional target を living-human setting で較正できる計測系
  - 完了条件: same-subject living-human route で cargo class と transport phase を比較可能な benchmark または causal intervention 系が整備されること

## 参考文献

1. Park M, Salgado JM, Ostroff L, Helton TD, Robinson CG, Harris KM, Ehlers MD. Plasticity-induced growth of dendritic spines by exocytic trafficking from recycling endosomes. *Neuron*. 2006;52(5):817-830.
   - https://doi.org/10.1016/j.neuron.2006.09.040
2. Correia SS, Bassani S, Brown TC, Lisé M-F, Backos DS, El-Husseini A, Passafaro M, Esteban JA. Motor protein-dependent transport of AMPA receptors into spines during long-term potentiation. *Nature Neuroscience*. 2008;11:457-466.
   - https://doi.org/10.1038/nn2063
3. Maas C, Belgardt D, Lee HK, Heisler FF, Lappe-Siefke C, Magiera MM, van Dijk J, Hausrat TJ, Janke C, Kneussel M. Synaptic activation modifies microtubules underlying transport of postsynaptic cargo. *PNAS*. 2009;106(21):8731-8736.
   - https://doi.org/10.1073/pnas.0902304106
4. Uchida S, Martel G, Pavlowsky A, Takizawa S, Hevi C, Watanabe Y, Alarcon JM, Shumyatsky GP. Learning-induced and stathmin-dependent changes in microtubule stability are critical for memory and disrupted in ageing. *Nature Communications*. 2014;5:4389.
   - https://doi.org/10.1038/ncomms5389
5. Zhao J, Fok AHK, Fan R, Kwan P-Y, Chan H-L, Lo LHY, Chan Y-S, Yung W-H, Huang J, Lai CSW, Lai K-O. Specific depletion of the motor protein KIF5B leads to deficits in dendritic transport, synaptic plasticity and memory. *eLife*. 2020;9:e53456.
   - https://doi.org/10.7554/eLife.53456
6. Swarnkar S, Avchalumov Y, Espadas I, Grinman E, Liu X-A, Raveendra BL, Zucca A, Mediouni S, Sadhu A, Valente S, Page D, Miller K, Puthanveettil SV. Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. *Cell Reports*. 2021;36(2):109369.
   - https://doi.org/10.1016/j.celrep.2021.109369
7. Wong VC, Houlihan PR, Liu H, Walpita D, DeSantis MC, Liu Z, O'Shea EK. Plasticity-induced actin polymerization in the dendritic shaft regulates intracellular AMPA receptor trafficking. *eLife*. 2024;13:e80622.
   - https://doi.org/10.7554/eLife.80622
8. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Current Biology*. 2024;34(8):1687-1704.e8.
   - https://doi.org/10.1016/j.cub.2024.03.010
9. de Queiroz BR, Laghrissi H, Rajeev S, Blot L, De Graeve F, Dehecq M, Keleman K, Ule J, Hubstenberger A, Besse F. Axonal RNA localization is essential for long-term memory. *Nature Communications*. 2025;16:2560.
   - https://doi.org/10.1038/s41467-025-57651-7
