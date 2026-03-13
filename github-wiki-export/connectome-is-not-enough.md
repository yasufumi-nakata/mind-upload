# Wiki：配線図だけでは足りない理由

> connectome-complete は emulation-complete ではありません
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Technical / natural science only

## このページの役割
このページは、『コネクトームが取れれば脳の再現に十分ではないか』という直感を、一次文献に基づいて分解するためのページです。哲学や法制度ではなく、どの状態変数が欠けると何が言えなくなるかに絞って整理します。

## 正確さの前提
ここで示すのは『最低限これを外すと主張が弱くなる』という整理であり、最終的な十分条件が確定したという意味ではありません。

## 公開ページへ戻る
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - この論点の前提になる全体像を初歩から整理します。
- [Wiki: Decode と Emulate](https://github.com/yasufumi-nakata/mind-upload/wiki/decode-vs-emulate) - 出力の翻訳と内部生成の違いを整理します。
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - どこまでの証拠でどの強さの主張が許されるかを確認できます。

## いま分かっていること
- 全脳 connectome の作成は大きく前進していますが、それだけで動的再現が完了したとは言えません。
- シナプス効率、遅延、神経修飾、グリア、細胞型ラベルは、静的な edge list からは落ちやすい情報です。
- 粗い生理 proxy を ground truth と混同すると、内部状態の主張を過大化しやすくなります。

## まだ分かっていないこと
- どの状態クラスをどの解像度まで取れば WBE の十分条件に近づくかは未確定です。
- 欠落した状態変数をどこまで推定や coarse-graining で補えるかは、今後の検証課題です。
- 人で直接取得できない状態を、どの動物・侵襲系で較正すべきかはまだ固定されていません。

---

<h2>結論</h2>
<p>
配線図は WBE の重要な土台ですが、<strong>それだけでは動的再現の下限要件になりません</strong>。同じ隣接関係でも、細胞型ラベル、シナプス効率、伝導遅延、神経修飾、グリア結合状態が違えば、学習、位相同期、覚醒度依存の応答、長期安定性は大きく変わります。したがって、このサイトでは <strong>connectome-complete を structural atlas / scaffold の達成</strong>として扱い、<strong>emulation-complete と言い換えません</strong>。
</p>

<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。技術と自然科学の側面だけから、「何の状態変数が欠けると何が主張できなくなるか」を整理します。
</p>

<h2>先に固定する 5 つの状態クラス</h2>
<table>
<thead>
<tr>
<th>状態クラス</th>
<th>配線図だけでは何が欠けるか</th>
<th>欠けたまま言える範囲</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>細胞型ラベル</strong></td>
<td>同じ隣接関係でも、転写型ごとに結合モチーフ、シナプス特性、髄鞘化の傾向が変わります。</td>
<td>構造アトラスや候補 scaffold としては有用ですが、機能同等性の十分条件にはなりません。</td>
</tr>
<tr>
<td><strong>シナプス効率・短期状態</strong></td>
<td>edge の有無だけでは重み、放出確率、短期可塑性、LTP/LTD の履歴を決められません。</td>
<td>静的配線の記述までは可能ですが、L2 の介入予測や L3 の閉ループ安定性は主張できません。</td>
</tr>
<tr>
<td><strong>遅延・髄鞘</strong></td>
<td>同じグラフでも伝導速度が違えば、位相、同期、抑制の到達タイミングが変わります。</td>
<td>時間整合性やリアルタイム制御の主張を止め、遅延不確実性を残す必要があります。</td>
</tr>
<tr>
<td><strong>神経修飾場</strong></td>
<td>覚醒度、学習率、利得調整は静的 wiring だけでは復元できず、瞳孔径や HRV は粗い proxy にとどまります。</td>
<td>人データでは共変量や層別化に使えても、トランスミッタ特異的な内部状態の ground truth とは言えません。</td>
</tr>
<tr>
<td><strong>グリア・代謝結合状態</strong></td>
<td>アストロサイト等は可塑性や記憶想起に因果的に関与し、単なる支持組織ではありません。</td>
<td>長期可塑性や状態維持を含む主張は弱め、適用範囲を限定して書く必要があります。</td>
</tr>
</tbody>
</table>

<h2>配線図研究は大きく進んだが、それ自体は終点ではない</h2>
<p>
Dorkenwald らは成体ショウジョウバエ全脳の wiring diagram を示し、約 13 万ニューロン規模で全脳 connectome を提示しました。一方で MICrONS Consortium は、マウス視覚皮質の立方ミリメートル規模で、同一個体の機能計測と connectomics を結びつけるデータセットを公開しました。これは非常に大きな前進ですが、逆に言えば、<strong>現在ようやく「配線＋局所機能」を結び始めた段階</strong>であり、全脳・全状態の動的再現とはまだ別問題であることも示しています。
</p>

<strong>ここでの読み替え</strong>
<p>
connectome-complete は「何がつながっているか」がかなり分かったという意味では重要です。しかし、それだけでは「どの強さで」「どの遅延で」「どの neuromodulatory context で」「どの glial coupling の下で」動くかまでは固定されません。
</p>

<h2>なぜこの 5 クラスが抜けやすいのか</h2>

<h3>1. 細胞型ラベルは node ID の飾りではありません</h3>
<p>
Gamlin らは、マウス視覚皮質で予測された Sst transcriptomic types ごとに、接続モチーフ、シナプス特性、髄鞘化が系統的に異なることを示しました。つまり、<strong>同じグラフ構造でも node label が違えば回路の物理的意味が変わる</strong>ということです。cell type を落とした unlabeled graph は、圧縮としては便利でも、機能再現の前提情報をかなり失います。
</p>

<h3>2. シナプスは binary edge ではありません</h3>
<p>
Holler らは新皮質シナプスで、超微細構造と release property を結びつけて解析し、単純な「つながっている/いない」では伝達特性を表せないことを示しました。Matsuzaki らは単一 dendritic spine における LTP 誘導で、spine enlargement と AMPA 電流増加が結びつくことを示しています。したがって、<strong>edge list だけでは current state の weight も plastic history も落ちます</strong>。
</p>

<h3>3. 遅延と髄鞘は timing の一部です</h3>
<p>
Gibson らは神経活動が oligodendrogenesis と adaptive myelination を促進することを示し、McKenzie らは motor skill learning に active central myelination が必要であることを報告しました。さらに Micheva らは、PV interneuron の局所軸索でも髄鞘化の程度が伝導速度と相関することを示しました。つまり、<strong>同じ配線でも timing state が違えば、局所抑制回路や学習のダイナミクスが変わる</strong>ため、delay を graph の外へ追い出すことはできません。
</p>

<h3>4. 神経修飾は「1つの気分スカラー」ではありません</h3>
<p>
Reimer らは、瞳孔変動が皮質内の adrenergic と cholinergic activity の両方を追うことを示しました。これは逆に、<strong>瞳孔径がどちらか一方の transmitter state を一意に表すわけではない</strong>ことも意味します。人で瞳孔径や HRV を使うのは有用ですが、トランスミッタ特異的・領域特異的な内部状態の ground truth と見なすのは過大主張です。
</p>

<h3>5. グリアは後付けの補助変数ではありません</h3>
<p>
Adamsky らは astrocytic activation が de novo neuronal potentiation と memory enhancement を生みうることを示しました。Cahill らは、局所的で瞬間的な neurotransmitter input が、分単位にわたる広い astrocyte network の応答へ符号化されることを報告しています。したがって、<strong>グリアを無視したモデルは、可塑性や slow network state を部分的に欠いたモデル</strong>として扱うべきです。
</p>

<h2>このサイトで採用する読み替えルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>connectome-complete：</strong>構造アトラス、候補 scaffold、圧縮の出発点として扱います。L2/L3 の emulation 達成とは書きません。</li>
<li><strong>pupil / HRV：</strong>人データでは有用な state covariate ですが、トランスミッタ特異的 ground truth としては扱いません。</li>
<li><strong>state variable が無いとき：</strong>推定したなら誤差と棄権条件を、推定していないなら absent と明記します。</li>
<li><strong>glia / neuromodulation を落とすとき：</strong>その近似で何の振る舞いを捨てたのかを、適用範囲として本文に書きます。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted transcriptomic types in mouse visual cortex. <em>Nature</em>. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Holler, S., et al. (2021). Structure and function of a neocortical synapse. <em>Nature</em>, 591, 111–116. <a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">doi:10.1038/s41586-020-03134-2</a></li>
<li>Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., & Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. <em>Nature</em>, 429, 761–766. <a href="https://doi.org/10.1038/nature02617" target="_blank">doi:10.1038/nature02617</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318–322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Micheva, K. D., Kiraly, M., Perez, M. M., & Madison, D. V. (2021). Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. <em>Cerebral Cortex</em>, 31(7), 3374–3392. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">doi:10.1093/cercor/bhab018</a></li>
<li>Reimer, J., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Adamsky, A., et al. (2018). Astrocytic activation generates de novo neuronal potentiation and memory enhancement. <em>Nature Neuroscience</em>, 21, 1725–1733. <a href="https://doi.org/10.1038/s41593-018-0253-6" target="_blank">doi:10.1038/s41593-018-0253-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146–153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
</ol>
