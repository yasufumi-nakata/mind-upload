# Wiki: 主張と証拠の読み方

> 強い言葉は安いです。強力な証拠はありません。
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-04-01 / Role: 読書ガイド

## このページの役割
このページでは、派手な神経科学と WBE の文言を、主張の強さ、証拠のクラス、および主張が強く読み取れるようになる前に必要な最小限のルート カードに戻します。目標は進歩を阻害することではなく、スコアのインフレと証拠クラスの崩壊を入り口で阻止することです。

## 正確性に関する注記
このページはテクノロジーと自然科学の側面に留まります。ヘッドライン、ハイスコア、または 1 つのモデリング フレームワークを、開示された測定条件、外部検証、または棄権の代替として扱うものではありません。

## 公開ページへ戻る
- [WBE の概要](https://mind-upload.com/wbe_101.html)
- [検証プラットフォーム](https://mind-upload.com/verification.html)
- [よくある質問](https://mind-upload.com/faq.html)

## 関連 Wiki ページ
- [Wiki: WBE の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - 請求項を読む前に全体的な技術的な全体像を設定します。
- [Wiki: 検証インフラストラクチャの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - ルート カード、監査、事前登録が運用上重要である理由を説明します。
- [Wiki: 観察から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - ESI、DCM、SCM がすべて同じ種類の主張をサポートしていない理由を説明します。
- [Wiki: 測定スタックの可観測性とクレームの上限](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling) - 各モダリティが直接観察する内容と、請求の上限がどこに現れるかを示します。

## 現在わかっていること
- 再現可能な分析、解読、介入予測、身元主張には、さまざまな証拠が必要です。
- 異なる因果関係のストーリーから同じスコアが発生する可能性があるため、直接観測可能なルートとショートカット ルートを分離する必要があります。
- 同じ被験者または同じセッションのヒューマン プロキシ バンドルでは、数量タイプの不一致、コホート レジームの不一致、および共通要因のあいまいさが未解決のままになる可能性があります。
- 最近の一次文献では、デコード、人間代理構成、トラクトグラフィー、効果的な接続性、熱力学的主張、および閉ループに関する、より厳格な初心者向けの読み取りルールがサポートされています。

## まだわかっていないこと
- どの測定スタックが WBE レベルの内部状態のキャプチャに十分であるかはまだ未解決のままです。
- 今後の L4 連続性テストがどこまで ID 主張を正当化するかは未解決のままです。

---

<h2>基本ルール</h2>
<p>
神経科学や WBE の見出しが強力に聞こえる場合、それが印象的であるかどうかを最初に尋ねないでください。 <strong> 直接観察されたこと</strong>、<strong> モデルまたは以前のモデルを通じてのみ推測されたこと</strong>、<strong> 結果がまだ特定できないこと</strong> を尋ねます。このページはそれを行うための最短の初心者ルートです。
</p>

<strong>2026-03-26 深化: この初心者ページにもう一度書き直す必要がある理由</strong>
<p>
2026 年 3 月 19 日の書き換えにより、いくつかの大きなオーバーリードが修正されましたが、初心者向けの重要なショートカットが 1 つ残っていました。それは、<strong> 同一被験者マルチモーダル </strong> または <strong> リビング ヒューマン全脳測定 </strong> を、すでにほぼ完全な状態アクセスを意味しているかのように読み取るのがまだ簡単すぎました。このサイト全体の最近の公開アップデートでは、トラクトグラフィー、効果的な接続、熱力学的不可逆性、神経の寄与、および身体/環境の境界のためのルート カードに加えて、<strong>Human Proxy Composition Card</strong> および <strong>Fusion Card</strong> が必要になりました。このページでは、人間とプロキシの区別を後の技術的なページに任せるのではなく、入り口で明らかにしています。
</p>

<strong>2026-03-29 深化: 因果関係グラフのヘッドラインにはまだクロージングとサンプリング監査が必要</strong>
<p>
このページには、有効な接続のショートカットが 1 つ残っていました。 <strong>「因果関係の配線が見つかった」</strong> を読むのはまだ簡単すぎて、あたかも候補モデルとモデルの比較で主な故障モードがすでにカバーされているかのように聞こえました。現在の文献はそれを裏付けていません。 <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">Smith et al. (2011)</a> は、ラグベースの fMRI 法のパフォーマンスが悪く、<strong> の機能的に不正確な ROIs</strong> がネットワーク推定に特に悪影響を及ぼすことを示しました。 <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">バーネット＆アンプ; Seth (2017)</a> は、サブサンプリングによって <strong> 検出可能黒点 </strong> が作成される可能性があることを示しました。 <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">ヴィンクら(2020) </a> は、安静状態の EEG 機能接続性が、TMS 誘発伝播分散の 10% 未満の </strong> 未満の <strong> を説明することを示しました。 <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">ヴィラベルデら(2019)</a> は、状態、入力、パラメーターの可観測性がそれ自体の問題である理由を示しました。<a href="https://doi.org/10.1002/hbm.70285" target="_blank">Novelli et al. (2025) </a> は、<strong> 遅い BOLD サンプリング </strong> が依然として偽のグレンジャー因果推論を誘発する可能性があることを示しました。<a href="https://doi.org/10.1002/hbm.26782" target="_blank">Jafarian et al。 (2024) </a> は、信頼性自体が厳しい調達体制に条件があることを示しました。 (2026) </a> は、潜在的な交絡因子が依然として活発な再構成問題であることを示しました。したがって、このサイトでは、因果関係グラフの見出しは、上昇する前に、<strong>観察されたサブシステムの閉鎖/潜在交絡監査</strong>、<strong>ノード定義ポリシー</strong>、<strong>サンプリング/変換感度</strong>、<strong>検証</strong>、<strong>信頼性ウィンドウ</strong>、および<strong>棄権</strong>を開示する必要があります。モデル条件付き因果仮説を上回る。
</p>

<h2>技術的なレベルを失うことなく、L0 ～ L5 を日常言語で言い換える</h2>
<table>
<thead>
<tr>
<th>レベル</th>
<th>毎日の安全な読書</th>
<th>最低限の証拠フロア</th>
<th>ブロックへの最速のオーバーリード</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>他の人が同じ結果を再実行できます。</td>
<td>パブリック データまたはアーティファクト パック、コード、環境、分割ルール、およびログは、サードパーティによる再実行に十分な完全性を備えています。</td>
<td><strong>rerunnable</strong> を <strong>generalizable</strong>.</td> として読み取らないでください
</tr>
<tr>
<td><strong>L1</strong></td>
<td>A 信号は、規定の条件下でデコードまたは分類できます。</td>
<td>参加者/セッションの独立した評価、測定条件の開示、関連するベースライン、ショートカット監査、信頼崩壊時の棄権。</td>
<td><strong>高スコア</strong>を<strong>標的特異的な神経証拠として読み取らない</strong>または<strong>正しい内部メカニズム</strong>.</td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>条件が変更された後もモデルは何かを予測または制御します。</td>
<td>保留された摂動または反事実の評価、事前に登録された成功/失敗ルール、および効果が固定データセット体制を超えて存続するという証拠。</td>
<td><strong>観測データに適合</strong>を読み込まない<strong>因果的堅牢性</strong>.</td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>A 閉ループは、開示された境界の下で安定して動作します。</td>
<td>L待ち時間/ジッター/安全停止ログ、再キャリブレーション負荷、および感覚、運動、および内受容ループの保存、置換、および省略された身体/環境境界カードの名前付け。</td>
<td><strong>リアルタイムデモ</strong>を<strong>解決された実施形態として読み取らないでください</strong>または<strong>状態完全閉ループ</strong>.</td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>連続性またはアイデンティティは明示的にテストされています。</td>
<td>事前登録された導通テスト、分岐処理、メモリ/値/学習基準、および明示的な代替説明。</td>
<td><strong>機能的類似性</strong>を<strong>同一性保持</strong>.</td>として読み取らない
</tr>
<tr>
<td><strong>L5</strong></td>
<td>A システムは世界で耐久性のある動作を考慮されています。</td>
<td>運用、安全、およびガバナンスの条件は、公開された形式で存在する必要があります。</td>
<td><strong>ラボ内で動作する</strong>を読み取らないでください<strong>導入準備完了</strong>.</td>
</tr>
</tbody>
</table>

<h2>一般的な見出しフレーズをより安全な最初の読みに変換する</h2>
<table>
<thead>
<tr>
<th>見出しスタイルのフレーズ</th>
<th>最も安全なデフォルト読み取り</th>
<th>より強力なものを読む前に尋ねるべきこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>「脳から回収された文章」</strong></td>
<td>通常は、タスクおよび参加者固有の条件下での L1 デコードまたは支援 BCI 結果。</td>
<td>タスクの制約、事前言語、候補セット、被験者の協力要件、キャリブレーション負担、およびノーブレイン/ノーLM/シャッフルベースラインは何でしたか?</td>
</tr>
<tr>
<td><strong>「95%の精度でバイオマーカーを発見」</strong></td>
<td>通常は、特定の取得および分割レジームに基づく L1 分類子です。</td>
<td>サブジェクトとセッションは切り離されていましたか?メタデータまたはサブジェクトのフィンガープリントでスコアが説明できましたか?また、サイト/デバイス/データセット全体でパフォーマンスがチェックされましたか?</td>
</tr>
<tr>
<td><strong>「生きた人間の脳全体の状態を計測した」</strong></td>
<td>通常は、特定のコホート、ハードウェア、モデルの負荷の下でいくつかの制限された量を制約する、プロキシが豊富な人間または同時のマルチモーダルな結果です。</td>
<td>各行は何を直接観察しましたか、行は実際に同じサブジェクト/同じセッション/同じ摂動でしたか、共有対固有の分解と共通ドライバ監査は存続しましたか、キャリブレータの役割と残留隠れ状態の上限はどのようなものでしたか?</td>
</tr>
<tr>
<td><strong>「生きている人間のコネクトームをマッピングした」</strong></td>
<td>通常は、エッジ完全なコネクトームではなく、トラクトグラフィー条件付きマクロ経路推定です。</td>
<td>直接観察可能物、トラクトグラフィーの事前分布/フィルタリングの選択、不確実性の処理、および同一脳または外部検証ルートは何でしたか?</td>
</tr>
<tr>
<td><strong>「因果関係のある配線/効果的な接続が見つかりました」</strong></td>
<td>通常は、モデル条件付き因果仮説。</td>
<td>どの候補モデル空間が競合しましたか、観測されたサブシステムまたは潜在交絡境界はどのように監査されましたか、ノードはどのように定義されましたか、どのような観測とサンプリングの仮定が課されましたか、どのようにモデル回復がチェックされましたか、どのような検証または信頼性ウィンドウが存在しますか?</td>
</tr>
<tr>
<td><strong>「脳データにおけるエントロピー生成/不可逆性の測定」</strong></td>
<td>通常は、モダリティと推定器で条件付けされた補助的非平衡解析。</td>
<td>信号ルート、粗視化、推定器ファミリー、ヌル制御、数量タイプ、棄権境界とは何ですか?</td>
</tr>
<tr>
<td><strong>「安定したリアルタイム閉ループを実行しました」</strong></td>
<td>通常は、特定の感覚/運動契約に基づくローカルな閉ループの成功。</td>
<td>どのループが保存され、どのループが置き換えられ、どの再キャリブレーションが必要で、どの身体/環境チャネルが省略されたままですか?</td>
</tr>
</tbody>
</table>

<h2>なぜ初心者ルールを厳しくしなければならなかったのか</h2>

<strong>1。高い精度はデフォルトではターゲット固有の証拠にはなりません</strong>
<p>
これは、初心者が最も誤解しやすい最初の場所です。 <a href="https://www.nature.com/articles/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019) </a> は、モデルがターゲット レーベルだけでなく参加者が誰であるかを学習するため、レコード単位の分割がパフォーマンスを水増しする可能性があることを示しました。 <a href="https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.672946/full" target="_blank">Diら(2021)</a> は、安静状態の脳波が時間堅牢な個人識別をサポートできることを示しました。 <a href="https://www.frontiersin.org/articles/10.3389/fnhum.2020.00103/full" target="_blank">Xuら。 (2020) </a> は、データセット間の変動が EEG デコードの一般化を弱めることを示しました。一方、<a href="https://www.nature.com/articles/s41593-023-01304-9" target="_blank">Tangらは、 (2023) </a> は、非侵襲的な意味論的再構成には被験者の協力が必要であることを示しました。 (2023)</a> は、移植された参加者固有の条件下で強力な音声 BCI パフォーマンスを達成しました。したがって、このサイトでは、分割単位、測定条件、タスク/言語事前、ショートカットルートが公開されるまでは、デコード見出しは強く読まれないようにしています。
</p>

<strong>2。プロキシが豊富な人間のマルチモーダルな証拠は自動的に同一被験者状態の閉鎖にはなりません</strong>
<p>
現在の人間の委任状は、あたかもすでに 1 つの状態完全なメーターに収束しているかのように、修辞的に列挙するのが簡単であるため、初心者ルートにも厳格化が必要でした。一次文献ではそのショートカットはサポートされていません。 <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">ヨハンセンら。 (2024) </a> は、33 人の参加者による SV2A アトラスを提供しました。<a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al。 (2025) </a> は、13 人の複製を使用して 51 人の青少年における 5 つの代謝物の区画類似性グラフを定義しました。<a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al。 (2025) </a> は、5 人の健康な参加者における 7 T 動的 DMRSI 動態マップを報告しました。<a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al。 (2025) </a> は、その配列が正味の流れの方向を決定しない健康な若年成人における特殊な 7 T CSF 移動経路を報告しました。 (2026) </a> は、治験機器とマルチコンパートメント モデルを使用した 39 人の参加者によるランダム化クロスオーバー試験において、モデルに基づいた一晩のバイオマーカー流出を推定しました。これらは実際の進歩ですが、1 つの共有された推論対象ではありません。並行して、<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii ら。 (2024) </a> は、同時モダリティ全体で共通構造と分岐構造の両方を示しました。<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025) </a> は、同時 EEG-PET-MRI において結合した全体的な進行と 2 つの異なるネットワーク パターンを示しました。<a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025) </a> は主要なグローバル fMRI モードの実質的な自律結合を示し、<a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025) </a> は、重要な皮質 ΔBOLD ボクセルの約 40% が酸素代謝の変化に対抗できることを示しました。したがって、このサイトでは、<strong>same-subject</strong>、<strong>multimodal</strong>、および <strong>proxy-rich</strong> 自体は、全脳状態言語を正当化するものではありません。代わりに、プロキシ クラス、キャリブレーター ロール、および共通ドライバーの監査がトリガーされます。
</p>

<strong>3。 「Connectome」は依然としてさまざまな証拠クラスに名前を付けています</strong>
<p>
<strong>connectome</strong> という単語が証拠クラスで大きな広がりを隠しているため、初心者ルートも強化する必要がありました。 <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4246325/" target="_blank">トーマスら。 (2014)</a> は、拡散 MRI トラクトグラフィーの解剖学的精度に固有の限界を示しました。<a href="https://www.nature.com/articles/s41467-017-01285-x" target="_blank">Maier-Hein et al. (2017) </a> は、コミュニティ チャレンジで基本的な曖昧さと多くの無効なバンドルを暴露しました。<a href="https://pubmed.ncbi.nlm.nih.gov/32816112/" target="_blank">Schilling et al。 (2020) </a> は、高い解剖学的精度が強力な開始/終了/除外事前分布に依存することを示しました。 (2021) </a> は同じ脳内で局所的に繰り返される故障モード。したがって、生きている人間のトラクトグラフィー グラフは、デフォルトではコネクトーム完全としてここでは読み込まれません。トラクトグラフィールートカードが表示されない限り、</strong> より前の <strong> マクロ経路に留まります。
</p>

<strong>4。モデル条件付きグラフは因果関係が発見されない</strong>
<p>
効果的な接続を実現するために、問題は DCM や関連モデルが役に立たないということではありません。問題はそれらを読みすぎることです。 <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811904001648" target="_blank">ペニーら(2004) </a> は、DCM 推論がモデル構造に依存することを明示しました。 (2012)</a> は、より大きな候補空間をより効率的に検索できることを示しました。しかし、発見された因果関係として有向グラフを読み取るには、まだ十分ではありません。 <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">Smith et al. (2011)</a> は、遅延ベースの fMRI 法のパフォーマンスが悪く、<strong> 機能的に不正確な ROIs</strong> がネットワーク推定に特に悪影響を及ぼすことを示しました。 <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">バーネット&アンプ; Seth (2017)</a> は、サブサンプリングによって <strong> 検出可能なブラック スポット </strong> および <strong> スイート スポット </strong> が作成される可能性があることを示しました。 <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">ヴィンクら(2020) </a> は、安静状態の EEG 機能的接続性が、TMS 誘発伝播分散の 10% 未満の </strong> 未満の <strong> を説明することを示しました。 <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">ヴィラベルデら(2019)</a> は、完全な入力状態パラメータ システムの <strong>observability</strong> が独自の疑問である理由を示しました。 <a href="https://doi.org/10.1002/hbm.70285" target="_blank">Novelli et al. (2025) </a> は、現実的な HRF 変動だけでは偽陽性を強制する必要はないが、<strong> の遅い BOLD サンプリング </strong> は依然として偽のグレンジャー因果推論を誘発する可能性があることを示しました。 <a href="https://doi.org/10.1002/hbm.26782" target="_blank">ジャファリアンら(2024) </a> は、厳密に一致した MEG セッションの下で信頼性が高くなる可能性があることを示しました。 (2026)</a> は、潜在的な交絡因子が依然として活発な再構成問題であることを示しました。したがって、このサイトでは、<strong>モデル空間開示のない密な有効接続性グラフ</strong>、<strong>観察されたサブシステムの閉鎖/潜在交絡監査</strong>、<strong>ノード定義ポリシー</strong>、<strong>サンプリング/変換感度</strong>、<strong>回復</strong>、<strong>検証</strong>、<strong>信頼性window</strong>、<strong>abstention</strong>は<strong>モデル条件付き因果仮説</strong>のままです。
</p>

<strong>5。熱力学キーワードは依然としてさまざまな測定オブジェクトを隠します</strong>
<p>
古い初心者向けの表現も、熱力学的主張としては弱すぎました。 <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8617485/" target="_blank">Lynnら。 (2021) </a> は、粗粒度の BOLD 状態遷移からエントロピー生成の下限を推定しました。<a href="https://academic.oup.com/cercor/article/33/5/1856/6577164" target="_blank">de la Fuente et al。 (2023) </a> は ECoG で時間的不可逆性復号を使用し、<a href="https://www.nature.com/articles/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> は、非定常状態空間運動イジング モデルにおけるモデルベースのエントロピー フローを推定しました。これらは関連していますが、同一のオブジェクトではありません。したがって、このサイトでは、初心者が <strong>「熱力学的紙」</strong> が物理的散逸または WBE 関連コストの一般的な測定値を自動的に意味するという解釈を許可しなくなりました。
</p>

<strong>6。リアルタイム ループを成功させるには、身体と環境の境界を明らかにする必要がある</strong>
<p>
最後に、クローズドループの見出しには、より厳格な初心者ルールが必要でした。 <a href="https://pubmed.ncbi.nlm.nih.gov/31551604/" target="_blank">Musall et al. (2019)</a> は、豊富に変化した動きが皮質全体の活動を支配することを示しました。<a href="https://www.nature.com/articles/nn.3567" target="_blank">Saleem et al. (2013)</a> は、移動運動によって視覚皮質コーディングが変化することを示しました。また、<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8715714/" target="_blank">Flesher et al. (2021) </a> は、触覚フィードバックを復元するとロボット アームの制御が向上することを示しました。したがって、安全な読み取り値は、<strong>「解決された閉ループ」</strong> ではなく、<strong>「特定の保持/置換境界の下で動作する特定のローカル ループ」です。</strong>
</p>

<h2>見出しの強力なバージョンを信じる前の 7 つの質問</h2>

<h4>チェックリスト</h4>
<ul>
<li><strong>直接観察されたもの?</strong>センサー出力と推定された内部状態を分離。</li>
<li><strong>どのようなモデル空間または事前分布が課せられましたか?</strong>候補モデル、言語事前分布、トラクトグラフィーフィルター、および神経質量の仮定がすべて重要です。</li>
<li><strong>スコアを再現できるショートカットはどれですか?</strong> サブジェクト/セッションのフィンガープリント、メタデータの漏洩、デバイスの違い、および候補セットの構造を明示的にチェックする必要があります。</li>
<li><strong>これがヒューマン バンドルまたはマルチモーダル バンドルの場合、各行は何を直接監視しますか?</strong> プロキシ クラス、運用の成熟度、キャリブレーターの役割、および考えられる共通ドライバー ルートは個別に名前を付ける必要があります。</li>
<li><strong>どのような外部検証または保持された検証が存在しますか?</strong>同一データセットの適合は、摂動、刺激、同一脳トレース、または外部ベンチマーク予測よりも弱いです。</li>
<li><strong>どのようなループまたは状態変数が測定の範囲外に残っていますか?</strong>境界および隠れ状態の省略が依然としてクレームの上限を設定しています。</li>
<li><strong>論文はどこを棄権しますか?</strong>強力な論文には、どの解釈を行うかが記載されています<em></em>はサポートしません。</li>
</ul>

<h2>この初心者ページの次に進むべき場所</h2>
<table>
<thead>
<tr>
<th>見出しの主な内容が...</th>
<th>次に読む</th>
<th>なぜ</th>
</tr>
</thead>
<tbody>
<tr>
<td>デコード / バイオマーカー / 音声 / 脳波スコア</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling">測定スタックの可観測性とクレーム上限</a></td>
<td>直接観察されたものと開いたままのショートカット ルートを修正します。</td>
</tr>
<tr>
<td>L生きている人間のマルチモーダル/プロキシリッチの全脳クレーム</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition">Human プロキシの構成とルートの成熟度</a></td>
<td>同じ主題の言語が許可される前に、行、プロキシ クラス、キャリブレーターの役割、および共通ドライバー監査によって直接監視可能を分離します。</td>
</tr>
<tr>
<td>コネクトーム / トラクトグラフィー / 事前構造用</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/connectome-is-not-enough">配線図だけでは不十分な理由</a></td>
<td>足場の進行状況と隠れ状態の完全性を分離します。</td>
</tr>
<tr>
<td>DCM / 効果的な接続性 / 因果関係グラフ</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation#effective-connectivity-route-card">有効接続ルートカード</a></td>
<td>候補とモデルの依存関係が始まりにすぎない理由、およびクロージャ、ノード定義、サンプリング、検証が依然として開示されなければならない理由を示しています。</td>
</tr>
<tr>
<td>エントロピー生成 / 不可逆性 / 時間の矢</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/thermodynamic-grounding-basics#irreversibility-route-card">不可逆性ルートカード</a></td>
<td>エスティメーター ファミリとヌル コントロールを分離します。</td>
</tr>
<tr>
<td>クローズドループ / BCI / 実施例</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ、レイテンシー、ジッター、安全停止</a></td>
<td>レイテンシ ログと境界開示が別個の要件である理由を説明します。</td>
</tr>
</tbody>
</table>

<h2>参考資料</h2>
<ol>
<li>Chaibub Neto, E.、Pratap, A.、Perumal, T.M. 他（2019年）。機械学習ベースの診断アプリケーションに対する被験者の特性の影響を検出します。 <em>npj デジタル メディシン</em>、2、99。<a href="https://www.nature.com/articles/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Xu、M.、Yao、S.、Wei、Z.、他。 （2020年）。深層学習による EEG デコードにおけるデータセット間の変動性の問題。 <em>人間の神経科学のフロンティア</em>、14、103.<a href="https://www.frontiersin.org/articles/10.3389/fnhum.2020.00103/full" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Di, Y.、An, X.、Zhong, W.、Liu, S.、およびミン、D. (2021)。安静状態の脳波に基づく個人識別の時間堅牢性分析。 <em>人間の神経科学のフロンティア</em>、15、672946.<a href="https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.672946/full" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
<li>Tang、J.、LeBel、A.、Jain、S.、およびヒュース、A.G. (2023)。非侵襲的な脳記録からの連続言語の意味的再構築。 <em>Nature Neuroscience</em>、26、858-866。 <a href="https://www.nature.com/articles/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Willett, F. R.、Kunz, E.M.、Fan, C. 他（2023年）。高性能言語人工神経。 <em>Nature</em>、620、1031-1036。 <a href="https://www.nature.com/articles/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Johansen, A.、Bzdok, D.、Veronese, M.、他（2024年）。シナプス密度の生体内高解像度ヒト脳アトラス。 <em>Journal of Neuroscience</em>。 <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Vafaii、H.、Mandino、F.、Desrosiers-Grégoire、G.、他。 （2024年）。自発的な脳活動の多峰性測定により、皮質機能組織の共通パターンと多様なパターンの両方が明らかになります。 <em>ネイチャーコミュニケーションズ</em>。 <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Llucchetti, F.、Céléreau, E.、Steullet, P.、他(2025年)。 MR 分光イメージングを使用して人間の脳の代謝コネクトームを構築すると、大脳の生化学的組織が明らかになります。 <em>ネイチャーコミュニケーションズ</em>。 <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Li, X.、Zhu, X.-H.、Li, Y. 他(2025年)。動的重水素磁気共鳴分光イメージングを使用した、人間の脳における主要なグルコース代謝率の定量的マッピング。 <em>PNAS Nexus</em>。 <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Hirschler, L.、Runderkamp, B.A.R.、Decker, A. 他(2025年)。ヒトの MRI で測定された CSF 可動性の領域固有の要因。 <em>Nature Neuroscience</em>。 <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Chen、J. E.、Lewis、L. D.、Coursey、S. E.、他(2025年)。 EEG-PET-MRI を同時に行うことで、覚醒時とノンレム睡眠時の時間的に結合し、空間的に構造化された脳のダイナミクスを特定します。 <em>ネイチャーコミュニケーションズ</em>。 <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T.、Wang, S.、Nomi, J.S. 他(2025年)。グローバル fMRI 信号の自律生理学的結合。 <em>Nature Neuroscience</em>。 <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Epp、S.M.、Castrillon、G.、Yuan、B.、他。 (2025年)。大胆な信号変化は、人間の皮質全体の酸素代謝を妨げる可能性があります。 <em>Nature Neuroscience</em>。 <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Dagum, P.、Elbert, D.L.、Giovangrandi, L. 他（2026年）。グリンファティック系は、ヒトの脳からアミロイド ベータとタウを血漿まで除去します。 <em>ネイチャーコミュニケーションズ</em>。 <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Thomas, C.、Ye, F.Q.、Irfanoglu, M.O.、他（2014年）。拡散 MRI トラクトグラフィーから得られる脳接続の解剖学的精度には本質的に限界があります。 <em>PNAS</em>、111(46)、16574-16579。 <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4246325/" target="_blank">doi:10.1073/pnas.1405672111</a></li>
<li>Maier-Hein、K.H.、Neher、P.F.、Houde、J.-C.、他。 （2017年）。拡散トラクトグラフィーに基づいてヒトのコネクトームをマッピングするという課題。 <em>Nature Communications</em>、8、1349。<a href="https://www.nature.com/articles/s41467-017-01285-x" target="_blank">doi:10.1038/s41467-017-01285-x</a></li>
<li>Schilling, K.G.、Petit, L.、Rheault, F. 他（2020年）。白質経路がどこで始まり、どこで終わり、どこへ行かないかがわかれば、拡散 MRI トラクトグラフィーから得られる脳の接続は解剖学的に非常に正確になります。 <em>脳の構造と機能</em>、225、2387-2402。 <a href="https://pubmed.ncbi.nlm.nih.gov/32816112/" target="_blank">doi:10.1007/s00429-020-02129-z</a></li>
<li>Grisot, G.、Haber, S.N.、Hawrylycz, M.、Yendiki, A. 他（2021年）。同じ脳内の拡散 MRI と解剖学的追跡により、トラクトグラフィーの一般的な失敗モードが明らかになります。 <em>NeuroImage</em>、239、118300。<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8475636/" target="_blank">doi:10.1016/j.neuroimage.2021.118300</a></li>
<li>Penny、WD、Stephan、K.E.、Mechelli、A.、およびフリストン、K.J. (2004)。動的因果モデルの比較。 <em>NeuroImage</em>、22(3)、1157-1172。 <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811904001648" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa、M.J.、Friston、K.、およびペニー、W. (2012)。動的因果モデルの事後選択。 <em>Journal of Neuroscience Methods</em>、208(1)、66-78。 <a href="https://pubmed.ncbi.nlm.nih.gov/22561579/" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Frässle、S.、Paulus、F.M.、Krach、S.、およびジャンセン、A. (2016)。顔認識ネットワークにおける効果的な接続の信頼性をテストおよび再テストします。 <em>人間の脳のマッピング</em>、37(2)、730-744。 <a href="https://pubmed.ncbi.nlm.nih.gov/26611397/" target="_blank">doi:10.1002/hbm.23061</a></li>
<li>Frässle、S.、Manjaly、Z.M.、Do、C.T.、他（2021年）。人間のコネクトミクスのための有向接続性の全脳推定。 <em>NeuroImage</em>、225、117491.<a href="https://pubmed.ncbi.nlm.nih.gov/33115664/" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Smith、S.M.、Miller、K.L.、Salimi-Khorshidi、G.、Webster、M.、Beckmann、C.F.、Nichols、T.E.、Ramsey、J.D.、および;ウールリッチ、M.W. (2011)。 FMRI のネットワーク モデリング手法。 <em>NeuroImage</em>、54(2)、875-891。 <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">doi:10.1016/j.neuroimage.2010.08.063</a></li>
<li>バーネット、L.、＆amp;セス、AK. (2017)。サブサンプリングされた連続時間神経生理学的プロセスに対するグレンジャー因果関係の検出可能性。 <em>Journal of Neuroscience Methods</em>、275、93-121。 <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">doi:10.1016/j.jneumeth.2016.10.016</a></li>
<li>ヴィラベルデ、A.F.、チアンティス、N.、およびJ. R. バンガ (2019)。非線形生物学モデルの未知の入力、状態、パラメーターの完全な可観測性と推定。 <em>王立協会インターフェースジャーナル</em>、16(156)、20190043。<a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">doi:10.1098/rsif.2019.0043</a></li>
<li>Vink、J.J.T.、Klooster、D.C.W.、Ozdemir、R.A.、Westover、MB、Pascual-Leone、A.、および;シャフィ、M.M. (2020)。 EEG の機能的接続性は、脳の因果関係の弱い予測因子です。 <em>脳トポグラフィー</em>、33(2)、221-237。 <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">doi:10.1007/s10548-020-00757-6</a></li>
<li>Jafarian, A.、Karadag Assem, M.、Kocagoncu, E. 他（2024年）。安静状態の脳磁図の動的因果モデリングの信頼性。 <em>人間の脳のマッピング</em>、45(10)、e26782。 <a href="https://doi.org/10.1002/hbm.26782" target="_blank">doi:10.1002/hbm.26782</a></li>
<li>Novelli, L.、Barnett, L.、Seth, A. K.、およびラジ、A. (2025)。血行動態応答関数の最小位相特性、および fMRI におけるグレンジャー因果関係への影響。 <em>人間の脳のマッピング</em>、46(10)、e70285。 <a href="https://doi.org/10.1002/hbm.70285" target="_blank">doi:10.1002/hbm.70285</a></li>
<li>Yan, J.、Zhang, S.-W.、Zhang, C.、Huang, W.、Shi, J.、およびチェン、L. (2026)。生物学的ネットワーク再構築のための潜在交絡因子の下での動的因果関係。 <em>パターン分析とマシンインテリジェンスに関するIEEEトランザクション</em>。 <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">doi:10.1109/TPAMI.2026.3658839</a></li>
<li>Lynn、C.W.、Cornblath、E.J.、Papadopoulos、L.、他（2021年）。人間の脳における詳細なバランスの崩れとエントロピー生成。 <em>PNAS</em>、118(47)、e2109889118。 <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8617485/" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>デ・ラ・フエンテ、L.A.、ザンバーラン、F.、ボカッチョ、H.、他（2023年）。意識の兆候としての神経力学の時間的不可逆性。 <em>大脳皮質</em>、33(5)、1856-1865。 <a href="https://academic.oup.com/cercor/article/33/5/1856/6577164" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>石原 和也 &amp;島崎 洋 (2025)状態空間運動イジング モデルは、まばらに活動する非平衡ニューロンのダイナミクスにおけるタスク依存のエントロピー フローを明らかにします。 <em>Nature Communications</em>、16、10852。<a href="https://www.nature.com/articles/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Musall, S.、Kaufman, M.T.、Juavinett, A.L.、Gluf, S.、およびアラスカ州チャーチランド (2019)。単一試行の神経力学は、豊富に変化した動きによって支配されます。 <em>Nature Neuroscience</em>、22、1677-1686。 <a href="https://www.nature.com/articles/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>サリーム、A.B.、アヤズ、A.、ジェフリー、K.J.、ハリス、K.D.、およびカランディーニ、M. (2013)。マウスの視覚野における視覚運動と移動運動の統合。 <em>Nature Neuroscience</em>、16、1864-1869。 <a href="https://www.nature.com/articles/nn.3567" target="_blank">doi:10.1038/nn.3567</a></li>
<li>Flesher、S.N.、Downey、J.E.、Weiss、J.M.、他（2021年）。触覚を呼び起こすブレイン コンピューター インターフェイスにより、ロボット アームの制御が向上します。 <em>Science</em>、372(6544)、831-836。 <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8715714/" target="_blank">doi:10.1126/science.abd0380</a></li>
</ol>
