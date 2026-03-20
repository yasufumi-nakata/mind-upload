# Site Deepening Audit (2026-03-20, Literature Front Door Technical Shortlist)

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `research_harvest_50.md`

## 今回の選定理由

- 2026-03-20 時点で，文献入口はすでに `priority route` と `evidence class` を持っておりました。
- ただし，技術・自然科学の読者が最初に必要とするのは，広い年次アーカイブや U 番号表そのものではなく，`まずどの一次文献から読めば front door の論点が最短で立つか` という最小導線です。
- 現状の `mind_uploading_papers.md` は fast lane を入れた後でも，その先は mixed year cards に落ちるため，law / philosophy / cultural theory を含む年次順ノイズを再び踏みやすい状態でした。
- これは技術・自然科学の観点で重要です。理由は，最初の 5-10 分で読む文献の選び方が粗いと，foundation model, human observability, maintenance-state, direct validation, closed-loop communication という互いに異なる evidence class を再び混同しやすくなるからです。

## 根拠付き批判

### 1. 既存の fast lane は正しかったが，なお `最初の 1 本` を決めるには広すぎました

- 問題:
  - `mind_uploading_papers.md` は `priority route` と `technical evidence classes` を入れ，技術入口としてはかなり改善されていました。
  - しかし technical reader は，その後すぐ mixed year cards に落ちるため，依然として `どの anchor paper から始めるべきか` を自力で復元する必要がありました。
- 根拠:
  - Kostas et al. (2021), Jiang et al. (2024), Lee et al. (2025), EEG Challenge 2025 leaderboard, EEG-FM-Bench (2025), PRISM (2026) は，いずれも EEG foundation model を論じていますが，強めている論点は `pretraining gains` だけではなく `benchmark provenance` と `ranking stability` です。
  - Li et al. (2025) と Dagum et al. (2026) は human measurement frontier に入りますが，inferential object も route burden も大きく異なります。
  - Terceros et al. (2025), Dewa et al. (2025), Bukalo et al. (2026) は maintenance-state boundary papers であり，measurement advance ではありません。
- 批判:
  - したがって，技術読者に対しては `route` だけでなく `最初の anchor set` まで front door で固定しないと，evidence class の混同を完全には止め切れません。

### 2. 文献入口が混在構造のままだと，law / philosophy ノイズが再び初手へ戻ってきます

- 問題:
  - このアーカイブは intentionally broad であり，年次カードには law / philosophy / VR / cultural theory も含まれています。
  - これは archive としては正しい一方，technical reader の最初の導線としてはノイズが大きいです。
- 根拠:
  - EEG source validation の読み筋は Mikulan et al. (2020), Unnwongse et al. (2023), Hao et al. (2025) でかなり明確に立ちます。
  - speech / communication frontier の読み筋も Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025) で比較的短く固定できます。
- 批判:
  - つまり broad archive を維持したままでも，front door だけは `technical-only shortlist` を分離する方が科学的読解には適しています。
  - これは内容選別の問題ではなく，最初の evidence gate をどこに置くかの問題です。

### 3. `research_harvest_50.md` 側も，U番号から paper anchor へ飛ぶ橋がまだ弱めでした

- 問題:
  - `research_harvest_50.md` は U1/U7 → U4 → U13 → U8 → U3 → U10 の default route を明示しています。
  - ただし，読者によっては U 番号より先に `具体的な paper anchor` が欲しいため，paper archive との接続を明示した方が入口として強くなります。
- 根拠:
  - Li et al. (2025), Dagum et al. (2026), Terceros et al. (2025), Dewa et al. (2025), Bukalo et al. (2026) は，現在の technical route の中で `human observability` と `maintenance-state boundary` を短時間で立ち上げる anchor になります。
- 批判:
  - U-map と paper archive は役割が違いますが，front door では相互リンクを明示した方が技術読者の迷子が減ります。

## 今回実行した変更

- `mind_uploading_papers.md`
  - front matter の `known_points` / `page_highlights` に technical-only shortlist の役割を追加しました。
  - sidebar navigation に `2025-2026 technical-only shortlist` を追加しました。
  - 新規 section `technical-shortlist-20260320` を追加し，以下の 5 ルートを最小 front door として固定しました。
    - EEG foundation-model governance
    - human observability ladder
    - maintenance-state boundary papers
    - direct source-validation anchors
    - closed-loop communication frontier
  - 各行で `what gets stronger directly here` と `what still must not be claimed` を併記し，evidence class の混同を抑える形へしました。
  - technical reader 向けに，mixed year cards を後回しにしてよいことを明示しました。
- `research_harvest_50.md`
  - front matter の `page_highlights` / `known_points` に，paper-level technical shortlist への導線を追加しました。
  - `technical-priority-route-20260315` 節内へ note box を追加し，U-route から `mind_uploading_papers.html#technical-shortlist-20260320` へ直接跳べるようにしました。

## 外部依存で保留

- なし
  - 今回の変更は，公開本文の再構成と導線改善で完結しております。

## 参考文献

1. Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Frontiers in Human Neuroscience*. 2021.
   - https://doi.org/10.3389/fnhum.2021.653659
2. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR*. 2024.
   - https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html
3. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML poster / OpenReview*. 2025.
   - https://openreview.net/forum?id=J5SbLoq7Uv
4. EEG Foundation Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
5. EEG Foundation Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
6. Xiong W, Li J, Li J, Zhu K. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
7. Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
   - https://arxiv.org/abs/2603.02268
8. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
9. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
10. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09774-6
11. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
12. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
13. Mikulan E, Russo S, Parmigiani S, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020.
   - https://doi.org/10.1038/s41597-020-0467-x
14. Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. *Brain Communications*. 2023.
   - https://doi.org/10.1093/braincomms/fcad023
15. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
   - https://doi.org/10.1111/epi.18552
16. Willett FR, Avansino DT, Hochberg LR, Henderson JM, Shenoy KV. High-performance brain-to-text communication via handwriting. *Nature*. 2023.
   - https://doi.org/10.1038/s41586-023-06377-x
17. Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01905-6
18. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
