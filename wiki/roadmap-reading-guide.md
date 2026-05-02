---
layout: default
title: 'Wiki: ロードマップの見方'
description: これは、P/M/R/I/V/D の記号の意味と、混乱を避けるためにどのような順序で読むべきかを説明する補足ページです。
article_type: ウィキ
subtitle: テクノロジーのロードマップを長いリストではなく依存関係マップとして読む
author: マインドアップロード研究プロジェクト
last_updated: '2026-03-06'
note: 読書ガイド
audience: 技術ロードマップの記号が多くて迷ってしまう方、読む順番を知りたい方。
reading_time: 8～12分
page_intro: このページは、技術ロードマップにおける P/M/R/I/V/D の意味と、どこから読めば迷わないかを説明する補足ページです。ロードマップ本文を改めてまとめるのではなく、「マップの読み方」そのものを整理します。
accuracy_note: このページは読書補助です。問題の正式なリストと現在の取り決めについては、必ず技術ロードマップの本文に戻ってください。
page_highlights:
- P/M/R/I/V/Dを単なる記号ではなく「質問の種類」として解説していきます。
- どの順番でレイヤーが詰まりやすいのか、なぜ前のレイヤーをスキップできないのかがわかります。
- 興味に応じて読むための入り口も別にあります。
known_points:
- Pは進捗の定義、Mは測定、Rは再構築、Iは実行、Vは検証、Dは社会実装です。
- 議論が強ければ強いほど、議論は後退し、前の層が組織化されていないほど、前に進むことが難しくなります。
- ロードマップは、結論をまとめたものではなく、依存関係のマップとして読むのが最善です。
unknown_points:
- どのルートが最短で最も効果的であるかは、将来データベンチが開発されるにつれて変わる可能性があります。
- VとDの最終条件には未解決の問題がまだ多く残っている。
wiki_links:
- label: 'Wiki: WBE の基本'
  url: /wiki/mind-upload-basics.html
  description: このマップが必要な理由の全体像を知りたい人向けです。
- label: 'Wiki: 検証インフラストラクチャの基本'
  url: /wiki/verification-basics.html
  description: Vシリーズで直したいところを補完。
- label: ウィキホーム
  url: /wiki/
  description: 他の基本ページに戻ることができます。
recommended_pages:
- label: 技術ロードマップ
  url: /tech_roadmap.html
- label: WBE の概要
  url: /wbe_101.html
- label: 検証プラットフォーム
  url: /verification.html
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず一言で言うと</h2>
<p>
テクノロジーロードマップとは、将来のストーリーが崩壊する前に、最初に解決する必要があるものを示す地図です。長いリストのように見えますが、実際には「仮定→測定→見積もり→実装→検証→社会実装」という依存関係を表しています。
</p>
</div>

<div class="note-box">
<strong>読み方を決めたら次のページも決めたい</strong>
<p>
ロードマップ上の記号の意味だけでなく、ロードマップを読んだ後に測定、再構成、実装、検証、社会実装のどこに進むべきか知りたい場合は、<a href="roadmap-next-routes.html">、ロードマップ後にたどるべき5つの道筋</a>をご覧ください。
</p>
</div>

<section class="section" id="letters">
日常言語の<h2 class="section-title">P/M/R/I/V/D</h2>
<table class="data-table">
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
</section>

<section class="section" id="routes">
<h2 class="section-title">関心ごとの閲覧順序</h2>
<table class="data-table">
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
</section>

<section class="section" id="not-timeline">
<h2 class="section-title">これは依存関係であり、年表ではありません</h2>
<p>
P→M→R→I→V→Dという順番で数字が並んでいるとしても、今年必ずここまで行くというわけではありません。重要なことは、後の議論は前の層の失敗に対してより脆弱であるということです。たとえば、M と R があいまいなまま V の強い同一性主張に進むと、入力制限と推定の不確実性が残ります。
</p>
<div class="cta-box">
<h4>次</h4>
<p>公式の問題リストと技術ロードマップ本文のインデックスを確認してください。 </p>
<a href="../tech_roadmap.html">技術ロードマップへ→</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE 基本→</a></li>
<li><a href="verification-basics.html">検証基盤の基礎→</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG 前処理と QC →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../tech_roadmap.html">テクノロジーロードマップ→</a></li>
<li><a href="../verification.html">検証インフラ→</a></li>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
</ul>
</div>
</aside>
</main>