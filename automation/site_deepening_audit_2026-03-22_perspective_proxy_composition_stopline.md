# Site Deepening Audit (2026-03-22, Perspective human-proxy composition stop line)

## 対象

- 主対象: `perspective.md`
- 参照整合先: `verification.md`, `wiki/human-proxy-composition.md`, `wiki/state-continuity-bridge.md`

## 今回の選定理由

- `index.md` と `wbe_101.md` では、living-human proxy rows を並べても自動的には state closure にならないことが、かなり明示的に止められていました。
- 一方で `perspective.md` は人間 in vivo 代理計測の層別化自体は進んでいたものの、`複数 row をどういう条件で bundle として昇格させるか` が `Verification` ほど明文化されていませんでした。
- その結果、長文研究ノートを真面目に読む読者ほど、`proxy-rich human evidence` を `almost state-complete` に寄せて読める余地が残っていました。

## 根拠付き批判

### 1. row の多さが latent-state closure に見えうる停止線がまだ弱かった

- 問題:
  - `perspective.md` は human proxy class と operational maturity を分けていました。
  - しかし `bundle promotion rule` が本文中に compact に見えていなかったため、`複数の強い human rows が同時に前進している` という事実が、`human whole-brain state is nearly measurable` という印象に変換されやすい構造でした。
- 批判:
  - これは概念不足ではなく比較不足です。ページ上で `何が違う quantity なのか`、`何が shared driver かもしれないのか`、`何を追加で示したら bundle 昇格が許されるのか` を短く固定する必要がありました。

### 2. 代表的 human rows は同じ inferential object を測っていません

- 根拠:
  - `Johansen et al. (2024)` は cohort-level regional synaptic-density atlas です。
  - `Lucchetti et al. (2025)` は five-metabolite parcel-similarity scaffold です。
  - `Li et al. (2025)` は dynamic kinetic glucose-rate imaging です。
  - `Hirschler et al. (2025)` は CSF mobility です。
  - `Dagum et al. (2026)` は overnight plasma biomarker changes を multicompartment model で解釈した efflux route です。
- 批判:
  - density, similarity, rate, mobility, efflux は同じ latent coordinate ではありません。
  - したがって、row を並べただけでは `same biological state axis` の検証になりません。

### 3. same-session multimodal agreement も composition 問題を自動解決しません

- 根拠:
  - `Vafaii et al. (2024)` は simultaneous Ca2+ / BOLD で common and divergent organization を示しました。
  - `Chen et al. (2025)` は simultaneous EEG-PET-MRI で coupled global progression と `two distinct network patterns` を示しました。
  - `Bolt et al. (2025)` は major global fMRI mode が autonomic physiology と強く結びつくことを示しました。
  - `Epp et al. (2025)` は有意な BOLD 変化と opposite oxygen-metabolism change が共存しうることを示しました。
- 批判:
  - つまり `rows move together` は `one solved latent variable` を意味しません。
  - same-session bundle でも `shared-driver audit` と `strongest single row を超える増分` の開示が必要です。

### 4. route existence と deployment-ready composition は別問題でした

- 根拠:
  - `Li et al. (2025)` は 7 T, dual-frequency coil, blood input を要する 5-participant route です。
  - `Baadsvik et al. (2024)` は 2 healthy volunteers に対する high-performance hardware 前提の proof-of-principle です。
  - `Hirschler et al. (2025)` は specialized 7 T CSF-mobility sequence です。
  - `Dagum et al. (2026)` は investigational device と model-based interpretation を含みます。
- 批判:
  - `a route exists` を `field-ready composable state meter exists` に読み替えるのは誤りです。
  - site-level research note でも operational maturity を bundle 昇格条件に含めるべきでした。

## 今回実行した変更

- `perspective.md`
  - front matter の `page_highlights` と `known_points` に human-proxy composition stop line を追加しました。
  - `wiki_links` に `Wiki: Human Proxy Composition and Route Maturity` を追加しました。
  - human evidence section に compact comparison table を追加し、
    - quantity-type collapse
    - operational-maturity collapse
    - common-driver / fusion collapse
    を別々に止めるようにしました。
  - `Human Proxy Composition Card` と `State-Continuity Bridge Card` を本文 stop rule として明示しました。

## 外部依存で保留

- same-subject, same-session, cross-stack, externally calibrated human proxy benchmark
  - 担当者: multimodal human benchmark 設計者
  - 前提条件: 同一被験者・同一摂動条件で `direct observable by row`, `shared-driver audit`, `increment over strongest single row` を比較できる公開 benchmark
  - 完了条件: living-human proxy bundle が rhetoric ではなく matched-condition incremental evidence として比較可能になること

## 参考文献

1. Johansen KK, et al. An in vivo human synaptic density atlas of cortical and subcortical gray matter. *J Neurosci*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Lucchetti F, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nat Commun*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
3. Li X, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
4. Baadsvik EL, et al. Myelin bilayer mapping in the human brain in vivo. *Magn Reson Med*. 2024.
   - https://doi.org/10.1002/mrm.29998
5. Hirschler L, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nat Neurosci*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
6. Dagum P, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nat Commun*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
7. Vafaii H, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nat Commun*. 2024.
   - https://doi.org/10.1038/s41467-023-44363-z
8. Chen JE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nat Commun*. 2025.
   - https://doi.org/10.1038/s41467-025-64414-x
9. Bolt T, et al. Autonomic physiological coupling of the global fMRI signal. *Nat Neurosci*. 2025.
   - https://doi.org/10.1038/s41593-025-01945-y
10. Epp S, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nat Neurosci*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
