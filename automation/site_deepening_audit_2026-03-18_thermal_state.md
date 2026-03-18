# Site Deepening Audit (2026-03-18, Thermal-State Is Not A Background Constant)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`
- 副対象: `faq.md`
- 副対象: `index.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`ionic milieu / chloride homeostasis`、`bioenergetic / mitochondrial state`、`myelin / timing-state`、`glial / clearance support` をかなり良く分解できていました。
- その一方で、`thermal-state` は熱力学ページでは周辺的に触れられるだけで、公開導線や maintenance-state の本文では独立の state class として固定されていませんでした。
- これは技術・自然科学の観点で改善優先度が高いです。なぜなら、同じ connectome、同じ cell type、同じ nominal weights であっても、局所温度が違えば synaptic reliability、membrane kinetics、field-potential amplitude、sequence timing の読みが変わりうるからです。

## 根拠付き批判

### 1. 旧 site は timing-state を myelin / conduction に寄せすぎており、temperature-dependent kinetics を独立変数として前景化していませんでした

- 問題:
  - 既存本文は `myelin / conduction` を timing-state として正しく扱っていました。
  - しかし、`the same delay proxy does not imply the same tissue operating temperature` という読みを止める導線が不足していました。
- 根拠:
  - Hardingham & Larkman (1998) は、rat visual cortex slice で excitatory synaptic transmission の reliability が温度依存であることを示しました。
  - Volgushev et al. (2000) は、rat visual cortical neurons で reversible cooling が membrane properties と spike generation を変えることを示しました。
  - Long & Fee (2008) は、songbird HVC の局所 cooling が song timing を全 timescale で伸張させることを示しました。
- 批判:
  - したがって、`timing-state = conduction delay` と読ませる構図は狭すぎます。
  - thermal-state は timing-state の脚注ではなく、timing-sensitive claim の ceiling を左右する独立 state として書くべきでした。

### 2. 旧 site は field-potential change を学習や maintenance の読みへ寄せる際の thermal confound を十分に前景化していませんでした

- 問題:
  - 既存サイトは shortcut, vascular-state, ionic-state をかなり強く監査していました。
  - しかし、field-potential amplitude 自体が thermal operating point で動きうることは public entry pages では十分に表現されていませんでした。
- 根拠:
  - Moser et al. (1993) は、rats の dentate field excitatory potentials が brain temperature に線形に従い、learning-induced change を mask しうることを示しました。
- 批判:
  - したがって、temperature を暗黙の定数扱いしたまま field-potential change を mechanism 読みに進めるのは危険です。
  - verification rule 側でも thermal-state を disclosure field に加える必要がありました。

### 3. 旧 site は human observability ceiling に ionic / energetic / myelin proxy を置いていたが、human thermometry の evidence class を固定していませんでした

- 問題:
  - site は `macro energetic proxy` や `macro ionic proxy` をよく分離していました。
  - しかし、human brain temperature については `macro thermal proxy` という class label がありませんでした。
- 根拠:
  - Rzechorzek et al. (2022) は、healthy human brain の daily temperature rhythm と 4D thermal map を MRS thermometry で示しました。
- 批判:
  - これは human thermometry が重要である一方、cell-specific thermal-state の ground truth ではないことを意味します。
  - したがって、human thermometry は `macro thermal proxy` と明記し、timing-state や energetic-state の ground truth に昇格させない rule が必要でした。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `thermal-state` を front matter, summary, maintenance-state table, dangerous-misreading table, human observability table, practical rules, minimum submissions に追加
  - `11 maintenance-states` を `12 maintenance-states` に更新
  - `thermal-state is not a background constant` 節を新設し、human thermometry を `macro thermal proxy` と明記
- `verification.md`
  - page highlights / known points / maintenance-state error budget に `thermal-state` を追加
  - `thermal-state is not a background constant` addendum を追加
  - minimum operating rule で thermal-state omission を stop condition に追加
- `wbe_101.md`
  - entry-level hidden-state explanation と hidden-state table に `thermal-state` を追加
  - human MRS thermometry を `macro thermal route` として補足
- `faq.md`
  - `connectome-complete` の限界を説明する短答に thermal-state を追加
  - human thermometry は macro proxy であることを短答レベルで明記
- `index.md`
  - landing page の highlights と maintenance-state note に thermal-state を追加
  - thermal-state を静かに定数扱いしないための入口 note を追加
- `glossary.md`
  - `Maintenance-state` の定義に thermal-state を追加
  - `Thermal-state` の短い用語定義を追加

## 外部依存で保留

- なし
  - 今回は公開本文・検証ルール・監査メモの改稿で完結しています。

## 参考文献

1. Hardingham NR, Larkman AU. The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. *The Journal of Physiology*. 1998;507(1):249-256.
   - https://doi.org/10.1111/j.1469-7793.1998.249bu.x
2. Volgushev M, Vidyasagar TR, Chistiakova M, Yousef T, Eysel UT. Membrane properties and spike generation in rat visual cortical cells during reversible cooling. *The Journal of Physiology*. 2000;522(1):59-76.
   - https://doi.org/10.1111/j.1469-7793.2000.00059.x
3. Moser E, Mathiesen I, Andersen P. Association between brain temperature and dentate field potentials in exploring and swimming rats. *Science*. 1993;259(5099):1324-1326.
   - https://doi.org/10.1126/science.8446900
4. Long MA, Fee MS. Using temperature to analyse temporal dynamics in the songbird motor pathway. *Nature*. 2008;456:189-194.
   - https://doi.org/10.1038/nature07448
5. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022;145(6):2031-2048.
   - https://doi.org/10.1093/brain/awab466
