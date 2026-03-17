# Site Deepening Audit (2026-03-18, Hemodynamic Vascular-State / CVR Ceiling)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `wiki/multimodal-integration-basics.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`
- 副対象: `index.md`

## 今回の選定理由

- 現在の公開サイトは、`fMRI/BOLD は hemodynamic proxy`、`multimodal != state-complete`、`alignment != mechanistic truth` という大枠までは既に書けていました。
- しかし、その書き方だけではまだ弱く、`hemodynamic modality では neural hidden state だけでなく vascular transfer state も別の誤差源である` ことが入口と submission rule に十分固定されていませんでした。
- この弱点は技術・自然科学の観点で優先度が高いです。なぜなら、group 差・縦断差・加齢差・multimodal fusion を raw BOLD / raw HbO/HbR 振幅からそのまま neural difference へ読み替える短絡を止めないと、measurement claim ceiling が崩れるからです。

## 根拠付き批判

### 1. 旧サイトは `BOLD は proxy` と言えていましたが、`vascular transfer state` を独立の submission-side limit として固定していませんでした

- 問題:
  - 旧 `Verification` と `Measurement Stack` 系ページでは、fMRI を hemodynamic proxy と呼んでいました。
  - しかし `baseline vascular state / cerebrovascular reactivity (CVR)` を、`remaining latent state` や `claim ceiling` における独立変数としてはまだ十分に前景化していませんでした。
- 根拠:
  - Murphy et al. (2011) は、inter-subject differences in local CBF / CBV が BOLD reactivity に寄与し、breath-hold 由来の vascular reactivity covariate を group analysis に入れると活性化領域が拡大することを示しました。
  - Williams et al. (2023) は、task BOLD magnitude が cortex の広い領域で hypercapnia-based CVR に強く対応することを示しました。
- 批判:
  - したがって `fMRI is a proxy` という一般論だけでは不十分です。
  - site rule としては、hemodynamic readout を読むときに `neural-side uncertainty` と `vascular-transfer-side uncertainty` を分けて監査しなければなりません。

### 2. 旧 site は group / longitudinal BOLD difference を止める gate がまだ弱かった

- 問題:
  - 現行の説明では、BOLD の group difference や cross-day difference を読む際の abstention condition が弱く、読者が `difference in BOLD amplitude = difference in neural state` と読みうる余地が残っていました。
- 根拠:
  - Wu et al. (2023) は、baseline CBF を考慮すると、adult lifespan にわたる multiple-demand network の BOLD response の一部は physiological confounding effects として切り分けられることを示しました。
  - Epp et al. (2025) は、significant task BOLD change を示す voxel の約 40% で oxygen metabolism change が逆向きになりうることを示しました。
- 批判:
  - したがって、BOLD amplitude difference をそのまま mechanistic neural difference に上げる仕様は甘いです。
  - `vascular-state / CVR calibration route` か `hemodynamic-limited difference` という abstention を公開仕様に入れる必要がありました。

### 3. 旧 multimodal 説明は synchronization / geometry を重視していましたが、hemodynamic side の calibration を gate にしていませんでした

- 問題:
  - `wiki/multimodal-integration-basics.md` では shared clock, geometry, artifact, invasive calibration を主に扱っていました。
  - しかし EEG+fMRI や EEG+fNIRS では、alignment が揃っても hemodynamic side に vascular ceiling が残る点が gate として書かれていませんでした。
- 根拠:
  - Murphy et al. (2011), Williams et al. (2023), Wu et al. (2023), Epp et al. (2025)。
  - Yucel et al. (2015) は、fNIRS で short-separation regression が autonomic/superficial confound を減らし、局在性と統計的有意性を改善することを示しました。
- 批判:
  - つまり `shared clock` と `co-registration` だけでは hemodynamic branch の解釈 ceiling は超えられません。
  - multimodal route には `hemodynamic transfer gate` を足す必要がありました。

## 今回実行した変更

- `index.md`
  - front matter に `BOLD / fNIRS amplitude != neural difference without vascular-state / CVR audit` を追加
  - 入口 note-box を追加し、hemodynamic misreading を最短導線で止めるように修正
- `verification.md`
  - page highlights / known points を更新
  - `Observability Budget` の `direct observables` と `remaining latent state` に hemodynamic-specific ceiling を追加
  - `vascular-state / CVR audit` addendum を新設
  - 最低運用ルールに `BOLD / fNIRS group difference without vascular audit is not accepted as neural difference` を追加
  - 参考文献を追加
- `tech_roadmap.md`
  - page highlights / known points を更新
  - M1 の fMRI row を `vascular transfer state / CVR` まで拡張
  - M1 note と M5 に hemodynamic calibration rule を追加
- `wiki/measurement-stack-and-claim-ceiling.md`
  - `last_updated` を `2026-03-18` に更新
  - hemodynamic ceiling を `fMRI / hemodynamic modalities` として改稿
  - `vascular transfer state` 節と fNIRS caution note を追加
  - site rules に `BOLD / fNIRS amplitude を neural difference に上げるな` を追加
  - 参考文献を追加
- `wiki/multimodal-integration-basics.md`
  - `last_updated` を `2026-03-18` に更新
  - `5 audit gates` を `6 audit gates` に更新
  - `Hemodynamic transfer gate` を追加
  - EEG+fMRI 節に vascular-state / CVR ceiling を追加
  - EEG+fNIRS に short-separation / superficial diagnostic rule を追加
  - 参考文献を追加

## 外部依存で保留

- なし
  - 今回の修正は、公開テキスト・claim ceiling・submission rule の改稿で完結しています。

## 参考文献

1. Murphy K, Harris AD, Wise RG. Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. *NeuroImage*. 2011;54(1):369-379.
   - https://doi.org/10.1016/j.neuroimage.2010.07.059
2. Williams RJ, Specht JL, Mazerolle EL, Lebel RM, MacDonald ME, Pike GB. Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. *Frontiers in Physiology*. 2023;14:1167148.
   - https://doi.org/10.3389/fphys.2023.1167148
3. Wu S, Tyler LK, Henson RNA, Rowe JB, Cam-CAN, Tsvetanov KA. Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. *Neurobiology of Aging*. 2023;121:1-14.
   - https://doi.org/10.1016/j.neurobiolaging.2022.09.006
4. Yucel MAY, Selb J, Aasted CMA, Petkov MP, Becerra L, Borsook D, Boas DA. Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. *Neurophotonics*. 2015;2(3):035005.
   - https://doi.org/10.1117/1.NPh.2.3.035005
5. Epp SM, Castrillon G, Yuan B, Andrews-Hanna J, Preibisch C, Riedl V. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
