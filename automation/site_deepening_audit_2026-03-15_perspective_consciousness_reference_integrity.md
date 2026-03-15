# Site Deepening Audit (2026-03-15, Perspective / Consciousness Metrics Reference Integrity and Construct Validity)

## 対象

- 主対象: `perspective.md`
- 副対象: `automation/site_deepening_audit_2026-03-14_perspective_consciousness_markers.md`

## 今回の選定理由

- `tech_roadmap.md` 側の consciousness metrics は 2026-03-15 時点でかなり整理されていましたが、`perspective.md` の `EEGで意識を測る` 節にはまだ 2 種類の弱点が残っていました。
- 第1に、参考文献 103-105 の DOI / 書誌情報が実際の一次文献と一致していませんでした。これは単なる表記ゆれではなく、第三者が根拠をたどれないため、検証可能性そのものを壊します。
- 第2に、本文は no-report を confound control と位置づけ直していた一方で、2025年の criterion placement 論文が示した `construct validity` の問題をまだ前面化できていませんでした。
- したがって今回は、`内容の厳密化` と `参考文献の整合性回復` を同時に行うのが最も効くと判断しました。

## 確認方法

- DOI content negotiation と Crossref metadata で、`perspective.md` の 103-105 番参照先が実在の一次文献タイトルと一致するかを照合しました。
- その後、Current Biology、European Journal of Neuroscience、Brain、eLife、Nature の一次文献メタデータを基準に、本文の主張強度と参考文献の対応を見直しました。

## 主要な批判点

### 1. 参考文献 103-105 の誤同定は、本文以前に検証可能性を損ねていました

- 問題:
  - 旧 `perspective.md` の ref-103 は `10.1016/j.cub.2025.03.031` を `Neural correlates of auditory awareness under no-report conditions` として参照していましたが、この DOI はその論文ではありませんでした。
  - ref-104 の `10.1093/brain/awaf332` と ref-105 の `10.1093/brain/awaf287` も、本文で述べている consciousness / DoC 論文とは一致しませんでした。
- なぜ重大か:
  - この節は site-wide の立場表明として何度も参照される箇所です。ここで DOI がずれていると、読者は `どの論文が本当に根拠なのか` を確認できません。
  - 科学ページでは、主張の強さ以前に `参照先が追えること` が最低条件です。
- 修正:
  - ref-103 を Dellert et al. (2025) `Neural correlates of consciousness in an auditory no-report fMRI study` へ差し替えました。
  - ref-104 を Casarotto et al. (2024) `Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state` へ差し替えました。
  - ref-105 を Manasova et al. (2026) `Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness` へ差し替えました。

### 2. no-report を書くだけでは足りず、criterion placement を別監査にしないと construct validity が崩れます

- 問題:
  - 旧版は `no-report = confound control` までは書けていましたが、response criterion の揺れが neural marker の解釈を壊す点を独立した条件として固定していませんでした。
- 根拠:
  - Fahrenfort et al. (2025) は、criterion placement の違いだけで conscious content marker の construct validity が脅かされることを示しました。
  - したがって、`報告させない` だけでは不十分で、`どういう基準で yes/no を置かせたか` も別ログで残す必要があります。
- 修正:
  - `この節で先に固定する4条件` を `5条件` に拡張し、criterion placement を独立条件として追加しました。
  - site rule も `no-report / criterion placement = confound control` へ更新しました。

### 3. auditory no-report の証拠は、EEG benchmark の根拠ではなく confound-control の根拠です

- 問題:
  - 旧版は auditory no-report の論文を、読者によっては `EEGで意識を測る` 主張の直接根拠のように読める構造でした。
- 根拠:
  - Dellert et al. (2025) の論文は auditory no-report **fMRI** study です。
  - この論文が支持するのは、auditory domain でも no-report 設計が post-perceptual confound を切り分ける、という点であって、EEG 単独の bedside deployability ではありません。
- 修正:
  - `construct validity を別監査にします` という note-box を追加し、modality をまたぐ no-report evidence は `confound control の根拠としてのみ使う` と明記しました。

### 4. multimodal validation の中身を具体化しないと、「multimodal」という言葉だけが独り歩きします

- 問題:
  - 旧版の `multimodal clinical panel` 行は概ね正しい方向でしたが、どの modality が何に効いているのかが曖昧でした。
- 根拠:
  - Manasova et al. (2026) は、DoC の診断 / 予後を multimodal・multisite で評価し、単一指標ではなく行動評価、HD-EEG、MRI、PET、臨床変数の束として読む必要を強めました。
- 修正:
  - 表現を `行動評価・HD-EEG・MRI・PET・臨床変数を束ねた multisite panel` へ変更し、multimodal を具体化しました。

## 今回実行した変更

- `perspective.md`
  - `EEGで意識を測る` 節の冒頭文を、`no-report + criterion placement + resting-state calibration + multisite validation` が読める形へ更新
  - site rule を `no-report / criterion placement = confound control` へ更新
  - `construct validity を別監査にします` の note-box を追加
  - `この節で先に固定する4条件` を `5条件` へ更新
  - phase 0 / ToDo に criterion placement 監査を追加
  - phase 2 の spontaneous-vs-evoked 解離文献を Casarotto et al. (2024) へ訂正
  - multimodal panel と concluding paragraph の文献を Manasova et al. (2026) へ訂正
  - ref-103 / ref-104 / ref-105 を一次文献メタデータに合わせて修正
  - ref-113 として Fahrenfort et al. (2025) を追加
- `automation/site_deepening_audit_2026-03-14_perspective_consciousness_markers.md`
  - 監査メモ内の誤った書誌情報を訂正

## 外部依存で保留

- 同一 cohort での no-report / criterion placement / perturbation / multimodal validation の公開ベンチ実装
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: 課題実装、臨床協力、TMS-EEG ないし代替 perturbation、行動評価との同時計測
  - 完了条件: no-report 条件、criterion placement、PCI 系指標、outcome 予測を同一 schema で比較できる公開ログがそろうこと

## 参考文献

- Ferrante O, et al. Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08888-1
- Tsuchiya N, et al. No-Report Paradigms: Extracting the True Neural Correlates of Consciousness. *Trends Cogn Sci*. 2015.
  - https://doi.org/10.1016/j.tics.2015.10.002
- Cohen MA, et al. Neural signatures of visual awareness independent of postperceptual processing. *Cereb Cortex*. 2024.
  - https://doi.org/10.1093/cercor/bhae415
- Dellert T, et al. Neural correlates of consciousness in an auditory no-report fMRI study. *Curr Biol*. 2025.
  - https://doi.org/10.1016/j.cub.2025.10.026
- Fahrenfort JJ, et al. Criterion placement threatens the construct validity of neural measures of consciousness. *eLife*. 2025.
  - https://doi.org/10.7554/eLife.102335
- Casali AG, et al. A theoretically based index of consciousness independent of sensory processing and behavior. *Sci Transl Med*. 2013.
  - https://doi.org/10.1126/scitranslmed.3006294
- Comolatti R, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. *Brain Stimul*. 2019.
  - https://doi.org/10.1016/j.brs.2019.05.013
- Hernandez-Pavon JC, et al. TMS combined with EEG: Recommendations and open issues. *Brain Stimul*. 2023.
  - https://doi.org/10.1016/j.brs.2023.02.009
- Maschke C, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. *Commun Biol*. 2024.
  - https://doi.org/10.1038/s42003-024-06613-8
- Casarotto S, et al. Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state. *Eur J Neurosci*. 2024.
  - https://doi.org/10.1111/ejn.16299
- Manasova D, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026.
  - https://doi.org/10.1093/brain/awaf412
