# Site Deepening Audit 2026-03-20: phospho-signaling / second-messenger state

## 対象
- 今回の深掘り対象は `phospho-signaling / second-messenger state` です。
- 具体的には、リン酸化部位占有率、kinase/phosphatase バランス、局所 cAMP/Ca2+/PKA nanodomain を、`transcript abundance` や `bulk protein abundance` とは独立の hidden state として扱う必要があります。

## 今回の選定理由
- 既存サイトは `transcription / chromatin`、`post-transcriptional RNA-state`、`proteostasis`、`cargo transport`、`ionic milieu`、`astrocyte / glial-state` などをかなり丁寧に分離できていました。
- しかしその一方で、`protein がある` ことと `その protein が今どの phospho-state で動作しているか` の区別がまだ弱く、memory-relevant plasticity の制御層が一段つぶれていました。
- この欠落は、connectome 完備や transcript/protein atlas の過大解釈につながります。特に `active signaling gate` を abundance-only 情報から埋めてしまう読み方を防ぐ必要がありました。

## 根拠付き批判

### 1. transcript abundance と phospho-state は同一ではありません
- CaMKII Thr286 自己リン酸化は LTP と学習に必要です。したがって、同じ gene expression や protein abundance でも、plasticity の作動条件は一致しません。
- 根拠:
  - Giese et al. (1998), Science, doi:10.1126/science.279.5352.870

### 2. AMPAR 系 plasticity は phosphosite ごとに挙動が異なります
- AMPA receptor phosphorylation site の違いだけで bidirectional plasticity の表現型が変わるため、`current weight` や `protein presence` を知っても、active plasticity rule は確定しません。
- 根拠:
  - Lee et al. (2003), Cell, doi:10.1016/S0092-8674(03)00122-3
  - Tomita et al. (2005), Neuron, doi:10.1016/j.neuron.2005.01.009

### 3. 学習関連 state は phospho-state として局所シナプスに残ります
- Fear conditioning に伴う lateral amygdala synapse の CaMKII phospho-state 変化は、`abundance` よりも `site-specific active state` が重要であることを示します。
- 根拠:
  - Rodrigues et al. (2004), Journal of Neuroscience, doi:10.1523/JNEUROSCI.5303-03.2004

### 4. second-messenger は細胞全体平均ではなく nanodomain として制御されます
- ER-plasma membrane junction が neuronal activity を Ca2+-activated PKA signaling に結びつけるという結果は、局所 signaling nanodomain を bulk abundance から復元できないことを示します。
- 根拠:
  - Vierra et al. (2023), Nature Communications, doi:10.1038/s41467-023-40930-6

### 5. human 側の observability ceiling も明示的に低いままです
- human brain phosphoproteome atlas は有用ですが ex vivo atlas です。living whole-brain の current phospho-state を comparable に読む route ではありません。
- 根拠:
  - Biswas et al. (2023), Journal of Proteome Research, doi:10.1021/acs.jproteome.2c00244

## 今回実行した変更
- `wbe_101.md`
  - hidden-state 一覧、entry-point note、human observability ceiling、参考文献を更新しました。
- `faq.md`
  - `Q2c` と `Q2d` に phospho-signaling / second-messenger state の欠落と human ceiling を追加しました。
- `verification.md`
  - latent-state error budget、maintenance-state error budget、state variable integrity gate、minimum operating rule、2026-03-20 addendum、参考文献を更新しました。
- `glossary.md`
  - `Maintenance-state` 定義の拡張と `Phospho-signaling / second-messenger state` 項目を追加しました。
- `wiki/connectome-is-not-enough.md`
  - state-class 数を 14 に更新し、table・本文・human observability ceiling・参考文献へ反映しました。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - maintenance-state 数を 16 に更新し、table・本文・human observability ceiling・claim-close-to-state-complete reconstruction・参考文献へ反映しました。

## 外部依存で保留
- human in vivo whole-brain phospho-state readout の獲得
  - 担当: 実験系・計測系研究コミュニティ
  - 前提条件: 非破壊かつ広域な phosphosite / signaling-nanodomain observability route の成立
  - 完了条件: living human whole-brain で phospho-state を comparable に測定できること
- phospho-state を WBE verification artifact にどう最小実装するかの標準化
  - 担当: サイト側 verification design
  - 前提条件: animal causal route と human proxy route の接続仕様がもう一段整理されること
  - 完了条件: submission template で required / optional / abstention を固定できること

## 参考文献
- Giese, K. P., Fedorov, N. B., Filipkowski, R. K., & Silva, A. J. (1998). Autophosphorylation at Thr286 of the alpha calcium-calmodulin kinase II in LTP and learning. Science. doi:10.1126/science.279.5352.870
- Lee, H.-K., Barbarosie, M., Kameyama, K., Bear, M. F., & Huganir, R. L. (2003). Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. Cell. doi:10.1016/S0092-8674(03)00122-3
- Rodrigues, S. M., Farb, C. R., Bauer, E. P., LeDoux, J. E., & Schafe, G. E. (2004). Pavlovian fear conditioning regulates Thr286 autophosphorylation of Ca2+/calmodulin-dependent protein kinase II at lateral amygdala synapses. Journal of Neuroscience. doi:10.1523/JNEUROSCI.5303-03.2004
- Tomita, S., Stein, V., Stocker, T. J., Nicoll, R. A., & Bredt, D. S. (2005). Bidirectional synaptic plasticity regulated by phosphorylation of stargazin-like TARPs. Neuron. doi:10.1016/j.neuron.2005.01.009
- Vierra, N. C., et al. (2023). Endoplasmic reticulum-plasma membrane junctions couple electrical activity to Ca2+-activated PKA signaling in neurons. Nature Communications. doi:10.1038/s41467-023-40930-6
- Biswas, D., et al. (2023). The landscape of the human brain phosphoproteome reveals region-specific phosphorylation events. Journal of Proteome Research. doi:10.1021/acs.jproteome.2c00244
