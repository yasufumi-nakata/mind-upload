# Wiki: 最初の問題の書き方

> 停滞している場所を価値ある仕事に変えるための基本
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: 問題の書き方の基本

## このページの役割
このページは、初めて Mind-Upload で問題を作成する人のための補足資料です。たとえ完全な解決策がなかったとしても、どこで立ち止まったのか、何が足りていないのか、次に進むために何を追加できるのかを書くことができれば、価値のある課題となります。

## 正確性に関する注記
ここで紹介するのは、問題を実行可能な変化に変えるために最低限必要なことです。個別の技術主張や外部連携条件等につきましては、必ず元のページに戻ってご確認ください。

## 公開ページへ戻る
- [貢献ガイド](https://mind-upload.com/issue.html)
- [検証ベース](https://mind-upload.com/verification.html)
- [パブリック コンテンツ統合ハブ](https://mind-upload.com/content_hub.html)

## 関連 Wiki ページ
- [Wiki: 参加/コラボレーション後にたどる 5 つの道筋ページ](https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes) - これは、問題が発生した後にどのページに移動したかを確認したい人向けです。
- [Wiki: 社内および外部の依存関係について最初に行うべきこと](https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies) - 問題に外部依存関係が混在している場合の分離を補います。
- [Wiki: 検証インフラストラクチャの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 事前条件と不確認条件が最初に配置される理由を説明します。

## 現在わかっていること
- たとえ完璧な解決策がなかったとしても、どこで止まっているのか、どのような欠陥があるのか​​がわかれば、取り組む価値のある課題となります。
- 賛成条件と反証条件によって、問題がどう終わるかが明確になります。
- 外部の依存関係を、これから加えようとする変更から分離する必要があります。

## まだわかっていないこと
- 最終的にどの課題が大きな成果につながるかは、その時の研究状況によって異なります。
- この Wiki だけでは、外部依存タスクがいつ確立されるかを決定することはできません。

---

<h2>問題は完全な答えではなく、感動的な質問</h2>
<p>
課題は完成した提案である必要はありません。むしろ重要なのは、どこで立ち止まったのか、何が足りないのか、そして他の人が見習えるように前進するために何を追加できるのかを記録に残すことです。
</p>

<h2>最初に知っておくべきこと</h2>
<table>
<thead>
<tr>
<th>誤解されやすい</th>
<th>このサイトの感想</th>
</tr>
</thead>
<tbody>
<tr>
<td>解決策全体を知らなければ問題を書くことはできません</td>
<td>解決策がない場合でも、問題がどこで停止し、どのようなタイプの欠陥であるかがわかっていれば、問題を作成できます。 </td>
</tr>
<tr>
<td>提案が大きければ大きいほど価値がある</td>
<td>小さな号であっても、修正位置や完了条件が明確であれば号を移動しやすくなります。 </td>
</tr>
<tr>
<td>すべての外部依存関係を同じ問題に記述することもできます</td>
<td>このリポジトリで実行する変更と外部依存タスクを別々に書き込みます。 </td>
</tr>
<tr>
<td>「わかりにくい」と書くだけで十分</td>
<td>どのページのどの単語や段落で止めたのかを明記しておくと修正がしやすくなります。 </td>
</tr>
</tbody>
</table>

<h2>よくある停止を問題に変える</h2>
<table>
<thead>
<tr>
<th>止め方</th>
<th>号に最低限書くべきこと</th>
<th>次のページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>用語がわかりません</strong></td>
<td>A 停止した用語、ページの場所、およびどのように誤読されたかを 1 段落で説明します。 </td>
<td><a href="https://mind-upload.com/glossary.html">用語集</a> / <a href="https://mind-upload.com/content_hub.html">コンテンツハブ</a></td>
</tr>
<tr>
<td><strong>強い主張はあるが、条件が見えない</strong></td>
<td>客観的な主張、不足している条件、前進するために何を追加すべきか、何を保留すべきか。 </td>
<td><a href="https://mind-upload.com/verification.html">検証</a> / <a href="https://mind-upload.com/tech_roadmap.html">ロードマップ</a></td>
</tr>
<tr>
<td><strong>ドキュメントを見つけましたが、どこに戻せばよいかわかりません</strong></td>
<td>ドキュメントのタイトル、それが効果的であると考えたもの、およびそれが未解決の問題、提案、または課題であるかどうかの提案。 </td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-to-action-route">文献から実装および参加までの直線的なパス</a></td>
</tr>
<tr>
<td><strong>実験または IRB が必要と思われるため停止します</strong></td>
<td>今ここでできる準備、外部に依存する項目、完了判断を分けて書く。 </td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">社内生産と外部依存関係</a></td>
</tr>
<tr>
<td><strong>どこに追加すればよいかわかりません</strong></td>
<td>追加したい情報、候補ページ、そしてなぜそこにあると思いますか? </td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/content-placement-basics">新しい情報を配置する場所を決める基本</a> / <a href="https://mind-upload.com/content_hub.html">コンテンツハブ</a></td>
</tr>
</tbody>
</table>

<h2>最小限のテンプレート</h2>
<table>
<thead>
<tr>
<th>アイテム</th>
<th>短くても盛り込みたい内容</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>どこで止まった</strong></td>
<td>対象ページ、節、段落、用語、表など、修正箇所を示す情報。</td>
</tr>
<tr>
<td><strong>足りないもの</strong></td>
<td> タイプには、不十分な定義、不十分なガイダンス、不十分な証拠、不明な状態ラベル、外部依存関係との混同が含まれます。 </td>
</tr>
<tr>
<td><strong>行われる変更</strong></td>
<td>I では、このリポジトリで実装できる 1 つの変更に焦点を当てます。 </td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td>IRB、設備、契約、共同研究契約など、当社だけでは完結できないもの。 </td>
</tr>
<tr>
<td><strong>アドバンス条件</strong></td>
<td>何を加えれば「さらに良くなる」？ </td>
</tr>
<tr>
<td><strong>反論条件</strong></td>
<td>何かが確認された場合、なぜ是正方針や申し立てを採用しないのでしょうか? </td>
</tr>
</tbody>
</table>

<h2>弱い銘柄と強い銘柄の違い</h2>
<table>
<thead>
<tr>
<th>弱い書き方</th>
<th>力強い書き方</th>
</tr>
</thead>
<tbody>
<tr>
<td>「このページはわかりにくいです」</td>
<td>「`verification.html`の冒頭の`benchmark`の意味が分からなかったのでやめました。一段落の定義かwikiへのリンクがあれば改善します。」</td>
</tr>
<tr>
<td>「脳波だけでは無理だと思います」</td>
<td>「脳波だけで言えることと他のモダリティが必要なことの比較表を『eeg_101.html』に追加することで誤解が減ると考えています。」</td>
</tr>
<tr>
<td>「共同研究をしたいのですが」</td>
<td>「`issue.html#external-collaboration` で OpenNeuro コラボレーションの前に必要な 1 ページの概要と最小限の成果物を指定することで、外部依存関係の第 1 段階が具体化されます。」</td>
</tr>
</tbody>
</table>

<h2>よくある間違い</h2>

<h4>間違い</h4>
<ul>
<li><strong>問題を大きくしすぎる：</strong> 1ページ、1ターム、1指揮者などの最小単位に切り詰めたほうがよいでしょう。 </li>
<li><strong>外部依存関係を完了条件に含める:</strong> その場で修正できるものと他者への依存関係を分離する。 </li>
<li><strong>前進条件のみ、反対条件なし:</strong>何が起こるかを知っていて、是正方針を採用しないことも必要です。 </li>
<li><strong>特定の場所を指定しない提案:</strong> Content Hub で統合先を確認すると重複が減ります。 </li>
</ul>

<h2>次に戻る場所</h2>
<p>
課題入口に戻るには<a href="https://mind-upload.com/issue.html">Contribution Guide</a>、参加ページを読んでブランチに戻るには<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes">参加・連携後にたどる5つのパス</a>、条件設計の前提に戻るには<a href="https://mind-upload.com/verification.html">Verification</a>を使用します。
</p>
