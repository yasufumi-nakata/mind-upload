# Site Deepening Audit (2026-03-26, EEG preprocessing split-locked transforms / derivative lineage)

## 対象

- 主対象: `wiki/eeg-preprocessing-and-qc.md`
- 同期対象: `github-wiki-export/eeg-preprocessing-and-qc.md`
- web確認対象:
  - `https://doi.org/10.1038/s42003-025-08464-3`
  - `https://doi.org/10.3389/fnins.2024.1373515`
  - `https://doi.org/10.1016/j.compbiomed.2025.110608`
  - `https://doi.org/10.1038/s41746-019-0178-x`
  - `https://doi.org/10.1016/j.neuroimage.2022.119034`
  - `https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html`
  - `https://scikit-learn.org/stable/common_pitfalls.html`
- 調査範囲: 技術 / 自然科学のみ

## 今回このページを選んだ理由

- `wiki/eeg-preprocessing-and-qc.md` は 2026-03-19 更新で、reference / filter / artifact の基本停止線はかなり整っていました。
- しかし、その後 site 全体で強化された
  - split / leakage
  - subject / session fingerprint
  - derivative lineage
  - benchmark governance
  のうち、前処理ページだけはなお `waveform cleanup` の比重が強く、`fit される前処理そのものが hold-out を汚しうる` という 2024-2025 年の重要な停止線が正面化されていませんでした。
- これは技術・自然科学の観点で弱点です。EEG では同一被験者・同一セッションの segment 同士が似ており、しかも ICA / Autoreject / normalization / PCA / learned denoiser のような data-fitted transform は train/test 境界の外で fit すると、その時点で hold-out へ情報が流れ込みうるためです。

## 根拠付き批判

### 1. 旧ページは preprocessing を split design から切り離しすぎていました

- 根拠:
  - [Kessler et al. (2025)](https://doi.org/10.1038/s42003-025-08464-3) は、ICA や autoreject のような処理で latent leakage が起こりうることを明示し、temporally separated segments や fold-wise preprocessing を対策候補として議論しています。
  - [Brookshire et al. (2024)](https://doi.org/10.3389/fnins.2024.1373515) は、segment-based holdout で同一 subject が train/test の両方へ入ると、subject-specific pattern の漏洩で精度が過大評価されうることを示しました。
  - [Del Pup et al. (2025)](https://doi.org/10.1016/j.compbiomed.2025.110608) は、sample-based cross-validation が EEG deep learning の性能を過大評価し、nested subject-based strategy がより現実的だと示しました。
  - [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) も一般則として、前処理は train で fit し test へ apply すべきだと明記しています。
- 批判:
  - したがって `前処理を先に済ませ、その後で split する` という暗黙の読み方を残すのは弱いです。
  - EEG 前処理ページ自体が、`fixed transform` と `data-fitted transform` を分けていないと、読者は hold-out を汚した clean derivative を `generalization evidence` と誤読しえます。

### 2. 旧ページは clean EEG の provenance を十分に固定していませんでした

- 根拠:
  - [BIDS Derivatives](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html) は、`Sources`、`source_entities`、`desc-<label>`、`descriptions.tsv` により、derivative の生成元と processing branch を明示する設計を与えています。
  - 同仕様は、derivative を後続処理で `critically reuse` できるだけの data / metadata を残すことを動機にしています。
- 批判:
  - 旧ページは raw-clean delta や retention は要求していましたが、`どの raw run / derivative branch から来た clean file か`、`window ancestry がどう hold-out に接続しているか` を主軸にしていませんでした。
  - そのため、見た目のよい clean EEG を reusable artifact と過読しうる構造が残っていました。

### 3. 旧ページでは subject/session shortcut の監査開始点が遅すぎました

- 根拠:
  - [Chaibub Neto et al. (2019)](https://doi.org/10.1038/s41746-019-0178-x) は、subject characteristic が ML 診断性能を汚染しうることを示しました。
  - [Gibson et al. (2022)](https://doi.org/10.1016/j.neuroimage.2022.119034) は、EEG variability が task-driven change より stable subject identity を強く反映しうることを示しました。
  - [Brookshire et al. (2024)](https://doi.org/10.3389/fnins.2024.1373515) も、same-subject segments の類似性を data leakage の中心問題として示しています。
- 批判:
  - よって shortcut / fingerprint audit を classifier 以降の話として処理するのは弱いです。
  - reference / montage / bad-channel map / interpolation pattern / normalization constant / temporal adjacency のようなものも、前処理段階から shortcut route たりえます。

## 今回実行した変更

- `wiki/eeg-preprocessing-and-qc.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - front matter の `description` / `page_highlights` / `known_points` / `unknown_points` を更新し、`split-locked transform`、`derivative lineage`、`subject/session shortcut risk` を前面化しました。
  - `2026-03-26 correction: preprocessing is also part of split design` note を新設しました。
  - 監査ゲートを `7` から `10` に拡張し、
    - split-locked transform
    - derivative-lineage / ancestry
    - shortcut / fingerprint
    を独立 gate として追加しました。
  - `If preprocessing learns from data, it belongs inside the training split` 節を新設し、
    - fixed preregistered transform
    - ICA / ASR / Autoreject / bad-channel model
    - normalization / PCA / feature selection / learned denoiser
    を分けて site rule を明記しました。
  - `Clean EEG is reusable only when derivative lineage and ancestry remain explicit` 節を新設し、
    - `Sources`
    - `source_entities`
    - `desc-<label>`
    - raw-window ancestry
    を minimum provenance に昇格しました。
  - `Shortcut and fingerprint audit starts before the classifier` 節を新設し、subject/session/acquisition-distribution shortcut を前処理段階から監査する構成へ改めました。
  - `Minimum submissions` を更新し、
    - split / evaluation manifest
    - transform-fit ledger
    - derivative-lineage manifest
    を追加しました。
  - `Misinterpretations` を更新し、
    - split 後でない fit
    - balanced random windows
    - automatic pipeline = reproducible
    の誤読を止めました。
  - 参考文献に Brookshire 2024、Del Pup 2025、Chaibub Neto 2019、Gibson 2022、BIDS Derivatives、scikit-learn official docs を追加しました。

## 外部依存タスク

- なし
  - 今回の修正はこのセッションで repo 内完結で実行可能でした。

## 参考文献

1. Kessler V, et al. How EEG preprocessing shapes decoding performance. *Communications Biology*. 2025. https://doi.org/10.1038/s42003-025-08464-3
2. Brookshire G, Kasper J, Blauch NM, et al. Data leakage in deep learning studies of translational EEG. *Frontiers in Neuroscience*. 2024. https://doi.org/10.3389/fnins.2024.1373515
3. Del Pup F, Zanola A, Tshimanga LF, et al. The role of data partitioning on the performance of EEG-based deep learning models in supervised cross-subject analysis: A preliminary study. *Computers in Biology and Medicine*. 2025. https://doi.org/10.1016/j.compbiomed.2025.110608
4. Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019. https://doi.org/10.1038/s41746-019-0178-x
5. Gibson E, Lobaugh NJ, Joordens S, McIntosh AR. EEG variability: Task-driven or subject-driven signal of interest? *NeuroImage*. 2022. https://doi.org/10.1016/j.neuroimage.2022.119034
6. BIDS Derivatives: Common data types and metadata. official docs. https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html
7. Scikit-learn: Common pitfalls and recommended practices. official docs. https://scikit-learn.org/stable/common_pitfalls.html
