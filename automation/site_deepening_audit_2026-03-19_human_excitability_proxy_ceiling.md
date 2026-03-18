# Site Deepening Audit (2026-03-19, Human Excitability / Maintenance Proxy Ceiling)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `wbe_101.md`
- 副対象: `index.md`
- 副対象: `faq.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、human maintenance-state evidence を `layered evidence` として読む方向性自体はかなり整っておりました。
- しかし page 間を突き合わせると、`verification.md` と `wiki/homeostatic-plasticity-and-maintenance-state.md` がすでに区別していた
  - `perturbation-conditioned maintenance / plasticity proxy`
  - `state-gated perturbation proxy`
  を、`wiki/measurement-stack-and-claim-ceiling.md` と front door 側が十分に明示しておりませんでした。
- この不整合は技術・自然科学の観点で問題です。なぜなら、human 側の TMS-EEG / PAS / EEG-state-gated evidence を独立した proxy class として固定しないと、読者が `human で current excitability controller がかなり直接見えてきた` と誤読しやすくなるからです。
- 加えて、AIS の代表論文 Grubb & Burrone (2010) の DOI が `10.1038/nature09160` と `10.1038/nature09185` でページ間不一致を起こしており、証跡追跡性を下げておりました。

## 根拠付き批判

### 1. `human maintenance-state evidence` の class rule が front door と measurement-stack で揃っていませんでした

- 問題:
  - `verification.md` では human 側 evidence を `structural scaffold / regional density proxy / macro biochemical / energetic / ionic / thermal / myelin / support proxy / perturbation-conditioned proxy` と class-labeled submission する方針がすでに導入されていました。
  - 一方 `wiki/measurement-stack-and-claim-ceiling.md` と `wbe_101.md` は、human ladder を説明しつつも、TMS-EEG / PAS / EEG-state-gated routes を front-door row として固定していませんでした。
- 根拠:
  - Huber et al. (2013) は wake の長さに応じて human cortical excitability が変化することを示しました。
  - Kuhn et al. (2016) は sleep deprivation と recovery sleep が homeostatic / associative plasticity の効き方を変えることを示しました。
  - Fehér et al. (2026) は nap が同種の recalibration を起こしうることを示しました。
  - Zrenner et al. (2018) は EEG-defined excitability state に応じて TMS-induced plasticity efficacy が変わることを示しました。
- 批判:
  - これらは `current AIS geometry` や `cell-specific recovery controller` の direct readout ではございません。
  - にもかかわらず独立 class として front door で固定しないと、`human excitability evidence` が `human excitability mechanism readout` に滑りやすくなります。

### 2. `perturbation-conditioned proxy` と `macro proxy` は同じ error term を減らしていませんでした

- 問題:
  - 旧 front door は biochemical / energetic / ionic / thermal / myelin / clearance proxy を並べていましたが、human perturbation routes を別 class として前に出していませんでした。
- 根拠:
  - Huber / Kuhn / Fehér は `sleep-wake or nap conditioned plasticity/excitability response` を押し上げます。
  - Zrenner は `state-gated causal modulation of plasticity efficacy` を押し上げます。
  - これらは sodium MRI や MRS thermometry のような tissue-property proxy と異なり、`conditioned response of a perturbational assay` を見ております。
- 批判:
  - よって `macro maintenance proxy` と `perturbation-conditioned excitability proxy` を同列に畳み込むのは粗すぎます。
  - 必要なのは measurement class ごとに `what is advanced` と `what is still latent` を分けることでした。

### 3. Grubb & Burrone (2010) の DOI 不一致は根拠追跡性を壊していました

- 問題:
  - `faq.md` と `glossary.md` が `10.1038/nature09185` を参照していました。
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` は `10.1038/nature09160` を参照していました。
- 根拠:
  - Nature 論文 `Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability` の DOI は `10.1038/nature09160` です。
- 批判:
  - これは単なる細部ではございません。hidden-state の論点を深掘りするページで DOI が揺れると、読者は一次文献の追跡で止まります。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - human maintenance-state ladder に
    - `Human sleep-homeostasis / plasticity proxy`
    - `Human state-gated perturbation proxy`
    の 2 行を追加しました。
  - section intro と `Site rule for human proxy classes` を改稿し、`perturbation-conditioned maintenance / state-gated perturbation proxy` を明示しました。
  - 参考文献へ Huber (2013), Kuhn (2016), Zrenner (2018), Fehér (2026) を追加しました。
- `wbe_101.md`
  - front-door human observability ladder に同じ 2 行を追加しました。
  - `Do not promote perturbation-conditioned human routes to direct controller readout` の note を追加し、AIS / channel / controller readout ではないことを固定しました。
  - 参考文献へ Huber (2013), Kuhn (2016), Zrenner (2018), Fehér (2026) を追加しました。
- `index.md`
  - human observability ladder の紹介文へ perturbation-conditioned sleep-homeostasis / plasticity proxies と EEG-state-gated perturbation routes を加えました。
- `faq.md`
  - human evidence ladder の説明を front door と整合する形へ改稿しました。
  - Grubb & Burrone (2010) DOI を `10.1038/nature09160` へ修正しました。
  - 参考文献へ Huber (2013), Kuhn (2016), Zrenner (2018), Fehér (2026) を追加しました。
- `glossary.md`
  - Grubb & Burrone (2010) DOI を `10.1038/nature09160` へ修正しました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・evidence class rule・引用整合の修正で完結しております。

## 参考文献

1. Grubb MS, Burrone J. Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. *Nature*. 2010;465(7301):1070-1074.
   - https://doi.org/10.1038/nature09160
2. Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
3. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
4. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
5. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
6. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
7. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
8. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
9. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
10. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
