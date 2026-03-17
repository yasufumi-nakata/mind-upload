# Site Deepening Audit (2026-03-17, Vascular State / CVR Gate for Hemodynamic Modalities)

## 対象

- 主対象: `wiki/multimodal-integration-basics.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`
- 副対象: `index.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`multimodal ≠ mechanistic truth`、`BOLD ≠ direct neural truth`、`shared clock ≠ sufficient validation` をかなり強く整理できていました。
- その一方で、hemodynamic modality の本文と提出物仕様ではなお、`HRF / task haemodynamics / venous bias` は監査対象として見えていても、`baseline vascular state / cerebrovascular reactivity (CVR)` が独立の measurement-side latent variable としては十分に前面化されていませんでした。
- この弱点は技術・自然科学の観点で優先度が高いです。なぜなら、現在の一次文献が比較的一貫して示しているのは、hemodynamic signal の解釈 ceiling が `神経側の hidden state` だけではなく、`vascular transfer state` にも支配されるという点だからです。ここが抜けると、group 差、縦断差、薬理差、疲労差を raw BOLD / raw fNIRS amplitude のまま neural difference と読み替えやすくなります。

## 根拠付き批判

### 1. 旧サイトは `BOLD は proxy` と書けていましたが、`vascular state / CVR` を独立の誤差源として提出物化していませんでした

- 問題:
  - hemodynamic gate は HRF heterogeneity、task-related haemodynamics、venous bias、BOLD-CMRO2 discordance をかなり丁寧に扱っていました。
  - しかし、baseline CBF / CBV や cerebrovascular reactivity が task BOLD magnitude そのものを動かすことを、Fusion Card や公開ルールの必須欄に固定していませんでした。
- 根拠:
  - Murphy et al. (2011) は、local CBF / CBV の個体差が BOLD reactivity を動かし、breath-hold 由来の CVR covariate を入れると group analysis の感度が上がることを示しました。
  - Williams et al. (2023) は、task-induced BOLD magnitude が cortex の複数領域で hypercapnia-based CVR によって強く予測され、CVR correction が感度を上げることを示しました。
- 批判:
  - したがって、`proxy` という一般論だけでは足りません。hemodynamic modality では `neural state` と `vascular transfer state` を分けて監査する必要があります。

### 2. 旧 Fusion Card は hemodynamic modality の比較条件を固定していましたが、group / longitudinal comparison を止める gate がまだ弱かった

- 問題:
  - 旧 Fusion Card では target neural claim、HRF、physiology nuisance、venous / depth diagnostic、mechanistic validator を要求していました。
  - しかし、group 差・加齢差・縦断差・薬理差を読むときに、`vascular-state / CVR calibration route` か `abstention condition` を出すことは要求されていませんでした。
- 根拠:
  - Wu et al. (2023) は adult lifespan cohort で baseline CBF が multiple-demand network の BOLD activity と fluid intelligence の関係を部分的に説明することを示しました。
  - Epp et al. (2025) は、human cortex で BOLD と酸素代謝変化が有意 voxel の約40%で逆向きになりうることを示しました。
- 批判:
  - したがって、shared clock と geometry が揃っていても、hemodynamic amplitude difference をそのまま neural difference へ上げる仕様は甘いです。`vascular-state / CVR audit` を別欄として必須化する必要があります。

### 3. 旧 site rule は `fNIRS` を hemodynamic proxy に含めていましたが、superficial/systemic confound の operational rule が薄かった

- 問題:
  - 旧カード文面には `fMRI / fNIRS` が並んでいましたが、fNIRS 特有の superficial / autonomic confound をどう止めるかは表の上で十分に operational ではありませんでした。
- 根拠:
  - Yücel et al. (2015) は、short-separation regression が task 依存の autonomic response 差を含む fNIRS で統計的有意性と局在性の両方を改善することを示しました。
- 批判:
  - したがって、`hemodynamic proxy audit` は fMRI 用語だけでは足りません。fNIRS を含む場合の `short-separation / superficial diagnostic` も欄として明記する必要があります。

## 今回実行した変更

- `wiki/multimodal-integration-basics.md`
  - `last_updated` を `2026-03-17` に更新
  - page highlights / known points に `vascular state / CVR` を追加
  - `EEG-fMRI で追加する hemodynamic proxy gate` に `Vascular-state / CVR audit` 行を追加
  - Fusion Card の hemodynamic row を `vascular-state / CVR calibration route` と `fNIRS short-separation / superficial diagnostic` つきへ更新
  - site rules に `BOLD / fNIRS 振幅差を default で neural difference と書かない` を追加
- `wiki/measurement-stack-and-claim-ceiling.md`
  - page highlights / known points に `vascular transfer state` を追加
  - `fMRI / BOLD を別扱いにする理由` を `6つの failure mode` へ拡張し、`vascular state / cerebrovascular reactivity` 行を追加
  - hemodynamic modality の `measurement-side latent variable` を説明する note を追加
  - site rules に `vascular-state / CVR audit が無い BOLD / fNIRS 差は hemodynamic-limited difference に留める` を追加
- `verification.md`
  - Fusion Card 導入文を `HRF・vascular state / CVR・task-related haemodynamics・venous / superficial bias` へ更新
  - Fusion Card の hemodynamic row を `vascular-state / CVR calibration route` と `fNIRS short-separation / superficial diagnostic` つきへ更新
  - `最低運用ルール` に `vascular-state / CVR audit が無い group / cross-day difference は neural difference として受理しない` を追加
  - 参考文献に Murphy / Williams / Wu / Yücel / Epp を追加
- `tech_roadmap.md`
  - `fMRI の proxy ceiling` note に `vascular state / CVR` を追加
  - M5 の追加監査を `vascular-state / CVR calibration または abstention` つきへ更新
  - 参考文献に Murphy / Williams / Wu を追加
- `index.md`
  - 入口の multimodal note に `baseline vascular state / CVR を別監査しない限り、BOLD の群差や縦断差を neural difference と読まない` ルールを追加

## 外部依存で保留

- なし
  - 今回の修正は、公開本文と提出物仕様の改稿で完結しています。

## 参考文献

1. Murphy K, Harris AD, Wise RG. Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. *NeuroImage*. 2011;54(1):369-379.
   - https://doi.org/10.1016/j.neuroimage.2010.07.059
2. Williams RJ, Specht JL, Mazerolle EL, Lebel RM, MacDonald ME, Pike GB. Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. *Frontiers in Physiology*. 2023;14:1167148.
   - https://doi.org/10.3389/fphys.2023.1167148
3. Wu S, Tyler LK, Henson RNA, Rowe JB, Cam-CAN, Tsvetanov KA. Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. *Neurobiology of Aging*. 2023;121:1-14.
   - https://doi.org/10.1016/j.neurobiolaging.2022.09.006
4. Yücel MAY, Selb J, Aasted CMA, Petkov MP, Becerra L, Borsook D, Boas DA. Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. *Neurophotonics*. 2015;2(3):035005.
   - https://doi.org/10.1117/1.NPh.2.3.035005
5. Epp KJ, Lu H, Lydon-Staley DM, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
