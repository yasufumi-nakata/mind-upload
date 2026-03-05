# Wiki：新しい情報の置き場所を決める基本

> 『何を書くか』の前に、『どこへ置くか』を決めるための基本
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Content placement basics

## このページの役割
このページは、Mind-Upload に新しい情報を足すときに、どこへ置くべきかを初歩から整理する補助教材です。公開ページは情報ポータル、wiki は学習用の詳説、Issue は実行する変更、Collaborations は外部依存の整理、運用領域は中間成果という役割差を、例と一緒に確認できます。

## 正確さの前提
ここで示すのは置き場所の基本です。個別の主張の正しさや採否は、必ず元ページの本文と根拠へ戻って判断してください。

## 公開ページへ戻る
- [公開コンテンツ統合ハブ](https://mind-upload.com/content_hub.html)
- [貢献ガイド](https://mind-upload.com/issue.html)
- [協業候補](https://mind-upload.com/collaborations.html)

## 関連 Wiki
- [Wiki: 公開ページの読み分けガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - 公開ページどうしの役割差を先に見たい人向けです。
- [Wiki: 参加・協業ページのあとに進む5つの道](https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes) - 置き場所の判断後に、次の作業へ進みたい人向けです。
- [Wiki: はじめての Issue の書き方](https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics) - 置き場所が Issue になったときの書き方を補います。

## いま分かっていること
- 置き場所を先に決めると、情報の重複や導線の散逸が減ります。
- 公開ページと wiki を分けると、入口の見やすさと説明の厚みを両立しやすいです。
- 外部依存タスクは、今この場で実行する変更とは分けて管理する必要があります。

## まだ分かっていないこと
- どの論点が将来独立ページになるかは、蓄積量と読者需要で変わります。
- 一部の話題は複数ページにまたがるため、最終的な統合先は今後も調整されます。

---

<h2>最初に決めるのは「内容」より「置き場所」です</h2>
<p>
新しい情報を見つけたとき、すぐ本文を書き始めると重複や迷子が増えます。先に<strong>その情報の役割</strong>を決めると、公開ページをポータルとして保ちつつ、必要な詳説を wiki へ増やしやすくなります。
</p>

<h2>まずは 5 つの置き場所を分ける</h2>
<table>
<thead>
<tr>
<th>置き場所</th>
<th>何を置くか</th>
<th>置かない方がよいもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>公開ページ</strong></td>
<td>いま分かっていること、まだ分かっていないこと、次に読む場所、判断表。</td>
<td>背景知識を最初から最後まで教える長い教材。</td>
</tr>
<tr>
<td><strong>wiki</strong></td>
<td>初歩の説明、似た言葉の違い、ページの読み方、学習用の補助教材。</td>
<td>最新の運用判断や実装状況の一次置き場。</td>
</tr>
<tr>
<td><strong>Issue</strong></td>
<td>今このリポジトリで実行する変更、修正位置、前進条件、反証条件。</td>
<td>外部依存を含む大きな計画を、完了済みのように書くこと。</td>
</tr>
<tr>
<td><strong>Collaborations</strong></td>
<td>共同研究、標準化提案、制度連携など、相手先や外部条件が必要な話。</td>
<td>こちらだけで完了できる小さな修正の記録。</td>
</tr>
<tr>
<td><strong>運用領域</strong></td>
<td>未整理メモ、中間成果、CSV、機械処理結果、監査ログ。</td>
<td>そのまま読者向け本文として見せること。</td>
</tr>
</tbody>
</table>

<h2>その情報が何に答えるかで置き場所を決める</h2>
<table>
<thead>
<tr>
<th>その情報が答える問い</th>
<th>まず置く先</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>この分野で、いま何が分かっていて何が未解決か</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a>、<a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a> などの公開ページ</td>
<td>公開ページは、判断の入口として既知/未知を示す役割だからです。</td>
</tr>
<tr>
<td><strong>用語や背景知識を初歩から説明したい</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki">wiki</a></td>
<td>学習用の厚みは wiki に寄せた方が、入口ページが見やすく保てるからです。</td>
</tr>
<tr>
<td><strong>今すぐ直せる修正を切りたい</strong></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a></td>
<td>実行可能な変更として、完了条件まで含めて管理できるからです。</td>
</tr>
<tr>
<td><strong>共同研究や標準化の候補を整理したい</strong></td>
<td><a href="https://mind-upload.com/collaborations.html">Collaborations</a></td>
<td>外部依存の話を、内製変更と混ぜないためです。</td>
</tr>
<tr>
<td><strong>まだ整理し切れていない生データやメモを残したい</strong></td>
<td>運用領域</td>
<td>統合先が決まる前の断片を、公開本文へ直接流し込まないためです。</td>
</tr>
</tbody>
</table>

<h2>よくあるケースの置き方</h2>
<table>
<thead>
<tr>
<th>見つけたもの</th>
<th>まず置く先</th>
<th>補助で見るページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>中学生向けに噛み砕いた説明</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki">wiki</a></td>
<td><a href="https://mind-upload.com/content_hub.html">Content Hub</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide">公開ページの読み分けガイド</a></td>
</tr>
<tr>
<td><strong>既存の主張に足りない条件や注意書き</strong></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a> から対象公開ページへ</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics">はじめての Issue の書き方</a></td>
</tr>
<tr>
<td><strong>新しい論文やデータセット</strong></td>
<td><a href="https://mind-upload.com/research_harvest_50.html">Research Harvest</a> か <a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-to-action-route">文献から実装・参加へ戻る一本道</a></td>
</tr>
<tr>
<td><strong>共同研究先へ渡す 1 ページ要約</strong></td>
<td><a href="https://mind-upload.com/collaborations.html">Collaborations</a> に接続する準備物</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製で先にやることと外部依存</a></td>
</tr>
<tr>
<td><strong>まだ真偽や置き場が決まっていない断片メモ</strong></td>
<td>運用領域</td>
<td><a href="https://mind-upload.com/content_hub.html">Content Hub</a></td>
</tr>
</tbody>
</table>

<h2>よくある失敗</h2>

<h4>Mistake</h4>
<ul>
<li><strong>とりあえず新規ページを作る：</strong> まず既存ページに統合できるかを確認してください。</li>
<li><strong>公開ページを教科書化する：</strong> 詳説は wiki へ寄せた方が入口が見やすくなります。</li>
<li><strong>Issue と Collaborations を混ぜる：</strong> 今できる変更と外部依存を分けてください。</li>
<li><strong>未整理メモをそのまま公開する：</strong> まず運用領域で整理してから統合先を決める方が安全です。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
統合先の一覧へ戻るなら <a href="https://mind-upload.com/content_hub.html">公開コンテンツ統合ハブ</a>、参加導線へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes">参加・協業ページのあとに進む5つの道</a>、Issue に落とし込む書き方へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics">はじめての Issue の書き方</a> をご利用ください。
</p>
