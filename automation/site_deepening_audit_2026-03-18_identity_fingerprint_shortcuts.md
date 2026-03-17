# Site Deepening Audit (2026-03-18, Subject/Session Fingerprint Shortcuts and Personalization Boundaries)

## 対象

- 主対象: `tech_roadmap.md`
- 副対象: `verification.md`
- 副対象: `datasets.md`
- 副対象: `eeg_101.md`
- 副対象: `index.md`

## 今回の選定理由

- 2026-03-18 時点で、サイトは `movement / EOG / EMG / auditory feedback` の shortcut をかなり強く止められていました。
- その一方で、`subject / session fingerprint` は Verification の文言に散発的に出るだけで、一次文献の根拠、提出物仕様、入口ページの注意書き、Roadmap の個人化節へまだ十分に落ちていませんでした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、EEG や biomarker のモデルは `target variable` だけでなく `誰の信号か` `どの session か` を強く読めるからであり、split 設計や metadata baseline が甘いと、`task/disease を読んだ` を `participant fingerprint を読んだ` と取り違えるからです。

## 主要な批判点

### 1. 旧 `R6 個人化` は、personalization を性能改善の技巧としては読めても、`identity confound` の問題としては弱すぎました

- 問題:
  - `tech_roadmap.md` の `R6` は、問い自体は正しかった一方で、本文が実質 1 行しかなく、`一般モデル + 個人差` と `fingerprint shortcut` を区別する規律がありませんでした。
- 根拠:
  - <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> は、repeated measures を participant-disjoint にしない機械学習診断で subject characteristics が性能を押し上げうることを示しました。
  - <a href="https://doi.org/10.1016/j.patcog.2020.107381" target="_blank">Wang et al. (2020)</a> は、EEG connectivity graph からの biometric identification を示しました。
  - <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> は、resting-state EEG による個人識別が時間をまたいでも比較的頑健であることを示しました。
  - <a href="https://doi.org/10.1016/j.neuroimage.2022.119034" target="_blank">Gibson et al. (2022)</a> は、EEG variability に subject-driven 成分が強く残ることを整理しました。
- 批判:
  - したがって `個人化が効いた` だけでは、`神経変数を読んだ` とは言えません。
  - R6 は `personalization is needed` と `personalization may be a confound` の両面を同時に管理すべきでした。

### 2. 旧 `Specificity & Shortcut Card` は `session fingerprint` を例示していましたが、`fingerprint audit` が提出物の独立欄になっていませんでした

- 問題:
  - `verification.md` は shortcut family をかなり丁寧に整理していました。
  - しかし、`raw recording ancestry`、`window/epoch independence`、`subject/session/site/device disjointness`、`metadata-only baseline` を 1 つの独立欄としては要求していませんでした。
- 根拠:
  - <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> は split 設計そのものが subject characteristics の leakage を作ることを示しました。
  - <a href="https://doi.org/10.1016/j.patcog.2020.107381" target="_blank">Wang et al. (2020)</a> と <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> は、EEG に stable な individual fingerprint が十分存在することを示しました。
- 批判:
  - `movement / EMG / feedback` を書いていても、`誰の recording か` を見抜く route を別欄で固定しなければ、diagnosis や biomarker の score は still ambiguous です。
  - fingerprint audit が無い Specificity Card は、`same task` と `same person` を混ぜる事故を止め切れませんでした。

### 3. 旧 site entry は `派手な decode を過大評価しない` ところまでは行けても、`高 score = target signal` ではなく `high score = subject fingerprint` の誤読を入口で止め切れていませんでした

- 問題:
  - `index.md`、`datasets.md`、`eeg_101.md` は movement / EMG / feedback confounds を強く説明していました。
  - しかし、同じ raw recording から切った窓や subject-specific structure だけでも高 score が出る、という読み替え事故は entry layer でまだ弱かったです。
- 根拠:
  - <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>、<a href="https://doi.org/10.1016/j.patcog.2020.107381" target="_blank">Wang et al. (2020)</a>、<a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2022.119034" target="_blank">Gibson et al. (2022)</a>。
  - 既存の shortcut 文献として、<a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a>、<a href="https://doi.org/10.1523/ENEURO.0401-17.2018" target="_blank">Mostert et al. (2018)</a>、<a href="https://doi.org/10.1088/1741-2560/2/4/014" target="_blank">McFarland et al. (2005)</a>、<a href="https://doi.org/10.1038/s42256-024-00837-5" target="_blank">Chen et al. (2024)</a>。
- 批判:
  - 入口でこの経路を止めないと、within-session score や repeated-window score を `population biomarker` と誤読しやすくなります。
  - site-wide のルールとして、movement confound と同格に fingerprint confound を見せる必要がありました。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points に `personalization と fingerprint confound を分ける` 観点を追加
  - `R6 個人化` を全面改稿し、`shared model + subject-disjoint evaluation`、`shared encoder + light adaptation`、`fully subject-specific decoder` の 3 ルートを区別
  - `raw recording ancestry`、`subject/session disjointness`、`metadata-only baseline`、`adaptation budget` を site rule に追加
- `verification.md`
  - page highlights / known points の shortcut 記述を `subject / session fingerprint` まで拡張
  - `Specificity & Shortcut Card` に `fingerprint audit / independence unit` 行を追加
  - `slice-wise hold-out` に `subject hold-out` を追加
  - `subject / session fingerprint は独立の shortcut` という note を新設
  - 最低運用ルールに `fingerprint audit` 欠落時の downgrade rule を追加
- `datasets.md`
  - page highlights / known points を `subject / session fingerprint` まで更新
  - dataset card / baseline note に fingerprint 文献を追加
  - site rule に `raw recording ancestry`、`subject/session disjointness`、`metadata-only baseline` を追加
- `eeg_101.md`
  - page highlights / known points の shortcut 記述を fingerprint まで拡張
  - `見えた` と `target を見た` の違いを説明する note に fingerprint 文献を追加
- `index.md`
  - `last_updated` を `2026-03-18` に更新
  - page highlights / known points に fingerprint shortcut を追加
  - entry-level note として `高い decode score が、その人らしさを読んだだけでないか` を新設

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と site-wide 提出物仕様の改稿で完結しています。

## 参考文献

1. Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019;2(1).
   - https://doi.org/10.1038/s41746-019-0178-x
2. Wang M, Hu J, Abbass HA. BrainPrint: EEG biometric identification based on analyzing brain connectivity graphs. *Pattern Recognition*. 2020;105:107381.
   - https://doi.org/10.1016/j.patcog.2020.107381
3. Di Y, An X, Zhong W, Liu S, Ming D. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. *Frontiers in Human Neuroscience*. 2021;15.
   - https://doi.org/10.3389/fnhum.2021.672946
4. Gibson E, Lobaugh NJ, Joordens S, McIntosh AR. EEG variability: Task-driven or subject-driven signal of interest? *NeuroImage*. 2022;252:119034.
   - https://doi.org/10.1016/j.neuroimage.2022.119034
5. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
   - https://doi.org/10.1038/s41593-019-0502-4
6. Mostert P, Albers AM, Brinkman L, Todorova L, de Lange FP. Eye movement-related confounds in neural decoding of visual working memory representations. *eNeuro*. 2018.
   - https://doi.org/10.1523/ENEURO.0401-17.2018
7. McFarland DJ, McCane LM, David SV, Wolpaw JR. Brain-computer interface operation: signal and noise during early training sessions. *Journal of Neural Engineering*. 2005;2(4):S123-S130.
   - https://doi.org/10.1088/1741-2560/2/4/014
8. Chen Z, Yao D, Wang M, et al. A neural speech decoding framework leveraging deep learning and speech synthesis. *Nature Machine Intelligence*. 2024.
   - https://doi.org/10.1038/s42256-024-00837-5
