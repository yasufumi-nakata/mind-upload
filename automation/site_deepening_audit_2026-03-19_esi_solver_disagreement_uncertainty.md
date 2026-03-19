# Site Deepening Audit (2026-03-19, ESI Solver Disagreement / Uncertainty Ceiling)

## 対象

- 主対象: `eeg_101.md`
- 副対象: `verification.md`
- 副対象: `wiki/observation-to-estimation.md`
- 副対象: `faq.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイトは、`ESI は solver 名で読むな`、`validation class を分けろ`、`individual MRI / electrode coordinates / conductivity assumptions を出せ` という基礎線はすでに整っておりました。
- その一方で、`同じデータに対して複数の妥当な inverse family / package / parameter window を流したとき、結果がどの程度ずれるなら claim ceiling を下げるべきか` が public rule になっておりませんでした。
- この欠落は技術・自然科学の観点で重要です。なぜなら、EEG inverse problem の本質的な不良設定性は、`validation class` を書くだけでは消えず、`one best map` を front door に置くと読者が `source fact` と誤読しやすいからです。

## 根拠付き批判

### 1. `validation class` だけでは `one best inverse map` の過大読みに歯止めがかかっていませんでした

- 問題:
  - 既存サイトは `simulation / phantom / intracranial stimulation / simultaneous SEEG / postsurgical outcome` を分けておりました。
  - しかし、それでも公開本文上は `best-looking map` が残りうるため、読者は `validated` を `stable` と読み替えやすい構造でした。
- 根拠:
  - Mahjoory et al. (2017) は、inverse method と software implementation の選択が EEG source localization をかなり変え、connectivity ではさらに一貫性が落ちることを示し、複数の source-imaging procedure で確認するよう勧めました。
  - Mikulan et al. (2020) は、known stimulation site を ground truth とした benchmark で、all-parameter combinations を見ると localization distance が広く分布し、session-wise optimum に届く解は少数であることを示しました。
- 批判:
  - したがって `validated ESI` という語だけでは不足です。
  - 必要なのは、`どの solver family / package / parameter window でどの程度動くか` を開示し、`best solution` を `stable solution` と同一視しない public rule でした。

### 2. 導電率不確実性がまだ `geometry note` に留まり、`solution-set spread` へ落ちていませんでした

- 問題:
  - 既存サイトは skull conductivity を重要と書いていましたが、その含意が `error bar を広げる` で止まり、`solution-set spread を mandatory disclosure にする` ところまで明文化しておりませんでした。
- 根拠:
  - Vorwerk et al. (2024) は、whole-cortex source で tissue conductivity uncertainty の global sensitivity を解析し、特に skull conductivity が signal topography と reconstructed depth に強い影響を与えること、quasi-tangential source で localization が大きく動くことを示しました。
  - Unnwongse et al. (2023) も、direct validation で mean localization error が source depth と skull-conductivity setting によって 10.3-26.0 mm に広がることを示しました。
- 批判:
  - つまり conductivity は単なる補足パラメータではございません。
  - `conductivity assumption` を書くだけでなく、`その仮定が result spread をどれだけ動かしたか` を出さなければ、読者は点推定を過信します。

### 3. simultaneous invasive validation でも `安定な source fact` にはまだ届きませんでした

- 問題:
  - site は simultaneous SEEG を高い validation class として適切に位置づけていましたが、front door では `そこまで行けばかなり source fact に近い` と読める余地が残っていました。
- 根拠:
  - Hao et al. (2025) は 29 例の simultaneous HD-EEG/SEEG で、ictal ESI が interictal ESI より良い一方、平均誤差はなお 14.07 ± 4.62 mm と 17.38 ± 4.16 mm であり、source depth と spike power が精度に強く影響すると報告しました。
- 批判:
  - これは重要な前進ですが、`simultaneous invasive validation = stable anatomical truth` ではございません。
  - 読み方として正しいのは、`validation class が強い` ことと `solution-set stability が高い` ことを分離することです。

## 今回実行した変更

- `eeg_101.md`
  - front matter に `one best inverse map is not enough` という guardrail を追加しました。
  - `What must now be stated rigorously about ESI` を `Four floors` に改め、`solver-stability floor` を追加しました。
  - `2026-03-19 addendum: a single best inverse map is not enough` を追加し、Mahjoory (2017), Mikulan (2020), Vorwerk (2024) に基づいて `cross-solver / cross-parameter spread` または `posterior / ensemble width` を必須化しました。
- `verification.md`
  - front matter の `page_highlights` / `known_points` に ESI solver-disagreement rule を追加しました。
  - `Observability Budget` に `solution-set stability` 行を追加しました。
  - `2026-03-19 addendum: ESI claims need a solver-disagreement audit` を追加しました。
  - `Additional audit logs` に `Inverse-Solver Agreement Log` を追加しました。
- `wiki/observation-to-estimation.md`
  - top matter に `cross-solver / cross-parameter disagreement is itself evidence about uncertainty` を追加しました。
  - ESI table に `Cross-solver stability` 行を追加しました。
  - `2026-03-19 deepening: one best map is not the same as a stable solution` を追加しました。
- `faq.md`
  - Q1 に、Mahjoory (2017) と Mikulan (2020) に基づく短い front-door correction を追加し、`pretty inverse map` をそのまま source fact に読まない rule を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・verification rule・wiki route・front door correction の改稿で完結しております。

## 参考文献

1. Mahjoory K, Nikulin VV, Botrel L, Linkenkaer-Hansen K, Fato MM, Haufe S. Consistency of EEG source localization and connectivity estimates. *NeuroImage*. 2017;152:590-601.
   - https://doi.org/10.1016/j.neuroimage.2017.02.076
2. Mikulan E, Russo S, Parmigiani S, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020;7:127.
   - https://doi.org/10.1038/s41597-020-0467-x
3. Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. *Brain Communications*. 2023;5(1):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
4. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024;18:1335212.
   - https://doi.org/10.3389/fnhum.2024.1335212
5. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
   - https://doi.org/10.1111/epi.18552
