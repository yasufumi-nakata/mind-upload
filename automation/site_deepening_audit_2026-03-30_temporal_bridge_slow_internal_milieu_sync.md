# Site Deepening Audit (2026-03-30, temporal / bridge slow internal-milieu sync)

## 対象

- 主対象:
  - `wiki/state-trait-and-drift.md`
  - `wiki/state-continuity-bridge.md`
- 同期対象:
  - `glossary.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学、法学、制度論

## 今回この箇所を選んだ理由

- 2026-03-30 時点で、front door 側と closed-loop 側ではすでに
  - `low latency != solved body / environment boundary`
  - `fast loop disclosure != slow internal-milieu disclosure`
  という停止線が明文化されておりました。
- しかし、時間方向の厳密ページである
  - `wiki/state-trait-and-drift.md`
  - `wiki/state-continuity-bridge.md`
  には、まだ `slow internal milieu`
  - circadian phase
  - glucocorticoid / steroid exposure
  - insulin / metabolic regime
  を独立の state-setting variable として扱う記述が十分に入っておりませんでした。
- この欠落は技術・自然科学の観点で危険でございます。理由は、同じ task、同じ visible fast loop、同じ decoder window でも、hippocampal retrieval や plasticity machinery が別 regime に入っている可能性を読者が見落としうるからでございます。

## 主要結論

- `state annotation` は movement / arousal / task mode だけでは不十分でございます。
- `same-subject` / `same-brain` / `same live stack` も、それだけでは `same regime` を保証いたしません。
- よって site rule 上は、時間方向の主張を読む際に少なくとも次を分ける必要がございます。
  - fast labels
  - slow internal milieu
  - biological drift
  - interface / decoder drift
- safe ceiling は以下でございます。
  - `same task` や `same fast loop` が示せても、slow internal-milieu disclosure がなければ `same operating regime` までは言えない
  - `cross-day reacquisition that still decodes` があっても、slow internal milieu が latent なら `same-state continuity` までは言えない

## 根拠付き批判

### 1. glucocorticoid state は visible loop が同じでも retrieval regime を変えます

- [de Quervain et al. (1998)](https://doi.org/10.1038/29542) は glucocorticoids が long-term spatial-memory retrieval を impair することを示しました。
- [Oei et al. (2007)](https://doi.org/10.1007/s11682-007-9003-2) は hydrocortisone により human hippocampal / prefrontal retrieval activity が低下することを示しました。

批判:

- したがって `same task + same subject + same fast interface` は `same retrieval regime` を意味しません。
- temporal page や bridge page が steroid / glucocorticoid state を explicit に要求しないままだと、bridge continuity が過大評価されます。

### 2. circadian timing は hippocampal plasticity machinery 自体を動かします

- [McCauley et al. (2020)](https://doi.org/10.1016/j.celrep.2020.108255) は hippocampal CA1 における neuron / astrocyte coupling と synaptic plasticity が circadian に modulate されることを示しました。
- [Barone et al. (2023)](https://doi.org/10.1126/sciadv.adj1010) は synaptic BMAL1 phosphorylation が circadian hippocampal plasticity を gate することを示しました。
- [Birnie et al. (2023)](https://doi.org/10.1073/pnas.2211996120) は corticosteroid treatment が hippocampal clock-linked plasticity and memory を disrupt する mechanistic chain を示しました。

批判:

- したがって `day-night` を一言書くだけでは不十分でございます。
- `circadian phase` と `corticosteroid rhythm / disruption` は、movement や arousal と別の state-setting variable として扱う必要がございます。

### 3. insulin / metabolic regime も human memory-side state を変えます

- [Benedict et al. (2004)](https://doi.org/10.1016/j.psyneuen.2004.04.003) は intranasal insulin による human memory 改善を示しました。
- [Reger et al. (2008)](https://doi.org/10.3233/JAD-2008-13309) は memory-impaired older adults で dose-dependent memory modulation を示しました。
- [Sherman et al. (2015)](https://doi.org/10.1016/j.neuropsychologia.2015.07.020) は circadian-rhythm consistency と hippocampal activity / memory の関連を示しました。

批判:

- よって `same decoder horizon` や `same repeated task` があっても、feeding / fasting / glucose-insulin regime や rhythm consistency が異なれば、same-regime continuity は自動では成立いたしません。

## 今回実行した変更

- `wiki/state-trait-and-drift.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` に slow internal-milieu split を追加しました。
  - `2026-03-30 addendum` を新設し、slow internal milieu を `state annotation` の一部として明文化しました。
  - temporal-validity fields の `state annotation` 行を、circadian / glucocorticoid / insulin-metabolic disclosure を含む形へ拡張しました。
  - `What the primary literature now supports` の冒頭を増補し、fast labels と slow internal milieu を分離しました。
  - `Minimum submission`、`Common misreadings`、`Operating rules` に同 stop line を反映しました。
- `wiki/state-continuity-bridge.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter に slow internal-milieu bridge burden を追加しました。
  - `2026-03-30 addendum` を新設し、bridge continuity が fast loop だけでは止まらないことを明示しました。
  - `Regime continuity` の定義に circadian / steroid / insulin-metabolic disclosure を追加しました。
  - `Cross-day or within-day reacquisition` 節を増補し、slow internal-milieu drift を bridge failure mode として書き込みました。
  - risk matrix、card stacking、misreading table に同 stop line を反映しました。
- `glossary.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - top-level highlights / known points に `fast labels versus slow internal milieu` を追加しました。
  - route-card note 群の近くに temporal-word guidance を追加しました。
  - 新規 term `Slow internal milieu` を追加し、`State-Continuity Bridge Card` と `Maintenance-state` の定義も同期しました。

## 今回止めた誤読

- `same task + same latency` = `same biological regime`
- `same-day success` = `state annotation は movement / arousal だけで十分`
- `cross-day reacquisition still decodes` = `same-state continuity`
- `same live stack` = `circadian / glucocorticoid / insulin-metabolic regime も同じ`
- `maintenance-state` と `slow internal milieu` の未分化な混同

## 外部依存タスク

- なし
  - 今回の変更は web 上の一次文献確認、公開ページ改稿、wiki export / site build 検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. de Quervain DJF, Roozendaal B, McGaugh JL. Stress and glucocorticoids impair retrieval of long-term spatial memory. *Nature*. 1998;394:787-790.
   - https://doi.org/10.1038/29542
2. Oei NYL, Elzinga BM, Wolf OT, de Ruiter MB, Damoiseaux JS, Kuijer JPA, Veltman DJ, Scheltens P, Rombouts SARB. Glucocorticoids decrease hippocampal and prefrontal activation during declarative memory retrieval in young men. *Brain Imaging and Behavior*. 2007;1:31-41.
   - https://doi.org/10.1007/s11682-007-9003-2
3. McCauley JP, Petroccione MA, D'Brant LY, et al. Circadian modulation of neurons and astrocytes controls synaptic plasticity in hippocampal area CA1. *Cell Reports*. 2020;33:108255.
   - https://doi.org/10.1016/j.celrep.2020.108255
4. Barone I, Gillette NM, Hawks-Mayer H, et al. Synaptic BMAL1 phosphorylation controls circadian hippocampal plasticity. *Science Advances*. 2023;9:eadj1010.
   - https://doi.org/10.1126/sciadv.adj1010
5. Birnie MT, Begum G, Sugden D, et al. Circadian regulation of hippocampal function is disrupted with corticosteroid treatment. *Proceedings of the National Academy of Sciences of the United States of America*. 2023;120:e2211996120.
   - https://doi.org/10.1073/pnas.2211996120
6. Benedict C, Hallschmid M, Hatke A, Schultes B, Fehm HL, Born J, Kern W. Intranasal insulin improves memory in humans. *Psychoneuroendocrinology*. 2004;29:1326-1334.
   - https://doi.org/10.1016/j.psyneuen.2004.04.003
7. Reger MA, Watson GS, Green PS, et al. Intranasal insulin administration dose-dependently modulates verbal memory and plasma amyloid-beta in memory-impaired older adults. *Journal of Alzheimer's Disease*. 2008;13:323-331.
   - https://doi.org/10.3233/JAD-2008-13309
8. Sherman SM, Mumford JA, Schnyer DM. Hippocampal activity mediates the relationship between circadian activity rhythms and memory in older adults. *Neuropsychologia*. 2015;75:617-625.
   - https://doi.org/10.1016/j.neuropsychologia.2015.07.020
