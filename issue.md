---
layout: default
title: 参加と提案のガイド
description: マインドアップロード・コモンズに提案や修正を加えるときの公開向けガイド。
article_type: 参加ガイド
subtitle: 実行できる変更、外部依存、証拠の強さを分けて提案するための入口
author: マインドアップロード研究プロジェクト
last_updated: '2026-05-17'
note: 公開向け参加ガイド
audience: ページ修正、文献追加、検証条件の改善を提案したい読者。
reading_time: 5～10分
page_intro: このページは、マインドアップロードに関する提案を、公開ページへ安全に統合できる形へ整えるためのガイドです。作業履歴ではなく、読者が次の提案を準備するための判断基準だけを残しています。
accuracy_note: このページは参加方法の整理であり、マインドアップロードがすでに実現可能であることを主張するものではありません。
page_highlights:
- 提案は、主張、根拠、反証条件、統合先を分けて書きます。
- このリポジトリ内で実行できる変更と、外部依存のある作業を混ぜません。
- 公開ページに載せる前に、マインドアップロードの検証や学習導線に直接関係するかを確認します。
known_points:
- 小さな文言修正、リンク修正、文献の整理、検証条件の明確化は、このサイト内で扱いやすい提案です。
- 参加者実験、倫理審査、法的判断、ハードウェア調達、長期運用保証は、外部依存のある作業として分離する必要があります。
- 強い主張ほど、データ、評価条件、失敗条件、再現手順を明示する必要があります。
unknown_points:
- 個別の提案が独立ページに値するかどうかは、既存ページへ統合できるかを確認した後に判断します。
- 実験や制度判断を伴う項目は、このサイトだけでは完了条件を満たせません。
wiki_links:
- label: 'Wiki: 事実・仮説・提案・タスクの違い'
  url: /wiki/facts-hypotheses-proposals-and-tasks.html
  description: 観察、仮説、提案、実行タスクを混ぜずに書くための補助ページ。
- label: 'Wiki: 参加後の次のルート'
  url: /wiki/participation-next-routes.html
  description: 提案後にどのページへ進むかを整理します。
- label: 'Wiki: 外部依存の分け方'
  url: /wiki/internal-prework-and-external-dependencies.html
  description: この場で実行できる準備と、外部主体が必要な項目を分けます。
recommended_pages:
- label: 検証
  url: /verification.html
- label: コンテンツ統合ハブ
  url: /content_hub.html
- label: 文献マップ
  url: /research_harvest_50.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>参加するときの基本</h2>
<p>
このサイトでは、マインドアップロードに関する提案を、読者が検証できる形で扱います。新しい主張を追加する場合は、何を主張しているのか、どの証拠に基づくのか、どこまでが未解決なのかを分けてください。
</p>
</div>

<section class="section" id="proposal-integration">
<h2 class="section-title">提案を公開ページへ統合する条件</h2>

<table class="data-table">
<thead>
<tr>
<th>確認すること</th>
<th>公開ページに必要な形</th>
</tr>
</thead>
<tbody>
<tr>
<td>目的</td>
<td>マインドアップロード、WBE、EEG、検証、再現性、同一性、意識理論のいずれに関係するかを明確にします。</td>
</tr>
<tr>
<td>根拠</td>
<td>論文、データセット、標準、ベンチマーク、反証条件のどれに基づくかを分けます。</td>
</tr>
<tr>
<td>主張の強さ</td>
<td>「示唆」「部分的に支持」「まだ未解決」「反証条件が必要」を区別します。</td>
</tr>
<tr>
<td>統合先</td>
<td>既存ページの節に入る場合は、独立ページを作らず、該当ページへ統合します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="external-collaboration">
<h2 class="section-title">外部依存の扱い</h2>
<p>
参加者実験、倫理審査、法的判断、ハードウェア調達、長期運用の保証は、このサイトの編集だけでは完了できません。そのため、公開ページでは「このセッションで実行できる変更」と「外部依存のため保留の項目」を分けます。
</p>

<div class="note-box">
<strong>外部依存タスクを書くときの最小条件</strong>
<p>
所有者、前提条件、完了条件を明記してください。たとえば、実験が必要な場合は、必要な承認、測定対象、成功条件、失敗時の扱いを分けて書きます。
</p>
</div>
</section>

<section class="section" id="safe-publication">
<h2 class="section-title">公開しないもの</h2>
<ul>
<li>作業報告、実行ログ、内部監査、個別の自動化結果。</li>
<li>秘密情報、トークン、認証情報、個人情報、未公開の連絡内容。</li>
<li>マインドアップロードの目的に直接関係しない一般的なタスク管理メモ。</li>
<li>検証条件のない断定的な実現可能性主張。</li>
</ul>
</section>

<section class="section" id="where-to-go-next">
<h2 class="section-title">次に読むページ</h2>
<ul>
<li><a href="verification.html">検証</a>: 成功条件、失敗条件、再現性の基準を確認します。</li>
<li><a href="content_hub.html">公開コンテンツ統合ハブ</a>: どのページへ統合するかを確認します。</li>
<li><a href="wiki/issue-writing-basics.html">Wiki: 最初の提案の書き方</a>: 提案本文の組み立て方を確認します。</li>
</ul>
</section>

</article>
</main>
