# Site Deepening Audit (2026-03-22, Front-Door Electrical-State Gap)

## 対象

- 主対象: `index.md`
- 副対象: `faq.md`

## 今回の選定理由

- `verification.md` と `wbe_101.md` では、すでに `chemical connectome is not electrical-state complete` が明文化されていました。
- しかし公開トップページ群では、この論点の露出がまだ弱く、入口だけ読む読者には `chemical wiring + inhibitory edge list` が fast synchrony や oscillatory coordination までかなり固定するかのように読める余地が残っていました。
- 技術・自然科学の観点では、この段差は危険です。理由は、`gap-junction coupling`、`endogenous field effect`、`local inhibitory driving force`、`human perturbation clue` が同じ inferential object ではないからです。

## 根拠付き批判

### 1. 現行 front door は chemical connectome と electrical-state ceiling の差を十分に止めていませんでした

- 問題:
  - `index.md` は ionic, myelin, thermal, bioenergetic, astrocyte, clearance の route differences を入口でよく止めていました。
  - その一方で、`shared extracellular / electrical state` については同じ粒度の front-door note がなく、`connectome-complete != emulation-complete` の一般論の中に埋もれていました。
- 根拠:
  - Galarreta & Hestrin (1999) は neocortical fast-spiking interneuron network の electrical synapses を示しました。
  - Anastassiou et al. (2011) は endogenous extracellular field が cortical spike timing を causally bias しうることを示しました。
  - Yang et al. (2024) は activity-dependent electrical synapses が persistent oscillations を支えうることを示しました。
  - Selfe et al. (2024) は inhibitory driving force を直接測るには specialized local optical route が要ることを示しました。
- 批判:
  - したがって、`chemical connectome` と `electrical-state regime` は同じ箱ではありません。
  - 入口でここを止めないと、読者は `graph plus nominal inhibition` を `fast synchrony もかなり固定された` と誤読できます。

### 2. FAQ の connectome-insufficiency answer は electrical-state family を十分に前面化していませんでした

- 問題:
  - `faq.md` の `Q2c` は connectome insufficiency の説明として非常に重要ですが、現行版では thermal, ionic, energetic, astrocyte, clearance を詳しく書く一方で、`shared extracellular / electrical state` が明示的な専用段落を持っていませんでした。
- 根拠:
  - Burman et al. (2023) は active cortical networks が fast synaptic inhibition を shunting mode に寄せうることを in vivo で示しました。
  - Selfe et al. (2024) は direct inhibitory driving-force measurement が専用の局所光学計測を要することを示しました。
- 批判:
  - これでは `inhibitory edge exists` と `that edge currently acts with the same driving force and synchrony consequence` の差が短い説明では見えません。
  - FAQ は最初の誤読を止めるページですから、この欠落は site-level reasoning rule の弱点でございました。

### 3. Human evidence は direct readout ではなく perturbation-conditioned clue として止める必要があります

- 問題:
  - electrical-state について、human side で現在どこまで言えるかが入口ページでは十分に固定されていませんでした。
- 根拠:
  - Feld et al. (2026) は mefloquine 前投与が declarative-memory retention と spindle-to-slow-oscillation coupling を損ねることを示しました。
  - ただし同論文自身が off-target effects を完全には除外しておらず、local electrical coupling の direct readout ではありません。
- 批判:
  - よって human evidence は `electrical coupling can matter` の perturbation clue にはなっても、`which cells were electrically coupled` や `local inhibitory driving force was identified` には上がりません。
  - この ceiling を入口で固定しないと、human sleep-memory paper が electrical-state observability progress に誤昇格します。

## 今回実行した変更

- `index.md`
  - `page_highlights` に `electrical-state evidence is not one class` の bullet を追加しました。
  - `known_points` に `chemical connectome plus nominal inhibitory edges != electrical-state complete` の bullet を追加しました。
  - ionic note の直後に front-door note を追加し、gap junction, ephaptic field, inhibitory driving force, human perturbation clue を分離しました。
- `faq.md`
  - `page_highlights` と `known_points` に electrical-state ceiling を追加しました。
  - `Q2c` に dedicated paragraph を追加し、connectome insufficiency の短い答えでも electrical-state family が見えるようにしました。
  - references に Galarreta & Hestrin (1999), Anastassiou et al. (2011), Burman et al. (2023), Yang et al. (2024), Selfe et al. (2024), Feld et al. (2026) を追加しました。

## 外部依存で保留

- spontaneous human same-subject benchmark for local electrical-state observability
  - 担当者: simultaneous invasive / noninvasive electrophysiology dataset designers
  - 前提条件: same-subject benchmark linking local electrical coupling or inhibitory driving-force measurements to human macro field or perturbation readouts
  - 完了条件: public benchmark showing which human route actually reduces which electrical-state uncertainty term

## 参考文献

1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/99496
2. Anastassiou CA, Perin R, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nature Neuroscience*. 2011;14(2):217-223.
   - https://doi.org/10.1038/nn.2727
3. Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ. Active cortical networks promote shunting fast synaptic inhibition in vivo. *Neuron*. 2023;111(22):3531-3540.e6.
   - https://doi.org/10.1016/j.neuron.2023.08.005
4. Yang Y-C, Wang G-H, Chou P, Hsueh S-W, Lai Y-C, Kuo C-C. Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. *PNAS*. 2024;121(8):e2313042121.
   - https://doi.org/10.1073/pnas.2313042121
5. Selfe JS, et al. All-optical reporting of inhibitory receptor driving force in the nervous system. *Nature Communications*. 2024;15:8913.
   - https://doi.org/10.1038/s41467-024-53074-y
6. Feld GB, Niethard N, Liu J, et al. Electrical Synapses Contribute to Sleep-Dependent Declarative Memory Retention. *European Journal of Neuroscience*. 2026;63(2):e70401.
   - https://doi.org/10.1111/ejn.70401
