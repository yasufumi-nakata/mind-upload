# Site Deepening Audit (2026-03-19, Beginner Claim / Evidence Route Alignment)

## 対象

- 主対象: `wiki/claims-and-evidence.md`
- 副対象: `wiki/mind-upload-basics.md`
- 副対象: `wiki/verification-basics.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイト本体は、`tractography route card`、`effective-connectivity route card`、`irreversibility route card`、`Body / Environment Boundary Card`、`Specificity & Shortcut Card` など、技術・自然科学側の誤読停止ルールをかなり強く整備済みでした。
- その一方で、初心者が最初に辿りやすい `wiki/claims-and-evidence.md`、`wiki/mind-upload-basics.md`、`wiki/verification-basics.md` は 2026-03-06 / 2026-03-14 の水準に留まり、`高スコア = 強い証拠`、`graph = connectome`、`DCM = causal wiring`、`real-time = embodiment solved` といった短絡を beginner 導線で十分に止められておりませんでした。
- これは技術・自然科学の観点で重要です。なぜなら、この 3 ページは `入口の読み方` を定める役割であり、ここが古いままだと、後段の厳密な page で追加した route-card 規律が入口で希釈されるからです。

## 根拠付き批判

### 1. beginner claim-reading page は `high score` を evidence class に戻す規律が弱すぎました

- 問題:
  - 旧 `wiki/claims-and-evidence.md` は `Recovered sentences from the brain` をほぼ `L1 decoding` とだけ説明しており、どの shortcut を止めるべきかを beginner 導線で固定しておりませんでした。
  - `subject/session fingerprint`、`task constraint`、`language prior`、`calibration burden`、`cross-dataset drift` が本文から見えにくく、読者が `score` をそのまま target-specific neural evidence に読み替える余地が残っておりました。
- 根拠:
  - Chaibub Neto et al. (2019) は、subject characteristics による confounding が ML diagnostic performance を押し上げうることを示しました。
  - Di et al. (2021) は、resting-state EEG が time-robust individual identification をかなり強く支えることを示しました。
  - Xu et al. (2020) は、EEG decoding の cross-dataset variability が deep-learning generalization を崩すことを示しました。
  - Tang et al. (2023) は non-invasive semantic reconstruction を示しましたが、subject cooperation と individual calibration に強く依存します。
  - Willett et al. (2023) は高性能 speech neuroprosthesis を示しましたが、implant・participant-specific training・bounded task regime の上での前進です。
- 批判:
  - したがって beginner page で `high accuracy` を `what was measured / what shortcut remained` に戻す規律が必要でした。
  - 旧記述は `L1` と言うだけで、`なぜ L1 なのか` を支える audit 項目が薄すぎました。

### 2. beginner front door は `connectome` と `tractography graph` の evidence-class split を十分に止めていませんでした

- 問題:
  - `wiki/mind-upload-basics.md` は structure is not enough という方向性は持っていましたが、living human brain で多くの読者が最初に思い浮かべる tractography-derived graph を独立 class として beginner 導線で固定しておりませんでした。
- 根拠:
  - Thomas et al. (2014) は diffusion MRI tractography の anatomical accuracy に本質限界があることを示しました。
  - Maier-Hein et al. (2017) は tractography challenge で多数の invalid bundles が systematic に出ることを示しました。
  - Schilling et al. (2020) は高い anatomical accuracy が強い start/end/exclusion priors に依存することを示しました。
  - Grisot et al. (2021) は same-brain validation で recurring failure modes を示しました。
- 批判:
  - したがって beginner route でも `connectome` を一語で扱うのは粗すぎます。
  - 入口の時点で `tractography graph = macro pathway prior` を明文化しないと、読者は graph の語感だけで structural completeness を過大読みにできます。

### 3. verification beginner page は `generic audit` で足りるように読めました

- 問題:
  - 旧 `wiki/verification-basics.md` は standard / benchmark / prereg / audit の4点セットを説明していましたが、claim family ごとに別 route card が必要な理由を beginner 向けに説明しておりませんでした。
  - そのため、読者が `audit を付ければ全部同じように厳密になる` と誤解する余地が残っていました。
- 根拠:
  - Penny et al. (2004) と Rosa et al. (2012) は DCM inference が candidate model space に依存することを固定しました。
  - Lynn et al. (2021) と Ishihara & Shimazaki (2025) は thermodynamic language が estimator family ごとに別物であることを示しました。
  - Musall et al. (2019) と Flesher et al. (2021) は closed-loop / brain control 読解で boundary disclosure が必要なことを支持します。
- 批判:
  - したがって verification beginner page は `route card` を beginner vocabulary に昇格させる必要がありました。
  - 単なる generic audit では、claim-specific な failure mode を隠してしまいます。

## 今回実行した変更

- `wiki/claims-and-evidence.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - `L0-L5` の beginner table を全面改稿し、L1/L2/L3 の minimum evidence floor を route-card 前提で再定義しました。
  - headline translation table を追加し、decode / biomarker / tractography / effective connectivity / thermodynamic / closed loop の safe default reading を固定しました。
  - `Why the beginner rules had to become stricter` 節を新設し、primary literature に基づく誤読停止理由を分野別に追記しました。
  - 参考文献を新設し、Chaibub Neto (2019), Xu (2020), Di (2021), Tang (2023), Willett (2023), Thomas (2014), Maier-Hein (2017), Schilling (2020), Grisot (2021), Penny (2004), Rosa (2012), Frässle (2016, 2021), Lynn (2021), de la Fuente (2023), Ishihara & Shimazaki (2025), Musall (2019), Saleem (2013), Flesher (2021) を追加しました。
- `wiki/mind-upload-basics.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - beginner overview を全面的に書き直し、`high score / one graph / one model / one real-time demo` を evidence class に戻す front-door note を追加しました。
  - `What this site is trying to build` 節に beginner 導線の次ページ選択 table を追加しました。
  - 参考文献を追加し、front door の stricter reading が一次文献に支えられていることを明示しました。
- `wiki/verification-basics.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - `route card` を beginner vocabulary へ昇格させ、standard / benchmark / prereg / route card / audit の 5 部品へ再整理しました。
  - claim family ごとに必要な card を示す table を追加しました。
  - 参考文献を追加し、generic audit では足りない理由を一次文献に結びつけました。

## 外部依存で保留

- なし
  - 今回の作業は公開 wiki 本文と監査メモの更新で完結しております。

## 参考文献

1. Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019;2:99.
   - https://doi.org/10.1038/s41746-019-0178-x
2. Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. *Frontiers in Human Neuroscience*. 2020;14:103.
   - https://doi.org/10.3389/fnhum.2020.00103
3. Di Y, An X, Zhong W, Liu S, Ming D. The time-robustness analysis of individual identification based on resting-state EEG. *Frontiers in Human Neuroscience*. 2021;15:672946.
   - https://doi.org/10.3389/fnhum.2021.672946
4. Tang J, LeBel A, Jain S, Huth AG. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nature Neuroscience*. 2023;26:858-866.
   - https://doi.org/10.1038/s41593-023-01304-9
5. Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023;620:1031-1036.
   - https://doi.org/10.1038/s41586-023-06377-x
6. Thomas C, Ye FQ, Irfanoglu MO, et al. Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. *PNAS*. 2014;111(46):16574-16579.
   - https://doi.org/10.1073/pnas.1405672111
7. Maier-Hein KH, Neher PF, Houde J-C, et al. The challenge of mapping the human connectome based on diffusion tractography. *Nature Communications*. 2017;8:1349.
   - https://doi.org/10.1038/s41467-017-01285-x
8. Schilling KG, Petit L, Rheault F, et al. Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. *Brain Structure and Function*. 2020;225(8):2387-2402.
   - https://doi.org/10.1007/s00429-020-02129-z
9. Grisot G, Haber SN, Hawrylycz M, Yendiki A, et al. Diffusion MRI and anatomic tracing in the same brain reveal common failure modes of tractography. *NeuroImage*. 2021;239:118300.
   - https://doi.org/10.1016/j.neuroimage.2021.118300
10. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004;22(3):1157-1172.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
11. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012;208(1):66-78.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
12. Frässle S, Paulus FM, Krach S, Jansen A. Test-retest reliability of effective connectivity in the face perception network. *Human Brain Mapping*. 2016;37(2):730-744.
   - https://doi.org/10.1002/hbm.23061
13. Frässle S, Manjaly ZM, Do CT, et al. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021;225:117491.
   - https://doi.org/10.1016/j.neuroimage.2020.117491
14. Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021;118(47):e2109889118.
   - https://doi.org/10.1073/pnas.2109889118
15. de la Fuente LA, Zamberlan F, Bocaccio H, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. *Cerebral Cortex*. 2023;33(5):1856-1865.
   - https://doi.org/10.1093/cercor/bhac177
16. Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*. 2025;16:10852.
   - https://doi.org/10.1038/s41467-025-66669-w
17. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019;22:1677-1686.
   - https://doi.org/10.1038/s41593-019-0502-4
18. Saleem AB, Ayaz A, Jeffery KJ, Harris KD, Carandini M. Integration of visual motion and locomotion in mouse visual cortex. *Nature Neuroscience*. 2013;16:1864-1869.
   - https://doi.org/10.1038/nn.3567
19. Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. *Science*. 2021;372(6544):831-836.
   - https://doi.org/10.1126/science.abd0380
