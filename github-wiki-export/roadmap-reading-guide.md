# Wiki: ロードマップの見方

> テクノロジーのロードマップを長いリストではなく依存関係マップとして読む
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-06 / Role: 読書ガイド

## このページの役割
このページは、技術ロードマップにおける P/M/R/I/V/D の意味と、どこから読めば迷わないかを説明する補足ページです。ロードマップ本文を改めてまとめるのではなく、「マップの読み方」そのものを整理します。

## 正確性に関する注記
このページは読書補助です。問題の正式なリストと現在の取り決めについては、必ず技術ロードマップの本文に戻ってください。

## 公開ページへ戻る
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [WBE の概要](https://mind-upload.com/wbe_101.html)
- [検証プラットフォーム](https://mind-upload.com/verification.html)

## 関連 Wiki ページ
- [Wiki: WBE の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - このマップが必要な理由の全体像を知りたい人向けです。
- [Wiki: 検証インフラストラクチャの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Vシリーズで直したいところを補完。
- [ウィキホーム](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基本ページに戻ることができます。

## 現在わかっていること
- Pは進捗の定義、Mは測定、Rは再構築、Iは実行、Vは検証、Dは社会実装です。
- 議論が強ければ強いほど、議論は後退し、前の層が組織化されていないほど、前に進むことが難しくなります。
- ロードマップは、結論をまとめたものではなく、依存関係のマップとして読むのが最善です。

## まだわかっていないこと
- どのルートが最短で最も効果的であるかは、将来データベンチが開発されるにつれて変わる可能性があります。
- VとDの最終条件には未解決の問題がまだ多く残っている。

---

<h2>まず一言で言うと</h2>
<p>
テクノロジーロードマップとは、将来のストーリーが崩壊する前に、最初に解決する必要があるものを示す地図です。長いリストのように見えますが、実際には「仮定→測定→見積もり→実装→検証→社会実装」という依存関係を表しています。
</p>

<strong>読み方を決めたら次のページも決めたい</strong>
<p>
ロードマップ上の記号の意味だけでなく、ロードマップを読んだ後に測定、再構成、実装、検証、社会実装のどこに進むべきか知りたい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-next-routes">、ロードマップ後にたどるべき5つの道筋</a>をご覧ください。
</p>

日常言語の<h2>P/M/R/I/V/D</h2>
<table>
<thead>
<tr>
<th>シンボル</th>
<th>何の質問ですか？</th>
<th>これが出たらどうなる</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
<td>私たちが成功と呼ぶもの</td>
<td>ゴールは設定されておらず、勝利条件は後から変更可能。 </td>
</tr>
<tr>
<td><strong>M</strong></td>
<td>何をどのくらいの精度で測定できるのか</td>
<td>そもそも入力に何が入っているのか分かりません。 </td>
</tr>
<tr>
<td><strong>R</strong></td>
<td>観察から何が推測できるか</td>
<td>測定された信号が必要以上に強い意味を持つように解釈されます。 </td>
</tr>
<tr>
<td><strong>I</strong></td>
<td>モデルの動かし方</td>
<td>机上では良く見えても、実際にはうまくいかない場合があります。 </td>
</tr>
<tr>
<td><strong>V</strong></td>
<td></td>の確認内容と確認方法
<td>I 前に進んでいるのか、それとも見た目だけなのかわかりません。 </td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>社会でどのように扱われるか</td>
<td>技術が動作しても、権利や安全上の理由から使用することはできません。 </td>
</tr>
</tbody>
</table>

<h2>関心ごとの閲覧順序</h2>
<table>
<thead>
<tr>
<th>今気になること</th>
<th>最初に読む記号</th>
<th>次のシンボル</th>
</tr>
</thead>
<tbody>
<tr>
<td>前進するために何を達成する必要があるのか知りたい</td>
<td><strong>P</strong></td>
<td><strong>V</strong></td>
</tr>
<tr>
<td>I 脳波と fMRI</td> の限界について知りたい
<td><strong>M</strong></td>
<td><strong>R</strong></td>
</tr>
<tr>
<td>モデルの仕組みを知りたい</td>
<td><strong>R</strong></td>
<td><strong>I</strong></td>
</tr>
<tr>
<td>アイデンティティや社会システムを見たい</td>
<td><strong>V</strong></td>
<td><strong>D</strong></td>
</tr>
</tbody>
</table>

<h2>これは依存関係であり、年表ではありません</h2>
<p>
P→M→R→I→V→Dという順番で数字が並んでいるとしても、今年必ずここまで行くというわけではありません。重要なことは、後の議論は前の層の失敗に対してより脆弱であるということです。たとえば、M と R があいまいなまま V の強い同一性主張に進むと、入力制限と推定の不確実性が残ります。
</p>

<h4>次</h4>
<p>公式の問題リストと技術ロードマップ本文のインデックスを確認してください。 </p>
<a href="https://mind-upload.com/tech_roadmap.html">技術ロードマップへ→</a>
