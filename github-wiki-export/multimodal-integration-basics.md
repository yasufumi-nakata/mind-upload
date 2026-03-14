# Wiki：マルチモーダル統合の基本

> 足し算で万能になるのではなく、同期・幾何・外部妥当化を増やす設計です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Technical / natural science only

## このページの役割
このページは、EEG、MEG、fMRI、侵襲記録、MRI を組み合わせると何が本当に改善するのかを、一次文献ベースで整理する wiki です。哲学や法制度ではなく、同期、座標合わせ、forward model、外部妥当化、state coverage の観点だけに絞ります。

## 正確さの前提
ここで示すのは『統合すれば何でも分かる』という話ではありません。どの条件を満たしたときに何が少し強く言えるか、そして何がまだ言えないかの整理です。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: EEGの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - まず EEG 単体の限界へ戻りたいときはこちらです。
- [Wiki: イベント同期と観測ログ](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - 共有時計、遅延、ジッタ、ドリフトの基本を補います。
- [Wiki: 不確実性・校正・棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - 統合しても不確実性が消えない理由を補います。
- [Wiki: 観測から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 観測値と推定値を混同しないための入口です。

## いま分かっていること
- 複数モダリティを組み合わせると、時間・空間・局所性の一部は補完できます。
- ただし改善量は、共有時計、個体別解剖、電極/センサー位置、導電率仮定、外部基準の有無に強く依存します。
- 侵襲記録は強い calibration route ですが、coverage bias と patient bias を抱えます。

## まだ分かっていないこと
- どの統合セットが WBE のどの段階に最も効くかは、まだ固定できません。
- 複数モダリティを統合しても、細胞・シナプス・神経修飾・グリア状態の十分性は未解決です。
- 統合後の不確実性をどう伝播・報告するかは、依然として研究課題です。

---

<h2>結論</h2>
<p>
マルチモーダル統合は、EEG の弱点を一部補えます。しかし、<strong>1 つの inverse problem を、同期・幾何・ノイズ・外部妥当化を伴う複数の問題へ置き換える</strong>だけでもあります。したがって、このサイトでは「モダリティを足した」という事実だけでは評価せず、<strong>どの監査ゲートを通したか</strong>で読みます。
</p>

<strong>このページの範囲</strong>
<p>
ここでは、技術と自然科学の側面だけを扱います。本人性、意識、法制度の話は含めません。問うのは、「何が観測できたか」ではなく、<strong>何がどこまで監査できたか</strong>です。
</p>

<h2>先に固定する 5 つの監査ゲート</h2>
<table>
<thead>
<tr>
<th>ゲート</th>
<th>通ったときに少し強く言えること</th>
<th>通っていないときに止めるべき主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同期ゲート</strong></td>
<td>共有時計、遅延、ジッタ、ドリフトが管理され、各モダリティの時系列を比較しやすくなります。</td>
<td>位相関係、因果順序、trial-level 統合を強く言うことです。</td>
</tr>
<tr>
<td><strong>幾何ゲート</strong></td>
<td>個体別 MRI、実測電極/センサー位置、forward model が揃い、source claim の根拠が少し強くなります。</td>
<td>「どこで起きたか」を一般化して断言することです。</td>
</tr>
<tr>
<td><strong>ノイズ/場ゲート</strong></td>
<td>MR artifact、motion artifact、background field、cross-talk を分けて扱えます。</td>
<td>きれいな fused map を、そのまま neural signal の真値とみなすことです。</td>
</tr>
<tr>
<td><strong>外部妥当化ゲート</strong></td>
<td>侵襲記録、頭蓋内刺激、術後転帰、ファントムなどに対する誤差を監査できます。</td>
<td>推定結果だけで「改善した」と言うことです。</td>
</tr>
<tr>
<td><strong>state coverage ゲート</strong></td>
<td>今回の統合が、時間・空間・局所性のどれを補い、どの状態変数を依然として欠くかを限定できます。</td>
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
<td><strong>EEG + 個体別 MRI / forward model</strong></td>
<td>Unnwongse ら (2023) は、頭蓋内電気刺激を ground truth にして、個体別 FEM と skull conductivity 最適化で localization error を直接検証しました。</td>
<td>誤差は source depth と導電率仮定に依存し、細粒度の局所回路や深部活動を一般に一意復元できるわけではありません。</td>
</tr>
<tr>
<td><strong>EEG + MEG</strong></td>
<td>Aydin ら (2014) は、較正した realistic head model を使うことで、EEG/MEG 統合が source reconstruction を改善しうることを示しました。</td>
<td>利点は skull conductivity 校正と co-registration に依存し、単純な modality stacking だけでは得られません。</td>
</tr>
<tr>
<td><strong>同時計測 EEG + fMRI</strong></td>
<td>Jorge らの 2 本の 2015 年論文と Wirsich ら (2021) は、1.5T〜7T でも同時計測が可能であり、適切な setup 下では再現可能な connectivity 解析へ進めることを示しました。</td>
<td>artifact と安全管理は磁場強度で悪化しやすく、時間分解能の非対称性や EEG 品質低下が残ります。</td>
</tr>
<tr>
<td><strong>EEG + 侵襲記録（ECoG / SEEG / DBS）</strong></td>
<td>Zhang ら (2006) は同時 scalp EEG/ECoG で皮質電位再構成を、Seeber ら (2019) は 256ch scalp EEG と同時 DBS 記録で subcortical detectability を示しました。</td>
<td>coverage は臨床必要部位に偏り、患者群バイアスも避けられません。全脳 ground truth にはなりません。</td>
</tr>
<tr>
<td><strong>OPM-MEG 系</strong></td>
<td>Boto ら (2018) は wearable OPM-MEG により、自然運動を含む条件での MEG 計測可能性を示しました。</td>
<td>background field nulling と motion-aware correction が前提であり、簡単な携帯代替装置ではありません。</td>
</tr>
</tbody>
</table>

<h2>各ルートが実際に足すもの</h2>

<h3>1. EEG + MRI は「解剖を足す」のであって、真値を足すのではありません</h3>
<p>
個体別 MRI、実測電極位置、現実的な forward model は、EEG source imaging の条件を大きく改善します。しかし Unnwongse ら (2023) が示したように、<strong>直接妥当化を行っても誤差は残り、深い source ほど難しくなる</strong>ため、「MRI を足したから局在した」とは読めません。正しい読み方は、「幾何の監査が一段進んだ」です。
</p>

<h3>2. EEG + MEG は感度分布の補完ですが、頭蓋導電率校正が効きます</h3>
<p>
EEG と MEG は volume conduction への感度が異なるため、統合には意味があります。ただし Aydin ら (2014) が示す通り、改善の鍵は <strong>calibrated realistic volume conductor model</strong> にあります。したがって、このルートの本質は「2 モダリティだから強い」ではなく、<strong>より良い物理モデルを伴って初めて強い</strong>です。
</p>

<h3>3. EEG + fMRI は時間と空間の補完ですが、artifact と安全が増えます</h3>
<p>
同時計測 EEG-fMRI は魅力的ですが、Jorge らの 2 本の 2015 年論文が示したように、磁場強度が上がるほど artifact と setup 依存性も増えます。Wirsich ら (2021) は 1.5T〜7T にわたり再現可能な connectome 解析を示しましたが、これは逆に、<strong>適切な hardware・cabling・artifact control を組んで初めて成立する</strong>ことも意味します。したがって、空間分解能を足しただけで済む話ではありません。
</p>

<h3>4. EEG + 侵襲記録は calibration route として強いが、coverage は狭いです</h3>
<p>
Zhang ら (2006) は simultaneous scalp EEG/ECoG を用いて、現実的な FEM と co-registered MRI/CT があれば皮質電位再構成の主要な空間パターンを保持できることを示しました。Seeber ら (2019) も、256ch scalp EEG と同時 DBS 記録により、深部信号が条件つきで detectable であることを示しました。しかし、これらは<strong>侵襲記録で見えている範囲だけ</strong>を強くするのであって、未計測領域まで保証するわけではありません。
</p>

<h2>このサイトで採用する読み替えルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>multimodal：</strong>「複数モダリティを足した」ではなく、「どの監査ゲートを通したか」で読みます。</li>
<li><strong>EEG + MRI：</strong>個体別解剖が入っても、外部妥当化が無ければ source claim は限定して書きます。</li>
<li><strong>EEG + fMRI：</strong>空間情報の補完としては有用ですが、artifact・安全・時系列整合の監査を必須にします。</li>
<li><strong>EEG + 侵襲記録：</strong>gold standard ではなく、coverage-limited な calibration / validation route として扱います。</li>
<li><strong>state coverage：</strong>シナプス、神経修飾、グリア、細胞型ラベルが未観測なら、未観測のままと明記します。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C., Garrido, M. I., Gramfort, A., et al. (2020). Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>, 23, 1473-1483. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Jorge, J., Grouiller, F., Ipek, O., et al. (2015). Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. <em>NeuroImage</em>, 105, 132-144. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">doi:10.1016/j.neuroimage.2014.10.055</a></li>
<li>Jorge, J., Grouiller, F., Gruetter, R., et al. (2015). Towards high-quality simultaneous EEG-fMRI at 7 T: Detection and reduction of EEG artifacts due to head motion. <em>NeuroImage</em>, 120, 143-153. <a href="https://doi.org/10.1016/j.neuroimage.2015.07.020" target="_blank">doi:10.1016/j.neuroimage.2015.07.020</a></li>
<li>Wirsich, J., Jorge, J., Iannotti, G. R., et al. (2021). The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. <em>NeuroImage</em>, 231, 117864. <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">doi:10.1016/j.neuroimage.2021.117864</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2014). Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. <em>PLoS ONE</em>, 9(3), e93154. <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">doi:10.1371/journal.pone.0093154</a></li>
<li>Zhang, Y., Ding, L., van Drongelen, W., et al. (2006). A cortical potential imaging study from simultaneous extra- and intracranial electrical recordings by means of the finite element method. <em>NeuroImage</em>, 31(4), 1517-1528. <a href="https://doi.org/10.1016/j.neuroimage.2006.02.027" target="_blank">doi:10.1016/j.neuroimage.2006.02.027</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <em>Nature Communications</em>, 10, 753. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <em>Nature</em>, 555, 657-661. <a href="https://doi.org/10.1038/nature26147" target="_blank">doi:10.1038/nature26147</a></li>
</ol>
