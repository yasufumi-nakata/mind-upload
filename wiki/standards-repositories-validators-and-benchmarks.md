---
layout: default
title: 'Wiki: 標準、リポジトリ、バリデータ、ベンチマーク'
description: BIDS、OpenNeuro/PhysioNet、HED、LSL、BIDS デリバティブ、MNE-BIDS、ワークフロー/パイプライン レシピ、MOABB、およびベンチマーク ガバナンス アーティファクトを分離するため、再現性の障害が
  1 つのラベル内に隠れることはありません。
article_type: ウィキ
subtitle: 個別の標準、リポジトリ、派生製品、ワークフロー レシピ、バリデータ、ベンチマーク ハーネス、およびベンチマークの来歴
author: マインドアップロード研究プロジェクト
last_updated: '2026-04-02'
note: 操作ガイド
audience: BIDS、OpenNeuro、PhysioNet、MNE-BIDS、MNE-BIDS-Pipeline、および MOABB を同じ種類のものとして見ている人々
reading_time: 10～15分
page_intro: このページでは、「`Standards,'' ``Repositories,'' ``Validators,'' ``Derivatives,'' ``Workflow / model recipes,'' ``Benchmarks,''
  and `「ベンチマークの来歴 / ガバナンス」」の役割を、バージョンの凍結、イベント セマンティクス、同期ミドルウェア、ローダー / ベンチマーク ツールとともに整理します。目標は、製品名を覚えることではなく、再現性が実際にどこで損なわれるかを理解することです。
accuracy_note: ここで説明するのは、基本的な役割の構成です。 BIDS ベッセル、HED セマンティクス、および LSL 同期は補完的であり、いずれかの最終的な有効性は保証されません。
page_highlights:
- BIDS は標準、OpenNeuro と PhysioNet はストレージ領域、Validator は機械的検査、Benchmark は比較ルールです。
- BIDS デリバティブと結果の来歴は生データのレイアウトとは別のものです。処理された出力には独自の系統とパイプラインの説明が必要です。
- OpenNeuro スナップショットまたは PhysioNet のバージョンを修正しないと、同じデータ名を再現できなくなります。
- HED と Motion-BIDS は、機械可読なセマンティクスと追加のメタデータを運ぶ BIDS の拡張機能です。
- LSL は同期ミドルウェアであり、BIDS やベンチマークに代わるものではありません。
- BIDS/HED/LSL は、それ自体では多峰性の生物学的融合を検証しません。別途 Fusion カードが必要です。
- MNE-BIDS のようなローダー、MNE-BIDS-Pipeline や BIDS Apps のようなワークフロー、BIDS Stats Models のようなモデル レシピ、MOABB のようなベンチマーク ハーネスには、それぞれ異なる役割があります。
- ベンチマークのハーネスとベンチマークの来歴は異なるオブジェクトです。公式ルール、分割/ランダム化、追加データ ポリシー、事前トレーニングされたチェックポイント ポリシー、推論段階の制限、およびその後のオーガナイザーによる事後分析はすべて、スコアの意味を変更する可能性があります。
- 公式チャレンジのホームページ、ルール ページ、提出の制約、およびリーダーボードの修正は、管理上の脚注としてではなく、ベンチマーク オブジェクトの一部としてカウントされます。
- パイプライン名だけではまだ大まかすぎます。派生リネージ、構成、スキップされたステップ、ソフトウェア バージョン、およびランタイム コンテナーは別個の再現性フィールドのままです。
known_points:
- 研究を比較可能にするためには、データ形式、公開先、派生系統、ワークフローレシピ、テスト方法、評価ルールを分離する必要があります。
- BIDS と EEG-BIDS は、スコアリング ルールそのものではなく、「配置方法」の基準です。
- HED のようなイベント セマンティクスは、BIDS にリストされているイベントの意味を機械可読な方法で補足する役割を果たします。
- LSL はストリーム間のクロック調整に役立ちますが、ハードウェア遅延の正確な情報ではありません。
- 時計が調整され、メタデータが標準化されている場合でも、マルチモーダル クレームでは、依然として融合モデル、共同登録、および調整の個別の監査が必要です。
- OpenNeuro と PhysioNet はパブリック プラットフォームですが、すべての入力形式と評価手順が自動的に保証されるわけではありません。
- 未処理の BIDS と BIDS 派生データは別個のレイヤーです。処理されたデータは、生のデータを黙って置き換えるのではなく、明示的な系統を伝える必要があります。
- ワークフロー名だけではレシピが凍結されるわけではありません。構成ファイル、スキップされたステージ、モデル グラフ、ソフトウェア/コンテナーのバージョンはすべて、出力を変更する可能性があります。
- データセット名が同じでも、スナップショット/バージョン、評価ファミリーが異なる場合は比較できません。
- ベンチマークのタイトルだけではまだ不十分です。ベンチマークの意味は、現在のルールのスナップショット、分割構築、非表示のグループ化、追加データ/事前トレーニング済みモデルのポリシー、推論段階の予算、オーガナイザーの事後分析に応じて変化します。
- MOABB は、セッション内/セッション間/被験者間などの評価ファミリーを修正しますが、チャレンジ操作では、ハーネス名だけでは表示されない追加の制約が追加される可能性があります。
- コンテナー化された実行はソフトウェアの移植性に役立ちますが、それ自体ではベンチマークの意味や結果の完全な来歴を凍結するわけではありません。
unknown_points:
- WBE の最終的な共通ベンチマークがどのような粒度であるべきかは不明です。
- どのバリデータと監査項目が最終的な標準となるかは、今後の運用設計によって決まります。
- デコード、ソース イメージング、マルチモーダル パイプラインにわたるワークフローの来歴に最適な共通スキーマは、現在も進化しています。
wiki_links:
- label: 'Wiki: 検証インフラストラクチャの基本'
  url: /wiki/verification-basics.html
  description: 標準、ベンチ、登録、監査の大きなマップに戻ります。
- label: 'Wiki: ベースライン/事前登録/モデルカード'
  url: /wiki/baselines-prereg-and-model-cards.html
  description: ベンチマークを超えた操作言語の違いを補います。
- label: 'Wiki: イベント同期と監視ログ'
  url: /wiki/event-sync-and-measurement-logs.html
  description: 標準に含めたいログ情報の具体例を追加します。
- label: ウィキホーム
  url: /wiki/
  description: 他の補助ページに戻ることができます。
recommended_pages:
- label: データとベンチ
  url: /datasets.html
- label: 検証ベース
  url: /verification.html
- label: ケースワーク
  url: /verification.html#casework
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>最短の区別</h2>
<p>
<strong>標準</strong>生データのレイアウトを修正、<strong>リポジトリ</strong>バージョン管理されたデータセットが公開される場所を修正、<strong>バリデータ</strong>スキーマ準拠をチェック、<strong>派生仕様</strong>処理された出力がソースにリンクされた状態を維持する方法を修正、<strong>ワークフロー/モデルレシピ</strong>出力が生成される方法を修正、<strong>ベンチマークハーネス</strong>プラス<strong>ベンチマークの来歴/ガバナンス</strong>スコアの意味を修正。どれも「研究インフラ」に見えますが、その役割は異なります。
</p>
</div>

<div class="note-box">
<strong>2026-03-26 修正: ベンチマークの出自はベンチマーク</strong> の一部です
<p>
このページの古いバージョンでは、ハーネス名が判明すると、<strong>benchmark</strong> が安定した比較ラベルのように聞こえます。それは弱すぎます。 <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) の公式ホームページ </a> には、元のチャレンジのプレプリントが実行中に <strong> 期限切れ</strong> になったため、Web サイトを最新のものとして扱う必要があると記載されています。公式の <a href="https://eeg2025.github.io/rules/" target="_blank"> ルール </a> では、<strong> 0.5 ～ 50 Hz フィルタリング後のダウンサンプリング </strong>、<strong> 追加データ開示 </strong>、<strong> 事前トレーニング済みモデル開示 </strong>、<strong> シングル GPU 20 GB 推論ステージ制約 </strong> が修正されています。公式<a href="https://eeg2025.github.io/submission/" target="_blank">提出ページ</a>は、<strong>推論のみのコード提出</strong>であることをさらに修正し、最終的な<a href="https://eeg2025.github.io/leaderboard/" target="_blank">リーダーボード</a>は後に<strong>チャレンジ2ランダム化エラー</strong>を明らかにし、最終賞を分けました。最近のベンチマーク論文では、より一般的な形式で同じ点が述べられています。<a href="https://doi.org/10.48550/arXiv.2508.17742" target="_blank">Xiong et al. (2025/2026)</a> は、一貫性のない評価プロトコルにより脳波基礎モデルの比較の信頼性が低くなると主張し、<a href="https://doi.org/10.48550/arXiv.2601.17883" target="_blank">Liu らは (2025/2026) (2026)</a> は、<strong>12 オープンソース基盤モデル </strong> および <strong>13 データセット </strong> にわたって、転送品質の読み取りがプロトコルの選択に大きく依存することを示しています。したがって、このサイトでは、<strong>benchmark 来歴 / ガバナンス</strong> を事後管理としてではなく、再現性の第一級の部分として扱います。
</p>
</div>

<div class="note-box">
<strong>2026-04-02 修正: BIDS にベンチマーク名を追加しても、デリバティブ、ワークフロー レシピ、または結果の来歴が修正されない</strong>
<p>
このページに残っている弱点はさらに微妙なものでした。 <strong>BIDS + リポジトリ + ベンチマーク名 </strong> でも再現性としてはほぼ十分です。現在の公式情報源および一次情報源は、その解釈をサポートしていません。 <a href="https://doi.org/10.7554/eLife.71774" target="_blank">Markiewicz et al. (2021)</a> は、OpenNeuro と BIDS が、共有可能でバージョン管理された生の入力を凍結するのに役立つことを示しています。ただし、BIDS 仕様では、<strong>GeneratedBy</strong> および <strong>SourceDatasets</strong> を保持する派生データセットと、明示的な <strong>Sources</strong> を保持する派生ファイルが別途必要です。 <a href="https://doi.org/10.1371/journal.pcbi.1005209" target="_blank">ゴルゴレフスキーら。 (2017)</a> は、BIDS アプリが自動ベンチマークの意味ではなく、展開とインターフェイスの移植性を解決することを示しています。 <a href="https://mne.tools/mne-bids-pipeline/stable/" target="_blank">MNE-BIDS-Pipeline</a> は、テキスト ファイル構成、キャッシュされた中間ステップ、および概要レポートを明示的に公開します。 <a href="https://bids-standard.github.io/stats-models/index.html" target="_blank">BIDS 統計モデル</a> は、別の機械可読モデル レシピを定義します。および<a href="https://doi.org/10.1038/sdata.2016.102" target="_blank">Maumetら。 (2016)</a> は、結果の来歴自体を別の標準化されたオブジェクトとしてパッケージ化できることを示しています。したがって、このサイトでは、<strong> 派生仕様 </strong>、<strong> ワークフロー / モデル レシピ </strong>、および <strong> 実行 / 結果の出所 </strong> は、「`BIDS'' or `」ベンチマーク内に隠された詳細としてではなく、別個のレイヤーとして扱われるようになりました。
</p>
</div>

<section class="section" id="why-separate">
<h2 class="section-title">なぜ分けて検討するのか</h2>
<p>
これらのレイヤーを混同すると、「`There's a benchmark because you uploaded it to OpenNeuro,'' ``Because it's BIDS, the processed outputs are already traceable,'' ``Because the pipeline name was given, the recipe is already frozen,'' or `「MOABB という名前が付けられたので、ベンチマークの意味はすでに決まっている」などの誤った印象を与えることになります。実際には、生データの調整、派生リネージの命名、ワークフローとモデルのレシピの凍結、比較ルールの定義、および正確なベンチマーク ガバナンスの凍結というタスクは別のものです。
</p>
</section>

<section class="section" id="terms">
<h2 class="section-title">最初に個別の条件</h2>
<table class="data-table">
<thead>
<tr>
<th>期間</th>
<th>機能</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>標準（生レイアウト）</strong></td>
<td> ファイルの配置、名前の付け方、メタデータの書き込み方法は同じです。 </td>
<td>BIDS、EEG-BIDS。 </td>
</tr>
<tr>
<td><strong>ストレージ/共有インフラストラクチャ (リポジトリ)</strong></td>
<td>他の人がデータを取得できるようにデータを公開します。 </td>
<td>OpenNeuro、PhysioNet、PDBなど </td>
</tr>
<tr>
<td><strong>バリデーター</strong></td>
<td> 標準違反やメタデータの欠落を機械的に検査します。 </td>
<td>BIDS バリデーター。 </td>
</tr>
<tr>
<td><strong>派生仕様/系統</strong></td>
<td>処理された出力を生の出力から分離し、直接のソースと生成パイプラインにリンクして戻します。 </td>
<td>BIDS デリバティブ、<code>GeneratedBy</code>、<code>SourceDatasets</code>、<code>Sources</code>。 </td>
</tr>
<tr>
<td><strong>ローダー/コンバーター</strong></td>
<td>標準化された方法でデータセットの読み取りまたは書き込みを行い、それらを分析ライブラリにブリッジします。 </td>
<td>MNE-入札。 </td>
</tr>
<tr>
<td><strong>ワークフロー/モデルレシピ</strong></td>
<td>出力を生成する順序付けされたステップ、構成値、オプションの分岐、グループ化ロジック、および分析グラフを修正します。 </td>
<td>MNE-BIDS-パイプライン構成、BIDS アプリ CLI、BIDS 統計モデル JSON。 </td>
</tr>
<tr>
<td><strong>実行/結果の出所</strong></td>
<td>どのソフトウェア、バージョン、コンテナ、コード、アクティビティが実際に報告された出力とレポートを生成したかを記録します。 </td>
<td>NIDM - 結果、パイプライン レポート、DataLad / BABS 監査証跡。 </td>
</tr>
<tr>
<td><strong>ベンチマークハーネス</strong></td>
<td>問題、区分、指標、禁止事項を修正して比較できるようにします。 </td>
<td>MOABB、MLPerf、ImageNet タイプの動作。 </td>
</tr>
<tr>
<td><strong>ベンチマーク来歴/ガバナンス</strong></td>
<td>スコアを定義する正確なルール スナップショット、分割構築、非表示グループ化、追加データ ポリシー、事前トレーニング済みチェックポイント ポリシー、実行制約、および事後検証を修正しました。 </td>
<td>公式チャレンジのホームページ/ルール/サブミッション/リーダーボード、ベンチマーク事後分析。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="operational-stack">
<h2 class="section-title">実際には、短いラベルでは十分ではないため、11 個のレイヤーを調べます</h2>
<table class="data-table">
<thead>
<tr>
<th>レイヤー</th>
<th>代表例</th>
<th>ここを修正する必要があります</th>
<th>まだ保証はありません</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1。規格</strong></td>
<td>BIDS、EEG-BIDS</td>
<td>ファイル名、必要なメタデータ、座標系、イベント/チャネル/電極の形式。 </td>
<td>train/test スプリットとインジケーターは未定です。 </td>
</tr>
<tr>
<td><strong>2。公開バージョン</strong></td>
<td>OpenNeuro スナップショット、PhysioNet バージョン</td>
<td>A サードパーティは、同じ入力に戻って、どのバージョンが取得されたかを知ることができます。 </td>
<td>このバージョンでは、ベンチマークの分割や前処理の条件が必ずしも修正されているわけではありません。 </td>
</tr>
<tr>
<td><strong>3。イベントセマンティクス/拡張スキーマ</strong></td>
<td>HED、モーション-BIDS</td>
<td><code>trial_type</code> の意味、イベント タグ、追加のセンサー メタデータ、および座標フレーム。 </td>
<td>クロックのアライメントとベンチマークの分割は自動的には決定されません。 </td>
</tr>
<tr>
<td><strong>4。同期ミドルウェア</strong></td>
<td>LSL</td>
<td>複数のストリームの時間調整、クロック オフセット推定、およびストリーム メタデータ。 </td>
<td>デバイス側遅延や刺激提示遅延などの真値は保証しておりません。 </td>
</tr>
<tr>
<td><strong>5。派生仕様/リネージュ</strong></td>
<td>BIDS デリバティブ、<code>GeneratedBy</code>、<code>SourceDatasets</code>、<code>Sources</code></td>
<td>処理された出力を生の出力から分離し、ソースの祖先と生成パイプラインを明示的にします。 </td>
<td>A クリーンまたはエポックされたファイルでも、リネージが欠落している場合は自明のとおりオーバーリードされる可能性があります。 </td>
</tr>
<tr>
<td><strong>6。変換・読み取り</strong></td>
<td>MNE-BIDS</td>
<td>BIDSPath、メタデータ抽出、MNE への読み取りパス、必要に応じてフォーマット変換。 </td>
<td>比較指標と評価ファミリーは固定されていません。 </td>
</tr>
<tr>
<td><strong>7。ワークフロー/モデルレシピ</strong></td>
<td>MNE-BIDS-パイプライン構成、BIDS アプリ CLI、BIDS 統計モデル JSON</td>
<td>ステップ順序、スキップされたステージまたはオプションのステージ、モデル グラフ、および派生出力を決定する構成値を修正します。 </td>
<td>レシピが変更されると、同じ生の入力でも異なる導関数が生成される可能性があります。 </td>
</tr>
<tr>
<td><strong>8。実行/結果の出自</strong></td>
<td>NIDM - 結果、パイプライン レポート、DataLad / BABS 実行レコード</td>
<td>どのソフトウェア、バージョン、コンテナ、コマンド、アクティビティがレポート対象の出力を実際に生成したかを記録します。 </td>
<td>A の図またはスコア テーブルは、それを作成したソフトウェアの状態から切り離すことができます。 </td>
</tr>
<tr>
<td><strong>9。ベンチマークハーネス</strong></td>
<td>MOABB</td>
<td>パラダイム、評価ファミリー、統計的比較、同じパイプラインの横断的評価。 </td>
<td>現在のルールのスナップショット、非表示のグループ化、追加データ ポリシー、実行制約は、ガバナンス文書も凍結されない限り修正されません。 </td>
</tr>
<tr>
<td><strong>10。ベンチマークの来歴 / ガバナンス</strong></td>
<td>公式ホームページ、ルールページ、投稿ページ、リーダーボード/事後分析</td>
<td>現在のベンチマーク バージョン、分割/ランダム化、非表示グループ化、追加データおよび事前トレーニング済みモデルのポリシー、推論段階の制限、および後の修正。 </td>
<td>これは依然として、ターゲット信号の特異性、ソースイメージングの真実性、または規定のベンチマークを超えた動作の安全性を証明するものではありません。 </td>
</tr>
<tr>
<td><strong>11。学習者/実行環境</strong></td>
<td>線形分類器、リーマン パイプライン、ディープ モデル、コンテナ イメージ、ロックファイル</td>
<td>どの推定器がどの前処理、乱数、実行時イメージ、ハイパーパラメータで実行されたか。 </td>
<td>上記1～10を修正しないと公平な比較になりません。 </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>2026-03 サイトルール</strong>
<p>
OpenNeuro はスナップショットをセマンティック バージョンの git タグとして扱い、PhysioNet も各プロジェクトのバージョンを明示的に引用します。したがって、このサイトでは、データセット名だけでなく、<strong> スナップショット / バージョン / DOI または永続 URL</strong> もアーティファクトに含めます。さらに、BIDS は生データ コンテナー、BIDS デリバティブは処理されたデータ レイヤー、HED/Motion-BIDS はセマンティクスと追加メタデータ、LSL は同期、MNE-BIDS は入力/出力パス、MNE-BIDS-Pipeline または BIDS アプリはワークフロー レシピ、BIDS Stats Models はモデル レシピ、NIDM-Results は結果来歴パッケージ化、MOABB は比較ルール。これらを混同しないでください。「`Since I used BIDS, I was able to get past the benchmark'' or `「LSL をインストールしたので、ハードウェアの遅延を解決できました。」」と読んでください。
</p>
</div>
<div class="note-box">
<strong>2026-03-20 追記: 同期インフラストラクチャは Fusion Card</strong> ではありません
<p>
残りの弱点は、<strong>BIDS + HED + LSL</strong> が完全なマルチモーダル有効性パッケージのように聞こえることでした。それは強すぎます。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> は、デバイス側の遅延の真実ではなく、LSL が同期ストリーム トランスポートを解決することを明らかにしました。 <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a> は、EEG-fMRI 融合がモデル条件付けされたままであることを示しました。 (2024)</a> プラス <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025) </a> は、同時マルチモーダル記録が一緒に取得された場合でもモダリティ固有の構造を保持できることを示しました。したがって、このサイトでは、標準と同期インフラストラクチャはマルチモーダルな調査に必要なインプットですが、請求上限が引き上げられる前に、別途 <a href="../verification.html#fusion-card">Fusion Card</a> が依然として必要です。
</p>
</div>
<div class="note-box">
<strong>2026-03-26 追記: ベンチマーク名はまだ固定ベンチマーク オブジェクトではありません</strong>
<p>
<a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB</a> は、<strong>within-session</strong>、<strong>cross-session</strong>、<strong>cross-subject</strong> などの評価ファミリーを正しく修正しますが、現在の EEG チャレンジ操作では、これがベンチマーク オブジェクトの一部にすぎないことが示されています。公式の <a href="https://eeg2025.github.io/rules/" target="_blank">EEG チャレンジ ルール </a> は、フィルター/ダウンサンプリング ルート、追加データ ポリシー、事前トレーニング済みモデルの開示、および推論段階のメモリ バジェットを修正しました。公式 <a href="https://eeg2025.github.io/submission/" target="_blank"> 提出ページ </a> は、コンテストが <strong> 推論のみであることを修正しました </strong>、そして最終的な <a href="https://eeg2025.github.io/leaderboard/" target="_blank"> リーダーボード </a> は、賞品を変更した <strong> 非ランダム化チャレンジ 2 の分割を明らかにしました </strong>構造。したがって、このサイトでは、<strong>harness</strong> と <strong> の現在のガバナンス/来歴文書 </strong> が一緒に凍結されない限り、ベンチマークの主張は不完全になります。
</p>
</div>
</section>

<section class="section" id="benchmark-provenance">
<h2 class="section-title">ベンチマークの出自は再現性の一部</h2>
<p>
このページの実質的な弱点は、<strong>ベンチマーク ハーネス</strong>に留まることでした。最近の公式および一次ソースは、そのショートカットをサポートしていません。 <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge の公式ホームページ </a> では、元のプレプリントが実行中に古くなったことが明示されており、公式 <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a> では操作上の制約が修正され、公式 <a href="https://eeg2025.github.io/submission/" target="_blank"> 提出ページ </a> では実行可能オブジェクトが <strong> 推論のみのコードに絞り込まれている </strong> と、最後の <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> では、ランキングの解釈方法が変更された分割構築の失敗が明らかにされています。並行して、<a href="https://doi.org/10.48550/arXiv.2508.17742" target="_blank">Xiong ら。 (2025/2026)</a> および <a href="https://doi.org/10.48550/arXiv.2601.17883" target="_blank">Liu ら。 (2026)</a> は両方とも、公正な EEG 基礎モデルの比較には標準化されたプロトコルが必要であり、ランキングは依然として評価の選択に大きく依存していると主張しています。したがって、このサイトでは、<strong>benchmark の来歴 / ガバナンス </strong> をハーネス名自体から分離するようになりました。
</p>
<table class="data-table">
<thead>
<tr>
<th>ベンチマークフィールド</th>
<th>修正内容</th>
<th>省略すると安全でないショートカット</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>現在のルールのスナップショット</strong></td>
<td>実行時に実際に適用されていたホームページ/ルール/スターターキットの状態。</td>
<td>最終的なベンチマーク定義として古い提案書を読む。</td>
</tr>
<tr>
<td><strong>分割/ランダム化/非表示グループ化</strong></td>
<td>治験の順序、被験者の連続性、セッションのグループ化、またはその他の隠れた構造が悪用される可能性があるかどうか。</td>
<td>デフォルトでポータブルな主語不変の一般化を反映しているかのようにリーダーボードを読み取る。</td>
</tr>
<tr>
<td><strong>追加データ/事前トレーニング済みモデルのポリシー</strong></td>
<td>外部コーパス、チェックポイント、または微調整ルートが許可されているかどうか、およびそれらをどのように開示する必要があるか。</td>
<td>同じ情報予算の下でトレーニングされたかのように比較が実行されます。</td>
</tr>
<tr>
<td><strong>推論段階の実行制約</strong></td>
<td>比較対象のオブジェクトが完全なトレーニング パイプライン、推論のみの送信、またはメモリ/ハードウェア限定の実行可能ファイルかどうか。</td>
<td>Tチャレンジ ランクを、システムの制約に依存しない純粋な表現学習比較として扱います。</td>
</tr>
<tr>
<td><strong>事後/訂正ステータス</strong></td>
<td>主催者が後にスプリットの欠陥、スコア定義の変更、賞金体系の改訂を明らかにしたかどうか。</td>
<td>最終的な科学的真実として初期のリーダーボードのスナップショットを読み取る。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="eeg-example">
<h2 class="section-title">EEG</h2>の例を見る
<table class="data-table">
<thead>
<tr>
<th>ステージ</th>
<th>そこで何をするか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1。標準に準拠</strong></td>
<td>EEG ファイル、events.tsv、channels.tsv、およびメタデータを BIDS 形式に調整します。 </td>
</tr>
<tr>
<td><strong>2。イベントセマンティクスを追加</strong></td>
<td><code>trial_type</code>、条件の説明、HED タグ、手動スコアリング ルール、レポート使用フラグを指定します。 </td>
</tr>
<tr>
<td><strong>3。監査同期</strong></td>
<td>クロックドメイン、LSL/TTL/フォトダイオード、遅延/ジッター/ドリフトの測定方法はお任せします。 </td>
</tr>
<tr>
<td><strong>4。 Validator</strong></td>で確認する
<td>規格違反や欠品を機械的に識別します。 </td>
</tr>
<tr>
<td><strong>5。ストレージに公開</strong></td>
<td>OpenNeuro や PhysioNet などの共有プラットフォームに配置すると、サードパーティが取得できるようになります。 </td>
</tr>
<tr>
<td><strong>6。フリーズ派生系統</strong></td>
<td>前処理された出力、エポック、機能、およびレポートを、明示的なソースの祖先を持つ派生情報として保持します。 </td>
</tr>
<tr>
<td><strong>7。ワークフロー/モデルレシピをフリーズ</strong></td>
<td> パイプライン構成、オプションのブランチ、モデル グラフ、および出力を生成したソフトウェア設定を記録します。 </td>
</tr>
<tr>
<td><strong>8。ベンチマークとの比較</strong></td>
<td>同じトレーニング/テスト分割、同じメトリクス、同じベースラインを持つモデルを比較します。 </td>
</tr>
<tr>
<td><strong>9。フリーズベンチマークの由来</strong></td>
<td>アクティブなルール ページ、分割/ランダム化ポリシー、追加データ/事前トレーニング済みモデル ポリシー、推論段階の制限、および事後ステータスをスコアとともに記録します。 </td>
</tr>
<tr>
<td><strong>10。フリーズのランタイム/結果の来歴</strong></td>
<td>ソフトウェアのバージョン、コンテナまたはロックファイル、コマンド、レポート、および結果バンドルを記録し、公開された数値やスコアを実行時に追跡できるようにします。 </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>これは重要</strong>
<p>
基準に合わせただけでは、まだ「比較するためのルール」がありません。ただし、たとえベンチマークがあったとしても、派生リネージ、ワークフロー レシピ、または実行時の来歴が暗黙的に残されている場合、比較は依然として失敗する可能性があります。それらすべての層が重要です。
</p>
</div>
</section>

<section class="section" id="missing-piece">
<h2 class="section-title">何が足りないのですか？</h2>
<table class="data-table">
<thead>
<tr>
<th>足りないもの</th>
<th>起こりやすい問題</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>規格</strong></td>
<td>ファイル名やメタデータが人それぞれ異なり、追試の入り口で止まっています。 </td>
</tr>
<tr>
<td><strong>保管場所</strong></td>
<td>の存在は知っていても、手に入れることも再利用することもできず、比較の輪は広がりません。 </td>
</tr>
<tr>
<td><strong>バリデーター</strong></td>
<td>規格違反の通知が遅れ、共有直前や再解析中に事故が発生する。 </td>
</tr>
<tr>
<td><strong>派生仕様・系統</strong></td>
<td>Processed 出力は raw 出力または他の出力と間違われる可能性があり、後で読む人はどのソース ファイルまたはブランチが出力を生成したかを区別できません。 </td>
</tr>
<tr>
<td><strong>ワークフロー/モデルレシピ</strong></td>
<td>同じパイプライン名では、さまざまなオプションのステップ、構成、モデル グラフが非表示になる可能性があるため、再実行では実際には同じ分析が再現されません。 </td>
</tr>
<tr>
<td><strong>実行/結果の出所</strong></td>
<td>A の図、表、または派生物は、それを作成した正確なソフトウェア、バージョン、コンテナー、コマンドまで遡ることができなくなりました。 </td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>人それぞれ異なる部門や指標で評価し、「勝つ」の意味は変動します。 </td>
</tr>
<tr>
<td><strong>ベンチマークの来歴/ガバナンス</strong></td>
<td>同じベンチマーク名では、異なるルールのスナップショット、非表示のグループ化、推論制限、またはその後の修正が非表示になるため、スコアが読み取られます。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="raw-is-not-enough">
<h2 class="section-title">生ファイルだけでは不十分な理由</h2>
<p>
波形ファイルがあるだけでは、標準やベンチマークとしては十分ではありません。少なくとも、イベント定義、刺激ログ、同期情報、QC ログ、除外理由がなければ、同じ課題を繰り返すことは困難です。
</p>
<div class="note-box">
<strong>安全な読書</strong>
<p>
「公開されている」ということと「比較可能である」ということは別のことです。出版はデザインの最初のステップであり、比較可能性は次のステップです。
</p>
</div>
</section>

<section class="section" id="common-confusions">
<h2 class="section-title">よくある混乱</h2>
<table class="data-table">
<thead>
<tr>
<th>よく言いがちなこと</th>
<th>より正確な言い換え</th>
</tr>
</thead>
<tbody>
<tr>
<td>「BIDSにしたからにはベンチマークがある」</td>
<td>BIDS は入力形式の標準であり、比較ルールそのものではありません。 </td>
</tr>
<tr>
<td>「OpenNeuroに載せたから標準化した」</td>
<td>保管領域に掲載する場合でも、規格やメタデータが必ずしも十分とは限りません。 </td>
</tr>
<tr>
<td>「データセット名が同じなので同じ入力を使用しました」</td>
<td>OpenNeuroスナップショットやPhysioNetのバージョンを直さないと同じ入力とは言えません。 </td>
</tr>
<tr>
<td>「ベンチマーク名だけでスコアの意味が決まる」</td>
<td>アクティブなルールのスナップショット、分割/ランダム化/非表示のグループ化ポリシー、追加データ/事前トレーニング済みモデルのポリシー、実行制約、事後分析ステータスが引き続き必要です。 </td>
</tr>
<tr>
<td>「バリデーターは通ったので研究には十分です」</td>
<td>Validator は正式なチェックであり、調査の有効性やベンチマークの強度を保証するものではありません。 </td>
</tr>
<tr>
<td>「MNE-BIDSで読み込めたのでベンチマークになりました」</td>
<td>MNE-BIDS は読み取り/変換補助ツールです。評価ファミリーと比較統計の修正は別のタスクです。 </td>
</tr>
<tr>
<td>「データは BIDS にあるため、処理された出力はすでに一目瞭然です」</td>
<td>Raw BIDS と BIDS 派生は別個のレイヤーであり、処理された出力には依然として明示的なリネージとソースの祖先が必要です。 </td>
</tr>
<tr>
<td>「MNE-BIDS-Pipeline または BIDS アプリに名前を付けると、すでにワークフローがフリーズします」</td>
<td>パイプライン名だけではまだ大まかすぎます。設定値、スキップされたステージ、モデルレシピ、ソフトウェアバージョンも凍結する必要があります。 </td>
</tr>
<tr>
<td>「コンテナ化された実行により、スコアの意味がすでに把握されています」</td>
<td>Container とランタイム ピンはソフトウェアの移植性に役立ちますが、ベンチマーク ハーネスとベンチマーク ガバナンスは依然として別個のオブジェクトのままです。 </td>
</tr>
<tr>
<td>「`events.tsv` があるため、イベントのセマンティクスは修正されています」</td>
<td><code>events.tsv</code> は時間と列のコンテナーであり、条件の意味とスコアラー ルールは <code>events.json</code>、HED、および補助ログで個別に修正する必要があります。 </td>
</tr>
<tr>
<td>「LSLを使うことでハードウェア遅延も解決」</td>
<td>LSL はストリーム同期に役立ちますが、ディスプレイ/オーディオ/アンプのデバイス側の遅延については別の測定が必要です。 </td>
</tr>
<tr>
<td>「MOABB スコアはタスク間で直接比較可能」</td>
<td>セッション内、セッション間、および被験者間は異なる評価ファミリーであり、同等に扱うことはできません。 </td>
</tr>
<tr>
<td>「前処理されたファイルを生の BIDS に変換しても安全です」</td>
<td>BIDS や MNE-BIDS は基本的に未加工または最小限の加工を施したデータを想定しており、改変データは系統を指定して派生データとして扱う方が安全です。 </td>
</tr>
<tr>
<td>「ベンチマークは勝てたので実運用には十分です」</td>
<td>Benchmarkは比較のための目安であり、実際の動作やL4/L5の確立を自動的に保証するものではありません。 </td>
</tr>
<tr>
<td>「チャレンジ提案書が最終ベンチマーク仕様です」</td>
<td>実行フェーズの Web サイト、ルール、スターター キット、および最終事後分析は、元の提案に取って代わられる可能性があるため、結果とともに凍結する必要があります。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="freeze-ids">
<h2 class="section-title">修正する必要がある最小 7 つの ID</h2>
<table class="data-table">
<thead>
<tr>
<th>ID</th>
<th>最低限欲しいもの</th>
<th>紛失した場合</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入力ID</strong></td>
<td>OpenNeuro スナップショット タグ、PhysioNet バージョン、DOI、取得日。 </td>
<td>同じデータセット名の異なるバージョンを混在させると、再試行できなくなります。 </td>
</tr>
<tr>
<td><strong>SスキーマID</strong></td>
<td>BIDS/EEG-BIDS のバージョン、Validator のバージョン、および警告が残された理由。 </td>
<td>規格の違いと実装の違いを区別することはできません。 </td>
</tr>
<tr>
<td><strong>派生ID</strong></td>
<td>派生データセット名、<code>GeneratedBy</code>、<code>SourceDatasets</code>、および直接の<code>Sources</code>系統。 </td>
<td>前処理された出力は、生の出力または別の派生ブランチと混同される可能性があります。 </td>
</tr>
<tr>
<td><strong>ワークフローID</strong></td>
<td>MNE-BIDS-パイプライン / BIDS アプリ / 構成ファイル / モデル グラフのバージョンと設定。 </td>
<td>同じ入力バージョンであっても、異なるレシピでは異なる結果が生成される可能性があります。 </td>
</tr>
<tr>
<td><strong>評価ID</strong></td>
<td>セッション内/セッション間/主題間、インジケーター、分割シード、禁止事項。 </td>
<td>スコアの意味が異なり、公平な比較が崩れてしまいます。 </td>
</tr>
<tr>
<td><strong>ベンチマーク ガバナンス ID</strong></td>
<td>Rules URL またはアーカイブされたスナップショット、分割/ランダム化ポリシー、非表示のグループ化メモ、追加データ/事前トレーニング済みモデルのポリシー、推論段階の制限、および事後ステータス。 </td>
<td> ベンチマークのタイトルは粗すぎるままになり、同じリーダーボード名に異なる科学的意味が隠される可能性があります。 </td>
</tr>
<tr>
<td><strong>Rランタイム/結果の出所ID</strong></td>
<td>ソフトウェアのバージョン、コンテナまたはロックファイル、コマンドログ、および結果バンドルまたはレポート識別子。 </td>
<td>公開された数値やスコアは、それを作成した正確な実行まで遡ることができません。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read">
強い議論を読むときの <h2 class="section-title">9 つの質問</h2>
<ol>
<li><strong>入力規格は何ですか?</strong>BIDSなどでフォーマットが合っているか確認してください。</li>
<li><strong>使用されたバージョン:</strong>スナップショット、バージョン、DOI、および取得日が修正されているかどうかを確認します。 </li>
<li><strong>イベント セマンティクスとクロック ドメインとは: </strong><code>trial_type</code>、HED、スコアラー ルール、LSL/TTL/フォトダイオード、遅延/ジッター監査について説明します。 </li>
<li><strong>生と派生を区別しましたか?</strong>処理された出力が、追跡可能な系統を持つ明示的な派生のままであるかどうかを確認してください。 </li>
<li><strong>読み取り/書き込みに使用されたもの:</strong>ローダー/トランスフォーマーを調べて、そのバージョンが指定されているかどうかを確認します。 </li>
<li><strong>出力を生成したワークフローまたはモデル レシピは何ですか?</strong>構成ファイル、オプションのブランチ、モデル グラフ、およびソフトウェア設定を探します。 </li>
<li><strong>どのようなランタイムまたは結果の出所レコードが存在しますか?</strong>コンテナ/ロックファイル、コマンドログ、レポート、または結果バンドルを確認してください。 </li>
<li><strong>どのベンチマーク ハーネスが使用されましたか?</strong>評価ファミリ、メトリクス、および比較統計が修正されているかどうかを確認します。 </li>
<li><strong>どのベンチマークの出所が有効でしたか?</strong>アクティブなルールのスナップショット、分割/ランダム化、追加データ/チェックポイント ポリシー、推論段階の制限、および事後ステータスを確認します。 </li>
</ol>
</section>

<section class="section" id="references">
<h2 class="section-title">参考資料と公式ページ</h2>
<ul>
<li><a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">ゴルゴレフスキーら。 (2016)、BIDS</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS 仕様: タスクイベント</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS 仕様: 脳波検査</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">BIDS 仕様: dataset_description、GeneratedBy、および SourceDatasets</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html" target="_blank">BIDS デリバティブ: 一般的なデータ型と系統メタデータ</a></li>
<li><a href="https://bids-standard.github.io/stats-models/index.html" target="_blank">BIDS 統計モデル仕様</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">パーネットら(2019)、EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">Robbins et al. (2021)、FAIR イベント注釈用 HED</a></li>
<li><a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">エルメス他(2025)、EEG データ注釈用の HED ライブラリ スキーマ</a></li>
<li><a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)、同期マルチモーダル記録用のラボ ストリーミング レイヤー</a></li>
<li><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al. (2024)、モーション-BIDS</a></li>
<li><a href="https://doi.org/10.7554/eLife.71774" target="_blank">Markiewicz et al. (2021)、OpenNeuro</a></li>
<li><a href="https://docs.openneuro.org/git.html" target="_blank">OpenNeuro ドキュメント: Git アクセスとスナップショット</a></li>
<li><a href="https://docs.openneuro.org/user_guide.html" target="_blank">OpenNeuro Docs: データセットのランディング ページとスナップショット メタデータ</a></li>
<li><a href="https://physionet.org/about/" target="_blank">PhysioNet: 概要と引用ポリシー</a></li>
<li><a href="https://physionet.org/about/content/" target="_blank">PhysioNet: リソースと引用に関するガイダンス</a></li>
<li><a href="https://doi.org/10.21105/joss.01896" target="_blank">アペルホフら。 (2019)、MNE-BIDS</a></li>
<li><a href="https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html" target="_blank">MNE-BIDS ドキュメント: write_raw_bids</a></li>
<li><a href="https://mne.tools/mne-bids-pipeline/stable/" target="_blank">MNE-BIDS-パイプライン ドキュメント</a></li>
<li><a href="https://doi.org/10.1371/journal.pcbi.1005209" target="_blank">ゴルゴレフスキーら。 (2017)、BIDS アプリ</a></li>
<li><a href="https://doi.org/10.1162/imag_a_00074" target="_blank">Zhao ら。 (2024)、BABS および大規模な BIDS-App 監査証跡</a></li>
<li><a href="https://doi.org/10.1038/sdata.2016.102" target="_blank">マウメットら(2016)、NIDM-結果</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">ジャヤラム＆amp;バラチャント (2018)、MOABB</a></li>
<li><a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB ドキュメント</a></li>
<li><a href="https://moabb.neurotechx.com/docs/auto_examples/paradigm_examples/index.html" target="_blank">MOABB ドキュメント: パラダイムと評価の例</a></li>
<li><a href="https://eeg2025.github.io/" target="_blank">EEG チャレンジ (2025): ホームページ</a></li>
<li><a href="https://eeg2025.github.io/rules/" target="_blank">EEG チャレンジ (2025): ルール</a></li>
<li><a href="https://eeg2025.github.io/submission/" target="_blank">EEG チャレンジ (2025): 提出</a></li>
<li><a href="https://eeg2025.github.io/leaderboard/" target="_blank">EEG チャレンジ (2025): 最終リーダーボードと主催者の修正</a></li>
<li><a href="https://doi.org/10.48550/arXiv.2508.17742" target="_blank">Xiong ら(2025/2026)、EEG-FM-ベンチ</a></li>
<li><a href="https://doi.org/10.48550/arXiv.2601.17883" target="_blank">Liu et al. (2026)、EEG 基礎モデル: 進捗状況、ベンチマーク、未解決の問題</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)、EEG および fMRI</a></li> 用のベイジアン融合およびマルチモーダル DCM
<li><a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii ら(2024)、多峰性自発的脳活動組織</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">チェンら(2025)、覚醒時とノンレム睡眠時の同時 EEG-PET-MRI</a></li>
</ul>
</section>

<section class="section" id="return">
<h2 class="section-title">次に戻る場所</h2>
<p>
<a href="../datasets.html">Data & Bench</a> を使用して実用的なエントリ ポイントに戻り、<a href="../verification.html">Verification Platform</a> を使用して全体設計に戻り、<a href="../verification.html#casework">Casework</a> を使用して他の分野の例に戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="verification-basics.html">検証基盤の基礎 →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">ベースライン/事前登録/モデルカード→</a></li>
<li><a href="event-sync-and-measurement-logs.html">イベント同期および観測ログ →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../datasets.html">データ＆ベンチ→</a></li>
<li><a href="../verification.html">検証インフラ→</a></li>
<li><a href="../verification.html#casework">ケースワーク→</a></li>
</ul>
</div>
</aside>
</main>
