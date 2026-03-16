# 2026-03-16 Site Deepening Audit: U7 Multimodal Evidence Classes

## 選定対象

- 公開サイト内で今回もっとも深掘りして更新すべき箇所として、`research_harvest_50.md` の `U7: マルチモーダル整合` と、それに連動する `mind_uploading_papers.md` の技術優先ルートを選定しました。

## 選定理由

- 他の主要ページでは、2026-03 の更新で `multimodal` を 1 語で読まないための境界が既に強化されていました。
- しかし文献ハブ側では、なお `BIDS/LSL の器`、`同時計測の concordance`、`侵襲校正`、`BOLD proxy ceiling` が十分に分離されておらず、技術読者が「整った metadata」や「shared clock」を、そのまま `direct neural truth` の強化と誤読しやすい構造が残っていました。
- これは site-wide の scientific consistency を損ねます。文献の入口が緩いままだと、後段ページで厳しく設定した claim ceiling が入口で破られるためです。

## 根拠付き批判

### 1. 器と証拠クラスが混ざっていました

- `Pernet et al. (2019)` と `Burns et al. (2024)` が与えるのは、EEG-BIDS / Motion-BIDS による **metadata と coordinate frame の共有可能性**です。
- `Kothe et al. (2025)` は LSL が synchronized multimodal recording を支える一方、**device-side delay や display latency の真値までは自動で与えない**と整理しています。
- したがって、BIDS / Motion-BIDS / LSL は重要ですが、これだけで multimodal gain や neural truth は主張できません。

### 2. 同時計測の concordance と mechanistic truth が混ざっていました

- `Jorge et al. (2015)` は simultaneous EEG-fMRI の artifact prevention と safety assessment を成立条件として示しました。
- `Wirsich et al. (2021)` は 1.5T〜7T にまたがる simultaneous EEG-fMRI で connectome 関係の再現可能性を示しました。
- しかしここで強くなるのは **shared clock 下の cross-modal concordance**であり、trial-level causal order や fine-grained mechanism ではありません。

### 3. 侵襲校正の coverage limit が前面に出ていませんでした

- `Mikulan et al. (2020)` は intracerebral stimulation + HD-EEG の ground-truth dataset を公開しました。
- `Unnwongse et al. (2023)` は intracranial electric stimulation による direct validation を示しました。
- `Hao et al. (2025)` は simultaneous HD-EEG / SEEG で source depth と source power が誤差を強く左右することを示しました。
- したがって direct validation route は重要ですが、これは **coverage-limited な local calibration**であり、whole-brain ground truth ではありません。

### 4. EEG-fMRI の ceiling を作る BOLD proxy 問題が文献導線で弱かったです

- `Logothetis et al. (2001)` は BOLD が単純な multiunit output より LFP に強く結びつくことを示しました。
- `Lee et al. (2010)` は cell type / wiring に依存して global / local fMRI signal が変わることを示しました。
- `Sirotin & Das (2009)` と `Cardoso et al. (2012)` は task-related haemodynamics が local neuronal activity だけでは閉じないことを示しました。
- `Handwerker et al. (2004)` は HRF の被験者差・領域差を、`Kay et al. (2019)` と `Kurzawski et al. (2022)` は venous / non-neural factor の空間バイアスを示しました。
- したがって EEG-fMRI の文献導線では、shared clock の話と同時に **hemodynamic proxy ceiling** を必ず提示する必要があります。

## 今回実行した変更

- `research_harvest_50.md`
  - `last_updated` を `2026-03-16` に更新しました。
  - 技術優先ルートの `U1 / U7` 行を、`取得関係・共有時計・侵襲校正・hemodynamic proxy ceiling` を読む行に修正しました。
  - `2026-03 U7 再監査：multimodal を 4 つの証拠クラスへ分けます` 節を追加しました。
  - `U7` のリサーチクエスチョン、既知、未解決、主要先行研究を、`器 / 同時計測 / 侵襲校正 / proxy ceiling` の4クラスで再構成しました。
- `mind_uploading_papers.md`
  - 技術優先ルートに `multimodal alignment / hemodynamic gate` を追加しました。
  - 年別アーカイブを読む前に、multimodal 文献を `shared clock` と `BOLD proxy ceiling` で分けて読む導線を追加しました。

## 参考文献

- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Scientific Data*. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Burns M, Nii L, Williams AN, et al. Motion-BIDS: extending BIDS to support standardized storage of motion data. *Scientific Data*. 2024.
  - https://doi.org/10.1038/s41597-024-03559-8
- Kothe C, Appelhoff S, Bullock T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
  - https://doi.org/10.1162/imag.a.136
- Jorge J, Grouiller F, Ipek O, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. *NeuroImage*. 2015.
  - https://doi.org/10.1016/j.neuroimage.2014.10.055
- Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. *NeuroImage*. 2021.
  - https://doi.org/10.1016/j.neuroimage.2021.117864
- Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Communications*. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
- Logothetis NK, Pauls J, Augath M, Trinath T, Oeltermann A. Neurophysiological investigation of the basis of the fMRI signal. *Nature*. 2001.
  - https://doi.org/10.1038/35084005
- Lee JH, Durand R, Gradinaru V, et al. Global and local fMRI signals driven by neurons defined optogenetically by type and wiring. *Nature*. 2010.
  - https://doi.org/10.1038/nature09108
- Sirotin YB, Das A. Anticipatory haemodynamic signals in sensory cortex not predicted by local neuronal activity. *Nature*. 2009.
  - https://doi.org/10.1038/nature07664
- Cardoso MMBM, Sirotin YB, Lima B, Glushenkova E, Das A. The neuroimaging signal is a linear sum of neurally distinct stimulus- and task-related components. *Nature Neuroscience*. 2012.
  - https://doi.org/10.1038/nn.3170
- Handwerker DA, Ollinger JM, D'Esposito M. Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses. *NeuroImage*. 2004.
  - https://doi.org/10.1016/j.neuroimage.2003.11.029
- Kay KN, Jamison KW, Zhang RY, Uğurbil K. A critical assessment of data quality and venous effects in sub-millimeter fMRI. *NeuroImage*. 2019.
  - https://doi.org/10.1016/j.neuroimage.2019.02.006
- Kurzawski JW, Yablonskiy DA, Pointer R, et al. Non-Neural Factors Influencing BOLD Response Magnitudes within Individual Subjects. *Journal of Neuroscience*. 2022.
  - https://doi.org/10.1523/JNEUROSCI.2532-21.2022
