# Wiki：はじめての Issue の書き方

> 止まった場所を、そのまま価値ある作業に変えるための基本
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Issue writing basics

## このページの役割
このページは、Mind-Upload で初めて Issue を書く人向けの補助教材です。完全な解決策を持っていなくても、どこで止まったか、何が不足か、何が足されれば前進かを分けて書ければ、価値の高い Issue になります。

## 正確さの前提
ここで紹介するのは、Issue を実行可能な変更へ変えるための最低限です。個別の技術的主張や外部連携条件は、必ず元ページへ戻って確認してください。

## 公開ページへ戻る
- [貢献ガイド](https://mind-upload.com/issue.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [公開コンテンツ統合ハブ](https://mind-upload.com/content_hub.html)

## 関連 Wiki
- [Wiki: 参加・協業ページのあとに進む5つの道](https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes) - Issue のあとにどのページへ進むかも一緒に見たい人向けです。
- [Wiki: 内製で先にやることと外部依存](https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies) - Issue の中に外部依存が混ざったときの切り分けを補います。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 前進条件や反証条件をなぜ先に置くかを補います。

## いま分かっていること
- 完全な解決案がなくても、止まった位置と不足の種類が分かれば十分に価値ある Issue になります。
- 前進条件と反証条件があると、Issue の終わり方が明確になります。
- 外部依存の話は、今すぐ実行する変更と切り分ける必要があります。

## まだ分かっていないこと
- どの Issue が最終的に大きな成果へつながるかは、その時点の研究状況で変わります。
- 外部依存タスクの成立時期は、この wiki だけでは決まりません。

---

<h2>Issue は「完全な答え」ではなく「動ける問い」です</h2>
<p>
Issue は、完成した提案書である必要はありません。むしろ大事なのは、<strong>どこで止まったか</strong>、<strong>何が不足しているか</strong>、<strong>何が足されれば前進か</strong>を、他の人が追える形で残すことです。
</p>

<h2>まず知っておきたい考え方</h2>
<table>
<thead>
<tr>
<th>誤解しやすい考え</th>
<th>このサイトでの考え方</th>
</tr>
</thead>
<tbody>
<tr>
<td>解決策が全部分からないと Issue を書けない</td>
<td>解決策がなくても、止まった場所と不足の種類が分かれば Issue にできます。</td>
</tr>
<tr>
<td>大きい提案ほど価値がある</td>
<td>小さくても、修正位置と完了条件が明確な Issue の方が動きやすいです。</td>
</tr>
<tr>
<td>外部依存も同じ Issue に全部書けばよい</td>
<td>今このリポジトリで実行する変更と、外部依存タスクは分けて書きます。</td>
</tr>
<tr>
<td>「分かりにくい」と書けば十分</td>
<td>どのページのどの言葉や段落で止まったかを具体化すると修正しやすくなります。</td>
</tr>
</tbody>
</table>

<h2>よくある止まり方を Issue に変える</h2>
<table>
<thead>
<tr>
<th>止まり方</th>
<th>Issue に最低限書くこと</th>
<th>次に戻るページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>用語が分からない</strong></td>
<td>止まった用語、ページ位置、どう誤読したか、1 段落で欲しい説明。</td>
<td><a href="https://mind-upload.com/glossary.html">Glossary</a> / <a href="https://mind-upload.com/content_hub.html">Content Hub</a></td>
</tr>
<tr>
<td><strong>主張が強いのに条件が見えない</strong></td>
<td>対象の主張、足りない条件、何が足されれば前進か、何が出たら保留か。</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a></td>
</tr>
<tr>
<td><strong>文献を見つけたが、どこへ戻すか分からない</strong></td>
<td>文献名、何に効くと思ったか、未解決問題か提案か Issue かの候補。</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-to-action-route">文献から実装・参加へ戻る一本道</a></td>
</tr>
<tr>
<td><strong>実験や IRB が必要そうで止まる</strong></td>
<td>今ここで作れる準備物、外部依存になる項目、完了判定を分けて書く。</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製で先にやることと外部依存</a></td>
</tr>
<tr>
<td><strong>どこへ追記すべきか分からない</strong></td>
<td>追加したい情報の種類、候補ページ、なぜそこだと思うか。</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/content-placement-basics">新しい情報の置き場所を決める基本</a> / <a href="https://mind-upload.com/content_hub.html">Content Hub</a></td>
</tr>
</tbody>
</table>

<h2>最低限のテンプレ</h2>
<table>
<thead>
<tr>
<th>項目</th>
<th>短くても入れたい内容</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>どこで止まったか</strong></td>
<td>対象ページ、節、段落、用語、表など、修正位置が分かる情報。</td>
</tr>
<tr>
<td><strong>何が不足しているか</strong></td>
<td>定義不足、導線不足、根拠不足、状態ラベル不明、外部依存の混同などの種類。</td>
</tr>
<tr>
<td><strong>今回実行する変更</strong></td>
<td>今このリポジトリで実施できる修正を 1 つに絞って書きます。</td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td>IRB、機材、契約、共同研究合意など、こちらだけでは完了できないもの。</td>
</tr>
<tr>
<td><strong>前進条件</strong></td>
<td>何が足されれば「改善した」と言えるか。</td>
</tr>
<tr>
<td><strong>反証条件</strong></td>
<td>何が確認されたら、その修正方針や主張を採らないか。</td>
</tr>
</tbody>
</table>

<h2>弱い Issue と強い Issue の違い</h2>
<table>
<thead>
<tr>
<th>弱い書き方</th>
<th>強い書き方</th>
</tr>
</thead>
<tbody>
<tr>
<td>「このページは分かりにくいです」</td>
<td>「`verification.html` の冒頭で `benchmark` の意味が分からず止まりました。1 段落の定義か wiki への導線があると改善と判定できます。」</td>
</tr>
<tr>
<td>「EEG だけでは無理だと思います」</td>
<td>「`eeg_101.html` に、EEG 単体で言えることと他モダリティが要ることの対比表を追加すると、誤読が減ると考えます。」</td>
</tr>
<tr>
<td>「共同研究したいです」</td>
<td>「`issue.html#external-collaboration` で、OpenNeuro 連携前に必要な 1 ページ要約と最小成果物を明示すると、外部依存の前段が具体化します。」</td>
</tr>
</tbody>
</table>

<h2>よくある失敗</h2>

<h4>Mistake</h4>
<ul>
<li><strong>問題を大きくしすぎる：</strong> まず 1 ページ、1 用語、1 導線のように最小単位へ切る方が動きます。</li>
<li><strong>外部依存を完了条件に入れてしまう：</strong> その場で直せることと、相手先依存を分けてください。</li>
<li><strong>前進条件だけで反証条件がない：</strong> 何が出たらその修正方針を採らないかも必要です。</li>
<li><strong>置き場が未定のまま提案する：</strong> Content Hub で統合先を確認すると、重複が減ります。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
Issue の入口へ戻るなら <a href="https://mind-upload.com/issue.html">貢献ガイド</a>、参加ページ読後の分岐へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes">参加・協業ページのあとに進む5つの道</a>、条件設計の前提へ戻るなら <a href="https://mind-upload.com/verification.html">Verification</a> をご利用ください。
</p>
