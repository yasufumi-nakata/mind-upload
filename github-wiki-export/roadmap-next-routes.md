# Wiki：ロードマップのあとに進む5つの道

> 依存関係の地図を見たあと、次の1ページを迷わず決めるためのガイド
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Roadmap route

## このページの役割
このページは、技術ロードマップを読んだあとに、どの論点を次に深掘りするかを整理する補助ガイドです。計測へ戻るのか、再構成や因果推定へ進むのか、実装へ降りるのか、検証条件へ戻るのか、制度や協業まで見るのかで、次の1ページは変わります。

## 正確さの前提
ここで示すのはロードマップ読後の入口です。各ノードの正式な論点や到達条件は、必ずロードマップ本文で確認してください。

## 公開ページへ戻る
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [EEG入門](https://mind-upload.com/eeg_101.html)

## 関連 Wiki
- [Wiki: ロードマップの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-reading-guide) - Roadmap 自体の読み方に戻りたい人向けです。
- [Wiki: L0〜L5ごとの読み進め方](https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes) - 主張レベル側から導線を見たい人向けです。
- [Wiki: Verificationのあとに進む4つの道](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes) - V 系列へ進んだあとをさらに具体化したい人向けです。

## いま分かっていること
- 技術ロードマップは全体地図なので、そのままでは次の1ページが広すぎます。
- 計測、再構成、実装、検証、社会実装では、戻るべきページが違います。
- Roadmap 読後に路線を 1 本に絞ると、理解と作業が進めやすくなります。

## まだ分かっていないこと
- どの路線が最短で効くかは、今後のデータやベンチ整備で変わり得ます。
- V と D の最終条件は、依然として未解決部分を多く含みます。

---

<h2>地図の次に路線を決める</h2>
<p>
技術ロードマップは「全体像」をつかむには有効ですが、そのままだと次にどこへ進むかが広すぎます。ここでは、<strong>いま何を深掘りしたいか</strong>で 5 本の道に分けて、次の1ページを固定します。
</p>

<h2>ロードマップのあとに進む5つの道</h2>
<table>
<thead>
<tr>
<th>次に知りたいこと</th>
<th>次に開くページ</th>
<th>そこで分かること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>計測の限界から詰めたい</strong></td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a> / <a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td>M 系列の前提になる、何が測れて何が単体では足りないかを確認できます。</td>
</tr>
<tr>
<td><strong>再構成や因果推定を深掘りしたい</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://mind-upload.com/perspective.html">Perspective</a></td>
<td>R 系列がどこで評価や因果検証に接続するかを確認できます。</td>
</tr>
<tr>
<td><strong>実装やL0の作業へ降りたい</strong></td>
<td><a href="https://mind-upload.com/hands_on.html">Hands-on</a> / <a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td>I 系列へ進む前の最小ループと、入口データの選定を具体化できます。</td>
</tr>
<tr>
<td><strong>検証条件を中心に見たい</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">Verificationのあとに進む4つの道</a></td>
<td>V 系列の主張レベルと、次の実務・閉ループ・本人性の分岐を確認できます。</td>
</tr>
<tr>
<td><strong>制度や外部連携まで含めて見たい</strong></td>
<td><a href="https://mind-upload.com/collaborations.html">Collaborations</a> / <a href="https://mind-upload.com/issue.html">Issue</a></td>
<td>D 系列や外部依存の話を、今できる準備と切り分けながら確認できます。</td>
</tr>
</tbody>
</table>

<h2>なぜこの分け方なのか</h2>
<table>
<thead>
<tr>
<th>道</th>
<th>Roadmap のあとにそのページへ行く理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>計測</strong></td>
<td>M 系列は入力の限界を決めるため、計測の基礎を別ページで確認した方が誤読が減るからです。</td>
</tr>
<tr>
<td><strong>再構成</strong></td>
<td>R 系列は評価や因果検証と結びつくため、Verification や Perspective で補う必要があるからです。</td>
</tr>
<tr>
<td><strong>実装</strong></td>
<td>I 系列は机上の整理だけでなく、Hands-on や Datasets で具体化しないと進みにくいからです。</td>
</tr>
<tr>
<td><strong>検証</strong></td>
<td>V 系列は全体設計と主張レベルを一緒に見る必要があるため、Verification 側で深掘りする方が自然だからです。</td>
</tr>
<tr>
<td><strong>社会実装</strong></td>
<td>D 系列は制度と外部依存が大きいため、Issue や Collaborations で具体化した方が実務に落ちやすいからです。</td>
</tr>
</tbody>
</table>

<h2>途中で止まったときの補助 wiki</h2>
<table>
<thead>
<tr>
<th>止まる場所</th>
<th>戻るとよい wiki</th>
</tr>
</thead>
<tbody>
<tr>
<td>P/M/R/I/V/D の読み方自体で止まる</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-reading-guide">ロードマップの読み方</a></td>
</tr>
<tr>
<td>主張レベル側から見たい</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes">L0〜L5ごとの読み進め方</a></td>
</tr>
<tr>
<td>実務側へ降りる順番で止まる</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route">EEGからL0までの一本道</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">Verificationのあとに進む4つの道</a></td>
</tr>
<tr>
<td>理論側へ戻る順番で止まる</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/wbe-to-theory-route">WBE入門から理論を深掘る4ルート</a></td>
</tr>
<tr>
<td>外部依存や参加導線で止まる</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製で先にやることと外部依存</a></td>
</tr>
</tbody>
</table>

<h2>よくある迷い方</h2>

<h4>Mistake</h4>
<ul>
<li><strong>Roadmap を読んだだけで次の作業が決まった気になる：</strong> 実際には路線を 1 本に絞る必要があります。</li>
<li><strong>M と R を飛ばして I や V に進む：</strong> 入力や推定の限界が残ったまま強い主張へ進みやすくなります。</li>
<li><strong>D 系列を抽象論のままにする：</strong> Issue や Collaborations へ戻して準備物を切る方が実務的です。</li>
<li><strong>Verification へ行けば全部分かると思う：</strong> V 系列のあとも、L0、L3、L4 で次の分岐があります。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
Roadmap 本文へ戻るなら <a href="https://mind-upload.com/tech_roadmap.html">技術ロードマップ</a>、検証側へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、理論側の分岐へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/wbe-to-theory-route">WBE入門から理論を深掘る4ルート</a> をご利用ください。
</p>
