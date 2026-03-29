# Site Deepening Audit (2026-03-30, datasets inverse-validation density / extent split)

## 対象

- 主対象:
  - `datasets.md`
- 調査範囲:
  - 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `datasets.md` は公開サイトの中で、実際に「どのデータから始めるべきか」「どこから source-imaging claim を強くしてよいか」を決める入口でございます。
- そのため、ここで `HD-EEG vs low-density` や `focal error vs source extent` を粗く書くと、以後の benchmark 設計全体が歪みます。
- 2026-03-30 時点の site-wide rule では `validation class`、`source regime`、`geometry / conductivity sensitivity` はかなり整理されていましたが、`datasets.md` にはなお次の簡略化が残っておりました。
  - `HD-EEG is the serious route, low-density is the weak route`
  - `direct validation = solved benchmark object`
  - `geometric center error` と `source extent / propagation-rich object` の圧縮

## 主要結論

- 現時点の一次文献は、`electrode density` を単独の主軸として読むことを支持しておりません。
- より安全な整理は、
  - `named montage / coverage policy`
  - `solver family`
  - `source regime`
  - `validation class`
  を分けることでございます。
- さらに `direct validation` であっても、
  - `focal-center distance`
  - `source extent / overlap`
  - `propagation-rich network object`
  は別 benchmark object として扱う必要がございます。

## 根拠付き批判

### 1. `HD-EEG vs low-density` の二項対立はもう粗すぎます

- [Horrillo-Maysonnial et al. (2023)](https://doi.org/10.1016/j.clinph.2023.08.009) は、`33-36 electrodes` の targeted-density montage が `83-electrode` HD montage に対して `54/58` sublobar concordance (`93%`) を示した一方、`tangential generators` では peak-vertex distance が悪化することを示しました。
- [Rong et al. (2025)](https://doi.org/10.1016/j.clinph.2025.04.009) は、DeepSIF 系の deep-learning ESI が `75 -> 16 electrodes` にまたがって比較的安定で、平均 spatial dispersion が `7.9/9.0 mm` だった一方、sLORETA と LCMV ははるかに大きい dispersion を示すと報告しました。

批判:

- したがって、`high-density でなければ議論にならない` と読むのも、
- 逆に `low-density でも十分と示された` と読むのも、
- どちらも過読でございます。
- 現在の一次文献が支持するのは、
  - montage design
  - solver family
  - generator regime
  を固定したうえでの `bounded success`
  であり、
  - `density no longer matters in general`
  ではありません。

### 2. direct validation があっても geometry / conductivity / depth dependence は残ります

- [Unnwongse et al. (2023)](https://doi.org/10.1093/braincomms/fcad023) は direct validation においても、coverage geometry と conductivity assumption が localization error を動かすことを示しました。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は simultaneous HD-EEG / SEEG において、ictal ESI (`14.07 ± 4.62 mm`) が interictal ESI (`17.38 ± 4.16 mm`) より良い一方、`source depth` と `spike power` が依然として精度を左右することを示しました。

批判:

- したがって `C-stage direct validation data を使った` という事実だけで、
  - montage dependence
  - depth dependence
  - generator visibility
  - conductivity sensitivity
  が解消したと読むことはできません。
- `validation class` を named で書くだけでなく、`same-geometry controls` の中に montage / coverage policy を入れる必要がございました。

### 3. `focal center error` と `source extent` は同じ benchmark object ではありません

- [Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219) は in-vivo focal-source benchmark において、method ranking が regularization や montage density に依存することを示しました。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は、そもそも `extended-source reconstruction` を別 object として扱っています。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) も、自身の `ECD` ベース比較は `spatial extent` を捉えきれない制限を認め、今後は SOZ / IZ の extent を取り込むべきだと述べています。

批判:

- これにより、`known site distance` で勝った solver をそのまま `distributed / extended / propagation-rich source` に一般化するのは不正確でございます。
- 入口ページの datasets では、ここを明示しないと、
  - focal-centre board
  - extent-overlap board
  - propagation-aware board
  が一つの leaderboard に潰れてしまいます。

## 今回実行した変更

- `datasets.md`
  - `last_updated` を `2026-03-30` に更新しました。
  - front matter の `page_highlights` を更新し、
    - `focal-centre vs source-extent`
    - `montage / coverage policy`
    - `bounded low-density / targeted-density success`
    を明示しました。
  - `known_points` と `unknown_points` を更新し、
    - low-density / targeted-density を universal claim にしない
    - focal-centre と source-extent を別 default board として扱う
    ことを明記しました。
  - validation ladder 節に新しい note-box を追加し、
    - Horrillo-Maysonnial 2023
    - Rong 2025
    - Unnwongse 2023
    - Hao 2025
    を用いて `HD vs low-density` の粗い二分法を止めました。
  - inverse-problem benchmark board 節に新しい note-box を追加し、
    - Feng 2025
    - Hao 2025
    を用いて `centre error ≠ source extent`
    を明文化しました。
  - section の site rule を更新し、
    - `source regime and target object`
    - `same-geometry controls including montage / coverage policy`
    を必須 disclosure に追加しました。

## 今回止めた誤読

- `HD-EEG = serious / low-density = weak`
- `targeted-density or DeepSIF success = electrode density no longer matters`
- `direct validation = geometry / conductivity / depth dependence solved`
- `focal-center error = source extent / overlap / propagation`
- `solver winner on one board = solver winner in general`

## 外部依存タスク

- なし
  - 今回の変更は、文献確認、公開ページ改稿、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Horrillo-Maysonnial A, Avigdor T, Abdallah C, et al. Targeted density electrode placement achieves high concordance with traditional high-density EEG for electrical source imaging in epilepsy. *Clinical Neurophysiology*. 2023;156:262-271.
   - https://doi.org/10.1016/j.clinph.2023.08.009
2. Rong J, Sun R, Joseph B, Worrell G, He B. Deep learning-based EEG source imaging is robust under varying electrode configurations. *Clinical Neurophysiology*. 2025;175:2010730.
   - https://doi.org/10.1016/j.clinph.2025.04.009
3. Unnwongse K, Van Klink N, Tousseyn S, et al. Validating EEG source imaging using intracranial electrical stimulation. *Brain Communications*. 2023;5(1):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
4. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66:4451-4464.
   - https://doi.org/10.1111/epi.18552
5. Pascarella A, Westin K, Blenkmann AO, et al. Performance characterization of EEG source imaging algorithms in an in-vivo benchmark for focal cortical source localization. *NeuroImage*. 2023;277:120219.
   - https://doi.org/10.1016/j.neuroimage.2023.120219
6. Feng Z, Guan C, Sun Y. Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2025.3642620
