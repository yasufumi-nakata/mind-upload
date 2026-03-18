# Site Deepening Audit (2026-03-18, Literature Entrance Needs an Observability Evidence Class)

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `research_harvest_50.md`
- 副対象: `wiki/paper-source-types-and-evidence-status.md`
- 副対象: `wiki/literature-and-evidence-reading.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`direct validator`、`task-limited system demo`、`dataset / benchmark / standard / toolchain`、`mechanistic boundary / hidden-state evidence` まではかなり整理できておりました。
- しかし文献入口ページ群では、近年の human measurement papers が押し上げているものが、まだ独立の evidence class として固定されていませんでした。
- これは技術・自然科学の観点で重要です。なぜなら、Shapson-Coe、Johansen、Lucchetti、Baadsvik、Rzechorzek、Hirschler のような論文は `system demo` でも `hidden-state closure` でもなく、`人間で今どの measurement class が見えるか` を押し上げる論文だからです。

## 根拠付き批判

### 1. 旧 literature entrance は `human measurement advance` の置き場を持っていませんでした

- 問題:
  - `mind_uploading_papers.md` の evidence class は `direct validator / demo / standard-benchmark / mechanistic boundary / review / context` でした。
  - そのため、human-side observability を押し上げる論文が `demo` か `boundary` に吸収されやすい構造でした。
- 根拠:
  - <https://doi.org/10.1126/science.adk4858> の Shapson-Coe et al. (2024) は、外科切除ヒト皮質 1 mm^3 の nanoscale ultrastructure reconstruction を示しました。これは `local human structural scaffold` の前進です。
  - <https://doi.org/10.1523/JNEUROSCI.1750-23.2024> の Johansen et al. (2024) は、高解像度 SV2A PET により `in vivo human synaptic-density atlas` を示しました。これは `regional synaptic-density proxy` の前進です。
  - <https://doi.org/10.1038/s41467-025-66124-w> の Lucchetti et al. (2025) は、whole-brain 1H-MRSI から `metabolic connectome` を構成しました。これは `macro biochemical scaffold` の前進です。
  - <https://doi.org/10.1002/mrm.29998> の Baadsvik et al. (2024) は、in vivo human brain における `myelin bilayer mapping` を示しました。これは `macro myelin proxy` の前進です。
  - <https://doi.org/10.1093/brain/awab466> の Rzechorzek et al. (2022) は healthy human brain thermometry により `4D temperature map` を構成しました。これは `macro thermal proxy` の前進です。
  - <https://doi.org/10.1038/s41593-025-02073-3> の Hirschler et al. (2025) は `CSF mobility` を noninvasive に高分解能で計測しました。これは `macro clearance / support-state proxy` の前進です。
- 批判:
  - したがって、これらを `human side でも測れ始めた` という 1 行で処理するのは粗すぎます。
  - 本来は `observability-class advance / human proxy ladder` を独立させ、`何が直接見えたか` と `何がまだ latent か` を最初から分けるべきでした。

### 2. 旧 page は `measurement gets stronger` と `state-complete gets closer` を十分に分離していませんでした

- 問題:
  - 文献入口ページでは `technology/natural science priority route` がありましたが、その中に `human observability` が独立 route として存在しませんでした。
- 根拠:
  - Shapson-Coe は living whole-brain state ではなく `fixed-tissue local ultrastructure` です。
  - Johansen は `regional synaptic-density proxy` であり、current synaptic efficacy や branch-local tag-capture を直接読んでいません。
  - Lucchetti は `biochemical organization` を押し上げていますが、current transcription / chromatin controller や branch-local energetic reserve を直接読んでいません。
  - Rzechorzek は `macro thermal map` を与えますが、cell-specific microtemperature や synapse-level heating burden を直接読んでいません。
  - Hirschler は `CSF mobility` を高分解能で見せますが、cell-specific immune control や local synaptic maintenance controller を直接読んでいません。
- 批判:
  - よって、human measurement papers を独立 route に置かないと、読者は `近年 human で色々見えた` を `hidden state がかなり埋まった` と誤読しやすくなります。

### 3. 旧 wiki の `source / status / evidence` 説明は、なお observability-class advance を欠いていました

- 問題:
  - `wiki/paper-source-types-and-evidence-status.md` は source type と status label を整理していましたが、`paper が何を直接増やすか` の表に observability class がありませんでした。
- 批判:
  - これは site-wide rule の欠落です。
  - 文献入口で `human PET / MRS / MRI paper` を見たとき、`それは demo か、validator か、proxy ladder か` を判定できないと、badge と chronology を超えた科学的読み方になりません。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points に `observability-class advance` を追加
  - `Priority route for technology and natural sciences` に `human observability / proxy ladder` を新設
  - `technical-evidence-classes` に `observability-class advance / human proxy ladder` を追加
  - `how to use` とテーマ別読書導線に `what humans can actually observe now` の入口を追加
  - 末尾 table の壊れた `structure estimation / hidden state` 行を修正
- `research_harvest_50.md`
  - `last_updated` を `2026-03-18` に更新
  - technical priority route を `measurement and human observability` へ拡張
  - human measurement papers を独立 evidence class として読む note を追加
- `wiki/paper-source-types-and-evidence-status.md`
  - title / subtitle / front matter を `source types + status labels + evidence classes` に更新
  - `three axes` を `four axes` に改め、evidence class を独立軸として追加
  - `observability-class advance / human proxy ladder` を含む evidence class table を新設
  - `human proxy paper = hidden state solved` という誤読を明示的に禁止
- `wiki/literature-and-evidence-reading.md`
  - `last_updated` を `2026-03-18` に更新
  - technical reading note に `human observability` を追加
  - misreading prevention を 4 rules 化し、`observability ≠ sufficiency` を明示

## 外部依存で保留

- なし
  - 今回の作業は公開本文・読み方ガイド・監査記録の改稿で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Finnema SJ, Nabulsi NB, Eid T, et al. Imaging synaptic density in the living human brain. *Science Translational Medicine*. 2016;8(348):348ra96.
   - https://doi.org/10.1126/scitranslmed.aaf6667
3. Naganawa M, Li S, Nabulsi N, et al. First-in-Human Evaluation of 18F-SynVesT-1, a Radioligand for PET Imaging of Synaptic Vesicle Glycoprotein 2A. *Journal of Nuclear Medicine*. 2021;62(4):561-567.
   - https://doi.org/10.2967/jnumed.120.249144
4. Johansen A, Hansen HD, Chonde DB, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024;44(29):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
5. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
6. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
7. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022;145(6):2031-2048.
   - https://doi.org/10.1093/brain/awab466
8. Hirschler L, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28:2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
