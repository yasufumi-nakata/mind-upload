# Site Deepening Audit (2026-04-01, beginner astrocyte route-role front-door sync)

## 対象

- 主対象:
  - `wiki/mind-upload-basics.md`
- 同期対象:
  - `github-wiki-export/mind-upload-basics.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学、法学、制度論

## 今回この箇所を選んだ理由

- site-wide の central rule pages では、2026-04-01 時点ですでに astrocyte PET を
  - `SMBT-1 first-in-human MAO-B target validation`
  - `SMBT-1 AD-spectrum disease-context`
  - `SMBT-1 brain quantification`
  - `SMBT-1 whole-body biodistribution`
  - `I2BS route`
  に分けて読ませる規則が整っておりました。
- しかし beginner front door である `wiki/mind-upload-basics.md` は、なお
  - `Human MAO-B astrocyte PET`
  - `Human I2BS astrocyte PET`
  の二段で止まっており、MAO-B family 内の route-role split が visible ではございませんでした。
- このズレは単なる wording の問題ではございません。入口ページで `MAO-B PET exists` と読める構造が残ると、deep page で止めた
  - target validation
  - disease-context contrast
  - brain quantification
  - whole-body tracer burden
  の非同一性が、最初の導線で再圧縮されるためでございます。

## 主要結論

- 今回もっとも改善優先度が高かったのは、新しい astrocyte 文献を増やすことではなく、`beginner front door にも route-role split を実装すること` でございました。
- 2026-04-01 時点の一次文献に照らすと、`astrocyte PET` は beginner page でも少なくとも
  - `target`
  - `route role`
  - `model / acquisition burden`
  - `safe calibrator role`
  を分けて書かなければなりません。
- よって今回の更新対象は、site の入口ページとしてレバレッジが最大の `wiki/mind-upload-basics.md` が最適と判断いたしました。

## 根拠付き批判

### 1. MAO-B family 内の route role を beginner page がまだ潰しておりました

- [Villemagne et al. (2022, `10.2967/jnumed.121.263254`)](https://doi.org/10.2967/jnumed.121.263254) は、healthy humans における `SMBT-1 first-in-human MAO-B target validation` でございます。
- [Villemagne et al. (2022, `10.2967/jnumed.121.263255`)](https://doi.org/10.2967/jnumed.121.263255) は、`77 volunteers` を対象にした `AD-spectrum disease-context route` でございます。
- [Hiraoka et al. (2025, `10.1007/s12149-025-02083-y`)](https://doi.org/10.1007/s12149-025-02083-y) は、arterial input と model comparison を伴う `brain-quantification route` でございます。
- [Mesfin et al. (2026, `10.1007/s12149-025-02144-2`)](https://doi.org/10.1007/s12149-025-02144-2) は、`six healthy volunteers`、`5.5 h` の `whole-body biodistribution route` でございます。

批判:

- これらはすべて `MAO-B astrocyte PET` に属しうる文献ですが、direct observable も safe ceiling も一致しておりません。
- したがって beginner page で `Human MAO-B astrocyte PET` の一行に戻すと、site-wide rule が禁止している family-internal collapse を front door で再導入してしまいます。

### 2. I2BS route は MAO-B route の代替行ではございません

- [Tyacke et al. (2018, `10.2967/jnumed.118.208009`)](https://doi.org/10.2967/jnumed.118.208009) は、`11C-BU99008` が idazoxan で低下し、isocarboxazid では block されない `I2BS target class` を示しました。
- [Livingston et al. (2022, `10.1038/s41380-021-01429-y`)](https://doi.org/10.1038/s41380-021-01429-y) は、その `I2BS route` を cognitively impaired individuals に適用した disease-context paper でございます。

批判:

- `I2BS PET` は `MAO-B PET` の別 quantification option ではございません。
- target class が異なる以上、bundle role も safe ceiling も同一行にまとめてはなりません。

### 3. MAO-B interpretation 自体が cohort- and pathology-conditioned であり route-free scalar ではございません

- [Best et al. (2026, `10.1038/s41380-025-03355-9`)](https://doi.org/10.1038/s41380-025-03355-9) は、people with AUD において mean binding difference が単純ではなく、severity と smoking が解釈を動かすことを示しました。
- [Jaisa-Aad et al. (2024, `10.1007/s00401-024-02712-2`)](https://doi.org/10.1007/s00401-024-02712-2) は、MAO-B が reactive astrogliosis biomarker であっても pathology class により safe reading が変わることを整理しました。

批判:

- したがって `MAO-B astrocyte PET` を even now one generic human astrocyte-state scalar と書くのは科学的に弱うございます。
- beginner page でも `target-defined and route-role-defined proxy` と書く必要がございました。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `last_updated` を `2026-04-01` に更新しました。
  - front matter の `page_highlights` と `known_points` を、`SMBT-1 target-validation / AD-spectrum / brain-quantification / whole-body-biodistribution / I2BS` の split が見える文言へ更新しました。
  - `2026-04-01 technical correction: astrocyte PET also splits by route role` note-box を追加しました。
  - human observability ladder の astrocyte block を 2 行から 5 行へ分解しました。
  - beginner summary の `quantity type` note を、`route role` まで明示する文言へ更新しました。
  - 参考文献へ
    - Villemagne et al. (2022, AD-spectrum)
    - Hiraoka et al. (2025)
    - Mesfin et al. (2026)
    - Best et al. (2026)
    を追加しました。

- `github-wiki-export/mind-upload-basics.md`
  - 上記と同内容へ同期し、GitHub Wiki export 側でも beginner front door の stop-rule が一致するよう更新しました。

## 今回止めた誤読

- `MAO-B astrocyte PET exists` = `human astrocyte route is one reusable row`
- `SMBT-1 first-in-human target validation` = `AD-context evidence`
- `brain quantification paper` = `whole-body tracer-burden paper`
- `I2BS PET` = `MAO-B route with another tracer`
- `astrocyte PET` = `route-free whole-brain astrocyte-state scalar`

## 外部依存タスク

- なし
  - 今回の作業は一次文献確認、repo 内ページ改稿、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of ^18F-SMBT-1, a Novel ^18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263254
2. Villemagne VL, Harada R, Doré V, et al. Assessing reactive astrogliosis with ^18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263255
3. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [^18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025.
   - https://doi.org/10.1007/s12149-025-02083-y
4. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [^18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
5. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of ^11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
6. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel ^11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
7. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [^11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
8. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024.
   - https://doi.org/10.1007/s00401-024-02712-2
