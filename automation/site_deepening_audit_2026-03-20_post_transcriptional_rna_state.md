# Site Deepening Audit (2026-03-20, Post-Transcriptional RNA-State)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 入口・運用反映: `wbe_101.md`, `faq.md`, `verification.md`, `glossary.md`

## 今回の選定理由

- 既存サイトは `connectome ≠ state-complete`、`cell type ≠ excitability-complete`、`transcription/chromatin ≠ cell identity`、`proteostasis ≠ cargo delivery` をかなり丁寧に分離できていました。
- しかしその一方で、`gene-level transcript abundance が近い` ことと、`現在の RNA processing / RNA fate controller が近い` ことが、まだ十分に分離されていませんでした。
- このままでは読者が `DEG` や `transcript count` を見ただけで、isoform choice, m6A-dependent translation / degradation, RNA-editing ratio までほぼ固定できると誤読しやすく、技術・自然科学の観点ではここが未補強の弱点でした。

## 主要な批判点

### 1. 旧サイトは `transcription / chromatin` と `post-transcriptional RNA-state` を十分に分けていませんでした

- 問題:
  - 既存本文は allocation eligibility や late stabilization program を `transcription / chromatin state` としてかなりうまく切り出していました。
  - しかし、同じ gene-level abundance でも、splice isoform, m6A reader engagement, RNA-editing ratio が違えば、最終的な receptor composition, plasticity route, memory-relevant stabilization はまだ変わりえます。
- 根拠:
  - Wang et al. (2015) は neuron-specific LSD1 splice isoform が memory formation を制御することを示しました。
  - Dai et al. (2019) は presynaptic neurexin alternative splicing が postsynaptic NMDA / AMPA response と contextual memory を変えることを示しました。
  - Shi et al. (2018) は YTHDF1 を介する m6A 読み出しが hippocampus-dependent learning and memory を促進することを示しました。
- 批判:
  - したがって、`current transcriptional program` を立てただけではまだ不十分であり、`post-transcriptional RNA-state` を独立 class として監査しなければ、site の hidden-state 論は粗すぎました。

### 2. 旧サイトは `gene-level abundance` を安全側で demote する規則がまだ弱かったです

- 問題:
  - transcriptomic evidence を `identity prior` や `time-stamped clue` に格下げする規則は整備されていました。
  - しかしその規則だけでは、読者が `gene-level abundance is not enough` ではなく `transcriptomics in general is weak` とだけ読んでしまい、どこで情報が失われるかが曖昧でした。
- 根拠:
  - Li et al. (2025) は YTHDF2-mediated m6A mRNA degradation を抑制すると protein synthesis と hippocampus-dependent memory が増強することを示しました。
  - Peterson et al. (2025) は ADAR2-mediated GluA2 RNA editing が homeostatic synaptic plasticity に寄与することを示しました。
- 批判:
  - 問題は `RNA data が弱い` ことではなく、`gene-level abundance では RNA processing / RNA fate layer を回収できない` ことです。この差を本文前面で明示しない限り、claim ceiling の説明として不十分でした。

### 3. human observability ceiling に RNA 後成的状態の不可視性が十分反映されていませんでした

- 問題:
  - human 側の observability ladder は、MRSI, sodium MRI, thermometry, myelin proxy, CSF proxy をかなり丁寧に区別できていました。
  - しかし `current post-transcriptional RNA-state` については、どの程度まで人で見えていないかが本文 frontdoor で十分に明示されていませんでした。
- 根拠:
  - Joglekar et al. (2024) は mouse / human brain における specialized splicing pattern を long-read single-cell atlas として示しました。
- 批判:
  - これは重要な前進ですが、あくまで atlas-building / ex vivo 系であり、whole-brain in vivo human route ではありません。
  - したがって、human observability の節で `current post-transcriptional RNA-state still lacks a comparable in vivo whole-brain human route` と書かなければ、proxy ladder は未完成でした。

### 4. verification 側で監査列になっていなければ、実務上は見落とされます

- 問題:
  - hidden state として本文に書いても、`verification.md` の latent-state error budget や integrity gate に入っていなければ、投稿物審査では自動的に見落とされやすい状態のままです。
- 批判:
  - サイト運用として有効な state class とは、説明文に存在するだけでなく、`何を提出しなければ latent とみなすか` が書かれているものに限られます。
- 修正:
  - verification 側に `post-transcriptional RNA-state` の error budget row, integrity-gate row, addendum を追加し、gene-level abundance 単独では不足と明示しました。

## 今回実行した変更

- `wbe_101.md`
  - hidden-state 導入文に post-transcriptional RNA-state 文献を追加しました。
  - hidden-state table と human observability ceiling に RNA 後成的状態を反映しました。
  - 参考文献を追加しました。
- `faq.md`
  - `connectome and cell type are not enough` の主説明に RNA 後成的状態を追加しました。
  - human ceiling の節で long-read atlas と in vivo whole-brain route の差を明示しました。
  - 参考文献を追加しました。
- `verification.md`
  - page highlights / known points を更新しました。
  - latent-state error budget, maintenance-state error budget, state variable integrity gate に `post-transcriptional RNA-state` を追加しました。
  - gene-level abundance だけでは足りないという addendum を追加しました。
  - 参考文献を追加しました。
- `glossary.md`
  - `Maintenance-state` の定義を更新しました。
  - `Post-transcriptional RNA-state` 項目を追加済みの本文に合わせて reference trail を補強しました。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - maintenance-state count を 15 へ更新しました。
  - `Post-transcriptional RNA-state is not the same as gene-level transcript abundance` 節を新設しました。
  - human observability ceiling, dangerous misreading, practical rules, minimum submissions に RNA 後成的状態を反映しました。
  - 参考文献を追加しました。
- `wiki/connectome-is-not-enough.md`
  - state-class count を 13 + 1 wall に更新しました。
  - state-class table に `Post-transcriptional RNA-state` を追加しました。
  - `Why are these 13 classes easy to skip` に新節を追加し、gene-level abundance からの過剰補完を禁止しました。
  - augmentation/ablation と site rules を更新しました。
  - 参考文献を追加しました。

## 外部依存で保留

- human in vivo での whole-brain post-transcriptional RNA-state ground truth
  - 担当者: 実験系共同研究者 / 高分解能 RNA 計測系研究者
  - 前提条件: living human brain において isoform choice, m6A-dependent translation / degradation, RNA-editing ratio を直接もしくは強く外部較正して longitudinal に比較できる計測系
  - 完了条件: human longitudinal setting で `current post-transcriptional RNA-state` を whole-brain あるいは少なくとも広域比較可能にする公開 benchmark または因果介入系が整備されること

## 参考文献

1. Wang J, Telese F, Tan Y, et al. LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. *Nature Neuroscience*. 2015;18(9):1256-1264.
   - https://doi.org/10.1038/nn.4069
2. Dai J, Aoto J, Südhof TC. Alternative splicing of presynaptic neurexins differentially controls postsynaptic NMDA and AMPA receptor responses. *Neuron*. 2019;102(5):993-1008.e5.
   - https://doi.org/10.1016/j.neuron.2019.03.032
3. Shi H, Zhang X, Weng Y-L, et al. m6A facilitates hippocampus-dependent learning and memory through YTHDF1. *Nature*. 2018;563(7730):249-253.
   - https://doi.org/10.1038/s41586-018-0666-1
4. Li Y, Zhu M, Li X, et al. Enhanced Protein Synthesis and Hippocampus-Dependent Memory via Inhibition of YTHDF2-Mediated m6A mRNA Degradation. *Advanced Science*. 2025;12(34):e14926.
   - https://doi.org/10.1002/advs.202514926
5. Peterson LN, Kasper JM, Allgaier JA, et al. ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. *Science Signaling*. 2025;18(886):eadr1442.
   - https://doi.org/10.1126/scisignal.adr1442
6. Joglekar A, Prjibelski A, Mahfouz A, et al. Single-cell long-read sequencing-based mapping reveals specialized splicing patterns in developing and adult mouse and human brain. *Nature Neuroscience*. 2024;27(6):1073-1088.
   - https://doi.org/10.1038/s41593-024-01616-4
