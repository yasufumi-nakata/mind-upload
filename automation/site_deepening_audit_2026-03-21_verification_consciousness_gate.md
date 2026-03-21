# Site Deepening Audit (2026-03-21, Verification Consciousness Readout Gate and Reference Integrity)

## 対象

- 主対象: `verification.md`
- 整合同期: `perspective.md`

## 今回の選定理由

- `verification.md` はこのサイトの運用仕様ページであり、ここで gate 定義が粗いままだと、他ページで止めている過大解釈が再び通ってしまいます。
- とくに `consciousness-readout-gate` 節は、技術・自然科学の観点では重要であるにもかかわらず、2026-03-21 時点でも本文が粗く、一次文献への接続と reference integrity の両方に問題が残っていました。
- 今回は哲学・法学ではなく、あくまで `construct validity`、`perturbation reliability`、`same-cohort calibration`、`multimodal deployability` の 4 点を技術的に再監査するのが最も効果的だと判断しました。

## 根拠付き批判

### 1. `no-report` と `criterion placement` は同じ gate ではありません

- 問題:
  - 旧節は `no-report`, `PCI`, `resting-state`, `multimodal` という 4 ラベルを並べていましたが、何をもって gate を通過したとみなすかが粗く、`no-report を入れた = construct validity が通った` と読める余地がありました。
- 根拠:
  - Cohen et al. (2024) は、視覚 awareness の neural signature を post-perceptual processing から切り分けるには design 上の統制が必要であることを示しました。
  - Fahrenfort et al. (2025) は、response criterion の置き方自体が neural measure の construct validity を脅かすと論じています。
- 批判:
  - したがって `report confound を減らした` と `criterion placement を独立監査した` は別 deliverable でございます。
  - これを一つの曖昧な caution にまとめると、construct-validity gate が運用規則として機能しません。

### 2. PCI / TMS-EEG は target-specific reliability と sensory contamination を明示しない限り benchmark になりません

- 問題:
  - 旧節は PCI / TMS-EEG を main benchmark 候補として位置づけつつ、どの条件ログが最低限必要かが十分に具体化されていませんでした。
- 根拠:
  - Gogulski et al. (2024) は dlPFC TMS-EEG の early/local response reliability が target と analysis window に強く依存することを示し、medial target では高い一致度を得られる一方、anterior target では低い一致度に留まることを報告しました。
  - Biabani et al. (2024) は prefrontal / premotor / parietal stimulation 後の TEP に auditory / somatosensory input が寄与しうることを示しました。
- 批判:
  - 以上より、`PCI が出た` だけで state-level benchmark と読むのは不適切です。
  - stimulation site、intensity、control/sham、artifact window、analysis window、target-specific reliability を欠いた比較は、比較表面だけが整っていて中身が不均一な benchmark になってしまいます。

### 3. resting-state complexity は perturbation の代用品ではなく、same-cohort calibration が必要です

- 問題:
  - 旧節は spontaneous 指標を auxiliary として扱っていましたが、なぜ calibration gate が独立に必要なのかの論理が弱く、`perturbation なしでも consciousness meter に近づいた` と読める余地が残っていました。
- 根拠:
  - Breyton et al. (2025) は perturbation を使わずに spatiotemporal brain complexity から consciousness-related separation を試みました。
  - 一方で Casarotto et al. (2024) は minimally conscious state で spontaneous EEG features と PCI が解離しうることを示しました。
- 批判:
  - したがって spontaneous complexity は有望でも、PCI の単純代替ではありません。
  - 同一 cohort 内で PCI、behavior、clinical outcome、pipeline sensitivity と較正されて初めて、calibration gate を通過した補助 readout として扱うべきです。

### 4. multimodal panel は `one stronger meter` ではなく、bundle として incremental value を問うべきです

- 問題:
  - 旧節は multimodal panel を deployability の方向として扱っていましたが、`何に対してどれだけ上乗せしたか` が弱く、`multimodal = 自動的に ready` と読める余地が残っていました。
- 根拠:
  - Amiri et al. (2022) の CONNECT-ME study は ICU における residual consciousness prediction を multimodal に扱いました。
  - Rohaut et al. (2024) は clinically unresponsive critical-care patients with brain injury に対して multimodal assessment が neuroprognosis performance を改善しうることを示しました。
  - Manasova et al. (2026) は multicentre 条件で、diagnosis に効く modality と prognosis に効く modality が同一ではなく、modality 数の増加で性能が上がる一方で modality disagreement も残ることを示しました。
- 批判:
  - 以上は `single portable consciousness meter` の成立ではなく、`bundle-level incremental value` の実証でございます。
  - ゆえに behavior-only baseline、missing-modality slice、site transfer、calibration error、measurement burden を欠く限り、deployability claim は止めるべきです。

### 5. 参考文献の DOI 整合が壊れていました

- 問題:
  - 旧 `verification.md` / `perspective.md` では、少なくとも 2 本の DOI が別論文を指しておりました。
- 根拠:
  - Crossref の direct resolution では、`10.1016/j.brs.2024.06.001` は Gogulski 論文ではなく Zhao et al. の visual working memory 論文を返します。
  - 同様に `10.1212/WNL.0000000000209439` は Rohaut 論文ではなく Neurology の reader response を返します。
  - `10.1038/s41591-024-03019-1` は Kawai 論文ではなく、Rohaut et al. (2024) の *Nature Medicine* 論文です。
- 批判:
  - これは単なる書誌ゆれではなく、第三者検証を壊す重大な不整合です。
  - scientific criticism を支える最低条件は `本文の主張に対応する一次ソースへ確実に到達できること` ですので、今回の修正対象に含める必要がありました。

## 今回実行した変更

- `verification.md`
  - `consciousness-readout-gate` の導入文を全面的に改稿しました。
  - 4 gates の最低要件と stop claim を、construct validity / perturbation reliability / same-cohort calibration / incremental deployability に沿って具体化しました。
  - reference list を修正し、Gogulski の DOI を正しい一次ソースへ差し替え、Casarotto / Amiri / Manasova を追加し、Rohaut / Kawai の混線を解消しました。
- `perspective.md`
  - consciousness 節の関連 citations を同期しました。
  - `ref-124`, `ref-127`, `ref-128` を正しい書誌情報へ更新しました。
  - `last_updated` を `2026-03-21` に更新しました。

## 外部依存で保留

- 同一 cohort で `no-report`, `criterion placement`, `PCI/TMS-EEG`, `resting-state complexity`, `multimodal prediction` を同一 schema で比較できる公開 benchmark package
  - 担当者: 実験系 consciousness 研究者 / ICU・DoC 共同研究者 / benchmark maintainer
  - 前提条件: same-cohort multimodal acquisition、behavior-only baseline、missing-modality slices、site-transfer evaluation の公開
  - 完了条件: 4 gates を card-level に一括監査できる benchmark が公開されること

## 参考文献

1. Cohen MA, et al. (2024). Neural signatures of visual awareness independent of postperceptual processing. *Cerebral Cortex*.  
   https://doi.org/10.1093/cercor/bhae415
2. Fahrenfort JJ, et al. (2025). Criterion placement threatens the construct validity of neural measures of consciousness. *eLife*.  
   https://doi.org/10.7554/eLife.102335
3. Gogulski J, Cline CC, Ross JM, Parmigiani S, Keller CJ. (2024). Reliability of the TMS-evoked potential in dorsolateral prefrontal cortex. *Cerebral Cortex*.  
   https://doi.org/10.1093/cercor/bhae130
4. Biabani M, Perera T, Zalesky A, et al. (2024). Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex. *Imaging Neuroscience*.  
   https://doi.org/10.1162/imag_a_00349
5. Breyton M, Lado MJ, Laureys S, et al. (2025). Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms. *eLife*.  
   https://doi.org/10.7554/eLife.98920
6. Casarotto S, Hassan M, Rosanova M, et al. (2024). Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state. *European Journal of Neuroscience*.  
   https://doi.org/10.1111/ejn.16299
7. Amiri AM, Fisher D, Raimondo F, et al. (2022). Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*.  
   https://doi.org/10.1093/brain/awac335
8. Rohaut B, Calligaris M, Hermann B, Perez P, et al. (2024). Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. *Nature Medicine*.  
   https://doi.org/10.1038/s41591-024-03019-1
9. Manasova D, Belloli T, Rosenfelder M, et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*.  
   https://doi.org/10.1093/brain/awaf412
