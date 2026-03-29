# Site Deepening Audit (2026-03-30, perspective same-brain connectomics / digital-twin ceiling)

## 対象

- 主対象:
  - `perspective.md`
- 整合対象:
  - `wbe_101.md`
  - `tech_roadmap.md`
  - `wiki/decode-vs-emulate.md`
- 調査範囲:
  - 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- 2026-03-30 時点の site-wide rule では，`same-brain functional connectomics` はすでに `sequential local scaffold` として読む方向へかなり厳密化されていました．
- ただし `perspective.md` と一部の補助ページには，
  - `local digital twin`
  - `local functional twin`
  という表現が残っており，measurement-stack 側で止めている ceiling より一段強く読める余地がありました．
- 技術・自然科学の観点では，ここはかなり危険でございます．`same-brain`，`digital twin`，`predicted transcriptomic type`，`current synaptic state`，`unique dynamics` は同じ主張ではないからでございます．

## 主要結論

- `same-brain functional connectomics` は，2026-03-30 時点の一次文献に照らすと，まず
  - `sequential same-brain structure-function scaffold`
  - `task-bounded conditional prediction`
  として読むべきでございます．
- よって `local digital twin` や `local functional twin` を site の safe ceiling として残すのは強すぎました．
- さらに，少なくとも次を分けて読まなければなりません。
  - sequential bridge class
  - morphology-linked label transfer versus direct transcriptomic assay
  - current synaptic efficacy / release state
  - dynamical identifiability / degeneracy burden

## 根拠付き批判

### 1. same-brain functional connectomics は sequential bridge であり，同時刻の完全状態標本ではありません

- [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6) は，in vivo physiology から synchrotron microtomography と volume EM へつなぐ correlative workflow を示しました。
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) は，同一マウスで in vivo calcium imaging と後続 EM を co-register した大規模 same-brain dataset を示しました。

批判:

- これらは非常に強い bridge ですが，carry しているのは
  - same-brain identity
  - local structure-function correspondence
  - registered subvolume
  であり，
  - same-time whole-brain state
  ではありません。

### 2. MICrONS 側の `digital twin` は stimulus-conditioned response model であり，same-brain connectomics 自体の別名ではありません

- [Ding et al. (2025)](https://doi.org/10.1038/s41586-025-08840-3) は，MICrONS dataset を用い，neural network を用いた validated response model で wiring rule を検証しました。
- したがって，ここでの `digital twin` は `stimulus-conditioned population-response model` を意味し，そのまま `same-brain local twin` を意味しません。

批判:

- 旧 wording は
  - same-brain scaffold
  - digital-twin model
  - conditional prediction
  を一段に読ませうる構造でした。
- site rule 上は，これらを別主張として止める必要がありました。

### 3. predicted cell-type label は direct transcriptomic truth と同義ではありません

- [Gamlin et al. (2025)](https://doi.org/10.1038/s41586-025-08805-6) は，Patch-seq と EM morphology を linking し，EM cells に predicted MET-types を割り当てました。

批判:

- これは morphology-linked label transfer の進展であって，
  - direct transcriptomic assay in the EM volume
  ではありません。
- `same-brain connectomics` を `direct cell-type truth` に昇格させるのは過読でございます。

### 4. structure-function correspondence は current synaptic state を直接 fix しません

- [Holler et al. (2021)](https://doi.org/10.1038/s41586-020-03134-2) は，wiring diagrams から function を推定する際に unresolved synaptic-strength structure が制限になることを示しました。
- [Dürst et al. (2022)](https://doi.org/10.1038/s41467-022-33565-6) は，vesicular release probability が個別シナプス強度を強く規定することを示しました。
- [Mittermaier et al. (2024)](https://doi.org/10.1038/s41467-024-53901-2) は，人間 neocortical tissue において membrane-potential state が synaptic consolidation を gate することを示しました。

批判:

- したがって，same-brain structure-function correspondence が強くなっても，
  - current efficacy
  - release probability
  - membrane-state-gated consolidation
  はなお別問題でございます。
- `same-brain functional connectomics` を `current synaptic-state readout` と読むことはできません。

### 5. connectome-constrained prediction は unique recovered dynamics を保証しません

- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は，同一 connectome を共有しても biophysical parameters の違いで dynamics が縮退しうること，ただし少数の recording がその縮退を減らせることを示しました。

批判:

- これは逆にいえば，
  - connectome-constrained success
  - output matching
  - response prediction
  だけでは，
  - unique mechanism
  - unique internal dynamics
  はなお言えないことを意味します。

## 今回実行した変更

- `perspective.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter に same-brain-connectomics ceiling sync を追記しました。
  - measurement-stack table の `volume EM / same-brain connectomics` row を改稿し，
    - direct observable
    - stronger claim
    - latent state
    - page ceiling
    を `sequential scaffold` 基準に揃えました。
  - `local functional twin` 系 wording を除去し，`sequential same-brain scaffold / local conditional predictor` へ置換しました。
  - `2026-03-30 correction` note-box を新設し，Bosch / MICrONS / Ding / Gamlin / Holler / Dürst / Mittermaier / Beiran を使って ceiling を明文化しました。
  - observability wall と key technical challenges 節の `digital twin` wording を，より狭い inferential object へ修正しました。
- `wbe_101.md`
  - `local digital twin` を `stimulus-conditioned digital-twin / connectome-constrained predictor families` へ修正しました。
  - connectome-progress note に，MICrONS-side digital twin は sequential scaffold に重ねた response model だと明記しました。
- `tech_roadmap.md`
  - M3 の connectomics upper bound を `local functional twins` から
    - sequential same-brain local scaffolds
    - stimulus-conditioned conditional predictors
    に修正しました。
- `wiki/decode-vs-emulate.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - `digital twin / connectome-constrained model` row を `stimulus-conditioned digital twin / connectome-constrained model` へ改稿しました。
  - operation rules と concluding paragraph も同じ ceiling に揃えました。

## 今回止めた誤読

- `same-brain` = `same-time local twin`
- `digital twin` = `same-brain connectomics itself`
- `predicted MET-type` = `direct transcriptomic truth`
- `structure-function correspondence` = `current synaptic-state readout`
- `connectome-constrained prediction` = `unique recovered dynamics`

## 外部依存タスク

- なし
  - 今回の変更は，文献確認，公開ページ改稿，ローカル検証，commit，push までこのセッションで完結可能でございます。

## 参考文献

1. Bosch C, Ackels T, Pacureanu A, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022;13:2923.
   - https://doi.org/10.1038/s41467-022-30199-6
2. MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640:435-447.
   - https://doi.org/10.1038/s41586-025-08790-w
3. Ding Z, et al. Functional connectomics reveals a general wiring rule in mouse visual cortex. *Nature*. 2025;640:459-469.
   - https://doi.org/10.1038/s41586-025-08840-3
4. Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. *Nature*. 2025;640:497-505.
   - https://doi.org/10.1038/s41586-025-08805-6
5. Holler S, Köstinger G, Martin KAC, Schuhknecht GFP, Stratford KJ. Structure and function of a neocortical synapse. *Nature*. 2021;591:111-116.
   - https://doi.org/10.1038/s41586-020-03134-2
6. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022;13:6126.
   - https://doi.org/10.1038/s41467-022-33565-6
7. Mittermaier FX, Kalbhenn T, Xu R, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024;15:10340.
   - https://doi.org/10.1038/s41467-024-53901-2
8. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574.
   - https://doi.org/10.1038/s41593-025-02080-4
