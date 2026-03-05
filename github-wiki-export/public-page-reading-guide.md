# Wiki：公開ページの読み分けガイド

> 『どのページから入るか』を目的別に決めるための地図
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Reading guide

## このページの役割
このページは、Mind-Upload の公開ページどうしの役割差を整理する補助ページです。どれも同じ説明をしているわけではなく、全体設計、入門、実務、文献、参加導線で役割が分かれています。

## 正確さの前提
ここで扱うのはページの使い分けです。個別の理論や技術条件は、必ず各ページ本文へ戻って確認してください。

## 公開ページへ戻る
- [スタートページ](https://mind-upload.com)
- [検証基盤](https://mind-upload.com/verification.html)
- [公開コンテンツ統合ハブ](https://mind-upload.com/content_hub.html)

## 関連 Wiki
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 学習用 wiki 全体の入口へ戻れます。
- [Wiki: 公開ページ冒頭ブロックの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/page-header-reading-guide) - 各公開ページの上部に出る案内ブロックの読み方を整理します。
- [Wiki: 文献と証拠ページの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading) - 文献ページどうしの違いは別ページで詳しく扱います。
- [Wiki: 提案と状態ラベルの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading) - Issue や技術提案の状態ラベルは別ページで整理します。

## いま分かっていること
- 公開ページは、要点・既知/未知・次の導線を示す情報ポータルとして役割分担されています。
- Verification、Roadmap、Perspective は似て見えても、役割がかなり違います。
- WBE 101 や EEG 101 は、長文ページへ入る前の足場として読むと効果的です。

## まだ分かっていないこと
- 将来どの公開ページを独立拡張するかは、今後の情報量と読者需要で変わります。
- 一部のテーマは、今後 wiki 側へさらに補講を足す余地があります。

---

<div class="abstract-box">
<h2>まず5つに分ける</h2>
<p>
公開ページは、大きく分けると <strong>入口</strong>、<strong>設計図</strong>、<strong>入門</strong>、<strong>実務</strong>、<strong>文献と参加導線</strong> の 5 種類です。どの役割のページかを先に分けるだけで、読む順番がかなり安定します。
</p>
</div>

<div class="note-box">
<strong>さらに理論系だけ、実務系だけで絞りたいとき</strong>
<p>
設計図や入門の中でも <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/theory-pages-reading-guide">理論系ページの読み分けガイド</a> で WBE 101 / Perspective / Idea / Roadmap の違いを、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide">実務系ページの読み分けガイド</a> で Verification / Datasets / Hands-on / Casework / Proposals の違いをそれぞれ詳しく追えます。
</p>
</div>
<div class="note-box">
<strong>まず最初の30分の回り方だけ決めたいとき</strong>
<p>
全体像、理論、実務、文献、参加のどこから入るかで最初の 3〜4 ページだけ先に固定したい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/first-30-minutes-by-goal">目的別の最初の30分ルート</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>各公開ページの『分かっていること / 分かっていないこと』をどう読むか知りたいとき</strong>
<p>
ページ上部の既知/未知、正確さの前提、外部依存の意味をそろえて読みたい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/known-unknown-and-status-reading">『分かっていること / 分かっていないこと』の読み方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>公開ページの上部にある案内ブロックの順番で迷ったとき</strong>
<p>
公開ページには共通して「このページの読み方」「向いている人」「正確さの前提」「いま分かっていること」「wiki で基礎から確認する」があります。本文に入る前に何をどう見ればよいかを整理したい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/page-header-reading-guide">公開ページ冒頭ブロックの読み方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>Verificationを読んだあとにどこへ進むか迷ったとき</strong>
<p>
公開ページ全体の役割差は分かったが、Verification のあとに L0 実装、L2 検証、L3 閉ループ、L4 本人性のどこへ進むかを 1 枚で見たい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">Verificationのあとに進む4つの道</a> をご覧ください。
</p>
</div>

<section class="section" id="five-kinds">
<h2 class="section-title">公開ページの役割差</h2>
<table class="data-table">
<thead>
<tr>
<th>種類</th>
<th>主なページ</th>
<th>何を決めるページか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入口</strong></td>
<td>index</td>
<td>最初にどこから読むかを決めます。</td>
</tr>
<tr>
<td><strong>設計図</strong></td>
<td>verification / tech_roadmap / perspective / idea</td>
<td>何を前進と呼ぶか、何が未解決か、理論と実装をどう結ぶかを決めます。</td>
</tr>
<tr>
<td><strong>入門</strong></td>
<td>wbe_101 / eeg_101 / faq / glossary</td>
<td>長文ページへ入る前に、言葉と主張の強さをそろえます。</td>
</tr>
<tr>
<td><strong>実務</strong></td>
<td>datasets / hands_on</td>
<td>何で試し、どの最小ループを作るかを決めます。</td>
</tr>
<tr>
<td><strong>文献と参加導線</strong></td>
<td>research_harvest_50 / mind_uploading_papers / proposals / issue / collaborations / content_hub</td>
<td>根拠、提案、参加方法、更新先を決めます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="which-page">
<h2 class="section-title">この疑問なら、まずこのページ</h2>
<table class="data-table">
<thead>
<tr>
<th>いま知りたいこと</th>
<th>まず開くページ</th>
<th>次に行くページ</th>
</tr>
</thead>
<tbody>
<tr>
<td>このサイトは何を作るのか</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
<td><a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a> で依存関係を見ます。</td>
</tr>
<tr>
<td>WBE の話を短く理解したい</td>
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a></td>
<td><a href="https://mind-upload.com/faq.html">FAQ</a> や <a href="https://mind-upload.com/verification.html">Verification</a> へ進みます。</td>
</tr>
<tr>
<td>EEG で何が言えるかを知りたい</td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a></td>
<td><a href="https://mind-upload.com/datasets.html">Datasets</a> や <a href="https://mind-upload.com/hands_on.html">Hands-on</a> へ進みます。</td>
</tr>
<tr>
<td>理論と限界を長文で追いたい</td>
<td><a href="https://mind-upload.com/perspective.html">Perspective</a></td>
<td><a href="https://mind-upload.com/idea.html">Idea</a> と往復します。</td>
</tr>
<tr>
<td>公開データで手を動かしたい</td>
<td><a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td><a href="https://mind-upload.com/hands_on.html">Hands-on</a> で L0 を作ります。</td>
</tr>
<tr>
<td>理論系ページの中だけで最初の1枚を決めたい</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/theory-pages-reading-guide">理論系ページの読み分けガイド</a></td>
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a> / <a href="https://mind-upload.com/perspective.html">Perspective</a> / <a href="https://mind-upload.com/idea.html">Idea</a> へ戻ります。</td>
</tr>
<tr>
<td>実務系ページの中だけで最初の1枚を決めたい</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide">実務系ページの読み分けガイド</a></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://mind-upload.com/datasets.html">Datasets</a> / <a href="https://mind-upload.com/hands_on.html">Hands-on</a> へ戻ります。</td>
</tr>
<tr>
<td>文献の山をどう読むか知りたい</td>
<td><a href="https://mind-upload.com/research_harvest_50.html">Research Harvest</a></td>
<td><a href="https://mind-upload.com/mind_uploading_papers.html">Papers</a> や <a href="https://mind-upload.com/proposals.html">Proposals</a> へ戻ります。</td>
</tr>
<tr>
<td>何を更新し、どこへ書くかを決めたい</td>
<td><a href="https://mind-upload.com/content_hub.html">Content Hub</a></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a> や <a href="https://mind-upload.com/collaborations.html">Collaborations</a> を見ます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="similar-pages">
<h2 class="section-title">似て見えるページの違い</h2>
<table class="data-table">
<thead>
<tr>
<th>似て見える組</th>
<th>違いを一言で言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Verification / Roadmap</strong></td>
<td>Verification は勝利条件と公共財、Roadmap は問いの依存関係です。</td>
</tr>
<tr>
<td><strong>Perspective / Idea</strong></td>
<td>Perspective は理論と限界の長文ノート、Idea は設計原理を絞って見るページです。</td>
</tr>
<tr>
<td><strong>WBE 101 / FAQ</strong></td>
<td>WBE 101 はまとまった入門、FAQ は短い疑問の解消です。</td>
</tr>
<tr>
<td><strong>Datasets / Hands-on</strong></td>
<td>Datasets は入口データ選び、Hands-on は実際の最小ループ作成です。</td>
</tr>
<tr>
<td><strong>Research Harvest / Papers</strong></td>
<td>Research Harvest は未解決問題ごとの地図、Papers は広く拾う論文アーカイブです。</td>
</tr>
<tr>
<td><strong>Issue / Collaborations</strong></td>
<td>Issue は今この場で切れる作業、Collaborations は外部連携候補の整理です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある迷い方</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>いきなり Perspective から入る：</strong> 長文で全体像を失いやすいので、先に Verification か WBE 101 が安全です。</li>
<li><strong>Datasets だけ見て終える：</strong> 何を成果物として残すかは Hands-on や Verification で補う必要があります。</li>
<li><strong>FAQ だけで判断する：</strong> FAQ は入口なので、強い主張は必ず本文へ戻ります。</li>
<li><strong>Content Hub を本文ページとして読む：</strong> ここは更新先を決める運用ハブであり、理論本文ではありません。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
最初の入口へ戻るなら <a href="https://mind-upload.com">スタートページ</a>、学習用 wiki 全体へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki">Wiki Home</a>、更新先を決めたいなら <a href="https://mind-upload.com/content_hub.html">Content Hub</a> をご利用ください。
</p>
</section>
