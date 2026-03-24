# Site Deepening Audit (2026-03-25, landing page phospho / proteostasis / cargo front door)

## 今回この箇所を選んだ理由

- 今回の主対象は `index.md` の landing page です。
- 2026-03-25 JST 時点で、公開中の `https://mind-upload.com/` を web で確認したところ、landing page には
  - `intrinsic excitability`
  - `synaptic-density PET`
  - `myelin`
  - `energetic`
  - `ECM / PNN`
  - `post-transcriptional RNA`
  - `ionic`
  - `electrical-state`
  - `astrocyte`
  - `clearance`
  の front-door stop line はある一方、
  - `phospho-signaling / second-messenger state`
  - `local proteostasis / synaptic-tagging state`
  - `cargo-transport / cytoskeletal trafficking state`
  の専用 note-box はありませんでした。
- しかし `wbe_101.md` と `wiki/homeostatic-plasticity-and-maintenance-state.md` では、これら 3 系統はすでに独立 route card として運用されております。
- つまり、site-wide rule は深部ページでは成立しているのに、最初の入口だけがまだ粗く、読者が
  - `transcript / proteome / nominal weight`
  - `local translation clue`
  - `one cargo image`
  を実際より強い state evidence と誤読できる状態でした。

## 観察した問題

### 1. landing page の hidden-state coverage が site-wide taxonomy に追いついておりませんでした

- `index.md` の front matter と note-box 群は 2026-03 の再監査でかなり強化されていました。
- それでも、`phospho-signaling`、`proteostasis`、`cargo-transport` だけは landing page で独立 family として露出しておりませんでした。
- 一方で `wbe_101.md` では同じ 3 family に対して、すでに
  - evidence class の分離
  - direct observable の固定
  - abstention boundary
  が書かれております。
- これは単なる見栄えの問題ではなく、public entrance と deeper page の spec がずれるという意味で public-spec inconsistency です。

### 2. phospho omission は transcript / proteome / weight の過読を招きます

- phospho-signaling は gene-level abundance や bulk proteome と同じ inferential object ではありません。
- `Lee et al. (2003)` と `Tomita et al. (2005)` は phosphosite-specific gate を扱っており、同じ AMPAR / TARP 背景でも plasticity expression が phosphosite ごとに変わることを示しています。
- `Havekes et al. (2016)` と `Vierra et al. (2023)` は compartmentalized second-messenger routing を扱っており、同じ細胞でも cAMP / kinase signaling は局所 signalosome 依存で変わります。
- `Altas et al. (2024)` は region-specific phosphorylation により neuroligin-3 localization が excitatory / inhibitory synapse のどちらへ寄るかが変わることを示しました。
- `Rodriguez et al. (2025)` は単一 phosphosite 改変が memory と synaptic plasticity を双方向に変えることを示しました。
- `Biswas et al. (2023)` は human brain phosphoproteome atlas ですが、ex vivo・region-structured atlas であり、current whole-brain in vivo phospho-controller ではありません。
- よって landing page にこの停止線がないと、`transcriptomics + proteomics + weights` が `active phospho-controller` に近いかのような誤読を止め切れません。

### 3. proteostasis omission は late stabilization を current weight に畳み込みます

- `Frey & Morris (1997)` と `Shires et al. (2012)` は synaptic tag / capture eligibility を扱います。
- `Govindarajan et al. (2011)` は relevant unit が neuron 全体ではなく dendritic branch になりうることを示しました。
- `Fonseca et al. (2006)` と `Parker et al. (2025)` は synthesis-degradation / proteasome-capacity balance が memory outcome と結びつくことを示しました。
- `Pandey et al. (2021)` と `Chang et al. (2024)` は autophagy-linked remodeling が late memory route の一部であることを示しました。
- `Lee et al. (2022)` と `Thomas et al. (2025)` は turnover-resistant persistence や candidate tag substrate を扱います。
- これらは同じ意味ではありません。にもかかわらず landing page で独立 stop line がないと、`current weights are known` から `late stabilization is nearly solved` への滑りを止めにくくなります。

### 4. cargo omission は local translation や ATP route を compartment-specific delivery の代替に見せます

- `Park et al. (2006)` と `Correia et al. (2008)` は postsynaptic AMPAR / recycling-endosome delivery を扱います。
- `Maas et al. (2009)`、`Uchida et al. (2014)`、`Wong et al. (2024)` は microtubule-path state や local vesicle confinement を扱います。
- `Swarnkar et al. (2021)` と `de Queiroz et al. (2025)` は RNA cargo localization / local translation support route を扱います。
- `Aiken & Holzbaur (2024)` は human-neuron preparation で presynaptic cargo delivery を patterning する local microtubule dynamics を扱います。
- したがって、`translation can happen`、`ATP is available`、`a cargo was seen somewhere` は、`the right receptor / RNA / presynaptic component reached the decisive branch, spine, or bouton` と同義ではありません。
- landing page がこの差を言わないままだと、読者は proteostasis と cargo を同じ maintenance bucket に畳み込んでしまいます。

## 今回実行する変更

- `index.md`
  - front matter の `page_highlights` に
    - `phospho-signaling`
    - `local proteostasis`
    - `cargo-transport`
    の 3 family を追加します。
  - `known_points` に、上記 3 family が current transcript / proteome / weight / local translation から自動では固定されないことを追加します。
  - front-door の human-observability note を更新し、current phospho-state と branch- / bouton-specific cargo delivery も still-missing route として明記します。
  - landing page に以下の note-box を新設します。
    - `If You Are Treating Phospho-Signaling Evidence As One Solved Row`
    - `If You Are Treating Proteostasis Evidence As One Solved Row`
    - `If You Are Treating Cargo-Transport Evidence As One Solved Row`
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成し、landing page front matter の更新を冊子側へ同期します。

## 修正しないもの

- `issue.md` は今回は前提既知として扱い、再読しておりません。
- 哲学・法学・personhood の議論は今回の修正対象に含めません。
- WBE 101 や wiki の route card 本体は今回は十分に整っているため、主変更は landing page とその要約同期に絞ります。

## 外部依存で保留

- なし
  - 今回の作業は repo 内の文書修正・要約再生成・push までで完結できます。

## 参考文献

1. Frey U, Morris RGM. Synaptic tagging and long-term potentiation. *Nature*. 1997;385(6616):533-536. https://doi.org/10.1038/385533a0
2. Shires KL, Da Silva BM, Hawthorne JP, Morris RGM, Martin SJ. Synaptic tagging and capture in the living rat. *Nature Communications*. 2012;3:1246. https://doi.org/10.1038/ncomms2250
3. Govindarajan A, Israely I, Huang S-Y, Tonegawa S. The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. *Neuron*. 2011;69(1):132-146. https://doi.org/10.1016/j.neuron.2010.12.008
4. Fonseca R, Nägerl UV, Bonhoeffer T. Neuronal activity determines the protein synthesis dependence of long-term potentiation. *Neuron*. 2006;51(3):339-352. https://doi.org/10.1016/j.neuron.2006.08.015
5. Pandey K, et al. Autophagy and its relevance to plasticity and memory. *Autophagy*. 2021. https://doi.org/10.1080/15548627.2020.1775393
6. Chang H, et al. Autophagy coupled to translation is required for long-term memory. *Proceedings of the National Academy of Sciences*. 2024. https://doi.org/10.1073/pnas.2315958121
7. Lee SH, et al. Synaptic memory survives molecular turnover by preserving its protein-protein interaction network. *Proceedings of the National Academy of Sciences*. 2022;119(11):e2211572119. https://doi.org/10.1073/pnas.2211572119
8. Thomas M, et al. Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. *Communications Biology*. 2025;8:756. https://doi.org/10.1038/s42003-025-08459-0
9. Parker J, et al. Proteasome augmentation mitigates age-related cognitive decline in mice. *Aging Cell*. 2025. https://doi.org/10.1111/acel.14492
10. Park M, et al. Recycling endosomes supply AMPA receptors for LTP. *Neuron*. 2006;52(5):817-830. https://doi.org/10.1016/j.neuron.2006.09.040
11. Correia SS, et al. Motor protein-dependent transport of AMPA receptors into spines during LTP. *Nature Neuroscience*. 2008;11(4):457-466. https://doi.org/10.1038/nn2063
12. Maas C, et al. Synaptic activation modifies microtubules underlying transport of postsynaptic cargo. *Proceedings of the National Academy of Sciences*. 2009;106(21):8731-8736. https://doi.org/10.1073/pnas.0902304106
13. Uchida S, et al. Learning-induced and stathmin-dependent changes in microtubule stability are critical for memory and disrupted in ageing. *Nature Communications*. 2014;5:4389. https://doi.org/10.1038/ncomms5389
14. Wong HH-W, et al. Vesicles containing endogenous AMPA receptors are locally confined to dendrites that have undergone plasticity. *eLife*. 2024;13:e80622. https://doi.org/10.7554/eLife.80622
15. Swarnkar S, et al. Kinesin family member 5C regulates structural plasticity and long-term memory by mediating activity-dependent localization of GluA1. *Cell Reports*. 2021;36(1):109369. https://doi.org/10.1016/j.celrep.2021.109369
16. de Queiroz RM, et al. Axonal RNA localization is essential for long-term memory. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57651-7
17. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Current Biology*. 2024;34(8):1687-1704.e8. https://doi.org/10.1016/j.cub.2024.03.010
18. Lee H-K, et al. Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. *Cell*. 2003;112(5):631-643. https://doi.org/10.1016/S0092-8674(03)00122-3
19. Tomita S, et al. Bidirectional synaptic plasticity regulated by phosphorylation of stargazin-like TARPs. *Neuron*. 2005;45(2):269-277. https://doi.org/10.1016/j.neuron.2005.01.009
20. Havekes R, et al. Sleep deprivation causes memory deficits by negatively impacting neuronal connectivity in hippocampal area CA1. *Journal of Neuroscience*. 2016;36(11):3236-3249. https://doi.org/10.1523/JNEUROSCI.0248-16.2016
21. Vierra NC, et al. Flexible spatiotemporal coupling of cAMP signalling in hippocampal neurons through exchange protein directly activated by cAMP 2. *Nature Communications*. 2023;14:6236. https://doi.org/10.1038/s41467-023-40930-6
22. Altas B, et al. Region-specific phosphorylation determines Neuroligin-3 localization to excitatory versus inhibitory synapses. *Biological Psychiatry*. 2024;96(10):815-828. https://doi.org/10.1016/j.biopsych.2023.12.020
23. Rodriguez AC, et al. HDAC3 Serine 424 phospho-mimic and phospho-null mutants bidirectionally modulate long-term memory formation and synaptic plasticity in the adult and aging mouse brain. *Journal of Neuroscience*. 2025;45(29):e1619242025. https://doi.org/10.1523/JNEUROSCI.1619-24.2025
24. Biswas D, et al. The landscape of the human brain phosphoproteome reveals region-specific phosphorylation events. *Journal of Proteome Research*. 2023;22(4):1390-1404. https://doi.org/10.1021/acs.jproteome.2c00244
