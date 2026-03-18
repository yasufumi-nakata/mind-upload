# Site Deepening Audit (2026-03-18, FAQ / Glossary Technical Front Door Alignment)

## 対象

- 主対象: `faq.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-17 から 2026-03-18 にかけて、公開サイトの中核ページでは `hidden-state`、`Specificity & Shortcut Card`、`vascular-state / CVR audit`、`maintenance-state` の記述がかなり厳密になっていました。
- その一方で、入口として最も読まれやすい `faq.md` と `glossary.md` はそれぞれ `2026-03-16`、`2026-03-14` の更新で止まっており、読者が短答と短語だけを読んだ場合に、サイト全体の現在の厳格さよりも古い理解へ戻される構造が残っていました。
- この弱点は技術・自然科学の観点で重要です。なぜなら、入口ページが `connectome + cell type` の不足、`high score` の shortcut 問題、`BOLD / fNIRS` の vascular ceiling を十分に前景化しなければ、後段の厳密な verification rule が読者に届く前に誤解が固定されるからです。

## 根拠付き批判

### 1. 旧 FAQ の `connectome is not enough` は、2026-03 時点の hidden-state 分解より粗すぎました

- 問題:
  - `faq.md` の Q2c は、connectome と cell type で足りない要素として主に sleep / myelin / glia を前に出していました。
  - しかし、直近の site-wide 更新で独立 state class として整理された `AIS / excitability`、`transcription / chromatin`、`local proteostasis / synaptic tagging`、`ECM / PNN`、`ionic milieu / chloride homeostasis`、`timing-state` が入口短答に落ちていませんでした。
- 根拠:
  - Gouwens et al. (2021) は同一 transcriptomic type 内でも morpho-electric spread があることを示しました。
  - Grubb & Burrone (2010) は activity-dependent AIS relocation を示しました。
  - Santoni et al. (2024) は chromatin plasticity が memory trace formation への neuronal eligibility を規定することを示しました。
  - Govindarajan et al. (2011) は protein-synthesis-dependent LTP の統合単位として dendritic branch を示しました。
  - Frischknecht et al. (2009) は ECM が AMPA receptor mobility と short-term plasticity を拘束することを示しました。
  - Glykys et al. (2014) は local impermeant anions が neuronal chloride concentration を拘束することを示しました。
  - Seidl et al. (2015) は node / internode geometry が conduction timing を調整することを示しました。
- 批判:
  - したがって、入口短答が `sleep / myelin / glia` 付近に留まるのは、現在のサイトが到達している hidden-state decomposition より甘いです。
  - front door では、`connectome-complete = structural scaffold only` をより広い state family の不在として短くても固定する必要がありました。

### 2. 旧 FAQ は `high score != target-specific neural readout` を独立の短答として持っていませんでした

- 問題:
  - 既存 FAQ は language prior や direct validation には触れていました。
  - しかし、`eye movement / EMG / uninstructed movement / fingerprint / acquisition distribution` を `score inflation route` としてまとめて止める短答がありませんでした。
- 根拠:
  - Musall et al. (2019) は、trial-by-trial neural dynamics が uninstructed movement に強く支配されうることを示しました。
  - Mostert et al. (2018) は、visual working memory decode に eye-movement confound が残りうることを示しました。
  - McFarland et al. (2005) は、early BCI session の performance に EMG が寄与しうることを示しました。
  - Chaibub Neto et al. (2019) は、repeated measures で identity confounding を design で制御しないと error が過小評価されることを示しました。
  - Xu et al. (2020) は、cross-dataset EEG decoding で recording distribution の差が generalization を崩すことを示しました。
- 批判:
  - そのため、旧 FAQ は `a high score came out` を `the target neural variable was read` と読ませないための最短防波堤としては不足していました。
  - 入口段階で `Specificity & Shortcut Card` の必要性を直接示すべきでした。

### 3. 旧 FAQ は `BOLD / fNIRS != neural difference` を hemodynamic gate として固定していませんでした

- 問題:
  - 現行サイトの core pages では `vascular-state / CVR audit` が既に明文化されていました。
  - しかし FAQ には、group difference や cross-day difference を BOLD / fNIRS 振幅からそのまま neural difference と読ませない短答がありませんでした。
- 根拠:
  - Murphy et al. (2011) は、vascular reactivity covariate が BOLD group analysis を改善することを示しました。
  - Williams et al. (2023) は、task BOLD magnitude が cortex 全域で CVR に強く対応することを示しました。
  - Yücel et al. (2015) は、fNIRS で short-separation regression が superficial confound を減らすことを示しました。
  - Epp et al. (2025) は、BOLD change と oxygen-metabolism change が逆向きになりうることを示しました。
- 批判:
  - したがって、FAQ がこの点を入口で止めないと、site-wide に導入済みの hemodynamic ceiling が front door で失われます。
  - 技術系読者向けには、`hemodynamic-limited difference` という棄権語を FAQ にも入れる必要がありました。

### 4. 旧 Glossary は、現在の verification language を受け止める短語基盤が不足していました

- 問題:
  - `glossary.md` は decode/emulate, observability/identifiability までは整っていました。
  - しかし、`claim ceiling`、`hidden state`、`Specificity & Shortcut Card`、`subject / session fingerprint`、`acquisition-distribution shortcut`、`vascular-state / CVR audit`、`maintenance-state`、`timing-state` といった、2026-03 の public rules を読むための基礎語彙が欠けていました。
- 根拠:
  - これらの語は、上記の一次文献が示す実際の自然科学的 boundary を短く運ぶために必要です。
  - つまり、shortcut route, vascular transfer state, timing-state, maintenance-state の自然科学的限界が本文に追加されても、glossary 側で短語が未整備なら読者はその差を再び `uncertainty` 一語へ潰してしまいます。
- 批判:
  - glossary の役割は「本論に戻るまでの短語の橋」です。
  - そこに新しい verification terms が無いのは、情報設計上の欠陥であり、技術・自然科学の境界条件を front door で保持できていませんでした。

## 今回実行した変更

- `faq.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points / wiki links を、`hidden-state`、`shortcut`、`vascular-state` を前面化する形へ更新
  - 入口 note と導線 table を改稿し、3 つの技術的 guardrail を明示
  - 新規短答 `Q1c` を追加し、`high score != target-specific neural readout` を front door で固定
  - 新規短答 `Q1d` を追加し、`BOLD / fNIRS != neural difference without vascular-state / CVR audit` を front door で固定
  - `Q2c` を改稿し、connectome 外に残る state family を current site policy に合わせて拡張
  - references を追加・修正し、shortcut / vascular / hidden-state 側の一次文献を front door から辿れるようにした
- `glossary.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points / wiki links を現行 verification language に合わせて更新
  - note box を追加し、`claim ceiling`、`hidden state`、`vascular-state / CVR audit` などが詰まった場合の復帰ルートを明示
  - 新節 `Verification and Hidden-State Terms` を追加し、上記の front-door 用語群を短義化
  - measurement / implementation / open-science の既存定義を修正し、`fMRI`、`fNIRS`、`Connectome`、`Model card` を current site rule に整合化
  - references を追加し、new glossary terms の背後にある一次文献を補強

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と監査メモの改稿で完結しております。

## 参考文献

1. Gouwens NW, et al. Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. *Nature*. 2021.
   - https://doi.org/10.1038/s41586-020-2907-3
2. Grubb MS, Burrone J. Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. *Nature*. 2010.
   - https://doi.org/10.1038/nature09185
3. Santoni G, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024.
   - https://doi.org/10.1126/science.adg9982
4. Govindarajan A, Israely I, Huang S-Y, Tonegawa S. The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. *Neuron*. 2011.
   - https://doi.org/10.1016/j.neuron.2010.12.008
5. Frischknecht R, Heine M, Perrais D, Seidenbecher CI, Choquet D, Gundelfinger ED. Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. *Nature Neuroscience*. 2009.
   - https://doi.org/10.1038/nn.2338
6. Glykys J, Dzhala V, Egawa K, et al. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014.
   - https://doi.org/10.1126/science.1245423
7. Seidl AH, Rubel EW, Barria A. Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. *Nature Communications*. 2015.
   - https://doi.org/10.1038/ncomms9073
8. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
   - https://doi.org/10.1038/s41593-019-0502-4
9. Mostert P, Albers AM, Brinkman L, Todorova L, de Lange FP. Eye movement-related confounds in neural decoding of visual working memory representations. *eNeuro*. 2018.
   - https://doi.org/10.1523/ENEURO.0401-17.2018
10. McFarland DJ, McCane LM, David SV, Wolpaw JR. Brain-computer interface operation: signal and noise during early training sessions. *Journal of Neural Engineering*. 2005.
   - https://doi.org/10.1088/1741-2560/2/4/014
11. Chaibub Neto E, Pratap A, Perumal TM, et al. Identity confounding in machine learning can be controlled by design. *npj Digital Medicine*. 2019.
   - https://doi.org/10.1038/s41746-019-0178-x
12. Xu M, Fanton S, Jahanbekam A, et al. The Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. *Frontiers in Human Neuroscience*. 2020.
   - https://doi.org/10.3389/fnhum.2020.00103
13. Murphy K, Harris AD, Wise RG. Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. *NeuroImage*. 2011.
   - https://doi.org/10.1016/j.neuroimage.2010.07.059
14. Williams RJ, Specht JL, Mazerolle EL, et al. Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. *Frontiers in Physiology*. 2023.
   - https://doi.org/10.3389/fphys.2023.1167148
15. Yücel MA, Selb J, Huppert TJ, Franceschini MA, Boas DA. Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. *Neurophotonics*. 2015.
   - https://doi.org/10.1117/1.NPh.2.3.035005
16. Epp SM, Halani S, Paquette M, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
