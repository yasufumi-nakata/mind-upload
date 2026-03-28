# Site Deepening Audit (2026-03-29, literature-hub spectroscopy taxonomy sync)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- 2026-03-28 から 2026-03-29 にかけて、front door 側の主要ページでは `31P` と deuterium の内部 split がかなり厳密に更新されておりました。
- しかし文献ハブである `mind_uploading_papers.md` と、問題別 evidence bank である `research_harvest_50.md` には、
  - `31P energetic balance`
  - `deuterium metabolite / rate imaging`
  のような、いまの site-wide taxonomy より一段粗い前景化がまだ残っておりました。
- このズレを放置すると、入口ページでは止めている誤読を、文献導線から再度流入させてしまいます。

## 主要結論

- `31P` は少なくとも
  - resting metabolite / pH balance
  - MT exchange-flux
  - whole-brain intracellular NAD-content mapping
  - localized functional NAD-dynamics
  に分けて読むべきでございます。
- deuterium 系も少なくとも
  - absolute metabolite mapping / quantification
  - blood-input / kinetic-model conditioned rate imaging
  - dose / protocol dependence
  - stated operating-point repeatability
  に分けて読むべきでございます。
- したがって literature hub でも、`spectroscopy improved` や `human metabolic proxy improved` のような圧縮を残してはいけません。

## 根拠付き批判

### 1. `31P` は modality 名だけでは inferential object が固定されません

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は resting human brain における ATP synthesis, phosphorus metabolites, pH, T1 を扱う route でございます。
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) は 7 T band-inversion / MT と 5-pool model を用い、PCr→ATP と Pi→ATP exchange flux を扱う route でございます。
- [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111) は 7 T whole-brain intracellular NAD-content map を示しました。
- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) は prior fMRI で局在化した occipital voxel における task-evoked NAD+ dynamics を示しました。

批判:

- これらを `31P energetic balance` の一段に押し込むと、resting balance, exchange-flux, macro NAD-content map, localized task dynamics が同じ row に潰れます。
- しかし quantity type, spatial support, time window, localization burden, model burden が違うため、同じ calibrator role を与えるのは不正確でございます。

### 2. deuterium も `metabolite / rate imaging` の一語では足りません

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は 7 T dynamic DMI から HDO / Glc / Glx / Lac の absolute concentrations と rates を explicit quantification pipeline で扱いました。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は dynamic DMRSI と blood-input / kinetic model により glucose-transport と key metabolic-rate terms を推定しました。
- [Ahmadian et al. (2025)](https://doi.org/10.1002/jmri.29532) は [6,6'-²H₂]glucose dose の違いが brain-side deuterated-metabolite visibility に影響することを示しました。
- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は 3 T healthy-volunteer DMI の repeatability を、ある stated protocol の operating-point 性質として示しました。

批判:

- `deuterium metabolite / rate imaging` の一語では、absolute metabolite distributions と kinetic-rate maps が区別されません。
- さらに dose / protocol dependence と repeatability を書かないと、読者は `deuterium route exists` を `portable energetic meter exists` に誤変換します。

### 3. literature hub 側の粗さは、front door 側の厳密さを相殺します

- `index.md`, `wbe_101.md`, `verification.md`, `wiki/human-proxy-composition.md`, `wiki/measurement-stack-and-claim-ceiling.md` では、すでに spectroscopy-derived human routes を family-split で読む規則が導入されております。
- それにもかかわらず literature hub 側に粗い要約が残ると、読者は detailed page に進む前に `one human spectroscopy ladder` の理解へ戻ってしまいます。

批判:

- 文献アーカイブと evidence bank は、詳細ページより taxonomy が古くてよい場所ではございません。
- むしろ archive front door は「どの route family の論文を読んでいるか」を最初に固定する役割を持つべきでございます。

## 今回実行した変更

- `mind_uploading_papers.md`
  - known-points と 2026 technical addendum を更新し、`31P` と deuterium の内部 split を front door で明示しました。
  - `Human in vivo observability ladder` と `observability-class advance / human in vivo proxy ladder` の rows を更新し、route family を quantity type ごとに分解しました。

- `research_harvest_50.md`
  - `Read human measurement papers as their own evidence class` を更新し、spectroscopy-derived human routes を family-split で説明するようにしました。
  - calibrator table に `Ren 2015`, `Ren 2017`, `Guo 2024`, `Kaiser 2026`, `Karkouri 2026` の rows を追加し、deuterium kinetic-rate row も明確化しました。

## 今回止めた誤読

- `31P paper exists` = `human energetic state is one row closer to solved`
- `resting 31P balance` = `MT exchange flux` = `whole-brain NAD content` = `localized task-evoked NAD dynamics`
- `deuterium imaging exists` = `absolute metabolite map` = `kinetic rate map` = `portable stable energetic meter`
- `literature hub だから少し粗くてよい`

## 外部依存タスク

- なし
  - 今回の変更は web 上の一次文献確認、repo 内本文修正、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
2. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26560
3. Guo R, Yang S, Wiesner HM, et al. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. *Frontiers in Neuroscience*. 2024.
   - https://doi.org/10.3389/fnins.2024.1389111
4. Kaiser A, Vind FA, Duarte JMN, et al. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
5. Karkouri J, Novoselova M, Rodgers CT, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
6. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
7. Ahmadian N, Karkouri J, Deelchand DK, et al. Human Brain Deuterium Metabolic Imaging at 7 T: Impact of Different [6,6'-2H2]Glucose Doses. *Journal of Magnetic Resonance Imaging*. 2025.
   - https://doi.org/10.1002/jmri.29532
8. Bøgh N, Vaeggemose M, Schulte RF, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024.
   - https://doi.org/10.1186/s41747-024-00426-4
