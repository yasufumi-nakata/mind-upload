# Wiki：要約・原文・Issue履歴の使い分け

> 要約は入口、判断は元ソースに戻るという読み方をそろえる
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Summary vs source

## このページの役割
このページは、Mind-Upload の公開ページや wiki を『要約の入口』としてどう使うかを整理する補助ガイドです。全体像をつかむだけなら要約で十分な場面もありますが、根拠として使う、判断する、修正する、反論する場面では、原文、DOI、Issue 履歴、一次研究へ戻る必要があります。その境界をそろえて読むためのページです。

## 正確さの前提
ここで扱うのは読み方のルールです。個別の論文や提案の評価は、必ず元ページや元ソースを確認してください。

## 公開ページへ戻る
- [文献地図](https://mind-upload.com/research_harvest_50.html)
- [論文集](https://mind-upload.com/mind_uploading_papers.html)
- [技術提案](https://mind-upload.com/proposals.html)

## 関連 Wiki
- [Wiki: 文献と証拠ページの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading) - 文献系ページどうしの役割差を先に見たい人向けです。
- [Wiki: 文献のソース種別と状態ラベル](https://github.com/yasufumi-nakata/mind-upload/wiki/paper-source-types-and-evidence-status) - どのソース種別なら一次研究へ戻るべきかを補います。
- [Wiki: 提案と状態ラベルの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading) - 提案ページと Issue 履歴の関係を整理します。

## いま分かっていること
- 公開ページや wiki の多くは、まず全体像を掴むための要約入口として有効です。
- 根拠として使うとき、引用するとき、修正するときは、元ソースへ戻る必要があります。
- 文献アーカイブ、文献地図、提案整理、Issue 履歴では、戻るべき元ソースが異なります。

## まだ分かっていないこと
- どの文献や提案が最終的に中心根拠として残るかは、今後の精査で変わります。
- 一部の要約は今後さらに更新され、戻るべき元ソースも増える可能性があります。

---

<div class="abstract-box">
<h2>要約は入口であって、最終判定ではありません</h2>
<p>
このサイトの要約ページは便利ですが、それだけで最終判断を済ませるためのものではありません。<strong>全体像をつかむ</strong>段階では要約で十分なこともありますが、<strong>根拠として使う</strong>、<strong>修正する</strong>、<strong>反論する</strong> ときは、原文や履歴へ戻る必要があります。
</p>
</div>

<section class="section" id="when-summary-is-enough">
<h2 class="section-title">要約で止めてよい場面</h2>
<table class="data-table">
<thead>
<tr>
<th>やりたいこと</th>
<th>要約で十分な理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ページの役割を知りたい</strong></td>
<td>公開ページの page intro や accuracy note で、そのページの守備範囲を把握できるからです。</td>
</tr>
<tr>
<td><strong>どの論点があるかをざっと見たい</strong></td>
<td>Papers や Research Harvest の要約で、論点の位置と量を素早く掴めるからです。</td>
</tr>
<tr>
<td><strong>次に戻るページを決めたい</strong></td>
<td>wiki の route ページは、次の1ページを決めるための補助として作られているからです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="when-to-go-back">
<h2 class="section-title">必ず元ソースへ戻る場面</h2>
<table class="data-table">
<thead>
<tr>
<th>やりたいこと</th>
<th>戻る先</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>論文を根拠として引用したい</strong></td>
<td>DOI、原文アブストラクト、一次研究</td>
<td>要約では方法、評価、限界の細部が落ちるためです。</td>
</tr>
<tr>
<td><strong>提案の妥当性を判断したい</strong></td>
<td>原文節、Technical Proposal、Issue 履歴</td>
<td>統合サマリーだけでは、採否の文脈や議論の変遷が見えないためです。</td>
</tr>
<tr>
<td><strong>Issue を切りたい</strong></td>
<td>対象ページ本文、根拠リンク、必要なら原文論文</td>
<td>どこで止まったかを正確に特定する必要があるためです。</td>
</tr>
<tr>
<td><strong>反論や修正提案をしたい</strong></td>
<td>元ページ本文と参照元</td>
<td>要約だけでは、本当にその主張が書かれているか断定できないためです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="by-page-type">
<h2 class="section-title">ページごとに戻る先が違います</h2>
<table class="data-table">
<thead>
<tr>
<th>ページ</th>
<th>要約として使う部分</th>
<th>戻る先</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Papers</strong></td>
<td>年別一覧、和訳要約、5ポイント整理</td>
<td>DOI、Original Abstract、元論文</td>
</tr>
<tr>
<td><strong>Research Harvest</strong></td>
<td>U別マップ、現状ラベル、根拠例</td>
<td>個別論文、DOI、対応する U の原典根拠</td>
</tr>
<tr>
<td><strong>Proposals</strong></td>
<td>統合本文、状態ラベル、Issue 対応マトリクス</td>
<td>原文節、Technical Proposal 本文、Issue 履歴</td>
</tr>
<tr>
<td><strong>Issue</strong></td>
<td>状態表、根拠リンク、早見表</td>
<td>対象ページ本文、実装箇所、外部依存の整理元</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="reading-order">
<h2 class="section-title">迷ったときの読み順</h2>
<ol>
<li>要約で「何の話か」を特定します。</li>
<li>その話を根拠として使うかどうかを決めます。</li>
<li>根拠として使うなら、必ず原文、DOI、Issue 履歴へ戻ります。</li>
<li>修正や提案に使うなら、対象ページ本文まで戻って位置を特定します。</li>
</ol>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある誤読</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>要約の掲載を採択済みと読む：</strong> 要約掲載と最終評価は別です。</li>
<li><strong>Review や二次要約だけで一次根拠にする：</strong> 重要な場面では一次研究へ戻る必要があります。</li>
<li><strong>Issue の根拠リンクだけで修正場所を確定する：</strong> 対象ページ本文まで戻る方が安全です。</li>
<li><strong>Technical Proposal の統合本文だけで変更可否を決める：</strong> 元 Issue の議論や原文節も確認する必要があります。</li>
</ul>
</div>
</section>

<div class="note-box">
<strong>要約を読んだあとに、本当に次へ進めるか確認したいとき</strong>
<p>
元ソース確認まではしたが、まだ条件や修正位置が足りないのかを段階で見たい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/understanding-vs-action-readiness">『分かった』と『次に進める』の違い</a> をご覧ください。
</p>
</div>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
文献系ページの役割差へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading">文献と証拠ページの読み方</a>、提案ページの状態へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading">提案と状態ラベルの読み方</a>、論文から参加へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-to-action-route">文献から実装・参加へ戻る一本道</a> をご利用ください。
</p>
</section>
