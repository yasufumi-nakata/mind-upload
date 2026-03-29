# Site Deepening Audit (2026-03-29, residual spectroscopy-route compression cleanup)

## 対象

- 主対象:
  - `perspective.md`
  - `verification.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
- 調査範囲: 技術 / 自然科学のみ
- 除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- front door 側の `index.md` / `faq.md` / `wbe_101.md` はすでに spectroscopy taxonomy をかなり厳密化しておりました。
- しかし，中心ページと長文 wiki の一部にはなお
  - `human energetic imaging`
  - `31P NAD routes`
  - `31P energetic-balance / exchange-flux / NAD routes`
  - `deuterium absolute-quantification and kinetic-rate routes`
  のような圧縮が残っておりました。
- これは site 内の科学的基準不一致でございます。入口では route-type 単位で止めているのに，中核ページで modality-family 単位へ戻すと，読者が route burden と claim ceiling を誤読しやすくなります。

## 根拠付き批判

### 1. human `31P` 自体がすでに複数の inferential object に分かれております

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は resting human brain の `ATP synthesis / phosphorus metabolites / pH` を扱う `31P metabolite / pH balance` route です。
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) は band-inversion / MT 5-pool model に基づく `31P MT exchange-flux` route です。
- [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111) は `whole-brain intracellular NAD-content mapping` route です。
- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) は `functionally localized task-evoked NAD+ dynamics` route です。

批判:

- これらは同じ `31P NAD route` でも，同じ `human energetic imaging` でもございません。
- quantity type，spatial support，time axis，model burden，safe calibrator role が異なります。
- したがって，中核ページに generic label を残すと，front door で止めた overread を再導入してしまいます。

### 2. deuterium 側も `absolute quantification` と `kinetic-rate imaging` を分ける必要がございます

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は absolute deuterated-metabolite concentrations を軸にした `absolute-quantification` route です。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は blood-input と kinetic model に依存した `kinetic-rate imaging` route です。
- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は repeatability が stated protocol に依存することを示しました。

批判:

- `deuterium route` とだけ書くと，absolute burden と model-conditioned rate term が混ざります。
- repeatability も generic guarantee ではなく route-specific operating condition です。

### 3. NAD route の内部でも static map と functional voxel assay は別 row でございます

- [de Graaf et al. (2017)](https://doi.org/10.1002/mrm.26465) は human brain 7 T で `NAD+` detection に overlap handling が必要であることを示しました。
- [Hendriks et al. (2019)](https://doi.org/10.1002/nbm.4137) は functional `31P` readout が high-SNR, 7 T, close-fitting coil, large visual spectroscopy volume に依存することを示しました。

批判:

- `whole-brain intracellular NAD-content mapping` と `localized task-evoked NAD+ dynamics` を一つの `31P NAD route` に押し込むと，
  - whole-brain macro content
  - localized task-linked dynamics
  - route-specific localization burden
  - route-specific hardware burden
  が見えなくなります。

## 今回実行した変更

- `perspective.md`
  - front-door highlight と technical-challenge paragraph の spectroscopy taxonomy を route-type 単位に修正しました。
  - `31P and deuterium route names need their own quantity split` note に `Ren 2015 / Ren 2017` を加え，resting balance と MT exchange-flux を明示しました。
- `verification.md`
  - energetic vs glial note と bioenergetic route-card note を更新し，`31P metabolite / pH balance`，`31P MT exchange-flux`，`31P NAD-content mapping`，`localized functional 31P NAD-dynamics`，`deuterium absolute quantification`，`deuterium kinetic-rate imaging` を別 route として書き分けました。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - summary bullets の generic `31P NAD routes` を分解しました。
  - human-observability table の `human energetic imaging` 1 行を 6 行へ分解しました。
  - misconception / practical-rule / minimum-submission wording を route-type 単位に更新しました。
- `wiki/measurement-stack-and-claim-ceiling.md`
  - spectroscopy note と human proxy-class rule を更新し，`31P MT exchange-flux` 欠落と `Li + Karkouri` の再圧縮を解消しました。

## 今回止めた誤読

- `human energetic imaging exists` = `local mitochondrial state is partly seen`
- `31P NAD route` = `whole-brain NAD map` = `task-evoked local NAD dynamics`
- `deuterium route` = `absolute metabolite burden` = `kinetic-rate truth`
- `same modality family` = `same inferential object`
- `front door だけ厳密なら，中核 wiki は少し粗くてもよい`

## 外部依存タスク

- なし
  - 今回の変更は web 確認，repo 内改稿，生成物更新，検証，commit，push までこのセッションで完結できます。

## 参考文献

1. Ren J, Sherry AD, Malloy CR. (31)P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
2. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26560
3. de Graaf RA, De Feyter HM, Brown PB, et al. Detection of cerebral NAD+ in humans at 7T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26465
4. Hendriks AD, van der Kemp WJM, Luijten PR, Petridou N, Klomp DWJ. SNR optimized 31P functional MRS to detect mitochondrial and extracellular pH change during visual stimulation. *NMR in Biomedicine*. 2019.
   - https://doi.org/10.1002/nbm.4137
5. Guo R, Yang S, Wiesner HM, et al. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. *Frontiers in Neuroscience*. 2024.
   - https://doi.org/10.3389/fnins.2024.1389111
6. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
7. Kaiser A, Vind FA, Duarte JMN, et al. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
8. Bøgh N, Vestergaard MB, Vølund M, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024.
   - https://doi.org/10.1186/s41747-024-00426-4
9. Karkouri J, Deelchand DK, Van de Moortele P-F, et al. Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
