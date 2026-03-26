# Site Deepening Audit (2026-03-27, Human Myelin MRI Quantity-Type Split)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `index.md`
- 副対象: `glossary.md`
- 副対象: `wbe_101.md`
- 派生同期: `summary_booklet.md`

## 今回の選定理由

- 現行サイトはすでに `myelin / oligodendrocyte timing support` を独立 family として扱い、`human myelin bilayer mapping` も living-human route として明示していました。
- しかし、その次の段階でまだ弱い点が残っていました。`human myelin MRI` がなお `macro-myelin proxy` という一括語で読めてしまい、`myelin water`, `MT-family contrast`, `bilayer-sensitive mapping`, `qT1 remyelination sensitivity` がほぼ同じ quantity type であるかのように見える余地がありました。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、myelin-related human observability ceiling を議論するには、`human myelin proxy exists` だけでは不十分で、`その route が何をどの measurement family で推定したのか` と `その route 固有の向き依存・装置依存・検証対象は何か` を固定しないと、timing-state の見え方を過大評価しやすいからです。

## 根拠付き批判

### 1. Human myelin MRI は一つの myelin meter ではありません

- 問題:
  - 既存サイトは `human myelin bilayer map` を正しく proxy として扱っていましたが、その内部で human myelin MRI の quantity-type split がまだ弱く、読者が `human myelin MRI = one macro myelin state` と誤読しうる状態でした。
- 根拠:
  - [Arshad et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/) は、`MWF` と calibrated `T1w/T2w` がともに高い再検査信頼性を持っても、`T1w/T2w` は subcortical white matter の myelin index として low criterion validity にとどまることを示しました。
  - [Koshino et al. (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6043493/) は、healthy adults で `SyMRI` と `MTsat` の white-matter agreement が強い一方、`T1w/T2w` は弱い対応しか示さないことを報告しました。
  - [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は、in vivo human brain で `myelin lipid-protein bilayer` を狙う別系統の ultrashort-T2 route を提示しましたが、対象は 2 healthy volunteers で high-performance hardware を要しました。
- 批判:
  - したがって、`human myelin MRI` を一括語で扱うと quantity type が消えます。
  - `myelin water`, `MT-family macromolecular contrast`, `bilayer-sensitive contrast` は同じ inferential object ではありません。

### 2. Human myelin MRI の measurement route 自体が向き依存・装置依存を持ちます

- 問題:
  - 既存サイトは `macro-myelin proxy` として ceiling を止めていましたが、なお `human myelin proxy` が一つの安定量として見える余地がありました。
- 根拠:
  - [Chen et al. (2025)](https://doi.org/10.1016/j.neuroimage.2025.121456) は、conventional quantitative MT imaging が white matter orientation に依存して変動しうる一方、`MPF-SL` では head orientation difference が `<2%` に抑えられたことを in vivo で示しました。
  - [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) も、myelin bilayer mapping で `SNR`, `scan time`, `RF power deposition`, `high-performance RF and gradient hardware` の制約を明示しています。
- 批判:
  - したがって、`human myelin MRI exists` を `myelin timing support is now generically visible` に昇格させるのは不適切です。
  - 少なくとも `quantity type`, `orientation dependence`, `hardware burden`, `validation target` を disclosure 項目にしなければなりません。

### 3. Human myelin MRI の各指標は remyelination や timing を同じようには読めません

- 問題:
  - 旧サイトは `human myelin map` と `remyelination recovery` を別 family として分けていましたが、human MRI 側でどの quantity が何に感度を持つかの split が弱いままでした。
- 根拠:
  - [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) は histology-linked postmortem MRI で、`qT1` は cortical remyelination を区別した一方、`MWF` と `MTR` は demyelinated cortex と remyelinated cortex を区別しなかったと報告しました。
  - 同論文は `qT1 and QSM, but not RD, correlated with MBP intensity` も示しており、どの MRI quantity がどの histological target に対応するかが route ごとに異なることを示しています。
- 批判:
  - したがって、`myelin-sensitive MRI` を一つの interchangeable class として読むのは粗いです。
  - `healthy myelin amount`, `remyelination-sensitive lesion contrast`, `timing-support proxy`, `bilayer contrast` は同じ claim family ではありません。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - myelin highlight を `human myelin-water / MT-family / bilayer / remyelination-sensitive MRI proxies` へ更新
  - `How this site reads current human myelin evidence` を新設
  - myelin route-card addendum を `quantity-type split` 中心に改稿
  - route-card field を `Human quantity type / measurement model` に更新
  - human observability row を `human myelin MRI quantity-type split` に更新
  - practical interpretation を `quantity-defined macro-myelin proxy family` に同期
  - references に `Arshad 2017`, `Koshino 2018`, `Chen 2025`, `Galbusera 2025` を追加

- `verification.md`
  - page highlight の myelin rule を `human quantity type / proxy class` に更新
  - myelin addendum を `MWF / T1w/T2w / MT-family / bilayer / qT1` の split へ改稿
  - Human Proxy Composition Card の human evidence row に myelin MRI disclosure ruleを追加
  - references を追加

- `index.md`
  - front-door の myelin note-boxを `human myelin MRI is not one meter` という形へ改稿

- `glossary.md`
  - `Support-state proxy` と `Timing-state` に myelin quantity-type split を反映

- `wbe_101.md`
  - human observability table の Baadsvik row を `one quantity-defined macro myelin route` として明確化

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成し、front matter 由来の公開要点を現行本文へ同期

## 今回の修正で止めた誤読

- `human myelin MRI = one generic macro myelin meter`
- `T1w/T2w, MWF, MT-family, bilayer mapping, qT1 remyelination sensitivity はほぼ同じ inferential object`
- `human myelin map exists = per-axon timing-state is near-directly visible`
- `a remyelination-sensitive MRI contrast exists = healthy myelin-state or timing-state was generically restored`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文と監査記録の更新のみで完結しています。

## 参考文献

1. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017;38(4):1780-1790.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
2. Koshino S, Hagiwara A, Okuda S, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018;8:10554.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC6043493/
3. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
4. Chen M, Tang S, Chen H, Zhou Z, Rong P, Lu H, Chen W. Orientation-independent magnetization transfer imaging of brain white matter. *NeuroImage*. 2025;309:121456.
   - https://doi.org/10.1016/j.neuroimage.2025.121456
5. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025;35(5):e70010.
   - https://doi.org/10.1111/bpa.70010
6. Gibson EM, Purger D, Mount CW, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. *Science*. 2014;344(6183):1252304.
   - https://doi.org/10.1126/science.1252304
7. McKenzie IA, Ohayon D, Li H, et al. Motor skill learning requires active central myelination. *Science*. 2014;346(6207):318-322.
   - https://doi.org/10.1126/science.1254960
8. Seidl AH, Rubel EW, Barria A. Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. *Nature Communications*. 2015;6:8073.
   - https://doi.org/10.1038/ncomms9073
9. Della-Flora Nunes G, Ots R, Völgyi K, et al. Distinct levels of remyelination are sufficient to restore neuronal function. *Nature Communications*. 2025;16:4009.
   - https://doi.org/10.1038/s41467-025-56092-6
