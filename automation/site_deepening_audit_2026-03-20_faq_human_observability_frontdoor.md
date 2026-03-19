# Site Deepening Audit (2026-03-20, FAQ Human Observability Front Door)

## 対象

- 主対象: `faq.md`
- 副対象: `summary_booklet.md`

## 今回の選定理由

- 2026-03-20 時点で、`WBE 101`、`tech_roadmap.md`、`wiki/measurement-stack-and-claim-ceiling.md` では、human observability を `proxy class x route maturity` の二軸で読む規則がかなり整っていました。
- その一方で、最初に多くの読者が開く `faq.md` では、この論点がまだ `Q2c` の長い hidden-state 説明に埋もれ気味で、独立した front-door stop rule としては弱めでした。
- これは技術・自然科学の観点で優先度が高いです。FAQ 入口が粗いと、読者は `human proxy-rich evidence` を `human state-complete measurement is getting close` と誤読したまま、後段の厳密な claim ceiling を読む前に結論を作ってしまうからです。

## 根拠付き批判

### 1. 旧 FAQ は `connectome is not enough` と `human observability is layered` を同じ Q2c に詰め込みすぎていました

- 問題:
  - 旧 `Q2c` は非常に重要でしたが、`connectome + cell type でも hidden state が残る` という論点と、`human measurement route が増えても proxy class が違う` という論点を同時に処理していました。
  - そのため、human-side evidence の読解規則が独立した front-door stop rule として見えにくくなっていました。
- 根拠:
  - `connectome insufficiency` を支える論文群と、`human observability ladder` を支える論文群は同じ問いに答えていません。
  - Shapson-Coe et al. (2024) は `1 mm^3` の human temporal cortex を nanoscale で再構成し、local ex vivo structural scaffold を押し上げました。
  - Johansen et al. (2024) は healthy humans `17F/16M` の SV2A PET atlas を postmortem autoradiography で較正し、regional synaptic-density proxy を示しました。
  - Lucchetti et al. (2025) は five-metabolite `1H-MRSI` から `51` healthy participants と independent replication `13` の metabolic similarity scaffold を示しました。
  - Li et al. (2025) は `7 T` dynamic DMRSI と kinetic model を用いて `5` healthy participants の glucose-related rate imaging を行いました。
  - Baadsvik et al. (2024) は `2` healthy volunteers で myelin bilayer mapping を示しました。
  - Hirschler et al. (2025) は `24` healthy participants の specialized MRI route で CSF mobility を示しました。
  - Dagum et al. (2026) は randomized crossover trial `39 participants`、investigational device、multicompartment model を通して sleep-linked glymphatic clearance physiology を論じました。
- 批判:
  - 以上はどれも `connectome の不足` とは別の入口論点です。
  - FAQ で独立 Q として分けないと、読者は `hidden state は多い` という一般論だけ覚え、`human route は何を直接強めたのか` を区別しないまま先へ進みます。

### 2. 旧 FAQ は `proxy class` と `route maturity / model burden` を初心者の停止条件として固定していませんでした

- 問題:
  - 旧文面でも human evidence が ladder であること自体は述べられていました。
  - しかし `what it constrains` と `how specialized / model-heavy it is` を FAQ の時点で明示的に二軸化していませんでした。
- 根拠:
  - Johansen et al. (2024) は atlas resource として重要ですが、cohort-level regional synaptic-density proxy です。
  - Lucchetti et al. (2025) は whole-brain biochemical scaffold を押し上げますが、flux imaging ではありません。
  - Li et al. (2025) は 7 T・dynamic acquisition・kinetic model・blood input を要する specialized energetic route です。
  - Baadsvik et al. (2024) は two-volunteer proof-of-principle であり、高性能ハードウェア依存です。
  - Dagum et al. (2026) は investigational wearable と multicompartment model に依存します。
- 批判:
  - したがって `human evidence exists` とだけ言うと、読者は proxy class と field-readiness を同時に過大評価します。
  - FAQ は短文であるほど、`proxy class` と `route maturity` を別々に読めという停止条件を明示する必要がありました。

### 3. 旧 FAQ には beginner-level comparison table がありませんでした

- 問題:
  - `WBE 101` には ladder table がありましたが、FAQ には `最短で比較できる 3 列 table` がありませんでした。
- 批判:
  - その結果、読者は強い 1 本の段落を読むだけで終わりがちで、`what it strengthens` と `what it still does not give you` を視覚的に分離できませんでした。
  - FAQ には長大な理論説明より、比較表の方が stop rule として機能します。

## 今回実行した変更

- `faq.md`
  - `page_highlights` の `seven technical guardrails` を `eight technical guardrails` に更新し、`human proxy-rich evidence is not automatically near-direct whole-brain state readout` を front-door guard として追加しました。
  - `known_points` に、human measurement advances を `proxy class x route maturity` で読む site rule を追加しました。
  - 上部 note box も `Eight technical guards now fixed at the front door` に更新しました。
  - 導線 table に `Q2d` を追加し、`Know what humans can actually observe today` という入口を新設しました。
  - 新規 section `Q2d. If human measurement keeps improving, are we close to state-complete readout?` を追加しました。
  - 同 section に、Shapson-Coe / Johansen / Lucchetti / Li / Baadsvik / Hirschler / Dagum を `what it strengthens` と `what it still does not give you` で読む比較 table を追加しました。
  - 同 section に、FAQ でも `proxy class` と `route maturity / model burden` を別軸で読む明示ルールを追加しました。
  - References に上記 7 本の一次文献を追加しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成し、FAQ の新しい human-observability front-door 改稿を冊子側へ反映しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文、生成物、監査メモの更新で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
4. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
5. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
6. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28:2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
