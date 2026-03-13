# Site Deepening Audit (2026-03-14, WBE Route / Decode-Emulate)

## 対象

- 主対象: `wbe_101.md`
- 副対象: `wiki/decode-vs-emulate.md`

## 今回の選定理由

- `wbe_101.md` は公開サイトの入口であり、ここでの比較軸が甘いと下位ページ全体の読み方が歪みます。
- 既存の「代替アプローチとの比較」は、技術・自然科学の証拠比較よりも、立場選好や将来像の比較に読める構造でした。
- `wiki/decode-vs-emulate.md` は参照頻度の高い補助ページですが、概念説明に止まり、一次文献ベースの境界事例が不足していました。

## 主要な批判点

### 1. `wbe_101.md` の比較表が「技術ルート比較」ではなく「立場選好」に見えていた

- 問題:
  - 既存表は `段階的置換（Mind-Upload採用）` と明示しており、入口ページで route preference を先に固定していました。
  - しかし、2026年3月時点で一次文献が強く支えるのは、非侵襲 decode、侵襲 speech BCI、局所 closed-loop 義継、connectomics + function、局所 digital twin です。
  - neuron-by-neuron の全脳置換 benchmark を公開一次文献として確認できていない段階で、特定 route を「採用」と前面に出すのは、証拠の強さより先に結論を置く書き方でした。
- 根拠:
  - Tang et al. (2023) は非侵襲 fMRI で連続言語の意味復元を示したが、decode であり subject cooperation が必要です。
  - Willett et al. (2023) は侵襲 speech BCI で 62 words/min, 125,000 語語彙を示したが、これも attempted speech decode が中心です。
  - Flesher et al. (2021) は tactile feedback を返す双方向 BCI で把持課題を改善したが、全脳ではなく感覚運動サブシステムの closed loop 実証です。
  - Berger et al. (2011) は海馬で局所義継を示したが、課題特異的・局所的です。
- 修正:
  - `wbe_101.md` の比較表を、`ルート / いま公表されている実証 / ここまでなら言える / まだ欠けるもの` の4列へ再構成しました。
  - 比較軸を、哲学的連続性ではなく `計測密度 / 介入可能性 / 閉ループ実証 / state completeness` に変更しました。

### 2. 既存の比較表は connectomics と simulation の限界を粗く書きすぎていた

- 問題:
  - `全脳シミュレーション` は「最も忠実な再現が可能」と書かれていましたが、これは parameter identifiability の難しさを飛ばした表現でした。
  - `スキャン＆コピー` も「必要解像度が非現実的」とだけ書かれており、どの状態変数が欠けるのかが見えませんでした。
- 根拠:
  - Dorkenwald et al. (2024) と MICrONS Consortium et al. (2025) は、connectome と機能計測の結合がようやく大きく前進した段階であることを示しています。
  - Billeh et al. (2020) は data-driven multi-scale V1 model を構築しましたが、領域限定・課題限定の model です。
  - Prinz et al. (2004) は、ほぼ同じ network activity が大きく異なる内部パラメータ集合から生じうることを示しており、出力一致だけでは faithful simulation を保証しません。
- 修正:
  - connectomics を `構造 atlas / scaffold / hypothesis engine` として位置づけ直しました。
  - simulation を `機序仮説のテストと局所 digital twin` とし、`同定可能性が解けない限り output match は十分でない` と明記しました。

### 3. `wiki/decode-vs-emulate.md` が概念説明に止まり、境界事例が文献で支えられていなかった

- 問題:
  - 既存ページは日常例中心で、Tang 2023 や Willett 2023 のような強い decode 事例、Flesher 2021 や Berger 2011 のような局所 closed-loop 義継事例が入っていませんでした。
  - そのため、「何が decode の上限か」「何が局所 emulate に近いか」が読者に見えにくい構造でした。
- 根拠:
  - Tang 2023 は非侵襲 decode の上限例です。
  - Willett 2023 は侵襲 decode の上限例です。
  - Flesher 2021 と Berger 2011 は causal / closed-loop の側へ進んだ局所証拠です。
- 修正:
  - `一次文献で見る境界事例` 節を新設し、4 つの route を decode → local emulate の勾配で並べました。
  - `4 つのゲート` として、OOD 一般化、介入一致、閉ループ安定性、state completeness を固定しました。

### 4. 入口ページの参考文献セットが、今回の技術比較と一致していなかった

- 問題:
  - 既存の `wbe_101.md` 参考文献には哲学文献が含まれており、今回更新した `技術ルート比較` 節の根拠とは整合していませんでした。
- 修正:
  - 参考文献を、Tang / Willett / Flesher / Berger / Dorkenwald / MICrONS / Billeh / Prinz 中心に差し替え、今回の比較表を直接支えるセットへ整理しました。

## 今回実行した変更

- `wbe_101.md`
  - `代替アプローチとの比較` 節を `技術ルートの比較（観測可能な証拠ベース）` へ全面改稿
  - route preference を削除し、公開一次文献の evidence profile 比較へ変更
  - 参考文献を技術・自然科学中心へ差し替え
- `wiki/decode-vs-emulate.md`
  - front matter を技術・自然科学向けに更新
  - 概念説明だけだった本文を、一次文献つきの境界事例ページへ拡張
  - `4つのゲート` と `このサイトでの運用ルール` を追加

## 外部依存で保留

- 全脳スケールの hybrid replacement / gradual replacement に関する公開 benchmark の継続監視
  - 担当者: AI / maintainer
  - 前提条件: 新規一次文献または公開データセットの出現
  - 完了条件: neuron-by-neuron ないし multi-area replacement を評価する再現可能 benchmark を確認し、`wbe_101.md` の比較表へ追加

## 参考文献

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science. 2021.
  - https://doi.org/10.1126/science.abd0380
- Berger TW, Hampson RE, Song D, et al. A cortical neural prosthesis for restoring and enhancing memory. J Neural Eng. 2011.
  - https://doi.org/10.1088/1741-2560/8/4/046017
- Dorkenwald S, McKellar CE, Macrina T, et al. Neuronal wiring diagram of an adult brain. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Billeh YN, Cai B, Gratiy SL, et al. Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex. Neuron. 2020.
  - https://doi.org/10.1016/j.neuron.2020.01.040
- Prinz AA, Bucher D, Marder E. Similar network activity from disparate circuit parameters. Nat Neurosci. 2004.
  - https://doi.org/10.1038/nn1352
