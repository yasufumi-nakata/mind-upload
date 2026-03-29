# Site Deepening Audit (2026-03-30, mind-upload-basics front-door sync)

## 対象

- 主対象:
  - `wiki/mind-upload-basics.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学、法学、制度論

## web確認対象

- `https://doi.org/10.1038/s41586-025-08790-w`
- `https://doi.org/10.1038/s41586-025-08840-3`
- `https://doi.org/10.1038/s41586-025-08805-6`
- `https://doi.org/10.1038/s41467-024-53901-2`
- `https://doi.org/10.1038/s41593-025-02080-4`
- `https://doi.org/10.1038/29542`
- `https://doi.org/10.1007/s11682-007-9003-2`
- `https://doi.org/10.1126/sciadv.adj1010`
- `https://doi.org/10.1073/pnas.2211996120`
- `https://doi.org/10.1038/47029`
- `https://doi.org/10.1523/JNEUROSCI.4493-13.2014`
- `https://doi.org/10.1016/j.neuroimage.2020.116682`

## 今回この箇所を選んだ理由

- 深いページ側では、2026-03-30 時点までに
  - `same-brain functional connectomics ≠ solved local twin`
  - `low latency ≠ solved body / environment boundary`
  - `chemical connectome ≠ shared extracellular / electrical-state complete`
  という stop-rule がかなり厳密に整理されておりました。
- しかし初心者向け入口である `wiki/mind-upload-basics.md` は、2026-03-29 更新のままで、
  - same-brain connectomics / digital-twin ceiling
  - fast loop と slow internal milieu の分離
  - extracellular-space geometry / diffusion barrier / osmotic regime
  の 3 点が front door で十分に再圧縮されておりませんでした。
- このズレは単なる表現の古さではありません。入口ページで粗いままだと、深いページで止めた誤読が最初の数分で再注入されるからでございます。

## 主要結論

- 今回もっとも改善優先度が高かったのは、新しい論文をさらに一枚加えることではなく、`初心者向け入口の scientific stop-rule を深いページの現在地に同期すること` でございました。
- 2026-03-30 時点の site-wide rule に照らすと、`wiki/mind-upload-basics.md` には少なくとも次の 3 点を明示する必要がありました。
  - `same-brain functional connectomics` は sequential local scaffold と task-bounded conditional predictor まで
  - `closed loop` は fast loop disclosure と slow internal-milieu disclosure を分ける
  - `chemical connectome` は extracellular / electrical-state family をなお欠く
- よって beginner page の改稿対象としては、このページが最もレバレッジが高いと判断いたしました。

## 根拠付き批判

### 1. same-brain functional connectomics を beginner page で止め切れていませんでした

- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) は、in vivo neurophysiology の後に same volume of cortex を ex vivo EM で取得する sequential same-brain pipeline を示しました。
- [Ding et al. (2025)](https://doi.org/10.1038/s41586-025-08840-3) は、その stack を使って validated stimulus-conditioned response model から一般 wiring rule を強めました。
- [Gamlin et al. (2025)](https://doi.org/10.1038/s41586-025-08805-6) は predicted transcriptomic types を connectomics に持ち込みましたが、direct transcriptomic assay in the EM volume ではございません。
- [Mittermaier et al. (2024)](https://doi.org/10.1038/s41467-024-53901-2) は human neocortical tissue で membrane-potential state が synaptic consolidation を gate することを示しました。
- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は connectome-constrained network でも dynamics がなお縮退しうることを示しました。

批判:

- beginner page がこれを front door で言わないままだと、
  - `same-brain`
  - `digital twin`
  - `predicted transcriptomic type`
  - `local twin`
  が一段で読まれます。
- しかし現在地の一次文献が支持する ceiling は、`sequential local scaffold + conditional predictor` までであり、
  - direct transcriptomic truth
  - current synaptic-state readout
  - unique local dynamics
  ではございません。

### 2. low latency の beginner 説明が fast loop 側に偏っておりました

- [de Quervain et al. (1998)](https://doi.org/10.1038/29542) は glucocorticoids が retrieval を impair することを示しました。
- [Oei et al. (2007)](https://doi.org/10.1007/s11682-007-9003-2) は hydrocortisone により hippocampal / prefrontal retrieval activity が低下することを示しました。
- [Barone et al. (2023)](https://doi.org/10.1126/sciadv.adj1010) は synaptic BMAL1 phosphorylation による circadian hippocampal plasticity control を示しました。
- [Birnie et al. (2023)](https://doi.org/10.1073/pnas.2211996120) は corticosteroid treatment により circadian regulation of hippocampal function が乱れ、memory impairment が生じることを示しました。

批判:

- したがって `same actuator + same loop latency` は `same operating regime` を意味しません。
- beginner page で `body / environment boundary` を語るなら、
  - sensory / motor / interoceptive fast loop
  - circadian / glucocorticoid / insulin-metabolic slow milieu
  を分けて読ませる必要がございました。

### 3. chemical connectome の beginner ceiling が extracellular / electrical family を十分に見せていませんでした

- [Galarreta & Hestrin (1999)](https://doi.org/10.1038/47029) は fast-spiking interneuron electrical-synapse network を示しました。
- [Graydon et al. (2014)](https://doi.org/10.1523/JNEUROSCI.4493-13.2014) は local extracellular geometry が neurotransmitter dilution と signaling を変えることを示しました。
- [Voldsbekk et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116682) は human white matter で wakefulness-related extracellular-space change と整合的な bounded diffusion-MRI clue を示しました。

批判:

- これにより、`chemical connectome + nominal inhibitory edges` は
  - electrical coupling
  - endogenous field effects
  - extracellular-space geometry / diffusion barrier
  - osmotic / wakefulness-linked ECS regime
  を閉じません。
- beginner page がここを front door で止めないと、connectome-only shortcut が再び入り込みます。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter の `page_highlights` と `known_points` に、上記 3 つの stop-rule を beginner-safe language で追加しました。
  - 新しい note-box `2026-03-30 correction: three beginner shortcuts this site no longer allows` を追加しました。
  - 同 note-box で
    - same-brain functional connectomics / digital-twin ceiling
    - fast loop versus slow internal milieu
    - shared extracellular / electrical-state ceiling
    を明文化しました。
  - follow-up route を
    - `wiki/connectome-is-not-enough.md`
    - `wiki/closed-loop-latency-jitter-and-safety-stops.md`
    - `wiki/measurement-stack-and-claim-ceiling.md`
    に結び直しました。
  - 参考文献へ今回の 12 本を追加しました。

## 今回止めた誤読

- `same-brain connectomics` = `solved local twin`
- `digital twin` = `direct current synaptic-state readout`
- `low latency` = `body / environment boundary mostly solved`
- `fast loop disclosure` = `slow endocrine / circadian stateも自動的に揃った`
- `chemical connectome` = `electrical-state or extracellular-state complete`

## 外部依存タスク

- なし
  - 今回の作業は web 上の一次文献確認、repo 内公開ページ改稿、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
2. Ding Z, et al. Functional connectomics reveals a general wiring rule in mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08840-3
3. Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08805-6
4. Mittermaier FX, Kalbhenn T, Xu R, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024;15:10340.
   - https://doi.org/10.1038/s41467-024-53901-2
5. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574.
   - https://doi.org/10.1038/s41593-025-02080-4
6. de Quervain DJ-F, Roozendaal B, McGaugh JL. Stress and glucocorticoids impair retrieval of long-term spatial memory. *Nature*. 1998;394:787-790.
   - https://doi.org/10.1038/29542
7. Oei NYL, Elzinga BM, Wolf OT, de Ruiter MB, Damoiseaux JS, Kuijer JPA, Veltman DJ, Scheltens P, Rombouts SARB. Glucocorticoids decrease hippocampal and prefrontal activation during declarative memory retrieval in young men. *Brain Imaging and Behavior*. 2007;1(1-2):31-41.
   - https://doi.org/10.1007/s11682-007-9003-2
8. Barone I, Gilette NM, Hawks-Mayer H, et al. Synaptic BMAL1 phosphorylation controls circadian hippocampal plasticity. *Science Advances*. 2023;9(43):eadj1010.
   - https://doi.org/10.1126/sciadv.adj1010
9. Birnie MT, Begum G, Sugden D, et al. Circadian regulation of hippocampal function is disrupted with corticosteroid treatment. *Proceedings of the National Academy of Sciences of the United States of America*. 2023;120(15):e2211996120.
   - https://doi.org/10.1073/pnas.2211996120
10. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/47029
11. Graydon CW, Cho S, Diamond JS, Kachar B, von Gersdorff H, Grimes WN. Specialized postsynaptic morphology enhances neurotransmitter dilution and high-frequency signaling at an auditory synapse. *Journal of Neuroscience*. 2014;34(24):8358-8372.
   - https://doi.org/10.1523/JNEUROSCI.4493-13.2014
12. Voldsbekk I, Maximov II, Zak N, Roelfs D, Geier O, Due-Tønnessen P, Elvsåshagen T, Strømstad M, Bjørnerud A, Groote I. Evidence for wakefulness-related changes to extracellular space in human brain white matter from diffusion-weighted MRI. *NeuroImage*. 2020;212:116682.
   - https://doi.org/10.1016/j.neuroimage.2020.116682
