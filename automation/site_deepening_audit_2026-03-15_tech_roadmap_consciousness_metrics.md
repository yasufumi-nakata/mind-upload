# Site Deepening Audit (2026-03-15, Tech Roadmap / Consciousness Metrics and Benchmark Layers)

## 対象

- 主対象: `tech_roadmap.md`
- 副対象: `wiki/consciousness-theory-map.md`

## 今回の選定理由

- 2026-03-15 時点で、入口ページ群と verification 系ページでは、measurement ceiling、perturbation、maintenance-state の整理がかなり進んでいました。
- その一方で、`tech_roadmap.md` の V6 / V10 / V11 と `wiki/consciousness-theory-map.md` には、なお `IIT / GNWT / FEP / PCI / criticality / TDA` を工学指標として近い重みで読める箇所が残っていました。
- これは技術・自然科学の観点で弱点です。なぜなら、2024-2025 の一次文献が比較的強く支持するのは、`単一理論の勝者` ではなく `prediction competition`、`単一意識メータ` ではなく `perturbation benchmark + spontaneous proxy + confound control` の分離だからです。

## 主要な批判点

### 1. 旧 `tech_roadmap.md` は、理論 family と benchmark layer をまだ十分に分け切れていませんでした

- 問題:
  - V6 は理論依存予測の検証を扱う節でしたが、旧版では `IIT近似`、`PCI`、`最小分岐セット`、`マルコフブランケット境界条件` が同一レベルの engineering route のように並んでいました。
  - この構造では、理論そのもの、摂動 benchmark、spontaneous proxy、数理補助解析の差が埋まり、読者が `理論名 = 合否指標` と誤読しやすくなります。
- 根拠:
  - Ferrante et al. (2025) は、IIT / GNWT / RPT の主要予測が部分的に支持されつつ鍵予測のいくつかが反証され、単一理論を勝者にしないことを示しました。
  - Casali et al. (2013) と Comolatti et al. (2019) は PCI / PCI-ST を perturbation benchmark として押し上げましたが、universal meter を与えたわけではありません。
  - Maschke et al. (2024) は spontaneous criticality と PCI の関連を示した一方、Casarotto et al. (2024) は minimally conscious state で spontaneous EEG feature と PCI の解離を示しました。
- 修正:
  - V6 を `prediction family`、`perturbation benchmark`、`spontaneous calibration track`、`confound control` の 4 本柱へ再編しました。
  - `理論名を pass/fail 指標にしない`、`PCI を benchmark 候補として扱う`、`criticality を proxy として較正する` という site rule を本文に埋め込みました。

### 2. 旧サイトは report / criterion confound を benchmark 設計の中心に置けていませんでした

- 問題:
  - `wiki/consciousness-theory-map.md` は初学者向けとして読みやすい一方、理論差より先に `post-perceptual processing` や `criterion placement` を統制すべきことが前面に出ていませんでした。
  - そのため、GNWT 系マーカーや report-dependent marker を、そのまま consciousness marker と読む余地が残っていました。
- 根拠:
  - Cohen et al. (2024) は visual awareness の neural signature を post-perceptual processing から切り分けました。
  - Fahrenfort et al. (2025) は criterion placement が conscious content marker の construct validity を脅かすことを示しました。
- 修正:
  - `wiki/consciousness-theory-map.md` を全面改稿し、`report / criterion confound` を独立した監査論点として表に入れました。
  - `no-report / criterion placement を先に固定する` を page rule として追記しました。

### 3. 旧 `V10` は Fisher 情報量を標準距離のように読ませていました

- 問題:
  - 旧版 V10 は Fisher Information Metric を事実上の既定 metric として採用していました。
  - しかし、2026-03 時点で本サイトが参照する一次文献群は、WBE の pass/fail を FIM 1 本で規定する実証 benchmark を与えていません。
- 根拠:
  - 現実に強い外部基準として積み上がっているのは、perturbation 応答、OOD 劣化、recovery、calibration のような observable behavior です。
  - これは上記の PCI / spontaneous marker / causal validation 文献群からの **推論** です。すなわち、現在の強い evidence は scalar geometry より external benchmark にあります。
- 修正:
  - V10 を `単一 metric を採用しない` 方針へ変更しました。
  - FIM、representation distance、manifold separation は候補群に下げ、`V2 / V3 / V4 の外部基準とどれだけ整合するか` を比較条件にしました。

### 4. 旧 `V11` は topology を「保証」に近く書きすぎていました

- 問題:
  - 旧版 V11 は TDA / persistent homology を導入し、神経活動多様体のトポロジー比較で `動的アトラクタ構造の同一性を幾何学的に保証する` と読める書き方でした。
  - これは一次文献の強さより一段強い表現です。
- 根拠:
  - Yoon et al. (2024) は cross-population topology comparison の数学的基盤を与えましたが、一般的な WBE pass/fail 指標を与えたわけではありません。
  - iScience 2024 の mouse V1 circular manifold 研究は、truthful topology の回収に sampling 障害があることを示しました。
- 修正:
  - V11 を `supplementary descriptor` へ降格しました。
  - `sampling / embedding / preprocessing / session drift / perturbation responsiveness` の sensitivity analysis を通った場合だけ補助指標として報告する、という運用へ改めました。

### 5. 旧 `wiki/consciousness-theory-map.md` は FEP を実装原理寄りに置きすぎていました

- 問題:
  - 旧版は `FEP = 実装原理寄り` としていましたが、読者には default engineering route のように映りえました。
- 根拠:
  - Ferrante et al. (2025) は単一理論 winner を支持していません。
  - したがって、FEP を engineering default と置くより、DCM / state-space / SCM を含む候補 family の 1 つとして扱う方が、現在の証拠強度に整合的です。これは一次文献群からの **推論** です。
- 修正:
  - `wiki/consciousness-theory-map.md` で FEP / Active Inference を `候補実装族` へ位置づけ直しました。
  - `theory family / benchmark / proxy / supplementary geometry` の 4 レイヤーに再編しました。

## 今回実行した変更

- `tech_roadmap.md`
  - V6 を `prediction family / perturbation benchmark / spontaneous proxy / confound control` へ再編
  - V10 を `単一 metric 採用` から `候補距離の benchmark 比較` へ変更
  - V11 を `保証` 表現から `補助解析` 表現へ変更
  - U11 を `IIT近似` から `proxy 較正` 問題へ変更
  - 参考文献へ 2024-2025 の一次文献を追記
- `wiki/consciousness-theory-map.md`
  - front matter を技術・自然科学中心に更新
  - ページ全体を全面改稿
  - `theory family / perturbation benchmark / spontaneous proxy / supplementary geometry` の役割表を追加
  - `一次文献が切る境界` 表と参考文献節を新設

## 外部依存で保留

- 同一 cohort での perturbation / spontaneous / geometry 指標の比較ベンチ実装
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: TMS-EEG または intracranial stimulation、no-report 課題、cohort-level follow-up の整備
  - 完了条件: PCI / spontaneous complexity / geometry descriptor を同じ cohort・同じ preprocessing rule・同じ failure mode で比較できる公開 benchmark が走ること

## 参考文献

- Ferrante O, et al. Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08888-1
- Cohen MA, et al. Neural signatures of visual awareness independent of postperceptual processing. *Cereb Cortex*. 2024.
  - https://doi.org/10.1093/cercor/bhae415
- Fahrenfort JJ, et al. Criterion placement threatens the construct validity of neural measures of conscious contents. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-02009-x
- Casali AG, et al. A theoretically based index of consciousness independent of sensory processing and behavior. *Sci Transl Med*. 2013.
  - https://doi.org/10.1126/scitranslmed.3006294
- Comolatti R, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. *Brain Stimul*. 2019.
  - https://doi.org/10.1016/j.brs.2019.05.013
- Maschke C, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. *Commun Biol*. 2024.
  - https://doi.org/10.1038/s42003-024-06613-8
- Casarotto S, et al. Dissociations between spontaneous electroencephalographic features and perturbational complexity index in the minimally conscious state. *Brain*. 2024.
  - https://doi.org/10.1093/brain/awae227
- Yoon B, Miolane N, Osting B, Linderman SW. Tracking the topology of neural manifolds across populations. *Proc Natl Acad Sci U S A*. 2024.
  - https://doi.org/10.1073/pnas.2402628121
- The topological structure of population activity in mouse visual cortex encodes visual stimuli. *iScience*. 2024.
  - https://doi.org/10.1016/j.isci.2024.111613
