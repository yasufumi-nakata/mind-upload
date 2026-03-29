# Site Deepening Audit (2026-03-29, front-door state-continuity witness rule)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
  - `wbe_101.md`
- 同期対象:
  - `summary_booklet.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## web確認対象

- `https://doi.org/10.1038/s41467-022-30199-6`
- `https://doi.org/10.1038/s41586-025-08790-w`
- `https://doi.org/10.1038/s41593-019-0555-4`
- `https://doi.org/10.1038/s41593-025-01982-7`
- `https://doi.org/10.1126/sciadv.abj0751`
- `https://doi.org/10.3389/fnhum.2021.672946`
- `https://doi.org/10.1038/s41467-025-59652-y`
- `https://doi.org/10.1038/s41551-025-01536-z`
- `https://doi.org/10.1038/s41586-025-09127-3`
- `https://doi.org/10.1016/j.crmeth.2023.100520`
- `https://doi.org/10.1523/ENEURO.0104-23.2023`
- `https://doi.org/10.1038/s41593-023-01498-y`
- `https://doi.org/10.1038/s41598-024-70609-x`

## 今回この箇所を選んだ理由

- 2026-03-28 の再監査で、`wiki/state-continuity-bridge.md` と `verification.md#state-continuity-bridge-card` には
  - `carried object / witness`
  - `tolerance / failure rule`
  - `rescue route`
  が導入されていました。
- しかし front door 側の `index.md`、`faq.md`、`wbe_101.md` は、依然として bridge burden を主として
  - elapsed time
  - regime continuity
  - coordinate transfer
  - bridge validation
  で読む構造に寄っておりました。
- そのままでは入口ページだけ読んだ読者が
  - `same-subject`
  - `same-brain`
  - `stable score across days`
  - `same-brain correlative workflow`
  を、まだ一段強く `same-state continuity` と誤読する余地が残ります。

## 主要結論

- `same-subject / same-brain` の front-door stop rule は、2026-03-29 時点の一次文献に対してまだ弱すぎました。
- 一次文献の現在地では、少なくとも入口でも次を分けて読まなければなりません。
  - specimen identity
  - carried object / witness
  - tolerance / failure rule
  - rescue route
- よって front door では
  - `same-subject = specimen identity only`
  - `stable score = possibly witness-specific or rescue-dependent stability`
  と止める必要がございました。

## 根拠付き批判

### 1. same-brain correlative workflow は one global state object を carry していません

- [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6) は correlative in vivo physiology から synchrotron microtomography と SBEM へつなぐ multistage workflow を示しました。
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) も、in vivo measurements の後に fixation, histology, sectioning を置く sequential pipeline を明示しています。

批判:

- これらは強い same-brain workflow ですが、carry しているのは global same-state ではなく、landmarks、targeted subvolumes、local structure-function correspondences でございます。
- それにもかかわらず front door が elapsed time / coordinate transfer だけで止まると、読者は `same-brain` を one global state sample に近いものと誤読しやすくなります。

### 2. bridge で安定しうる object は一種類ではありません

- [Gallego et al. (2020)](https://doi.org/10.1038/s41593-019-0555-4) は、recorded neurons が入れ替わっても latent dynamics が安定しうることを示しました。
- [Noda et al. (2025)](https://doi.org/10.1038/s41593-025-01982-7) は、selective neuron loss 後にも representational map の homeostasis を示しました。
- [Van De Ville et al. (2021)](https://doi.org/10.1126/sciadv.abj0751) は、brain fingerprints の identifiability が timescale に依存することを示しました。
- [Di et al. (2021)](https://doi.org/10.3389/fnhum.2021.672946) は、resting-state EEG identification の time robustness が feature family に依存することを示しました。

批判:

- つまり安定する witness は
  - latent manifold
  - representational map / geometry
  - fingerprint feature family
  のように複数あり、しかも failure mode が違います。
- したがって front door が `same-state continuity` を generic bridge burden の一語で止めるだけでは不十分で、`what object survived?` を明示しなければなりません。

### 3. stable performance は raw continuity の証拠とは限りません

- [Karpowicz et al. (2025)](https://doi.org/10.1038/s41467-025-59652-y) は latent-dynamics alignment により decoding stability を改善しました。
- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は hidden Markov model による unsupervised recalibration で cursor BCI の長期安定化を示しました。
- [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は強い speech neuroprosthesis advance を示しましたが、site rule 上は fixed-decoder durability とは別に読む必要があります。

批判:

- これらは `stable use` が
  - alignment
  - recalibration
  - short fixed-decoder horizon
  のどれで支えられているかを分けて読まなければならないことを示します。
- よって `score stayed good` を same-state continuity の shorthand として front door で許してはいけませんでした。

### 4. drift burden は elapsed time だけではありません

- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520) と [Idziak et al. (2023)](https://doi.org/10.1523/ENEURO.0104-23.2023) は preservation / fixation 自体が transformation であることを示しました。
- [Benisty et al. (2024)](https://doi.org/10.1038/s41593-023-01498-y) は spontaneous behavior が activity magnitude と functional connectivity を変えることを示しました。
- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) は 10-hour EEG dynamics が decoder-relevant drift を生むことを示しました。

批判:

- bridge risk は elapsed time だけでなく
  - transformation class
  - carried object
  - rescue dependence
  を含むべきでございます。
- front door がこの点を落とすと、deep page で導入済みの state-continuity rule が入口で弱くなります。

## 今回実行した変更

- `index.md`
  - front matter に
    - `named bridge witness`
    - `landmarks / latent manifolds / representational geometry / fingerprint features`
    - `alignment / recalibration / short fixed-decoder horizon`
    を追加しました。
  - note box `If You Are Treating Same-Subject As Same-State` を改稿し、
    - carried object / witness
    - tolerance / failure rule
    - rescue route
    を front door でも要求する文面へ更新しました。

- `faq.md`
  - front matter の ten-guardrail bullet を、bridge witness / tolerance / rescue route を含む形に強化しました。
  - `known_points` に、same-subject bridge で安定しうる object family と rescue dependence を追加しました。
  - front-door note `Ten technical guards now fixed at the front door` に bridge-specific stop rule を追記しました。
  - `Q2e` を改稿し、same-subject / same-brain claim を
    - specimen identity
    - carried object / witness
    - tolerance / failure rule
    - rescue route
    の順に止める構成へ更新しました。
  - checklist を `Four checks` から `Six checks` へ拡張しました。

- `wbe_101.md`
  - front matter に bridge witness rule を追加しました。
  - note box `Same-subject is still not same-state when the bridge is sequential` を改稿し、front door でも
    - landmarks / subvolumes
    - latent manifolds / representational maps / fingerprint features
    - alignment / recalibration / fixed-decoder horizon
    を別 object として読むよう更新しました。

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成し、front matter 由来の新しい bridge stop rule を同期しました。

## 今回止めた誤読

- `same-subject` = `same-state`
- `same-brain workflow` = `one global latent state survived`
- `stable score across days` = `raw continuity of the same neural object`
- `correlative bridge burden = elapsed time only`
- `bridge validation done` = `witness type and tolerance no longer matter`

## 外部依存タスク

- なし
  - 今回の変更は web 上の一次文献確認、repo 内公開ページ改稿、要約再生成、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Bosch C, Pacureanu A, Patino J, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
2. MICrONS Consortium, Bae JA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
3. Gallego JA, Perich MG, Miller LE, Solla SA. Long-term stability of cortical population dynamics underlying consistent behavior. *Nature Neuroscience*. 2020.
   - https://doi.org/10.1038/s41593-019-0555-4
4. Noda T, Takahashi N, Takahashi H, et al. Homeostasis of a representational map in the neocortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01982-7
5. Van De Ville D, Amico E, Abbas K, et al. When makes you unique: temporality of the human brain fingerprint. *Science Advances*. 2021.
   - https://doi.org/10.1126/sciadv.abj0751
6. Di Y, An X, Zhong W, Liu S, Ming D. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. *Frontiers in Human Neuroscience*. 2021.
   - https://doi.org/10.3389/fnhum.2021.672946
7. Karpowicz BM, Aghagolzadeh M, Shah NP, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-59652-y
8. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
9. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
10. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023.
    - https://doi.org/10.1016/j.crmeth.2023.100520
11. Idziak A, Inavalli VVGK, Bancelin S, Arizono M, Nagerl UV. The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. *eNeuro*. 2023.
    - https://doi.org/10.1523/ENEURO.0104-23.2023
12. Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. *Nature Neuroscience*. 2024.
    - https://doi.org/10.1038/s41593-023-01498-y
13. Egger J, Kostoglou K, Müller-Putz GR. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
    - https://doi.org/10.1038/s41598-024-70609-x
