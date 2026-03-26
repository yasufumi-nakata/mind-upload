# Site Deepening Audit (2026-03-26, beginner three-axis human proxy / bridge sync)

## 対象

- 主対象: `wiki/mind-upload-basics.md`
- 副対象: `wiki/index.md`
- エクスポート同期: `github-wiki-export/mind-upload-basics.md`
- web確認対象:
  - `https://doi.org/10.1523/JNEUROSCI.1750-23.2024`
  - `https://doi.org/10.1038/s41467-025-66124-w`
  - `https://doi.org/10.1093/pnasnexus/pgaf072`
  - `https://doi.org/10.1016/j.neurobiolaging.2024.12.012`
  - `https://doi.org/10.1038/s41467-025-58356-7`
  - `https://doi.org/10.1038/s41593-025-02073-3`
  - `https://doi.org/10.1038/s41467-026-68374-8`
  - `https://doi.org/10.1038/s41467-023-44363-z`
  - `https://doi.org/10.1038/s41467-025-64414-x`
  - `https://doi.org/10.1016/j.crmeth.2023.100520`
  - `https://doi.org/10.1038/s41598-024-70609-x`

## 今回この箇所を選んだ理由

- コア公開ページではすでに、
  - `proxy class`
  - `operational maturity`
  - `calibrator role`
  - `Human Proxy Composition Card`
  - `State-Continuity Bridge Card`
  をかなり明確に扱っていました。
- しかし初心者導線の `wiki/mind-upload-basics.md` は、なお `human evidence` を実質的に `proxy class + route maturity` の二軸に近く読ませており、`BBB permeability / exchange proxy` も front-door の表に独立 row として出ていませんでした。
- その結果、読者が
  - `human proxy rows increased`
  - `same-subject multimodal`
  - `same-brain`
  を、
  - `one improving human observability ladder`
  - `one latent-state sample`
  に近く読める余地が残っていました。
- これは技術 / 自然科学の観点で弱いです。一次文献が示しているのは、living-human route の増加、bundle composition の妥当性、same-state bridge の成立が別問題だということだからです。

## 根拠付き批判

### 1. beginner front door がまだ `human observability` を一段の上昇ラダーに近く読ませていました

- [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024) は `regional synaptic-density proxy atlas` を押し上げました。
- [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) は `parcel-level biochemical scaffold` を押し上げました。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は `kinetic energetic-rate imaging` を押し上げました。
- [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) と [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は `BBB permeability / exchange proxy` を押し上げました。
- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) と [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は `macro support-state / clearance-support physiology` を押し上げました。

批判:

- これらは同じ inferential object ではありません。
- beginner page が `proxy class` と `route maturity` だけで止まると、`what this route safely calibrates` が抜け落ち、結果として `human evidence improved` が `same-state closure is getting closer` に読み替わりやすくなります。

### 2. `BBB permeability / exchange proxy` が beginner table から欠けていたのは front-door として不十分でした

- [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は humans で multi-echo ASL により BBB water-permeability route を示しました。
- [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は total-body PET と kinetic modeling により molecular BBB permeability-surface area product を示しました。

批判:

- これは `neurovascular / BBB / pericyte family` の human-side observability を押し上げる重要な row です。
- beginner page がここを front-door で独立 class として出さないままだと、読者は neurovascular / BBB family を `vascular nuisance` や `generic support state` の下位語として読み続けてしまいます。

### 3. `more human rows` を `one same-state sample` に止める composition / bridge line が beginner page で弱いままでした

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は simultaneous multimodal recordings に common と divergent structure の両方が残ることを示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で tightly coupled temporal progression と distinct network patterns の共存を示しました。
- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520) は preservation route が extracellular-space retention を変えることを示しました。
- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) は 10-hour EEG dynamics が adaptive decoders を要請するほど drift することを示しました。

批判:

- したがって `same-subject`, `same-brain`, `multimodal` は、それだけでは `same-state` の証拠ではありません。
- beginner page がこの停止線を front-door で書かないままだと、深いページへ行く前に `bundle = closure` の誤読が再発します。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `last_updated` を `2026-03-26` に更新
  - `page_highlights` を `two-axis` から `three-axis + bridge/composition` に更新
  - `known_points` に BBB permeability / exchange proxy を加えました
  - `Wiki: State-Continuity Bridge` への導線を front matter に追加
  - 冒頭 note を `human evidence is three axes plus bridge / composition stop lines` に改稿
  - `Why even a beginner page now needs a human observability ladder` を三軸 table に改稿
  - table に `BBB permeability / exchange routes` row を追加
  - `More rows do not yet make one same-state sample` note を追加し、composition / bridge 停止線を beginner front door に明示
  - 結語の導線を `Human Proxy Composition` と `State-Continuity Bridge` まで拡張
  - 参考文献に Padrela 2025, Chung 2025, Vafaii 2024, Chen 2025, Lu 2023, Egger 2024 を追加

- `wiki/index.md`
  - `last_updated` を `2026-03-26` に更新
  - page highlight / known points に `three axes + bridge/composition` を追加
  - 冒頭 note を追加して beginner portal 全体の reading rule を同期
  - human proxy row を `Human Proxy Composition + State-Continuity Bridge` 併記に更新
  - next public page に `State-Continuity Bridge Card` への導線を追加

- `github-wiki-export/mind-upload-basics.md`
  - 上記 public wiki の変更を export 側へ同期

## 今回止めた誤読

- `human evidence improved = one monotonic human observability ladder`
- `proxy class + maturity = enough to read same-state progress`
- `BBB permeability route = generic support-state background`
- `same-subject / same-brain / multimodal = one latent-state sample`
- `more human rows = state closure is nearly solved`

## 外部依存タスク

- なし
  - 今回の修正は repo 内の公開本文、学習導線、export 同期、監査記録で完結しました。

## 参考文献

1. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *J Neurosci*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nat Commun*. 2025;16:11344.
   - https://doi.org/10.1038/s41467-025-66124-w
3. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
4. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiol Aging*. 2025;147:176-186.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
5. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nat Commun*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
6. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nat Neurosci*. 2025;28:2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nat Commun*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
8. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nat Commun*. 2024;15:229.
   - https://doi.org/10.1038/s41467-023-44363-z
9. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nat Commun*. 2025;16:8887.
   - https://doi.org/10.1038/s41467-025-64414-x
10. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Rep Methods*. 2023;3(8):100520.
   - https://doi.org/10.1016/j.crmeth.2023.100520
11. Egger J, Kostoglou K, Müller-Putz GR. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Sci Rep*. 2024;14:20449.
   - https://doi.org/10.1038/s41598-024-70609-x
