# Wiki: マルチモーダル統合の基本

> 共有クロック、共有ファクター、数量ブリッジは異なる成果です
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-04-03 / Role: 技術/自然科学のみ (フュージョン カードの一貫性のために 2026 年 4 月 3 日に書き直されました)

## このページの役割
このページでは、EEG、MEG、fMRI、PET、fNIRS、侵襲的記録、および MRI を組み合わせた場合に、現在の一次文献が実際に何をサポートしているかを整理します。その目的は、デフォルトで融合を称賛することではなく、同期、ジオメトリ、生理学、モデル負荷を分離し、バンドルの堅牢性を監査可能な部分に分割することです。

## 正確性に関する注記
このページは、モダリティを追加すると状態完全な読み出しが可能になると主張するものではありません。どの保険金請求の上限が上がり、どれが上がらないのか、またその理由について説明します。

## 公開ページへ戻る
- [脳波101](https://mind-upload.com/eeg_101.html)
- [検証](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki ページ
- [Wiki: 脳波の基礎](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - 脳波の上限だけを知りたい場合はここに戻ってください。
- [Wiki: 測定スタックごとの可観測性とクレームの上限](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling) - 次にこれをスタックごとの天井テーブルに使用します。
- [Wiki: 人間のプロキシ構成とルートの成熟度](https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition) - これは、マルチモーダル バンドルに生きている人間のプロキシ クラスも混在する場合に使用します。
- [Wiki: イベント同期と測定ログ](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - 共有クロック、遅延、ジッター、ドリフトが導入されます。
- [Wiki: 不確実性、自信、棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - 融合後も不確実性が残る理由を説明します。
- [Wiki: 観察から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 直接観察可能なものを、推論された潜在変数から分離します。
- [Wiki: ベースライン、事前登録、およびモデル カード](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - これは、マルチモーダル結果に Fusion Card ワークフローが必要な場合に使用します。

## 現在わかっていること
- モダリティを組み合わせることで、タイミング、空間的位置特定、キャリブレーション、またはバンドルレベルの予測に関する特定の質問を強化できます。
- ゲインは、同期パス、被験者固有の形状、フィールド/ノイズ制御、生理学側の解釈、およびモデルの負担によって異なります。
- 同時取得、共有コンポーネント、および外部で校正された 1 つの生物学的変数は、異なる請求レベルです。
- 同一セッションのマルチモーダル研究では、イベントロック電気生理学、血行力学ウィンドウ、スキャンウィンドウまたは運動代謝量を依然として混合できるため、共有クロックは 1 つの時間的オブジェクトを定義しません。
- 共有の低周波/グローバル因子は、神経、自律神経、および血管の寄与を混合する可能性があるため、共通の構造は自動的なターゲット変数の特異性ではありません。
- 結合された軌道は、比較される生物学的軸に名前が付けられ、外部に接地されない限り、まだ量的な橋にはなりません。
- マルチモーダルゲインは、どのサンプルが完全なバンドルを保持したか、欠落モダリティがどのように処理されたか、ハードレジームで不一致が増大するかどうかに依存する可能性があります。
- EEG + fMRI および EEG + fNIRS の場合、位置合わせだけでは不十分です。血行動態移入と表面/全身汚染は引き続き個別の監査となります。
- OPM-MEG は、固定 SQUID システムよりも多くの動きに耐えることができますが、それは開示されたシールド、アクティブフィールド制御、校正、および解剖学的仮定の下でのみです。
- 侵襲的記録は依然として、空間バイアスとコホートバイアスが強い貴重な外部キャリブレーション ルートです。

## まだわかっていないこと
- WBE 関連の各段階にどのマルチモーダル バンドルが最適であるかはまだ決まっていません。
- より豊富なマルチモーダルスタックであっても、シナプス、グリア、転写、神経調節、または維持状態の観察可能性の十分性は依然として確立されていません。
- 人間のマルチモーダルスタック全体で共有分解と固有分解をベンチマークする方法は未解決のままです。
- 同時マルチモーダル研究全体で有効ウィンドウの互換性をベンチマークする方法は未解決のままです。
- 電気生理学的、血行力学、代謝、自律神経のスタック全体にわたってどの量のブリッジを外部から校正できるかは未解決のままです。
- 完全なケースの可用性、センターミックス、またはサブグループの不一致が異なる場合に、マルチモーダルバンドルを公平に比較​​する方法は未解決のままです。

---

<h2>結論</h2>
<p>
マルチモーダルな統合により、請求の上限がいくらか引き上げられる可能性がありますが、逆の問題、生理学上の橋渡し、または堅牢性の負担が解消されるわけではありません。このサイトでは、マルチモーダル論文は、<strong> 同期</strong>、<strong> ジオメトリ</strong>、<strong> 時間核関係</strong>、<strong> 血行力学または代謝解釈</strong>、<strong> 共有対特異的構造</strong>、<strong> 量ブリッジ</strong>、および<strong>バンドルの堅牢性</strong> の後にのみ読まれます。別途監査されます。
</p>

<strong>このページがサイトにどのように適合するか</strong>
<p>
こちらは<a href="https://mind-upload.com/verification.html#fusion-card">Verification:Fusion Card</a>の背景ページです。検証により動作ルールが得られます。このページでは、なぜルールが厳格でなければならないのか、現在どのルートがより高い測定値を獲得しているのか、そして請求の上限がどこで止まるのかについて説明します。
</p>

<strong>このページを書き直す必要があった理由</strong>
<p>
古いバージョンは正しい方向を示していましたが、依然として 3 つのショートカットが簡単に作成できませんでした。まず、<strong>same-session</strong> は、依然として 1 つの一致する時間オブジェクトと誤認される可能性があります。第二に、<strong> 共有因子 </strong> は、依然として標的生物学的変数または解決された <strong> 量ブリッジ </strong> と間違われる可能性があります。第三に、<strong> マルチモーダル ゲイン</strong> は依然として、堅牢で可用性を問わないバンドルであると誤解される可能性があります。一次文献では、これらのジャンプはいずれもサポートされていません。現在の書き換えでは、これらの停止ルールが明示的になり、また 1 つの過剰修正が修正されています。つまり、生理学に関連したグローバル要因は、自動的には単なる「アーチファクト」ではなくなります。それは実際の結合プロセスである可能性がありますが、依然として関心のあるニューラルターゲット変数と等しくないことがあります。
</p>

<strong>Sスコープ</strong>
<p>
このページは技術および自然科学の側面のみに留まります。アイデンティティ、意識、法律、倫理を解決するために多様な言語を使用しません。より狭い質問は次のとおりです: <strong> マルチモーダル ペーパーで実際に追加されたものは何ですか? 条件付きで残っているものは何ですか? </strong>
</p>

<h2>最初に修正するための 11 の監査ゲート</h2>
<table>
<thead>
<tr>
<th>ゲート</th>
<th>ゲートを通過できるもの</th>
<th>ゲートが存在しない場合でもこのサイトが主張を停止するもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同期ゲート</strong></td>
<td>共有クロック、遅延、ジッター、ドリフトは、時間内でストリームを比較するのに十分なほど十分に開示されています。</td>
<td>共有タイムスタンプだけでは、時間的に整合した潜在状態の証拠にはなりません。</td>
</tr>
<tr>
<td><strong>ジオメトリゲート</strong></td>
<td>個別の MRI、測定された電極またはセンサーの位置、および宣言されたフォワード モデルにより、空間解釈が強化されます。</td>
<td>解剖学を追加したからといって結果が正確な解剖学的真実として読み取れるわけではありません。</td>
</tr>
<tr>
<td><strong>ノイズ/フィールドゲート</strong></td>
<td>MR アーティファクト、モーション アーティファクト、背景磁場、クロストーク、クロストーク ルートは透過的に処理されます。</td>
<td>A のクリーンな融合出力は、直接的なニューラル グラウンド トゥルースとして扱われません。</td>
</tr>
<tr>
<td><strong>血行動態トランスファーゲート</strong></td>
<td>fMRI または fNIRS の場合、血管状態、CVR、および表面/全身負荷は校正されるか、または棄権限界として残されます。</td>
<td>BOLD、HbO、または HbR の振幅の違いは、デフォルトではクリーンな神経の違いとして読み取られません。</td>
</tr>
<tr>
<td><strong>外部検証ゲート</strong></td>
<td>エラーは、侵襲的記録、電気刺激、術後の結果、ファントム、またはその他の外部参照に対して監査できます。</td>
<td>Model 出力だけでは、検証されたローカリゼーションまたは融合された真実として読み取られません。</td>
</tr>
<tr>
<td><strong>フュージョン カード ゲート</strong></td>
<td>取得関係、ラグ監査、共同登録範囲、融合モデル、単峰性ベースラインまたは以前のみのベースラインに対するゲインが表示されます。</td>
<td>「同時」、「マルチモーダル」、または「アトラス情報」は、自己検証型フュージョンとして扱われません。</td>
</tr>
<tr>
<td><strong>有効ウィンドウ/テンポラルカーネルゲート</strong></td>
<td>各スタックの時間オブジェクトには、イベントロック電気生理学、血行動態応答ウィンドウ、スキャンウィンドウ平均、または分単位の運動ルートなどの名前が付けられます。</td>
<td>カーネルが依然として異なる場合、同一セッションの取得は 1 つの同期状態サンプルに昇格されません。</td>
</tr>
<tr>
<td><strong>共有コンポーネント ゲートと固有コンポーネント ゲート</strong></td>
<td>この論文では、その効果が共有成分、モダリティ固有の残差、または生理学に関連した全体的要因に存在するかどうかが述べられています。</td>
<td>A 共通因子は、デフォルトではターゲット生物学的変数に昇格されません。</td>
</tr>
<tr>
<td><strong>数量ブリッジ/生理学的接地ゲート</strong></td>
<td>この論文は、モダリティを比較する生物学的軸に名前を付け、それらの量がなぜ比例するのかを示しています。</td>
<td>クロスモーダル共分散は、ブリッジが宣言されていないと、1 つの解決されたニューラル量に昇格されません。</td>
</tr>
<tr>
<td><strong>バンドル堅牢性ゲート</strong></td>
<td>この論文は、完全な症例スライス、欠落モダリティの処理、センターまたはスキャナー間の転送、およびハードサブグループでの不一致を開示しています。</td>
<td>「より多くのモダリティでパフォーマンスが向上」は、堅牢で取得が完了したバンドルの証拠としては読み取れません。</td>
</tr>
<tr>
<td><strong>州カバレッジゲート</strong></td>
<td>この論文には、どの州の家族が実際に拘束され、どの州の家族が観察されていないのかが記載されています。</td>
<td>マルチモーダル統合は、WBE 関連の隠し変数の完全な状態に昇格されません。</td>
</tr>
</tbody>
</table>

<strong>このサイトの最小融合パッケージ</strong>
<p>
マルチモーダルまたはアトラス優先ルートの場合、このページは <a href="https://mind-upload.com/verification.html#fusion-card">Verification と同じ開示バンドルに従います: Fusion Card</a>: <strong> 取得関係 </strong>、<strong> クロック / ラグ監査 </strong>、<strong> 有効ウィンドウ / 時間的カーネル関係 </strong>、<strong> ジオメトリ / 共同登録スコープ</strong>、<strong> 融合オブジェクトおよびモデル負荷</strong>、 <strong> 共有コンポーネントと固有コンポーネントの開示</strong>、<strong>数量ブリッジ/生理学根拠</strong>、<strong>単峰性/以前のみのベースラインを超える証拠の増加</strong>、<strong>可用性/完全症例スライス</strong>、<strong>欠落モダリティポリシー</strong>、<strong>クロスセンター/クロススキャナー転送窓</strong>、および<strong>外部校正プラス棄権境界</strong>。これらのフィールドが欠落している場合、結果は個別にサポートされている最も強力なスタックの上限に留まります。
</p>

<strong> 1 つのフレーズにまとめられることが多い 3 つのオブジェクト</strong>
<p>
このサイトでは、<strong> 同期ストリーム </strong>、<strong>a 共有クロスモーダル因子 </strong>、および <strong>one 外部接地生物量 </strong> の 3 つの異なる成果です。一つ目は取得物件です。 2つ目は統計結果です。 3 つ目は生物学的解釈ですが、依然として校正、ブリッジロジック、棄権境界線が必要です。
</p>

<h2>各主要ルートについて現在の一次文献がサポートしているもの</h2>
<table>
<thead>
<tr>
<th>ルート</th>
<th>現在の一次文献が実際にサポートしているもの</th>
<th>未解決または条件付きのままのもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG+個別MRI/フォワードモデル</strong></td>
<td>被験者固有の解剖学的構造、測定された電極位置、および現実的な頭部モデルにより、ソースイメージング条件が強化され、頭蓋内刺激に対して外部からチェックできます。</td>
<td>深さバイアス、導電率の不確実性、および非固有性が残ります。これは改良されたジオメトリであり、直接的なローカル回路の真実ではありません。</td>
</tr>
<tr>
<td><strong>EEG + MEG</strong></td>
<td>相補的な感度プロファイルは、校正された現実的な導体モデルが使用される場合に、ソースの再構築を向上させることができます。</td>
<td>ゲインは、モダリティ数だけではなく、相互位置合わせと伝導率モデリングに依存します。</td>
</tr>
<tr>
<td><strong>EEG + fMRI</strong></td>
<td>共同取得により、再現可能なクロススタック解析と時間情報と空間情報のモデル条件付き融合をサポートできます。</td>
<td>時間的カーネルの不一致、MR アーティファクト負荷、および血管状態 / CVR 解釈は依然として別個の上限のままです。</td>
</tr>
<tr>
<td><strong>EEG + fNIRS</strong></td>
<td>ポータブル血行力学的電気生理学的ペアリングは、表面信号と全身信号を測定して明示的に回帰する場合に、限定されたタスクの読み取りを強化できます。</td>
<td>短期間の分離または同等の表面的診断がなければ、HbO/HbR の違いは依然として脳外および自律神経への負担をもたらします。</td>
</tr>
<tr>
<td><strong>EEG + PET + MRI</strong></td>
<td>トリモーダル取得により、1 回の実験セッション内で調整された電気生理学的、血行力学的、代謝の進行を明らかにできます。</td>
<td>PET の定量化はモデルを保持したままであり、時間カーネルは依然として異なり、共有された軌跡自体は 1 つの検証された潜在状態を確立しません。</td>
</tr>
<tr>
<td><strong>EEG + 侵襲的記録</strong></td>
<td>頭皮記録と侵襲的記録の同時記録により、限られた空間領域と選択されたソース領域に対して強力な外部キャリブレーションを提供します。</td>
<td>カバレッジはまばらで、臨床的に偏っていて、全脳のグラウンドトゥルースではありません。</td>
</tr>
<tr>
<td><strong>OPM-MEG</strong></td>
<td>ウェアラブル システムは、フィールド制御が慎重に設計されている場合、MEG を立位、歩行、および対話型のパラダイムに拡張できます。</td>
<td>シールド クラス、アクティブ ヌリング、センサー キャリブレーション、解剖学的ルート、およびクロストークが依然として請求の上限を定義します。</td>
</tr>
</tbody>
</table>

<h2>各ルートが実際に追加するもの</h2>

<h3>1。 EEG + MRI は、グラウンド トゥルースではなく、監査済みのジオメトリを追加します</h3>
<p>
個々の MRI、測定された電極位置、および現実的なフォワード モデルにより、EEG ソース イメージング条件が大幅に改善されます。 <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023) </a> はその後、ヒト患者における直接刺激に基づく検証を追加しました。それは本当に前進です。しかし、安全な解釈はまだ狭いです。主題固有のジオメトリが追加された後でも、ソースの深さ、導電率の選択、および逆ファミリの選択が引き続き重要です。したがって、このサイトでは、EEG + MRI は、直接的な局所的な神経の真実や解決された一意性ではなく、<strong> より優れた幾何学的可聴性 </strong> として読み取られます。
</p>

<h3>2。 EEG + MEG は物理モデルが改善された場合にのみ感度プロファイルを補完します</h3>
<p>
EEG と MEG は、信号源の方向と体積伝導に対して異なる反応を示すため、組み合わせる価値があります。しかし、その利益は抽象的な二峰性から得られるものではありません。 <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">Aydin et al. (2014)</a> は、改善が <strong> で校正された現実的な体積導体モデル </strong> に依存することを示しました。したがって、このサイトでは、EEG + MEG は、一般的な「より多くのセンサーがソース問題を解決した」結果としてではなく、<strong> 伝導率モデル、相互登録、および逆仮定 </strong> が開示された場合にのみ上限が上昇するルートとして解釈されます。
</p>

<h3>3。 EEG + fMRI はスタック間の相補性を追加しますが、神経のみの読み出しではありません</h3>
<p>
同時 EEG-fMRI は、1 つの収集プロトコルの下で高速電気生理学を低速の血行動態組織化に関連付けることができるため、依然として科学的に有用です。 <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">ホルヘら(2015a)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2015.07.020" target="_blank">Jorge et al. (2015b)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al。 (2021)</a> は、このルートが実行可能であり、再現可能なクロススタック分析をサポートできることを示しました。しかし、天井は依然として 2 つの異なる場所で早期に停止します。
</p>
<p>
最初の制限は一時的なものです。 <a href="https://doi.org/10.1155/2016/4182483" target="_blank">Nguyen 他(2016) </a> は、時空間的に制約された EEG-fMRI ソース イメージングであっても、<strong>not</strong> が EEG と血行力学的反応の間の時間的不一致を消去しないことを明らかにしました。 2 番目の制限は解釈的なものです。 <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">マーフィーら(2011)</a>、<a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a>、<a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> は、血管状態と CVR の違いが太字の読み取りにとって依然として重要である理由を示しています。 (2025)</a> は、タスクの大胆な変更が皮質の各部分にわたる酸素代謝の変化にさえ対抗できることを示しています。したがって、このサイトでは、EEG + fMRI は <strong> 共有取得と宣言されたクロスカーネル関係 </strong> のままであり、自動的に同じ状態または同じ量の証拠が得られるわけではありません。
</p>

<strong>同じ停止ルールがEEG + fNIRS</strong>に適用されます
<p>
携帯型血行力学ルートは科学的には有用ですが、生理学的な負担を免れることはできません。 <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yucel et al. (2015) </a> は、自律神経反応がタスク間で異なる場合に、短時間分離回帰によって局在化と統計的有意性が向上することを示しました。 (2025) </a> は、モーター需要が最小限の作業記憶タスクであっても、短チャネル回帰により感度と妥当性が向上することを示しました。したがって、このサイトでは、<strong>short-separation または同等の表面的/全身的開示 </strong> を伴わない EEG + fNIRS は、クリーンな神経差測定値として扱われません。
</p>

<h3>4。 EEG + PET + MRI は、統合されたグラウンド トゥルースではなく、調整されたマルチタイムスケールの生理機能を追加します</h3>
<p>
トリモーダル EEG-PET-MRI は、このページで最も強化が必要なルートです。 <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">チェンら。 (2025) </a> は、EEG-PET-MRI を同時に行うことで、覚醒時とノンレム睡眠にわたる明確な空間ネットワーク構造とともに、緊密に結合した全体的な血行動態と代謝の進行を明らかにできることを示しました。 1 つのプロトコルで同じセッション内で電気生理学的覚醒、血行力学的変動、代謝低下を比較できるようになったので、これは大きな進歩です。
</p>
<p>
しかし、安全な読み取りは依然として融合状態の真実のかなり手前で止まっています。 PET 定量化は依然としてモデルに基づいています。血行力学的側面には依然として血管の解釈が含まれています。時間オブジェクトはまだ分割されています: <a href="https://doi.org/10.1016/j.neuroimage.2021.118131" target="_blank">Ripp et al。 (2021) </a> は、FDG-PET/fMRI の同時作業記憶データで、PET は依然としてイベントスケールのタイミングではなく、<strong> スキャンウィンドウ平均 </strong> を通じて読み取られる必要があることを示しました。したがって、このサイトでは、第 2 スケールの電気生理学、血行動態応答ウィンドウ、および PET カーネルがどのように比較されているかを論文が明示的に示していない限り、三峰性同期は <strong> 調整されたマルチタイムスケールの証拠 </strong> として解釈されます。
</p>

<strong>A 共有グローバル要素は自動的に神経ターゲットにはなりませんが、自動的に単なる迷惑になるわけでもありません</strong>
<p>
このページのより深い訂正は、共有される低周波構造は単純に賞賛したり否定したりするのではなく、<strong>typed</strong> でなければならないということです。 <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii ら(2024) </a> は、多峰性自発脳測定には <strong>common</strong> と <strong>divergent</strong> 組織の両方が含まれることを示しました。 <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">ボルト 他(2025) </a> は、主要なグローバル fMRI モードが自律神経生理学および脳波と強く結びついていることを示しました。 (2019) </a> は、EEG でマークされた覚醒イベント中の fMRI 信号変化に交感神経活動が寄与していることを示しました。正しい読み方は、「だから意味がない」でも、「だから対象の神経変数である」でもありません。正しい解釈としては、報告される共通因子は、<strong> 共有神経候補 </strong>、<strong> 生理学関連共通ドライバー </strong>、<strong> モダリティ固有の残差 </strong>、または <strong> 混合 / 未解決 </strong> としてラベル付けされる必要があります。
</p>

<p>
結合された軌道が <strong> 数量ブリッジ </strong> になる前に、もう 1 つの停止ルールが必要です。 <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp ら(2025) </a> は、重要なタスクの BOLD の変更が、多くの皮質ボクセルにわたる酸素代謝の変化に対抗できることを示しました。したがって、EEG、fMRI、PET にわたる強い結合があっても、それ自体では 3 つのスタックすべてが 1 つの解決された生物学的量を読み取ることを示すわけではありません。このサイトでは、マルチモーダル論文は、<strong>共有軌道</strong>、<strong>生理学にリンクされた共通ドライバー</strong>、または名前付き生物学的軸</strong>上の明示的な<strong>量ブリッジのみを確立したかどうかを記載する必要があります。
</p>

<h3>5。デフォルトでバンドルを堅牢にすることなく、より多くのモダリティが役立つ可能性があります</h3>
<p>
次の補正は幾何学的なものではなく操作的なものです。マルチモーダル論文は予測や不確実性を改善することができますが、モダリティの欠落、サイトの移動、またはハードサブグループ内の不一致に対して脆弱なままのバンドルを残します。 <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024) </a> は、急性脳損傷において、モダリティを追加することで予後の不確実性が減少し、精度が向上する可能性があることを示しました。これは真のバンドルレベルの利益です。ただし、そのゲインは堅牢なマルチモーダル バンドルと同じではありません。
</p>
<p>
<a href="https://doi.org/10.1093/brain/awac335" target="_blank">アミリら(2023) </a> は、同一サンプルの直接的なマルチモーダル比較が、制限された <strong> 完全機能サブセット </strong> に依存していることを示しました。そのため、比較自体は、誰が実際にフルバンドルを実行したかに依存します。 <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">マナソワら(2026) </a> は、その後、マルチモーダル分類器が欠損モダリティの処理とセンター間検査を組み合わせられる一方で、<strong> 意識レベルが低い </strong> または <strong> </strong> 患者において高い <strong> ペアごとの不一致 </strong> を示していることを示しました。したがって、このサイトでは、論文がさらに証明しない限り、「マルチモーダルゲイン」は<strong>、宣言された可用性、転送、および不一致体制の下でのバンドルパフォーマンス証拠</strong>で止まります。
</p>

<h3>6。 EEG + 侵襲的記録は強力なキャリブレーション ルートですが、限られた範囲のみに適用されます</h3>
<p>
頭皮記録と侵襲的記録の同時記録は、ヒトのマルチモーダル研究に利用できる最も強力な外部キャリブレーション ルートの 1 つです。 <a href="https://doi.org/10.1016/j.neuroimage.2006.02.027" target="_blank">Zhang ら。 (2006) </a> は頭皮 EEG と ECoG を同時に使用して、現実的な FEM と同時登録された MRI/CT が主要な皮質電位パターンを保存できることを示しました。 (2019) </a> は、皮質下の電気生理学的活動が高密度 EEG ソース イメージングによって条件付きで検出可能であることを示しました。ただし、これらは <strong> のカバレッジに制限された </strong> の利益です。このサイトでは、同時侵襲ルートは、全脳のゴールドスタンダードとしてではなく、記録された領域およびソース領域</strong>の校正/検証ルートとして扱われます。
</p>

<h3>7。 OPM-MEG は移動許容範囲を拡張しますが、フィールド制御とソースモデルの監査がなければ拡張できません</h3>
<p>
ウェアラブル OPM-MEG は、センサーが頭とともに動くため、固定式 SQUID ヘルメットではサポートされないパラダイムをサポートするため、真の進歩です。 <a href="https://doi.org/10.1038/nature26147" target="_blank">Boto et al. (2018)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">Sセイモア 他(2021)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">ホームズら。 (2023a)</a>、<a href="https://doi.org/10.3390/s23125454" target="_blank">Holmes et al. (2023b)</a> は、ますます自然主義的な使用例を示しています。しかし、共通の教訓は「動きが解決した」ということではありません。 </strong>の磁気環境が十分に厳密に制御されている場合、<strong>の動きが測定可能になるということです。
</p>
<p>
エンジニアリングの上限は依然としてフィールド環境とソース モデリングを貫いています。 <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">メラーら(2022)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">Rea 他(2021)</a>、<a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">Holmes et al. (2025)</a> は、バックグラウンドフィールド制御、アクティブ補償、およびシールドクラスが依然として重要である理由を示しています。 <a href="https://doi.org/10.3390/s22083059" target="_blank">Iivanainen et al. (2022)</a>、<a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">Rhodes et al. (2025)</a>、および<a href="https://doi.org/10.1063/5.0273491" target="_blank">Wuら。 (2025)</a> は、キャリブレーション、解剖学的ルート、クロストークが依然としてライブの負担である理由を示しています。したがって、このサイトでは、ウェアラブル OPM-MEG は、制約のない現実世界の脳の読み出しではなく、開示されたフィールド制御およびソースモデルの仮定の下での <strong> 動き耐性マクロ電気生理学のままである </strong> です。
</p>

<strong>「ウェアラブル」をシールドフリー、キャリブレーションフリー、または状態完了と読み取らないでください</strong>
<p>
OPM-MEG が日常の行動にはるかに近いものであるとしても、公的主張は依然として、<strong> シールド クラス </strong>、<strong> フィールド ヌリング / 干渉抑制メソッド </strong>、<strong> 動き追跡ルート </strong>、<strong> センサー校正パス </strong>、<strong> 解剖ルート </strong>、および <strong> 棄権が始まる場所 </strong> と名付けなければなりません。これらが欠落している場合、このサイトでは結果を実現可能性または概念実証の上限に保ちます。
</p>

<h2>このサイトで採用されているルールの閲覧</h2>

<h4>ルール</h4>
<ul>
<li><strong>multimodal:</strong> 「複数のモダリティが追加された」ではなく、「どの監査ゲートを通過したか」と読み替えてください。
<li><strong>same-session / atlas-informed:</strong> <a href="https://mind-upload.com/verification.html#fusion-card">Fusion Card</a> が取得関係、ラグ監査、時間カーネル関係、共同登録スコープ、共有対固有ロジック、単峰性 / 事前のみのベースライン、可用性スライス、および外部キャリブレーションを開示しない限り、これを 1 つの検証済みの生物学的状態変数として読み取らないでください。</li>
<li><strong>共有因子:</strong> 自動ターゲット特異性として読み取らないでください。共有神経候補、生理学に関連した共通ドライバー、モダリティ固有の残差、または未解決としてラベル付けします。</li>
<li><strong>量ブリッジ:</strong> 共分散のみから推測しないでください。生物学的軸と生理学基礎ルールに明示的に名前を付けます。</li>
<li><strong>マルチモーダルゲイン:</strong> 欠落モダリティの処理、転送、およびハードサブグループの不一致も開示されていない限り、「より多くのモダリティでパフォーマンスが向上」をロバスト性と解釈しないでください。</li>
<li><strong>EEG + fMRI / fNIRS:</strong> 血行力学振幅は、血管状態 / CVR または表面信号負荷が監査されるまで、伝達制限量のままです。</li>
<li><strong>EEG + 侵襲的記録:</strong> 全脳の真実ではなく、範囲を限定した校正または検証として扱います。</li>
<li><strong>OPM-MEG:</strong> ウェアラブルおよびモーショントレラントは、シールド、フィールド制御、校正、解剖学、またはクロストーク監査を放棄しません。</li>
<li><strong>状態カバレッジ:</strong> シナプス、グリア、転写、または維持サポート変数が観察されないままである場合、それらは融合後も未観察としてマークされたままになります。</li>
</ul>

<h2>参考資料</h2>
<ol>
<li>Pernet, C.R.、Appelhoff, S.、Gorgolewski, K.J. 他（2019年）。 EEG-BIDS、脳波検査用の脳画像データ構造の拡張。 <em>S科学的データ</em>、6、103。<a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C.、Garrido, M.I.、Gramfort, A. 他（2020年）。再現可能なEEGおよびMEG研究のためのOHBM COBIDAS MEEG委員会からの問題と推奨事項。 <em>Nature Neuroscience</em>、23、1473-1483。 <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Kothe, C.、Shirazi, S. Y.、Stenner, T.、Medine, D.、Boulay, C.、Grivich, M. I.、Artoni, F.、Mullen, T.、Delorme, A.、およびMakeig、S. (2025)。同期されたマルチモーダル記録のためのラボ ストリーミング レイヤー。 <em>画像神経科学</em>、3、IMAG.a.136。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H.、Jafarian, A.、Zeidman, P.、Litvak, V.、Razi, A.、Garrido, M.、Friston, K.、およびドニゾー、J. (2020)。 EEG および fMRI 用のベイジアン フュージョンおよびマルチモーダル DCM。 <em>NeuroImage</em>、211、116595。<a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>グエン、T.、ポッター、T.、グエン、T.、カルモニク、C.、グロスマン、R.、&amp;;張 Y. (2016)。時空間特異的 fMRI によって導かれた EEG ソース イメージング: 動的な認知プロセスの理解に向けて。 <em>神経可塑性</em>、2016、4182483。<a href="https://doi.org/10.1155/2016/4182483" target="_blank">doi:10.1155/2016/4182483</a></li>
<li>Ripp, I.、Wallenwein、L.A.、Wu, Q.、Emch, M.、Koch, K.、Cumming, P.、&amp;;ヤクシェフ、I. (2021)。作業記憶タスクによる神経活性化: PET/fMRI 同時研究。 <em>NeuroImage</em>、237、118131.<a href="https://doi.org/10.1016/j.neuroimage.2021.118131" target="_blank">doi:10.1016/j.neuroimage.2021.118131</a></li>
<li>Vafaii、H.、マンディーノ、F.、デロジエ・グレゴワール、G.、オコナー、D.、マルチェビッチ、M.、シェン、X.、Ge、X.、ハーマン、P.、ハイダー、F.、パパデメトリス、X.、チャクラヴァルティ、M.、クレア、M.C.、コンスタブル、R.T.、レイク、E.M. R.、＆amp;ペソア、L. (2024)。自発的な脳活動の多峰性測定により、皮質機能組織の共通パターンと多様なパターンの両方が明らかになります。 <em>Nature Communications</em>、15、229.<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E.、Lewis, L. D.、Courey, S. E.、Catana, C.、Polimeni, J. R.、Fan, J.、Droppa, K. S.、Patel, R.、Wey, H.-Y.、Chang, C.、Manoach, D. S.、Price, J. C.、Sander, C. Y.、および;ローゼン、B.R. (2025)。 EEG-PET-MRI を同時に行うことで、覚醒時とノンレム睡眠時の時間的に結合し、空間的に構造化された脳のダイナミクスを特定します。 <em>Nature Communications</em>、16、8887。<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T.S.、van den Brink, R.L.、Song, C. 他(2025年)。グローバル fMRI 信号の自律生理学的結合。 <em>Nature Neuroscience</em>、28、1266-1278。 <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Özbay, P.S.、Chang, C.、Picchioni, D. 他（2019年）。交感神経活動は fMRI 信号に寄与します。 <em>コミュニケーション生物学</em>、2、421。<a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">doi:10.1038/s42003-019-0659-0</a></li>
<li>Rohaut, B.、Calligaris, C.、Hermann, B. 他。 （2024年）。マルチモーダル評価は、臨床的に反応性のない脳損傷のある救命救急患者の神経予後成績を改善します。 <em>Nature Medicine</em>、30、2349-2355。 <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Amiri、M.、Andelic、N.、Westhall、E. 他（2023年）。集中治療室における残留意識のマルチモーダル予測: CONNECT-ME 研究。 <em>ブレイン</em>、146(1)、50-69。 <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/ブレイン/awac335</a></li>
<li>Manasova, D.、Hermann, B.、Calligaris, C. 他（2026年）。意識障害における診断および予後マーカーの多角的多施設研究。 <em>ブレイン</em>。 <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/脳/awaf412</a></li>
<li>Jorge, J.、Grouiller, F.、Ipek, O. 他（2015年）。超高磁場での同時 EEG-fMRI: アーチファクトの防止と安全性評価。 <em>NeuroImage</em>、105、132-144。 <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">doi:10.1016/j.neuroimage.2014.10.055</a></li>
<li>Jorge, J.、Grouiller, F.、Gruetter, R. 他（2015年）。 7 T での高品質同時 EEG-fMRI に向けて: 頭部の動きによる EEG アーチファクトの検出と低減。 <em>NeuroImage</em>、120、143-153。 <a href="https://doi.org/10.1016/j.neuroimage.2015.07.020" target="_blank">doi:10.1016/j.neuroimage.2015.07.020</a></li>
<li>Wirsich, J.、Jorge, J.、Iannotti, G.R.、他（2021年）。 EEG と fMRI コネクトーム間の関係は、1.5T から 7T までの同時 EEG-fMRI 研究全体で再現可能です。 <em>NeuroImage</em>、231、117864.<a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">doi:10.1016/j.neuroimage.2021.117864</a></li>
<li>マーフィー、K.、ハリス、A.D.、およびワイズ、R.G. (2011)。息止めによる血管反応性の違いを確実に測定: 刺激誘発状態と安静状態の BOLD fMRI データを正規化します。 <em>NeuroImage</em>、54(1)、369-379。 <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>ウィリアムズ、R. J.、シュペヒト、J. L.、マゼロル、E. L.、レベル、R. M.、マクドナルド、M. E.、およびパイク、GB (2023)。 BOLD fMRI タスクの反応と大脳皮質全体の脳血管反応性の対応。 <em>生理学におけるフロンティア</em>、14、1167148.<a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Wu、S.、タイラー、L.K.、ヘンソン、R.N.A.、ロウ、J.B.、Cam-CAN、およびツベタノフ、K.A. (2023)。脳血流は、成人の生涯にわたる複数の需要ネットワークの活動と流動性知能を予測します。 <em>老化の神経生物学</em>、121、1-14。 <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">doi:10.1016/j.neurobiolaging.2022.09.006</a></li>
<li>Yucel, M. A. Y.、Selb, J.、Aasted, C. M. A.、Petkov, M. P.、Becerra, L.、Borsook, D.、および;ボアス、D.A. (2015)。短い分離回帰により統計的有意性が向上し、異なる自律神経反応を伴うタスクについて近赤外分光法によって得られる血行力学的反応の局所性が向上します。 <em>ニューロフォトニクス</em>、2(3)、035005。<a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>An、J.、Goyal、P.、Luft、A.R.、およびシェーンハマー、J.G. (2025)。機能的近赤外分光法短チャネル回帰は、作業記憶負荷の皮質活性化推定を改善します。 <em>ニューロフォトニクス</em>、12(3)、035009。<a href="https://doi.org/10.1117/1.NPh.12.3.035009" target="_blank">doi:10.1117/1.NPh.12.3.035009</a></li>
<li>Epp、S.M.、Castrillon、G.、Yuan、B.、Andrews-Hanna、J.、Preibisch、C.、およびリードル、V. (2025)。大胆な信号変化は、人間の皮質全体の酸素代謝を妨げる可能性があります。 <em>Nature Neuroscience</em>。 <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Aydin, U.、Vorwerk, J.、Kupper, P.、他（2014年）。 EEG と MEG を組み合わせて、校正された現実的な体積導体モデルを使用しててんかん活動を再構築します。 <em>PLoS ONE</em>、9(3)、e93154。 <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">doi:10.1371/journal.pone.0093154</a></li>
<li>Zhang, Y.、Ding, L.、van Drongelen, W. 他（2006年）。有限要素法による頭蓋外および頭蓋内の同時電気記録からの皮質電位イメージング研究。 <em>NeuroImage</em>、31(4)、1517-1528。 <a href="https://doi.org/10.1016/j.neuroimage.2006.02.027" target="_blank">doi:10.1016/j.neuroimage.2006.02.027</a></li>
<li>Seeber, M.、Cantonas, L.-M.、Hoevels, M.、他（2019年）。皮質下の電気生理学的活動は、高密度EEGソースイメージングで検出可能です。 <em>Nature Communications</em>、10、753.<a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse、K.、Achakulvisut、T.、Wu、J.Y.、他。 （2023年）。人間の患者における頭蓋内電気刺激によるEEGソースイメージングの直接検証。 <em>ブレインコミュニケーションズ</em>、5(2)、fcad023。 <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/ブレインコム/fcad023</a></li>
<li>Boto, E.、Holmes, N.、Leggett, J. 他（2018年）。ウェアラブル システムを使用して、脳磁図を現実世界のアプリケーションに移行します。 <em>ネイチャー</em>、555、657-661。 <a href="https://doi.org/10.1038/nature26147" target="_blank">ドイ:10.1038/nature26147</a></li>
<li>Seymour、R.A.、Alexander、N.、Mellor、S.、O'Neill、G.C.、Tierney、T.M.、Barnes、G.R.、およびマグワイア、EA (2021)。 OPM を使用して、立っているモバイル参加者の神経活動を測定します。 <em>NeuroImage</em>、244、118604.<a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">doi:10.1016/j.neuroimage.2021.118604</a></li>
<li>Mellor、S.J.、Tierney、T.M.、O'Neill、G.C.、Alexander、N.、Seymour、R.A.、Holmes、N.、Lopez、J.D.、Hill、R.M.、Boto、E.、Rea、M.、Roberts、G.、Leggett、J.、Bowtell、R.、Brookes、M.J.、マグワイア、EA、ウォーカー、MC、およびバーンズ、G.R. (2022)。可動OP-MEGの磁場マッピングと補正。 <em>IEEE Transactions on Biomedical Engineering</em>、69(2)、528-536。 <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">doi:10.1109/TBME.2021.3100770</a></li>
<li>Rea, M.、Holmes, N.、Hill, R.M.、Boto, E.、Leggett, J.、Edwards, L. J.、Wolger, D.、Dawson, E.、Shah, V.、Osborne, J.、Bowtell, R.、およびM.J.ブルックス (2021)。ウェアラブル脳磁計のための高精度の磁場のモデリングと制御。 <em>NeuroImage</em>、241、118401.<a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">doi:10.1016/j.neuroimage.2021.118401</a></li>
<li>ホームズ、N.、レア、M.、ヒル、R.M.、レゲット、J.、エドワーズ、L.J.、ホブソン、P.J.、ボト、E.、ティアニー、T.M.、リアー、L.、レイナ リベロ、G.、シャー、V.、オズボーン、J.、フロムホールド、T.M.、グローバー、P.、ブルックス、M.J.、&amp;ボーテル、R. (2023)。マトリックスコイルアクティブ磁気シールドを使用したウェアラブル脳磁計での歩行動作を可能にします。 <em>NeuroImage</em>、274、120157.<a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">doi:10.1016/j.neuroimage.2023.120157</a></li>
<li>Holmes, N.、Rea, M.、Hill, R.M.、Boto, E.、Leggett, J.、Edwards, L. J.、Rhodes, N.、Shah, V.、Osborne, J.、Fromhold, T. M.、Glover, P.、Montague, P. R.、Brookes, M. J.、および;ボーテル、R. (2023)。ウェアラブル脳磁計による自然主義的なハイパースキャン。 <em>センサー</em>、23(12)、5454。<a href="https://doi.org/10.3390/s23125454" target="_blank">doi:10.3390/s23125454</a></li>
<li>Holmes, N.、Leggett, J.、Hill, R.M.、Rier, L.、Boto, E.、Schofield, H.、Hayward, T.、Dawson, E.、Wolger, D.、Shah, V.、Taulu, S.、Brookes, M. J.、およびボーテル、R. (2025)。軽く遮蔽された環境でのウェアラブル脳磁計。 <em>IEEE Transactions on Biomedical Engineering</em>、72(2)、609-618。 <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">doi:10.1109/TBME.2024.3465654</a></li>
<li>Iivanainen, J.、Borna, A.、Zetter, R.、Carter, T. R.、Stephen, J.M.、McKay, J.、Parkkonen, L.、Taulu, S.、およびシュウィント、P.D.D. (2022)。電磁コイルを使用した光ポンピング磁力計の校正と位置特定。 <em>センサー</em>、22(8)、3059。<a href="https://doi.org/10.3390/s22083059" target="_blank">doi:10.3390/s22083059</a></li>
<li>Rhodes, N.、Rier, L.、Boto, E.、Hill, R.M.、およびM.J.ブルックス (2025)。光ポンピング磁力計ベースの脳磁図法を使用した、MRI を使用しない信号源再構成。 <em>イメージング神経科学</em>、3、IMAG.a.8。 <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">doi:10.1162/IMAG.a.8</a></li>
<li>Wu, T.、Xiao, W.、Peng, X.、Wu, T.、およびGuo、H. (2025)。生体磁気測定用の光ポンピング磁力計アレイにおけるクロストークの低減。 <em>科学機器のレビュー</em>、96(8)、085004。<a href="https://doi.org/10.1063/5.0273491" target="_blank">doi:10.1063/5.0273491</a></li>
</ol>
