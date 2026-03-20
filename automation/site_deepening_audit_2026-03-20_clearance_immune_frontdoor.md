# Site Deepening Audit (2026-03-20, Clearance / Immune Support Front Door)

## 対象

- 主対象: `index.md`, `wbe_101.md`, `faq.md`, `verification.md`
- 補助対象: `glossary.md`, `perspective.md`, `wiki/homeostatic-plasticity-and-maintenance-state.md`

## 今回の選定理由

- 2026-03-20 時点で、wiki 側では `clearance / immune support` を独立した maintenance-state としてかなり明示できていました。
- その一方で、公開入口側ではなお `clearance` が `slow support` の一部として読めても、`passive cleanup` と `local controller readout` の両方向の誤読を十分に止め切れていませんでした。
- これは技術・自然科学の観点で優先度が高いです。一次文献が示しているのは、`clearance / immune support` が synaptic physiology や multiday recovery と関わる独立 state である一方、現在の human route はなお `macro support-state proxy` に留まるという二重境界だからです。

## 根拠付き批判

### 1. 旧フロントドアは `clearance / immune support` をまだ一般的な support background として読みうる状態でした

- 問題:
  - `index.md`, `wbe_101.md`, `faq.md`, `verification.md` には clearance への言及が既にありました。
  - しかし公開入口での主な強調は `proxy class` や `maintenance-state budget` 側に寄っており、`clearance / immune support is not passive cleanup` が front door wording としてはまだ弱めでした。
- 根拠:
  - Louveau et al. (2015) は CNS lymphatic vessels の構造と機能を示しました。
  - Ahn et al. (2019) は skull-base meningeal lymphatic vessels が CSF を排出することを示しました。
  - Kim et al. (2025) は meningeal-lymphatics-microglia axis が synaptic physiology を調節することを示しました。
- 批判:
  - 以上を踏まえると、clearance を単なる cleanup metaphor や一般的 support background として読む余地は、現在の一次文献に対して粗すぎます。

### 2. ただし human 側の前進を `local immune controller` へ昇格させるのも誤りです

- 問題:
  - clearance を前面化すると、逆向きの誤読、すなわち `human glymphatic evidence now reads local maintenance logic` も起こりえます。
- 根拠:
  - Eide & Ringstad (2021) はヒトで睡眠剥奪により molecular clearance が低下することを示しましたが、local controller の同定ではありません。
  - Hirschler et al. (2025) は region-specific CSF mobility driver を MRI で示しましたが、flux 自体の直接測定ではありません。
  - Dagum et al. (2026) は healthy older adults を対象に、investigational device と multicompartment model を通じて overnight Aβ / tau clearance to plasma を論じましたが、やはり local synaptic maintenance controller を読んでいるわけではありません。
- 批判:
  - したがって site rule は二段階であるべきです。
  - `clearance / immune support is a real multiday support-state` と同時に、`current human clearance evidence is still macro support-state proxy` を front door で明示しなければなりません。

### 3. 参照整合性にも弱点があり、一次文献への導線の精度が落ちていました

- 問題:
  - 関連ページの一部で Eide & Ringstad (2021) の DOI が `10.1093/brain/awab285` と記載されていました。
- 根拠:
  - 一次文献の正しい DOI は `10.1093/brain/awaa443` です。
- 批判:
  - front door deepening は本文内容だけでなく reference integrity も含みます。
  - DOI がずれていれば、根拠付き批判としての再検証可能性が下がります。

## 今回実行した変更

- `index.md`
  - front matter の `page_highlights` / `known_points` を clearance / immune support に同期しました。
  - front-door note `If You Are Treating Clearance As Passive Cleanup Or As Direct Readout` を追加しました。
  - maintenance-state note 内の `clearance proxies` を `clearance / immune proxy class` へ更新しました。
- `wbe_101.md`
  - `page_highlights` / `known_points` に clearance / immune support を追加しました。
  - human observability ladder の clearance row を `meningeal-lymphatic segment responsibility` まで明示する形へ更新しました。
  - note box `Clearance / immune support is not passive cleanup` を追加しました。
  - 参考文献へ Louveau / Ahn / Kim / Eide を追加しました。
- `faq.md`
  - `known_points` と Q2c を clearance / immune support に同期しました。
  - Q2d table の missing column へ `local immune-controller / synaptic-maintenance logic` を追加しました。
  - human clearance evidence の safe reading paragraph を追加しました。
  - 参考文献へ Louveau / Ahn / Kim / Eide を追加しました。
- `verification.md`
  - `page_highlights` / `known_points` に clearance / immune support ceiling を追加しました。
  - maintenance-state error budget の clearance row を meningeal-lymphatic / CSF-interstitial / microglia-related wording へ更新しました。
  - note box `2026-03-20 addendum: clearance / immune support is not passive cleanup` を追加しました。
  - 参考文献へ Louveau / Ahn / Kim / Eide を追加しました。
- `glossary.md`
  - `page_highlights` / `known_points` を clearance / immune support に同期しました。
  - `Clearance / immune support` 項目を追加しました。
  - `Support-state proxy` 定義を clearance ceiling に合わせて更新しました。
- `perspective.md`
  - clearance / immune support を論じる文脈で Ahn et al. (2019) を追加しました。
  - Eide & Ringstad (2021) の DOI を `awaa443` へ修正しました。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - clearance section に Ahn et al. (2019) を追加しました。
  - Eide & Ringstad (2021) の DOI を `awaa443` へ修正しました。

## 外部依存で保留

- human same-subject local immune-controller ground truth
  - 担当者: 実験系共同研究者 / 高分解能ヒト計測系研究者
  - 前提条件: meningeal-lymphatic, CSF-interstitial, microglia-related maintenance controller を living human brain で局所かつ longitudinal に較正できる計測系
  - 完了条件: local synaptic maintenance / immune-controller state を human longitudinal setting で比較可能にする公開 benchmark または因果介入ルートが整備されること

## 参考文献

1. Louveau A, Smirnov I, Keyes TJ, et al. Structural and functional features of central nervous system lymphatic vessels. *Nature*. 2015;523:337-341.
   - https://doi.org/10.1038/nature14432
2. Ahn JH, Cho H, Kim J-H, et al. Meningeal lymphatic vessels at the skull base drain cerebrospinal fluid. *Nature*. 2019;572:62-66.
   - https://doi.org/10.1038/s41586-019-1419-5
3. Eide PK, Ringstad G. Sleep deprivation impairs molecular clearance from the human brain. *Brain*. 2021;144(3):863-874.
   - https://doi.org/10.1093/brain/awaa443
4. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025;188(8):2129-2148.e21.
   - https://doi.org/10.1016/j.cell.2025.02.022
5. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
6. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
