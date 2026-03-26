# Site Deepening Audit (2026-03-27, Human Ionic Quantity-Type Split)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`
- 副対象: `index.md`
- 副対象: `glossary.md`
- 派生同期: `summary_booklet.md`

## 今回の選定理由

- 現行サイトはすでに `ionic milieu / chloride homeostasis` を独立 family として扱い、human 側にも `sodium MRI / ionic proxy` を置いていました。
- しかし、その次の段階でまだ弱い点が残っていました。`human sodium MRI` がなお `macro ionic proxy` という一括語で読めてしまい、`tissue sodium concentration`, `SQ+TQF-derived ISMF / ISC / ISVF`, `normalized sodium density-weighted`, `mono-/bi-T2 separation`, `short-component fraction` がほぼ同じ inferential object であるかのように見える余地がありました。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、human observability ceiling を議論する際には、`human ionic route exists` だけでは不十分で、`その route がどの sodium quantity をどの compartment model で推定したのか` を固定しないと、`current chloride homeostasis` への overread が起きやすいからです。

## 根拠付き批判

### 1. Human sodium MRI は一つの ionic meter ではありません

- 問題:
  - 旧サイトは `human sodium MRI` を正しく coarse proxy として扱っていましたが、その内部の quantity-type split がまだ弱く、読者が `human sodium MRI = one macro ionic state meter` と誤読しうる状態でした。
- 根拠:
  - [Qian et al. (2012)](https://doi.org/10.1002/mrm.23225) は、healthy human brain における high-resolution 7 T sodium imaging を示しましたが、主 object は `tissue sodium mapping` です。
  - [Fleysher et al. (2013)](https://doi.org/10.1002/nbm.2813) は、combined SQ + TQF imaging から `ISMF`, `ISC`, `ISVF` を推定しました。つまり、同じ sodium MRI でも `TSC` とは別の quantity family です。
  - [Qian et al. (2025)](https://doi.org/10.1038/s41598-025-07800-1) は、multi-TE single-quantum sodium MRI により `mono-T2`, `bi-T2`, `total` を分離しました。これも別の signal decomposition route です。
- 批判:
  - したがって、`human sodium MRI` を一括語で扱うと quantity type が消えます。
  - `TSC`, `ISMF / ISC / ISVF`, `mono-/bi-T2 separated sodium` は同じ inferential object ではありません。

### 2. Human sodium route には compartment model と acquisition burden の違いがあります

- 問題:
  - 旧サイトは `macro ionic proxy` として ceiling を止めていましたが、なお `human sodium route` が一つの安定量として見える余地がありました。
- 根拠:
  - [Fleysher et al. (2013)](https://doi.org/10.1002/nbm.2813) は `TSC` と `ISMF` が `ISC` と `ISVF` の compound measures であり、組み合わせて変換する model-based route であることを示しました。
  - [Rodriguez et al. (2022)](https://doi.org/10.1038/s41598-022-18388-1) は、simultaneous `1H / 23Na` MRI における `normalized sodium density-weighted quantification` の repeatability を評価しました。つまり human row には `repeatability-qualified density-weighted route` という別の quantity / scaling family があります。
  - [Tsang et al. (2012)](https://doi.org/10.1002/mrm.23147) は、human brain TQF sodium imaging で limited SNR と single-quantum breakthrough / spatial smearing を明示しました。
- 批判:
  - したがって、`human sodium imaging exists` を `current ionic state can now be read generically in humans` に昇格させるのは不適切です。
  - 少なくとも `quantity type`, `compartment model`, `repeatability`, `acquisition burden` を disclosure 項目にしなければなりません。

### 3. Different sodium metrics can move differently in the same biological context

- 問題:
  - 旧サイトは `human sodium MRI` を coarse route としては正しく止めていましたが、`which sodium quantity moved` を十分に front door で固定していませんでした。
- 根拠:
  - [Azilinon et al. (2023)](https://doi.org/10.1002/hbm.26102) は epilepsy で `TSC` と short-component fraction `f` を併記し、`f` は epileptogenic zone でのみ上昇する一方、`TSC` は broader patient regions で上昇したことを示しました。
- 批判:
  - したがって、`a sodium metric changed` を `the ionic state changed in one generic way` と読むのは粗いです。
  - `TSC increase` と `short-component-fraction increase` は同じ claim family ではありません。

### 4. それでも human ionic route は chloride-state ground truth ではありません

- 問題:
  - quantity-type split を入れると、逆に `intracellular sodium` や `bi-T2 sodium` が直接 `chloride set point` に近いと誤読される危険があります。
- 根拠:
  - いずれの human route も `cell-specific chloride concentration`, `KCC2 / NKCC1 balance`, `local E_GABAA`, `perisynaptic K+ microdomain` を直接は与えていません。
  - これは [Glykys et al. (2014)](https://doi.org/10.1126/science.1245423) や [Heubl et al. (2017)](https://doi.org/10.1038/s41467-017-01749-0) が問題にしている mechanistic object と別です。
- 批判:
  - したがって、quantity split を入れた後でも safe reading は `quantity-defined macro ionic proxy family` に留まります。
  - `current chloride homeostasis is now measured` へは進めません。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - ionic highlight を `quantity-defined human sodium / ionic proxies` へ更新
  - `How to read current human ionic evidence` を `TSC / SQ+TQF-derived ISMF-ISC-ISVF / normalized sodium density-weighted / short-component fraction / mono-bi-T2 separation` の split 中心に改稿
  - ionic route-card addendum を `human ionic quantity type` 問題へ更新
  - route-card table に `Human quantity type / compartment model` 行を追加
  - human proxy summary を `quantity-defined macro-ionic proxy family` に更新
  - references に `Fleysher 2013`, `Rodriguez 2022`, `Azilinon 2023` を追加

- `verification.md`
  - page highlight の ionic rule を `human quantity type / compartment model` まで含む形へ更新
  - Observability Budget の human evidence row に sodium-MRI quantity disclosure rule を追加
  - maintenance-state budget の ionic row に `human quantity type / compartment model` を追加
  - ionic addendum を `TSC / ISMF-ISC-ISVF / density-weighted / short-component fraction / mono-bi-T2` の split へ改稿
  - references を追加

- `wbe_101.md`
  - page highlight の ionic bullet を quantity-defined family へ更新
  - human observability ladder の ionic row を `Human sodium MRI / ionic proxy family` として改稿
  - entry note を `human sodium MRI is not one meter` という形へ改稿
  - measurement-stack caution の ionic paragraph を quantity-defined split に同期
  - references を追加

- `index.md`
  - front-door の ionic highlight を `quantity-defined human sodium / ionic proxies` へ更新
  - landing note-box を `human sodium MRI is not one meter` という形へ改稿

- `glossary.md`
  - `Support-state proxy` に quantity-defined ionic-route examples を追加

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` による再生成対象にしました

## 今回の修正で止めた誤読

- `human sodium MRI = one generic ionic-state meter`
- `TSC, SQ+TQF-derived ISC/ISVF, short-component fraction, mono-/bi-T2 separation はほぼ同じ inferential object`
- `human sodium route exists = current chloride homeostasis is now generically visible`
- `intracellular-sodium-like route exists = local E_GABAA or transporter balance is near-directly visible`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文・監査メモ・要約同期で完結しています。

## 参考文献

1. Qian Y, Zhao T, Zheng H, Weimer J, Boada FE. High-resolution sodium imaging of human brain at 7 T. *Magnetic Resonance in Medicine*. 2012;68(1):227-233.
   - https://doi.org/10.1002/mrm.23225
2. Fleysher L, Oesingmann N, Brown R, Sodickson DK, Wiggins GC, Inglese M. Noninvasive quantification of intracellular sodium in human brain using ultrahigh-field MRI. *NMR in Biomedicine*. 2013;26(1):9-19.
   - https://doi.org/10.1002/nbm.2813
3. Tsang A, Stobbe RW, Beaulieu C. Triple-quantum-filtered sodium imaging of the human brain at 4.7 T. *Magnetic Resonance in Medicine*. 2012;67(6):1633-1643.
   - https://doi.org/10.1002/mrm.23147
4. Rodriguez GG, Yu Z, O'Donnell LF, Calderon L, Cloos MA, Madelin G. Repeatability of simultaneous 3D 1H MRF/23Na MRI in brain at 7 T. *Scientific Reports*. 2022;12:14156.
   - https://doi.org/10.1038/s41598-022-18388-1
5. Azilinon M, Makhalova J, Zaaraoui W, et al. Combining sodium MRI, proton MR spectroscopic imaging, and intracerebral EEG in epilepsy. *Human Brain Mapping*. 2023;44(2):825-840.
   - https://doi.org/10.1002/hbm.26102
6. Qian Y, Lin Y-C, Chen X, Ge Y, Lui YW, Boada FE. Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. *Scientific Reports*. 2025;15:27427.
   - https://doi.org/10.1038/s41598-025-07800-1
7. Glykys J, Dzhala V, Egawa K, et al. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014;343(6171):670-675.
   - https://doi.org/10.1126/science.1245423
8. Heubl M, Zhang J, Pressey JC, et al. GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. *Nature Communications*. 2017;8:1776.
   - https://doi.org/10.1038/s41467-017-01749-0
