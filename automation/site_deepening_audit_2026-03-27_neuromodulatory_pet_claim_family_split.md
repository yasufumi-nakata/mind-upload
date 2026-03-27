# Site Deepening Audit (2026-03-27, Neuromodulatory PET Claim-Family Split)

## 対象

- 主対象: `perspective.md`
- 主対象: `tech_roadmap.md`
- 同期対象: `index.md`
- 同期対象: `wbe_101.md`
- 派生同期: `summary_booklet.md`

## web確認対象

- `https://mind-upload.com/perspective.html`
- `https://pubmed.ncbi.nlm.nih.gov/23649882/`
- `https://pubmed.ncbi.nlm.nih.gov/9607763/`
- `https://www.nature.com/articles/s41467-018-08143-4`
- `https://pubmed.ncbi.nlm.nih.gov/31715617/`

## 今回この箇所を選んだ理由

- site 全体の route-card 側では、すでに `occupancy PET` と `displacement / release-sensitive PET` を別 row として扱っていました。
- しかし主要導線である `perspective.md` と `tech_roadmap.md` には、なお `occupancy / displacement PET` を一つの human PET row として圧縮する箇所が残っていました。
- この圧縮は技術・自然科学の観点で弱いです。`外因性の target engagement` と `challenge-linked endogenous release proxy` は、同じ direct observable でも同じ claim family でもないからです。

## 根拠付き批判

### 1. Occupancy PET は「薬剤が選択した target をどれだけ占有したか」を問う route です

- 根拠:
  - [Wong et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23649882/) は healthy male subjects に `10, 20, 40, 60, 80 mg` の lurasidone を与え、`[11C]raclopride` PET で D2 receptor occupancy を評価しました。
  - 同論文では occupancy が `41-43%`, `51-55%`, `63-67%`, `77-84%`, `73-79%` と dose-dependent に報告されており、問うている object は `selected receptor target engagement` です。
- 批判:
  - したがって、occupancy PET は「現在の transmitter release を見る route」ではありません。
  - `occupancy` を `release proxy` と同列にまとめると、薬剤投与下での受容体占有と、行動・challenge に伴う内因性 transmitter fluctuation の差が消えます。

### 2. Displacement / release-sensitive PET は「challenge と時間窓に縛られた endogenous release proxy」です

- 根拠:
  - [Koepp et al. (1998)](https://pubmed.ncbi.nlm.nih.gov/9607763/) は、video game 実行中に striatum で `11C-raclopride` binding が baseline より低下し、performance と相関することを示しました。これは `goal-directed task window` に縛られた dopamine-release proxy です。
  - [Lippert et al. (2019)](https://www.nature.com/articles/s41467-018-08143-4) は、`minute-by-minute` の `11C-raclopride` fluctuation から stimulus-evoked dopamine release を評価する方法を示し、human milkshake task に適用しました。これは occupancy ではなく `time-dependent stimulus-evoked release proxy` です。
  - [Erritzoe et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/31715617/) は `17` healthy male volunteers に `d-amphetamine 0.5 mg/kg` を投与し、`[11C]CIMBI-36` PET で frontal cortex の `BP_ND` 低下を `5-HT release index` として扱いました。
- 批判:
  - したがって displacement / release-sensitive PET は、`named challenge`, `ligand`, `scan window`, `kinetic model` に依存する bounded release proxy です。
  - `occupancy PET` と一括化すると、`administered-drug target engagement` と `challenge-linked endogenous release inference` の measurement-model burden が混ざります。

### 3. Main pages でこの二者を圧縮すると、site 自身の route-card rule と衝突します

- 根拠:
  - `wiki/measurement-stack-and-claim-ceiling.md` と `wiki/homeostatic-plasticity-and-maintenance-state.md` では、すでに occupancy と displacement / release-sensitive PET を別 row で扱っています。
  - 一方で `perspective.md` と `tech_roadmap.md` には、なお `occupancy / displacement PET` を一つの row / rung として置く箇所が残っていました。
- 批判:
  - front door と core long-form pages に圧縮が残ると、詳細 wiki で止めている誤読が main pages で再導入されます。
  - 特に `human PET neuromodulatory route exists` を `current transmitter state is partly measured` と誤読しやすくなります。

### 4. Roadmap 側では rung の数そのものがずれていました

- 問題:
  - `R10` は neuromodulation を `4` rungs として説明していましたが、実際には
    - mixed arousal proxy
    - local transmitter sensor
    - receptor / transporter atlas
    - occupancy PET
    - displacement / release-sensitive PET
    の `5` rungs です。
- 批判:
  - rung 数が少ないままだと、`target engagement` と `endogenous release proxy` が operationally 同じ階段に見えてしまいます。
  - これは roadmap と verification / wiki の reading rule をずらします。

## 今回実行した変更

- `perspective.md`
  - `page_highlights` の human PET bullet を `occupancy PET target-engagement routes` と `challenge-linked displacement / release PET routes` に分離
  - human observability table の `Human occupancy / displacement PET` row を 2 row に分割
  - `Proxy class, operational maturity, and calibrator role are different axes` note に occupancy と release-proxy の差を追記

- `tech_roadmap.md`
  - M1 / M3 の human route table で `occupancy PET` と `displacement / release-sensitive PET` を別 row に分割
  - M3 説明段落の `selected occupancy / displacement routes` を claim-family split に改稿
  - `R10` の operational rule を `4 rungs` から `5 rungs` に更新
  - `R10` 本文に `Wong 2013` と `Erritzoe 2020` を明示的に追加

- `index.md`
  - front-door bullet と explanatory paragraph の `occupancy / displacement PET` を split wording に更新

- `wbe_101.md`
  - human evidence layered bullet を split wording に更新

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` による再生成対象として同期

## 今回の修正で止めた誤読

- `occupancy PET = displacement / release PET`
- `administered-drug target engagement = endogenous transmitter release`
- `one human neuromodulatory PET row exists = current whole-brain transmitter field is partly observed`
- `roadmap の neuromodulation ladder は 4 rung で十分`
