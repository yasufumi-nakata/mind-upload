# Site Deepening Audit (2026-03-20, L0 Artifact Pack Sync)

## 対象

- 主対象: `wiki/l0-minimum-artifact-pack.md`
- 副対象: `datasets.md`

## 今回の選定理由

- 2026-03-20 時点で、公開サイトの `datasets.md` はすでに `Event Fidelity Card`、`label provenance`、`acquisition-distribution shortcut`、`derivative lineage`、`stopping claim` まで要求する運用水準に上がっていました。
- その一方で、実際に L0 提出物の形を決める `wiki/l0-minimum-artifact-pack.md` は、なお `version + BIDS + QC + split + baseline + runbook` を中心にしており、最新の実務要件を十分に反映しておりませんでした。
- この不整合は技術・自然科学の観点で重要です。理由は、実践入口の artifact pack が弱いと、読者は `BIDS を通して accuracy を出した` だけで L0 が成立したかのように誤読し、event fidelity・label provenance・setup shortcut・derivative lineage という実際には結果の意味を大きく変える条件を落としやすくなるからです。

## 根拠付き批判

### 1. 旧 L0 artifact pack は BIDS/QC を重視していた一方で、annotation の階層と event fidelity を十分に operationalize していませんでした

- 問題:
  - 旧 `wiki/l0-minimum-artifact-pack.md` は `dataset version`、`BIDS skeleton`、`Validator`、`QC log` を置いていました。
  - しかし `datasets.md` がすでに要求している `event semantics`、`clock domain + delay/jitter audit`、`label provenance / scorer / report-usage flag` を、L0 の提出物として固定していませんでした。
- 根拠:
  - BIDS annotation tutorial は、annotation を dataset / subject / session / scans / events の複数層で扱い、`dataset_description.json`、`README`、`participants.tsv`、`sessions.tsv`、`scans.tsv`、`events.tsv` を整理しています。
  - EEG-BIDS (Pernet et al., 2019) は、EEG-BIDS が raw EEG の共有可能性と再利用性を高める一方、それ自体は次段の解析の `necessary step` に過ぎないと位置づけています。
  - MNE-BIDS docs も、既に変更された preloaded data を raw として無造作に書き戻すことをデフォルトで防ぎ、必要時は derivatives として扱うべきだと明示しています。
  - EEGMMIDB、CHB-MIT、Sleep-EDF、TUH/TUSZ はいずれも label/event origin が異なり、cue annotation、expert interval、R&K hypnogram、report-derived label を同じ「ラベル付き EEG」として扱うと評価意味が崩れます。
- 批判:
  - したがって、L0 pack が `BIDS に置ける` だけで止まるのは弱すぎます。
  - L0 段階でも `event fidelity` と `label provenance` を pack に含めないと、その後の accuracy が何を測ったのかを第三者が再構成できません。

### 2. 旧 L0 artifact pack は score を支える evaluation family と hold-out ancestry を十分に固定していませんでした

- 問題:
  - 旧 pack は `split rule` を要求していましたが、`within-session / cross-session / cross-subject / adaptation` の family 差、独立 hold-out unit、window ancestry、target-session data usage までを強く要求していませんでした。
- 根拠:
  - MOABB は within-session / cross-session / cross-subject を別 evaluation class として実装しています。
  - Ma et al. (2022) の 5-day motor-imagery dataset では、within-session 68.8%、cross-session 53.7%、cross-session adaptation 78.9% と大きく差が出ており、同じ accuracy でも支持できる主張が違うことが明瞭です。
  - Chaibub Neto et al. (2019) は record-wise split による identity confounding が性能を過大化しうることを示しました。
- 批判:
  - したがって `split rule があります` だけでは不十分です。
  - `何を hold out したか`、`同一 raw recording から切り出した window が両側に入っていないか`、`adaptation を許したか` を L0 pack に固定しない限り、比較可能性の最低線すら確保できません。

### 3. 旧 L0 artifact pack は acquisition-distribution shortcut と derivative lineage を運用項目として前面化していませんでした

- 問題:
  - 旧 pack は `baseline` と `execution steps` を要求していましたが、`site / device / reference / electrode layout / protocol` を独立 shortcut family として summary すること、metadata-only baseline を置くこと、preprocessed data を derivatives として明示することを弱くしか書いていませんでした。
- 根拠:
  - Melnik et al. (2017) は EEG recording が subject / session だけでなく system にも依存することを示しました。
  - Xu et al. (2020) は amplifier, cap, sampling rate, filtering などの dataset variability が cross-dataset decoding を崩すことを示しました。
  - MNE-BIDS docs は modified / preloaded data の raw 書き戻しを既定で防ぎ、derivatives として扱う場合のみ慎重に許可しています。
- 批判:
  - したがって L0 pack に `acquisition-distribution summary + harmonization log + derivative lineage` を入れないと、後から見た第三者は signal difference と setup difference を区別できません。
  - これは L1/L2 の話ではなく、L0 comparability の最低条件です。

## 今回実行した変更

- `wiki/l0-minimum-artifact-pack.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` を、現行の practical-page rule に同期しました。
  - `Minimum 8 points` をやめ、`Minimum 11 items` として以下を pack に固定しました。
    - dataset identity
    - BIDS / EEG-BIDS skeleton
    - Event Fidelity Card
    - label provenance / report-usage flag
    - split family + hold-out ancestry
    - acquisition-distribution summary + harmonization log
    - QC / exclusion log
    - baseline + nuisance / metadata checks
    - derivative lineage
    - execution steps / environment
    - failure examples + stopping claim
  - `why the old pack is now too weak` 節と `five bundles` 節を追加し、なぜ pack を増やす必要があるかを説明しました。
  - 参考文献節を新設し、公式仕様・公式 docs・一次文献・公式 dataset pages をまとめました。
- `datasets.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - `page_highlights` / `known_points` に、L0 artifact pack sync の要点を追加しました。
  - `L0 minimum loop` 節の導入・bullet・note を更新し、現在の practical rule が `version/BIDS/QC` だけでなく `event fidelity / label provenance / acquisition distribution / derivative lineage / stopping claim` まで含むことを明文化しました。

## 外部依存で保留

- なし
  - 今回の変更は公開本文と wiki 運用本文の同期で完結しております。

## 参考文献

1. BIDS Website. Annotating a BIDS dataset.
   - https://bids.neuroimaging.io/getting_started/tutorials/annotation.html
2. BIDS Specification 1.11.1. Electroencephalography.
   - https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
3. Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Scientific Data*. 2019;6:103.
   - https://doi.org/10.1038/s41597-019-0104-8
4. MNE-BIDS documentation. `write_raw_bids`.
   - https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html
5. Jayaram V, Barachant A. MOABB: trustworthy algorithm benchmarking for BCIs. *Journal of Neural Engineering*. 2018;15(6):066011.
   - https://doi.org/10.1088/1741-2552/aadea0
6. MOABB Docs: WithinSessionEvaluation.
   - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.WithinSessionEvaluation.html
7. MOABB Docs: CrossSessionEvaluation.
   - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSessionEvaluation.html
8. MOABB Docs: CrossSubjectEvaluation.
   - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSubjectEvaluation.html
9. Ma T, Xiao X, Li W, et al. A large EEG dataset for studying cross-session variability in motor imagery BCI. *Scientific Data*. 2022;9:569.
   - https://doi.org/10.1038/s41597-022-01647-1
10. Chaibub Neto E, Osório RS, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019;2:99.
   - https://doi.org/10.1038/s41746-019-0178-x
11. Melnik A, Legkov P, Izdebski K, et al. Systems, subjects, sessions: to what extent do these factors influence EEG data? *Frontiers in Human Neuroscience*. 2017;11:150.
   - https://doi.org/10.3389/fnhum.2017.00150
12. Xu M, Frølich L, et al. Cross-dataset deep learning for EEG. *Frontiers in Human Neuroscience*. 2020;14:103.
   - https://doi.org/10.3389/fnhum.2020.00103
13. PhysioNet. EEG Motor Movement/Imagery Dataset.
   - https://physionet.org/content/eegmmidb/1.0.0/
14. PhysioNet. CHB-MIT Scalp EEG Database.
   - https://physionet.org/content/chbmit/1.0.0/
15. PhysioNet. Sleep-EDF Database Expanded.
   - https://physionet.org/content/sleep-edfx/1.0.0/
16. Obeid I, Picone J. The Temple University Hospital EEG Data Corpus. *Frontiers in Neuroscience*. 2016;10:196.
   - https://doi.org/10.3389/fnins.2016.00196
