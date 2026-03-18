# Site Deepening Audit (2026-03-18, Neuromodulatory Observability Boundary)

## 対象

- 主対象: `index.md`
- 主対象: `wbe_101.md`
- 主対象: `verification.md`
- 主対象: `tech_roadmap.md`
- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`

## 今回の選定理由

- 2026-03-18 時点で、このサイトは `neuromodulation` を重要な潜在状態としては扱えていました。
- しかし公開導線では、次の非同値な route がまだ十分に分離されていませんでした。
  - `mixed arousal proxy (pupil / HRV / locomotion)`
  - `local axon activity / transmitter sensor`
  - `receptor / transporter atlas / autoradiography`
  - `occupancy / displacement PET`
- この粗さは技術・自然科学の観点で重大でございます。なぜなら、これらはすべて「neuromodulation に関係する route」ではありますが、直接増える情報、残る潜在変数、許される claim ceiling がそれぞれ違うからです。

## 主要な批判点

### 1. 入口ページの human evidence ladder が neuromodulatory route を実質的に欠いていました

- 問題:
  - `index.md` と `wbe_101.md` の human evidence ladder は、`local ultrastructure -> synaptic-density PET -> macro support-state proxies` の骨格はよく整理されていました。
  - しかし human-side の neuromodulatory route である `receptor / transporter atlas` と `occupancy / displacement PET` が front door で見えず、読者は `human evidence exists` を一段強く読みすぎる余地がありました。
- 根拠:
  - Hansen et al. (2022) は 1,200 人超の PET data から 19 receptor / transporter の normative atlas を構築し、receptor profile が structure/function/cognition と対応することを示しました。
  - Goulas et al. (2021) は human cortex の receptor density に sensory-to-association axis と laminar organization の自然軸があることを示しました。
  - これらは `current transmitter state` ではなく、まず `regional chemoarchitectural prior` を与える route と読むのが妥当でございます。
- 修正:
  - `index.md` と `wbe_101.md` に receptor / transporter atlas prior と occupancy / displacement PET の行を追加しました。

### 2. 旧 latent-state error budget は neuromodulatory row が粗すぎました

- 問題:
  - `verification.md` の neuromodulatory row は、旧版では `what proxy family was used` 程度で止まっていました。
  - これでは mixed proxy と local sensor と PET が同じ監査欄に入ってしまい、必要 disclosure の差が消えていました。
- 根拠:
  - Reimer et al. (2016) は pupil fluctuation が adrenergic と cholinergic の双方を追うことを示しました。
  - Neyhart et al. (2024) は cortical ACh signal が local axon activity と clearance kinetics に依存することを示しました。
  - Koepp et al. (1998) と Lippert et al. (2019) は raclopride PET が challenge- and window-limited な dopamine release proxy であることを示しました。
- 批判:
  - したがって `neuromodulation` を一欄で監査する場合でも、最低限 `route label / receptor family / ligand / challenge / temporal window / spatial scope / abstention boundary` が必要でございます。
- 修正:
  - `verification.md` の latent-state row と augmentation row を改稿し、route-specific disclosure へ更新しました。

### 3. Roadmap R10 がまだ「気分スカラー」批判で止まっていました

- 問題:
  - `tech_roadmap.md` の R10 は「pupil / HRV は粗い」という批判までは入っていましたが、どの route がどこまで言えるかという ladder を明文化していませんでした。
- 根拠:
  - Hansen et al. (2022), Goulas et al. (2021) は receptor map が regional prior であることを支持します。
  - Koepp et al. (1998), Lippert et al. (2019) は PET displacement が task- and time-window-limited proxy であることを支持します。
- 修正:
  - R10 を `mixed proxy -> local sensor -> receptor atlas -> occupancy/displacement PET` の ladder として改稿しました。

### 4. Measurement-stack wiki が最も重要な分離をまだ table 上で固定できていませんでした

- 問題:
  - `wiki/measurement-stack-and-claim-ceiling.md` は旧版で `local transmitter imaging / behavior-linked proxy` を 1 行に束ねていました。
  - これでは `pupil` と `local ACh sensor` と `receptor atlas` と `PET displacement` の claim ceiling が同列に見えてしまいます。
- 根拠:
  - Reimer et al. (2016): mixed proxy
  - Lohani et al. (2022), Neyhart et al. (2024): local transmitter heterogeneity and local clearance
  - Hansen et al. (2022), Goulas et al. (2021): receptor atlas / autoradiography as structured prior
  - Koepp et al. (1998), Lippert et al. (2019): challenge-limited release proxy
- 修正:
  - measurement-stack table を 4 行へ分解し、`neuromodulatory-proxy-ladder` セクションを新設しました。
  - あわせて EEG / MEG row の HTML 崩れも修正しました。

### 5. 既存 audit artifact に書誌誤りがありました

- 問題:
  - `automation/site_deepening_audit_2026-03-16_neuromodulatory_pet_routes.md` では Koepp et al. (1998) の DOI が `10.1038/28364` になっていました。
- 根拠:
  - PubMed / Nature の正しい DOI は `10.1038/30498` です。
- 修正:
  - 当該 audit artifact の DOI を訂正しました。

## 今回実行した変更

- `index.md`
  - human route の説明に receptor / transporter atlas と occupancy / displacement PET を追加
  - neuromodulation の読み違いを防ぐ front-door note を追加
- `wbe_101.md`
  - human observability ladder に `receptor / transporter atlas prior` と `occupancy / release-sensitive PET` を追加
  - neuromodulation を 1 行に圧縮しない rule を追加
  - 参考文献を追加
- `faq.md`
  - human evidence ladder の説明に neuromodulatory route を追加
- `verification.md`
  - latent-state error budget の neuromodulatory row を route-specific disclosure へ改稿
  - augmentation row も同じロジックへ同期
  - neuromodulation ladder の explanatory note を追加
- `tech_roadmap.md`
  - R10 を ladder-based policy に改稿
  - section 名称を `neuromodulation` へ修正
  - 参考文献を追加
- `wiki/measurement-stack-and-claim-ceiling.md`
  - neuromodulatory route を 4 行に分割
  - `neuromodulatory-proxy-ladder` セクションを追加
  - claim ceiling / stop-rule を改稿
  - 参考文献を追加
- `automation/site_deepening_audit_2026-03-16_neuromodulatory_pet_routes.md`
  - Koepp DOI を訂正

## 外部依存で保留

- なし
  - 今回の作業は、一次文献確認とこのリポジトリ内の本文更新で完結しています。

## 参考文献

1. Reimer J, McGinley MJ, Liu Y, et al. Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. *Nature Communications*. 2016.
   - https://doi.org/10.1038/ncomms13289
2. Lohani S, Moberly AH, Benisty H, et al. Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01202-6
3. Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. *Cell Reports*. 2024.
   - https://doi.org/10.1016/j.celrep.2024.114808
4. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01186-3
5. Goulas A, Changeux J-P, Wagstyl K, Amunts K, Palomero-Gallagher N, Hilgetag CC. The natural axis of transmitter receptor distribution in the human cerebral cortex. *PNAS*. 2021.
   - https://doi.org/10.1073/pnas.2020574118
6. Wong DF, Kuwabara H, Hsu DJ, et al. D2 receptor occupancy in the brains of healthy subjects by the novel atypical antipsychotic lurasidone. *Journal of Clinical Psychiatry*. 2013.
   - https://doi.org/10.4088/JCP.12m08042
7. Koepp MJ, Gunn RN, Lawrence AD, et al. Evidence for striatal dopamine release during a video game. *Nature*. 1998.
   - https://doi.org/10.1038/30498
8. Lippert RN, Bolding KA, Abbott LF, et al. Time-dependent assessment of stimulus-evoked regional dopamine release. *Nature Communications*. 2019.
   - https://doi.org/10.1038/s41467-019-09897-z
