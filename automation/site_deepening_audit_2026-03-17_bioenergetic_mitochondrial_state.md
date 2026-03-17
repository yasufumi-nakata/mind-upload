# Site Deepening Audit (2026-03-17, Bioenergetic / Mitochondrial State Ceiling)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`connectome-complete ≠ emulation-complete`、`same-day fit ≠ cross-day maintenance`、`human macro scaffold ≠ local ground truth` をかなり明確に区別できていました。
- その一方で、`bioenergetic / mitochondrial state` はなお `glial / metabolic support` や `macro biochemical scaffold` に吸収されやすく、読者が `代謝の話は全部ひとまとめでよい` と誤読する余地が残っていました。
- これは技術・自然科学の観点で優先度が高い弱点です。なぜなら、同じ connectome、同じ cell type、同じ astrocyte support があっても、局所 ATP 供給、mitochondrial positioning、fission / fusion、redox reserve が違えば、反復刺激時の信頼性や dendritic plasticity の上限はまだ変わりうるからです。

## 主要な批判点

### 1. 旧サイトは `glial / metabolic support` と `bioenergetic / mitochondrial state` を十分に分離できていませんでした

- 問題:
  - 既存本文は astrocyte-neuron lactate shuttle、astrocyte ensemble、slow metabolic support を正しく重視していました。
  - しかし、ニューロン局所の ATP 供給とミトコンドリア配置までを独立の latent state としては切り出せていませんでした。
- 根拠:
  - Rangaraju et al. (2014) は activity-driven local ATP synthesis が presynaptic function に必要であることを示しました。
  - Rangaraju et al. (2019) は spatially stable mitochondrial compartments が plasticity 時の local translation を支えることを示しました。
  - Divakaruni et al. (2018) は LTP induction に rapid な dendritic mitochondrial fission が必要であることを示しました。
  - Bapat et al. (2024) は dendrite 上で stabilised された mitochondria が局所 plasticity を支えることを示しました。
  - Hu et al. (2025) は synaptic mitochondria 内 ATP synthase の極性化が learning / plasticity signal に応じて変わることを示しました。
- 批判:
  - したがって、`glial support を見た` と `neuronal local bioenergetics を見た` は同義ではありません。

### 2. 旧サイトは `human metabolic connectome` と `human energetic proxy` の違いを本文導線に十分反映できていませんでした

- 問題:
  - human 側の前進は既にかなり丁寧に整理されていましたが、`5-metabolite parcel covariance` と `ATP / glucose turnover` が別の measurement class だという区別が薄く残っていました。
- 根拠:
  - Lucchetti et al. (2025) が押し上げたのは 5 代謝物の parcel-level covariance に基づく macro-biochemical scaffold です。
  - Ren et al. (2015) は 31P-MRS で ATP synthesis、metabolite concentrations、pH を示しました。
  - Li et al. (2025) は dynamic deuterium metabolic imaging で whole-brain glucose metabolic turnover を示しました。
- 批判:
  - したがって、`human metabolic connectome`、`human energetic imaging`、`cell-specific mitochondrial state` を同一視してはなりません。

### 3. 旧サイトは `repeated-burst reliability` と `dendritic plasticity energetic mechanism` の棄権条件を検証ページへ落とし切れていませんでした

- 問題:
  - verification 側には `glial / slow-state support` と `delay / myelin / axonal support` はありましたが、energetic mechanism を止める専用 row がありませんでした。
- 批判:
  - これでは `macro metabolic proxy が少しある` だけで、局所 energetic mechanism まで扱えたように誤読されます。
- 修正:
  - latent-state error budget に `bioenergetic / mitochondrial state` を独立行として追加し、energetic log が無い場合の棄権条件を明記しました。

### 4. 旧サイトはロードマップ上で `bioenergetic / mitochondrial state` を実装課題へ十分落とせていませんでした

- 問題:
  - Wiki で latent state として扱っても、Roadmap の R3/R5 で別行になっていないと、結局どの提出物に何を要求するかが曖昧に戻ります。
- 批判:
  - 技術ロードマップでは、`何が state variable か` と `何を提出物にするか` が一致していなければなりません。
- 修正:
  - `tech_roadmap.md` に `bioenergetic / mitochondrial state` を latent-state class として追加し、remote-memory claim 時の site rule にも組み込みました。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `bioenergetic / mitochondrial state` を 10 番目の状態クラスとして追加
  - timescale matrix に独立行を追加
  - human metabolic connectome の限界説明へ `local ATP reserve / mitochondrial positioning` 不可視性を追加
  - 参考文献へ Rangaraju (2014, 2019), Divakaruni (2018), Bapat (2024), Hu (2025), Ren (2015), Li (2025) を追加
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - maintenance-state を 8 クラスへ更新
  - `bioenergetic / mitochondrial state は glial support の別名ではありません` 節を追加
  - human observability 表へ `human energetic imaging` 行を追加
  - dangerous misreadings / site rules / claim table に energetic-mechanism の監査項目を追加
  - 参考文献へ同上の一次文献を追加
- `wbe_101.md`
  - hidden state 4 層の説明へ `bioenergetic / mitochondrial state` を追加
  - evidence table と hidden-state summary に energetic state を追加
  - human observability の短縮説明へ energetic proxy の上限を追加
  - 参考文献へ同上の一次文献を追加
- `verification.md`
  - latent-state error budget に `bioenergetic / mitochondrial state` 行を追加
  - `bioenergetic proxy は glial support の別名ではありません` note を追加
  - state-completeness gate を 8 状態クラスへ更新
  - 参考文献へ同上の一次文献を追加
- `tech_roadmap.md`
  - latent-state / maintenance-state の壁に `bioenergetic / mitochondrial state` を追加
  - R3 の latent-state class 表に独立行を追加
  - R5 の site rule に energetic state を追加

## 外部依存で保留

- なし
  - 今回の修正は、公開本文と監査ルールの改稿で完結しています。

## 参考文献

1. Rangaraju V, Calloway N, Ryan TA. Activity-driven local ATP synthesis is required for synaptic function. *Cell*. 2014.
   - https://doi.org/10.1016/j.cell.2013.12.042
2. Rangaraju V, Lauterbach M, Schuman EM. Spatially stable mitochondrial compartments fuel local translation during plasticity. *Cell*. 2019.
   - https://doi.org/10.1016/j.cell.2018.12.013
3. Divakaruni SS, Van Dyke AM, Chandra R, et al. Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. *Neuron*. 2018.
   - https://doi.org/10.1016/j.neuron.2018.09.025
4. Bapat P, Nirschl JJ, Wilkerson JR, et al. VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-023-44233-8
5. Hu H, Tang J, Wu Y, et al. Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. *Communications Biology*. 2025.
   - https://doi.org/10.1038/s42003-025-08963-3
6. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
7. Li J, Xu HN, Yuan J, et al. Dynamic deuterium metabolic imaging reveals whole-brain glucose metabolic turnover and neuronal function in humans. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf079
