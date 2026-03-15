# Site Deepening Audit (2026-03-15, Perspective / Verification Boundaries)

## 対象

- 主対象: `perspective.md`

## 今回の選定理由

- `perspective.md` はサイト内でもっとも立場表明として参照されやすい長文ページです。
- 2026-03-15 時点で、各論の更新は進んでいましたが、`Decoding → Emulation` 節ではなお `局所 connectomics`、`非侵襲 source imaging`、`sleep 依存の maintenance-state`、`closed-loop intervention`、`thermodynamic readout` が一つの「難しさ」に見えやすい構造が残っていました。
- これは技術・自然科学の観点で改善優先度が高いです。なぜなら、別種類の前進を同列に読むと、`局所 digital twin` を `human whole-brain state-complete` に、`良い decode / localization` を `一意復元` に、`局所 causal gain` を `WBE 検証` に過大評価しやすいからです。

## 主要な批判点

### 1. Observability と identifiability が混ざっていました

- 問題:
  - 旧版は `計測の前進` と `内部状態の一意復元` の境界を、箇条書きでは示していても表として固定していませんでした。
  - そのため、局所 connectomics や source imaging の改善を、そのまま `全脳状態がかなり見えた` と誤読する余地がありました。
- 根拠:
  - Dorkenwald et al. (2024) は成体ショウジョウバエ全脳の wiring diagram を示しました。
  - MICrONS Consortium et al. (2025) は単一マウス 1 mm³ 皮質で same-brain function / connectomics の対応を前進させましたが、human whole-brain ではありません。
  - Michel & Brunet (2019) と Aydin et al. (2019) は、EEG inverse problem がなお head model と導電率仮定に依存することを整理しています。
  - Frässle et al. (2021) は model-family comparison を前進させましたが、一般的一意復元を保証したわけではありません。
- 修正:
  - `observability` と `identifiability` を別行にした表を追加しました。
  - `local digital twin / ESI / whole-brain WBE` を同列に書かない site rule を本文へ明記しました。

### 2. maintenance-state の壁が `connectome は足りない` の一言で圧縮されすぎていました

- 問題:
  - 旧版でも hidden state は触れていましたが、sleep / wake、髄鞘、glial / metabolic support が `cross-day claim を止める独立の壁` としては固定されていませんでした。
  - そのため、same-day の activity match や decode 成績が、overnight maintenance や timing-sensitive stability の証拠に近いように見える余地が残っていました。
- 根拠:
  - Hengen et al. (2016)、Torrado Pacheco et al. (2021)、Xu et al. (2024) は sleep / wake に依存した homeostatic recovery を示しました。
  - Looser et al. (2024) は oligodendrocyte-axon metabolic coupling を示しました。
  - Cahill et al. (2024) と Lee et al. (2022) は glial / active maintenance を強めました。
- 修正:
  - `maintenance-state の壁` を独立行として追加しました。
  - `cross-day claim では maintenance-state の縦断ログが必要` と本文へ明記しました。

### 3. intervention evidence の局所性が弱く、closed-loop 成功を上位主張へ読み替えやすい構造でした

- 問題:
  - 旧版は causal evidence の重要性は強調していましたが、どの介入が `局所 subsystem evidence` で、どこから先が未支持かが表で固定されていませんでした。
- 根拠:
  - Hernandez-Pavon et al. (2023) は TMS-EEG の比較可能性に必要な刺激条件・マスキング・artifact 管理を整理しました。
  - Flesher et al. (2021) は双方向 BCI による局所 causal gain を示しました。
  - Oehrn et al. (2024) は adaptive DBS の臨床 feasibility を前進させましたが、疾患条件つきの local loop です。
- 修正:
  - `intervention の壁` を独立行として追加しました。
  - `受動観測 / held-out perturbation / online loop / 長期適応運用` を段階証拠として分けて読む方針へ改めました。

### 4. thermodynamic readout が補助ログであることは書かれていましたが、他の壁との相対位置が曖昧でした

- 問題:
  - 旧版は thermodynamic caution 自体は正しかったものの、observability / intervention と並べた相対位置が弱く、読者が `物理制約に触れたから一段強い` と感じやすい構造でした。
- 根拠:
  - Lynn et al. (2021) と de la Fuente et al. (2022) が示したのは coarse-grained neural dynamics の irreversibility シグネチャです。
  - Ishihara & Shimazaki (2025) は spiking から arrow of time を安定に推定する難しさを残しています。
- 修正:
  - `thermodynamic readout の壁` を表へ明示し、補助ログである位置づけを他の壁と並べて固定しました。

## 今回実行した変更

- `perspective.md`
  - `last_updated` を 2026-03-15 に更新
  - `page_highlights` / `known_points` / `wiki_links` を、verification boundary を読みやすい方向へ更新
  - `Decoding → Emulation` 節に `5つの壁` の表を追加
  - `この節で禁止する読み替え` を note-box で追加
  - `最低限の証拠鎖` に `cross-day を含む maintenance-state ログ` を追加
  - `Limitations` の工学的限界を `observability / identifiability / maintenance-state / intervention scope` の4本柱へ再編

## 外部依存で保留

- cross-day maintenance-state benchmark の公開データ整備
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: sleep state、recovery、myelin / glial proxy、intervention log を同一個体で追える公開データ
  - 完了条件: same-day fit、cross-day stability、online perturbation を同一 schema で比較できること

## 参考文献

- Dorkenwald S, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Michel CM, Brunet D. EEG source imaging: a practical review of the methodology. *Front Neurol*. 2019.
  - https://doi.org/10.3389/fneur.2019.00325
- Aydin U, Vorwerk J, Küpper P, et al. Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. *Front Neurosci*. 2019.
  - https://doi.org/10.3389/fnins.2019.00531
- Frässle S, et al. Regression DCMs for fMRI. *NeuroImage*. 2021.
  - https://doi.org/10.1016/j.neuroimage.2020.117566
- Hengen KB, et al. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Torrado Pacheco A, et al. Sleep Promotes Downward Firing Rate Homeostasis. *Neuron*. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nat Commun*. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nat Neurosci*. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *PNAS*. 2022.
  - https://doi.org/10.1073/pnas.2211572119
- Hernandez-Pavon JC, et al. TMS combined with EEG: Recommendations and open issues. *Brain Stimul*. 2023.
  - https://doi.org/10.1016/j.brs.2023.02.009
- Flesher SN, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. *Science*. 2021.
  - https://doi.org/10.1126/science.abd0380
- Oehrn CR, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson’s disease: a blinded randomized feasibility trial. *Nat Med*. 2024.
  - https://doi.org/10.1038/s41591-024-03196-z
- Lynn CW, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021.
  - https://doi.org/10.1073/pnas.2109889118
- de la Fuente LA, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. *Cereb Cortex*. 2022.
  - https://doi.org/10.1093/cercor/bhac177
- Ishihara K, Shimazaki H. Entropy flow reveals the arrow of time from neuronal spiking activity. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-66669-w
