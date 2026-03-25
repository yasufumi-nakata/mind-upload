# Site Deepening Audit (2026-03-25, Summary Booklet technical stop lines)

## 対象

- 主対象: `summary_booklet.md`
- 実装対象: `scripts/build_summary_booklet.rb`

## 今回この箇所を選んだ理由

- 2026-03-25 JST 時点で、公開ページ本体の `hidden-state / human proxy / state-continuity / shortcut / temporal validity` の規律はかなり強化されておりました。
- しかし `summary_booklet.md` は自動要約の都合で、
  - front matter の先頭項目
  - 単純な `first(n)`
  - 強い文字数短縮
  に依存しており、入口で最も落としてはいけない技術的 stop line が薄まりやすい状態でした。
- とくに冊子の既定出力では、`same-subject != same-state`、`proxy-rich != state closure`、`connectome-complete != emulation-complete`、`same-day != cross-day` といった技術・自然科学上の停止線より、哲学寄りの unresolved 項目が前に出やすくなっておりました。
- これは自然科学の観点で弱点です。なぜなら、入口冊子は「最初に何をどう誤読しないか」を固定する層であり、ここで停止線が落ちると、本体ページで厳密化した measurement-model caveat や bridge audit が reader に届く前に progress narrative へ圧縮されやすいからです。

## 根拠付き批判

### 1. `connectome / cell type だけでは足りない` という中心停止線が booklet 冒頭で十分に保持されていませんでした

- 根拠:
  - Gouwens et al. (2021) は、同一 transcriptomic type の内部にも morpho-electric 変動が残ることを示しました。
  - Hengen et al. (2016) と Xu et al. (2024) は、睡眠・回復・計算レジームの差が配線図の外側にある maintenance-state を露出させることを示しました。
- 批判:
  - したがって `connectome-complete` や `cell-type-complete` を `dynamics-complete` と誤読させないことは front door の最優先要件です。
  - にもかかわらず旧 booklet は、その停止線を表紙や既知/未解決欄で安定して前景化できておりませんでした。

### 2. `human proxy は layered` かつ `bundle は自動加算されない` という停止線が summary 層で希薄でした

- 根拠:
  - Johansen et al. (2024) は healthy-human SV2A atlas であり、Smart et al. (2021) は短時間 activation で `binding` が不変でも `influx` が動くことを示しました。これは `synaptic-density proxy != momentary synaptic efficacy` を意味します。
  - Lucchetti et al. (2025) は `five-metabolite parcel-similarity graph` を与え、Li et al. (2025) は dynamic DMRSI + kinetic model により rate imaging を与えました。両者は同じ object ではありません。
  - Chen et al. (2025), Bolt et al. (2025), Epp et al. (2025) は、同時取得や multimodal agreement があっても common driver と modality-specific residual を分けなければ one-state closure とは言えないことを示しました。
- 批判:
  - したがって `human evidence is layered` と `proxy-rich != state closure` は summary 層で落としてはならない規律です。
  - 旧 booklet は page ごとの技術的上限よりも一般紹介を優先しており、この composition ceiling が入口で十分に見えませんでした。

### 3. `same-subject` と `same-day` の誤読停止線が、booklet では technical unresolved として十分に整理されていませんでした

- 根拠:
  - Egger et al. (2024) は 10 時間の simulated day-long BCI use で decoder-relevant EEG dynamics が動くことを示しました。
  - Bosch et al. (2022) と MICrONS Consortium et al. (2025) は、same-brain workflow でも landmark / deformation / sequential bridge burden が残ることを示しました。
- 批判:
  - したがって `same-subject` は specimen identity の一部であり、`same-state continuity` の証拠ではありません。
  - また `same-day accuracy` は `cross-day robustness` や `maintenance-consistent dynamics` の証拠ではありません。
  - 旧 booklet は未解決欄で哲学寄り unresolved を前に出しがちで、bridge / drift / temporal-validity を入口の保留項目として十分に見せておりませんでした。

## 今回実行した変更

- `scripts/build_summary_booklet.rb`
  - technical stop line 用の優先抽出ロジックを追加しました。
  - `connectome -> layered human evidence -> same-subject bridge -> proxy composition -> temporal validity -> shortcut` の順に booklet の主要停止線を安定表示するようにしました。
  - `identity / personhood / social deployment / philosophy` を booklet の主要 unresolved 候補から外し、technical-only の unresolved を優先するようにしました。
  - `route card` 細目を summary 冒頭へ出しすぎないように除外し、入口冊子に必要な一般停止線を優先するようにしました。
  - 各ページカードの bullet も `first(3)` ではなく、科学的に重要な stop line を優先選択するようにしました。
- `summary_booklet.md`
  - 表紙カードの `すぐ断言しないもの` を `入口で止める過読` へ変更しました。
  - `Known vs Unknown` を technical-first に更新しました。
  - `入口で落としてはいけない技術的停止線` セクションを新設しました。
  - 同セクションで `観測の上限` と `比較と解釈の上限` を分け、connectome/hidden-state と proxy/bridge/drift/shortcut を別々に前景化しました。

## 外部依存で保留

- なし
  - 今回の変更は、このリポジトリ内の要約生成規則と生成物の更新で完結しております。

## 参考文献

1. Gouwens NW, et al. Phenotypic variation of transcriptomic cell types in mouse motor cortex. *Nature*. 2021.
   - https://doi.org/10.1038/s41586-020-2907-3
2. Hengen KB, et al. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016.
   - https://doi.org/10.1016/j.cell.2016.01.046
3. Xu Y, et al. Sleep restores optimal computational regime in cortical networks. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-024-47838-5
4. Johansen A, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
5. Smart K, et al. Binding of the synaptic vesicle radiotracer [11C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
6. Lucchetti F, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
7. Li X, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
8. Chen JE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-64414-x
9. Bolt TS, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01945-y
10. Epp SM, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
11. Egger A, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
12. Bosch C, et al. Linking in vivo physiology to synchrotron X-ray tomography and volume electron microscopy in the mouse barrel cortex. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
13. MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
