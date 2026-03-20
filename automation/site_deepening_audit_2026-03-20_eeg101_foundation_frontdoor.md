# Site Deepening Audit (2026-03-20, EEG 101 Foundation-Model Front Door)

## 対象

- 主対象: `eeg_101.md`
- 副対象: `summary_booklet.md`

## 今回の選定理由

- 2026-03-20 時点で，`verification.md` と `wiki/eeg-foundation-models.md` は，EEG foundation model の読み方をかなり厳密に持っておりました。
- その一方で，公開 primer である `eeg_101.md` はなお，`large pretrained EEG model` を安全に読むための front-door wording が，Verification 側より一段弱い状態でした。
- とくに弱かったのは，`benchmark provenance` が単なる提出様式ではなく，公式 competition の運営変更と postmortem によって leaderboard の意味そのものを変える，という点です。
- 初学者はまず primer を読みます。したがって，ここで止めないと，後段の厳密な Pretraining Card を読む前に `high leaderboard rank = portable cross-subject robustness solved` と過大読みにしやすくなります。

## 根拠付き批判

### 1. 旧 `eeg_101.md` は foundation-model caution を持っていましたが，`score interpretation changes when benchmark operations change` までは front door で言い切れていませんでした

- 問題:
  - 旧本文は BENDR, LaBraM, Lee et al. を使って，large EEG models の score-only reading を止めていました。
  - しかし，公式 benchmark の運営ページ・submission rule・leaderboard postmortem までを，一級の evidence として front door に統合していませんでした。
- 根拠:
  - EEG Challenge 2025 公式ホームページは，challenge paper が execution-phase changes に対してすでに outdated だと明記しています。
  - 公式 submission page は `inference-only code competition` を明記しています。
  - 公式 rules page は，extra pretraining datasets，pretrained checkpoints，fine-tuning method の開示と，single-GPU 20 GB inference budget を要求しています。
  - 公式 leaderboard は，Challenge 2 で samples を randomize していなかったため contiguous trials から same-subject structure を exploit できたと organizers 自身が開示し，最終的に Challenge 1 / 2 を別 award にしました。
- 批判:
  - 以上を踏まえると，benchmark provenance は単なる事務的 metadata ではありません。
  - それ自体が，score の意味を変える evidence-bearing condition です。
  - これを primer front door に書かないのは，2025-2026 の一次・公式ソースに対して弱すぎました。

### 2. 旧 primer は `large model may not transfer as much as the headline suggests` までは書けていましたが，`cross-benchmark inconsistency` を十分に前面化していませんでした

- 問題:
  - 旧 note box は，BENDR, LaBraM, Lee et al. によって，foundation-model headline の overread をかなり止めていました。
  - しかし，`benchmark inconsistency itself changes model ranking` という newer source の論点が未統合でした。
- 根拠:
  - Lee et al. (2025) は，state-of-the-art LBMs が従来 deep baselines に対して marginal gain しか示さず，parameter efficiency も別問題だと示しました。
  - EEG-FM-Bench (2025) は，inconsistent protocols が cross-model comparison を unreliable にすると明記しています。
  - PRISM (2026) は，EEG-Bench と EEG-FM-Bench の systematic inconsistency により，identical datasets でも model ranking が最大 24 pp 反転しうると報告しました。
- 批判:
  - したがって，foundation-model の claim ceiling は `model architecture` や `pretraining scale` だけでは決まりません。
  - `which benchmark, which split, which checkpoint, which normalization, which adaptation regime` まで含めて初めて比較可能です。
  - ここを primer で front-load しないと，読者は後から出てくる Pretraining Card を補足資料と誤認しやすくなります。

### 3. `challenge paper` と `current benchmark operations` を分ける rule も primer で必要でした

- 問題:
  - 初学者は arXiv paper を見て benchmark の current rule まで分かったつもりになりやすいです。
  - しかし，EEG Challenge 2025 公式ホームページ自身が，paper は recent changes を反映していないと述べています。
- 批判:
  - 技術・自然科学の front door では，`paper` と `current operations` を別物として読む規則を primer 側で明示しなければなりません。
  - でないと，challenge proposal を benchmark ground truth のように扱う読みが残ります。

## 今回実行した変更

- `eeg_101.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - `page_highlights` と `known_points` に，official benchmark operations / postmortem が foundation-model score の解釈を変えるという site rule を追加しました。
  - `When a large pretrained EEG model looks like a general decoder` note を改稿し，BENDR / LaBraM / Lee / EEG-FM-Bench / PRISM まで通して，score-only reading を止める表現へ更新しました。
  - 新しい note box `Benchmark operations are part of the result, not administrative detail` を追加しました。
  - 公式 homepage / rules / submission / leaderboard と，関連文献を references 側へ追加しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成予定です。

## 外部依存で保留

- なし
  - 今回の変更は，公開本文・参考文献・冊子再生成で完結します。

## 参考文献

1. Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Front Hum Neurosci*. 2021;15:653659.
   - https://doi.org/10.3389/fnhum.2021.653659
2. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR*. 2024.
   - https://proceedings.iclr.cc/paper_files/paper/2024/file/47393e8594c82ce8fd83adc672cf9872-Paper-Conference.pdf
3. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML / PMLR*. 2025.
   - https://proceedings.mlr.press/v267/lee25a.html
4. Aristimunha B, Truong D, Guetschel P, et al. EEG Foundation Challenge: From Cross-Task to Cross-Subject EEG Decoding. *NeurIPS Competition Track*. 2025.
   - https://arxiv.org/abs/2506.19141
5. EEG Challenge (2025). Official homepage.
   - https://eeg2025.github.io/
6. EEG Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
7. EEG Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
8. EEG Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
9. Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
10. Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
    - https://arxiv.org/abs/2603.02268
