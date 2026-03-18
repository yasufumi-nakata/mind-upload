# Site Deepening Audit (2026-03-19, Effective Connectivity Route Card)

## 対象

- 主対象: `wiki/observation-to-estimation.md`
- 副対象: `faq.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03 時点の公開サイトは、`観測 != 推定 != 因果検証`、`DCM は候補モデル比較である`、`SCM は介入言語である` という大枠の区別は既にかなり整理できておりました。
- その一方で、公開ページの front door 側では、`effective connectivity` や `DCM` という語自体が、読者に `脳の真の因果配線が発見された` という印象を残しうる状態でした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、tractography や hidden-state の誤読を止めても、`directed graph が出た = causal wiring を見た` という誤読が残れば、WBE に必要な identifiability 基準が再び崩れるからです。

## 根拠付き批判

### 1. `candidate model space` が site-wide に operational rule になっていませんでした

- 問題:
  - `tech_roadmap.md` の R4 は、候補モデル空間・family comparison・model recovery を要求していました。
  - しかし、公開 front door 側には `effective connectivity` 読解の最小提出物がなく、`DCM を使った` という方法名だけで一段強い主張に読める余地が残っていました。
- 根拠:
  - Penny et al. (2004) は、DCM のモデル比較が比較対象のモデル群に依存することを明確にしました。
  - Rosa et al. (2012) は、full model から非常に大きい model space を高速に探索できることを示しました。これは計算上の前進ですが、同時に `真のモデルが自動的に一意化されたわけではない` ことも意味します。
- 批判:
  - したがって、`better model evidence` は `compared model set 内で better` という意味であって、`世界で唯一正しい回路` ではありません。
  - サイト側では、この点を method 名ではなく route-card で固定する必要がありました。

### 2. whole-brain / fast DCM の進歩が、identifiability 解決に読める余地がありました

- 問題:
  - 公開サイトは whole-brain effective connectivity や regression DCM の進歩を前向きに位置づけていました。
  - しかし、その進歩が `tractability の改善` なのか `因果同定の完成` なのかを front door で十分に分離していませんでした。
- 根拠:
  - Frässle et al. (2021) は、>200 regions / >40,000 connections の directed-connectivity 推定を human fMRI で可能にしましたが、同時に `emerging methods require empirical validation` としていました。
  - Wu et al. (2024) は DCM regression を高速化しましたが、Abstract 自体が `computational complexity` を主問題としており、計算速度を 50% 以上削減したことを主要成果として報告しています。
  - rDCM の test-retest 論文は、linearization、fixed HRF、mean-field independence などの simplifications を明示しています。
- 批判:
  - つまり、whole-brain 化や高速化は重要ですが、それは `より多くの候補モデルを現実的に比較できる` 方向の進歩であって、`観測データから真の因果機構を一意に復元できる` という意味ではありません。
  - この distinction がなければ、directed graph を見た時点で causal identity 議論へ飛ぶ誤読が残ります。

### 3. reliability を portability や truth と取り違える余地が残っていました

- 問題:
  - 既存テキストは DCM / effective connectivity の reliability を重要視していましたが、その `適用条件` が明文化されていませんでした。
- 根拠:
  - Frässle et al. (2016) は face-perception network で effective connectivity の test-retest reliability を扱いましたが、これは controlled task / network 条件での話です。
  - Jafarian et al. (2024) は resting-state MEG DCM で close-in-time, similar-circumstance 条件下の reproducibility を示しました。
- 批判:
  - したがって `reliable` は `どの task / session interval / acquisition condition で reliable か` とセットで読まれなければなりません。
  - これを site-wide に固定しないと、同一ラボ・近接条件の repeatability を `general causal portability` に誤って引き上げる余地が残ります。

## 今回実行した変更

- `faq.md`
  - `DCM / effective connectivity` を front door で止める新しい Q&A を追加しました。
  - `effective connectivity` を `model-conditioned causal hypothesis` として読む rule を明文化しました。
  - 参考文献へ Penny (2004), Rosa (2012), Frässle (2016, 2021), Wu (2024), Jafarian (2024) を追加しました。
- `verification.md`
  - page highlights / known points に effective-connectivity route card を追加しました。
  - `If A Paper Says "Effective Connectivity"` という note-box を追加しました。
  - `Log with applicable conditions` に `Effective Connectivity Route Card` を追加しました。
- `tech_roadmap.md`
  - `R4` に 2026-03-19 addendum を追加し、whole-brain / fast DCM を `tractability progress` として読み、identifiability と切り分ける方針を明文化しました。
  - `R4` の required route card 項目を本文基準として固定しました。
  - causal-inference references に新規文献を追加しました。
- `wiki/observation-to-estimation.md`
  - `effective-connectivity route card` 節を新設しました。
  - DCM section に 2026-03-19 の deepening note を追加し、scaling と identifiability を切り分けました。
  - top matter の highlights / known points を route-card 方針に合わせて更新しました。
  - 参考文献へ Rosa (2012), Frässle (2016, 2021), Wu (2024), Jafarian (2024) を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・運用基準・参考文献の改稿で完結しております。

## 参考文献

1. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004;22(3):1157-1172.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
2. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012;208(1):66-78.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
3. Hauser A, Bühlmann P. Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. *Journal of Machine Learning Research*. 2012;13:2409-2464.
   - https://jmlr.org/papers/v13/hauser12a.html
4. Frässle S, Paulus FM, Krach S, Jansen A. Test-retest reliability of effective connectivity in the face perception network. *Human Brain Mapping*. 2016;37(2):730-744.
   - https://doi.org/10.1002/hbm.23061
5. Frässle S, Manjaly ZM, Do CT, Kasper L, Pruessmann KP, Stephan KE. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021;225:117491.
   - https://doi.org/10.1016/j.neuroimage.2020.117491
6. Vink J, Ramos-Nuñez AI, Bellesi A, et al. The brain's functional connectome is a poor predictor of the brain's causal activity flow. *PLOS Computational Biology*. 2020;16(1):e1007866.
   - https://doi.org/10.1371/journal.pcbi.1007866
7. Jafarian A, Assem MK, Kocagoncu E, et al. Reliability of dynamic causal modelling of resting-state magnetoencephalography. *Human Brain Mapping*. 2024.
   - https://doi.org/10.1002/hbm.26782
8. Wu H, Hu X, Zeng Y. A fast dynamic causal modeling regression method for fMRI. *NeuroImage*. 2024;304:120954.
   - https://doi.org/10.1016/j.neuroimage.2024.120954
