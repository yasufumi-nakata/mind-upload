# Site Deepening Audit (2026-03-14, Language Prior / Brain-to-Text)

## 対象

- 主対象: `perspective.md`

## 今回の選定理由

- `perspective.md` はサイト内でもっとも長く、立場表明として参照されやすいページです。
- その一方で、旧版の `LLM研究アップデート` 節は、brain-to-text の一次文献と、汎用LLMの運用論を同じレベルで並べていました。
- これは技術・自然科学の観点では弱点です。なぜなら、脳解読の主要な制約は RLHF や RAG の有無ではなく、`神経寄与の切り分け`、`課題依存性`、`streaming 運用の tail latency`、`drift / recalibration`、`subject cooperation` にあるからです。

## 主要な批判点

### 1. 旧版は「脳解読の証拠」と「汎用LLMの便利機能」を混同していました

- 問題:
  - 旧版は RLHF、DPO、QLoRA、RAG、ReAct、Toolformer、SelfCheckGPT を並べていましたが、これらは brain-to-text の主要な一次証拠ではありません。
  - そのため、読者が「LLM周辺技術を足せば脳解読の壁を越えられる」と誤読する余地がありました。
- 根拠:
  - Tang et al. (2023) は non-invasive semantic reconstruction を示しましたが、decoder の学習と適用の双方で参加者の協力が必要でした。
  - Défossez et al. (2023) は non-invasive brain recordings から 3 秒音声区間の識別を示しましたが、open-ended generation ではなく retrieval / identification に近い設定です。
  - d'Ascoli et al. (2025) は 723 参加者で単語デコードを示しましたが、モダリティ、課題、データ量が性能を大きく左右しました。
  - したがって、中心問題は「LM をどう便利に使うか」ではなく、「神経データが language prior をどこまで上回るか」を測ることです。
- 修正:
  - `perspective.md` の該当節を、generic LLM 論から `brain-to-text / speech neuroprosthesis / neural encoding` の一次文献レビューへ全面改稿しました。
  - site rule として、「汎用LLM論文は主証拠にしない」ことを本文へ明記しました。

### 2. 非侵襲 decode、侵襲 speech BCI、LLM埋め込みによる encoding が未分離でした

- 問題:
  - 旧版では「脳活動から文が出る」研究を一塊で扱っており、モダリティ差と証拠強度差が見えませんでした。
  - とくに、encoding model と decoder を同じ重みで読めてしまう点が危険でした。
- 根拠:
  - Horikawa et al. (2025) と Tang et al. (2023) は、非侵襲計測による semantic / caption reconstruction の前進です。
  - Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025) は、侵襲 speech neuroprosthesis の streaming / low-latency 実証です。
  - Zada et al. (2024) と Goldstein et al. (2025) は、LLM 埋め込みや意味関係表現が脳活動をよく予測する encoding evidence ですが、decoder truth ではありません。
- 修正:
  - `perspective.md` に `証拠階層を4つに分ける` 表を追加しました。
  - `非侵襲 semantic / caption decoding`、`非侵襲 word / speech decoding`、`侵襲 streaming speech neuroprosthesis`、`LLM 埋め込みによる neural encoding` を分離しました。
  - 各トラックごとに「今言えること」と「まだ言えないこと」を固定しました。

### 3. 言語事前分布の混入を監査する評価パックが不足していました

- 問題:
  - 旧版は `LLM由来ノイズ` を概念的に述べるだけで、何を baseline として並べるべきかが弱い状態でした。
  - これでは、candidate set が小さい課題や強い language prior が効く条件で、高い見かけ性能を過大評価してしまいます。
- 根拠:
  - Tang et al. (2023) は participant cooperation を必要とし、データ取得条件そのものが性能に直結することを示しました。
  - d'Ascoli et al. (2025) は modality、課題、データ量によって decode 性能が大きく変わることを示しました。
  - Littlejohn et al. (2025) と Wairagkar et al. (2025) は streaming communication で latency と silence / abstention が中核指標になることを示しました。
- 修正:
  - `最低限必要な評価パック` として、`brainなし`、`time-shuffle`、`trial-shuffle`、`LM-only`、`no-LM`、candidate set size、held-out / OOD、cross-day、latency、abstention、recalibration burden を本文へ追加しました。
  - 研究プログラム表の Phase 1 も、generic な「因果的整合性チェック」から、具体的な監査項目を伴う評価パックへ書き換えました。

### 4. decode の成功がそのまま WBE / emulate へ読める構造が残っていました

- 問題:
  - 旧版でも decode と emulate の差は述べていましたが、brain-to-text 節自体はなお楽観寄りに読める構造でした。
- 根拠:
  - invasive speech BCI の最良例は communication subsystem の closed-loop 改善です。
  - LLM embedding を使う neural encoding の成功は、「脳が言語モデルの表現空間に部分的に写る」ことを示しても、「脳の因果ダイナミクスを再現した」ことは示しません。
- 修正:
  - `Mind-Upload 側での運用ルール` を追加し、L1 / L2 / L3 の主張条件を固定しました。
  - `decode 成功、embedding 類似、会話の自然さを emulate / WBE / 本人性保存へ読み替えない` と明記しました。

## 今回実行した変更

- `perspective.md`
  - `LLM研究アップデート` 節を `Brain-to-Textアップデート：言語事前分布、streaming、evidence gate` へ全面改稿
  - `証拠階層を4つに分ける` 表を新設
  - `最低限必要な評価パック` と `Mind-Upload 側での運用ルール` を追加
  - 研究プログラム表の Phase 1 を、brain-to-text 評価パック中心へ修正
  - 2023-2025 の primary papers を参考文献へ追加

## 外部依存で保留

- brain-to-text の L3 benchmark 実装
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: 公開可能な streaming BCI ログ、latency / abstention / recalibration を含む評価データ
  - 完了条件: `brainなし / LMなし / shuffle / OOD / drift / latency` を同じベンチで再現できること

## 参考文献

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- Horikawa T, et al. Mind captioning: Evolving descriptive text of mental content from human brain activity. Sci Adv. 2025.
  - https://doi.org/10.1126/sciadv.adw1464
- Défossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. Nat Mach Intell. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Zada Z, Goldstein A, et al. Contextual embeddings from deep language models predict fMRI responses to naturalistic language. Neuron. 2024.
  - https://doi.org/10.1016/j.neuron.2024.09.018
- Goldstein A, Bar A, et al. Connecting concepts in the brain by mapping cortical representations of semantic relations. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01903-8
