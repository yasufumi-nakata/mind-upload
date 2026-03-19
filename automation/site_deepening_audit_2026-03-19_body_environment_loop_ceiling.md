# Site Deepening Audit (2026-03-19, Body / Environment Loop Ceiling)

## 対象

- 主対象: `verification.md`
- 副対象: `tech_roadmap.md`
- 副対象: `wbe_101.md`
- 副対象: `faq.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイトは、`connectome-complete != state-complete`、`decode != emulate`、`latency != biological timing-state`、`DCM != causal wiring` など、脳内 hidden state と観測・推定の限界についてはかなり強く整理できていました。
- その一方で、`closed loop` と `body/environment` の関係は、公開入口ではまだ主に `低遅延・低ジッタ・安全停止` の問題として読める状態でした。
- これは技術・自然科学の観点で重要です。なぜなら、一次文献は、脳活動が body/environment から独立に完結しているのではなく、運動、自己運動、前庭・多感覚手掛かり、呼吸、arousal、触覚フィードバックなどにより再編されることを示しているからです。したがって `loop が速い` は `subject boundary が再現された` を意味しません。

## 根拠付き批判

### 1. 旧 L3 読解は `timing audit` を前景化し、`boundary audit` を十分に要求していませんでした

- 問題:
  - `verification.md` と `faq.md` は、L3 を主に latency / jitter / drift / safe-stop の監査として整理していました。
  - しかし、それだけでは `どの sensory / motor / interoceptive loop が保持されたか` が分かりません。
- 根拠:
  - Musall et al. (2019) は、single-trial neural dynamics が richly varied movements に強く支配されることを示しました。
  - Stringer et al. (2019) は、spontaneous behaviors が multidimensional, brainwide activity を駆動することを示しました。
- 批判:
  - したがって `loop is stable` を主張するなら、`何の loop か` を先に固定しなければなりません。
  - timing log だけでは `body/environment loop` の欠落を隠したまま local controller を強く読み上げる余地が残ります。

### 2. 旧 front door は `body/environment removal` が neural code を変えることを entry level で十分に示していませんでした

- 問題:
  - 旧 `wbe_101.md` と `tech_roadmap.md` は `environment` や `embodiment` という語を用いていましたが、主に implementation planning の語として扱っていました。
  - そのため、読者が `body/environment` を後段のオプション設計と読み、脳内 state-completeness と切り離して受け取る余地がありました。
- 根拠:
  - Saleem et al. (2013) は、mouse V1 が visual motion と locomotion を統合していることを示しました。
  - Ravassard et al. (2013) は、VR で vestibular and other sensory cues を落とすと hippocampal place-cell population activation と theta dynamics が real world と変わることを示しました。
- 批判:
  - これは `same brain, different body/environment loop` で neural representation 自体が変わりうることを意味します。
  - したがって subject boundary は哲学的注記ではなく、計測・検証の一次変数です。

### 3. 旧 closed-loop 読解は `interoceptive / organism-wide state` を body/environment boundary に含めていませんでした

- 問題:
  - 既存ページは pupil, HRV, autonomic confound には触れていましたが、body/environment boundary の本体としては位置付けていませんでした。
- 根拠:
  - Zelano et al. (2016) は、nasal respiration が human limbic oscillations を entrain し、memory retrieval を変えることを示しました。
  - Raut et al. (2025) は、brain-wide and body-wide physiology が low-dimensional arousal manifold により大きく組織されることを示しました。
- 批判:
  - したがって `brain-only fast loop` を `state-complete closed loop` と読むのは過大評価です。
  - 呼吸や arousal を含む organism-wide state を latent のままにするなら、その ceiling を本文で明示する必要がありました。

### 4. 旧 site は `feedback restored local control` と `embodiment solved` の差を十分に固定していませんでした

- 問題:
  - 既存ページは Flesher et al. (2021) などを local closed-loop advance として適切に高く評価していました。
  - しかし、その advancement が `局所 surrogate sensorimotor loop` の改善であることを、L3 一般ルールへは十分に落としていませんでした。
- 根拠:
  - Flesher et al. (2021) は tactile feedback を戻すことで robotic arm control が改善することを示しました。
- 批判:
  - これは `feedback channel matters` を支持しますが、同時に `どの feedback / body surrogate を戻したのか` を書かなければ claim ceiling が定まらないことも意味します。
  - よって public rule としては `Body / Environment Boundary Card` が必要でした。

## 今回実行した変更

- `verification.md`
  - `L3` の最小要件に `disclosed body / environment boundary` を追加しました。
  - `Body / Environment Boundary Card` セクションを新設し、required fields と minimum operating rule を明文化しました。
  - `Additional audit logs` に `Body / Environment Boundary Card` を追加しました。
- `tech_roadmap.md`
  - `M4` を全面補強し、subject boundary を measurement requirement として再定義しました。
  - `I6` を改稿し、embodiment を yes/no 語ではなく retained / substituted loop disclosure と ablation planning の問題へ変更しました。
  - `V2` の required logs に boundary card を加え、`U3` 現状欄を更新しました。
- `wbe_101.md`
  - page highlights / known points を更新し、`low latency != solved body/environment boundary` を front door に追加しました。
  - claim ladder の `L3` 定義を改稿しました。
  - `Low latency is not the whole L3 story` note-box を追加しました。
  - invasive / hybrid neuroprosthesis 行の missing column に `declared body / environment boundary` を追加しました。
- `faq.md`
  - technical guardrail を `5 -> 6` に更新しました。
  - 新規 Q&A `If latency is low, does that mean the body/environment problem is solved?` を追加しました。
  - FAQ 入口の overread block へ `body/environment boundary` を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・検証基準・参考文献の改稿で完結しています。

## 参考文献

1. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019;22:1677-1686.
   - https://doi.org/10.1038/s41593-019-0502-4
2. Stringer C, Pachitariu M, Steinmetz N, et al. Spontaneous behaviors drive multidimensional, brainwide activity. *Science*. 2019;364:eaav7893.
   - https://doi.org/10.1126/science.aav7893
3. Saleem AB, Ayaz A, Jeffery KJ, Harris KD, Carandini M. Integration of visual motion and locomotion in mouse visual cortex. *Nature Neuroscience*. 2013;16(12):1864-1869.
   - https://doi.org/10.1038/nn.3567
4. Ravassard P, Kees A, Willers B, et al. Multisensory control of hippocampal spatiotemporal selectivity. *Science*. 2013;340(6138):1342-1346.
   - https://doi.org/10.1126/science.1232655
5. Zelano C, Jiang H, Zhou G, et al. Nasal respiration entrains human limbic oscillations and modulates cognitive function. *Journal of Neuroscience*. 2016;36(49):12448-12467.
   - https://doi.org/10.1523/JNEUROSCI.2586-16.2016
6. Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. *Science*. 2021;372(6544):831-836.
   - https://doi.org/10.1126/science.abd0380
7. Raut RV, Rosenthal ZP, Wang X, et al. Arousal as a universal embedding for spatiotemporal brain dynamics. *Nature*. 2025;647(8089):454-461.
   - https://doi.org/10.1038/s41586-025-09544-4
