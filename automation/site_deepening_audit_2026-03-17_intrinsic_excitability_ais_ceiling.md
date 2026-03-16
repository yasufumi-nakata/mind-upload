# Site Deepening Audit (2026-03-17, Intrinsic Excitability / AIS / Recovery Ceiling)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`connectome-complete ≠ emulation-complete`、`same-day fit ≠ cross-day maintenance`、`cell type ≠ state-complete` をかなり明確に区別できていました。
- その一方で、`intrinsic excitability / homeostatic set point` はなお 1 本の行に寄りすぎており、読者が `threshold / gain / learning allocation / recovery controller` を同じ粒度の話として読んでしまう余地が残っていました。
- これは技術・自然科学の観点で優先度が高い弱点です。なぜなら、WBE や長期 BCI では `配線が同じ`、`cell type が同じ`、`その時点の excitability landscape が同じ`、`perturbation 後の戻り先が同じ` が似て見えても別主張だからです。

## 主要な批判点

### 1. 旧サイトは `intrinsic excitability` を 1 行に畳み込みすぎていました

- 問題:
  - 既存本文は `intrinsic excitability / homeostatic set point` が hidden state であること自体は正しく押さえていました。
  - しかし、`relative excitability による memory allocation`、`AIS geometry / channel distribution による gain 調整`、`recovery set point` が同じ evidence tier に見えていました。
- 根拠:
  - Yiu et al. (2014) は relative excitability が memory trace への recruitment を左右することを示しました。
  - Hadzibegovic et al. (2026) は early intrinsic excitability plasticity が memory formation と precision を規定することを示しました。
  - Grubb & Burrone (2010) は activity-dependent AIS relocation が excitability を fine-tune することを示しました。
  - Kuba et al. (2010) は presynaptic activity が AIS の Na+ channel distribution を変えることを示しました。
- 批判:
  - したがって、`intrinsic excitability` は 1 個の欠測欄ではなく、少なくとも `allocation`、`AIS / channel state`、`recovery controller` に分けるべきです。

### 2. 旧サイトは `同じ connectome / 同じ cell type` でも数時間から数日スパンの gain が動くことを、まだ十分前面化できていませんでした

- 問題:
  - connectome と cell type の限界は説明できていましたが、AIS plasticity の具体的な自然科学的根拠がまだ薄く、読者が `残る差は微調整程度` と誤読しうる余地がありました。
- 根拠:
  - Jamann et al. (2021) は sensory input に応じた rapid homeostatic AIS scaling を mouse barrel cortex で示しました。
  - Fréal et al. (2023) は sodium channel endocytosis が AIS plasticity を駆動することを示しました。
  - Benoit et al. (2025) は associative fear learning の間に AIS dynamics が変わることを示しました。
- 批判:
  - したがって、`同じ wiring / same graph` を `same spike-initiation rule` や `same learning readiness` に読み替えることはできません。

### 3. 旧サイトは human 側での excitability 証拠を `proxy だが causal` として十分整理できていませんでした

- 問題:
  - human で直接見えている層と latent の層の区別は既に強かった一方、human 側にも excitability state を因果 proxy として扱える文献があることが本文導線に十分入っていませんでした。
- 根拠:
  - Zrenner et al. (2018) は EEG-defined excitability states が TMS-induced plasticity efficacy を左右することを示しました。
- 批判:
  - ここから直接言えるのは `human でも excitability state は振る舞いを左右する` という点ですが、AIS geometry や channel distribution の direct readout ではありません。
  - よって `human proxy` と `direct local state` を同一視してはなりません。

### 4. Verification 側の監査ルールは `excitability landscape` と `recovery controller` の分離が不足していました

- 問題:
  - `verification.md` の latent-state error budget では、旧 row が `intrinsic excitability / homeostatic controller` をまとめて扱っていました。
- 批判:
  - これでは `same-day gain` と `cross-day recovery` が同じ欄に入り、どの claim を止める不足かが曖昧になります。
- 修正:
  - `intrinsic excitability landscape (gain / AIS / allocation state)` と `homeostatic controller / recovery set point` を分離し、棄権条件も分けました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `last_updated` を `2026-03-17` に更新
  - `AIS / ion-channel landscape` を metadata と冒頭要約へ反映
  - `intrinsic excitability は 1 行ではなく、AIS と ion-channel landscape に分かれます` 節を追加
  - human observability 表に `human perturbation-gated excitability proxy` 行を追加
  - dangerous misreadings と site rules に `AIS / channel state を latent として残す` 規則を追加
  - 参考文献へ Grubb (2010), Kuba (2010), Jamann (2021), Fréal (2023), Benoit (2025), Zrenner (2018) を追加
- `wbe_101.md`
  - `last_updated` を `2026-03-17` に更新
  - hidden state evidence table に `excitability landscape / AIS plasticity` 行を追加
  - `intrinsic excitability を 1 行に潰さない` note を追加
  - hidden-state 行の説明を `AIS geometry / channel distribution` まで拡張
  - 参考文献へ Grubb (2010), Kuba (2010), Jamann (2021), Yiu (2014), Benoit (2025) を追加
- `verification.md`
  - latent-state error budget の旧 row を `excitability landscape` と `recovery controller` に分割
  - `intrinsic excitability は 1 行では粗すぎます` note を追加
  - 参考文献へ Grubb (2010), Kuba (2010), Jamann (2021), Fréal (2023), Benoit (2025), Yiu (2014) を追加

## 外部依存で保留

- なし
  - 今回の修正は、公開本文と監査ルールの改稿で完結しています。

## 参考文献

1. Yiu AP, et al. Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. *Neuron*. 2014.
   - https://doi.org/10.1016/j.neuron.2014.07.017
2. Grubb MS, Burrone J. Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. *Nature*. 2010.
   - https://doi.org/10.1038/nature09160
3. Kuba H, Oichi Y, Ohmori H. Presynaptic activity regulates Na+ channel distribution at the axon initial segment. *Nature*. 2010.
   - https://doi.org/10.1038/nature09087
4. Jamann N, Dannehl D, Lehmann N, et al. Sensory input drives rapid homeostatic scaling of the axon initial segment in mouse barrel cortex. *Nature Communications*. 2021.
   - https://doi.org/10.1038/s41467-020-20232-x
5. Fréal A, Jamann N, Ten Bos J, et al. Sodium channel endocytosis drives axon initial segment plasticity. *Science Advances*. 2023.
   - https://doi.org/10.1126/sciadv.adf3885
6. Benoit CM, Ganea DA, Paricio-Montesinos R, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02152-5
7. Hadzibegovic N, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-025-66975-3
8. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimulation*. 2018.
   - https://doi.org/10.1016/j.brs.2017.11.016
