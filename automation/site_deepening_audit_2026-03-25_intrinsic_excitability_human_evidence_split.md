# Site Deepening Audit (2026-03-25, Intrinsic Excitability Human-Evidence Split)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `index.md`
- 副対象: `verification.md`
- Scope: 技術 / 自然科学のみ

## 今回この論点を選んだ理由

- 公開サイトはすでに `intrinsic excitability / homeostatic set point` を hidden-state family としては分離できておりました。
- しかし human 側の evidence だけは、まだ `living-human perturbation-conditioned proxy` に寄りすぎておりました。
- この整理は不十分です。一次文献を確認すると、human 側には少なくとも次の 2 系統がございます。
  - `local clinical-unit route`
  - `noninvasive perturbation-conditioned proxy`
- ここを分けないと、`human evidence exists` という文言が
  - 局所・侵襲・臨床条件付き single-unit readout
  - 非侵襲・state-dependent・motor / corticospinal assay proxy
  を同じ種類の前進として見せてしまいます。

## 根拠付き批判

### 1. human intrinsic-excitability evidence は one-bucket ではございません

- [Tallman et al. (2025)](https://doi.org/10.1038/s41598-025-21967-7) は、てんかん患者の海馬 single-unit 記録を用い、encoding 時の relative firing increase を示した remembered item だけで sparse episodic-memory code が立つことを示しました。
- ただし同論文自身が、human では excitability の direct measure は困難であり、firing は indirect index にすぎないと明記しております。
- したがって、これは `human local clinical-unit allocation route` と読むのが適切であり、`whole-brain excitability evidence` ではございません。

### 2. noninvasive human route は別の inferential object を見ています

- [Huber et al. (2013)](https://doi.org/10.1093/cercor/bhs014) は time awake に応じた cortical excitability change を示しました。
- [Kuhn et al. (2016)](https://doi.org/10.1038/ncomms12455) は sleep deprivation 後の TMS / PAS / EEG 指標から、human cortex における homeostatic / associative plasticity の recalibration を示しました。
- [Zrenner et al. (2018)](https://doi.org/10.1016/j.brs.2017.11.016) は EEG-defined excitability state が TMS-induced plasticity efficacy を変えることを示しました。
- [Khatri et al. (2025)](https://doi.org/10.1016/j.brs.2024.12.1193) は personalized whole-brain EEG pattern から real-time に strong / weak CST state を当て、MEP の大きさと分散を変えられることを示しました。

批判:

- これらは重要な human progress ですが、direct observable は motor / corticospinal assay outcome や plasticity efficacy であり、AIS geometry、ion-channel distribution、cell-specific recovery controller ではございません。
- よって `human route` を 1 本の proxy 行として書くと、local clinical-unit route と noninvasive perturbation-conditioned route の claim ceiling が混ざります。

### 3. site の stop line は human evidence class を明示しないと弱いままです

- 既存の route card は `claim family`、`physiological locus`、`time axis` をよく分けておりました。
- しかし human 側に限っては `proxy` の語が広すぎ、局所侵襲 route と非侵襲 state-conditioned route を峻別できておりませんでした。

批判:

- これでは、読者が `human excitability evidence` を見たときに
  - どこまでが local readout か
  - どこからが perturbation-conditioned proxy か
  - 何が依然 latent か
  を読み分けにくくなります。
- 科学的に正しい止め方は `human evidence class / proxy class` を route-card field として固定することです。

## 今回実行した変更

### 1. `wiki/homeostatic-plasticity-and-maintenance-state.md`

- `intrinsic-excitability-route-card` の addendum を更新し、human 側を
  - `human hippocampal single-unit allocation route`
  - `noninvasive living-human perturbation-conditioned proxy routes`
  に分けました。
- route-card field を `Human evidence class / proxy class` に更新しました。
- `Why this route card is necessary here` に Tallman と Khatri を加え、human directness の差を本文で固定しました。
- human observability table に `human clinical single-unit allocation route` 行を追加しました。
- `human state-gated perturbation proxy` 行に Khatri を追加しました。
- calibrator-role matrix に `Clinical single-unit hippocampal route` 行を追加しました。

### 2. `wbe_101.md`

- entry-point note を更新し、human 側を `clinical single-unit route` と `noninvasive proxy route` に分けました。
- route card の required fields を `human evidence class / proxy class` に更新しました。

### 3. `index.md`

- front-door note を更新し、Tallman を human local-unit route として追加しました。
- `one excitability paper` を whole-brain controller map に読まない stop lineを明確化しました。

### 4. `verification.md`

- page highlight と addendum の field 名を `human evidence class / proxy class` に更新しました。
- addendum 本文に Tallman と Khatri を追加し、submission 側でも human route の分割を要求する形へ修正しました。

## その結果、このサイトで何が改善されたか

- `human intrinsic-excitability evidence` を見たときに、読者は
  - local clinical-unit readout なのか
  - noninvasive perturbation-conditioned proxy なのか
  を最初に確認できるようになりました。
- その結果、
  - `human single-unit evidence exists`
  - `real-time EEG-TMS control works`
  をどちらも `human excitability solved` に圧縮する読み違いを止められます。
- これは WBE 文脈で特に重要です。なぜなら、局所 human evidence が増えても、それだけで same-subject whole-brain controller identification には進まないからです。

## 外部依存で保留

- なし
- 今回の変更は、公開本文・verification rule・wiki の human ladder・監査記録の更新で完結しております。

## 参考文献

1. Yiu AP, et al. Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. *Neuron*. 2014;83(3):722-735.
   - https://doi.org/10.1016/j.neuron.2014.07.017
2. Hadzibegovic N, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025;17:291.
   - https://doi.org/10.1038/s41467-025-66975-3
3. Benoit CM, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02152-5
4. Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016;165(1):180-191.
   - https://doi.org/10.1016/j.cell.2016.01.046
5. Tallman CW, Siler SN, Lee H, et al. Neuronal allocation and sparse coding of episodic memories in the human hippocampus. *Scientific Reports*. 2025;15:21967.
   - https://doi.org/10.1038/s41598-025-21967-7
6. Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
   - https://doi.org/10.1093/cercor/bhs014
7. Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
   - https://doi.org/10.1038/ncomms12455
8. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
   - https://doi.org/10.1016/j.brs.2017.11.016
9. Khatri UU, Pulliam K, Manesiya M, Vieyra Cortez M, Millán J del R, Hussain SJ. Personalized whole-brain activity patterns predict human corticospinal tract activation in real-time. *Brain Stimulation*. 2025;18(1):64-76.
   - https://doi.org/10.1016/j.brs.2024.12.1193
10. Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
   - https://doi.org/10.1016/j.neuroimage.2026.121723
