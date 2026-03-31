# Site Deepening Audit (2026-03-31, connectome timing-state / myelin route-card sync)

## 対象

- 主対象:
  - `wiki/connectome-is-not-enough.md`
- 同期対象:
  - `verification.md`
- 調査範囲:
  - 技術
  - 自然科学

## 今回この箇所を選んだ理由

- 2026-03-31 時点の公開サイトでは、`wiki/homeostatic-plasticity-and-maintenance-state.md`、`wbe_101.md`、`verification.md` の addendum 群で、`myelin / timing-state` はすでにかなり厳密に split されておりました。
- しかし、中心ページである `wiki/connectome-is-not-enough.md` の central table と augmentation table では、なお
  - `Delay / timing-state`
  - `fixed-delay baseline`
  - `human myelin or tract-speed readout`
  を比較的粗い一行で読める構造が残っておりました。
- この不整合を放置すると、読者は
  - animal causal literature が示す `learning / microgeometry / plasticity brake / recovery boundary`
  の分離と、
  - human proxy literature が示す `tract-speed versus typed myelin quantity`
  の分離を、
  再び `timing = one scalar delay` に圧縮できます。
- `connectome is not enough` は本サイトの中核ページですので、この圧縮余地は technical front door で止める必要がございました。

## web確認対象

- `https://doi.org/10.1038/s41593-023-01272-0`
- `https://doi.org/10.1038/s41467-025-56092-6`
- `https://doi.org/10.1002/mrm.29998`
- `https://doi.org/10.1016/j.neuroimage.2025.121456`
- `https://doi.org/10.1111/bpa.70010`
- `https://doi.org/10.1038/s41467-025-58604-w`

## 根拠付き批判

### 1. 中心ページの `Delay / timing-state` 一行は、同サイト内部で既に成立している `myelin evidence is not one class` ルールより弱うございました

- `wiki/homeostatic-plasticity-and-maintenance-state.md` では既に、
  - activity-dependent oligodendrogenesis / learning
  - node / internode / periaxonal timing-state control
  - plasticity-brake function
  - remyelination-to-function recovery
  - human quantity-defined myelin proxy families
  を別 object として扱っておりました。
- それにもかかわらず `wiki/connectome-is-not-enough.md` の central table が `Delay / timing-state` を一行で処理すると、読者は中心ページで再び
  - `timing = delay constant`
  - `human myelin paper = timing-state almost seen`
  と読めてしまいます。

### 2. timing-state の missing variable は「速い / 遅い」だけではなく、少なくとも `learning`, `microgeometry`, `plasticity brake`, `recovery boundary` に分かれます

- [Gibson et al. (2014)](https://doi.org/10.1126/science.1252304) と [McKenzie et al. (2014)](https://doi.org/10.1126/science.1254960) は、myelination が learning-linked controller 側の variable であることを示しました。
- [Seidl et al. (2015)](https://doi.org/10.1038/ncomms9073), [Dutta et al. (2018)](https://doi.org/10.1073/pnas.1811013115), [Cohen et al. (2020)](https://doi.org/10.1016/j.cell.2019.11.039), [Micheva et al. (2021)](https://doi.org/10.1093/cercor/bhab018), [Dubey et al. (2022)](https://doi.org/10.7554/eLife.73827) は、node/internode/periaxonal/PV-axon myelination が timing precision と synchrony を左右することを示しました。
- [Xin et al. (2024)](https://doi.org/10.1038/s41586-024-07853-8) は developmental myelination が plasticity brake になりうることを示しました。
- [Della-Flora Nunes et al. (2025)](https://doi.org/10.1038/s41467-025-56092-6) は、functional recovery が complete myelin restoration を意味しないことを示しました。

批判:

- したがって `timing-state` を one row として読むと、少なくとも
  - timing precision
  - learning-linked oligodendrogenesis
  - plasticity-permissive state
  - partial versus complete remyelination
  が混線いたします。

### 3. human timing-side evidence も one row ではございません

- [van Blooijs et al. (2023)](https://doi.org/10.1038/s41593-023-01272-0) は tract-scale transmission-speed route でございます。
- [Arshad et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/) は `MWF versus calibrated T1w/T2w` comparison route でございます。
- [Hagiwara et al. (2018)](https://doi.org/10.1038/s41598-018-28852-6) は `SyMRI / MTsat` comparison route でございます。
- [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は bilayer-sensitive proof-of-principle で、healthy volunteers 2 名の specialized route でございます。
- [Chen et al. (2025)](https://doi.org/10.1016/j.neuroimage.2025.121456) は orientation dependence 自体が route variable であることを示しました。
- [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) は qT1 remyelination-sensitive pathology route を示しました。
- [Genc et al. (2025)](https://doi.org/10.1038/s41467-025-58604-w) は developmental cortical microstructure と oligodendrocyte-related biology の alignment を示しましたが、histopathological confirmation を要すると述べています。

批判:

- これらは同じ `human myelin evidence` ではございません。
- `tract-speed`, `MWF`, `MT-family`, `bilayer-sensitive`, `qT1 remyelination-sensitive`, `developmental dMRI with ex vivo alignment` は quantity type も measurement burden も validation ceiling も異なります。
- よって `human myelin or tract-speed readout` を一行で済ませる verification rule は、現行サイトの他ページより停止線が甘うございました。

### 4. `verification.md` の latent-state error budget 行も、他の maintenance-state rows に比べて timing-state だけ要求が弱うございました

- `ionic`, `shared extracellular / electrical state`, `neuromodulatory`, `clearance / immune`, `bioenergetic` などは、すでに claim family や direct observable をかなり具体的に要求しております。
- それに対し `Timing-state / conduction support` 行は、修正前は
  - measured
  - externally calibrated
  - absorbed into a constant
  - left latent
  の開示だけで止まっておりました。

批判:

- これでは
  - どの timing claim family なのか
  - 何を直接見たのか
  - recovery boundary をどう扱うのか
  - human quantity type が何なのか
  が欠落し、他 family よりも verification 要求が弱くなります。

## 今回実行した変更

### `wiki/connectome-is-not-enough.md`

- `last_updated` を `2026-03-31` に更新しました。
- `page_highlights` の timing-state bullet を、`activity-dependent oligodendrogenesis / node-internode-periaxonal microgeometry / plasticity-brake / remyelination recovery / human typed proxy` の split が見える文言へ更新しました。
- `known_points` に、timing-state claims は `claim-family / structural-unit / recovery-boundary / human quantity type` disclosure が必要であることを追加しました。
- abstract の hidden-state 列挙を `conduction delay` ではなく `timing-state / conduction support` と書き換えました。
- central table の `Delay / timing-state` row を `Timing-state / conduction support` に改稿し、
  - learning
  - microgeometry
  - plasticity-brake state
  - remyelination state
  - human proxy misread
  を止める文言へ更新しました。
- Section 10 の heading を `Timing-state is not one scalar delay term` に変更しました。
- timing-state 節に
  - `learning / microgeometry / plasticity brake / recovery boundary / human proxy class`
  を分離する note-box
  - expanded human observability ceiling
  - new `timing-state / myelin route card`
  を追加しました。
- augmentation / ablation table の `+ timing-state / conduction audit` 行を、claim family・recovery boundary・human quantity type を要件に含む形へ強化しました。
- 参考文献一覧に今回前面化した
  - Xin 2024
  - Della-Flora Nunes 2025
  - Arshad 2017
  - Hagiwara 2018
  - Baadsvik 2024
  - Chen 2025
  - Galbusera 2025
  - Genc 2025
  を追加しました。

### `verification.md`

- `Latent-state error budget` の `Timing-state / conduction support` 行を、単なる measured/calibrated/constant/latent 開示から、
  - claim family
  - direct structural unit / observable
  - functional target
  - recovery / completeness boundary
  - human quantity type / proxy class
  を必須とする route-card 要件へ更新しました。

## 今回止めた誤読

- `timing-state = one scalar delay`
- `animal timing-microgeometry literature` と `human myelin proxy literature` は同じ階段
- `functional recovery after remyelination` = `healthy myelin-state fully restored`
- `human tract-speed estimate` = `per-axon timing-state readout`
- `myelin MRI exists` = `timing-state is almost observed`

## 検証予定

- `ruby scripts/export_github_wiki.rb`
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `bundle exec jekyll build`
- `git diff --stat`
- `git diff --check`

## external dependency tasks

- なし
  - 今回の作業は文献確認、public page 修正、export 同期、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. *Science*. 2014. https://doi.org/10.1126/science.1252304
2. McKenzie IA, et al. Motor skill learning requires active central myelination. *Science*. 2014. https://doi.org/10.1126/science.1254960
3. Seidl AH, Rubel EW, Barría A. Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. *Nat Commun*. 2015. https://doi.org/10.1038/ncomms9073
4. Dutta DJ, Woo DH, Lee PR, et al. Regulation of myelin structure and conduction velocity by perinodal astrocytes. *PNAS*. 2018. https://doi.org/10.1073/pnas.1811013115
5. Cohen CCH, Popovic MA, Klooster J, et al. Saltatory conduction along myelinated axons involves a periaxonal nanocircuit. *Cell*. 2020. https://doi.org/10.1016/j.cell.2019.11.039
6. Micheva KD, Kiraly M, Perez MM, Madison DV. Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. *Cereb Cortex*. 2021. https://doi.org/10.1093/cercor/bhab018
7. Dubey S, Kuschmitz S, Mezey SE, et al. Myelination synchronizes cortical oscillations by consolidating parvalbumin-mediated phasic inhibition. *eLife*. 2022. https://doi.org/10.7554/eLife.73827
8. van Blooijs D, de Haan AM, Renaud S, et al. Developmental trajectory of transmission speed in the human brain. *Nat Neurosci*. 2023. https://doi.org/10.1038/s41593-023-01272-0
9. Xin W, Kaneko M, Roth RH, et al. Oligodendrocytes and myelin limit neuronal plasticity in visual cortex. *Nature*. 2024. https://doi.org/10.1038/s41586-024-07853-8
10. Della-Flora Nunes G, Osso LA, Haynes JA, et al. Incomplete remyelination via therapeutically enhanced oligodendrogenesis is sufficient to recover visual cortical function. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-56092-6
11. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Hum Brain Mapp*. 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
12. Hagiwara A, Hori M, Kamagata K, et al. Myelin measurement: Comparison between simultaneous tissue relaxometry, magnetization transfer saturation index, and T1w/T2w ratio methods. *Sci Rep*. 2018. https://doi.org/10.1038/s41598-018-28852-6
13. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magn Reson Med*. 2024. https://doi.org/10.1002/mrm.29998
14. Chen M, Tang S, Chen H, et al. Orientation-independent magnetization transfer imaging of brain white matter. *NeuroImage*. 2025. https://doi.org/10.1016/j.neuroimage.2025.121456
15. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathol*. 2025. https://doi.org/10.1111/bpa.70010
16. Genc S, Ball G, Chamberland M, et al. MRI signatures of cortical microstructure in human development align with oligodendrocyte cell-type expression. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-58604-w
