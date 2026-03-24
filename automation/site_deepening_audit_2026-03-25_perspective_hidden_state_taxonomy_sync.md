# Site Deepening Audit (2026-03-25, perspective hidden-state taxonomy sync)

## 今回この箇所を選んだ理由

- 今回の主対象は `perspective.md` の `Gap between connectome and dynamics` 節です。
- 前回までの自動更新で `human proxy composition` と `intrinsic excitability` は強化済みでしたが、長文ノートの中心ページではまだ `15-class maintenance / hidden-state problem` という古い数え方が残っておりました。
- その一方で、現行サイト側の運用ルールはすでに `phospho-signaling / second-messenger state`、`neuromodulatory specificity / transmitter context`、`firing-rate set point / recovery controller`、`shared extracellular / electrical state` を別々の inferential object として扱っております。
- つまり、入口に近い長文ノートが、現在の route-card 体系より粗い taxonomy を残しており、読者に `connectome + cell type` が実際より state-complete に近いかのような印象を与えうる状態でした。

## 観察した問題

### 1. `perspective.md` の数え方が現行 taxonomy に追いついておりませんでした

- front matter の `page_highlights` にはまだ `15-class maintenance / hidden-state problem` と書かれております。
- しかし現行サイトでは、少なくとも以下は別系統の stop rule としてすでに運用されております。
  - `intrinsic excitability / AIS / ion-channel configuration`
  - `firing-rate set point / recovery controller`
  - `phospho-signaling / second-messenger state`
  - `neuromodulatory specificity / transmitter context`
  - `shared extracellular / electrical state`
- 特に `firing-rate set point` を `intrinsic excitability` に畳み込んだままにすると、`allocation bias` と `post-perturbation recovery controller` が同じ evidence class であるかのように読めてしまいます。これは現在のサイト規律と一致しません。

### 2. `phospho-signaling` と `neuromodulatory specificity` の omission が科学的に弱い圧縮でした

- phospho-signaling は transcript abundance や bulk proteome と同じ object ではありません。AMPA receptor phosphosite gating と compartmentalized second-messenger routing は、同じ `gene expression` や `weight snapshot` から自動では復元されません。
  - Lee et al. (2003), Cell, doi:10.1016/S0092-8674(03)00122-3
  - Tomita et al. (2005), Neuron, doi:10.1016/j.neuron.2005.01.009
  - Vierra et al. (2023), Nat Commun, doi:10.1038/s41467-023-40930-6
  - Rodriguez et al. (2025), J Neurosci, doi:10.1523/JNEUROSCI.1619-24.2025
- neuromodulatory evidence も `one mood scalar` ではありません。pupil-linked mixed arousal proxy、local transmitter sensing、receptor/transporter atlas prior、occupancy PET、displacement / release proxy は別の inferential object です。
  - Reimer et al. (2016), Nat Commun, doi:10.1038/ncomms13289
  - Hansen et al. (2022), Nat Neurosci, doi:10.1038/s41593-022-01186-3
  - Neyhart et al. (2024), Cell Reports, doi:10.1016/j.celrep.2024.114808
  - Wong et al. (2013), Psychopharmacology, doi:10.1007/s00213-013-3103-z
- よって `perspective.md` でこの 2 系統が hidden-state table から落ちたままだと、現行の route-card stop rule を長文ノート自体が弱めてしまいます。

### 3. taxonomy の数字が公開ページ間で揺れておりました

- `perspective.md` は `15-class`
- `summary_booklet.md` はその front matter を再利用するため同じ `15-class`
- `wiki/homeostatic-plasticity-and-maintenance-state.md` は見出しが `16 maintenance-states to fix first` なのに、本文 table には実際には 17 行あります
- これは単なる見栄えの問題ではなく、どこまでを独立の latent family として監査するかがページごとにずれて見える、という public-spec inconsistency です。

## 今回実行する変更

- `perspective.md`
  - `15-class` 表現をやめ、`17 maintenance-state families plus a separate shared electrical-state class` へ改めます。
  - hidden-state paragraph を現行 taxonomy に同期し、`phospho-signaling` と `neuromodulatory specificity` を明示します。
  - table を route-card 現行運用に近い粒度へ改稿し、`firing-rate set point / recovery controller` を独立させます。
  - どの rule が `homeostatic-plasticity-and-maintenance-state` にあり、どの rule が `connectome-is-not-enough` の electrical-state route card にあるかを読者に見える形へします。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - section title の `16 maintenance-states` を table 実体に合わせて修正します。
- `summary_booklet.md`
  - 生成スクリプトで再生成し、公開冊子側にも古い `15-class` が残らないようにします。

## 修正しないもの

- `issue.md` の論点整理は今回は前提として扱い、再監査しません。
- 哲学・法学・personhood 側の議論は今回の修正対象に含めません。
- route card 本体の新設は今回は行わず、既存 route-card 体系へ `perspective` を同期することを優先します。

## 参考文献

- Lee, H.-K., et al. (2003). Cell. doi:10.1016/S0092-8674(03)00122-3
- Tomita, S., et al. (2005). Neuron. doi:10.1016/j.neuron.2005.01.009
- Vierra, N. C., et al. (2023). Nature Communications. doi:10.1038/s41467-023-40930-6
- Rodriguez, G. A., et al. (2025). Journal of Neuroscience. doi:10.1523/JNEUROSCI.1619-24.2025
- Reimer, J., et al. (2016). Nature Communications. doi:10.1038/ncomms13289
- Hansen, J. Y., et al. (2022). Nature Neuroscience. doi:10.1038/s41593-022-01186-3
- Neyhart, E. J., et al. (2024). Cell Reports. doi:10.1016/j.celrep.2024.114808
- Wong, D. F., et al. (2013). Psychopharmacology. doi:10.1007/s00213-013-3103-z
