# Site Deepening Audit (2026-04-03, literature proteostasis / cargo split)

## 1. 対象
- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 参照:
  - `index.md`
  - `verification.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`

## 2. 問題設定
- このサイトは 2026-04-03 時点で、入口ページ・Verification・wiki route card 側では `local proteostasis` と `cargo-routing` をかなり厳密に family split していました。
- しかし literature hub 側では、その split が `post-transcriptional RNA` や `phospho-signaling` ほど front door に露出しておらず、読者が
  - `proteostasis` を一つの consolidation controller
  - `cargo-routing` を一つの trafficking background
  として再圧縮しやすい非対称が残っていました。
- これはサイト自身が採用している `route family -> direct observable -> claim ceiling` の読解規則と噛み合っていませんでした。

## 3. 根拠付きの批判

### 3.1 `local proteostasis` を 1 行に潰すと、少なくとも 5 つの別問題が消えます
- `Frey & Morris (1997)` と `Shires et al. (2012)` は `tag / capture eligibility` の問題です。
- `Govindarajan et al. (2011)` は `branch-level integration` の問題です。
- `Fonseca et al. (2006)` は `protein synthesis vs proteasome-dependent degradation balance` の問題です。
- `Pandey et al. (2021)` は `translation-coupled autophagy` の問題です。
- `Chalatsi et al. (2026)` は `PVALB interneuron proteostasis / excitability / hippocampus-dependent memory` の問題で、generic autophagy として潰せません。
- `Lee et al. (2022)` と `Thomas et al. (2025)` は `turnover-resistant persistence` または `candidate tag substrate` の問題です。
- よって `proteostasis evidence exists` から `late stabilization controller is now specified` へ進むのは、論理的に 1 段以上強すぎます。

### 3.2 `cargo-routing` を 1 行に潰すと、局所 delivery と compartment が消えます
- `Park et al. (2006)` と `Correia et al. (2008)` は `postsynaptic AMPAR / recycling-endosome delivery` です。
- `Uchida et al. (2014)` と `Wong et al. (2024)` は `transport-path gating / local vesicle confinement` です。
- `Nakayama et al. (2017)`, `Liau et al. (2023)`, `Espadas et al. (2024)` は `dendritic / synaptic RNA-cargo organization` です。
- `de Queiroz et al. (2025)` は `axonal RNA localization required for long-term memory` です。
- `Aiken & Holzbaur (2024)` は `presynaptic cargo delivery / pausing in human neurons` です。
- よって `one cargo paper` から `the right receptors, RNAs, or presynaptic components reached the right compartment` と読むことはできません。

### 3.3 literature hub 側でこの split が弱いと、サイト全体の front door が崩れます
- `index.md` と `verification.md` はすでに `proteostasis` / `cargo-routing` を route card 付きで分離しています。
- それにもかかわらず `mind_uploading_papers.md` と `research_harvest_50.md` で family split が弱いと、読者は文献入口で再び generic `maintenance support` に戻ってしまいます。
- これは `route family first` というサイトの中心規則に反します。

## 4. 今回実施した修正
- `mind_uploading_papers.md`
  - `known_points` に `local proteostasis` / `cargo-routing` の明示的 split を追加
  - `Read local proteostasis papers through an explicit route-family split` を追加
  - `Read cargo-routing papers through an explicit route-family split` を追加
  - `technical-only shortlist` の `RNA / phospho / proteostasis / cargo split` 行を `Chalatsi et al. (2026)`, `Thomas et al. (2025)`, `de Queiroz et al. (2025)` まで含む形に補強
- `research_harvest_50.md`
  - `note` と `page_highlights` に `proteostasis / cargo front-door sync` を追加
  - `Read U3 local proteostasis papers as a route-family split` を追加
  - `Read U3 cargo-routing papers as a route-family split` を追加
  - literature-shortlist への導線文にも `proteostasis / cargo route-family splits` を明記

## 5. 参考文献
1. Frey U, Morris RGM. Synaptic tagging and long-term potentiation. *Nature*. 1997. https://doi.org/10.1038/385533a0
2. Shires KL, et al. Synaptic tagging and capture in the living rat. *Nat Commun*. 2012. https://doi.org/10.1038/ncomms2250
3. Govindarajan A, et al. The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. *Neuron*. 2011. https://doi.org/10.1016/j.neuron.2010.12.008
4. Fonseca R, et al. A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of late LTP. *Neuron*. 2006. https://doi.org/10.1016/j.neuron.2006.08.015
5. Pandey K, et al. Autophagy coupled to translation is required for long-term memory. *Autophagy*. 2021. https://doi.org/10.1080/15548627.2020.1775393
6. Chalatsi T, et al. Autophagy regulates PVALB (parvalbumin) interneuron excitability and memory. *Autophagy*. 2026. https://doi.org/10.1080/15548627.2025.2597463
7. Lee SH, et al. Identification of long-lived synaptic proteins by proteomic analysis of synaptosome protein turnover. *PNAS*. 2022. https://doi.org/10.1073/pnas.2211572119
8. Thomas M, et al. Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. *Commun Biol*. 2025. https://doi.org/10.1038/s42003-025-08459-0
9. Park M, et al. Recycling endosomes supply AMPA receptors for LTP. *Neuron*. 2006. https://doi.org/10.1016/j.neuron.2006.09.040
10. Correia SS, et al. Motor protein-dependent transport of AMPA receptors into spines during LTP. *Nat Neurosci*. 2008. https://doi.org/10.1038/nn2063
11. Uchida N, et al. Learning-induced microtubule stability governs memory and GluA2 localization. *Nat Commun*. 2014. https://doi.org/10.1038/ncomms5389
12. Wong HH-W, et al. Local confinement of endogenous GluA1 vesicles near stimulated dendrites. *eLife*. 2024. https://doi.org/10.7554/eLife.80622
13. Nakayama K, et al. RNG105/caprin1 is essential for dendritic mRNA localization and long-term memory. *eLife*. 2017. https://doi.org/10.7554/eLife.29677
14. Liau T, et al. Activity-dependent organization of synaptic RNA cargo. *Nat Commun*. 2023. https://doi.org/10.1038/s41467-023-43535-1
15. Espadas I, et al. Spine-targeted RNA support defines a separate cargo route. *Nat Commun*. 2024. https://doi.org/10.1038/s41467-024-46972-8
16. de Queiroz BR, et al. Axonal RNA localization is essential for long-term memory. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-57651-7
17. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Curr Biol*. 2024. https://doi.org/10.1016/j.cub.2024.03.010

## 6. external dependency tasks
- なし

## 7. 検証
- `bundle exec jekyll build` を実行して公開サイト生成が通ることを確認する
- ビルド後に差分と公開文面の整合を確認する
