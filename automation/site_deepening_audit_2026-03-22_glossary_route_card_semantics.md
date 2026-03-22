# Site Deepening Audit (2026-03-22, glossary route-card semantics)

## 対象

- 主対象: `glossary.md`

## 今回の選定理由

- 2026-03-22 までの更新で、主要ページ側にはすでに
  - `field-formation wall`
  - `Fusion Card`
  - `Human Proxy Composition Card`
  - `shared-driver audit`
  - `strongest single row`
  - `State-Continuity Bridge Card`
  という新しい停止線が導入されておりました。
- しかし `glossary.md` は 2026-03-20 時点の語彙水準に留まっており、これらの語が短い定義として回収されていませんでした。
- その結果、本文ページでは科学的に分離済みの論点が、用語レベルでは再び圧縮されうる状態でした。

## 根拠付き批判

### 1. `field-formation wall` が未定義のままだと、inverse 以前の可視性壁が消えます

- 問題:
  - サイトはすでに `EEG/MEG では source class がそもそも scalp に届くか` を独立の停止線として採用していますが、Glossary 側にはこの短い説明がありませんでした。
- 根拠:
  - Ahlfors et al. (2010) は source orientation によって EEG/MEG 感度が大きく変わることを示しました。
  - Goldenholz et al. (2009) は source extent と anatomy が cortical SNR を大きく変えることを示しました。
  - Piastra et al. (2021) は CSF を含む head-model detail が EEG/MEG sensitivity estimate を変えることを示しました。
- 批判:
  - したがって `inverse problem` だけを読んでも不十分です。
  - `field-formation wall` が短く定義されないままだと、読者は `solver` と `visibility` を再び同じ箱に戻します。

### 2. `Fusion Card` と `Human Proxy Composition Card` が未定義だと、同時取得や多モダリティ列挙が過読されます

- 問題:
  - 主要ページでは、simultaneous acquisition や proxy-rich bundle をそのまま state-identification に上げない運用へ更新済みでした。
  - しかし Glossary に短い定義が無いため、読者は card 名を手続き的ラベルとして読み飛ばせる状態でした。
- 根拠:
  - Kothe et al. (2025) は LSL が stream synchronization infrastructure であり、device-side delay truth そのものではないことを明示しました。
  - Wei et al. (2020) は EEG-fMRI fusion が model-conditioned inference であることを示しました。
  - Vafaii et al. (2024) と Chen et al. (2025) は simultaneous multimodal recordings でも common structure と divergent structure が併存しうることを示しました。
  - Johansen et al. (2024), Lucchetti et al. (2025), Li et al. (2025), Hirschler et al. (2025), Dagum et al. (2026) は、それぞれ異なる quantity type と route burden を持つ human proxy rows を提供しています。
- 批判:
  - したがって `simultaneous` や `proxy-rich` は、それだけでは上位主張の根拠になりません。
  - この区別を Glossary が受け止めないと、主要ページの厳密さが入口の意味論で失われます。

### 3. `shared-driver audit` と `strongest single row` が未定義だと、bundle critique の心臓部が見えません

- 問題:
  - サイトは `bundle が strongest single row を超えて何を足したか` と `agreement が shared driver で説明できないか` を composition の中心に置き始めています。
  - しかしこの二語が未定義だと、Human Proxy Composition Card の核心が読者に伝わりません。
- 根拠:
  - Bolt et al. (2025) は global fMRI mode が autonomic physiology と強く結合しうることを示しました。
  - Epp et al. (2025) は task BOLD changes と oxygen metabolism が反対符号をとりうることを示しました。
  - Chen et al. (2025) は tightly coupled global progression と distinct network patterns の併存を示しました。
- 批判:
  - よって `rows moved together` は十分条件ではありません。
  - shared-driver audit と strongest-single-row comparison は decorative language ではなく、過読を止める最小限の技術語です。

### 4. `State-Continuity Bridge Card` と `same-state evidence` が未定義だと、same-subject が same-state に戻ります

- 問題:
  - サイトはすでに `same-subject / same-brain != same-state` を強く打ち出していますが、その短い語彙整備が Glossary に不足していました。
- 根拠:
  - Lu et al. (2023) は preservation route が extracellular space retention と ultrastructural quality を変えることを示しました。
  - MICrONS Consortium et al. (2025) は in vivo function から ex vivo EM への workflow が sequential multi-stage pipeline であることを示しました。
- 批判:
  - したがって specimen identity と state continuity は別概念です。
  - この区別が Glossary に無い限り、読者は `same-brain` を `same-state` に言い換えやすいままです。

## 今回実行した変更

- `glossary.md`
  - `last_updated` を `2026-03-22` に更新しました。
  - page highlights / known points を更新し、new route-card semantics の遅れを解消しました。
  - route-card 名が増えたときの案内用 note-box を追加しました。
  - `Verification and Hidden-State Terms` に以下の語を追加しました。
    - `Human Proxy Composition Card`
    - `shared-driver audit`
    - `strongest single row`
    - `Fusion Card`
    - `State-Continuity Bridge Card`
    - `same-state evidence`
  - `Modeling` に `field-formation wall` を追加しました。
  - references に、上記語義の背後にある主要一次文献を追記しました。

## なぜこの修正が良いか

- 主要ページで作った科学的停止線が、短い定義としても再利用可能になります。
- `route card` 群が jargon ではなく、どの失敗モードを止める語なのかが一目で分かるようになります。
- 用語層が追随することで、FAQ や WBE 101 を短く読んだ読者が旧来の圧縮読みに戻りにくくなります。

## 外部依存で保留

- なし

## 参考文献

1. Ahlfors SP, Han J, Belliveau JW, Hämäläinen MS. Sensitivity of MEG and EEG to Source Orientation. *Brain Topography*. 2010;23(3):227-232.
   - https://doi.org/10.1007/s10548-010-0154-x
2. Goldenholz DM, Ahlfors SP, Hämäläinen MS, Sharon D, Ishitobi M, Vaina LM, Stufflebeam SM. Mapping the signal-to-noise-ratios of cortical sources in magnetoencephalography and electroencephalography. *Human Brain Mapping*. 2009;30(4):1077-1086.
   - https://doi.org/10.1002/hbm.20571
3. Piastra MC, Nüßing A, Vorwerk J, Clerc M, Engwer C, Wolters CH. A comprehensive study on electroencephalography and magnetoencephalography sensitivity to cortical and subcortical sources. *Human Brain Mapping*. 2021;42(4):978-992.
   - https://doi.org/10.1002/hbm.25272
4. Kothe C, Shirazi SY, Stenner T, Medine D, Boulay C, Grivich MI, Artoni F, Mullen T, Delorme A, Makeig S. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025;3:IMAG.a.136.
   - https://doi.org/10.1162/IMAG.a.136
5. Wei H, Prasad G, Ombao H, Hajnal JV. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020;211:116595.
   - https://doi.org/10.1016/j.neuroimage.2020.116595
6. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024;15:229.
   - https://doi.org/10.1038/s41467-023-44363-z
7. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
8. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
9. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
10. Hirschler L, et al. Whole-brain mapping of cerebrospinal fluid mobility in humans. *Nature Neuroscience*. 2025.
    - https://doi.org/10.1038/s41593-025-02073-3
11. Dagum P, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
    - https://doi.org/10.1038/s41467-026-68374-8
12. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025.
    - https://doi.org/10.1038/s41467-025-64414-x
13. Bolt T, Falahpour M, Nalci A, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025.
    - https://doi.org/10.1038/s41593-025-01945-y
14. Epp SM, Castrillón G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
    - https://doi.org/10.1038/s41593-025-02132-9
15. Lu X, Han X, Meirovitch Y, Sjöstedt E, Schalek RL, Lichtman JW. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023;3(7):100520.
    - https://doi.org/10.1016/j.crmeth.2023.100520
16. MICrONS Consortium, Bae JA, Bak JH, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640:435-447.
    - https://doi.org/10.1038/s41586-025-08790-w
