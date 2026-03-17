# Site Deepening Audit (2026-03-18, Local Proteostasis / Synaptic Tagging)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 入口・運用反映: `wbe_101.md`, `verification.md`

## 今回の選定理由

- 既存サイトは `connectome → cell type → transcription/chromatin → ECM/PNN → glia/metabolism` の分解をかなり前進させていました。
- しかしそのあいだにある `どのシナプス/樹状枝が plasticity-related proteins を捕捉し、late stabilization を成立させるか` という局所 proteostasis 層は、まだ `synaptic weight` や `molecular turnover` の周辺に埋もれていました。
- このままでは読者が `weight snapshot があれば late stabilization もほぼ固定できる` と誤読しやすく、技術・自然科学の観点ではここが未補強の弱点でした。

## 主要な批判点

### 1. `current synaptic state` と `late stabilization route` が近すぎました

- 問題:
  - 旧版では synaptic efficiency / short-term state は独立していましたが、`late LTP capture` や `reconsolidation persistence` を決める局所機構が独立 class として前面化していませんでした。
  - そのため、`現在の weight が近い` ことと `長期固定化の経路が近い` ことが、同じ層で読まれやすい構造でした。
- 根拠:
  - Frey & Morris (1997) は synaptic tagging を提起し、late LTP が plasticity-related proteins の capture 条件に依存することを示しました。
  - Shires et al. (2012) は living rat で synaptic tagging and capture を示しました。
  - Govindarajan et al. (2011) は protein-synthesis-dependent LTP の統合単位として dendritic branch が優先されることを示しました。
- 修正:
  - `local proteostasis / synaptic-tagging state` を `wbe_101`, `verification`, `wiki/connectome-is-not-enough`, `wiki/homeostatic-plasticity-and-maintenance-state` で独立 hidden state / state class として追加しました。

### 2. `molecular turnover` が抽象的すぎて、何を測るべきか曖昧でした

- 問題:
  - 旧版の `memory under molecular turnover` は方向性としては正しかった一方、`何が turnover の下で persistence を支えるのか` が抽象的で、検証変数が立っていませんでした。
  - これでは `静的分子保存では足りない` という批判はできても、`では何を別列にすべきか` が弱いままでした。
- 根拠:
  - Fonseca et al. (2006) は late-LTP maintenance が protein synthesis と proteasome-dependent degradation のバランスに依存することを示しました。
  - Pandey et al. (2021) は local autophagy-coupled translation が long-term memory formation に必要であることを示しました。
  - Lee et al. (2022) は active state transfer により synaptic memory が molecular turnover の下でも存続しうることを示しました。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` の該当節を `Local proteostasis / synaptic tagging under molecular turnover` に置換し、`tag / capture / translation / degradation / autophagy` を明示しました。

### 3. structural tag の時間幅と branch-local persistence が十分に見えていませんでした

- 問題:
  - 旧版では transcription, ECM, mitochondria はありましたが、`タグがどの程度持続するか` `どの構造状態が capture 可能性を担うか` が不足していました。
  - そのため、late stabilization を transcription 側か energy 側へだけ押し込んでしまう危険がありました。
- 根拠:
  - Thomas et al. (2025) は LTP 誘導後の actin dynamics と spine geometry の変化が synaptic tag の時間幅にわたって持続することを示しました。
- 修正:
  - `wbe_101.md` と `verification.md` の説明文に structural tag persistence を反映し、`branch-local persistence` を claim ceiling の一部として明記しました。

### 4. verification 側で監査項目になっていなかったため、実務的には見落とされる状態でした

- 問題:
  - hidden state として言及しても、Verification の `remaining latent state` や augmentation table に入っていなければ、site の運用ルールとしては弱いままです。
- 修正:
  - `verification.md` で以下を追加しました。
    - `remaining latent state` 列に `local proteostasis / synaptic-tagging state`
    - `State variable integrity gate` の新規 row
    - `current weight is not the late-stabilization route` addendum
    - `+ local proteostasis / synaptic-tagging audit` 行

## 今回実行した変更

- `wbe_101.md`
  - hidden-state 導入文に synaptic tagging / local proteostasis 文献を追加
  - hidden-state table に `Local proteostasis / synaptic-tagging state` を追加
  - 参考文献を追加
- `verification.md`
  - page highlights / known points を更新
  - `State variable integrity gate` を 9 class に更新
  - local proteostasis 用 addendum と augmentation row を追加
  - `remaining latent state` 列挙を更新
  - 参考文献を追加
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - front matter と abstract を更新
  - maintenance-state table の `molecular turnover` 行を `local proteostasis / synaptic tagging` に置換
  - 該当節を全面改稿
  - dangerous misreading / practical rule / minimum submissions を更新
  - human observability ceiling に `branch-local tag/proteostasis route` の未観測性を追加
  - 参考文献を追加
- `wiki/connectome-is-not-enough.md`
  - `9 state classes and 1 putative wall` へ更新
  - state-class table に `Local proteostasis / synaptic-tagging state` を追加
  - `Synapses are not binary edges` 節に late-stabilization route の note を追加
  - augmentation/ablation と site rules を更新
  - 参考文献を追加

## 外部依存で保留

- human in vivo での branch-local tag / proteostasis ground truth
  - 担当者: 実験系共同研究者 / 測定系研究者
  - 前提条件: human で spine/branch-local capture, translation, degradation, autophagy を直接もしくは強く外部較正できる計測系
  - 完了条件: `which branch carried the tag` を human longitudinal setting で比較可能にする公開 benchmark が整備されること

## 参考文献

1. Frey U, Morris RGM. Synaptic tagging and long-term potentiation. *Nature*. 1997;385(6616):533-536.
   - https://doi.org/10.1038/385533a0
2. Shires KL, Da Silva BM, Hawthorne JP, Morris RGM, Martin SJ. Synaptic tagging and capture in the living rat. *Nature Communications*. 2012;3:1246.
   - https://doi.org/10.1038/ncomms2250
3. Govindarajan A, Israely I, Huang S-Y, Tonegawa S. The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. *Neuron*. 2011;69(1):132-146.
   - https://doi.org/10.1016/j.neuron.2010.12.008
4. Fonseca R, Vabulas RM, Hartl FU, Bonhoeffer T, Nägerl UV. A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. *Neuron*. 2006;52(2):239-245.
   - https://doi.org/10.1016/j.neuron.2006.08.015
5. Pandey K, Yu X-W, Steinmetz A, Alberini CM. Autophagy coupled to translation is required for long-term memory formation. *Autophagy*. 2021;17(9):2489-2505.
   - https://doi.org/10.1080/15548627.2020.1775393
6. Thomas M, Bogaciu C-A, Rizzoli SO, et al. Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. *Communications Biology*. 2025;8:756.
   - https://doi.org/10.1038/s42003-025-08459-0
7. Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *PNAS*. 2022;119(42):e2211572119.
   - https://doi.org/10.1073/pnas.2211572119
