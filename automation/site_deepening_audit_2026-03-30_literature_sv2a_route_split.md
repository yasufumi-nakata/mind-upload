# Site Deepening Audit (2026-03-30, literature front door SV2A route split)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 調査範囲:
  - 技術
  - 自然科学

## web確認対象

- `https://doi.org/10.1007/s00259-024-06885-6`
- `https://doi.org/10.1523/JNEUROSCI.1750-23.2024`
- `https://doi.org/10.1038/s41380-024-02776-2`
- `https://doi.org/10.1162/imag_a_00190`
- `https://doi.org/10.1177/0271678X20946198`
- `https://doi.org/10.1038/s41380-022-01465-2`

## 今回この箇所を選んだ理由

- core pages と verification 側では、living-human observability を route family ごとに割って読む stop line がかなり整っていました。
- しかし文献入口である `mind_uploading_papers.md` と `research_harvest_50.md` では、`SV2A PET` がまだひとまとまりの human measurement advance として読める余地が残っていました。
- この圧縮を放置すると、
  - quantification route
  - healthy atlas
  - disease contrast
  - task / cognition association
  - activation null
  - intervention response
  が同一の inferential object に見えてしまい、`current synaptic state` や `current synaptic efficacy` に過読されます。

## 主要結論

- `SV2A / synaptic-density PET` は一つの solved route ではございません。
- 少なくとも
  - tracer / quantification
  - healthy baseline atlas
  - disease-linked contrast
  - task / cognition association
  - activation null under brief stimulation
  - intervention response ceiling
  を分けて読む必要がございます。
- したがって文献入口ページでも、`SV2A PET` という一語を直接 `current synaptic efficacy` や `momentary synaptic state` に接続させない stop line を明示すべきでございました。

## 根拠付き批判

### 1. Quantification route は atlas でも disease contrast でもありません

- 根拠:
  - [Naganawa et al. (2024)](https://doi.org/10.1007/s00259-024-06885-6) は、<sup>18</sup>F-SynVesT-1 について 1TC を reference standard とした simplified reference tissue model 2 を検証し、noninvasive quantification route を詰めました。
- 批判:
  - これは tracer-specific quantification の話であり、healthy atlas truth でも disease-linked effect でもございません。
  - 文献入口で `SV2A PET` を一行で済ませると、この quantification burden が消えます。

### 2. Healthy atlas は disease contrast と同じ inferential slice ではありません

- 根拠:
  - [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024) は、高解像度の in vivo human synaptic-density atlas を提示しました。
- 批判:
  - これは healthy baseline construction に強い文献であり、病態差・介入感受性・momentary state readout を直接閉じるものではございません。
  - atlas を見たことと、current synaptic efficacy を測れたことは別でございます。

### 3. Disease contrast は universal baseline や current-state meter ではありません

- 根拠:
  - [Matuskey et al. (2025)](https://doi.org/10.1038/s41380-024-02776-2) は、自閉スペクトラム症成人における [<sup>11</sup>C]UCB-J の lower synaptic density を case-control 比較として示しました。
- 批判:
  - これは disease-linked regional contrast であり、healthy atlas の代用でも、momentary synaptic state の readout でもございません。
  - 病態差が見えたことを current-state observability に読み替えるのは論理の飛躍でございます。

### 4. Task / cognition association は activation truth ではありません

- 根拠:
  - [Shatalina et al. (2024)](https://doi.org/10.1162/imag_a_00190) は、healthy adults における [<sup>11</sup>C]UCB-J と task switching / switch cost との関連を示しました。
- 批判:
  - これは selected executive-function association の slice であり、全課題一般の cognition meter でも、momentary activation meter でもございません。
  - `task-related association` と `current synaptic efficacy readout` は別物でございます。

### 5. Brief activation null は PET binding の時間分解能と ceiling を示します

- 根拠:
  - [Smart et al. (2021)](https://doi.org/10.1177/0271678X20946198) は、brief visual stimulation で tracer delivery は増えても [<sup>11</sup>C]UCB-J binding は変化しなかったことを示しました。
- 批判:
  - これは `activation changed` と `SV2A binding changed` が自動で一致しないことを示す重要な null でございます。
  - したがって `SV2A PET = momentary neural activity meter` と読む余地は入口で止める必要がございました。

### 6. Intervention response null は symptom improvement と同じではありません

- 根拠:
  - [Holmes et al. (2022)](https://doi.org/10.1038/s41380-022-01465-2) は、ketamine 後 24 時間で症状改善が見えても overall SV2A density change は測定されなかったことを示しました。
- 批判:
  - 介入で臨床症状が動いたことと、SV2A PET が whole-brain synaptic restoration truth を返したことは別でございます。
  - intervention response ceiling を分けないまま `SV2A PET` を一語で扱うと、この差が消えます。

## 今回実行した変更

- `mind_uploading_papers.md`
  - front matter の `known_points` / `page_highlights` に、SV2A PET route split を追加しました。
  - 技術導入部に新規 note-box `Read SV2A / synaptic-density PET as several separate questions` を追加しました。
  - evidence-class table の `observability-class advance / human in vivo proxy ladder` 行を更新し、SV2A PET を
    - tracer / quantification
    - atlas
    - disease
    - task
    - activation
    - intervention
    slice に分けて読むよう修正しました。

- `research_harvest_50.md`
  - front matter の `page_highlights` / `known_points` に、U7 内の SV2A route split を追加しました。
  - human-measurement note-box 内に、SV2A route split の stop line paragraph を追加しました。
  - human measurement anchor table に
    - Naganawa et al. (2024)
    - Matuskey et al. (2025)
    - Shatalina et al. (2024)
    を追加し、Johansen 2024 だけでは表現できない slice 分解を明示しました。

## 今回止めた誤読

- `SV2A PET` = one solved human synaptic-state route
- `SV2A atlas` = disease contrast or intervention response
- `task-linked association` = current synaptic efficacy meter
- `brief activation` = PET binding should change immediately
- `clinical improvement after intervention` = measurable global SV2A restoration

## 外部依存タスク

- なし
  - 今回の修正は文献確認、ページ修正、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Naganawa M, et al. A noninvasive quantification method for [<sup>18</sup>F]SynVesT-1 PET imaging using a simplified reference tissue model 2 validated by a one-tissue compartment model. *European Journal of Nuclear Medicine and Molecular Imaging*. 2024.
   - https://doi.org/10.1007/s00259-024-06885-6
2. Johansen A, et al. In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Matuskey D, et al. Lower synaptic density in autistic adults assessed with [<sup>11</sup>C]UCB-J PET. *Molecular Psychiatry*. 2025.
   - https://doi.org/10.1038/s41380-024-02776-2
4. Shatalina E, et al. Synaptic density is associated with task-related activation and task-switching costs in healthy humans. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00190
5. Smart K, et al. In vivo demonstration of limited sensitivity of [<sup>11</sup>C]UCB-J to acute changes in synaptic density during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
6. Holmes SE, et al. Lower synaptic density is associated with depression severity and network alterations, but ketamine response does not show measurable overall SV2A change at 24 h. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-022-01465-2
