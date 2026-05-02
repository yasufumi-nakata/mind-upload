# Wiki: ベースライン / ベンチマーク / 事前登録 / モデルカード

> スコアレポートからクレームに必要な現在のアーティファクトスタックまで
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-04-04 / Role: 学習ガイド / 現在のカードフィールドの同期

## このページの役割
このページでは、ベースライン、ベンチマーク、事前登録、モデル カード、および結果がマルチモーダル フュージョン、大規模な事前トレーニング、ショートカット耐性、言語対応デコード、ルート固有の測定/推論クレーム、生きている人間のプロキシ バンドル、または連続した同一サブジェクト ブリッジに依存する場合に必要となる追加カードの操作上の違いについて説明します。今回の改訂では、カード名だけでは大まかになりすぎた部分と、フィールドレベルの開示が必要になった部分も示しています。

## 正確性に関する注記
このページは、アーティファクト スタックの学習ガイドです。権限のあるカード フィールドと停止ルールは公開検証ページにまだ存在します。

## 公開ページへ戻る
- [検証](https://mind-upload.com/verification.html)
- [データセット / L0 の実践](https://mind-upload.com/datasets.html#l0-practice)
- [検証ケースワーク](https://mind-upload.com/verification.html#casework)

## 関連 Wiki ページ
- [Wiki: 検証の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 標準、ベンチマーク、レジストリ、監査が必要な理由のより広い地図。
- [Wiki: データセットの分割と漏洩](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - 分割の衛生管理、取得と配布のショートカット、ベンチマークの来歴について説明します。
- [Wiki: EEG 基礎モデル](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-foundation-models) - 事前トレーニング クレームに汎用モデル カード以上のものが必要な理由を説明します。
- [Wiki: 人間の代理構成](https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition) - 複数の生きている人間のプロキシ行が一緒に昇格される場合とそうでない場合について説明します。
- [Wiki: 観察から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 逆問題、ESI、効果的な接続性、および因果関係の同等性の制限を整理します。
- [Wiki: 不確実性、校正、および棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - 確率、予測セット、および棄権が独自のカードを必要とする場合について説明します。
- [Wiki: 熱力学的接地の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/thermodynamic-grounding-basics) - 不可逆性言語に信号ルート、推定量ファミリー、数量タイプの開示が必要な理由を説明します。
- [Wiki: 閉ループ、レイテンシー、ジッター、および安全停止](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - 介入のタイミングと身体/環境の境界が別個の監査である理由を説明します。
- [Wiki: 状態継続ブリッジ](https://github.com/yasufumi-nakata/mind-upload/wiki/state-continuity-bridge) - 同じ主題または同じ脳の文言が自動的に同じ状態の証拠を意味しない理由を説明します。

## 現在わかっていること
- 比較可能な進捗には、ベースライン、ベンチマーク オブジェクト、事前登録された停止ルール、結果レポート、および明示的な障害の開示が必要です。
- ベンチマークの意味は、データセットとスコアだけでなく、分割ランダム性、メトリック バンドル、追加データ ポリシー、運用上の制約、事後検証にも依存します。
- 可観測性バジェット、特異性とショートカット カード、神経貢献カード、融合カード、事前トレーニング カード、ルート固有のカード/ログ、人間代理構成カード、時間的有効性カード、校正と棄権カード、および状態継続性ブリッジ カードは、さまざまな障害モードに対応します。
- このサイトでは、カード名だけではもはや十分ではありません。Fusion、Human Proxy Composition、および State-Continuity Bridge の各カードでは、新しい形式のオーバーリードをブロックするためにフィールド レベルの開示が必要になりました。
- アーティファクトスタックが主張と一致しない場合、スコアが高くても科学的に弱い可能性があります。

## まだわかっていないこと
- このアーティファクト スタックのどのサブセットがこのサイトを超えてフィールド全体のデフォルトになるかはまだ決まっていません。
- 否定的な結果や失敗例に対して期待される正確な最小限の開示は、今後も進化し続けます。

---

<h2>最短マップ</h2>
<p>
<strong>baseline</strong> は最小の比較パートナーです。 <strong>benchmark</strong> は、タスクとスコアだけでなく、分割ルール、メトリック バンドル、および結果の操作上の読み取りも修正します。 <strong>事前登録</strong>は、実行開始前に成功、失敗、棄権の意味を修正します。 <strong>モデルカード</strong>は何が起こったかを報告します。その後、クレームの形状に応じて追加のカードが添付されます。その積み重ねがなければ、良いスコアは依然として比較可能な進歩とは言えません。
</p>

<strong>2026-03 追記: L1 以上には依然として可観測性予算が必要</strong>
<p>
L1 以上の結果の場合、このサイトは通常のモデル カードの上に <a href="https://mind-upload.com/verification.html#observability-budget">Observability Budget</a> をスタックするため、測定スタック、直接観測可能量、残留潜在状態、請求上限、および棄権条件がスコアによって暗示されるのではなく可視化されます。
</p>

<strong>2026-03-25 追記: ベンチマークは単なるデータに 1 つのスコアを加えたものではありません</strong>
<p>
このページの以前のバージョンでは、まだ <strong>benchmark</strong> が静的なスコアシートのように聞こえます。それは弱すぎます。 <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) の公式ホームページ </a> には、元のチャレンジのプレプリントが実行中に古くなったため、Web サイトとスターター キットを最新のものとして扱う必要があると記載されています。公式の <a href="https://eeg2025.github.io/rules/" target="_blank"> ルール </a> では、<strong> 追加の事前トレーニング データ </strong>、<strong> 事前トレーニング済みモデル / 微調整方法 </strong>、<strong> 単一 GPU 20 GB の推論段階の制約 </strong> の開示が要求されていますが、公式 <a href="https://eeg2025.github.io/leaderboard/" target="_blank"> リーダーボード </a> は後に、チャレンジ 2 のサンプルがランダム化されていないことを明らかにし、賞品の構造とランキングの意味が変更されました。 <a href="https://arxiv.org/abs/2508.17742" target="_blank">Xiongら。 (2025)</a> および <a href="https://arxiv.org/abs/2601.17883" target="_blank">Liu ら。 (2026) </a> はその後、プロトコルと評価の選択が EEG 基礎モデルの比較に実質的に影響を与えることをより一般的に示しました。同様に、<a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">Saito &amp;レームスマイヤー (2015)</a>、<a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">ロイ他。 (2021)</a>、<a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">Sun他(2017)</a>、<a href="https://doi.org/10.7554/eLife.70092" target="_blank">ヴァラット＆アンプWalker (2021)</a> は、<strong> メトリクス セマンティクス </strong> もスコアの意味を変更する理由を示しています。したがって、このサイトでは、ベンチマークには、データセット名と 1 つの数字だけでなく、<strong> 分割 / ランダム化ルール </strong>、<strong> タスク一致メトリック バンドル </strong>、<strong> ベンチマーク バージョン </strong>、<strong> 追加データ / チェックポイント ポリシー </strong>、<strong> 推論段階の制限 </strong>、および <strong> オーガナイザー事後分析 </strong> が含まれるようになりました。
</p>

<strong>2026-03-25 追記: モデル カードはアーティファクト スタック全体ではありません</strong>
<p>
次の弱点は、汎用の <strong> モデル カード </strong> がすべての結果の最終レポート層であるかのように聞こえることでした。それも弱すぎる。 <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>、<a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu 他(2020)</a>、<a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di 他(2021)</a> は、デコードと転送クレームが依然として <strong> 主題/取得ショートカット </strong> に乗っているため、スコア報告だけではターゲット変数の特異性を確立できない理由を示しています。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a>、<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii 他(2024)</a>、<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> は、<strong> 同時 </strong> または <strong> マルチモーダル </strong> が融合監査に置き換わらない理由を示しています。 <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">ヨハンセンら。 (2024)</a>、<a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li 他。 (2025)</a>、<a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al。 (2024)</a>、<a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a>、<a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026) </a> は、すでに現場で使用可能な 1 つの全脳メーターではなく、さまざまな生きた人間の量のタイプと負荷を制約します。 <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Luら(2023)</a>、<a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a>、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONSコンソーシアムほか(2025)</a>、<a href="https://doi.org/10.1038/nature14467" target="_blank">Attardo et al. (2015)</a> は、同じ主題または同じ脳の文言が依然として連続的な橋渡しの負担を残す理由を示しています。したがって、このサイトでは、モデル カードは <strong>claim トリガー アーティファクト スタック </strong> の 1 つのレイヤーにすぎません。
</p>

<strong>2026-03-30 追記: 一般的なコンパニオン カードは、現在のサイト ルールにはもはや不十分です</strong>
<p>
このページの次の弱点は、範囲は狭いものの重要でした。現在の公開サイトでは現在、いくつかのクレーム ファミリに対して <strong>route 固有のカードまたはログ </strong> が必要であるにもかかわらず、以前の汎用コンパニオン カードしかリストされていませんでした。一次文献では、これらのルートを 1 つの汎用レポート層に圧縮することはサポートされていません。 <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tangら(2023)</a>、<a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairragkar et al。 (2025)</a> は、言語対応の出力に、スコアだけではなく、<strong>Neural Contribution Card</strong> に加えて時間的および校正の開示が必要な理由を示しています。 <a href="https://doi.org/10.1016/j.clinph.2023.08.009" target="_blank">Horrillo-Maysonnial 他(2023)</a>、<a href="https://doi.org/10.1016/j.clinph.2025.04.009" target="_blank">Rong 他(2025)</a>、<a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> は、なぜ ESI クレームに検証クラス、ソース体制、ベンチマーク オブジェクトの型指定とソルバーの不一致の開示が必要なのかを示しています。 <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">ガジワニら(2023)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">He et al. (2024)</a>、および <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">Manzano-Patr'n et al. (2025)</a> は、トラクトグラフィーに 1 つのグラフ見出しではなくオブジェクトの型指定が必要な理由を示しています。 <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">Smith et al. (2011)</a>、<a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">バーネット&amp;セス (2017)</a>、<a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">Villaverde 他(2019)</a>、<a href="https://doi.org/10.1002/hbm.70285" target="_blank">Novelli et al. (2025)</a> は、クロージャ、ノード ポリシー、サンプリング感度が開示されない限り、実効接続グラフがモデル条件付きのままである理由を示しています。 <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lリンら。 (2021)</a>と<a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">石原＆amp; Shimazaki (2025)</a> は、非可逆性言語が複数の推定量ファミリと閉包仮定を隠す理由を示しています。したがって、このページでは、<strong> 汎用コンパニオン カード </strong> を 1 つのバケットとして扱うのではなく、<strong> ルート固有のカード/ログ </strong> から分離するようになりました。
</p>

<strong>2026-04-04 追記: 3 枚のカードは名前レベルの開示ではなく、フィールド レベルの開示が必要になりました</strong>
<p>
このページの次の弱点は、ルートスタックの拡張後にのみ明らかになりました。現在の一次文献ではそうではないと述べているにもかかわらず、3 枚のカードは依然として短いラベルによって満足されているように聞こえました。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>、<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii 他。 (2024)</a>、<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a>、<a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">ボルト 他(2025)</a>、<a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp 他(2025)</a>、<a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a>、<a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova 他。 (2026)</a> は、<strong>Fusion</strong> が依然として同期、時間カーネル関係、共有構造と固有構造、数量ブリッジ、およびバンドルの堅牢性を分離する必要がある理由を示しています。 <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Liら(2025)</a>、<a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B'gh 他(2024)</a>、<a href="https://doi.org/10.1002/nbm.5256" target="_blank">モーガンら。 (2024)</a>、<a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> は、<strong>Human Proxy Composite</strong> が依然として数量タイプ、動作点依存性、メソッド ファミリの不等価性、および不一致トポロジを分離する必要がある理由を示しています。 <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">ボッシュ他(2022)</a>、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONSコンソーシアムほか(2025)</a>、<a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego 他(2020)</a>、<a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz 他(2025)</a>、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairragkar et al。 (2025)</a> は、なぜ <strong>State-Continuity Bridge</strong> が依然として標本の識別性やスコア生存のみに依存するのではなく、搬送物体、許容ルール、および救助ルートに名前を付ける必要があるのか​​を示しています。したがって、このガイドでは、これら 3 枚のカードを、短い名前と 1 つの文で満たされるものとして扱うことはなくなりました。
</p>

<h2>まずは役割を分ける</h2>
<table>
<thead>
<tr>
<th>アーティファクト</th>
<th>主役</th>
<th>他のものでは修正されないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベースライン</strong></td>
<td>最低限の比較相手。</td>
<td>新しいスコアがコンテキストなしで読み取られるのを防ぎます。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>ベンチマーク オブジェクト: タスク、分割ルール、メトリック バンドル、およびガバナンス。</td>
<td>スコアが解釈される前に比較が実際に何を意味するかを修正します。</td>
</tr>
<tr>
<td><strong>事前登録</strong></td>
<td>走り出す前の約束。</td>
<td>後知恵のプレッシャーが現れる前に、成功、失敗、停止、棄権のルールを修正します。</td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>1 つのトレーニング済みシステムの結果レポート。</td>
<td>提出されたシステムのスコア、ベースライン、障害例、コンピューティング使用状況、および実質的な弱点を記録します。</td>
</tr>
<tr>
<td><strong>可観測性バジェット</strong></td>
<td>測定側天井。</td>
<td>直接観察されたもの、潜在的に残っているもの、および適用される請求上限を修正します。</td>
</tr>
<tr>
<td><strong>特異性とショートカットカード</strong></td>
<td>デコード/バイオマーカー/転送クレームのショートカット監査。</td>
<td>対象の神経変数をサブジェクト、セッション、サイト、デバイス、プロトコル、その他の迷惑ルートから分離します。</td>
</tr>
<tr>
<td><strong>神経貢献カード</strong></td>
<td>言語対応のショートカット監査。</td>
<td>タスクの制約、候補セット、プロンプトまたは言語モデルの足場、脳なし / LM なし / シャッフル コントロール、およびテキスト / 音声出力の被験者の協力を修正します。</td>
</tr>
<tr>
<td><strong>フュージョンカード</strong></td>
<td>マルチモーダル/アトラス事前統合監査。</td>
<td>取得関係の修正、ラグ監査、<strong>有効ウィンドウ/時間的カーネル関係</strong>、ジオメトリ/共同登録スコープ、融合モデル、<strong>共有コンポーネント対固有コンポーネントの開示</strong>、<strong>量ブリッジ/生理学グラウンディング</strong>、単峰性ベースライン、<strong>完全なケース/欠落モダリティの開示</strong>、転送または意見の不一致ウィンドウ、外部校正、および棄権。</td>
</tr>
<tr>
<td><strong>プレトレーニングカード</strong></td>
<td>EEG 財団 / 自己監視型転送監査。</td>
<td>コーパスの同一性/重複、調和、適応レジーム、ベンチマークの来歴、および効率の制約を修正します。</td>
</tr>
<tr>
<td><strong>ルート固有のカード/ログ</strong></td>
<td>クレームファミリー固有の開示レイヤー。</td>
<td> ESI、トラクトグラフィー、有効接続性、不可逆性、介入、および境界の主張を、1 つの汎用レポートに圧縮するのではなく、独自の故障モードごとに入力します。</td>
</tr>
<tr>
<td><strong>人間プロキシ構成カード</strong></td>
<td>複数の生きた人間のプロキシ行のバンドル監査。</td>
<td>プロキシクラスの修正、<strong>行による直接観察可能性と証拠の役割</strong>、同一被験者関係、<strong>有効時間窓/状態軸</strong>、体制の互換性、<strong>運用の成熟度</strong>、<strong>キャリブレータの役割</strong>、モデル負荷、<strong>メソッドファミリーの不等価性</strong>、<strong>合意/ 不一致トポロジーと解決ポリシー</strong>、増分証拠、および残留潜在状態の上限。</td>
</tr>
<tr>
<td><strong>ステート・コンティニュイティ・ブリッジ・カード</strong></td>
<td>順次ブリッジ監査。</td>
<td>取得順序、経過時間、レジーム連続性、座標転送/変形、<strong>搬送物体/ブリッジ目撃者</strong>、<strong>許容/失敗ルール</strong>、<strong>レスキュールートと生の連続性</strong>、ブリッジ検証ラング、および同一状態言語が許可される前の残留ドリフト天井を修正します。</td>
</tr>
<tr>
<td><strong>時間的有効性カード</strong></td>
<td>時間汎化上限。</td>
<td>固定デコーダ間隔、状態注釈、再キャリブレーション負担、ドリフト処理、数時間から数日にわたる転送上限を修正します。</td>
</tr>
<tr>
<td><strong>校正と調整棄権カード</strong></td>
<td>不確実性とフォールバック監査。</td>
<td>フィット/キャリブレーション/テスト分離、評価スライス、カバレッジリスク目標、および出力に信頼性または棄権が含まれる場合のフォールバック動作を修正します。</td>
</tr>
<tr>
<td><strong>失敗例/否定的な結果</strong></td>
<td>壊れた場所の記録。</td>
<td>現場が偶然の成功からのみ学習することを防ぎます。</td>
</tr>
</tbody>
</table>

<h2>このサイトのベンチマークで修正される内容</h2>
<table>
<thead>
<tr>
<th>ベンチマークフィールド</th>
<th>それが重要な理由</th>
<th>これがないとどうなる</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>タスクとターゲットの定義</strong></td>
<td>S予測または検出された内容を正確に示します。</td>
<td>A スコアは、より広範なタスク ファミリに適用されるかのようにオーバーリードされる可能性があります。</td>
</tr>
<tr>
<td><strong>分割/ランダム化ルール</strong></td>
<td>被験者、セッション、試験順序、および非表示のグループ化が制御されたかどうかを定義します。</td>
<td>ID または連続トライアルのショートカットにより、リーダーボードの意味が変わる可能性があります。</td>
</tr>
<tr>
<td><strong>Tタスク一致メトリックバンドル</strong></td>
<td>誤報、遅延、マクロ F1、カッパなど、このタスクに必要なメトリクスを修正します。</td>
<td>1 つのヘッドライン スコアで実際の故障モードを隠すことができます。</td>
</tr>
<tr>
<td><strong>追加データ/チェックポイント ポリシー</strong></td>
<td>外部データまたは事前トレーニングされたモデルによって比較が変更されたかどうかを示します。</td>
<td>転送ゲインは、送信されたパイプラインのみからのものであるかのように誤って読み取られる可能性があります。</td>
</tr>
<tr>
<td><strong>動作制限</strong></td>
<td>推論時のコンピューティング、コード送信条件、その他のデプロイメント側の制約を修正します。</td>
<td>A の結果は、より緩やかな動作体制に依存している場合、ポータブルであると誤って読み取られる可能性があります。</td>
</tr>
<tr>
<td><strong>バージョン/事後ステータス</strong></td>
<td>Sオーガナイザーのアップデート、スターターキットの変更、またはその後のエラー開示によってベンチマーク オブジェクトが変更されたかどうかを示します。</td>
<td>時代遅れのプレプリントや初期のリーダーボードは、最終的なベンチマークの真実として読み取られる可能性があります。</td>
</tr>
</tbody>
</table>

<h2>クレームによってどの追加アーティファクトがトリガーされるか</h2>
<table>
<thead>
<tr>
<th>クレーム形状</th>
<th>ベーススタック</th>
<th>追加する追加のアーティファクト</th>
<th>ブロックするもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>任意の L1+ 測定クレーム</strong></td>
<td>ベースライン + ベンチマーク + 事前登録 + モデルカード</td>
<td><strong>可観測性バジェット</strong></td>
<td>Sあたかも実際より多くを直接観測したかのように、測定スタックのオーバーリードを停止します。</td>
</tr>
<tr>
<td><strong>デコード / バイオマーカー / トランスファークレーム</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>特異性とショートカットカード</strong></td>
<td>サブジェクト/セッション/サイト/デバイス/プロトコルのショートカットがターゲット変数のキャプチャと誤認されるのを防ぎます。</td>
</tr>
<tr>
<td><strong>基礎/自己教師あり脳波の主張</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>プレトレーニングカード</strong>プラス<strong>特異性とショートカットカード</strong></td>
<td>S転送勝利が一般的な移植性またはショートカット耐性のある表現学習として過剰に読み取られるのを防ぎます。</td>
</tr>
<tr>
<td><strong>言語対応のテキスト/音声/頭脳からテキストへの主張</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>神経貢献カード</strong>プラス<strong>特異性および特性ショートカットカード</strong>; <strong>キャリブレーションと追加棄権カード</strong>、信頼度、検索セット、または予測セットの言語が報告された場合。</td>
<td>あたかもニューラル寄与、信頼性、およびプロンプト依存性がすでに分離されているかのように、流暢な出力またはトップ K の取得がオーバーリードされるのを防ぎます。</td>
</tr>
<tr>
<td><strong>EEGソースイメージング/逆再構成クレーム</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>逆ソルバー合意ログ</strong> プラス、名前付き検証クラス、ソース レジーム、モンタージュ/カバレッジ ポリシー、およびベンチマーク オブジェクトの開示。</td>
<td>Sあたかも深度バイアス、ソース範囲、カバレッジジオメトリ、ソルバーの不一致がすでに解決されているかのように、1 つのローカリゼーション ヘッドラインが読み上げられるのを防ぎます。</td>
</tr>
<tr>
<td><strong>拡散 MRI トラクトグラフィー / 構造コネクトームクレーム</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>トラクトグラフィールートカード</strong></td>
<td>Sあたかも取得、エンドポイントの割り当て、グラフ構築、不確実性、およびキャリブレーションが修正されたかのように、1 つのトラクトグラフィー グラフのオーバーリードを停止します。</td>
</tr>
<tr>
<td><strong>有効接続 / DCM / 有向グラフ主張</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>有効接続ルートカード</strong></td>
<td>S候補モデル ファミリ、クロージャ、ノード ポリシー、およびサンプリング感度が暗黙的なままである場合、発見された因果関係として有向グラフがオーバーリードされるのを停止します。</td>
</tr>
<tr>
<td><strong>熱力学/不可逆性主張</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>不可逆性/熱力学ルートカード</strong></td>
<td>Sあたかも信号ルート、粗視化、推定器ファミリー、数量タイプがすでに固定されているかのように、時間の矢またはエントロピー フロー言語がオーバーリードされるのを防ぎます。</td>
</tr>
<tr>
<td><strong>マルチモーダルまたはアトラス事前の請求</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>フュージョンカード</strong></td>
<td>S同時性、同期ミドルウェア、または検証済みの融合の代わりとなる以前の機能を停止します。</td>
</tr>
<tr>
<td><strong>介入/クローズドループクレーム</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>介入カード</strong>;具体化された主張または人間参加型の主張の場合は、<strong>Body / Environmental Boundary Card</strong>.</td> も追加します
<td>S低レイテンシーまたは 1 つの制御トレースが、型指定された介入、保持されたループ境界、または安全な展開の主張に代わることを停止します。</td>
</tr>
<tr>
<td><strong>複数の生きている人間のプロキシ行を一緒に使用</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>人間プロキシ構成カード</strong></td>
<td>S行ごとの役割、レジームの互換性、成熟度、不一致が暗黙的なままである場合、プロキシが豊富なバンドルが同じサブジェクト状態の識別としてオーバーリードされるのを防ぎます。</td>
</tr>
<tr>
<td><strong>同一主題・同一脳シーケンシャルブリッジ</strong></td>
<td>ベーススタック + 可観測性バジェット</td>
<td><strong>ステート・コンティニュイティ・ブリッジ・カード</strong>; <strong>時間的有効性カード</strong>を追加するのは、ブリッジが数時間から数日を超える場合、または固定デコーダ間隔が要求される場合です。</td>
<td>Sは、標本識別、スコア生存、またはレスキュー依存の安定性が、同じ状態の証拠または安定した時間一般化としてオーバーリードされるのを防ぎます。</td>
</tr>
<tr>
<td><strong>確率、間隔、予測セット、または棄権を含む出力</strong></td>
<td>基本スタック + クレームによってすでにトリガーされたカード</td>
<td><strong>校正と調整棄権カード</strong></td>
<td>S生の信頼度、しきい値調整、または選択的レポートが、調整されたリスク制御として過剰に読み取られるのを防ぎます。</td>
</tr>
</tbody>
</table>

<h2>短いラベルが弱くなりすぎた3枚のカード</h2>
<p>
次の問題はカード数ではなく、<strong>カードの充足性</strong>でした。スタックの拡張後、現在のサイトのルールがすでに厳しくなっているにもかかわらず、これら 3 枚のカードは依然として短いラベルによって満足されているように聞こえました。このセクションでは、現在のフィールドレベルの要件に合わせた学習ガイドを提供します。
</p>
<table>
<thead>
<tr>
<th>カード</th>
<th>以前の短い説明が弱すぎる理由</th>
<th>このガイドで期待される最小フィールド</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>フュージョンカード</strong></td>
<td><a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>、<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii 他。 (2024)</a>、<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a>、<a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">ボルト 他(2025)</a>、<a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp 他(2025)</a>、<a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a>、<a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al。 (2026)</a> は、同期捕捉、共有低周波構造、数量ブリッジ、およびバンドルの堅牢性が異なる成果である理由を示しています。</td>
<td><strong>取得関係</strong>、<strong>有効期間/時間的カーネル関係</strong>、<strong>共有コンポーネント対固有コンポーネントの開示</strong>、<strong>量ブリッジ/生理学グラウンディング</strong>、単峰性ベースラインおよび以前のみのベースライン、<strong>完全症例/欠落モダリティポリシー</strong>、転送または意見の不一致ウィンドウ、外部校正、および棄権。</td>
</tr>
<tr>
<td><strong>人間プロキシ構成カード</strong></td>
<td><a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li ら(2025)</a>、<a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B'gh 他(2024)</a>、<a href="https://doi.org/10.1002/nbm.5256" target="_blank">モーガンら。 (2024)</a>、<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii 他。 (2024)</a>、<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen 他(2025)</a>、<a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova 他。 (2026)</a> は、すべての行が実際の人間のデータである場合でも、数量タイプ、動作点、共通ドライバー負荷、および不一致トポロジが依然として重要である理由を示します。</td>
<td><strong>プロキシクラス</strong>、<strong>行ごとの直接観察可能および証拠の役割</strong>、<strong>有効時間ウィンドウ/状態軸</strong>、体制の互換性、<strong>運用の成熟度</strong>、<strong>キャリブレータの役割</strong>、<strong>メソッドファミリーの不等価性</strong>、行間の一致/不一致と解決ポリシー、最も強い単一行を超える増分、および残留潜在状態の上限。</td>
</tr>
<tr>
<td><strong>状態継続ブリッジ カード</strong></td>
<td><a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">ボッシュ他(2022)</a>、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONSコンソーシアムほか(2025)</a>、<a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a>、<a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">ヴァン・デ・ヴィル他(2021)</a>、<a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz 他(2025)</a>、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">ウィルソンら。 (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairragkar et al。 (2025)</a> は、標本の身元、輸送物体、救助戦略、スコア生存率が異なるオブジェクトである理由を示します。</td>
<td><strong>ブリッジクラス</strong>、取得順序、経過時間、レジーム連続性、座標転送/変形、<strong>搬送物体/目撃者</strong>、<strong>許容/失敗ルール</strong>、<strong>救助ルートと生の連続性</strong>、ブリッジ検証ラング、および残留ドリフト天井。</td>
</tr>
</tbody>
</table>

<h2>ルート固有のカードを追加する必要があった理由</h2>
<table>
<thead>
<tr>
<th>クレームファミリー</th>
<th>一般的なスコアシートが弱すぎる理由</th>
<th>Card またはこのサイトで現在要求されているログは </th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>言語対応デコード/音声</strong></td>
<td>高スコアは、ターゲットの神経経路だけではなく、候補セットの制限、言語事前分布、プロンプト スキャフォールド、またはセッション固有のサポートによっても得られる可能性があります。</td>
<td><strong>神経貢献カード</strong>プラス<strong>特異性および特性ショートカットカード</strong>; <strong>キャリブレーションと追加棄権カード </strong> および <strong>T 請求が同じセッションを離れるときの時間的有効性カード </strong>。</td>
</tr>
<tr>
<td><strong>EEG ソースイメージング / 逆再構成</strong></td>
<td>A の単一ローカリゼーション スコアは、検証クラス、ソース レジーム、モンタージュ/カバレッジ ポリシー、ソースの深さまたは範囲、ソルバーの不一致によって結果の意味がすべて変わる可能性があるため、弱すぎます。</td>
<td><strong>インバースソルバー合意ログ</strong>、および名前付き検証クラスとベンチマークオブジェクトの開示。</td>
</tr>
<tr>
<td><strong>トラクトグラフィー / 構造コネクトーム</strong></td>
<td>Hub マップとコネクトーム メトリクスは、取得/調和、皮質エンドポイント割り当て、グラフ構築、不確実性ルーティング、外部キャリブレーションによって変化する可能性があります。デフォルトでは、グラフは 1 つの固定オブジェクトではありません。</td>
<td><strong>トラクトグラフィールートカード</strong>.</td>
</tr>
<tr>
<td><strong>効果的な接続 / DCM</strong></td>
<td>出力は依然として、候補モデル ファミリ、観察されたサブシステムのクロージャ / 潜在交絡監査、ノード定義ポリシー、サンプリング / 変換の感度、検証、および信頼性ウィンドウに依存します。</td>
<td><strong>有効接続ルートカード</strong>.</td>
</tr>
<tr>
<td><strong>熱力学的不可逆性</strong></td>
<td>さまざまな論文が、さまざまな信号ルート、粗視化、および推定器ファミリーからさまざまな量を計算しているため、1 つの非可逆性の見出しが 1 つの測定オブジェクトの名前を表すわけではありません。</td>
<td><strong>不可逆性/熱力学ルートカード</strong>.</td>
</tr>
<tr>
<td><strong>マルチモーダル/アトラス事前統合</strong></td>
<td>A の同期またはアトラス情報による結果では、検証された 1 つの生物学的量ではなく、互換性のない時間的オブジェクト、生理学に関連した共有因子、欠落モダリティ スライス、およびモダリティ固有の不一致が依然として混在する可能性があります。</td>
<td><strong>Fusion Card</strong>、有効期間、共有対特定、数量ブリッジ、完全なケース、および不一致の開示を備えています。</td>
</tr>
<tr>
<td><strong>クローズドループ/内蔵コントローラ</strong></td>
<td>L潜時だけでは、何が混乱したか、どの感覚 / 運動 / 内受容チャネルが保存または省略されたか、または結果が時間の経過とともにどの程度一般化したかはわかりません。</td>
<td><strong>介入カード</strong>プラス<strong>身体/環境境界カード</strong>; <strong>時間的有効性カード</strong>を追加するのは、申し立てが同じセッションのデモを上回る場合です。</td>
</tr>
<tr>
<td><strong>L生体プロキシバンドル</strong></td>
<td>プロキシが豊富な人間の証拠は、同じ被験者の状態サンプルではなく、さまざまな数量タイプ、空間単位、タイムスケール、モデル負荷、役割の割り当て、不一致のトポロジーを混合することができます。</td>
<td><strong>ヒューマン プロキシ構成カード</strong>、行ごとの役割、レジームの互換性、成熟度、キャリブレーターの役割、および意見の相違の開示付き。</td>
</tr>
<tr>
<td><strong>連続同一主題/同一脳ブリッジ</strong></td>
<td>標本のアイデンティティは、それ自体では、固定、変形、睡眠/覚醒レジーム、経過時間、日をまたぐ再取得、または適応支援スコアレスキューにわたる状態の連続性を修正しません。</td>
<td><strong>状態継続性ブリッジ カード</strong>、および <strong>T時間的有効性カード</strong>（ブリッジが数時間から数日にわたる場合、搬送物体、許容ルール、およびレスキュー モード開示を含む）。</td>
</tr>
</tbody>
</table>

<h2>スタックが累積される理由</h2>
<table>
<thead>
<tr>
<th>これが欠けている場合</th>
<th>通常の故障モード</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベースラインなし</strong></td>
<td>ゲインが意味のあるものなのか、些細なものなのかが不明瞭になります。</td>
</tr>
<tr>
<td><strong>ベンチマーク オブジェクトなし</strong></td>
<td>異なる実行または論文は異なる非表示ルールに基づいて採点され、それでも比較されます。</td>
</tr>
<tr>
<td><strong>事前登録なし</strong></td>
<td>結果が判明した後、成功条件と停止条件が変動する可能性があります。</td>
</tr>
<tr>
<td><strong>モデルカードなし</strong></td>
<td>故障モードは消えますが、ヘッドライン番号のみが表示されます。</td>
</tr>
<tr>
<td><strong>請求に一致するコンパニオン カードがありません</strong></td>
<td>結果は、実際にサポートされている証拠よりも上にサイレントに宣伝されます。</td>
</tr>
<tr>
<td><strong>陰性結果の記録なし</strong></td>
<td>同じ障害が再発見され、新しい障害であるかのように名前が変更されます。</td>
</tr>
</tbody>
</table>

<h2>最小限の流れとして見る</h2>

01

<h4>ベースラインを置く</h4>
<p>シンプルでも最低限の比較相手から始めましょう。</p>

02

<h4>ベンチマークオブジェクトを修正</h4>
<p>システムを比較する前に、タスク、分割/ランダム化ルール、タスクに一致するメトリック バンドル、運用ベンチマーク制約を調整します。</p>

03

<h4>事前登録成功・失敗・棄権</h4>
<p>より強力な主張を承認、停止、または拒否するとみなされるものを事前に決定します。</p>

04

<h4>トリガーされたコンパニオン カードで結果をレポート</h4>
<p>モデル カード、可観測性バジェット、およびクレーム形状に必要な追加カードはそのままにしておきます。</p>

05

<h4>失敗例を常に見えるようにする</h4>
<p>パイプラインがたまたま動作していた場所だけでなく、破損した場所も記録します。</p>

<h2>失敗例がスタックに残る理由</h2>
<p>
成功した事例だけが保持されると、現場は請求の上限が実際にどこにあるのかを示す歪んだ地図を学習することになります。このサイトでは、使用可能な障害レコードには、<strong> 条件</strong>、<strong> 失敗したメトリクス</strong>、<strong> 障害の原因がリーク、OOD シフト、コンピューティング制限、ブリッジ障害、または融合の不一致によるものなのか</strong>、<strong> したがってブロックされたままであるより強力な主張</strong> が記載されています。
</p>

<strong>最小故障記録</strong>
<p>
データ体制、分割ルール、メトリック バンドル、トリガーされたカード、およびそもそもサポートが失われた主張を述べます。 <strong>itは</strong>を一般化していないなどのあいまいな文章は、調和が変更された後、<strong>のサイト間転送が崩壊し、誤報が2倍になり、特異性と特異性が2倍になったという報告書よりも弱い。ショートカット カードが未解決のまま</strong>になりました。
</p>

<h2>公開ページを読み取る際の最小限のチェック</h2>

<h4>チェックリスト</h4>
<ul>
<li><strong>ベースラインはありますか?</strong>新しい結果が何と比較されるかは明確ですか?</li>
<li><strong>ベンチマーク オブジェクトは修正されていますか?</strong>タスク、分割/ランダム化ルール、メトリック バンドル、バージョン、ガバナンスは表示されていますか?</li>
<li><strong>事前登録はありますか?</strong>実行前に成功、失敗、停止、棄権のルールが記載されていますか?</li>
<li><strong>モデル カードと可観測性バジェットはありますか?</strong>スコア、弱点、失敗例、直接観察可能なもの、潜在状態、クレーム上限は表示されますか?</li>
<li><strong>デコード/バイオマーカー/転送結果の場合、特異性およびショートカット カードが表示されますか?</strong> 件名、セッション、サイト、デバイス、およびプロトコルのショートカットは個別に監査されますか?</li>
<li><strong>テキストまたは音声を発する場合、神経貢献カードは表示されますか?</strong>候補セット、言語モデルまたはプロンプト足場、脳なし/LMなしコントロール、被験者の協力は開示されていますか?</li>
<li><strong>基礎/自己教師あり脳波結果の場合、事前トレーニングカードは表示されますか?</strong>コーパスの重複、調和、適応レジーム、ベンチマークバージョン、および推論段階の制限が記載されていますか?</li>
<li><strong>ESI、トラクトグラフィー、有効接続性、または熱力学的主張の場合、ルート固有のカードまたはログは表示されますか?</strong>検証クラス/グラフ オブジェクト/クロージャー/推定器ファミリーの詳細は、1 つの見出しに隠されるのではなく書かれていますか?</li>
<li><strong>マルチモーダルまたはアトラス優先の場合、フュージョン カードは表示されますか?</strong>取得関係、有効ウィンドウ/時間カーネル関係、共有対固有の開示、数量ブリッジ、完全ケースまたは欠落モダリティ ポリシー、および外部キャリブレーションが書き込まれていますか?</li>
<li><strong>それが閉ループまたは介入の結果である場合、介入カードは表示されますか?また、実施形態が重要な場合は、本体/環境境界カードが表示されますか?</strong>トリガールール、タイミング監査、保持されたループチャネル、および低速境界の省略は開示されていますか?</li>
<li><strong>複数の生きた人間のプロキシ行が一緒に使用されている場合、人間プロキシ構成カードは表示されますか?</strong>プロキシのクラス、直接観察可能であり、行ごとの役割、レジームの互換性、成熟度/キャリブレーターの役割、不一致トポロジー、および最も強い単一行に対する増分が開示されていますか?</li>
<li><strong>クレームが体制間の同一被験者または同一脳の測定を橋渡しする場合、状態継続性ブリッジカードは表示されますか?</strong>搬送物体、許容/失敗ルール、救助ルート、経過時間、体制継続性、変形/登録負荷、およびブリッジ検証ラングが書き込まれていますか?</li>
<li><strong>主張が数時間から数日にわたって上昇する場合、または確信/棄権を報告する場合、時間的妥当性と校正および検証が行われます。棄権カードが表示されますか?</strong> 再校正の負担、転送上限、適合/校正/テストの分離、およびフォールバック動作が記載されていますか?</li>
</ul>

<h2>参考資料</h2>
<ol>
<li>斉藤 哲也 &amp;レムスマイヤー、M. (2015)。不均衡なデータセットでバイナリ分類器を評価する場合、適合率-再現率プロットは ROC プロットよりも有益です。 <a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">doi:10.1371/journal.pone.0118432</a></li>
<li>Roy, Y.、Banville, H.、Albuquerque, I. 他（2021年）。深層学習ベースの脳波分析: 系統的レビュー。 <a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">doi:10.1016/j.ebiom.2021.103275</a></li>
<li>Sun、H.、Paixao、L.、Oliva、J.T.、他（2017年）。睡眠時の脳波から脳年齢を測定します。 <a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">doi:10.1093/スリープ/zsx139</a></li>
<li>ヴァラット、R.、＆amp;ウォーカー、M.P. (2021)。自動睡眠ステージングのためのオープンソースの高性能ツール。 <a href="https://doi.org/10.7554/eLife.70092" target="_blank">doi:10.7554/eLife.70092</a></li>
<li>Chaibub Neto, E.、Pratap, A.、Perumal, T.M. 他（2019年）。機械学習ベースの診断アプリケーションに対する被験者の特性の影響を検出します。 <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Xu、M.、Yao、S.、Wei、Z.、他。 （2020年）。深層学習による EEG デコードにおけるデータセット間の変動性の問題。 <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Di, Y.、An, X.、Zhong, W.、Liu, S.、およびミン、D. (2021)。安静状態脳波に基づく個人識別の時間ロバスト性分析。 <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
<li>EEG チャレンジ (2025) のホームページ。 <a href="https://eeg2025.github.io/" target="_blank">公式サイト</a></li>
<li>EEG チャレンジ (2025) ルール。 <a href="https://eeg2025.github.io/rules/" target="_blank">公式ルール</a></li>
<li>EEG チャレンジ (2025) スターター キット。 <a href="https://eeg2025.github.io/baseline/" target="_blank">公式スターターキットページ</a></li>
<li>EEG Challenge (2025) のリーダーボードと主催者の事後分析。 <a href="https://eeg2025.github.io/leaderboard/" target="_blank">公式リーダーボード</a></li>
<li>Xiong, W.、Li, J.、Li, J.、Zhu, K.、およびジャン、C. (2025/2026)。 EEG-FM-Bench: EEG 基礎モデルの系統的評価のための包括的なベンチマーク。 <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
<li>Liu, D.、Chen, Y.、Chen, Z.、Cui, Z.、Wen, Y.、An, J.、Luo, J.、およびウー、D. (2026)。 EEG 基礎モデル: 進捗状況、ベンチマーク、未解決の問題。 <a href="https://arxiv.org/abs/2601.17883" target="_blank">arXiv:2601.17883</a></li>
<li>Kothe, C.、Shirazi, S. Y.、Stenner, T. 他(2025年)。同期されたマルチモーダル記録のためのラボ ストリーミング レイヤー。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H.、Jafarian, A.、Zeidman, P. 他（2020年）。 EEG および fMRI 用のベイジアン フュージョンおよびマルチモーダル DCM。 <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>Vafaii、H.、Mandino、F.、Desrosiers-Gregoire、G.、他。 （2024年）。自発的な脳活動の多峰性測定により、皮質機能組織の共通パターンと多様なパターンの両方が明らかになります。 <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen、J. E.、Lewis、L. D.、Coursey、S. E.、他(2025年)。 EEG-PET-MRI を同時に行うことで、覚醒時とノンレム睡眠時の時間的に結合し、空間的に構造化された脳のダイナミクスを特定します。 <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Johansen, A.、Beliveau, V.、Colliander, E. 他（2024年）。シナプス密度の生体内高解像度人間の脳アトラス。 <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Li, X.、Zhu, X.-H.、Li, Y. 他(2025年)。動的重水素磁気共鳴分光イメージングを使用した、人間の脳における主要なグルコース代謝率の定量的マッピング。 <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Baadsvik, E.L.、Weiger, M.、Froidevaux, R. 他（2024年）。生体内における人間の脳のミエリン二重層マッピング。 <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Hirschler、L.、他。 (2025年)。ヒトの MRI で測定された CSF 可動性の領域固有の要因。 <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum、P.、他。 （2026年）。グリンファティック系は、ヒトの脳からアミロイド ベータとタウを血漿まで除去します。 <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Lu, X.、Han, X.、Meirovitch, Y. 他（2023年）。哺乳動物の脳全体の高品質な光学的および超微細構造研究のために細胞外空間を保存します。 <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Bosch, C.、Ackels, T.、Pacureanu, A. 他（2022年）。相関生体内生理学、シンクロトロンマイクロトモグラフィー、体積電子顕微鏡法による脳組織の機能的かつマルチスケール 3D 構造研究。 <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>MICrONS コンソーシアム、J.A. Bae、W.-C. Lee A.、ら。 (2025年)。マウス視覚野の複数の領域にわたる機能的コネクトミクス。 <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>アタルド、A.、フィッツジェラルド、J. E.、およびM.J. シュニッツァー (2015)。生きた成人CA1海馬における樹状突起棘の不永性。 <a href="https://doi.org/10.1038/nature14467" target="_blank">ドイ:10.1038/nature14467</a></li>
<li>Tang、J.、LeBel、A.、Jain、S.、およびヒュース、A.G. (2023)。非侵襲的な脳記録からの連続言語の意味的再構築。 <em>Nature Neuroscience</em>、26、858-866。 <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Défossez、A.、Caucheteux、C.、Rapin、J.、Kabeli、O.、&amp;キング、J.-R. （2023年）。非侵襲的な脳記録から音声知覚を解読します。 <em>Nature Machine Intelligence</em>、5、1097-1107。 <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">doi:10.1038/s42256-023-00714-5</a></li>
<li>d'Ascoli, S.、Bel, C.、Rapin, J.、Banville, H.、Benchetrit, Y.、Pallier, C.、およびキング、J.-R. (2025年)。非侵襲的な脳記録から個々の単語を解読する方向へ。 <em>Nature Communications</em>、16、10521.<a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Wairragkar, M.、Card, N.S.、Singer-Clark, T.、Hou, X.、Iacobacci, C.、Miller, L.M.、Hochberg, L.R.、Brandman, D.M.、&amp;;スタヴィスキー、SD (2025)。瞬間的に音声を合成する神経人工器官。 <em>ネイチャー</em>、644(8075)、145-152。 <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Horrillo-Maysonnial、A.、Avigdor、T.、Abdallah、C.、他（2023年）。標的密度の電極配置は、てんかんにおける電源イメージングのための従来の高密度EEGとの高い一致を実現します。 <em>臨床神経生理学</em>、156、262-271。 <a href="https://doi.org/10.1016/j.clinph.2023.08.009" target="_blank">doi:10.1016/j.clinph.2023.08.009</a></li>
<li>Rong、J.、Sun、R.、Joseph、B.、Worrell、G.、および彼、B. (2025)。深層学習ベースの EEG ソース イメージングは​​、電極構成が変化しても堅牢です。 <em>C臨床神経生理学</em>、175、2010730。<a href="https://doi.org/10.1016/j.clinph.2025.04.009" target="_blank">doi:10.1016/j.clinph.2025.04.009</a></li>
<li>Unnwongse, K.、Van Klink, N.、Tousseyn, S. 他（2023年）。頭蓋内電気刺激を使用したEEGソースイメージングの検証。 <em>ブレインコミュニケーションズ</em>、5(1)、fcad023。 <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/ブレインコム/fcad023</a></li>
<li>Hao, S.、Zhao, H.、Feng, Z. 他(2025年)。薬剤耐性てんかんにおける HD-EEG ソースイメージングと同時 SEEG 記録。 <em>てんかん</em>、66(11)、4451-4464。 <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Pascarella, A.、Mikulan, E.、Sciacchitano, F. 他（2023年）。焦点ソースを使用した ESI メソッドの生体内検証。 <em>NeuroImage</em>、277、120219.<a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">doi:10.1016/j.neuroimage.2023.120219</a></li>
<li>Feng、Z.、Guan、C.、および日曜日、Y. (2025)。 Block-Champagne: 拡張 E/MEG ソースをイメージングするための新しいベイジアン フレームワーク。 <em>医用画像に関するIEEEトランザクション</em>。 <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Gajwani、M.、Oldham、S.、Pang、J.C.、Arnatkevičiütė、A.、Tiego、J.、Bellgrove、M.A.、&amp;;フォルニト、A. (2023)。ヒトコネクトームのハブは拡散 MRI で一貫して特定できますか? <em>ネットワーク神経科学</em>、7(4)、1277-1304。 <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">doi:10.1162/netn_a_00324</a></li>
<li>He, Y.、Hong, Y.、Wu, Y. 他（2024年）。球面デコンボリューションに基づくトラクトグラムのフィルタリングにより、構造コネクトームの左右性が変化します。 <em>NeuroImage</em>、297、120904.<a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">doi:10.1016/j.neuroimage.2024.120904</a></li>
<li>McMaster、E.M.、Newlin、NR、Rudravaram、G. 他(2025年)。ボクセル サイズの差異を考慮した調和のとれたコネクトーム リサンプリング。 <em>磁気共鳴画像</em>, 122, 110424.<a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">doi:10.1016/j.mri.2025.110424</a></li>
<li>Bramati、I.B.、Szczupak、D.、Carneiro Monteiro、M.、Meereles、F.、Menezes Guimarães、D.、Dean、R.J.、Paul、L.K.、および;トヴァー・モール、F. (2026)。拡散 MRI サンプリング スキームは、拡散測定基準とトラクトグラフィーに偏りをもたらします。 <em>ニューロイメージングのフロンティア</em>、5、1670604.<a href="https://doi.org/10.3389/fnimg.2026.1670604" target="_blank">doi:10.3389/fnimg.2026.1670604</a></li>
<li>Manzano-Patrón, J.P.、Deistler, M.、Schröder, C. 他(2025年)。拡散 MRI におけるシミュレーションベースの推論を使用した不確実性マッピングと確率的トラクトグラフィー: 古典的なベイズとの比較。 <em>医療画像分析</em>、103、103580.<a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">doi:10.1016/j.media.2025.103580</a></li>
<li>Zhu, S.、Huszar, I.N.、Cottaar, M. 他(2025年)。ハイブリッド MRI 顕微鏡トラクトグラフィーによる構造コネクトームの画像化。 <em>医療画像分析</em>、102、103498.<a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">doi:10.1016/j.media.2025.103498</a></li>
<li>Penny、WD、Stephan、K.E.、Mechelli、A.、およびフリストン、K.J. (2004)。動的因果モデルの比較。 <em>NeuroImage</em>、22(3)、1157-1172。 <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa、M.J.、Friston、K.、およびペニー、W. (2012)。動的因果モデルの事後選択。 <em>Journal of Neuroscience Methods</em>、208(1)、66-78。 <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Smith、S.M.、Miller、K.L.、Salimi-Khorshidi、G.、Webster、M.、Beckmann、C.F.、Nichols、T.E.、Ramsey、J.D.、および;ウールリッチ、M.W. (2011)。 FMRI のネットワーク モデリング手法。 <em>NeuroImage</em>、54(2)、875-891。 <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">doi:10.1016/j.neuroimage.2010.08.063</a></li>
<li>バーネット、L.、＆amp;セス、AK. (2017)。サブサンプリングされた連続時間神経生理学的プロセスに対するグレンジャー因果関係の検出可能性。 <em>Journal of Neuroscience Methods</em>、275、93-121。 <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">doi:10.1016/j.jneumeth.2016.10.016</a></li>
<li>Vink、J.J.T.、Klooster、D.C.W.、Ozdemir、R.A.、Westover、MB、Pascual-Leone、A.、および;シャフィ、M.M. (2020)。 EEG の機能的接続性は、脳の因果関係の弱い予測因子です。 <em>脳トポグラフィー</em>、33(2)、221-237。 <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">doi:10.1007/s10548-020-00757-6</a></li>
<li>ビジャベルデ、A.F.、チアンティス、N.、およびJ. R. バンガ (2019)。非線形生物学モデルの未知の入力、状態、パラメーターの完全な可観測性と推定。 <em>Journal of the Royal Society Interface</em>、16(156)、20190043.<a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">doi:10.1098/rsif.2019.0043</a></li>
<li>Novelli, L.、Barnett, L.、Seth, A. K.、&amp;ラジ、A. (2025)。血行動態応答関数の最小位相特性、および fMRI におけるグレンジャー因果関係への影響。 <em>人間の脳のマッピング</em>、46(10)、e70285。 <a href="https://doi.org/10.1002/hbm.70285" target="_blank">doi:10.1002/hbm.70285</a></li>
<li>Jafarian, A.、Karadag Assem, M.、Kocagoncu, E. 他（2024年）。安静状態の脳磁図の動的因果モデリングの信頼性。 <em>人間の脳のマッピング</em>、45(10)、e26782。 <a href="https://doi.org/10.1002/hbm.26782" target="_blank">doi:10.1002/hbm.26782</a></li>
<li>Yan, J.、Zhang, S.-W.、Zhang, C.、Huang, W.、Shi, J.、およびチェン、L. (2026)。生物学的ネットワーク再構築のための潜在交絡因子の下での動的因果関係。 <em>パターン分析とマシンインテリジェンスに関するIEEEトランザクション</em>。 <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">doi:10.1109/TPAMI.2026.3658839</a></li>
<li>Lynn、C.W.、Cornblath、E.J.、Papadopoulos、L.、他（2021年）。人間の脳における詳細なバランスの崩れとエントロピー生成。 <em>PNAS</em>、118(47)、e2109889118。 <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>石原 和也 &amp; <li>島崎 洋 (2025)状態空間運動イジング モデルは、まばらに活動する非平衡ニューロンのダイナミクスにおけるタスク依存のエントロピー フローを明らかにします。 <em>Nature Communications</em>、16、10852。<a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Egger, A.、Bayon, C.、d'Almeida, J. 他（2024年）。手のジェスチャーの解読に影響を与える時間脳波ダイナミクス: 10 時間の研究。 <em>Scientific Reports</em>、14、20247.<a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
<li>Idziak、A.、Inavalli、V.V.G.K.、Bancelin、S.、Arizano、M.、およびナゲルル、U.V. (2023)。マウスの器官型海馬スライスの微細解剖学に対する化学固定の影響。 <em>eニューロ</em>。 <a href="https://doi.org/10.1523/ENEURO.0104-23.2023" target="_blank">doi:10.1523/ENEURO.0104-23.2023</a></li>
<li>Benisty, H.、Barson, D.、Moberly, A. H.、他（2024年）。皮質ネットワークの機能的接続の急速な変動は、自発的な行動を符号化します。 <em>Nature Neuroscience</em>。 <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
</ol>

<h2>次の行き先</h2>
<p>
権威のあるカードフィールドについては <a href="https://mind-upload.com/verification.html">Verification</a> に、実践的な実装については <a href="https://mind-upload.com/datasets.html#l0-practice">Datasets / L0 Practice</a> に、クロスドメインの判例については <a href="https://mind-upload.com/verification.html#casework">Verification Casework</a> に戻ってください。
</p>
