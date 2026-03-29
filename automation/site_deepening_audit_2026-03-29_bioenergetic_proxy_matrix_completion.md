# Site Deepening Audit (2026-03-29, bioenergetic proxy matrix completion)

## 対象

- 主対象:
  - `tech_roadmap.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `verification.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- サイト全体の public rule は、すでに human energetic routes を
  - `31P metabolite / pH balance`
  - `31P MT exchange-flux`
  - `31P NAD-content mapping`
  - `31P functional NAD-dynamics`
  - `deuterium absolute quantification`
  - `deuterium kinetic-rate imaging`
  に分割して読ませる方向へ進んでおりました。
- しかし実表と route-card 本文にはなお 2 つの破れが残っておりました。
  - `tech_roadmap.md` の M3 human proxy matrix に `31P MT exchange-flux` 行が欠落していたこと
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` の bioenergetic route card 本文が `Karkouri 2026` を narrative 側で取り落とし、deuterium route の operating burden も弱く書いていたこと
- これは単なる記述漏れではございません。`route family name is not yet one row` と書いておきながら、実表で row を落とすと、サイト自身が再び
  - `31P energetic route`
  - `deuterium route`
  という粗い bucket に戻ってしまいます。

## 主要結論

- `31P MT exchange-flux` は `31P metabolite / pH balance` の下位説明ではございません。別の inferential object であり、別 row が必要でございました。
- `deuterium absolute quantification` と `deuterium kinetic-rate imaging` も、同じ deuterium family の中の別 row であり、しかも route-local operating burden が異なります。
- とくに deuterium 側は
  - dose dependence
  - time-point dependence
  - repeatability being protocol-specific
  が一次ソースで示されており、`deuterium route` とだけ書くのは不正確でございました。
- したがって、roadmap の表、bioenergetic route card、verification rule の 3 箇所を同期して修正する必要がございました。

## 根拠付き批判

### 1. `31P MT exchange-flux` の欠落は site-wide taxonomy と矛盾しておりました

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は resting human brain の `ATP synthesis / phosphorus metabolites / pH` を扱う route です。
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) は `PCr→γ-ATP` と `Pi→γ-ATP` exchange flux を、`three band inversion modules` と `five-pool Bloch-McConnell-Solomon model` で推定する route です。

批判:

- この 2 本は同じ `31P energetic route` ではございません。
- 片方は resting metabolite / pH balance、もう片方は model-conditioned exchange flux です。
- それにもかかわらず `tech_roadmap.md` の M3 table では `Ren 2017` 行だけが欠落しており、page highlights / known points の split rule と実表が食い違っておりました。

### 2. `deuterium absolute quantification` と `deuterium kinetic-rate imaging` は同じ row ではございません

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は 7 T で `HDO / Glc / Glx / Lac` の absolute deuterated-metabolite concentration map を作る absolute-quantification route です。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は 7 T dynamic DMRSI, blood-input measurement, kinetic model によって `CMR_Glc`, `CMR_Lac`, `V_TCA`, `T_max` を推定する kinetic-rate route です。

批判:

- 前者は absolute metabolite distribution、後者は model-conditioned rate term でございます。
- spatial support, input-function burden, kinetic-model burden, safe calibrator role が異なるため、同じ `deuterium route` に戻してはなりません。
- bioenergetic route card の表はすでに split を要求していた一方で、本文 narrative 側が `Li 2025` 中心で `Karkouri 2026` を弱く扱っており、site の rule consistency を損ねておりました。

### 3. deuterium route は quantity split だけでなく operating-condition split も必要でございます

- [Ahmadian et al. (2025)](https://doi.org/10.1002/jmri.29532) は、human brain DMI signal が `[6,6'-2H2]glucose` dose に依存し、`0.50 g/kg` と `0.75 g/kg` は `60-100 min` で近い一方、`0.25 g/kg` は低いことを示しました。
- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は 3 T healthy-volunteer DMI の repeatability が protocol-specific であり、best repeatability は `120 min` timepoint に依存することを示しました。

批判:

- したがって deuterium row は modality label だけでは足りません。
- 同じ deuterium でも
  - dose
  - timepoint
  - protocol / field strength
  - processing route
  が違えば signal visibility や repeatability が変わります。
- `deuterium evidence exists` を stable human energetic meter のように扱うのは、一次ソースに対して弱すぎました。

## 今回実行した変更

- `tech_roadmap.md`
  - M3 の主要説明 paragraph に `Ren 2017`, `Ahmadian 2025`, `Bøgh 2024` を追加しました。
  - human proxy matrix に `Human 31P MT exchange-flux route` 行を追加しました。
  - deuterium absolute / kinetic rows に `route-specific dose / timing burden` を明示しました。

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - bioenergetic human-observability note に `Ahmadian 2025` と `Bøgh 2024` を追加しました。
  - bioenergetic route-card narrative に `Karkouri 2026` を追加し、deuterium route の `dose / time-point / protocol` burden を明示しました。
  - route-card table の `Controller / perturbation route`, `Quantity type / model burden`, `Human observability / external calibration` を更新し、absolute-quantification pipeline と repeatability regime を分離しました。

- `verification.md`
  - energetic-vs-glial stop lineに `Ahmadian 2025` と `Bøgh 2024` を追加しました。
  - bioenergetic route-card summary に `dose / time-point / repeatability regime` の明示を追加しました。

## 今回止めた誤読

- `31P energetic route` = `metabolite / pH balance` = `MT exchange-flux`
- `deuterium route` = `absolute metabolite map` = `kinetic-rate imaging`
- `same modality family` = `same inferential object`
- `deuterium signal exists` = `route-free stable energetic meter`
- `public rule は細かいが roadmap table は多少粗くてもよい`

## 外部依存タスク

- なし
  - 今回の作業は一次ソース確認、repo 内改稿、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26560
2. Karkouri J, Novoselova M, Miller S, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
3. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
4. Ahmadian N, Konig MM, Otto S, et al. Human Brain Deuterium Metabolic Imaging at 7 T: Impact of Different [6,6'-2H2]Glucose Doses. *Journal of Magnetic Resonance Imaging*. 2025.
   - https://doi.org/10.1002/jmri.29532
5. Bøgh N, Vaeggemose M, Schulte RF, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024.
   - https://doi.org/10.1186/s41747-024-00426-4
6. Ren J, Sherry AD, Malloy CR. (31)P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
