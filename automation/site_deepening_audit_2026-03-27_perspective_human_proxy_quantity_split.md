# Site Deepening Audit (2026-03-27, Perspective Human Proxy Quantity-Type Split)

## 対象

- 主対象: `perspective.md`
- 参照同期: `wiki/human-proxy-composition.md`
- 参照同期: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 参照同期: `index.md`
- 参照同期: `wbe_101.md`

## 今回の選定理由

- `perspective.md` はサイトの中核研究ノートですが、`last_updated` が 2026-03-26 のままで、human in vivo proxy table の粒度が他の主要ページより一段粗い状態でした。
- とくに human-route table に `Macro support-state proxies` という一括行が残っており、`ionic / thermal / myelin` が同じ measurement class であるかのように読める構造がありました。
- さらにこの表には、すでに他ページでは分離済みの `BBB water-exchange`, `tracer-specific BBB transport`, `target-defined astrocyte PET` が欠落していました。
- 入口ページ群では quantity type と calibrator role の規律が強化されているため、中核ページだけが古い圧縮語を残すと、読者が入口で学んだ stop rule を本論で失う危険があります。

## 改善優先と判断した情報

### 1. `Macro support-state proxies` は技術的に粗すぎました

- 問題:
  - 旧 `perspective.md` では `Qian 2012`, `Rzechorzek 2022`, `Baadsvik 2024` が同じ行に置かれていました。
  - しかしこれは `tissue sodium`, `brain temperature`, `myelin bilayer` という互いに異なる quantity type を一括語で処理しており、何を直接観測しているかが消えていました。
- 根拠:
  - [Qian et al. (2012)](https://doi.org/10.1002/mrm.23225) は human brain の `tissue sodium content` map です。
  - [Fleysher et al. (2013)](https://doi.org/10.1002/nbm.2813) は `SQ+TQF` により `ISMF / ISC / ISVF` を導出しており、Qian 2012 と同じ quantity ではありません。
  - [Qian et al. (2025)](https://doi.org/10.1038/s41598-025-07800-1) は `mono-/bi-T2 sodium separation` であり、同じ sodium route 内でも inferential object が違います。
  - [Rzechorzek et al. (2022)](https://doi.org/10.1093/brain/awab466) は `MRS thermometry` による macro thermal route です。
  - [Rogala et al. (2024)](https://doi.org/10.3389/fnhum.2024.1398034) は healthy-adult brain temperature measurement の reference-range route です。
  - [Hagiwara et al. (2018)](https://doi.org/10.1038/s41598-018-28852-6) は `SyMRI / MTsat / T1w/T2w` 比較であり、myelin route 内部の非同値性を示します。
  - [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は `myelin bilayer mapping` です。
  - [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) は `remyelination-sensitive qT1` と `MWF / MTR` の非同値性を示しました。
- 批判:
  - したがって、`ionic / thermal / myelin` を一行で扱うと `direct observable`, `model burden`, `calibrator role` が消えます。
  - これは site-wide に導入済みの `quantity type is part of the claim` という規律に反します。

### 2. BBB route が perspective page で欠落していました

- 問題:
  - 旧表は `Padrela 2025` と `Chung 2025` を本文には持ちながら、human proxy table に独立 row として持っていませんでした。
  - そのため読者は BBB human route を `macro support-state` か `clearance` の一部として読めてしまう構造でした。
- 根拠:
  - [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は `DP-ASL` と `ME-ASL` の method-dependent な `Kw` の差を示しました。
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は `Tex` を扱う multi-echo ASL の lifespan reference-range route です。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は `tracer-specific BBB PS` を高時間分解能 PET と kinetic modeling で推定したもので、同時に tracer mechanism 依存です。
- 批判:
  - `water exchange` と `tracer-specific transport` は同じ inferential object ではありません。
  - BBB route を独立表に持たないのは、perspective page の human observability 読解を過度に粗くします。

### 3. Astrocyte human route が perspective page で欠落していました

- 問題:
  - 旧表には glia imaging の一般行はありましたが、human proxy table に `target-defined astrocyte PET` がありませんでした。
  - そのため `astrocyte-related human evidence` が `neuromodulator / glia imaging` の一般論に吸収されていました。
- 根拠:
  - [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) は `18F-SMBT-1` が `MAO-B` route であり、selegiline によって全脳で `>85% blockade` を示しました。
  - [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は `11C-BU99008` が `I2BS` route であり、`idazoxan` では dose-dependent block があり、`isocarboxazid` では block されませんでした。
  - [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) は `11C-BU99008` uptake が regionally dynamic であり、AD continuum 内で単純単調ではないことを示しました。
  - [Jaisa-Aad et al. (2024)](https://doi.org/10.1007/s00401-024-02712-2) は MAO-B biomarker interpretation が ADRD class ごとの病理文脈に依存することを整理しました。
- 批判:
  - したがって、human astrocyte route は `generic glia imaging` ではなく `target-defined MAO-B / I2BS proxy` として分離すべきです。
  - これを perspective page で欠落させると、他ページで止めていた `generic astrocyte-state meter` という誤読が戻ります。

### 4. `proxy class` と `operational maturity` だけでは不十分でした

- 問題:
  - 旧 perspective page は二軸までは説明していましたが、`calibrator role` が中核ページでは十分に見えませんでした。
- 根拠:
  - `Johansen 2024` は synaptic-density proxy を与えますが、chloride homeostasis は calibrate しません。
  - `Li 2025` は energetic-rate route ですが、BBB transport は calibrate しません。
  - `Morgan 2024 / Padrela 2025` は BBB water-exchange route ですが、astrocyte ensemble identity は calibrate しません。
  - `Villemagne 2022 / Tyacke 2018` は target-defined astrocyte PET route ですが、clearance flux や neurovascular controller identity は calibrate しません。
- 批判:
  - したがって、perspective page でも `proxy class`, `operational maturity`, `calibrator role` の三軸を明示しないと、bundle の読み方が緩くなります。

## 今回実行した変更

- `perspective.md`
  - `last_updated` を `2026-03-27` に更新
  - page highlights で `macro support-state proxies` を廃し、`ionic / thermal / myelin / BBB / astrocyte / clearance` の split を front matter に反映
  - `2026-03-27 correction` note-box を新設し、quantity type と calibrator role の観点から perspective page 自体の弱点を明示
  - human-route table の `Macro support-state proxies` 行を削除
  - `Quantity-defined human ionic routes`
  - `Human macro thermal routes`
  - `Quantity-defined human myelin MRI routes`
  - `BBB water-exchange MRI`
  - `Tracer-specific BBB PET transport`
  - `Target-defined astrocyte PET routes`
  - 上記 6 行を新設して quantity-defined table へ置換
  - `Human CSF mobility / sleep-linked clearance proxy` の safe reading を `Clearance support-state proxy` に明確化
  - `Proxy class is not the same thing as operational maturity` を `Proxy class, operational maturity, and calibrator role are different axes` に改稿
  - `The stop rule is now explicit` note-box に `calibrator role` 要件を追加
  - `Key Technical Challenges` 冒頭の human evidence summary を新 split に合わせて改稿

## 今回の修正で止めた誤読

- `sodium MRI + brain thermometry + myelin MRI = one macro support-state meter`
- `BBB route = generic support-state row`
- `astrocyte PET = generic glia imaging`
- `proxy class + maturity がわかれば、何を calibrate するかもほぼわかる`

## 外部依存で保留

- なし
  - 今回の変更は公開本文と監査メモの改稿で完結しています。

## 参考文献

1. Qian Y, Panigrahy A, Laymon CM, et al. Sodium MRI of human brain at 7 T: initial experience and comparison with 3 T. *Magn Reson Med*. 2012. https://doi.org/10.1002/mrm.23225
2. Fleysher L, Oesingmann N, Brown R, et al. Noninvasive quantification of intracellular sodium in human brain using ultrahigh-field MRI. *NMR Biomed*. 2013;26(1):9-19. https://doi.org/10.1002/nbm.2813
3. Qian Y, Lin YC, Chen X, et al. Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. *Sci Rep*. 2025;15:27427. https://doi.org/10.1038/s41598-025-07800-1
4. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022;145(6):2031-2048. https://doi.org/10.1093/brain/awab466
5. Rogala J, Molenda M, Romanowski M, et al. Measurement of healthy adult brain temperature using 1H magnetic resonance spectroscopy thermometry. *Front Hum Neurosci*. 2024. https://doi.org/10.3389/fnhum.2024.1398034
6. Hagiwara A, Hori M, Kamagata K, et al. Myelin measurement: comparison between simultaneous tissue relaxometry, magnetization transfer saturation index, and T1w/T2w ratio methods. *Sci Rep*. 2018;8:10554. https://doi.org/10.1038/s41598-018-28852-6
7. Baadsvik EL, Helms G, Callaghan MF, et al. Myelin bilayer mapping in the human brain in vivo. *Magn Reson Med*. 2024;91(4):1573-1590. https://doi.org/10.1002/mrm.29998
8. Galbusera R, Senda J, van der Weijden CWJ, et al. qT1 reveals remyelination in multiple sclerosis cortex whereas MWF and MTR do not. *Brain Pathol*. 2025. https://doi.org/10.1111/bpa.70010
9. Morgan AR, Gatto A, Elmenhorst D, et al. Blood-brain barrier water exchange rate using diffusion-prepared and multi-echo ASL. *NMR Biomed*. 2024. https://doi.org/10.1002/nbm.5256
10. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiol Aging*. 2025;147:176-186. https://doi.org/10.1016/j.neurobiolaging.2024.12.012
11. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nat Commun*. 2025;16:3076. https://doi.org/10.1038/s41467-025-58356-7
12. Villemagne VL, Harada R, Doré V, et al. First-in-humans evaluation of 18F-SMBT-1, a novel 18F-labeled monoamine oxidase-B PET tracer for imaging reactive astrogliosis. *J Nucl Med*. 2022;63(10):1551-1559. https://doi.org/10.2967/jnumed.121.263254
13. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *J Nucl Med*. 2018;59(10):1597-1602. https://doi.org/10.2967/jnumed.118.208009
14. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Mol Psychiatry*. 2022;27(4):2019-2029. https://doi.org/10.1038/s41380-021-01429-y
15. Jaisa-Aad K, Bi M, Toyonaga T, et al. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathol*. 2024;147:66. https://doi.org/10.1007/s00401-024-02712-2
