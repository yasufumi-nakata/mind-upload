# Site Deepening Audit (2026-03-20, Perspective Observability / Hidden-State Sync)

## 対象

- 主対象: `perspective.md`
- 副対象: `summary_booklet.md`

## 今回の選定理由

- 2026-03-20 時点で、公開サイトの入口ページ群 `index.md` / `wbe_101.md` / `faq.md` / `verification.md` は、human observability と maintenance-state をかなり細かく分解できていました。
- その一方で、長文研究ノートである `perspective.md` には、なお `human evidence advanced` と `connectome is not enough` が少し圧縮された形で残っていました。
- これは技術・自然科学の観点で優先度が高いです。`perspective.md` は理論と計測と実装を接続する中核ページであり、ここが粗いと、読者が front-door 側で禁止した過大読みを長文側で再び行えるからです。

## 根拠付き批判

### 1. 旧 `perspective.md` は human-side advance をまだ粗い observability 向上物語へ寄せていました

- 問題:
  - 旧版は `local connectomics`、`human structural scaffold evidence`、`synaptic-density PET`、`macro energetic / myelin / ionic proxies` をある程度分けていました。
  - しかし `human receptor / transporter atlas prior`、`occupancy / displacement PET`、`whole-brain MRSI biochemical scaffold`、`dynamic DMRSI energetic imaging`、`macro support-state proxies`、`CSF / glymphatic support-state proxy` の間の object 差と inferential ceiling 差が、まだ十分に固定されていませんでした。
- 根拠:
  - Shapson-Coe et al. (2024) は human cortex の局所 ex vivo nanoscale scaffold を示しました。
  - Johansen et al. (2024) は 33 healthy participants の SV2A PET atlas を postmortem autoradiography で較正しました。
  - Hansen et al. (2022) と Goulas et al. (2021) は receptor / transporter atlas が normative chemoarchitectural prior であることを示しました。
  - Wong et al. (2013) は occupancy PET が administered ligand の target engagement を問う route であることを示しました。
  - Koepp et al. (1998), Lippert et al. (2019), Erritzoe et al. (2020) は displacement / release-sensitive PET が challenge-limited release proxy であることを示しました。
  - Lucchetti et al. (2025) は 51 healthy participants と independent replication 13 で five-metabolite `1H-MRSI` similarity scaffold を示しました。
  - Li et al. (2025) は `7 T` dynamic DMRSI と kinetic model を用い、5 healthy participants で glucose-related rate imaging を行いました。
  - Baadsvik et al. (2024) は 2 healthy volunteers の myelin bilayer mapping を示しました。
  - Hirschler et al. (2025) は 24 healthy adults における specialized 7 T CSF-mobility route を示しました。
  - Dagum et al. (2026) は investigational wearable と compartmental model を伴う crossover design で sleep-linked clearance を論じました。
- 批判:
  - 以上はすべて `human evidence improved` の一文で括ってよい object ではありません。
  - 旧 `perspective.md` では、`proxy class` と `operational maturity / model burden` が十分に分離されておらず、`proxy-rich evidence` が `near-direct state closure` に近く読まれる余地が残っていました。

### 2. 旧 `perspective.md` は `10-class latent-state problem` のままで、サイト全体の hidden-state 分解とずれていました

- 問題:
  - 入口ページ群と wiki 側では、maintenance-state が既に `at least fifteen` の class へ広がっていました。
  - しかし `perspective.md` はなお 10-class table に留まり、`post-transcriptional RNA-state`、`cargo-transport / cytoskeletal trafficking state`、`sleep/wake-dependent renormalization`、`shared extracellular / electrical state`、`clearance / immune support` が十分に前面化されていませんでした。
- 根拠:
  - Santoni et al. (2024) は chromatin plasticity が memory-trace eligibility を前もって規定しうることを示しました。
  - Wang et al. (2015) は neuron-specific LSD1 isoform が memory formation に関わることを示しました。
  - Park et al. (2006) と Swarnkar et al. (2021) は compartment-specific cargo delivery が plasticity と long-term memory に関わることを示しました。
  - Glykys et al. (2014) は local impermeant anions が neuronal chloride concentration を規定することを示しました。
  - Yang et al. (2024) は dynamic electrical synapses が persistent oscillations を支えることを示しました。
  - Williamson et al. (2025) は learning-associated astrocyte ensembles が memory recall を制御することを示しました。
  - Louveau et al. (2015), Eide & Ringstad (2021), Kim et al. (2025), Dagum et al. (2026) は clearance / immune support が単なる cleanup metaphor ではなく multiday support-state であることを示しました。
- 批判:
  - 旧 `perspective.md` のままでは、`connectome + cell type is insufficient` という主張自体は正しくても、どの hidden-state family が何故残るのかが site-wide rule より粗く見えました。
  - 長文研究ノート側が coarse だと、読者は front-door 側の stricter rule を `primer 向けの注意書き` と誤認しやすくなります。

### 3. 長文研究ノートは site-wide rule の最終集約ページであり、ここでの圧縮は影響が大きいです

- 問題:
  - `perspective.md` は、`theory -> measurement -> inference -> implementation` を一つの narrative に束ねるページです。
  - したがって、ここで `proxy class != route maturity` と `hidden-state class expansion` が明記されていないと、他ページで厳密化した claim ceiling が長文の中で再び崩れます。
- 批判:
  - この不整合は単なる表現の好みではなく、site-level reasoning rule の破綻でございます。
  - 技術・自然科学の側面だけで見ても、計測対象、推定対象、support-state、model burden を分けない議論は claim ceiling を壊します。

## 今回実行した変更

- `perspective.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - front matter の `page_highlights` / `known_points` に、`15-class maintenance / hidden-state` と `proxy class != operational maturity` を反映しました。
  - human evidence section を改稿し、`local ultrastructure`、`synaptic-density PET atlas`、`receptor / transporter atlas prior`、`occupancy / displacement PET`、`MRSI biochemical scaffold`、`31P-MRS / dynamic DMRSI`、`macro support-state proxies`、`CSF mobility / sleep-linked clearance proxy`、`hemodynamic transfer audit` を別 row に分けました。
  - 同 section に `Proxy class is not the same thing as operational maturity` note を追加し、sample size / hardware burden / model burden を明記しました。
  - `Gap between connectome and dynamics` を改稿し、hidden-state table を `15` row に拡張しました。
  - 同 section に `post-transcriptional RNA-state`、`cargo-transport / cytoskeletal trafficking state`、`sleep/wake-dependent renormalization`、`shared extracellular / electrical state`、`clearance / immune support` を追加しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成し、`perspective.md` の front matter 更新を冊子へ反映しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・自動生成冊子・監査メモの更新で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022;25:1569-1581.
   - https://doi.org/10.1038/s41593-022-01186-3
4. Goulas A, Changeux J-P, Wagstyl K, Amunts K, Palomero-Gallagher N, Hilgetag CC. The natural axis of transmitter receptor distribution in the human cerebral cortex. *PNAS*. 2021;118(3):e2020574118.
   - https://doi.org/10.1073/pnas.2020574118
5. Wong DF, Kuwabara H, Hsu DJ, et al. Determination of dopamine D2 receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. *Psychopharmacology*. 2013;229:245-252.
   - https://doi.org/10.1007/s00213-013-3103-z
6. Koepp MJ, Gunn RN, Lawrence AD, et al. Evidence for striatal dopamine release during a video game. *Nature*. 1998;393:266-268.
   - https://doi.org/10.1038/30498
7. Lippert RN, Hess S, Vollmert C, et al. Maternal serotonin controls separation-induced ultrasonic calling in mouse pups. *Nature Communications*. 2019;10:4260.
   - https://doi.org/10.1038/s41467-018-08143-4
8. Erritzoe D, Searle GE, Tziortzi A, et al. In vivo imaging of cerebral serotonin release by d-amphetamine: a [11C]Cimbi-36 PET study in humans. *Neuropsychopharmacology*. 2020;45:1241-1248.
   - https://doi.org/10.1038/s41386-019-0567-5
9. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
10. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
    - https://doi.org/10.1093/pnasnexus/pgaf072
11. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
    - https://doi.org/10.1002/mrm.29998
12. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28:2392-2401.
    - https://doi.org/10.1038/s41593-025-02073-3
13. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
    - https://doi.org/10.1038/s41467-026-68374-8
14. Santoni G, Astori S, Leleu M, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024;385(6705):eadg9982.
    - https://doi.org/10.1126/science.adg9982
15. Wang J, Telese F, Tan Y, et al. LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. *Nature Neuroscience*. 2015;18:1256-1264.
    - https://doi.org/10.1038/nn.4069
16. Park M, Salgado JM, Ostroff L, et al. Plasticity-induced growth of dendritic spines by exocytic trafficking from recycling endosomes. *Neuron*. 2006;52(5):817-830.
    - https://doi.org/10.1016/j.neuron.2006.09.040
17. Swarnkar S, Avchalumov Y, Espadas I, et al. Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. *Cell Reports*. 2021;36(2):109369.
    - https://doi.org/10.1016/j.celrep.2021.109369
18. Glykys J, Dzhala V, Egawa K, et al. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014;343(6171):670-675.
    - https://doi.org/10.1126/science.1245423
19. Yang Y-C, Wang G-H, Chou P, et al. Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. *PNAS*. 2024;121(14):e2313042121.
    - https://doi.org/10.1073/pnas.2313042121
20. Williamson NR, Kwon W, Woo J, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025;636:433-441.
    - https://doi.org/10.1038/s41586-024-08170-w
21. Louveau A, Smirnov I, Keyes TJ, et al. Structural and functional features of central nervous system lymphatic vessels. *Nature*. 2015;523:337-341.
    - https://doi.org/10.1038/nature14432
22. Eide PK, Ringstad G. Sleep deprivation impairs molecular clearance from the human brain. *Brain*. 2021;144(3):863-874.
    - https://doi.org/10.1093/brain/awab285
23. Kim S, Xu J, Son Y, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology and behavior. *Cell*. 2025;188(6):1515-1533.e22.
    - https://doi.org/10.1016/j.cell.2025.02.022
