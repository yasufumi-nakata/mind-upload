# Site Deepening Audit (2026-03-28, state-trait fingerprint-object / regime split)

## 対象

- 主対象: `wiki/state-trait-and-drift.md`
- 同期対象:
  - `github-wiki-export/state-trait-and-drift.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1126/sciadv.abj0751`
- `https://doi.org/10.3389/fnhum.2021.672946`
- `https://doi.org/10.1016/j.neuroimage.2023.120260`
- `https://doi.org/10.1038/s41598-025-34509-y`

## 今回この箇所を選んだ理由

- `wiki/state-trait-and-drift.md` はすでに
  - `same-day success != trait evidence`
  - `adaptive rescue != fixed-decoder durability`
  - `participant-specific longitudinal success != generic transfer`
  をかなり明確に切り分けていました。
- しかしなお、
  - `fingerprint succeeded`
  - `person identification stayed high`
  - `trait-like signature remained`
  を、そのまま
  - `one universal backbone object was measured`
  - `state-invariant trait was found`
  と読み替える余地が残っていました。
- これは技術・自然科学の観点で弱点です。現在の一次文献は、identifiability の担い手が
  - timescale
  - feature family
  - aperiodic / nonlinear component
  - state regime
  によって変わりうることを示しているからです。

## 根拠付き批判

### 1. functional fingerprint は 1 つの時間窓・1 つの network ではありません

- [Van De Ville et al. (2021)](https://doi.org/10.1126/sciadv.abj0751) は、brain fingerprint が長い window で最適化される一方、短い window にも highly identifiable snapshots があり、寄与する network も timescale ごとに変わることを示しました。

批判:

- したがって `functional fingerprint was stable` を、そのまま `one stable trait object` と読むのは弱いです。
- 少なくとも `which temporal window` と `which network family` が identifiability を担ったかを出さないと、trait claim の中身が空欄のまま残ります。

### 2. EEG individuality も feature family を固定しなければ意味が粗すぎます

- [Di et al. (2021)](https://doi.org/10.3389/fnhum.2021.672946) は resting-state EEG の individual identification が複数 run・少なくとも 2 週間以上の間隔でも高精度に維持されうることを示しました。
- しかしこれは `resting-state EEG identity exists` を示すのであって、どの feature family でも同じ backbone が読めることを示したわけではありません。

批判:

- `EEG identity was robust` だけでは trait claim はまだ粗いです。
- power / coherence / other feature family のどれが backbone 候補として働いたかを分けずに `trait` と書くのは過読です。

### 3. subject-specific information は stationary correlation 以外でも担われます

- [Sorrentino et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120260) は、source-reconstructed MEG で、subject differentiation が fast, intermittent な avalanche dynamics と non-linear component に強く支えられ、stationary correlation structure より識別力が高いことを示しました。

批判:

- よって `fingerprint = static FC-like backbone` と固定するのも弱いです。
- 非線形・非定常イベントが識別を担うなら、paper が測ったものは `stable trait` ではなく `intermittent identifiable event family` かもしれません。

### 4. strong individuality は nominal label generalization と両立しません

- [Kyllönen et al. (2026)](https://doi.org/10.1038/s41598-025-34509-y) は、2 site・2 night の sleep EEG で trait-like individual signatures が強く、same-individual training/test では高精度だった一方、across-participant insomnia classification は chance に落ちることを示しました。
- 同論文は high-frequency cortical activity が identity signal を強く担うことも示しました。

批判:

- したがって `trait-like signature remained` を `target phenomenon was captured` と読むのは危険です。
- stable individuality は、state-invariant backbone を示すより先に、`individual baseline dominates the task label` を示している可能性があります。

## 今回実行した変更

- `wiki/state-trait-and-drift.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` に、fingerprint carrier と state regime の切り分けを追加しました。
  - 新しい note-box `2026-03-28 addendum: fingerprint success is not yet one backbone object` を追加しました。
  - `Trait-like backbone sits above unit-level immutability` 節を増補し、
    - timescale dependence
    - feature-family dependence
    - nonlinear / aperiodic carrier
    - same-regime individuality versus cross-regime persistence
    を分離しました。
  - `Minimum submission` に `backbone / fingerprint object` 行を追加しました。
  - `Common misreadings` に `high person-identification accuracy = one state-invariant trait` を止める行を追加しました。
  - `Operating rules` を更新し、trait claim では fingerprint object / timescale / state-regime disclosure を要求する形へ改めました。
  - references を追加しました。

## 今回止めた誤読

- `person-identification succeeded = one universal trait object was measured`
- `functional fingerprint = one fixed FC backbone`
- `EEG individuality persisted = state-invariant trait survived`
- `same-individual success = target phenomenon generalized`
- `trait-like signature = label-specific signal`

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、export 同期、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Van De Ville D, Amico E, Abbas K, et al. When makes you unique: Temporality of the human brain fingerprint. *Science Advances*. 2021;7:eabj0751.
   - https://doi.org/10.1126/sciadv.abj0751
2. Di X, Guo Z, Meng X, et al. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. *Frontiers in Human Neuroscience*. 2021;15:672946.
   - https://doi.org/10.3389/fnhum.2021.672946
3. Sorrentino P, Troisi Lopez E, Romano A, et al. Brain fingerprint is based on the aperiodic, scale-free, neuronal activity. *NeuroImage*. 2023;277:120260.
   - https://doi.org/10.1016/j.neuroimage.2023.120260
4. Kyllönen M, Cox R, Makkonen T, et al. Trait-like individual signatures dominate sleep EEG over insomnia-specific features. *Scientific Reports*. 2026;16:4408.
   - https://doi.org/10.1038/s41598-025-34509-y
