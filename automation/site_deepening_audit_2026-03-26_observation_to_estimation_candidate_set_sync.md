# Site Deepening Audit (2026-03-26, observation-to-estimation candidate-set sync)

## 対象

- 主対象: `wiki/observation-to-estimation.md`
- 同期対象: `wiki/measurement-and-modeling-terms.md`, `glossary.md`, `github-wiki-export/observation-to-estimation.md`, `github-wiki-export/measurement-and-modeling-terms.md`
- web確認対象:
  - `https://mind-upload.com/wiki/observation-to-estimation.html`
  - `https://mind-upload.com/wiki/measurement-and-modeling-terms.html`
  - `https://mind-upload.com/glossary.html`
- 調査範囲: 技術 / 自然科学のみ

## 今回このページを選んだ理由

- `wiki/observation-to-estimation.md` は site の中核であるにもかかわらず、更新日が `2026-03-20` のままで、直近に site-wide で前面化された
  - `Observability Budget`
  - `Fusion Card`
  - `State-Continuity Bridge Card`
  - `Connectome-Constrained Model Card`
  との接続が本文レベルで弱い状態でした。
- その結果、読者は依然として
  - `multimodal`
  - `same-brain`
  - `connectome-constrained`
  - `same-subject`
  を、別々の audit ではなく一本の「候補集合がかなり閉じた証拠」として読めてしまいます。
- これは自然科学的に弱いです。現在の一次文献が示しているのは、観測可能性の増加、bridge の成立、候補モデルの縮退、外的妥当性の獲得が別問題だということだからです。

## 主批判

### 1. 4つの監査ゲートでは不十分で、`observability budget` と `bridge / composition validity` が落ちていました

- [Villaverde (2019)](https://doi.org/10.1155/2019/8497093) は observability と structural identifiability が別問題であることを整理しました。
- [Villaverde et al. (2019)](https://doi.org/10.1098/rsif.2019.0043) は unknown inputs・states・parameters を同時に扱う必要を示しました。

批判:

- `geometry + uncertainty + candidate-model set + external validation` だけでは、そもそも何が直接観測され、どこから latent 化しているのかが page 入口で固定されません。
- さらに `same-session multimodal` や `same-brain sequential` のような bundle が出てきた時、bridge / composition 自体の妥当性を独立に監査できません。

### 2. `richer measurement` を `candidate-set closure` に読み替える停止線が弱いままでした

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は simultaneous multimodal recordings に共通成分と相違成分の両方が残ることを示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で tightly coupled temporal progression と distinct network patterns が共存することを示しました。
- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は connectome-constrained recurrent networks でも追加録音なしには動力学の縮退が残ることを示しました。
- [Liu et al. (2025)](https://doi.org/10.1016/j.csbj.2025.10.058) は practical identifiability が fitting method だけでなく data-collection policy に依存することを示しました。

批判:

- よって `同時計測になった`, `構造制約を入れた`, `stack を増やした` を、そのまま `候補集合がかなり閉じた` と読むのは不適切です。
- page 自体が `Fusion Card`, `Connectome-Constrained Model Card`, `Identifiability Card` に接続していないと、観測増加が uniqueness に短絡されます。

### 3. `same-brain / same-subject` を `same-state` に読み替える停止線がこのページでは弱いままでした

- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520) は preservation route が extracellular-space retention を変えることを示しました。
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) は dataset の major steps を sequential in vivo-to-postmortem workflow として明示しました。
- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) は 10-hour EEG dynamics が adaptive decoder を要請するほど変動することを示しました。

批判:

- したがって `same-brain` や `same-subject` の語だけでは one-state sample は保証されません。
- 観測→推定 wiki でも `State-Continuity Bridge Card` と `Temporal Validity Card` を明示しないと、sequence と drift の site-wide rule がここだけ弱くなります。

### 4. beginner route と glossary も site-wide rule とずれていました

- `wiki/measurement-and-modeling-terms.md` は modeling flow の初心者向け導線ですが、`more sensors / same-brain / connectome prior` を別監査として止める一文が不足していました。
- `glossary.md` は `Human observability ladder` をまだ `two axes` と説明しており、直近の `proxy class / operational maturity / calibrator role` 三軸ルールと不整合でした。

批判:

- 入口導線や用語定義が古いままだと、主ページだけ直しても読者は別ページで再び旧ルールに戻ります。

## 今回実行した変更

- `wiki/observation-to-estimation.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter に
    - `observability budget`
    - `fusion`
    - `bridge`
    - `connectome-constrained conditional model`
    の論点を反映
  - 本文の監査ゲートを `4段` から `6段` へ改稿
    - geometry
    - observability budget
    - uncertainty
    - candidate model set
    - bridge / composition validity
    - external validation
  - `Richer conditioning is not candidate-set closure` 節を新設
  - `same-session multimodal`
    `same-brain sequential bridge`
    `connectome-constrained prediction`
    を別々の audit として table 化
  - sidebar と front-matter link を `measurement-stack`, `multimodal integration`, `state-continuity bridge` へ同期
  - 参考文献に Vafaii 2024, Chen 2025, Lu 2023, MICrONS 2025, Egger 2024 を追加

- `wiki/measurement-and-modeling-terms.md`
  - `last_updated` を `2026-03-26` に更新
  - beginner route に `Fusion Card`, `State-Continuity Bridge Card`, `Identifiability Card` を足し、入口導線を同期

- `glossary.md`
  - `last_updated` を `2026-03-26` に更新
  - `Calibrator role` を新規定義
  - `Human observability ladder` を `two axes` から `three axes` に修正

## 今回の変更で止めた誤読

- `multimodal = one validated latent state`
- `same-brain = same-state evidence`
- `connectome-constrained = unique internal-state recovery`
- `more observables = identifiability solved`
- `human observability ladder = proxy class と maturity だけの二軸`

## 外部依存タスク

- なし。今回の修正はこのセッションで repo 内完結で実行可能でした。

## 参考文献

1. Villaverde AF. Observability and Structural Identifiability of Nonlinear Biological Systems. *Complexity*. 2019. https://doi.org/10.1155/2019/8497093
2. Villaverde AF, Tsiantis N, Banga JR. Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. *J R Soc Interface*. 2019. https://doi.org/10.1098/rsif.2019.0043
3. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nat Commun*. 2024. https://doi.org/10.1038/s41467-023-44363-z
4. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-64414-x
5. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023. https://doi.org/10.1016/j.crmeth.2023.100520
6. MICrONS Consortium, Bae JA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025. https://doi.org/10.1038/s41586-025-08790-w
7. Egger J, Kostoglou K, Müller-Putz GR. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Sci Rep*. 2024. https://doi.org/10.1038/s41598-024-70609-x
8. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-02080-4
9. Liu X, Wanika L, Chappell MJ, Branke J. Efficient data collection for establishing practical identifiability via active learning. *Comput Struct Biotechnol J*. 2025. https://doi.org/10.1016/j.csbj.2025.10.058
