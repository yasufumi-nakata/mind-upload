# Wiki：EEG foundation model と事前学習

> 表現学習の前進と、まだ止める主張を分けて読む
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-16 / 位置づけ: Technical / natural science only

## このページの役割
このページは、EEG の foundation / self-supervised model をどう読むかを整理する学習用 wiki です。最近の大規模事前学習は確かに前進ですが、それを『一般化が解けた』『WBE に一段近づいた』と短絡しないために、pretraining corpus、channel mismatch、adaptation regime、evaluation family を分けて読みます。

## 正確さの前提
ここで扱うのは技術と自然科学の読み方です。WBE 全体の達成判定や哲学的論点は扱いません。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: ベースライン・事前登録・モデルカード](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Pretraining Card を通常の model card 運用へ接続できます。
- [Wiki: データ分割とリーク](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - overlap audit がなぜ必要かを補います。
- [Wiki: state・trait・ドリフト](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - cross-day / longitudinal claim を分けるときの基礎に戻れます。

## いま分かっていること
- self-supervised / foundation model は、少ラベル条件や mixed-task downstream で有望な改善を示しています。
- EEG は format heterogeneity が大きく、channel 数、reference、sample rate、window length の差が比較を壊しやすいです。
- downstream score は frozen / linear-probe / fine-tune の違いで意味が変わります。
- benchmark の split construction や preprocessing だけでも model ranking が動きうることが、2025〜2026 の文献で示され始めています。
- foundation model の成功を、そのまま source identifiability や WBE state-completeness に読み替えることはできません。

## まだ分かっていないこと
- どの pretraining objective が broad downstream で最も安定かは未確定です。
- cross-day / cross-device / cross-task / longitudinal deployability を同時に満たす既定路線はまだありません。
- benchmark version、split rule、checkpoint selection まで含めて標準監査する共通規格も、まだ固まっていません。
- いつ indiscriminate scale より targeted diversity が効くのかも、まだ固定された法則にはなっていません。

---

<h2>まず結論を一言でいうと</h2>
<p>
EEG foundation model は、<strong>表現学習</strong>と<strong>少ラベル downstream</strong>を押し上げる重要な前進です。ただし、それは <strong>どのデータで pretrain したか</strong>、<strong>どう format をそろえたか</strong>、<strong>どこまで downstream で適応したか</strong> を分けて初めて読めます。大きな model 名だけでは、一般化の強さも、止めるべき主張も決まりません。
</p>

<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。扱うのは、EEG の foundation / self-supervised model を、技術と自然科学の根拠だけでどう読むかです。
</p>

<strong>2026-03 文献監査で問題になった点</strong>
<p>
旧サイトは、QC、split、multimodal、drift はかなり強化できていましたが、<strong>foundation model 自体の読み方</strong>が抜けていました。この穴があると、最近の大規模事前学習を「dataset shift が解けた」「general decoder ができた」「WBE に近づいた」と短絡する余地が残ります。そこで本ページでは、一次文献が実際に何を前進させ、何をまだ未解決として残しているかを切り分けます。
</p>

<h2>一次文献が今支持する境界</h2>
<table>
<thead>
<tr>
<th>実例</th>
<th>比較的強く言えること</th>
<th>論文自身が残している壁</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Kostas et al. (2021)</strong><br>BENDR</td>
<td>self-supervised pretraining が novel subjects / hardware / tasks へ breadth を持ちうることを示しました。</td>
<td>downstream applicability はなお未確定で、pretraining だけで万能な転移が保証されたわけではありません。</td>
</tr>
<tr>
<td><strong>Wang et al. (2023)</strong><br>BIOT</td>
<td>sampling rate、channel、recording duration、missing values が違う heterogeneous biosignal を cross-data 学習へ持ち込む具体策を示しました。</td>
<td>裏返すと、format harmonization を書かない結果は比較不能だということです。</td>
</tr>
<tr>
<td><strong>Jiang et al. (2024)</strong><br>LaBraM</td>
<td>約 20 dataset、約 2,500 時間の EEG で cross-dataset pretraining を行い、複数 downstream task で強い性能を示しました。</td>
<td>EEG 側の主課題として、electrode mismatch、unequal length、varied task design、low SNR を正面から残しています。</td>
</tr>
<tr>
<td><strong>Wang et al. (2024)</strong><br>EEGPT</td>
<td>low SNR、inter-subject variability、channel mismatch に対して、pretrained transformer と linear probing で強い downstream 性能を示しました。</td>
<td>高スコアがそのまま cross-day deployability や source identifiability を意味するわけではありません。</td>
</tr>
<tr>
<td><strong>Lee et al. (2025)</strong><br>ICML fine-tuning audit</td>
<td>現行 large brainwave foundation model は従来 deep baseline をわずかに上回り、LoRA などの PEFT で trainable parameter を大きく減らせると示しました。</td>
<td>改善幅は小さく、abstract レベルでも約 0.5% 程度です。したがって「大きい model ほど勝つ」とは読めません。</td>
</tr>
<tr>
<td><strong>EEG Foundation Challenge (2025)</strong><br>NeurIPS competition</td>
<td>cross-task transfer と subject-invariant representation を、3,000 人超の HBN-EEG 参加者で標準化して測ろうとしています。</td>
<td>裏返すと、2025 年時点でも benchmark 規格そのものがまだ整備中であり、単発の task win は universal generalization の証拠ではありません。</td>
</tr>
<tr>
<td><strong>Xiong et al. (2025)</strong><br>EEG-FM-Bench</td>
<td>foundation model の増殖が standardized evaluation を追い越し、fragmented comparison が科学的進歩を鈍らせていると明示しました。</td>
<td>benchmark をそろえない比較は scientific inefficiency を生み、architecture の真の差を隠します。</td>
</tr>
<tr>
<td><strong>El Ouahidi et al. (2025)</strong><br>REVE</td>
<td>arbitrary length と electrode arrangement を扱える 4D positional encoding を導入し、大規模 pretraining で多様 setup への転移を前進させました。</td>
<td>論文の出発点自体が「既存 EEG foundation model は setup variation に弱い」ことであり、heterogeneity 問題は未解決のまま central です。</td>
</tr>
<tr>
<td><strong>Han et al. (2025)</strong><br>DIVER-1</td>
<td>largest-scale corpus と systematic scaling law analysis を提示し、electrophysiology では data-constrained scaling が成り立つと報告しました。</td>
<td>固定 data / compute では smaller models trained longer が larger models trained briefly を上回りうるため、parameter count 単独で優劣は決まりません。</td>
</tr>
<tr>
<td><strong>Wang et al. (2025)</strong><br>NeuroTTT</td>
<td>pretraining-downstream misalignment と cross-subject shift に対し、domain-tuned self-supervision と test-time training が有効だと示しました。</td>
<td>裏返すと、foundation model 単体で downstream adaptation が十分だという前提は成立していません。</td>
</tr>
<tr>
<td><strong>Lahiri et al. (2026)</strong><br>PRISM</td>
<td>targeted diversity を含む pretraining が fine-tuning 下で優位になりうること、clinical mimicker task で大きな改善を示しうることを報告しました。</td>
<td>benchmark inconsistency だけで identical dataset 上の ranking が最大 24 pp 反転しうるため、model ranking 自体を監査対象にすべきです。</td>
</tr>
</tbody>
</table>

<h2>foundation model を読む前の 7 つの gate</h2>
<table>
<thead>
<tr>
<th>gate</th>
<th>なぜ必要か</th>
<th>最低限ほしい証跡</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>G1: corpus identity / overlap</strong></td>
<td>pretraining corpus も dataset です。downstream と近縁データが混ざれば split の意味が崩れます。</td>
<td>corpus 名、version / snapshot、総時間、downstream dataset / subject / session との overlap audit。</td>
</tr>
<tr>
<td><strong>G2: population / setup diversity</strong></td>
<td>dataset 数や総時間だけでは不十分です。population、device、electrode layout が偏っていれば、pretraining は recording distribution artifact を学びえます。</td>
<td>population の範囲、device 種別、clinical / lab の別、electrode schema、reference 系の分布。</td>
</tr>
<tr>
<td><strong>G3: harmonization</strong></td>
<td>EEG は channel 数、reference、sample rate、window length の差が大きく、整形差だけで性能が動きます。</td>
<td>channel map、reference、resampling、token length、missing-channel / missing-segment policy。</td>
</tr>
<tr>
<td><strong>G4: adaptation regime</strong></td>
<td>frozen feature extraction と full fine-tune、さらに test-time training では、「何が転移したか」の意味が違います。</td>
<td>frozen / linear-probe / PEFT / full fine-tune / TTT の別、target data 使用量、label budget、再較正量。</td>
</tr>
<tr>
<td><strong>G5: benchmark provenance</strong></td>
<td>2025〜2026 の benchmark 文献は、split construction、checkpoint selection、segment length だけでも ranking が動くことを示しています。</td>
<td>benchmark 名、version、split rule、checkpoint selection、segment length、normalization、外部 hold-out の作り方。</td>
</tr>
<tr>
<td><strong>G6: scale / efficiency</strong></td>
<td>EEG では「大きいほど強い」が必ずしも成り立ちません。parameter、data、compute、trainable fraction を同時に読まないと誤ります。</td>
<td>総 parameter 数、trainable parameter 数、pretraining epoch / step、corpus 規模、学習時間、adapter 量。</td>
</tr>
<tr>
<td><strong>G7: claim ceiling</strong></td>
<td>foundation model の成功は、あくまで macro decode / representation learning の前進です。</td>
<td>何を still latent に残したか、source identifiability / direct validation / WBE state-completeness を止める明示。</td>
</tr>
</tbody>
</table>

<h2>このサイトで要求する Pretraining Card</h2>
<p>
foundation / self-supervised 系の結果には、通常の model card に加えて <strong>Pretraining Card</strong> を付けます。これは論文側の既存規格ではなく、heterogeneous corpus pretraining を比較可能に保つための <strong>本サイトの運用ルール</strong>です。
</p>

<table>
<thead>
<tr>
<th>項目</th>
<th>最低限書くこと</th>
<th>書かないと危険な誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Corpus</strong></td>
<td>pretraining corpus 名、version、総時間、除外条件、overlap audit。</td>
<td>一般化性能だと思っていたものが、実は近縁データ再利用だった可能性を見落とします。</td>
</tr>
<tr>
<td><strong>Population / Setup</strong></td>
<td>population、device、electrode layout、reference 系、clinical / lab の別。</td>
<td>dataset 数の多さを、そのまま recording diversity と誤読します。</td>
</tr>
<tr>
<td><strong>Harmonization</strong></td>
<td>channel schema、reference、sample rate、tokenization、normalization、missing-value policy。</td>
<td>整形の差を model 能力の差と誤読します。</td>
</tr>
<tr>
<td><strong>Objective</strong></td>
<td>masked / autoregressive / contrastive などの pretraining objective。</td>
<td>どの inductive bias が効いたかを比較できません。</td>
</tr>
<tr>
<td><strong>Adaptation</strong></td>
<td>frozen / linear-probe / PEFT / full fine-tune / TTT、target data 使用量、label budget、再較正の有無。</td>
<td>「general representation が効いた」のか「target へ強く適応した」のかを混同します。</td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>benchmark 名、version、split rule、checkpoint selection、segment length、normalization。</td>
<td>benchmark 設計差で起きた ranking 変動を、model 自体の差と誤読します。</td>
</tr>
<tr>
<td><strong>Scale / Efficiency</strong></td>
<td>総 parameter 数、trainable parameter 数、pretraining step / epoch、学習時間、adapter 量、推論コスト。</td>
<td>「大きい model だから強い」と読み、実際には compute 配分や PEFT が効いた可能性を落とします。</td>
</tr>
<tr>
<td><strong>Evaluation</strong></td>
<td>evaluation family、hold-out unit、device-holdout、cross-day、abstention、失敗条件。</td>
<td>same-day の高 score を deployability と読み替えます。</td>
</tr>
<tr>
<td><strong>Stopped claim</strong></td>
<td>それでもまだ言えないことを 1 行で明示します。</td>
<td>foundation model の成功を source truth や WBE へ過大外挿します。</td>
</tr>
</tbody>
</table>

<h2>このサイトでの運用ルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>foundation model の結果も split 監査を免除しません：</strong>pretraining corpus を含めて独立性を確認します。</li>
<li><strong>population / setup diversity を hidden にしません：</strong>dataset 数ではなく、どの recording distribution を含んだかを出します。</li>
<li><strong>format harmonization を hidden にしません：</strong>channel / reference / sampling の整形手順を必ず出します。</li>
<li><strong>adaptation の量を隠しません：</strong>linear probing、full fine-tune、TTT を同じ「transfer 成功」として並べません。</li>
<li><strong>benchmark provenance を hidden にしません：</strong>split / checkpoint / preprocessing の違いで ranking が動くので、benchmark 仕様も成果物です。</li>
<li><strong>scale / efficiency を hidden にしません：</strong>parameter 数、trainable fraction、学習時間を出さずに「foundation model が勝った」とは書きません。</li>
<li><strong>高スコアでも claim ceiling は維持します：</strong>source identifiability、direct validation、closed-loop deployability、WBE state-completeness は別ゲートです。</li>
<li><strong>Pretraining Card が無い結果は限定つき decode として扱います：</strong>L2 以上へ自動昇格させません。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Kostas, D., Aroca-Ouellette, S., &amp; Rudzicz, F. (2021). BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. <em>Frontiers in Human Neuroscience</em>, 15, 653659. <a href="https://doi.org/10.3389/fnhum.2021.653659" target="_blank">doi:10.3389/fnhum.2021.653659</a></li>
<li>Wang, H., Lu, C., Xie, B., et al. (2023). BIOT: Biosignal Transformer for Cross-data Learning in the Wild. <em>NeurIPS 2023</em>. <a href="https://papers.nips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf" target="_blank">paper</a></li>
<li>Jiang, W.-B., Zhao, L., &amp; Lu, B.-L. (2024). Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. <em>ICLR 2024</em>. <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html" target="_blank">proceedings</a></li>
<li>Wang, G., Liu, W., He, Y., Xu, C., Ma, L., &amp; Li, H. (2024). EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals. <em>NeurIPS 2024</em>. <a href="https://neurips.cc/virtual/2024/poster/93793" target="_blank">poster / abstract</a></li>
<li>Lee, N., Barmpas, K., Panagakis, Y., Adamos, D., Laskaris, N., &amp; Zafeiriou, S. (2025). Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. <em>ICML 2025 poster</em>. <a href="https://openreview.net/forum?id=J5SbLoq7Uv" target="_blank">OpenReview</a></li>
<li>EEG Foundation Challenge (2025). From Cross-Task to Cross-Subject EEG Decoding. <em>NeurIPS 2025 competition</em>. <a href="https://eeg2025.github.io/" target="_blank">official website</a></li>
<li>Xiong, W., Li, J., Li, J., &amp; Zhu, K. (2025). EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. <em>arXiv</em>. <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
<li>El Ouahidi, Y., Lys, J., Thölke, P., Farrugia, N., Pasdeloup, B., Gripon, V., Jerbi, K., &amp; Lioi, G. (2025). REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. <em>arXiv</em>. <a href="https://arxiv.org/abs/2510.21585" target="_blank">arXiv:2510.21585</a></li>
<li>Han, D. D., Gwon, Y., Lee, A. L., et al. (2025). DIVER-1: Deep Integration of Vast Electrophysiological Recordings at Scale. <em>arXiv</em>. <a href="https://arxiv.org/abs/2512.19097" target="_blank">arXiv:2512.19097</a></li>
<li>Wang, S., Deng, Y., Bao, Z., Zhan, X., &amp; Duan, Y. (2025). NeuroTTT: Bridging Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training. <em>arXiv</em>. <a href="https://arxiv.org/abs/2509.26301" target="_blank">arXiv:2509.26301</a></li>
<li>Lahiri, J. B., Runwal, P., Kulkarni, A., Jain, M., Mishra, A. R., Panwar, S., &amp; Singh, S. (2026). PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. <em>arXiv</em>. <a href="https://arxiv.org/abs/2603.02268" target="_blank">arXiv:2603.02268</a></li>
</ol>
