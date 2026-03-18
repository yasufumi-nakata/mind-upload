# Site Deepening Audit (2026-03-18, Measurement Stack Human Proxy Ladder Alignment)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 同期対象: `github-wiki-export/measurement-stack-and-claim-ceiling.md`
- 参照元: `wbe_101.md`

## 今回の選定理由

- 2026-03-18 時点で公開サイトは、`connectome-complete != emulation-complete`、`multimodal != state-complete`、`proxy-rich evidence != direct ground truth` をかなり強く整理できておりました。
- しかし、入口導線である `wbe_101.md` には human observability ladder が追加されていた一方、技術参照の中心である `wiki/measurement-stack-and-claim-ceiling.md` では、その層別整理がまだ十分に統合されておりませんでした。
- この不整合は技術・自然科学の観点で重要です。なぜなら、local ultrastructure、SV2A PET、whole-brain MRSI、31P-MRS / dynamic DMRSI、sodium MRI、MRS thermometry、myelin bilayer mapping、CSF / glymphatic proxy を 1 本の「human evidence is getting close」という物語に潰すと、`human proxy-rich evidence` が `human near-direct maintenance-state observation` に誤変換されやすくなるからです。

## 根拠付き批判

### 1. 旧 measurement-stack page は stack 差は説明できていましたが、human maintenance-state proxy の層差を site-wide rule にしていませんでした

- 問題:
  - 旧 `wiki/measurement-stack-and-claim-ceiling.md` は EEG / fMRI / atlas / Patch-seq / EM / same-brain connectomics / PET / glia imaging を整理していました。
  - しかし、human 側の最近の前進を `どの proxy class なのか` で切り分ける表がありませんでした。
- 根拠:
  - Shapson-Coe et al. (2024) が押し上げたのは `local human structural scaffold` です。
  - Johansen et al. (2024) が押し上げたのは `regional synaptic-density proxy` です。
  - Lucchetti et al. (2025) が押し上げたのは `macro biochemical scaffold` です。
  - Ren et al. (2015) と Li et al. (2025) が押し上げたのは `macro energetic proxy` です。
  - Qian et al. (2012, 2025) が押し上げたのは `macro ionic proxy` です。
  - Rzechorzek et al. (2022) が押し上げたのは `macro thermal proxy` です。
  - Baadsvik et al. (2024) が押し上げたのは `macro myelin proxy` です。
  - Hirschler et al. (2025) と Dagum et al. (2026) が押し上げたのは `macro support-state proxy` です。
- 批判:
  - したがって、これらを 1 本の `human observability` として書くのは粗すぎました。
  - 技術ページでこそ、`何が直接進んだのか` と `何がまだ latent なのか` を class 名つきで固定する必要がありました。

### 2. 入口ページと technical reference の間に claim ceiling の齟齬がありました

- 問題:
  - `wbe_101.md` には human observability ladder がありました。
  - しかし `wiki/measurement-stack-and-claim-ceiling.md` には、その technical 版が存在しませんでした。
- 批判:
  - この状態では、入口では proxy class を分けて読んだ読者が、技術ページに戻ると再び `measurement stack` の大箱だけで読む構造になります。
  - site-wide rule としては、入口と本論のあいだで claim ceiling が同じ向きに並んでいなければなりません。

### 3. `human evidence exists` と `human state-complete measurement is close` の差を measurement page 自体が止め切れていませんでした

- 問題:
  - 旧 measurement page は `multimodal` や `same-brain` の誤読は止められていました。
  - しかし、human maintenance-state proxy 群を別表にしていなかったため、読者が PET / MRSI / sodium MRI / thermometry / myelin / glymphatic をまとめて「かなり見えてきた」と圧縮できる余地が残っていました。
- 批判:
  - その圧縮を許すと、current transcription / chromatin state、ECM / PNN gate state、branch-local proteostasis / synaptic-tag capture、current chloride set point、branch-local mitochondrial positioning の未観測性が埋もれます。
  - これは自然科学的には主張の過昇格です。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - front matter の description / intro / highlights / known points を更新し、human proxy classes をページの主題として前面化
  - 新規節 `#human-maintenance-proxy-ladder` を追加
  - `local structural scaffold / synaptic-density proxy / biochemical scaffold / energetic proxy / ionic proxy / thermal proxy / myelin proxy / support-state proxy / still-missing human routes` を 1 表に整理
  - `Site rule for human proxy classes` と `Why this ladder matters operationally` を追加
  - `Practical rules` に human-side summary で proxy class を名指しする規則を追加
  - augmentation table に `human maintenance-state proxies` row を追加
  - 参考文献を追加
- `github-wiki-export/measurement-stack-and-claim-ceiling.md`
  - 上記の technical 改稿を GitHub Wiki export 側にも同期

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と GitHub Wiki export の改稿で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
4. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
5. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
6. Qian Y, Zhao T, Zheng H, Weimer J, Boada FE. High-resolution sodium imaging of human brain at 7 T. *Magnetic Resonance in Medicine*. 2012;68(1):227-233.
   - https://doi.org/10.1002/mrm.23225
7. Qian Y, Lin YC, Chen X, et al. Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. *Scientific Reports*. 2025;15:27427.
   - https://doi.org/10.1038/s41598-025-07800-1
8. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022;145(6):2031-2048.
   - https://doi.org/10.1093/brain/awab466
9. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
10. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
11. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
