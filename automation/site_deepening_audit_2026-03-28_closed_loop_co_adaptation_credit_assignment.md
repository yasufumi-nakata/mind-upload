# Site Deepening Audit (2026-03-28, closed-loop co-adaptation / credit-assignment wall)

## 対象

- 主対象: `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- 同期対象:
  - `github-wiki-export/closed-loop-latency-jitter-and-safety-stops.md`
  - `verification.md`
- web確認対象:
  - `https://mind-upload.com/wiki/closed-loop-latency-jitter-and-safety-stops.html`
  - `https://doi.org/10.1016/j.neuron.2014.04.048`
  - `https://doi.org/10.1371/journal.pbio.2003787`
  - `https://doi.org/10.3389/fnhum.2019.00362`
  - `https://doi.org/10.1016/j.eswa.2023.120205`
  - `https://doi.org/10.1038/s41586-025-09127-3`
  - `https://doi.org/10.1038/s41551-025-01536-z`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `closed-loop` 系ページは、2026-03-28 時点ですでに
  - latency / jitter
  - fixed-decoder durability
  - rescue-mode recalibration
  - clinic-home transfer / eligibility
  をかなり厳密に分けていました。
- しかしなお一つ、重要な混線源が残っていました。`online performance improved` を読んだときに、
  - user-side learning
  - decoder update
  - application / interaction redesign
  のどれが寄与したのかを、ページが独立項目として固定していませんでした。
- この欠落があると、`オンラインで良くなった` がそのまま
  - `decoder が安定した`
  - `固定デコーダで持続した`
  - `deployable になった`
  に読めてしまいます。

## 根拠付き批判

### 1. closed-loop の改善は timing だけではなく、co-adaptation の産物でありえます

- [Orsborn et al. (2014)](https://doi.org/10.1016/j.neuron.2014.04.048) は、decoder adaptation が neural plasticity 自体を形作りうることを示しました。
- したがって、closed-loop gain を見ても、それは「既存 decoder が安定だった」のではなく、「decoder 更新が neural strategy を変えた」結果かもしれません。

批判:

- `fast online control` をそのまま `stable fixed decoder` と読むのは技術的に誤りです。
- timing audit と credit assignment audit は別問題です。

### 2. non-invasive EEG BCI でも、classifier adaptation と user learning は独立に切り分ける必要があります

- [Abu-Rmileh et al. (2019)](https://doi.org/10.3389/fnhum.2019.00362) は、4 日間の EEG motor imagery BCI で、固定 classifier 群と継続適応 classifier 群を直接比較しました。
- [Perdikis et al. (2018)](https://doi.org/10.1371/journal.pbio.2003787) は、長期 mutual learning の end-user 例を示し、頻繁な recalibration が subject learning を阻害しうると論じました。
- [Lin et al. (2023)](https://doi.org/10.1016/j.eswa.2023.120205) は、real-time mutual learning で classifier 更新と users' imagination strategy change が両方とも成績改善に寄与しうることを示しました。

批判:

- `accuracy improved online` だけでは、user が学習したのか、classifier が追従したのか、両方なのかが分かりません。
- したがって `same-session online gain` は、`credit-assigned fixed-policy result` より弱い evidence slice として扱うべきです。

### 3. 2025 年の speech / cursor neuroprosthesis でも、closed-loop 成功は固定 decoder の成功と同義ではありません

- [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) では、session ごとに過去 session を使って decoder を再学習し、participant の engagement / enunciation が synthesis quality に影響したと報告されています。
- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) では、closed-loop block ごとに decoder weights を更新しつつ、open-loop block を別に置いて closed-loop correction を含まない probe を取っています。

批判:

- これは `modern online loop` ですら、fixed decoder / updated decoder / user correction を分離しないと意味が変わることを示します。
- よって、この分離を page rule として明文化しないのは site-wide governance 上の穴でした。

## 今回実行した変更

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `accuracy_note` / `page_highlights` / `known_points` / `unknown_points` に `co-adaptation regime` を追加しました。
  - `2026-03-28 re-audit: co-adaptation is a separate evidence wall` を追加しました。
  - `Co-adaptation must be separated before online gains are interpreted` セクションを追加し、
    - user-side learning
    - decoder-side adaptation
    - application / interaction shaping
    を別 object として固定しました。
  - `four barriers` を `five barriers` に更新し、`co-adaptation / credit assignment` を最初の壁として追加しました。
  - `card stack` に `same-session fixed-policy local loop` と `same-session co-adaptive local loop` を分離して追加しました。
  - `minimum log` に `co-adaptation regime`, `credit-assignment probe`, `user/application training changes` を追加しました。
  - `11 questions` を `12 questions` に更新し、`Does it separate user learning, decoder updates, and interface redesign?` を追加しました。
  - 参考文献へ Orsborn 2014, Perdikis 2018, Abu-Rmileh 2019, Lin 2023 を追加しました。

- `github-wiki-export/closed-loop-latency-jitter-and-safety-stops.md`
  - GitHub Wiki 側にも同じ co-adaptation / credit-assignment rule を同期しました。

- `verification.md`
  - header highlights に `Co-Adaptation Log` を追加しました。
  - `2026-03-28 addendum` を追加し、L3 entrance で co-adaptation を先に切り分ける規則を明文化しました。
  - `Gate 1 / online decode` を、frozen/update disclosure を要求する形へ更新しました。
  - `Additional audit logs` に `Co-Adaptation Log` を追加しました。
  - 参考文献へ Orsborn 2014, Perdikis 2018, Abu-Rmileh 2019, Lin 2023 を追加しました。

## 今回止めた誤読

- `same-session online improvement = fixed decoder が安定した`
- `online loop が成立 = latency 問題だけが支配的`
- `adaptive rescue がうまくいった = user learning も deployability も同時に改善した`
- `speech / cursor loop の高成績 = session-to-session retraining や blockwise update の影響は小さい`
- `オンラインで良くなった` という一言から、user learning / decoder adaptation / interface redesign をまとめて読んでよい

## 外部依存タスク

- なし
  - 今回の作業は repo 内本文、監査メモ、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Orsborn AL, Moorman HG, Overduin SA, Shanechi MM, Dimitrov DF, Carmena JM. Closed-loop decoder adaptation shapes neural plasticity for skillful neuroprosthetic control. *Neuron*. 2014;82(6):1380-1393.
   - https://doi.org/10.1016/j.neuron.2014.04.048
2. Perdikis S, Tonin L, Saeedi S, Schneider C, Millán J del R. The Cybathlon BCI race: successful longitudinal mutual learning with two tetraplegic users. *PLoS Biology*. 2018;16(5):e2003787.
   - https://doi.org/10.1371/journal.pbio.2003787
3. Abu-Rmileh A, Zakkay E, Shmuelof L, Shriki O. Co-adaptive training improves efficacy of a multi-day EEG-based motor imagery BCI training. *Frontiers in Human Neuroscience*. 2019;13:362.
   - https://doi.org/10.3389/fnhum.2019.00362
4. Lin CY, Lu CF, Jao CW, Wang PS, Wu YT. Toward consistency between humans and classifiers: improved performance of a real-time brain-computer interface using a mutual learning system. *Expert Systems with Applications*. 2023;226:120205.
   - https://doi.org/10.1016/j.eswa.2023.120205
5. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
6. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
