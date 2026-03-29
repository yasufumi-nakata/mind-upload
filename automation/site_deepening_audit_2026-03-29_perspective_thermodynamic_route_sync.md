# Site Deepening Audit (2026-03-29, perspective / thermodynamic route-card sync)

## 対象

- 主対象: `perspective.md`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `perspective.md` は公開サイトの中でも、理論・計測・実装を一続きで読ませる中心ページです。
- ただし 2026-03-29 時点でも、このページの thermodynamics / causality 周辺には一段弱い点が残っていました。
  - `verification.md` と `wiki/thermodynamic-grounding-basics.md` では、thermodynamic claim に対して
    - signal route / state definition
    - coarse-graining / timescale
    - observed-state closure / memory order / reverse-transition support
    - estimator family / dynamical assumptions
    - physiology-side grounding
    - cost isolation
    を要求していました。
  - しかし `perspective.md` 側はなお
    - `EPR/irreversibility is auxiliary`
    - `main judgment uses perturbation / OOD / abstention`
    という抽象度で止まっており、<strong>どの thermodynamic quantity を、どの仮定で、どこまで読めるのか</strong> が front door で十分に固定されていませんでした。
- さらに proposal 58 / 61 / 62 の公開文面には、
  - logical cost
  - wall-plug / implementation cost
  - irreversibility / EPR
  - PCI / SCM
  が技術的には別物であるにもかかわらず、文として曖昧に混ざっている箇所がありました。
- これは技術的に危険でございます。WBE 文脈では、`non-equilibrium signature がある`、`因果介入 benchmark がある`、`計算量が大きい`、`消費電力がある` は同じ意味ではありません。この分離が甘いままですと、強い読者ほど「結局どこまでが thermodynamic evidence で、どこからが causal / engineering burden なのか」が読み取りにくくなります。

## web確認対象

- `https://doi.org/10.1073/pnas.2109889118`
- `https://doi.org/10.1093/cercor/bhac177`
- `https://doi.org/10.1038/s41467-025-66669-w`
- `https://doi.org/10.1073/pnas.2318333121`
- `https://doi.org/10.1038/s41593-025-02132-9`

## 根拠付き批判

### 1. 「irreversibility」という語だけでは、何を測ったのかが決まりません

- [Lynn et al. (2021)](https://doi.org/10.1073/pnas.2109889118) は、coarse-grained BOLD state transitions から entropy-production lower bounds を推定しました。
- [de la Fuente et al. (2023)](https://doi.org/10.1093/cercor/bhac177) は、ECoG の temporal irreversibility 読み取りが principal-component choice, feature set, model complexity に依存することを示しました。
- [Ishihara & Shimazaki (2025)](https://doi.org/10.1038/s41467-025-66669-w) は、spike train からの entropy flow 推定を state-space kinetic Ising model の下で行いました。

批判:

- 旧 `perspective.md` は `EPR/irreversibility is auxiliary` とは述べていましたが、読者がなお
  - lower bound
  - asymmetry score
  - model-based entropy flow
  を一続きの thermodynamic meter と誤読する余地がありました。
- これは一次文献の構造と整合しません。thermodynamic vocabulary が共通でも、inferential object は同じではございません。

### 2. coarse observation と hidden cycle / memory の問題を front door でも固定する必要がありました

- [Blom et al. (2024)](https://doi.org/10.1073/pnas.2318333121) は、coarse resolution で観測すると dissipative cycles が隠れ、観測系列が memory を帯び、単純な Markov reading では dissipation estimate が大きく過小評価されうることを示しました。

批判:

- verification/wiki 側ではすでに `observed-state closure / memory order / reverse-transition support` を route-card 項目として固定していた一方、旧 `perspective.md` の front-door 文面ではこの stop rule が見えにくいままでした。
- そのままでは、読者が `irreversibility paper がある = non-equilibrium readout はかなり確立した` と読みやすくなります。

### 3. energetic language は physiology-side grounding がなければ上げられません

- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は、有意な task BOLD 変化のうち約 40% の voxels で oxygen metabolism change が逆向きになりうることを示しました。

批判:

- したがって、observation-side irreversibility や BOLD-based asymmetry を、そのまま physical dissipation / metabolic cost に昇格させるのは不正確でございます。
- 旧 `perspective.md` は direction としては慎重でしたが、`physiology-side grounding` を front-door で明示していなかったため、`thermodynamic` と `energetic` の読み替え停止線がまだ弱い状態でした。

### 4. proposal 58 / 61 / 62 の公開文面は、技術的に別の objects を同列に見せていました

批判:

- `logical complexity`, `wall-plug power`, `PCI`, `SCM`, `irreversibility`, `EPR` は、評価対象も failure mode も異なります。
- ところが旧 proposal 58 / 61 / 62 では、これらが broken English を含む曖昧な文章で近接し、`全部まとめて validity の話` に見えやすくなっていました。
- 公開ページでこの混線を残すと、厳密化された verification/wiki 側の route-card culture が perspective では薄まります。

## 今回実行した変更

- `perspective.md`
  - front matter の `note` を更新し、2026-03-29 の thermodynamic-route sync を明記しました。
  - `page_highlights` に、thermodynamic / irreversibility claim も explicit route card の下で読むことを追加しました。
  - `known_points` に、irreversibility label, wall-plug power, computational complexity は別 object であることを追加しました。
  - `Thermodynamic readout wall` 行を改稿し、
    - de la Fuente の年表記を 2023 に修正し、
    - Lynn / de la Fuente / Ishihara / Blom / Epp に基づいて
    - quantity type, closure / memory, physiology grounding, cost isolation
    を front-door で見えるようにしました。
  - `2026-03-29 addendum: thermodynamic labels still need state-definition, closure, and energy-grounding audits` を追加しました。
  - proposal 58 / 61 / 62 を全面改稿し、
    - irreversibility log
    - energy / wall-plug cost
    - causal benchmark
    - theory-related computational burden
    を分離して記述しました。

## 今回止めた誤読

- `irreversibility result = one common thermodynamic meter`
- `coarse-grained non-equilibrium signature = microscopic dissipation`
- `BOLD-side asymmetry / irreversibility = energetic grounding`
- `PCI / SCM / EPR / implementation cost are one validity bundle`
- `thermodynamic language appeared = route-card burden is already met`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開文書改稿、監査メモ、生成物更新、検証、commit、push までこのセッションで完結可能です。

## 参考文献

1. Lynn CW, Cornblath EJ, Papadopoulos L, et al. (2021). Broken detailed balance and entropy production in the human brain. *PNAS*, 118(47), e2109889118.
   - https://doi.org/10.1073/pnas.2109889118
2. de la Fuente LA, Perl YS, Zamberlan F, et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. *Cerebral Cortex*, 33(7), 3798-3813.
   - https://doi.org/10.1093/cercor/bhac177
3. Ishihara K, Shimazaki H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*, 16, 10852.
   - https://doi.org/10.1038/s41467-025-66669-w
4. Blom K, Song K, Vouga E, Godec A, Makarov DE. (2024). Milestoning estimators of dissipation in systems observed at a coarse resolution. *PNAS*, 121(18), e2318333121.
   - https://doi.org/10.1073/pnas.2318333121
5. Epp SM, Castrillón G, Yuan B, et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*.
   - https://doi.org/10.1038/s41593-025-02132-9
