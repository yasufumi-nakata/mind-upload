# Site Deepening Audit (2026-03-25, landing page transcription / chromatin front door)

## 対象

- 主対象: `index.md`
- 同期対象: `summary_booklet.md`
- 調査方法: 公開中の `https://mind-upload.com/` を web で確認し、ローカル原稿と突き合わせました
- 範囲: 技術・自然科学のみ

## 今回この箇所を選んだ理由

- 2026-03-25 JST 時点で、公開トップページにはすでに
  - `intrinsic excitability`
  - `SV2A / synaptic-density PET`
  - `myelin`
  - `bioenergetic`
  - `ECM / PNN`
  - `post-transcriptional RNA`
  - `phospho-signaling`
  - `proteostasis`
  - `cargo`
  - `ionic`
  などの front-door stop line が並んでおりました。
- しかし `transcription / chromatin` だけは、`still-missing whole-brain in vivo routes` の一文には現れる一方で、専用の note-box がなく、`inferential object の分解` が入口では見えておりませんでした。
- これは site-wide で弱いです。なぜなら下流ページではすでに
  - `allocation eligibility`
  - `time-windowed response map`
  - `persistent stabilization cascade`
  - `locus-specific causal editability`
  を別物として扱っているのに、最初の入口だけが `transcriptomic evidence` を一塊に読ませうるからです。

## 根拠付き批判

### 1. landing page だけが `transcription / chromatin` を one-bucket に近い形で通しておりました

- 観察:
  - 公開トップページは `post-transcriptional RNA` には専用 stop line を置いていました。
  - その一方で `transcription / chromatin` は、human observability の説明で「まだ whole-brain route がない」と述べるだけで、`何が別 object なのか` が入口では見えませんでした。
- 批判:
  - これでは読者が
    - `cell atlas がある`
    - `DEG list がある`
    - `spatial transcriptomics がある`
    を、`current plasticity-competent program がかなり固定された` と過読しやすくなります。
  - 入口ページは誤読が最も固定されやすい場所なので、ここでの omission は軽微ではありません。

### 2. 一次資料は `transcription / chromatin` を単一クラスとして扱っておりません

- 根拠:
  - Santoni et al. (2024) は、`memory trace formation` に先立つ `neuronal eligibility` を chromatin plasticity と結び付けました。
  - Traunmüller et al. (2025) は、新奇環境曝露後の hippocampus で `temporally defined` かつ `region-specific` な chromatin accessibility / gene-expression 変化を示しました。
  - Terceros et al. (2026) は、memory stabilization に関わる `thalamocortical transcriptional gates` を提示しました。
  - Coda et al. (2025) は、defined engram cells における `locus-specific` epigenetic editing が memory expression を因果的に操作しうることを示しました。
- 批判:
  - したがって `transcription / chromatin evidence` は少なくとも
    - 学習前の割当可能性
    - 学習後の時系列反応地図
    - 安定化カスケード
    - 座位特異的な因果編集可能性
    の別 object に分ける必要があります。
  - これを入口で分けないまま `RNA note はあるが transcription note はない` 状態にしておくのは、技術的停止線として粗すぎました。

### 3. transcriptomic memory claim は内容だけでなく統計単位でも崩れうるため、入口で stop line を置く価値が高いです

- 根拠:
  - Sun et al. (2024) は long-term memory に関する spatial / single-cell transcriptomic signature を提示しました。
  - これに対し Mukamel & Yu (2025) は `False positives in study of memory-related gene expression` として、解析と統計の扱いに批判を加えました。
  - Sun et al. (2025) は reply を返しており、この論点が `単にシグネチャが見えたか` では終わらないことを示しています。
  - Zimmerman et al. (2021) は single-cell study における pseudoreplication が type I error を膨らませることを体系的に示しました。
- 批判:
  - したがって、memory-related transcriptomic signature は `どの生物学を見たか` だけでなく、`どの統計単位で立っているか` でも重みが変わります。
  - この stop line を下流の wiki にだけ置き、landing page では沈めたままにするのは弱いです。

### 4. site-wide rule との整合性を landing page が落としていました

- 観察:
  - `wbe_101.md`、`verification.md`、`wiki/homeostatic-plasticity-and-maintenance-state.md` では、すでに transcription / chromatin の route-card language が導入されていました。
  - しかし landing page は、その site-wide rule を front door に再掲しておりませんでした。
- 批判:
  - これは public-spec inconsistency です。
  - 厳しい規律は、最初に見るページほど見える形で置く必要があります。

## 今回実行した変更

- `index.md`
  - `page_highlights` に `transcription / chromatin evidence is not one class` を追加しました。
  - hidden-state family の要約に `activity-dependent transcription / chromatin state` と `post-transcriptional RNA-state` を明示的に追加しました。
  - `known_points` に
    - transcription / chromatin を distinct hidden-state family として読む規則
    - memory-related single-cell / spatial transcriptomic claim が animal-level independence と multiple-comparison handling に敏感である点
    を追加しました。
  - front-door に `If You Are Treating Transcription / Chromatin Evidence As One Solved Row` note-box を新設しました。
  - 同 note では
    - allocation eligibility
    - time-resolved response
    - stabilization cascade
    - locus-specific editability
    - transcriptomic-signature interpretation の統計依存性
    を 1 段落で明示し、`Wiki: transcription / chromatin route card` へ導線を付けました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成し、landing page の front matter 変更を冊子へ同期しました。

## 今回修正しないもの

- 哲学・法学・personhood の議論
- `issue.md` の再確認
- 新しい wiki 追加
  - 今回の問題は新ページ不足ではなく、front door での停止線欠落でした

## 外部依存で保留

- なし
  - 今回の作業は、このリポジトリ内の文書修正・冊子再生成・検証・push までで完結できます。

## 参考文献 / 公式ソース

1. Santoni G, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024.
   - https://doi.org/10.1126/science.adg9982
2. Traunmüller L, et al. Novel environment exposure drives temporally defined and region-specific chromatin accessibility and gene expression changes in the hippocampus. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-63029-6
3. Coda DM, Watt L, Glauser L, et al. Cell-type- and locus-specific epigenetic editing of memory expression. *Nature Genetics*. 2025;57:2661-2668.
   - https://doi.org/10.1038/s41588-025-02368-y
4. Terceros Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-09774-6
5. Sun W, Liu Z, Jiang X, et al. Spatial transcriptomics reveal neuron-astrocyte synergy in long-term memory. *Nature*. 2024;627:374-381.
   - https://doi.org/10.1038/s41586-023-07011-6
6. Mukamel EA, Yu X. False positives in study of memory-related gene expression. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08988-y
7. Sun W, Liu Z, Jiang X, et al. Reply to: False positives in study of memory-related gene expression. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08989-x
8. Zimmerman KD, Espeland MA, Langefeld CD. A practical solution to pseudoreplication bias in single-cell studies. *Nature Communications*. 2021;12:738.
   - https://doi.org/10.1038/s41467-021-21038-1
