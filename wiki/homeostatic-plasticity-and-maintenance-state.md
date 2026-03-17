---
layout: default
title: "Wiki：恒常性可塑性と維持状態"
description: "connectome や細胞型ラベルがあっても残る、内在興奮性・AIS / ion-channel landscape・睡眠依存 homeostasis・髄鞘/代謝維持・clearance / immune support・分子ターンオーバー下の維持機構を一次文献から整理します。"
article_type: Wiki
subtitle: "『配線図＋細胞型』でも、長期ダイナミクスはまだ決まりません"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Technical / natural science only"
audience: "connectome の限界をさらに一段深く、内在状態と維持機構の側から確認したい人"
reading_time: "16〜22分"
page_intro: "このページは、『配線図も cell type も分かれば、残りはだいたい埋まるのではないか』という直感に対し、内在興奮性、AIS / ion-channel landscape、発火率 set point、睡眠依存の再正規化、髄鞘/オリゴデンドロサイト結合、グリア代謝、clearance / immune support、分子ターンオーバー下の維持機構がなお別変数として残ることを、一次文献ベースで整理する wiki です。哲学や法制度ではなく、技術と自然科学だけに絞ります。"
accuracy_note: "ここで示すのは、長期ダイナミクスや記憶維持を読むときに最低限外してはいけない hidden state の整理です。これで十分条件が確定したという意味ではありません。"
page_highlights:
  - "maintenance-state は内在興奮性だけではなく、AIS / ion-channel landscape、睡眠依存 homeostasis、髄鞘/オリゴデンドロサイト、グリア代謝と astrocyte ensemble、clearance / immune support まで含みます。"
  - "短期の活動一致と、長期の維持機構が同じであることは別の主張です。"
  - "記憶が残ること自体も、静的分子の保存ではなく、再正規化・再固定化・代謝支援を含む active maintenance として読む必要があります。"
  - "sleep は平均発火率を戻すだけでなく、synapse diversity の維持にも関わるため、maintenance-state を1次元の補正量として扱えません。"
  - "intrinsic excitability は 1 行ではなく、relative excitability、AIS geometry / Na+ channel distribution、recovery controller に分けて読む必要があります。"
  - "human 側の前進も、EM 断片、whole-brain MRSI、myelin bilayer map、sleep / TMS proxy、CSF / glymphatic proxy という別階層の証拠として読み分ける必要があります。"
known_points:
  - "同じ transcriptomic type の内部にも morpho-electric phenotype の連続性や variability が残ります。"
  - "firing rate や synaptic strength は、sleep/wake cycle をまたぐ homeostatic plasticity によって調整されます。"
  - "髄鞘、オリゴデンドロサイト、アストロサイト、microglia / meningeal lymphatic 系の状態は timing、代謝、記憶想起、長期回復、clearance support に関わります。"
  - "human でも MRSI-based metabolic connectome、myelin bilayer mapping、TMS/EEG・sleep plasticity proxy、CSF / glymphatic proxy により macro scaffold と support-state proxy は見え始めていますが、cell-specific maintenance-state はまだ粗く残ります。"
unknown_points:
  - "どの粒度まで excitability / sleep-homeostasis / metabolic support / clearance support を測れば WBE の十分条件に近づくかは未確定です。"
  - "人で直接測れない maintenance state を、MRSI / myelin bilayer / TMS-EEG / sleep plasticity proxy / CSF-glymphatic proxy のどれで、どの外部基準へ較正すべきかは未確定です。"
  - "長期 closed-loop claim に対して、どの sleep / myelin / metabolic / clearance 指標を共通提出物にするかもまだ固定されていません。"
  - "parcel-level metabolic similarity や CSF mobility proxy が cell-specific glial / immune / transmitter / synaptic maintenance-state をどこまで拘束するかも未確定です。"
wiki_links:
  - label: "Wiki: 配線図だけでは足りない理由"
    url: "/wiki/connectome-is-not-enough.html"
    description: "connectome の不足を、より広い state variable の観点から先に整理します。"
  - label: "Wiki: state・trait・ドリフト"
    url: "/wiki/state-trait-and-drift.html"
    description: "縦断評価で maintenance state と drift をどう分けるかを補います。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "観測から latent state をどこまで持ち上げてよいかを補います。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "WBE入門"
    url: "/wbe_101.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い結論</h2>
<p>
<strong>connectome と cell type が分かっても、長期ダイナミクスはまだ決まりません</strong>。現状の一次文献が比較的一貫して示しているのは、少なくとも 7 種類の maintenance-state が残るということです。第一に、同じ transcriptomic type の内部でも morpho-electric phenotype と ion-channel expression は幅を持ち、さらに AIS geometry や Na+ channel distribution が数時間から数日スパンで動きえます。第二に、神経回路は firing rate や synaptic strength を homeostatic に調整し、<strong>今の活動</strong>を保つだけでなく、<strong>どこへ戻るか</strong>という set point 自体を持ちます。第三に、sleep / wake cycle は synaptic scaling と firing-rate homeostasis を時間的に分業させます。第四に、髄鞘とオリゴデンドロサイト結合は timing だけでなく axonal support にも関わります。第五に、アストロサイトやグリア代謝は記憶固定化の背景ではなく、<strong>記憶想起、数日スパンの安定化、恐怖記憶表現</strong>にも関わります。第六に、meningeal lymphatic drainage、CSF-interstitial exchange、microglia を含む clearance / immune support は synaptic physiology と multiday recovery を支えます。第七に、分子ターンオーバー下で記憶が残るとしても、それは静止した分子の永久保存ではなく、active maintenance が働いているという意味です。したがって、本サイトでは <strong>relative excitability・AIS / channel state・恒常性 set point・睡眠依存再正規化・髄鞘/代謝維持・astrocyte ensemble・clearance / immune support を含む再固定化機構</strong>を、connectome の外側に残る hidden state として扱います。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここでは哲学、法制度、コピー問題は扱いません。扱うのは、WBE や長期 BCI を読むときに、配線図、cell type、短期活動一致だけではまだ過小規定である理由です。
</p>
</div>

<section class="section" id="six-maintenance-classes">
<h2 class="section-title">先に固定する 7 つの maintenance-state</h2>
<table class="data-table">
<thead>
<tr>
<th>maintenance-state</th>
<th>何が欠けるか</th>
<th>危険な誤読</th>
<th>現時点での扱い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>内在興奮性 / AIS / ion-channel 構成</strong></td>
<td>threshold、gain、afterhyperpolarization、burstiness、rebound、AIS length / position、Na+ channel distribution など、入力に対する細胞側の応答則です。</td>
<td>cell-type ラベルか短い活動記録があれば、同じ入力出力則までほぼ決まる、と読むことです。</td>
<td>morpho-electric か patch / perturbation を伴わない限り、latent state として残します。</td>
</tr>
<tr>
<td><strong>発火率 set point / recovery controller</strong></td>
<td>回路が perturbation 後にどこへ戻るか、どの時定数で戻るか、どの代償経路を使うかです。</td>
<td>今の平均 firing rate が似ていれば、維持機構も同じだ、と読むことです。</td>
<td>longitudinal claim では fixed-model 劣化と回復ログ、set point を示す指標が無ければ降格します。</td>
</tr>
<tr>
<td><strong>sleep / wake 依存の再正規化</strong></td>
<td>synaptic scaling、phosphoproteome、network regime が、いつ reset され、いつ蓄積されるかです。</td>
<td>覚醒中の活動や same-day decode が似ていれば、翌日の維持機構も同じだ、と読むことです。</td>
<td>sleep state や overnight recovery を欠く場合、cross-day stability は限定つきに留めます。</td>
</tr>
<tr>
<td><strong>髄鞘 / オリゴデンドロサイト support</strong></td>
<td>伝導速度、activity-dependent myelination、axonal metabolic support の変化です。</td>
<td>delay を定数で置けば timing も energy support も十分だ、と読むことです。</td>
<td>myelin / oligodendroglial state が無ければ、timing-sensitive claim と長期回復 claim を弱めます。</td>
</tr>
<tr>
<td><strong>グリア代謝 / substrate routing</strong></td>
<td>astrocyte-neuron lactate shuttle、astrocyte ensemble の再活性化、local transmitter に対する astrocyte network 応答、slow metabolic support です。</td>
<td>ニューロン側のエングラムだけ追えば、想起や数日後の安定化までほぼ決まる、と読むことです。</td>
<td>glial / metabolic state を落とすなら、可塑性・記憶想起・再安定化・slow state の適用範囲を限定します。</td>
</tr>
<tr>
<td><strong>clearance / immune support</strong></td>
<td>meningeal lymphatic drainage、CSF-interstitial exchange、microglia-mediated surveillance、protein / metabolite clearance と回復時の免疫支持です。</td>
<td>clearance は passive housekeeping なので、momentary neural fit や翌日の安定性にはほぼ関係しない、と読むことです。</td>
<td>clearance / immune support を落とすなら、multiday recovery、protein-clearance、support-state claim を弱め、human proxy は support-state proxy と明記します。</td>
</tr>
<tr>
<td><strong>分子ターンオーバー下の再固定化</strong></td>
<td>受容体・キナーゼ・足場タンパク質が入れ替わっても、何が記憶痕跡を保つかです。</td>
<td>記憶が残るなら、静的な分子 snapshot だけ保存すれば十分だ、と読むことです。</td>
<td>分子保持を主張せず、maintenance mechanism が未測定なら未測定と明記します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-cell-type-is-not-enough">
<h2 class="section-title">なぜ cell type と短期活動一致だけでは不足するのか</h2>

<h3>1. transcriptomic type は morpho-electric phenotype を完全には固定しません</h3>
<p>
<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> は、mouse motor cortex の transcriptomic cell types が morpho-electric space の中で連続的な変動を持つことを示しました。これは、<strong>cell-type ラベルが分かっても、その場の電気生理パラメータまで一意に決まるわけではない</strong>ことを意味します。さらに <a href="https://doi.org/10.1038/nn1639" target="_blank">Schulz et al. (2006)</a> は、同定済みニューロンで ion channel mRNA と電流量に大きな個体差がありながら、機能はある程度保たれうることを示しました。したがって、connectome に cell-type ラベルを重ねても、<strong>threshold と gain の層</strong>はまだ残ります。
</p>

<h3>2. 維持されているのは「今の値」ではなく「戻り先」であることがあります</h3>
<p>
<a href="https://doi.org/10.1038/36103" target="_blank">Turrigiano et al. (1998)</a> は、慢性活動遮断や活動増加に対して neocortical neurons が quantal amplitude を bidirectionally scaling することを示しました。さらに <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a> は、activity-dependent な ion-channel expression の簡潔な生物物理モデルから、activity set point、cell type、compensation の関係が説明できることを示しました。<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> は、in vivo の視覚野で individual neuron が precise firing-rate set point へ戻ることを示しています。ここで重要なのは、<strong>snapshot としての活動値</strong>だけでなく、<strong>perturbation 後にどこへ戻るか</strong>という controller 側の状態が別変数だという点でございます。
</p>

<h3>3. intrinsic excitability は 1 行ではなく、AIS と ion-channel landscape に分かれます</h3>
<p>
今回もっとも深掘りすべきだった弱点は、<strong>intrinsic excitability</strong> を 1 つの latent state として書くと、<strong>relative excitability による memory allocation</strong>、<strong>AIS geometry / Na+ channel distribution による gain 調整</strong>、<strong>homeostatic recovery controller</strong> が同じ証拠階層に見えてしまう点でございました。<a href="https://doi.org/10.1038/nature09160" target="_blank">Grubb &amp; Burrone (2010)</a> は activity に応じた AIS relocation が neuronal excitability を fine-tune することを示し、<a href="https://doi.org/10.1038/nature09087" target="_blank">Kuba et al. (2010)</a> は presynaptic activity が AIS の Na+ channel distribution を調整しうることを示しました。さらに <a href="https://doi.org/10.1038/s41467-020-20232-x" target="_blank">Jamann et al. (2021)</a> は mouse barrel cortex で sensory input に応じた rapid homeostatic AIS scaling を、<a href="https://doi.org/10.1126/sciadv.adf3885" target="_blank">Fréal et al. (2023)</a> は sodium channel endocytosis が AIS plasticity を駆動することを、<a href="https://doi.org/10.1038/s41593-025-02152-5" target="_blank">Benoit et al. (2025)</a> は associative fear learning の間に AIS dynamics が変わることを示しました。したがって、<strong>同じ connectome と同じ cell type</strong> が分かっていても、<strong>数時間から数日スパンの threshold / gain / spike-initiation rule</strong> はなお latent に残ります。
</p>
<div class="note-box">
<strong>この節から直接言えること</strong>
<p>
ここから直接言えるのは、WBE や長期 BCI の入力出力則を読むとき、<strong>intrinsic excitability を 1 個の数字や 1 行の欠測欄に潰してはいけない</strong>という点でございます。allocation、AIS / channel state、recovery controller は別々に測るか、少なくとも別々に棄権理由を書く必要があります。
</p>
</div>

<h3>4. sleep / wake cycle は synapse と network regime を再配線します</h3>
<p>
現行サイトの弱点は、maintenance-state を excitability と molecular turnover に寄せすぎて、<strong>sleep が再正規化の時間軸そのものを担う</strong>ことを前面に出せていなかった点です。<a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a> は、wake で上がった firing rate が sleep 中に downward homeostasis で戻ることを示しました。<a href="https://doi.org/10.1126/science.aah5982" target="_blank">de Vivo et al. (2017)</a> は wake / sleep cycle をまたぐ ultrastructural な synaptic scaling を示し、<a href="https://doi.org/10.1126/science.aai8355" target="_blank">Diering et al. (2017)</a> は Homer1a を介した sleep 中の excitatory synapse scaling-down を示しました。さらに <a href="https://doi.org/10.1126/science.aav2642" target="_blank">Noya et al. (2019)</a> は forebrain synaptic proteome が sleep によって駆動されることを示し、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a> は sleep が cortical network をよりよい computational regime へ戻すことを報告しました。加えて <a href="https://doi.org/10.1016/j.cub.2024.07.032" target="_blank">Koukaroudi et al. (2024)</a> は、sleep deprivation が cortex と hippocampus の excitatory synapse diversity を減らすことを示し、maintenance-state が単なる平均値の再較正ではなく、<strong>synaptic repertoire の分布維持</strong>も含むことを強めました。したがって、<strong>same-day の活動一致だけで maintenance-state が合ったと読むことはできません</strong>。sleep history と overnight recovery log が無ければ、翌日の安定性や学習後の再平衡はまだ別問題です。
</p>

<h3>5. 髄鞘とオリゴデンドロサイトは timing と support の変数です</h3>
<p>
現行ページは内在興奮性には触れていても、<strong>delay を生む基盤である髄鞘の可塑性</strong>を maintenance-state として十分に固定していませんでした。<a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a> は neuronal activity が oligodendrogenesis と adaptive myelination を促進することを示し、<a href="https://doi.org/10.1126/science.1254960" target="_blank">McKenzie et al. (2014)</a> は motor skill learning に active central myelination が必要であることを示しました。さらに <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a> は oligodendrocyte-axon metabolic coupling が extracellular K<sup>+</sup> に媒介され、axonal health の維持に関わることを示しました。したがって、<strong>同じ配線と同じ cell type でも、myelin / oligodendroglial state が違えば timing と回復性は変わりえます</strong>。delay を固定定数で置いたモデルは便利ですが、その近似で何を捨てたかを明記すべきでございます。
</p>

<h3>6. アストロサイトは記憶想起・安定化・表現の state variable です</h3>
<p>
maintenance-state を neuron-centric に読みすぎると、エネルギー供給と local transmitter integration を「背景ノイズ」と誤読しやすくなります。<a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011)</a> は astrocyte-neuron lactate transport が long-term memory formation に必要であることを示しました。<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> は、局所的で瞬間的な neurotransmitter input が分オーダーにわたる広い astrocyte network state に符号化されることを示しました。さらに <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a> は hippocampus で learning-associated astrocyte ensemble が engram neuron の近傍に形成され、ensemble 再活性化が memory recall を引き起こし、astrocyte 特異的 NFIA deletion が recall を抑えることを示しました。<a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a> は emotional memory に伴う astrocyte ensemble が repeated recall をまたいで数日スパンの安定化へ寄与し、noradrenergic input と local engram signal を統合して memory stability と precision を左右することを示しました。さらに <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> は basolateral amygdala astrocytes が fear retrieval / extinction に応じて再編成され、astrocyte Ca<sup>2+</sup> signaling が amygdala-prefrontal circuit の neural representation を支えることを示しました。ここから直接言えるのは、<strong>glial / metabolic background を後付け補正とみなすのは危険であり、長期記憶では astrocyte ensemble 自体が state variable として残る</strong>という点です。memory consolidation や slow network state を論じるなら、少なくとも astrocyte / metabolic support をどこまで測ったか、どこから先を proxy で代用したかを区別する必要があります。
</p>

<div class="note-box">
<strong>証拠強度の読み方</strong>
<p>
一方で、<a href="https://doi.org/10.1038/s41586-023-07011-6" target="_blank">Sun et al. (2024)</a> の spatial transcriptomics は peri-engram neuron と astrocyte の相互作用、および <em>Igfbp2</em> を long-term memory candidate として提案しましたが、<a href="https://doi.org/10.1038/s41586-025-08988-y" target="_blank">Mukamel &amp; Yu (2025)</a> は multiple-comparison と同一動物由来細胞の依存性を補正すると有意な DEG は残らないと批判し、<a href="https://doi.org/10.1038/s41586-025-08989-x" target="_blank">Sun et al. (2025)</a> は解析意図の違いを理由に反論しました。したがって本サイトでは、この系を <strong>transcriptomic clue / hypothesis-generating evidence</strong> として扱い、glia の因果的な重みづけは <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> のような再活性化・阻害・回路表現の介入研究の方へ置きます。
</p>
</div>

<h3>7. clearance / immune support は passive cleanup ではありません</h3>
<p>
今回さらに深掘りして見えた弱点は、<strong>astrocyte / metabolic support</strong> を厚く書いた一方で、<strong>meningeal lymphatics、CSF-interstitial exchange、microglia を含む clearance / immune support</strong> を独立の maintenance-state として十分に切り出せていなかった点でございます。<a href="https://doi.org/10.1038/nature14432" target="_blank">Louveau et al. (2015)</a> は CNS lymphatic vessels の構造と機能を示し、<a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a> は meningeal lymphatics-microglia axis が synaptic physiology を調整することを示しました。human 側でも <a href="https://doi.org/10.1093/brain/awab285" target="_blank">Eide &amp; Ringstad (2021)</a> は sleep deprivation が molecular clearance を阻害することを、<a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> は MRI で region-specific な CSF mobility driver を測れることを、<a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> は human で glymphatic route に沿った amyloid-beta / tau clearance を示しました。ここから直接言えるのは、<strong>clearance / immune support は単なる掃除の比喩ではなく、multiday support-state として measurable になりつつある</strong>という点です。ただし同時に、これら human データは <strong>local synaptic weight</strong> や <strong>moment-to-moment neural truth</strong> の direct readout ではありません。したがって本サイトでは、clearance / immune support を <strong>slow support-state</strong> として独立扱いしつつ、human ではまず <strong>macro support proxy</strong> として読みます。
</p>

<h3>8. 分子ターンオーバー下の記憶は、静的保存ではなく再固定化として読むべきです</h3>
<p>
<a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">Lee et al. (2022)</a> は、シミュレーションと解析を通じて、synaptic memory が molecular turnover の下でも active な CaMKII state transfer により維持されうることを示しました。ここから直接言えるのは、「分子が入れ替わっても記憶が残ることはありうる」という点です。しかし逆に言えば、<strong>記憶の持続は静的分子 snapshot の十分性を意味せず、維持機構が働いていることを意味する</strong>と読む方が安全でございます。sleep 中の synaptic scaling や glial-metabolic support を合わせて読むと、記憶維持は単一分子の凍結保存ではなく、<strong>再正規化と再固定化の連鎖</strong>として扱う方が一次文献に近い整理になります。
</p>

<h3>9. 相対 excitability は将来の記憶配分を左右します</h3>
<p>
<a href="https://doi.org/10.1016/j.neuron.2014.07.017" target="_blank">Yiu et al. (2014)</a> は、学習前の相対的な neuronal excitability が、どのニューロンが memory trace に組み込まれやすいかを左右することを示しました。さらに <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2026)</a> は、neocortical engram neurons の early intrinsic excitability plasticity が memory formation と precision を規定することを示しています。したがって、<strong>connectome が同じでも excitability landscape が違えば、将来の学習経路と記憶配分は変わりえます</strong>。
</p>
</section>

<section class="section" id="human-observability-ceiling">
<h2 class="section-title">2026-03 追補：human maintenance-state の直接観測はまだ粗い</h2>
<p>
今回さらに深掘りして見えた弱点は、human observability の節が、<strong>EM 断片</strong>、<strong>whole-brain MRSI</strong>、<strong>myelin bilayer imaging</strong>、<strong>TMS-EEG / sleep plasticity proxy</strong>、<strong>CSF / glymphatic proxy</strong> を同じ「human で見え始めた証拠」としてまとめすぎていた点でございます。一次文献を並べると、それぞれが押し上げているのは <strong>structural scaffold</strong>、<strong>macro-biochemical scaffold</strong>、<strong>macro-myelin proxy</strong>、<strong>perturbation-conditioned plasticity proxy</strong>、<strong>macro support-state proxy</strong> という別々の層です。どれも重要ですが、<strong>current synaptic efficacy</strong>、<strong>local transmitter specificity</strong>、<strong>astrocyte ensemble</strong>、<strong>sleep-dependent recovery controller</strong>、<strong>cell-specific immune controller</strong> を直接は与えません。したがって、human 側でも maintenance-state はなお <strong>macro scaffold / macro proxy / local hidden state</strong> に分かれて残ります。
</p>
<table class="data-table">
<thead>
<tr>
<th>human で見え始めたもの</th>
<th>直接見えている層</th>
<th>まだ latent の層</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>human nanoscale ultrastructure</strong><br>Shapson-Coe ら</td>
<td>固定済み human cortex 断片の ultrastructure、細胞・シナプス配置、局所構造 scaffold。</td>
<td>current weight、sleep-history、recovery controller、neuromodulatory context、glial slow-state。</td>
</tr>
<tr>
<td><strong>human metabolic connectome</strong><br>Lucchetti ら</td>
<td>Glx / Ins / Cho / tCr / tNAA に基づく parcel-level biochemical organization と、その再現性。</td>
<td>cell-specific metabolic routing、astrocyte ensemble、local transmitter state、synapse-specific maintenance。</td>
</tr>
<tr>
<td><strong>human myelin bilayer map</strong><br>Baadsvik ら</td>
<td>in vivo の 1.4 mm 級 myelin bilayer contrast と、regional myelin distribution。</td>
<td>single-axon conduction delay、activity-dependent myelination、oligodendrocyte-axon metabolic support、cell-specific timing controller。</td>
</tr>
<tr>
<td><strong>human sleep-homeostasis / plasticity proxy</strong><br>Huber ら、Kuhn ら、Fehér ら</td>
<td>wake / sleep / nap に応じて TMS-EEG excitability や PAS 誘導 plasticity が変わる、という macro な perturbational proxy。</td>
<td>どの cell type、どの synapse、どの glia、どの controller がその変化を担ったか。</td>
</tr>
<tr>
<td><strong>human state-gated perturbation proxy</strong><br>Zrenner ら</td>
<td>EEG-defined excitability state が TMS-induced plasticity efficacy を左右する、という state-conditioned causal proxy。</td>
<td>AIS geometry、channel distribution、cell-specific allocation state、長期 recovery controller。</td>
</tr>
<tr>
<td><strong>human CSF / glymphatic proxy</strong><br>Hirschler ら、Dagum ら</td>
<td>region-specific な CSF mobility と、glymphatic route に沿った protein clearance の macro support-state proxy。</td>
<td>どの synapse、どの astrocyte、どの microglia、どの meningeal lymphatic controller がその差を担ったか。</td>
</tr>
</tbody>
</table>
<p>
この差は実務上重要でございます。<a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> は fixed tissue の局所 ultrastructure を、<a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> は whole-brain の biochemical covariance を、<a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> は myelin bilayer の in vivo map を、<a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">Huber et al. (2013)</a>、<a href="https://doi.org/10.1038/ncomms12455" target="_blank">Kuhn et al. (2016)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">Fehér et al. (2026)</a>、<a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> は sleep / wake / nap や瞬間 brain state が human plasticity response を変えることを、<a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> と <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> は human で CSF / glymphatic support-state を measurable にし始めたことを、それぞれ別々に押し上げました。重要なのは、<strong>これらが同じ種類の direct measurement ではない</strong>という点であり、1 本の human proxy を cell-specific maintenance-state の ground truth へ読み替えてはいけないことです。
</p>
<div class="note-box">
<strong>この追補での実務的な読み替え</strong>
<p>
したがって、本サイトでは <strong>human metabolic connectome</strong> を <strong>macro-biochemical scaffold</strong>、<strong>human myelin bilayer map</strong> を <strong>macro-myelin proxy</strong>、<strong>TMS-EEG / sleep plasticity</strong> を <strong>perturbational proxy</strong>、<strong>CSF mobility / glymphatic clearance</strong> を <strong>macro support-state proxy</strong> として扱います。いずれも有望ですが、<strong>glial / transmitter maintenance-state の ground truth</strong>、<strong>cell-specific recovery controller</strong>、<strong>local immune controller</strong> とは書きません。同様に human EM 断片も、<strong>state-complete snapshot</strong> ではなく <strong>structural scaffold の強化</strong> として扱います。human で直接見えていない層は、animal causal evidence で existence を支えつつ、human 側では observability ceiling と abstention を明示するのが安全でございます。
</p>
</div>
</section>

<section class="section" id="dangerous-misreadings">
<h2 class="section-title">よくある誤読と、このサイトでの降格ルール</h2>
<table class="data-table">
<thead>
<tr>
<th>危険な読み方</th>
<th>なぜ危険か</th>
<th>このサイトでの扱い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>cell-type ラベルが分かれば入力出力則もほぼ決まる</strong></td>
<td>同じ type の内部にも morpho-electric variability と channel-expression variability が残ります。</td>
<td>cell-type だけでは excitability fixed と書かず、latent state として残します。</td>
</tr>
<tr>
<td><strong>同じ connectome / cell type なら、AIS や channel-state もほぼ同じだ</strong></td>
<td>AIS length / position と Na+ channel distribution は、activity・sensory input・learning に応じて動きます。</td>
<td>patch、perturbation、AIS proxy が無ければ、gain / allocation / spike-initiation rule は latent state として残します。</td>
</tr>
<tr>
<td><strong>平均 firing rate が戻ったので内部状態も同じに戻った</strong></td>
<td>同じ rate を別の conductance 組み合わせや別の controller で達成している可能性があります。</td>
<td>rate 回復だけで内部同一性を主張せず、perturbation と recovery のログを要求します。</td>
</tr>
<tr>
<td><strong>日中の活動や decoder 成績が似ていれば、overnight maintenance も同じだ</strong></td>
<td>sleep 中の synaptic scaling、firing-rate homeostasis、network regime の回復が別に残ります。</td>
<td>sleep / wake 注釈や翌日 recovery を出していない場合、cross-day stability claim は降格します。</td>
</tr>
<tr>
<td><strong>human metabolic connectome があれば、glial / transmitter maintenance-state も直接見えた</strong></td>
<td>parcel-level metabolic similarity は有用ですが、cell-specific astrocyte ensemble や transmitter state をそのまま与えません。</td>
<td>human MRSI は macro-biochemical scaffold として扱い、local maintenance-state の ground truth とは書きません。</td>
</tr>
<tr>
<td><strong>human myelin bilayer map や nap / TMS proxy があれば、cell-specific maintenance controller も見えた</strong></td>
<td>myelin bilayer map は mm 級の tissue proxy であり、TMS-EEG / PAS は perturbational readout です。どの axon、oligodendrocyte、astrocyte、synapse がその変化を担ったかは別に残ります。</td>
<td>human myelin / sleep / excitability データは macro or perturbational proxy と明記し、cell-specific controller の ground truth には上げません。</td>
</tr>
<tr>
<td><strong>human CSF mobility や glymphatic clearance が見えたので、local immune / clearance controller も同定できた</strong></td>
<td>human CSF / glymphatic data は macro support-state proxy であり、どの microglia、meningeal lymphatic segment、astrocyte endfoot、局所 synapse が差を担ったかは別に残ります。</td>
<td>human clearance proxy は support-state proxy と書き、moment-to-moment neural truth や cell-specific immune controller へは上げません。</td>
</tr>
<tr>
<td><strong>delay を定数で置けば、髄鞘やオリゴデンドロサイトは後回しでよい</strong></td>
<td>adaptive myelination と axon-glia coupling は timing と long-term support に関わります。</td>
<td>timing-sensitive claim では myelin / conduction の未測定を本文に明記します。</td>
</tr>
<tr>
<td><strong>ニューロン側の engram やスパイク列が似ていれば、想起や数日後の安定化も同じだ</strong></td>
<td>astrocyte ensemble、lactate transport、local transmitter integration は memory recall、restabilization、fear-state representation に関与します。</td>
<td>glial / metabolic support を落とすときは、可塑性・記憶固定化・想起・再安定化・slow state の適用範囲を限定します。</td>
</tr>
<tr>
<td><strong>記憶が長持ちするなら、保存すべき分子状態は静的だ</strong></td>
<td>持続はしばしば turnover をまたぐ active maintenance と再固定化の結果です。</td>
<td>分子 snapshot の十分性は主張せず、維持機構の未測定を明記します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">このサイトで採用する実務ルール</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>長期 claim では maintenance-state を別列に出す：</strong>connectome / cell type / synapse と、intrinsic excitability、sleep-homeostasis、myelin / oligodendroglial support、glial / metabolic support、clearance / immune support を混ぜません。</li>
<li><strong>intrinsic excitability を 1 行に潰さない：</strong>relative excitability、AIS / channel state、recovery controller を別欄にします。</li>
<li><strong>sleep / wake 履歴を測っていなければ測っていないと書く：</strong>same-day fit から overnight maintenance を自動補完しません。</li>
<li><strong>sleep を平均値補正に縮約しない：</strong>synapse diversity や network regime まで落ちる可能性を残します。</li>
<li><strong>delay を定数で吸収したら吸収したと書く：</strong>timing state と axonal support を無言でモデル内へ押し込みません。</li>
<li><strong>memory persistence を static storage と言い換えない：</strong>turnover をまたぐ再固定化と支援機構の可能性を先に残します。</li>
<li><strong>perturbation 後の recovery を重視する：</strong>何が起きたかだけでなく、どこへ戻るか、睡眠をまたいでどう戻るかをログに残します。</li>
<li><strong>proxy の限界を先に書く：</strong>EEG / pupil / behavior だけで maintenance-state を一意に決めたとは書きません。</li>
<li><strong>human proxy class を混ぜない：</strong>EM 断片、whole-brain MRSI、myelin bilayer map、sleep / TMS proxy を同じ「human で見えた」の 1 語に畳み込みません。</li>
<li><strong>human MRSI を local ground truth と誤読しない：</strong>macro-biochemical scaffold と cell-specific maintenance-state を分けて書きます。</li>
<li><strong>human CSF / glymphatic proxy を local controller と誤読しない：</strong>macro support-state proxy と cell-specific immune / clearance state を分けて書きます。</li>
<li><strong>neuron-only の成功から glia omission を補完しない：</strong>想起・再安定化・fear-state representation は astrocyte state を別に残します。</li>
</ul>
</div>
<table class="data-table">
<thead>
<tr>
<th>主張したいこと</th>
<th>最低限ほしい提出物</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>cross-day stability</strong></td>
<td>fixed model の劣化曲線、recovery time、sleep / wake 注釈、state / trait / drift の切り分け、possible なら firing-rate distribution や excitability proxy。</td>
</tr>
<tr>
<td><strong>gain / excitability claim</strong></td>
<td>relative excitability か perturbation proxy、possible なら AIS / channel proxy、within-day / cross-day の gain drift、未測定 allocation / recovery controller の omission log。</td>
</tr>
<tr>
<td><strong>長期 memory / learning claim</strong></td>
<td>学習前後の perturbation 応答、relative excitability か allocation proxy、overnight renormalization の有無、glial / astrocyte covariate か omission log、possible なら clearance / immune covariate、未測定 maintenance-state 一覧。</td>
</tr>
<tr>
<td><strong>timing-sensitive claim</strong></td>
<td>delay / phase error、myelin か conduction proxy、timing support を固定定数で近似した箇所、未測定 oligodendroglial state。</td>
</tr>
<tr>
<td><strong>state-complete reconstruction に近い claim</strong></td>
<td>connectome・cell type・synapse・delay / myelin・neuromodulation・glia / metabolic support・clearance / immune support・sleep-homeostasis・intrinsic excitability / homeostasis をどこまで取得したか、あるいは latent として棄権したか。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>Schulz, D. J., Goaillard, J.-M., &amp; Marder, E. (2006). Variable channel expression in identified single and electrically coupled neurons in different animals. <em>Nature Neuroscience</em>, 9(3), 356-362. <a href="https://doi.org/10.1038/nn1639" target="_blank">doi:10.1038/nn1639</a></li>
<li>Grubb, M. S., &amp; Burrone, J. (2010). Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. <em>Nature</em>, 465(7301), 1070-1074. <a href="https://doi.org/10.1038/nature09160" target="_blank">doi:10.1038/nature09160</a></li>
<li>Kuba, H., Oichi, Y., &amp; Ohmori, H. (2010). Presynaptic activity regulates Na+ channel distribution at the axon initial segment. <em>Nature</em>, 465(7301), 1075-1078. <a href="https://doi.org/10.1038/nature09087" target="_blank">doi:10.1038/nature09087</a></li>
<li>Jamann, N., Dannehl, D., Lehmann, N., et al. (2021). Sensory input drives rapid homeostatic scaling of the axon initial segment in mouse barrel cortex. <em>Nature Communications</em>, 12, 23. <a href="https://doi.org/10.1038/s41467-020-20232-x" target="_blank">doi:10.1038/s41467-020-20232-x</a></li>
<li>Fréal, A., Jamann, N., Ten Bos, J., et al. (2023). Sodium channel endocytosis drives axon initial segment plasticity. <em>Science Advances</em>, 9(37). <a href="https://doi.org/10.1126/sciadv.adf3885" target="_blank">doi:10.1126/sciadv.adf3885</a></li>
<li>Benoit, C. M., Ganea, D. A., Paricio-Montesinos, R., et al. (2025). Axon initial segment dynamics during associative fear learning. <em>Nature Neuroscience</em>, 29(3), 535-542. <a href="https://doi.org/10.1038/s41593-025-02152-5" target="_blank">doi:10.1038/s41593-025-02152-5</a></li>
<li>Turrigiano, G. G., Leslie, K. R., Desai, N. S., Rutherford, L. C., &amp; Nelson, S. B. (1998). Activity-dependent scaling of quantal amplitude in neocortical neurons. <em>Nature</em>, 391, 892-896. <a href="https://doi.org/10.1038/36103" target="_blank">doi:10.1038/36103</a></li>
<li>O'Leary, T., Williams, A. H., Franci, A., &amp; Marder, E. (2014). Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. <em>Neuron</em>, 82(4), 809-821. <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">doi:10.1016/j.neuron.2014.04.002</a></li>
<li>Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., &amp; Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <em>Cell</em>, 165(1), 180-191. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <em>Neuron</em>, 109(3), 530-544.e6. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">doi:10.1016/j.neuron.2021.04.004</a></li>
<li>Diering, G. H., et al. (2017). Homer1a drives homeostatic scaling-down of excitatory synapses during sleep. <em>Science</em>, 355(6324), 511-515. <a href="https://doi.org/10.1126/science.aai8355" target="_blank">doi:10.1126/science.aai8355</a></li>
<li>de Vivo, L., et al. (2017). Ultrastructural evidence for synaptic scaling across the wake/sleep cycle. <em>Science</em>, 355(6324), 507-510. <a href="https://doi.org/10.1126/science.aah5982" target="_blank">doi:10.1126/science.aah5982</a></li>
<li>Noya, S. B., et al. (2019). The forebrain synaptic transcriptome is organized by clocks but its proteome is driven by sleep. <em>Science</em>, 366(6462), eaav2642. <a href="https://doi.org/10.1126/science.aav2642" target="_blank">doi:10.1126/science.aav2642</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <em>Nature Neuroscience</em>, 27, 972-980. <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">doi:10.1038/s41593-023-01536-9</a></li>
<li>Koukaroudi, D., Qiu, Z., Fransén, E., et al. (2024). Sleep maintains excitatory synapse diversity in the cortex and hippocampus. <em>Current Biology</em>, 34(16), 3836-3843.e5. <a href="https://doi.org/10.1016/j.cub.2024.07.032" target="_blank">doi:10.1016/j.cub.2024.07.032</a></li>
<li>Yiu, A. P., et al. (2014). Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. <em>Neuron</em>, 83(3), 722-735. <a href="https://doi.org/10.1016/j.neuron.2014.07.017" target="_blank">doi:10.1016/j.neuron.2014.07.017</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <em>Brain Stimulation</em>, 11(2), 374-389. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Huber, R., Mäki, H., Rosanova, M., Casarotto, S., Canali, P., Casali, A. G., Tononi, G., &amp; Massimini, M. (2013). Human cortical excitability increases with time awake. <em>Cerebral Cortex</em>, 23(2), 332-338. <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">doi:10.1093/cercor/bhs014</a></li>
<li>Kuhn, M., Wolf, E., Maier, J. G., Mainberger, F., Feige, B., Schmid, H., et al. (2016). Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. <em>Nature Communications</em>, 7, 12455. <a href="https://doi.org/10.1038/ncomms12455" target="_blank">doi:10.1038/ncomms12455</a></li>
<li>Fehér, K. D., Henckaerts, P., Hirsch, V., Bucsenez, U., Kuhn, M., Maier, J. G., et al. (2026). A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. <em>NeuroImage</em>, 327, 121723. <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">doi:10.1016/j.neuroimage.2026.121723</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318-322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <em>Nature Neuroscience</em>, 27, 1598-1609. <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">doi:10.1038/s41593-023-01558-3</a></li>
<li>Suzuki, A., et al. (2011). Astrocyte-neuron lactate transport is required for long-term memory formation. <em>Cell</em>, 144(5), 810-823. <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">doi:10.1016/j.cell.2011.02.018</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146-153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Sun, X., et al. (2024). Spatial transcriptomics reveal neuron-astrocyte synergy in long-term memory. <em>Nature</em>, 627, 374-381. <a href="https://doi.org/10.1038/s41586-023-07011-6" target="_blank">doi:10.1038/s41586-023-07011-6</a></li>
<li>Mukamel, E. A., &amp; Yu, X. (2025). False positives in study of memory-related gene expression. <em>Nature</em>, 642, E1-E3. <a href="https://doi.org/10.1038/s41586-025-08988-y" target="_blank">doi:10.1038/s41586-025-08988-y</a></li>
<li>Sun, X., et al. (2025). Reply to: False positives in study of memory-related gene expression. <em>Nature</em>, 642, E4-E6. <a href="https://doi.org/10.1038/s41586-025-08989-x" target="_blank">doi:10.1038/s41586-025-08989-x</a></li>
<li>Williamson, N. R., et al. (2025). Learning-associated astrocyte ensembles regulate memory recall. <em>Nature</em>, 636, 445-454. <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">doi:10.1038/s41586-024-08170-w</a></li>
<li>Dewa, K., et al. (2025). The astrocytic ensemble acts as a multiday trace to stabilize memory. <em>Nature</em>, 648, 99-107. <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">doi:10.1038/s41586-025-09619-2</a></li>
<li>Bukalo, O., et al. (2026). Astrocytes enable amygdala neural representations supporting memory. <em>Nature</em>. <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">doi:10.1038/s41586-025-10068-0</a></li>
<li>Louveau, A., Smirnov, I., Keyes, T. J., et al. (2015). Structural and functional features of central nervous system lymphatic vessels. <em>Nature</em>, 523, 337-341. <a href="https://doi.org/10.1038/nature14432" target="_blank">doi:10.1038/nature14432</a></li>
<li>Kim, J., et al. (2025). Meningeal lymphatics-microglia axis regulates synaptic physiology. <em>Cell</em>, 188(8), 2129-2148.e21. <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">doi:10.1016/j.cell.2025.02.022</a></li>
<li>Eide, P. K., &amp; Ringstad, G. (2021). Sleep deprivation impairs molecular clearance from the human brain. <em>Brain</em>, 144(3), 863-874. <a href="https://doi.org/10.1093/brain/awab285" target="_blank">doi:10.1093/brain/awab285</a></li>
<li>Lee, J.-C., Wang, C.-Y., Lin, C.-L., &amp; Lu, H.-C. (2022). Synaptic memory survives molecular turnover. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 119(42), e2211572119. <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">doi:10.1073/pnas.2211572119</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <em>Science</em>, 384(6696), eadk4858. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <em>Nature Communications</em>, 16, 11344. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., Schildknecht, C. M., Ineichen, B. V., &amp; Pruessmann, K. P. (2024). Myelin bilayer mapping in the human brain in vivo. <em>Magnetic Resonance in Medicine</em>, 91(6), 2332-2344. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Hirschler, L., et al. (2025). Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans. <em>Nature Neuroscience</em>, 28, 1115-1126. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., et al. (2026). The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. <em>Nature Communications</em>, 17, 7800. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="connectome-is-not-enough.html">配線図だけでは足りない理由 →</a></li>
<li><a href="state-trait-and-drift.html">state・trait・ドリフト →</a></li>
<li><a href="observation-to-estimation.html">観測から推定へ →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../verification.html#state-completeness-gate">状態変数の完全性ゲート →</a></li>
<li><a href="../tech_roadmap.html#qa-m3">M3 空間粒度 →</a></li>
<li><a href="../wbe_101.html#definition">WBE の操作的定義 →</a></li>
</ul>
</div>
</aside>
</main>
