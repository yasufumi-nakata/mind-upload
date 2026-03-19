# Site Deepening Audit (2026-03-20, Astrocyte-State Front Door)

## 対象

- 主対象: `index.md`, `wbe_101.md`, `faq.md`, `verification.md`
- 補助対象: `glossary.md`, `summary_booklet.md`

## 今回の選定理由

- 2026-03-20 時点で、wiki 側では astrocyte ensemble と glial maintenance をかなり丁寧に分離できていました。
- その一方で、公開フロントドア側ではなお `glial / astrocyte support` がやや一般的な support background として読める余地が残っていました。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、2024-2026 の一次文献は astrocyte-state を少なくとも rodent の hippocampus / amygdala / cortex で `minutes-scale transmitter integration`、`recall`、`multiday stabilization`、`fear-state representation` に関わる変数として押し上げており、generic support の一語では粗すぎるからです。

## 根拠付き批判

### 1. 旧フロントドアは astrocyte-state を `metabolic support` に寄せすぎていました

- 問題:
  - `wbe_101.md` と `faq.md` は glia の重要性を否定していませんでした。
  - しかし front-door の表現はなお `glial metabolism` や `glial / astrocyte support` に寄り、近年の causal literature が示す state-variable 性を十分に前面化できていませんでした。
- 根拠:
  - Cahill et al. (2024) は局所 neurotransmitter 入力が minutes-scale の広域 cortical astrocyte network state として符号化されることを示しました。
  - Williamson et al. (2025) は learning-associated astrocyte ensembles が hippocampal memory recall を調節することを示しました。
  - Dewa et al. (2025) は astrocytic ensemble が emotional memory の multiday stabilization に関わることを示しました。
  - Bukalo et al. (2026) は basolateral amygdala astrocyte Ca2+ signalling が fear-memory retrieval / extinction representations を支えることを示しました。
- 批判:
  - 以上を踏まえると、front-door が astrocyte-state を単なる背景 support と読ませる構造は、現在の一次文献に対して粗すぎます。

### 2. ただし、この文献群を `human whole-brain readout` に昇格させるのも誤りです

- 問題:
  - astrocyte-state を前面化すると、逆向きの誤読、すなわち `glia も読めば memory content をかなり直接読める` という飛躍も生じえます。
- 根拠:
  - Cahill et al. (2024), Williamson et al. (2025), Dewa et al. (2025), Bukalo et al. (2026) はいずれも rodent・region-limited・task-bounded の causal literature です。
- 批判:
  - したがって site rule は二段階であるべきです。
  - `astrocyte-state is not generic support background` と同時に、`astrocyte-state evidence is still not direct human whole-brain memory readout` を front door で明示しなければなりません。

### 3. Verification 側では `何を最低限書くか` まで落とさないと運用上は抜けます

- 問題:
  - `verification.md` の maintenance-state error budget と latent-state table は glial importance を示していましたが、なお `network / ensemble state`、`reconsolidation`、`fear-state representation` までの提出要件が front-door wording では十分明確ではありませんでした。
- 批判:
  - 支持文献があっても submission rule に落ちなければ site operation 上は抜け穴です。
- 修正方針:
  - glial / astrocyte row を `astrocyte network / ensemble state` を明示する形へ更新し、rodent-to-human observability gap も同時に書くようにしました。

## 今回実行した変更

- `index.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - front matter に astrocyte-state を独立した known point として追加しました。
  - landing page に `If You Are Still Treating Astrocytes As Generic Support Background` note を追加しました。
- `wbe_101.md`
  - page highlight / known point を astrocyte-state に同期しました。
  - hidden-state の長文段落を、Suzuki / Cahill / Williamson / Dewa / Bukalo を使って `astrocyte-state is not just background` へ改稿しました。
  - hidden-state table の glia row を `Astrocyte / glial-state` として更新しました。
  - entry-point note box を追加しました。
- `faq.md`
  - long-term hidden-state bullet を astrocyte-state に更新しました。
  - Q2c の説明を、astrocyte-state の rodent causal evidence と human ceiling を同時に読める表現へ改稿しました。
  - 参考文献を追加しました。
- `verification.md`
  - page highlight / known point に astrocyte-state ceiling を追加しました。
  - maintenance-state error budget の glial row を `network / ensemble state` を含む形へ更新しました。
  - `astrocyte-state is not generic support background` note を追加しました。
  - latent-state table と practical rule を astrocyte-state に同期しました。
- `glossary.md`
  - `astrocyte-state` を語彙レベルで追加しました。
  - maintenance-state / support-state proxy の定義を astrocyte ensemble ceiling に合わせて更新しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成予定です。

## 外部依存で保留

- human same-subject, whole-brain astrocyte-state readout
  - 担当者: 実験系共同研究者 / ヒト高分解能計測系研究者
  - 前提条件: astrocyte network / ensemble state を人で直接または強く較正できる計測系
  - 完了条件: human longitudinal setting で astrocyte-state を比較可能にする公開 benchmark または causal calibration route が整備されること

## 参考文献

1. Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
   - https://doi.org/10.1038/s41586-024-07311-5
2. Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-024-08170-w
3. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
4. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
5. Suzuki A, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011.
   - https://doi.org/10.1016/j.cell.2011.02.018
