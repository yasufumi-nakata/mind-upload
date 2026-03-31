# Site Deepening Audit (2026-03-31, human proxy myelin family-internal split)

## 対象

- 主対象:
  - `wiki/human-proxy-composition.md`
- 同期対象:
  - `verification.md`
  - `wbe_101.md`
- 調査範囲:
  - 技術
  - 自然科学

## web確認対象

- `https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/`
- `https://doi.org/10.1038/s41598-018-28852-6`
- `https://doi.org/10.1002/mrm.29998`
- `https://doi.org/10.1111/bpa.70010`

## 今回この箇所を選んだ理由

- 直近の site 更新で、`SV2A PET` や `astrocyte PET` は family 内の比較型まで public rule に落ちておりました。
- しかし central bundle rule である `wiki/human-proxy-composition.md` では、なお `human myelin MRI` が `quantity-defined family` の一行で読める構造が残っていました。
- これを放置すると、
  - `MWF versus calibrated T1w/T2w comparison`
  - `SyMRI / MTsat comparison`
  - `bilayer-sensitive mapping`
  - `qT1 remyelination-sensitive pathology route`
  が一つの reusable bundle row に圧縮されます。
- human proxy bundle の主眼は「同じ human family 名を並べれば state closure に近づく」という誤読を止めることですので、この compression は central rule 側で止める必要がございました。

## 主要結論

- `human myelin MRI` は一つの interchangeable bundle row ではございません。
- 少なくとも
  - `MWF versus calibrated T1w/T2w comparison`
  - `relaxometry / MTsat comparison`
  - `bilayer-sensitive mapping`
  - `qT1 remyelination-sensitive pathology route`
  を別の comparison family として扱う必要がございます。
- したがって bundle composition では、`myelin MRI` とだけ書くのは不十分であり、family-internal comparison family を固定しなければなりません。

## 根拠付き批判

### 1. `MWF` と `calibrated T1w/T2w` は同じ row ではございません

- 根拠:
  - [Arshad et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/) は、healthy adults において `MWF` と `calibrated T1w/T2w` の test-retest reliability と concurrent validity を比較しました。
- 批判:
  - ここで主に問われているのは、`one myelin-sensitive metric exists` ではなく、`which metric remains reliable and criterion-valid under the named route` でございます。
  - したがって、この paper を `human myelin MRI exists` の一語に還元すると、comparison route 自体が消えます。

### 2. `SyMRI / MTsat` comparison は `MWF` comparison の代用ではございません

- 根拠:
  - [Hagiwara et al. (2018)](https://doi.org/10.1038/s41598-018-28852-6) は、20 healthy adults で `SyMRI`、`MTsat`、`T1w/T2w` を比較し、white matter では `SyMRI` と `MTsat` の相関が強く、`T1w/T2w` はそれより弱いことを示しました。
- 批判:
  - これは `cross-method agreement inside one acquisition family` の問題であり、`MWF versus calibrated T1w/T2w` の repeat-scan validity route と同じではございません。
  - よって `Hagiwara + Arshad` をまとめて `human myelin MRI comparison` に圧縮すると、何が比較されたのかが曖昧になります。

### 3. `bilayer-sensitive mapping` は high-burden proof-of-principle であり generic myelin row ではございません

- 根拠:
  - [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は、human brain in vivo で myelin bilayer mapping を示しましたが、healthy volunteers 2 名の specialized route でございます。
- 批判:
  - これは `proof-of-principle bilayer-sensitive route` であり、routine whole-brain myelin observability や remyelination-sensitive route の代用ではございません。
  - したがって `myelin MRI` の generic bundle row に含めるだけでは、deployment burden と quantity type が消えます。

### 4. `qT1 remyelination-sensitive route` は living-human routine row ではございません

- 根拠:
  - [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) は、postmortem MS cortex において `qT1` が remyelination に感度を持つ一方、`MWF` と `MTR` は demyelinated と remyelinated cortex を分けなかったと報告しました。
- 批判:
  - これは `pathology-conditioned remyelination-sensitive route` であり、living-human routine route でも、bilayer mapping でも、healthy comparison route でもございません。
  - `myelin family` を一行で扱うと、この pathology-specific ceiling が消えてしまいます。

### 5. central composition rule は myelin family 内部の comparison type を入力条件に持つべきでした

- 根拠:
  - 上記 4 本はすべて `human myelin MRI` に属しうる文献ですが、direct observable、cohort、deployment burden、pathology dependence、safe ceiling が一致しておりません。
- 批判:
  - `Human Proxy Composition Card` がこの split を持たない場合、bundle 側の `quantity-type / common-axis compatibility` 監査が甘くなります。
  - central rule には `family label` の次に `family-internal comparison family` を固定する要件が必要でございました。

## 今回実行した変更

- `wiki/human-proxy-composition.md`
  - front matter の `description`、`page_highlights`、`known_points` に myelin family-internal split を追加しました。
  - route matrix の `Quantity-defined myelin MRI family` を 4 行へ分解しました。
  - `Human myelin MRI is not one reusable bundle row` note-box を追加し、`MWF / calibrated T1w/T2w`、`SyMRI / MTsat`、`bilayer-sensitive`、`qT1 remyelination-sensitive` を別 comparison family として明示しました。
  - `Method-family collapse` に myelin family 内部の non-equivalence を追加しました。
  - three-axes table の `Quantity-defined myelin MRI family` 行を 4 行へ分解しました。

- `verification.md`
  - `Human Proxy Composition Card` の family-internal correction に myelin family split を追加しました。
  - `Proxy-row inventory and direct observables` の例示に myelin family-internal typing を追加しました。

- `wbe_101.md`
  - beginner-facing human proxy table の myelin row を `Baadsvik only` から `human myelin MRI family` へ改稿しました。
  - `Human myelin MRI is not one reusable proxy row` note-box を追加しました。
  - references に `Arshad et al. (2017)`、`Hagiwara et al. (2018)`、`Galbusera et al. (2025)` を追加しました。

## 今回止めた誤読

- `human myelin MRI` = one solved human myelin row
- `MWF / calibrated T1w:T2w` = `SyMRI / MTsat` = `bilayer-sensitive mapping` = `qT1 remyelination-sensitive route`
- `proof-of-principle bilayer map` = routine same-subject human observability
- `postmortem remyelination-sensitive route` = living-human current myelin-state readout
- `myelin family exists` = `per-axon timing-state is now measured in humans`

## 検証結果

- `git diff --check`
  - pass
- `bundle exec jekyll build`
  - pass

## 外部依存タスク

- なし
  - 今回の作業は文献確認、本文修正、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
2. Hagiwara A, Hori M, Kamagata K, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018.
   - https://doi.org/10.1038/s41598-018-28852-6
3. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
4. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025.
   - https://doi.org/10.1111/bpa.70010
