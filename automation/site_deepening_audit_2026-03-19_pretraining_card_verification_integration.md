# Site Deepening Audit (2026-03-19, Pretraining Card / Verification Integration)

## 対象

- 主対象: `verification.md`
- 副対象: `wiki/baselines-prereg-and-model-cards.md`
- 副対象: `eeg_101.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイトは、EEG foundation model を過大読解しないための専用ページ `wiki/eeg-foundation-models.md` をすでに持っていました。
- しかし、`Pretraining Card` の規則が主にその一ページへ閉じており、`verification.md` と `wiki/baselines-prereg-and-model-cards.md` という共通運用ページには十分に昇格しておりませんでした。
- この不整合は技術・自然科学の観点で弱点です。なぜなら、foundation / self-supervised EEG の比較では
  - pretraining corpus の実体
  - downstream 側との overlap
  - channel / reference / sample-rate harmonization
  - adaptation regime
  - benchmark provenance
  - scale / efficiency
  が、結果の意味そのものを変えるからです。
- したがって `Pretraining Card` は周辺 Wiki の補助導線ではなく、Verification の共通 artifact として扱うべきでした。

## 根拠付き批判

### 1. 旧 site は foundation-model 固有の audit を共通検証規則へ十分に統合していませんでした

- 問題:
  - `wiki/eeg-foundation-models.md` では `Pretraining Card` を要求していましたが、`verification.md` の共通 card 群や `wiki/baselines-prereg-and-model-cards.md` の model-card 説明には、その位置づけが十分に出ていませんでした。
- 根拠:
  - Kostas et al. (2021) は、unseen datasets / hardware / subjects / tasks への transfer を BENDR の中心課題として扱いました。
  - Jiang et al. (2024) は LaBraM で高性能を示しつつも、electrode mismatch、unequal length、varied task design、low SNR を open challenge として明記しました。
  - Xiong et al. (2025) は EEG-FM-Bench で、standardized evaluation の欠如が cross-model comparison を unreliable にすると述べました。
- 批判:
  - これらは `large model + score` だけでは結果の意味が固定されないことを示します。
  - それにもかかわらず共通 verification rule に入っていないと、読者は foundation-model 結果を通常の model card だけで十分と誤読しやすくなります。

### 2. 旧 site は benchmark operation 側がすでに要求している disclosure を Verification 側で受け止め切れていませんでした

- 問題:
  - `verification.md` は多くの route card を要求していましたが、foundation-model comparison に固有の disclosure を card として持っていませんでした。
- 根拠:
  - EEG Challenge (2025) rules は、additional pretraining datasets の明記、used pretrained models の明記、fine-tuning 方法の明記を明示的に要求しています。
- 批判:
  - これは capability proof ではありませんが、comparability の最低条件についての運用上の一次資料です。
  - したがって、site rule もこれを benchmark-specific rule のままにせず、一般化した `Pretraining Card` として扱うのが妥当です。

### 3. 旧 site は `model won` と `adaptation / compute allocation won` の分離が共通ページ側で弱いままでした

- 問題:
  - 専用 Wiki では scale / efficiency や adaptation regime を書いていましたが、共通 model-card 説明ページではその差が十分に固定されていませんでした。
- 根拠:
  - Lee et al. (2025) は、large brainwave foundation models が conventional deep baselines を marginal にしか上回らず、LoRA で trainable parameters を大きく減らせることを示しました。
- 批判:
  - したがって、foundation-model の勝利は `architecture universalized` の勝利とは限らず、`fine-tuning strategy` や `parameter-efficient adaptation` の勝利かもしれません。
  - これを common model-card page 側で固定しないと、スコアの意味が大きくぶれます。

## 今回実行した変更

- `verification.md`
  - `page_highlights` と `known_points` に `Pretraining Card` を追加しました。
  - 新規節 `2026-03-19 addendum: attach a Pretraining Card to foundation / self-supervised EEG results` を追加しました。
  - `corpus identity / overlap audit`、`population / setup diversity`、`harmonization policy`、`adaptation regime`、`benchmark provenance`、`scale / efficiency`、`evaluation family / stop line` を required fields として明文化しました。
  - `Additional audit logs` に `Pretraining Card` を追加しました。
  - 参考文献を追加しました。
- `wiki/baselines-prereg-and-model-cards.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - `page_highlights` と `known_points` に foundation-model 固有の audit 要件を追加しました。
  - `2026-03-19 Addendum` を追加し、通常の model card と `Pretraining Card` の役割差を明記しました。
  - `When a normal model card is not enough` 節を追加しました。
  - checklist に `Pretraining Card` の確認項目を追加しました。
  - 参考文献を追加しました。
- `eeg_101.md`
  - `page_highlights` と `known_points` の foundation-model 説明を強化しました。
  - `wiki_links` に `Wiki: EEG foundation models and pretraining` を追加しました。
  - 新規 note-box `When a large pretrained EEG model looks like a general decoder` を追加し、entry page から `Pretraining Card` へ直行できるようにしました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・共通検証規則・監査導線の改稿で完結しています。

## 参考文献

1. Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Front Hum Neurosci*. 2021;15:653659.
   - https://doi.org/10.3389/fnhum.2021.653659
2. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR 2024*.
   - https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html
3. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML 2025 poster*.
   - https://openreview.net/forum?id=J5SbLoq7Uv
4. EEG Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
5. Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
