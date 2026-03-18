# Site Deepening Audit (2026-03-18, Ionic Milieu / Chloride Homeostasis Is Not Background Chemistry)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`activity-dependent transcription / chromatin`、`local proteostasis / synaptic tagging`、`ECM / PNN`、`timing-state`、`bioenergetics`、`glia / clearance` をかなり強く分解できていました。
- その一方で、`ionic milieu / chloride homeostasis` は独立の state class として固定されておらず、読者が `connectome + cell type + weights が揃えば inhibitory sign や state transition もほぼ決まる` と誤読しうる余地が残っていました。
- これは技術・自然科学の観点で重要です。なぜなら、同じ配線・同じ細胞型・同じ名目上のシナプスでも、`intracellular chloride set point`、`KCC2/NKCC1 state`、`extracellular K+ / Ca2+ / pH composition` が違えば、GABA の極性、発火しやすさ、睡眠覚醒状態、律動安定性、記憶関連可塑性の読みが変わりうるからです。

## 根拠付き批判

### 1. 旧 site は `intrinsic excitability` と `glia / metabolic support` を分けていた一方、`ionic milieu / chloride homeostasis` を独立 state にしていませんでした

- 問題:
  - 現行記述は、閾値・ゲイン・AIS・髄鞘・グリア・代謝をよく分けていました。
  - しかし、`local chloride set point` や `extracellular ion composition` が独立 state であることは前景化されていませんでした。
- 根拠:
  - Glykys et al. (2014) は、局所の impermeant anions が neuronal chloride concentration と GABA_A signaling polarity の set point を拘束することを示しました。
  - Heubl et al. (2017) は、GABA_A receptor-mediated inhibition が Cl-sensitive WNK1 kinase を介して KCC2 activity を急速に調整することを示しました。
- 批判:
  - したがって、`cell type + intrinsic excitability` だけで inhibitory sign や局所の chloride rule がかなり決まる、という読み方は強すぎました。
  - `ionic milieu / chloride homeostasis` は excitability の脚注でも glia の脚注でもなく、独立 state class として書くべきでした。

### 2. 旧 site は sleep / wake と maintenance-state を扱っていたが、`interstitial ion composition` を state-transition route として固定していませんでした

- 問題:
  - `sleep-dependent renormalization` は厚く扱われていました。
  - しかし、`sleep / wake state itself can shift when interstitial ions shift` という route は site-wide rule に入っていませんでした。
- 根拠:
  - Ding et al. (2016) は、interstitial K+, Ca2+, Mg2+, and H+ の組成変化が cortical activity と sleep-wake state を制御しうることを示しました。
- 批判:
  - これは、`sleep history` を時間ラベルだけで読むのでは不十分で、state-transition side に ionic milieu が残ることを意味します。
  - したがって、maintenance-state の議論から ionic route を抜いたままでは、state change の機序説明が 1 段欠けていました。

### 3. 旧 site は plasticity と memory stabilization を分けていたが、`chloride transporter state` の学習・記憶寄与を前景化していませんでした

- 問題:
  - 既存ページ群は proteostasis や ECM を通じて plasticity gate をよく整理していました。
  - しかし、KCC2-dependent な inhibitory regulation が memory / rhythmogenesis / spine plasticity に触れる層は独立説明されていませんでした。
- 根拠:
  - Simonnet et al. (2023) は、mouse dorsal hippocampus で KCC2 silencing が spatial/contextual memory を損ね、rhythmogenesis と hyperexcitability を変えることを示しました。
  - Nakamura et al. (2019) は、neuronal KCC2 overexpression が dendritic spine plasticity と motor learning を高めることを示しました。
- 批判:
  - したがって、chloride homeostasis は seizure/pathology の話に閉じず、memory-relevant plasticity route にも関与します。
  - ここを落とすと、`weight / transcription / ECM` までは書いたのに `inhibitory sign rule` を取り逃がす構図になります。

### 4. 旧 site は human observability ceiling で energetic / myelin / CSF proxies を分けていたが、`human ionic proxy` を位置づけていませんでした

- 問題:
  - human observability はかなり整理されていました。
  - しかし、ionic layer については `in vivo human whole-brain route exists only as coarse proxy` という line が本文で固定されていませんでした。
- 根拠:
  - Qian et al. (2012) は、healthy human brain における 7T sodium MRI を示しましたが、これは mm-class tissue sodium mapping です。
  - Huberfeld et al. (2007) は human temporal lobe epilepsy tissue で perturbed chloride homeostasis を示しましたが、これは病的組織における mechanistic evidence です。
- 批判:
  - したがって、human ionic evidence は `another biological layer exists` を支持しても、cell-specific chloride homeostasis や local E_GABA の ground truth ではありません。
  - site rule として、human ionic route は `macro ionic proxy` と書くべきでした。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `ionic milieu / chloride homeostasis` を front matter, summary, state table, human observability, dangerous misreadings, minimum submissions に追加
  - `10 maintenance-states` を `11 maintenance-states` に更新
  - 新節を追加し、chloride set point / interstitial ion composition / KCC2-dependent plasticity / human ionic proxy ceiling を一次文献つきで明文化
- `wiki/connectome-is-not-enough.md`
  - `9 state classes` を `10 state classes` に更新
  - state-class table と augmentation / ablation table に `ionic milieu / chloride homeostasis` を追加
  - site rules と minimum submissions を ionic state まで拡張
- `verification.md`
  - `remaining latent state`、`latent-state error budget`、`maintenance-state error budget`、`state variable integrity gate` に ionic state を追加
  - `ionic milieu is not background chemistry` addendum を新設
  - augmentation claim に `+ ionic milieu / chloride-homeostasis audit` を追加
- `wbe_101.md`
  - entry-level hidden-state explanation と table に ionic state を追加
  - page highlights / known points を更新し、connectome-complete の誤読を入口で止めるよう改稿

## 外部依存で保留

- なし
  - 今回の変更は、公開本文・検証ルール・監査メモの改稿で完結しています。

## 参考文献

1. Glykys J, Dzhala V, Egawa K, Balena T, Saponjian Y, Kuchibhotla KV, Bacskai BJ, Kahle KT, Zeuthen T, Staley KJ. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014;343(6171):670-675.
   - https://doi.org/10.1126/science.1245423
2. Heubl M, Zhang J, Pressey JC, Al Awabdh S, Renner M, Gomez-Castro F, Moutkine I, Eugène E, Russeau M, Kahle KT, Poncer JC, Lévi S. GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. *Nature Communications*. 2017;8:1776.
   - https://doi.org/10.1038/s41467-017-01749-0
3. Ding F, O'Donnell J, Xu Q, Kang N, Goldman N, Nedergaard M. Changes in the composition of brain interstitial ions control the sleep-wake cycle. *Science*. 2016;352(6285):550-555.
   - https://doi.org/10.1126/science.aad4821
4. Huberfeld G, Wittner L, Clemenceau S, Baulac M, Kaila K, Miles R, Rivera C. Perturbed chloride homeostasis and GABAergic signaling in human temporal lobe epilepsy. *Journal of Neuroscience*. 2007;27(37):9866-9873.
   - https://doi.org/10.1523/JNEUROSCI.2761-07.2007
5. Simonnet C, Sinha M, Goutierre M, Moutkine I, Daumas S, Poncer JC. Silencing KCC2 in mouse dorsal hippocampus compromises spatial and contextual memory. *Neuropsychopharmacology*. 2023;48(7):1067-1077.
   - https://doi.org/10.1038/s41386-022-01480-5
6. Nakamura K, Moorhouse AJ, Cheung DL, Eto K, Takeda I, Rozenbroek PW, Inada H, Housley GD, Wake H, Nabekura J. Overexpression of neuronal K+-Cl- co-transporter enhances dendritic spine plasticity and motor learning. *The Journal of Physiological Sciences*. 2019;69:453-463.
   - https://doi.org/10.1007/s12576-018-00654-5
7. Qian Y, Zhao T, Zheng H, Weimer J, Boada FE. High-resolution sodium imaging of human brain at 7 T. *Magnetic Resonance in Medicine*. 2012;68(1):227-233.
   - https://doi.org/10.1002/mrm.23225
