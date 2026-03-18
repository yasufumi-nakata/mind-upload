# Site Deepening Audit (2026-03-18, WBE 101 Human Observability Ladder)

## 対象

- 主対象: `wbe_101.md`
- 副対象: `faq.md`
- 副対象: `index.md`
- 副対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`

## 今回の選定理由

- 2026-03-18 時点で、公開サイトは `connectome-complete != emulation-complete` をかなり強く固定できていました。
- しかし入口導線では、`何がまだ hidden state なのか` は強く言えていても、`人間で今どの層まで実際に観測・近似できているか` が十分に evidence class 化されていませんでした。
- この欠落は技術・自然科学の観点で重要です。なぜなら、human 側の前進を 1 本の「かなり見えてきた」物語へ圧縮すると、局所 ex vivo ultrastructure、SV2A PET、whole-brain MRSI、31P-MRS / dynamic DMRSI、MRS thermometry、myelin bilayer mapping、CSF/glymphatic proxy の意味の差が消え、proxy-rich evidence を near-direct readout と誤読しやすくなるからです。

## 根拠付き批判

### 1. 旧 `wbe_101.md` は hidden-state の列挙には強い一方、human observability の層構造を入口で十分に分けていませんでした

- 問題:
  - `wbe_101.md` には hidden-state table と measurement-stack note がありました。
  - しかし、読者が入口段階で最も知りたい `human で何が実際に観測可能になってきたのか` を、proxy class ごとに短く比較する front-door table がありませんでした。
- 根拠:
  - Shapson-Coe et al. (2024) は human cortex の局所 nanoscale ultrastructure を押し上げました。
  - Johansen et al. (2024) は living human brain の SV2A density atlas を押し上げました。
  - Lucchetti et al. (2025) は whole-brain MRSI から biochemical organization を押し上げました。
  - Ren et al. (2015) と Li et al. (2025) は macro energetic route を押し上げました。
  - Rzechorzek et al. (2022) は macro thermal route を押し上げました。
  - Baadsvik et al. (2024) は macro myelin bilayer route を押し上げました。
  - Hirschler et al. (2025) と Dagum et al. (2026) は macro clearance / support-state route を押し上げました。
- 批判:
  - これらはすべて別々の evidence class であり、同じ `human state observability` ではありません。
  - front door でこの差を見せなければ、`人間で色々見えてきた` が `人間で state-complete measurement にかなり近づいた` へ誤変換されます。

### 2. 旧 FAQ は `connectome is not enough` を強く説明していましたが、human proxy ladder への最短復帰路がありませんでした

- 問題:
  - `faq.md` の Q2c は hidden-state の分解自体はかなり良くなっていました。
  - しかし、そこで `では human 側の最近の前進はどう読むべきか` に対する最短リンクがありませんでした。
- 批判:
  - FAQ は入口の誤読を止めるページです。
  - hidden-state の列挙だけで終えると、読者は human proxy-rich papers の位置づけを自力で再構成しなければならず、proxy と ground truth を混同しやすいままでした。

### 3. 旧 landing page も `human evidence exists` と `human state-complete measurement is close` の差を front door で明文化していませんでした

- 問題:
  - `index.md` は `connectome-complete != emulation-complete`、`vascular-state / CVR`、`shortcut audit` をかなり良く止めていました。
  - その一方で、human observability の話は supporting wiki へ後退しており、入口ではまだ `hidden state が多い` という形でしか見えませんでした。
- 批判:
  - 入口ページでは `何が観測できるか` と `何がまだ latent か` の両方を短く見せる必要があります。
  - とくに 2024-2026 の primary literature は `human data が全くない` と読むのも誤りなので、そこを proxy class で整理し直す必要がありました。

### 4. DOI の混在は根拠追跡性を下げていました

- 問題:
  - dynamic DMRSI の Li et al. (2025) について、公開本文の一部に `10.1093/pnasnexus/pgaf079` が混在していました。
- 根拠:
  - Oxford Academic / PubMed の一次情報では、該当論文は `10.1093/pnasnexus/pgaf072` です。
- 批判:
  - この種の DOI 不整合は、proxy evidence の読み分け以上に基本的な証跡を崩します。
  - 入口・wiki ともに引用の一貫性を保つ必要がありました。

## 今回実行した変更

- `wbe_101.md`
  - page highlights / known points に human evidence の layered reading を追加
  - 新節 `#human-observability-ladder` を追加
  - local ultrastructure, synaptic-density PET, biochemical scaffold, energetic imaging, thermometry, myelin bilayer, CSF/glymphatic proxy, and still-missing whole-brain in vivo routes を 1 つの front-door table に整理
  - `human evidence exists != state-complete measurement is close` を note box で明示
  - 参考文献を追加
- `faq.md`
  - `Q. If we know the connectome and cell type...` に human proxy ladder への復帰導線を追加
- `index.md`
  - page highlights / known points に human evidence の layered reading を追加
  - landing page に `human routes are real advances and which are still only proxies` note を追加
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - Li et al. (2025) の DOI / title を `pgaf072` ベースへ修正
- `github-wiki-export/homeostatic-plasticity-and-maintenance-state.md`
  - 同上の DOI / title 修正

## 外部依存で保留

- なし
  - 今回の変更は、公開本文・入口導線・引用整合の改稿で完結しています。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
4. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
5. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
6. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022;145(6):2031-2048.
   - https://doi.org/10.1093/brain/awab466
7. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
8. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
9. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
