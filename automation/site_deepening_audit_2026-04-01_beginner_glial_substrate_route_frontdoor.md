# Site Deepening Audit (2026-04-01, beginner glial substrate-routing front-door sync)

## 対象

- 主対象:
  - `wiki/mind-upload-basics.md`
- 同期対象:
  - `github-wiki-export/mind-upload-basics.md`
- 生成物の付随同期:
  - `github-wiki-export/homeostatic-plasticity-and-maintenance-state.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- beginner front door である `wiki/mind-upload-basics.md` は、2026-04-01 時点で
  - human observability の `quantity type`
  - astrocyte PET の `route role`
  - BBB / spectroscopy / clearance の route split
  をかなり前面化できておりました。
- しかし同ページには、なお `human energetic imaging` や `astrocyte-related PET` を読んだ読者が、
  - `which glial supplier`
  - `which fuel object`
  - `which neuronal sink`
  - `which regime trigger`
  が見えているかのように誤読しうる隙が残っておりました。
- 深いページである `wiki/homeostatic-plasticity-and-maintenance-state.md` や public page 側では、すでに `glial substrate-routing` を
  - lactate-shuttle
  - starvation ketone-body
  - intensive-learning fatty-acid
  - apoE / sortilin lipid-delivery
  に分ける stop-rule が実装されております。
- にもかかわらず beginner front door にその stop-rule が visible でないのは、入口で family-internal collapse を再導入するため、影響範囲が大きいと判断いたしました。

## 主要結論

- 今回もっとも改善優先度が高かったのは、新しい glial 文献を単に増やすことではなく、`beginner page でも glial substrate-routing を独立した claim family として止めること` でございました。
- 一次文献に照らすと、`glial metabolic support` は beginner level でも少なくとも
  - claim family
  - supplier cell / neuronal sink
  - fuel object / carrier
  - regime trigger
  - human observability ceiling
  を明示しなければなりません。
- したがって今回の更新対象は、site の導線としてレバレッジが最も高い `wiki/mind-upload-basics.md` が最適でございました。

## 根拠付き批判

### 1. beginner page は human energetic proxy と glial substrate-routing の差をまだ十分に止めておりませんでした

- [Kaiser et al. (2026, `10.1177/0271678X261415784`)](https://doi.org/10.1177/0271678X261415784) は、`25 healthy volunteers` における `visual-cortex voxel` の `31P functional NAD-dynamics route` でございます。
- [Karkouri et al. (2026, `10.1002/mrm.70308`)](https://doi.org/10.1002/mrm.70308) は、`7 T` の `deuterium metabolite-mapping / absolute-quantification route` でございます。
- [Villemagne et al. (2022, `10.2967/jnumed.121.263254`)](https://doi.org/10.2967/jnumed.121.263254) は、healthy humans における `SMBT-1 MAO-B target-validation route` でございます。
- [Hiraoka et al. (2025, `10.1007/s12149-025-02083-y`)](https://doi.org/10.1007/s12149-025-02083-y) は、arterial sampling と model comparison を伴う `brain-quantification route` でございます。
- [Mesfin et al. (2026, `10.1007/s12149-025-02144-2`)](https://doi.org/10.1007/s12149-025-02144-2) は、`six healthy volunteers` と `5.5 h` の `whole-body biodistribution route` でございます。

批判:

- これらはすべて `human energetic / astrocyte-related route` に属しえますが、直接観測している object が一致しておりません。
- 31P fMRS は局所 NAD dynamics、deuterium imaging は macro metabolite / rate object、astrocyte PET は target-defined tracer route を与えるものであり、`glial supplier-fuel-sink path` をそのまま観測しているわけではございません。
- よって `human energetic imaging exists` や `astrocyte PET exists` を `glial substrate-routing is visible` と読むことは、2026-04-01 時点の一次文献からは支持されません。

### 2. glial substrate-routing 自体が、すでに 1 本の route ではございません

- [Suzuki et al. (2011, `10.1016/j.cell.2011.02.018`)](https://doi.org/10.1016/j.cell.2011.02.018) は、`astrocyte-neuron lactate transport` が長期記憶形成に必要であることを示した `lactate-shuttle route` でございます。
- [Silva et al. (2022, `10.1038/s42255-022-00528-6`)](https://doi.org/10.1038/s42255-022-00528-6) は、starvation 下で `glial ketogenesis` が記憶維持を支える `ketone-body route` でございます。
- [Pavlowsky et al. (2025, `10.1038/s42255-025-01416-5`)](https://doi.org/10.1038/s42255-025-01416-5) は、`intensive learning` 後の `glia-to-neuron fatty-acid route` でございます。
- [Greda et al. (2025, `10.1038/s42255-025-01389-5`)](https://doi.org/10.1038/s42255-025-01389-5) は、glucose limitation 下での `apoE3 / sortilin-dependent lipid-delivery and neuronal fuel-choice route` でございます。
- [Qi et al. (2021, `10.1016/j.celrep.2020.108572`)](https://doi.org/10.1016/j.celrep.2020.108572) は、`ApoE4` により `neuron-astrocyte coupling of fatty-acid metabolism` が損なわれることを示し、coupling 自体が genotype-sensitive であることを示しました。

批判:

- 上記 5 本は、fuel object, supplier cell, neuronal sink, regime trigger, and failure mode が一致しておりません。
- したがって `glial metabolic support` という 1 語へ戻すと、
  - lactate
  - ketone
  - fatty acid
  - lipoprotein-mediated lipid uptake
  - genotype-conditioned coupling
  の非同一性を入口で消してしまいます。

### 3. よって beginner page には `human observability ceiling` を明示する stop-rule が必要でございました

- 上記 mechanistic literature は、glial route を `one background support variable` ではなく `family of distinct controllers` として扱うことを要求しております。
- 他方で current living-human route は、macro energetic or target-defined proxy を押し上げてはおりますが、`operative glial supplier-fuel-sink route` そのものは直接識別しておりません。
- これは current human-route literature からの推論でございます。すなわち、
  - `31P functional NAD-dynamics`
  - `deuterium metabolite / rate imaging`
  - `SMBT-1 / I2BS astrocyte-related PET`
  は、それぞれ異なる bounded object を constraining しており、`in vivo glial substrate-routing identity` までは上げられません。

批判:

- beginner page にこの abstention がないと、読者は
  - `human energetic proxy exists`
  - `astrocyte PET exists`
  - `therefore metabolic support is mostly visible`
  と短絡しえます。
- その short cut は、現在の一次文献では支持されておりませんでした。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `page_highlights` に、`human energetic imaging / astrocyte PET ≠ glial substrate-routing identification` の bullet を追加しました。
  - `known_points` に、current human route が `supplier / fuel / sink` を特定しないことを明文化しました。
  - `2026-04-01 correction: glial substrate-routing is not a generic energetic row` note-box を追加しました。
  - `What still remains outside these human routes` を、`glial substrate-routing` を独立 hidden-state family として visible にする文言へ更新しました。
  - bibliography に `Suzuki / Silva / Qi / Pavlowsky / Greda` を追加しました。
  - `What to do with that information` に `maintenance-state families` を明示し、次導線を補強しました。

- `github-wiki-export/mind-upload-basics.md`
  - export を再生成して同期しました。

- `github-wiki-export/homeostatic-plasticity-and-maintenance-state.md`
  - 今回 source file 自体は編集しておりませんが、export 再生成により既存 source との差分が output 側へ反映されました。
  - これは generated file の同期であり、今回の主修正対象ではございません。

## 今回止めた誤読

- `human energetic imaging exists` = `glial substrate-routing is directly observed`
- `astrocyte-related PET exists` = `fuel-routing route is identified`
- `glial metabolic support` = `one route family`
- `glial substrate-routing` = `astrocyte-network state`
- `macro energetic proxy` = `supplier-fuel-sink identity`

## 検証

- `ruby scripts/export_github_wiki.rb`
  - 成功しました。
- `VERIFY_GITHUB_WIKI_BUILD=1 scripts/verify_github_wiki_toolchain.sh`
  - syntax / boundary / ops-reference / noise-cleanup までは通過しました。
  - その後の `export-validate` は、今回生成した `github-wiki-export/*.md` の未コミット差分検知で停止しました。
  - これは generated file の drift 検知であり、内容不整合ではございません。
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功しました。
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功しました。

## 外部依存タスク

- なし
  - 今回の作業は、一次文献確認、repo 内ページ改稿、export 同期、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Suzuki A, Stern SA, Bozdagi O, Huntley GW, Walker RH, Magistretti PJ, Alberini CM. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011;144(5):810-823.
   - https://doi.org/10.1016/j.cell.2011.02.018
2. Silva B, et al. Glial ketogenesis regulates memory maintenance during starvation. *Nature Metabolism*. 2022;4:1534-1547.
   - https://doi.org/10.1038/s42255-022-00528-6
3. Qi G, Mi Y, Shi X, Gu H, Brinton RD, Yin F. ApoE4 impairs neuron-astrocyte coupling of fatty acid metabolism. *Cell Reports*. 2021;34(1):108572.
   - https://doi.org/10.1016/j.celrep.2020.108572
4. Pavlowsky A, et al. Neuronal fatty acid oxidation fuels memory after intensive learning in Drosophila. *Nature Metabolism*. 2025;7:2467-2483.
   - https://doi.org/10.1038/s42255-025-01416-5
5. Greda AK, et al. Interaction of sortilin with apolipoprotein E3 enables neurons to use long-chain fatty acids as alternative metabolic fuel. *Nature Metabolism*. 2025;7:2346-2365.
   - https://doi.org/10.1038/s42255-025-01389-5
6. Kaiser A, Vind FA, Duarte JMN, Jelescu I, Lin Y, Yu X, Widmaier M, Wenz D, Xin L. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
7. Karkouri J, Deelchand DK, Van de Moortele P-F, et al. Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
8. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263254
9. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025;39:255-265.
   - https://doi.org/10.1007/s12149-025-02083-y
10. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
