# Site Deepening Audit (2026-03-27, Paper Archive Human In Vivo Route Taxonomy)

## 対象

- 主対象: `mind_uploading_papers.md`

## 今回の選定理由

- 2026-03-27 時点で site の主要ページは、human observability を `one human proxy ladder` としてではなく、`quantity-defined` / `target-defined` / `transport-defined` な route family の束としてかなり整理できていました。
- しかし paper archive の入口である `mind_uploading_papers.md` には、なお living-human in vivo route を一段粗く圧縮して読める箇所が残っていました。
- このズレは技術・自然科学の観点で優先度が高いです。理由は、archive front door が粗いままだと、読者が詳細ページで止められているはずの誤読を、年次カードに入る直前で再度起こすからです。

## 根拠付き批判

### 1. `human in vivo observability` を一つの progress bar として読める状態が残っていました

- 問題:
  - 旧 `mind_uploading_papers.md` では living-human route を慎重に扱っていたものの、なお `human MRI / PET progress` が一つの observability ladder であるかのように読める箇所が残っていました。
- 根拠:
  - [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は five-metabolite の parcel-level similarity structure を扱う 1H-MRSI route です。
  - [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は 31P-MRS により ATP synthesis, phosphorus-metabolite concentrations, pH, T1 を扱う energetic-balance route です。
  - [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は dynamic DMRSI により glucose-related kinetic rate を推定する route です。
  - [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は BBB water-exchange ASL route の method dependence を示しました。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は tracer-specific BBB permeability-surface-area product を PET kinetic modeling で扱いました。
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) と [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は astrocyte PET でも target class が異なることを示しました。
  - [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は sleep-linked clearance physiology を wearable + compartment model で扱う route です。
- 批判:
  - したがって、これらを単に `human in vivo observability` とだけ束ねると、quantity type, target class, transport regime, model burden, calibrator role が消えます。
  - safe reading は `route family を先に固定し、その後に proxy class / operational maturity / calibrator role を読むこと` です。

### 2. route family を固定しないと calibrator role が過大評価されます

- 問題:
  - archive front door が粗いままだと、読者は `human proxy exists` を `human hidden state is becoming directly measurable` に滑らせやすくなります。
- 根拠:
  - [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024) は regional synaptic-density PET を与えますが、transcriptional or signaling closure は与えません。
  - [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は myelin bilayer-sensitive mapping route を与えますが、generic maintenance-state meter ではありません。
  - [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) と [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は bounded clearance / mobility physiology を与えますが、cell-specific controller state を直接は与えません。
- 批判:
  - したがって、front door でも `何が calibrate できるか` を route family ごとに明示しないと、reader-facing claim ceiling が緩みます。
  - `proxy-rich bundle` と `common state meter` は別物であり、その区別を入口から固定する必要がありました。

### 3. 主要ページで止めていた誤読を archive page が再導入していました

- 問題:
  - `wbe_101.md`, `verification.md`, `wiki/human-proxy-composition.md`, `wiki/measurement-stack-and-claim-ceiling.md` では、すでに human route family の圧縮を止める言い回しが導入されていました。
  - それにもかかわらず `mind_uploading_papers.md` の front matter, fast-lane table, long-form caution, recommendation row では、その taxonomy が十分に前面化されていませんでした。
- 根拠:
  - 同日に実施済みの site-wide audit 群は、spectroscopy split, BBB quantity-type split, astrocyte target split, human proxy composition split をそれぞれ別ファイルで固定しています。
- 批判:
  - つまり、archive page は技術ページより一段古い taxonomy を保持していました。
  - public front door の一貫性を保つには、archive page も同じ route taxonomy に同期させる必要がありました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `known_points` を更新し、living-human in vivo route は `route family fixed first` の原則で読むことを明記
  - `page_highlights` を更新し、human measurement papers は route family を固定してから `proxy class / operational maturity / safe calibrator role` を読むよう同期
  - technical addendum の human observability correction を強化し、`Lucchetti / Ren / Li / Morgan / Chung / Villemagne / Tyacke / Dagum` を route-family taxonomy に沿って明記
  - `human in vivo observability / proxy ladder` row を改稿し、regional synaptic-density PET, 1H-MRSI parcel similarity, 31P energetic balance, deuterium metabolite-rate imaging, quantity-defined myelin, BBB water exchange, tracer-specific BBB transport, target-defined astrocyte PET, clearance-support physiology へ分解
  - `Split destructive structure from living-human observability` note-box を拡張し、destructive structure と living-human route family の違いを強調
  - `Route name alone is too coarse for human in vivo papers` note-box を追加し、modality name だけでは quantity / target / transport / model burden が固定されないことを明記
  - technical shortlist の `observability-class advance / human in vivo proxy ladder` row を同じ taxonomy に同期
  - long evidence-class introduction を更新し、human-measurement lane の calibrator role を論文ごとに分解
  - recommendation row `I want to see what humans can actually observe now` を更新し、living-human routesの最短読書線を taxonomy 付きで提示

## 今回の修正で止めた誤読

- `human MRI / PET progress` を一つの observability meter と読むこと
- `1H-MRSI`, `31P-MRS`, `DMRSI`, `BBB ASL`, `BBB PET`, `astrocyte PET`, `clearance physiology` を同じ inferential object の variation と読むこと
- `human proxy が増えた = hidden state closure が近い` と読むこと
- `modality name が同じなら calibrator role も近い` と読むこと
- 主要ページでは split しているのに、archive front door だけ古い圧縮語で読んでしまうこと

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文と監査記録の更新で完結しています。

## 参考文献

1. Johansen A, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
3. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
4. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
5. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
6. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024;37(12):e5256.
   - https://doi.org/10.1002/nbm.5256
7. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
8. Villemagne VL, Harada R, Dore V, et al. First-in-humans evaluation of 18F-SMBT-1, a novel 18F-labeled monoamine oxidase-B PET tracer for imaging reactive astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263255
9. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018;59(10):1597-1602.
   - https://doi.org/10.2967/jnumed.118.208009
10. Hirschler L, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
11. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
