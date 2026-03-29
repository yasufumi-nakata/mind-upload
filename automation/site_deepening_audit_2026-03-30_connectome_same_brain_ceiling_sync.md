# Site Deepening Audit (2026-03-30, connectome same-brain ceiling sync)

## 対象

- 主対象:
  - `wiki/connectome-is-not-enough.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学
  - 法学
  - 制度論

## web確認対象

- `https://doi.org/10.1038/s41467-022-30199-6`
- `https://doi.org/10.1038/s41586-025-08790-w`
- `https://doi.org/10.1038/s41586-025-08840-3`
- `https://doi.org/10.1038/s41586-025-08805-6`
- `https://doi.org/10.1038/s41586-020-03134-2`
- `https://doi.org/10.1038/s41467-022-33565-6`
- `https://doi.org/10.1038/s41467-024-53901-2`
- `https://doi.org/10.1038/s41593-025-02080-4`

## 今回この箇所を選んだ理由

- 2026-03-30 時点で site-wide rule は、measurement-stack / perspective / WBE 101 側では `same-brain functional connectomics` をかなり厳密に止められていました。
- ただし `wiki/connectome-is-not-enough.md` には、`same-brain local digital-twin scaffold` という、現行 ceiling より強く読める表現がまだ残っておりました。
- これは技術・自然科学の観点で危険でございます。`same-brain bridge`、`predicted transcriptomic label`、`current synaptic state`、`validated conditional predictor`、`unique local dynamics` は同じ主張ではないからでございます。

## 主要結論

- `wiki/connectome-is-not-enough.md` の旧 wording は、2026-03-30 時点の一次文献に対してまだ強すぎました。
- 一次文献が今支えているのは、少なくとも
  - `sequential same-brain bridge`
  - `morphology-linked label transfer`
  - `structure-function correspondence`
  - `task-bounded conditional prediction`
  まででございます。
- よって site rule 上の safe ceiling は
  - `sequential same-brain local scaffold`
  - `task-bounded conditional predictor`
  に止めるべきであり、
  - `direct transcriptomic truth`
  - `current synaptic-state readout`
  - `unique local twin`
  - `whole-brain state-complete template`
  へは自動昇格させてはなりません。

## 根拠付き批判

### 1. same-brain functional connectomics は sequential bridge であり，同時刻の完全状態標本ではありません

- [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6) は in vivo physiology から targeted volume EM へつなぐ correlative multistage workflow を示しました。
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) は，同一マウスで dense calcium imaging と後続 EM reconstruction を結ぶ large-scale same-brain dataset を示しました。

批判:

- これらは非常に強い same-brain workflow ですが，carry しているのは
  - specimen identity
  - landmarks
  - targeted subvolumes
  - local structure-function correspondences
  であり，
  - same-time whole-state
  ではありません。

### 2. `digital twin` wording は same-brain connectomics 自体の別名ではありません

- [Ding et al. (2025)](https://doi.org/10.1038/s41586-025-08840-3) は MICrONS dataset 上で validated stimulus-conditioned response model を使い wiring rule を検証しました。

批判:

- ここでの `digital twin` は `validated stimulus-conditioned predictor` を指しており，
  - same-brain scaffold
  - response model
  - unique recovered dynamics
  を同一視してよいという意味ではございません。
- 旧 wording はこの 3 つを一段に読ませうる構造でした。

### 3. predicted transcriptomic type は direct transcriptomic truth と同義ではありません

- [Gamlin et al. (2025)](https://doi.org/10.1038/s41586-025-08805-6) は Patch-seq morphology を通じて predicted Sst transcriptomic types を EM volume に割り当てました。

批判:

- これは morphology-linked label transfer の進展であって，
  - direct transcriptomic assay in the EM volume
  ではありません。
- したがって `same-brain connectomics` を `direct cell-type truth` に昇格させるのは過読でございます。

### 4. structure-function correspondence は current synaptic state を直接 fix しません

- [Holler et al. (2021)](https://doi.org/10.1038/s41586-020-03134-2) は，wiring から function を読む際に unresolved synaptic-strength structure が制約になることを示しました。
- [Dürst et al. (2022)](https://doi.org/10.1038/s41467-022-33565-6) は vesicular release probability が individual synaptic strength を強く規定することを示しました。
- [Mittermaier et al. (2024)](https://doi.org/10.1038/s41467-024-53901-2) は human neocortical tissue で membrane-potential state が synaptic consolidation を gate することを示しました。

批判:

- したがって same-brain structure-function correspondence が強まっても，
  - current efficacy
  - release probability
  - membrane-state-gated consolidation
  はなお別問題でございます。
- `same-brain functional connectomics` を `current synaptic-state readout` と読むことはできません。

### 5. connectome-constrained success は unique dynamics を保証しません

- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は，同一 connectome を共有しても biophysical parameters の違いで recurrent dynamics が縮退しうることを示しました。

批判:

- これは逆にいえば，
  - connectome-constrained prediction
  - output matching
  - response-model validation
  だけでは，
  - unique mechanism
  - unique internal dynamics
  はなお言えないことを意味します。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - front matter の `page_highlights` と `known_points` に same-brain-connectomics ceiling sync を追加しました。
  - connectome progress table の `same-brain local structure-function scaffold` row を改稿し，
    - `Bosch / MICrONS / Ding`
    - sequential bridge
    - direct assay ceiling
    - synaptic-state ceiling
    - dynamical-identifiability ceiling
    を明示しました。
  - 新規 note-box `2026-03-30 addendum: same-brain functional connectomics is a sequential scaffold, not a solved local twin` を追加しました。
  - 上記 addendum に 4 行 table を追加し，
    - sequential bridge wall
    - label-transfer wall
    - current-synaptic-state wall
    - dynamical-identifiability wall
    を分けて読めるようにしました。
  - augmentation / ablation table の
    - `+ same-brain function / behavior`
    - `+ transcriptomic / cell-type label`
    row を stricter ceiling に更新しました。
  - site rule に `same-brain functional connectomics` 専用の禁止則を追加しました。
  - minimum submissions table に `same-brain functional-connectomics claim` row を追加しました。
  - 参考文献へ Bosch (2022), Ding (2025), Dürst (2022), Mittermaier (2024) を追加しました。

## 今回止めた誤読

- `same-brain` = `same-time whole-state`
- `digital twin` = `same-brain connectomics itself`
- `predicted transcriptomic type` = `direct transcriptomic truth`
- `structure-function correspondence` = `current synaptic-state readout`
- `validated connectome-constrained prediction` = `unique local dynamics`

## 外部依存タスク

- なし
  - 今回の変更は，web 上の一次文献確認，repo 内公開ページ改稿，検証，commit，push までこのセッションで完結できます。

## 参考文献

1. Bosch C, Pacureanu A, Patino J, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022;13:2923.
   - https://doi.org/10.1038/s41467-022-30199-6
2. MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640:435-447.
   - https://doi.org/10.1038/s41586-025-08790-w
3. Ding Z, et al. Functional connectomics reveals a general wiring rule in mouse visual cortex. *Nature*. 2025;640:459-469.
   - https://doi.org/10.1038/s41586-025-08840-3
4. Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. *Nature*. 2025;640:497-505.
   - https://doi.org/10.1038/s41586-025-08805-6
5. Holler S, et al. Structure and function of a neocortical synapse. *Nature*. 2021;591:111-116.
   - https://doi.org/10.1038/s41586-020-03134-2
6. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022;13:6126.
   - https://doi.org/10.1038/s41467-022-33565-6
7. Mittermaier FX, Kalbhenn T, Xu R, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024;15:10340.
   - https://doi.org/10.1038/s41467-024-53901-2
8. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574.
   - https://doi.org/10.1038/s41593-025-02080-4
