# Site Deepening Audit (2026-03-25, Tech Roadmap / latent-state family and plasticity route completion)

## 対象

- 主対象: `tech_roadmap.md`
- 同期対象: `summary_booklet.md`

## 今回の選定理由

- 公開導線の中核である `tech_roadmap.md` は、front matter の `page_highlights` ではすでに
  - `R3 / R5 separate latent-state and maintenance-state questions by evidence tier and timescale`
  - `R0 now separates structural scaffold, fast executable state, and maintenance-state families`
  を掲げていました。
- しかし 2026-03-25 JST 時点の live page では、`R3` はほぼ 3 行だけ、`R5` も `Do not learn / Learn with restrictions / Infer to learning rule` という粗い分岐だけで、site-wide rule に比べて本文が追いついていませんでした。
- これは単なる加筆不足ではありません。公開サイトの一番重要な roadmap page で、要約が本文より厳しく、本文が読者に `latent state` と `plasticity` を抽象名詞のまま読ませてしまう構造でした。

## 根拠付き批判

### 1. `R3` が latent state を単一 hidden variable のように読ませていました

- 問題:
  - 旧 `R3` は「観測ノイズから真の状態を分け、予測に効くかを見る」という方向性自体は正しかったです。
  - しかし、`どの state family を recover しているのか`、`どの family を omitted のままにしているのか`、`何日の主張まで支えるのか` が本文で固定されていませんでした。
- 根拠:
  - Lee et al. (2003), Havekes et al. (2016), Vierra et al. (2023), Altas et al. (2024) は、phospho-signaling / second-messenger routing が transcript abundance や bulk proteome とは別の plasticity gate であることを示しました。
  - Frey & Morris (1997), Shires et al. (2012), Govindarajan et al. (2011), Pandey et al. (2021), Chang et al. (2024) は、local proteostasis / tag-capture route が別の integrative unit と turnover window を持つことを示しました。
  - Correia et al. (2008), Swarnkar et al. (2021), Aiken & Holzbaur (2024), de Queiroz et al. (2025) は、cargo-routing が `what reaches the right compartment` という独立 state であり、graph 固定でも plasticity outcome が変わりうることを示しました。
- 批判:
  - したがって、`prediction が上がった latent state` を、そのまま `maintenance-complete latent state` のように読ませるのは過大です。
  - この弱点は Roadmap 入口でこそ止めるべきでした。

### 2. `R5` が plasticity を yes/no スイッチに寄せすぎていました

- 問題:
  - 旧 `R5` は `learning rule を入れるかどうか` を主軸にしており、claim timescale の違いが薄くなっていました。
  - そのままだと、same-session fit、cross-day hold、reconsolidation、remote memory、recovery after perturbation が、同じ `plasticity included` に潰れます。
- 根拠:
  - Frey & Morris (1997), Shires et al. (2012), Govindarajan et al. (2011), Fonseca et al. (2006), Pandey et al. (2021), Chang et al. (2024), Parker et al. (2025) は、late stabilization 自体が単一機構でないことを示しました。
  - Lee et al. (2003), Havekes et al. (2016), Vierra et al. (2023), Rodriguez et al. (2025) は、phospho-state が `current weight` そのものではなく gate / controller として効くことを示しました。
  - Correia et al. (2008), Aiken & Holzbaur (2024), de Queiroz et al. (2025) は、delivery route が変わるだけでも plasticity expression と memory outcome が変わりうることを示しました。
- 批判:
  - したがって、`learning-capable model` と `continuity-preserving plasticity route` を同じ欄に置くのは粗すぎました。
  - Roadmap は `timescale audit` と `submission bundle` まで書いて初めて、他ページの verification rule と整合します。

### 3. site-wide rule と live Roadmap 本文の間に internal inconsistency がありました

- 問題:
  - 既存の `verification.md`, `wbe_101.md`, `wiki/homeostatic-plasticity-and-maintenance-state.md` は、すでに route-card language で phospho / proteostasis / cargo を分解していました。
  - それにもかかわらず Roadmap の `R3/R5` は、読者が最初に見る page であるにもかかわらず、その分解を本文に落としていませんでした。
- 批判:
  - これは public-spec inconsistency です。
  - 入口ページだけが抽象的なままだと、より厳密な奥のページへ進む前に誤読が固定されます。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を `2026-03-25` に更新しました。
  - `page_highlights` / `known_points` に、maintenance-relevant claim で phospho / proteostasis / cargo の開示が必須であることを追加しました。
  - `R3` を全面改稿し、
    - phospho-signaling / second-messenger route
    - local proteostasis / tag-capture route
    - cargo-transport / cytoskeletal trafficking route
    を `fast executable state` と分けて読む table を追加しました。
  - `R3` に `State-family card required for maintenance-relevant R3 claims` を追加し、`State-Continuity Bridge Card` と `Maintenance-State Error Budget` への接続を明記しました。
  - `R5` を claim-timescale audit として改稿し、
    - fixed model / no plasticity claim
    - fixed fast-state model + maintenance disclosure
    - explicit plasticity / maintenance model
    の 3 route と最小提出物を追加しました。
  - `R5` に `Temporal Validity Card`、`State-Continuity Bridge Card`、`Maintenance-State Error Budget` の bundle rule を追加しました。
  - 追記した一次文献を references section に追加しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成し、Roadmap の更新日と要点を同期しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文、監査記録、冊子再生成、ビルド検証で完結できます。

## 参考文献

1. Lee H-K, Barbarosie M, Kameyama K, Bear MF, Huganir RL. Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. *Cell*. 2003.
   - https://doi.org/10.1016/S0092-8674(03)00122-3
2. Havekes R, Park AJ, Tolentino RE, et al. Compartmentalized PDE4A5 signaling impairs hippocampal synaptic plasticity and long-term memory. *Journal of Neuroscience*. 2016.
   - https://doi.org/10.1523/JNEUROSCI.0248-16.2016
3. Vierra NC, et al. Endoplasmic reticulum-plasma membrane junctions couple electrical activity to Ca2+-activated PKA signaling in neurons. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-40930-6
4. Altas B, Tuffy LP, Patrizi A, et al. Region-specific phosphorylation determines Neuroligin-3 localization to excitatory versus inhibitory synapses. *Biological Psychiatry*. 2024.
   - https://doi.org/10.1016/j.biopsych.2023.12.020
5. Rodriguez AC, Kramár EA, Augustynski AS, et al. HDAC3 Serine 424 phospho-mimic and phospho-null mutants bidirectionally modulate long-term memory formation and synaptic plasticity in the adult and aging mouse brain. *Journal of Neuroscience*. 2025.
   - https://doi.org/10.1523/JNEUROSCI.1619-24.2025
6. Frey U, Morris RGM. Synaptic tagging and long-term potentiation. *Nature*. 1997.
   - https://doi.org/10.1038/385533a0
7. Shires KL, Da Silva BM, Hawthorne JP, et al. Synaptic tagging and capture in the living rat. *Nature Communications*. 2012.
   - https://doi.org/10.1038/ncomms2250
8. Govindarajan A, Israely I, Huang SY, Tonegawa S. The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. *Neuron*. 2011.
   - https://doi.org/10.1016/j.neuron.2010.12.008
9. Fonseca R, Vabulas RM, Hartl FU, Bonhoeffer T, Nagerl UV. A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. *Neuron*. 2006.
   - https://doi.org/10.1016/j.neuron.2006.08.015
10. Pandey K, Yu X-W, Steinmetz A, Alberini CM. Autophagy coupled to translation is required for long-term memory. *Autophagy*. 2021.
   - https://doi.org/10.1080/15548627.2020.1775393
11. Chang YC, Gao Y, Lee JY, et al. Identification of secretory autophagy as a mechanism modulating activity-induced synaptic remodeling. *Proceedings of the National Academy of Sciences USA*. 2024.
   - https://doi.org/10.1073/pnas.2315958121
12. Parker D, Davidson K, Osmulski PA, et al. Proteasome augmentation mitigates age-related cognitive decline in mice. *Aging Cell*. 2025.
   - https://doi.org/10.1111/acel.14492
13. Correia SS, Bassani S, Brown TC, et al. Motor protein-dependent transport of AMPA receptors into spines during long-term potentiation. *Nature Neuroscience*. 2008.
   - https://doi.org/10.1038/nn2063
14. Swarnkar S, Avchalumov Y, Espadas I, et al. Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. *Cell Reports*. 2021.
   - https://doi.org/10.1016/j.celrep.2021.109369
15. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Current Biology*. 2024.
   - https://doi.org/10.1016/j.cub.2024.03.010
16. de Queiroz BR, et al. Axonal RNA localization is essential for long-term memory. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-57651-7
