---
layout: default
title: 'Wiki: イベント同期と監視ログの基本'
description: イベント マーカー、イベント セマンティクス、時間同期、手動スコアリング、レポート由来のラベルの観点から、生の EEG だけでは十分ではない理由を説明します。
article_type: ウィキ
subtitle: 信号だけでなく、ラベルのソースを残さないと、比較はうまくいきません。
author: マインドアップロード研究プロジェクト
last_updated: '2026-03-28'
note: 実践ガイド
audience: EEG データの取り扱いを開始し、最低限の BIDS と QC を体験したい人
reading_time: 12～18分
page_intro: このページは、イベント マーカー、イベント セマンティクス、時間同期、手動スコアリング、レポート由来のラベルの観点から、生の EEG 波形だけでは研究で再現できない理由を説明する Wiki です。目的は、「`waveform
  files are available but cannot be compared,'' but also ``labels are available but provenance is ambiguous and cannot be
  compared,'' and `」時間が利用できるだけでなく、クロック ドメインがあいまいで比較できないことを防ぐことです。」
accuracy_note: ここで扱っているのは最小限の観察ログとラベルの来歴ですが、2026-03-28 のアップデートでは、BIDS イベント テーブル、HED セマンティクス、LSL 同期、物理タイミング検証、Motion-BIDS タイプのメタデータの役割の違いも明確にしています。各問題には追加のメタデータが必要ですが、イベント、意味、クロック
  システム、タイミング検証クラスを分離するという原則は変わりません。
page_highlights:
- 生の脳波だけでは、何が起こった瞬間の信号を伝えることができない場合があります。
- イベント マーカー、刺激ログ、同期情報は後で復元できない場合があります。
- BIDS の `events.tsv` はタイムスタンプ テーブルであり、それ自体がイベント セマンティクスではありません。
- LSL は LAN 内同期を強化しますが、デバイス内遅延または刺激提示遅延の真の値を自動的に提供するわけではありません。
- 保存されたデータ アンカー、ストリーム アライメント、デジタル トリガー キャプチャ、物理出力オンセット、および制御されていない応答タイミングは、異なるタイミング検証クラスです。
- キューオンセット、エキスパートインターバル、ヒプノグラム、レポート由来ラベルは、同じラベル付きデータであっても異なります。
- 不良チャンネルや不良セグメントの録画も証拠の一部です。
known_points:
- 波形ファイルだけでは、課題や刺激の反応を再構築するには不十分な場合があります。
- 遅延、ジッター、ドリフトを記録しないと、時間分解能における強みが損なわれてしまいます。
- BIDS/EEG-BIDS はイベントとメタデータのコンテナを提供しますが、HED のような機械可読セマンティクスは研究間での再利用に役立ちます。
- LSL とトリガー ラインを使用する場合でも、クロック ドメインとデバイス側の遅延を指定しないと時間忠実度を監査することはできません。
- BIDS のオンセットまたはサンプル インデックスは、それ自体では物理的なディスプレイ/オーディオのオンセットを証明するものではなく、デジタル トリガーだけでは制御されていない応答タイミングを証明するものでもありません。
- アノテーションの出所を書かないと、同じラベル名を再利用できない場合があります。
- 不良チャンネル/不良セグメントの記録は、除外の透明性に直接関係します。
unknown_points:
- すべての割り当てにどの程度詳細なメタデータが必要になるかについては、まだ運用設計の途中です。
- 複雑な多峰同時測定における最小同期ログをどのように統一するかが今後の課題である。
- HED / オントロジー / スコアラー ルールでイベント セマンティクスをどこまで必須にするかを調整する必要があります。
- レポート由来のラベルをシグナルのみのベンチマークからどの程度分離する必要があるかについてのサイト全体のスキーマはまだ最終決定中です。
wiki_links:
- label: 'Wiki: EEG の前処理と QC'
  url: /wiki/eeg-preprocessing-and-qc.html
  description: 観察後に結果が変化した部分を補正します。
- label: 'Wiki: 検証インフラストラクチャの基本'
  url: /wiki/verification-basics.html
  description: 丸太が公共財である理由を学びましょう。
- label: 'Wiki: 閉ループ、遅延、ジッター、安全停止'
  url: /wiki/closed-loop-latency-jitter-and-safety-stops.html
  description: L3 閉ループ評価における遅延とジッターの読み取り方法を補正します。
- label: ウィキホーム
  url: /wiki/
  description: 学習ページ全体に戻ります。
recommended_pages:
- label: 脳波検査の概要
  url: /eeg_101.html
- label: データとベンチ
  url: /datasets.html
- label: 実践
  url: /datasets.html#l0-practice
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>最短の答え</h2>
<p>
生の EEG は一連の電気信号です。しかし、研究でよく知りたいのは「<strong>いつ、どのような信号が発生する</strong>」ということです。その対応表がないと後から見ても意味が曖昧になってしまいます。
</p>
</div>

<div class="note-box">
<strong>2026-03 文献監査で追加された前提条件</strong>
<p>
このページではイベントログだけでなく、<strong>label起源</strong>も観測ログとして扱います。つまり、同じ「正しいラベル」を使ったとしても、<strong>アノテーションチャンネル</strong>なのか、<strong>エキスパートのインターバルアノテーション</strong>なのか、<strong>全夜催眠</strong>なのか、<strong>医師のレポートから導き出したラベル</strong>なのかが書かれていない限り、比較可能なベンチマークにはなりません。
</p>
</div>

<div class="note-box">
<strong>このページの主な弱点を修正する必要があります</strong>
<p>
このサイトはイベントと同期が重要であるとすでに述べていますが、それでも <strong> 時間アンカー </strong>、<strong> イベント セマンティクス </strong>、および <strong> クロック アライメント </strong> を明確に分離していませんでした。 BIDS タスク イベントは、<code>events.tsv</code> および JSON サイドカーを通じて説明的なフレームワークを提供します。 （2021）およびHermes et al。 (2025) によると、研究間の再利用には、HED</strong> などの <strong> マシン可読セマンティクスも必要です。さらに、Kothe et al. (2025) に示されているように、LSL は、デバイス内部遅延や刺激提示遅延を自動的に与えることなく、ネットワーク同期を強化できます。このため、このサイトではイベントの忠実度を 1 つのチェックボックスとして扱うのではなく、3 つの段階で監査します。
</p>
</div>

<div class="note-box">
<strong>2026-03-28 再監査: タイミング証拠にはまだラダーが必要</strong>
<p>
残りの弱点は、このページでは、読者が <strong>BIDS オンセット/サンプル フィールド </strong>、<strong>LSL アライメント </strong>、<strong>TTL マーカー </strong>、<strong> フォトダイオード トレース </strong>、および <strong> マイク / ループバック テスト </strong> を、交換可能なタイミングの証明であるかのように扱うことができることです。現在の標準および主要な文献は、その圧縮をサポートしていません。 BIDS 仕様では、画面またはスピーカーでの物理的なオンセットではなく、<strong> 最初に保存されたデータ ポイント </strong> を基準にして <code>onset</code> を定義します。ヘルメスら。 (2025) は、HED がハードウェア レイテンシの真実ではなく、マシンが動作可能なセマンティクスを鮮明にすることを示しています。コーテら。 (2025) は、LSL がクロスデバイス オフセットとジッターを補償できることを示していますが、残りのセットアップ オフセットは実際の機器でテストする必要があります。ルポーブルら。 (2024) および Bridges ら。次に、(2020) は、ソフトウェア パッケージ、オペレーティング システム、およびハードウェアの組み合わせによって遅延とジッターが大幅に変化する可能性があるため、物理的刺激の開始と応答のタイミングには外部検証が必要であることを示しました。したがって、このサイトでは、タイミング証拠を 1 つの同期チェックボックスではなく <strong> 検証ラダー </strong> として読み取るようになりました。
</p>
</div>

<section class="section" id="why-raw-is-not-enough">
<h2 class="section-title">生の脳波だけでは不十分な理由</h2>
<p>
例えば、課題中に刺激が何回現れたのか、どのタイミングでボタンが押されたのか、ノイズによりどの部分が除外されたのかなどが分からないと、同じ波形でも人によって解釈が異なります。つまり、波形だけを見ていると、何を比較しているのかが分かりにくい可能性があります。
</p>
</section>

<section class="section" id="event-markers">
<h2 class="section-title">イベントマーカーと刺激ログ</h2>
<table class="data-table">
<thead>
<tr>
<th>レコード</th>
<th></th>に必要なものは何ですか
</tr>
</thead>
<tbody>
<tr>
<td><strong>イベントマーカー</strong></td>
<td> 刺激提示、反応、状態変化などが波形上のどこに相当するかを示します。 </td>
</tr>
<tr>
<td><strong>刺激ログ</strong></td>
<td>どのような刺激が、どのような順序で、どのような条件で現れたかを記録します。 </td>
</tr>
<tr>
<td><strong>反応ログ</strong></td>
<td>被験者のボタンの押下、回答、試行の失敗などを波形と関連付けます。 </td>
</tr>
</tbody>
</table>
<p>
イベントマーカーだけがあっても、刺激の内容や状態の名称があいまいであれば、再解析することは困難です。逆に、EEG 時間とリンクしていなければ、刺激ログがあるだけでは十分ではありません。
</p>
</section>

<section class="section" id="event-fidelity-layers">
<h2 class="section-title">イベントの忠実度は 3 つのレイヤーで監査されます</h2>
<table class="data-table">
<thead>
<tr>
<th>レイヤー</th>
<th>ここを修正する必要があります</th>
<th>紛失すると起こりやすい誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1。タイムアンカー</strong></td>
<td>Cオンセット/持続時間、サンプルインデックス、クロックドメイン、刺激/応答ログとの対応。 </td>
<td>「いつその出来事が起こったのか」が曖昧になり、画期的かつ遅れた評価が崩れる。 </td>
</tr>
<tr>
<td><strong>2。イベントのセマンティクス</strong></td>
<td><code>trial_type</code>、条件名、HED タグ、手動スコアリング ルール、レポート使用フラグ。 </td>
<td>ラベル名が同じでも意味が異なり、研究横断的なメタ/メガ分析が崩れてしまいます。 </td>
</tr>
<tr>
<td><strong>3。同期とトランスポート</strong></td>
<td>Cクロックオフセット、遅延、ジッター、ドリフト、トランスポートパス、リサンプリング/スムージングの有無。 </td>
<td>LSL またはトリガーが単なるサブミリ秒のグラウンドトゥルースである場合、それを読み間違える可能性があります。 </td>
</tr>
</tbody>
</table>
<p>
BIDS タスク イベントは主に <strong> 第 1 層 </strong> を提供し、HED は <strong> 第 2 層セマンティクス </strong> を補足し、LSL は <strong> 第 3 層ネットワーク同期 </strong> をサポートします。したがって、このサイトではこれらを互換性のあるツールとして扱いません。
</p>
</section>

<section class="section" id="timing-validation-ladder">
<h2 class="section-title">タイミング検証は 1 つのボックスではなく、はしごです</h2>
<table class="data-table">
<thead>
<tr>
<th>検証クラス</th>
<th>直接修正するもの</th>
<th>まだ証明されていないこと</th>
<th>保存すべき典型的なアーティファクト</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>保存データアンカー</strong></td>
<td><code>onset</code>、<code>duration</code>、およびオプションで <code>sample</code>.</td> によって、保存されたデータ ファイル内のイベントが存在する場所を修正します
<td> は、物理的なディスプレイ/オーディオの開始、デバイスのスループット遅延、または参加者の応答タイミングを証明しません。</td>
<td><code>events.tsv</code>、<code>events.json</code>、取得開始定義、破棄サンプルルール.</td>
</tr>
<tr>
<td><strong>ストリームアライメント</strong></td>
<td>同期ストリーム全体でのクロスデバイス クロック オフセット、ドリフト、ネットワーク ジッターの処理を修正します。</td>
<td> は、ディスプレイ、スピーカー、アンプ、ボタンの実際の遅延を証明するものではありません。</td>
<td>LSL/XDF ログ、クロック ドメイン、オフセット / RTT サマリー、再同期ポリシー。</td>
</tr>
<tr>
<td><strong>取得側デジタルマーカーキャプチャ</strong></td>
<td>トリガパルスが収集システムまたはDAQ入力に到達したタイミングを修正します。</td>
<td>刺激が実際に視覚/聴覚になったとき、または参加者が実際に反応したときは証明されません。</td>
<td>TTL またはマーカー トレース、DAQ チャネル、トリガー配線マップ、マーカーとストリームの関係。</td>
</tr>
<tr>
<td><strong>物理的出力開始</strong></td>
<td>アクチュエータにおける視覚または聴覚イベントの現実世界の開始と継続時間を修正します。</td>
<td> は、主観的な知覚時間、神経処理遅延、または応答デバイスのタイミングを証明するものではありません。</td>
<td>フォトダイオード トレース、マイク トレース、オーディオ ループバック、高速カメラ、または同等のセットアップに関するメモ。</td>
</tr>
<tr>
<td><strong>制御不能な応答タイミング</strong></td>
<td>ログに記録された応答タイムスタンプと実際のボタン/キー/アクチュエータの応答の間のギャップを修正します。</td>
<td>は、刺激の開始タイミングや内部認知潜時を証明しません。</td>
<td>接触マイク、力センサー、ループバック、レスポンスボックス検証ログ。</td>
</tr>
</tbody>
</table>
<p>
このサイトでは、提出物は<strong>実際にテストされた最も高い段に</strong>という名前を付ける必要があります。 「BIDS を使用しました」と言うと、保存されたデータのアンカーが修正されます。 「LSL を使用しました」と言うと、ストリームの位置合わせが修正されます。 「TTL マーカーを送信しました」と言うと、取得側のデジタル キャプチャが修正されます。 <strong>物理的刺激の開始</strong>または<strong>真の応答タイミング</strong>に関する主張には、フォトダイオード、マイク、またはループバックなどの外部測定ラングが必要です。
</p>
</section>

<section class="section" id="label-provenance">
<h2 class="section-title">4つの異なる方法でラベルの由来を読む</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベルタイプ</th>
<th>代表例</th>
<th>それが直接表すもの</th>
<th>保持する必要がある最小限の補助ログ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>cueロックアノテーションチャンネル</strong></td>
<td>EEG モーターの動き/画像 T0 / T1 / T2</td>
<td>問題の合図とモーション/画像の開始の設計タイミング。 </td>
<td>Leave 実行 ID、タスク ID、サブジェクト ID、ビジュアル キュー条件、およびエポシング ルール。 </td>
</tr>
<tr>
<td><strong>エキスパート間隔注釈</strong></td>
<td>CHB-MIT 発作開始 / オフセット</td>
<td>長時間録画時のイベント部です。 </td>
<td>ファイルの順序、ギャップ、ケースから主題へのサポート、モンタージュの変更を残します。 </td>
</tr>
<tr>
<td><strong>手動催眠術</strong></td>
<td>Sleep-EDFのR&Kスリープステージ</td>
<td>これは一晩の粗い状態のラベルです。 </td>
<td>採点マニュアル、採点者ID、夜間・学習条件、ラベルマッピングを残します。 </td>
</tr>
<tr>
<td><strong>レポート由来/トリアージラベル</strong></td>
<td>TUH EEG / TUSZ レポートのキーワード検索と臨床医レポート</td>
<td>C臨床ラベルとトリアージ情報がセッション/ファイルに添付されます。 </td>
<td>Leave レポート使用フラグ、患者 / セッション ID、信号のみまたはマルチモーダル宣言。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="timing">
<h2 class="section-title">時間同期で注意すべき 3 つのこと</h2>
<table class="data-table">
<thead>
<tr>
<th>期間</th>
<th>意味</th>
<th>何が問題ですか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>遅延</strong></td>
<td>実際のイベントと記録の差は何msですか？ </td>
<td>刺激後の反応時間がずれるため、誤った解釈が生じます。 </td>
</tr>
<tr>
<td><strong>ジッター</strong></td>
<td>毎回の偏差はどれくらい変動しますか？ </td>
<td>平均化するとピークがぼやけ、応答が弱く見えます。 </td>
</tr>
<tr>
<td><strong>ドリフト</strong></td>
<td>長時間使用すると時計の遅れが大きくなります。 </td>
<td>時間が遅くなるほど同期誤差が大きくなります。 </td>
</tr>
</tbody>
</table>
<p>
ここでは観測ログの意味について説明します。これらが L3 閉ループ評価におけるエンドツーエンドの安定性と安全な停止にどのような影響を与えるかを知りたい場合は、<a href="closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ、遅延、ジッター、および安全な停止</a> が補足レッスンです。
</p>
</section>

<section class="section" id="lsl-scope">
<h2 class="section-title">LSL は強力ですが、ハードウェアのグラウンド トゥルースではありません</h2>
<p>
Lab Streaming Layer (LSL) は、同じ LAN 内で複数のストリームを同期し、クロック オフセットとストリーム メタデータを一貫して処理するための基盤として非常に役立ちます。コーテら。 (2025) LSL はソフトウェアベースの同期でミリ秒の精度を達成できることを示しました。ただし、同じ論文では、<strong> 入力デバイスのスループット遅延とオンデバイス処理遅延は、LSL だけでは推定または補正できないことも明らかにしています </strong>。したがって、LSL を使用する場合でも、表示遅延、音声遅延、およびアンプのバッファ遅延を個別に測定する必要があります。
</p>
<table class="data-table">
<thead>
<tr>
<th>LSL</th>を使っていても残しておいたほうがいいもの
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>タイムスタンプドメイン</strong></td>
<td> 発表用PC、取得用PC、デバイス時計のいずれを基準としているのか書かないと時差の意味がなくなってしまいます。 </td>
</tr>
<tr>
<td><strong>デバイス側遅延</strong></td>
<td>アンプ、ディスプレイ、オーディオ出力、マイクロコントローラーの内部遅延は、ソフトウェアのタイムスタンプだけでは判断できません。 </td>
</tr>
<tr>
<td><strong>ドリフト/再同期ポリシー</strong></td>
<td>長時間記録ではドリフト補正の有無により後半のアライメント誤差が変化します。 </td>
</tr>
<tr>
<td><strong>検証方法</strong></td>
<td>フォトダイオード、ループバック、TTL、共通信号入力など、遅延の推定にどの方法を使用したかを知る必要があります。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="starter-dataset-logging">
<h2 class="section-title">4 つのスターター データセットで何を記録するか</h2>
<div class="note-box">
<strong>最後の列はこのサイトの運営上の理由</strong>
<p>
以下の <strong> 読みすぎてはいけないこと </strong> 列は、公式データセットのドキュメントや一次文献に直接記載されているログの粒度からこのサイトが引いた運用上の境界を示しています。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>データセット</th>
<th>電流ロギング</th>
<th>保存すべき追加の詳細</th>
<th>深読みしてはいけないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG 運動/画像</strong></td>
<td><code>.event</code> およびアノテーション チャンネルは、T0 / T1 / T2 タグでキューロックされたオンセットを記録します。 </td>
<td>サブジェクト、実行、タスク ブロック、エポッキング ウィンドウ、および EOG / EMG 監査結果を保持します。 </td>
<td>このキューロック運動タスクを自発的思考の読み出しとして読み取らないでください。 </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td> 概要および <code>.seizure</code> 注釈は、発作間隔、事件構造、ファイル ギャップ、および代理日付を保存します。 </td>
<td>症例と被験者の関連性、ギャップの長さ、記録が連続的であるかどうか、およびモンタージュの概要を保持します。 </td>
<td>各ファイルを独立したサンプルとして扱ったり、データセットをギャップのない監視ログとして読み取ったりしないでください。 </td>
</tr>
<tr>
<td><strong>スリープ-EDF</strong></td>
<td> データセットには、R&K 催眠図、Fpz-Cz / Pz-Oz EEG、1 Hz イベント マーカーが含まれています。 </td>
<td> スコアリングマニュアル、スコアラー、スタディアーム、ナイト ID、および AASM ラベルへのマッピングルールを保持します。 </td>
<td> EEG 自体が 100 Hz でサンプリングされているという理由だけで、1 秒未満の睡眠イベント タイミングを主張しないでください。 </td>
</tr>
<tr>
<td><strong>TUH 脳波 / TUSZ</strong></td>
<td>サブセットに応じて、データセットには患者/セッション階層、EDF、臨床医レポート、および専門家の発作注釈が含まれます。 </td>
<td>レポート使用フラグ、患者/セッション分割、レポートキーワード由来のトリアージを保持します。 </td>
<td>レポート支援臨床ラベルを純粋な EEG 信号のみの結果として書き込まないでください。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="bad-records">
<h2 class="section-title">不良チャネル/不良セグメントを残す理由</h2>
<p>
ノイズが大きいチャンネルや体の動きによって壊れたセクションを除外するのが通常です。ただし、その記録がなければ、後で別の人が同じ除外を再現することはできません。
</p>
<div class="key-points">
<h4>最低限抑えておきたいこと</h4>
<ul>
<li><strong>不良チャネル:</strong>どのチャネルが不良とマークされましたか?その理由は何ですか? </li>
<li><strong>不正なセグメント:</strong>どの時間セグメントを除外しましたか? </li>
<li><strong>しきい値:</strong>除外するためにどのような基準が使用されましたか? </li>
<li><strong>修正方法:</strong>補間または破棄しましたか? </li>
</ul>
</div>
</section>

<section class="section" id="bids">
<h2 class="section-title">EEG-BIDS</h2>に必要な最小限の情報
<table class="data-table">
<thead>
<tr>
<th>アイテム</th>
<th>意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>`events.tsv`</strong></td>
<td>刺激と反応の時間と種類を残します。 </td>
</tr>
<tr>
<td><strong>`events.json` および HED</strong></td>
<td><code>trial_type</code> およびその他の列の意味を説明し、オプションで HED タグを使用してイベント セマンティクスを機械可読にします。 </td>
</tr>
<tr>
<td><strong>`channels.tsv`</strong></td>
<td>各チャンネルのステータスと種類を残します。 </td>
</tr>
<tr>
<td><strong>JSON メタデータ</strong></td>
<td>サンプリング周波数、基準方法、測定条件等はお任せください。
</tr>
<tr>
<td><strong>クロック/同期ログ</strong></td>
<td>Clockドメイン、遅延、ジッター、ドリフト、同期方法、測定方法を別ログに記録します。 </td>
</tr>
<tr>
<td><strong>`*_coordsystem.json` および拡張スキーマ</strong></td>
<td>電極、モーション センサー、またはポーズ ストリームを使用する場合は、座標系と測定の配置を第一級のメタデータとして残します。 </td>
</tr>
<tr>
<td><strong>QC / 除外ログ</strong></td>
<td>不良チャネル、不良セグメント、ノイズ、除外理由を外部ログと派生ファイルに残します。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="event-fidelity-card">
<h2 class="section-title">このサイトではイベント フィデリティ カードが必要</h2>
<p>
2026 年 3 月 28 日のサイト ルール以降、イベントを含むデータセット カードと Runbook には、少なくとも次の 6 つの項目が含まれている必要があります。重要なのは、すべてが完璧になるまで待つことではなく、欠けている部分を可視化し、どこで主張を止めなければならないかを定義することです。
</p>
<table class="data-table">
<thead>
<tr>
<th>アイテム</th>
<th>最低限含めるべき詳細</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1。イベントアンカー</strong></td>
<td>Onset / 継続時間 / サンプル、ソース ファイル、および時間が参照するクロック ドメイン。 </td>
</tr>
<tr>
<td><strong>2。イベントのセマンティクス</strong></td>
<td><code>trial_type</code>、条件定義、HED または同等の語彙、およびセマンティクスが信号のみの注釈または手動スコアリング/レポートから得られるかどうか。 </td>
</tr>
<tr>
<td><strong>3。クロックドメインとストリームアライメント</strong></td>
<td> クロック ドメイン、同期ミドルウェア (存在する場合)、オフセット/ドリフト処理、および再同期ポリシーに名前を付けます。 </td>
</tr>
<tr>
<td><strong>4。タイミング検証クラス</strong></td>
<td> タイミング証拠が、保存されたデータ アンカーのみ、デジタル マーカー キャプチャ、物理的な出力オンセット、または制御されていない応答テストから得られたものであるかどうか、測定された遅延/ジッターの概要と測定方法とともに名前を付けます。 </td>
</tr>
<tr>
<td><strong>5。来歴</strong></td>
<td>Scorer ID、スコアリングマニュアル、レポート使用フラグ、ラベルがシグナル専用かマルチモーダルか。 </td>
</tr>
<tr>
<td><strong>6。ジオメトリ/マルチモーダルメタデータ</strong></td>
<td>電極座標、座標系、および追加のモーション、ビデオ、または生理学的ストリームのフレームとスキーマ。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="cannot-recover">
<h2 class="section-title">後から復元することが困難な情報</h2>
<p>
次の情報を記録しておかないと、後で推測する必要があります。
</p>
<ul>
<li><strong>刺激提示の正確な時間:</strong>大まかな順序は置き換えることができません。 </li>
<li><strong>クロック ドメイン:</strong>タイムスタンプがどのクロックに属しているかを指定しないと、複数のストリーム間の差異を解釈できません。 </li>
<li><strong>タイミング検証クラス:</strong>数値が保存されたデータ アンカー、TTL、フォトダイオード、マイク、またはループバックからのものであるかどうかを指定しないと、同期の証拠を解釈することができなくなります。 </li>
<li><strong>実際の遅延とジッター:</strong> 機器やソフトウェアの設定が不十分な場合があります。 </li>
<li><strong>機器側遅延：</strong>LSLやトリガーを使用する場合でも、ディスプレイ、オーディオ、アンプの内部遅延を別途測定する必要があります。 </li>
<li><strong>除外理由:</strong>思い返しても、なぜ捨てたのか分かりません。 </li>
<li><strong>Lラベルの来歴:</strong>ラベルが手動スコアリングによるものかレポートから派生したルールによるものかを記録しない場合、ラベル名が同じであっても安全に比較することはできません。 </li>
<li><strong>イベントセマンティクス:</strong><code>trial_type</code>、条件名、または HED タグの意味がない場合、同じ名前が異なる条件である可能性があります。 </li>
<li><strong>スコアリングマニュアル/スコアラー:</strong>Sleep-EDFのような手動ヒプノグラムは、参照とスコアラーを失うと再利用のために意味が変わります。 </li>
<li><strong>レポート使用フラグ:</strong>TUH スタイルのデータセットでは、そうしないと、ラベルがレポートに依存しているのか、信号のみの処理から来たのかを後から判断することができません。 </li>
<li><strong>座標系とセンサー フレーム:</strong> モーションとポーズを追加してもフレームを離れることはできないため、マルチモーダル統合は再利用できなくなります。 </li>
<li><strong>現場作業上の注意：</strong> 電極トラブルや同期エラーは波形だけでは読み取れません。 </li>
</ul>
</section>

<section class="section" id="references">
<h2 class="section-title">参考資料</h2>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS 仕様: イベント</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS 仕様: 脳波検査</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">パーネット他(2019)、EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">Robbins et al. (2021)、FAIR 機能の構築: HED</a></li> を使用した時系列データ内のイベントの注釈付け
<li><a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">エルメス等(2025)、EEG データ注釈用の HED ライブラリ スキーマ</a></li>
<li><a href="https://doi.org/10.1162/imag_a_00136" target="_blank">Kothe et al. (2025)、同期マルチモーダル記録用のラボ ストリーミング レイヤー</a></li>
<li><a href="https://doi.org/10.3758/s13428-024-02508-y" target="_blank">LLepauvre et al. (2024)、イベントベースの実験をテストするための標準化されたフレームワーク</a></li>
<li><a href="https://doi.org/10.7717/peerj.9414" target="_blank">ブリッジズら(2020)、タイミングのメガスタディ: ラボベースとオンラインの両方のさまざまな実験ジェネレーターの比較</a></li>
<li><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al. (2024)、モーション-BIDS</a></li>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG 運動動作/画像データセット</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT 頭皮脳波データベース</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF データベースの拡張</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid＆amp; Picone (2016)、テンプル大学病院 EEG データ コーパス</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">シャーら(2018)、テンプル大学病院発作検出コーパス</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/19238800/" target="_blank">Moser et al. (2009)、AASM および Rechtschaffen &amp; に基づく睡眠分類。カレス</a></li>
</ul>
</section>

<section class="section" id="return">
<h2 class="section-title">次に戻る場所</h2>
<p>
EEG 全体の役割に戻るには <a href="../eeg_101.html"> Introduction to EEG</a>、スターター データの選択に戻るには <a href="../datasets.html">Data & Bench</a>、最小限のループ手順に戻るには <a href="../datasets.html#l0-practice">Hands-on</a> を使用してください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="eeg-preprocessing-and-qc.html">EEG 前処理と QC →</a></li>
<li><a href="measurement-and-modeling-terms.html">測定からモデリングまで→</a></li>
<li><a href="verification-basics.html">検証基盤の基礎→</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">脳波入門→</a></li>
<li><a href="../datasets.html">データ＆ベンチ→</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン→</a></li>
</ul>
</div>
</aside>
</main>
