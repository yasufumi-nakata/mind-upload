# Site Deepening Audit (2026-03-18, Specificity / Shortcut Card for EEG Decode and Biomarker Claims)

## 対象

- 主対象: `verification.md`
- 副対象: `eeg_101.md`
- 副対象: `datasets.md`

## 今回の選定理由

- 2026-03-17 時点でサイトは、`observability`、`identifiability`、`deployability`、`language prior`、`benchmark governance`、`maintenance-state` をかなり強く整理できていました。
- その一方で、`高い decode score が target neural variable を読んだのか、それとも eye movement / EMG / uninstructed movement / auditory feedback / session fingerprint を読んだのか` は、複数ページに散在する注意書きとしては存在していても、site-wide の提出物仕様にはまだなっていませんでした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、sensor に情報が入っていることと、その情報が目的変数に特異的であることは別であり、ここを混ぜると `signal present` を `target-specific readout` に誤昇格させるからです。

## 主要な批判点

### 1. 旧 site rule は `何が見えたか` を固定できても、`どの経路で score が出たか` を site-wide に固定できていませんでした

- 問題:
  - `verification.md` の Observability Budget は、measurement stack、direct observables、remaining latent state をうまく固定していました。
  - しかし、同じ observed signal が `target neural variable` 由来なのか、`nuisance route` 由来なのかを site-wide に固定する欄がありませんでした。
- 根拠:
  - Musall et al. (2019) は、task 中の neural dynamics が uninstructed movements に強く支配されうることを示しました。
  - Mostert et al. (2018) は、visual working memory decode で eye movement-related confounds が残りうることを示しました。
  - Muthukumaraswamy (2013) は、高 beta / gamma 近傍で muscle artifact が neural activity と重なりやすいことを整理しました。
- 批判:
  - `何かが sensor に入った` だけでは、`target neural variable を読んだ` とは言えません。
  - Observability Budget だけでは、signal presence と route specificity を分けきれませんでした。

### 2. 旧 site は speech / language には Neural Contribution Card を持っていましたが、一般 decode / biomarker には対称な仕様がありませんでした

- 問題:
  - `verification.md` は brain-to-text / speech decode に対して Neural Contribution Card を持ち、language prior と brain-derived information を丁寧に分離していました。
  - しかし、motor imagery、visual decode、state biomarker、clinical classifier のような一般 decode に対しては、同じ構造の監査仕様がありませんでした。
- 根拠:
  - McFarland et al. (2005) は、early BCI session で EMG が BCI performance を押し上げうることを示しました。
  - Chen et al. (2024) は、speech decode で post-onset auditory feedback を含む non-causal path が offline score を inflate しうることを示しました。
- 批判:
  - これは `language prior だけは card 化するが、movement / EMG / EOG / feedback は narrative で済ませる` という非対称性でした。
  - 実際には、どちらも `target path と shortcut path の分離` という同じ問題です。

### 3. 旧 `eeg_101.md` は 3 gate でしたが、`specificity gate` が無いため entry page で誤読が残りました

- 問題:
  - 旧 `eeg_101.md` は observability / identifiability / deployability の 3 分割を採っていました。
  - しかし、`情報がある` と `target neural variable に比較的特異的である` の間に 1 段の gate がありませんでした。
- 根拠:
  - Mostert et al. (2018) は attempted fixation 下でも eye movement confound を示しました。
  - McFarland et al. (2005) は early BCI session の signal source に EMG が入りうることを示しました。
  - Chen et al. (2024) は causal / non-causal の差で speech decode の score 解釈が変わることを示しました。
- 批判:
  - 3 gate のままでは、entry page で `high score = neural readout` の誤読を十分に止められませんでした。

### 4. 旧 `datasets.md` は evaluation family を固定していましたが、shortcut slice を固定していませんでした

- 問題:
  - `datasets.md` は within-session / cross-session / cross-subject / adaptation を分けていました。
  - しかし、`low vs high movement`、`fixed gaze vs free viewing`、`feedback on vs off`、`artifact burden slice` のような nuisance regime の hold-out は card 化していませんでした。
- 批判:
  - これでは evaluation family を分けても、なお target specificity の読み替えが残ります。

## 今回実行した変更

- `verification.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points に `Specificity & Shortcut Card` の方針を追加
  - `Leaderboard & Model Cards` の site-wide 提出物一覧に `Specificity & Shortcut Card` を追加
  - 新節 `Specificity & Shortcut Card` を追加
  - `target variable / intended causal path`、`plausible nuisance routes`、`nuisance observables / auxiliary channels`、`nuisance-only baselines`、`slice-wise hold-out`、`countermeasure / perturbation check`、`claim ceiling` を固定
  - `Neural Contribution Card` を、この一般カードの言語系特化版として位置づけ直した
- `eeg_101.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points を更新
  - `EEG の主張は 3 つの gate` を `4 つの gate` に改稿し、`specificity gate` を追加
  - same-day score と shortcut route の関係を、Mostert / McFarland / Chen まで含めて entry page に下ろした
  - `Verification の Specificity & Shortcut Card` への導線を追加
- `datasets.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points を更新
  - generalization 節に `同じ score でも、どの経路で出たかを固定する` note を追加
  - dataset card / baseline 結果にも `Specificity & Shortcut Card` を重ねる方針を追記

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と site-wide 提出物仕様の改稿で完結しています。

## 参考文献

1. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
   - https://doi.org/10.1038/s41593-019-0502-4
2. Mostert P, Albers AM, Brinkman L, Todorova L, de Lange FP. Eye movement-related confounds in neural decoding of visual working memory representations. *eNeuro*. 2018.
   - https://doi.org/10.1523/ENEURO.0401-17.2018
3. Muthukumaraswamy SD. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. *Frontiers in Human Neuroscience*. 2013.
   - https://doi.org/10.3389/fnhum.2013.00138
4. McFarland DJ, McCane LM, David SV, Wolpaw JR. Brain-computer interface operation: signal and noise during early training sessions. *Journal of Neural Engineering*. 2005.
   - https://doi.org/10.1088/1741-2560/2/4/014
5. Chen Z, Yao D, Wang M, et al. A neural speech decoding framework leveraging deep learning and speech synthesis. *Nature Machine Intelligence*. 2024.
   - https://doi.org/10.1038/s42256-024-00837-5
6. Ma B, Zhang Y, Cheng J, et al. A large EEG dataset for studying cross-session variability in motor imagery BCI. *Scientific Data*. 2022.
   - https://doi.org/10.1038/s41597-022-01647-1
7. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
