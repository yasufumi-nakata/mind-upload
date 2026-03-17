# Site Deepening Audit (2026-03-18, Human Maintenance-State Observability Alignment)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 参照導線: `index.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`connectome-complete ≠ emulation-complete`、`same-day fit ≠ cross-day maintenance`、`human proxy ≠ local ground truth` という方向性自体は正しく持っておりました。
- しかし、`wiki/homeostatic-plasticity-and-maintenance-state.md` の要所には、最近の追記由来と思われる壊れた引用タグ、崩れた英文、文献間の evidence class の混線が残っておりました。
- さらに `index.md` が強調していた `latent-state error budget` と `maintenance-state error budget` は、`verification.md` 本文に対応節が存在せず、入口ページの主張と検証ページの提出仕様が接続されていませんでした。
- 技術・自然科学の観点では、これは単なる文面の問題ではございません。`human で何が見えたか` を `1つの前進` として畳み込むと、固定組織 ultrastructure、SV2A PET、MRSI、31P-MRS / dynamic DMI、myelin bilayer map、TMS-EEG / sleep proxy、CSF / glymphatic proxy の違いが消え、読者が `maintenance-state をかなり直接見始めた` と誤読しやすくなります。

## 主要な批判点

### 1. 旧 human observability 節は、異なる measurement class を 1 本の前進として畳み込みすぎておりました

- 問題:
  - 旧文面では、Shapson-Coe、SV2A PET、Lucchetti、Ren / Li、Baadsvik、Huber / Kuhn / Fehér / Zrenner、Hirschler / Dagum が同じ種類の `human maintenance-state evidence` として並びやすい構造でした。
- 根拠:
  - Shapson-Coe et al. (2024) が押し上げたのは `fixed-tissue structural scaffold` です。
  - Finnema et al. (2016), Naganawa et al. (2021), Johansen et al. (2024) が押し上げたのは `regional synaptic-density proxy` です。
  - Lucchetti et al. (2025) が押し上げたのは `parcel-level macro-biochemical scaffold` です。
  - Ren et al. (2015) と Li et al. (2025) が押し上げたのは `macro energetic proxy` です。
  - Baadsvik et al. (2024) が押し上げたのは `macro-myelin proxy` です。
  - Huber et al. (2013), Kuhn et al. (2016), Fehér et al. (2026), Zrenner et al. (2018) が押し上げたのは `perturbation-conditioned plasticity proxy` です。
  - Hirschler et al. (2025) と Dagum et al. (2026) が押し上げたのは `macro support-state proxy` です。
- 批判:
  - したがって、これらを同じ `human でも見えてきた` に畳み込むのは粗すぎます。
  - 本来は `何の層が直接見えたのか` と `何がまだ latent なのか` を site-wide rule として固定する必要がありました。

### 2. 旧ページには壊れた引用タグと崩れた英文が混在し、根拠追跡性を下げておりました

- 問題:
  - AIS、sleep、myelin、bioenergetic、astrocyte、clearance の各節で、`href=` の欠落、途中で切れた文、誤った接続句が混入しておりました。
- 批判:
  - これは単なる体裁ではございません。一次文献を根拠として読むページで引用タグが壊れていると、どの結論がどの論文に対応するかが追えなくなります。
  - `証跡のない成果は成果ではない` という運用規律に照らしても、公開科学サイトとして放置できない弱点でした。

### 3. `verification.md` は top-level guidance で予告していた error budget を本文へ実装できていませんでした

- 問題:
  - `verification.md` front matter と `index.md` は `latent-state error budget` および `maintenance-state error budget` を重要導線として前面化していました。
  - しかし本文には対応する `id` 節が存在せず、入口ページからのリンクが着地しませんでした。
- 批判:
  - これは site-wide rule の欠落です。
  - 読者に `latent-state` や `maintenance-state` を要求するなら、少なくとも `何を提出物として書くべきか` を検証ページ本体に明示しなければなりません。

### 4. 旧 verification 導線は `cross-day success` と `maintenance-consistent success` の差を十分に operational にしていませんでした

- 問題:
  - 既存ページは sleep、timing、bioenergetics、glia、clearance の重要性を別ページで論じていました。
  - しかし Verification 本文では、cross-day / reconsolidation / remote-memory claim に対して `controller state`、`sleep history`、`timing support`、`bioenergetic support`、`glial support`、`clearance / immune proxy` を 1 つの提出仕様へ束ねていませんでした。
- 批判:
  - この状態では、単なる temporal hold を `maintenance-consistent` へ誤昇格させやすくなります。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - AIS / sleep / myelin / bioenergetic / astrocyte / clearance の各節を全文改稿し、壊れた引用タグと崩れた英文を修正しました。
  - `Human maintenance-state observability is layered, not direct` 節へ改題し、human-side evidence を
    - `structural scaffold`
    - `regional synaptic-density proxy`
    - `macro-biochemical scaffold`
    - `macro energetic proxy`
    - `macro-myelin proxy`
    - `perturbation-conditioned plasticity proxy`
    - `macro support-state proxy`
    の 7 類型に分離しました。
  - human observability table に `Safe site reading` 列を追加し、各 measurement class からどこまでしか言えないかを site-wide rule として固定しました。
  - `current transcription / chromatin state`、`current ECM / PNN gate state`、`branch-local proteostasis / tag-capture route` には、なお comparable な in vivo whole-brain human route が無いことを明文化しました。
- `verification.md`
  - 新規節 `#latent-state-error-budget` を追加し、L2+ submission が state family ごとに何を開示すべきかを table 化しました。
  - 新規節 `#maintenance-state-error-budget` を追加し、cross-day / recovery / remote-memory claim が何を別途申告しなければならないかを table 化しました。
  - human 側の maintenance evidence について、`class-labeled submission` を site-wide rule として追加しました。
- `index.md`
  - 変更なし
  - ただし、既存の `#latent-state-error-budget` / `#maintenance-state-error-budget` リンクは、今回の `verification.md` 追記によって実際に着地するようになりました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文、検証仕様、導線整合性の改稿で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Finnema SJ, Nabulsi NB, Eid T, et al. Imaging synaptic density in the living human brain. *Science Translational Medicine*. 2016;8(348):348ra96.
   - https://doi.org/10.1126/scitranslmed.aaf6667
3. Naganawa M, Nabulsi N, Lin S-F, et al. First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. *Journal of Nuclear Medicine*. 2021;62(4):561-567.
   - https://doi.org/10.2967/jnumed.120.249144
4. Johansen A, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
5. Shatalina E, et al. The relationship between SV2A levels, neural activity, and cognitive function in healthy humans. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00190
6. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
7. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
8. Li J, Xu HN, Yuan J, et al. Dynamic deuterium metabolic imaging reveals whole-brain glucose metabolic turnover and neuronal function in humans. *PNAS Nexus*. 2025;4(3):pgaf079.
   - https://doi.org/10.1093/pnasnexus/pgaf079
9. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
10. Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
11. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
12. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
13. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
14. Hirschler L, et al. Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28:1115-1126.
   - https://doi.org/10.1038/s41593-025-02073-3
15. Dagum P, et al. The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:7800.
   - https://doi.org/10.1038/s41467-026-68374-8
16. Suzuki A, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011;144(5):810-823.
   - https://doi.org/10.1016/j.cell.2011.02.018
17. Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024;629:146-153.
   - https://doi.org/10.1038/s41586-024-07311-5
18. Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025;636:445-454.
   - https://doi.org/10.1038/s41586-024-08170-w
19. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025;648:99-107.
   - https://doi.org/10.1038/s41586-025-09619-2
20. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
