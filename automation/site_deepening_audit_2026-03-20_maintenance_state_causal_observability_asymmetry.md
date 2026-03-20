# Site Deepening Audit (2026-03-20, Maintenance-State Causal / Observability Asymmetry)

## 対象

- 主対象: `wbe_101.md`
- 副対象: `faq.md`, `verification.md`, `wiki/homeostatic-plasticity-and-maintenance-state.md`

## 今回の選定理由

- 2026-03-20 時点で、公開サイトはすでに
  - `connectome-complete != state-complete`
  - `human proxy-rich evidence != state closure`
  - `maintenance-state は複数 family に分解して読む`
  という規則をかなり明確に持っていました。
- しかし front door にはなお一つ弱点が残っていました。`強い causal evidence がある hidden-state family` と `人で今見えている measurement route` の関係が、同じ表の中で対比されていなかったことです。
- その欠落により、読者は無意識に
  - rodent/local causal paper
  - human macro / perturbation proxy paper
  を頭の中で接続し、`responsible controller is basically measured in humans` と過大読みにしやすい構造でした。

## 根拠付き批判

### 1. 既存の human observability ladder は正しかったが、なお `causal relevance` とのズレを front door で一枚にしていませんでした

- 問題:
  - `wbe_101.md` と `faq.md` は human proxy class と route maturity をかなり厳密に分けていました。
  - しかし、読者が本当に誤読しやすいのは `human proxy row` 単独よりも、`rodent causal paper + human proxy paper` の頭内合成です。
- 根拠:
  - Hadzibegovic et al. (2025) は ACC engram neuron の early intrinsic excitability plasticity が remote memory formation / precision に permissive であることを rodent causal manipulation で示しました。
  - Terceros et al. (2026) は thalamo-cortical circuit における sequential transcriptional gates が memory stabilization に time-dependent causal role を持つことを示しました。
  - Dewa et al. (2025) と Bukalo et al. (2026) は astrocyte ensemble / astrocyte Ca2+ signaling が multiday stabilization や fear-memory representation を支えることを示しました。
  - 他方で human 側の前進は、Zrenner et al. (2018) の perturbation-conditioned excitability proxy、Hirschler et al. (2025) の CSF mobility MRI、Dagum et al. (2026) の sleep-linked clearance proxy といった別種の object です。
- 批判:
  - したがって front door では `human proxy got richer` だけでは不十分で、`causal relevance ladder` と `human observability ladder` が別軸であること自体を明示する必要がありました。

### 2. maintenance-state の一部 family では、因果証拠と human readout の spatial unit が大きくずれています

- 問題:
  - 既存ページは state family を多数列挙していましたが、`どの family でズレが特に大きいか` は一目で分かる形になっていませんでした。
- 根拠:
  - Relative excitability / allocation controller:
    - Hadzibegovic et al. (2025) は local rodent engram manipulation。
    - Human route は Huber et al. (2013), Kuhn et al. (2016), Fehér et al. (2026), Zrenner et al. (2018) の perturbation-conditioned proxy。
  - Transcriptional stabilization gate:
    - Santoni et al. (2024), Terceros et al. (2026) は rodent causal gate。
    - comparable whole-brain in vivo human route は現状なし。
  - Astrocyte ensemble state:
    - Williamson et al. (2025), Dewa et al. (2025), Bukalo et al. (2026) は rodent causal ensemble studies。
    - direct living-human astrocyte-ensemble route は現状なし。
  - Clearance / immune support:
    - Kim et al. (2025) は meningeal-lymphatics-microglia axis の causal link。
    - Human route は Hirschler et al. (2025) と Dagum et al. (2026) の macro support-state proxy。
- 批判:
  - これらは all evidence improving という一本の progress bar ではありません。
  - family ごとに `causal paper が何を固定したか` と `human route が何をまだ固定していないか` を並べる必要がありました。

### 3. reference integrity にも小さいが重要な乱れがありました

- 問題:
  - `Hadzibegovic et al.` の年が一部公開ページで `2026` になっていました。
- 根拠:
  - PubMed / Nature Communications の記載は `2025 Dec 5`、`Nat Commun. 2025;17(1):291.` です。
- 批判:
  - この種の deepening は表現だけでなく citation integrity まで含みます。
  - 年次がずれていると、再検証時の参照整合性が落ちます。

## 今回実行した変更

- `wbe_101.md`
  - front matter の `page_highlights` / `known_points` に `causal evidence ladder != human observability ladder` を追加しました。
  - 新規 anchor `#causal-observability-asymmetry` を追加しました。
  - `state family / strongest causal evidence / best human route / safe reading` の crosswalk table を追加しました。
  - Hadzibegovic et al. (2025) を references に追加しました。
- `faq.md`
  - front matter の `page_highlights` / `known_points` に同 asymmetry rule を追加しました。
  - Q2d に short correction paragraph を追加し、`WBE 101` の新規 anchor へ接続しました。
- `verification.md`
  - front matter に `bridge assumptions must be disclosed` ルールを追加しました。
  - `maintenance-state error budget` 内へ `causal relevance and human observability must be bridged, not fused` note を追加しました。
  - Hadzibegovic et al. の年を `2025` へ修正しました。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - Hadzibegovic et al. の年を `2025` へ修正しました。

## 外部依存で保留

- human same-family bridge validation
  - 担当者: 実験系・高分解能計測系の研究者
  - 前提条件: 同一 state family について、rodent/local causal controller と living-human proxy route を同一 translation chain で較正する設計
  - 完了条件: `which family is causal` と `which family is observed in humans` の橋渡し仮定を benchmark / external calibration で検証できること

## 参考文献

1. Hadzibegovic S, Zhu L, Ginger M, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025;17(1):291.
   - https://doi.org/10.1038/s41467-025-66975-3
2. Santoni G, Astori S, Leleu M, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024;385(6705):eadg9982.
   - https://doi.org/10.1126/science.adg9982
3. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026;649(8099):1254-1263.
   - https://doi.org/10.1038/s41586-025-09774-6
4. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
5. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
6. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
7. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
8. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
9. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
   - https://doi.org/10.1016/j.cell.2025.02.022
