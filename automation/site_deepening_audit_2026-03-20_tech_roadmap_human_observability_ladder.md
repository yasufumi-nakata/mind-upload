# Site Deepening Audit (2026-03-20, Tech Roadmap Human Observability Ladder)

## 対象

- 主対象: `tech_roadmap.md`
- 副対象: `summary_booklet.md`

## 今回の選定理由

- 2026-03-20 時点で、公開サイト本体は `WBE 101` と `Verification` において、human-side evidence をかなり丁寧に `proxy class` ごとへ分解できていました。
- その一方で、全体の依存関係を決める `tech_roadmap.md` では、なお `human で見えてきたもの` が 1 本の observability 向上物語に近く読める余地が残っていました。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、Roadmap は読者が `何を測る問題なのか` を最初に整理するページであり、ここが粗いと `proxy-rich human evidence` が `human state-complete measurement is getting close` へ誤変換されやすいからです。

## 根拠付き批判

### 1. 旧 `tech_roadmap.md` は human-side advance を `macro proxy vs local connectomics` の二分法へ寄せすぎていました

- 問題:
  - `M1` と `M3` は、non-invasive human measurement が macro proxy であり、same-brain connectomics が local scaffold を強めることは適切に述べていました。
  - しかし `human in vivo evidence` 自体の内部差、すなわち `local ultrastructure`、`SV2A PET atlas`、`1H-MRSI biochemical scaffold`、`dynamic DMRSI rate imaging`、`myelin bilayer mapping`、`CSF / glymphatic support proxy` が別々の evidence class であることを Roadmap 上で十分に見せていませんでした。
- 根拠:
  - Shapson-Coe et al. (2024) は human temporal cortex の 1 mm^3 ex vivo fragment を nanoscale で再構成し、局所 structural scaffold を押し上げました。
  - Johansen et al. (2024) は healthy humans 17F/16M の [11C]UCB-J PET を autoradiography で較正し、regional synaptic-density atlas を作りました。
  - Lucchetti et al. (2025) は five-metabolite 1H-MRSI profile から within-subject metabolic similarity matrix を構成し、51 healthy participants と independent replication 13 を示しました。
  - Li et al. (2025) は 7 T dynamic DMRSI と kinetic model を用い、5 healthy participants で CMRGlc / CMRLac / VTCA / Tmax を whole-brain imaging しました。
  - Baadsvik et al. (2024) は 2 healthy volunteers で myelin bilayer mapping を示しました。
  - Hirschler et al. (2025) は human CSF mobility の region-specific driver を specialized MRI で示しました。
  - Dagum et al. (2026) は randomized crossover trial 39 participants、investigational device、multicompartment model を用いて sleep-linked glymphatic clearance を論じました。
- 批判:
  - 以上はすべて `human evidence improved` の一文で括れる object ではありません。
  - Roadmap 上でこれを分けないと、読者は `人で色々な route が増えた` を `人で whole-brain current state が近い` と過大読みにしやすくなります。

### 2. 旧 Roadmap は evidence class と operational maturity を別軸として固定していませんでした

- 問題:
  - 旧記述は `what variable class the route constrains` にはある程度触れていましたが、`specialized hardware`、`small cohort`、`kinetic model burden`、`investigational device`、`same-subject fusion not shown` といった運用成熟度の差が弱く見えました。
- 根拠:
  - Lucchetti et al. (2025) は 51 + 13 の MRSI similarity scaffold であり、flux imaging ではありません。
  - Li et al. (2025) は 7 T、0.7 cc nominal voxel、blood input functions、kinetic modeling を前提とします。
  - Baadsvik et al. (2024) は 3 T でも high-performance RF / gradient hardware と multi-TE ultrashort acquisition を必要とし、2 volunteers の proof-of-principle でした。
  - Dagum et al. (2026) は sleep EEG / HRV / impedance plethysmography / dynamic impedance spectroscopy を組み合わせ、compartmental model を通じて plasma biomarker 変化を読んでいます。
- 批判:
  - したがって、`what it constrains` と `how field-ready it is` を分けない限り、proxy class と deployment maturity が混線します。
  - Roadmap はこの二軸を明示し、`proxy-rich but ceiling-limited` という読みを固定する必要がありました。

### 3. Roadmap から WBE 101 / Verification への復帰導線が、この論点ではまだ弱めでした

- 問題:
  - `WBE 101` と `Verification` には human observability ladder と Observability Budget がある一方、Roadmap 冒頭からそこへ入る導線が十分に目立っていませんでした。
- 批判:
  - Roadmap は dependency map です。
  - ここで `current human measurement ladder` と `submission-side stop rule` への復帰路を前面化しないと、後段の厳密な guardrail を読者が見落とします。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - `page_highlights` / `known_points` / `unknown_points` に、human in vivo evidence を `proxy class × route maturity` の 2 軸で読む site rule を追加しました。
  - 冒頭 note box に `WBE 101: human observability ladder` と `Verification: Observability Budget` への復帰導線を追加しました。
  - `M3` に `2026-03-20 addendum: human in vivo evidence is a two-axis ladder, not one progress bar` を追加しました。
  - 同 addendum に、local ultrastructure / SV2A PET / 1H-MRSI metabolic scaffold / dynamic DMRSI + myelin bilayer / CSF mobility + glymphatic clearance を比較する table を追加しました。
  - 参考文献へ Shapson-Coe (2024), Johansen (2024), Baadsvik (2024), Lucchetti (2025), Li (2025), Hirschler (2025), Dagum (2026) を追加しました。
- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` により再生成し、Roadmap の front matter 更新を冊子へ反映しました。
  - 併せて FAQ の `seven technical guardrails` が冊子側へ同期されることを確認対象に含めました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・自動生成冊子・監査メモの更新で完結しております。

## 参考文献

1. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
   - https://doi.org/10.1126/science.adk4858
2. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
3. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
4. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
5. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
6. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
