# Site Deepening Audit (2026-04-04, Perspective SV2A Route-Role Sync)

## 対象

- 主対象: `perspective.md`

## 今回の選定理由

- 2026-04-04 時点の公開サイトは、`index.md`、`wbe_101.md`、`verification.md` では `SV2A / synaptic-density PET` の過読防止がかなり進んでいました。
- しかし長文の技術ノート `perspective.md` では、`SV2A PET` を `regional synaptic-density proxy` と `presynaptic release-machinery ceiling` の間に置く説明はあっても、`family-internal comparison` と `evidence role` の分離が front door ほど明示的ではありませんでした。
- この差は技術・自然科学の観点で重要でございます。なぜなら、現行の一次文献は `SV2A PET がある` ことだけでは何も一意に言えず、少なくとも
  - tracer / quantification route
  - same-subject baseline / repeatability
  - healthy atlas / cohort prior
  - cross-sectional risk contrast
  - task / cognition association
  - within-subject activation-null boundary
  - 24 h intervention-response boundary
  を区別しない限り、`human synaptic observability` を不当に強く読んでしまうからです。

## 主要な批判点

### 1. `perspective.md` は SV2A family の内部役割をまだ十分に分割していませんでした

- 問題:
  - 既存本文は `regional synaptic-density PET atlas` を一つの human route として置いていました。
  - しかし、その中に混在する `quantification`, `repeatability`, `atlas`, `risk contrast`, `association`, `activation boundary`, `intervention boundary` が本文導線では十分に分離されていませんでした。
- 根拠:
  - Naganawa et al. (2021) は `18F-SynVesT-1` の first-in-human quantification route を与えました。
  - Finnema et al. (2018) は `11C-UCB-J` の route-local test-retest reliability を与えました。
  - Johansen et al. (2024) は 33 healthy participants に基づく calibrated atlas を与えました。
  - Snellman et al. (2024) は cognitively unimpaired APOE ε4 carriers における cross-sectional risk contrast を与えました。
  - Shatalina et al. (2024) は healthy adults で task switching / cognition association を与えました。
  - Smart et al. (2021) は visual activation で `K1` は上がっても `VT` / `BPND` は変わらない activation-null boundary を与えました。
  - Holmes et al. (2022) は ketamine 24 h 後でも全体として measurable overall SV2A increase を認めなかった intervention-response boundary を与えました。
- 批判:
  - したがって、`SV2A PET has advanced` を一つの reusable human row として扱うのは不正確でございます。
  - 強く言えるのは `どの route role が前進したか` までであり、`current synaptic state がかなり見えた` ではありません。

### 2. 既存ページでは `task association` と `momentary state readout` の境界がまだ弱く見えました

- 問題:
  - `Shatalina et al. (2024)` のような association study は、個人差レベルでの task switching relevance を示します。
  - しかし、それは `moment-to-moment synaptic change detection` や `current synaptic efficacy` の証拠ではありません。
- 根拠:
  - Shatalina et al. (2024) は 25 healthy adults で task switching activity / switch cost との関係を示しましたが、N-back では同じ形の関係を示していませんでした。
  - Smart et al. (2021) は 7 healthy volunteers において visual stimulation で `K1` は増加しても `VT` / `BPND` は不変と報告しました。
- 批判:
  - よって `SV2A signal correlates with some behavior` を `SV2A PET reads rapid synaptic state` と読むのは過大評価でございます。

### 3. 既存ページでは `intervention-response boundary` が `synaptic restoration readout` と読まれうる余地が残っていました

- 問題:
  - ketamine literature は読者に `symptom improvement -> synaptic restoration -> SV2A increase should be visible` という連想を生みやすいです。
  - しかし human PET では、その連想は imaging window と measured object に強く依存します。
- 根拠:
  - Holmes et al. (2022) は healthy controls 9 名、clinical participants 12 名で 24 h 後の imaging を行い、overall measurable SV2A increase を認めませんでした。
  - 著者自身も post-hoc exploratory finding は replication を要すると明記しています。
- 批判:
  - したがって、`intervention improved symptoms` を `whole-brain presynaptic-density increase was measured` と接続するのは、この時点では根拠不足でございます。

## 今回実行した変更

- `perspective.md`
  - `last_updated` を `2026-04-04` に更新
  - front matter の `note` に `SV2A route-role sync` を追加
  - `page_highlights` に `SV2A family-internal role split` を追加
  - `known_points` に `current human SV2A evidence is internally split` を追加
  - 本文に新しい note-box を追加し、SV2A family 内の `quantification / repeatability / atlas / risk contrast / association / activation-null / intervention-response` を明示
  - 本文に比較表を追加し、各 route role が直接何を制約し、何へは昇格できないかを列挙

## 変更後にこのページで防げる過読

- `SV2A PET が進んだ -> current synaptic efficacy がかなり見えた`
- `task association がある -> moment-to-moment synaptic state が読める`
- `visual activation で tracer delivery が変わった -> synaptic density も変わった`
- `ketamine で症状が改善した -> 24 h whole-brain SV2A increase が測れた`
- `healthy atlas / risk contrast / intervention study` を一つの interchangeable bundle role として扱う

## 外部依存で保留

- なし
  - 今回の作業は、このセッション内で `perspective.md` を改稿することで完結しております。

## 参考文献

1. Naganawa M, Li S, Nabulsi N, et al. First-in-Human Evaluation of 18F-SynVesT-1, a Radioligand for PET Imaging of Synaptic Vesicle Glycoprotein 2A. *Journal of Nuclear Medicine*. 2021.
   - https://doi.org/10.2967/jnumed.120.249144
2. Finnema SJ, Nabulsi NB, Eid T, et al. Imaging synaptic density in the living human brain. *Science Translational Medicine*. 2016.
   - https://doi.org/10.1126/scitranslmed.aaf6667
3. Finnema SJ, et al. Test-retest reproducibility of [11C]UCB-J PET imaging in healthy volunteers. *Journal of Cerebral Blood Flow & Metabolism*. 2018.
   - https://doi.org/10.1177/0271678X17724947
4. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
5. Snellman A, et al. SV2A PET shows hippocampal synaptic loss in cognitively unimpaired APOE ε4/ε4 homozygotes. *Alzheimer's & Dementia*. 2024.
   - https://doi.org/10.1002/alz.14327
6. Shatalina E, Onwordi EC, Whitehurst T, et al. The relationship between SV2A levels, neural activity, and cognitive function in healthy humans: A [11C]UCB-J PET and fMRI study. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00190
7. Smart K, Hillmer AT, Huang Y, et al. Binding of the synaptic vesicle radiotracer [11C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
8. Holmes SE, Finnema SJ, Naganawa M, et al. Imaging the effect of ketamine on synaptic density (SV2A) in the living brain. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-022-01465-2
9. Molnár G, Rózsa M, Baka J, et al. Human pyramidal to interneuron synapses are mediated by multi-vesicular release and multiple docked vesicles. *eLife*. 2016.
   - https://doi.org/10.7554/eLife.18167
10. Sakamoto H, Ariyoshi T, Kimpara N, et al. Synaptic weight set by Munc13-1 supramolecular assemblies. *Nature Neuroscience*. 2018.
   - https://doi.org/10.1038/s41593-017-0041-9
11. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-33565-6
12. Emperador-Melero J, Kaeser PS, et al. Distinct active-zone machineries organize CaV2 clustering and vesicle priming. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-024-01720-5
