# 2026-03-31 site deepening audit: datasets / beginner inverse-family sync

## 対象として選んだ箇所

- `datasets.md`
- `wiki/verification-basics.md`

今回ここを優先した理由は、2026-03-31 時点で core policy 側では `inverse family` の停止条件がかなり明確になっている一方、practical / beginner 側ではまだ `direct validation board + solver winner = one stronger truth meter` と読める余地が残っていたためです。入口と実務ページでこの誤読を止められないと、深部ページでいくら厳密にしても再圧縮が起きます。

## 根拠付き批判

### 1. `validation class` と `source regime` だけでは、inverse family ごとに違う target object / uncertainty object を止め切れません

- [Luria et al. (2024)](https://doi.org/10.3389/fnhum.2024.1359753) は、M/EEG source localization を **probabilistic focal-support** として返します。
- [Tong et al. (2025)](https://doi.org/10.1109/TMI.2024.3506596) は、**sparse spatial-temporal** source imaging に対して **debiased estimation / inference** を与えます。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は、**extended-source reconstruction** を uncertainty quantification 付きで扱います。
- したがって、`same board` や `same C-stage data` だけで 1 本の solver leaderboard にまとめるのは粗いです。family が違う時点で、そもそも何を recover し、どの uncertainty を返しているかが違います。

### 2. forward-model uncertainty は inverse family の見栄えとは独立に残ります

- [Vorwerk et al. (2024)](https://doi.org/10.3389/fnhum.2024.1335212) は、tissue conductivity uncertainty が EEG source analysis に大きく効くことを示しました。
- [Vorwerk et al. (2026)](https://doi.org/10.1088/1741-2552/ae2f01) は、individually estimated skull conductivity が source-analysis uncertainty を減らしうる一方で、brain base では改善が限定的であることも示しました。
- よって、posterior map や debiased interval が整って見えても、upstream physics が自動で監査済みになるわけではありません。

### 3. `direct validation` 自体も one board ではありません

- [Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219) は **in-vivo focal-source** board です。
- [Unnwongse et al. (2023)](https://doi.org/10.1093/braincomms/fcad023) は **intracranial electrical stimulation** board です。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は **simultaneous HD-EEG / SEEG** board です。
- [Jahromi et al. (2026)](https://doi.org/10.1016/j.compbiomed.2026.111449) は **3D-printed pediatric deep-source phantom** board です。
- これらは source depth, geometry, validation object, and operating regime が違います。したがって `directly validated` という一語だけでは benchmark portability を正当化できません。

### 4. この弱点は実務入口と beginner page で直すべきでした

- `datasets.md` は practical page であり、ここが粗いままだと実装者が最初に `same raw data + one score` の比較へ流れやすくなります。
- `wiki/verification-basics.md` は beginner の規範ページであり、ここが粗いままだと site-wide rule の最小公倍数が下がります。
- したがって今回は、新しい technical deep page を増やすより、既に成立している inverse-family policy を実務入口と beginner page に同期する方が合理的でした。

## 今回実行した変更

### `datasets.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `page_highlights` / `known_points` を、inverse family / uncertainty object を明示する文言へ更新しました。
- C-stage public benchmark の note-box に、`Jahromi et al. (2026)` の deep-source phantom board を追加し、validation board の非一様性を visible にしました。
- inverse-benchmark-board section を更新し、
  - `validation class`
  - `source regime / target object`
  - `inverse family / uncertainty object`
  - `same-geometry controls`
  - `sensitivity sweep`
  の 5 軸で読むよう固定しました。
- `Inverse family is not just a solver style label` note-box を追加しました。
- benchmark table に `Inverse-family comparison under one named board` 行を追加しました。
- disagreement table と section rule を更新し、public benchmark の最小開示項目に `inverse family plus the uncertainty object it returns` を追加しました。
- references に `Vorwerk 2024`, `Luria 2024`, `Tong 2025`, `Vorwerk 2026`, `Jahromi 2026` を追加しました。

### `wiki/verification-basics.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `page_highlights` / `known_points` で、ESI route card に `inverse family / uncertainty object` を追加しました。
- `2026-03-31 correction: ESI route cards also need inverse-family and uncertainty-object disclosure` note-box を追加しました。
- claim-family table の `EEG source imaging / inverse reconstruction` row を更新し、初心者向けにも inverse-family split を visible にしました。
- references に `Vorwerk 2024`, `Luria 2024`, `Tong 2025`, `Vorwerk 2026`, `Jahromi 2026` を追加しました。

## 今回止めた誤読

- `C-stage direct validation = one universal ESI truth board`
- `probabilistic / debiased / extended-source` は同じ hidden object を別表現で見ているだけ
- `better uncertainty map = forward-model uncertainty もほぼ処理済み`
- `one direct-validation win = other source regimes / geometries / depths へもそのまま移植可能`
- `datasets page と beginner page は深部 page ほど厳密でなくてもよい`

## 検証

- `bundle exec jekyll build` を実行してビルド通過を確認する
- `git diff --stat` と要点 diff で反映箇所を確認する

## external dependency tasks

- 今回の主作業に関して、外部依存で止めた項目はありません。

## 参考文献

1. Luria G, Viani S, Pascarella A, et al. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Frontiers in Human Neuroscience*. 2024. https://doi.org/10.3389/fnhum.2024.1359753
2. Tong PF, Yang H, Ding X, et al. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Transactions on Medical Imaging*. 2025. https://doi.org/10.1109/TMI.2024.3506596
3. Feng Z, Guan C, Sun Y. Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. *IEEE Transactions on Medical Imaging*. 2025. https://doi.org/10.1109/TMI.2025.3642620
4. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024. https://doi.org/10.3389/fnhum.2024.1335212
5. Vorwerk J, Rampp S, Wolters CH, Baumgarten D. Potential of EEG and EEG/MEG skull conductivity estimation to improve source analysis in presurgical evaluation of epilepsy. *Journal of Neural Engineering*. 2026. https://doi.org/10.1088/1741-2552/ae2f01
6. Pascarella A, Mikulan E, Sciacchitano F, et al. An in-vivo validation of ESI methods with focal sources. *NeuroImage*. 2023. https://doi.org/10.1016/j.neuroimage.2023.120219
7. Unnwongse K, Van Klink N, Tousseyn S, et al. Validating EEG source imaging using intracranial electrical stimulation. *Brain Communications*. 2023. https://doi.org/10.1093/braincomms/fcad023
8. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025. https://doi.org/10.1111/epi.18552
9. Jahromi S, Sdoukopoulou G, Chikara RK, et al. 3D printed pediatric head phantom for assessing deep epileptic sources localization. *Computers in Biology and Medicine*. 2026. https://doi.org/10.1016/j.compbiomed.2026.111449
