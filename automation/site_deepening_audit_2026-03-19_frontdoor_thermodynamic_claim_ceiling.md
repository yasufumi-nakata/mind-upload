# Site Deepening Audit (2026-03-19, Front-Door Thermodynamic Claim Ceiling)

## 対象

- 主対象: `faq.md`
- 副対象: `index.md`
- 副対象: `wbe_101.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-19 時点で、`verification.md` と `wiki/thermodynamic-grounding-basics.md` には、thermodynamic / irreversibility claim を過大読解しないための route-card 規則がすでに整っておりました。
- しかし front door 側を見ると、その読解規則は十分に伝播しておらず、読者は依然として `entropy production` `arrow-of-time` `irreversibility` `EPR` を 1 個の強い測定量として読みやすい状態でした。
- これは技術・自然科学の観点で弱点です。connectome, hemodynamics, effective connectivity の過大読みを止めても、thermodynamic claim だけが入口で自由に強く読めるなら、WBE の claim ceiling が別の語で崩れます。

## 根拠付き批判

### 1. thermodynamic claim の読解規則が downstream に偏っていました

- 問題:
  - `verification.md` には `Irreversibility / Thermodynamic Route Card` があり、`wiki/thermodynamic-grounding-basics.md` にも estimator-family の分離がありました。
  - 一方で `faq.md` と `index.md` には、読者が最初に踏む短い説明としての thermodynamic guardrail が不足していました。
- 批判:
  - その結果、`arrow-of-time was detected` を `brain's physical cost was measured` や `WBE-relevant thermodynamic condition moved` と誤読する余地が残っていました。

### 2. 一次文献上、同じ thermodynamic 語でも measurement object が異なっていました

- 根拠:
  - Bérut et al. (2012) は bit erasure の Landauer lower bound を実験検証しました。
  - Attwell & Laughlin (2001) は rodent grey matter の signaling energy budget を整理しました。
  - Lynn et al. (2021) は coarse-grained BOLD state transition から entropy-production の lower bound を扱いました。
  - Deco et al. (2022) は time-shifted correlation asymmetry を用いました。
  - de la Fuente et al. (2023) は ECoG の temporal inversion を deep-learning classifier で識別しました。
  - Nartallo-Kaluarachchi et al. (2025) は directed visibility-graph degree distributions から multilevel irreversibility を評価しました。
  - Ishihara & Shimazaki (2025) は state-space kinetic Ising model の上で model-based entropy flow を推定しました。
- 批判:
  - したがって `thermodynamic result` は 1 個の共通通貨ではございません。
  - 同じ語で呼ばれていても、`bit-erasure lower bound` `tissue energy budget` `trajectory-irreversibility lower bound` `asymmetry score` `graph index` `model-based entropy flow` は異なる claim ceiling を持ちます。

### 3. cost isolation が front door で明文化されていませんでした

- 問題:
  - 既存本文には `cost isolation` が verification 層にはありましたが、入口では `thermodynamic` と `wall-power` や `brain energy cost` の混同を十分に止めていませんでした。
- 根拠:
  - Bérut et al. (2012) は whole-brain wall-power ではなく bit erasure の最低散逸を扱っています。
  - Attwell & Laughlin (2001) は biological tissue 側の descriptive budget であり、digital emulation の acceptance KPI ではありません。
  - Lynn et al. (2021), Deco et al. (2022), de la Fuente et al. (2023), Nartallo-Kaluarachchi et al. (2025), Ishihara & Shimazaki (2025) は neural data からの nonequilibrium 指標であり、hardware power の直接測定ではありません。
- 批判:
  - よって入口では、`signal-side irreversibility metric` と `implementation-side energy cost` を別物として固定する必要がありました。

## 今回実行した変更

- `faq.md`
  - front matter を `five technical guardrails` に更新しました。
  - front-door note を 5 つの guardrail に拡張し、thermodynamic overread を明示しました。
  - `Q1f` を新設し、entropy production / irreversibility / arrow-of-time をどう読むかを一次文献つきで追加しました。
  - 参考文献に Bérut (2012), Attwell & Laughlin (2001), Lynn (2021), Deco (2022), de la Fuente (2023), Nartallo-Kaluarachchi (2025), Ishihara & Shimazaki (2025) を追加しました。
- `index.md`
  - landing page の highlights / known points に thermodynamic claim ceiling を追加しました。
  - `If You Want To Read Thermodynamic Claims Without Promoting Them Too Early` の note-box を追加しました。
- `wbe_101.md`
  - front matter に thermodynamic papers の safe reading を追加しました。
  - definition 節に thermodynamic claims の補助的地位を明記する note-box を追加しました。
- `glossary.md`
  - `Thermodynamics and cost` セクションを追加し、Landauer lower bound, energy budget, NESS, irreversibility / EPR proxy, route card を定義しました。
  - thermodynamic words にも claim ceiling が必要であることを補足 note として追加しました。
  - 参考文献に thermodynamic / irreversibility 系一次文献を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開テキスト、読解規則、引用導線の修正で完結しております。

## 参考文献

1. Bérut A, Arakelyan A, Petrosyan A, et al. Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*. 2012.
   - https://doi.org/10.1038/nature10872
2. Attwell D, Laughlin SB. An energy budget for signaling in the grey matter of the brain. *Journal of Cerebral Blood Flow & Metabolism*. 2001.
   - https://doi.org/10.1097/00004647-200110000-00001
3. Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021.
   - https://doi.org/10.1073/pnas.2109889118
4. Deco G, Sanz Perl Y, Bocaccio H, Tagliazucchi E, Kringelbach ML. The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. *Communications Biology*. 2022.
   - https://doi.org/10.1038/s42003-022-03505-7
5. de la Fuente LA, Zamberlan F, Bocaccio H, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. *Cerebral Cortex*. 2023.
   - https://doi.org/10.1093/cercor/bhac177
6. Nartallo-Kaluarachchi R, Bonetti L, Fernández-Rubio G, et al. Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. *PNAS*. 2025.
   - https://doi.org/10.1073/pnas.2408791122
7. Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66669-w
