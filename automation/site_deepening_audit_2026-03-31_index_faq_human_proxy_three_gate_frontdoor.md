# Site Deepening Audit (2026-03-31, index / FAQ human-proxy three-gate front-door sync)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- `wiki/human-proxy-composition.md` と `verification.md` では既に、
  - `robustness`
  - `effective time window / physiological-regime compatibility`
  - `increment over the strongest single row + disagreement topology`
  まで含めた `three-gate` ルールが成立しておりました。
- しかし front door である `index.md` と `faq.md` では、human-proxy stop line が依然として主に
  - `proxy class`
  - `operational maturity`
  - `calibrator role`
  に寄っており、読者が再び
  - `proxy-rich = almost same-subject state identification`
  - `same-session = one state axis`
  - `repeatable once = portable bundle`
  - `multimodal gain = disagreements solved`
  と圧縮できる余地が残っておりました。
- この project では deep page だけ厳密でも不十分でございます。入口が弱いと、下層ページでどれだけ strict な route card を置いても、読者モデルが先に歪みます。

## web確認対象

- https://doi.org/10.1523/JNEUROSCI.1750-23.2024
- https://doi.org/10.1038/s41467-025-66124-w
- https://doi.org/10.1093/pnasnexus/pgaf072
- https://doi.org/10.1038/s41467-026-68374-8
- https://doi.org/10.1186/s41747-024-00426-4
- https://doi.org/10.1177/0271678X17724947
- https://doi.org/10.1016/j.neuroimage.2021.117864
- https://doi.org/10.1038/s41467-023-44363-z
- https://doi.org/10.1038/s41467-025-64414-x
- https://doi.org/10.1038/s41593-025-01945-y
- https://doi.org/10.1038/s41593-025-02132-9
- https://doi.org/10.1038/s41591-024-03019-1
- https://doi.org/10.1093/brain/awaf412

## 根拠付き批判

### 1. front door の human-proxy 停止線は、deep page 側の `three-gate` ルールより弱うございました

- 既存の `index.md` と `faq.md` は、
  - `proxy class`
  - `operational maturity`
  - `calibrator role`
  の重要性を明示しておりました。
- しかし、それだけではなお
  - 同じ subject で何か複数測った
  - modality が多い
  - それぞれ論文として成立している
  という事実をもって、`same-subject state identification` に近い印象を与え得ます。

批判:

- `three axes` だけでは `bundle failure mode` が止まりません。
- 本当に必要なのは、bundle が
  - operationally robust か
  - biologically same axis と読めるか
  - strongest single row を超える incremental value を持つか
  を separate gate として front door で止めることでございます。

### 2. `same-session` でも one state variable とは限りません

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は simultaneous Ca2+ / BOLD で `common and divergent` organization を示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で `coupled global progression` と `two distinct network patterns` を示しました。
- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は global fMRI mode が autonomic physiology と強く結びつくことを示しました。
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は、significant task BOLD changes と opposite oxygen-metabolism changes が同じ cortex で共存し得ることを示しました。

批判:

- したがって `same-session multimodal` を one solved state sample と読むのは不正確でございます。
- front door で少なくとも
  - `effective time window / state axis`
  - `physiological or perturbation regime compatibility`
  - `shared-driver audit`
  を要求しなければ、`同期している = 同じ hidden state を見ている` という誤読を止められません。

### 3. `repeatability once` と `portability of the bundle` は別問題でございます

- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は、3 T DMI の repeatability が stated oral-glucose protocol と time-point window に依存することを示しました。
- [Finnema et al. (2018)](https://doi.org/10.1177/0271678X17724947) は、[11C]UCB-J SV2A PET の regional V_T に対して route-specific な 3-9% の mean absolute test-retest reproducibility を示しました。
- [Wirsich et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.117864) は、一部の simultaneous EEG-fMRI connectome relation が 4 centres / 1.5T-7T を跨いでも再現し得ることを示しました。

批判:

- これらは `repeatability exists` という一言に圧縮してよい文献ではございません。
- むしろ
  - route-local repeatability
  - cross-centre / cross-protocol transfer
  - overlap / complete-case geometry
  を分けて書かなければ、`once reproducible = deployable bundle` という誤読を front door が許します。

### 4. `average multimodal gain` と `discordance solved` も別でございます

- [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1) は multimodal assessment が uncertainty と long-term outcome prediction を改善し得る一方で、marker discrepancy が `choice paralysis` や biased decisions を生み得ると明示しました。
- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は multimodal multicentre モデルで performance gain を示しつつ、`pairwise disagreements` が MCS や improved patients で高いことを示しました。

批判:

- よって `bundle improved` をもって `bundle converged` と読んではなりません。
- front door は
  - where disagreement concentrates
  - what resolution policy is used
  - whether the bundle beats the strongest single row under matched conditions
  を最低限固定する必要がございました。

## 今回実行した変更

### `index.md`

- `page_highlights` の human-proxy bullet を、`effective time window / physiological-regime compatibility`, `route-local repeatability versus transfer`, `disagreement handling` まで含む文言へ強化しました。
- `known_points` の proxy-composition bullet を、`effective time window / regime compatibility`, `route-local repeatability versus transfer`, `disagreement topology` まで含む stop line へ更新しました。
- `If You Want To Know When Several Human Proxy Rows May Be Combined` の note-box を全面的に強化し、front door で
  - robustness
  - shared-driver / effective-window
  - increment-plus-disagreement
  の 3 gate を明示しました。
- その直下に `Front-door gate` table を追加し、
  - what must be shown
  - why the gate exists
  を landing page レベルで固定しました。

### `faq.md`

- `page_highlights` に、three-axis の後でも `three-gate composition check` が必要であることを追加しました。
- `known_points` に、proxy class / maturity / calibrator role の後でも bundle-level gates が必要であることを追加しました。
- `Eleven technical guards now fixed at the front door` に、human-proxy stop rule を
  - robustness gate
  - effective-window / physiological-regime compatibility gate
  - increment-over-the-strongest-single-row gate with disagreement handling
  まで含む文言へ更新しました。

## 今回止めた誤読

- `proxy-rich` = `same-subject state identification is almost done`
- `same-session` = `same hidden-state axis`
- `repeatable at one operating point` = `portable bundle`
- `multimodal average gain` = `disagreements are solved`
- `three axes are logged` = `composition problem is solved`

## 検証

- `bundle exec jekyll build`
- `git diff --stat`
- `git diff --check`

## external dependency tasks

- なし
  - 今回の作業は web 文献確認、front door 文言修正、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Johansen A, et al. Healthy-human SV2A atlas / baseline route. *J Neurosci*. 2024. https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Lucchetti J, et al. Five-metabolite human 1H-MRSI similarity scaffold. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-66124-w
3. Li X, et al. Dynamic deuterium kinetic-rate imaging in five healthy participants. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
4. Dagum P, et al. Sleep-linked biomarker-efflux route in a multi-site randomized crossover design. *Nat Commun*. 2026. https://doi.org/10.1038/s41467-026-68374-8
5. Bøgh N, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *Eur Radiol Exp*. 2024. https://doi.org/10.1186/s41747-024-00426-4
6. Finnema SJ, et al. Kinetic evaluation and test-retest reproducibility of [11C]UCB-J in humans. *J Cereb Blood Flow Metab*. 2018. https://doi.org/10.1177/0271678X17724947
7. Wirsich J, et al. Reproducibility of simultaneous EEG-fMRI connectome relationships across centres and field strengths. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.117864
8. Vafaii N, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent cortical organization. *Nat Commun*. 2024. https://doi.org/10.1038/s41467-023-44363-z
9. Chen J, et al. Simultaneous EEG-PET-MRI can show coupled global progression plus distinct network patterns. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-64414-x
10. Bolt T, et al. Autonomic physiological coupling of the global fMRI signal. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-01945-y
11. Epp JR, et al. Task BOLD and oxygen-metabolism changes can diverge in sign. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-02132-9
12. Rohaut B, et al. Multimodal assessment improves neuroprognosis performance but increases discrepancy risk across markers. *Nat Med*. 2024. https://doi.org/10.1038/s41591-024-03019-1
13. Manasova A, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026. https://doi.org/10.1093/brain/awaf412
