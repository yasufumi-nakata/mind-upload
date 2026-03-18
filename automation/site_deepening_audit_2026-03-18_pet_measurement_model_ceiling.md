# Site Deepening Audit (2026-03-18, PET Measurement-Model Ceiling)

## 対象

- 主対象: `wbe_101.md`
- 副対象: `faq.md`
- 副対象: `verification.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`

## 今回の選定理由

- 2026-03-18 時点で、公開サイトは `human evidence is layered`、`receptor atlas != occupancy PET != release-sensitive PET`、`connectome-complete != emulation-complete` をかなり明確に区別できていました。
- その一方で、PET 系の human evidence については、`どのクラスの proxy なのか` は書けていても、`その proxy をどう定量したか` という測定モデル条件が公開導線でまだ十分に前面化されていませんでした。
- これは技術・自然科学の観点で重要でございます。なぜなら、PET 系の claim ceiling は modality 名だけでは決まらず、少なくとも
  - tracer / radioligand
  - arterial input か reference-region か
  - kinetic model か simplified window か
  - challenge / scan window
  - partial-volume handling の要否
  に依存するからです。

## 根拠付き批判

### 1. 旧 `WBE 101` は human observability ladder を持っていましたが、PET 行の測定モデル条件をまだ十分に固定していませんでした

- 問題:
  - `wbe_101.md` は human observability ladder で `SV2A PET`、`receptor / transporter atlas`、`occupancy / release-sensitive PET` を分けていました。
  - しかし、それぞれが `measurement label` ではなく `measurement model` を伴う proxy であることが、入口ではまだ弱うございました。
- 根拠:
  - Naganawa et al. (2021) は human SV2A PET で metabolite-corrected arterial input、1TC/2TC、SUVR-1 window を比較し、定量値が model / window に依存することを示しました。
  - Smart et al. (2021) は [11C]UCB-J で brief visual activation 中に `K1` は上がっても `VT` と `BPND` は変わらないことを示し、SV2A PET が momentary synaptic efficacy の readout ではないことを直接示しました。
  - Hansen et al. (2022) は 1,200 人超の健常者 PET を collate して normative receptor atlas を作成しており、これは current individual state ではなく group-average chemoarchitectural prior です。
  - Wong et al. (2013), Koepp et al. (1998), Lippert et al. (2019) は occupancy / displacement PET が receptor-family・challenge・time-window に制限された問いに答える route であることを示しました。
- 批判:
  - したがって、旧文面のままでは `PET で見えた` が `current state を PET で測った` へ過大変換されうる構造でした。

### 2. 旧 `Verification` は neuromodulatory ladder を持っていましたが、submission-side disclosure として PET measurement model が不足していました

- 問題:
  - `verification.md` の latent-state error budget では、neuromodulatory specificity に `ligand / challenge / temporal window` はありました。
  - しかし `arterial-versus-reference quantification route`、`kinetic or simplified model`、`partial-volume handling` が明示要件に入っていませんでした。
- 批判:
  - これは submission rule として弱うございました。
  - 同じ `occupancy PET` でも、どの tracer を使い、どの model で binding を推定し、どの時間窓を採用したかが書かれなければ、claim ceiling を読み分けられません。

### 3. 旧 `measurement-stack` wiki は human PET class を完全には揃えていませんでした

- 問題:
  - `wiki/measurement-stack-and-claim-ceiling.md` は `receptor / transporter atlas` と `occupancy / release-sensitive PET` を持っていましたが、`SV2A PET / synaptic-density PET` 行がありませんでした。
- 根拠:
  - Johansen et al. (2024) は human in vivo の high-resolution synaptic-density atlas を提示しており、これは `regional synaptic-density proxy` として独立クラスです。
  - しかも Smart et al. (2021) により、同クラスが momentary activation readout ではないことも直接示されています。
- 批判:
  - stack page にこの行が無いままだと、front-door の human ladder と stack-level claim ceiling の対応が 1 段欠けます。

### 4. 書誌追跡性にも修正が必要でした

- 問題:
  - lurasidone occupancy PET の DOI / title に不整合がありました。
  - Lippert et al. (2019) の release-sensitive PET 論文でも DOI / 著者列 / article number に不整合がありました。
- 根拠:
  - PubMed 上の一次情報では、Wong et al. (2013) の該当 PET occupancy 論文は `10.1007/s00213-013-3103-z` です。
  - Nature Communications の原著ページでは、Lippert 論文は `Nat Commun 10, 336 (2019)`、DOI は `10.1038/s41467-018-08143-4` です。
- 批判:
  - この種の DOI 不整合は、claim ceiling 議論以前に証跡の追跡性を下げます。
  - 今回の run では public-facing files 側を一次情報に合わせて訂正しました。

## 今回実行した変更

- `wbe_101.md`
  - `regional synaptic-density PET` 行に `kinetic modeling / validated simplified window` を追加
  - `receptor atlas` 行に `averaged across healthy cohorts` を追加
  - `occupancy / release-sensitive PET` 行に `explicit tracer and quantification model` を追加
  - 新規 note `PET rows need a measurement model` を追加
  - 参考文献へ Naganawa (2021) と Smart (2021) を追加
  - Wong (2013) の DOI / title を一次情報に合わせて訂正
  - Lippert (2019) の DOI / 著者列を一次情報に合わせて訂正
- `faq.md`
  - Q2c に `PET rows でも measurement model が必要` という短答を追加
- `verification.md`
  - `Neuromodulatory specificity` の minimum disclosure に `tracer / ligand`、`occupancy-versus-displacement design`、`arterial-versus-reference quantification route`、`kinetic or simplified model`、`partial-volume handling` を追加
  - `Human evidence class / observability ceiling` に PET route の定量モデル開示要件を追加
  - 新規 note `PET-based evidence is unreadable without the measurement model` を追加
  - 参考文献へ Naganawa (2021), Smart (2021), Wong (2013) を追加
  - Lippert (2019) の DOI / 著者列を一次情報に合わせて訂正
- `tech_roadmap.md`
  - R10 の本文参照 DOI を一次情報に合わせて訂正
  - 参考文献の Lippert (2019) を一次情報に合わせて訂正
- `wiki/measurement-stack-and-claim-ceiling.md`
  - front matter に `synaptic-density PET` を追加
  - measurement-stack table に `SV2A PET / synaptic-density PET` 行を新設
  - `receptor atlas` 行と `occupancy / release-sensitive PET` 行に measurement-model 条件を追記
  - 新規 note `PET routes still need tracer and quantification disclosure` を追加
  - 参考文献へ Naganawa (2021), Smart (2021), Johansen (2024), Wong (2013) を追加
  - Lippert (2019) の DOI / 著者列 / article number を一次情報に合わせて訂正

## 外部依存で保留

- なし
  - 今回の修正は、このリポジトリ内の公開本文・wiki・引用整合性修正で完結しております。

## 参考文献

1. Naganawa M, Li S, Nabulsi N, et al. First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. *Journal of Nuclear Medicine*. 2021.
   - https://doi.org/10.2967/jnumed.120.249144
2. Smart K, Liu H, Matuskey D, et al. Binding of the synaptic vesicle radiotracer [11C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
3. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
4. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01186-3
5. Wong DF, Kuwabara H, Hsu DJ, et al. Determination of dopamine D2 receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. *Psychopharmacology*. 2013.
   - https://doi.org/10.1007/s00213-013-3103-z
6. Koepp MJ, Gunn RN, Lawrence AD, et al. Evidence for striatal dopamine release during a video game. *Nature*. 1998.
   - https://doi.org/10.1038/30498
7. Lippert RN, Cremer AL, Thanarajah SE, et al. Time-dependent assessment of stimulus-evoked regional dopamine release. *Nature Communications*. 2019.
   - https://doi.org/10.1038/s41467-018-08143-4
