# Site Deepening Audit (2026-03-20, Beginner Human Observability Front Door)

## 対象

- 主対象: `wiki/mind-upload-basics.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-20 時点で、公開コアページ側では `human observability` を `proxy class x route maturity` の二軸で読む規則がかなり明確になっていました。
- その一方で、最初に技術面の全体像を学ぶ `wiki/mind-upload-basics.md` は、なお `human evidence improved` を一段の進捗に近く読ませる余地が残っていました。
- これは技術・自然科学の観点で優先度が高いです。初学者向け入口が粗いと、その後の厳密な claim ceiling を読む前に、読者が `human proxy-rich evidence = near-direct state capture` と過大読みにしやすいからです。

## 根拠付き批判

### 1. 旧 beginner page は human-side advance をまだ一つの observability 改善物語として読ませる余地がありました

- 問題:
  - 旧 `wiki/mind-upload-basics.md` は、decode / tractography / DCM / thermodynamics / closed loop の route-card 化は説明していました。
  - しかし human-side measurement 自体の内部差、すなわち `local ultrastructure`、`regional synaptic-density PET`、`whole-brain biochemical scaffold`、`dynamic energetic imaging`、`macro myelin mapping`、`CSF / glymphatic support-state proxy` が別々の object であることを beginner level で十分に固定できていませんでした。
- 根拠:
  - Shapson-Coe et al. (2024) は human temporal cortex の `1 mm^3` を nanoscale で再構成し、局所 structural scaffold を押し上げました。
  - Johansen et al. (2024) は healthy humans `17F/16M` の SV2A PET atlas を、postmortem autoradiography で較正しました。
  - Lucchetti et al. (2025) は `51` healthy participants と independent sample `13` に対して、five-metabolite `1H-MRSI` similarity graph を示しました。
  - Li et al. (2025) は `7 T` dynamic DMRSI と kinetic model を使い、`5` healthy participants で glucose-related rate imaging を行いました。
  - Baadsvik et al. (2024) は `2` healthy volunteers で myelin bilayer mapping を示しました。
  - Hirschler et al. (2025) は `24` healthy individuals で CSF mobility MRI を示しました。
  - Dagum et al. (2026) は randomized crossover trial `39 participants`、investigational device、multicompartment model を通して sleep-linked glymphatic clearance を論じました。
- 批判:
  - 以上はどれも `human evidence improved` の一文で括ってよい object ではありません。
  - beginner page でこれを分けないと、読者は `人で多くの route が増えた` を `human state-complete measurement is getting close` と誤読しやすくなります。

### 2. 旧 beginner page は proxy class と route maturity / model burden を別軸として固定していませんでした

- 問題:
  - 旧構成では `何の proxy か` は暗黙に読めても、`specialized hardware`、`small cohort`、`kinetic model burden`、`investigational device` の差が目立ちませんでした。
- 根拠:
  - Li et al. (2025) は `0.7 cc nominal voxel`、whole-brain coverage、blood input functions、kinetic modeling を前提とします。
  - Baadsvik et al. (2024) は high-performance RF / gradient hardware を必要とします。
  - Dagum et al. (2026) は investigational device と multicompartment model に依存します。
- 批判:
  - したがって、`what it constrains` と `how specialized / model-heavy it is` を分けない限り、読者は proxy の意味と field-readiness を混同します。
  - beginner page でも二軸を明示しないと、前段の説明だけで十分と誤解されます。

### 3. beginner page から maintenance-state の最新境界へ戻る導線が弱めでした

- 問題:
  - 旧 `wiki/mind-upload-basics.md` は、human observability が増えてもなお何が latent のままかを beginner level では十分に強調していませんでした。
- 根拠:
  - Santoni et al. (2024) は chromatin plasticity が engram eligibility を前もって規定しうることを示しました。
  - Terceros et al. (2026) は thalamocortical transcriptional gates が memory stabilization に time-dependent に効くことを示しました。
  - Cahill et al. (2024) は local neurotransmitter input が broad astrocyte network へ minutes-long に符号化されることを示しました。
- 批判:
  - これらは、human proxy が増えても maintenance-state family がまだ閉じていないことを示します。
  - beginner page 側で `human evidence increased` だけを先に読むと、この latent family が background noise へ戻ってしまいます。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` に、`human observability = proxy class x route maturity` という site rule を追加しました。
  - 冒頭 note box に `human evidence is not one progress bar` を追加しました。
  - 新規 section `Why even a beginner page now needs a human observability ladder` を追加しました。
  - 同 section に、Shapson-Coe / Johansen / Lucchetti / Li / Baadsvik / Hirschler / Dagum を比較する beginner table を追加しました。
  - 同 section に、Santoni / Terceros / Cahill を用いた `what still remains outside these human routes` note を追加しました。
  - `measurement-stack-and-claim-ceiling` と `homeostatic-plasticity-and-maintenance-state` への導線を追加しました。
- `glossary.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - `page_highlights` / `known_points` に `proxy class` と `route maturity / model burden` を追加しました。
  - note box `When human-evidence terms start sounding like one thing` を追加しました。
  - 用語表に `Proxy class`、`Route maturity / model burden`、`Human observability ladder`、`Support-state proxy` を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・用語整理・監査メモの更新で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
4. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
5. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
6. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28:2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
8. Santoni G, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024;385(6705):eadg9982.
   - https://doi.org/10.1126/science.adg9982
9. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026;649:1254-1263.
   - https://doi.org/10.1038/s41586-025-09774-6
10. Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024;629:146-153.
   - https://doi.org/10.1038/s41586-024-07311-5
