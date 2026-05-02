# Wiki: ID とコピーの問題

> 見た目は同じでも、同一人物かどうかは別問題です。
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: 初心者ガイド

## このページの役割
このページは、Mind-Uploadの議論でよく出てくる「`copying problem'' and `の真正性」を初期から整理したWikiです。哲学の固有名詞を覚える前に、なぜこの問題がテクノロジーから逃れられないのかを理解することを目指します。

## 正確性に関する注記
このページは分かりやすく解説しておりますが、その人物の身元について最終的な結論を導くページではありません。未解決のままであることを明確にします。

## 公開ページへ戻る
- [理論フレーム](https://mind-upload.com/perspective.html#design-principles)
- [WBE の概要](https://mind-upload.com/wbe_101.html)
- [検証プラットフォーム](https://mind-upload.com/verification.html)

## 関連 Wiki ページ
- [Wiki: WBE の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - 全体像からこの問題の位置を確認することができます。
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - L4 の ID 主張の強さを補います。
- [Wiki: アイデンティティ評価と連続性テスト](https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests) - 哲学的な問題を整理して、事前に登録したテスト設計に戻します。
- [ウィキホーム](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基本ページに戻ることができます。

## 現在わかっていること
- たとえ行動が似ていても、それだけではその人の同一性を確認することはできません。
- 複数のコピーが存在する状況では、どれが本人であるかは自動的には判断されません。
- したがって、Mind-Upload では、連続性をどのように検証するかは別の問題として扱います。

## まだわかっていないこと
- 2 人の人物が「同一人物」とみなされる条件については合意がありません。
- 心理的連続性を重視するか、因果的連続性を重視するか、現象的意識を重視するかによって結論は変わります。
- また、継続的な移行設計がアイデンティティを適切に保護するかどうかも証明されていません。

---

<h2>第一区別</h2>
<p>
たとえ他の人とまったく同じ話し方、同じ記憶、同じ反応をしたとしても、それだけで同じ人間であるとは限りません。 Mind-Upload では、この違いが曖昧になることを避けるために、<strong> パフォーマンス マッチング </strong> と <strong> アイデンティティ アサーション </strong> を異なるレベルとして扱います。
</p>

<h2>なぜ難しいのか</h2>
<table>
<thead>
<tr>
<th>質問</th>
<th>なぜ難しいのか</th>
</tr>
</thead>
<tbody>
<tr>
<td>もし同じ思い出を共有できるとしたら、それは私でしょうか?</td>
<td>記憶の再現と経験の連続性は同じではない可能性があるからです。 </td>
</tr>
<tr>
<td>1枚のみの場合はご本人様</td>
<td>を2つ作成した場合、同じロジックではどちらが本人であるかを判断することは困難です。 </td>
</tr>
<tr>
<td>少しずつ交換した方が安全ですか？</td>
<td>連続遷移は直感的には強そうですが、十分条件かどうかはまだわかりません。 </td>
</tr>
</tbody>
</table>

<h2>静的コピーと継続的移行の違い</h2>
<table>
<thead>
<tr>
<th>考える</th>
<th>注目すべき点</th>
<th>残りの質問</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>静的コピー</strong></td>
<td>ある時点の構造や情報をコピーすること。 </td>
<td>複数枚持っているとどれが本人か分からなくなります。 </td>
</tr>
<tr>
<td><strong>継続的移行</strong></td>
<td>プロセスと対話を中断することなく引き継ぎます。 </td>
<td>連続性がアイデンティティの十分条件であるかどうかはまだ証明されていません。 </td>
</tr>
</tbody>
</table>

<h2>エンジニアリングに戻り、何をテストしたいですか</h2>
<p>
この点を工学に戻しますと、単によく似ているかどうかだけを見るだけでは十分ではありません。事前に登録されたテストを通じて、記憶、価値観、学習履歴、状況の変化への対応の連続性を調べる必要があります。言い換えれば、哲学的な議論をそのまま放置するのではなく、</strong> のアイデンティティの主張を保留する原因となる失敗がどのようなものであるかを定義する方向に進みます。
</p>
<p>最初にテスト設計の概要を見たい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">Wiki: ID 評価と継続性テスト</a> が補足コースです。 </p>

<h4>次</h4>
<p>この問題を理論的なフレームとしてどのように扱うかをここで確認できます。 </p>
<a href="https://mind-upload.com/perspective.html#design-principles">理論フレームへ→</a>
