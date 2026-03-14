---
layout: default
title: "Wiki：意識理論マップ"
description: "IIT、GNWT、FEP、PCI、resting-state complexity、manifold geometry を、理論・摂動 benchmark・proxy・補助解析に分けて整理する技術ノートです。"
article_type: Wiki
subtitle: "理論名より先に、prediction family と benchmark layer を分ける"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Technical / natural science only"
audience: "IIT、GNWT、FEP、PCI、criticality の役割差で止まりやすい人"
reading_time: "12〜18分"
page_intro: "このページは、Mind-Upload で繰り返し出てくる意識理論と意識指標を、技術と自然科学の観点だけから整理する補助ページです。どれが真理かを決めるためではなく、何が prediction family で、何が perturbation benchmark で、何が spontaneous proxy や補助解析なのかを先に分けます。"
accuracy_note: "ここで示す使い分けは、各論文がそのまま宣言している結論ではありません。2026-03 時点の一次文献が比較的強く支持することと、なお残る未確定部分から本サイトが引く運用上の整理でございます。"
page_highlights:
  - "IIT、GNWT、FEP は theory family、PCI/PCI-ST は perturbation benchmark、criticality は spontaneous proxy、TDA は補助解析です。"
  - "Ferrante et al. (2025) 以後は、単一理論の勝敗より preregistered prediction competition の設計が重要です。"
  - "PCI は強い benchmark 候補ですが universal meter ではなく、criticality と geometry は外部較正つきの補助トラックです。"
known_points:
  - "理論名と測定指標を混ぜると、何が仮説で何が検証指標かが分からなくなります。"
  - "no-report / task-relevance / criterion placement の統制を外すと、理論マーカーの構成概念妥当性が崩れます。"
  - "摂動指標と自発指標はしばしば関連しますが、同一 cohort でも解離しうるため、置換関係としては扱えません。"
  - "manifold / topology 解析は有望ですが、sampling と前処理に敏感で、単独の合否指標にはなりません。"
unknown_points:
  - "どの理論 family が最終的に WBE の十分条件へ近いかは未確定です。"
  - "どの perturbation benchmark が altered states と disorders of consciousness を最も安定にまたぐかも未確定です。"
  - "spontaneous proxy と geometry descriptor を、どの条件で主要指標へ繰り上げられるかは未解決です。"
wiki_links:
  - label: "Wiki: 反事実・介入・摂動"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "理論マーカーを介入 benchmark へ落とす条件を整理します。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "観測適合と因果同定を混同しないためのページです。"
  - label: "Wiki: 文献と証拠ページの読み方"
    url: "/wiki/literature-and-evidence-reading.html"
    description: "理論論文と一次実験論文の役割差を整理します。"
recommended_pages:
  - label: "研究ノート"
    url: "/perspective.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "検証基盤"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>2026-03の短い結論</h2>
<p>
現時点の一次文献が比較的強く支持するのは、<strong>理論をそのまま採択すること</strong>ではなく、<strong>理論ごとの予測を事前登録して競わせること</strong>でございます。Ferrante らの adversarial collaboration は、IIT / GNWT / RPT のどれか 1 つを勝者にしませんでした。同時に、PCI / PCI-ST は強い perturbation benchmark 候補ですが universal meter ではなく、resting-state complexity / criticality は cohort ごとの較正が必要な proxy であり、manifold / topology 解析は補助的 descriptor に留まります。したがって本サイトでは、理論名を pass/fail 指標にせず、<strong>prediction family</strong>、<strong>perturbation benchmark</strong>、<strong>spontaneous proxy</strong>、<strong>supplementary geometry</strong> を分離して運用します。
</p>
</div>

<section class="section" id="roles">
<h2 class="section-title">まずは役割で分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>項目</th>
<th>何か</th>
<th>いま比較的強く言えること</th>
<th>このサイトでの扱い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT</strong></td>
<td>prediction family / consciousness theory です。</td>
<td>統合や因果構造に関する予測を与えますが、それ自体が engineering benchmark ではありません。</td>
<td><strong>予測生成器</strong>として扱い、単独の合否指標にはしません。</td>
</tr>
<tr>
<td><strong>GNWT</strong></td>
<td>prediction family / consciousness theory です。</td>
<td>広域共有や task relevance に関する予測を与えますが、report confound を強く受けます。</td>
<td><strong>予測生成器</strong>として扱い、no-report / criterion placement の統制を必須にします。</td>
</tr>
<tr>
<td><strong>FEP / Active Inference</strong></td>
<td>広い model family / control framework です。</td>
<td>生成モデルと制御を統一的に書けますが、単独で human consciousness benchmark の勝者になったわけではありません。</td>
<td><strong>候補実装族</strong>として扱い、DCM / state-space / SCM との同一ベンチ比較を前提にします。</td>
</tr>
<tr>
<td><strong>PCI / PCI-ST</strong></td>
<td>perturbation benchmark です。</td>
<td>TMS-EEG や intracranial stimulation に対する応答複雑性を比較的一貫して測れます。</td>
<td><strong>主 benchmark 候補</strong>として扱いますが、刺激条件とアーチファクト管理を必須にします。</td>
</tr>
<tr>
<td><strong>resting-state complexity / criticality</strong></td>
<td>spontaneous proxy です。</td>
<td>altered states や一部 cohort で PCI や意識状態と相関しますが、同一 cohort でも解離しえます。</td>
<td><strong>calibration track</strong>として扱い、PCI や行動評価の置換とはみなしません。</td>
</tr>
<tr>
<td><strong>manifold / topology / geometry</strong></td>
<td>supplementary descriptor です。</td>
<td>スカラー指標では落ちる構造差を補助的に見られますが、sampling・埋め込み・前処理に敏感です。</td>
<td><strong>補助解析</strong>として扱い、単独の pass/fail には使いません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="evidence-boundaries">
<h2 class="section-title">一次文献が切る境界</h2>
<table class="data-table">
<thead>
<tr>
<th>論点</th>
<th>一次文献が比較的強く支持すること</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>理論の勝敗</strong></td>
<td>Ferrante et al. (2025) は、IIT / GNWT / RPT の主要予測が部分的に支持されつつ、鍵予測のいくつかが反証されることを示しました。</td>
<td>単一理論を engineering default に昇格させることはできません。</td>
</tr>
<tr>
<td><strong>report / criterion confound</strong></td>
<td>Cohen et al. (2024) と Fahrenfort et al. (2025) は、post-perceptual processing や criterion placement が neural marker を大きく動かしうることを示しました。</td>
<td>report-dependent marker を、そのまま consciousness marker と同一視できません。</td>
</tr>
<tr>
<td><strong>PCI / PCI-ST</strong></td>
<td>Casali et al. (2013) と Comolatti et al. (2019) は、摂動応答複雑性を altered states をまたいで比較する benchmark を与えました。</td>
<td>刺激条件・artifact handling を外した PCI を universal meter のようには扱えません。</td>
</tr>
<tr>
<td><strong>spontaneous complexity / criticality</strong></td>
<td>Maschke et al. (2024) は麻酔下で spontaneous criticality と PCI の関連を示し、Casarotto et al. (2024) は minimally conscious state で spontaneous feature と PCI の解離を示しました。</td>
<td>resting-state proxy を PCI の置換指標として固定できません。</td>
</tr>
<tr>
<td><strong>manifold / topology</strong></td>
<td>Yoon et al. (2024) は cross-population で topology を比較する数学的土台を与え、iScience 2024 の V1 circular manifold 研究は truthful topology の回収に sampling 障害があることを示しました。</td>
<td>topology distance を consciousness structure の保証や WBE 合否指標へ直接は上げられません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Mind-Upload での使い方</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>理論名を pass/fail にしません：</strong>IIT / GNWT / FEP は prediction family として競わせます。</li>
<li><strong>PCI は perturbation benchmark と明記します：</strong>刺激条件、マスキング、artifact window、cohort を出さない場合は強い主張に使いません。</li>
<li><strong>自発指標は較正してから使います：</strong>criticality、Lempel-Ziv、wSMI などは PCI や行動評価との外部較正を前提にします。</li>
<li><strong>geometry は補助解析です：</strong>TDA や manifold distance は、sampling / preprocessing 感度分析を通った場合だけ補助的に報告します。</li>
<li><strong>no-report と criterion placement を先に固定します：</strong>この統制がない場合、理論差より task/report confound を見ている可能性が残ります。</li>
</ul>
</div>

<div class="note-box">
<strong>技術ページへ戻すときの読み替え</strong>
<p>
<a href="../tech_roadmap.html">技術ロードマップ</a> では V6 を theory competition と benchmark hierarchy の問題として読み、<a href="../verification.html">検証基盤</a> では perturbation benchmark、OOD、long-run stability、abstention を束で確認します。つまり、このページは「どの理論が正しいか」を決めるためより、「どの種類の evidence をどの強さで扱うか」をそろえるための地図でございます。
</p>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Ferrante O, et al. Adversarial testing of global neuronal workspace and integrated information theories of consciousness. <em>Nature</em>. 2025. <a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">doi:10.1038/s41586-025-08888-1</a></li>
<li>Cohen MA, et al. Neural signatures of visual awareness independent of postperceptual processing. <em>Cerebral Cortex</em>. 2024. <a href="https://doi.org/10.1093/cercor/bhae415" target="_blank">doi:10.1093/cercor/bhae415</a></li>
<li>Fahrenfort JJ, et al. Criterion placement threatens the construct validity of neural measures of conscious contents. <em>Nature Neuroscience</em>. 2025. <a href="https://doi.org/10.1038/s41593-025-02009-x" target="_blank">doi:10.1038/s41593-025-02009-x</a></li>
<li>Casali AG, et al. A theoretically based index of consciousness independent of sensory processing and behavior. <em>Science Translational Medicine</em>. 2013. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Comolatti R, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. <em>Brain Stimulation</em>. 2019. <a href="https://doi.org/10.1016/j.brs.2019.05.013" target="_blank">doi:10.1016/j.brs.2019.05.013</a></li>
<li>Maschke C, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. <em>Communications Biology</em>. 2024. <a href="https://doi.org/10.1038/s42003-024-06613-8" target="_blank">doi:10.1038/s42003-024-06613-8</a></li>
<li>Casarotto S, et al. Dissociations between spontaneous electroencephalographic features and perturbational complexity index in the minimally conscious state. <em>Brain</em>. 2024. <a href="https://doi.org/10.1093/brain/awae227" target="_blank">doi:10.1093/brain/awae227</a></li>
<li>Yoon B, Miolane N, Osting B, Linderman SW. Tracking the topology of neural manifolds across populations. <em>PNAS</em>. 2024. <a href="https://doi.org/10.1073/pnas.2402628121" target="_blank">doi:10.1073/pnas.2402628121</a></li>
<li>The topological structure of population activity in mouse visual cortex encodes visual stimuli. <em>iScience</em>. 2024. <a href="https://doi.org/10.1016/j.isci.2024.111613" target="_blank">doi:10.1016/j.isci.2024.111613</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>このページで固定すること</h4>
<ul>
<li>theory family と benchmark layer の区別</li>
<li>PCI と spontaneous proxy の役割差</li>
<li>geometry / topology の扱い方</li>
</ul>
</div>
<div class="sidebar-box">
<h4>戻り先</h4>
<ul>
<li><a href="../perspective.html">研究ノート →</a></li>
<li><a href="../tech_roadmap.html">技術ロードマップ →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
