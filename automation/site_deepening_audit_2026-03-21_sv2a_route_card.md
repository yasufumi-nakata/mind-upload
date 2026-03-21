# Site Deepening Audit (2026-03-21, SV2A / Synaptic-Density PET Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`
- 副対象: `index.md`

## 今回の選定理由

- 2026-03-21 時点で，サイトは `SV2A PET = regional synaptic-density proxy` という上限自体はすでに持っていました。
- ただし，その表現だけではなお `SV2A PET` を一つの証拠クラスとして読み，`現在のシナプス効率` や `急性可塑性変化` と近いものとして誤読できる余地が残っていました。
- とくに，健康成人アトラス，疾患/リスク群比較，課題/認知相関，介入後の縦断比較は，測っているもの・比較設計・主張上限が同じではありません。
- 既存サイト内では，myelin / ionic / bioenergetic / astrocyte / clearance / ECM / cargo / sleep replay には個別ルートカードがある一方で，SV2A PET にはその監査面がまだ不足していました。

## 主要な批判点

### 1. `SV2A PET` がなお一つのバケツとして読める状態でした

- 問題:
  - 既存記述は `regional synaptic-density proxy` という ceiling を与えていました。
  - しかし，それだけでは `どの比較設計の話か` が弱く，健康アトラス，病態差，課題相関，薬理介入を同じ語で処理できてしまいました。
- 根拠:
  - Finnema et al. (2016) は living-human SV2A PET の成立と temporal lobe epilepsy での感度を示しました。
  - Johansen et al. (2024) は healthy-human atlas です。
  - Shatalina et al. (2024) は healthy-human の task / cognition association です。
  - Holmes et al. (2022) は ketamine 24 h 後でも overall SV2A change を測定できなかったことを示しました。
- 今回実行した変更:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` に `#sv2a-route-card` を追加しました。
  - `claim family / tracer / quantification / comparison design / functional target / abstention boundary` を固定しました。

### 2. 測定モデル依存性が front door 側でまだ弱く見えていました

- 問題:
  - サイトは PET 一般について `measurement model が必要` と述べていました。
  - しかし SV2A PET 固有には，`tracer / arterial vs reference / compartment model / simplified window / anatomy handling` が one-line ceiling より前に見えていませんでした。
- 根拠:
  - Naganawa et al. (2021) は tracer と quantification route が結果解釈の一部であることを示しています。
  - Smart et al. (2021) は短い visual activation で tracer influx が変わっても binding measure 自体は不変であり，momentary synaptic efficacy meter ではないことを示しています。
- 今回実行した変更:
  - `wiki/measurement-stack-and-claim-ceiling.md` の PET caution を SV2A 固有の route-family 差分まで拡張しました。
  - `verification.md` に `synaptic-density PET is not one audit item` を追加し，提出ルール側へ昇格しました。

### 3. トップページ群に「どこをどう読むべきか」の導線が不足していました

- 問題:
  - 詳細 wiki を読めば ceiling は分かるものの，`index.md` と `wbe_101.md` の入口ではまだ `synaptic-density PET exists = current synaptic state is nearly readable` という誤解を防ぎ切れていませんでした。
- 根拠:
  - Johansen / Shatalina / Smart / Holmes は同じ `SV2A PET` でも答える問いが違います。
  - したがって，front door で route card へのリンクを出す必要がありました。
- 今回実行した変更:
  - `index.md` に front-door note を追加しました。
  - `wbe_101.md` に entry-point note と reference を追加しました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `SV2A / synaptic-density PET` 専用 route card を追加
  - `Practical interpretation` に human synaptic-density PET を明示
  - dangerous misreading 行を追加
  - Smart / Holmes を reference に追加
- `wiki/measurement-stack-and-claim-ceiling.md`
  - page highlight を追加
  - PET caution を SV2A の route-family 差分まで拡張
  - Shatalina / Holmes を reference に追加
- `verification.md`
  - page highlight を追加
  - `synaptic-density PET is not one audit item` note を追加
  - Shatalina / Holmes を reference に追加
- `wbe_101.md`
  - page highlight を追加
  - SV2A route-card note を追加
  - Shatalina / Holmes を reference に追加
- `index.md`
  - front-door highlight を追加
  - `If You Are Treating Synaptic-Density PET As Current Synaptic State` note を追加

## 検証方針

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`

## 外部依存で保留

- なし
  - 今回の変更は，文献調査，本文修正，ビルド確認，push までこのセッション内で完結可能です。

## 参考文献

- Finnema SJ, Nabulsi NB, Eid T, et al. Imaging synaptic density in the living human brain. *Science Translational Medicine*. 2016;8(348):348ra96.
  - https://doi.org/10.1126/scitranslmed.aaf6667
- Naganawa M, Li S, Nabulsi N, et al. First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. *Journal of Nuclear Medicine*. 2021;62(4):561-567.
  - https://doi.org/10.2967/jnumed.120.249144
- Smart K, Liu H, Matuskey D, et al. Binding of the synaptic vesicle radiotracer [11C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021;41(5):1067-1079.
  - https://doi.org/10.1177/0271678X20946198
- Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
  - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
- Shatalina E, Onwordi EC, Whitehurst T, et al. The relationship between SV2A levels, neural activity, and cognitive function in healthy humans: A [11C]UCB-J PET and fMRI study. *Imaging Neuroscience*. 2024;2:1-16.
  - https://doi.org/10.1162/imag_a_00190
- Holmes SE, Finnema SJ, Naganawa M, et al. Imaging the effect of ketamine on synaptic density (SV2A) in the living brain. *Molecular Psychiatry*. 2022;27(4):2273-2281.
  - https://doi.org/10.1038/s41380-022-01465-2
