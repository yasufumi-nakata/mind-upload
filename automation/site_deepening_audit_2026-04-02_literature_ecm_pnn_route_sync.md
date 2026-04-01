# Site Deepening Audit (2026-04-02, literature ECM / PNN route sync)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 同期先:
  - `index.md`
  - `verification.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://mind-upload.com/mind_uploading_papers.html`
- `https://mind-upload.com/research_harvest_50.html`
- `https://mind-upload.com/index.html`
- `https://mind-upload.com/verification.html#maintenance-state-error-budget`
- `https://mind-upload.com/wiki/homeostatic-plasticity-and-maintenance-state.html#ecm-pnn-route-card`
- `https://doi.org/10.1126/science.1072699`
- `https://doi.org/10.1038/nn.2338`
- `https://doi.org/10.1016/j.cell.2020.05.050`
- `https://doi.org/10.1016/j.matbio.2024.11.001`
- `https://doi.org/10.1523/JNEUROSCI.1626-24.2024`
- `https://doi.org/10.1111/acel.70139`
- `https://doi.org/10.1002/epi4.12963`
- `https://doi.org/10.1007/s12035-024-04306-1`

## 今回この箇所を選んだ理由

- `mind_uploading_papers.md` と `research_harvest_50.md` は、このサイトで文献一覧から入る読者にとっての主要な front door でございます。
- 2026-04-02 時点で、トップページ、verification、wiki 側ではすでに
  - ECM / PNN gate state
  - shared extracellular / electrical state
  - generic support variable
  を分ける stop line が入っておりました。
- しかし文献 front door 側では、maintenance-state family split の説明に ECM / PNN がまだ十分に露出しておらず、読者が
  - matrix biology
  - PNN remodeling
  - memory support
  - human histology
  を再び一つの support bucket に圧縮して読む余地が残っておりました。

## 主要結論

- ECM / PNN 文献は、少なくとも
  - plasticity-window reopening
  - receptor-mobility / short-term-plasticity constraint
  - microglia-driven ECM remodeling
  - synapse-specific inhibitory-plasticity control
  - CA2-versus-PV memory support
  - age-linked rescue
  - human ex vivo histology
  の route families に分けて読むべきでございます。
- よって、このサイトの文献 front door でも ECM / PNN を maintenance-state family split の独立項目として明示し、generic support への圧縮を止める必要がございました。
- 安全な上限は、`ECM / PNN route-family evidence` であって、
  - living-human whole-brain ECM gate-state readout
  - one common plasticity meter
  - solved human maintenance observable
  ではございません。

## 根拠付き批判

### 1. PNN 除去による plasticity 再開は「可塑性窓の再開」 route であり、一般 support ではございません

- [Pizzorusso et al. (2002)](https://doi.org/10.1126/science.1072699) は、adult visual cortex で perineuronal-net digestion により ocular-dominance plasticity を再活性化できることを示しました。

批判:

- これは ECM / PNN が `whether a prior plasticity gate can be reopened` を左右する route であることを示します。
- したがって ECM / PNN 論文を単に `support variable` としてまとめると、可塑性窓の開閉という重要な route-specific claim を失います。

### 2. ECM は receptor mobility / short-term plasticity の制約 route でもあり、同じ意味ではございません

- [Frischknecht et al. (2009)](https://doi.org/10.1038/nn.2338) は、brain extracellular matrix が AMPA receptor の lateral mobility と short-term synaptic plasticity を制約することを示しました。

批判:

- これは `matrix exists` という静的説明ではなく、受容体移動度と短期可塑性の operating regime を変える route でございます。
- したがって、Pizzorusso 型の plasticity-window reopening と同じ bucket に落とすのは不正確でございます。

### 3. Microglia-ECM 論文は remodeling / memory-precision route であり、単純な matrix maintenance ではございません

- [Nguyen et al. (2020)](https://doi.org/10.1016/j.cell.2020.05.050) は、neuronal IL-33 により microglia が ECM を engulf し、その remodeling が synapse plasticity と remote memory precision を支えることを示しました。

批判:

- これは ECM を固定足場としてではなく、microglia-dependent remodeling target として読むべきことを示します。
- よって ECM / PNN 文献には `immune-linked remodeling` という別 route family が存在します。

### 4. Inhibitory-plasticity 論文と CA2/PV memory-support 論文も別 route でございます

- [Jabłońska et al. (2024)](https://doi.org/10.1016/j.matbio.2024.11.001) は、PNN が synapse-specific inhibitory plasticity を調整する route を示しました。
- [Alexander et al. (2025)](https://doi.org/10.1523/JNEUROSCI.1626-24.2024) は、CA2 pyramidal cells と parvalbumin cells の perineuronal nets が hippocampal-dependent memory に differential に効くことを示しました。

批判:

- 前者は inhibitory-plasticity control、後者は cell-type-specific memory-support であり、同じ claim ceiling を持ちません。
- `PNN matters for memory` という一文でまとめると、synapse-specific route と cell-type-specific support route が混線いたします。

### 5. 加齢 rescue と human histology は human in vivo closure を与えません

- [Mehak et al. (2025)](https://doi.org/10.1111/acel.70139) は aged mice における CA2 PNN targeting と recognition-memory rescue を示しました。
- [Lehner et al. (2024)](https://doi.org/10.1002/epi4.12963) は human hippocampus で age-dependent PNN increase と epilepsy-related precocious aging を示しました。
- [Banovac et al. (2025)](https://doi.org/10.1007/s12035-024-04306-1) は human prefrontal cortex の PNN morphology / molecular characteristics を示しました。

批判:

- これらは重要な前進ですが、
  - animal intervention rescue
  - human ex vivo age-linked histology
  - human microcircuit specialization histology
  をそれぞれ強めるだけであり、
  - living-human whole-brain gate-state measurement
  - same-session maintenance closure
  - direct WBE-relevant state observability
  を与えるわけではございません。

## 今回実行した変更

### `mind_uploading_papers.md`

- `last_updated` と note はすでに 2026-04-02 更新済みでしたので、そのまま維持しました。
- `front door` の弱点説明に `ECM / PNN gate state` を追加しました。
- `Shared extracellular / electrical-state` note-box の直後に、`Read ECM / PNN papers through an explicit route-family split` note-box を新設しました。
- technical fast-lane table に `ECM / PNN route-family split` row を追加しました。
- `Read maintenance-state papers as route-changing evidence` note-box に ECM / PNN 文献群と `ECM / PNN gate state` を追加しました。

### `research_harvest_50.md`

- U3 `maintenance-state family split` row に `ECM / PNN gate state` を追加しました。
- `Read same-brain functional connectomics as scaffold, not as a solved local twin` と `Read U8 closed-loop stability as more than fast timing` の間に、`Read U3 ECM / PNN papers as route-family claims, not as one support bucket` note-box を新設しました。

## 今回止めた誤読

- `ECM / PNN = one generic support variable`
- `PNN paper = one common plasticity meter`
- `microglial ECM remodeling = same thing as critical-period reopening`
- `human PNN histology = living-human maintenance-state readout`
- `CA2 / PV memory support result = whole-brain ECM gate closure`

## 検証

- `bundle exec jekyll build`
  - 成功
- `git diff --check`
  - 成功
- `rg -n "ECM / PNN route-family split|Read ECM / PNN papers through an explicit route-family split|Read U3 ECM / PNN papers as route-family claims|ECM / PNN gate state" _site/mind_uploading_papers.html _site/research_harvest_50.html`
  - 追加した公開文面が `_site` に出力されることを確認

## external dependency tasks

- なし
  - 今回の主作業は一次文献確認、repo 内公開文面修正、ローカル build 検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Pizzorusso T, Medini P, Berardi N, Chierzi S, Fawcett JW, Maffei L. Reactivation of ocular dominance plasticity in the adult visual cortex. *Science*. 2002.
   - https://doi.org/10.1126/science.1072699
2. Frischknecht R, Heine M, Perrais D, Seidenbecher CI, Choquet D, Gundelfinger ED. Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. *Nature Neuroscience*. 2009.
   - https://doi.org/10.1038/nn.2338
3. Nguyen PT, Dorman LC, Pan S, et al. Microglial Remodeling of the Extracellular Matrix Promotes Synapse Plasticity. *Cell*. 2020.
   - https://doi.org/10.1016/j.cell.2020.05.050
4. Jabłońska J, Wiera G, Mozrzymas JW. Extracellular matrix integrity regulates GABAergic plasticity in the hippocampus. *Matrix Biology*. 2024.
   - https://doi.org/10.1016/j.matbio.2024.11.001
5. Alexander GM, Nikolova VD, Stöber TM, et al. Perineuronal Nets on CA2 Pyramidal Cells and Parvalbumin-Expressing Cells Differentially Regulate Hippocampal-Dependent Memory. *Journal of Neuroscience*. 2025.
   - https://doi.org/10.1523/JNEUROSCI.1626-24.2024
6. Mehak SF, Bettagere Shivakumar A, Jijimon F, et al. Targeting CA2 Perineuronal Nets Restores Recognition Memory and Theta Oscillations in Aged Mice. *Aging Cell*. 2025.
   - https://doi.org/10.1111/acel.70139
7. Lehner A, Hoffmann L, Rampp S, et al. Age-dependent increase of perineuronal nets in the human hippocampus and precocious aging in epilepsy. *Epilepsia Open*. 2024.
   - https://doi.org/10.1002/epi4.12963
8. Banovac I, Prkačdin MV, Kirchbaum I, Trnski-Levak S, Bobić-Rasonja M, Sedmak G, Petanjek Z, Jovanov-Milosevic N. Morphological and Molecular Characteristics of Perineuronal Nets in the Human Prefrontal Cortex: A Possible Link to Microcircuitry Specialization. *Molecular Neurobiology*. 2025.
   - https://doi.org/10.1007/s12035-024-04306-1
