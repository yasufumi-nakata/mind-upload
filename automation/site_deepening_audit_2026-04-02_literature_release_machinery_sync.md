# Site Deepening Audit (2026-04-02, literature front-door release-machinery sync)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.7554/eLife.18167`
- `https://doi.org/10.1038/s41593-017-0041-9`
- `https://doi.org/10.1038/s41467-022-33565-6`
- `https://doi.org/10.1038/s41593-024-01720-5`
- `https://doi.org/10.1177/0271678X20946198`
- `https://doi.org/10.1038/s41586-020-03134-2`
- `https://doi.org/10.1038/s41467-024-53901-2`
- `https://doi.org/10.1007/s00259-024-06885-6`
- `https://doi.org/10.1523/JNEUROSCI.1750-23.2024`
- `https://doi.org/10.1038/s41380-024-02776-2`
- `https://doi.org/10.1162/imag_a_00190`
- `https://doi.org/10.1038/s41380-022-01465-2`

## 今回この箇所を選んだ理由

- 2026-04-01 時点で、core page 側ではすでに
  - `regional SV2A density`
  - `same-brain structure-function linkage`
  - `presynaptic release machinery / active-zone nanostructure`
  を切り分ける rule が入っておりました。
- しかし literature front door である
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
  には、その stop line が十分に前面化されておらず、読者が
  - `SV2A PET`
  - `same-brain functional connectomics`
  - `human measurement advance`
  を、current presynaptic release machinery の根拠として過読する余地が残っておりました。
- したがって今回の correction value は、新 topic の追加ではなく、既存の文献入口に `release-machinery ceiling` を site-wide rule として同期することにございました。

## 主要結論

- `same-brain scaffold` は `presynaptic release-machinery truth` ではございません。
- `regional SV2A density` は `release-site number` ではございません。
- `release probability` は重要ですが、それだけで `active-zone nanostructure / priming-site assembly` を尽くしません。
- よって literature front door でも
  - `synapse count`
  - `regional SV2A density`
  - `same-brain structure-function linkage`
  - `release-site number`
  - `docked-vesicle architecture`
  - `active-zone nanostructure / priming-site assembly`
  - `current release competence`
  を別 object として明示する必要がございました。

## 根拠付き批判

### 1. Human synapse / same-brain correspondence だけでは release-site architecture は閉じません

- 根拠:
  - [Molnár et al. (2016)](https://doi.org/10.7554/eLife.18167)
  - [Holler et al. (2021)](https://doi.org/10.1038/s41586-020-03134-2)
- 批判:
  - human synapse には複数 docked vesicle と multivesicular release があり、さらに structure-function correspondence が強くても、それだけで current release-ready architecture は一意化されません。
  - よって `same-brain structure-function linkage` を `release-site truth` に昇格させるのは過読でございます。

### 2. Presynaptic weight / release probability は one scalar ではございません

- 根拠:
  - [Sakamoto et al. (2018)](https://doi.org/10.1038/s41593-017-0041-9)
  - [Dürst et al. (2022)](https://doi.org/10.1038/s41467-022-33565-6)
  - [Emperador-Melero et al. (2024)](https://doi.org/10.1038/s41593-024-01720-5)
- 批判:
  - release probability は synaptic strength に強く関わりますが、release-site number や active-zone の内部機構を一つの scalar に圧縮して読むことはできません。
  - したがって `current synaptic efficacy` や `release probability` を `presynaptic machinery` 全体の proxy として扱うのも不適切でございます。

### 3. SV2A PET は release-machinery readout ではなく route-sliced proxy でございます

- 根拠:
  - [Naganawa et al. (2024)](https://doi.org/10.1007/s00259-024-06885-6)
  - [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024)
  - [Matuskey et al. (2025)](https://doi.org/10.1038/s41380-024-02776-2)
  - [Shatalina et al. (2024)](https://doi.org/10.1162/imag_a_00190)
  - [Smart et al. (2021)](https://doi.org/10.1177/0271678X20946198)
  - [Holmes et al. (2022)](https://doi.org/10.1038/s41380-022-01465-2)
- 批判:
  - quantification route、healthy atlas、disease contrast、task association、activation null、intervention response は別 slice であり、一つの `SV2A PET` として束ねると claim ceiling が崩れます。
  - 特に Smart et al. は brief activation で delivery は変わっても binding は変わらないことを示しており、momentary release competence の meter として読むことを直接止めます。

### 4. Same-brain scaffold と SV2A の両方を literature front door で止める必要がございました

- 根拠:
  - [Mittermaier et al. (2024)](https://doi.org/10.1038/s41467-024-53901-2)
  - [Smart et al. (2021)](https://doi.org/10.1177/0271678X20946198)
- 批判:
  - same-brain 側では membrane-state-gated consolidation が残り、SV2A 側では activation-timescale ceiling が残ります。
  - したがって、この2系統はどちらも `bounded calibrator class` として扱うべきであり、front door から同一 object に圧縮してはなりません。

## 今回実行した変更

- `mind_uploading_papers.md`
  - front matter の `note` を更新しました。
  - `known_points` と `page_highlights` に、same-brain scaffold / SV2A proxy と presynaptic release machinery を切り分ける rule を追加しました。
  - `Read SV2A / synaptic-density PET as several separate questions` の直後に、新しい note-box を追加しました。
  - `Same-brain functional connectomics is not a solved local twin` note-box を更新し、release-site number / active-zone nanostructure ceiling を同期しました。
  - `technical-evidence-classes` 節に、Molnár / Sakamoto / Dürst / Emperador-Melero / Holler / Mittermaier を mechanistic ceiling として接続しました。
  - evidence-class table の
    - `destructive-structure audit`
    - `observability-class advance / human in vivo proxy ladder`
    - `mechanistic boundary / hidden-state evidence`
    を更新し、release-machinery ceiling を明文化しました。

- `research_harvest_50.md`
  - front matter の `note` を更新しました。
  - `page_highlights` と `known_points` に、same-brain scaffold / SV2A proxy の ceiling rule を追加しました。
  - `Read same-brain functional connectomics as scaffold, not as a solved local twin` note-box を更新しました。
  - SV2A 説明段落の直後に、same-brain と SV2A をまとめて release-machinery ceiling へ接続する段落を追加しました。
  - U7 の anchor table で
    - Johansen
    - Naganawa
    - Matuskey
    - Shatalina
    の `Still not closed` を更新しました。
  - 同 table に
    - Smart et al. (2021)
    - Holmes et al. (2022)
    の行を追加し、activation-timescale ceiling と intervention-response ceiling を front door へ可視化しました。

## 今回止めた誤読

- `same-brain local scaffold` = `presynaptic release-machinery truth`
- `regional SV2A density` = `release-site number`
- `SV2A PET activation study` = `momentary synaptic efficacy meter`
- `SV2A intervention study` = `current release competence readout`
- `current synaptic efficacy` = `active-zone architecture`

## 検証結果

- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功しました。
- `git diff --check`
  - 成功しました。
- `rg -n "presynaptic release-machinery ceiling|presynaptic release-machinery truth|Holmes et al. \\(2022\\)|release-site number, active-zone nanostructure / priming-site assembly" _site/mind_uploading_papers.html _site/research_harvest_50.html`
  - `_site` 側へ新しい stop line と Smart / Holmes 行が反映されていることを確認しました。

## 外部依存タスク

- なし
  - 今回の作業は、web 上の一次文献確認、本文修正、build / diff / generated HTML 確認、commit、push までこのセッションで完結できます。

## 参考文献

1. Molnár G, Rózsa M, Baka J, Holderith N, Barzó P, Nusser Z, Tamás G. Human pyramidal to interneuron synapses are mediated by multi-vesicular release and multiple docked vesicles. *eLife*. 2016;5:e18167.
   - https://doi.org/10.7554/eLife.18167
2. Sakamoto H, Ariyoshi T, Kimpara N, Sugao K, Taiko I, Takikawa K, Asanuma D, Namiki S, Hirose K. Synaptic weight set by Munc13-1 supramolecular assemblies. *Nature Neuroscience*. 2018;21(1):41-49.
   - https://doi.org/10.1038/s41593-017-0041-9
3. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022;13:6126.
   - https://doi.org/10.1038/s41467-022-33565-6
4. Emperador-Melero J, Andersen JW, Metzbower SR, et al. Distinct active zone protein machineries mediate Ca<sup>2+</sup> channel clustering and vesicle priming at hippocampal synapses. *Nature Neuroscience*. 2024;27:1680-1694.
   - https://doi.org/10.1038/s41593-024-01720-5
5. Smart K, Liu H, Matuskey D, et al. Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
6. Holler S, et al. Structure and function of a neocortical synapse. *Nature*. 2021;591:111-116.
   - https://doi.org/10.1038/s41586-020-03134-2
7. Mittermaier FX, Kalbhenn T, Xu R, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024;15:10340.
   - https://doi.org/10.1038/s41467-024-53901-2
8. Naganawa M, et al. Quantification of synaptic density in the human brain with <sup>18</sup>F-SynVesT-1 PET. *European Journal of Nuclear Medicine and Molecular Imaging*. 2024.
   - https://doi.org/10.1007/s00259-024-06885-6
9. Johansen A, et al. Regional synaptic density mapped in vivo in the healthy human brain. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
10. Matuskey D, et al. Synaptic density in autistic adults measured with [<sup>11</sup>C]UCB-J PET. *Molecular Psychiatry*. 2025.
   - https://doi.org/10.1038/s41380-024-02776-2
11. Shatalina E, et al. Synaptic vesicle glycoprotein 2A PET and task-switching behavior in healthy adults. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00190
12. Holmes SE, et al. Ketamine does not produce measurable overall SV2A change 24 h after treatment despite symptom improvement. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-022-01465-2
