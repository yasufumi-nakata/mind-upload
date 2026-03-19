# Site Deepening Audit (2026-03-20, Literature Front Door Sync)

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `research_harvest_50.md`

## 今回の選定理由

- 2026-03-20 時点で、コアページ側では `human observability` を proxy class ごとに分け、さらに `route maturity / model burden` を別軸で読む規則がかなり明確になっていました。
- その一方で、文献入口である `mind_uploading_papers.md` と `research_harvest_50.md` は、なお 2025-2026 の更新を十分に吸収しきれておらず、特に
  - dynamic DMRSI による kinetic glucose-rate imaging
  - sleep-linked clearance physiology
  - transcriptional stabilization gate
  - astrocyte multiday trace / astrocyte-enabled neural representation
  が front door の読解規則へ十分に織り込まれていませんでした。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、文献入口で規則が粗いと、コアページ側でいくら ceiling を厳密化しても、読者が最初に `proxy-rich human evidence = hidden-state closure` や `maintenance-state paper = generic support background` と誤読してしまうからです。

## 根拠付き批判

### 1. 旧 literature front door は `human observability` を route class と route maturity の 2 軸で固定できていませんでした

- 問題:
  - 旧 `mind_uploading_papers.md` と `research_harvest_50.md` は、Shapson-Coe / Johansen / Lucchetti / Baadsvik / Rzechorzek / Hirschler を human observability の代表として並べていました。
  - しかし、`dynamic DMRSI` と `sleep-linked clearance physiology` が加わったことで、同じ `human proxy` でも inferential object と operational burden がかなり異なることを文献入口で明文化する必要がありました。
- 根拠:
  - Li et al. (2025) は dynamic deuterium MRSI と kinetic model により glucose transport / metabolic rates を推定しました。
  - Dagum et al. (2026) は investigational wearable と compartmental model を用いて、sleep-linked clearance physiology を論じました。
  - これらは Lucchetti et al. (2025) の static metabolic similarity scaffold や Rzechorzek et al. (2022) の macro thermometry と同じ種類の object ではありません。
- 批判:
  - したがって、文献入口で `human proxy` を 1 本の progress bar に見せる構造は、最新文献に照らして粗すぎます。
  - 少なくとも `何の proxy class か` と `どれだけ specialized / model-heavy か` を分けて読ませる必要がありました。

### 2. 旧 maintenance-state route は 2025-2026 の causal literature を十分に front door へ反映していませんでした

- 問題:
  - 旧ルートは sleep / myelin / metabolic support を中心に maintenance-state を読む構造でした。
  - しかし 2025-2026 の一次文献は、maintenance-state をより具体的な hidden-state family へ分解しています。
- 根拠:
  - Terceros et al. (2025) は thalamocortical transcriptional gates と time-dependent causal requirements を通じて memory stabilization を扱いました。
  - Dewa et al. (2025) は astrocytic ensemble が multiday trace として memory stabilization を支えることを示しました。
  - Bukalo et al. (2026) は astrocyte Ca2+ signaling が amygdala の memory-supporting neural representations を支えることを示しました。
- 批判:
  - これらを `support variables matter` の一般論へ戻してしまうと、`何が latent family として残るか` が再び曖昧になります。
  - 文献入口でも `transcriptional stabilization gates` と `astrocyte-state evidence` を独立した boundary paper として読ませる必要がありました。

### 3. コアページと文献入口の非対称が、サイト内の evidence gate を弱めていました

- 問題:
  - `WBE 101` や `tech_roadmap.md` では、proxy class と route maturity を二軸で読む規則や、maintenance-state を複数 hidden-state family へ分ける規則が既にかなり明示されていました。
  - しかし文献入口では、その規則がまだ要約されきっておらず、読者が最初に古い読み方をしてしまう余地がありました。
- 批判:
  - 文献入口が緩いと、後段の厳しい page rule が見落とされます。
  - したがって、文献入口側をコアページへ同期すること自体が、技術フロントドアの品質改善として必要でした。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - front matter の `known_points` / `page_highlights` に、`proxy class x route maturity` と `maintenance-state = transcriptional / astrocyte evidence を含む` という規則を追加しました。
  - `If you want the 2026 technical addendum first` note を追加し、Li (2025), Dagum (2026), Terceros (2025), Dewa (2025), Bukalo (2026) を front door へ明示しました。
  - `technical-fast-lane` の human observability row を、dynamic DMRSI と sleep-linked clearance を含む形へ更新しました。
  - 同 row で、proxy class と route burden を別軸で読む site rule を本文へ織り込みました。
  - `maintenance-state / mechanistic boundary` row を、transcriptional stabilization gate と astrocyte multiday trace を含む形へ更新しました。
  - note boxes と evidence-class table も同規則へ同期しました。
- `research_harvest_50.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - front matter の `page_highlights` / `known_points` を同じ規則へ更新しました。
  - technical priority route の導入段落へ Li (2025), Dagum (2026), Terceros (2025), Dewa (2025), Bukalo (2026) を追加しました。
  - `Measurement and human observability` row に `route maturity / model burden` の確認を追加しました。
  - `maintenance-state` row に `transcriptional stabilization` と `astrocyte multiday trace` を追加しました。
  - `Read maintenance-state papers as more than support background` note を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文の更新と監査メモの記録で完結しております。

## 参考文献

1. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
2. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
3. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09774-6
4. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
5. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
6. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
7. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
8. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024.
   - https://doi.org/10.1126/science.adk4858
