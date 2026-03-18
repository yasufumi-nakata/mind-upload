# Site Deepening Audit (2026-03-18, Connectome Progress Must Be Split Into Evidence Classes)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`connectome-complete ≠ emulation-complete` という結論自体は既に正しく固定できておりました。
- しかし、読者が最も影響を受けやすい `connectome progress` の読み方には、なお 1 つの圧縮が残っておりました。具体的には、`whole-brain wiring atlas`、`same-brain local structure-function scaffold`、`connectome-constrained conditional predictor`、`identifiability / degeneracy audit` が、ひと続きの「connectome がかなり効いてきた」という話に近く読める構造でした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、どの一次文献が `何を直接前進させたか` を分離しない限り、`配線が見えた`、`局所で機能とつながった`、`活動予測が当たった`、`内部状態がほぼ決まった` が混線し、WBE に対する evidence ceiling が実際より高く読まれるからです。

## 根拠付き批判

### 1. 旧ページは flagship connectome papers を 1 本の進歩物語へ圧縮しすぎていました

- 問題:
  - `wiki/connectome-is-not-enough.md` では、Dorkenwald / MICrONS / Lappalainen を並べて「大きな前進」と述べていました。
  - しかし、これでは `atlas`、`same-brain scaffold`、`conditional predictor` の違いが本文上で十分に固定されませんでした。
- 根拠:
  - Dorkenwald et al. (2024) は、約 13 万ニューロン・約 5×10^7 chemical synapses を含む adult fly 全脳 wiring diagram を示しました。
  - MICrONS Consortium et al. (2025) は、awake mouse の visual cortex における約 75,000 neurons の dense calcium imaging を、20 万超の cells と 5 億 synapses を含む EM reconstruction に同一個体で co-register しました。
  - Lappalainen et al. (2024) は、connectome-constrained かつ task-optimized な fly visual-system model により単一ニューロン解像度の活動予測を示しました。
- 批判:
  - したがって、これらを 1 本の「connectome が十分に近づいた」証拠列にするのは強すぎます。
  - 少なくとも `構造 atlas`、`局所 structure-function scaffold`、`条件付き activity predictor` は site-wide rule として分けるべきでした。

### 2. 旧ページは `activity prediction succeeded` と `state uniqueness improved` を十分に分けていませんでした

- 問題:
  - Lappalainen et al. (2024) の位置づけは概ね正しかったものの、`conditional model / hypothesis engine` と `internal-state recovery` の境界が本文上ではまだ短く済まされておりました。
- 根拠:
  - Lappalainen et al. (2024) は、connectome が free parameters を大きく減らし、single-neuron-scale prediction を可能にすることを示しました。
  - しかし同論文は、electrical synapses、nonlinear chemical synapses、neuromodulation を model 外へ明示的に残しております。
- 批判:
  - よって、`よく当たる connectome-constrained model` は `missing state がほぼ埋まった` ことを意味しません。
  - site rule では、これを `conditional predictor / hypothesis engine` として固定し、L2/L3 completeness へ自動昇格させない必要がありました。

### 3. 旧ページは `connectome constrains dynamics` と `connectome uniquely determines dynamics` の差をもっと前に出すべきでした

- 問題:
  - `degeneracy` 節自体はありましたが、前段の flagship connectome section と十分に一体化しておらず、読者が後から読む補足に見える余地がありました。
- 根拠:
  - Beiran & Litwin-Kumar (2025) は、student / teacher networks が同じ synaptic weights を共有していても、biophysical parameters が異なれば recurrent dynamics は大きくずれうることを示しました。
  - 同時に、少数ニューロンの activity recording がこの degeneracy をかなり減らせることも示しました。
- 批判:
  - したがって、connectome は `無意味` でも `ほぼ十分` でもございません。
  - 正しい読み方は、`solution space を狭めるが unique にはしない。recordings / perturbations / abstention rules が別に要る` です。この点を flagship papers の表の中で見えるようにすべきでした。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - front matter の `page_highlights` と `known_points` を更新し、flagship connectome papers を 4 つの evidence class に分けて読む site rule を前面化
  - `connectome-progress` 節の本文を全面改稿し、Dorkenwald / MICrONS / Lappalainen / Beiran-Litwin-Kumar を 1 本の進歩物語ではなく、別々の不確実性削減として整理
  - `Replace here` の未完了 note を削除
  - 新しい比較 table を追加し、`evidence class` / `what it advances` / `what it still does not support` / `site reading` を明示
  - `connectome progress` を読むときは必ず evidence class を先に答える、という operational rule を追加
- `wbe_101.md`
  - 入口の比較 table を `Structural connectomics / local calibration / connectome-constrained modeling` へ更新
  - connectome progress を 1 つの claim level に潰さない short note を追加
  - Lappalainen et al. (2024) と Beiran & Litwin-Kumar (2025) を references に追加

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と内部監査記録の改稿で完結しております。

## 参考文献

1. Dorkenwald S, Matsliah A, Sterling AR, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024;634:124-138.
   - https://doi.org/10.1038/s41586-024-07558-y
2. MICrONS Consortium. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640:435-447.
   - https://doi.org/10.1038/s41586-025-08790-w
3. Lappalainen JK, Tschopp FD, Prakhya S, et al. Connectome-constrained networks predict neural activity across the fly visual system. *Nature*. 2024;634:1132-1140.
   - https://doi.org/10.1038/s41586-024-07939-3
4. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574.
   - https://doi.org/10.1038/s41593-025-02080-4
