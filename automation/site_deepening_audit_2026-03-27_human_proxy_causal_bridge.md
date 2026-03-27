# Site Deepening Audit (2026-03-27, human proxy causal bridge)

## 対象

- 主対象: `wiki/human-proxy-composition.md`
- 同期対象: `github-wiki-export/human-proxy-composition.md`
- 入口同期: `wbe_101.md`
- 検証同期: `verification.md`
- web確認対象:
  - `https://mind-upload.com/wiki/human-proxy-composition.html`
  - `https://mind-upload.com/wbe_101.html`
  - `https://mind-upload.com/verification.html`
  - `https://doi.org/10.1038/s41586-024-08170-w`
  - `https://doi.org/10.1038/s41586-025-09619-2`
  - `https://doi.org/10.1038/s41586-025-10068-0`
  - `https://doi.org/10.2967/jnumed.121.263255`
  - `https://doi.org/10.2967/jnumed.118.208009`
  - `https://doi.org/10.1038/s41593-025-02073-3`
  - `https://doi.org/10.1038/s41467-026-68374-8`

## 今回この箇所を選んだ理由

- このサイトではすでに `proxy class` と `calibrator role` の分離が進んでいましたが、`human proxy composition` の中核ページには、なお一つ大きな圧縮が残っていました。
- その圧縮とは、`局所動物実験での因果性` と `生体ヒトでの観測可能性` を並置しただけで、あたかも `責任を持つヒト内部コントローラが計測された` かのように読めてしまう点です。
- これは単なる表現上の曖昧さではありません。技術的には、
  - 種差
  - 空間単位差
  - 時間スケール差
  - 直接観測量の差
  - 介入系と受動観測系の差
  を跨いでいます。
- したがって、ここを止めない限り、サイト全体の stop line は `proxy family split` の次段で再び崩れます。

## 根拠付き批判

### 1. rodent causal paper と human proxy paper は、同じ inferential object を直接は共有していません

- `Williamson et al. (2025)` は、海馬での learning-associated astrocyte ensembles が memory recall を調節することを示しました。
- `Dewa et al. (2025)` は、astrocytic ensemble が multiday trace として memory stabilization に寄与することを示しました。
- `Bukalo et al. (2026)` は、basolateral amygdala astrocyte Ca2+ signaling が fear-memory retrieval / extinction representations を支えることを示しました。

批判:

- これらは強い因果論文ですが、対象は rodent の局所回路・局所細胞集団です。
- 一方で、ヒト側の `Villemagne et al. (2022)` は MAO-B linked reactive astrogliosis burden、`Tyacke et al. (2018)` は I2BS binding route、`Hirschler et al. (2025)` は CSF mobility、`Dagum et al. (2026)` は model-based overnight efflux を与えるにとどまります。
- したがって、両者を並べても言えるのは高々 `ある state family がどこかで因果的に重要であり、どこかで部分的に観測可能である` ということまでです。
- そこから直ちに `責任を持つヒト内部コントローラを測れた` と結論するのは、技術的にも自然科学的にも飛躍です。

### 2. human observability の改善は、controller identity の解決とは別問題です

- `Tyacke et al. (2018)` は first-in-human の I2BS PET を成立させましたが、これは target-defined binding route の成立であって、局所 astrocyte ensemble identity の直接読出しではありません。
- `Villemagne et al. (2022)` は MAO-B tracer で AD spectrum 上の reactive astrogliosis burden を示しましたが、局所 causal controller を同定したわけではありません。
- `Hirschler et al. (2025)` は人間の CSF mobility の region-specific driver を示しましたが、mobility proxy は controller state そのものではありません。
- `Dagum et al. (2026)` はヒト glymphatic clearance を plasma biomarker 側からモデル化しましたが、これは multicompartment inference を含む efflux route です。

批判:

- つまり、human observability が前進しても、そのまま `controller measurement` が前進したとは限りません。
- `target-defined binding`, `mobility`, `model-based efflux` は、どれも direct observable と model burden が異なります。
- にもかかわらず、サイト側で causal bridge を明示しないと、読者は `human proxy advances = causal mechanism now visible in humans` と誤読しやすくなります。

### 3. composition page の中央規則に bridge requirement が無いと、front door の厳しさが中核ページで失われます

- `wbe_101.md` と `verification.md` にはすでに proxy family の厳密化が入っていました。
- しかし `wiki/human-proxy-composition.md` に causal-bridge の stop line が無いままだと、読者は composition page で再び
  - `rodent causality + human proxy = measured human controller`
  という要約を行えます。

批判:

- これは site-wide governance 上の穴です。
- 中核ページで bridge assumption を要求しない限り、入口ページで止めた誤読が、統合ページで再導入されます。
- よって、修正対象として最優先でした。

## 今回実行した変更

- `wiki/human-proxy-composition.md`
  - `page_highlights` と `known_points` に、`local causal relevance` と `living-human observability` は別軸であることを追加しました。
  - `Another shortcut this page now blocks` を追加し、動物因果論文とヒトプロキシ論文の安易な加算を明示的に禁止しました。
  - `Eight collapse errors to block` を `Nine collapse errors to block` に拡張し、`Causal-bridge collapse` を新設しました。
  - 新セクション `Causal relevance is not yet human controller measurement` を追加しました。
  - `promotion rule` に `causal-bridge statement when local animal causality and human proxy evidence are mixed` を追加しました。
  - 参考文献に `Williamson 2025`, `Dewa 2025`, `Bukalo 2026` を追加しました。

- `github-wiki-export/human-proxy-composition.md`
  - 上記の central rule を export 側にも同期しました。
  - 参考文献タイトルを DOI の Crossref metadata で再確認し、`Learning-associated astrocyte ensembles regulate memory recall` と `The astrocytic ensemble acts as a multiday trace to stabilize memory` に正規化しました。

- `wbe_101.md`
  - 既存の `causal-observability-asymmetry` note から、今回追加した `human-proxy-composition` の causal bridge 節へ誘導するリンクを追加しました。

- `verification.md`
  - 既存の addendum から、今回追加した `human-proxy-composition` の causal bridge 節へ誘導するリンクを追加しました。

## 今回止めた誤読

- `rodent causal astrocyte controller` が、そのまま `human measured controller` である
- `human astrocyte PET / CSF / efflux` が、そのまま `causal controller identity` を与える
- `causally important somewhere + human proxy somewhere` が、そのまま `same controller measured in humans` へ昇格できる
- `composition page` では bridge assumption を省略してよい

## 外部依存タスク

- なし
  - 今回の修正は repo 内の本文、export、導線、build、push までで完結できます。

## 参考文献

1. Williamson MR, Kwon W, Woo J, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-024-08170-w
2. Dewa K, Kaseda K, Kuwahara A, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
3. Bukalo O, O'Sullivan R, Tanisumi Y, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
4. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
5. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263255
6. Hirschler L, Runderkamp BA, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
