# Site Deepening Audit (2026-03-21, Ionic / Chloride Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 運用ルール反映: `verification.md`
- 入口反映: `wbe_101.md`, `index.md`

## 今回の選定理由

- サイトはすでに `ionic milieu / chloride homeostasis` を重要 hidden-state として扱っていましたが、`myelin`, `bioenergetics`, `astrocyte`, `clearance` ほどには route-card 化されていませんでした。
- そのため読者が、`chloride set point`, `interstitial-ion state switch`, `perisynaptic K+ clearance`, `sleep-wake-history-dependent E_GABAA shift`, `human pathology`, `human sodium MRI / CSF assay` を同じ `ionic evidence` として圧縮できてしまう余地が残っていました。
- これは技術・自然科学の観点で危険です。なぜなら、それぞれが減らしている不確実性項と claim ceiling が違うからです。

## 根拠付き批判

### 1. Chloride set point と interstitial-ion state switch は同じ inferential object ではありません

- 問題:
  - 既存サイトは `ionic milieu / chloride homeostasis` を 1 行で重要視していましたが、`何を直接見たのか` が front door でまだ粗く、local chloride set point と global state-transition route が分離されていませんでした。
- 根拠:
  - Glykys et al. (2014) は local impermeant anions が neuronal chloride concentration を決めることを示しました。
  - Ding et al. (2016) は interstitial K+, Ca2+, Mg2+, H+ の変更で cortical activity と sleep/wake state が変わることを示しました。
  - Forsberg et al. (2022) は healthy humans で wake / sleep / sleep deprivation に伴う CSF potassium change を示しました。
- 批判:
  - したがって `ionic state matters` だけでは粗すぎます。local chloride set point と interstitial-ion state switch は別の claim family です。

### 2. Transporter-state regulation と perisynaptic K+ clearance は別です

- 問題:
  - KCC2 を含む論文群が一括して `chloride transporter evidence` に見えていました。
- 根拠:
  - Heubl et al. (2017) は GABA_A receptor activity が Cl-sensitive WNK1 を介して KCC2 surface expression を素早く変えることを示しました。
  - Byvaltsev et al. (2023) は KCC2 reverse mode が perisynaptic K+ clearance を担い、glutamatergic transmission と LTP を変えることを示しました。
- 批判:
  - 前者は transporter-state regulation、後者は perisynaptic K+ handling です。同じ `KCC2 evidence` として扱うと、どの局所変数が制約されたのかを見失います。

### 3. Sleep-wake-history-dependent E_GABAA shift は sleep amount や generic excitability ではありません

- 問題:
  - 既存サイトでは ionic topic が sleep architecture と excitability の間に埋もれやすく、`recent waking changes chloride-linked inhibitory regime` という論点が front door で弱い状態でした。
- 根拠:
  - Alfonsa et al. (2025) は recent waking に伴う depolarized E_GABAA が cortical pyramidal neurons の residual depolarization と LTP induction を変えることを示しました。
- 批判:
  - したがって `sleep affected plasticity` を `sleep happened` や `excitability changed` だけで読むのは不十分です。chloride-linked inhibitory regime 自体を別 family として開示すべきです。

### 4. Human pathology route と healthy-human proxy route は同じ観測階層ではありません

- 問題:
  - Human evidence が一見あるように見えても、それが pathology tissue なのか healthy-human in vivo proxy なのかが front door ではまだ固定されていませんでした。
- 根拠:
  - Huberfeld et al. (2007) は human temporal-lobe epilepsy tissue で depolarizing GABA と altered KCC2 expression を示しました。
  - Qian et al. (2012) は 7T sodium MRI を、Qian et al. (2025) は mono-/bi-T2 sodium separation を healthy humans で示しました。
  - Forsberg et al. (2022) は healthy humans で CSF ion concentrations の circadian / sleep-linked change を示しました。
- 批判:
  - しかし human pathology tissue, sodium MRI, and CSF assays は同じ evidence class ではありません。どれも local chloride homeostasis ground truth には達していませんが、何を proxy しているかは違います。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights`, `known_points`, `unknown_points` に ionic route-card 規則を追加しました。
  - human observability table の ionic row を `human sodium MRI / ionic proxy` へ更新しました。
  - `human CSF ionic assay` 行を追加し、Forsberg et al. (2022) を healthy-human macro ionic proxy として分離しました。
  - `#ionic-route-card` を新設し、以下の field を固定しました。
    - claim family
    - biological regime / spatial scale
    - direct ionic observable
    - perturbation / controller route
    - functional target
    - human observability / external calibration
    - abstention boundary
  - references に Forsberg et al. (2022), Byvaltsev et al. (2023), Alfonsa et al. (2025), Qian et al. (2025) を追加しました。
- `verification.md`
  - `page_highlights` に ionic route-card rule を追加しました。
  - latent-state error budget の `Ionic milieu / chloride homeostasis` 行を route-card 粒度へ拡張しました。
  - maintenance-state error budget の `Ionic / chloride state` 行を route-card 粒度へ拡張しました。
  - 既存の ionic addendum を `ionic / chloride evidence also needs a route card` へ更新し、evidence class compression を block する文に差し替えました。
  - references に Forsberg et al. (2022), Byvaltsev et al. (2023), Alfonsa et al. (2025), Qian et al. (2025) を追加しました。
- `wbe_101.md`
  - `page_highlights` に ionic evidence is not one class を追加しました。
  - entry-level note `Ionic / chloride evidence now gets its own route card` を追加しました。
  - references に Forsberg et al. (2022), Byvaltsev et al. (2023), Alfonsa et al. (2025) を追加しました。
- `index.md`
  - landing-page highlight を更新しました。
  - `If You Are Treating Ionic Evidence As One Solved Row` note を追加し、front door で ionic evidence の圧縮誤読を止めました。

## 外部依存で保留

- same-subject benchmark for calibrating healthy-human ionic proxies against local inhibitory-state targets
  - 担当者: external human neuroimaging / electrophysiology benchmark designers
  - 前提条件: same-subject design linking sodium MRI or CSF ion proxy with externally validated local chloride / E_GABAA / transporter targets
  - 完了条件: the site can point to a public benchmark showing which human ionic proxy reduces which chloride-related uncertainty term

## 参考文献

1. Glykys J, Dzhala V, Egawa K, et al. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014;343(6171):670-675.
   - https://doi.org/10.1126/science.1245423
2. Heubl M, Zhang J, Pressey JC, et al. GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. *Nature Communications*. 2017;8:1776.
   - https://doi.org/10.1038/s41467-017-01749-0
3. Ding F, O'Donnell J, Xu Q, Kang N, Goldman N, Nedergaard M. Changes in the composition of brain interstitial ions control the sleep-wake cycle. *Science*. 2016;352(6285):550-555.
   - https://doi.org/10.1126/science.aad4821
4. Huberfeld G, Wittner L, Clemenceau S, et al. Perturbed chloride homeostasis and GABAergic signaling in human temporal lobe epilepsy. *Journal of Neuroscience*. 2007;27(37):9866-9873.
   - https://doi.org/10.1523/JNEUROSCI.2761-07.2007
5. Forsberg M, Olsson M, Seth H, et al. Ion concentrations in cerebrospinal fluid in wakefulness, sleep and sleep deprivation in healthy humans. *Journal of Sleep Research*. 2022;31(3):e13522.
   - https://doi.org/10.1111/jsr.13522
6. Simonnet C, Sinha M, Goutierre M, Moutkine I, Daumas S, Poncer J-C. Silencing KCC2 in mouse dorsal hippocampus compromises spatial and contextual memory. *Neuropsychopharmacology*. 2023;48(7):1067-1077.
   - https://doi.org/10.1038/s41386-022-01480-5
7. Byvaltsev E, Behbood M, Schleimer J-H, et al. KCC2 reverse mode helps to clear postsynaptically released potassium at glutamatergic synapses. *Cell Reports*. 2023;42(8):112934.
   - https://doi.org/10.1016/j.celrep.2023.112934
8. Alfonsa H, Chakrabarty A, Vyazovskiy VV, Akerman CJ. Sleep-wake-related changes in intracellular chloride regulate plasticity at glutamatergic cortical synapses. *Current Biology*. 2025;35(6):1373-1381.e3.
   - https://doi.org/10.1016/j.cub.2025.01.050
9. Qian Y, Zhao T, Zheng H, Weimer J, Boada FE. High-resolution sodium imaging of human brain at 7 T. *Magnetic Resonance in Medicine*. 2012;68(1):227-233.
   - https://doi.org/10.1002/mrm.23225
10. Qian Y, Lin Y-C, Chen X, Ge Y, Lui YW, Boada FE. Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. *Scientific Reports*. 2025;15:27427.
   - https://doi.org/10.1038/s41598-025-07800-1
