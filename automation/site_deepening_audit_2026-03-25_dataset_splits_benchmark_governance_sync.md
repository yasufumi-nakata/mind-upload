# Site Deepening Audit (2026-03-25, dataset split / benchmark-governance sync)

## 対象

- 主対象: `wiki/dataset-splits-and-leakage.md`
- 範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `datasets.md`、`eeg_101.md`、`wiki/eeg-foundation-models.md` では既に
  - `acquisition-distribution shortcut`
  - `benchmark provenance`
  - `official challenge postmortem`
  を独立 stop line として扱っていました。
- しかし `wiki/dataset-splits-and-leakage.md` は、依然として
  - subject / session / time split
  - preprocessing leakage
  - report leakage
  を中心とする古い版に近く、
  - `site / device / reference / electrode layout`
  - `benchmark version / hidden grouping / inference-stage rules / postmortem`
  が弱いままでした。
- これは site-wide inconsistency です。L0 実務で最も参照される wiki が古いままだと、公開トップで強く止めている規律が、手順ページで再び緩んでしまうからです。

## 根拠付き批判

### 1. split hygiene だけでは identity / acquisition shortcut を止め切れません

- [Chaibub Neto et al. (2019)](https://doi.org/10.1038/s41746-019-0178-x) は、record-wise split が diagnostic setting で prediction error を大きく過小評価しうること、subject-wise split が identity confounding を自動的に中和することを示しました。
- [Melnik et al. (2017)](https://doi.org/10.3389/fnhum.2017.00150) は、EEG 記録が subject だけでなく session や system にも影響されることを示しました。
- [Xu et al. (2020)](https://doi.org/10.3389/fnhum.2020.00103) は、cross-dataset EEG decoding が acquisition environment に強く依存することを示しました。
- [Di et al. (2021)](https://doi.org/10.3389/fnhum.2021.672946) は、resting-state EEG から個体識別が時間を隔ててもかなり成立することを示しました。

批判:

- したがって `subject / session / time split を書いた` だけでは不十分です。
- `site / device / reference / electrode layout / protocol distribution` を独立 shortcut family として公開しなければ、モデルが target neural variable ではなく acquisition-distribution を読んでいる可能性が残ります。

### 2. benchmark governance は administrative detail ではなく benchmark object の一部です

- EEG Challenge (2025) の公式 [homepage](https://eeg2025.github.io/) は、challenge preprint が execution-phase 変更に対して古くなっており、website と starter kit を current source として使うよう明記しています。
- 公式 [rules](https://eeg2025.github.io/rules/) は、additional pretraining data、pretrained model / fine-tuning disclosure、code submission at inference stage、single-GPU 20 GB budget を要求しています。
- 公式 [submission page](https://eeg2025.github.io/submission/) は、inference-only code competition であることを固定しています。
- 公式 [leaderboard](https://eeg2025.github.io/leaderboard/) は、Challenge 2 sample が randomize されておらず contiguous-trial same-subject structure を exploit できたと公表し、最終賞構造を変更しました。

批判:

- これは周辺事情ではありません。
- `benchmark version`、`split / randomization`、`hidden grouping`、`extra-data / checkpoint policy`、`inference-stage restrictions`、`postmortem` はすべて benchmark result の意味を変えます。
- それにもかかわらず dataset-split wiki が benchmark governance を扱っていないのは、2026-03 時点の site-wide rule に比べて明らかに弱い状態でした。

## 今回実行した変更

- `wiki/dataset-splits-and-leakage.md`
  - `last_updated` を `2026-03-25` に更新しました。
  - front matter の description / page_intro / accuracy_note / highlights / known_points を更新し、`acquisition-distribution shortcut` と `benchmark-governance` を前面化しました。
  - `Wiki: EEG foundation models and pretraining` への導線を追加しました。
  - `2026-03 re-audit: split hygiene is necessary, not sufficient` note-box を追加しました。
  - common leak table を 5 件から 7 件に拡張し、
    - `site / device / reference / layout shortcut`
    - `challenge operations changed`
    を追加しました。
  - `Split hygiene still leaves four shortcut families` table を新設し、
    - subject / session fingerprint
    - acquisition-distribution shortcut
    - report / metadata shortcut
    - benchmark-governance shortcut
    を独立 stop line として固定しました。
  - `Benchmark governance is part of leakage control, not administrative detail` note-box を追加し、EEG Challenge 2025 の公式 sources を根拠として benchmark object の再定義を明文化しました。
  - report checklist を改稿し、evaluation family、window ancestry、acquisition-distribution audit、benchmark provenance、stopping claim を追加しました。
  - references に Chaibub Neto, Melnik, Xu, Di と EEG Challenge 2025 公式 sources を追加しました。

## 今回修正しないもの

- `datasets.md` 側の front-door 規律
  - こちらは既に同種の stop line を持っており、今回の主問題は wiki 側の遅れでした。
- 哲学 / 法学 / personhood 論点
  - 今回は技術・自然科学だけを扱いました。
- `issue.md`
  - ユーザー前提どおり再確認していません。

## 外部依存で保留

- なし
  - 今回の変更は、このリポジトリ内の公開 wiki 修正・検証・push までで完結できます。

## 参考文献 / 公式ソース

1. Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019.
   - https://doi.org/10.1038/s41746-019-0178-x
2. Melnik A, Legkov P, Izdebski K, et al. Systems, subjects, sessions: To what extent do these factors influence EEG data? *Frontiers in Human Neuroscience*. 2017.
   - https://doi.org/10.3389/fnhum.2017.00150
3. Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. *Frontiers in Human Neuroscience*. 2020.
   - https://doi.org/10.3389/fnhum.2020.00103
4. Di Y, An X, Zhong W, Liu S, Ming D. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. *Frontiers in Human Neuroscience*. 2021.
   - https://doi.org/10.3389/fnhum.2021.672946
5. EEG Challenge (2025) official homepage.
   - https://eeg2025.github.io/
6. EEG Challenge (2025) official rules.
   - https://eeg2025.github.io/rules/
7. EEG Challenge (2025) official submission page.
   - https://eeg2025.github.io/submission/
8. EEG Challenge (2025) official leaderboard / organizer postmortem.
   - https://eeg2025.github.io/leaderboard/
