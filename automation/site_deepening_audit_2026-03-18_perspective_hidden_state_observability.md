# Site Deepening Audit (2026-03-18, Perspective Hidden-State / Observability Refit)

## 対象

- 主対象: `perspective.md`
- 参照整合: `wbe_101.md`, `verification.md`, `tech_roadmap.md`

## 今回の選定理由

- 公開サイト全体では、2026-03-18 時点で `hidden-state`, `maintenance-state`, `human observability`, `vascular-state / CVR` の分解がかなり前進しておりました。
- しかし中心ページである `perspective.md` は、他ページより更新が一段遅れており、`multimodal` という一語に異なる measurement class を畳み込みやすい構造が残っておりました。
- 技術・自然科学の観点では、ここは単なる文章の古さではございません。中心ページの分類が粗いままだと、読者が
  - `local connectomics = state-complete progress`
  - `human proxy exists = current state is almost visible`
  - `BOLD difference = neural difference`
  - `same-day fit = maintenance-consistent dynamics`
  と誤読しやすくなります。

## 根拠付き批判

### 1. 旧 `Perspective` は human evidence を layered evidence として固定しきれていませんでした

- 問題:
  - `perspective.md` は atlas, patch-seq, connectomics, neuromodulator / glia imaging の差を言い始めていましたが、human-side measurement class の差までは十分に site rule 化しておりませんでした。
- 根拠:
  - <https://doi.org/10.1126/science.adk4858> は human cortex の fixed-tissue local ultrastructure を押し上げましたが、living whole-brain dynamics は与えません。
  - <https://doi.org/10.1126/scitranslmed.aaf6667>, <https://doi.org/10.2967/jnumed.120.249144>, <https://doi.org/10.1523/JNEUROSCI.1750-23.2024> は regional synaptic-density proxy を押し上げましたが、release probability や tagged spine の ground truth ではありません。
  - <https://doi.org/10.1038/s41467-025-66124-w>, <https://doi.org/10.1002/nbm.3384>, <https://doi.org/10.1093/pnasnexus/pgaf072> は macro biochemical / energetic organization を押し上げましたが、branch-local ATP reserve や mitochondrial positioning は残ります。
  - <https://doi.org/10.1002/mrm.29998>, <https://doi.org/10.1002/mrm.23225>, <https://doi.org/10.1093/brain/awab466> は myelin / ionic / thermal proxy を押し上げましたが、cell-specific chloride set point や microtemperature の直接測定ではありません。
- 批判:
  - したがって `human evidence has advanced` を 1 本の進捗として書くのは粗すぎます。
  - 中心ページでは、`which layer was advanced` と `which state class remains latent` を並べて書く必要がありました。

### 2. 旧 `Gap between connectome and dynamics` は state class の分解がまだ粗く、recent public pages に追いついていませんでした

- 問題:
  - 旧文面は 6 state classes を挙げておりましたが、2026-03-18 時点の site-wide rule が既に分離していた
    - transcription / chromatin
    - local proteostasis / synaptic tagging
    - sleep architecture / replay-coupling
    - thermal-state
    - ECM / PNN
    - ionic milieu / chloride homeostasis
    - bioenergetic / mitochondrial state
    を十分に前景化しておりませんでした。
- 根拠:
  - <https://doi.org/10.1038/s41586-020-2907-3> と <https://doi.org/10.1016/j.cell.2016.01.046> は、cell type が同じでも morpho-electric phenotype や firing-rate set point が固定されないことを示します。
  - <https://doi.org/10.1038/s42003-025-08459-0> と <https://doi.org/10.1080/15548627.2020.1775393> は、late stabilization が local tag / capture / proteostasis route に依存することを示します。
  - <https://doi.org/10.1016/j.neuron.2013.03.006>, <https://doi.org/10.1038/s41467-024-49572-8>, <https://doi.org/10.1016/j.neuron.2025.03.020> は、sleep duration だけでなく replay-coupling / timing window が consolidation に重要であることを示します。
  - <https://doi.org/10.1126/science.1245423> と <https://doi.org/10.1126/science.aad4821> は、chloride set point や interstitial ions が inhibitory polarity や state transition に関わることを示します。
  - <https://doi.org/10.1016/j.cell.2018.12.013> と <https://doi.org/10.1038/s41467-023-44233-8> は、branch-local mitochondrial positioning が synaptic plasticity を制約することを示します。
- 批判:
  - したがって `wiring is not enough` を一般論で済ませる段階は過ぎております。
  - どの hidden-state family が何を壊すのかを 1 段具体化しなければ、技術的な批判として弱いままでした。

### 3. 旧 macro measurement row は hemodynamic side の vascular transfer ceiling を十分に書けていませんでした

- 問題:
  - 旧 `EEG / MEG / fMRI` row は neural hidden state を中心に説明していましたが、fMRI / fNIRS では `vascular transfer state` も独立の ceiling であることが弱いままでした。
- 根拠:
  - <https://doi.org/10.1016/j.neuroimage.2010.07.059> は local CBF / CBV difference が BOLD reactivity variance に寄与することを示しました。
  - <https://doi.org/10.3389/fphys.2023.1167148> は task BOLD magnitude が cortex 全体で CVR と強く対応することを示しました。
  - <https://doi.org/10.1038/s41593-025-02132-9> は significant BOLD change の相当部分で oxygen metabolism が逆向きになりうることを示しました。
- 批判:
  - よって `fMRI is a hemodynamic proxy` という一般論だけでは不十分です。
  - 中心ページでも `neural-side uncertainty` と `vascular-side uncertainty` を分離する必要がありました。

## 今回実行する変更

- `perspective.md`
  - `last_updated` を 2026-03-18 に更新
  - front matter の highlights / known points / unknown points を recent site-wide rule に整合させる
  - measurement stack table の macro row を `EEG / MEG / fMRI / fNIRS` として改稿し、vascular transfer / CVR ceiling を明示する
  - 新規節 `Human evidence is layered, not one progress bar` を追加し、human-side evidence class を
    - local human ultrastructure
    - regional synaptic-density proxy
    - parcel-level biochemical / energetic organization
    - macro support-state proxy
    - hemodynamic transfer audit
    の 5 類型に分離する
  - `Gap between connectome and dynamics` を `10 hidden-state classes` に更新し、safe reading を table 化する

## 外部依存で保留

- なし
  - 今回の作業は公開本文の改稿で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - <https://doi.org/10.1126/science.adk4858>
2. Dorkenwald S, Matsliah A, Sterling AR, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024;634:124-138.
   - <https://doi.org/10.1038/s41586-024-07558-y>
3. MICrONS Consortium, Bae JA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640:435-447.
   - <https://doi.org/10.1038/s41586-025-08790-w>
4. Finnema SJ, Nabulsi NB, Eid T, et al. Imaging synaptic density in the living human brain. *Science Translational Medicine*. 2016;8(348):348ra96.
   - <https://doi.org/10.1126/scitranslmed.aaf6667>
5. Naganawa M, Nabulsi N, Lin S-F, et al. First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. *Journal of Nuclear Medicine*. 2021;62(4):561-567.
   - <https://doi.org/10.2967/jnumed.120.249144>
6. Johansen A, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024.
   - <https://doi.org/10.1523/JNEUROSCI.1750-23.2024>
7. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - <https://doi.org/10.1038/s41467-025-66124-w>
8. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - <https://doi.org/10.1002/nbm.3384>
9. Li J, Xu HN, Yuan J, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - <https://doi.org/10.1093/pnasnexus/pgaf072>
10. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - <https://doi.org/10.1002/mrm.29998>
11. Qian Y, Zhao T, Zheng H, et al. High-resolution sodium imaging of human brain at 7 T. *Magnetic Resonance in Medicine*. 2012;68(1):227-233.
   - <https://doi.org/10.1002/mrm.23225>
12. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. Daily brain temperature rhythms and mortality after brain injury. *Brain*. 2022;145(3):867-882.
   - <https://doi.org/10.1093/brain/awab466>
13. Gouwens NW, Sorensen SA, Berg J, et al. Phenotypic variation of transcriptomic cell types in mouse motor cortex. *Nature*. 2021;598:144-150.
   - <https://doi.org/10.1038/s41586-020-2907-3>
14. Thomas M, Bogaciu C-A, Rizzoli SO, et al. Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. *Communications Biology*. 2025;8:756.
   - <https://doi.org/10.1038/s42003-025-08459-0>
15. Pandey K, Yu X-W, Steinmetz A, Alberini CM. Autophagy coupled to translation is required for long-term memory formation. *Autophagy*. 2021;17(9):2489-2505.
   - <https://doi.org/10.1080/15548627.2020.1775393>
16. Hengen KB, Torrado Pacheco A, McGregor JN, et al. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016;165(1):180-191.
   - <https://doi.org/10.1016/j.cell.2016.01.046>
17. Schreiner T, Petzka M, Staudigl T, Staresina BP. Endogenous memory reactivation during sleep in humans is clocked by slow oscillation-spindle complexes. *Nature Communications*. 2021;12:3112.
   - <https://doi.org/10.1038/s41467-021-23520-2>
18. Schreiner T, Martínez-Vargas M, Margineanu A, et al. Dynamic interplay of slow oscillations and spindles during sleep prevents forgetting of overlapping memories. *Nature Communications*. 2024;15:5150.
   - <https://doi.org/10.1038/s41467-024-49572-8>
19. Deng X, et al. Selective suppression of sleep replays by neural coding and oscillatory phase. *Neuron*. 2025.
   - <https://doi.org/10.1016/j.neuron.2025.03.020>
20. Glykys J, Dzhala V, Egawa K, et al. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014;343(6171):670-675.
   - <https://doi.org/10.1126/science.1245423>
21. Ding F, O'Donnell J, Xu Q, et al. Changes in the composition of brain interstitial ions control the sleep-wake cycle. *Science*. 2016;352(6285):550-555.
   - <https://doi.org/10.1126/science.aad4821>
22. Rangaraju V, Lauterbach M, Schuman EM. Spatially stable mitochondrial compartments fuel local translation during plasticity. *Cell*. 2019;176(1-2):73-84.e15.
   - <https://doi.org/10.1016/j.cell.2018.12.013>
23. Bapat P, Nirschl JJ, Wilkerson JR, et al. VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. *Nature Communications*. 2024;15:917.
   - <https://doi.org/10.1038/s41467-023-44233-8>
24. Cahill MK, Gazit V, Ginzberg M, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024;629:146-153.
   - <https://doi.org/10.1038/s41586-024-07311-5>
25. Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *PNAS*. 2022;119(42):e2211572119.
   - <https://doi.org/10.1073/pnas.2211572119>
26. Murphy K, Harris AD, Wise RG. Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. *NeuroImage*. 2011;54(1):369-379.
   - <https://doi.org/10.1016/j.neuroimage.2010.07.059>
27. Williams RJ, Specht JL, Mazerolle EL, et al. Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. *Frontiers in Physiology*. 2023;14:1167148.
   - <https://doi.org/10.3389/fphys.2023.1167148>
28. Epp SM, Castrillon G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - <https://doi.org/10.1038/s41593-025-02132-9>
