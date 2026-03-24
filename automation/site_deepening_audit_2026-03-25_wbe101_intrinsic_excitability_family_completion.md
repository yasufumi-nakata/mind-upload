# Site Deepening Audit (2026-03-25, WBE 101 intrinsic-excitability family completion)

## 対象

- 主対象: `wbe_101.md`
- 同期対象: `summary_booklet.md`

## 今回この箇所を選んだ理由

- `index.md`、`verification.md`、`perspective.md`、`wiki/homeostatic-plasticity-and-maintenance-state.md` は、2026-03 の再監査で `intrinsic excitability` を
  - relative excitability / allocation
  - AIS / ion-channel-state plasticity
  - firing-rate set point / recovery controller
  - living-human perturbation-conditioned proxy
  の少なくとも4系統へ分ける規律をかなり明示できていました。
- しかし初心者入口である `wbe_101.md` だけは、front matter と front-door note と因果-観測非対称テーブルの3箇所で、`AIS / channel-state` 系が落ちたままでした。
- この omission は表現上の細部ではありません。`WBE 101` は最初に読まれる public spec なので、ここで `AIS / channel-state` が見えないと、読者は `allocation bias` と `recovery controller` と human proxy を「excitability evidence」の1行として読んでしまいます。

## 根拠付き批判

### 1. `wbe_101.md` だけが `intrinsic excitability` を site-wide rule より粗く記述していました

- 観察:
  - `wbe_101.md` の `page_highlights` は、更新前には `allocation / engram bias`、`homeostatic return control`、`living-human perturbation-conditioned proxies` の3つしか前面に出していませんでした。
  - 同ページの front-door note も、`Hadzibegovic (2025)`、`Hengen (2016)`、`Huber/Kuhn/Fehér/Zrenner` の3系統だけを挙げ、`AIS / ion-channel-state` の route family を省いていました。
  - さらに「The strongest causal papers and the best human routes are not the same ladder」の表でも、excitability 側は `Relative excitability / allocation controller` の1行しかありませんでした。
- 批判:
  - これは site 内部の public-spec inconsistency です。
  - route card 側が `claim family` と `physiological locus` を要求しているのに、最初の入口だけがそれを落としていると、最も誤読しやすい page が最も粗い規則を提示することになります。

### 2. AIS / ion-channel-state route の脱落は科学的に弱い圧縮でした

- 根拠:
  - `Yiu et al. (2014)` と `Hadzibegovic et al. (2025)` は、memory allocation / early engram excitability を扱っています。
  - `Grubb & Burrone (2010)` は activity-dependent AIS relocation を示しました。
  - `Kuba et al. (2010)` は presynaptic activity に応じた Na+ channel distribution を示しました。
  - `Jamann et al. (2021)` は sensory input に応じた rapid AIS scaling を示しました。
  - `Fréal et al. (2023)` は sodium-channel endocytosis による AIS plasticity を示しました。
  - `Benoit et al. (2025)` は associative fear learning 中の AIS dynamics を示しました。
- 批判:
  - これらは `allocation bias` でも `recovery controller` でもありません。
  - したがって `AIS / channel-state` を前面の entry text から落とすと、「どこが変わった excitability なのか」が不明になります。
  - これは単なる文献不足ではなく、inferential object の取り違えを誘う omission です。

### 3. human excitability proxy の安全な読み方も、AIS 不在だと弱まります

- 根拠:
  - `Huber et al. (2013)`、`Kuhn et al. (2016)`、`Fehér et al. (2026)`、`Zrenner et al. (2018)` は、wake/sleep/history-dependent or EEG-state-dependent の human perturbation-conditioned proxy を与えます。
  - `O'Leary et al. (2014)` と `Hengen et al. (2016)` は、activity set point と recovery controller の別系統を与えます。
- 批判:
  - human 側 proxy の ceiling を正しく読むには、「proxy が何を見ていないか」を entry point で見せる必要があります。
  - `AIS / channel-state` を落としたままだと、読者は human perturbation route を `excitability route のほぼ全部` と誤認しやすくなります。
  - それでは `human proxy exists` が `controller is nearly observed` に滑ります。

## 今回実行した変更

- `wbe_101.md`
  - `page_highlights` を更新し、`intrinsic excitability` を4系統で読む rule を front matter に反映しました。
  - `known_points` に、allocation / AIS / firing-rate homeostasis / human proxy が別 object であることを追加しました。
  - `state-completeness` 節の冒頭に、`relative excitability`、`AIS / channel-state plasticity`、`firing-rate set point / recovery control` を分ける一次文献群を追加しました。
  - front-door note `Intrinsic-excitability evidence now gets its own route card` を改稿し、4系統の route family を明示しました。
  - `causal-observability-asymmetry` 節の table を 1 行から 3 行へ展開し、
    - allocation controller
    - AIS / channel-state route
    - firing-rate set point / recovery controller
    を別々に記述しました。
  - 参考文献に `Yiu (2014)`, `Grubb & Burrone (2010)`, `Kuba (2010)`, `O'Leary (2014)`, `Jamann (2021)`, `Fréal (2023)`, `Benoit (2025)` を追加しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成し、WBE 101 の front-door 修正を冊子側へ同期します。

## 外部依存で保留

- なし
  - 今回の作業はサイト本文、監査記録、冊子再生成で完結できます。

## 参考文献

1. Yiu AP, Rashid AJ, Josselyn SA. Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. *Neuron*. 2014;83(3):722-735.
   - https://doi.org/10.1016/j.neuron.2014.07.017
2. Grubb MS, Burrone J. Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. *Nature*. 2010;465(7301):1070-1074.
   - https://doi.org/10.1038/nature09160
3. Kuba H, Oichi Y, Ohmori H. Presynaptic activity regulates Na+ channel distribution at the axon initial segment. *Nature*. 2010;465(7301):1075-1078.
   - https://doi.org/10.1038/nature09087
4. O'Leary T, Williams AH, Franci A, Marder E. Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. *Neuron*. 2014;82(4):809-821.
   - https://doi.org/10.1016/j.neuron.2014.04.002
5. Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016;165(1):180-191.
   - https://doi.org/10.1016/j.cell.2016.01.046
6. Hadzibegovic S, Zhu L, Ginger M, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025;17:291.
   - https://doi.org/10.1038/s41467-025-66975-3
7. Jamann N, Dannehl D, Lehmann N, et al. Sensory input drives rapid homeostatic scaling of the axon initial segment in mouse barrel cortex. *Nature Communications*. 2021;12:23.
   - https://doi.org/10.1038/s41467-020-20232-x
8. Fréal A, Jamann N, Ten Bos J, et al. Sodium channel endocytosis drives axon initial segment plasticity. *Science Advances*. 2023;9(37):eadf3885.
   - https://doi.org/10.1126/sciadv.adf3885
9. Benoit CM, Ganea DA, Paricio-Montesinos R, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025;29(3):535-542.
   - https://doi.org/10.1038/s41593-025-02152-5
10. Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
11. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
12. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
13. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
