# Site Deepening Audit (2026-03-16, Entry Pages / Multimodal Evidence Class and BOLD Proxy Ceiling)

## 対象

- 主対象: `index.md`
- 主対象: `wbe_101.md`
- 補強対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 補強対象: `wiki/multimodal-integration-basics.md`

## 今回の選定理由

- 2026-03-16 時点で、詳細 wiki 側では `multimodal` の evidence class と `fMRI/BOLD` の proxy ceiling がかなり明確に整理されていました。
- しかし、公開サイトの入口である `index.md` と `wbe_101.md` では、まだ
  - `multimodal` が少なくとも 4 種類の acquisition relation に分かれること
  - EEG-fMRI で shared clock があっても BOLD を direct neural truth と読めないこと
  - BOLD と酸素代謝が cortical voxel レベルで逆向きになりうること
  が十分に前景化されていませんでした。
- この欠落は重大でございます。入口ページが緩いままだと、詳細ページで厳しく設定した claim ceiling より前に、読者が `multimodal = 強い mechanistic evidence` と誤読しうるからです。

## 根拠付き批判

### 1. 入口ページは `multimodal` の中身をまだ 1 語で流しやすかったです

- `Burns et al. (2024)` と `Pernet et al. (2019)` が押し上げるのは、主として metadata と schema の再利用可能性です。
- `Kothe et al. (2025)` は LSL が synchronized multimodal recording を支えることを整理しつつ、device-side delay や display latency の真値まで自動で与えるわけではないことを示しました。
- `Wirsich et al. (2021)` は simultaneous EEG-fMRI の reproducible cross-modal concordance を示しましたが、そこで強くなるのは shared clock 下の整合であり、mechanistic truth ではありません。
- したがって、`器`、`同時計測`、`侵襲校正`、`atlas / prior` を 1 つの `multimodal` へ潰すと、何が直接増えたのかが消えます。

### 2. 入口ページは `fMRI は proxy` とだけ書き、proxy の壊れ方をまだ十分に具体化していませんでした

- `Logothetis et al. (2001)` は BOLD が単純な multiunit output よりも局所場電位に強く結びつくことを示しました。
- `Sirotin & Das (2009)` と `Cardoso et al. (2012)` は task-related / anticipatory haemodynamics が local neuronal activity とずれうることを示しました。
- `Handwerker et al. (2004)` と `Bailes et al. (2023)` は HRF の個体差・領域差・局所差を示しました。
- `Kay et al. (2019)` と `Kurzawski et al. (2022)` は venous / non-neural factor が BOLD map を歪めうることを示しました。
- よって、`fMRI は血流 proxy` とだけ書くのでは足りず、どの failure mode が解釈 ceiling を作るかまで前景化する必要があります。

### 3. 2025年12月16日公開の一次文献が、BOLD 過読への追加警告を与えました

- `Epp et al. (2025)` は human cortex の calibrated fMRI で、BOLD と酸素代謝変化が有意 voxel の約 40% で逆向きになりうることを示しました。
- これは重要でございます。なぜなら、shared clock や細かい voxel map があっても、`BOLD の符号 / 振幅 = local metabolic demand` と読むのは強すぎることを、より直接に示すからです。
- 現行サイトの deep wiki は BOLD の proxy 性をかなり整理していましたが、この最新の定量的警告はまだ入っていませんでした。

## 今回実行した変更

- `index.md`
  - 入口ページに `multimodal を見たときに、何が本当に増えたか先に切り分けたいとき` を追加しました。
  - `同時計測 + 共有時計 / 幾何統合 / 侵襲校正 / atlas prior` を 1 語で読まない site rule を入口で明示しました。
  - Epp et al. (2025) の所見を短く追加し、Fusion Card と hemodynamic proxy gate への導線を置きました。
- `wbe_101.md`
  - hidden state と measurement stack を説明する位置に、`multimodal でも、そのまま state-complete には上げない` note を追加しました。
  - Epp et al. (2025) を使い、EEG-fMRI でも BOLD を direct neural truth と読まない境界を入口段階で固定しました。
- `wiki/measurement-stack-and-claim-ceiling.md`
  - `fMRI / BOLD を別扱いにする理由` 節を 4 failure mode から 5 failure mode へ拡張しました。
  - `BOLD-CMRO2 discordance` を新しい failure mode として追加しました。
  - site rule を `metabolic / calibrated validator または abstention condition` 必須へ更新しました。
  - 参考文献に Epp et al. (2025) を追加しました。
- `wiki/multimodal-integration-basics.md`
  - `hemodynamic proxy gate` に `BOLD-CMRO2 consistency / metabolic validator` を追加しました。
  - 短い結論に、shared clock や細かい voxel map だけでは energetic mechanism へ上げない旨を追記しました。
  - 参考文献に Epp et al. (2025) を追加しました。

## 外部依存で保留

- なし
  - 今回の変更は、このリポジトリ内の文面更新と参考文献整合で完結しています。

## 参考文献

1. Epp KJ, Lu H, Lydon-Staley DM, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. Published online 2025-12-16.
   - https://doi.org/10.1038/s41593-025-02132-9
2. Kothe C, Appelhoff S, Bullock T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025;3:IMAG.a.136.
   - https://doi.org/10.1162/imag.a.136
3. Burns M, Nii L, Williams AN, et al. Motion-BIDS: extending BIDS to support standardized storage of motion data. *Scientific Data*. 2024;11:857.
   - https://doi.org/10.1038/s41597-024-03559-8
4. Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Scientific Data*. 2019;6:103.
   - https://doi.org/10.1038/s41597-019-0104-8
5. Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. *NeuroImage*. 2021;231:117864.
   - https://doi.org/10.1016/j.neuroimage.2021.117864
6. Logothetis NK, Pauls J, Augath M, Trinath T, Oeltermann A. Neurophysiological investigation of the basis of the fMRI signal. *Nature*. 2001;412:150-157.
   - https://doi.org/10.1038/35084005
7. Sirotin YB, Das A. Anticipatory haemodynamic signals in sensory cortex not predicted by local neuronal activity. *Nature*. 2009;457:475-479.
   - https://doi.org/10.1038/nature07664
8. Cardoso MMBM, Sirotin YB, Lima B, Glushenkova E, Das A. The neuroimaging signal is a linear sum of neurally distinct stimulus- and task-related components. *Nature Neuroscience*. 2012;15:1298-1306.
   - https://doi.org/10.1038/nn.3170
9. Handwerker DA, Ollinger JM, D'Esposito M. Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses. *NeuroImage*. 2004;21:1639-1651.
   - https://doi.org/10.1016/j.neuroimage.2003.11.029
10. Kay KN, Jamison KW, Zhang RY, Uğurbil K. A critical assessment of data quality and venous effects in sub-millimeter fMRI. *NeuroImage*. 2019;189:847-869.
   - https://doi.org/10.1016/j.neuroimage.2019.02.006
11. Kurzawski JW, Yablonskiy DA, Pointer R, et al. Non-Neural Factors Influencing BOLD Response Magnitudes within Individual Subjects. *Journal of Neuroscience*. 2022;42:7256-7266.
   - https://doi.org/10.1523/JNEUROSCI.2532-21.2022
