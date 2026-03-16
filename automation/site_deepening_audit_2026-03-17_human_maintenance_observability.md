# Site Deepening Audit (2026-03-17, Human Maintenance-State Observability)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 既存サイトは、rodent 側の maintenance-state 因果文献をかなり厚く押さえていました。
- しかし `human で今どこまで直接見えているか` の整理は、Shapson-Coe / Lucchetti / Zrenner を挙げつつも、`何の層が見えているのか` をまだ十分に分解できていませんでした。
- このままでは、human 側のデータ増加を `state-complete へ近づいた` と誤読しやすい構造が残ります。技術・自然科学の観点では、ここが今もっとも更新価値の高い弱点でした。

## 主要な批判点

### 1. human observability の節が、異なる measurement class を 1 つの前進として畳み込みすぎていました

- 問題:
  - 旧版は human EM 断片、whole-brain MRSI、sleep 系の証拠、TMS-state gating を並べていましたが、それぞれが押し上げている観測層の違いが弱く、読者が `human でもかなり直接見えてきた` と誤読しうる構造でした。
  - しかし一次文献を並べると、Shapson-Coe は `fixed tissue の局所 ultrastructure`、Lucchetti は `parcel-level biochemical organization`、Baadsvik は `macro-myelin proxy`、Zrenner / Kuhn / Fehér / Huber は `perturbation-conditioned plasticity / excitability proxy` を押し上げており、同じ種類の direct measurement ではありません。
- 根拠:
  - Shapson-Coe et al. (2024) は nanoscale の human cortical fragment を再構成しましたが、固定済み断片の structural scaffold です。
  - Lucchetti et al. (2025) は whole-brain 1H-MRSI から metabolic connectome を構成しましたが、parcel-level の macro-biochemical organization です。
  - Baadsvik et al. (2024) は in vivo の myelin bilayer map を 1.4 mm 級で提示しましたが、single-axon conduction や oligodendroglial support は直接は与えません。
  - Huber et al. (2013)、Kuhn et al. (2016)、Fehér et al. (2026)、Zrenner et al. (2018) は、sleep / wake / nap や momentary excitability state が human plasticity readout を変えることを示しましたが、cell-specific controller の直読ではありません。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` の human observability 節を全面改稿し、`structural scaffold / macro-biochemical scaffold / macro-myelin proxy / perturbational proxy / local hidden state` に分解しました。

### 2. human myelin proxy が欠落していたため、timing / myelin state の human ceiling が見えにくかった

- 問題:
  - 旧版は髄鞘の重要性を rodent causal evidence で支えていましたが、human 側で `何が見え始めているか` が MRSI と EM に偏っていました。
  - そのため、読者が `human では myelin まわりはまだ何も見えていない` か、逆に `myelin も直接見えた` かの二極化した読み方をしやすい状態でした。
- 根拠:
  - Baadsvik et al. (2024) は myelin bilayer の in vivo mapping を示しましたが、これは macro な tissue map であり、activity-dependent myelination、single-axon delay、oligodendrocyte-axon metabolic support を直接返しません。
- 修正:
  - human observability table に `human myelin bilayer map` 行を追加し、`direct に見えた層` と `なお latent の層` を明文化しました。

### 3. sleep / TMS 系 human proxy が `maintenance-state の存在証拠` に留まり、何がまだ未観測かが弱かった

- 問題:
  - 旧版は sleep の重要性を示していましたが、human 側では `sleep が maintenance を担う` と `どの controller が見えたか` が混ざっていました。
  - これでは `human で sleep 依存性が示された = maintenance-state の担い手も実質同定できた` と誤読しやすくなります。
- 根拠:
  - Huber et al. (2013) は TMS-EEG 応答が time awake で上がり recovery sleep で下がることを示しました。
  - Kuhn et al. (2016) は sleep deprivation 後に human cortex の net synaptic strength 指標が増え、PAS 誘導 plasticity が低下することを示しました。
  - Fehér et al. (2026) は短い nap でも net synaptic strength proxy が下がり、LTP-like plasticity proxy が回復することを示しました。
  - Zrenner et al. (2018) は EEG-defined excitability state が TMS-induced plasticity efficacy を左右することを示しました。
- 修正:
  - human observability 節で、sleep-homeostasis / plasticity proxy と state-gated perturbation proxy を分離しました。
  - `どの cell type / synapse / glia / controller が変化を担ったか` はまだ latent と明記しました。

### 4. 入口ページが human 側の proxy class の違いを十分に見せていませんでした

- 問題:
  - `wbe_101.md` では human direct observability ceiling を押さえていましたが、EM、MRSI、myelin、TMS-state gating、nap plasticity を区別していなかったため、入口の段階で proxy の種類差が埋もれていました。
- 修正:
  - `wbe_101.md` の `human direct observability ceiling` 行と注記を更新し、`structure / macro-biochemical scaffold / myelin bilayer proxy / state-dependent plasticity proxy` を分けて記載しました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - front matter の highlights / known / unknown を human proxy class を意識した内容へ更新
  - `human maintenance-state の直接観測` 節を再構成
  - `human myelin bilayer map` と `human sleep-homeostasis / plasticity proxy` を追加
  - `human myelin bilayer map や nap / TMS proxy があれば cell-specific controller も見えた` という誤読を新規に降格ルールへ追加
  - 参考文献に Baadsvik (2024), Huber (2013), Kuhn (2016), Fehér (2026) を追加
- `wbe_101.md`
  - human direct observability ceiling の表現を更新
  - 入口用の注記に human proxy class の違いを反映

## 外部依存で保留

- human maintenance-state benchmark の整備
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: 同一被験者で MRSI、myelin proxy、TMS-EEG / PAS、sleep annotation を束ねた公開データ
  - 完了条件: `macro scaffold`、`macro proxy`、`perturbational proxy`、`local hidden state` を共通 schema で比較できる benchmark が site-wide に再利用できること

## 参考文献

- Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
  - https://doi.org/10.1126/science.adk4858
- Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
  - https://doi.org/10.1038/s41467-025-66124-w
- Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
  - https://doi.org/10.1002/mrm.29998
- Huber R, Mäki H, Rosanova M, Casarotto S, Canali P, Casali AG, Tononi G, Massimini M. Human cortical excitability increases with time awake. *Cerebral Cortex*. 2013;23(2):332-338.
  - https://doi.org/10.1093/cercor/bhs014
- Kuhn M, Wolf E, Maier JG, Mainberger F, Feige B, Schmid H, et al. Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. *Nature Communications*. 2016;7:12455.
  - https://doi.org/10.1038/ncomms12455
- Fehér KD, Henckaerts P, Hirsch V, Bucsenez U, Kuhn M, Maier JG, et al. A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. *NeuroImage*. 2026;327:121723.
  - https://doi.org/10.1016/j.neuroimage.2026.121723
- Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018;11(2):374-389.
  - https://doi.org/10.1016/j.brs.2017.11.016
