---
layout: default
title: "Wiki：計測からモデル化までの用語ガイド"
description: "EEG、QC、BIDS、ESI、connectivity、DCM、SCM、Observability Budget / Fusion Card / Temporal Validity Card / Calibration & Abstention Card を、direct / proxy / inferred / deployable の境界つきで説明します。"
article_type: Wiki
subtitle: "detectable と identified を混同しない"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Learning guide"
audience: "計測語とモデル語が混ざって見える人、主張の強さを段階つきで読みたい人"
reading_time: "12〜18分"
page_intro: "このページは、EEG のような計測語、ESI や DCM のようなモデル語、BIDS や QC のような運用語を『観測→整理→推定→妥当化→運用』の流れでつなげて理解するための wiki です。単語を個別に暗記するより、どの段階で主張が 1 段強くなるかを先に分けることを目的にします。"
accuracy_note: "ここで示す流れは理解のための整理です。実際の研究では往復や例外がありますが、detectability、localization、identifiability、direct validation、deployability を混同しないことは崩しません。"
page_highlights:
  - "EEG、QC、BIDS、ESI、connectivity、DCM、SCM、site-wide の提出物仕様を 1 本の流れで理解できます。"
  - "direct / proxy / inferred / deployable を、detectability / localization / identifiability / validation と混ぜずに切り分けます。"
  - "Observability Budget、Fusion Card、latent-state error budget、Temporal Validity Card、Calibration & Abstention Card が、どの段階の失敗モードを止めるかを結び付けます。"
  - "connectivity claim は localization の次の段であり、source mixing や ghost interaction の別監査が要ると分かります。"
known_points:
  - "計測、前処理、推定、妥当化、運用は役割が違い、それぞれ別の言葉が使われます。"
  - "観測段階でも、direct measurement、proxy、model-dependent inference、operational deployability は別です。"
  - "観測信号はそのまま脳内状態ではなく、推定には不確実性、候補モデル依存性、parameter degeneracy が伴います。"
  - "fMRI / BOLD や SV2A PET のような proxy では、neural hidden state に加えて measurement-side hidden state も残ります。"
  - "BIDS、QC、calibration、abstention はおまけではなく、比較可能性と deployability を支える要素です。"
unknown_points:
  - "非侵襲計測だけで WBE に十分な内部状態をどこまで復元できるかは未解決です。"
  - "どのモデル化の組み合わせが最終的に最も有効かは、まだ研究途中です。"
  - "校正・棄権・再較正負荷の共通 pass/fail を、どこまで site-wide に固定できるかも未解決です。"
wiki_links:
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "計測の入口として、EEG が何を測るかを確認できます。"
  - label: "Wiki: EEG前処理とQC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "整理段階で何が結果を変えるかを補います。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "観測、ESI、DCM、SCM、因果同値類を詳しく補います。"
  - label: "Wiki: 不確実性・校正・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "confidence と calibration、abstention、recalibration burden を詳しく補います。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "最後の検証段階で何を固定するかを補います。"
recommended_pages:
  - label: "用語集"
    url: "/glossary.html"
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "検証基盤"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い地図</h2>
<p>
このサイトで出る言葉は、大きく分けると 5 段階です。<strong>観測する</strong>、<strong>整える</strong>、<strong>推定する</strong>、<strong>外から確かめる</strong>、<strong>長く運用できるかを見る</strong>、でございます。単語が難しく見えても、「今どの段階の話か」を先に分けると混乱が減ります。
</p>
</div>

<div class="note-box">
<strong>2026-03 の更新点</strong>
<p>
今回の更新では、最近の公開ページで強化した境界を、この補助ページにも下ろしました。特に <strong>detectability / localization / identifiability / direct validation / deployability</strong> を 1 列で読めるようにしつつ、<strong>direct / proxy / inferred / deployable</strong> も別の軸として明示しました。さらに、この 5 段階を <a href="../verification.html#observability-budget">Observability Budget</a>、<a href="../verification.html#fusion-card">Fusion Card</a>、<a href="../verification.html#latent-state-error-budget">latent-state error budget</a>、<a href="../verification.html#temporal-validity-card">Temporal Validity Card</a>、<a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> へ対応づけ、学習ガイドと site-wide 提出物仕様のずれを埋めました。
</p>
</div>

<section class="section" id="five-steps">
<h2 class="section-title">5段階で見る</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>ここで出やすい言葉</th>
<th>何をしているか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 観測</strong></td>
<td>EEG, MEG, fMRI, ECoG, SV2A PET, observability budget, claim ceiling</td>
<td>脳や身体から外に出てくる信号を測り、「何が direct で何が proxy か」「何がまだ latent か」を固定します。</td>
</tr>
<tr>
<td><strong>2. 整理</strong></td>
<td>QC, 前処理, 参照法, BIDS, event log</td>
<td>ノイズ、参照、同期、欠損、注釈 provenance を残し、他人が追える形へそろえます。</td>
</tr>
<tr>
<td><strong>3. 推定</strong></td>
<td>detectability, localization, connectivity, identifiability, ESI, DCM, SCM, latent-state error budget, Fusion Card</td>
<td>観測から、どこまで source、回路、因果構造を推定できるかと、どの latent state / transfer assumption が残るかを段階つきで考えます。</td>
</tr>
<tr>
<td><strong>4. 妥当化</strong></td>
<td>direct validation, family comparison, held-out perturbation, Intervention Card, benchmark</td>
<td>その推定やモデルを、外部 ground truth や介入、候補モデル比較で確かめます。</td>
</tr>
<tr>
<td><strong>5. 運用</strong></td>
<td>Temporal Validity Card, Calibration &amp; Abstention Card, calibration, coverage, abstention, tail latency, recalibration burden</td>
<td>精度が高いだけでなく、低信頼時に止まれるか、何日・何状態まで持つか、長期に使えるかを測ります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="card-map">
<h2 class="section-title">5段階と site-wide 提出物の対応</h2>
<p>
今回この補助ページで最も改善すべきだった弱点は、<strong>段階の説明</strong>はあっても、公開サイトが実際に要求する <strong>提出物仕様</strong> へまだ十分につながっていなかった点でございます。これでは、同じ「見えた」「当たった」「使えた」という言葉の中に、measurement ceiling、latent-state ceiling、介入妥当化、縦断妥当化、confidence semantics が混ざります。そこで以下の対応表を追加し、どの段階でどの card が誤読を止めるかを明示します。
</p>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>いちばん先に答える問い</th>
<th>このサイトで主に対応する提出物</th>
<th>ここで止める誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測</strong></td>
<td>何が direct で、何が proxy で、何が未観測か。</td>
<td><a href="../verification.html#observability-budget">Observability Budget</a></td>
<td><code>multimodal だから全部見えた</code>、<code>proxy だから neural truth</code> を止めます。</td>
</tr>
<tr>
<td><strong>整理</strong></td>
<td>何を除き、何を残し、同期と provenance をどう固定したか。</td>
<td>QC log / BIDS / event-sync log</td>
<td><code>前処理は見栄え調整</code>、<code>同期は細部</code> を止めます。</td>
</tr>
<tr>
<td><strong>推定</strong></td>
<td>どの latent state と transfer assumption がなお残るか。</td>
<td><a href="../verification.html#latent-state-error-budget">latent-state error budget</a> / <a href="../verification.html#fusion-card">Fusion Card</a></td>
<td><code>fit したから mechanism も分かった</code>、<code>統合したから真相に近い</code> を止めます。</td>
</tr>
<tr>
<td><strong>妥当化</strong></td>
<td>外部基準や介入で、どこまで候補モデルを狭めたか。</td>
<td><a href="../verification.html#intervention-card">Intervention Card</a> / family comparison / benchmark log</td>
<td><code>localized だから causal</code>、<code>1 回の positive result で validated</code> を止めます。</td>
</tr>
<tr>
<td><strong>運用</strong></td>
<td>何日・何状態・どの低信頼条件まで外挿できるか。</td>
<td><a href="../verification.html#temporal-validity-card">Temporal Validity Card</a> / <a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a></td>
<td><code>same-day high score = chronic deployable</code>、<code>high confidence = safe</code> を止めます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="observation">
<h2 class="section-title">1. 観測: まず信号を取る</h2>
<p>
EEG や MEG は、脳の中を直接見ているのではなく、外から観測できる信号を測っています。ここで大事なのは、<strong>観測したものと、脳内で本当に起きていることは同じではない</strong>という点です。最初に必要なのは「どこまで直接見えているか」の上限を決めることでございます。
</p>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ひとことで言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>頭皮上の電位差を高速に測る方法です。時間変化に強い一方、空間的にはぼやけやすく、導電率仮定にも依存します。</td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>磁場を測る方法です。EEG と補完関係がありますが、高価で装置制約が大きいです。</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>血流変化を測る方法です。位置には強いですが、時間分解能は遅いです。</td>
</tr>
<tr>
<td><strong>ECoG / SEEG</strong></td>
<td>侵襲計測です。高精度ですが、適用範囲に強い制約があります。</td>
</tr>
<tr>
<td><strong>Observability Budget</strong></td>
<td>その measurement stack で、何が直接見えて何が latent のまま残るかを先に固定する考え方です。</td>
</tr>
<tr>
<td><strong>Claim Ceiling</strong></td>
<td>その計測から無理なく言える主張の上限です。多モーダル化しても state-complete と自動では読みません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>ここで止めるべき誤読</strong>
<p>
Seeber et al. (2019) は high-density EEG で deep activity が <strong>detectable</strong> になりうることを示しましたが、これは deep source の一般的一意復元を意味しません。Aydin et al. (2019) が示したように、頭部導電率の不確かさだけでも推定は動きます。したがって観測段階では、まず <strong>observability budget</strong> と <strong>claim ceiling</strong> を書きます。
</p>
</div>
</section>

<section class="section" id="direct-proxy-inferred">
<h2 class="section-title">direct / proxy / inferred / deployable を同じ『見えた』にしない</h2>
<p>
技術・自然科学の観点で今回もっとも改善すべきだった弱点は、この補助ページが <strong>「見えた」</strong> を広く使いすぎ、<strong>sensor signal を直接観測した</strong>、<strong>proxy を得た</strong>、<strong>モデル依存で推定した</strong>、<strong>長期運用できた</strong> を 1 列に見せやすかった点でございます。一次文献を並べると、少なくとも以下の 4 層は分ける必要があります。
</p>
<table class="data-table">
<thead>
<tr>
<th>route</th>
<th>direct に取れているもの</th>
<th>proxy / inferred に留まるもの</th>
<th>このサイトで別に要求するもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG</strong></td>
<td>頭皮上の電位差や磁場、その時間変化です。</td>
<td>source localization、connectivity、因果機序は forward / inverse model と候補モデル族に依存します。</td>
<td><a href="../verification.html#observability-budget">Observability Budget</a> と不確実性の公開が必要です。</td>
</tr>
<tr>
<td><strong>fMRI / BOLD</strong></td>
<td>血行動態 signal と領域スケールの遅い network state です。</td>
<td>neural explanation は HRF、vascular state / CVR、venous geometry を介した proxy に留まります。</td>
<td><a href="../verification.html#fusion-card">Fusion Card</a> と hemodynamic transfer の監査が必要です。</td>
</tr>
<tr>
<td><strong>SV2A PET</strong></td>
<td>tracer uptake と kinetic model に基づく regional SV2A binding です。</td>
<td>regional presynaptic-density proxy までは言えますが、current synaptic efficacy や postsynaptic receptor occupancy は残ります。</td>
<td><a href="../verification.html#observability-budget">Observability Budget</a> で proxy class を固定します。</td>
</tr>
<tr>
<td><strong>chronic extracellular probe</strong></td>
<td>implant 近傍の waveform、threshold crossing、local population activity です。</td>
<td>stable unit identity across days、long-term deployability、recalibration-light 運用は sorting / drift / matching / recalibration を介した別問題です。</td>
<td><a href="../verification.html#temporal-validity-card">Temporal Validity Card</a> と drift audit が必要です。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>一次文献が切る境界</strong>
<p>
<a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019)</a> は deep activity の <strong>detectability</strong> を、<a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">Aydin et al. (2019)</a> は conductivity uncertainty の影響を、<a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> と <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> は BOLD の measurement-side hidden state を、<a href="https://doi.org/10.1126/scitranslmed.aaf6667" target="_blank">Finnema et al. (2016)</a>、<a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a>、<a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> は human in vivo の synaptic-density proxy route を、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> は long-term deployability と recalibration burden の壁を示しました。したがって本サイトでは、<strong>direct signal</strong>、<strong>proxy</strong>、<strong>model-dependent inference</strong>、<strong>operational evidence</strong> を同じ「見えた」で済ませません。
</p>
</div>
</section>

<section class="section" id="cleanup">
<h2 class="section-title">2. 整理: 信号をそのまま信じない</h2>
<p>
観測した信号には、まばたき、筋電、体動、機器ノイズなどが混ざります。そのため、次に必要なのが QC と前処理です。ここは見栄えを整える作業ではなく、<strong>どの情報を残し、何を除いたかを記録する作業</strong>です。
</p>
<div class="key-points">
<h4>ここで出る言葉</h4>
<ul>
<li><strong>QC：</strong>欠損、ノイズ、アーティファクト、除外理由を数値で残します。</li>
<li><strong>前処理：</strong>参照法、フィルタ、artifact suppression、bad segment の扱いを固定します。</li>
<li><strong>同期ログ：</strong>latency、jitter、marker provenance、annotation provenance を別に残します。</li>
<li><strong>BIDS：</strong>データとメタデータを他人が追える形でそろえる規格です。</li>
</ul>
</div>
<p>
この段階を飛ばすと、あとで高性能なモデルが出てきても、比較可能な証拠にはなりません。
</p>
<div class="note-box">
<strong>前処理は connectivity claim の前提です</strong>
<p>
lagged metric や directed metric を後段で使うとしても、reference choice、artifact suppression、time sync が曖昧なら、後段の network claim は比較不能です。connectivity を語る前に、まず整理段階のログを固定します。
</p>
</div>
</section>

<section class="section" id="estimation">
<h2 class="section-title">3. 推定: 観測から中身をどこまで言えるか</h2>
<p>
整理した信号をもとに、脳内の活動や因果構造を推定したくなります。ここで出てくるのが、逆問題、ESI、connectivity、DCM、SCM です。ただし、この段階では<strong>推定は推定であり、不確実性と候補モデル依存性が残る</strong>ことを忘れてはいけません。
</p>
<table class="data-table">
<thead>
<tr>
<th>主張の段</th>
<th>何が言えるか</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Detectability</strong></td>
<td>source や条件差の存在を見つけられるかです。</td>
<td>どこから来たか、唯一の機序か、介入で再現するかはまだ言えません。</td>
</tr>
<tr>
<td><strong>Localization</strong></td>
<td>推定 source を空間的にどこへ置くかです。</td>
<td>candidate model family の唯一性や causal mechanism まではまだ言えません。</td>
</tr>
<tr>
<td><strong>Connectivity</strong></td>
<td>source 間の coupling を要約します。functional と directed で要求仮定が異なります。</td>
<td>lagged metric や directed metric を使っても、ghost interaction や causal identification が消えたとは言えません。</td>
</tr>
<tr>
<td><strong>Identifiability</strong></td>
<td>代替モデル族をどこまで除外できるかです。</td>
<td>観測データだけでは Markov equivalence class が残ることが多く、介入や family comparison が要ります。</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>役割</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>逆問題</strong></td>
<td>外から見えた信号から中の原因を推定する問題です。一般に 1 つに決まりません。</td>
</tr>
<tr>
<td><strong>ESI</strong></td>
<td>EEG から脳内ソースを推定する枠組みです。点推定だけでなく、不確実性も報告する必要があります。</td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>候補生成モデルを比較し、どの結合構造が data を説明しやすいかをみる枠組みです。Bayes factor や family comparison が中心です。</td>
</tr>
<tr>
<td><strong>SCM</strong></td>
<td>因果関係を明示して、介入や反事実を扱いやすくするモデルです。観測だけでは equivalence class が残りやすいです。</td>
</tr>
<tr>
<td><strong>Parameter Degeneracy</strong></td>
<td>異なる内部パラメータ群が、ほぼ同じ出力を作れてしまうことです。出力一致だけで唯一の機序とは言えません。</td>
</tr>
<tr>
<td><strong>Ghost Interaction</strong></td>
<td>source reconstruction 後にも残りうる見かけの coupling です。network claim の過大解釈を防ぐ警告語です。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>ここで起きやすいすり替え</strong>
<p>
EEG を観測したことと、脳内状態を一意に再構成したことは同じではありません。さらに、source localization が通ったことと、connectivity や因果構造まで分かったことも同じではありません。
</p>
</div>

<div class="note-box">
<strong>2026-03 の補足</strong>
<p>
Mikulan et al. (2020)、Unnwongse et al. (2023)、Hao et al. (2025) が前進させたのは、ESI の <strong>direct validation route</strong> であって、内部状態の一般的一意復元ではありません。さらに Haufe et al. (2013) と Palva et al. (2018) は、connectivity claim が source mixing と ghost interaction に敏感であることを示しました。詳しくは <a href="observation-to-estimation.html">Wiki: 観測から推定へ</a> をご覧ください。
</p>
</div>
</section>

<section class="section" id="validation">
<h2 class="section-title">4. 妥当化: 推定をどう信用するか</h2>
<p>
次に必要なのは、「この推定やモデルを、外部 ground truth や介入でどこまで確かめたか」です。ここで Direct Validation、Family Comparison、Held-out Perturbation、Benchmark のような言葉が出てきます。
</p>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>何のために要るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Direct Validation</strong></td>
<td>SEEG、intracranial stimulation、同時記録などの外部 ground truth と照合します。</td>
</tr>
<tr>
<td><strong>Family Comparison</strong></td>
<td>DCM などで単一モデルではなく候補モデル族を比較し、構造仮説の相対強度を見ます。</td>
</tr>
<tr>
<td><strong>Held-out Perturbation</strong></td>
<td>観測に合うだけでなく、未学習の条件変更や介入応答を当てられるかを見ます。</td>
</tr>
<tr>
<td><strong>Benchmark / Baseline / Preregistration / Model Card</strong></td>
<td>比較条件、出発点、事前ルール、失敗例を固定し、後付けの強化を防ぎます。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>connectivity の妥当化は localization より一段厳しいです</strong>
<p>
Penny et al. (2004) が示すように DCM は候補構造の比較です。Hauser &amp; Bühlmann (2012) が示すように、介入は identifiability を細かくします。Vink et al. (2020) は resting-state EEG functional connectivity が causal interaction の弱い予測子にとどまることを示しました。したがって、本サイトでは <strong>fit</strong> をそのまま <strong>causal validation</strong> と読み替えません。
</p>
</div>
</section>

<section class="section" id="deployment">
<h2 class="section-title">5. 運用: 使い続けられるかをどう見るか</h2>
<p>
最後に必要なのは、「その推定や decoder が、低信頼条件で止まり、長期 drift の中でも使い続けられるか」です。ここでは accuracy よりも、<strong>confidence と calibration の差</strong>、<strong>coverage と risk の交換</strong>、<strong>recalibration burden</strong> が重要になります。
</p>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>何を見るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Calibration</strong></td>
<td>confidence が実際の頻度と合っているかです。高 confidence でも miscalibrated なら危険です。</td>
</tr>
<tr>
<td><strong>Coverage</strong></td>
<td>モデルが判定を返した割合です。棄権と組で見ます。</td>
</tr>
<tr>
<td><strong>Abstention</strong></td>
<td>低信頼時に「分からない」と返せるかです。過信を減らす安全弁です。</td>
</tr>
<tr>
<td><strong>Tail Latency</strong></td>
<td>P95 / P99 の遅延です。平均 latency だけでは closed loop の安全性は読めません。</td>
</tr>
<tr>
<td><strong>Recalibration Burden</strong></td>
<td>使い続けるためにどれだけ再較正が必要かです。臨床運用の大きな壁です。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>精度が高いだけでは deployable ではありません</strong>
<p>
Segal et al. (2023) は EEG seizure prediction で calibration により false alarm rate を制御できることを示し、Wilson et al. (2025) は intracortical BCI で long-term unsupervised recalibration が主要ボトルネックであることを示しました。したがって本サイトでは、<strong>high accuracy = deployable</strong> とは書かず、calibration、abstention、tail latency、recalibration burden を別指標で残します。
</p>
</div>
<div class="note-box">
<strong>このサイトでは運用段階を 2 枚の card に分けます</strong>
<p>
<a href="../verification.html#temporal-validity-card">Temporal Validity Card</a> は <strong>何日・何状態・何回の再較正まで外挿できるか</strong> を固定し、<a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> は <strong>confidence / interval / set / fallback の意味</strong> を固定します。片方だけでは、<strong>validity horizon</strong> と <strong>reliability semantics</strong> が混ざります。
</p>
</div>
</section>

<section class="section" id="rules">
<h2 class="section-title">このページから持ち帰る 7 つの site rule</h2>
<div class="key-points">
<h4>読み替え禁止の最短版</h4>
<ul>
<li><strong>direct signal ≠ neural truth：</strong>sensor で直接測れたものと、脳内状態の意味づけは別です。</li>
<li><strong>proxy ≠ identified state：</strong>BOLD や SV2A PET は有力でも、proxy class を超えて読みません。</li>
<li><strong>detectable ≠ localized：</strong>見えたことと、どこから来たかは別です。</li>
<li><strong>localized ≠ identified：</strong>source を置けても、唯一の内部機序とは限りません。</li>
<li><strong>connectivity ≠ causality solved：</strong>network metric は別監査を要します。</li>
<li><strong>fit ≠ validated：</strong>外部 ground truth、family comparison、介入が要ります。</li>
<li><strong>accurate ≠ deployable：</strong>calibration、abstention、recalibration burden を別に出します。</li>
</ul>
</div>
</section>

<section class="section" id="boundary">
<h2 class="section-title">この流れで何が分かり、何がまだ分からないか</h2>
<table class="data-table">
<thead>
<tr>
<th>分かること</th>
<th>まだ分からないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>用語が、どの段階の仕事に属するか。</td>
<td>どのモデルが最終的に意識や本人性を十分に説明するか。</td>
</tr>
<tr>
<td>観測、推定、妥当化、運用を混同しない読み方。</td>
<td>非侵襲計測だけで WBE に十分な情報を取れるかどうか。</td>
</tr>
<tr>
<td>BIDS、QC、calibration、abstention がなぜ技術の外側ではなく中身なのか。</td>
<td>どのマルチモーダル統合と介入設計の組み合わせが最終的に最良か。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Aydin, U., Vorwerk, J., Küpper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Mikulan, E., Russo, S., Parmigiani, S., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., Lebel, R. M., MacDonald, M. E., &amp; Pike, G. B. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Finnema, S. J., Nabulsi, N. B., Eid, T., et al. (2016). Imaging synaptic density in the living human brain. <a href="https://doi.org/10.1126/scitranslmed.aaf6667" target="_blank">doi:10.1126/scitranslmed.aaf6667</a></li>
<li>Naganawa, M., Nabulsi, N., Lin, S.-F., et al. (2021). First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">doi:10.2967/jnumed.120.249144</a></li>
<li>Johansen, A., et al. (2024). An in vivo high-resolution human brain atlas of synaptic density. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Haufe, S., Nikulin, V. V., Müller, K.-R., &amp; Nolte, G. (2013). A critical assessment of connectivity measures for EEG data: a simulation study. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva, J. M., Wang, S. H., Palva, S., et al. (2018). Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Hauser, A., &amp; Bühlmann, P. (2012). Characterization and Greedy Learning of Interventional Markov Equivalence Classes of Directed Acyclic Graphs. <a href="https://jmlr.csail.mit.edu/papers/v13/hauser12a.html" target="_blank">JMLR 13:2409-2464</a></li>
<li>Vink, J. J. T., Klooster, D. C. W., Ozdemir, R. A., et al. (2020). EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">doi:10.1007/s10548-020-00757-6</a></li>
<li>Segal, G., Keidar, N., Lotan, R. M., et al. (2023). Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">doi:10.3389/fnins.2023.1184990</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Prinz, A. A., Bucher, D., &amp; Marder, E. (2004). Similar network activity from disparate circuit parameters. <a href="https://doi.org/10.1038/nn1352" target="_blank">doi:10.1038/nn1352</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
短い定義へ戻るなら <a href="../glossary.html">用語集</a>、EEG の役割をもう一度読むなら <a href="../eeg_101.html">EEG入門</a>、比較可能な検証へ進むなら <a href="../verification.html">検証基盤</a>、観測と推定の違いをさらに詰めるなら <a href="observation-to-estimation.html">Wiki: 観測から推定へ</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-basics.html">EEGの基本 →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG前処理とQC →</a></li>
<li><a href="observation-to-estimation.html">観測から推定へ →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">不確実性・校正・棄権 →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../glossary.html">用語集 →</a></li>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
