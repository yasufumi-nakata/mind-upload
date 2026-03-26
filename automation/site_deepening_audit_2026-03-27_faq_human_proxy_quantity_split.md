# Site Deepening Audit (2026-03-27, FAQ human proxy quantity / target / transport split)

## 対象

- 主対象: `faq.md`
- 参照整合先: `wbe_101.md`, `verification.md`, `wiki/human-proxy-composition.md`, `wiki/measurement-stack-and-claim-ceiling.md`, `wiki/homeostatic-plasticity-and-maintenance-state.md`
- web確認対象:
  - `https://mind-upload.com/faq.html`
  - `https://doi.org/10.1038/s41467-025-66124-w`
  - `https://doi.org/10.1002/nbm.3384`
  - `https://doi.org/10.1093/pnasnexus/pgaf072`
  - `https://doi.org/10.1002/mrm.29998`
  - `https://doi.org/10.1002/nbm.5256`
  - `https://doi.org/10.1038/s41467-025-58356-7`
  - `https://doi.org/10.2967/jnumed.121.263254`
  - `https://doi.org/10.2967/jnumed.118.208009`
  - `https://doi.org/10.1038/s41380-021-01429-y`
  - `https://doi.org/10.1038/s41593-025-02073-3`
  - `https://doi.org/10.1038/s41467-026-68374-8`

## 今回このページを選んだ理由

- 公開中の `faq.md` は front door として重要ですが、Q2d がなお `dynamic energetic and support-state proxies` という粗い束を残していました。
- その結果、詳細ページではすでに分けている
  - `1H-MRSI similarity`
  - `31P energetic balance`
  - `deuterium kinetic-rate imaging`
  - `myelin-bilayer mapping`
  - `BBB water exchange`
  - `tracer-specific BBB transport`
  - `MAO-B / I2BS astrocyte PET`
  - `CSF mobility / biomarker-efflux`
  を、FAQの入口では再び一つの「human observability advance」として読めてしまう状態でした。
- これは技術・自然科学の観点で弱いです。入口の分類語が粗いと、その先の claim ceiling も粗く読まれるからです。

## 根拠付き批判

### 1. 旧Q2dは different quantity type を一つの progress bar に圧縮していました

- [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は five-metabolite `parcel-level similarity scaffold` です。
- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は `31P energetic-balance route` です。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は `dynamic deuterium kinetic-rate imaging` です。
- [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は `myelin-bilayer mapping` です。
- [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は BBB `water-exchange` 推定が route choice に依存することを示しました。
- [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は `tracer-specific BBB permeability-surface-area` を kinetic model 下で扱いました。
- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) と [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) は human astrocyte PET が `MAO-B` と `I2BS` の別 target class であることを示しました。
- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) と [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は `CSF mobility / sleep-linked biomarker efflux` を進めましたが、やはり同じ quantity ではありません。

批判:

- したがって、`human MRI / PET evidence is improving` を一括で読むのは粗いです。
- FAQの入口でも `quantity type`, `target class`, `transport regime` を出さないと、詳細ページの stop line が前段で無効化されます。

### 2. 旧Q2dは `same modality label = same inferential object` と誤読できました

- `MRI` の中でも
  - `1H-MRSI similarity`
  - `31P energetic balance`
  - `deuterium kinetic rate`
  - `myelin bilayer`
  - `BBB water exchange`
  - `CSF mobility`
  は別です。
- `PET` の中でも
  - `SV2A synaptic-density atlas`
  - `tracer-specific BBB transport`
  - `MAO-B astrocyte-related route`
  - `I2BS astrocyte-related route`
  は別です。

批判:

- モダリティ名だけを front door の主分類にすると、何を直接観測したのかが消えます。
- 入口ページでも `route name alone is too coarse` を明示する必要がありました。

### 3. 旧Q2dは FAQ 入口と詳細ページの claim ceiling をずらしていました

- `wbe_101.md`, `verification.md`, `wiki/human-proxy-composition.md`, `wiki/measurement-stack-and-claim-ceiling.md`, `wiki/homeostatic-plasticity-and-maintenance-state.md` は、すでに `proxy class`, `operational maturity`, `calibrator role` に加え、`quantity-defined / target-defined` の規律を導入しています。
- しかし FAQ は旧い束ね方を残していたため、読者が最初の5分で受け取る rule が site-wide rule より粗い状態でした。

批判:

- これは読者の理解を site 全体で不安定にします。
- FAQ は short page ですが、だからこそ分類語の精度を落としてはいけません。

## 今回実行した変更

- `faq.md`
  - `last_updated` を `2026-03-27` に更新
  - front matter の highlight / known point を `quantity type / target class / transport regime` に同期
  - Q2d 導入文を改稿し、`Lucchetti / Ren / Li / Baadsvik / Morgan / Chung / Villemagne / Tyacke / Hirschler / Dagum` を使って human route の内部差を明示
  - Q2d の table を 4 row から 9 row に分解
    - destructive local ultrastructure
    - SV2A PET atlas
    - five-metabolite 1H-MRSI similarity scaffold
    - 31P-MRS energetic-balance route
    - dynamic deuterium metabolite / rate imaging
    - myelin-bilayer mapping
    - BBB water-exchange and tracer-specific transport routes
    - target-defined astrocyte-related PET routes
    - CSF-mobility and sleep-linked clearance routes
  - `Route name alone is too coarse` note-box を追加
  - `Seven quick checks` を実際の bullet 数に合わせて `Eight quick checks` に修正
  - `Same quantity?` bullet を `density / similarity / energetic balance / kinetic rate / water exchange / tracer-specific transport / support-state efflux` に更新
  - Morgan 2024 と Chung 2025 を references に追加

## 今回止めた誤読

- `human measurement improved` = `one common human state meter is forming`
- `MRI` や `PET` という modality label だけで inferential object を読める
- `dynamic energetic and support-state proxies` が一つの可換な bundle である
- `human astrocyte PET` が一つの generic astrocyte scalar である
- `human BBB proxy` が一つの generic leakiness scalar である

## 外部依存タスク

- なし
  - 今回の変更は repo 内の FAQ 本文と監査記録の更新で完結しています。

## 参考文献

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
2. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
3. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
4. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
5. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024;37(12):e5256.
   - https://doi.org/10.1002/nbm.5256
6. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
7. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263254
8. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018;59(10):1597-1602.
   - https://doi.org/10.2967/jnumed.118.208009
9. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022;27(4):2019-2029.
   - https://doi.org/10.1038/s41380-021-01429-y
10. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
11. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
