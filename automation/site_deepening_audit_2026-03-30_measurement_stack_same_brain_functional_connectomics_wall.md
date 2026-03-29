# Site Deepening Audit (2026-03-30, measurement-stack same-brain functional connectomics wall)

## 対象

- 主対象:
  - `wiki/measurement-stack-and-claim-ceiling.md`
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

- 2026-03-29 時点の公開サイトは、`same-subject / same-brain ≠ same-state`、`connectome-complete ≠ emulation-complete`、`multimodal ≠ state-complete` をかなり明確に止められていました。
- その一方で、中核の measurement-stack ページでは `same-brain functional connectomics` がまだ一段粗く、読者が次を一まとまりに誤読しうる余地が残っておりました。
  - sequential local bridge
  - morphology-bridged label transfer
  - current synaptic-state evidence
  - identifiable / unique dynamics
- これは技術・自然科学の観点で優先度が高い弱点です。WBE 議論では `同一脳で structure-function correspondence がある`、`同一ボリュームで transcriptomic identity を直接測った`、`その瞬間の synaptic efficacy が読めた`、`connectome から dynamics が一意に決まった` は、似て見えても別々の主張だからでございます。

## 主要結論

- `same-brain functional connectomics` の旧記述は、2026-03-30 時点の一次文献に対してまだ弱すぎました。
- 一次文献の現在地では、少なくとも次を分けて読まなければなりません。
  - sequential bridge class
  - label source
  - current synaptic-state evidence class
  - dynamics-identifiability burden
- よって site rule 上の ceiling は
  - `sequential local structure-function scaffold`
  - `local conditional-prediction route`
  に止めるべきであり、
  - `direct cell-type truth`
  - `current synaptic-state readout`
  - `unique recovered dynamics`
  - `whole-brain twin`
  へは自動昇格させてはなりません。

## 根拠付き批判

### 1. same-brain functional connectomics は、まず sequential bridge として読むべきです

- [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6) は in vivo physiology から synchrotron microtomography と volume EM へつなぐ correlative workflow を示しました。
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) も、dense in vivo recording の後に fixation / histology / EM reconstruction を置く same-brain pipeline を示しました。

批判:

- これらは非常に強い same-brain workflow ですが、carry しているのは same-time whole-brain state ではなく、
  - landmarks
  - targeted subvolumes
  - local structure-function correspondences
  でございます。
- したがって `same-brain` を one global state object と読むことはできません。

### 2. label transfer は direct transcriptomic truth と同義ではありません

- [Gamlin et al. (2025)](https://doi.org/10.1038/s41586-025-08805-6) は predicted Sst transcriptomic types の connectomics を示しました。
- しかし同研究で large-scale EM volume に持ち込まれた transcriptomic identity は、直接 transcriptomic assay ではなく morphology-based classification を介した予測ラベルでございます。

批判:

- したがって、same-brain connectomics が transcriptomic classes に言及していても、
  - direct transcriptomic measurement
  - morphology-bridged label transfer
  は分けて読まなければなりません。
- 旧ページはこの区切りがまだ弱く、読者が `same-brain connectomics = direct cell-type truth` と誤読しうる余地がありました。

### 3. structure-function correspondence は current synaptic-state readout ではありません

- [Ding et al. (2025)](https://doi.org/10.1038/s41586-025-08840-3) は functional connectomics から local wiring rule を強めました。
- しかし [Holler et al. (2021)](https://doi.org/10.1038/s41586-020-03134-2) は identified neocortical synapse における structure-function link を強めつつも、構造対応だけで momentary synaptic state を閉じていないことを示しております。
- [Dürst et al. (2022)](https://doi.org/10.1038/s41467-022-33565-6) は synaptic strength に vesicular release probability が大きく関与することを示しました。
- [Mittermaier et al. (2024)](https://doi.org/10.1038/s41467-024-53901-2) は human neocortical tissue で membrane potential state が synaptic consolidation を gate することを示しました。

批判:

- したがって、同一脳内で structure-function correspondence が強まっても、それだけで
  - current efficacy
  - release state
  - membrane-state-gated consolidation
  を直接読めたことにはなりません。
- `same-brain functional connectomics` は `current synaptic-state` を直接観測した stack ではなく、まず local scaffold として読むべきでございます。

### 4. connectome-constrained prediction は unique dynamics と同義ではありません

- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は connectome-constrained recurrent networks において、connectivity を固定しても biophysical parameters の違いにより dynamics がなお縮退しうることを示しました。
- 同研究はさらに、小数の追加 recording によりその縮退を大きく減らせることを示しました。

批判:

- これは逆に言えば、connectome-constrained prediction の成功だけでは
  - unique internal dynamics
  - unique recovered mechanism
  はまだ保証されないことを意味します。
- したがって same-brain functional connectomics を `dynamics solved` と読むのではなく、`extra recordings or perturbations may still be needed to collapse the solution space` と読む必要がございました。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter の `page_highlights` と `known_points` に、same-brain functional connectomics を
    - sequential bridge
    - label-transfer
    - synaptic-state
    - dynamics-identifiability
    に分けて読む site rule を追加しました。
  - measurement-stack table の `same-brain functional connectomics` row を改稿し、
    - direct observable
    - stronger claim
    - remaining latent state
    - claim ceiling
    をより厳密に書き直しました。
  - 本文 `4.` を、`labels / current synaptic state / unique dynamics` まで分けて読む構成へ更新しました。
  - 新規 subsection `4.5. Same-brain functional connectomics is a sequential local scaffold, not current synaptic-state or a unique whole-brain twin` を追加しました。
  - 同 subsection に
    - sequential bridge wall
    - label-transfer wall
    - synaptic-state wall
    - dynamics-identifiability wall
    の 4 行 table を追加しました。
  - practical rules に
    - same-brain functional connectomics を one solved route として圧縮しない
    という禁止則を追加しました。
  - `What to add next` table に same-brain functional connectomics row を追加しました。
  - 参考文献へ Bosch (2022), Ding (2025), Holler (2021), Dürst (2022), Mittermaier (2024), Beiran & Litwin-Kumar (2025) を追加しました。

## 今回止めた誤読

- `same-brain` = `same-time whole-state`
- `predicted transcriptomic type` = `direct transcriptomic truth`
- `same-brain structure-function correspondence` = `current synaptic-state readout`
- `connectome-constrained prediction` = `unique recovered dynamics`
- `same-brain functional connectomics` = `whole-brain twin`

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、repo 内公開ページ改稿、検証、commit、push までこのセッションで完結できます。

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
7. Mittermaier V, Kononenko NL, Jin Y, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024;15:10340.
   - https://doi.org/10.1038/s41467-024-53901-2
8. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574.
   - https://doi.org/10.1038/s41593-025-02080-4
