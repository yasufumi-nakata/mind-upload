# 2026-03-26 サイト深掘り監査: literature pages に残っていた brain-to-text の coarse bucket を route split へ補正

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `research_harvest_50.md`
- 補助対象: `wiki/paper-source-types-and-evidence-status.md`

## 今回の選定理由

- 2026-03-26 JST 時点で、`verification.md` と `perspective.md` にはすでに `Neural Contribution Card` が入り、language-facing papers を
  - `within-subject semantic reconstruction`
  - `fixed-segment retrieval`
  - `known-onset word decoding`
  - `prompt-conditioned generation`
  - `communication subsystem`
  の別 route として読む規則が導入されておりました。
- しかし literature front door 側では、なお `brain-to-text` や `non-invasive language decode` が比較的広い一塊として読める構造が残っておりました。
- これは技術・自然科学の観点で弱点です。なぜなら、一次文献が押し上げているのは「脳から言語っぽい出力が出た」という一個の能力ではなく、`timing / segmentation regime`、`prior scaffold / prompt budget`、`brain-minus-prior baseline`、`subject route / cooperation / adaptation burden` が違う複数の route だからです。

## 根拠付き批判

### 1. `brain-to-text` を一つの evidence bucket にすると、route の違いが消えます

- 問題:
  - `mind_uploading_papers.md` は技術導線をかなり改善済みでしたが、language-facing papers だけは front door でなお一括りに近く、`semantic reconstruction`、`segment retrieval`、`known-onset decoding`、`prompt-conditioned generation` の差が十分には見えませんでした。
- 根拠:
  - [Tang et al. (2023)](https://doi.org/10.1038/s41593-023-01304-9) は `within-subject fMRI semantic reconstruction` であり、被験者協力が route 条件です。
  - [Défossez et al. (2023)](https://doi.org/10.1038/s42256-023-00714-5) は `3-second speech-segment identification` であり、abstract でも lexical / contextual semantic representation dependence が強調されています。
  - [d'Ascoli et al. (2025)](https://doi.org/10.1038/s41467-025-65499-0) は 723 人・500 万語規模の `known-onset word decoding` ですが、MEG > EEG、reading > listening、training data と test-time averaging の効果を明示しており、protocol asymmetry が結果の一部です。
  - [Ye et al. (2025)](https://doi.org/10.1038/s42003-025-07731-7) は `prompt-conditioned generation` であり、prompt length と LLM scaffold を切り離せません。
- 批判:
  - したがって `brain-to-text` を generic label のまま front door に置くと、読者は timing / scaffold の差を見落とし、`fluent output = same class of evidence` と誤読しやすくなります。

### 2. invasive speech papers も `one frontier` ではありません

- 問題:
  - 旧 front door は invasive speech を主に streaming / low-latency communication として読める構造でした。
  - しかし 2025 literature では、`real-time communication subsystem` と `cross-subject transfer initialization` が別の改善軸として現れています。
- 根拠:
  - [Willett et al. (2023)](https://doi.org/10.1038/s41586-023-06377-x), [Littlejohn et al. (2025)](https://doi.org/10.1038/s41593-025-01905-6), [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は streaming communication, brain-to-voice, low-latency synthesis を押し上げます。
  - [Singh et al. (2025)](https://doi.org/10.1038/s41467-025-63825-0) は distributed sEEG を用いた phoneme decoding と cross-subject transfer learning により、variable coverage 下での decoder initialization を押し上げます。
- 批判:
  - したがって invasive side でも、`communication performance` と `transfer-ready latent manifold` は分けて読まないと、generalizable prosthesis の language がそのまま free conversation や zero-recalibration に昇格しやすくなります。

### 3. evidence-class guide 側で coarse bucket が残ると、front door 修正が逆流します

- 問題:
  - `wiki/paper-source-types-and-evidence-status.md` は evidence class の辞書ですが、ここが `task-limited system demonstration` を広く書きすぎると、reader は public page の stop line を再び一般化してしまいます。
- 根拠:
  - Tang / Défossez / d'Ascoli / Ye / Singh / Willett / Littlejohn / Wairagkar はすべて `task-limited` ではある一方、constraint される inferential object が同じではありません。
- 批判:
  - したがって evidence-class guide にも `language-facing demos need a Neural Contribution Card` を入れ、front door と辞書ページの規律を一致させる必要がありました。

## 今回実行した変更

### 1. `mind_uploading_papers.md`

- front matter の `page_highlights` に、language-facing papers を one bucket にしない規則を追加
- `2026-03 Literature audit: Priority route for technology and natural sciences` の language row を改稿
  - `Tang / Défossez / d'Ascoli / Ye` を一行に揃えつつ、何が別 route かを本文で固定
  - next page を `Verification: Neural Contribution Card` へ接続
- invasive speech row に [Singh et al. (2025)](https://doi.org/10.1038/s41467-025-63825-0) を追加し、`communication subsystem` と `transfer initialization` を区別
- 新しい note box `Read language-facing papers only after a Neural Contribution Card` を追加
  - timing / segmentation regime
  - prior scaffold / prompt budget
  - brain-minus-prior baseline
  - subject route / cooperation / adaptation burden
  を front door 側で可視化
- `2025-2026 technical-only shortlist` に `Language-decode neural-contribution split` を追加
- `task-limited system demonstration` の evidence-class table を更新し、Tang / Défossez / d'Ascoli / Ye / Singh / Willett / Littlejohn / Wairagkar を同一証拠とみなさない説明へ修正
- quick guide の `I want to see brain-to-text / language decode` と `I want to see invasive closed loop communication` を更新

### 2. `research_harvest_50.md`

- U13 `Mimic separation` の technical reading を更新
  - traction bullet を `distinct language routes` へ改稿
  - representative references を published primary literature 中心へ更新
  - note box を追加し、Tang / Défossez / d'Ascoli / Ye / Willett / Littlejohn / Wairagkar を `same paper family` と読まない規則を明示
  - unresolved に `timing regime / prompt budget / candidate-bank disclosure` の未標準化を追記

### 3. `wiki/paper-source-types-and-evidence-status.md`

- `last_updated` を `2026-03-26` に更新
- `page_highlights` / `known_points` に language-facing demo の route split を追加
- `task-limited system demonstration` row を更新し、language route の coarse reading を抑制
- new note box `Language-facing demos need one more split` を追加し、`Verification: Neural Contribution Card` への導線を追加

## 外部依存で保留

- なし
  - 今回の変更は公開本文の再構成と参考導線の更新で完結しております。

## 参考文献

1. Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nature Neuroscience*. 2023.
   - https://doi.org/10.1038/s41593-023-01304-9
2. Défossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. *Nature Machine Intelligence*. 2023.
   - https://doi.org/10.1038/s42256-023-00714-5
3. d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-65499-0
4. Ye Z, Ai Q, Liu Y, de Rijke M, Zhang M, Lioma C, Ruotsalo T. Generative language reconstruction from brain recordings. *Communications Biology*. 2025.
   - https://doi.org/10.1038/s42003-025-07731-7
5. Willett FR, Avansino DT, Hochberg LR, Henderson JM, Shenoy KV. High-performance brain-to-text communication via handwriting. *Nature*. 2023.
   - https://doi.org/10.1038/s41586-023-06377-x
6. Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01905-6
7. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
8. Singh A, Thomas T, Li J, Hickok G, Pitkow X, Tandon N. Transfer learning via distributed brain recordings enables reliable speech decoding. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-63825-0
