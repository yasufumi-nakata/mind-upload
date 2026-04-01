# Site Deepening Audit (2026-04-01, deuterium operating-point sync)

## 対象

- 主対象:
  - `index.md`
  - `wbe_101.md`
  - `research_harvest_50.md`
  - `wiki/human-proxy-composition.md`
- 同期対象:
  - `github-wiki-export/human-proxy-composition.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.1093/pnasnexus/pgaf072`
- `https://doi.org/10.1002/mrm.70308`
- `https://doi.org/10.1002/jmri.29532`
- `https://doi.org/10.1186/s41747-024-00426-4`

## 今回この箇所を選んだ理由

- site 全体ではすでに `1H-MRSI` / `31P` / `deuterium` の quantity-type split はかなり進んでおりました。
- しかし front door 側では、`deuterium absolute quantification` と `deuterium kinetic-rate imaging` を分けた後でも、まだ `deuterium` という family 名だけで route burden がほぼ固定されたように読める箇所が残っておりました。
- とくに
  - `dose dependence`
  - `time-point dependence`
  - `same-setup repeatability`
  - `mixed healthy / pathology cohort`
  が入口ページでは弱く、deep page の厳密さに比べて再圧縮の余地が残っておりました。

## 主要結論

- `deuterium` は quantity type だけで止めるとまだ粗すぎます。
- 一次文献が支持する最小の安全読解単位は、少なくとも
  - `absolute quantification` か `kinetic-rate imaging` か
  - `dose`
  - `timing window`
  - `field strength / coil route`
  - `same-setup repeatability` か `cross-protocol portability` か
  - `healthy-only` か `mixed healthy / pathology method paper` か
  を明示した operating point でございます。
- したがって `deuterium imaging exists` を
  - generic energetic observability
  - route-free portability
  - protocol-independent repeatability
  - healthy-human baseline readiness
  に昇格させるのは、現行一次文献では支持されません。

## 根拠付き批判

### 1. absolute quantification と kinetic-rate imaging を分けても、なお operating point が残ります

- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は `7 T dynamic DMRSI`、`blood input`、`explicit kinetic model`、`0.7 cc nominal voxel`、`2.5 min/image`、`five healthy participants` という強い route burden つきで kinetic-rate maps を示しております。
- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は `absolute quantification` を強めましたが、`12 healthy volunteers + 5 glioblastoma patients` の mixed-cohort method paper であり、abstracted protocol では `two healthy post-glucose scans` に留まります。

批判:

- よって `absolute` と `kinetic` を分けただけでは不十分でございます。
- その route がどの cohort・どの operating point で成立しているのかまで visible にしなければ、human observability の ceiling を過大評価しやすくなります。

### 2. deuterium route は dose-invariant ではありません

- [Ahmadian et al. (2025)](https://doi.org/10.1002/jmri.29532) は human-brain DMI signal が administered `[6,6'-2H2]glucose dose` に materially depend することを示しました。

批判:

- したがって `deuterium map` を route-free quantity と読むことはできません。
- 同じ family 名でも、投入量が変われば downstream metabolite visibility 自体が変わるため、dose disclosure なしの比較は危ういです。

### 3. repeatability は protocol-free の性質ではありません

- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は healthy volunteers における `3 T DMI` repeatability を示しましたが、それは named oral-glucose protocol と named time-point window の下での結果であり、whole-brain repeatability は `120 min` が最良でございました。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) でも repeated dynamic DMRSI の類似性は `same brain / same setup / same acquisition parameters` という operating point に留まっております。

批判:

- よって `repeatable deuterium imaging exists` を `portable deuterium route exists` と読み替えるのは誤りでございます。
- route-local repeatability と cross-protocol portability は分けて明示すべきです。

### 4. front door が operating-point burden を落とすと、deep page の厳密さが相殺されます

- `faq.md` や一部の deeper technical pages では、すでに deuterium に対して `dose` / `repeatability` / `mixed cohort` の caution が入っておりました。
- 一方で入口ページや primer 側では、まだ `deuterium` を quantity-type split 後の比較的きれいな family 名として読みやすい箇所が残っておりました。

批判:

- これは site-wide governance 上の弱点でございます。
- 深いページで止めた overreading が、入口の粗さから再流入するからでございます。

## 今回実行した変更

### `index.md`

- spectroscopy front-door note を更新し、
  - `Li et al. (2025)` の same-setup operating point
  - `Karkouri et al. (2026)` の mixed healthy / glioblastoma cohort
  - `Ahmadian et al. (2025)` の dose dependence
  - `Bøgh et al. (2024)` の time-point-dependent repeatability
  を追加しました。
- `deuterium` rows are not dose-, timing-, or protocol-invariant by default という stop lineを明示しました。

### `wbe_101.md`

- spectroscopy note-box を改稿し、deuterium family に operating-point burden が残ることを明記しました。
- deuterium table rows を更新し、
  - Karkouri row に `dose / timing invariance` 非成立を追加
  - Li row に `same-setup repeatability` 限定を追加
 しました。
- references に
  - Ahmadian et al. (2025)
  - Bøgh et al. (2024)
  を追加しました。

### `research_harvest_50.md`

- `Read human measurement papers as their own evidence class` note を更新し、deuterium family 内で `dose` と `repeatability regime` が route burden であることを追加しました。
- deuterium rows を更新し、
  - Karkouri row を mixed healthy / glioblastoma workflow として明示
  - Li row を fixed 7 T operating point として明示
 しました。

### `wiki/human-proxy-composition.md`

- deuterium absolute-quantification row に mixed cohort / two healthy post-glucose detail を追加しました。
- deuterium kinetic-rate row に same-operating-point repeatability limitation を追加しました。
- `Deuterium route names still hide operating-point dependence` note-box を新設し、
  - quantity type
  - dose
  - timing window
  - field strength / coil route
  - within-setup repeatability vs cross-protocol portability
  の開示を composition rule に組み込みました。
- references に Ahmadian et al. (2025) を追加しました。

### `github-wiki-export/human-proxy-composition.md`

- `ruby scripts/export_github_wiki.rb` により wiki 側変更を export 側へ同期しました。

## 今回止めた誤読

- `deuterium imaging` = one stable human energetic row
- `absolute quantification` = route-free healthy baseline
- `kinetic-rate imaging` = generic energetic portability
- `repeatability shown` = cross-protocol portability shown
- `same family name` = same dose / timing / coil / cohort burden

## 検証

- `ruby scripts/export_github_wiki.rb`
  - 成功
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功
- `bundle exec jekyll build`
  - 成功
- `git diff --check`
  - 成功
- `rg -n "dose|120 min|same operating point|mixed 12-healthy / 5-glioblastoma|two healthy post-glucose" _site/index.html _site/wbe_101.html _site/research_harvest_50.html _site/wiki/human-proxy-composition.html github-wiki-export/human-proxy-composition.md`
  - 追加文面が build 出力と wiki export に反映されていることを確認

## external dependency tasks

- なし
  - 今回の主作業は、一次文献確認、公開文面改稿、wiki export 同期、build 検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
2. Karkouri J, Novoselova M, Rodgers CT, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. *Magnetic Resonance in Medicine*. 2026. https://doi.org/10.1002/mrm.70308
3. Ahmadian N, Karkouri J, Deelchand DK, et al. Human Brain Deuterium Metabolic Imaging at 7 T: Impact of Different [6,6'-2H2]Glucose Doses. *Journal of Magnetic Resonance Imaging*. 2025. https://doi.org/10.1002/jmri.29532
4. Bøgh N, Vaeggemose M, Schulte RF, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024. https://doi.org/10.1186/s41747-024-00426-4
