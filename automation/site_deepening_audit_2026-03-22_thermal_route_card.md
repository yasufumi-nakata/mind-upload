# Site Deepening Audit (2026-03-22, Thermal Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 運用ルール反映: `verification.md`
- 入口反映: `wbe_101.md`, `index.md`

## 今回の選定理由

- サイトはすでに `thermal-state` を hidden-state family としては扱っていましたが、`myelin`, `ionic`, `bioenergetic`, `astrocyte`, `clearance` ほどには route-card 化されていませんでした。
- そのため読者が、`slice / local physiology`, `field-potential confound`, `local cooling / warming timing perturbation`, `device-heating artifact`, `brain-state / neurovascular proxy`, `human MRS thermometry` を同じ `thermal evidence` として圧縮できてしまう余地が残っていました。
- これは技術・自然科学の観点で危険です。なぜなら、それぞれが直接見ている thermal object も、減らしている不確実性項も、到達する claim ceiling も違うからです。

## 根拠付き批判

### 1. 温度依存の operating-point physiology と field-potential confound は同じ inferential object ではありません

- 問題:
  - 既存サイトは `thermal-state matters` とまでは書けていましたが、`temperature changes synaptic / membrane operating point` と `temperature can fake or mask the recorded readout` が front door でまだ分離されていませんでした。
- 根拠:
  - Hardingham & Larkman (1998) は rat visual-cortex slice で excitatory synaptic transmission の reliability が温度依存であることを示しました。
  - Van Hook (2020) は visual thalamus で warming が release probability, synaptic depression, membrane conductance, spike output をまとめて変えることを示しました。
  - Moser et al. (1993) は dentate field potentials が brain temperature に強く追従し、learning-specific change を mask しうることを示しました。
- 批判:
  - したがって `temperature affected the system` という 1 行では粗すぎます。
  - operating point を変えた論文と readout confound を警告した論文では、submission 時に開示すべき項目が違います。

### 2. Thermal timing perturbation と device-heating artifact は別に止める必要があります

- 問題:
  - thermal topic が timing-state の脚注のように扱われると、`local cooling changed sequence timing` と `the perturbation itself heated the tissue` が同じ意味に読まれます。
- 根拠:
  - Long & Fee (2008) は songbird motor pathway の局所 cooling で neural sequence timing が系統的に伸張することを示しました。
  - Reig et al. (2010) は cortical slow / fast rhythms が温度で変調されることを示しました。
  - Owen et al. (2019) は in vivo optogenetic manipulations 自体に thermal constraints があり、光刺激が神経操作とは別に tissue heating を導入しうることを示しました。
- 批判:
  - 前二者は `temperature as perturbation / controller`、後者は `temperature as artifact introduced by the tool` です。
  - この区別を明示しないと、thermal manipulation paper を causal controller evidence と artifact warning のどちらとして読んでいるのか不明になります。

### 3. Brain-state proxy / neurovascular route と local thermal controller route は別です

- 問題:
  - thermal evidence を 1 クラスに圧縮すると、`temperature tracks state` という論文を `local thermal mechanism was identified` へ過読しやすくなります。
- 根拠:
  - Boorman et al. (2023) は in vivo で bidirectional な brain-temperature alteration が neurovascular responses を大きく変えることを示しました。
  - Lazopulo et al. (2025) は mouse で brain temperature が brain state と oscillatory activity の proxy になりうることを示しました。
- 批判:
  - しかし、proxy であることと controller identity が分かったことは別です。
  - したがって `brain temperature covaries with state` は、そのまま `the local thermal controller was measured` を意味しません。

### 4. Human thermal routes は重要ですが、なお macro proxy class に留まります

- 問題:
  - 既存サイトは human thermometry を `macro thermal proxy` と呼んでいましたが、`which macro route?` が粗く、task-linked mapping と healthy-adult thermometry を同じ一行で読めてしまいました。
- 根拠:
  - Rzechorzek et al. (2022) は human brain の 4D temperature map と daily rhythm を示しました。
  - Rogala et al. (2024) は working-memory performance と BOLD relation の文脈で local temperature variation を評価しました。
  - Tan et al. (2025) は healthy adults の frontal-lobe temperature を <sup>1</sup>H-MRS thermometry で測定し、年齢差と brain-body temperature gradient を報告しました。
- 批判:
  - これらは living-human thermal observability の前進ですが、なお `cell-specific microtemperature`, `synapse-specific heating burden`, `local thermal controller`, `branch- or bouton-level thermal sensitivity` を直接は見ていません。
  - したがって human thermometry を timing-state completion や local thermal-state ground truth に昇格させるのは不適切です。

### 5. Verification 側の thermal rule が弱く、提出仕様としてはまだ止まりませんでした

- 問題:
  - 旧 `verification.md` の thermal row は、`brain temperature / heating logs / thermometry を測ったか` という有無確認にはなっていましたが、何の thermal claim family を扱っているかまでは固定していませんでした。
- 根拠:
  - 上記の一次文献群は、少なくとも `local physiology`, `field-potential confound`, `timing perturbation`, `device-heating artifact`, `brain-state proxy`, `human macro thermometry` を分けないと claim ceiling が混ざることを示しています。
- 批判:
  - したがって verification rule は、`測ったかどうか` だけでなく `何を thermal evidence と呼んでいるのか` を提出物に書かせる必要がありました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `last_updated` を `2026-03-22` に更新しました。
  - thermal section を拡張し、human thermometry を `human brain thermometry / task-linked thermal mapping` に更新しました。
  - `#thermal-route-card` を追加し、以下の field を固定しました。
    - claim family
    - direct thermal observable
    - spatial / preparation regime
    - driver / perturbation route
    - time window
    - functional target
    - human proxy class / acquisition burden
    - abstention boundary
  - references に Van Hook (2020), Reig et al. (2010), Owen et al. (2019), Boorman et al. (2023), Lazopulo et al. (2025), Rogala et al. (2024), Tan et al. (2025) を追加しました。
- `verification.md`
  - `last_updated` を `2026-03-22` に更新しました。
  - `page_highlights` の thermal bullet を route-card 仕様へ更新しました。
  - maintenance-state error budget の `Thermal-state` 行を `route card` 粒度に拡張しました。
  - thermal addendum を `thermal evidence also needs a route card` へ更新し、evidence-class compression を block する文に差し替えました。
  - references に Owen et al. (2019), Rogala et al. (2024), Tan et al. (2025) を追加しました。
- `wbe_101.md`
  - `last_updated` を `2026-03-22` に更新しました。
  - `page_highlights` の thermal bullet を `evidence is not one class` へ更新しました。
  - front-door note `Thermal evidence now gets its own route card` を追加しました。
  - human observability ladder の thermal row を `human brain thermometry / task-linked thermal mapping` に更新しました。
  - measurement-stack caution で human thermal routes の ceiling を Rzechorzek / Rogala / Tan まで明示しました。
  - references に Owen et al. (2019), Rogala et al. (2024), Tan et al. (2025) を追加しました。
- `index.md`
  - `last_updated` を `2026-03-22` に更新しました。
  - top-page thermal note を `temperature was constant` から `thermal evidence was treated as one solved row` へ更新しました。

## 外部依存で保留

- same-subject benchmark for calibrating human thermal proxies against local thermal targets
  - 担当者: external human neuroimaging / electrophysiology benchmark designers
  - 前提条件: same-subject design linking MRS thermometry or task-linked thermal mapping with externally validated local thermal perturbation or controller targets
  - 完了条件: the site can point to a public benchmark showing which human thermal proxy reduces which local thermal uncertainty term

## 参考文献

1. Hardingham NR, Larkman AU. The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. *The Journal of Physiology*. 1998;507(1):249-256.
   - https://doi.org/10.1111/j.1469-7793.1998.249bu.x
2. Moser E, Mathiesen I, Andersen P. Association between brain temperature and dentate field potentials in exploring and swimming rats. *Science*. 1993;259(5099):1324-1326.
   - https://doi.org/10.1126/science.8446900
3. Long MA, Fee MS. Using temperature to analyse temporal dynamics in the songbird motor pathway. *Nature*. 2008;456:189-194.
   - https://doi.org/10.1038/nature07448
4. Reig R, Mattia M, Compte A, Belmonte C, Sanchez-Vives MV. Temperature modulation of slow and fast cortical rhythms. *Journal of Neurophysiology*. 2010;103(3):1253-1261.
   - https://doi.org/10.1152/jn.00890.2009
5. Van Hook MJ. Temperature effects on synaptic transmission and neuronal function in the visual thalamus. *PLoS One*. 2020;15(4):e0232451.
   - https://doi.org/10.1371/journal.pone.0232451
6. Owen SF, Liu MH, Kreitzer AC. Thermal constraints on in vivo optogenetic manipulations. *Nature Neuroscience*. 2019;22:1061-1065.
   - https://doi.org/10.1038/s41593-019-0422-3
7. Boorman LW, Harris SS, Shabir O, et al. Bidirectional alterations in brain temperature profoundly modulate spatiotemporal neurovascular responses in-vivo. *Communications Biology*. 2023;6:185.
   - https://doi.org/10.1038/s42003-023-04542-6
8. Lazopulo A, Emmenegger Y, Đukanović N, Hoekstra MMB, et al. Brain temperature as proxy for brain state and oscillatory activity in the mouse. *Scientific Reports*. 2025;15:21175.
   - https://doi.org/10.1038/s41598-025-21175-3
9. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022;145(6):2031-2048.
   - https://doi.org/10.1093/brain/awab466
10. Rogala J, et al. Local variation in brain temperature explains gender-specificity of working memory performance. *Frontiers in Human Neuroscience*. 2024;18:1398034.
   - https://doi.org/10.3389/fnhum.2024.1398034
11. Tan Y, Liu W, Li Y, et al. Measurement of Healthy Adult Brain Temperature Using <sup>1</sup>H Magnetic Resonance Spectroscopy Thermometry. *Clinical Neuroradiology*. 2025;35(1):159-164.
   - https://doi.org/10.1007/s00062-024-01467-3
