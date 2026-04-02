# Site Deepening Audit (2026-04-03, human-proxy neuromodulatory composition split)

## 対象

- 主対象: `wiki/human-proxy-composition.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## web確認対象

- `https://www.nature.com/articles/s41467-025-57289-5`
- `https://www.nature.com/articles/s41593-022-01186-3`
- `https://pubmed.ncbi.nlm.nih.gov/40738968/`
- `https://pubmed.ncbi.nlm.nih.gov/23649882/`
- `https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1651016/full`
- `https://pubmed.ncbi.nlm.nih.gov/9607763/`
- `https://pubmed.ncbi.nlm.nih.gov/31715617/`
- `https://www.sciencedaily.com/releases/2025/03/250328112547.htm`

## 今回この箇所を選んだ理由

- 2026-04-03 時点で、front door 側や literature front door 側では、neuromodulatory evidence を
  - mixed arousal proxy
  - receptor / transporter atlas prior
  - occupancy PET
  - challenge-linked displacement / release-sensitive PET
  に分ける規則がすでにかなり見えるようになっておりました。
- しかし `wiki/human-proxy-composition.md` には、その split が bundle-composition rule としては十分に埋め込まれておりませんでした。
- この page は「複数の human proxy row をどう束ねてよいか」を決める中心ページでございます。ここで neuromodulatory family split が欠けると、読者は
  - `arousal proxy がある`
  - `receptor atlas がある`
  - `occupancy PET がある`
  - `release-sensitive PET がある`
  - `したがって human neuromodulatory state はかなり直接に測れている`
  と誤読しやすくなります。

## 主要結論

- `human neuromodulatory evidence` は一つの reusable row ではございません。
- [Carro-Domínguez et al. (2025)](https://doi.org/10.1038/s41467-025-57289-5) は human sleep における `mixed arousal proxy` であり、transmitter-specific readout ではございません。
- [Hansen et al. (2022)](https://doi.org/10.1038/s41593-022-01186-3) と [Nakuci & Bansal (2025)](https://doi.org/10.1038/s42003-025-08492-z) は `receptor / transporter atlas prior` とその modeling scaffold を示しておりますが、same-subject current-state readout ではございません。
- [Wong et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23649882/) と [Schlosser et al. (2025)](https://doi.org/10.3389/fnins.2025.1651016) は `occupancy / non-occupancy under administered drug` を問う route であり、endogenous release route ではございません。
- [Koepp et al. (1998)](https://pubmed.ncbi.nlm.nih.gov/9607763/), [Erritzoe et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/31715617/), [Miederer et al. (2025)](https://doi.org/10.2967/jnumed.124.268317) は `challenge-linked release proxy` であり、baseline current whole-brain neuromodulatory field を与えるわけではございません。

## 根拠付き批判

### 1. Mixed arousal proxy を transmitter-specific row に読み替えてはいけません

- [Carro-Domínguez et al. (2025)](https://doi.org/10.1038/s41467-025-57289-5) は、human sleep 中の pupil size を arousal proxy として用い、sleep spindle cluster や auditory stimulation response との関係を示しました。
- 同論文自体が、pupil size は arousal-level-regulating systems の activity を indirect に index する proxy であり、parasympathetic cholinergic activity や orexin 系など複数要因の影響可能性を認めております。

批判:

- したがって `pupil-based human arousal evidence` は coarse mixed proxy であり、`specific transmitter field` や `receptor occupancy` や `release dynamics` と同列ではございません。
- composition page でこれを別 row に固定しないと、bundle 側で neuromodulation が過大評価されます。

### 2. Receptor / transporter atlas prior は current state ではなく normative prior でございます

- [Hansen et al. (2022)](https://doi.org/10.1038/s41593-022-01186-3) は、`19` receptor / transporter map を `1,200+` healthy individuals から集約した cortical atlas を構築しました。
- [Nakuci & Bansal (2025)](https://doi.org/10.1038/s42003-025-08492-z) は、そのような density map を neuroreceptor-based modeling framework の入力として使い、spontaneous BOLD activity を reconstruct しました。

批判:

- これは重要な進展ですが、意味するのは `regional chemoarchitectural prior` と `modeling scaffold` であって、`this subject's current neuromodulatory state` ではございません。
- composition page にこの row が無いままですと、atlas prior が occupancy や release proxy と同じ bundle role を持つように読めてしまいます。

### 3. Occupancy PET は target engagement を問う route であり endogenous release ではございません

- [Wong et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23649882/) は lurasidone 投与下の D2 receptor occupancy を healthy male subjects で測定した PET study でございます。
- [Schlosser et al. (2025)](https://doi.org/10.3389/fnins.2025.1651016) は ketamine 0.8 mg/kg 投与後の SERT occupancy を [11C]DASB PET で調べ、`did not significantly differ from zero` という informative null を報告しました。

批判:

- occupancy PET の direct question は `selected administered compound engages selected target or not` でございます。
- これは `endogenous transmitter release changed during a task/challenge` という question とは別であり、同じ neuromodulatory row に圧縮してはいけません。

### 4. Release-sensitive PET は challenge と時間窓に縛られた bounded proxy でございます

- [Koepp et al. (1998)](https://pubmed.ncbi.nlm.nih.gov/9607763/) は video game task 中の striatal dopamine release proxy を raclopride displacement として示しました。
- [Erritzoe et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/31715617/) は d-amphetamine challenge 下で [11C]CIMBI-36 を用い、serotonin release proxy を評価しました。
- [Miederer et al. (2025)](https://doi.org/10.2967/jnumed.124.268317) は [18F]fallypride PET の block design で、task switching 中の ventromedial prefrontal cortex dopamine release proxy を示しました。

批判:

- これらは `named task/challenge`, `named ligand`, `named time window`, `named kinetic interpretation` に依存する bounded route でございます。
- したがって composition page では occupancy PET と別 row にしなければなりませんし、atlas prior や arousal proxy とも bundle role が異なります。

### 5. Composition page でこの split を欠くこと自体が site 全体の規則違反に近いです

- `wiki/human-proxy-composition.md` は、proxy bundle を promotion する前の central rule page でございます。
- site の他の front-door pages や literature-organizing pages が neuromodulatory split を学習していても、この central page がそれを table row と correction note に落としていなければ、読者は composition layer で再び圧縮読みに戻ります。

批判:

- これは単なる書きぶりの問題ではございません。
- `bundle role`, `evidence class`, `time window`, `direct observable` を混線させる taxonomy drift であり、科学的 ceiling を不当に上げてしまいます。

## 今回実行した変更

- `wiki/human-proxy-composition.md`
  - front matter の `description`, `note`, `page_highlights` を更新し、neuromodulatory family split を composition page の front door でも明示しました。
  - `What this page fixes` を更新し、mixed arousal proxy / receptor-transporter atlas prior / occupancy PET / release-sensitive PET の再圧縮を明示的に禁止しました。
  - 新しい correction note を追加しました。
    - `2026-04-03 correction: neuromodulatory family split also belongs inside composition`
  - main route table に以下の 4 row を追加しました。
    - `Human pupil-size arousal proxy in sleep`
    - `Human receptor / transporter atlas prior`
    - `Human occupancy PET`
    - `Human challenge-linked displacement / release-sensitive PET`
  - `What must be fixed before a proxy bundle is promoted` の `Proxy class of each row` 説明文にも neuromodulatory rows を追加し、proxy-class disclosure に含めました。
  - references に今回追加した primary literature を追記しました。

## 今回止めた誤読

- `human neuromodulatory evidence exists` だから current neuromodulatory state はかなり見えている
- `pupil / arousal proxy = receptor atlas prior = occupancy PET = release-sensitive PET`
- `occupancy PET = endogenous transmitter release`
- `atlas prior を個人 current state の近似として bundle に混ぜてよい`
- `challenge-linked release proxy を baseline whole-brain neuromodulatory field として読んでよい`

## 検証

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "neuromodulatory family split|Human occupancy PET|challenge-linked displacement / release-sensitive PET|receptor / transporter atlas prior|pupil-size arousal proxy" wiki/human-proxy-composition.md`
- `rg -n "Human occupancy PET|challenge-linked displacement / release-sensitive PET|receptor / transporter atlas prior|pupil-size arousal proxy" _site/wiki/human-proxy-composition.html`

## 外部依存タスク

- なし
  - 今回の変更は、一次文献の web 確認、repo 内の改稿、ローカル build 検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Carro-Domínguez M, Huwiler S, Oberlin S, et al. Pupil size reveals arousal level fluctuations in human sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57289-5
2. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022. https://doi.org/10.1038/s41593-022-01186-3
3. Nakuci J, Bansal K. The neuroreceptors and transporters underlying spontaneous brain activity. *Communications Biology*. 2025. https://doi.org/10.1038/s42003-025-08492-z
4. Wong DF, Kuwabara H, Brašić JR, et al. Determination of dopamine D2 receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. *Psychopharmacology (Berl)*. 2013. https://doi.org/10.1007/s00213-013-3103-z
5. Schlosser G, Murgaš M, Godbersen GM, et al. Human in vivo assessment of ketamine binding of the serotonin transporter-follow up at a higher dose. *Frontiers in Neuroscience*. 2025. https://doi.org/10.3389/fnins.2025.1651016
6. Koepp MJ, Gunn RN, Lawrence AD, et al. Evidence for striatal dopamine release during a video game. *Nature*. 1998. https://doi.org/10.1038/30498
7. Erritzoe D, Ashok AH, Searle GE, et al. Serotonin release measured in the human brain: a PET study with [11C]CIMBI-36 and d-amphetamine challenge. *Neuropsychopharmacology*. 2020. https://doi.org/10.1038/s41386-019-0567-5
8. Miederer I, Buchholz H-G, Rademacher L, et al. Dopaminergic Mechanisms of Cognitive Flexibility: An [18F]Fallypride PET Study. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268317
