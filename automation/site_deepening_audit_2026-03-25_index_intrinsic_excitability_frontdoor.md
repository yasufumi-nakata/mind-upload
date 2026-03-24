# Site Deepening Audit (2026-03-25, landing page intrinsic-excitability front door)

## 対象

- 主対象: `index.md`
- 派生対象: `summary_booklet.md`

## 今回この箇所を選んだ理由

- 2026-03-25 時点で、`intrinsic excitability / homeostatic set point` 自体の route card は `wiki/homeostatic-plasticity-and-maintenance-state.md`、`wbe_101.md`、`verification.md` で既に整備されておりました。
- しかし最初の入口である `index.md` には、`SV2A`、`myelin`、`ionic`、`neuromodulatory`、`astrocyte`、`clearance` などの front-door stop line はある一方、`intrinsic excitability` だけは専用 note がなく、latent-state error budget への抽象参照に留まっておりました。
- これは技術・自然科学の観点で弱点です。なぜなら、`intrinsic excitability` は
  - allocation bias
  - AIS / ion-channel-state plasticity
  - firing-rate set point / recovery controller
  - living-human perturbation-conditioned proxy
  という別の inferential object を含むのに、landing page でその分離が見えないと、読者が「excitability evidence がある = 現在の excitability landscape が測れた」と誤読しうるからです。

## 根拠付き批判

### 1. landing page だけが `intrinsic excitability` を one-bucket のまま通しておりました

- 観察:
  - `index.md` の front matter は `post-transcriptional RNA`、`ionic`、`neuromodulatory`、`electrical-state`、`astrocyte` などには `is not one class` を明示しておりました。
  - その一方で `intrinsic excitability` は `latent-state error budget` にのみ現れ、専用の front-door stop line がありませんでした。
- なぜ問題か:
  - `intrinsic excitability` は単一の measurement class ではございません。
  - `Yiu et al. (2014)` は学習直前の relative excitability と memory-trace allocation を扱っております。
  - `Hadzibegovic et al. (2025)` は early engram-excitability plasticity を扱っております。
  - `Benoit et al. (2025)` は AIS dynamics という局所構造・生理 route を扱っております。
  - `Hengen et al. (2016)` は firing-rate homeostasis / recovery control を扱っております。
- 批判:
  - これらを landing page がひとまとめにしていると、allocation、AIS microstructure、set-point recovery が同じ evidence class に見えてしまいます。

### 2. human 側は direct readout ではなく proxy route なのに、その停止線が landing page で見えませんでした

- 観察:
  - human 側 excitability は `wbe_101.md` と `verification.md` ではすでに `living-human perturbation-conditioned proxy` として扱われておりました。
  - しかし `index.md` では同じ論点が front-door note として露出しておらず、human observability ceiling との接続が弱い状態でした。
- 根拠:
  - `Huber et al. (2013)` は time-awake 依存の human cortical excitability を示しました。
  - `Kuhn et al. (2016)` と `Fehér et al. (2026)` は sleep / nap による human cortex の homeostatic / associative plasticity recalibration を示しました。
  - `Zrenner et al. (2018)` は real-time EEG-defined state により TMS-induced plasticity efficacy が変わることを示しました。
- 批判:
  - これらは重要な human route ですが、AIS geometry や ion-channel distribution や cell-specific recovery controller の direct readout ではございません。
  - 入口でこの線を引かないと、`human excitability evidence exists` が `human excitability state is directly measured` に滑ります。

### 3. 入口で止めないと、他の hidden-state route card 体系との整合性が崩れます

- 観察:
  - サイトは March 2026 の再監査で、measurement class の過圧縮を front door で止める方針へ明確に舵を切っております。
  - それにもかかわらず `intrinsic excitability` だけ note-box 不在のままだと、page 間で「どこまで front-door 扱いなのか」が揺れます。
- 批判:
  - これは単なる見栄えの問題ではなく、読者が landing page にある stop line を site-wide rule と読む以上、`intrinsic excitability` の omission は public-spec inconsistency です。

## 今回実行した変更

- `index.md`
  - `last_updated` を `2026-03-25` に更新しました。
  - front matter の `page_highlights` に `intrinsic-excitability evidence is not one class` を追加しました。
  - `known_points` に、allocation bias / AIS / recovery controller / human proxy が同一の evidence class ではないことを追加しました。
  - landing page note-box `If You Are Treating Intrinsic Excitability As One Solved Row` を新設しました。
  - note 内で `Yiu (2014)`, `Hadzibegovic (2025)`, `Benoit (2025)`, `Hengen (2016)`, `Huber (2013)`, `Kuhn (2016)`, `Fehér (2026)`, `Zrenner (2018)` を distinct route として明示しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成し、front matter 変更を冊子へ同期します。

## 外部依存で保留

- なし
  - 今回の作業は、landing page の記述修正、監査記録、要約冊子同期で完結できます。

## 参考文献

1. Yiu AP, Rashid AJ, Josselyn SA. Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. *Neuron*. 2014;83(3):722-735.
   - https://doi.org/10.1016/j.neuron.2014.07.017
2. Hadzibegovic S, Zhu L, Ginger M, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025;17:291.
   - https://doi.org/10.1038/s41467-025-66975-3
3. Benoit CM, Ganea DA, Paricio-Montesinos R, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025;29(3):535-542.
   - https://doi.org/10.1038/s41593-025-02152-5
4. O'Leary T, Williams AH, Franci A, Marder E. Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. *Neuron*. 2014;82(4):809-821.
   - https://doi.org/10.1016/j.neuron.2014.04.002
5. Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016;165(1):180-191.
   - https://doi.org/10.1016/j.cell.2016.01.046
6. Huber R, Maki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
7. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
8. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
9. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
