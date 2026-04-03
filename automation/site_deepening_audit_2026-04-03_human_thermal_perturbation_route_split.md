# Site Deepening Audit (2026-04-03, Human Thermal Perturbation Route Split)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- front door 反映: `wbe_101.md`, `index.md`, `perspective.md`, `faq.md`
- verification rule 反映: `verification.md`

## 今回の選定理由

- 直近の監査ログを確認したところ、thermal topic はすでに `route card` 化されていましたが、human lane の整理がまだ浅いままでした。
- 現状の公開文面では、human thermal evidence が実質的に `macro thermometry / task-linked mapping` に寄り過ぎており、`human perturbation-conditioned thermal route` が front door に十分出ていませんでした。
- これは技術・自然科学の観点で重要です。なぜなら、受動的 macro thermometry と、熱摂動条件下での motor / executive / neurovascular response は、直接観測している object も、因果の読み方も、残る latent variable も違うからです。

## 根拠付き批判

### 1. Human thermal evidence を passive macro thermometry だけで代表させるのは、現在の一次文献に対して粗すぎます

- 問題:
  - 既存サイトは human thermal route を主として `Rzechorzek / Rogala / Tan (2025)` の文脈で扱っていました。
  - しかしこの並べ方だと、`human thermal evidence = macro thermometry` と読めてしまいます。
- 根拠:
  - Rzechorzek et al. (2022) は 4D brain-temperature map と daily rhythm の route です。
  - Rogala et al. (2024) は working-memory 文脈の task-linked thermal mapping route です。
  - Tan et al. (2025) は healthy-adult frontal-lobe thermometry と brain-body gradient の route です。
- 批判:
  - これらは重要ですが、いずれも基本的には `passive or task-linked macro thermometry` です。
  - したがって、human thermal lane 全体をこれだけで代表させると、human 側に存在する perturbation-conditioned route が隠れます。

### 2. Human systemic heat perturbation は passive thermometry と別 row にすべきです

- 問題:
  - severe heat exposure 下での human brain-temperature study を passive thermometry と同じ row に入れると、`temperature was mapped` と `temperature was pushed and functional consequences were jointly measured` が同じ意味に見えます。
- 根拠:
  - Tan et al. (2024) は healthy participants 11 名で exertional または passive hyperthermia を用い、MRI-based brain thermometry, cerebral perfusion, task-based brain activity を合わせて測定しました。
  - PubMed abstract では、motor cortex の brain temperature 上昇、bilateral motor cortical activity の抑制、passive hyperthermia 下での executive function 低下が示されています。
- 批判:
  - これは `passive map` ではなく `systemic heat-perturbation route` です。
  - しかし同時に、local thermal controller identity や cell-specific microtemperature を与えるものでもありません。
  - よって `macro thermal proxy` とも `local controller readout` とも違う、独立した human perturbation-conditioned row として扱うべきです。

### 3. Human focal cooling route も、macro thermometry とは別の inferential object です

- 問題:
  - intraoperative focal cooling を macro thermometry と一緒にしてしまうと、human thermal evidence の中で `where temperature sits` と `how tissue responds across temperature ranges` の差が見えなくなります。
- 根拠:
  - Inoue et al. (2025) は refractory epilepsy 患者 13 名で、brain temperature, ECoG, cerebral hemoglobin concentration を同時に測る multimodality probe を用いて focal brain cooling を評価しました。
  - PubMed / ScienceDirect の abstract では、18-28°C と 18°C 未満で hemoglobin response の符号が変わる非線形な neurovascular modulation が示されています。
  - 追加の先行ヒト文献として Smyth et al. (2015) は intraoperative active/passive focal cooling で human neocortex の depth-dependent cooling を示しています。
- 批判:
  - これは `human passive thermometry` ではなく、`human intraoperative focal-cooling perturbation route` です。
  - ただし対象は特殊な surgical setting に限られ、routine whole-brain observability には直結しません。
  - よってここも独立 row とし、claim ceiling を bounded human perturbation route に止める必要があります。

### 4. したがって human thermal lane は少なくとも 2 つに分けないと claim ceiling が混ざります

- 分けるべき row:
  - `human passive / task-linked macro thermometry`
  - `human perturbation-conditioned thermal routes`
- 違い:
  - direct observable
    - 前者は macro temperature map / task-linked voxel temperature / frontal-lobe thermometry
    - 後者は perturbation 下の measured brain temperature plus motor / executive / neurovascular response
  - driver
    - 前者は passive observation または task-linked acquisition
    - 後者は systemic heat exposure または focal cooling
  - abstention boundary
    - 前者も後者も local thermal controller identity は与えない
    - ただし前者は perturbation leverage が弱く、後者は regime transfer と routine observability が弱い

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - human thermal paragraph に Tan et al. (2024) と Inoue et al. (2025) を追加しました。
  - `thermal-route-card` の claim family, driver / perturbation route, human route class を更新しました。
  - human observability ladder で thermal row を 2 分割しました。
  - addendum 側の proxy-family wording を `macro thermal / perturbation-conditioned thermal proxy family` に更新しました。
- `wbe_101.md`
  - front-door thermal note を更新し、human passive / task-linked macro thermometry と human perturbation-conditioned thermal routes を分離しました。
  - human observability table の thermal row を 2 分割しました。
  - measurement-ceiling paragraph に Tan et al. (2024), Inoue et al. (2025) を追加しました。
- `verification.md`
  - thermal addendum を更新し、human passive / task-linked macro thermometry と human perturbation-conditioned thermal routes を別 class と明記しました。
  - human maintenance evidence class list の thermal label を更新しました。
  - thermal-state audit の比較対象に `human perturbation-conditioned thermal route` を追加しました。
- `perspective.md`
  - human support-state route split paragraph を更新しました。
  - human-route table の thermal row を 2 分割しました。
- `index.md`
  - front-door highlights の thermal proxy family 表現を更新しました。
  - thermal note を April 2026 pass として書き換え、human perturbation-conditioned thermal routes を追加しました。
- `faq.md`
  - thermal-state paragraph に human perturbation-conditioned thermal routes を追加し、cell-specific ground truth ではないことを明確化しました。

## 外部依存で保留

- なし

## 参考文献

1. Hardingham NR, Larkman AU. The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. *J Physiol*. 1998;507(1):249-256.
   - https://doi.org/10.1111/j.1469-7793.1998.249bu.x
2. Moser E, Mathiesen I, Andersen P. Association between brain temperature and dentate field potentials in exploring and swimming rats. *Science*. 1993;259(5099):1324-1326.
   - https://doi.org/10.1126/science.8446900
3. Long MA, Fee MS. Using temperature to analyse temporal dynamics in the songbird motor pathway. *Nature*. 2008;456:189-194.
   - https://doi.org/10.1038/nature07448
4. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022;145(6):2031-2048.
   - https://doi.org/10.1093/brain/awab466
5. Rogala J, et al. Local variation in brain temperature explains gender-specificity of working memory performance. *Front Hum Neurosci*. 2024;18:1398034.
   - https://doi.org/10.3389/fnhum.2024.1398034
6. Tan Y, Liu W, Li Y, et al. Measurement of Healthy Adult Brain Temperature Using 1H Magnetic Resonance Spectroscopy Thermometry. *Clin Neuroradiol*. 2025;35(1):159-164.
   - https://doi.org/10.1007/s00062-024-01467-3
7. Tan XR, Stephenson MC, Alhadad SB, et al. Elevated brain temperature under severe heat exposure impairs cortical motor activity and executive function. *J Sport Health Sci*. 2024;13(2):233-244.
   - https://doi.org/10.1016/j.jshs.2023.09.001
8. Inoue T, Nomura S, Yamakawa T, et al. Intraoperative evaluation using a multimodality probe of temperature-dependent neurovascular modulation during focal brain cooling. *Clin Neurophysiol*. 2025;173:31-42.
   - https://doi.org/10.1016/j.clinph.2025.02.262
9. Smyth MD, Han RH, Yarbrough CK, et al. Temperatures achieved in human and canine neocortex during intraoperative passive or active focal cooling. *Ther Hypothermia Temp Manag*. 2015;5(2):95-103.
   - https://doi.org/10.1089/ther.2014.0025
