# Site Deepening Audit (2026-03-26, closed-loop temporal validity / deployability split)

## 対象

- 主対象: `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- 同期対象: `github-wiki-export/closed-loop-latency-jitter-and-safety-stops.md`
- 参照整合先: `verification.md`, `wiki/state-trait-and-drift.md`, `eeg_101.md`, `tech_roadmap.md`
- web確認対象:
  - `https://mind-upload.com/wiki/closed-loop-latency-jitter-and-safety-stops.html`
  - `https://doi.org/10.1038/s41593-025-01905-6`
  - `https://doi.org/10.1038/s41586-025-09127-3`
  - `https://doi.org/10.1038/s41551-025-01536-z`
  - `https://doi.org/10.1038/s41591-024-03196-z`
  - `https://doi.org/10.1038/s41531-026-01269-z`
  - `https://doi.org/10.1038/s41551-025-01438-0`
  - `https://doi.org/10.1038/s41531-025-01124-7`
- 調査範囲: 技術 / 自然科学のみ

## 今回このページを選んだ理由

- 公開中の `wiki/closed-loop-latency-jitter-and-safety-stops.md` は `2026-03-19` 更新のままで、site-wide に前面化された
  - `Temporal Validity Card`
  - `Body / Environment Boundary Card`
  - `Calibration & Abstention Card`
  - chronic closed-loop の deployability burden
  との接続がまだ弱い状態でした。
- その結果、読者は依然として
  - `オンラインで動いた`
  - `速かった`
  - `後で再較正して戻せた`
  - `在宅でも一応使えた`
  を、一段ずつ別の evidence slice ではなく一つの「閉ループ成熟度」として読めてしまいます。
- これは自然科学的に弱いです。一次文献が示しているのは、same-session の timing 成功、fixed decoder の時間的耐久性、rescue-mode の更新 burden、eligibility / continuation / home-use transfer が別問題だということだからです。

## 主批判

### 1. 旧ページは `same-session low latency` と `fixed-decoder durability` をまだ十分に分離していませんでした

- 問題:
  - 旧ページは timing, jitter, tail latency をかなり整理できていました。
  - しかし `速く動いた loop` と `更新なしで時間をまたいで保てた loop` を独立の stop line としてはまだ固定できていませんでした。
- 根拠:
  - [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は accumulating neural changes により static decoder が使えない期間が生じることを前提に、one-month 閉ループ運用を fixed-decoder comparator 付きで評価しました。
- 批判:
  - したがって `same-session fast` を `durable` に読み替えるのは過大です。
  - closed-loop wiki 自体が `fixed decoder interval` を明示しないと、same-session success が cross-day durability へ短絡されます。

### 2. 旧ページは `fixed-decoder failure` と `adaptive rescue` を一つの drift 問題に圧縮していました

- 問題:
  - 旧版では `recalibration burden / drift` が一段でした。
  - しかし実際には、`更新なしで耐えたか` と `更新して救えたか` は別々に読まなければなりません。
- 根拠:
  - [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は unsupervised recalibration を multi-timescale で扱いました。
  - [Dixon et al. (2026)](https://doi.org/10.1038/s41551-025-01438-0) は remotely optimized neural decoder による movement-responsive aDBS を示しました。
  - [Busch et al. (2025)](https://doi.org/10.1038/s41531-025-01124-7) は biomarker selection, threshold definition, artifact-related maladaptation を programming burden として明示しました。
- 批判:
  - したがって `再較正すれば戻った` を `もともと安定だった` と読んではなりません。
  - rescue-mode はそれ自体が別の operating regime であり、manual / unsupervised / remote optimization を分けて記録すべきです。

### 3. 旧ページは `deployable chronic loop` の前にある `eligibility / continuation` の stop line が弱いままでした

- 問題:
  - 旧ページには clinic/home transition と programming burden への言及はありました。
  - しかし `どれだけの患者がそもそも適格なのか`、`どれだけ継続できたのか` を独立の evidence object として前景化できていませんでした。
- 根拠:
  - [Oehrn et al. (2024)](https://doi.org/10.1038/s41591-024-03196-z) は in-clinic と at-home をまたぐ chronic aDBS feasibility を示しました。
  - [Busch et al. (2025)](https://doi.org/10.1038/s41531-025-01124-7) では 8 例中 6 例が aDBS 継続を選択しました。
  - [Cascino et al. (2026)](https://doi.org/10.1038/s41531-026-01269-z) では 20 連続 chronic cDBS 症例のうち 9 例のみが適格で、2025年7月時点で 5 例が chronic aDBS 継続でした。
- 批判:
  - したがって `benefit was shown in programmed cases` を `route is broadly deployable` に読み替えるのは不適切です。
  - 継続率と適格率は symptom effect と別に出さないと、運用可能性を過読します。

### 4. 旧ページは `timing page` でありながら、実際には `card stack` の問題を十分に可視化していませんでした

- 問題:
  - 旧版は timing と boundary の二層までは整理していました。
  - しかし closed-loop claim が same-session を離れたときに
    - `Temporal Validity Card`
    - `Body / Environment Boundary Card`
    - `Calibration & Abstention Card`
    をどう重ねるのかが本文レベルでは弱いままでした。
- 批判:
  - そのままでは読者が `timing wiki を読めば L3 の論点は足りた` と誤解します。
  - 実際には same-session, fixed-decoder, rescued, chronic naturalistic の各 slice ごとに別の card stack が必要です。

## 今回実行した変更

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter の `description`, `page_intro`, `accuracy_note`, `page_highlights`, `known_points`, `unknown_points`, `wiki_links` を更新
  - `Three public cards are stacked here, not one timing score` note を新設
  - 長期運用セクションを `three barriers` から `four barriers` へ改稿
    - tail latency / output path
    - fixed-decoder durability
    - rescue-mode recalibration / remote optimization burden
    - eligibility / continuation / naturalistic transfer
  - `Which public card gets stacked when the loop leaves same-session` section を新設
  - checklist に
    - fixed decoder interval / training-free horizon
    - rescue-mode policy
    - eligibility / continuation / naturalistic deployment
    を追加
  - `9 questions` を `11 questions` へ更新し、
    - fixed decoder vs rescue
    - rescue cost
    - eligibility / continuation vs benefit
    を独立質問として追加
  - 参考文献に Dixon 2026, Busch 2025 を追加

## 今回止めた誤読

- `online で動いた = durable`
- `durability が落ちたが rescue できた = originally stable`
- `programmed cases で benefit = route is broadly deployable`
- `timing wiki = L3 の card stack まで十分`
- `same-session fast loop = chronic home-use closed loop`

## 外部依存タスク

- なし
  - 今回の修正は公開本文、監査メモ、wiki export 再生成、build 検証で repo 内完結です。

## 参考文献

1. Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01905-6
2. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
3. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
4. Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. *Nature Medicine*. 2024.
   - https://doi.org/10.1038/s41591-024-03196-z
5. Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. *npj Parkinson's Disease*. 2026.
   - https://doi.org/10.1038/s41531-026-01269-z
6. Dixon TC, Strandquist G, Zeng A, et al. Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. *Nature Biomedical Engineering*. 2026;10:110-124.
   - https://doi.org/10.1038/s41551-025-01438-0
7. Busch JL, Kaplan J, Behnke JK, et al. Chronic adaptive deep brain stimulation for Parkinson’s disease: clinical outcomes and programming strategies. *npj Parkinson's Disease*. 2025;11:264.
   - https://doi.org/10.1038/s41531-025-01124-7
