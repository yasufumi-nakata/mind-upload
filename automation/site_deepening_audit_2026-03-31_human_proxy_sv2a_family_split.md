# Site Deepening Audit (2026-03-31, human proxy SV2A family-internal split)

## 対象

- 主対象:
  - `wiki/human-proxy-composition.md`
- 同期対象:
  - `verification.md`
  - `wbe_101.md`
- 調査範囲:
  - 技術
  - 自然科学

## web確認対象

- `https://doi.org/10.2967/jnumed.120.249144`
- `https://doi.org/10.1523/JNEUROSCI.1750-23.2024`
- `https://doi.org/10.1002/alz.14327`
- `https://doi.org/10.1162/imag_a_00190`
- `https://doi.org/10.1177/0271678X20946198`
- `https://doi.org/10.1038/s41380-022-01465-2`

## 今回この箇所を選んだ理由

- site 全体ではすでに、human proxy を `family name = one solved row` と読ませない方向へ強く補正していました。
- しかし `wiki/human-proxy-composition.md` では、なお `SV2A PET` を bundle 内の一つの reusable row として読める余地が残っていました。
- この余地を残すと、
  - quantification route
  - healthy atlas / baseline
  - disease / risk contrast
  - task / cognition association
  - activation-null
  - intervention-response
  が同一の inferential object に圧縮され、`human synaptic-density evidence` が過剰に一般化されます。
- composition page は site 内の central rule なので、ここが粗いままだと front door 側で止めた誤読が再注入されます。

## 主要結論

- `SV2A PET` は一つの interchangeable bundle row ではございません。
- 少なくとも
  - `quantification route`
  - `healthy atlas / baseline`
  - `disease / risk contrast`
  - `task / cognition association`
  - `activation-null`
  - `intervention-response`
  を別の comparison family として扱う必要がございます。
- したがって human proxy bundle の審査では、`SV2A PET` という family label を書くだけでは不十分であり、family-internal comparison family を明記しなければなりません。

## 根拠付き批判

### 1. Quantification route は atlas でも disease contrast でもございません

- 根拠:
  - [Naganawa et al. (2021)](https://doi.org/10.2967/jnumed.120.249144) は、<sup>18</sup>F-SynVesT-1 の first-in-human 評価として、metabolite-corrected arterial input、1TC / 2TC 比較、reference-region 運用、安定 scan time を含む quantification route を詰めました。
- 批判:
  - これは tracer / kinetic-model / scan-window を固定するための quantification paper であり、healthy baseline atlas でも disease-linked contrast でもございません。
  - bundle composition で `SV2A PET` を一語で処理すると、この quantification burden が消えます。

### 2. Healthy atlas は risk contrast と同じ row ではございません

- 根拠:
  - [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024) は、33 healthy adults の in vivo human brain synaptic-density atlas を提示しました。
- 批判:
  - これは cohort-level baseline / atlas route であり、same-subject state tracking や disease-linked contrast の代用ではございません。
  - atlas を持っていることと、病態差や current-state change を読めることは別でございます。

### 3. Risk contrast は cognition meter でも rapid-state meter でもございません

- 根拠:
  - [Snellman et al. (2024)](https://doi.org/10.1002/alz.14327) は、cognitively unimpaired older adults において APOE ε4/ε4 群の hippocampal [<sup>11</sup>C]UCB-J SUVR が APOE ε3/ε3 群より低いことを示しました。
- 批判:
  - これは risk-stratified group contrast であり、healthy atlas の延長でも、task-linked cognition meter でも、momentary activity readout でもございません。
  - risk contrast の成立を、汎用的な human synaptic-state observability へ拡張するのは過読でございます。

### 4. Task / cognition association は activation truth を意味しません

- 根拠:
  - [Shatalina et al. (2024)](https://doi.org/10.1162/imag_a_00190) は、healthy adults における [<sup>11</sup>C]UCB-J と task switching / switch cost の関連を示しました。
- 批判:
  - これは selected task association であり、all-task generalization や universal cognition meter を意味しません。
  - `task-related association` を `current synaptic efficacy readout` に読み替えるのは不適切でございます。

### 5. Activation-null は時間分解能の ceiling を示します

- 根拠:
  - [Smart et al. (2021)](https://doi.org/10.1177/0271678X20946198) は、brief visual stimulation により tracer influx K<sub>1</sub> は増加しても binding は変化しなかったことを示しました。
- 批判:
  - これは `brief activation changed` と `SV2A binding changed` が自動で一致しないことを示す重要な null でございます。
  - よって `SV2A PET = momentary neural activity meter` という解釈は composition page 側でも明示的に止める必要がございました。

### 6. Intervention-response null は symptom improvement と同じではございません

- 根拠:
  - [Holmes et al. (2022)](https://doi.org/10.1038/s41380-022-01465-2) は、ketamine 後 24 時間で臨床症状の改善が見えても overall SV2A density の measurable change は示されなかったと報告しました。
- 批判:
  - intervention response と measurable synaptic restoration は別でございます。
  - したがって `SV2A PET` を一つの row と見なすと、intervention-response ceiling が見えなくなります。

### 7. composition page は family-internal split を bundle の入力条件として持つべきでした

- 根拠:
  - 上記 6 本は同じ tracer-family 名の下に置かれがちですが、比較対象、時間窓、cohort、解釈可能な latent variable が一致しておりません。
- 批判:
  - `human-proxy-composition` がこの split を持たない場合、bundle 審査そのものが粗くなります。
  - central rule page には、family label を読む前に comparison family を固定する規則が必要でございました。

## 今回実行した変更

- `wiki/human-proxy-composition.md`
  - front matter の `description` / `page_highlights` / `known_points` に、SV2A family-internal split を追加しました。
  - `What this page fixes` に、`SV2A PET` を generic synaptic-density row と読めてしまっていた問題を明記しました。
  - `2026-03-31 correction` note-box を追加し、Naganawa / Johansen / Snellman / Shatalina / Smart / Holmes を comparison family ごとに明示しました。
  - route matrix の `SV2A PET` 行を
    - quantification route
    - healthy atlas route
    - disease / risk-contrast route
    - task / activation / intervention route family
    の 4 行へ分解しました。
  - `Nine collapse errors to block` に `Family-internal route collapse` を追加しました。
  - `SV2A PET is not one reusable bundle row` note-box を追加し、family label の内部で stop line を引きました。
  - three-axes table の `SV2A PET` 行を `SV2A PET family` 行へ改稿し、family-internal typing を必須化しました。
  - references に `Snellman et al. (2024)` を追加しました。

- `verification.md`
  - Human Proxy Composition Card の説明に、`SV2A PET` を one reusable bundle row と見なさない third correction を追加しました。
  - `Proxy-row inventory and direct observables` 行に、family-internal comparison family の命名要件を追加しました。
  - `Human evidence class / observability ceiling` 行に、PET family 内の comparison family 開示要件を追加しました。

- `wbe_101.md`
  - `last_updated` を `2026-03-31` に更新しました。
  - synaptic-density PET note-box に `Snellman et al. (2024)` を追加し、risk-contrast route を明示しました。
  - `human-proxy-composition-rule` note-box に、SV2A family-internal split を beginner-facing に同期しました。
  - references に `Snellman et al. (2024)` を追加しました。

## 今回止めた誤読

- `SV2A PET` = one solved human synaptic-state row
- `healthy atlas` = disease / risk contrast
- `risk contrast` = cognition meter
- `task-linked association` = momentary neural activity truth
- `brief activation null` が存在しても generic activity meter と読める
- `intervention response` = measurable synaptic restoration

## 検証結果

- `git diff --check`
  - pass
- `bundle exec jekyll build`
  - pass

## 外部依存タスク

- なし
  - 今回の作業は文献確認、本文修正、監査メモ追加、build、commit、push までこのセッションで完結できます。

## 参考文献

1. Naganawa M, Li S, Nabulsi N, et al. First-in-Human Evaluation of <sup>18</sup>F-SynVesT-1, a Radioligand for PET Imaging of Synaptic Vesicle Glycoprotein 2A. *Journal of Nuclear Medicine*. 2021.
   - https://doi.org/10.2967/jnumed.120.249144
2. Johansen A, et al. In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Snellman A, Tuisku J, Koivumäki M, et al. SV2A PET shows hippocampal synaptic loss in cognitively unimpaired APOE ε4/ε4 homozygotes. *Alzheimer's & Dementia*. 2024.
   - https://doi.org/10.1002/alz.14327
4. Shatalina E, Onwordi EC, Whitehurst T, et al. The relationship between SV2A levels, neural activity, and cognitive function in healthy humans: A [<sup>11</sup>C]UCB-J PET and fMRI study. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00190
5. Smart K, Liu H, Matuskey D, et al. Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
6. Holmes SE, Finnema SJ, Naganawa M, et al. Imaging the effect of ketamine on synaptic density (SV2A) in the living brain. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-022-01465-2
