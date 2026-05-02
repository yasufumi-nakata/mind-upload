# Wiki:「知っていること・知らないこと」の読み方

> 主張と留保の境界を調整して情報ポータルとして読む
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: 読み取りステータスと範囲

## このページの役割
このページは、Mind-Upload 公開ページの「現在わかっていること」「まだわかっていないこと」「このページで言えること/言えないこと」を誤読しないための補助ガイドです。情報ポータルとして、公開ページがまず主張できることと留保すべきことをどう示すのかを読み取るために使います。

## 正確性に関する注記
この記事では、公開ページを読む方法について説明します。個々の理論やテクニックの信頼性を確認するには、必ず元のページのテキストと証拠に戻ってください。

## 公開ページへ戻る
- [スタートページ](https://mind-upload.com)
- [検証プラットフォーム](https://mind-upload.com/verification.html)
- [パブリック コンテンツ統合ハブ](https://mind-upload.com/content_hub.html)

## 関連 Wiki ページ
- [Wiki: 公開ページを読むためのガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - これは、どの公開ページから読むかを事前に決めたい人向けです。
- [Wiki: 部分解決/探索段階/未開発の見方](https://github.com/yasufumi-nakata/mind-upload/wiki/progress-labels-and-open-problem-status) - 進捗ラベルの意味を詳しく知りたい方向けです。
- [Wiki: 社内および外部の依存関係について最初に行うべきこと](https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies) - これは、現在実行できる変更から外部の依存関係を分離する方法を詳しく知りたい人向けです。

## 現在わかっていること
- 公開ページは、あなたの主張の強さと留保の範囲を示す情報ポータルとして設計されています。
- 「現在わかっていること」とは、そのページの範囲内で比較的強く言えることを指します。
- 「まだわかっていないこと」と「外部依存関係」を分離することで、過度の期待や誤解を減らせます。

## まだわかっていないこと
- 今後、課題がどこまで「既知」に移行できるかは、研究開発の進展次第だ。
- L4 や L5 のような強力な主張には、依然として多くの未解決の問題があります。

---

<h2>公開ページには「肯定する場」と「保留する場」が分かれている</h2>
<p>
このサイトの公開ページは、いかなる主張をする場所でもありません。むしろ、読者が誤って強い結論に飛びつかないように、今比較的強く言えること、まだ言えないこと、このページの役割ではないことを分けています。
</p>

<h2>最初に 4 つのセクションをお読みください</h2>
<table>
<thead>
<tr>
<th>ディスプレイ</th>
<th></th>の読み方
<th>読み間違えやすい</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>現在わかっていること</strong></td>
<td>これはそのページの範囲内では比較的強く言えます。 </td>
<td>フィールド全体が完成したと読むのは無理があります。 </td>
</tr>
<tr>
<td><strong>まだわかっていないこと</strong></td>
<td>未解決の部分、条件不足、証拠不足、合意不足など。
<td>これを「不可能であることが証明された」と読むのは別の話です。 </td>
</tr>
<tr>
<td><strong>精度の仮定</strong></td>
<td>このページが主張しない内容とその防御範囲を示します。 </td>
<td>これは警告ではなく、境界線として読まれるべきです。 </td>
</tr>
<tr>
<td><strong>外部依存関係</strong></td>
<td>これらは、このリポジトリだけを使用して完了できないタスクまたは条件です。 </td>
<td>「今は何もできない」と読むのは間違いで、先に準備をしておけば大丈夫です。 </td>
</tr>
</tbody>
</table>

<h2>「知っています」は「すべて解決しました」という意味ではありません</h2>
<table>
<thead>
<tr>
<th>公開ページの言い方</th>
<th>実際の意味</th>
</tr>
</thead>
<tbody>
<tr>
<td>標準、共有インフラストラクチャ、評価、監査が必要</td>
<td>要件の整理が比較的安定していることを意味します。これは実装が完了したことを意味するものではありません。 </td>
</tr>
<tr>
<td>条件付き昇格はEEG</td>で作成可能
<td> 限られた範囲内で同等の進歩が可能であることを意味します。 WBE のすべてが証明された話ではありません。 </td>
</tr>
<tr>
<td>入り口ページで自分のアイデンティティや意識を主張しないでください</td>
<td>は玄関役ではないということです。それは不必要だという意味ではありません。 </td>
</tr>
</tbody>
</table>

<h2>「わからない」は「不可能」という意味ではない </h2>
<table>
<thead>
<tr>
<th>タイプ不明</th>
<th>不足は何ですか？</th>
<th>次に探す場所</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>証拠が不十分</strong></td>
<td>必要なデータ、比較条件、反証条件が欠落しています。 </td>
<td><a href="https://mind-upload.com/verification.html">検証</a></td>
</tr>
<tr>
<td><strong>条件未定</strong></td>
<td>前進するために何を満たさなければならないのか、何を保留するために満たさなければならないのかは不明です。 </td>
<td><a href="https://mind-upload.com/tech_roadmap.html">ロードマップ</a> / <a href="https://mind-upload.com/verification.html">検証</a></td>
</tr>
<tr>
<td><strong>コンセンサスの欠如</strong></td>
<td>アイデンティティやシステム設計などの問題については、分野を超えた合意がまだありません。 </td>
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a> / <a href="https://mind-upload.com/issue.html#external-collaboration">コラボレーション</a></td>
</tr>
<tr>
<td><strong>外部依存関係</strong></td>
<td>治験審査委員会、設備、契約、共同研究先等の外部条件が必要です。 </td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">社内生産と外部依存関係</a></td>
</tr>
</tbody>
</table>

<h2>ページ冒頭の使い方</h2>
<table>
<thead>
<tr>
<th>最初の要素</th>
<th></th>何に使うのですか
</tr>
</thead>
<tbody>
<tr>
<td><strong>ページの紹介</strong></td>
<td>ページの役割を確認してください。まず、理論的なテキストにするか、実践的な作業にするか、それとも運用上のハブにするかを決定します。 </td>
</tr>
<tr>
<td><strong>精度注記</strong></td>
<td>ページが意図的にノークレームをどの程度行っているかを確認してください。 </td>
</tr>
<tr>
<td><strong>既知 / 不明</strong></td>
<td>比較的安定した基盤と未解決の基盤を分離します。 </td>
</tr>
<tr>
<td><strong>wiki リンク</strong></td>
<td>そこで止まりがちな前提を学習ページで補足します。 </td>
</tr>
<tr>
<td><strong>おすすめページ</strong></td>
<td>そのページの後に戻る公開ページを決定します。 </td>
</tr>
</tbody>
</table>

<h2>よくある間違い</h2>

<h4>間違い</h4>
<ul>
<li><strong>完了レポートとして「知っています」を読む:</strong> ほとんどの場合、それは必要な条件や比較的安定した仮定を整理したものです。 </li>
<li><strong>「わかりません」を否定的証明として読む:</strong> 未解決または不十分な証拠は、不可能性の証明とは異なります。 </li>
<li><strong>装飾としての精度に関する注意事項を読む:</strong> これは実際には主張の境界を決定する重要な情報です。 </li>
<li><strong>外部依存関係を保留ボックスとして残す:</strong> まず、社内でできる準備を切り出す必要があります。 </li>
</ul>

<h2>次に戻る場所</h2>
<p>
公開ページの役割の違いに戻りたい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide">公開ページの見方ガイド</a>に戻ってください。進捗ラベルの詳しい意味については<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/progress-labels-and-open-problem-status">部分解、探索段階、未開発の見方</a>に戻ってください。外部依存関係の分離に戻る場合は、<a Use href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies"> 内部事前作業と外部依存関係 </a> に戻ります。
</p>
