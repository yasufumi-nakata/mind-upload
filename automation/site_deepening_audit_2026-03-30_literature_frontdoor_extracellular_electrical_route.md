# Site Deepening Audit (2026-03-30, literature front door extracellular / electrical-state route)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 同期先として確認したページ:
  - `index.md`
  - `wbe_101.md`
  - `verification.md`
  - `wiki/connectome-is-not-enough.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## web確認対象

- `https://doi.org/10.1038/47029`
- `https://doi.org/10.1038/nn.2727`
- `https://doi.org/10.1523/JNEUROSCI.4493-13.2014`
- `https://doi.org/10.1002/jnr.20871`
- `https://doi.org/10.1126/science.1241224`
- `https://doi.org/10.1016/j.neuroimage.2020.116682`
- `https://doi.org/10.1111/ejn.70401`

## 今回この箇所を選んだ理由

- `index.md`、`wbe_101.md`、`verification.md`、`wiki/connectome-is-not-enough.md` では、`shared extracellular / electrical state` を
  - gap-junction coupling
  - endogenous-field / ephaptic effect
  - extracellular-space geometry / diffusion-barrier / osmotic regime
  - bounded human diffusion-MRI clue
  - perturbation-conditioned human clue
  に分ける stop rule がすでに導入されておりました。
- しかし technical readers が最初に入る `mind_uploading_papers.md` と `research_harvest_50.md` では、その split がまだ前景化されておらず、U3 の文献導線だけが古い圧縮を残しておりました。
- その結果、archive 側から入った読者には
  - `electrical-state`
  - `sleep-linked extracellular-space change`
  - `human diffusion clue`
  が一段に見え、route-family の違いが落ちておりました。

## 主要結論

- literature front door でも、`shared extracellular / electrical state` は少なくとも次の 5 分割で読ませる必要がございました。
  - gap-junction coupling network
  - endogenous-field / ephaptic route
  - extracellular-space geometry / diffusion-barrier / osmotic regime
  - sleep-linked interstitial-space proxy
  - bounded human diffusion-MRI or perturbation clue
- よって archive / evidence-bank の safe ceiling は
  - `shared extracellular / electrical-state route-family split`
  として固定し、
  - `one electrical-state meter`
  - `one human route to current extracellular state`
  を禁止する必要がございました。

## 根拠付き批判

### 1. electrical coupling と extracellular geometry は同じ inferential object ではございません

- [Galarreta & Hestrin (1999)](https://doi.org/10.1038/47029) は、neocortical fast-spiking cells の `gap-junction coupling network` を示しました。
- [Anastassiou et al. (2011)](https://doi.org/10.1038/nn.2727) は、physiological field fluctuations が `ephaptic` に spike timing を bias しうることを示しました。
- [Graydon et al. (2014)](https://doi.org/10.1523/JNEUROSCI.4493-13.2014) は、局所 extracellular volume fraction と geometry が transmitter dilution と spillover を変えることを示しました。

批判:

- したがって `electrical-state` という 1 語で
  - coupling topology
  - field effect
  - extracellular dilution geometry
  をまとめるのは粗すぎます。
- literature front door でこの分割が見えないと、読者は `connectome is missing some electrical detail` 程度に矮小化してしまいます。

### 2. extracellular-space change は rewiring なしでも excitability と exchange を動かします

- [Kilb et al. (2006)](https://doi.org/10.1002/jnr.20871) は、hypoosmolar 条件で ECS volume fraction が低下し、epileptiform activity susceptibility が上がることを示しました。
- [Xie et al. (2013)](https://doi.org/10.1126/science.1241224) は、sleep/anesthesia で interstitial space が拡大し、CSF-interstitial exchange が増えることを示しました。

批判:

- これは `same synapse graph` でも
  - osmotic regime
  - sleep-linked interstitial-space width
  - exchange condition
  が変われば、局所ダイナミクスの意味が変わることを意味します。
- 文献 front door にこの stop rule がないと、U3 文献の読みが `controller variables matter` で止まり、medium が state variable であることが見えません。

### 3. human evidence は bounded clue であり one route ではございません

- [Voldsbekk et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116682) は、wakefulness に伴う human white matter diffusion 変化を extracellular-space explanation と整合的な bounded proxy clue として示しました。
- [Feld et al. (2026)](https://doi.org/10.1111/ejn.70401) は、mefloquine による electrical-synapse blockade が declarative-memory retention と spindle-to-slow-oscillation coupling を損なうことを示しましたが、薬理学的 caveat も明示しております。

批判:

- したがって human route は
  - diffusion-MRI proxy clue
  - pharmacological perturbation clue
  のように ceiling が違います。
- これを `human electrical-state evidence` とまとめるのは不正確でございます。

### 4. archive と evidence bank の U3 導線だけが site-wide stop rule から遅れておりました

- 公開 front door ではすでに `shared extracellular / electrical state` の split が固定されております。
- しかし literature front doors では
  - `maintenance-state family split`
  - `neuromodulatory split`
  - `neurovascular / BBB split`
  はあっても、
  - `shared extracellular / electrical-state split`
  が front-door row と note の形で未配置でした。

批判:

- これは導線の非対称でございます。
- 入口ページでは止めている過読が、archive 入口だけで再流入しておりました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `known_points` と `page_highlights` に `shared extracellular / electrical-state` route-family split を追加しました。
  - technical fast lane 冒頭に新規 note box `Shared extracellular / electrical-state papers are not one maintenance route` を追加しました。
  - main fast-lane table に `shared extracellular / electrical-state route split` row を追加しました。
  - `2025-2026 technical-only shortlist` にも同 route row を追加しました。
- `research_harvest_50.md`
  - `page_highlights` と `known_points` に U3 の `shared extracellular / electrical-state` split を追加しました。
  - priority-route table の `maintenance-state family split` 行を更新しました。
  - 新規 note box `Read shared extracellular / electrical-state papers as a separate U3 route` を追加しました。
  - paper-anchor note に同 route-family split を追記しました。

## 今回止めた誤読

- `shared extracellular / electrical state = one maintenance variable`
- `electrical-state paper = coupling + field + extracellular geometry を一括で測った`
- `human diffusion-MRI clue = direct human extracellular-state readout`
- `mefloquine sleep result = local electrical-synapse ground truth`
- `U3 maintenance papers = controller biology だけで medium / geometry は補助背景`

## 外部依存タスク

- なし
  - 今回の作業は一次文献確認、公開文面改稿、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/47029
2. Anastassiou CA, Perin R, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nature Neuroscience*. 2011;14:217-223.
   - https://doi.org/10.1038/nn.2727
3. Graydon CW, Cho S, Diamond JS, Kachar B, von Gersdorff H, Grimes WN. Specialized postsynaptic morphology enhances neurotransmitter dilution and high-frequency signaling at an auditory synapse. *Journal of Neuroscience*. 2014;34(24):8358-8372.
   - https://doi.org/10.1523/JNEUROSCI.4493-13.2014
4. Kilb W, Dierkes PW, Syková E, Vargová L, Luhmann HJ. Hypoosmolar conditions reduce extracellular volume fraction and enhance epileptiform activity in the CA3 region of the immature rat hippocampus. *Journal of Neuroscience Research*. 2006;84(1):119-129.
   - https://doi.org/10.1002/jnr.20871
5. Xie L, Kang H, Xu Q, Chen MJ, Liao Y, Thiyagarajan M, O'Donnell J, Christensen DJ, Nicholson C, Iliff JJ, Takano T, Deane R, Nedergaard M. Sleep drives metabolite clearance from the adult brain. *Science*. 2013;342(6156):373-377.
   - https://doi.org/10.1126/science.1241224
6. Voldsbekk I, Maximov II, Zak N, Roelfs D, Geier O, Due-Tønnessen P, Elvsåshagen T, Strømstad M, Bjørnerud A, Groote I. Evidence for wakefulness-related changes to extracellular space in human brain white matter from diffusion-weighted MRI. *NeuroImage*. 2020;212:116682.
   - https://doi.org/10.1016/j.neuroimage.2020.116682
7. Feld GB, Niethard N, Liu J, et al. Electrical Synapses Contribute to Sleep-Dependent Declarative Memory Retention. *European Journal of Neuroscience*. 2026;63(2):e70401.
   - https://doi.org/10.1111/ejn.70401
