# Site Deepening Audit (2026-03-29, literature intrinsic-excitability human split)

## 対象

- 主対象: `mind_uploading_papers.md`
- 主対象: `research_harvest_50.md`

## 今回この箇所を選んだ理由

- `index.md`、`verification.md`、`wbe_101.md`、`wiki/homeostatic-plasticity-and-maintenance-state.md` では、2026-03 の再監査により `intrinsic excitability` を
  - allocation / early engram bias
  - AIS / ion-channel-state plasticity
  - homeostatic set-point / recovery control
  - human local clinical-unit allocation
  - human sleep-homeostasis / plasticity proxy
  - human state-gated perturbation proxy
  として分ける規律がかなり明示されていました。
- しかし、実際に文献入口として読まれる `mind_uploading_papers.md` と `research_harvest_50.md` は、この human-side split を front door へまだ十分に反映できておりませんでした。
- その結果、読者が `human excitability evidence exists` を `one common human excitability meter exists` と誤読する余地が残っていました。

## 根拠付き批判

### 1. literature hub だけが site-wide rule より粗い excitability 読みを残していました

- 観察:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` では、`Tallman et al. (2025)` を human hippocampal single-unit allocation route、`Huber et al. (2013)` / `Kuhn et al. (2016)` / `Fehér et al. (2026)` を sleep-history or plasticity-recalibration proxy、`Zrenner et al. (2018)` / `Khatri et al. (2025)` を state-gated perturbation proxy として明示済みでした。
  - それに対し `mind_uploading_papers.md` の technical addendum / shortlist と `research_harvest_50.md` の human-observability table は、human intrinsic-excitability evidence をまだ一段粗く読ませる余地を残していました。
- 批判:
  - これは public reading rule の不整合でございます。
  - 最初に読まれやすい literature front door が粗いままだと、core page で止めた overread が archive entry point で再導入されます。

### 2. human intrinsic-excitability evidence は一次文献上も単一オブジェクトではありません

- 根拠:
  - `Tallman et al. (2025)` は、てんかん患者海馬の single-unit 記録で、encoding 時の relative firing increase と episodic-memory sparse coding の関連を示しました。これは local clinical-unit allocation-related readout であり、論文自体も firing を excitability の直接定義とは置いておりません。
  - `Huber et al. (2013)` は time awake に応じた human cortical excitability の変化を示しました。
  - `Kuhn et al. (2016)` と `Fehér et al. (2026)` は、sleep / nap が human cortex の homeostatic / associative plasticity を recalibrate することを示しました。
  - `Zrenner et al. (2018)` と `Khatri et al. (2025)` は、EEG-defined あるいは personalized state に応じて TMS-induced plasticity efficacy や corticospinal response が変わることを示しました。
- 批判:
  - これらは spatial unit も direct observable も perturbation burden も異なります。
  - よって、これらを 1 行の `human excitability` として圧縮すると、local clinical-unit route、sleep-history proxy、state-gated perturbation proxy の違いが消えます。
  - その圧縮は human route の claim ceiling を誤読させます。

### 3. human 側の route split が見えないと controller-side causality と observability が再び混ざります

- 根拠:
  - `Hadzibegovic et al. (2025)` は early intrinsic-excitability plasticity と memory formation / precision を示しました。
  - `Benoit et al. (2025)` は associative fear learning 中の AIS dynamics を示しました。
  - `Hengen et al. (2016)` は firing-rate homeostasis が sleep / wake regime に依存することを示しました。
- 批判:
  - つまり animal causal literature 側でも `intrinsic excitability` は allocation、AIS / channel-state、set-point / recovery control に分かれています。
  - それにもかかわらず human literature hub が `human excitability evidence` を一枚岩として残すと、human proxy が controller-side causality にかなり近いもののように誤読されます。
  - これは一次文献が許す ceiling を超えています。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `If you want the 2026 technical addendum first` に、human intrinsic-excitability lane 自体が
    - Tallman の local clinical single-unit allocation route
    - Huber / Kuhn / Fehér の sleep-history / plasticity-recalibration proxy
    - Zrenner / Khatri の state-gated perturbation proxy
    に分かれることを追加しました。
  - `Human intrinsic-excitability evidence is already split across three human routes` の note box を追加し、front door だけ読んでも human-side split が見えるようにしました。
  - technical route table の `maintenance-state / mechanistic boundary` 行を改稿し、animal-side split と human-side split を同じ行で可視化しました。
  - shortlist の `Maintenance-state family split` 行も同じ taxonomy へ同期しました。
- `research_harvest_50.md`
  - U3 row の maintenance-state family split を allocation / AIS / set-point / human subroutes まで見える形へ更新しました。
  - `Read human measurement papers as their own evidence class` に、human intrinsic-excitability route split を追記しました。
  - 同 table に
    - Tallman の local clinical-unit allocation row
    - Huber / Kuhn / Fehér の sleep-homeostasis / plasticity proxy row
    - Zrenner / Khatri の state-gated perturbation proxy row
    を追加し、safe calibrator role と still-not-closed を明示しました。
  - `Read maintenance-state papers as more than support background` に、human intrinsic-excitability papers は one common meter ではないことを追記しました。

## 外部依存で保留

- なし
  - 今回の修正は repo 内の本文更新、監査メモ、build 検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Tallman CW, Siler SN, Lee H, et al. Neuronal allocation and sparse coding of episodic memories in the human hippocampus. *Scientific Reports*. 2025;15:21967.
   - https://doi.org/10.1038/s41598-025-21967-7
2. Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
3. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
4. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
5. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
6. Khatri UU, Pulliam K, Manesiya M, Vieyra Cortez M, Millán J del R, Hussain SJ. Personalized whole-brain activity patterns predict human corticospinal tract activation in real-time. *Brain Stimulation*. 2025;18(1):64-76.
   - https://doi.org/10.1016/j.brs.2024.12.1193
7. Hadzibegovic S, Zhu L, Ginger M, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025;16:291.
   - https://doi.org/10.1038/s41467-025-66975-3
8. Benoit CM, Ganea DA, Paricio-Montesinos R, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025;28:535-542.
   - https://doi.org/10.1038/s41593-025-02152-5
9. Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016;165(1):180-191.
   - https://doi.org/10.1016/j.cell.2016.01.046
