# Site Deepening Audit (2026-03-25, baseline / benchmark / model-card artifact stack)

## 対象

- 主対象: `wiki/baselines-prereg-and-model-cards.md`
- 同期対象: `github-wiki-export/baselines-prereg-and-model-cards.md`
- 範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- 公開サイトの中核規則は 2026-03-25 時点でかなり厳密になっております。
- 具体的には、
  - `benchmark governance`
  - `metric semantics`
  - `Specificity & Shortcut Card`
  - `Human Proxy Composition Card`
  - `State-Continuity Bridge Card`
  - `Pretraining Card`
  - `Fusion Card`
  が、`verification.md` や関連 wiki で独立の stop line として運用されております。
- しかし `wiki/baselines-prereg-and-model-cards.md` だけは、依然として
  - `baseline`
  - `benchmark`
  - `pre-registration`
  - `model card`
  - `Fusion Card`
  - `Pretraining Card`
  までが主語であり、現在の site-wide rule に比べて artifact stack の説明が遅れておりました。
- その結果、技術読者はこのページを読むと、`model card + score` を中心に据えた古い理解へ戻りやすく、最新の公開規則より弱い reading rule を学んでしまいます。

## 根拠付き批判

### 1. benchmark は score sheet ではございません

- EEG Challenge (2025) の公式 [homepage](https://eeg2025.github.io/) は、challenge preprint が execution-phase 変更に対して古くなっており、website と starter kit を current source として使うよう明記しております。
- 公式 [rules](https://eeg2025.github.io/rules/) は、additional pretraining data、pretrained model / fine-tuning disclosure、code submission at inference stage、single-GPU 20 GB budget を要求しております。
- 公式 [leaderboard](https://eeg2025.github.io/leaderboard/) は、Challenge 2 sample が randomize されておらず contiguous-trial same-subject structure が残っていたことを公表し、結果の読み方自体を変えました。
- [Xiong et al. (2025)](https://arxiv.org/abs/2508.17742) と [Liu et al. (2026)](https://arxiv.org/abs/2601.17883) も、EEG foundation-model 比較が protocol と evaluation design に敏感であることを示しております。

批判:

- したがって、`benchmark = task + dataset + score` という説明は 2026-03 時点では科学的に弱すぎます。
- benchmark object には少なくとも
  - split / randomization rule
  - task-matched metric bundle
  - extra-data / checkpoint policy
  - inference-stage restriction
  - benchmark version / postmortem
  が含まれます。

### 2. metric semantics は benchmark の外側ではなく内側です

- [Saito & Rehmsmeier (2015)](https://doi.org/10.1371/journal.pone.0118432) は、class imbalance 下で ROC だけでは不十分で precision-recall がより informative になりうることを示しました。
- [Roy et al. (2021)](https://doi.org/10.1016/j.ebiom.2021.103275) は EEG clinical DL の実務評価が event sensitivity, false alarms, latency など task-dependent object に依存することを示しております。
- [Sun et al. (2017)](https://doi.org/10.1093/sleep/zsx139) と [Vallat & Walker (2021)](https://doi.org/10.7554/eLife.70092) は、sleep staging で class imbalance と pooled summary が per-stage weakness を隠しうることを示しました。

批判:

- したがって、benchmark row が `which indicators to compare` とだけ書かれているのは粗すぎます。
- `one headline number` を避けるために、benchmark row 自体へ `task-matched metric bundle` を入れる必要がございました。

### 3. model card 単独では decode / transfer claim の shortcut を止められません

- [Chaibub Neto et al. (2019)](https://doi.org/10.1038/s41746-019-0178-x) は subject characteristics による confounding を示しました。
- [Xu et al. (2020)](https://doi.org/10.3389/fnhum.2020.00103) は cross-dataset EEG decoding が acquisition environment に強く依存することを示しました。
- [Di et al. (2021)](https://doi.org/10.3389/fnhum.2021.672946) は resting-state EEG から時間をまたいだ個体識別が可能であることを示しました。

批判:

- したがって、score と weakness を書いた model card だけでは、`target neural variable` と `shortcut` を分離できません。
- 現在の site-wide rule に合わせるなら、`Specificity & Shortcut Card` を artifact stack に明示する必要がございました。

### 4. multimodal / proxy-rich / same-subject wording は別々の監査を要します

- [Kothe et al. (2025)](https://doi.org/10.1162/IMAG.a.136), [Wei et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116595), [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z), [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は、同期収録や fusion が即ち validated integration ではないことを示しております。
- [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024), [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072), [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998), [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3), [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は living-human proxy rows が quantity type / model burden / operational maturity の異なる rows であることを示しております。
- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520), [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6), [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w), [Attardo et al. (2015)](https://doi.org/10.1038/nature14467) は same-subject / same-brain wording が sequential bridge burden を消さないことを示しております。

批判:

- にもかかわらず旧ページは、`Fusion Card` と `Pretraining Card` までしか artifact stack を列挙しておりませんでした。
- これは現在の verification rule より弱く、
  - several living-human proxy rows
  - same-subject / same-brain sequential bridge
  - decode / transfer shortcut resistance
  を public learning page で再び見えにくくしておりました。

## 今回実行した変更

### `wiki/baselines-prereg-and-model-cards.md`

- `last_updated` を `2026-03-25` に更新しました。
- front matter を更新し、`benchmark governance`、`metric semantics`、`Specificity & Shortcut Card`、`Human Proxy Composition Card`、`State-Continuity Bridge Card` を page role に反映しました。
- addendum を 3 系統へ整理しました。
  - benchmark object の再定義
  - model card が full stack ではないこと
  - Observability Budget の位置づけ
- `roles` table を 3 列に拡張し、以下を独立 artifact として追加しました。
  - `Observability Budget`
  - `Specificity & Shortcut Card`
  - `Human Proxy Composition Card`
  - `State-Continuity Bridge Card`
- `What a benchmark fixes on this site` table を新設し、
  - split / randomization
  - metric bundle
  - extra-data / checkpoint policy
  - operational restriction
  - version / postmortem
  を benchmark object の内部へ移しました。
- `Which extra artifacts are triggered by the claim` table を新設し、claim shape ごとに追加カードを固定しました。
- `simple-flow` を 5 段階へ改め、`benchmark object` と `triggered companion cards` を最小手順へ組み込みました。
- public-page checklist を現行 site-wide rule に同期し、
  - metric bundle
  - benchmark governance
  - shortcut audit
  - proxy composition
  - state-continuity bridge
  を確認項目へ追加しました。
- references を全面更新しました。

### `github-wiki-export/baselines-prereg-and-model-cards.md`

- `wiki/` source から再生成対象として同期します。

## その結果、このサイトで何が改善されたか

- 学習ページの入口でも、`good score = comparable evidence` という誤読を止められるようになりました。
- `model card` を万能 artifact と読むのではなく、claim shape に応じて
  - shortcut
  - multimodal fusion
  - pretraining governance
  - human proxy composition
  - sequential bridge continuity
  を別カードで監査する site rule が visible になりました。
- その結果、Verification 本体と wiki 入門ページの規律が揃いました。

## 外部依存で保留

- なし
  - 今回の作業は、このリポジトリ内の wiki source 修正、export 再生成、検証、commit、push までで完結できます。

## 参考文献 / 公式ソース

1. EEG Challenge (2025) homepage.
   - https://eeg2025.github.io/
2. EEG Challenge (2025) rules.
   - https://eeg2025.github.io/rules/
3. EEG Challenge (2025) leaderboard.
   - https://eeg2025.github.io/leaderboard/
4. Saito T, Rehmsmeier M. The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets. *PLOS ONE*. 2015.
   - https://doi.org/10.1371/journal.pone.0118432
5. Roy Y, Banville H, Albuquerque I, et al. Deep learning-based electroencephalography analysis: a systematic review. *EBioMedicine*. 2021.
   - https://doi.org/10.1016/j.ebiom.2021.103275
6. Sun H, Paixao L, Oliva JT, et al. Brain age from the electroencephalogram of sleep. *Sleep*. 2017.
   - https://doi.org/10.1093/sleep/zsx139
7. Vallat R, Walker MP. An open-source, high-performance tool for automated sleep staging. *eLife*. 2021.
   - https://doi.org/10.7554/eLife.70092
8. Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019.
   - https://doi.org/10.1038/s41746-019-0178-x
9. Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. *Frontiers in Human Neuroscience*. 2020.
   - https://doi.org/10.3389/fnhum.2020.00103
10. Di Y, An X, Zhong W, Liu S, Ming D. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. *Frontiers in Human Neuroscience*. 2021.
   - https://doi.org/10.3389/fnhum.2021.672946
11. Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
12. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
   - https://arxiv.org/abs/2601.17883
13. Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
   - https://doi.org/10.1162/IMAG.a.136
14. Wei H, Jafarian A, Zeidman P, et al. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020.
   - https://doi.org/10.1016/j.neuroimage.2020.116595
15. Vafaii H, Mandino F, Desrosiers-Gregoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-023-44363-z
16. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-64414-x
17. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
18. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
19. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
20. Hirschler L, et al. Region-specific drivers of cerebrospinal fluid mobility in the human brain. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
21. Dagum P, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
22. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023.
   - https://doi.org/10.1016/j.crmeth.2023.100520
23. Bosch C, Ackels T, Pacureanu A, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
24. MICrONS Consortium, Bae JA, Lee W-CA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
25. Attardo A, Fitzgerald JE, Schnitzer MJ. Impermanence of dendritic spines in live adult CA1 hippocampus. *Nature*. 2015.
   - https://doi.org/10.1038/nature14467
