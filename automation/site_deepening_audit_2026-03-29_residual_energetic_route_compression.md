# Site Deepening Audit (2026-03-29, residual energetic-route compression)

## 対象

- 主対象:
  - `wbe_101.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wiki/connectome-is-not-enough.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- front door の bullet や table では human energetic routes の split がかなり進んでおりました。
- しかし長文本文にはなお
  - `human energetic imaging`
  - `macro energetic routes`
  - `31P-MRS ... and dynamic DMRSI`
  のような modality-family 単位の圧縮が残っておりました。
- この圧縮は wording の問題ではございません。`quantity type`、`spatial support`、`time axis`、`model burden` が違う route を再び一つの energetic row に戻してしまうため、site 全体の route-card 文化と矛盾いたします。

## web確認対象

- [Ren et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/27868234/)
- [Guo et al. (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11190064/)
- [Li et al. (2025)](https://pubmed.ncbi.nlm.nih.gov/40109558/)
- [Bøgh et al. (2024)](https://link.springer.com/article/10.1186/s41747-024-00426-4)

## 根拠付き批判

### 1. `31P` の human route だけでも既に複数の inferential object へ分かれております

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) は resting human brain の `ATP synthesis / phosphorus-metabolite concentration / pH balance` route でございます。
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) は `PCr→γ-ATP` と `Pi→γ-ATP` を `three band inversion modules` と `5-pool Bloch-McConnell-Solomon model` で推定する `MT exchange-flux` route でございます。
- [Guo et al. (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11190064/) は `entire human brain` の `intracellular NAD content` を 7 T `31P-MRSI` で whole-brain map として扱いました。
- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) は `functionally localized occipital voxel` における `task-evoked NAD+ dynamics` を扱う局所 functional route でございます。

批判:

- これらは同じ `31P route` ではございません。
- resting metabolite / pH balance、model-conditioned exchange flux、whole-brain NAD content、localized functional NAD dynamics は別 row でございます。
- したがって本文で `31P-MRS` と一括すると、site が front door で止めた quantity-type collapse を長文本文で再導入してしまいます。

### 2. deuterium 側も `absolute quantification` と `kinetic-rate imaging` は別物でございます

- [Li et al. (2025)](https://pubmed.ncbi.nlm.nih.gov/40109558/) は `0.7 cc nominal voxel`、`2.5 min/image`、whole-brain coverage、blood-input function、kinetic model に依存して `CMR_Glc`、`CMR_Lac`、`V_TCA`、`T_max` を推定しました。
- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は absolute deuterated-metabolite concentration と rate を dedicated quantification pipeline の下で扱う route でございます。

批判:

- 片方は `model-conditioned kinetic-rate term`、片方は `absolute deuterated-metabolite distribution / quantification` でございます。
- これを `dynamic DMRSI` や `deuterium imaging` でまとめると、absolute burden と rate term が混ざります。
- safe calibrator role も同じではございません。

### 3. route-local operating condition も object の一部でございます

- [Bøgh et al. (2024)](https://link.springer.com/article/10.1186/s41747-024-00426-4) は healthy volunteers 6 名の 3 T DMI repeatability を示しましたが、best repeatability は `120-min timepoint` の operating point に依存しておりました。
- Li 2025 の kinetic maps も blood-input function と explicit kinetic model を前提にしております。

批判:

- `repeatable deuterium route exists` は `all deuterium routes are portable and interchangeable` を意味しません。
- timepoint、blood input、quantification pipeline、kinetic model は route の外側ではなく route の一部でございます。

### 4. 本サイトで最も問題なのは、front door と long-form body の scientific granularity mismatch でございます

- `wbe_101.md` の bullet / table は既に route split をかなり導入しておりました。
- しかし same page の explanatory note には `energetic imaging` や `Ren 2015 and Li 2025` という再圧縮が残っておりました。
- `wiki/measurement-stack-and-claim-ceiling.md` でも central ladder paragraph に `Ren 2015 and Li 2025 pushed up macro energetic routes` が残っておりました。
- `wiki/connectome-is-not-enough.md` でも human energetic observability note が `Ren 2015 + Li 2025` だけで代表されておりました。

批判:

- このずれを放置すると、厳密な table を読んだ後でも本文 narrative で `same modality family = one energetic row` と誤読されます。
- したがって修正対象は front matter ではなく、長文 narrative の stop line であるべきでした。

## 今回実行した変更

- `wbe_101.md`
  - `Bioenergetic evidence now gets its own route card` を修正し、human energetic observability を
    - `31P metabolite / pH balance`
    - `31P MT exchange-flux`
    - `31P NAD-content mapping`
    - `localized functional 31P NAD-dynamics`
    - `deuterium metabolite-mapping / absolute-quantification`
    - `deuterium kinetic-rate imaging`
    に分解しました。
  - `Entry rule from this ladder` の `energetic imaging` を route-type list に置換しました。
  - `Do not confuse hidden state with the measurement stack` の energetic paragraph を route-type 単位に改稿しました。

- `wiki/measurement-stack-and-claim-ceiling.md`
  - central ladder paragraph の `macro energetic routes` を解消し、six route types を明示しました。
  - `Proxy class, operational maturity, and calibrator role` の note に `Ren et al. (2017)` を追加し、31P family 内の calibrator split を narrative 側でも可視化しました。

- `wiki/connectome-is-not-enough.md`
  - `Human observability ceiling for bioenergetic / mitochondrial state` を改稿し、`Ren 2015 + Li 2025` の旧圧縮を six-route taxonomy に置換しました。
  - `last_updated` を `2026-03-29` に更新しました。
  - 参考文献に `Ren 2017`, `Guo 2024`, `Kaiser 2026`, `Karkouri 2026` を追加しました。

## 今回止めた誤読

- `31P-MRS` = one energetic row
- `human energetic imaging` = one stable object
- `deuterium imaging` = absolute metabolite map = kinetic-rate map
- `macro energetic route` = branch-local mitochondrial or controller readout
- front-door table だけ厳密なら narrative body は粗くてもよい

## 外部依存タスク

- なし
  - 今回の変更は web での一次文献再確認、repo 内改稿、検証、commit、push までこのセッションで完結可能です。

## 参考文献

1. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26560
2. Guo R, Yang S, Wiesner HM, et al. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. *Frontiers in Neuroscience*. 2024.
   - https://doi.org/10.3389/fnins.2024.1389111
3. Kaiser A, Vind FA, Duarte JMN, et al. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
4. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
5. Karkouri J, Deelchand DK, Van de Moortele P-F, et al. Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
6. Bøgh N, Vaeggemose M, Schulte RF, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024.
   - https://doi.org/10.1186/s41747-024-00426-4
