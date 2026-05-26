---
layout: default
title: 貢献ガイド
description: Mind-Upload プロジェクトに参加し、問題のステータスを読み取り、実行可能な変更を外部の依存関係から区別する方法。
article_type: ガイド
subtitle: リサーチ ワークフローに参加し、問題トラッカーを読んでください。
author: マインドアップロード研究プロジェクト
last_updated: '2026-05-03'
note: 貢献 + 問題トラッカー
audience: 初めて参加する人、発行状況を確認したい人、実行可能な貢献を始めたい人。
reading_time: 10～20分
page_intro: このページでは、Mind-Upload に参加する方法、問題のステータスを読み取る方法、および外部に依存したままのタスクから今すぐ実行できる変更を分離する方法について説明します。
accuracy_note: ここにリストされている項目はすべて実装されているわけではありません。このページでは、提案書、文書化された設計、および外部依存関係を分離して、完成した作業として誤解されないようにします。
page_highlights:
- 文章、用語、リンク構造の改善など、小さいながらも価値のある参加方法を紹介します。
- これにより、ドキュメントレベルの反映と実装されたアーティファクトを混同することなく、問題のステータスを追跡できます。
- 曖昧な強い主張よりも、達成条件や反証条件が明確な問題を優先する。
- GitHub Issues 全 273 件を、状態、要旨、主な反映先、コメント数つきの Wiki インベントリから確認できます。
known_points:
- テキストの改善、用語の整理、リンクの修正などの小さな変更でも、このサイトへの重要な貢献となります。
- 発行状況ラベルは実施状況や出版状況を読み取るためのものであり、科学的な確認を意味するものではありません。
- 外部に依存するタスクは、現時点で実行できる変更とは別に扱う必要があります。
unknown_points:
- 今後、どの提案を具体化・共同研究に進めるかは、発行段階ではまだ決まっていない。
- このページだけでは、外部に依存するタスクの完了時間や相手方の同意を保証することはできません。
wiki_links:
- label: ウィキホーム
  url: /wiki/
  description: これは、最初にその分野の前提知識を補いたい人のためのエントリーポイントです。
- label: 'Wiki: 内部の事前作業と外部の依存関係'
  url: /wiki/internal-prework-and-external-dependencies.html
  description: このリポジトリで現在実行できることと、外部の依存関係になるものを分離します。
- label: 'Wiki: WBE の基本'
  url: /wiki/mind-upload-basics.html
  description: 貢献する前にトピックを理解したい場合の出発点です。
- label: 'Wiki: 検証の基本'
  url: /wiki/verification-basics.html
  description: なぜ達成条件と反証条件が重要なのかを説明します。
recommended_pages:
- label: スタートページ
  url: /index.html
- label: 検証
  url: /verification.html
- label: 用語集
  url: /glossary.html
---
<!-- 重要: この情報を削除したり上書きしたりしないでください。これはプロジェクトの恒久的な知識ベースです。 -->

<main class="main-container">
<article class="content-column">

<!-- Intro -->
<div class="abstract-box">
<h2>ようこそ</h2>
<p>
Mind-Upload は、マインド アップロードを検証可能な研究に発展させるオープン コミュニティです。分野や経験を問わず、文章の改善や用語の整理、誤解の指摘など、再現性の向上に直結する業務にすぐに参加できます。
</p>
</div>

<div class="key-points">
<h4>初めての方へ</h4>
<ul>
<li><strong>疑わしい場合:</strong> <a href="index.html">開始</a> → <a href="verification.html">検証</a> → <a href="tech_roadmap.html#definition">進行状況の定義</a></li>
<li><strong>用語に行き詰まった場合:</strong> <a href="glossary.html">用語集</a> および <a href="faq.html">FAQ</a> を使用してください。</li>
<li><strong>価値の高い最初の貢献:</strong> 達成条件と反証条件の両方を明示した問題。</li>
</ul>
</div>

<div class="note-box">
<strong>参加の感想</strong>
<p>
大規模な実装から始める必要はありません。曖昧な表現の修正、用語の定義の確認、リンク切れや証拠の欠落の指摘はすべて、ここでの有意義な貢献です。当サイトは再現性を高める小さな修正の積み重ねを大切にしています。
</p>
</div>
<div class="note-box">
<strong>最初に学ぶか参加するか迷った場合</strong>
<p>
概要を理解する、最初から学ぶ、実際に修正または貢献するという 3 つのモードにサイトを分類したい場合は、<a href="wiki/site-usage-modes.html">Wiki: このサイトを使用する 3 つの方法</a> を参照してください。
</p>
</div>

<div class="note-box">
<strong>前提知識が不十分だと思われる場合</strong>
<p>
無理に問題を書き始めるよりも、まず WBE と <a href="wiki/">wiki</a> の検証インフラストラクチャの基本を理解する方が安全です。用語の前提条件を適切に設定すると、どこで停止したかをより正確に報告できるようになります。
</p>
</div>
<div class="note-box">
<strong>最初から問題の書き方を確認したい場合</strong>
<p>
「わからない」を役立つ問題に変える方法、および達成条件と反証条件を設定する方法を知りたい場合は、<a href="wiki/issue-writing-basics.html">Wiki: 最初の問題の書き方</a> を参照してください。
</p>
</div>
<div class="note-box">
<strong>GitHub Issues 全件を確認したい場合</strong>
<p>
2026 年 5 月 3 日時点で取得できる GitHub Issues は 273 件です。未完了 0 件、クローズ済み 273 件、issue 番号範囲 #2～#280、取得コメント 240 件を、<a href="wiki/github-issues-inventory.html">Wiki: GitHub Issues 全件インベントリ</a> に取り込みました。各 issue は、状態、要旨、主な反映先、ラベル、コメント数と GitHub URL で追跡できます。
</p>
</div>
<div class="note-box">
<strong>Issue #267-#280 の対応根拠を確認したい場合</strong>
<p>
2026 年 5 月 3 日の open issue 対応では、EEG/ESI/DCM/維持状態/熱力学/マルチモーダル統合の批判を、既存の検証カードと Wiki ルールへ対応付けました。issue ごとの反映先、残る外部依存、#280 の Omoikane BioData bridge 研究ギャップは、<a href="wiki/open-issues-267-280-resolution.html">Wiki: Issue #267-#280 対応監査</a> と <a href="wiki/omoikane-biodata-mind-state-bridge-gap-register.html">Wiki: Omoikane BioData bridge ギャップ登録</a> から確認してください。
</p>
</div>
<div class="note-box">
<strong>特に RQ ごとの助成金計画のためにここにいる場合</strong>
<p>
このページでは貢献ルートと発行作業を分けています。本当に必要なのは、マインド アップロードのリサーチ質問から資金提供可能なテーマと固定脳波データセット アンカーへの現在の 1 つずつ質問のルートである場合は、<a href="wiki/mind-upload-rq-solvability-bridge.html">RQ 解決可能性ブリッジ</a> から始めて、<a href="wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html">grant とデータセット プレイブック</a>、<a href="wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.html">RQ ごとのディープ書類</a>、<a href="wiki/mind-upload-current-public-six-rq-brief.html">現在の公開6RQ概要</a>、および<a href="https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md">現在の資金候補リスト</a>。
</p>
</div>
<div class="note-box">
<strong>論文執筆が現段階で停止した場合</strong>
<p>
下書きが「これは正直まだ解決できない」という点に達した場合は、ギャップがなくなるまで文を和らげるのではなく、ここでの停止を有界の<code>現段階の制限</code>として返します。最新の書き込みパスでは、現在の <code>U0-2 / U0-3</code> レーンについて 3 つの繰り返しの理由が明確になりました。より強力な継続性の文言を提起する前に、ドラフトでは依然としてデータセット レベルのアブレーション テーブル、閾値安定性台帳、および記録フレームの開示が必要です。言い換えれば、ブロッカーは多くの場合、欠落している形容詞ではなく、欠落しているアーティファクトまたは開示です。その境界のルート サマリーは現在、<a href="wiki/mind-upload-rq-solvability-bridge.html">RQ 可解決性ブリッジ</a> に存在しており、クレーム サーフェスが狭いままでなければならない場合、将来の論文フィードバックはそこを指すはずです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (22:06 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@39248d59caaa</code>、<code>EEG-DATA@7ba2201e2b5</code> 後の、<code>2026-04-04 22:06 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@f90279417a9f</code> は依然として同じ公開 6 を同じ実行順序で保持しています。最新のプルされたデルタはキャリーフォワードのみのままです: <code>mind-upload</code> は、ルートを広げることなく、現在の 6 つの外側にペア流体バリア ルート ガイダンスを追加します。 <code>EEG-DATA</code> は、<code>IEEE DataPort EEG 記録</code> 監査を強化しながら、</code> 監査を強化します。 <code>30,935</code> マージされた一意の行、<code>28,898</code> 高信頼行、<code>24,910</code> すぐに使用可能な行、および <code>24,540</code> 高信頼行即時行、および <code>auto-research-funds</code> は、実際の候補リストを置き換えることなく、ムービングヘッド参照のみを緩和します。したがって、3 スタックの読み取りは、依然として一般的ではなく明示的なままです。<code>U13-2/U13-5</code> は音声側制御と転送ギャップのペアのままであり、<code>U0-2/U0-3</code> はアイデンティティ ドリフト フロアとしきい値ガバナンスのペアのままであり、 <code>U14-4/U14-2</code> はカード契約と固定分割再実行ガバナンスのペアのままです。パブリック セーフな文言も、より明確な点で狭いままです。<code>D03/D02/D01</code> は、DOI/DataCite/カタログ側の読み取りでは、実際の IEEE DataPort ランディング ページよりもオープンに見えるため、<code>D10</code> が唯一の明確なパブリック オープン プライマリ アンカーのままです。 <code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままであり、現在の外部 6 サポート ファミリーは引き続き <code>D11/D08/D05/D20</code> のままです。チェックされたライブ ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Sat, 04 Apr 2026 12:16:08 GMT</code>; を返しました。チェックされたボディはまだ表面化しています <code>2026-04-04 17:07 JST</code> <code>問題 / 概要 / ブリッジ / プレイブック / U13-2 ルート</code> および <code>2026-04-04 19:09 JST</code> の文言このソース同期の前に <code>U13-5 ルート</code> を実行します。実際の資金提供の橋も狭いままです。<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25まで引き続き募集中です。日本時間 15:00</code>、<code>樫の目奨学金</code> は引き続き <code>2026-04-09</code> 必須のサイドルートのまま、<code>中谷財団研究助成金</code> は引き続き次サイクル監視、 <code>セコム総合研究助成</code>は、<code>2026年3月31日12:00 JST</code>以降は終了となります。新しい読み取り専用 Todoist 監査でもまだ十分であるため (<code>items=207</code>; <code>projects=2</code>)、この実行では新しい Todoist 項目は正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (17:07 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@dc8ec5dc5e62</code>、<code>EEG-DATA@f115f11c2da4</code> 後の <code>2026-04-04 17:07 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@8d0f5128fcdc</code> は引き続き同じパブリック 6 を同じ実行順序で保持します。最新のプルされたデルタは繰り越しのみのままです: <code>mind-upload</code> は、ルートを広げることなく、現在の 6 つの外側でバリア側の人間代理の役割を分割します。 <code>EEG-DATA</code> は、<code>EEGIS 想像音声</code> メタデータを維持しながら深めます。 <code>30,930</code> マージされた固有の行、<code>28,893</code> の信頼度の高い行、現在の README スナップショット内の <code>24,909</code> すぐに使用できる行、および<code>auto-research-funds</code> は、<code>上広倫理財団</code> レガシー同期を追加し、<code>8,616</code> 援助 ID、<code>4,319</code> 行をレポートするようになりました。 <code>3,971</code> 公式ソース行。したがって、3 スタックの読み取りは、依然として一般的ではなく明示的なままです。<code>U13-2/U13-5</code> は音声側制御と転送ギャップのペアのままであり、<code>U0-2/U0-3</code> はアイデンティティ ドリフト フロアとしきい値ガバナンスのペアのままであり、 <code>U14-4/U14-2</code> は、カード契約と固定分割再実行ガバナンスのペアのままです。パブリックセーフの文言は依然として <code>D10</code> を唯一の明確なパブリックオープンプライマリアンカーとして維持しますが、<code>D03/D02/D01</code> はゲートサポート計画アンカーのままであり、外部の現在の 6 つのサポートファミリーは引き続き残ります。 <code>D11/D08/D05/D20</code>。チェックされたライブ ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Sat, 04 Apr 2026 07:12:56 GMT</code>; を返しました。チェックされたボディは、このソース同期の前に、<code>2026-04-04 14:10 JST</code><code>issue/brief/bridge/playbook/U13-2route</code>の文言がまだ表面化していました。実際の資金提供の橋も狭いままです。<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25まで引き続き募集中です。日本時間 15:00</code>、<code>樫の目奨学金</code> は引き続き <code>2026-04-09</code> 必須のサイドルートのまま、<code>中谷財団研究助成金</code> は引き続き次サイクル監視、 <code>セコム総合研究助成</code>は、<code>2026年3月31日12:00 JST</code>以降は終了となります。新しい読み取り専用 Todoist 監査でもまだ十分です (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>樫野目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>JSM=0</code>; <code>Doumei=0</code>; <code>研究のススメ=0</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (14:10 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@cafeab4bc2a50c28eb749288a7970342456ddcc3</code> 後の <code>2026-04-04 14:10 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@e0695bcac83d970e422a5c4f42514b3381004223</code>、および<code>auto-research-funds@a4852d89376c3fd770a8dc58303a5a98b326d623</code> は引き続き同じ公開 6 を同じ実行順序で保持します。最新のプルされたデルタは繰り越しのみのままです: <code>mind-upload</code> は、ルートを広げることなく、初期の EEG 基礎モデルのソースとステータスの分割に加えて、用語集の興奮性とイオン用語を強化します。 <code>EEG-DATA</code> は、<code>neuroTUM Cybathlon</code> を深めます。 <code>Zenodo TSA v7.8</code>、<code>poetry EEG</code> メタデータを維持しながら、<code>30,930</code> マージされた一意の行、<code>28,893</code> の高信頼行、 <code>24,909</code> 即時行、<code>24,539</code> 高信頼性即時行、および <code>auto-research-funds</code> は、実用的な内容を置き換えることなく <code>JELA Diakonia</code> 奨学金カードを追加します。候補者リスト。 3 つのスタックの読み取りも、一般的ではなく明示的なままです。<code>U13-2/U13-5</code> は音声側制御と転送ギャップのペアのまま、<code>U0-2/U0-3</code> はアイデンティティ ドリフト フロアとしきい値ガバナンスのペアのままです。 <code>U14-4/U14-2</code> は、カード契約と固定分割再実行ガバナンスのペアのままです。したがって、パブリック セーフな文言では、<code>D10</code> が唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Sat, 04 Apr 2026 04:18:04 GMT</code>; を返しました。チェックされた本文はまだ表面化しています <code>2026-04-04 12:02 JST</code> <code>issue / Brief / Bridge / Playbook</code> および <code>2026-04-04 09:05 JST</code> これより前の古い現在の 6 行パケットに関する文言ソース同期。最新のリポジトリの進行状況では、ルートを変更せずに言語、メタデータ、および隣接する奨学金コンテキストが引き続き強化されるため、この実行では、フロント ドア、プレイブック、および現在の 6 行のすべてのパケットにわたる制限された <code>14:10 JST</code> ソース同期のみが伝送され、キューは変更されません。実際の資金提供の橋は依然として狭いままです。<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25まで引き続き募集中です。日本時間 15:00</code>、<code>樫の目奨学金</code> は依然として <code>2026-04-09</code> 必須のサイドルートのまま、<code>中谷財団研究助成金</code> は次のサイクルの監視のまま、 <code>セコム総合研究助成</code>は、<code>2026年3月31日12:00 JST</code>以降は終了となります。新しい読み取り専用 Todoist 監査も依然として十分です (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>Doumei=0</code>; <code>研究のススメ=0</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (12:02 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@f84f6e53753b8d8d9082f27d1bbe307e606bd3c2</code> 後の <code>2026-04-04 12:02 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@017ae806c4dd30719223fc20470ef3ccd676ee29</code> および <code>auto-research-funds@d4024a5b8a1aa7bdef83abe82eeacfc9c5a0d720</code> は依然として同じ公開 6 を維持します同じ実行順序で。取得された最新のデルタは引き続きキャリーフォワードのみです。 <code>mind-upload</code> は、ルートを広げることなく、公開ページ間で EEG 記録フレーム コントラクトを同期します。 <code>EEG-DATA</code> は、EEG データセットを維持しながら、移動容量の EEG データセットを詳細に調べます。 <code>30,929</code> マージされた一意の行、<code>28,892</code> 高信頼行、<code>24,908</code> 即時行、および <code>24,538</code> 高信頼即時行、および <code>auto-research-funds</code> は、実際の候補リストを置き換えることなく、以前の <code>11:04 JST</code> 資金に関する追加条項をそのまま保持しています。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Sat, 04 Apr 2026 02:19:09 GMT</code>; を返しました。チェックされた本文はすでに <code>2026-04-04 11:04 JST</code> <code>issue/brief/bridge/playbook</code> の文言で表示されていますが、チェックされた <code>U13-2</code> 行パケットはまだ表示されています<code>2026-04-04 09:05 JST</code> このソース同期前。最新のリポジトリの進行状況はルート保守的なままですが、最初の行のパケットがフロント ドアよりも遅れているため、この実行では、キューを変更せずに、フロント ドア、プレイブック、および <code>U13-2</code> 行パケット全体で制限された <code>12:02 JST</code> ソース同期のみが伝送されます。実際の資金提供の橋は依然として狭いままです。<code>蔵基金</code>は<code>2026年4月17日17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026年5月25日まで引き続き募集中です。 15:00 JST</code>、<code>樫の目奨学金</code>は引き続き<code>2026-04-09</code>は必須のサイドルートのまま、<code>中谷財団研究助成金</code>は次のサイクルの監視のまま、 <code>セコム一般研究助成</code>は、<code>2026年3月31日12:00 JST</code>以降は終了となります。新しい読み取り専用 Todoist 監査も依然として十分です (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>Doumei=0</code>; <code>研究のススメ=0</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (11:04 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@812e1650bae1c3da50df7355cc73bb4510f33464</code> 後の <code>2026-04-04 11:04 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@1deac45c75a2d0a2f0d21a9ce5e52df1ff9bb3c5</code>、および <code>auto-research-funds@9741ee45a02597d2253e58bbf0ea083b56fe9553</code> は依然として同じ執行順序で同じ公開6。最新のプルされたデルタは依然としてキャリーフォワードのみです: <code>mind-upload</code> は、ルートを広げることなく用語集のブリッジ監視の用語を厳格化します。 <code>EEG-DATA</code> は、重複した EEG-fMRI オーバーライド行を縮小し、<code>30,929</code> をマージされた固有の行に保ちます。現在の <code>D10 / D03 / D02 / を残しつつ、行、<code>28,892</code> の高信頼行、<code>24,908</code> の即時行、および <code>24,538</code> の高信頼の即時行D01</code> ファミリーは変更されず、<code>auto-research-funds</code> は、実質的な候補リストを置き換えることなく、現在のサイクルのファンディング カードに従来の補償範囲を追加します。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ フロントドア ページと <code>U13-2</code> 行パケットは再び <code>HTTP/2 200</code> と <code>Last-Modified: Sat, 04 Apr 2026 01:14:45 GMT</code>; を返しました。チェックされた本体は、このソース同期の前に <code>2026-04-04 09:05 JST</code> という文言がまだ表面化していました。最新のリポジトリの進行状況はパブリック セーフですがルートは保守的であるため、この実行では、行パケットは変更せずに、境界付きの <code>11:04 JST</code> ソース同期のみをフロントドア ルート ページとプレイブックに追加します。公式スポットチェックにより、<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25 15:00まで受け付けられます。 JST</code>、<code>樫の目奨学金</code>、<code>2026-04-09</code> 必着、<code>中谷財団研究助成金</code>、次サイクル監視中、<code>セコム総合研究Grant</code> は <code>2026 年 3 月 31 日 12:00 JST</code> 後に終了しました。新しい読み取り専用 Todoist 監査も依然として十分なままであるため (<code>items=206</code>; <code>projects=2</code>)、この実行では新しい Todoist 項目は正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (09:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@e571567f017d0b544317f900a21a966f1427c9c8</code> 後の <code>2026-04-04 09:05 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@fbbb0d8c01e0aadfce6a2789ab262f73037cf521</code>、および <code>auto-research-funds@d7f6fb9bc158742be3a6adc2540a382d066de07f</code> は引き続き同じ公開を維持します同じ実行順序で 6 つ。最新のプルされたデルタは依然としてキャリーフォワードのみです: <code>mind-upload</code> は、最近の事前トレーニング オーバーラップ監査に加えて以前の <code>08:07 JST</code> ルートホールド同期を保持するだけですが、<code>EEG-DATA</code> は引き続き保持されます。 <code>30,929</code> マージされた一意の行、<code>28,892</code> 高信頼行、<code>24,909</code> 即時行、および <code>24,539</code> 高信頼即時<code>OpenNeuro ds007020</code> を限定的な残り側サポート ノートとして扱い、<code>HeartBEAM</code> と figshare <code>EEG を保存時に保持し、TMS</code> のみをバックアップ ファミリとして保持しながら行を作成します。 <code>auto-research-funds</code> は、<code>JGC-S</code> を隣接する滑走路としてのみ維持しながら、徹底的に検討された 4 月 4 日の奨学金の更新を追加します。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ フロントドア ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 23:18:55 GMT</code> を返し、そのルートに面した本体はすでに以前の <code>2026-04-04 から表面化しています。 08:07 JST</code> このソース同期の前にメモを保持します。現在の 6 行のパケットも <code>HTTP/2 200</code> と <code>Last-Modified: Sat, 04 Apr 2026 00:11:41 GMT</code> を返しましたが、依然として <code>2026-04-04 01:04 として表面化しました。この行パケット同期の前の JST</code> 文言。公式スポットチェックにより、<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25 15:00まで受け付け中です。 JST</code>、<code>樫の目奨学金</code>、<code>2026-04-09</code>必着、<code>中谷財団研究助成金</code>、次のサイクルウォッチ中、および<code>セコム総合研究Grant</code> は <code>2026 年 3 月 31 日 12:00 JST</code> 後に終了しました。新しい読み取り専用 Todoist 監査も依然として十分なままであるため (<code>items=206</code>; <code>projects=2</code>)、この実行では新しい Todoist 項目は正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (08:07 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@418c8f5d0ef9e871531d9cfb8548887e57f54d68</code> 後の <code>2026-04-04 08:07 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@dc6d833b83e9a5e6a181edfee5349f561f65b043</code>、および<code>auto-research-funds@58d8738be5d55cff13d7bd626479783d6818de1f</code>同じ公開6を同じ実行順序で維持します。最新のプルされたデルタは引き続きキャリーフォワードのみです: <code>mind-upload</code> はルートを広げることなくフロントドアの人間とプロキシの比較を強化します。 <code>EEG-DATA</code> は依然として <code>30,929</code> マージされた一意の行を保持します。 <code>28,892</code> 高信頼行、<code>24,909</code> 即時行、<code>24,539</code> 高信頼即時行 (<code>HeartBEAM</code> および figshare のプロモート中) <code>EEG は保存時で、TMS</code> はバックアップファミリーとしてのみ使用され、<code>auto-research-funds</code> は、実質的な最終候補者リストを置き換えることなく、隣接する滑走路としてのみ <code>JGC-S</code> の外国人留学生奨学金を追加します。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ公開ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 22:10:18 GMT</code>; を返しました。ルートに面した本体は、このソース同期の前に <code>2026-04-04 01:04 JST</code> という文言がまだ表面に出ていました。公式スポットチェックにより、<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25 15:00まで受け付けられます。 JST</code>、毎年恒例の<code>1月中旬から4月上旬</code>ウィンドウの<code>樫の目奨学金</code>、およびリポジトリ側の<code>2026-04-09</code>必着読書、<code>中谷財団の研究次のサイクルウォッチではgrant</code>、<code>セコム総合研究助成金</code>は<code>2026年3月31日12:00 JST</code>後に終了しました。新しい読み取り専用 Todoist 監査も依然として十分です (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>慶応義塾大学大学院奨学金=2</code>; <code>G-7=1</code>; <code>同盟=0</code>; Susume=0</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (01:04 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@9b6a8b971ba08949b377ece744539c19180ad76e</code> 後の <code>2026-04-04 01:04 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@56d765da60ba8d67bf8cb5bc61e4f1fdb06229c</code>、および <code>auto-research-funds@3c8569e284d61c47a6ac5ed8d8091aa15c6d53b3</code> は引き続き同じ執行順序で同じ公開6。最新のプルされたデルタは引き続きキャリーフォワードのみです。 <code>mind-upload</code> は、ルートを広げることなくアーティファクト スタックのフィールド レベルの開示強化を追加し、<code>EEG-DATA</code> は、<code>Numbers</code> のパブリック OpenNeuro メタデータを深化します。 <code>PRIOS</code> 一方で、<code>summary.json</code> は依然として <code>30,921</code> マージされた一意の行、<code>28,884</code> の高信頼行を報告します。 <code>24,900</code> 即時行、<code>24,530</code> 高信頼即時行、および <code>auto-research-funds</code> は、<code> 同盟育成会</code> の現在のカバレッジを追加し、 <code>研究のすゝめ助成金</code> は、実質的な候補リストを変更することなく。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ公開ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 15:13:06 GMT</code>; を返しました。ルートに面した本体は、このソース同期の前に <code>2026-04-04 00:06 JST</code> という文言がまだ表面に出ていました。公式スポットチェックにより、<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25 15:00まで受け付けられます。 JST</code>、<code>樫の目奨学金</code>、<code>2026-04-09</code>必着、<code>中谷財団研究助成</code>プラス<code>セコム総合研究助成</code>監視/クローズ状態。新しい読み取り専用 Todoist 監査も依然として十分です (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>慶大大学院奨学金=2</code>; <code>G-7=1</code>; <code>同盟会=0</code>;そのため、今回の実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 4 日 (00:06 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@84d84fb5a82d22d70d12c92a957327b3937bc422</code> 後の <code>2026-04-04 00:06 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@b468ecc5f8c0ed34fb85c0bbc2a2e3c9282ce965</code>、および<code>auto-research-funds@eccee095a939a604cd4c684a2af6379f9dc3fa88</code>は依然として同じままです同じ執行順序で公開6件。最新のプルされたデルタは引き続きキャリーフォワードのみです: <code>mind-upload</code> は以前の <code>23:06 JST</code> ルート再読み込みの追加を保持するだけであり、<code>EEG-DATA</code> は <code>高速マッピング セマンティック統合 EEG を追加します。 dataset</code> に対し、<code>summary.json</code> は、<code>30,921</code> マージされた一意の行、<code>28,884</code> の高信頼行、<code>24,900</code> を報告するようになりました。即時行、<code>24,530</code> 高信頼性即時行、<code>auto-research-funds</code> は、実質的な候補リストを置き換えることなく、<code>飯塚の現在のカードと韓国のレガシー同期</code> を追加します。したがって、パブリック セーフな文言では、<code>D10</code> を現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持し、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ公開ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 14:13:44 GMT</code>; を返しました。ルートに面した本体は、この情報源より前の <code>brief / Bridge / U13-2</code> の <code>22:04 JST</code> および <code>issue</code> の <code>22:04/22:05 JST</code> でまだ浮上していました。同期します。公式スポットチェックにより、<code>蔵基金</code>は<code>2026-04-17 17:00 JST</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25 15:00まで受け付け中です。 JST</code>、<code>樫の目奨学金</code>、<code>2026-04-09</code>必着、<code>中谷財団研究助成</code>プラス<code>セコム総合研究助成</code>監視/クローズ状態。新しい読み取り専用 Todoist 監査も依然として十分です (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>慶応大学院奨学金=2</code>; <code>G-7=1</code>; <code>ENEOS=1</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 3 日 (22:04 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@1ab35b64796f3936e525befb5d9428d789a16263</code> 後の <code>2026-04-03 22:04 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@be3d03d1c286dcd37fb056317a693e47c39f7f3a</code>、<code>auto-research-funds@845e6849a6c36e6e83394e32cf8dc4b5fe6fdc07</code>同じ公開6を同じ実行順序で維持します。取得された最新のデルタは現在、<code>EEG-DATA</code> に集中しています。 <code>summary.json</code> レポート <code>30,918</code> マージされた一意の行、<code>28,881</code> の高信頼行、最新の完全リフレッシュ後の <code>24,898</code> 即時行、および <code>24,528</code> 高信頼性即時行、一方 <code>mind-upload</code> および <code>auto-research-funds</code> は、それらの行をそのまま保持するようになりました。以前の <code>21:05 JST</code> を、実際の候補リストを置き換えることなく追加しました。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ公開ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 12:24:26 GMT</code>; を返しました。彼らのルートに面した本体はすでに<code>問題/概要/橋</code>で<code>21:05 JST</code>に浮上していますが、<code>U13-2ルート</code>はまだ<code>21:05 JST</code>で浮上しています。 <code>11:07 JST</code>。公式のスポットチェックにより、実際的な橋渡しはまだ狭いままです。<code>蔵基金</code>は引き続き募集中 (<code>2026-04-17 17:00 JST</code>)、<code>中谷財団大学院奨学金</code>は引き続き募集中 (<code>2026-04-01 - 2026-05-25 15:00 JST</code>)、監視/閉じられた読み取りの残りの部分は、以前の再読み取りから変更されません。新しい読み取り専用 Todoist 監査も依然として十分です (<code>items=205</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>慶応大学院奨学金=2</code>; <code>G-7=1</code>; <code>ENEOS=0</code>; ため、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 3 日 (22:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@1ab35b64796f3936e525befb5d9428d789a16263</code> 後の <code>2026-04-03 22:05 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@be3d03d1c286dcd37fb056317a693e47c39f7f3a</code>、<code>auto-research-funds@845e6849a6c36e6e83394e32cf8dc4b5fe6fdc07</code>同じ公開6を同じ実行順序で維持します。最新のプルされたデルタは引き続きキャリーフォワードのみです: <code>mind-upload</code> は以前の <code>21:05 JST</code> ルートホールド同期を運ぶだけであり、<code>EEG-DATA</code> は <code>3 つの深い EEG データセットを追加します</code> をオーバーライドし、<code>30,918</code> マージされた一意の行、<code>28,881</code> の高信頼行、<code>24,898</code> の即時行、および<code>24,528</code> の信頼性の高い即時行、および <code>auto-research-funds</code> には、実際の最終候補リストを置き換えることなく、以前の <code>21:05 JST</code> の資金追加付録が含まれるようになりました。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ公開ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 12:24:26 GMT</code>; を返しました。彼らのルートに面した本体は、このソース同期の前に、<code>21:05 JST</code> <code>issue / Brief / Bridge / U13-2</code> に関するメモを保持する時点ですでに表面化しています。今回の公式スポットチェックでは、<code>蔵基金</code> (<code>2026-02-02 - 2026-04-17 17:00 JST</code>) と<code>中谷財団大学院奨学金</code> が引き続き維持されます。 (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) が開いている間、<code>樫の目奨学金</code> は学生滑走路側ルート (<code>2026-04-09 到着必須</code>) のままです。 <code>中谷財団研究助成金</code>は、現在の公開ページでまだ終了とマークされているため、次のサイクルで監視され続けます。また、<code>セコム一般研究助成金</code>は、<code>2026-03-31 12:00 JST</code>以降も終了したままです。新しい読み取り専用 Todoist 監査でもまだ十分です (<code>items=205</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>樫野目=2</code>; <code>脳科学財団=8</code>; <code>; Institute=1</code>; <code>慶応大学大学院奨学金=2</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 3 日 (21:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@3db1aa653b74d164c3a57b75677e345ea10356e0</code> 後の <code>2026-04-03 21:05 JST</code> での実際のプルの再読み込み、 <code>EEG-DATA@c10c95274ecf1397768eb28de48aac8ce925c22d</code>、および <code>auto-research-funds@4a67e06b530bc742521f80fa5b13ccbe1115ebb9</code> は依然として同じ執行順序で同じ公開6。最新のプルされたデルタは引き続きキャリーフォワードのみです: <code>mind-upload</code> は以前の <code>20:05 JST</code> ルートホールドの付録を保持するだけで、<code>EEG-DATA</code> はレポート中に欠落している EEG データセットに対する BDSP 手動の詳細な調査を追加します。 <code>30,914</code> マージされた一意の行、<code>28,877</code> 高信頼行、<code>24,896</code> 即時行、および <code>24,526</code> 高信頼即時行、および <code>auto-research-funds</code> は、実際の最終候補リストを置き換えることなく、以前の <code>20:05 JST</code> 資金に関する追加条項を保持するようになりました。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ公開ページは再び <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 11:17:44 GMT</code>; を返しました。彼らのルートに面した本体は、<code>20:05 JST</code> <code>問題/概要/橋</code> の早い時間にすでに浮上していますが、<code>U13-2 ルート</code> は <code>11:07 JST</code> にもまだ浮上しています。今回の公式スポットチェックでは、<code>蔵基金</code> (<code>2026-04-17 17:00 JST</code>) および<code>中谷財団大学院奨学金</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) は開場しますが、<code>樫の目奨学金</code> は学生滑走路側ルートを維持します (<code>2026-04-09 到着必須</code>)、<code>中谷財団研究助成金</code>現在の公開ページではまだ終了済みとマークされており、<code>セコム一般研究助成金</code> は <code>2026-03-31 12:00 JST</code> 以降も終了したままであるため、次のサイクルの監視を続けます。新しい読み取り専用 Todoist 監査でもまだ十分です (<code>items=205</code>; <code>projects=2</code>; <code>nakatani family=11</code>; <code>G-7=1</code>; <code>ENEOS=0</code>; <code>慶応大学院奨学金=2</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 3 日 (20:05 JST) の最新ルート保留</strong>
<p>
<code>2026-04-03 20:05 JST</code> での、<code>mind-upload@b4fd73d9e983</code>、<code>EEG-DATA@649ff098ab57</code> 後の実際のプルの再読み込み。 <code>auto-research-funds@7c1b835d1d13</code> は引き続き同じ公開 6 を同じ実行順序で保持します。最新のプルされたデルタは、アクティブな EEG ファースト バッチを広げるのではなく、サポート スペースをさらに深めます。<code>mind-upload</code> は、現在の 6 つ以外の人間の熱証拠を <code>パッシブ / タスクにリンクされたマクロ温度測定</code> と <code>摂動条件付き熱ルート</code> に分割します。 <code>EEG-DATA</code> は、制限付きの <code>アルツハイマー病における経頭蓋磁気刺激 - データ</code> BDSP の詳細を追加し、<code>30,912</code> マージされた固有の行をレポートするようになりました。 <code>28,875</code> 高信頼行、<code>24,894</code> 直接使用可能な行、<code>auto-research-funds</code> は <code>ENEOS</code> の現在のカード カバレッジを完了し、 <code>G-7</code> 奨学金を受け取りながら、実際の最終候補リストを置き換えることなく、<code>8,600</code> 援助 ID、<code>4,308</code> 行、および <code>3,959</code> 行の公式ソース行を報告します。したがって、パブリック セーフの文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ公開ページは、<code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 10:19:46 GMT</code> を返しましたが、ルートに面した本体はまだ以前の <code>11:05/11:07 に表示されていました。 JST</code> は、このソース同期の前にメモを保持します。今回の公式スポットチェックでは、<code>蔵基金</code> (<code>2026-04-17 17:00 JST</code>) および<code>中谷財団大学院奨学金</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) は開場しますが、<code>樫の目奨学金</code> は学生滑走路側ルートを維持します (<code>2026-04-09 到着必須</code>)、<code>中谷財団研究助成金</code>現在の公開ページではまだ終了済みとマークされており、<code>セコム一般研究助成金</code> は <code>2026-03-31 12:00 JST</code> 以降も終了したままであるため、次のサイクルの監視を続けます。新しい読み取り専用 Todoist 監査でもまだ十分です (<code>items=205</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>樫野目=2</code>; <code>脳科学財団=8</code>; <code>; Institute=1</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 3 日 (11:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@f70432e4a6c8</code>、<code>EEG-DATA@1981d34c5f71</code> 後の <code>2026-04-03 11:05 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@bfebe94da875</code> は引き続き同じ公開 6 を同じ実行順序で保持します。最新のプルされたデルタは、アクティブな EEG-first バッチを広げるのではなく、依然としてサポート スペースを狭めています。 <code>mind-upload</code> は、現在の 6 つ以外の <code>睡眠リプレイの整合性 / 生理学的ゲート</code> の文言を強化し、<code>EEG-DATA</code> は、そのインベントリを更新し、 <code>COG-BCI</code> ファミリーでは、<code>30,904</code> マージされた一意の行、<code>28,867</code> の高信頼行、および <code>24,890</code> 直接使用可能な行を報告しています。 <code>auto-research-funds</code> は、<code>10:06 JST マインドアップロード資金に関する付録</code> を引き継ぎ、<code>8,596</code> 援助 ID、<code>4,308</code> 行をレポートします。 <code>3,958</code> 実際の候補リストを置き換えることなく、公式ソースの行を追加します。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ ルート ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Fri, 03 Apr 2026 01:31:28 GMT</code> を返しましたが、ルートに面した本体は以前の <code>05:12 JST</code> ホールド ノートを依然として表示していました。このソース同期の前に。今回の公式スポットチェックでは、<code>蔵基金</code> (<code>2026-04-17 17:00 JST</code>) および<code>中谷財団大学院奨学金</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) は開場しますが、<code>樫の目奨学金</code> は学生滑走路側ルートを維持します (<code>2026-04-09 到着必須</code>)、<code>中谷財団研究助成金</code>現在の公開ページではまだ終了済みとマークされており、<code>セコム一般研究助成金</code> は <code>2026-03-31 12:00 JST</code> 以降も終了したままであるため、次のサイクルの監視を続けます。新しい読み取り専用 Todoist 監査でもまだ十分です (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>樫野目=2</code>; <code>脳科学財団=8</code>; <code>; Institute=1</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 3 日 (05:12 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@a9fc5d1cb691</code>、<code>EEG-DATA@8c3ace28bad0</code> 後の <code>2026-04-03 05:12 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@35756f8381c4</code> は依然として同じ公開 6 を同じ実行順序で保持しています。最新のプルされたデルタは、アクティブな EEG-first バッチを広げるのではなく、依然としてサポート スペースを狭めています: <code>mind-upload</code> は現在 <code>docs にあります: アクティブ キューを変更せずにエクスポートされたルート ミラーの位置を維持する同期 github wiki エクスポート</code> ヘッド、<code>EEG-DATA</code> は引き継がれます<code>VR ナビゲーション データセット</code> 出力更新は、最近の <code>EESM17</code> メタデータに基づいて更新され、<code>30,900</code> マージされた一意の行、<code>28,863</code> の高信頼行をレポートします。および <code>24,885</code> 直接使用可能な行、および <code>auto-research-funds</code> は、最近の <code>JSSF 研究出版物</code> の更新に加え、<code>JSPS 海外フェロー</code> の現在のカード スナップショットを追加し、レポートを作成しています。 <code>8,594</code> 援助 ID、<code>4,307</code> 行、および <code>3,957</code> 行の公式ソース行を、実際の候補リストを置き換えることなく提供します。したがって、パブリック セーフの文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ ルート ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Thu, 02 Apr 2026 19:17:56 GMT</code> を返しましたが、ルートに面した本体は以前の <code>04:05/04:06 で表示されました。 JST</code> は、このソース同期の前にメモを保持します。今回の公式スポットチェックでは、<code>蔵基金</code> (<code>2026-04-17 17:00 JST</code>) および<code>中谷財団大学院奨学金</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) は開場しますが、<code>樫の目奨学金</code> は学生滑走路側ルートを維持します (<code>2026-04-09 到着必須</code>)、<code>中谷財団研究助成金</code>現在の公開ページではまだ終了済みとマークされており、<code>セコム一般研究助成金</code> は <code>2026-03-31 12:00 JST</code> 以降も終了したままであるため、次のサイクルの監視を続けます。新しい読み取り専用 Todoist 監査でもまだ十分です (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>樫野目=2</code>; <code>脳科学財団=8</code>; <code>; Institute=1</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 3 日 (04:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@f5e13ebdc474</code>、<code>EEG-DATA@53f5c8166faf</code> 後の <code>2026-04-03 04:05 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@1f190fec93a9</code> は依然として同じ公開 6 を同じ実行順序で保持しています。最新のプルされたデルタは、アクティブな EEG-first バッチを広げるのではなく、依然としてサポート スペースを狭めています。 <code>mind-upload</code> は、現在の 6 つ以外の <code>BCSFB / 人間とプロキシの構成</code> の文献同期を繰り越し、<code>EEG-DATA</code> は引き続きレポートします。 <code>30,900</code> マージされた固有の行、<code>28,863</code> の高信頼行、および現在のアンカー ファミリを置き換えないカタログ更新後に直接使用可能な行 <code>24,885</code> <code>auto-research-funds</code> は、<code>MUFJ 研究助成金</code> データを更新し、<code>8,593</code> 援助 ID、<code>4,306</code> 行、および<code>3,956</code> 実際の候補リストを置き換えることなく、公式ソースの行を追加します。したがって、パブリック セーフな文言では、<code>D10</code> を現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持し、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ ルート ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Thu, 02 Apr 2026 18:14:39 GMT</code> を返しました。この実行の公式スポット チェックでは依然として <code>Kura Fund</code> が維持されています。 (<code>2026-04-17 17:00 JST</code>) および<code>中谷財団大学院奨学金</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) は、 <code>樫の目奨学金</code> は学生滑走路側ルートのまま (<code>2026-04-09 到着必須</code>)、<code>中谷財団研究助成金</code> は現在の公開ページではまだ終了とマークされているため次のサイクルの監視を継続、<code>セコム総合研究Grant</code> は、<code>2026 年 3 月 31 日 12:00 JST</code> 以降も閉鎖されたままです。新しい読み取り専用 Todoist 監査でもまだ十分です (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>樫野目=2</code>; <code>脳科学財団=8</code>; <code>; Institute=1</code>) なので、この実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (23:08 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@f5d1d1dd1683</code>、<code>EEG-DATA@ee1463d28288</code> 後の、<code>2026-04-02 23:08 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@ec24a355abbc</code> は引き続き同じ公開 6 を同じ実行順序で保持します。最新のプルデルタは、アクティブな EEG-first バッチを広げるのではなく、ルート規律とサポート空間をさらに深めます。<code>mind-upload</code> は、現在の 6 つ以外の因果関係と人間の代理ブリッジを明確にし、<code>EEG-DATA</code> は候補のキュレーションを洗練し、レポートを作成します。 <code>30,896</code> マージされた固有行、<code>28,859</code> 高信頼行、<code>24,882</code> 直接使用可能な行、および <code>auto-research-funds</code> が追加されます。 <code>Geo-Karaku</code> は、実際の候補リストを置き換えることなく、現在のカードを追加します。したがって、パブリック セーフな文言では、<code>D10</code> が現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーとして維持されますが、<code>D03/D02/D01</code> はゲート サポート プランニング アンカーのままです。チェックされたライブ ルート ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Thu, 02 Apr 2026 13:12:21 GMT</code> を返しました。この実行の公式スポット チェックでは依然として <code>Kura Fund</code> と<code>中谷財団大学院奨学金</code> はオープンしていますが、<code>中谷財団研究助成金</code> および <code>セコム一般研究助成金</code> は閉鎖/監視されており、新鮮な読み取り専用の Todoist 監査でも十分なままです。 (<code>items=203</code>; <code>projects=2</code>; <code>蔵=2</code>; <code>中谷家=11</code>; <code>樫の目=2</code>; <code>セコム=3</code>)。したがって、このアップデートは解決済みクレームのアップデートではなく、制限されたルートホールドの追加であり、今回の実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>現在の 6 つの調査質問を EEG 対応の作業パッケージに変換したい場合</strong>
<p>
実行順に並べると、現在の公開深化バッチは <code>U13-2</code>、<code>U13-5</code>、<code>U0-2</code>、<code>U0-3</code>、<code>U14-4</code>、<code>U14-2</code> です。これらは解決済みの問いではありません。1 つの主張、1 つのデータセットアンカー、1 つの KPI 束、1 つの明示的な外部依存境界を先に固定するための、現在の有界な作業パッケージです。2026 年 4 月 3 日 <code>02:05 JST</code> の実プル再読後も、このバッチは意図的に狭いままです。中心は <code>inner-speech decoding + identity drift + reproducibility auditing</code> と保守的なアンカー集合 <code>D10/D03/D01/D02</code> であり、これは Mind-Upload の研究質問を EEG 対応で資金化可能な作業パッケージへ接続する、現時点で最も整理された橋だからです。これは解決済み主張の更新ではなく、ルート設定の更新です。
</p>
<p>
<code>2026-04-03 02:05 JST</code> の実プル再読では、<code>mind-upload@94a41524ca1a</code>、<code>EEG-DATA@03172b700180</code>、<code>auto-research-funds@e6fde9b4f248</code> の後でも、<code>D10</code> が現在の 6 つにおける唯一の明確な公開オープン一次アンカーであり、<code>D03</code>、<code>D02</code>、<code>D01</code> は公開ルート上のゲート付き支援アンカーとして読むべき状態でした。最新差分はルートを広げるのではなく支援を深めています。<code>mind-upload</code> は現在の 6 つの外側にある <code>BCSFB</code> フロントドアファミリーを明確化し、<code>EEG-DATA</code> は最新の Zenodo visual EEG 深掘り後に <code>30,900</code> マージ済み一意行、<code>28,863</code> 高信頼行、<code>24,885</code> 直接利用可能行を報告し、<code>auto-research-funds</code> は実用的な候補リストを置き換えずに <code>NII</code> オープン連携のレガシー資金カードを保持しています。確認したライブのルートページは <code>HTTP/2 200</code> と <code>Last-Modified: Thu, 02 Apr 2026 16:25:49 GMT</code> を返しましたが、本文はまだ有界な <code>00:07 JST</code> の保持ノートを出していたため、この編集はバッチを拡大せず、入口ページの説明を同じ現行基準にそろえるものです。
</p>
<p>
したがって現在の実行順は <code>U13-2 → U13-5 → U0-2 → U0-3 → U14-4 → U14-2</code> のままです。公開向けの進捗は解決済み主張ではなく、有界な成果物を意味します。<code>U13-2</code> では <code>brain-minus-prior</code> 対照表、<code>U13-5</code> では知覚から想起への分岐仕様ノート、<code>U0-2</code> では <code>offset/jitter + state-feature drift</code> 監査、<code>U0-3</code> では閾値安定性と過適合除外ルール、<code>U14-4</code> では入力済みカード例、<code>U14-2</code> では固定分割の再実行契約です。現在の行パケットは、各行に 1 つのコンパクトな <code>first-pass KPI bundle + stop rule</code> も記録しているため、読者は主張が広がる前にどこでルートを止めるべきかを確認できます。今回の主な公開安全上の絞り込みは、バッチ全体ではなく行単位です。<code>U13-5</code> は、可視の <code>D03</code> メタデータが依然として認知負荷パッケージであるため明示的な想起妥当性の留保を持ち、<code>U14-4/U14-2</code> は、<code>D01</code> がレイテンシ / 開示の下限にすぎず、より広い再実行文言にはまだ <code>D13</code> が必要であることを明示しています。<code>Kura Fund</code> と <code>中谷財団大学院奨学金</code> は短期ブリッジであり、<code>樫の目奨学金</code> は学生ランウェイ側ルートにとどまり、より広い神経科学助成ルートは監視モードです。資金側では <code>NII</code> の繰り越しが連携側のリマインダーとして有用ですが、現在の 6 つを置き換える理由ではなく隣接レーンです。大規模な社会実装プログラムは、この EEG-first ルートの外側にあります。EEG が今閉じられるもの、外部支援がまだ必要なもの、資金レーンがどこに収まるかを 1 ページで見たい場合は、<a href="wiki/mind-upload-rq-solvability-bridge.html">RQ 可解決性ブリッジ</a>から始めてください。現在の 6 つを変更せず、外側にある最も整理された公開オープン <code>A</code> 級ルートを見たい場合は、<a href="wiki/u7-1-synchronization-contract-route.html">U7-1 同期契約ルートパケット</a>に進んでください。同期誤差そのものを、現在の 6 つや次の監視キューを変えずに明示的なリリースブロック指標へ変える隣接行が必要な場合は、<a href="wiki/u7-2-timing-metric-route.html">U7-2 タイミング指標ルートパケット</a>、<a href="wiki/u1-2-uncertainty-calibration-route.html">U1-2 不確実性校正ルートパケット</a>、<a href="wiki/u4-2-minimal-causal-route.html">U4-2 最小因果ルートパケット</a>、<a href="wiki/u8-1-closed-loop-delay-tolerance-route.html">U8-1 閉ループ遅延許容ルートパケット</a>を続けて参照してください。同じ 6 問の行ごとの圧縮版は、<a href="wiki/mind-upload-current-public-six-rq-brief.html">現在の公開 6 ルート概要</a>を参照してください。正確な <code>Dxx + DOI</code> アンカー、first-pass KPI、各行 1 つの明示的な停止規則、EEG 主張の外に残す外部依存関係は、<a href="wiki/mind-upload-rq60-deep-focus-notes.html">ディープフォーカスノート</a>、<a href="wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html">助成金とデータセットのプレイブック</a>、<a href="wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.html">RQ ごとのディープ書類</a>、<a href="https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md">現在の資金候補リスト</a>から確認してください。
</p>
<p>
現在の 6 つを、無関係な 6 つの行としてではなく、1 つの狭いソルブファースト プログラムとして読み取る場合、順序は依然として、音声側寄与下限については <code>U13-2 → U13-5</code>、次にアイデンティティ ドリフト タイミングとしきい値下限については <code>U0-2 → U0-3</code>、次に <code>U14-4 →開示から再実行までの契約フロアの U14-2</code>。これらの最後の 4 行の下にある最もクリーンなパブリック オープン サポートは、まだバッチ自体の外に残っています。 <code>U7-1</code> は、<code>D11</code> で同期コントラクトをパブリック オープンに保ち、<code>U7-2</code> は、その同じファミリーを明示的なタイミング メトリックとリリース ブロックしきい値に変換します。 <code>U1-2</code> は、逆不確実性パケットを <code>D08</code> に基づいて維持します。そのため、サポートするインフラストラクチャ行がすでにパブリックで読み取り可能であっても、バッチは修正されたままになります。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (19:03 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@e1a7e7e2f22c</code>、<code>EEG-DATA@a7f9390492fd</code> 後の <code>2026-04-02 19:03 JST</code> での実際のプルの再読み込み<code>auto-research-funds@00cdbaa9a122</code> は依然として同じパブリック 6 と同じ実行順序を維持しています。最新の <code>mind-upload</code> ヘッドは、現在の 6 つ以外の人間の神経血管ページ上で <code>血液-CSF 関門 / 脈絡叢</code> ルート分割を深めますが、<code>EEG-DATA</code> は依然として報告しています<code>30,892</code> マージされた固有行、<code>28,855</code> 高信頼行、<code>24,880</code> <code>OSF gazx2</code> の後に直接使用可能な行<code>OpenNeuro ds007081</code> の詳細、<code>auto-research-funds</code> は依然として <code>8,590</code> 援助 ID、<code>4,301</code> 行で最新の概要を保持しています。 <code>3,951</code> 公式ソース行。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではありません。チェックされたライブ公開ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Thu, 02 Apr 2026 09:37:54 GMT</code> を返しましたが、ルートに面した文言は以前の <code>18:06 JST</code> 保持のままでした。したがって、この実行では、クレーム サーフェスを拡大するのではなく、制限されたルートホールド同期を追加するだけであることに注意してください。公式の資金提供の橋は依然として狭い（<code>蔵基金 = 2026-04-17 17:00</code>、<code>中谷財団大学院奨学金 = 2026-05-25 15:00</code>、<code>樫の目奨学金 = 2026-04-09到着</code>、<code>セコム一般研究助成金 = 終了</code>、<code>中谷財団研究助成金 = 次サイクル監視</code>)、新鮮な読み取り専用 Todoist 監査でもまだ十分なままでした (<code>items=203</code>; <code>プロジェクト=2</code>; <code>倉=2</code>; <code>中谷家=11</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>高齢化社会問題解決のためのAI解決=0</code>)。したがって、このアップデートは解決済みクレームのアップデートではなく、制限されたルートホールドの追加であり、今回の実行では新しい Todoist アイテムは正当化されませんでした。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (11:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@208e59e2180c</code>、<code>EEG-DATA@00d85380f3fd</code> 後の <code>2026-04-02 11:05 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@f4ba35518400</code> は引き続き同じパブリック 6 と同じ実行順序を維持します。最新の <code>EEG-DATA</code> は、維持されている <code> ChineseEEG-2</code> リリースとパブリック <code>auditory-eeg</code> ファミリを詳細に調べ、<code>30,887</code> マージされた一意の行を引き続きレポートします。 <code>28,850</code> の信頼性の高い行と、<code>24,875</code> すぐに使用できる行です。これにより、<code>U13-2/U13-5</code> のパブリックオープンのスピーチ側のバックアップラダーが強化されますが、それでも、<code>D10</code> を唯一の明確なパブリックオープンのプライマリアンカーとして置き換えたり、<code>U13-5</code> を制限しているリコールと妥当性のギャップを修復したりすることはできません。直接のライブアクセス再読み込みでは、現在の <code>D03/D02/D01</code> DataPort ページに <code>Subscription Required</code> および <code>LOGIN TO ACCESS DATASET FILES</code> が表示され、チェックされたライブ パブリック ページは引き続き <code>HTTP を返します。 200</code>、<code>Last-Modified: Thu, 02 Apr 2026 01:22:44 GMT</code>、公式の資金調達の橋は依然として狭いままであり、新鮮な読み取り専用の Todoist 監査で依然として十分です (<code>items=203</code>; <code>プロジェクト=2</code>; <code>倉=2</code>; <code>中谷家=7</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>日本生産技術研究所=1</code>)。したがって、この更新は、解決された要求の更新ではなく、制限されたルート保持の追加のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (11:09 JST) の最新ルート保留</strong>
<p>
<code>2026-04-02 11:09 JST</code> での、<code>mind-upload@208e59e2180c</code>、<code>EEG-DATA@00d85380f3f</code> 後の実際のプルの再読み込み。 <code>auto-research-funds@f4ba35518400</code> は引き続き同じパブリック 6 と同じ実行順序を維持します。現在の <code>mind-upload</code> ヘッドは、以前の 10:07 のルートホールド パケット リフレッシュ自体であり、<code>EEG-DATA</code> は、一般公開のスピーチ/リスニングおよび聴覚生体認証の詳細を追加すると同時に、<code>30,887</code> マージされた固有の行をレポートします。 <code>28,850</code> の信頼性の高い行、<code>24,875</code> 直接使用可能な行、および <code>auto-research-funds</code> は、現在のリポジトリ統計が維持されている間、同じ実用的な候補リストを維持します。 <code>8,585</code> 援助 ID、<code>4,293</code> 行、および <code>3,943</code> 公式ソース行。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではありません。 <code>ds007591</code> および <code>ds007602</code> は音声側のバックアップ カバレッジを強化しますが、依然としてそれぞれ 3 人の参加者のみを解放します。 <code> ChineseEEG-2</code> は読み取り/聴取アライメントの適用範囲を拡大しますが、<code>U13-5</code> の意図したリコールラベル付きブランチはまだ公開されていません。また、PhysioNet <code>auditory-eeg</code> は明らかに公開されていますが、1 日の 4 チャネル適用範囲のみであるため、置き換えられません。現在のアイデンティティ ドリフト フロアの <code>D02</code>。チェックされたライブ公開ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Thu, 02 Apr 2026 01:22:44 GMT</code> を返しました。資金調達の橋は依然として狭いままであり、新鮮な読み取り専用 Todoist 監査でも依然として十分です(<code>items=203</code>; <code>projects=2</code>; <code>蔵=2</code>; <code>中谷家=11</code>; <code>中谷卒業生奨学金=7</code>; <code>樫ノ目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>日本産業技術研究所=1</code>)。したがって、この更新は、解決された要求の更新ではなく、制限されたルート保持の追加のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (10:07 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@be507c810b11</code>、<code>EEG-DATA@3f20f48cca6e</code> 後の <code>2026-04-02 10:07 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@fb32c05163f4</code> は引き続き同じパブリック 6 と同じ実行順序を維持します。最新の <code>mind-upload</code> ヘッドは、現在の 6 つ以外の EEG 基礎設定と同等の境界を改良し、<code>EEG-DATA</code> は HBN EEG リリース 11 ルートを詳細に調べ、<code>30,887</code> マージされた固有の行を報告します。 <code>28,850</code> の信頼性の高い行、<code>24,871</code> 直接使用可能な行、および <code>auto-research-funds</code> は、現在のリポジトリ統計が維持されている間、同じ実用的な候補リストを維持します。 <code>8,585</code> 援助 ID、<code>4,293</code> 行、および <code>3,943</code> 公式ソース行。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではありません。行レベルの読み取りは、その変更されていないバッチ内でさらに 1 ステップ強化されるだけです。 <code>U13-5</code> には、表示される <code>D03</code> メタデータがまだリコールラベルの付いたパッケージではなく、<code>U14-4/U14-2</code> がまだ保持されているため、明示的なリコール有効性の警告が依然として含まれています。 <code>D13</code> は、現在の <code>D01</code> 公開フロアを超える最初の一般公開再実行サポート ファミリーです。チェックされたライブ公開ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Thu, 02 Apr 2026 00:15:06 GMT</code> を返しました。資金調達の橋は依然として狭いままであり、新鮮な読み取り専用 Todoist 監査でも依然として十分です(<code>items=203</code>; <code>projects=2</code>; <code>蔵=2</code>; <code>中谷家=11</code>; <code>中谷大学院奨学金=7</code>; <code>樫野目=2</code>; <code>セコム=3</code>; <code>脳科学財団=8</code>; <code>大川=2</code>; <code>日本生産技術研究所=1</code>;したがって、この更新は、解決された要求の更新ではなく、制限されたルート保持の追加のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (09:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@d7f30648fc40</code>、<code>EEG-DATA@ac8cc6fc8e74</code> 後の、<code>2026-04-02 09:05 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@31ec17305f6a</code> は依然として同じパブリック 6 と同じ執行順序を維持しています。最新の <code>mind-upload</code> ヘッドは、現在の 6 つ以外の文献ミエリンルート分割を強化し、<code>EEG-DATA</code> は <code>merged_unique=30886</code> を報告するようになりました。 <code>high_confidence=28849</code>、および <code>access_counts_high.immediate=24500</code>、および <code>auto-research-funds</code> は、<code>Aoi 大学院奨学金</code> / <code>JSSF 研究助成</code> は、実用的な内容を変更することなく、<code>8,585</code> 支援 ID、<code>4,293</code> 行、および <code>3,943</code> の公式ソース行に README 統計の更新を加えてマージします。候補者リスト。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、チェックされたライブ公開ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Wed, 01 Apr 2026 23:29:12 を返しました。 GMT</code>、そして公式の資金提供の橋はまだ狭いままです。<code>クラ基金</code>は<code>2026-04-17 17:00</code>まで開いており、<code>中谷財団大学院奨学金</code>は引き続き開いています。 <code>2026-05-25 15:00</code>、<code>中谷財団研究助成金</code>は引き続き次のサイクルに注目し、<code>樫の目奨学金</code>は依然として公式ページに年次<code>1月中旬から</code> 枠は 4 月初旬、<code>セコム一般研究助成金</code> は現在のサイクルでは終了したままです。新しい読み取り専用 Todoist 監査でも十分です (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>中谷大学院奨学金=7</code>; <code>樫野目=2</code>; <code>セコム=3</code>)、ライブページは以前の <code>04:09 JST</code> / <code>03:08 JST</code> はこのソース同期の前に再読み込みされるため、この更新はエントリ ページのパブリック ルート ホールドの文言を更新するだけで、解決された要求の更新ではなく、制限されたルート設定の付録のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (04:09 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@92d1547bfeb9</code>、<code>EEG-DATA@2e3799a174d9</code> 後の、<code>2026-04-02 04:09 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@f5f55bcbf724</code> は引き続き同じパブリック 6 と同じ実行順序を維持します。最新の <code>mind-upload</code> ヘッドは、現在の 6 つ以外の初心者分子メンテナンス ファミリを分割し、<code>EEG-DATA</code> は <code>merged_unique=30877</code> を報告するようになりました。 <code>high_confidence=28840</code>、<code>access_counts_high.immediate=24492</code>、および <code>auto-research-funds</code> は、実質的な最終候補リストを変更せずに 4 月 2 日の資金更新を繰り越します。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、チェックされたライブ公開ページは引き続き <code>HTTP/2 200</code> と <code>Last-Modified: Wed, 01 Apr 2026 18:24:31 GMT</code> を返しました。そして、公式の資金提供の橋は依然として狭いままです。<code>蔵基金</code>は<code>2026-04-17 17:00</code>まで、<code>中谷財団大学院奨学金</code>は<code>2026-05-25まで引き続き募集中です。 15:00</code>、<code>中谷財団研究助成</code>は次のサイクル監視のまま、<code>セコム一般研究助成</code>は現在のサイクルで終了したまま、<code>樫の目奨学金</code>は支援側滑走路としてのみ残ります。新しい読み取り専用 Todoist 監査でも十分です (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>) なので、このソース同期はエントリ ページのパブリック ルート ホールドの文言を更新するだけであり、解決された要求の更新ではなく、制限されたルート設定の付録のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (03:08 JST) の最新ルート保留</strong>
<p>
<code>2026-04-02 03:08 JST</code> での実際のプルの再読み込み (<code>mind-upload@d391dbede29e</code>、<code>EEG-DATA@f9df9ba85a6</code>)、および<code>auto-research-funds@95f804055809</code> は依然として同じパブリック 6 と同じ実行順序を維持しています。最新の <code>mind-upload</code> は、現在の 6 つ以外の ECM / PNN 文献ルートをヘッド スプリットし、<code>EEG-DATA</code> は、2 つの即時アクセスの詳細な候補 (<code>10.48804/NV4RGL</code> および<code>10.7281/T1/B660D2</code>) は、現在のアンカー ファミリを置き換えることなく、<code>auto-research-funds</code> は、実質的な候補リストを変更することなく、Gakusho / NII 資金の統合と README 統計の更新を追加します。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、チェックされたライブ公開ページは引き続き <code>HTTP/2 200</code> と <code>Last-Modified: Wed, 01 Apr 2026 17:27:08 GMT</code> を返しました。そして公式の資金調達窓口は依然として同じ狭い橋を維持している。新しい読み取り専用 Todoist 監査でも十分です (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>) なので、このソース同期はエントリ ページのパブリック ルート ホールドの文言を更新するだけであり、解決済みのクレームの更新ではなく、制限されたルート設定の付録のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 2 日 (00:03 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@cff3abab58e8</code>、<code>EEG-DATA@a885ef3f029d</code> 後の <code>2026-04-02 00:03 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@0f60872538dc</code> は依然として同じパブリック 6 と同じ実行順序を維持しています。最新の <code>mind-upload</code> ヘッドは、現在の 6 つ以外の重水素動作点の文言を強化し、<code>EEG-DATA</code> は <code>DANDI 001187</code> の詳細を追加し、レポートを作成しました。 <code>merged_unique=30875</code>、<code>high_confidence=28838</code>、<code>access_counts_high.immediate=24492</code>、<code>自動研究資金</code>実際の候補リストを置き換えることなく、<code>Isono</code>/<code>Okabe</code> リフレッシュを引き継ぎます。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、チェックされたライブ公開ページは引き続き <code>HTTP 200</code> と <code>Last-Modified: Wed, 01 Apr 2026 14:17:54 GMT</code> を返しました。公式の資金調達窓口は依然として同じ狭い橋を維持しています。新しい読み取り専用 Todoist 監査でも十分です (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>nakatani family=11</code>; <code>nakatani大学院奨学金=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>) そのため、このソース更新は、解決された要求の更新ではなく、制限付きのルート設定の補遺のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 1 日 (22:05 JST) の最新ルート保留</strong>
<p>
<code>2026-04-01 22:05 JST</code> での、<code>mind-upload@84e5337</code>、<code>EEG-DATA@bbb8d6c63d7</code> 後の実際のプルの再読み込み。 <code>auto-research-funds@5ff33413e</code> は依然として同じパブリック 6 と同じ実行順序を維持しています。最新の <code>mind-upload</code> ヘッドは、現在の 6 つのドアの外にある玄関のクリアランス ルート ラベルを明確にし、<code>EEG-DATA</code> は、<code>merged_unique=30873</code> を維持しながら詳細なメタデータを更新します。 <code>high_confidence=28836</code>、<code>access_counts_high.immediate=24487</code>、<code>auto-research-funds</code> には、<code>山岡大学院奨学金</code> スナップショット プラスが追加されます。 README に表示される統計は、実際の候補リストを変更せずに更新されます。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、チェックされたライブ公開ページは依然として <code>HTTP/2 200</code> と <code>Last-Modified: Wed, 01 Apr 2026 12:13:54 GMT</code> を返しました。そして公式の資金調達窓口は依然として同じ狭い橋を維持している。新しい読み取り専用 Todoist 監査でも十分です (<code>items=203</code>; <code>Kura=2</code>; <code>中谷家=11</code>; <code>中谷大学院奨学金=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>) であるため、このソース更新は、解決された要求の更新ではなく、制限されたルート設定の補遺のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 1 日 (18:05 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@9984d0b</code>、<code>EEG-DATA@5fc1df00f07</code> 後の <code>2026-04-01 18:05 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@d7092c8e9</code> は依然として同じパブリック 6 と同じ執行順序を維持しています。最新の <code>mind-upload</code> ヘッドは、ウェアラブル <code>OPM / MEG</code> のルート同期と現在の 6 つ以外の測定スタックの明確化、<code>EEG-DATA</code> の継続的追跡 EEG BCI の詳細レポートを追加します。 <code>merged_unique=30873</code>、<code>high_confidence=28836</code>、<code>access_counts_high.immediate=24486</code>、および<code>auto-research-funds</code> は、最近の繰越奨学金の更新後も同じ実用的な候補者リストを保持しています。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、ライブ公開ページは依然として <code>200</code> と <code>Last-Modified: Wed, 01 Apr 2026 08:22:51 を返します。 GMT</code>、そして公式の資金調達窓口は依然として同じ狭い橋を維持しています。新しい読み取り専用 Todoist 監査でも十分です (<code>items=203</code>; <code>Kura=2</code>; <code>中谷家=11</code>; <code>中谷大学院奨学金=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>) なので、これは解決された要求の更新ではなく、制限されたルート設定の更新のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 1 日 (17:06 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@c5a0550</code>、<code>EEG-DATA@82893f6ca6e</code> 後の <code>2026-04-01 17:06 JST</code> での実際のプルの再読み込み<code>auto-research-funds@ec6f7d068</code> は引き続き同じパブリック 6 と同じ実行順序を維持します。最新の <code>mind-upload</code> ヘッドは、現在の 6 つ以外のアストロ サイト PET ルート分割を深め、<code>EEG-DATA</code> は KMI EEG データセットを詳細に調べ、<code>merged_unique=30871</code> を報告します。 <code>high_confidence=28834</code>、<code>access_counts_high.immediate=24484</code>、<code>auto-research-funds</code> により、<code>Megachips 2026 奨学金</code> が追加されます。実際の候補リストを変更することなく、スナップショットと README 統計を更新します。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、ライブ公開ページは依然として <code>Last-Modified: Wed, 01 Apr 2026 07:16:09 GMT</code> の <code>200</code> を返し、公式の資金調達窓口も同様です。狭い橋は今もそのままです。新しい読み取り専用の Todoist 監査でも十分です (<code>items=203</code>; <code>Kura=2</code>; <code>中谷家=11</code>; <code>中谷大学院奨学金=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>) なので、これは解決された要求の更新ではなく、制限されたルート設定の更新のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 1 日 (14:08 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@ccef40f</code>、<code>EEG-DATA@deefd5f95c6</code> 後の <code>2026-04-01 14:08 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@f5f76c485</code> は、同じパブリック 6 と同じ実行順序を維持します。更新された <code>EEG-DATA</code> ヘッドは、<code>merged_unique=30869</code>、<code>high_confidence=28832</code> を報告するようになりました。 <code>access_counts_high.immediate=24482</code> と、その新しい実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールドを含む <code>18,312 / 28,832</code> 行をカバーするようになりました。これらの利点は、<code>D10/D03/D02/D01</code> を置き換えるのではなく、ルートのサポートをさらに強化します。ルート セーフ アクセスの読み取りも、ある特定の点で狭いままです。更新されたローカル カタログでは、引き続きカタログ側の即時行として <code>D03/D02</code> が表示され、即時/要チェックの混合ペアとして <code>D01</code> が表示されますが、ライブ アクセス読み取りは引き続き厳格であるため、<code>D10</code> <code>D03/D02/D01</code> は依然として公開文言におけるゲート付きサポート アンカーのままですが、唯一の明確なパブリック オープン プライマリ アンカーのままです。変更されていないバッチ内での行レベルの文言が若干厳しくなりました。表示される <code>D03</code> メタデータは依然としてリコール固有のラベルを公開せず、表示される <code>D01</code> パッケージの内容は依然として再実行ベンチマークではなくレイテンシ/同期フロアとして読み取られるため、<code>U13-5</code>明示的なリコールの有効性に関する警告を維持し、<code>U14-4/U14-2</code> を最初の公開再実行サポート ファミリとして <code>D13</code> を維持します。ライブ公開ページは依然として <code>200</code> を返し、現在は <code>Last-Modified: Wed, 01 Apr 2026 04:20:02 GMT</code> を共有しています。公式の資金ブリッジはまだ変更されておらず (<code>蔵基金</code>、<code>中谷財団大学院奨学金</code>、<code>樫の目奨学金</code>、<code>セコム総合研究助成金</code>終了)、新しい読み取り専用の Todoist 同期によりルートが表示されます。すでに取り上げています (<code>items=203</code>、<code>蔵=2</code>、<code>中谷家=11</code>、<code>樫の目=2</code>、 <code>Secom=3</code>) なので、このページでは依然として、解決された要求の更新ではなく、制限されたルート設定の更新について説明します。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 1 日の最新ルート保留</strong>
<p>
<code>mind-upload@aa21ab9855c1</code>、<code>EEG-DATA@cccd137a3468</code> 後の <code>2026-04-01 11:06 JST</code> でのプル後の再読み込み。 <code>auto-research-funds@3a691196cb9f</code> は、同じパブリック 6 と同じ実行順序を維持します。最新の <code>EEG-DATA</code> 変更により、リポジトリ全体のメタデータが強化され、更新された概要では <code>merged_unique=30866</code>、<code>high_confidence=28829</code> がレポートされるようになりました。現在の<code>auto-research-funds</code> ヘッドは、実際の候補リストを変更せずにリポジトリレベルの統計を更新します。ルートセーフ アクセスの読み取り値も狭いままです。<code>D10</code> は唯一の明確なパブリック オープン プライマリ アンカーのままですが、<code>D03/D02/D01</code> はゲート サポート アンカーのままです。ライブ公開ページでは依然として <code>200</code> と <code>issue.html</code> が同じ順序で同じ 6 つの名前を返しているため、このページでは、解決されたクレームではなく、限定されたルート設定の更新について説明し続けます。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 1 日 (14:09 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@ccef40f2f7cf</code>、<code>EEG-DATA@deefd5f95c6d</code> 後の、<code>2026-04-01 14:09 JST</code> での実際のプルの再読み込み。 <code>auto-research-funds@f5f76c485ccb</code> は依然として同じパブリック 6 と同じ実行順序を維持しています。最新の <code>mind-upload</code> ヘッドは、現在の 6 つ以外のシナプス前解放機構の上限を明確にし、<code>EEG-DATA</code> は Mendeley EEG メタデータを深め、<code>merged_unique=30869</code> を報告するようになりました。 <code>high_confidence=28832</code>、<code>access_counts_high.immediate=24482</code>、および <code>auto-research-funds</code> はリポレベルの統計のみを更新します。これらの変更はいずれも <code>D10/D03/D02/D01</code> を置き換えるものではなく、ライブ公開ページは引き続き <code>200</code> と <code>Last-Modified: Wed, 01 Apr 2026 04:20:02 GMT</code> を返し、公式の資金調達窓口も同様です。狭い橋は今もそのままです。新しい読み取り専用の Todoist 監査でも十分です (<code>items=203</code>; <code>Kura=2</code>; <code>中谷家=11</code>; <code>Kasinome=2</code>; <code>Secom=3</code>) なので、これは解決された要求の更新ではなく、制限されたルート設定の更新のままです。
</p>
</div>
<div class="note-box">
<strong>2026 年 4 月 1 日 (12:06 JST) の最新ルート保留</strong>
<p>
<code>mind-upload@9f4bc8e760b1</code>、<code>EEG-DATA@1324f9e1ae2b</code> 後の <code>2026-04-01 12:06 JST</code> での 2 回目の no-opactual-pull 再読み込み。 <code>auto-research-funds@6548b1650535</code> は依然として同じパブリック 6 と同じ執行順序を維持しています。最新の <code>EEG-DATA</code> ヘッドは、<code>merged_unique=30867</code>、<code>high_confidence=28830</code> を報告するようになりました。 <code>access_counts_high.immediate=24480</code> ですが、これはアンカーの置き換えではなくメタデータの深化であるため、現在のパブリック ファミリーは <code>D10 / D03 / D02 / D01</code> のままで、次の監視順序は <code>U7-1 / U1-2 / U4-2 / のままです。 U8-1</code>。ブラウザ レベルのライブ再チェックでは、<code>issue.html</code>、パブリック 6 ブリーフ、解決可能性ブリッジ、および <code>U8-1</code> ルート ページの <code>200</code> が返され、<code>Last-Modified: 01 年水曜日でした。 2026 年 4 月 02:26:28 GMT</code> がこれらの公開サーフェスに表示されます。公式の資金調達ページでは、依然として同じ狭い橋が開いているか監視ステータスで固定されています: <code>Kura Fund = 2026-02-02 - 2026-04-17 17:00</code>, <code>中谷財団大学院奨学金 = 2026-04-01 - 2026-05-25 15:00</code>、<code>樫の目奨学金 = 2026-01-14 - 2026-04-09</code>、<code>セコム総合研究助成金</code>は、現在のサイクルでは引き続き終了します。したがって、この再読み込みでは、解決されたクレームやバッチ切り替えは追加されません。現在のルートを公共の安全かつ最新の状態に保つだけです。
</p>
</div>
<div class="note-box">
<strong>理解はしているが、作業を開始するかどうかわからない場合</strong>
<p>
トピックの理解、ソースと条件の確認、変更の準備の違いについてのステップバイステップのガイドが必要な場合は、<a href="wiki/understanding-vs-action-readiness.html">Wiki: 理解と行動の準備の違い</a> を参照してください。
</p>
</div>
<div class="note-box">
<strong>研究ノート、提案書、問題の役割の間で混乱している場合</strong>
<p>
このページは、今ここで処理できるタスクの入り口であるため、理論メモや提案整理表とは役割が異なります。事実、仮説、提案、実装タスクの違いを 1 ページにまとめたい場合は、<a href="wiki/facts-hypotheses-proposals-and-tasks.html">Wiki: 事実、仮説、提案、および実行タスク</a> を参照してください。
</p>
</div>
<div class="note-box">
<strong>外部依存関係の分離に行き詰まった場合</strong>
<p>
治験審査委員会、実験、設備、法的事項が絡む場合でも、必要な仕様、判定条件、公開ログフォーマットを社内で事前に準備することが可能です。このリポジトリで使用される分離ルールについては、<a href="wiki/internal-prework-and-external-dependencies.html">Wiki: 内部事前作業と外部依存関係</a> を参照してください。
</p>
</div>
<div class="note-box">
<strong>ドキュメントを読んだ後、問題に投稿するまでの流れを確認したい場合</strong>
<p>
論文や文献マップを読んだ後、どの未解決の問題に戻り、どのような条件でそれを問題として提起すべきかを確認したい場合は、<a href="wiki/literature-to-action-route.html">Wiki: 文献から実装および参加への直線的なパス</a> を参照してください。
</p>
</div>
<div class="note-box">
<strong>このページの次のページを決めたいとき</strong>
<p>
参加したいが、小さな修正を行うべきか、条件設計に移行するべきか、外部依存関係を分解すべきかわからない場合は、<a href="wiki/participation-next-routes.html">Wiki: 参加/コラボレーション ページ</a> 後の 5 つのルートを参照してください。
</p>
</div>
<div class="note-box">
<strong>読んだ内容をどのアーティファクトに返せばよいかわからない場合</strong>
<p>
読んだ内容を文献の整理、理論の更新、提案、問題、または外部依存タスクに変換するための全体的なフローが必要な場合は、<a href="wiki/reading-to-change-workflow.html">Wiki: 読書を変更に接続する</a> を参照してください。
</p>
</div>

<section class="section" id="first-contribution-guide">
<h2 class="section-title">最初のステップを決定するためのクイックガイド</h2>
<table class="data-table">
<thead>
<tr>
<th>こんなときは</th>
<th>最初に行うべきこと</th>
<th>次のページ</th>
</tr>
</thead>
<tbody>
<tr>
<td>文章は難しいですが、つまずいた箇所を指摘できます</td>
<td>どのページ、段落、または用語がブロックされたかを問題に記入してください。</td>
<td><a href="glossary.html">用語集</a> / <a href="faq.html">FAQ</a></td>
</tr>
<tr>
<td>主張はありますが、成功条件や反証条件がわかりません</td>
<td>何が進捗とみなされるのか、何が失敗とみなされるのか、両方を指摘してください。</td>
<td><a href="verification.html">検証</a> / <a href="tech_roadmap.html">ロードマップ</a></td>
</tr>
<tr>
<td>新しい論文/記事/データを見つけました</td>
<td>コンテンツを要約する前に、コンテンツを既存のページのどこに統合するかを決定します。</td>
<td><a href="research_harvest_50.html">リサーチハーベスト</a> / <a href="datasets.html">データセット</a></td>
</tr>
<tr>
<td>タイプミス、リンク切れ、または小さな文言の修正はすぐに行うことができます</td>
<td>修正をプル リクエストとして送信し、必要に応じてページの役割を明確にする一文を追加します。</td>
<td><a href="content_hub.html">コンテンツ ハブ</a></td>
</tr>
<tr>
<td>実験、治験審査委員会、設備、または法的審査を必要とする仕事を続けたい</td>
<td>現在実行できる準備作業を、真の外部依存関係から分離します。</td>
<td><a href="issue.html#external-collaboration">外部依存関係/コラボレーション句</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="status-label-guide">
<h2 class="section-title">状態ラベルの読み方</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベル</th>
<th>日常用語</th>
<th>まだ確認事項がある</th>
</tr>
</thead>
<tbody>
<tr>
<td>反映済み (ドキュメント)</td>
<td>このステータスはサイトのテキストに反映されています。</td>
<td>すべてのコード、公開データ、評価ログが利用可能であることを保証するものではありません。</td>
</tr>
<tr>
<td>提案</td>
<td>変更のデザインはテキストにあります。</td>
<td>実装またはサードパーティによる検証がまだ行われていない可能性があります。</td>
</tr>
<tr>
<td>提案受理(文書)</td>
<td>提案は受け入れられ、本文に組み込まれました。</td>
<td>再現性基準を満たすアーティファクトは引き続き別途必要です。</td>
</tr>
<tr>
<td>検討中の提案</td>
<td>これは現在有力なアイデアとして扱われていますが、確定したものではありません。</td>
<td>内容は、反論、代替案、または実現可能性チェックの後でも変更される可能性があります。</td>
</tr>
<tr>
<td>実施方針の反映(文書)/実施計画(文書)</td>
<td>実装の方向性と手順はテキストでまとめられています。</td>
<td>実用的なコードと検証結果の公開は、引き続き別のタスクとなります。</td>
</tr>
<tr>
<td>設計完了 (実装コードは未公開)</td>
<td>このアイデアは安定していますが、外部再テスト パスはまだありません。</td>
<td>L0 を再現するには、コード、データ、プロシージャを公開する必要があります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="good-issue-minimum">
<h2 class="section-title">高価値の問題の最小要件</h2>
<table class="data-table">
<thead>
<tr>
<th>アイテム</th>
<th>短い号でも含めるべき内容</th>
<th>それが重要な理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>どこで止まった</strong></td>
<td>ページ、セクション、段落、用語など、読者が行き詰まった正確な場所。</td>
<td>これにより、漠然とした「わかりにくい」という不満だけが残るのではなく、修復目標が具体的になります。</td>
</tr>
<tr>
<td><strong>足りないもの</strong></td>
<td>ギャップとはどのようなものですか: 不十分な定義、不十分な証拠、不明確な条件、または欠落しているステータスラベル。</td>
<td>ギャップのタイプを知ると、テキストの追加と構造の修正を区別しやすくなります。</td>
</tr>
<tr>
<td><strong>達成条件</strong></td>
<td>問題が改善されたとみなされるためには、何を追加または変更する必要があるかを一文で述べてください。</td>
<td>これにより、未解決の問題が減り、修正がいつ完了するかを判断しやすくなります。</td>
</tr>
<tr>
<td><strong>反証条件</strong></td>
<td>クレームや提案を拒否する結果となる所見や条件を述べてください。</td>
<td>このサイトでは、より強力な提案には、その提案が間違っていると判断するためのより明確な条件が必要です。</td>
</tr>
<tr>
<td><strong>外部依存性の有無</strong></td>
<td>リポジトリ内で今すぐ修正できるか、それとも IRB、実験、設備、または外部の合意が必要かどうかを区別します。</td>
<td>これにより、すぐに実行可能な変更が、別のトラックを必要とするタスクと混合されるのを防ぎます。</td>
</tr>
</tbody>
</table>
</section>

<!-- Contribution Methods -->
<section class="section">
<h2 class="section-title">貢献方法</h2>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>問題を作成する (ディスカッション)</h4>
<p>新しいアイデアの提案、バグの報告、理論についての議論はすべて GitHub Issues で行ってください。 </p>
<div class="tag-list">
<span class="tag">バグレポート</span>
<span class="tag">機能リクエスト</span>
<span class="tag">質問</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>プル リクエストの送信 (実装)</h4>
<p>コードの修正とドキュメントの改善は、プル リクエストを通じて受け付けられます。フォークしてブランチを作成し、変更を提案してください。 </p>
</div>
</div>
</div>

<div class="cta-box">
<h4>貢献を開始</h4>
<p>GitHub Issue を作成してディスカッションに参加してください。 </p>
<a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">問題を開く</a>
</div>
</section>

<!-- Resolved Issues -->
<section class="section">
<h2 class="section-title">解決されたマイルストーン</h2>
<p>コミュニティの貢献により主要な問題が解決されました。 </p>

<div class="key-points">
<h4>設計完了 (実装コードは未公開)</h4>
<ul>
<li><strong>問題 #10:</strong> MU シミュレーションと LLM シミュレーション間の判別基準 (予測不可能性、自己更新性、因果的応答性) の 3 軸ベンチマーク — <em>設計ドキュメントが完成しました。再現可能な実装コード、テストデータ、評価結果は公開されていません。 </em></li>
<li><strong>課題 #12:</strong> 境界問題に対するグリアおよび代謝指標を含むハイブリッド測定プロトコル — <em>概念設計が完了。プロトコルの詳細、必要な機器リスト、パイロットデータはまだ入手できません。 </em></li>
<li><strong>問題 #34:</strong> M8 品質管理 (QC) メトリクスの JSON ログ出力関数 — <em>スキーマ設計が完了しました。実装コードはリポジトリに反映されていません。 </em></li>
<li><strong>問題 #43:</strong> R2 経験的ベイズソース推定と不確かさの定量化 (信頼区間) — <em>理論的枠組みが文書化されています。 <code>02_source_imaging.py</code> の実装コードは公開されていません。 </em></li>
</ul>
</div>
<div class="note-box">
<strong>透明性に関するメモ</strong>
<p>
上記問題はサイト上で文書レベルで対処されていますが、第三者が再現・検証できる形（実行コード、テストデータ、評価結果）として公開されていません。本プロジェクトで定める再現性基準（L0：第三者による再現性）を満たすためには、これらの実装を公開する必要があります。
</p>
</div>
</section>

<section class="section" id="technical-issue-tracker">
<h2 class="section-title">Technical Issue Tracker (統合テキスト)</h2>
<p>
技術提案課題への対応状況は以下の通りです。各ステータスの根拠は、研究ノートの統合提案概要セクションに直接リンクされています。
</p>

<table class="data-table">
<thead>
<tr>
<th>問題</th>
<th>互換性のあるコンテンツ (概要)</th>
<th>ステータス</th>
<th>理由リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#46</strong></td>
<td>測定 QA、同期補正、アーティファクト除去、BIDS/Motion-BIDS 統合ポリシーを整理する</td>
<td>提案</td>
<td><a href="perspective.html#proposal-46">#46 観点から見た概要</a></td>
</tr>
<tr>
<td><strong>#47</strong></td>
<td>BIDS 標準化、ASR/ZapLine、wPLI/STE、LSL 同期の強化された実装ポリシー</td>
<td>提案受理(文書)</td>
<td><a href="perspective.html#proposal-47">#47 観点から見た概要</a></td>
</tr>
<tr>
<td><strong>#48</strong></td>
<td>OPM-MEG、転移学習、チームフロー因果関係、IIT実装拡張提案を提出</td>
<td>検討中の提案</td>
<td><a href="perspective.html#proposal-48">#48 観点から見た概要</a></td>
</tr>
<tr>
<td><strong>#56</strong></td>
<td>反事実の区別不能性を実現するための PCI と do-calculus を導入した検証設計への変更</td>
<td>提案</td>
<td><a href="perspective.html#proposal-56">#56 観点から見た概要</a></td>
</tr>
<tr>
<td><strong>#58</strong></td>
<td>NESS 散逸、因果関係特定可能性、IIT 近似計算の 3 つの問題に対する設計ポリシーを明確化</td>
<td>提案</td>
<td><a href="perspective.html#proposal-58">#58 観点から見た概要</a></td>
</tr>
<tr>
<td><strong>#61</strong></td>
<td>現在展開されている問題、2 層の熱力学コスト、SCM の厳密性、およびマルチモデル推論の修正</td>
<td>実装方針の反映 (文書)</td>
<td><a href="perspective.html#proposal-61">#61 観点から見た概要</a></td>
</tr>
<tr>
<td><strong>#62</strong></td>
<td>#58 の批判に応じた同値クラスの警告と IIT 近似の実装計画の追加強化</td>
<td>実装計画(文書)</td>
<td><a href="perspective.html#proposal-62">#62 観点から見た概要</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>運用ルール</strong>
<p>
このトラッカーはサイト内で確認できる軌跡のみを更新します。実験、法的審査、機器調達などの外部実装作業は外部依存として分離され、ここで完了したとは主張されません。
</p>
</div>
</section>

<section class="section" id="proposal-integration">
<h2 class="section-title">技術提案書の統合テキスト</h2>
<p>
古い <code>proposals.md</code> の主要なポイントがこのセクションに統合されました。ここでは、提案のステータス、根拠、実装への影響を、問題の経路から切り離すことなく追跡できます。
</p>

<table class="data-table">
<thead>
<tr>
<th>ステータス</th>
<th>意味</th>
<th>残りの確認</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>提案書の公開</strong></td>
<td>テキストとして公開され、レビューが可能です。</td>
<td>その有効性と優先度はまだ評価が必要です。</td>
</tr>
<tr>
<td><strong>提案は承認されました</strong></td>
<td>政策として取り入れる価値があると判断しました。</td>
<td>実装方法、評価条件、公表形式についてはまだ検討の必要があります。</td>
</tr>
<tr>
<td><strong>実装ポリシーの反映</strong></td>
<td>そのアイデアはテキストとデザインに反映されています。</td>
<td>再テストできるコード、データ、評価結果は別途必要です。</td>
</tr>
<tr>
<td><strong>外部依存関係</strong></td>
<td>実験、設備、法的審査、パートナー契約など、リポジトリ外の条件が必要です。</td>
<td>このリポジトリ内では、まず要件仕様、判定条件、ログ形式が用意されます。</td>
</tr>
</tbody>
</table>

<div class="note-box" id="stream-e-rigor">
<strong>ストリーム E: より厳格な提案の立場</strong>
<p>
問題 #257 から #260 は、逆問題の不確実性、因果的等価クラス、熱力学的一貫性、欠落している BIDS セマンティクスの処理をまとめて強化します。本文側では、変更は<a href="verification.html#verification-rigor-2026-02">追加検証要件</a>、<a href="verification.html#thermodynamic-verification">熱力学検証要件</a>、および<a href="verification.html#causal-perturbation-suite">因果摂動スイート</a>に反映されます。問題点に関しては、このセクションではそれらの変更の根拠を追跡し、外部依存関係を分離します。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>テクノロジー ストリーム</th>
<th>主な焦点</th>
<th>本文中の訪問先</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>測定/同期/BIDS</strong></td>
<td>QA、同期補正、およびメタデータの標準化を測定証跡として修正します。</td>
<td><a href="perspective.html#proposal-46">視点 #46</a> / <a href="perspective.html#proposal-47">#47</a></td>
</tr>
<tr>
<td><strong>前処理/接続</strong></td>
<td>ASR、ZapLine、wPLI、STE、および関連ツールを同等の前処理およびメトリック システムとして扱います。</td>
<td><a href="perspective.html#proposal-47">視点 #47</a></td>
</tr>
<tr>
<td><strong>介入/因果関係</strong></td>
<td>観察だけでは十分ではないため、このストリームは PCI と介入設計をグラウンドトゥルース側に押し上げます。</td>
<td><a href="perspective.html#proposal-56">視点 #56</a></td>
</tr>
<tr>
<td><strong>熱力学/識別可能性</strong></td>
<td>因果関係の特定可能性を同時に監査しながら、論理コストを散逸コストから分離します。</td>
<td><a href="perspective.html#proposal-58">視点 #58</a> / <a href="perspective.html#proposal-61">#61</a> / <a href="perspective.html#proposal-62">#62</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="recent-issue-responses">
<h2 class="section-title">最新号 (#257 ～ #263) と互換性があります</h2>
<p>
次の表は、2026 年 2 月後半に追加された問題がどのように処理されたかを記録しています。 「このパスで実行された変更」と「外部依存関係としてまだ保留中の項目」を明示的に分離します。
</p>

<table class="data-table">
<thead>
<tr>
<th>問題</th>
<th>リクエスト</th>
<th>今回行われる変更</th>
<th>ステータス</th>
<th>参考</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#257</strong></td>
<td>より厳密な逆問題の不確実性、因果関係の等価性、熱力学的一貫性</td>
<td>HBM 不確実性マップ、因果等価クラス、および NESS/EPR 要件を本文標準に追加</td>
<td>反映済み (ドキュメント)</td>
<td><a href="issue.html#stream-e-rigor">提案#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification#verification-rigor-2026-02</a></td>
</tr>
<tr>
<td><strong>#258</strong></td>
<td>IIT の計算複雑さの制約と熱力学的検証要件の明確化</td>
<td>PCI-ST 中央運用および熱力学 KPI (論理コスト/散逸コストの分離) を追加</td>
<td>反映済み (ドキュメント)</td>
<td><a href="issue.html#stream-e-rigor">提案#ストリーム-e-rigor</a> / <a href="verification.html#thermodynamic-verification">検証#熱力学検証</a></td>
</tr>
<tr>
<td><strong>#259</strong></td>
<td>ASR の副作用と BIDS セマンティクスの欠如への対応</td>
<td>ASR の前後に MI/PLV 監査および CogPO/NIF/主観的レポートのメタデータ要件を追加</td>
<td>反映済み (ドキュメント)</td>
<td><a href="issue.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification#verification-rigor-2026-02</a></td>
</tr>
<tr>
<td><strong>#260</strong></td>
<td>逆問題、反事実仮説、熱力学の統合の強化</td>
<td>追加 #257 ～ #259 を統合要件としてバンドルし、検証条件を再定義</td>
<td>反映済み (ドキュメント)</td>
<td><a href="issue.html#stream-e-rigor">提案#ストリームe-rigor</a> / <a href="verification.html#causal-perturbation-suite">検証#因果摂動スイート</a></td>
</tr>
<tr>
<td><strong>#261</strong></td>
<td>外部記事 URL コンテンツを追加</td>
<td>収集した文献パスに追加し、参照URLをEvidence Bankに登録</td>
<td>反映済み (ドキュメント)</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#最近の摂取-2026-02</a></td>
</tr>
<tr>
<td><strong>#262</strong></td>
<td>ScienceDirect/arXiv URL コンテンツの追加</td>
<td>証拠銀行の新しい受け入れログに 2 つの URL を追加</td>
<td>反映済み (ドキュメント)</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
<tr>
<td><strong>#263</strong></td>
<td>arXiv URL コンテンツを追加</td>
<td>arXiv ドキュメントを承認ログに追加し、確認ステータスを明確に示します</td>
<td>反映済み (ドキュメント)</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>外部依存性のため保留</strong>
<ul>
<li><strong>タスク:</strong> ヒトを対象とした TMS/tDCS 介入実験 <strong>所有者:</strong> 実験 PI <strong>前提条件:</strong> IRB の承認、設備の確保、参加者の募集 <strong>完了条件:</strong> 公開可能なデータと監査ログは事前に登録されたプロトコル</li> に基づいて取得されます。
</ul>
</div>
</section>

<section class="section" id="external-collaboration">
<h2 class="section-title">外部依存/連携候補</h2>
<p>
古い <code>collaborations.md</code> の主要なポイントは、このセクションに統合されました。ここで重要な点は、候補名そのものではなく、まず社内で準備できるものと、真に外部の同意が必要なものとを区別することです。
</p>

<table class="data-table">
<thead>
<tr>
<th>タイプ</th>
<th>このリポジトリ内でさらにできること</th>
<th>外部依存が残るもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>標準化の準備</strong></td>
<td>ドラフト仕様、比較表、ログ形式、および監査要件の定義</td>
<td>コミュニティでの採用、公式仕様への反映</td>
</tr>
<tr>
<td><strong>データ公開の準備</strong></td>
<td>BIDS 変換、QC ログ、説明、再現手順の開発</td>
<td>外部リポジトリによる権利の確認と受諾</td>
</tr>
<tr>
<td><strong>共同研究の準備</strong></td>
<td>1 ページの概要、最低限の成果物、評価設計、出版準備</td>
<td>IRB、装置、共著者契約、実験の実施</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>優先候補者</th>
<th>最小範囲</th>
<th>まず社内で作りたいもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BIDS / EEG-BIDS コミュニティ</strong></td>
<td>EEG QC ログ、同期ログ、および派生拡張機能のディスカッション</td>
<td>拡張仕様のドラフト、メタデータの例、相違点テーブル</td>
</tr>
<tr>
<td><strong>OpenNeuro</strong></td>
<td>DOI を使用した公開用の 1 つの BIDS データセットの準備</td>
<td>BIDS 変換されたサンプル、バリデーターの結果、README</td>
</tr>
<tr>
<td><strong>MOABB / NeuroTechX</strong></td>
<td>L0/L1ベンチ比較可能</td>
<td>タスク定義、ベースライン、および最低限の成果物の仕様</td>
</tr>
<tr>
<td><strong>MNE-Python</strong></td>
<td>BIDS → 前処理 → メトリクス再現パイプライン</td>
<td>チュートリアルにできる最小限のノートブック/スクリプト</td>
</tr>
<tr>
<td><strong>LSL コミュニティ</strong></td>
<td>同期監査ログの標準化</td>
<td>テンプレート、許容誤差、および障害ログの定義</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>このセクションの読み方</strong>
<p>
ここにリストされている候補は、それらが合意された、または実装にコミットしたことを意味するものではありません。今私たちがやるべきことは、要求仕様書や最低限の成果物、判断条件などを公開可能な形で準備してから相手に送付することです。
</p>
</div>
</section>

<!-- Verification Audit -->
<section class="section" id="verification-audit">
<h2 class="section-title">検証監査 (180 件の検証監査)</h2>
<p>
これらは、2026 年 2 月に実施されたすべてのサイト コンテンツの体系的な検証監査の結果です。4 つのカテゴリで 180 件の GitHub の問題を登録し、サイトの修正を通じて対応しています。
</p>

<table class="data-table">
<thead>
<tr>
<th>カテゴリ</th>
<th>問題範囲</th>
<th>症例数</th>
<th>互換性ステータス</th>
<th>主な変更点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>LIT (文献検証)</strong></td>
<td>#71–#110</td>
<td>40 アイテム</td>
<td>文書修正</td>
<td>DOI 検証、重複参照の削除 (ref-68/69/72/75)、FlyWire 2024 の追加、未検証の引用の削除</td>
</tr>
<tr>
<td><strong>THEO (理論上のギャップ)</strong></td>
<td>#111–#145</td>
<td>35 個のアイテム</td>
<td>文書修正</td>
<td>難しい問題の立場を明確にする、展開中の議論に対応する、FEP 批判を認識する、哲学的前提を表現する</td>
</tr>
<tr>
<td><strong>IMPL (実装ギャップ)</strong></td>
<td>#146–#195</td>
<td>50 アイテム</td>
<td>文書修正</td>
<td>実装状況の透明性レポート、L0未達成の明確な表示、証拠ギャップ分析、展開セクションの追加</td>
</tr>
<tr>
<td><strong>METH (方法論/最新研究)</strong></td>
<td>#196–#250</td>
<td>55 個のアイテム</td>
<td>文書修正</td>
<td>Connectome の進捗状況が更新され、代替アプローチの比較表、倫理 FAQ が追加、用語集が拡張されました (13 の用語が追加されました)</td>
</tr>
</tbody>
</table>

<div class="key-points">
<h4>主要な修正 (サイト間)</h4>
<ul>
<li><strong>perspective.md:</strong>4 つの重複した参照を削除、制限セクションを追加、FlyWire 接続を更新、Chalmers 1995</li> を追加
<li><strong>idea.md: </strong>制限事項と未解決の質問セクションを追加、Weber 2025 への DOI リンクを追加、5 つの参考資料を追加</li>
<li><strong>verification.md:</strong> 実装ステータス透明性レポートシートを追加、科学的ギャップ分析セクションを追加、MOABB/FAIR リファレンスを追加</li>
<li><strong>glossary.md:</strong>意識理論セクション (IIT/GNWT/FEP/PCI/マルコフブランケットなどの 8 用語) および実装インフラストラクチャセクション (5 用語) を追加</li>
<li><strong>faq.md: </strong>5 つの質問を追加しました: 難しい問題、コピーの問題、計算結果、倫理、他のプロジェクトとの比較</li>
<li><strong>wbe_101.md:</strong>哲学的前提比較表と代替アプローチ比較表を追加</li>
<li><strong>proposals.md:</strong>証拠のギャップセクションを追加 (ASR/OPM-MEG/do-calculus/NESS の問題の明確化)</li>
<li><strong>tech_roadmap.md:</strong>I8/I9 構造のバグを修正し、展開とガバナンス セクション (D0 ～ D3) を追加</li>
</ul>
</div>

<div class="note-box">
<strong>透明性に関するメモ</strong>
<p>
上記の変更はすべて「ドキュメント レベル」です。実行コード、テストデータ、評価結果（L0達成）の公表が別途必要であり、今回の監査では矛盾点の明確化を優先した。
</p>
</div>
</section>

<!-- Technical Critique Response -->
<section class="section" id="technical-critique">
<h2 class="section-title">Technical Critique 互換 (#64–#70)</h2>
<p>
これは、2026 年 2 月に提出された 7 件の技術的および科学的批判 (問題 #64 ～ #70) に対する回答です。共通のテーマが要約され、各ファイルに反映されています。
</p>

<table class="data-table">
<thead>
<tr>
<th>テーマ</th>
<th>対応する問題</th>
<th>変更内容</th>
<th>反映先</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT 4.0 の複雑性/展開される議論</strong></td>
<td>#64、#65、#68、#69</td>
<td>哲学的ゾンビリスクの説明、ニューロモーフィズムの必要性の強調、階層的粗視化の導入</td>
<td><a href="perspective.html#decoding-to-emulation-gap">視点</a></td>
</tr>
<tr>
<td><strong>EEG 空間分解能の限界</strong></td>
<td>#64、#66、#67、#70</td>
<td>情報理論の限界 (7 桁のギャップ) を説明し、WBE における実際の役割を再定義</td>
<td><a href="eeg_101.html#information-theoretic-limits">eeg_101</a></td>
</tr>
<tr>
<td><strong>反事実的仮想等価性の不十分</strong></td>
<td>#65、#66、#69、#70</td>
<td>3 つの指標の追加: EI、Causal Density、STE、Pearl の因果ラダーを使用した評価フレームワーク</td>
<td><a href="perspective.html#decoding-to-emulation-gap">視点</a> / <a href="verification.html#verification-rigor">検証</a></td>
</tr>
<tr>
<td><strong>NESS 熱力学接地</strong></td>
<td>#68</td>
<td>ランダウアーの制限を超える EPR 要件とフィッシャー情報の組み合わせ</td>
<td><a href="perspective.html#decoding-to-emulation-gap">視点</a></td>
</tr>
<tr>
<td><strong>DCM/ベイジアン法の制限</strong></td>
<td>#64、#65、#67、#70</td>
<td>BMR、因果フィンガープリンティング、および適応型前処理の紹介 (リーマン ポテト)</td>
<td><a href="issue.html#proposal-integration">提案</a></td>
</tr>
<tr>
<td><strong>ESI 不確かさの定量化</strong></td>
<td>#67、#69、#70</td>
<td>必須の信頼区間、適応型ASR/ZapLineプラス、前方問題誤差伝播</td>
<td><a href="eeg_101.html#esi-uncertainty">eeg_101</a> / <a href="verification.html#verification-rigor">検証</a></td>
</tr>
</tbody>
</table>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>リソース</h4>
<ul>
<li><a href="https://github.com/yasufumi-nakata/mind-upload" target="_blank">GitHub リポジトリ →</a></li>
<li><a href="perspective.html#design-principles">理論的枠組み →</a></li>
<li><a href="tech_roadmap.html">技術ロードマップ →</a></li>
</ul>
</div>

<div class="note-box">
<strong>行動規範</strong>
<p>
参加者全員が気持ちよく議論できるよう、お互いに敬意を持って接してください。科学的批判は歓迎されますが、攻撃的な言動は容認されません。
</p>
</div>

</aside>
</main>
