# Site Deepening Audit (2026-04-02, human local-route vs proxy split)

## 対象

- 主対象: `wiki/human-proxy-composition.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `tech_roadmap.md`

## 今回この箇所を選んだ理由

- `wiki/homeostatic-plasticity-and-maintenance-state.md` ではすでに human-side excitability / maintenance evidence を
  - human clinical single-unit allocation route
  - human sleep-homeostasis / plasticity proxy
  - human state-gated perturbation proxy
  に分ける site-wide rule が見えていました。
- しかし front door として読まれやすい `wiki/human-proxy-composition.md`、`wiki/measurement-stack-and-claim-ceiling.md`、`tech_roadmap.md` では、この split がまだ十分に前面化されておりませんでした。
- その結果、読者が `human excitability evidence exists` を `one common human excitability meter exists` と誤読する余地が残っていました。

## 根拠付き批判

### 1. local human clinical-unit evidence と noninvasive perturbation evidence は別物でございます

- 根拠:
  - `Tallman et al. (2025)` は、てんかん患者海馬の single-unit 記録において、encoding 時の relative firing increase と episodic-memory sparse coding の関連を示しました。
  - ただし同論文は、firing を excitability の直接測定ではなく `indirect index` と位置づけております。
  - したがって、これは human clinical single-unit allocation-related route であり、whole-brain noninvasive route ではございません。
- 批判:
  - それにもかかわらず front door がこれを `human excitability evidence` の一部としてだけ扱うと、local pathology-conditioned unit evidence が whole-brain observability に近いように読めてしまいます。

### 2. sleep-history / plasticity recalibration と state-gated perturbation も同一行にはできません

- 根拠:
  - `Huber et al. (2013)` は time awake に応じた human cortical excitability change を示しました。
  - `Kuhn et al. (2016)` と `Fehér et al. (2026)` は、sleep deprivation や nap が PAS / TMS-EEG readout を再調整することを示しました。
  - `Zrenner et al. (2018)` と `Khatri et al. (2025)` は、EEG-defined あるいは personalized whole-brain state に依存して TMS-induced plasticity efficacy や corticospinal response が変化することを示しました。
- 批判:
  - 前者は sleep-history / plasticity-recalibration route、後者は state-gated perturbation route であり、direct observable、closed-loop burden、safe calibrator role が異なります。
  - それらを 1 行の `perturbation-conditioned human excitability` に圧縮すると、human route の claim ceiling を不当に高く読ませます。

### 3. front door の不整合は site-wide stop rule を破ります

- 観察:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` では human local-route split がすでに明文化されておりました。
  - しかし `wiki/human-proxy-composition.md` の route matrix と collapse-error rule、`wiki/measurement-stack-and-claim-ceiling.md` の human maintenance ladder、`tech_roadmap.md` の M3 table では、この split がまだ欠けておりました。
- 批判:
  - 深部ページで overread を止めても、front door で同じ混同を許せば public reading rule は再び崩れます。
  - これは技術的な observability ceiling の説明として不整合でございます。

## 今回実行した変更

- `wiki/human-proxy-composition.md`
  - front matter を `2026-04-02 human local-route split` に更新しました。
  - `human excitability evidence` を one reusable row にしてはならないという correction note を追加しました。
  - route matrix に
    - `Human clinical single-unit allocation route`
    - `Human sleep-homeostasis / plasticity proxy`
    - `Human state-gated perturbation proxy`
    を追加しました。
  - collapse-errors table に `Human excitability-route collapse` を追加し、section title を count-fixed wording へ更新しました。
  - promotion rule に `Human evidence class of each perturbation-conditioned row` を追加しました。
  - references に `Tallman (2025)`、`Huber (2013)`、`Kuhn (2016)`、`Zrenner (2018)`、`Khatri (2025)`、`Fehér (2026)` を同期しました。

- `wiki/measurement-stack-and-claim-ceiling.md`
  - front matter の note / highlights / known points に human local-route split を追加しました。
  - `Human maintenance-state routes also form a ladder` の導入段落に `Tallman (2025)` と `Khatri (2025)` を加え、human excitability-side evidence が 3 ルートに分かれることを明示しました。
  - ladder table に
    - `Human clinical single-unit allocation route`
    - `Human sleep-homeostasis / plasticity proxy`
    - `Human state-gated perturbation proxy`
    を separate rows として記載しました。
  - `Site rule for human proxy classes` と calibrator-role note も同 split に合わせて改稿しました。
  - references に `Tallman (2025)` と `Khatri (2025)` を追加しました。

- `tech_roadmap.md`
  - `last_updated` を `2026-04-02` に更新しました。
  - page highlights / known points に `human excitability evidence is not one row` を追加しました。
  - M3 addendum に `Tallman (2025)`、`Huber (2013)`、`Kuhn (2016)`、`Fehér (2026)`、`Zrenner (2018)`、`Khatri (2025)` を追加し、local clinical-unit route と noninvasive perturbation-conditioned routes を分離しました。
  - M3 table に同 3 rows を追加しました。
  - references を同期しました。

## 外部依存で保留

- なし
  - 今回の修正は repo 内の本文更新、監査メモ、build 検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Tallman CW, Siler SN, Lee H, et al. Neuronal allocation and sparse coding of episodic memories in the human hippocampus. *Scientific Reports*. 2025;15:21967.
   - https://doi.org/10.1038/s41598-025-21967-7
2. Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
3. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
4. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
5. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
6. Khatri UU, Pulliam K, Manesiya M, Vieyra Cortez M, Millán J del R, Hussain SJ. Personalized whole-brain activity patterns predict human corticospinal tract activation in real-time. *Brain Stimulation*. 2025;18(1):64-76.
   - https://doi.org/10.1016/j.brs.2024.12.1193
