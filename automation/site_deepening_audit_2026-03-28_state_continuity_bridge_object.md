# Site Deepening Audit (2026-03-28, state continuity bridge object)

## 対象

- 主対象: `wiki/state-continuity-bridge.md`
- 参照整合先: `verification.md`

## 今回の選定理由

- 2026-03-28 JST 時点で、サイト全体の `same-subject / same-brain` 停止線はかなり強くなっておりました。
- ただし `wiki/state-continuity-bridge.md` だけは、`bridge class` と `hidden-state family` は示せていても、`何を carry over したいのか` がまだ十分に固定されておりませんでした。
- この欠落は技術・自然科学の観点で弱点です。理由は、同じ `bridge` でも実際に持ち越される object が
  - landmark / targeted subvolume
  - latent manifold
  - representational geometry
  - fingerprint feature family
  のように異なり、それぞれ failure mode も validation rule も違うからです。

## 根拠付き批判

### 1. `same-subject` と `elapsed time` だけでは bridge object が空欄のままです

- 問題:
  - 旧ページは「何秒・何日空いたか」「どの state family が drift するか」は整理していました。
  - しかし「何が actually preserved されたと言いたいのか」が表に出ておらず、読者が暗黙に `whole state` を想像できる余地が残っておりました。
- 根拠:
  - Bosch et al. (2022) は in vivo physiology から synchrotron microtomography / volume EM への multistage workflow を示しましたが、carry しているのは landmark と targeted subvolume です。
  - MICrONS Consortium et al. (2025) も same-brain function-plus-EM を大きく前進させましたが、global same-state capture ではなく local structure-function correspondence です。
- 批判:
  - したがって、bridge では `window` だけでなく `object` を named しないと、same-brain wording が過大に読まれます。

### 2. 安定に見えるものは one universal object ではありません

- 問題:
  - 旧ページは drift risk を強調していましたが、逆に「何が安定しうるのか」の object-level split は十分に出していませんでした。
- 根拠:
  - Gallego et al. (2020) は recorded neurons が入れ替わっても low-dimensional latent dynamics が安定しうることを示しました。
  - Roth & Merriam (2023) は human V1 で response amplitude は drift しても representational similarity は保たれうることを示しました。
  - Noda et al. (2025) は selective neuron loss の後でも population-level representational map が回復しうることを示しました。
  - Van De Ville et al. (2021) と Di et al. (2021) は fingerprint-like identifiability が timescale や feature family に依存することを示しました。
- 批判:
  - したがって、bridge で「安定」と書くなら `latent manifold` なのか `representational geometry` なのか `fingerprint feature family` なのかを named しないと、object がすり替わります。

### 3. score stability は raw continuity と同義ではありません

- 問題:
  - 旧ページは cross-day drift を扱っていましたが、`score が維持された` と `same object が保たれた` の区別がまだ弱いままでした。
- 根拠:
  - Karpowicz et al. (2025) は latent-dynamics alignment によって decoding stability を改善しました。
  - Wilson et al. (2025) は hidden Markov model による unsupervised recalibration で one-month closed-loop cursor control を維持しましたが、これは neural change の不存在ではなく adaptation route の成功です。
  - Wairagkar et al. (2025) は brain-to-voice decoder の fixed slice が約 15 日で目立って劣化することを示しました。
- 批判:
  - したがって、`still works` は bridge validity の十分条件ではありません。
  - rescue mode, recalibration burden, fixed-decoder horizon を書かずに continuity を主張すると、adaptive salvage を preserved state と誤読させます。

### 4. workflow sophistication ではなく tolerance / failure rule が必要です

- 問題:
  - 旧ページには `bridge validation rung` はありましたが、「どこで bridge failed と判定するのか」が運用上まだ曖昧でした。
- 根拠:
  - Bosch / MICrONS は correspondence を local に絞り、quality-controlled な witness を持っております。
  - Van De Ville / Di は fingerprint object が time window と feature family によって変わることを示しております。
  - Karpowicz / Wilson / Wairagkar は performance が alignment や recalibration で大きく左右されることを示しております。
- 批判:
  - したがって `bridge witness` と `tolerance / failure rule` を card に追加しないと、bridge validation は still too narrative です。

## 今回実行した変更

- `wiki/state-continuity-bridge.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter に `carried object / witness` の stop line を追加しました。
  - `2026-03-28 addendum` として、bridge object と tolerance budget を要求する note-box を追加しました。
  - `A bridge must name what is supposed to survive` の新節を追加し、
    - landmark / targeted subvolume
    - latent manifold
    - representational geometry / map
    - fingerprint feature family
    を別 object として分離しました。
  - `Performance rescue is not the same thing as raw continuity` note を追加し、alignment / recalibration / fixed-decoder horizon の違いを明記しました。
  - `A bridge needs a tolerance and failure rule` の新節を追加し、carried object, tolerance, negative control, rescue mode を分離しました。
  - misreading table に `stable score or fingerprint = same object persisted` を拒否する行を追加しました。
  - references に Gallego, Roth & Merriam, Noda, Van De Ville, Di, Karpowicz, Wilson, Wairagkar を追加しました。
- `verification.md`
  - `State-Continuity Bridge Card` に `Carried object / bridge witness and tolerance rule` 行を追加しました。
  - `2026-03-28 addendum` を追加し、bridge card が `when` だけでなく `what survived` と `how failure would be detected` を問うことを明文化しました。

## 外部依存で保留

- bridge witness benchmark の公開整備
  - 担当者: correlative imaging 研究者 / chronic BCI 研究者 / benchmark 設計者 / maintainer
  - 前提条件: landmark correspondence, latent manifold alignment, representational geometry stability, fingerprint feature-family transfer を同一 schema で比較できる公開データ
  - 完了条件: bridge object ごとに tolerance / negative-control / rescue-mode を比較できる benchmark board が整備されること

## 参考文献

1. Bosch C, Pacureanu A, Patino J, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
2. MICrONS Consortium, Bae JA, Lee W-CA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
3. Gallego JA, Perich MG, Chowdhury RH, et al. Long-term stability of cortical population dynamics underlying consistent behavior. *Nature Neuroscience*. 2020.
   - https://doi.org/10.1038/s41593-019-0555-4
4. Roth ZN, Merriam EP. Representations in human primary visual cortex drift over time. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-40144-w
5. Noda T, Hattori R, Yamanaka A, et al. Homeostasis of a representational map in the neocortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01982-7
6. Van De Ville D, Farouj Y, Preti MG, Liégeois R, Amico E. When makes you unique: Temporality of the human brain fingerprint. *Science Advances*. 2021.
   - https://doi.org/10.1126/sciadv.abj0751
7. Di Y, An X, Zhong W, Liu S, Ming D. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. *Frontiers in Human Neuroscience*. 2021.
   - https://doi.org/10.3389/fnhum.2021.672946
8. Karpowicz BM, O'Shea DJ, Wyche S, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-59652-y
9. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
10. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
