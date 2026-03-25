# Site Deepening Audit (2026-03-26, claims/evidence human-proxy beginner sync)

## 対象

- 主対象: `wiki/claims-and-evidence.md`
- 同期対象: `wiki/literature-and-evidence-reading.md`
- エクスポート同期: `github-wiki-export/claims-and-evidence.md`, `github-wiki-export/literature-and-evidence-reading.md`
- web確認対象:
  - `https://mind-upload.com/wiki/claims-and-evidence.html`
  - `https://mind-upload.com/wiki/literature-and-evidence-reading.html`
  - `https://www.nature.com/articles/s41467-023-44363-z`
  - `https://www.nature.com/articles/s41467-025-64414-x`
  - `https://www.nature.com/articles/s41593-025-01945-y`
  - `https://www.nature.com/articles/s41593-025-02132-9`
  - `https://www.nature.com/articles/s41467-026-68374-8`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- 2026-03-26 JST 時点で、`index.md`、`wbe_101.md`、`verification.md`、`wiki/human-proxy-composition.md` ではすでに
  - `proxy-rich human evidence`
  - `same-subject / same-session multimodal`
  - `common-driver audit`
  - `proxy class / operational maturity / calibrator role`
  を明示的に分ける site-wide rule が前景化されていました。
- しかし `wiki/claims-and-evidence.md` は beginner の claim-reading page であるにもかかわらず、入口で止める overread が主に
  - decode
  - tractography
  - DCM / effective connectivity
  - thermodynamics
  - closed loop
  に偏っており、`living-human whole-brain state measurement` 系 headline を正面から止めていませんでした。
- さらに `wiki/literature-and-evidence-reading.md` も、`human measurement paper` を `observability-class advance` として読む注意はありましたが、`same-subject / multimodal / proxy-rich` を `same-state evidence` に読み替えないための次ページ導線が弱い状態でした。

## 根拠付き批判

### 1. beginner page が現在の site-wide 最大の過読の一つを止め切れていませんでした

- `wiki/claims-and-evidence.md` は decode / graph / irreversibility / closed loop の overread には強くなっていました。
- しかし現在の site で同じくらい危険な overread は、`proxy-rich human multimodal evidence = whole-brain state closure` です。
- 一次文献はこの短絡を支持していません。
  - [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024) は 33 人 healthy participants の SV2A atlas です。
  - [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は 51 名 adolescent cohort を主とする five-metabolite parcel-similarity graph です。
  - [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は 7 T dynamic DMRSI による five-participant kinetic route です。
  - [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) は specialized 7 T CSF-mobility route です。
  - [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は 39 participants randomized crossover trial を multicompartment model で読む route です。
- これらは quantity type, spatial unit, time window, cohort regime, model burden が違います。したがって beginner page でも `same-subject` や `whole-brain` という言い回しを、そのまま state-closure に読ませない停止線が必要でした。

### 2. simultaneous multimodal 自体が one latent state の self-validation にはなりません

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は simultaneous multimodal recordings に common と divergent の両方が残ることを示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で coupled global progression と two distinct network patterns の共存を示しました。
- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は major global fMRI mode が autonomic physiology に substantial coupling を持つことを示しました。
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は significant ΔBOLD voxels の約 40% で oxygen metabolism changes が opposing になりうることを示しました。

批判:

- したがって `same-session multimodal` や `shared factor` という言い方だけでは target neural variable への specificity は確保されません。
- beginner page に `common-driver audit` と `shared-vs-specific decomposition` を明示しないままでは、site 本文で止めている overread を入口で再導入してしまいます。

### 3. literature reading guide に人間計測 paper の次ルートが不足していました

- `wiki/literature-and-evidence-reading.md` は `new human measurement paper` を見たときに `observability-class advance` として止まる規律は持っていました。
- しかし 2026-03 site-wide rule では、そこからさらに
  - `proxy class`
  - `calibrator role`
  - `common-driver audit`
  - `same-state ではなく proxy composition かどうか`
  を読む必要があります。

批判:

- ここが弱いままだと、paper collection から入った読者は `same-subject`, `multimodal`, `whole-brain`, `in humans` という語を見ただけで state-identification 側へ過読しやすくなります。
- したがって reading guide 側でも `human-proxy-composition` への直接導線が必要でした。

## 今回実行した変更

- `wiki/claims-and-evidence.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - front matter の `page_highlights` / `known_points` に `proxy-rich human multimodal evidence` の停止線を追加しました。
  - 冒頭 note を `2026-03-26` 版に更新し、`Human Proxy Composition Card` と `Fusion Card` を beginner entrance に昇格させました。
  - headline translation table に `Measured the whole-brain state in living humans` 行を追加しました。
  - `Why the beginner rules had to become stricter` に human-proxy / multimodal overread の節を追加しました。
  - checklist を `Six questions` から `Seven questions` に更新し、human / multimodal bundle の direct-observable と common-driver 問いを追加しました。
  - next-step table と sidebar に `human-proxy-composition` への導線を追加しました。
  - 参考文献に Johansen 2024, Vafaii 2024, Lucchetti 2025, Li 2025, Hirschler 2025, Chen 2025, Bolt 2025, Epp 2025, Dagum 2026 を追加しました。

- `wiki/literature-and-evidence-reading.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - `page_highlights` / `known_points` に `same-subject / multimodal human paper` の overread 停止線を追加しました。
  - `When the paper sounds like living-human whole-brain state measurement` note を追加し、`human-proxy-composition` と `measurement-stack-and-claim-ceiling` への導線を新設しました。
  - misreading rules に `Do not collapse proxy-rich into state-closed` を追加しました。
  - next-step section に human-proxy page への戻り先を追記しました。

- `github-wiki-export/claims-and-evidence.md`
  - 上記 beginner-rule 改稿を同期しました。

- `github-wiki-export/literature-and-evidence-reading.md`
  - 上記 reading-guide 改稿を同期しました。

## 今回止めた誤読

- `same-subject multimodal = same-state evidence`
- `proxy-rich human evidence = almost whole-brain state closure`
- `shared factor = target neural variable`
- `living-human whole-brain measurement = one common inferential object`
- `observability-class advance = state-identification evidence`

## 外部依存タスク

- なし。今回の改稿・同期・検証・push はこのセッションで repo 内完結可能です。

## 参考文献

1. Johansen A, Bzdok D, Veronese M, et al. A healthy human brain atlas of synaptic density. *J Neurosci*. 2024. https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nat Commun*. 2024. https://doi.org/10.1038/s41467-023-44363-z
3. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-66124-w
4. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
5. Hirschler L, Brisset J-C, Baledent O, et al. Human CSF mobility MRI maps sleep-state-dependent support dynamics. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-02073-3
6. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-64414-x
7. Bolt T, Wang S, Nomi JS, et al. Autonomic physiological coupling of the global fMRI signal. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-01945-y
8. Epp SM, Castrillon G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-02132-9
9. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nat Commun*. 2026. https://doi.org/10.1038/s41467-026-68374-8
