# Site Deepening Audit (2026-03-29, deuterium absolute-vs-kinetic split)

## 対象

- 主対象:
  - `index.md`
  - `wbe_101.md`
  - `verification.md`
  - `tech_roadmap.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wiki/human-proxy-composition.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `wiki/mind-upload-basics.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1093/pnasnexus/pgaf072`
- `https://doi.org/10.1002/mrm.70308`
- `https://doi.org/10.1002/mrm.29331`
- `https://doi.org/10.1002/jmri.29104`
- `https://doi.org/10.1186/s41747-024-00426-4`
- `https://doi.org/10.1016/j.neuroimage.2022.119574`

## 今回この箇所を選んだ理由

- サイトはすでに human proxy をかなり細かく分解しておりましたが、deuterium 系だけはまだ `deuterium metabolite / rate imaging` に近い圧縮が残っておりました。
- しかし一次文献の現在地では、少なくとも human-side の deuterium 系は
  - absolute deuterated-metabolite mapping / quantification
  - blood-input 依存の kinetic-rate imaging
  - dose / protocol 依存性
  - repeatability / portability
  という別の inferential object に分かれます。
- この圧縮を残すと、読者が `human deuterium paper exists` を `human glucose-metabolic rate is already one stable row closer to solved` と誤読します。

## 根拠付き批判

### 1. absolute metabolite map と kinetic-rate map は同じ quantity ではありません

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は 7 T human brain DMI で、`12` healthy volunteers と `5` treatment-naive glioblastoma patients を対象に、HDO / glucose / Glx / lactate の absolute concentrations と rate estimates を、absolute-quantification pipeline を明示して扱いました。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は 7 T dynamic DMRSI と blood input function を用い、dynamic study の `8` healthy volunteers のうち `5` 名で blood input function を取り、glucose transport と key metabolic-rate terms を kinetic model で whole-brain map として推定しました。

批判:

- したがって `deuterium metabolite / rate imaging` という単一ラベルでは、absolute metabolite burden と model-conditioned kinetic-rate term が潰れます。
- 両者は acquisition design、必要ハードウェア、外部入力、model burden、推定される quantity type が異なるため、同じ calibrator role に置くのは弱いです。

### 2. deuterium metabolite mapping 自体も dose / protocol 依存です

- [Ahmadian et al. (2024)](https://doi.org/10.1002/jmri.29104) は healthy volunteers の 7 T DMI で、[6,6'-²H₂]glucose の異なる経口投与量が downstream deuterated-metabolite visibility と protocol design に影響することを示しました。
- [de Feyter et al. (2022)](https://doi.org/10.1002/mrm.29331) は human whole-brain DMI の in vivo 実装を示しましたが、これは route feasibility の前進であって、そのまま rate-identifiability を保証するものではありません。

批判:

- metabolite map が成立することと、そこから kinetic term が安定に識別できることは別問題です。
- 投与量、時系列設計、sampling window、spectral separation を書かないまま `deuterium imaging` と総称すると、protocol-sensitive な制約が見えなくなります。

### 3. repeatability と portability は別軸です

- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は 3 T healthy-brain DMI の repeatability を報告しましたが、これは stated protocol 下の operating-point 特性です。
- [Niess et al. (2023)](https://doi.org/10.1016/j.neuroimage.2022.119574) は 7 T direct ²H detection と clinical 3 T indirect ¹H QELT を比較し、検出経路の違い自体が observability / reproducibility burden を変えることを示しました。

批判:

- `repeatable DMI exists` を `all deuterium routes are interchangeable` に昇格してはいけません。
- 直接 ²H 検出、間接 ¹H 検出、absolute quantification、dynamic kinetic fitting は、それぞれ別の route card を要します。

### 4. deuterium route が改善しても human maintenance-state closure には直結しません

- Karkouri 2026 も Li 2025 も、human in vivo energetic observability にとって重要な前進ではあります。
- しかし両者が与えるのは macro-scale deuterated-metabolite burden あるいは model-conditioned glucose-rate term であり、branch-local mitochondrial positioning、tagged synapse の ATP sufficiency、cell-specific recovery controller identity ではありません。

批判:

- このため、deuterium row を分けずに前景化すると、`human energetic imaging got better` が `cell-specific maintenance controller is close` に誤変換されます。
- 本サイトの基本ルールである `proxy class`, `quantity type`, `model burden`, `claim ceiling` の分離と整合しなくなります。

## 今回実行した変更

- `index.md`
  - front-door の evidence bullets と explanatory paragraph で、`deuterium metabolite-mapping / absolute-quantification routes` と `deuterium kinetic-rate imaging` を別表現に改めました。

- `wbe_101.md`
  - human observability ladder の deuterium 1 行を
    - `Human deuterium metabolite-mapping / absolute-quantification route`
    - `Human deuterium kinetic-rate imaging route`
    の 2 行へ分割しました。
  - spectroscopy note を更新し、Karkouri 2026 と Li 2025 の inferential object を分離しました。

- `verification.md`
  - spectroscopy-derived human maintenance routes の rule を更新し、deuterium の absolute-map route と kinetic-rate route を別 proxy class として明示しました。
  - verification-side の批判文でも、Karkouri 2026 と Li 2025 を別 quantity type として扱うよう修正しました。

- `tech_roadmap.md`
  - human route taxonomy の表現を更新し、deuterium family を absolute-quantification route と kinetic-rate route に分離しました。

- `wiki/measurement-stack-and-claim-ceiling.md`
  - measurement stack table と route-card paragraph を更新し、absolute deuterated-metabolite maps と kinetic glucose-rate maps を別 row に分離しました。

- `wiki/human-proxy-composition.md`
  - route matrix と calibrator-role matrix を更新し、deuterium の quantity type / model burden の違いが表で見えるよう修正しました。

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - bioenergetic route card と calibrator matrix を更新し、`Dynamic DMI / 31P-MRS` の圧縮行を解消しました。
  - deuterium absolute quantification と deuterium kinetic-rate imaging を別の macro energetic proxy class として明文化しました。

- `wiki/mind-upload-basics.md`
  - 初学者向け説明でも、deuterium route を `absolute-quantification` と `kinetic-rate imaging` に分けて説明するよう修正しました。

## 今回止めた誤読

- `human deuterium paper exists` = `human glucose metabolic rate is one solved row`
- `absolute deuterated metabolite burden` = `kinetic glucose-rate mapping`
- `repeatability paper exists` = `all deuterium routes are portable and interchangeable`
- `human energetic proxy improved` = `branch-local mitochondrial state or recovery controller is close to observable`

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査メモ、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
2. Karkouri J, Deelchand DK, Van de Moortele P-F, et al. Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
3. de Feyter HM, Behar KL, Corbin ZA, et al. Deuterium metabolic imaging of the human brain in vivo at 7 T. *Magnetic Resonance in Medicine*. 2022.
   - https://doi.org/10.1002/mrm.29331
4. Ahmadian A, Karkouri J, Deelchand DK, et al. Varying doses of oral deuterated glucose for deuterium metabolic imaging of the healthy human brain at 7 T. *Journal of Magnetic Resonance Imaging*. 2024.
   - https://doi.org/10.1002/jmri.29104
5. Bøgh N, Jørgensen JT, Schytz HW, et al. Repeatability of deuterium metabolic imaging in the healthy brain at 3 T. *European Radiology Experimental*. 2024.
   - https://doi.org/10.1186/s41747-024-00426-4
6. Niess F, Deelchand DK, Mekle R, et al. Reproducibility of human brain glucose metabolism quantification using direct deuterium detection at 7 T and indirect proton detection at clinical 3 T. *NeuroImage*. 2023.
   - https://doi.org/10.1016/j.neuroimage.2022.119574
