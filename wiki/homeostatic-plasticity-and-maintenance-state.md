---
layout: default
title: "Wiki：恒常性可塑性と維持状態"
description: "connectome や細胞型ラベルがあっても残る、内在興奮性・発火 set point・分子ターンオーバー下の維持機構を一次文献から整理します。"
article_type: Wiki
subtitle: "『配線図＋細胞型』でも、長期ダイナミクスはまだ決まりません"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Technical / natural science only"
audience: "connectome の限界をさらに一段深く、内在状態と維持機構の側から確認したい人"
reading_time: "14〜18分"
page_intro: "このページは、『配線図も cell type も分かれば、残りはだいたい埋まるのではないか』という直感に対し、内在興奮性、発火率 set point、分子ターンオーバー下の維持機構がなお別変数として残ることを、一次文献ベースで整理する wiki です。哲学や法制度ではなく、技術と自然科学だけに絞ります。"
accuracy_note: "ここで示すのは、長期ダイナミクスや記憶維持を読むときに最低限外してはいけない hidden state の整理です。これで十分条件が確定したと言う意味ではありません。"
page_highlights:
  - "connectome と cell type があっても、内在興奮性と homeostatic controller はまだ別変数として残ります。"
  - "短期の活動一致と、長期の維持機構が同じであることは別の主張です。"
  - "記憶が残ること自体も、静的分子の保存ではなく、しばしば active maintenance を前提に読み替える必要があります。"
known_points:
  - "同じ transcriptomic type の内部にも morpho-electric phenotype の連続性や variability が残ります。"
  - "firing rate や synaptic strength は、homeostatic plasticity によって時間とともに調整されます。"
  - "分子ターンオーバーがあっても記憶が保たれるなら、その背後には維持・移送・再較正の機構が必要です。"
unknown_points:
  - "どの粒度まで excitability / homeostasis を測れば WBE の十分条件に近づくかは未確定です。"
  - "人で直接測れない maintenance state を、どの proxy とどの外部基準で較正すべきかは未確定です。"
  - "長期 closed-loop claim に対して、どの set point 指標を共通提出物にするかもまだ固定されていません。"
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
<strong>connectome と cell type が分かっても、長期ダイナミクスはまだ決まりません</strong>。理由は少なくとも 3 つございます。第一に、同じ transcriptomic type の内部でも morpho-electric phenotype と ion-channel expression は幅を持ちます。第二に、神経回路は firing rate や synaptic strength を homeostatic に調整し、<strong>今の活動</strong>を保つだけでなく、<strong>どこへ戻るか</strong>という set point 自体を持ちます。第三に、分子ターンオーバー下で記憶が残るとしても、それは静止した分子の永久保存ではなく、active maintenance が働いているという意味です。したがって、本サイトでは <strong>内在興奮性・恒常性 set point・維持機構</strong>を、connectome の外側に残る hidden state として扱います。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここでは哲学、法制度、コピー問題は扱いません。扱うのは、WBE や長期 BCI を読むときに、配線図、cell type、短期活動一致だけではまだ過小規定である理由です。
</p>
</div>

<section class="section" id="three-maintenance-classes">
<h2 class="section-title">先に固定する 3 つの maintenance-state</h2>
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
<td><strong>内在興奮性 / ion-channel 構成</strong></td>
<td>threshold、gain、afterhyperpolarization、burstiness、rebound など、入力に対する細胞側の応答則です。</td>
<td>cell-type ラベルか短い活動記録があれば、同じ入力出力則までほぼ決まる、と読むことです。</td>
<td>morpho-electric か patch / perturbation を伴わない限り、latent state として残します。</td>
</tr>
<tr>
<td><strong>発火率 set point / homeostatic controller</strong></td>
<td>回路が perturbation 後にどこへ戻るか、どの時定数で戻るか、どの代償経路を使うかです。</td>
<td>今の平均 firing rate が似ていれば、維持機構も同じだ、と読むことです。</td>
<td>longitudinal claim では fixed-model 劣化と回復ログ、set point を示す指標が無ければ降格します。</td>
</tr>
<tr>
<td><strong>分子ターンオーバー下の維持機構</strong></td>
<td>受容体・キナーゼ・足場タンパク質が入れ替わっても、何が記憶痕跡を保つかです。</td>
<td>記憶が残るなら、静的な分子 snapshot だけ保存すれば十分だ、と読むことです。</td>
<td>分子保持を主張せず、maintenance mechanism が未測定なら未測定と明記します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-cell-type-is-not-enough">
<h2 class="section-title">なぜ cell type だけでは不足するのか</h2>

<h3>1. transcriptomic type は morpho-electric phenotype を完全には固定しません</h3>
<p>
<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> は、mouse motor cortex の transcriptomic cell types が morpho-electric space の中で連続的な変動を持つことを示しました。これは、<strong>cell-type ラベルが分かっても、その場の電気生理パラメータまで一意に決まるわけではない</strong>ことを意味します。さらに <a href="https://doi.org/10.1038/nn1639" target="_blank">Schulz et al. (2006)</a> は、同定済みニューロンで ion channel mRNA と電流量に大きな個体差がありながら、機能はある程度保たれうることを示しました。したがって、connectome に cell-type ラベルを重ねても、<strong>threshold と gain の層</strong>はまだ残ります。
</p>

<h3>2. 維持されているのは「今の値」ではなく「戻り先」であることがあります</h3>
<p>
<a href="https://doi.org/10.1038/36103" target="_blank">Turrigiano et al. (1998)</a> は、慢性活動遮断や活動増加に対して neocortical neurons が quantal amplitude を bidirectionally scaling することを示しました。さらに <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a> は、activity-dependent な ion-channel expression の簡潔な生物物理モデルから、activity set point、cell type、compensation の関係が説明できることを示しました。<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> は、in vivo の視覚野で individual neuron が precise firing-rate set point へ戻ることを示しています。ここで重要なのは、<strong>snapshot としての活動値</strong>だけでなく、<strong>perturbation 後にどこへ戻るか</strong>という controller 側の状態が別変数だという点でございます。
</p>

<h3>3. 相対 excitability は将来の記憶配分を左右します</h3>
<p>
<a href="https://doi.org/10.1016/j.neuron.2014.07.017" target="_blank">Yiu et al. (2014)</a> は、学習前の相対的な neuronal excitability が、どのニューロンが memory trace に組み込まれやすいかを左右することを示しました。さらに <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2026)</a> は、neocortical engram neurons の early intrinsic excitability plasticity が memory formation と precision を規定することを示しています。したがって、<strong>connectome が同じでも excitability landscape が違えば、将来の学習経路と記憶配分は変わりえます</strong>。
</p>

<h3>4. 分子ターンオーバー下の記憶は、静的保存ではなく active maintenance として読むべきです</h3>
<p>
<a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">Lee et al. (2022)</a> は、シミュレーションと解析を通じて、synaptic memory が molecular turnover の下でも active な CaMKII state transfer により維持されうることを示しました。ここから直接言えるのは、「分子が入れ替わっても記憶が残ることはありうる」という点です。しかし逆に言えば、<strong>記憶の持続は静的分子 snapshot の十分性を意味せず、維持機構が働いていることを意味する</strong>と読む方が安全でございます。
</p>
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
<td><strong>平均 firing rate が戻ったので内部状態も同じに戻った</strong></td>
<td>同じ rate を別の conductance 組み合わせや別の controller で達成している可能性があります。</td>
<td>rate 回復だけで内部同一性を主張せず、perturbation と recovery のログを要求します。</td>
</tr>
<tr>
<td><strong>短期の活動予測が当たったので長期安定性も大丈夫だ</strong></td>
<td>長期では homeostatic plasticity と maintenance mechanism が効きます。</td>
<td>cross-day / cross-perturbation の held-out 劣化を出していない場合は強い主張へ上げません。</td>
</tr>
<tr>
<td><strong>記憶が長持ちするなら、保存すべき分子状態は静的だ</strong></td>
<td>持続はしばしば turnover をまたぐ active maintenance の結果です。</td>
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
<li><strong>長期 claim では maintenance-state を別列に出す：</strong>connectome / cell type / synapse と、intrinsic excitability / homeostasis を混ぜません。</li>
<li><strong>set point を測っていなければ測っていないと書く：</strong>activity snapshot から自動補完したことにはしません。</li>
<li><strong>memory persistence を static storage と言い換えない：</strong>turnover をまたぐ維持機構の可能性を先に残します。</li>
<li><strong>perturbation 後の recovery を重視する：</strong>何が起きたかだけでなく、どこへ戻るかをログに残します。</li>
<li><strong>proxy の限界を先に書く：</strong>EEG / pupil / behavior だけで excitability-homeostasis を一意に決めたとは書きません。</li>
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
<td>fixed model の劣化曲線、recovery time、state / trait / drift の切り分け、possible なら firing-rate distribution や excitability proxy。</td>
</tr>
<tr>
<td><strong>長期 memory / learning claim</strong></td>
<td>学習前後の perturbation 応答、relative excitability か allocation proxy、未測定 maintenance-state 一覧。</td>
</tr>
<tr>
<td><strong>state-complete reconstruction に近い claim</strong></td>
<td>connectome・cell type・synapse・delay・neuromodulation・glia に加え、intrinsic excitability / homeostasis をどこまで取得したか、あるいは latent として棄権したか。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>Schulz, D. J., Goaillard, J.-M., &amp; Marder, E. (2006). Variable channel expression in identified single and electrically coupled neurons in different animals. <em>Nature Neuroscience</em>, 9(3), 356-362. <a href="https://doi.org/10.1038/nn1639" target="_blank">doi:10.1038/nn1639</a></li>
<li>Turrigiano, G. G., Leslie, K. R., Desai, N. S., Rutherford, L. C., &amp; Nelson, S. B. (1998). Activity-dependent scaling of quantal amplitude in neocortical neurons. <em>Nature</em>, 391, 892-896. <a href="https://doi.org/10.1038/36103" target="_blank">doi:10.1038/36103</a></li>
<li>O'Leary, T., Williams, A. H., Franci, A., &amp; Marder, E. (2014). Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. <em>Neuron</em>, 82(4), 809-821. <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">doi:10.1016/j.neuron.2014.04.002</a></li>
<li>Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., &amp; Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <em>Cell</em>, 165(1), 180-191. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Yiu, A. P., et al. (2014). Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. <em>Neuron</em>, 83(3), 722-735. <a href="https://doi.org/10.1016/j.neuron.2014.07.017" target="_blank">doi:10.1016/j.neuron.2014.07.017</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Lee, J.-C., Wang, C.-Y., Lin, C.-L., &amp; Lu, H.-C. (2022). Synaptic memory survives molecular turnover. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 119(42), e2211572119. <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">doi:10.1073/pnas.2211572119</a></li>
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
