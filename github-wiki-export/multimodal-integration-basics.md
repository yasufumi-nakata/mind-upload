# Wiki：マルチモーダル統合の基本

> multimodal は 1 種類ではなく、取得関係ごとに claim ceiling が違います
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-16 / 位置づけ: Technical / natural science only

## このページの役割
このページは、EEG、MEG、fMRI、侵襲記録、MRI、atlas prior を組み合わせるとき、何が直接観測で何が依然として推定かを整理する wiki です。哲学や法制度ではなく、取得関係、共有時計、幾何、融合モデル、外部妥当化、state coverage だけに絞ります。

## 正確さの前提
ここで示す claim ceiling は、各論文がそのまま宣言している最終結論ではありません。一次文献が直接与える観測量と、依然として未観測の状態変数から本サイトが引く運用上の推論でございます。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: EEGの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - まず EEG 単体の限界へ戻りたいときはこちらです。
- [Wiki: イベント同期と観測ログ](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - 共有時計、遅延、ジッタ、ドリフトの基本を補います。
- [Wiki: 観測から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 観測値と推定値を混同しないための入口です。
- [Wiki: 計測スタックごとの observability と claim ceiling](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling) - stack ごとの直接観測量と主張上限へ戻れます。

## いま分かっていること
- 複数モダリティを組み合わせると、時間・空間・局所性・外部妥当化の一部は補完できます。
- ただし改善量は、取得関係、共有時計、個体別解剖、co-registration、融合モデル、外部基準の有無に強く依存します。
- fMRI を含む統合では、shared clock があっても BOLD を direct neural truth とは読めません。
- 侵襲記録は強い calibration route ですが、coverage bias と patient bias を抱えます。
- atlas や Patch-seq は強い prior を与えますが、current state を直接観測したことにはなりません。
- same-brain structure-function data は局所 conditional prediction を押し上げますが、all-state / whole-brain completeness とは別問題です。

## まだ分かっていないこと
- どの統合セットが WBE のどの段階に最も効くかは、まだ固定できません。
- 複数モダリティを統合しても、細胞・シナプス・神経修飾・グリア状態の十分性は未解決です。
- 統合後の不確実性をどう伝播・比較可能な形で報告するかも、まだ整備途上です。

---

<h2>結論</h2>
<p>
今回もっとも深く修正すべきだった弱点は、<strong>multimodal</strong> という 1 語の中に、<strong>同時取得</strong>、<strong>同一個体の幾何統合</strong>、<strong>coverage-limited な侵襲校正</strong>、<strong>atlas / Patch-seq による prior 付与</strong>が混在していた点でございます。これらは全部「複数モダリティ」ですが、直接追加される証拠が違います。したがって本サイトでは、モダリティ名の足し算ではなく、<strong>取得関係</strong>と<strong>外部妥当化の型</strong>ごとに claim ceiling を固定します。
</p>

<strong>このページの範囲</strong>
<p>
ここでは、技術と自然科学の側面だけを扱います。本人性、意識、法制度は扱いません。問うのは、「何を何に結び付けたか」と「その結果どこまでなら強く言えるか」でございます。
</p>

<h2>今回深掘りする弱点</h2>
<p>
従来の公開ページは、EEG+fMRI、EEG+MEG、EEG+侵襲記録などの代表例を正しく挙げていました。しかし、<strong>同時取得して共有時計を持つ統合</strong>と、<strong>後から同一個体の geometry を足す統合</strong>と、<strong>別個体 atlas を prior として入れる統合</strong>を、まだ十分に分離できていませんでした。
</p>
<p>
この混同は科学的に不利でございます。<a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019)</a> が示す EEG-BIDS は modality-specific metadata の器を与え、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">Kothe et al. (2025)</a> は共有時計を支える LSL が device-side delay の真値までは自動で与えないことを示し、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Burns et al. (2024)</a> は multimodal motion metadata を BIDS に埋め込む必要を示しました。つまり、<strong>「複数モダリティを使った」</strong>だけでは、共有時計も、登録精度も、融合後の不確実性も固定されません。
</p>

<h2>multimodal を 4 種類の取得関係へ分けます</h2>

<strong>最後の列は本サイトの運用推論です</strong>
<p>
下の <strong>claim ceiling</strong> は、各論文のタイトルそのものではなく、一次文献が直接与える観測量と依然として残る latent state から、本サイトが引く境界でございます。
</p>

<table>
<thead>
<tr>
<th>取得関係</th>
<th>何が直接足されるか</th>
<th>代表例</th>
<th>このサイトでの claim ceiling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 同時取得 + 共有時計</strong></td>
<td>trial-level の時間整合、cross-modal latency の監査、同一時点の共変動です。</td>
<td>同時計測 EEG-fMRI、EEG-ECoG、EEG-SEEG、LSL で束ねた multimodal recording です。</td>
<td><strong>同期つきの macro/local concordance まで</strong>です。clock validation が無ければ trial-level 因果順序は強く書きません。</td>
</tr>
<tr>
<td><strong>2. 同一個体だが非同時の幾何統合</strong></td>
<td>個体別解剖、電極/センサー位置、forward model、conductivity calibration です。</td>
<td>EEG + MRI、EEG + MEG、EEG + head model 校正です。</td>
<td><strong>幾何つき localization の改善まで</strong>です。同時性が無ければ trial-level state alignment とは書きません。</td>
</tr>
<tr>
<td><strong>3. coverage-limited な侵襲校正</strong></td>
<td>implant 近傍や刺激既知部位に対する外部妥当化です。</td>
<td>intracranial stimulation + HD-EEG、同時 scalp EEG/ECoG、同時 HD-EEG/SEEG、DBS 同時計測です。</td>
<td><strong>局所 detectability / localization の直接妥当化まで</strong>です。未計測領域を含む whole-brain ground truth には上げません。</td>
</tr>
<tr>
<td><strong>4. atlas / bridge / prior 付与</strong></td>
<td>cell-type、morphology、same-brain local structure-function link、transcriptomic prior です。</td>
<td>whole-brain atlas、Patch-seq bridge、MICrONS、predicted transcriptomic type の connectomics です。</td>
<td><strong>molecular / structural prior と local functional twin まで</strong>です。current state や human whole-brain state-complete とは書きません。</td>
</tr>
</tbody>
</table>

<h2>統合の前に固定する 6 つの監査ゲート</h2>
<table>
<thead>
<tr>
<th>ゲート</th>
<th>最低限ほしいもの</th>
<th>足りないと止まる主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1: 取得関係</strong></td>
<td>同時取得か、同一個体の非同時計測か、別個体 atlas prior かを明示します。</td>
<td>multimodal という語だけで、同一時点比較や same-brain claim をすることです。</td>
</tr>
<tr>
<td><strong>Gate 2: 共有時計と遅延監査</strong></td>
<td>clock domain、offset、delay、jitter、drift、validation method を残します。</td>
<td>trial-level の phase relation、causal order、closed-loop timing を強く言うことです。</td>
</tr>
<tr>
<td><strong>Gate 3: 幾何と登録</strong></td>
<td>個体別 MRI、電極/センサー位置、co-registration、forward model、conductivity 仮定を残します。</td>
<td>「どこで起きたか」を一般化して断言することです。</td>
</tr>
<tr>
<td><strong>Gate 4: 融合モデルと不確実性</strong></td>
<td>late fusion か shared latent model か、重み付け、事後分布、感度分析を公開します。</td>
<td>fused map を直接観測の真値として扱うことです。</td>
</tr>
<tr>
<td><strong>Gate 5: 外部妥当化</strong></td>
<td>ファントム、同時侵襲記録、頭蓋内刺激、術後転帰、same-brain co-registration などを示します。</td>
<td>見た目の改善や相関上昇だけで「局在が改善した」と書くことです。</td>
</tr>
<tr>
<td><strong>Gate 6: state coverage</strong></td>
<td>今回の統合で何を still latent に残したかを、cell type、synaptic efficacy、neuromodulation、glia、sleep-history 単位で書きます。</td>
<td>統合しただけで WBE に十分な観測になったと読むことです。</td>
</tr>
</tbody>
</table>

<h2>主要ルートごとに、いま何が実証されているか</h2>
<table>
<thead>
<tr>
<th>ルート</th>
<th>一次文献が支えるところ</th>
<th>まだ残る制約</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同時計測 EEG + fMRI</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a> は、1.5T〜7T にまたがる simultaneous EEG-fMRI で connectome 関係が再現可能であることを示しました。<a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">Jorge et al. (2015)</a> は ultra-high field で artifact prevention と safety assessment が前提条件であることを示しました。</td>
<td>時間分解能の非対称性、MR artifact、head motion、region-specific HRF、task-related haemodynamics、venous / depth bias、setup 依存性が残ります。したがって、空間情報を足しただけで fine-grained neural truth や trial-level causal order になったとは言えません。</td>
</tr>
<tr>
<td><strong>EEG + MEG + 現実的 head model</strong></td>
<td><a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">Aydin et al. (2014)</a> は、calibrated realistic volume conductor model を使うと combined EEG/MEG が source reconstruction を改善しうることを示しました。</td>
<td>改善は skull conductivity 校正と co-registration に依存します。したがって、単なる modality stacking と calibrated physics model を同一視しません。</td>
</tr>
<tr>
<td><strong>HD-EEG + intracranial validation</strong></td>
<td><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a> は intracerebral stimulation + HD-EEG の ground-truth dataset を公開し、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> は intracranial stimulation による direct validation を示しました。</td>
<td>direct validation は implanted / stimulated site 周辺の妥当化であり、未計測領域を含む general source truth ではありません。coverage bias と patient bias が残ります。</td>
</tr>
<tr>
<td><strong>same-brain structure-function link</strong></td>
<td><a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> は、mouse visual cortex の multi-area で dense activity と EM connectome を結び、同一脳での structure-function link を前進させました。</td>
<td>これは local functional twin の前進であり、human whole-brain、all-state、longitudinal completeness ではありません。</td>
</tr>
<tr>
<td><strong>atlas / Patch-seq / transcriptomic bridge</strong></td>
<td><a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">Yao et al. (2023)</a> は whole-mouse-brain atlas を、<a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">Gamlin et al. (2025)</a> は predicted transcriptomic type と connectomics の橋渡しを示しました。</td>
<td>ここで強くなるのは identity prior と structural / transcriptomic constraint であり、current synaptic efficacy、neuromodulatory field、glial slow state を直接観測したことにはなりません。</td>
</tr>
</tbody>
</table>

<h2>EEG-fMRI で追加する hemodynamic proxy gate</h2>
<p>
shared clock と co-registration は、EEG-fMRI を比較可能にするための必要条件ですが、十分条件ではございません。理由は単純で、fMRI 側の signal が <strong>direct neural truth</strong> ではなく、<strong>neurovascular transfer を通した hemodynamic proxy</strong> だからです。したがって EEG-fMRI では、通常の Fusion Card に加えて、少なくとも以下の gate を別に通します。
</p>
<table>
<thead>
<tr>
<th>gate</th>
<th>一次文献が支持すること</th>
<th>最低限ほしい提出物</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Neural target statement</strong></td>
<td><a href="https://doi.org/10.1038/35084005" target="_blank">Logothetis et al. (2001)</a> と <a href="https://doi.org/10.1038/nature09108" target="_blank">Lee et al. (2010)</a> は、BOLD が cell-type / population-input 依存の neurovascular proxy であることを示しました。</td>
<td>BOLD を `spike count`、`population input`、`network occupancy` のどれとして読むのかを明示します。</td>
</tr>
<tr>
<td><strong>Task / anticipatory component audit</strong></td>
<td><a href="https://doi.org/10.1038/nature07664" target="_blank">Sirotin &amp; Das (2009)</a> と <a href="https://doi.org/10.1038/nn.3170" target="_blank">Cardoso et al. (2012)</a> は、task-related haemodynamics が local neuronal activity だけでは説明しきれないことを示しました。</td>
<td>stimulus-related / task-related covariate、anticipation block、behavioural nuisance を分けて残します。</td>
</tr>
<tr>
<td><strong>HRF model granularity</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">Handwerker et al. (2004)</a> と <a href="https://doi.org/10.7554/eLife.86453" target="_blank">Bailes et al. (2023)</a> は、HRF timing が subject / region / local circuit で変わりうることを示しました。</td>
<td>canonical HRF か region-specific / subject-specific / voxelwise HRF か、latency claim の棄権条件も含めて残します。</td>
</tr>
<tr>
<td><strong>Venous / depth diagnostic</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">Kay et al. (2019)</a> と <a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">Kurzawski et al. (2022)</a> は、sub-mm map や BOLD magnitude が venous / non-neural factor に強く影響されうることを示しました。</td>
<td>large-vessel mask、depth-dependent diagnostic、non-neural factor の補正 / 棄権条件を残します。</td>
</tr>
<tr>
<td><strong>BOLD-CMRO<sub>2</sub> consistency / metabolic validator</strong></td>
<td><a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> は human cortex の calibrated fMRI で、BOLD と酸素代謝変化が有意 voxel の約40%で逆向きになりうることを示しました。</td>
<td>代謝や energetic mechanism を主張する場合は、calibrated BOLD、CMRO<sub>2</sub> 関連 readout、または明示的な abstention を残します。shared clock だけで metabolic interpretation へ上げません。</td>
</tr>
<tr>
<td><strong>Mechanistic validator</strong></td>
<td>shared clock があっても、EEG-fMRI だけでは mechanistic interpretation は閉じません。electrophysiology、intracranial validation、fPET / calibrated BOLD などの別 validator が必要です。</td>
<td>mechanism claim をする場合は external validator を明示し、無い場合は macro concordance までに留めます。</td>
</tr>
</tbody>
</table>

<strong>短い結論</strong>
<p>
EEG-fMRI の強みは、<strong>同一時点の macro-scale concordance</strong> と <strong>広域 coverage + ms 制約の併用</strong>にございます。しかし、hemodynamic proxy gate が無い場合、その ceiling はあくまで <strong>synchronized cross-modal constraint</strong> であって、fine-grained neural truth ではありません。さらに <strong>BOLD-CMRO<sub>2</sub> の不一致</strong>が残る以上、shared clock や細かい voxel map だけで energetic mechanism まで閉じたとは書きません。
</p>

<h2>融合後の地図は、直接観測ではなく推定です</h2>
<p>
ここが現行サイトでまだ弱かった批判点でございます。複数モダリティを 1 枚の map や latent state に融合したとしても、その出力は <strong>raw signal をそのまま見た真値</strong>ではありません。<a href="https://doi.org/10.1016/j.neuroimage.2019.116595" target="_blank">Wei et al. (2020)</a> が示した Bayesian fusion / multimodal DCM は、まさに <strong>共有 latent model を明示して初めて</strong> EEG と fMRI を結び付ける枠組みです。逆に言えば、融合モデル、事前分布、重み付け、事後不確実性を出さない fused map は、比較不能な黒箱に近づきます。
</p>

<strong>このサイトでの読み替え</strong>
<p>
したがって本サイトでは、fusion output を見るときに <strong>raw per modality</strong>、<strong>registration error</strong>、<strong>fusion model</strong>、<strong>uncertainty propagation</strong> の 4 点を同時提出物とします。これが無い場合、その融合結果は「解釈補助」または「prior つき推定」として扱い、直接観測の階段へは上げません。
</p>

<h2>今後の提出物に必須化する Fusion Card</h2>
<table>
<thead>
<tr>
<th>項目</th>
<th>最低限書くこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Acquisition relation</strong></td>
<td>simultaneous、same-subject non-simultaneous、coverage-limited validation、atlas prior のどれか。</td>
</tr>
<tr>
<td><strong>Clock and timing</strong></td>
<td>clock domain、offset / delay / jitter / drift、validation method、resync policy。</td>
</tr>
<tr>
<td><strong>Geometry and registration</strong></td>
<td>individual MRI、sensor/electrode coordinates、co-registration error、head model、conductivity assumptions。</td>
</tr>
<tr>
<td><strong>Fusion model</strong></td>
<td>late fusion か shared latent model か、loss、weights、priors、uncertainty representation。</td>
</tr>
<tr>
<td><strong>Hemodynamic proxy audit<br>(when fMRI / fNIRS is included)</strong></td>
<td>BOLD / CBF / fNIRS のどの proxy を使ったか、target neural claim、HRF model granularity、physiology nuisance、venous / depth diagnostic、mechanistic validator を書きます。</td>
</tr>
<tr>
<td><strong>Incremental evidence</strong></td>
<td>single-modality baseline、missing-modality ablation、behaviour-only / anatomy-only baseline と比べて、何がどれだけ増えたか。</td>
</tr>
<tr>
<td><strong>External validator</strong></td>
<td>phantom、intracranial stimulation、simultaneous invasive recording、post-op outcome、same-brain co-registration のどれで較正したか。</td>
</tr>
<tr>
<td><strong>Coverage boundary</strong></td>
<td>どの modality が何を still latent に残したか。cell type、synaptic efficacy、neuromodulation、glia、sleep-history を含めます。</td>
</tr>
<tr>
<td><strong>Raw retention</strong></td>
<td>各 modality の raw、QC、bad segment、artifact correction 前後、BIDS / metadata の所在。</td>
</tr>
</tbody>
</table>

<strong>受理条件</strong>
<p>
Fusion Card が無い場合、本サイトでは `multimodal result` を強く読まず、原則として <strong>single-modality result に prior を足した推定</strong>または<strong>限定つきの cross-modal concordance</strong>として扱います。さらに <strong>single-modality baseline や missing-modality ablation が無い場合</strong>、本サイトでは multimodal gain を書きません。
</p>

<h2>この批判から生じる site rule</h2>

<h4>Rule</h4>
<ul>
<li><strong>multimodal とだけ書かない：</strong>同時取得か、同一個体の geometry 統合か、侵襲校正か、atlas prior かを書き分けます。</li>
<li><strong>shared clock が無い統合を、trial-level alignment と書かない：</strong>same-subject の非同時計測は geometry を強くしますが、同一時点の state alignment を直接は与えません。</li>
<li><strong>atlas / Patch-seq / transcriptomics は prior と書く：</strong>cell-type label や molecular atlas を、current state observation と書きません。</li>
<li><strong>侵襲記録は gold standard ではなく coverage-limited validation と書く：</strong>implant 周辺で強いが、未計測領域を保証しません。</li>
<li><strong>fusion output を raw truth と書かない：</strong>fusion model、weights、uncertainty、registration error を同時に残します。</li>
<li><strong>fMRI / fNIRS を含む統合では hemodynamic proxy audit を出す：</strong>shared clock があっても、HRF・task-related haemodynamics・venous bias を通さずに neural truth とは書きません。</li>
<li><strong>same-brain local twin を whole-brain WBE と読み替えない：</strong>MICrONS や related datasets は local conditional prediction の大きな前進ですが、all-state completeness とは別です。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Sci Data</em>. 2019;6:103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Kothe C, Appelhoff S, Bullock T, et al. The lab streaming layer for synchronized multimodal recording. <em>Imaging Neurosci</em>. 2025;3:IMAG.a.136. <a href="https://doi.org/10.1162/imag.a.136" target="_blank">doi:10.1162/imag.a.136</a></li>
<li>Burns M, Nii L, Williams AN, et al. Motion-BIDS: extending BIDS to support standardized storage of motion data. <em>Sci Data</em>. 2024;11:857. <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">doi:10.1038/s41597-024-03559-8</a></li>
<li>Wei H, Jafarian A, Zeidman P, et al. Bayesian fusion and multimodal DCM for EEG and fMRI. <em>NeuroImage</em>. 2020;211:116595. <a href="https://doi.org/10.1016/j.neuroimage.2019.116595" target="_blank">doi:10.1016/j.neuroimage.2019.116595</a></li>
<li>Jorge J, Grouiller F, Ipek O, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. <em>NeuroImage</em>. 2015;105:132-144. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">doi:10.1016/j.neuroimage.2014.10.055</a></li>
<li>Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. <em>NeuroImage</em>. 2021;231:117864. <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">doi:10.1016/j.neuroimage.2021.117864</a></li>
<li>Aydin U, Vorwerk J, Kupper P, et al. Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. <em>PLoS One</em>. 2014;9(3):e93154. <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">doi:10.1371/journal.pone.0093154</a></li>
<li>Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Sci Data</em>. 2020;7:127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Commun</em>. 2023;5(2):fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>. 2025;638:425-435. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Yao Z, van Velthoven CTJ, Nguyen TN, et al. A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <em>Nature</em>. 2023;624:317-332. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>. 2025;638:316-324. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Logothetis NK, Pauls J, Augath M, Trinath T, Oeltermann A. Neurophysiological investigation of the basis of the fMRI signal. <em>Nature</em>. 2001;412:150-157. <a href="https://doi.org/10.1038/35084005" target="_blank">doi:10.1038/35084005</a></li>
<li>Lee JH, Durand R, Gradinaru V, et al. Global and local fMRI signals driven by neurons defined optogenetically by type and wiring. <em>Nature</em>. 2010;465:788-792. <a href="https://doi.org/10.1038/nature09108" target="_blank">doi:10.1038/nature09108</a></li>
<li>Sirotin YB, Das A. Anticipatory haemodynamic signals in sensory cortex not predicted by local neuronal activity. <em>Nature</em>. 2009;457:475-479. <a href="https://doi.org/10.1038/nature07664" target="_blank">doi:10.1038/nature07664</a></li>
<li>Cardoso MMBM, Sirotin YB, Lima B, Glushenkova E, Das A. The neuroimaging signal is a linear sum of neurally distinct stimulus- and task-related components. <em>Nature Neuroscience</em>. 2012;15:1298-1306. <a href="https://doi.org/10.1038/nn.3170" target="_blank">doi:10.1038/nn.3170</a></li>
<li>Handwerker DA, Ollinger JM, D'Esposito M. Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses. <em>NeuroImage</em>. 2004;21:1639-1651. <a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">doi:10.1016/j.neuroimage.2003.11.029</a></li>
<li>Bailes J, Millman R, Franklin C, et al. Resting-state fMRI signals contain spectral signatures of local hemodynamic response timing. <em>eLife</em>. 2023. <a href="https://doi.org/10.7554/eLife.86453" target="_blank">doi:10.7554/eLife.86453</a></li>
<li>Kay KN, Jamison KW, Zhang RY, Uğurbil K. A critical assessment of data quality and venous effects in sub-millimeter fMRI. <em>NeuroImage</em>. 2019;189:847-869. <a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">doi:10.1016/j.neuroimage.2019.02.006</a></li>
<li>Kurzawski JW, Yablonskiy DA, Pointer R, et al. Non-Neural Factors Influencing BOLD Response Magnitudes within Individual Subjects. <em>Journal of Neuroscience</em>. 2022;42:7256-7266. <a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">doi:10.1523/JNEUROSCI.2532-21.2022</a></li>
<li>Epp KJ, Lu H, Lydon-Staley DM, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. 2025. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
</ol>
