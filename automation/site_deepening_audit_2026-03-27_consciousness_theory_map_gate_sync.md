# Site Deepening Audit (2026-03-27, Consciousness Theory Map 4-Gate Synchronization)

## 対象

- 主対象: `wiki/consciousness-theory-map.md`

## 今回の選定理由

- `perspective.md` と `verification.md` では、意識 readout を `construct validity / perturbational validity / same-cohort calibration / incremental validity` の 4-gate で読む規律がすでに導入されていました。
- しかし `wiki/consciousness-theory-map.md` は 2026-03-15 時点のままで、理論名・PCI・criticality の役割分離まではできていても、`どの gate を通った結果なのか` がまだ曖昧でした。
- さらに、参考文献に DOI の取り違えが残っていました。これは単なる表記ゆれではなく、読者が一次文献へ遡れないため、検証可能性そのものを損ねます。
- 技術・自然科学だけで改善でき、かつ theory-side の入口ページとして波及効果が大きいため、今回の深掘り対象に選びました。

## 根拠付き批判

### 1. 理論名と readout の役割分離だけでは足りません

- 問題:
  - 旧ページは `IIT / GNWT / FEP = theory`, `PCI = benchmark`, `criticality = proxy` という分離まではできていました。
  - しかし `construct validity`, `perturbational validity`, `same-cohort calibration`, `incremental validity` が独立 gate であることを本文構造として固定していませんでした。
- 根拠:
  - [Cohen et al. (2024)](https://doi.org/10.1093/cercor/bhae415), [Fahrenfort et al. (2025)](https://doi.org/10.7554/eLife.102335), [Dellert et al. (2025)](https://doi.org/10.1016/j.cub.2025.10.026) は、construct validity を no-report と criterion placement で別監査すべきことを支持します。
  - [Casali et al. (2013)](https://doi.org/10.1126/scitranslmed.3006294), [Comolatti et al. (2019)](https://doi.org/10.1016/j.brs.2019.05.013), [Hernandez-Pavon et al. (2023)](https://doi.org/10.1016/j.brs.2023.02.009), [Gogulski et al. (2024)](https://doi.org/10.1093/cercor/bhae130), [Biabani et al. (2024)](https://doi.org/10.1162/imag_a_00349) は、PCI/TMS-EEG の読解に perturbation log と sensory-control disclosure が必要なことを示します。
  - [Maschke et al. (2024)](https://doi.org/10.1038/s42003-024-06613-8), [Casarotto et al. (2024)](https://doi.org/10.1111/ejn.16299), [Breyton et al. (2025)](https://doi.org/10.7554/eLife.98920) は、spontaneous 指標が promising でも same-cohort calibration を外せないことを示します。
  - [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1), [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は、multimodal panel が別の incremental-validity / deployability 問題であることを示します。
- 批判:
  - よって、理論・benchmark・proxy の 3 区分だけではまだ粗いです。
  - 同じ `awareness-related` という語でくくっても、どの gate を通った結果なのかが違えば claim ceiling は変わります。

### 2. 参考文献 DOI の取り違えは、内容以前に検証可能性を壊します

- 問題:
  - 旧ページでは Fahrenfort 論文の DOI が `10.1038/s41593-025-02009-x` とされていました。
  - しかし DOI content negotiation で確認すると、これは `Mapping human thalamocortical connectivity with electrical stimulation and recording` を指し、criterion placement 論文ではありません。
  - 同様に Casarotto 論文は `10.1093/brain/awae227` ではなく、正しくは `10.1111/ejn.16299` です。`10.1093/brain/awae227` は別論文 `Piezo2 voltage-block regulates mechanical pain sensitivity` を指します。
- 根拠:
  - DOI metadata 直照合で、
    - `10.7554/eLife.102335` → *Criterion placement threatens the construct validity of neural measures of consciousness*
    - `10.1111/ejn.16299` → *Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state*
    - `10.1093/brain/awae227` → 別論文
    であることを確認しました。
- 批判:
  - 入口ページで DOI がズレていると、本文の理路が正しくても読者は一次文献へ到達できません。
  - 科学ページでは、まず reference integrity を直す必要があります。

### 3. Deployability を theory/benchmark/proxy の外に出していませんでした

- 問題:
  - 旧ページには multimodal clinical panel が独立役割として入っていませんでした。
  - そのため、theory-side map なのに clinical bundle の議論が visibility の外に残り、`PCI` や `criticality` と deployability の混線が起こりやすい状態でした。
- 根拠:
  - [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1) と [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は、multimodal panel の価値が `behavior-only baseline 超過`, `cross-centre robustness`, `missing-modality slice` で決まることを示しています。
- 批判:
  - したがって、deployability は theory や benchmark の下位概念ではなく、独立 track として明示しなければなりません。

### 4. 表構造そのものにも読み手の誤解を誘う崩れがありました

- 問題:
  - 旧ファイルには `Treat it as a <td>...` のような壊れた HTML が残っていました。
- 批判:
  - これは科学的主張の誤りではありませんが、入口 wiki の可読性と信頼感を下げます。
  - 役割分離の表で構造が壊れているのは、このページの目的に対して悪手です。

## 今回実行した変更

- `wiki/consciousness-theory-map.md`
  - `last_updated` を `2026-03-27` に更新
  - page intro / highlights / known_points / unknown_points を 4-gate 読みに同期
  - 役割テーブルを `theory family / construct-validity control / perturbation benchmark / spontaneous proxy / deployability panel / auxiliary geometry` の 6 系統へ再編
  - `What the primary literature cuts apart` テーブルを新設し、construct / perturbation / calibration / deployability の各 gate を一次文献で区切り直し
  - `The 4 gates that change claim strength on this site` テーブルを追加
  - site rules を `perspective` / `verification` と整合する形へ改稿
  - Fahrenfort 論文の DOI を `10.7554/eLife.102335` へ修正
  - Casarotto 論文の DOI と書誌を `10.1111/ejn.16299`, *European Journal of Neuroscience* へ修正
  - Rohaut / Manasova / Dellert / Hernandez-Pavon / Gogulski / Biabani / Breyton を追加
  - 壊れていた HTML table row を正常化

## 今回の修正で止めた誤読

- `theory name + PCI + criticality を並べれば十分に整理できている`
- `no-report はそのまま consciousness readout の一種`
- `PCI-like value があれば perturbation 条件や sensory contamination を省略してよい`
- `resting-state complexity が PCI と関係するなら代替 benchmark と読める`
- `multimodal panel は theory/benchmark の拡張であり、deployability gate を独立させなくてよい`
- `間違った DOI でも文脈が合っていれば十分`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開 wiki 本文と監査メモの更新で完結しています。

## 参考文献

1. Ferrante O, et al. Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08888-1
2. Cohen MA, et al. Neural signatures of visual awareness independent of postperceptual processing. *Cerebral Cortex*. 2024.
   - https://doi.org/10.1093/cercor/bhae415
3. Fahrenfort JJ, et al. Criterion placement threatens the construct validity of neural measures of consciousness. *eLife*. 2025.
   - https://doi.org/10.7554/eLife.102335
4. Dellert T, et al. Neural correlates of consciousness in an auditory no-report fMRI study. *Current Biology*. 2025.
   - https://doi.org/10.1016/j.cub.2025.10.026
5. Casali AG, et al. A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*. 2013.
   - https://doi.org/10.1126/scitranslmed.3006294
6. Comolatti R, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. *Brain Stimulation*. 2019.
   - https://doi.org/10.1016/j.brs.2019.05.013
7. Hernandez-Pavon JC, et al. TMS combined with EEG: Recommendations and open issues for data collection and analysis. *Brain Stimulation*. 2023.
   - https://doi.org/10.1016/j.brs.2023.02.009
8. Gogulski J, et al. Reliability of the TMS-evoked potential in dorsolateral prefrontal cortex. *Cerebral Cortex*. 2024.
   - https://doi.org/10.1093/cercor/bhae130
9. Biabani M, et al. Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00349
10. Maschke C, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. *Communications Biology*. 2024.
   - https://doi.org/10.1038/s42003-024-06613-8
11. Casarotto S, et al. Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state. *European Journal of Neuroscience*. 2024.
   - https://doi.org/10.1111/ejn.16299
12. Breyton M, et al. Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms. *eLife*. 2025.
   - https://doi.org/10.7554/eLife.98920
13. Rohaut B, et al. Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. *Nature Medicine*. 2024.
   - https://doi.org/10.1038/s41591-024-03019-1
14. Manasova D, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026.
   - https://doi.org/10.1093/brain/awaf412
15. Yoon B, Miolane N, Osting B, Linderman SW. Tracking the topology of neural manifolds across populations. *PNAS*. 2024.
   - https://doi.org/10.1073/pnas.2402628121
16. The topological structure of population activity in mouse visual cortex encodes visual stimuli. *iScience*. 2024.
   - https://doi.org/10.1016/j.isci.2024.111613
