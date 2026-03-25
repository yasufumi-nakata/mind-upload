# 2026-03-26 サイト深掘り監査: measurement-stack の human proxy 三軸不足

- 対象ページ: `wiki/measurement-stack-and-claim-ceiling.md`
- 同期参照: `wbe_101.md`, `tech_roadmap.md`, `verification.md`, `wiki/human-proxy-composition.md`
- web 確認対象: `https://mind-upload.com/wiki/measurement-stack-and-claim-ceiling.html`

## 1. 今回このページを選んだ理由

- 直近のサイト全体では、living-human route を `proxy class / operational maturity / calibrator role` の三軸で読む規則がすでに前面化されております。
- しかし `wiki/measurement-stack-and-claim-ceiling.md` は、human maintenance-state ladder をかなり強化した一方で、まだ主軸が `proxy class + maturity` に寄っており、`どの hidden-state family を安全に較正する route なのか` が table-level では弱い状態でした。
- このずれは技術・自然科学の読者にとって実害があります。人間側 proxy が増えたことを、そのまま `maintenance-state の較正範囲も広がった` と読み替えやすくなるためです。
- さらに、このページ単体では `same-subject / same-brain` の sequential bridge stop line がまだ弱く、live-to-fix や separated-regime acquisition を一つの state sample と誤読する余地が残っておりました。

## 2. 主批判

### 2-1. `proxy class` と `operational maturity` だけでは、何を較正できるかが固定されません

- `Johansen et al. (2024)` は in vivo SV2A atlas ですが、そこから直接言えるのは regional synaptic-density proxy までであり、momentary synaptic efficacy ではありません。
- `Lucchetti et al. (2025)` は five-metabolite 1H-MRSI similarity graph であり、parcel-level biochemical scaffold です。kinetic metabolic rate や local controller を直接測っているわけではありません。
- `Li et al. (2025)` は 7 T dynamic DMRSI + kinetic model による energetic-rate route ですが、branch-local ATP reserve や mitochondrial positioning を直接与えません。
- `Baadsvik et al. (2024)` は myelin bilayer mapping の proof-of-principle ですが、per-axon timing controller を固定しません。
- `Hirschler et al. (2025)` と `Dagum et al. (2026)` は support-state / clearance 側を押し上げますが、cell-specific immune controller や synapse-level maintenance logic ではありません。

### 2-2. `same-subject` は `same-state` を自動では与えません

- `Lu et al. (2023)` は preservation route と fixation time course が extracellular-space retention と geometry を変えることを示しました。
- `Shapson-Coe et al. (2024)` は人間 nanoscale reconstruction を前進させましたが、rapidly preserved local surgical fragment です。
- `MICrONS Consortium et al. (2025)` は same-brain function + EM を強く押し上げましたが、simultaneous capture ではなく sequential local pipeline です。
- したがって、live / ex vivo をまたぐ bundle や separated physiological regime をまたぐ bundle は、specimen identity があっても state continuity を自動では獲得しません。

## 3. 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md` の `last_updated` を `2026-03-26` に更新しました。
- front matter の `page_highlights` と `known_points` に、以下の二点を追加しました。
  - human maintenance-state route は `proxy class / operational maturity / calibrator role` の三軸で読む
  - `same-subject / same-brain` は sequential bridge 条件なしには `same-state` にならない
- `7. Human maintenance-state routes also form a ladder` の table を改稿し、各 row について
  - proxy class
  - operational maturity / burden
  - safe calibrator role
  - still latent
  - claim ceiling
  を同時に見えるようにしました。
- 同節に `Proxy class, operational maturity, and calibrator role have to be logged separately` の note を追加し、三軸を operational rule として固定しました。
- 同節に `Same-subject still does not solve the bridge by itself` の note を追加し、live / ex vivo や separated-regime bundle に `State-Continuity Bridge Card` を要求する stop line を明記しました。
- `8. Proxy-rich human evidence still does not become state-complete by composition` の導入文を三軸前提へ更新しました。
- composition table に
  - `Same-subject sequential pipeline = same-state multistack sample`
  という誤読を止める行を追加しました。
- `Composition rule on this site` を更新し、Fusion Card に加えて sequential bridge では `State-Continuity Bridge Card` も必要であることを明記しました。
- `Practical rules` と末尾 table も三軸 + bridge disclosure を前提に書き換えました。

## 4. 今回の変更で止めた誤読

- `human proxy が増えた = hidden-state calibration が広く進んだ`
- `specialized but real route = deployable route`
- `same-subject / same-brain = same-state multistack sample`
- `proxy-rich bundle = state-complete human observability`

## 5. 外部依存タスク

- なし。今回の修正はこのセッションで repo 内完結で実行可能でした。

## 6. 参考文献

1. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023;3(7):100520. https://doi.org/10.1016/j.crmeth.2023.100520
2. Shapson-Coe A, Januszewski M, Berger DR, et al. A petascale automated imaging pipeline for mapping neuronal circuits in the human brain. *Science*. 2024. https://doi.org/10.1126/science.adk4858
3. MICrONS Consortium, Bae JA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640:435-447. https://doi.org/10.1038/s41586-025-08790-w
4. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024;44(33):e1750232024. https://doi.org/10.1523/JNEUROSCI.1750-23.2024
5. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344. https://doi.org/10.1038/s41467-025-66124-w
6. Li Y, et al. Whole-brain glucose transport and metabolism with dynamic deuterium MR spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
7. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344. https://doi.org/10.1002/mrm.29998
8. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401. https://doi.org/10.1038/s41593-025-02073-3
9. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715. https://doi.org/10.1038/s41467-026-68374-8
