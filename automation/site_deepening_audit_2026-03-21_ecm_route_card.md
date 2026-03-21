# Site Deepening Audit (2026-03-21, ECM / PNN Route Card and Human Ceiling Clarification)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 参照整合先: `wbe_101.md`, `index.md`, `verification.md`

## 今回の選定理由

- 2026-03-21 時点で、公開サイトは `perisynaptic ECM / PNN state` を重要な hidden state としてはすでに扱っていました。
- しかし、他の maintenance-state 群と異なり、ECM / PNN だけはまだ独立の `route card` に落ちておらず、
  - plasticity-window reopening
  - receptor-mobility constraint
  - microglia / proteolysis controller
  - cell-type-specific memory support
  - aging / pathology-associated rescue or shift
  - human ex vivo morphology / pathology
  を一つの言葉で読める余地が残っていました。
- この欠落は技術・自然科学の観点で重要です。理由は、ECM / PNN の文脈では `same memory word` が `same measurement object` を意味しないからでございます。

## 根拠付き批判

### 1. 既存サイトは ECM / PNN の重要性は説明していましたが、まだ `claim family` を分け切れていませんでした

- 問題:
  - 既存ページは Pizzorusso / Frischknecht / Gogolla / Chelini / Jabłońska を使って ECM / PNN の重要性自体は示していました。
  - しかし、`何を測ったか` と `何を変えたか` を route-card の欄に固定していなかったため、読者が `ECM paper = plasticity gate general solved` と過読しやすい構造が残っていました。
- 根拠:
  - Pizzorusso et al. (2002) は adult visual cortex における plasticity-window reopening の route です。
  - Frischknecht et al. (2009) は AMPA receptor lateral mobility と short-term plasticity の route です。
  - Nguyen et al. (2020) は neuronal IL-33 / microglial ECM engulfment による synapse remodeling と memory consolidation の route です。
  - Alexander et al. (2025) は CA2 pyramidal-cell PNN と PV-cell PNN が同じ memory object を支えていないことを示しました。
- 批判:
  - したがって、ECM / PNN evidence は最初から heterogeneous であり、`ECM matters for memory` という 1 行では scientific stop rule として弱すぎます。
  - 特に `matrix object`, `cell population`, `functional target` を固定しない限り、同じ語が別の claim object を指してしまいます。

### 2. rescue と healthy ECM-state completion は同じではありません

- 問題:
  - 既存本文には ECM / PNN 関連の rescue / intervention route を generic improvement と読める余地がありました。
- 根拠:
  - Mehak et al. (2025) は aged mouse dCA2 で PNN intensity 上昇と recognition-memory deficit / theta-power reduction を示し、ChABC で rescue を示しました。
- 批判:
  - これは `aged condition で rescue が起きた` のであって、`healthy youthful ECM-state が fully reconstructed された` ことと同義ではありません。
  - よって ECM / PNN には `recovery / completeness boundary` を独立欄として持たせる必要があります。

### 3. human evidence は存在しても、まだ `in vivo whole-brain current ECM gate` ではありません

- 問題:
  - 旧構成は human relevance を `Boonen et al. (2022)` の病理組織で止めていましたが、human 側の ceiling を route-card の形で固定していませんでした。
- 根拠:
  - Lehner et al. (2024) は human hippocampus で age-dependent PNN increase と epilepsy-associated precocious aging を示しましたが、これは histopathology です。
  - Banovac et al. (2025) は human postmortem prefrontal cortex で PNN の laminar / molecular heterogeneity を示しましたが、これも postmortem histology です。
- 批判:
  - したがって、human ECM evidence は `human relevance exists` を支持しても、`same-subject time-varying in vivo ECM-state readout` の ground truth ではありません。
  - 旧サイトはこの ceiling を説明していても、他 route card のような submission-side stop rule にまでは落としていませんでした。

### 4. ECM / PNN は `one matrix variable` ではなく、cell-type and circuit specific です

- 問題:
  - 旧ページは ECM / PNN を synapse-count や glia とは独立させていましたが、なお `one matrix row` として読める余地がありました。
- 根拠:
  - Alexander et al. (2025) は CA2 pyramidal-cell PNN deletion で social memory と reversal learning が落ち、PV-cell PNN deletion では contextual fear memory が落ちることを示しました。
- 批判:
  - これは `ECM state` が brain-wide one-dimensional knob ではないことを意味します。
  - route card に `matrix object and cell population` 欄を置かない限り、CA2-specific route と PV-specific route を同列比較してしまいます。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights` に ECM / PNN evidence の heterogeneous claim-family を追加しました。
  - `unknown_points` に ECM / PNN route-card 必須欄の未確定点を追加しました。
  - 新規 `#ecm-pnn-route-card` を追加し、
    - claim family
    - matrix object and cell population
    - direct observable
    - controller / perturbation route
    - functional target
    - recovery / completeness boundary
    - human observability / external calibration
    - abstention boundary
    を明文化しました。
  - 参考文献として Nguyen (2020), Lehner (2024), Alexander (2025), Banovac (2025), Mehak (2025) を追加しました。
- `wbe_101.md`
  - entry-level note-box として `ECM / PNN evidence now gets its own route card` を追加しました。
  - 初学者が `ECM matters` を one-line summary として過読しないよう、claim family と human ceiling への導線を付けました。
- `index.md`
  - front-door に `If You Are Treating ECM / PNN Evidence As One Solved Row` を追加しました。
  - ChABC rescue, cell-type-specific PNN route, human ex vivo histology を同じ成果物として読まない停止線を追加しました。
- `verification.md`
  - ECM / PNN addendum を route-card 仕様へ更新しました。
  - verification 本文から `Wiki: ECM / PNN route card` へ直接飛べるようにしました。
  - 参考文献として Nguyen (2020), Lehner (2024), Alexander (2025), Banovac (2025), Mehak (2025) を追加しました。

## 外部依存で保留

- human in vivo ECM / PNN observability benchmark
  - 担当者: ECM / circuit-plasticity 研究者、human neuroimaging method 開発者、benchmark maintainer
  - 前提条件: same-subject longitudinal acquisition で ECM / PNN-relevant external calibrator を伴う human-compatible route が公開されること
  - 完了条件: ex vivo histology と in vivo proxy を同一 schema で比較し、current ECM gate claim を直接監査できる benchmark が整備されること

## 参考文献

1. Pizzorusso T, Medini P, Berardi N, Chierzi S, Fawcett JW, Maffei L. Reactivation of ocular dominance plasticity in the adult visual cortex. *Science*. 2002.
   - https://doi.org/10.1126/science.1072699
2. Frischknecht R, Heine M, Perrais D, Seidenbecher CI, Choquet D, Gundelfinger ED. Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. *Nature Neuroscience*. 2009.
   - https://doi.org/10.1038/nn.2338
3. Gogolla N, Caroni P, Lüthi A, Herry C. Perineuronal nets protect fear memories from erasure. *Science*. 2009.
   - https://doi.org/10.1126/science.1174146
4. Nguyen PT, Dorman LC, Pan S, et al. Microglial Remodeling of the Extracellular Matrix Promotes Synapse Plasticity. *Cell*. 2020.
   - https://doi.org/10.1016/j.cell.2020.05.050
5. Chelini G, Pantazopoulos H, Durning P, et al. Focal clusters of peri-synaptic matrix contribute to activity-dependent plasticity and memory in mice. *Cell Reports*. 2024.
   - https://doi.org/10.1016/j.celrep.2024.114112
6. Jabłońska K, Kaczor K, Kółeczko M, et al. Extracellular matrix integrity regulates GABAergic plasticity in the hippocampus. *Matrix Biology*. 2024.
   - https://doi.org/10.1016/j.matbio.2024.11.001
7. Lehner A, Hoffmann L, Rampp S, et al. Age-dependent increase of perineuronal nets in the human hippocampus and precocious aging in epilepsy. *Epilepsia Open*. 2024.
   - https://doi.org/10.1002/epi4.12963
8. Alexander GM, Nikolova VD, Stöber TM, Gruzdev A, Moy SS, Dudek SM. Perineuronal Nets on CA2 Pyramidal Cells and Parvalbumin-Expressing Cells Differentially Regulate Hippocampal-Dependent Memory. *Journal of Neuroscience*. 2025.
   - https://doi.org/10.1523/JNEUROSCI.1626-24.2024
9. Banovac I, Prkačin MV, Kirchbaum I, et al. Morphological and Molecular Characteristics of Perineuronal Nets in the Human Prefrontal Cortex-A Possible Link to Microcircuitry Specialization. *Molecular Neurobiology*. 2025.
   - https://doi.org/10.1007/s12035-024-04306-1
10. Mehak SF, Shivakumar AB, Jijimon F, Gupta A, Pillai VG, Gangadharan G. Targeting CA2 Perineuronal Nets Restores Recognition Memory and Theta Oscillations in Aged Mice. *Aging Cell*. 2025.
   - https://doi.org/10.1111/acel.70139
11. Boonen M, Hellings N, Hoedemaekers T, et al. Reorganization of the brain extracellular matrix in hippocampal sclerosis. *International Journal of Molecular Sciences*. 2022.
   - https://doi.org/10.3390/ijms23158197
