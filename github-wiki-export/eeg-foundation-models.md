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
- foundation model の成功を、そのまま source identifiability や WBE state-completeness に読み替えることはできません。

## まだ分かっていないこと
- どの pretraining objective が broad downstream で最も安定かは未確定です。
- cross-day / cross-device / cross-task / longitudinal deployability を同時に満たす既定路線はまだありません。
- pretraining corpus overlap をどう標準監査するかも、分野としては未整備です。

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
<td><strong>Zhang et al. (2025)</strong><br>Cross Device Representation Consistency</td>
<td>cross-device pretraining が subject-independent task と wearable / heterogeneous setting で実用性を押し上げうることを示しました。</td>
<td>それでも real-world robustness は task-dependent で、device hold-out や longitudinal drift の監査は別に要ります。</td>
</tr>
</tbody>
</table>

<h2>foundation model を読む前の 5 つの gate</h2>
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
<td><strong>G2: harmonization</strong></td>
<td>EEG は channel 数、reference、sample rate、window length の差が大きく、整形差だけで性能が動きます。</td>
<td>channel map、reference、resampling、token length、missing-channel / missing-segment policy。</td>
</tr>
<tr>
<td><strong>G3: adaptation regime</strong></td>
<td>frozen feature extraction と full fine-tune では、「何が転移したか」の意味が違います。</td>
<td>frozen / linear-probe / PEFT / full fine-tune の別、target data 使用量、再較正量。</td>
</tr>
<tr>
<td><strong>G4: evaluation family</strong></td>
<td>within-session、cross-session、cross-subject、device-holdout、closed-loop は別の問いです。</td>
<td>独立な hold-out 単位、cross-day / device-holdout の有無、fixed decoder interval、abstention / uncertainty。</td>
</tr>
<tr>
<td><strong>G5: claim ceiling</strong></td>
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
<td>frozen / linear-probe / PEFT / full fine-tune、target data 使用量、再較正の有無。</td>
<td>「general representation が効いた」のか「target へ強く適応した」のかを混同します。</td>
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
<li><strong>format harmonization を にしません：</strong>channel / reference / sampling の整形手順を必ず出します。</li>
<li><strong>adaptation の量を隠しません：</strong>linear probing と full fine-tune を同じ「transfer 成功」として並べません。</li>
<li><strong>高スコアでも claim ceiling は維持します：</strong>source identifiability、direct validation、closed-loop deployability、WBE state-completeness は別ゲートです。</li>
<li><strong>Pretraining Card が無い結果は限定つき decode として扱います：</strong>L2 以上へ自動昇格させません。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Kostas, D., Aroca-Ouellette, S., &amp; Rudzicz, F. (2021). BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. <em>Frontiers in Human Neuroscience</em>, 15, 653659. <a href="https://doi.org/10.3389/fnhum.2021.653659" target="_blank">doi:10.3389/fnhum.2021.653659</a></li>
<li>Wang, H., Lu, C., Xie, B., et al. (2023). BIOT: Biosignal Transformer for Cross-data Learning in the Wild. <em>NeurIPS 2023</em>. <a href="https://papers.nips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf" target="_blank">paper</a></li>
<li>Jiang, W.-B., Zhao, L., &amp; Lu, B.-L. (2024). Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. <em>ICLR 2024</em>. <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html" target="_blank">proceedings</a></li>
<li>Wang, G., Liu, W., He, Y., Xu, C., Ma, L., &amp; Li, H. (2024). EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals. <em>NeurIPS 2024</em>. <a href="https://neurips.cc/virtual/2024/poster/93793" target="_blank">poster / abstract</a></li>
<li>Zhang, M., Zhao, S., Xie, L., Liu, T., Yao, D., &amp; Yin, E. (2025). Self-Supervised Contrastive Pre-Training for EEG-Based Recognition via Cross Device Representation Consistency. <em>IEEE Transactions on Biomedical Engineering</em>. <a href="https://doi.org/10.1109/TBME.2025.3613730" target="_blank">doi:10.1109/TBME.2025.3613730</a></li>
</ol>
