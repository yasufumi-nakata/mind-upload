# Site Deepening Audit (2026-03-20, Literature Maintenance-State Family Sync)

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `research_harvest_50.md`

## 今回の選定理由

- コアページ側では 2026-03-20 時点で、`maintenance-state` を単一の support bucket ではなく、`post-transcriptional RNA-state`、`phospho-signaling / second-messenger state`、`local proteostasis / synaptic-tagging state`、`cargo-transport / cytoskeletal trafficking state`、`astrocyte / glial-state` などの family に分けて読む規則がかなり明示されていました。
- その一方で、文献入口である `mind_uploading_papers.md` と `research_harvest_50.md` は、なお `transcriptional stabilization` と `astrocyte-state` を中心に maintenance-state を代表させる構造が残っており、`RNA / phospho / proteostasis / cargo` の family が front door で弱く見えていました。
- これは技術・自然科学の観点で優先度が高いです。理由は、文献入口の粗さが残ると、コアページでせっかく防いでいる `connectome + cell type + proxy-rich human evidence ≈ long-horizon closure` という誤読が再流入するからです。

## 根拠付き批判

### 1. 旧 literature front door は maintenance-state をまだ `generic support background` に寄せすぎていました

- 問題:
  - `mind_uploading_papers.md` の fast lane と `research_harvest_50.md` の technical route は、maintenance-state をかなり改善していました。
  - しかし front door で強調されていた family は主として `transcriptional stabilization` と `astrocyte multiday trace` であり、他の mechanistic families が見えにくいままでした。
- 根拠:
  - <https://doi.org/10.1038/s41586-018-0666-1> Shi et al. (2018) は m6A reader を介して hippocampus-dependent learning and memory が変わることを示しました。
  - <https://doi.org/10.1126/scisignal.adr1442> Peterson et al. (2025) は ADAR2-mediated GluA2 RNA editing が homeostatic synaptic plasticity に寄与することを示しました。
  - <https://doi.org/10.1038/s41467-023-40930-6> Vierra et al. (2023) は compartmentalized Ca2+/PKA signaling routing を示しました。
  - <https://doi.org/10.1080/15548627.2020.1775393> Pandey et al. (2021) は autophagy coupled to translation が long-term memory に必要であることを示しました。
  - <https://doi.org/10.1016/j.cub.2024.03.010> Aiken & Holzbaur (2024) は presynaptic cargo delivery の局所制御を示しました。
- 批判:
  - したがって、maintenance-state を `support variables matter` に近い書き方へ戻すのは、現在の一次文献に対して粗すぎます。

### 2. 旧 literature front door は `human observability ceiling` から RNA / phospho / proteostasis / cargo の未観測性を十分に明示していませんでした

- 問題:
  - `human observability / proxy ladder` は proxy class と route maturity をかなり丁寧に分けていました。
  - しかしその ceiling の列では、`current post-transcriptional RNA-state`、`current phospho-signaling / second-messenger state`、`branch-local proteostasis / tag-capture`、`branch- or bouton-specific cargo-routing` が十分に列挙されていませんでした。
- 根拠:
  - <https://doi.org/10.1038/s41593-024-01616-4> Joglekar et al. (2024) は specialized splicing pattern の atlas を示しましたが、whole-brain in vivo human route ではありません。
  - <https://doi.org/10.1021/acs.jproteome.2c00244> Biswas et al. (2023) は human brain phosphoproteome atlas を示しましたが、こちらも ex vivo atlas です。
  - 現在の human proxy routes は、Shapson-Coe / Johansen / Lucchetti / Li / Baadsvik / Rzechorzek / Hirschler / Dagum でそれぞれ別の observability class を押し上げていますが、これらは RNA processing, phosphosite occupancy, branch-local tag capture, local cargo routing を直接閉じていません。
- 批判:
  - したがって、文献入口でも `human proxy-rich evidence ≠ hidden-state closure` を、未観測 family の実名で書かなければ不十分でした。

### 3. technical route の `U3` が family decomposition を欠くと、U1/U7 と U3 の違いが再び曖昧になります

- 問題:
  - `research_harvest_50.md` では U1/U7 が human observability、U3 が maintenance-state です。
  - しかし U3 の説明が broad support wording に寄ると、`what humans can see today` と `what remains mechanistically latent` の違いが front door でぼやけます。
- 根拠:
  - <https://doi.org/10.1038/s41586-025-09774-6> Terceros et al. (2025) は transcriptional stabilization gate を、<https://doi.org/10.1038/s41586-025-09619-2> Dewa et al. (2025) と <https://doi.org/10.1038/s41586-025-10068-0> Bukalo et al. (2026) は astrocyte multiday trace / neural representation を押し上げました。
  - そこへ Shi / Peterson / Vierra / Pandey / Aiken を合わせると、U3 は一つの support bucket ではなく複数の hidden-state family の集合として読まなければならないことが明確です。
- 批判:
  - したがって U3 front door には family decomposition が必要でした。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `known_points` / `page_highlights` の maintenance-state bullet を、`transcriptional stabilization` と `astrocyte-state` だけでなく `post-transcriptional RNA control`、`phospho-signaling`、`local proteostasis`、`cargo-routing` まで含む表現へ更新しました。
  - `human observability / proxy ladder` row の ceiling を更新し、`current post-transcriptional RNA-state`、`current phospho-signaling / second-messenger state`、`branch-local proteostasis / synaptic-tag capture`、`branch- or bouton-specific cargo-routing`、`cell-specific immune-controller state` を明示しました。
  - `maintenance-state / mechanistic boundary` row を更新し、RNA / phospho / proteostasis / cargo families を boundary wording に追加しました。
  - `Read maintenance-state papers as route-changing evidence` note を更新し、Shi / Peterson / Vierra / Pandey / Aiken を追加して family decomposition を明文化しました。
  - `technical-only shortlist` の maintenance-state row に、2025-2026 anchors は broader maintenance-state family の一部であることを追記しました。
- `research_harvest_50.md`
  - `page_highlights` / `known_points` の maintenance-state bullet を、RNA / phospho / proteostasis / cargo families まで含む表現へ更新しました。
  - technical priority route の `U3` row を更新し、`post-transcriptional RNA control`、`phospho-signaling`、`local proteostasis / tag-capture balance`、`cargo-routing state` を追加しました。
  - `Read human measurement papers as their own evidence class` note に、human observability からなお落ちる latent-state ceilings を追記しました。
  - `Read maintenance-state papers as more than support background` note を更新し、Shi / Peterson / Vierra / Pandey / Aiken を追加して family decomposition を明文化しました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文の同期と監査メモの追加で完結しております。

## 参考文献

1. Shi H, Zhang X, Weng Y-L, et al. m6A facilitates hippocampus-dependent learning and memory through YTHDF1. *Nature*. 2018;563:249-253.
   - https://doi.org/10.1038/s41586-018-0666-1
2. Peterson LN, Kasper JM, Allgaier JA, et al. ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. *Science Signaling*. 2025;18(886):eadr1442.
   - https://doi.org/10.1126/scisignal.adr1442
3. Vierra NC, et al. Endoplasmic reticulum-plasma membrane junctions couple electrical activity to Ca2+-activated PKA signaling in neurons. *Nature Communications*. 2023;14:6040.
   - https://doi.org/10.1038/s41467-023-40930-6
4. Pandey K, Yu X-W, Steinmetz A, Alberini CM. Autophagy coupled to translation is required for long-term memory formation. *Autophagy*. 2021;17(9):2489-2505.
   - https://doi.org/10.1080/15548627.2020.1775393
5. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Current Biology*. 2024;34(8):1687-1704.e8.
   - https://doi.org/10.1016/j.cub.2024.03.010
6. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09774-6
7. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
8. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
9. Joglekar A, Prjibelski A, Mahfouz A, et al. Single-cell long-read sequencing-based mapping reveals specialized splicing patterns in developing and adult mouse and human brain. *Nature Neuroscience*. 2024;27(6):1073-1088.
   - https://doi.org/10.1038/s41593-024-01616-4
10. Biswas D, et al. The landscape of the human brain phosphoproteome reveals region-specific phosphorylation events. *Journal of Proteome Research*. 2023;22(4):1390-1404.
   - https://doi.org/10.1021/acs.jproteome.2c00244
