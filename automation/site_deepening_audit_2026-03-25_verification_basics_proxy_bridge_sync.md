# Site Deepening Audit (2026-03-25, verification-basics proxy / bridge sync)

## 対象

- 主対象: `wiki/verification-basics.md`
- 範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `verification.md`、`wiki/human-proxy-composition.md`、`wiki/state-continuity-bridge.md`、`wbe_101.md` では、2026-03-25 時点で既に
  - `proxy-rich != same-subject state closure`
  - `same-subject / same-brain != same-state`
  - `bridge validation is its own rung`
  という stop line がかなり明確でした。
- しかし beginner 導線の `wiki/verification-basics.md` は、なお
  - decode
  - tractography
  - effective connectivity
  - thermodynamic irreversibility
  - closed loop
  の5系統を中心に説明しており、直近で重要になった
  - `Human Proxy Composition Card`
  - `State-Continuity Bridge Card`
  を前面の verification 入門としては十分に固定していませんでした。
- これは site-wide inconsistency です。最も浅い verification 入口が最も甘い規則を残すと、奥のページでどれだけ厳しく止めても、読者は front door で「proxy が多い = state に近い」「same subject = same state」と誤読しやすいからです。

## 根拠付き批判

### 1. living-human proxy bundle は 1 本の progress bar ではありません

- [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024) は、`[11C]UCB-J` に基づく in vivo human synaptic-density atlas を提示しましたが、これは regional SV2A density proxy です。
- [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は、5 metabolite に基づく parcel-level metabolic similarity object を提示しましたが、これは structural wiring でも kinetic rate でもありません。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は、dynamic deuterium MRSI と kinetic model により glucose-related rate を推定しましたが、small-cohort・specialized hardware・model burden を伴います。
- [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) は myelin bilayer mapping を in vivo human で示しましたが、proof-of-principle 的な specialized route です。
- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) は MRI で CSF mobility を測定しましたが、paper 自身が flow / diffusion とは区別しています。
- [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は randomized crossover trial で sleep-linked brain-to-plasma efflux を model-based に扱いましたが、これは overnight biomarker-efflux route です。

批判:

- したがって、living-human route を beginner page で `human evidence improved` とだけ扱うのは、2026-03 時点では粗すぎます。
- density, similarity, rate, mobility, model-based efflux は異なる inferential object であり、同じ latent state を同じ単位で見ているわけではありません。
- beginner verification page に `Human Proxy Composition Card` を置かないと、読者は「複数 row が増えた」ことを「same-subject state closure に近づいた」ことと取り違えます。

### 2. same-subject / same-brain は specimen identity であって same-state ではありません

- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520) は preservation route が extracellular space と downstream ultrastructural quality を変えることを示しました。
- [Idziak et al. (2023)](https://doi.org/10.1523/ENEURO.0104-23.2023) は live-versus-fixed comparison により、chemical fixation が membrane integrity と dendritic spine morphology を変えうることを示しました。
- [Musall et al. (2019)](https://doi.org/10.1038/s41593-019-0502-4) は richly varied movement が cortex-wide variance の大きな部分を支配することを示しました。
- [Benisty et al. (2024)](https://doi.org/10.1038/s41593-023-01498-y) は spontaneous behavior が functional-connectivity structure 自体を素早く変えることを示しました。
- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) は 10-hour EEG dynamics が decoding に効くことを示しました。

批判:

- よって `same subject` や `same brain` は specimen identity を固定しても、time continuity, regime continuity, coordinate continuity, bridge validation を自動では固定しません。
- にもかかわらず beginner verification page が bridge card を明示しないのは、`same-brain workflow = same-state evidence` という危険な短絡を front door で止め損ねています。

### 3. verification 入門でこの2 stop line を落とすと、奥ページの厳しさが front door で消えます

- 観察:
  - `wiki/human-proxy-composition.md` は proxy class / operational maturity / calibrator role を分離しています。
  - `wiki/state-continuity-bridge.md` は specimen continuity / time continuity / regime continuity / coordinate continuity を分離しています。
  - `verification.md` も card 群として既に公開仕様へ組み込んでいます。
- 批判:
  - それにもかかわらず `wiki/verification-basics.md` が旧来の5 claim family だけで止まると、verification の beginner understanding が current spec より一段甘くなります。
  - これは単なる導線不足ではなく、scientific stop line の脱落です。

## 今回実行した変更

- `wiki/verification-basics.md`
  - `last_updated` を `2026-03-25` に更新しました。
  - front matter の `description` / `page_intro` / `page_highlights` / `known_points` / `unknown_points` を改稿し、`human proxy composition` と `state-continuity bridge` を beginner verification の中核 stop line に昇格しました。
  - `wiki_links` に `Wiki: Human Proxy Composition and Route Maturity` と `Wiki: State-Continuity Bridge` を追加しました。
  - 冒頭 abstract を改稿し、比較対象として `metric bundle` `proxy combination` `bridge assumption` を明示しました。
  - `2026-03-25 beginner tightening` note-box を追加し、proxy bundle と bridge が side detail ではなく scientific stop line であることを固定しました。
  - `The five parts of comparable progress` table の benchmark / route card / audit 記述を current site rule に合わせて更新しました。
  - `What goes wrong when one part is missing` table を改稿し、benchmark-version / metric-bundle / bridge-class の脱落を beginner level で読めるようにしました。
  - `Two newer beginner stop lines` note-box を追加しました。
  - claim-family table に
    - `Living-human proxy bundle`
    - `Sequential same-subject / same-brain bridge`
    の2行を追加し、それぞれ `Human Proxy Composition Card` と `State-Continuity Bridge Card` へ接続しました。
  - `Representative primary-literature reasons` を拡張し、Johansen / Lucchetti / Hirschler / Dagum / Lu / Idziak / Benisty / Egger を追加しました。
  - next-step table と sidebar に同2ページへの導線を追加しました。
  - references に proxy-composition / bridge 系の一次文献を追記しました。

## 今回修正しないもの

- 哲学 / 法学 / personhood
  - ユーザー指示どおり対象外です。
- `issue.md`
  - ユーザー指示どおり確認していません。

## 外部依存で保留

- なし
  - 今回の変更は、このリポジトリ内の文書改稿、export、build、commit、push までで完結できます。

## 参考文献

1. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
3. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
4. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
5. Hirschler L, Runderkamp BA, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
6. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
7. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023.
   - https://doi.org/10.1016/j.crmeth.2023.100520
8. Idziak A, Inavalli VVGK, Bancelin S, Arizono M, Nagerl UV. The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. *eNeuro*. 2023.
   - https://doi.org/10.1523/ENEURO.0104-23.2023
9. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
   - https://doi.org/10.1038/s41593-019-0502-4
10. Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-023-01498-y
11. Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
