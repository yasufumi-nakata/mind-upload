---
layout: default
title: "OpenSourceBrain Documentation: 3D エクスプローラーのトラブルシューティング"
description: "OpenSourceBrain/Documentation: source/OSBv1/Troubleshooting_3d_explorer.md の日本語訳"
article_type: 翻訳資料
last_updated: '2026-05-20'
audience: 外部資料を日本語で原文順に読みたい読者
reading_time: 原文量に依存
page_intro: "このページは外部資料の日本語訳です。原文の見出し順と本文順を保ち、コード・URL・出典表記はできるだけ原形のまま残しています。"
accuracy_note: "機械翻訳をベースにした日本語訳です。実装手順や引用は必ず原典も確認してください。"
---

<main class="main-container">
<article class="content-column">

<div class="note-box">
<strong>出典とライセンス</strong>
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Troubleshooting_3d_explorer.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Troubleshooting_3d_explorer.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:troubleshooting_3d"></a>
<a id="troubleshooting-the-3d-explorer"></a>
# 3D エクスプローラーのトラブルシューティング

OSBv1 上の [3Dエクスプローラー](/external/opensourcebrain/documentation/source/OSBv1/Five_Minute_Introduction.html#v1:five_min_intro:explorer) でより大規模で複雑なモデルを表示する場合、OSB クラスターで発生しているコンピューティング負荷 (複数のユーザーなど) によっては、エクスプローラー インターフェイスのロードに予想よりも時間がかかることがあります。
プロジェクトのロード時に遅延が発生した場合に従うべき一般的なヒントをいくつか示します。

- 「プロジェクトを読み込んでいます ..」というテキストが表示された白いページが表示されても、エクスプローラーが読み込まれない場合は、**ページを数回更新**してください (ほとんどのブラウザでは `control + r` または `F5` を使用するか、[再読み込み] ボタンを使用します)。これにより、エクスプローラーが再初期化されます。

- 3D エクスプローラーが読み込まれた後、Open Source Brain ロゴがページ内 (左上隅の中央のいずれか) で回転しているのが見える場合があります。これは、実行しようとした操作 (例: 接続の読み込みやプロットへの記録されたデータ) が処理中であることを示す進行タイマーです。
ロードされるデータの量によっては、これには数分かかる場合があります。
数分待っても (3 ～ 5 分ほど) 読み込まれない場合は、ページを更新してください。

<a id="v1:troubleshooting_3d:contact"></a>
<a id="contact-us"></a>
## お問い合わせください

待ってページを更新しても問題が解決しない場合は、[お問い合わせ](/external/opensourcebrain/documentation/source/General/Contacts.html#contact) と次の情報を提供してください。

- プラットフォームにアクセスしていた時刻 (タイムゾーン情報を含む)
- どのようなプロジェクトに取り組んでいたか
- どのような操作を実行しようとしていたのか。

これにより、プラットフォームのログをチェックして、修正すべき問題があるかどうかを確認できるようになります。

あるいは、**[この問題](https://github.com/OpenSourceBrain/geppetto-osb/issues/347)** で 3D インターフェイスのロードに失敗する場合のシナリオのより具体的な詳細が記載されています。そこを参照するか、あなたの経験をコメントに追加してください。
</section>

</article>
</main>
