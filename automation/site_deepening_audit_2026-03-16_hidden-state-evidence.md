# site deepening audit: hidden-state evidence (2026-03-16)

## 選定対象

- 対象ページ: `wbe_101.md` の hidden-state 節を主対象とし、`verification.md` の latent-state error budget を運用側の受け皿として再監査しました。
- 選定理由: この節は、`connectome-complete` を `emulation-complete` と読み替えないための中核前提であり、WBE 101、FAQ、Verification、Perspective、関連 Wiki へ論理が波及していました。ここが曖昧だと、サイト全体の claim ceiling が甘くなります。

## 主な問題

### 1. 引用整合性の破綻

- `Sleep restores an optimal computational regime in cortical networks` の DOI / 誌名が誤っていました。
  - 旧: `10.1038/s41467-024-47838-5` / Nature Communications
  - 正: `10.1038/s41593-023-01536-9` / Nature Neuroscience
- `Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health` の DOI が誤っていました。
  - 旧: `10.1038/s41593-023-01517-y`
  - 正: `10.1038/s41593-023-01558-3`
- 問題点: hidden-state 論の根拠として繰り返し使っている文献の DOI が誤っていると、読者が一次資料へ戻れず、サイト全体の検証可能性を損ねます。

### 2. 証拠階層の混線

- 現状は、morpho-electric heterogeneity、sleep-homeostasis、myelin / metabolic support、astrocyte memory-related evidence、human scaffold imaging が同じ段で並びやすく、証拠の強さと外挿範囲が見えにくい状態でした。
- 問題点:
  - `cell type だけでは足りない` という local dynamics 側の話
  - `same-day fit と cross-day maintenance は別` という時間軸の話
  - `rodent local causal evidence を human whole-brain へは直結できない` という外的妥当性の話
  が一文の中で潰れていました。

### 3. 時間スケールの混線

- same-day decoding / activity match と、overnight recovery / multiday stabilization / long-term axonal health が同じ `hidden state` という見出しの下で一括処理されていました。
- 問題点: どの論文がどの時間軸の claim ceiling を下げるのかが分かりにくく、短期一致から長期維持へ不当に昇格しやすい構成でした。

### 4. human 観測可能性の ceiling が本文で弱い

- human EM 断片や MRSI-based metabolic connectome の前進は重要ですが、local transmitter specificity、astrocyte ensemble、sleep-history controller の直接観測とは別物です。
- 問題点: human 側で「何が見え始めたか」と「何がまだ latent か」の境界が本文中で十分に固定されていませんでした。

## 今回実行した変更

### 公開ページ

- `wbe_101.md`
  - hidden-state 節を、`evidence tier` ごとの表へ再構成しました。
  - rodent causal evidence と human coarse scaffold を分ける注記を追加しました。
- `verification.md`
  - latent-state error budget に `dominant timescale` / `evidence tier` / `transfer ceiling` を必須列として追加する運用ルールを挿入しました。
- `faq.md`
  - connectome + cell type に関する回答へ、rodent causal evidence と human observability ceiling の区別を追記しました。

### 整合性修正

- DOI 修正を、FAQ / Perspective / Papers / Wiki ソースへ反映しました。
- GitHub Wiki export を再生成して、公開導線と Wiki 側の引用整合性も合わせます。

## 修正の要点

- `connectome-complete` は structural scaffold の前進であり、`emulation-complete` の宣言ではありません。
- astrocyte / myelin / sleep-homeostasis の論点は重要ですが、どれも同じ強さ・同じ時間軸・同じ species transfer では扱えません。
- 読者が一次文献へ戻れること自体が、このサイトの検証基盤の一部です。DOI の正確性は内容の一部であり、装飾ではありません。

## 一次資料

1. Gouwens NW, et al. (2021). Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. https://doi.org/10.1038/s41586-020-2907-3
2. Hengen KB, et al. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. https://doi.org/10.1016/j.cell.2016.01.046
3. Torrado Pacheco A, et al. (2021). Sleep promotes downward firing rate homeostasis. https://doi.org/10.1016/j.neuron.2021.04.004
4. Xu W, et al. (2024). Sleep restores an optimal computational regime in cortical networks. https://doi.org/10.1038/s41593-023-01536-9
5. Gibson EM, et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. https://doi.org/10.1126/science.1252304
6. McKenzie IA, et al. (2014). Motor skill learning requires active central myelination. https://doi.org/10.1126/science.1254960
7. Looser ZJ, et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. https://doi.org/10.1038/s41593-023-01558-3
8. Suzuki A, et al. (2011). Astrocyte-neuron lactate transport is required for long-term memory formation. https://doi.org/10.1016/j.cell.2011.02.018
9. Cahill MK, et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. https://doi.org/10.1038/s41586-024-07311-5
10. Williamson NR, et al. (2025). Learning-associated astrocyte ensembles regulate memory recall. https://doi.org/10.1038/s41586-024-08170-w
11. Dewa K, et al. (2025). The astrocytic ensemble acts as a multiday trace to stabilize memory. https://doi.org/10.1038/s41586-025-09619-2
12. Bukalo O, et al. (2026). Astrocytes enable amygdala neural representations supporting memory. https://doi.org/10.1038/s41586-025-10068-0
13. Lee J-C, et al. (2022). Synaptic memory survives molecular turnover. https://doi.org/10.1073/pnas.2211572119
14. Beiran M, Litwin-Kumar A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. https://doi.org/10.1038/s41593-025-02080-4
15. MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. https://doi.org/10.1038/s41586-025-08790-w
16. Shapson-Coe A, et al. (2024). Connectomic reconstruction of a human brain cortical column and columnar neurons. https://doi.org/10.1126/science.adk4858
17. Lucchetti F, et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. https://doi.org/10.1038/s41467-025-66124-w
