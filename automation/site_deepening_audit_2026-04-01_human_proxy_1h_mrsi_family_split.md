# Site Deepening Audit (2026-04-01, human proxy 1H-MRSI family split)

## 対象

- 主対象:
  - `index.md`
  - `wbe_101.md`
  - `faq.md`
  - `verification.md`
  - `wiki/mind-upload-basics.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wiki/human-proxy-composition.md`
- 同期対象:
  - `perspective.md`
  - `tech_roadmap.md`
  - `mind_uploading_papers.md`
  - `summary_booklet.md`
  - `wiki/verification-basics.md`
  - `github-wiki-export/*.md` の対応ページ
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `1H-MRSI similarity scaffold` として site 内で参照している一次文献
  - Lucchetti et al. (2025)
- `high-resolution 1H-MRSI metabolite-distribution route` として site 内で別立てすべき一次文献
  - Guo et al. (2025)
- `same family` に見えやすいが実際には inferential object が異なる比較対象
  - Ren et al. (2015)
  - Wright et al. (2022)
  - Li et al. (2025)
  - Karkouri et al. (2026)
  - Bhogal et al. (2020)
  - Baboli et al. (2024)

## 今回この箇所を選んだ理由

- 2026-04-01 時点の site では、spectroscopy family 全体についてはかなり詳細に分解できておりましたが、`1H-MRSI` family の内部ではなお
  - `five-metabolite parcel-similarity scaffold`
  - `high-resolution metabolite-distribution mapping`
  を front door から一目で区別できない箇所が残っておりました。
- とくに `Lucchetti et al. (2025)` を `1H-MRSI route` の代表例として置く構図は、読者に
  - `1H-MRSI = high-resolution metabolic imaging`
  - `1H-MRSI = absolute or near-absolute metabolite distribution`
  - `1H-MRSI similarity scaffold = kinetic or energetic mapping`
  といった誤読を生じさせやすい状態でございました。
- さらに DOI `10.1109/TBME.2025.3572448` の文献情報が一部ページで別論文名へずれており、reference hygiene の観点でも correction value が高いと判断いたしました。

## 主要結論

- 今回もっとも修正優先度が高かったのは、`spectroscopy evidence を増やすこと` ではなく、`1H-MRSI family 内部の inferential object split を front door から深いページまで貫通させること` でございました。
- 一次文献に照らすと、
  - Lucchetti et al. (2025) は `five-metabolite parcel-level similarity scaffold`
  - Guo et al. (2025) は `high-resolution metabolite-distribution mapping under ultrahigh-field reconstruction burden`
  であり、同じ `1H-MRSI` でも claim ceiling は一致いたしません。
- したがって本 site では、`1H-MRSI exists` を 1 本の near-direct metabolic readout として扱わず、
  - similarity
  - high-resolution distribution
  - 31P balance
  - 31P exchange flux
  - 31P NAD-content / functional NAD dynamics
  - deuterium absolute metabolite mapping / quantification
  - deuterium kinetic-rate imaging
  を別行で止める必要がございました。

## 根拠付き批判

### 1. Lucchetti 2025 は high-resolution metabolite map ではなく、five-metabolite similarity scaffold でございます

- [Lucchetti et al. (2025, `10.1038/s41467-025-66124-w`)](https://doi.org/10.1038/s41467-025-66124-w) は、whole-brain MRSI を用いて biochemical organization を論じる重要な human-side advance でございます。
- しかしこの route の主 object は、site の表現に即して言えば `five-metabolite parcel-similarity scaffold` であり、局所 voxel ごとの高解像度 absolute distribution を直接主張するものではございません。

批判:

- site の front door で Lucchetti 2025 だけが `1H-MRSI` の代表として立つと、読者は `similarity scaffold` と `distribution map` を同じ measurement class と誤認しやすくなります。
- その誤認は、`what exact quantity is constrained?` という本 site の stop-rule に反しております。

### 2. Guo 2025 は別の inferential object を持つ 1H-MRSI route であり、Lucchetti 2025 の下位互換ではございません

- [Guo et al. (2025, `10.1109/TBME.2025.3572448`)](https://doi.org/10.1109/TBME.2025.3572448) は、extended spatiospectral encoding と subspace modeling を用いた `high-resolution brain metabolic imaging at ultrahigh field` でございます。
- この route は、parcel similarity ではなく `high-resolution metabolite-distribution structure` を主 object とし、ghosting / aliasing / low-SNR / reconstruction burden が reading の一部になります。

批判:

- `Guo 2025 = just another MRSI paper` として Lucchetti 2025 の行に吸収すると、
  - reconstruction burden
  - spatial target
  - artifact-control dependence
  - distribution-vs-similarity distinction
  が消えてしまいます。
- よって Guo 2025 は、Lucchetti 2025 と同じ family に属しても、同じ row に圧縮してはならない evidence でございました。

### 3. 1H-MRSI と deuterium / 31P routes は quantity type が違うため、相互代入できません

- [Ren et al. (2015, `10.1002/nbm.3384`)](https://doi.org/10.1002/nbm.3384) は `31P metabolite / pH balance` route でございます。
- [Wright et al. (2022, `10.1016/j.neuroimage.2022.119574`)](https://doi.org/10.1016/j.neuroimage.2022.119574) は `31P magnetization-transfer based ATP metabolic imaging` の route でございます。
- [Li et al. (2025, `10.1093/pnasnexus/pgaf072`)](https://doi.org/10.1093/pnasnexus/pgaf072) は `dynamic deuterium metabolic imaging with blood-input and kinetic modeling` であり、CMR-related rate object を扱います。
- [Karkouri et al. (2026, `10.1002/mrm.70308`)](https://doi.org/10.1002/mrm.70308) は `deuterated metabolite concentrations and rates` の quantification route でございます。

批判:

- これらはすべて human spectroscopy ではございますが、same quantity ではございません。
- `spectroscopy exists` を理由に similarity, distribution, balance, exchange-flux, NAD-content, NAD-dynamics, absolute mapping, rate imaging を一列に畳むことは、measurement-model の観点から支持されません。

### 4. method review 側の記述も、1H-MRSI family split を支持しております

- [Bhogal et al. (2020, `10.1002/brb3.1852`)](https://doi.org/10.1002/brb3.1852) は MRSI の technical review であり、acquisition / reconstruction / quantification burden を整理しております。
- [Baboli et al. (2024, `10.1148/radiol.232401`)](https://doi.org/10.1148/radiol.232401) は radiological overview として MRSI 系の current opportunities / limitations を整理しております。

批判:

- review レベルでも、`MRSI` は one-click direct readout として扱われておらず、spatial resolution, SNR, artifact control, quantification pipeline, model assumptions が output meaning を変えます。
- したがって site 側でも `1H-MRSI` を family 名のまま front door に置くのではなく、family-internal route split を visible にする方が一貫的でございました。

## 今回実行した変更

- `index.md`
  - front-door highlights に `high-resolution 1H-MRSI metabolite-distribution routes` を追加しました。
  - human proxy table に `Guo et al. (2025)` の独立行を追加しました。
  - spectroscopy paragraph を更新し、Lucchetti / Guo / 31P / deuterium を別 object として明記しました。

- `wbe_101.md`
  - beginner ladder に `High-resolution 1H-MRSI metabolite-distribution route` を追加しました。
  - spectroscopy family の説明を `static similarity` と `high-resolution metabolite distribution` に分離しました。

- `faq.md`
  - `same quantity?` 誤読を止める表と本文を更新しました。
  - `Guo et al. (2025)` の reference metadata を修正しました。

- `verification.md`
  - Observability Budget / spectroscopy addendum を更新し、`static similarity` と `high-resolution metabolite-distribution mapping` を分離しました。
  - `Guo et al. (2025)` の reference metadata を修正しました。

- `wiki/mind-upload-basics.md`
  - beginner front door の high-level bullet と human observability ladder に `Guo et al. (2025)` を追加しました。

- `wiki/measurement-stack-and-claim-ceiling.md`
  - maintenance-state ladder に `high-resolution 1H-MRSI metabolite-distribution proxy` を追加しました。
  - route naming rule を更新し、`high-resolution metabolite-distribution proxy` を独立 family として visible にしました。

- `wiki/human-proxy-composition.md`
  - `What this page fixes` と family tables を更新し、`five-metabolite similarity` と `high-resolution metabolite-distribution` を collapse しないことを明記しました。
  - `Guo et al. (2025)` の reference metadata を修正しました。

- 補助同期:
  - `perspective.md`
  - `tech_roadmap.md`
  - `mind_uploading_papers.md`
  - `summary_booklet.md`
  - `wiki/verification-basics.md`
  - `github-wiki-export/*.md`
  を整合させ、front door と deep page の taxonomy drift を減らしました。

## 今回止めた誤読

- `1H-MRSI exists` = `one generic near-direct metabolic readout`
- `Lucchetti 2025` = `high-resolution metabolite-distribution mapping`
- `Guo 2025` = `just another example of the same row as Lucchetti 2025`
- `human spectroscopy` = `same quantity type`
- `similarity scaffold` = `absolute metabolite map`
- `distribution map` = `kinetic rate imaging`

## 検証結果

- `ruby scripts/export_github_wiki.rb`
  - 成功しました。
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功しました。
- `git diff --check`
  - 成功しました。
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功しました。
- export 再生成により
  - `github-wiki-export/mind-upload-eeg-rq60-grant-dataset-playbook.md`
  - `github-wiki-export/mind-upload-rq-solvability-bridge.md`
  に既存 source の最新反映差分が出ましたが、source inconsistency ではなく generated output の同期でございました。

## 外部依存タスク

- なし
  - 今回の作業は、web 上の一次文献確認、repo 内ページ改稿、export 同期、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
2. Guo R, Li Y, Zhao Y, et al. High-Resolution Brain Metabolic Imaging at Ultrahigh Field Using Extended Spatiospectral Encoding and Subspace Modeling. *IEEE Transactions on Biomedical Engineering*. 2025;72(12):3558-3566.
   - https://doi.org/10.1109/TBME.2025.3572448
3. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
4. Wright AJ, Brown GG, Haris M, et al. Mapping ATP metabolic flux in the brain using 3D localized 31P magnetization transfer. *NeuroImage*. 2022;257:119574.
   - https://doi.org/10.1016/j.neuroimage.2022.119574
5. Li Y, Guo R, Lu M, et al. Dynamic deuterium metabolic imaging of the human brain at 7 T with kinetic modeling. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
6. Karkouri J, Deelchand DK, Van de Moortele P-F, et al. Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
7. Bhogal AA, Siero JCW, Fisher E, et al. Overview of MR spectroscopic imaging: current state of the art. *Brain and Behavior*. 2020;10(10):e01852.
   - https://doi.org/10.1002/brb3.1852
8. Baboli A, Maudsley AA, Shingo T, et al. Clinical MR spectroscopic imaging of the brain: current applications and future directions. *Radiology*. 2024;312(2):e232401.
   - https://doi.org/10.1148/radiol.232401
