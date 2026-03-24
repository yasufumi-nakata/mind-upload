# Site Deepening Audit (2026-03-25, Intrinsic Excitability / Homeostatic-Set-Point Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 2026-03-25 時点の公開サイトは、`intrinsic excitability / homeostatic set point` を hidden-state family としては明確に扱えておりました。
- しかし page 間を突き合わせると、`transcription`、`post-transcriptional RNA`、`phospho-signaling`、`proteostasis`、`ECM / PNN`、`myelin`、`ionic`、`bioenergetic` などに追加済みの `route card` が、`intrinsic excitability` にだけ未整備でした。
- この欠落は技術・自然科学の観点で問題です。なぜなら、現行本文だけでは
  - allocation / engram-bias
  - AIS / ion-channel-state plasticity
  - homeostatic set-point / recovery control
  - living-human perturbation-conditioned proxy
  という別々の inferential object が、`excitability evidence` という 1 バケツに再圧縮されうるからです。
- 既存の `automation/site_deepening_audit_2026-03-19_human_excitability_proxy_ceiling.md` は human proxy ceiling の是正、
  `automation/site_deepening_audit_2026-03-20_maintenance_state_causal_observability_asymmetry.md` は rodent causal evidence と human observability の非対称性の是正に効いておりました。
- それでもなお、submission rule と front door に対応する `公開ルールの型` がないため、読者は `excitability` の語だけで claim family を混同しえました。今回はその欠陥を埋める作業です。

## 根拠付き批判

### 1. `intrinsic excitability` が複数の claim family を含むのに、公開ルールは one-bucket のままでした

- 問題:
  - サイト本文は `intrinsic excitability / homeostatic set point` を latent-state family として列挙していました。
  - しかし `verification.md` に route-card rule がなく、`wbe_101.md` にも front-door stop line がありませんでした。
- 根拠:
  - Yiu et al. (2014) は、学習直前の relative excitability が memory-trace recruitment を左右することを示しました。
  - Hadzibegovic et al. (2025) は、neocortical engram neuron の early intrinsic excitability plasticity が memory formation / precision に必要であることを示しました。
  - Grubb & Burrone (2010), Kuba et al. (2010), Jamann et al. (2021), Fréal et al. (2023), Benoit et al. (2025) は、AIS position / Na+ channel distribution / AIS plasticity という別の route を示しました。
  - O'Leary et al. (2014) と Hengen et al. (2016) は、homeostatic set point / recovery controller の route を示しました。
- 批判:
  - これらは同じ evidence class ではございません。
  - allocation bias を示す論文、AIS microstructure を示す論文、recovery-controller を示す論文を、`excitability evidence` と一括りにすると、どの error term が減ったのか見えなくなります。

### 2. human 側の前進は direct controller readout ではなく perturbation-conditioned proxy なのに、その区別を route-card field として固定していませんでした

- 問題:
  - 既存サイトは human 側で Huber / Kuhn / Fehér / Zrenner を参照し、wake-sleep / nap / EEG-state dependence を説明していました。
  - しかし route-card field がないため、`human excitability evidence` が `human excitability controller readout` に滑る余地が残っていました。
- 根拠:
  - Huber et al. (2013) は、time awake に応じて human cortical excitability が変化することを示しました。
  - Kuhn et al. (2016) は、sleep が homeostatic plasticity と associative plasticity を recalibrate することを示しました。
  - Fehér et al. (2026) は、nap でも同種の recalibration が起こりうることを示しました。
  - Zrenner et al. (2018) は、real-time EEG-defined state に応じて TMS-induced plasticity efficacy が変わることを示しました。
- 批判:
  - これらは living-human route として重要ですが、AIS geometry、ion-channel distribution、cell-specific recovery controller の direct observable ではございません。
  - したがって `human proxy class` と `abstention boundary` を route card の必須項目にしない限り、human 側 observability ceiling が曖昧なまま残ります。

### 3. `time axis` を固定しないと、fast permissive change と slow recovery controller が同じ意味に見えてしまいます

- 問題:
  - intrinsic excitability には、learning 前の allocation bias、minutes-to-hours の AIS reconfiguration、hours-to-days の firing-rate recovery、momentary EEG-state gating が混在します。
  - 既存サイトはこの違いを本文では説明していましたが、submission rule として固定していませんでした。
- 根拠:
  - Benoit et al. (2025) は associative fear learning 中の AIS dynamics を示しました。
  - Jamann et al. (2021) は sensory input に応じた rapid AIS scaling を示しました。
  - Hengen et al. (2016) は sleep/wake regime に依存した firing-rate homeostasis を示しました。
  - Zrenner et al. (2018) は momentary EEG state に依存した plasticity efficacy を示しました。
- 批判:
  - これらを同一の `excitability state` とだけ書くと、読者は short-lived permissive state と longer-horizon return destination を区別できません。
  - route card に `time axis / intervention window` を要求しない限り、claim ceiling を正しく止められません。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `intrinsic-excitability-route-card` を新設しました。
  - route-card field として
    - `Claim family`
    - `Physiological locus`
    - `Direct observable`
    - `Time axis / intervention window`
    - `Human proxy class`
    - `Abstention boundary`
    を追加しました。
  - `Why this route card is necessary here` note を追加し、allocation / AIS / recovery / human proxy の非同一性を一次文献で固定しました。
  - `last_updated` を `2026-03-25` に更新しました。
- `wbe_101.md`
  - front-door note `Intrinsic-excitability evidence now gets its own route card` を追加しました。
  - `page_highlights` に one-bucket compression を止める bullet を追加しました。
  - `last_updated` を `2026-03-25` に更新しました。
- `verification.md`
  - `page_highlights` に `intrinsic-excitability / homeostatic-set-point` route card を追加しました。
  - `2026-03-25 addendum: intrinsic-excitability evidence also needs a route card` を追加し、submission-side の stop rule を明文化しました。
  - references に Hengen (2016), Huber (2013), Kuhn (2016), Fehér (2026), Zrenner (2018) を追加しました。
  - `last_updated` を `2026-03-25` に更新しました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・submission rule・front-door explanation・監査記録の更新で完結しております。

## 参考文献

1. Yiu AP, et al. Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. *Neuron*. 2014;83(3):722-735.
   - https://doi.org/10.1016/j.neuron.2014.07.017
2. Hadzibegovic S, Zhu L, Ginger M, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025;17:291.
   - https://doi.org/10.1038/s41467-025-66975-3
3. Grubb MS, Burrone J. Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. *Nature*. 2010;465(7301):1070-1074.
   - https://doi.org/10.1038/nature09160
4. Kuba H, Oichi Y, Ohmori H. Presynaptic activity regulates Na+ channel distribution at the axon initial segment. *Nature*. 2010;465(7301):1075-1078.
   - https://doi.org/10.1038/nature09087
5. Jamann N, Dannehl D, Lehmann N, et al. Sensory input drives rapid homeostatic scaling of the axon initial segment in mouse barrel cortex. *Nature Communications*. 2021;12:23.
   - https://doi.org/10.1038/s41467-020-20232-x
6. Fréal A, Jamann N, Ten Bos J, et al. Sodium channel endocytosis drives axon initial segment plasticity. *Science Advances*. 2023;9(37).
   - https://doi.org/10.1126/sciadv.adf3885
7. Benoit CM, Ganea DA, Paricio-Montesinos R, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025;29(3):535-542.
   - https://doi.org/10.1038/s41593-025-02152-5
8. O'Leary T, Williams AH, Franci A, Marder E. Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. *Neuron*. 2014;82(4):809-821.
   - https://doi.org/10.1016/j.neuron.2014.04.002
9. Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016;165(1):180-191.
   - https://doi.org/10.1016/j.cell.2016.01.046
10. Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
11. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
12. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
13. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
