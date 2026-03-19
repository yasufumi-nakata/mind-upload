# Site Deepening Audit (2026-03-19, Closed-Loop Boundary Integration Into Timing Wiki)

## 対象

- 主対象: `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- 副対象: `faq.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイト本体は、`Body / Environment Boundary Card` 自体は `verification.md` と front door 側で既にかなり強く整理できておりました。
- しかし、閉ループの専用補助ページである `wiki/closed-loop-latency-jitter-and-safety-stops.md` は、主に `delay / jitter / drift / safe stop / recalibration burden` の整理に集中しており、`body/environment boundary` を timing wiki の内部規則としてまだ十分に統合しておりませんでした。
- この不整合は技術・自然科学の観点で弱点です。なぜなら、読者が dedicated closed-loop page に来た時点で、`loop quality = time quality` と読みやすくなり、`which sensory / motor / interoceptive / reafference routes were actually preserved` という一次変数が後景化するからです。

## 根拠付き批判

### 1. 専用 timing wiki が `ms budget` を前面化しすぎると、`subject boundary` を後段の注記へ押し下げてしまいます

- 問題:
  - 既存 wiki は、loop class、tail latency、phase error、recalibration burden、clinic/home transfer を丁寧に整理していました。
  - しかし、その入口ではまだ `timing audit` が主役であり、`boundary audit` は verification 側へ委ねられていました。
- 根拠:
  - Musall et al. (2019) は、single-trial neural dynamics が richly varied movements に強く支配されることを示しました。
  - Stringer et al. (2019) は、spontaneous behaviors が multidimensional, brainwide activity を駆動することを示しました。
- 批判:
  - したがって、loop が速いことを記録しても、`どの行動・身体・環境ループが入っていたのか` を固定しなければ、L3 の ceiling は定まりません。
  - timing 専用ページの中でも、この rule を明文化する必要がありました。

### 2. 旧 timing wiki には `efference copy / reafference` の明示がありませんでした

- 問題:
  - 既存ページは、loop type と latency failure を整理していましたが、self-generated sensory consequence の扱いが抜けていました。
- 根拠:
  - Keller et al. (2012) は、behaving mouse V1 で sensorimotor mismatch signals を示し、passive visual flow だけでは活動を十分に説明できないことを示しました。
  - Schneider et al. (2014) は、motor-to-auditory cortical circuit が movement 中の auditory response を抑制する corollary discharge を示しました。
- 批判:
  - これは `same external input` でも `self-generated action and predicted reafference` の有無で感覚皮質の状態が変わりうることを意味します。
  - よって `fast loop` を読むページでこそ、`efference / reafference route was present or absent` を先に書かせる必要がありました。

### 3. 旧 timing wiki には `interoceptive / organism-wide` route が body/environment boundary の一部として統合されていませんでした

- 問題:
  - 呼吸、arousal、autonomic covariates はサイト全体では触れられていましたが、この wiki の L3 読解質問票には入っていませんでした。
- 根拠:
  - Zelano et al. (2016) は、nasal respiration が human limbic oscillations を entrain し、memory retrieval を変えることを示しました。
  - Raut et al. (2025) は、brain activity, physiology, and behavior が latent arousal manifold で jointly organized されることを示しました。
- 批判:
  - したがって `brain-only fast controller` を `state-complete closed loop` と読むのは過大評価です。
  - interoceptive / organism-wide state が latent なら、その omission を timing wiki 内でも直接尋ねる必要がありました。

### 4. tactile feedback の local advance を `embodiment solved` に誤読させない説明が timing wiki に不足していました

- 問題:
  - 既存 wiki は streaming speech, aDBS, neurofeedback を timing class として整理していましたが、feedback topology そのものを別軸で問う表現が弱い状態でした。
- 根拠:
  - Flesher et al. (2021) は、tactile percept を戻す bidirectional BCI により robotic arm task performance が大きく改善することを示しました。
- 批判:
  - これは `feedback channel matters` を支持しますが、同時に `which channel was restored and which were still absent` を書かなければ claim ceiling が決まらないことも意味します。
  - よって timing wiki にも `boundary-before-latency` の節が必要でした。

## 今回実行した変更

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - `last_updated` を 2026-03-19 に更新しました。
  - front matter の `description`, `page_highlights`, `known_points` を更新し、`low latency != solved body/environment boundary` を timing wiki の冒頭方針へ昇格しました。
  - 新規節 `Before milliseconds, fix which loop boundary was actually preserved` を追加しました。
  - 新規 table で
    - self-motion / optic flow / proprioceptive coupling
    - sensorimotor mismatch / predicted reafference
    - vestibular / multisensory navigation cues
    - corollary discharge of self-generated sensory consequences
    - respiration / arousal / organism-wide physiology
    - tactile contact feedback
    を別 row で整理しました。
  - minimum log checklist に boundary fields を追加しました。
  - `6 questions` を `9 questions` へ改稿し、boundary disclosure と ablation test を timing questions より前へ移しました。
  - 参考文献へ Keller (2012), Schneider (2014), Musall (2019), Stringer (2019), Raut (2025), Flesher (2021) を追加しました。
- `faq.md`
  - Q5c の follow-up link を改稿し、`Verification: Body / Environment Boundary Card` に加えて、新しい wiki 節 `boundary-before-latency` へ直接導線を張りました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・読解規則・参考文献導線の改稿で完結しております。

## 参考文献

1. Keller GB, Bonhoeffer T, Hubener M. Sensorimotor mismatch signals in primary visual cortex of the behaving mouse. *Neuron*. 2012;74(5):809-815.
   - https://doi.org/10.1016/j.neuron.2012.03.040
2. Saleem AB, Ayaz A, Jeffery KJ, Harris KD, Carandini M. Integration of visual motion and locomotion in mouse visual cortex. *Nature Neuroscience*. 2013;16(12):1864-1869.
   - https://doi.org/10.1038/nn.3567
3. Ravassard P, Kees A, Willers B, et al. Multisensory control of hippocampal spatiotemporal selectivity. *Science*. 2013;340(6138):1342-1346.
   - https://doi.org/10.1126/science.1232655
4. Schneider DM, Nelson A, Mooney R. A synaptic and circuit basis for corollary discharge in the auditory cortex. *Nature*. 2014;513(7517):189-194.
   - https://doi.org/10.1038/nature13724
5. Zelano C, Jiang H, Zhou G, et al. Nasal respiration entrains human limbic oscillations and modulates cognitive function. *Journal of Neuroscience*. 2016;36(49):12448-12467.
   - https://doi.org/10.1523/JNEUROSCI.2586-16.2016
6. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019;22:1677-1686.
   - https://doi.org/10.1038/s41593-019-0502-4
7. Stringer C, Pachitariu M, Steinmetz N, et al. Spontaneous behaviors drive multidimensional, brainwide activity. *Science*. 2019;364(6437):eaav7893.
   - https://doi.org/10.1126/science.aav7893
8. Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. *Science*. 2021;372(6544):831-836.
   - https://doi.org/10.1126/science.abd0380
9. Raut RV, Rosenthal ZP, Wang X, et al. Arousal as a universal embedding for spatiotemporal brain dynamics. *Nature*. 2025;647:454-461.
   - https://doi.org/10.1038/s41586-025-09544-4
