# Wiki：読んだ内容を変更へつなぐ流れ

> 観察から、提案、実行、外部依存の切り分けまでを一本道で見る
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Reading to change workflow

## このページの役割
このページは、Mind-Upload のページを読んで得た気づきを、実際の変更や整理へつなぐための workflow ガイドです。新しい論文を見つけた、理論上の弱点に気づいた、提案の形が見えた、今すぐ直せる修正が分かった、外部依存が必要だと分かった、といった場面で、どのページへ戻して何を作るかを一本道で整理します。

## 正確さの前提
ここで示すのは workflow の整理です。個別の提案や論文の妥当性は、必ず元ページ本文と根拠へ戻って確認してください。

## 公開ページへ戻る
- [文献地図](https://mind-upload.com/research_harvest_50.html)
- [技術提案](https://mind-upload.com/issue.html#proposal-integration)
- [貢献ガイド](https://mind-upload.com/issue.html)

## 関連 Wiki
- [Wiki: 事実・仮説・提案・実行タスクの違い](https://github.com/yasufumi-nakata/mind-upload/wiki/facts-hypotheses-proposals-and-tasks) - ページごとの役割差を先に整理したい人向けです。
- [Wiki: 参加・協業ページのあとに進む5つの道](https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes) - 参加系ページのあとに次の1ページを決めたい人向けです。
- [Wiki: 新しい情報の置き場所を決める基本](https://github.com/yasufumi-nakata/mind-upload/wiki/content-placement-basics) - どこへ置くかをさらに詳しく見たい人向けです。

## いま分かっていること
- 読んだ内容をどの成果物へ変えるかを決めると、情報が散らばりにくくなります。
- 文献整理、理論整理、提案、実行タスク、外部依存では、戻るべきページが違います。
- 外部依存の話でも、先に内製できる準備物はかなりあります。

## まだ分かっていないこと
- どの気づきが最も大きな成果につながるかは、その時点の未解決問題や実装状況で変わります。
- 外部依存の話がどこまで具体的な連携へ進むかは、相手先や条件に依存します。

---

<h2>読むだけで終わらせないために、次の成果物を決めます</h2>
<p>
このサイトでは、読んで分かったことをそのまま放置しません。まず <strong>それが文献整理なのか</strong>、<strong>理論上の弱点なのか</strong>、<strong>提案へ上げる話なのか</strong>、<strong>今すぐ切れる修正なのか</strong>、<strong>外部依存なのか</strong> を決めて、戻る先を固定します。
</p>

<h2>基本の流れ</h2>
<table>
<thead>
<tr>
<th>読んで気づいたこと</th>
<th>戻る先</th>
<th>そこで作るもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>新しい論文や根拠を見つけた</strong></td>
<td><a href="https://mind-upload.com/research_harvest_50.html">Research Harvest</a> / <a href="https://mind-upload.com/mind_uploading_papers.html">Papers</a></td>
<td>未解決問題への接続、根拠例、広いアーカイブ登録。</td>
</tr>
<tr>
<td><strong>理論の弱点や前提差が見えた</strong></td>
<td><a href="https://mind-upload.com/perspective.html">Perspective</a> / <a href="https://mind-upload.com/perspective.html#design-principles">Idea</a></td>
<td>限界整理、理論フレーム、設計原理の見直し。</td>
</tr>
<tr>
<td><strong>進む方向や方針が見えた</strong></td>
<td><a href="https://mind-upload.com/issue.html#proposal-integration">Proposals</a></td>
<td>提案、ストリーム整理、根拠リンク。</td>
</tr>
<tr>
<td><strong>今このリポジトリで直せる変更が見えた</strong></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a></td>
<td>実行タスク、前進条件、反証条件、修正位置。</td>
</tr>
<tr>
<td><strong>外部連携や制度が必要だと分かった</strong></td>
<td><a href="https://mind-upload.com/issue.html#external-collaboration">Collaborations</a></td>
<td>外部依存タスク、内製準備物、最小成果物。</td>
</tr>
</tbody>
</table>

<h2>どこへ戻すかの見分け方</h2>
<table>
<thead>
<tr>
<th>見分けたいこと</th>
<th>判断のしかた</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>文献整理か、提案か</strong></td>
<td>「何が分かったか」を整理するなら文献整理、「どう進めるか」を示すなら提案です。</td>
</tr>
<tr>
<td><strong>提案か、Issue か</strong></td>
<td>今このリポジトリで直せる変更に落ちるなら Issue、まだ方向整理の段階なら提案です。</td>
</tr>
<tr>
<td><strong>Issue か、Collaborations か</strong></td>
<td>相手先や IRB、機材、契約が要るなら Collaborations、それなしで切れるなら Issue です。</td>
</tr>
<tr>
<td><strong>公開ページか、wiki か</strong></td>
<td>要点と既知/未知を示すなら公開ページ、初歩から学ぶ説明なら wiki です。</td>
</tr>
</tbody>
</table>

<h2>よくある具体例</h2>
<table>
<thead>
<tr>
<th>場面</th>
<th>戻る先</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>新しい EEG 論文を見つけた</strong></td>
<td><a href="https://mind-upload.com/research_harvest_50.html">Research Harvest</a></td>
<td>まずどの U に効くかを整理しないと、提案や Issue へ散らばりやすいためです。</td>
</tr>
<tr>
<td><strong>Perspective を読んで、理論の弱点が気になった</strong></td>
<td><a href="https://mind-upload.com/perspective.html">Perspective</a> / <a href="https://mind-upload.com/perspective.html#design-principles">Idea</a></td>
<td>先に理論整理として残した方が、提案や実装の前提がぶれにくいためです。</td>
</tr>
<tr>
<td><strong>Proposals を読んで、今すぐ直せる不足が見えた</strong></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a></td>
<td>提案整理から、具体的な修正と完了条件へ落とす段階だからです。</td>
</tr>
<tr>
<td><strong>Issue を書こうとしたら外部依存が大きかった</strong></td>
<td><a href="https://mind-upload.com/issue.html#external-collaboration">Collaborations</a></td>
<td>内製変更と外部依存を分ける必要があるためです。</td>
</tr>
</tbody>
</table>

<h2>よくある迷い方</h2>

<h4>Mistake</h4>
<ul>
<li><strong>面白い文献をそのまま提案にする：</strong> 先に未解決問題や論点整理へ戻した方が安全です。</li>
<li><strong>提案ページに今すぐの修正まで書き込む：</strong> 実行タスクは Issue に切り出す方が完了条件を持てます。</li>
<li><strong>外部依存を Issue に混ぜる：</strong> 内製変更と相手待ちを分けないと止まりやすいです。</li>
<li><strong>公開ページに背景説明を全部足す：</strong> 初歩からの詳説は wiki に寄せた方が入口が保てます。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
ページの役割差へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/facts-hypotheses-proposals-and-tasks">事実・仮説・提案・実行タスクの違い</a>、置き場所の判断へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/content-placement-basics">新しい情報の置き場所を決める基本</a>、参加の次ページ導線へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes">参加・協業ページのあとに進む5つの道</a> をご利用ください。
</p>
