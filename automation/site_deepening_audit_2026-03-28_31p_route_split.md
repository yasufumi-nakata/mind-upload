# Site Deepening Audit (2026-03-28, human 31P route split)

## 対象

- 主対象:
  - `wbe_101.md`
  - `index.md`
  - `verification.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `wiki/human-proxy-composition.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1002/nbm.3384`
- `https://doi.org/10.1002/mrm.26560`
- `https://doi.org/10.3389/fnins.2024.1389111`
- `https://doi.org/10.1177/0271678X261415784`
- `https://doi.org/10.1093/pnasnexus/pgaf072`

## 今回この箇所を選んだ理由

- サイト全体はすでに human proxy をかなり厳密に分解しておりましたが、`31P-MRS` だけはまだ `energetic-balance route` という一段に寄りすぎておりました。
- これは一次文献の現在地とずれています。少なくとも human-side の `31P` には
  - resting metabolite / pH balance
  - MT-based CK / Pi→ATP exchange flux
  - whole-brain intracellular NAD content
  - task-evoked NAD+ dynamics
  という別の inferential object がございます。
- この圧縮を残すと、読者が `31P paper exists` を `human energetic state is one row closer to solved` と誤読します。

## 根拠付き批判

### 1. resting 31P balance と MT exchange flux は同じ quantity ではありません

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は healthy human brain で ATP synthesis, phosphorus-metabolite concentrations, pH, T1 relaxation times を報告しました。
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) は 7 T band-inversion / magnetization-transfer と 5-pool model を用いて PCr→γ-ATP, Pi→γ-ATP, ATP intramolecular exchange を分けて推定しました。

批判:

- したがって `31P energetic balance` という単一ラベルでは、resting balance と model-conditioned exchange flux が潰れます。
- これは quantity type も model burden も違うため、同じ calibrator role に置くのは弱いです。

### 2. 31P は ATP / pH だけでなく NAD content を whole-brain map としても扱います

- [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111) は 7 T 31P-MRSI と subspace-based processing を用いて、human whole-brain intracellular NAD content を 2.3 cc nominal resolution で map しました。

批判:

- これは `31P = energetic-balance` という現行サイトの前景化が不十分であることを示します。
- NAD content map は ATP / PCr / pH と同じ object ではなく、redox-related quantity を別の SNR / fitting burden で扱う route です。

### 3. 31P は task-evoked dynamic assay にも使われます

- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) は 25 healthy volunteers で visual task 中の occipital voxel 31P-fMRS を行い、NAD+ dynamics を報告しました。

批判:

- これにより `31P` は static balance route だけでなく bounded task-dynamics route でもあることが明確です。
- したがって static 31P と dynamic 31P を同じ `macro energetic balance` row に押し込むのは、time window の観点でも不正確です。

### 4. deuterium rate imaging とも別です

- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は dynamic DMRSI と kinetic model を用いて glucose transport / metabolic-rate terms を whole-brain map として推定しました。

批判:

- `31P` 内部の split が曖昧なままだと、さらに `31P` と `deuterium` の差も読みにくくなります。
- site-wide の spectroscopy rule は `1H-MRSI vs 31P vs deuterium` だけでなく、`31P` 自体の内部 split まで要求すべきでした。

## 今回実行した変更

- `index.md`
  - front matter の human evidence bullet を更新し、`31P metabolite / pH balance`、`31P MT exchange-flux`、`31P NAD-content / functional routes` を分離しました。
  - front-door note-box の energetic / spectroscopy rows に Ren 2017, Guo 2024, Kaiser 2026 を追加し、`31P` の内部 split を明文化しました。

- `wbe_101.md`
  - front matter の spectroscopy / bioenergetic bullets を更新しました。
  - human observability ladder の `31P-MRS energetic-balance route` 1 行を
    - `31P metabolite-balance / pH`
    - `31P MT exchange-flux`
    - `31P NAD-content / functional route`
    の 3 行へ分割しました。
  - spectroscopy note-box と maturity note-box を更新し、31P rows を one row と読めないよう修正しました。
  - references に Ren 2017, Guo 2024, Kaiser 2026 を追加しました。

- `verification.md`
  - page_highlights / known_points の spectroscopy grammar を更新しました。
  - `Human Proxy Composition Card` の説明と `2026-03-27 addendum` を更新し、31P split を verification-side rule に昇格しました。
  - references に Ren 2017, Guo 2024, Kaiser 2026 を追加しました。

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - page_highlights / calibrator-role wording を更新しました。
  - bioenergetic section の human-side note を `one macro energetic proxy` から `several macro energetic proxy classes` へ改稿しました。
  - bioenergetic route card の field definition を更新し、31P balance / flux / NAD route を別 quantity class として扱うよう修正しました。
  - references に Ren 2017, Guo 2024, Kaiser 2026 を追加しました。

- `wiki/human-proxy-composition.md`
  - page_highlights / known_points / early note-box を更新しました。
  - human route table の single 31P row を
    - metabolite-balance / pH
    - MT exchange-flux
    - NAD-content / functional route
    の 3 rows に分割しました。
  - references に Ren 2017, Guo 2024, Kaiser 2026 を追加しました。

## 今回止めた誤読

- `31P paper exists` = `human energetic state is one near-direct meter`
- `resting ATP / pH balance` = `exchange flux` = `NAD content` = `task dynamics`
- `31P energetic route` と `deuterium kinetic-rate route` はだいたい同じ
- `one spectroscopy row improved` から `human maintenance-state closure got closer` と読める

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査メモ、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
2. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26560
3. Guo R, Yang S, Wiesner HM, et al. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. *Frontiers in Neuroscience*. 2024.
   - https://doi.org/10.3389/fnins.2024.1389111
4. Kaiser A, Vind FA, Duarte JMN, et al. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
5. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
