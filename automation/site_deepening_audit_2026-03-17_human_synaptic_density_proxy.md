# Site Deepening Audit (2026-03-17, Human Synaptic-Density Proxy / SV2A PET Ceiling)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `faq.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`structural scaffold ≠ current synaptic state`、`connectome-complete ≠ emulation-complete`、`human proxy ≠ state-complete` をかなり明確に区別できていました。
- その一方で、human 側の synapse-related measurement class が本文導線ではなお粗く、`EM fragment` と `current synaptic efficacy` の間にある `SV2A PET / synaptic-density PET` が独立クラスとして前面化されていませんでした。
- この欠落は技術・自然科学の観点で重要でございます。なぜなら、いまの一次文献は human in vivo で `regional synaptic-density proxy` を押し上げていますが、それを明示しないと、読者が
  - `human では synapse はまだほとんど見えない`
  - `human では current synaptic state までかなり見えた`
  の両方向に誤読しうるからです。

## 主要な批判点

### 1. 旧 human observability 導線は、SV2A PET を measurement class として持っていませんでした

- 問題:
  - `wbe_101.md` と `faq.md` の human observability ceiling は、局所 ex vivo microcircuit、human EM fragment、MRSI、myelin bilayer、sleep/TMS proxy、CSF/glymphatic proxy を整理していました。
  - しかし、human in vivo の synapse-related route として現在最も実用的な `SV2A PET` が独立欄になっていませんでした。
- 根拠:
  - Finnema et al. (2016) は living human brain で SV2A PET による synaptic density imaging を前進させました。
  - Naganawa et al. (2021) は 18F-SynVesT-1 の first-in-human 評価で tracer route を拡張しました。
  - Johansen et al. (2024) は in vivo high-resolution human brain atlas of synaptic density を提示しました。
- 批判:
  - したがって、human observability の表に SV2A PET が無いままだと、`human synapse-related observability` の現在地が不必要に二値化されます。

### 2. 旧サイトは `synaptic density` と `current synaptic efficacy` の境界を、human in vivo 文脈で十分に固定していませんでした

- 問題:
  - サイト全体では current synaptic efficacy / release probability / receptor occupancy の区別を既に強く書いていました。
  - しかし human in vivo の measurement class 側から見ると、`SV2A PET が何を増やし、何をまだ与えないか` が明示されていませんでした。
- 根拠:
  - Finnema, Naganawa, Johansen が押し上げたのは `regional presynaptic vesicle density` の proxy です。
  - Shatalina et al. (2024) は SV2A level と neural activity / cognition の関係を示しましたが、これは関係の存在であって current efficacy との同一性ではありません。
  - Holler et al. (2021), Dürst et al. (2022), Matsuzaki et al. (2004), Vardalaki et al. (2022), Mittermaier et al. (2024) が示す通り、current synaptic state には release probability、postsynaptic receptor occupancy、state-gated consolidation が別に残ります。
- 批判:
  - したがって、SV2A PET を `human で synaptic state がかなり見えた` と読むのは過大でございます。
  - ここで比較的強く言えるのは `regional synaptic-density proxy` までであり、`current effective weight` や `momentary synaptic state` ではありません。

### 3. 旧 measurement-stack 表は、EM と same-brain connectomics の間にある human synaptic-density route を欠いていました

- 問題:
  - `wiki/measurement-stack-and-claim-ceiling.md` は stack ごとの ceiling を非常に強く整理していましたが、表の route に `SV2A PET / synaptic-density PET` がありませんでした。
  - そのため、human in vivo synapse-related route を measurement stack として参照しづらい構造でした。
- 修正方針:
  - stack table に `SV2A PET / synaptic-density PET` 行を追加し、`regional presynaptic-density proxy` と `current synaptic efficacy` を分離しました。
  - state-variable matrix の `current synaptic efficacy / plastic history` 行にも、`SV2A PET / synaptic-density atlas` を `proxy / bridge` として追加しました。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - `SV2A PET / synaptic-density PET` を独立 measurement stack として追加
  - `regional presynaptic-density proxy` と `current effective weight` を分離
  - 追補 note を追加し、human synaptic-density PET を structural scaffold と current state の中間層として明記
  - 参考文献へ Finnema (2016), Naganawa (2021), Johansen (2024), Shatalina (2024) を追加
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - human observability 説明に `SV2A PET` を追加
  - table に `human synaptic-density PET` 行を追加
  - `regional synaptic-density proxy` と `current synaptic efficacy / receptor occupancy` の差を本文で明文化
  - 参考文献を追加
- `wbe_101.md`
  - page highlight に `human SV2A PET` の ceiling を追加
  - `human direct observability ceiling` 行と explanatory paragraph を更新
  - `SV2A PET = human in vivo synaptic-density proxy` だが `current synaptic state` ではないことを明記
  - 参考文献を追加
- `faq.md`
  - `human observability ceiling` の短答に SV2A PET を追加
  - `presynaptic vesicle density proxy ≠ release probability / postsynaptic receptor occupancy` を短文で固定
  - 参考文献を追加

## 外部依存で保留

- なし
  - 今回の修正は、このリポジトリ内の公開本文改稿で完結しています。

## 参考文献

1. Finnema SJ, Nabulsi NB, Eid T, et al. Imaging synaptic density in the living human brain. *Science Translational Medicine*. 2016.
   - https://doi.org/10.1126/scitranslmed.aaf6667
2. Naganawa M, Nabulsi N, Lin S-F, et al. First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. *Journal of Nuclear Medicine*. 2021.
   - https://doi.org/10.2967/jnumed.120.249144
3. Johansen A, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
4. Shatalina E, et al. The relationship between SV2A levels, neural activity, and cognitive function in healthy humans. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00190
5. Holler S, et al. Structure and function of a neocortical synapse. *Nature*. 2021.
   - https://doi.org/10.1038/s41586-020-03134-2
6. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-33565-6
7. Matsuzaki M, Honkura N, Ellis-Davies GCR, Kasai H. Structural basis of long-term potentiation in single dendritic spines. *Nature*. 2004.
   - https://doi.org/10.1038/nature02617
8. Vardalaki D, Chung K, Harnett MT. Filopodia are a structural substrate for silent synapses in adult neocortex. *Nature*. 2022.
   - https://doi.org/10.1038/s41586-022-05483-6
9. Mittermaier V, Kononenko NL, Jin Y, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-024-53901-2
