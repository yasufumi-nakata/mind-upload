# Site Deepening Audit (2026-03-25, EEG foundation-model shortcut-resistance bridge)

## 対象

- 主対象: `wiki/eeg-foundation-models.md`
- 副対象: `verification.md`
- 副対象: `eeg_101.md`

## 今回この箇所を選んだ理由

- 2026-03-25 JST 時点で、サイトは `EEG foundation models / pretraining` の読み方自体はすでに持っておりました。
- ただし、その規律はまだ主に
  - `corpus identity`
  - `harmonization`
  - `adaptation regime`
  - `benchmark provenance`
  - `scale / efficiency`
  に集中しており、`その transfer が target neural variable 由来なのか、identity / setup shortcut 由来なのか` を foundation-model 専用ページで十分に前景化しておりませんでした。
- これは技術・自然科学の観点で弱点です。なぜなら、large-scale pretraining や `adapting to any setup` という見出しは、読者に `shortcut-resistant neural representation が得られた` という過読を誘発しやすい一方、その飛躍は既存の `Specificity & Shortcut Card` 規律では止められるべきだからです。

## 根拠付き批判

### 1. 現行 page は `benchmark provenance` までは強いが、`shortcut-resistance` を独立 gate にしておりませんでした

- 観察:
  - `wiki/eeg-foundation-models.md` は source tier, challenge governance, split randomness, hidden grouping を丁寧に整理しておりました。
  - しかし `high transfer score` が `target neural variable` 由来なのか、`subject / site / device / reference / protocol` 由来なのかを foundation-model 文脈で独立 gate にしておりませんでした。
- なぜ問題か:
  - benchmark provenance が健全でも、representation 自体が shortcut-rich なら、`general transfer` を `neural invariance` と誤読できます。
  - 既存サイトは decode / biomarker ではこの問題を `Specificity & Shortcut Card` で止めているため、foundation-model だけ narrative で済ませるのは public-spec inconsistency です。

### 2. `any setup` と `shortcut-resistant representation` は同義ではありません

- 根拠:
  - El Ouahidi et al. (2025) `REVE` は arbitrary length / electrode arrangement を扱い、92 datasets・25,000 subjects・60,000+ hours という大規模 pretraining を提示しています。
  - しかしこれは `setup heterogeneity を処理できる` ことの証拠であり、`identity / setup shortcut を表現から切り離した` ことの証拠ではありません。
  - Lahiri et al. (2026) `PRISM` は narrow-source と diverse-source の pretrained checkpoints を比較し、linear probe と fine-tuning で優劣が入れ替わること、clinical mimicker task では diverse pretraining が有利になりうることを示しています。
  - Liu et al. (2026) は 12 open-source EEG foundation models と specialist baselines を 13 datasets で比較し、linear probing はしばしば不十分であり、scratch specialists も競争力を保ち、larger foundation models が自動では強くならないことを示しました。
- 批判:
  - したがって、`works with many setups` や `wins with little fine-tuning` という表現だけでは、representation が何を invariant にしたのかは分かりません。
  - foundation-model page には `setup adaptation` と `shortcut resistance` を分ける stop line が必要でした。

### 3. 既存の shortcut literature と接続しないと、pretraining page だけが site-wide rule より甘くなります

- 根拠:
  - Chaibub Neto et al. (2019) は repeated measures の扱い方しだいで identity confounding が入りうることを示しました。
  - Xu et al. (2020) は cross-dataset EEG decoding が acquisition environment に強く依存することを示しました。
  - Di et al. (2021) は resting-state EEG だけで time-robust individual identification が可能であることを示しました。
- 批判:
  - これらは foundation-model 専用論文ではありませんが、だからこそ重要です。
  - EEG foundation models も EEG signal から表現を学習している以上、identity / acquisition shortcut の系統から自由ではありません。
  - にもかかわらず foundation-model page が `Pretraining Card` だけで閉じると、読者は `pretraining を書けば shortcut 監査も済んだ` と誤解できます。

## 今回実行した変更

- `wiki/eeg-foundation-models.md`
  - `last_updated` を `2026-03-25` に更新しました。
  - front matter に `shortcut-resistant transfer` の停止線を追加しました。
  - `adapting to any setup is not yet shortcut-resistant transfer` note-box を新設しました。
  - `Liu et al. (2026)` を evidence-tier table に追加しました。
  - `The 8 gates` を `The 9 gates` に改め、`G6: shortcut-resistance / specificity bridge` を追加しました。
  - `Pretraining Card` に `Shortcut-resistance / Specificity Bridge` 行を追加しました。
  - operating rules に `any setup` を shortcut-resistant と同義に読まない site rule を追加しました。
- `verification.md`
  - Pretraining Card の導入文を更新し、`REVE` と `PRISM` / `Liu et al. (2026)` が示す再評価点を統合しました。
  - `shortcut-resistance / specificity bridge` 行を Pretraining Card に追加しました。
  - minimum operating rules に `Specificity & Shortcut Card` への bridge を必須化しました。
- `eeg_101.md`
  - foundation-model note を更新し、`works across setups` と `stopped reading shortcuts` を分けました。
  - references に `REVE` と `Liu et al. (2026)` を追加しました。

## 修正しないもの

- 哲学・法学・personhood の議論は今回の対象に含めません。
- `issue.md` の整理はユーザー前提として扱い、今回は再読しておりません。
- benchmark そのものの rerun や external reproduction は今回のセッション範囲外です。

## 外部依存で保留

- なし
  - 今回の作業は、公開文章の改稿・wiki export 同期・検証・push までこのリポジトリ内で完結できます。

## 参考文献

1. El Ouahidi Y, Lys J, Thölke P, Farrugia N, Pasdeloup B, Gripon V, Jerbi K, Lioi G. REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. *arXiv*. 2025.
   - https://arxiv.org/abs/2510.21585
2. Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
   - https://arxiv.org/abs/2603.02268
3. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
   - https://arxiv.org/abs/2601.17883
4. Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019;2:99.
   - https://doi.org/10.1038/s41746-019-0178-x
5. Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. *Frontiers in Human Neuroscience*. 2020;14:103.
   - https://doi.org/10.3389/fnhum.2020.00103
6. Di Y, An X, Zhong W, Liu S, Ming D. The time-robustness analysis of individual identification based on resting-state EEG. *Frontiers in Human Neuroscience*. 2021;15:672946.
   - https://doi.org/10.3389/fnhum.2021.672946
7. Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Frontiers in Human Neuroscience*. 2021;15:653659.
   - https://doi.org/10.3389/fnhum.2021.653659
8. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR*. 2024.
   - https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html
9. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML 2025 poster*.
   - https://openreview.net/forum?id=J5SbLoq7Uv
10. EEG Challenge (2025). Rules / Submission / Leaderboard.
   - https://eeg2025.github.io/rules/
   - https://eeg2025.github.io/submission/
   - https://eeg2025.github.io/leaderboard/
