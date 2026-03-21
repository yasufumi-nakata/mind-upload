# 2026-03-22 site deepening audit: electrical-state route card

## 対象
- `shared extracellular / electrical state`
- 対象ページ:
  - `verification.md`
  - `wiki/connectome-is-not-enough.md`
  - `github-wiki-export/connectome-is-not-enough.md`
  - `wbe_101.md`
  - `index.md`
  - `faq.md`
  - `perspective.md`

## 今回の選定理由
- 既存サイトは「chemical connectome は electrical-state complete ではない」という警告自体は持っていましたが、`どの種類の electrical-state claim なのか` を公開ルールとして分離していませんでした。
- この欠落により、局所 gap junction 論文、ephaptic / endogenous-field 論文、inhibitory driving-force 論文、activity-dependent electrical-synapse remodeling 論文、ヒト睡眠摂動論文が、同じ `electrical-state evidence` として過読されうる状態でした。
- さらに、Galarreta & Hestrin (1999) の DOI が公開ページ群で `10.1038/99496` と誤記されており、参照の完全性に実害がありました。正しい DOI は `10.1038/47029` です。

## 根拠付き批判
1. 推論対象の圧縮が強すぎました。
   - Galarreta & Hestrin (1999) は fast-spiking interneuron 間の `gap-junction coupling network` を示した論文です。
   - Anastassiou et al. (2011) は `endogenous-field / ephaptic effect on spike timing` を示した論文です。
   - Burman et al. (2023) は `active cortex における shunting-dominant inhibitory driving-force regime` を示した論文です。
   - Yang et al. (2024) は `activity-dependent electrical-synapse remodeling` を示した論文です。
   - Selfe et al. (2024) は `ORCHID による direct inhibitory-driving-force assay` を示した論文です。
   - Feld et al. (2026) は `human perturbation-conditioned clue` であり、局所 electrical state の直接 readout ではありません。
   - したがって、これらを 1 行の `electrical-state evidence` に圧縮すると、局所機構・特殊 assay・ヒト摂動ヒントの区別が崩れます。

2. Human observability ceiling の扱いが不十分でした。
   - ヒト側で現在もっとも近いのは Feld et al. (2026) のような睡眠中 coordination への pharmacological perturbation clue であり、`どの細胞が electrical coupling していたか` や `局所 inhibitory driving force が何であったか` を同定するものではありません。
   - それにもかかわらず route card がないと、局所 rodent / slice / optical evidence と human perturbation evidence が同じレベルで読まれる危険がありました。

3. 参照整合性に欠陥がありました。
   - 公開ページ群に Galarreta & Hestrin (1999) の DOI 誤記が複数残っていました。
   - 参照 DOI の誤りは、根拠の再検証可能性そのものを損なうため、内容上の弱さではなく公開科学基盤上の欠陥として扱うべきです。

## 今回実行した変更
- `verification.md`
  - page highlight を更新し、electrical-state claim に route card を必須化しました。
  - latent-state budget と maintenance-state budget の両方に `Shared extracellular / electrical state` 行を追加しました。
  - addendum を `electrical-state evidence also needs a route card` に更新し、claim family / direct observable / spatial regime / perturbation-calibration route / human evidence class / abstention を明文化しました。
- `wiki/connectome-is-not-enough.md`
  - electrical-state セクション本文を更新し、Burman et al. (2023) を加えて論点を `gap junction / endogenous field / driving-force regime / remodeling / human clue` に分離しました。
  - `#electrical-state-route-card` を新設し、route-card table と operational rule を追加しました。
  - references の DOI を修正しました。
- `github-wiki-export/connectome-is-not-enough.md`
  - source wiki の変更を手作業で同期しました。
  - このリポジトリでは export 側に未整理の差分が別件で残っていたため、今回は touched page のみを明示的に同期しました。
- `wbe_101.md`
  - entry page に `Electrical-state evidence now gets its own route card` note-box を追加しました。
  - electrical-state を route-card 必須として page highlight に反映しました。
  - references の DOI を修正しました。
- `index.md`, `faq.md`, `perspective.md`
  - electrical-state の入口説明を Burman / route-card 導線込みで更新しました。
  - 公開ページ上の DOI 誤記を修正しました。

## 外部依存で保留
- タスク: living-human local electrical-state の直接 calibration route
  - 担当: invasive human electrophysiology / optical method を扱う実験研究者
  - 前提条件: 局所 electrical coupling または inhibitory driving force を安全に較正できる human-compatible assay
  - 完了条件: same-subject human で direct local electrical observable と外部 calibration を併記できること

## 参考文献
1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/47029
2. Anastassiou CA, Perin R, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nat Neurosci*. 2011;14(2):217-223.
   - https://doi.org/10.1038/nn.2727
3. Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ. Active cortical networks promote shunting fast synaptic inhibition in vivo. *Neuron*. 2023;111(22):3643-3658.e6.
   - https://doi.org/10.1016/j.neuron.2023.08.005
4. Yang Y-C, Wang G-H, Chou P, Hsueh S-W, Lai Y-C, Kuo C-C. Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. *PNAS*. 2024;121(8):e2313042121.
   - https://doi.org/10.1073/pnas.2313042121
5. Selfe JS, et al. All-optical reporting of inhibitory receptor driving force in the nervous system. *Nat Commun*. 2024;15:8913.
   - https://doi.org/10.1038/s41467-024-53074-y
6. Feld GB, Niethard N, Liu J, et al. Electrical synapses contribute to sleep-dependent declarative memory retention. *Eur J Neurosci*. 2026;63(2):e70401.
   - https://doi.org/10.1111/ejn.70401
