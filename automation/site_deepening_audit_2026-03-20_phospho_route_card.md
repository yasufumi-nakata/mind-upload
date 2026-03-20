# Site Deepening Audit (2026-03-20, Phospho-Signaling Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 公開サイトはすでに `phospho-signaling / second-messenger state` を独立 hidden-state として扱っており、`transcript or protein abundance != active phospho-controller` という方向性自体は正しかったです。
- しかし現状のままだと、`phosphosite-specific plasticity gate`、`compartmentalized second-messenger routing`、`single-site phospho-mutant causal intervention`、`human ex vivo phosphoproteome atlas` が、なお同じ `phospho evidence` として読めてしまいました。
- これは技術・自然科学の観点では粗すぎます。なぜなら、direct observable、空間スケール、時間軸、因果強度が違えば、主張できる ceiling もまったく変わるからです。

## 主要な批判点

### 1. `phospho evidence` が単一の証拠クラスのように見えていました

- 問題:
  - 旧版でも phospho-state の重要性は書かれていましたが、`何を直接見た研究か` がまだ十分に分解されていませんでした。
  - この構造だと、読者が `AMPA receptor phosphosite gating`、`local cAMP/PKA nanodomain routing`、`phospho-mutant memory rescue/impairment`、`human region atlas` を近い重みで読んでしまいます。
- 根拠:
  - Lee et al. (2003) と Tomita et al. (2005) は、異なる phosphosite が bidirectional synaptic plasticity の表現型を変えることを示しました。
  - Havekes et al. (2016) は、PDE4A5 の compartment-specific targeting が hippocampal LTP と long-term memory を変えることを示し、`global cAMP level` と `localized signalosome routing` を分ける必要を示しました。
  - Vierra et al. (2023) は、ER-plasma membrane junction が neuronal Ca2+-activated PKA signaling nanodomain を作ることを示しました。
  - Altas et al. (2024) は、mouse と human brain sample の両方で region-specific phosphorylation が Neuroligin-3 の excitatory / inhibitory synapse localization を変えることを示しました。
  - Rodriguez et al. (2025) は、HDAC3 S424 phospho-mimic / phospho-null mutation が adult / aging mouse の LTP と長期記憶を双方向に変えることを示しました。
  - Biswas et al. (2023) は human brain 12 region の ex vivo phosphoproteome atlas を提示しましたが、これは live in vivo phospho-controller の direct readout ではありません。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` に `phospho-signaling route card` を新設し、claim family / assay / compartment / timing / causal leverage / abstention boundary を分離しました。

### 2. `measured or perturbed` だけでは phospho-state の監査として弱すぎました

- 問題:
  - 旧 `verification.md` は、phospho-signaling 行で `measured / perturbed / externally calibrated / latent` という大枠は要求していました。
  - しかしこれだけでは、`phosphosite occupancy`、`kinase/phosphatase pathway intervention`、`local second-messenger imaging`、`region-level phosphoproteomics` の差が submission-side に固定されません。
- 根拠:
  - 同じ `phosphorylation was involved` でも、Lee et al. (2003) は phosphosite rule、Havekes et al. (2016) は compartment targeting、Altas et al. (2024) は region-specific localization、Rodriguez et al. (2025) は single-site causal mutant、Biswas et al. (2023) は atlas です。
  - これらを同じ disclosure で受けると、endpoint atlas が local controller に、局所 signalosome perturbation が whole-brain state evidence に昇格しやすくなります。
- 修正:
  - `verification.md` の maintenance-state budget 行を改稿し、claim family / assay-direct observable / spatial or compartment scope / timing window / causal leverage の記載を必須化しました。
  - さらに `phospho-signaling evidence also needs a route card` note を追加し、wiki 側の route card に接続しました。

### 3. 入口ページでの stop rule が transcription / sleep replay に比べて弱いままでした

- 問題:
  - `wbe_101.md` では phospho-state の重要性は説明されていましたが、entry-point wording はまだ `longer operating rule is in the wiki section` という紹介に留まっていました。
  - そのため、front door だけを読む読者には `phospho-signaling = another hidden variable` 以上の operational distinction が届き切りませんでした。
- 根拠:
  - transcription / sleep replay は既に `route card` という語で証拠クラスの分解が入口に出ていました。
  - phospho-state だけ route-card 化されていないと、ページ間で audit language の強さが揃いません。
- 修正:
  - `wbe_101.md` の note box を `Phospho-signaling evidence now gets its own route card` に改稿し、`phosphosite gate / compartmentalized routing / phospho-mutant intervention / human atlas` を入口で分けました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights` に phospho route-card 方針を追加
  - `unknown_points` を route-card 未整備から human-compatible external calibrator の未解決点へ更新
  - phospho section に Havekes et al. (2016), Altas et al. (2024), Rodriguez et al. (2025) を追加
  - `phospho-route-card` note box と route-card table を新設
- `verification.md`
  - `page_highlights` に phospho route-card 要件を追加
  - maintenance-state budget の phospho 行を route-card 粒度へ拡張
  - `phospho-signaling evidence also needs a route card` note box を追加
- `wbe_101.md`
  - phospho note box を route-card front door へ改稿
  - phospho evidence の証拠クラス差を entry point で明文化

## 外部依存タスク

- なし

## 参考文献

1. Lee H-K, Barbarosie M, Kameyama K, Bear MF, Huganir RL. Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. *Cell*. 2003. doi:10.1016/S0092-8674(03)00122-3
2. Tomita S, Stein V, Stocker TJ, Nicoll RA, Bredt DS. Bidirectional synaptic plasticity regulated by phosphorylation of stargazin-like TARPs. *Neuron*. 2005. doi:10.1016/j.neuron.2005.01.009
3. Havekes R, Park AJ, Tolentino RE, et al. Compartmentalized PDE4A5 signaling impairs hippocampal synaptic plasticity and long-term memory. *Journal of Neuroscience*. 2016. doi:10.1523/JNEUROSCI.0248-16.2016
4. Vierra NC, et al. Endoplasmic reticulum-plasma membrane junctions couple electrical activity to Ca2+-activated PKA signaling in neurons. *Nature Communications*. 2023. doi:10.1038/s41467-023-40930-6
5. Altas B, Tuffy LP, Patrizi A, et al. Region-specific phosphorylation determines Neuroligin-3 localization to excitatory versus inhibitory synapses. *Biological Psychiatry*. 2024. doi:10.1016/j.biopsych.2023.12.020
6. Rodriguez AC, Kramár EA, Augustynski AS, et al. HDAC3 Serine 424 phospho-mimic and phospho-null mutants bidirectionally modulate long-term memory formation and synaptic plasticity in the adult and aging mouse brain. *Journal of Neuroscience*. 2025. doi:10.1523/JNEUROSCI.1619-24.2025
7. Biswas D, et al. The landscape of the human brain phosphoproteome reveals region-specific phosphorylation events. *Journal of Proteome Research*. 2023. doi:10.1021/acs.jproteome.2c00244
