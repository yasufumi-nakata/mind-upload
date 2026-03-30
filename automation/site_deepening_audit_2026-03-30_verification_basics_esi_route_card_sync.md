# Site Deepening Audit (2026-03-30, verification-basics ESI route-card sync)

## 対象

- 主対象:
  - `wiki/verification-basics.md`
- 調査範囲:
  - 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `wiki/verification-basics.md` は、Verification Commons の入門ページとして「なぜ generic score sheet では足りないか」を最初に説明する位置にございます。
- しかし 2026-03-30 時点では、この beginner layer に
  - `EEG source imaging / inverse reconstruction`
  の claim family が table ごと抜けており、
  - `validation class`
  - `source regime`
  - `montage / coverage policy`
  - `focal-centre vs source-extent`
  の区別が、より深い `datasets.md` / `eeg_101.md` / `verification.md` にしか置かれておりませんでした。
- そのままですと、初学者が
  - `one localization score`
  - `HD vs low-density`
  - `direct validation`
  をそれぞれ一段圧縮して読んでしまう余地が残ります。

## 主要結論

- beginner page にも、ESI は独立の claim family として置く必要がございました。
- 現在の一次文献が支持する safer reading は、
  - `named validation class`
  - `source regime`
  - `same-geometry controls including montage / coverage policy`
  - `target object (centre / extent / overlap / propagation)`
  を分けることでございます。
- よって `wiki/verification-basics.md` にも、ESI 用の route-card entry と、その理由を支える note / references を同期すべきでございました。

## 根拠付き批判

### 1. beginner page の claim-family table に ESI が欠けていたのは site rule と不整合でございました

- `verification.md` と `datasets.md` では、すでに
  - `simulation / phantom`
  - `intracranial stimulation`
  - `simultaneous invasive recording`
  - `postsurgical outcome`
  が別 validation class であると固定されております。
- しかし `wiki/verification-basics.md` の「Why modern neuroscience needs claim-specific route cards」table には、その claim family 自体が載っておりませんでした。

批判:

- これでは beginner page だけ読む読者にとって、
  - decode
  - tractography
  - effective connectivity
  - thermodynamics
  - closed loop
  - human proxy
  - bridge
  は独立の失敗様式を持つ一方、
  - ESI
  だけは generic caution で十分であるかのように見えてしまいます。
- site-wide policy と揃えるためには、ESI も独立の claim family として明示する必要がございました。

### 2. `HD vs low-density` を beginner page で止めないのは粗すぎます

- [Horrillo-Maysonnial et al. (2023)](https://doi.org/10.1016/j.clinph.2023.08.009) は、`33-36 electrodes` の targeted-density montage が `83-electrode` HD montage に対して `54/58` sublobar concordance (`93%`) を示しつつ、`tangential generators` では距離が悪化することを示しました。
- [Rong et al. (2025)](https://doi.org/10.1016/j.clinph.2025.04.009) は、DeepSIF が `75 -> 16 electrodes` にわたって比較的安定し、`7.9/9.0 mm` の spatial dispersion を示した一方、従来法との差を残しております。

批判:

- したがって beginner layer でも、
  - `high density is the only serious route`
  も、
  - `low density solved the density problem`
  も、
  どちらも止める必要がございます。
- より安全な rule は `montage / coverage policy + solver family + source regime + validation class` で読むことです。

### 3. `direct validation` でも source depth / conductivity / target object は残ります

- [Unnwongse et al. (2023)](https://doi.org/10.1093/braincomms/fcad023) は、intracranial stimulation を ground truth にしても conductivity と depth dependence が localization error を動かすことを示しました。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は、simultaneous HD-EEG / SEEG において ictal ESI (`14.07 ± 4.62 mm`) が interictal ESI (`17.38 ± 4.16 mm`) より良好でも、`source depth` と `spike power` が依然として精度を左右すると示しました。

批判:

- beginner page でも `directly validated` を one solved rung と見せてはいけません。
- さらに [Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219) は focal-source benchmark において method ranking と parameter sensitivity を系統比較し、[Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は extended-source reconstruction 自体を別 object として扱っております。
- したがって `centre error` と `source extent` は同じ benchmark object ではなく、beginner page でも分けて導入すべきでございました。

## 今回実行した変更

- `wiki/verification-basics.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` に ESI beginner rule を追加しました。
  - 新規 note-box
    - `2026-03-30 correction: ESI route cards also need validation-class, montage, and target-object disclosure`
    を追加しました。
  - `Why modern neuroscience needs claim-specific route cards` table に
    - `EEG source imaging / inverse reconstruction`
    の row を追加しました。
  - `Representative primary-literature reasons` に ESI route-card rationale を追加しました。
  - `How this beginner page connects to the site` table に
    - `Datasets and Hands-On Work`
    - `EEG 101`
    への ESI-specific 読者導線を追加しました。
  - 参考文献へ
    - Horrillo-Maysonnial 2023
    - Rong 2025
    - Unnwongse 2023
    - Hao 2025
    - Pascarella 2023
    - Feng 2025
    を追加しました。

## 今回止めた誤読

- `one localization score = improved source imaging in general`
- `HD-EEG = serious / low-density = weak`
- `DeepSIF low-density success = density no longer matters`
- `direct validation = geometry / depth / conductivity solved`
- `focal-centre benchmark = source-extent / overlap / propagation benchmark`

## 外部依存タスク

- なし
  - 今回の作業は、一次文献確認、repo 内ページ改稿、export / build 検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Horrillo-Maysonnial A, Avigdor T, Abdallah C, et al. Targeted density electrode placement achieves high concordance with traditional high-density EEG for electrical source imaging in epilepsy. *Clinical Neurophysiology*. 2023;156:262-271.
   - https://doi.org/10.1016/j.clinph.2023.08.009
2. Rong J, Sun R, Joseph B, Worrell G, He B. Deep learning-based EEG source imaging is robust under varying electrode configurations. *Clinical Neurophysiology*. 2025;175:2010730.
   - https://doi.org/10.1016/j.clinph.2025.04.009
3. Unnwongse K, Van Klink N, Tousseyn S, et al. Validating EEG source imaging using intracranial electrical stimulation. *Brain Communications*. 2023;5(1):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
4. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
   - https://doi.org/10.1111/epi.18552
5. Pascarella A, Mikulan E, Sciacchitano F, et al. An in-vivo validation of ESI methods with focal sources. *NeuroImage*. 2023;277:120219.
   - https://doi.org/10.1016/j.neuroimage.2023.120219
6. Feng Z, Guan C, Sun Y. Block-Champagne: A novel Bayesian framework for imaging extended E/MEG source. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2025.3642620
