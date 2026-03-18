# Site Deepening Audit (2026-03-18, Front-Door Bioenergetic / Mitochondrial Alignment)

## 対象

- 主対象: `wbe_101.md`
- 副対象: `faq.md`
- 副対象: `verification.md`
- 副対象: `index.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 公開サイトにはすでに `wiki/homeostatic-plasticity-and-maintenance-state.md` があり、そこでは `bioenergetic / mitochondrial state` を独立した maintenance-state としてかなり深く扱っていました。
- しかし、入口導線である `index.md`、`wbe_101.md`、`faq.md`、`verification.md`、`glossary.md` では、この層がまだ `glial / metabolic support` に吸収されやすい状態でした。
- これは技術・自然科学の観点で修正優先度が高いです。なぜなら、同じ connectome、同じ cell type、同じ astrocyte support があっても、局所 ATP 供給、mitochondrial positioning、fission / fusion、redox reserve が違えば、反復刺激時の信頼性や dendritic plasticity の上限はまだ変わりうるからです。

## まず改善優先度が高い箇所

### 1. WBE 101 の hidden-state 表が bioenergetic / mitochondrial state を独立行として示していませんでした

- 問題:
  - 入口ページの hidden-state 表は `ionic milieu / chloride homeostasis` までは独立層として前面化されていましたが、局所 energetic mechanism は `glial / metabolic support` の中へ埋もれていました。
- 批判:
  - これでは読者が `代謝の話は astrocyte やグリアを読めば十分` と誤読します。
  - しかし、一次文献はそうは言っていません。ニューロン局所の ATP 供給とミトコンドリア配置は、それ自体で可塑性の制約条件です。

### 2. FAQ が connectome-complete の限界を説明する際に energetic state を十分に分離できていませんでした

- 問題:
  - FAQ は「connectome と cell type だけでは足りない」を短く整理できていましたが、bioenergetic / mitochondrial state が短答導線に入っていませんでした。
- 批判:
  - FAQ は入口の誤読を潰すページです。ここで energetic state が抜けると、その後の読者は `timing と glia を見れば maintenance-state はだいたい押さえた` と誤解しやすくなります。

### 3. Verification の maintenance-state error budget が energetic route と glial route の差を本文で十分に説明していませんでした

- 問題:
  - `Bioenergetic support` 行自体は存在していましたが、本文上は `glial / astrocyte support` との差がなお薄く、読者が両者を一つの support-state として読める余地が残っていました。
- 批判:
  - 検証ルールは、区別すべき latent state を区別したまま提出要求へ落としていなければ意味がありません。
  - とくに repeated-burst reliability や dendritic plasticity を含む主張では、astrocyte support と mitochondrial micro-organization を分けて書かなければ claim ceiling を下げ切れません。

## 根拠付きの批判

### 1. 局所 ATP 供給は glial support の別名ではありません

- <https://doi.org/10.1016/j.cell.2013.12.042> Rangaraju et al. (2014) は、activity-driven local ATP synthesis が presynaptic function に必要であることを示しました。
- <https://doi.org/10.1016/j.cell.2018.12.013> Rangaraju et al. (2019) は、spatially stable mitochondrial compartments が plasticity 時の local translation を支えることを示しました。
- <https://doi.org/10.1016/j.neuron.2018.09.025> Divakaruni et al. (2018) は、LTP induction に rapid な dendritic mitochondrial fission が必要であることを示しました。
- <https://doi.org/10.1038/s41467-023-44233-8> Bapat et al. (2024) は、dendrite 上で stabilised された mitochondria が局所 plasticity を支えることを示しました。
- <https://doi.org/10.1038/s42003-025-08963-3> Hu et al. (2025) は、learning / plasticity signal に応じて synaptic mitochondria 内 ATP synthase の空間配置が変わることを示しました。

以上から、`glial / metabolic support を見た` と `neuronal local bioenergetics を見た` は同義ではありません。前者は support route の一部にすぎず、後者は局所 plasticity mechanism そのものにかかる state です。

### 2. human energetic imaging も、まだ local mitochondrial state の ground truth ではありません

- <https://doi.org/10.1002/nbm.3384> Ren et al. (2015) は 31P-MRS により ATP synthesis、metabolite concentration、pH を測定しました。
- <https://doi.org/10.1093/pnasnexus/pgaf072> Li et al. (2025) は dynamic DMRSI により whole-brain の glucose transport、CMRGlc、VTCA を 7T で定量化しました。

しかし、これらが押し上げたのはあくまで macro energetic proxy です。どの dendritic branch の ATP reserve が不足しているか、どの synapse 近傍に mitochondria が停泊しているか、どの compartment で fission/fusion balance が崩れているかまでは直接示しません。したがって、human energetic imaging を local mitochondrial state の ground truth として扱うのは過剰主張です。

### 3. よって公開導線でも `timing-state`, `bioenergetic / mitochondrial state`, `glial / astrocyte support` を分ける必要があります

- timing-state は conduction と synchrony の変動源です。
- bioenergetic / mitochondrial state は local ATP reserve と plasticity mechanism の変動源です。
- glial / astrocyte support は lactate shuttle、astrocyte ensemble、slow support-state の変動源です。

この 3 つは重なりはあっても、同じ state class ではありません。入口ページでまとめてしまうと、Verification の claim ceiling が入口説明の時点で曖昧に戻ります。

## 今回実行した変更

- `index.md`
  - landing page の要約文と maintenance-state note で `bioenergetic / mitochondrial support` を独立表示
- `wbe_101.md`
  - front matter の highlights / known points を更新
  - hidden-state 段落に bioenergetic / mitochondrial state の一次文献を追加
  - hidden-state table に独立行を追加
  - 31P-MRS / dynamic DMRSI を macro energetic route として明記
  - 参考文献を追加
- `faq.md`
  - `connectome-complete` に関する短答へ energetic state を追加
  - 31P-MRS / dynamic DMRSI の observability ceiling を短答の中で明記
  - Looser et al. (2024) の DOI を `10.1038/s41593-023-01558-3` に修正
  - 参考文献を追加
- `verification.md`
  - maintenance-state error budget の導入文と row 名を更新
  - energetic route と glial route を分ける note を追加
  - minimum operating rule で energetic support と glial support を分離
  - 参考文献を追加
- `glossary.md`
  - `Maintenance-state` の定義に `bioenergetic / mitochondrial support` を追加

## 外部依存で保留

- なし
  - 今回は公開本文・用語・監査ルールの改稿で完結しています。

## 参考文献

1. Rangaraju V, Calloway N, Ryan TA. Activity-driven local ATP synthesis is required for synaptic function. *Cell*. 2014.
   - <https://doi.org/10.1016/j.cell.2013.12.042>
2. Rangaraju V, Lauterbach M, Schuman EM. Spatially stable mitochondrial compartments fuel local translation during plasticity. *Cell*. 2019.
   - <https://doi.org/10.1016/j.cell.2018.12.013>
3. Divakaruni SS, Van Dyke AM, Chandra R, et al. Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. *Neuron*. 2018.
   - <https://doi.org/10.1016/j.neuron.2018.09.025>
4. Bapat P, Nirschl JJ, Wilkerson JR, et al. VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. *Nature Communications*. 2024.
   - <https://doi.org/10.1038/s41467-023-44233-8>
5. Hu H, Tang J, Wu Y, et al. Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. *Communications Biology*. 2025.
   - <https://doi.org/10.1038/s42003-025-08963-3>
6. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - <https://doi.org/10.1002/nbm.3384>
7. Li X, Zhu XH, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - <https://doi.org/10.1093/pnasnexus/pgaf072>
