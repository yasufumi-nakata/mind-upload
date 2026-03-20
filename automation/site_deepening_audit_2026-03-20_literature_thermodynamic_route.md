# Site Deepening Audit (2026-03-20, Literature Thermodynamic Route Split)

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `research_harvest_50.md`

## 今回の選定理由

- 2026-03-20 時点で、`index.md`、`faq.md`、`verification.md`、`wiki/thermodynamic-grounding-basics.md` 側では、熱力学・不可逆性の過大読みに対してかなり明確な route-card 規則が入っておりました。
- その一方で、文献入口である `mind_uploading_papers.md` と `research_harvest_50.md` は、なお `thermodynamic consistency` を比較的ひと塊で読ませる構造が残っておりました。
- これは技術・自然科学の観点で弱点です。理由は、文献入口で `thermodynamic result` を 1 本の進歩線として読むと、`coarse-grained lower bound`、`time-asymmetry classifier`、`visibility-graph irreversibility`、`model-based entropy flow`、`physiology-side oxygen-metabolism calibration` が再び同じ inferential weight を持つように誤読されるからです。

## 根拠付き批判

### 1. 文献入口は thermodynamic / irreversibility を 1 本の frontier として読みすぎていました

- 問題:
  - `mind_uploading_papers.md` の priority route と shortlist は、decode / source validation / effective connectivity / observability / maintenance-state をかなりうまく分けていました。
  - しかし thermodynamic / irreversibility だけは front door の route として独立しておらず、year-order や U10 本文の奥に沈んでいました。
- 根拠:
  - Lynn et al. (2021) は coarse-grained fMRI state transitions から entropy-production lower bound を推定しました。
  - de la Fuente et al. (2023) は ECoG に対する inversion decoding で temporal irreversibility を扱いました。
  - Nartallo-Kaluarachchi et al. (2025) は multilevel visibility-graph irreversibility を MEG へ適用しました。
  - Ishihara & Shimazaki (2025) は state-space kinetic Ising model による model-based entropy flow を spike ensembles から推定しました。
- 批判:
  - したがって、これらを 1 つの `thermodynamic evidence` として読むのは粗すぎます。
  - 文献入口でも route family を先に答える必要がありました。

### 2. `physical grounding` という見出しだけでは physiology-side grounding の不足を止め切れませんでした

- 問題:
  - 旧 `research_harvest_50.md` の U10 は、Landauer / NESS / EPR をまとめて置きつつ、主に review / book / arXiv で組まれていました。
  - その構造だと、brain-signal irreversibility がそのまま metabolic cost や dissipation の readout へ昇格する誤読を止めにくいです。
- 根拠:
  - Epp et al. (2025) は、significant な BOLD change が oxygen-metabolism change と逆向きになりうることを示しました。
  - つまり energetic language を使うなら、brain-signal irreversibility とは別に physiology-side grounding が必要です。
- 批判:
  - 文献入口で `thermodynamic consistency` を読む際にも、route family と physiology-side grounding を分けるべきでした。

### 3. coarse-graining と finite-data regime が、文献入口ではまだ軽く読めてしまっていました

- 問題:
  - 旧 U10 は、熱力学の theoretical importance 自体は示していましたが、estimate が coarse-graining や欠測逆遷移に敏感であることを front door で明示していませんでした。
- 根拠:
  - Teza & Stella (2020) は coarse graining が entropy production を保存しうる条件を示しました。
  - Cocconi et al. (2022) は entropy production の scaling が coarse-graining の仕方に依存することを示しました。
  - Baiesi et al. (2024) は missing backward transitions が entropy-production estimation を壊しうることを示し、lower-bound approach を提案しました。
- 批判:
  - したがって、`one number was reported` という事実だけで cross-paper comparison へ進むのは危険です。
  - 文献入口でも `state definition / coarse-graining / data regime` を route burden として前面化する必要がありました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - front matter の `known_points` / `page_highlights` に thermodynamic route-family split を追加しました。
  - `technical-fast-lane` の説明を 8 ルートから 9 ルートへ更新し、`thermodynamic / irreversibility route family` を追加しました。
  - 同 route に Lynn / de la Fuente / Nartallo-Kaluarachchi / Ishihara / Epp を配置し、`what can be said` と `what still must not be said` を明示しました。
  - `technical-shortlist-20260320` に `Thermodynamic route-family split` 行を追加しました。
  - `technical-evidence-classes` に `auxiliary thermodynamic / irreversibility route family` を追加しました。
  - note box と recommended views table に thermodynamic reading route を追加しました。
- `research_harvest_50.md`
  - front matter の `page_highlights` / `known_points` に U10 の route-family split を追加しました。
  - priority route の本文と U10 row を更新し、`signal route / coarse-graining / estimator family / physiology-side grounding` を verify-first にしました。
  - priority-route note box と paper-anchor note を thermodynamic route まで拡張しました。
  - U10 section に addendum note を追加し、旧構造の弱点を明示しました。
  - U10 の `What has some traction now` / `What still needs research` / `Major studies and route anchors` を、review-heavy なまとめから primary-literature-heavy な route-family summary へ改稿しました。

## 外部依存で保留

- なし
  - 今回の変更は、公開本文の更新と監査メモの記録で完結しております。

## 参考文献

1. Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021.
   - https://doi.org/10.1073/pnas.2109889118
2. de la Fuente LA, Zamberlan F, Bocaccio H, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. *Cerebral Cortex*. 2023.
   - https://doi.org/10.1093/cercor/bhac177
3. Nartallo-Kaluarachchi R, Bonetti L, Fernández-Rubio G, et al. Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. *PNAS*. 2025.
   - https://doi.org/10.1073/pnas.2408791122
4. Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66669-w
5. Epp SM, Castrillón G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
6. Teza G, Stella AL. Exact coarse graining preserves entropy production out of equilibrium. *Physical Review Letters*. 2020.
   - https://doi.org/10.1103/PhysRevLett.125.110601
7. Cocconi L, Salbreux G, Pruessner G. Scaling of entropy production under coarse graining in active disordered media. *Physical Review E*. 2022.
   - https://doi.org/10.1103/PhysRevE.105.L042601
8. Baiesi M, Nishiyama T, Falasco G. Effective estimation of entropy production with lacking data. *Communications Physics*. 2024.
   - https://doi.org/10.1038/s42005-024-01742-2
9. Bérut A, Arakelyan A, Petrosyan A, et al. Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*. 2012.
   - https://doi.org/10.1038/nature10872
10. Deco G, Perl YS, Gilson M, et al. The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. *Communications Biology*. 2022.
   - https://doi.org/10.1038/s42003-022-03505-7
