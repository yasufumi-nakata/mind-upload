# Site Deepening Audit (2026-03-17, Implant Tissue Response Ceiling / chronic invasive BCI)

## 対象

- 主対象: `wiki/state-trait-and-drift.md`
- 副対象: `verification.md`
- 副対象: `perspective.md`
- 参照整合: `wiki/decode-vs-emulate.md`

## 今回の選定理由

- 2026-03-17 時点でサイトは、`same-session streaming ≠ chronic deployability`、`fixed decoder longevity ≠ same-neuron identity`、`decode ≠ emulate` をかなり明確に区別できていました。
- その一方で、慢性侵襲記録の ceiling をなお `sorting / matching / recalibration` 側へ寄せて読みやすく、`implant 周囲の組織応答そのものが観測限界を作る` 点は主要本文でまだ弱かったです。
- これは技術・自然科学の観点で優先度が高い弱点です。なぜなら、慢性 intracortical BCI の性能低下や feature turnover を、`decoder 側の問題` と `純粋な生体 drift` だけで説明できるように見せるからです。

## 根拠付き批判

### 1. 旧サイトは `unit identity uncertainty` と `implant biology` を同じ箱に入れていました

- 問題:
  - `verification.md` と `wiki/state-trait-and-drift.md` は、same-neuron claim が sorting / matching を介した推定であることは正しく書けていました。
  - しかし、`unit-match probability` と `implant 周囲の vascular / BBB / glial / neuronal response` が同じ `tissue response` 行へ圧縮されており、読者が両者を 1 種類の不確実性として読める構造が残っていました。
- 根拠:
  - Szymanski et al. (2021) は、tetraplegic patient の chronically implanted intracortical microelectrode 周囲に encapsulation、foreign-body reaction、microhemorrhage、neuronal loss を報告しました。
  - Gregory et al. (2023) は、rat motor cortex の埋め込み array 周囲で deep-layer pyramidal neuron の structural / functional change を示しました。
  - Dynamic changes in mural cells drive vascular remodeling around chronically implanted neural probes (2025) は、chronic implant 周囲の mural cell と vascular remodeling を示しました。
- 批判:
  - したがって、慢性侵襲記録の drift は `sorting error` だけではなく、`local tissue そのものが変わる` ことでも生じます。
  - `same neuron across days` の監査と、`この interface は biologically neutral か` の監査は分けるべきでございます。

### 2. 旧 chronic speech BCI 導線は、`decoder longevity` と `tissue-response ceiling` を別提出物にしていませんでした

- 問題:
  - `perspective.md` は fixed decoder longevity、recalibration burden、same-neuron tracking ceiling をすでにかなり良く整理していました。
  - しかし、intracortical speech BCI の chronic ceiling に `implant biology` が前面化されておらず、長期低下を decoder / calibration 問題としてのみ読める余地がありました。
- 根拠:
  - Wilson et al. (2025) は、長期 intracortical BCI で unsupervised recalibration が必要になることを示しました。
  - Pun et al. (2024) は、human chronic intracortical recording の instability が performance 低下と強く相関することを示しました。
  - Abbott et al. (2024) は、planar amorphous silicon carbide array が chronic tissue response を弱めうることを報告しており、material / geometry 自体が性能上限を動かすことを示します。
- 批判:
  - したがって、speech BCI の long-term ceiling は `fixed decoder`、`recalibration burden`、`same-neuron identity` に加え、`implant biology` を別列で出さないと過小規定です。

### 3. 旧提出物規格では `signal-chain drift` と `implant biology drift` の分離が不足していました

- 問題:
  - Temporal Validity Card は再装着、sorting、unit matching をかなり明示できていました。
  - しかし `implant age`、`array type / material / geometry`、`vascular / BBB / encapsulation proxy` は独立欄になっていませんでした。
- 批判:
  - これでは `interface audit を出した` と言っても、signal-chain 監査だけで chronic invasive claim を通したことになります。
  - 本サイトの方針に照らすと、これは evidence ceiling の取り扱いとしてまだ甘いです。

### 4. 参照整合性の小さな破綻がありました

- 問題:
  - `perspective.md` と `wiki/decode-vs-emulate.md` の Kilosort4 DOI が、`10.1038/s41592-024-02232-7` になっていました。
- 修正:
  - 一次資料に合わせて `10.1038/s41592-024-02595-5` へ修正しました。

## 今回実行した変更

- `wiki/state-trait-and-drift.md`
  - `last_updated` を `2026-03-17` に更新
  - `4 buckets` を `5 buckets` に改め、`signal-chain / decoder drift` と `implant biology drift` を分離
  - `tissue response は sorting error ではなく implant biology の独立軸` 節を追加
  - `what to measure` と Temporal Validity Card 対応表へ `implant biology audit` 行を追加
  - site rule を `drift は 3 系統に分ける` へ更新
  - human pathology / vascular remodeling / low-profile array の参考文献を追加
- `verification.md`
  - `latent-state error budget` の `chronic unit identity / tissue response` 行を、`sorting uncertainty` と `implant tissue response / interface biology` に分割
  - `tissue response は unit matching の別名ではない` note を追加
  - Temporal Validity Card の `interface / decoder drift audit` を `signal-chain / implant-biology drift audit` へ更新
  - page highlights / known points を更新
  - 参考文献へ Szymanski (2021), Wellman (2025), Abbott (2024) を追加
- `perspective.md`
  - highlights / known points を、`implant biology audit` を含む形へ更新
  - Research Program Phase 2 の implant metadata を `material / geometry / tissue-response proxy` まで拡張
  - `chronic speech BCI の 3 つの ceiling` を `4 つの ceiling` へ改稿
  - `implant biology ceiling` 行を追加
  - chronic stability 指標へ `implant age / material / geometry / tissue-response proxy` を追加
  - Kilosort4 DOI を修正
- `wiki/decode-vs-emulate.md`
  - Kilosort4 DOI を修正
  - chronic invasive claim に `implant age / material / geometry / tissue-response proxy` を追加

## 外部依存で保留

- なし
  - 今回の作業は、一次文献に基づく公開本文と提出物規格の更新で完結しています。

## 参考文献

1. Szymanski LJ, Kellis S, Liu CY, Jones KT, Andersen RA, Commins DL, Lee B, McCreery DB, Miller CA. Neuropathological effects of chronically implanted, intracortical microelectrodes in a tetraplegic patient. *Journal of Neural Engineering*. 2021;18(4):046026.
   - https://doi.org/10.1088/1741-2552/ac127e
2. Gregory NS, et al. Structural and functional changes of deep layer pyramidal neurons surrounding implanted microelectrode arrays in rat motor cortex. *Journal of Neural Engineering*. 2023;20(4):046022.
   - https://doi.org/10.1088/1741-2552/ace8ac
3. Dynamic changes in mural cells drive vascular remodeling around chronically implanted neural probes. *Biomaterials*. 2025.
   - https://doi.org/10.1016/j.biomaterials.2024.122963
4. Abbott JR, et al. Planar amorphous silicon carbide microelectrode arrays for chronic recording in rat motor cortex. *Biomaterials*. 2024;317:122543.
   - https://doi.org/10.1016/j.biomaterials.2024.122543
5. Pun TK, Khoshnevis M, Hosman T, et al. Measuring instability in chronic human intracortical neural recordings towards stable, long-term brain-computer interfaces. *Communications Biology*. 2024;7:1363.
   - https://doi.org/10.1038/s42003-024-06784-4
6. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
7. Pachitariu M, Sridhar S, Pennington J, Stringer C. Spike sorting with Kilosort4. *Nature Methods*. 2024;21:914-921.
   - https://doi.org/10.1038/s41592-024-02595-5
