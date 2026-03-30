# Site Deepening Audit (2026-03-30, front door same-brain functional connectomics stop rule)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
- 同期先として確認したページ:
  - `wbe_101.md`
  - `perspective.md`
  - `verification.md`
  - `wiki/connectome-is-not-enough.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wiki/state-continuity-bridge.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

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

- `perspective.md`、`mind_uploading_papers.md`、`research_harvest_50.md`、`wiki/connectome-is-not-enough.md` では、same-brain functional connectomics の ceiling はすでにかなり厳密に更新されておりました。
- しかし入口ページである `index.md` と `faq.md` では、関連 stop rule が
  - `same-subject / same-brain bridge`
  - `connectome insufficiency`
  の形では入っていても、
  - `same-brain functional connectomics`
  - `digital twin`
  - `predicted transcriptomic type`
  - `current synaptic-state`
  - `unique local dynamics`
  を明示的に分ける短い停止条件がまだ弱うございました。
- そのため、入口ページだけ読んだ読者が
  - `same mouse`
  - `functional connectomics`
  - `digital twin`
  をまとめて `solved local twin`
  と誤読する余地が残っておりました。

## 主要結論

- front door でも、same-brain functional connectomics は少なくとも次の 4 分割で止める必要がございました。
  - `sequential bridge class`
  - `label-transfer route versus direct transcriptomic assay`
  - `current synaptic-state ceiling`
  - `dynamical identifiability / degeneracy burden`
- よって入口説明の safe ceiling は
  - `sequential local structure-function scaffold`
  - `task-bounded conditional predictor`
  に留めるのが妥当でございます。
- 以下は入口ページで禁止すべき overread でございます。
  - `same-brain functional connectomics = direct transcriptomic truth`
  - `same-brain functional connectomics = current synaptic-state readout`
  - `digital twin = solved local twin`
  - `connectome-constrained prediction = unique recovered dynamics`

## 根拠付き批判

### 1. same-brain functional connectomics は multistage bridge であり，同時刻の state sample ではありません

- [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6) は，in vivo physiology を synchrotron microtomography と volume EM へつなぐ multistage correlative workflow を示しました。
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) は，約 `75,000 neurons` の activity を，後続 EM の `>200,000 cells`・`0.5 billion synapses` と同一マウスで結びつけました。

批判:

- これは非常に強い same-brain local bridge ですが，
  - same-time whole-state sample
  - same-time whole-brain local twin
  ではございません。
- carry されている主対象は
  - same-brain identity
  - local structure-function correspondence
  - registered subvolume
  でございます。

### 2. `digital twin` は same-brain connectomics 自体の別名ではありません

- [Ding et al. (2025)](https://doi.org/10.1038/s41586-025-08840-3) は，同 dataset 上で validated stimulus-conditioned response model を構築しました。
- 同論文は model internal representations の解釈について caution も明示しております。

批判:

- したがって，
  - same-brain connectomics
  - local conditional predictor
  - digital twin model
  を一段に圧縮するのは不正確でございます。
- `digital twin` は route-conditioned model claim であり，same-brain dataset そのものの別名ではございません。

### 3. predicted transcriptomic type は direct transcriptomic truth と同義ではありません

- [Gamlin et al. (2025)](https://doi.org/10.1038/s41586-025-08805-6) は，morphology-linked prediction により `predicted Sst transcriptomic types` を扱いました。

批判:

- これは label-transfer の進歩であり，
  - direct transcriptomic assay in the EM volume
  と同じではございません。
- したがって `same-brain connectomics solved cell type truth` と読むのは過読でございます。

### 4. structure-function correspondence は current synaptic state を直接 fix しません

- [Holler et al. (2021)](https://doi.org/10.1038/s41586-020-03134-2) は，wiring diagrams から function を読む際の unresolved synaptic-strength structure を明示しました。
- [Dürst et al. (2022)](https://doi.org/10.1038/s41467-022-33565-6) は，vesicular release probability が個別シナプス強度を大きく規定することを示しました。
- [Mittermaier et al. (2024)](https://doi.org/10.1038/s41467-024-53901-2) は，人間 neocortical tissue で membrane-potential state が synaptic consolidation を gate することを示しました。

批判:

- したがって same-brain structure-function correspondence が強くなっても，
  - current efficacy
  - release probability
  - membrane-state-gated consolidation
  は別問題のままでございます。

### 5. connectome-constrained prediction は unique local dynamics を保証しません

- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は，connectome-constrained recurrent networks が追加 recording なしでは dynamically degenerate たりうることを示しました。

批判:

- これは逆に，
  - output prediction success
  - connectome-constrained fit
  - response-model success
  をもって
  - unique internal dynamics recovered
  と読むことができないことを意味します。

## 今回実行した変更

- `index.md`
  - `page_highlights` に same-brain functional connectomics stop rule を追加しました。
  - `known_points` に safe ceiling を追加しました。
  - 新しい front-door note box
    - `If Same-Brain Functional Connectomics Sounds Like A Solved Local Twin`
    を追加し，Bosch / MICrONS / Ding / Gamlin / Holler / Dürst / Mittermaier / Beiran の 8 本で ceiling を固定しました。
- `faq.md`
  - `page_highlights` の front-door guardrail を `eleven` に更新し，同 stop rule を追加しました。
  - `known_points` に same-brain connectomics / digital-twin split を追加しました。
  - `Eleven technical guards now fixed at the front door` に same-brain stop rule を追加しました。
  - 冒頭の読者導線 table に `Q2c1` を追加しました。
  - 新規短答 `Q2c1` を追加し，入口だけ読んだ読者にも safe ceiling が伝わるようにしました。

## 今回止めた誤読

- `same-brain = same-time local twin`
- `digital twin model = solved local twin`
- `predicted transcriptomic type = direct transcriptomic truth`
- `structure-function correspondence = current synaptic-state readout`
- `connectome-constrained response model = unique local dynamics`

## 外部依存タスク

- なし
  - 今回の変更は，web 上の一次文献確認，公開ページ改稿，ローカル検証，commit，push までこのセッションで完結可能でございます。

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
