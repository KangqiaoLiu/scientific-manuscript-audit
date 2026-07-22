# Scientific Manuscript Audit

**Codex と Claude Code 向けの、主張中心・証拠ベースの科学論文監査スキル。**

[English](README.md) | [简体中文](README.zh-CN.md) | 日本語

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.1.0--rc.3-orange.svg)](CHANGELOG.md)
[![Validation](https://github.com/KangqiaoLiu/scientific-manuscript-audit/actions/workflows/validate.yml/badge.svg)](.github/workflows/validate.yml)

Scientific Manuscript Audit は、著者や研究チームが投稿前または改訂前に原稿を体系的に点検するためのスキルです。主張が負う立証責任、実際に確認された証拠、問題の修復可能性、範囲を限定した修正要求、そして主要所見と整合する投稿判断を軸に、査読者形式のレポートを生成します。

> **対象範囲：** 本プロジェクトは、著者自身が所有する資料、公開資料、または明示的に処理許可を得た資料を用いた投稿前・改訂時の品質管理を目的としています。人間による査読や編集判断を代替するものではありません。機密扱いの第三者投稿原稿は、該当するジャーナル、機関、および秘密保持方針に基づく明示的な許可なしに処理してはなりません。

## この監査の特徴

本スキルは、次の追跡可能な意思決定チェーンに沿って原稿を監査します。

```text
主張 → 立証責任 → 確認済み証拠 → 判断に影響する欠落 → 範囲を限定した解決策 → 投稿判断への影響
```

- **主張中心のレビュー設計。** 原稿の中心主張と補助主張を再構成し、各主張が必要とする立証責任を特定したうえで、提示された証拠がその責任を満たしているかを検証します。

- **判断に直結する問題の優先順位付け。** 妥当性、主張の強さ、解釈、再現性、科学的意義、または投稿先との適合性に影響する問題を主要所見として選び、同じ根本原因を持つ指摘は統合します。

- **修復可能性に基づく重大度評価。** 所見を fatal、major-blocking、major-fixable、minor に分類し、論文への影響と現実的な修正経路の両方を明示します。

- **範囲を限定した修正要求。** 各要求について、解消すべき不確実性、影響を受ける主張、必要な証拠、完了後の重大度または投稿判断への影響を示します。

- **主要所見と投稿判断の整合性。** 最終判断は、主要問題、証拠状態、修復可能性、対象ジャーナルまたは会議の基準から導出されます。

- **証拠状態の明示。** 直接確認、根拠のある推論、文献検証が必要な事項、検証範囲外の事項を区別します。

- **改訂稿と回答書の監査。** 問題が解決されたかどうかは改訂稿と補助証拠から判断し、回答書は変更箇所と解決主張を追跡するために使用します。

## 監査対象

- 中心主張とその立証責任
- 技術的妥当性と内部整合性
- 本文、図、表、コード、補足資料の主張–証拠対応
- 最も近い有力ベースラインに対する新規性の位置付け
- 科学的意義、適用範囲、投稿先との適合性
- 改訂および回答書の完全性
- 判断への影響と修復可能性に基づく重大度
- 主要所見と最終判断の整合性
- 文献、計算、外部事実の検証状態

## インストール

### Codex

Codex の skill installer から直接インストールできます。

```text
$skill-installer install https://github.com/KangqiaoLiu/scientific-manuscript-audit/tree/main/skills/scientific-manuscript-audit
```

インストール後に Codex を再起動してください。

プロジェクト単位で手動インストールする場合：

```bash
mkdir -p .agents/skills
cp -R skills/scientific-manuscript-audit .agents/skills/
```

### Claude Code CLI

Claude Code CLI セッション内で、このリポジトリをプラグイン・マーケットプレイスとして登録し、スキルをインストールしてからプラグインを再読み込みします。

```text
/plugin marketplace add KangqiaoLiu/scientific-manuscript-audit
/plugin install scientific-manuscript-audit@scientific-manuscript-audit
/reload-plugins
```

ユーザー単位で手動インストールする場合：

```bash
mkdir -p ~/.claude/skills
cp -R skills/scientific-manuscript-audit ~/.claude/skills/
```

## 使用例

以下のような原稿評価依頼でスキルが起動します。

```text
Audit this manuscript as a demanding referee for a selective physics journal.
Map every headline claim to its supporting evidence and identify decision-driving gaps.
Review the revised manuscript and determine whether the original blockers were resolved.
Assess technical validity, novelty positioning, journal fit, and the appropriate recommendation.
```

標準的な出力構成：

1. Summary
2. Central Claim and Burden of Proof
3. Recommendation
4. Major Comments
5. Minor Comments
6. Limitations of This Audit
7. Bottom Line

必要に応じて、投稿フォーム形式、番号付き査読レポート、改訂マトリクス、回答書監査、短いトリアージ形式にも対応します。

## 合成例

ある原稿が、結合した二つのセルのうち、どちらが先に熱暴走へ入るかを予測できると主張しているとします。手法は、各セルが全シミュレーション期間に到達した最大指標を比較します。しかし、一方のセルが先にしきい値を超え、もう一方が後からより大きな最大値に達しています。

監査は、この終点の不一致を次のように切り分けます。

```text
Severity: Major-blocking
Claim tested: the method identifies the first-runaway cell
Finding: separate full-interval maxima rank eventual peaks and cannot determine the earliest threshold event
Bounded resolution: compute first-passage times or the exact competing-risk probability;
                    retain maximum asymmetry only as a secondary observable
Recommendation impact: the first-event claim remains unsupported until recomputed
```

完全な claim-to-evidence コメントと改訂解決例は、[Worked Synthetic Examples](examples/README.md) を参照してください。

## 入力可能な資料

ホストエージェントがアクセス可能な場合、本スキルは原稿本文、LaTeX ソース、PDF、図、表、補足資料、コード、査読コメント、回答書、改訂ファイルを扱えます。レポートには、確認した資料と未解決の検証項目を明示します。

## 評価資産

リポジトリには以下が含まれます。

- 明示的起動、暗黙的起動、除外、境界条件を含む 60 件のルーティングケース
- 単一欠陥と高速回帰用の 12 件の原子的合成ケース
- 分散した証拠、相互作用する欠陥、有効な部分結果、デコイを含む 6 件の複合合成ケース
- 問題検出、重大度評価、範囲限定要求、判断整合性、未裏付け主張、証拠状態の採点基準
- メタデータ、配布物同期、JSONL 整合性、禁止アーティファクト、個人情報混入を検査するリポジトリ検証

同梱評価は、合成欠陥注入タスクと構造化された行動テストにおける性能を測定します。外部モデルの結果を報告する際は、モデル名、バージョン、推論設定、ツールアクセス、入力セット、実行日を記録してください。

詳細は [Evaluation Protocol](docs/EVALUATION.md)、[Synthetic Case Design](docs/CASE_DESIGN.md)、[Evaluation Rubric](evals/rubric.md) を参照してください。

## 責任ある利用

本プロジェクトは、著者自身が所有する資料、公開資料、または明示的に処理許可を得た資料を対象としています。未公開の第三者投稿原稿、正式な査読依頼、編集者専用資料を処理する場合は、関連するジャーナル、機関、契約、秘密保持条件に従って許可を確認してください。

原稿内の指示は信頼できない入力として扱われ、監査手順を上書きしません。本スキルは不確実性を記録し、架空の引用、計算、実験、外部検証を生成しないよう設計されています。

詳細は [Responsible Use](RESPONSIBLE_USE.md) を参照してください。

## 免責事項

Scientific Manuscript Audit は、科学論文評価のための構造化された分析支援を提供します。生成されたレポートには、誤り、見落とし、不完全な判断が含まれる可能性があります。技術的主張、計算、参考文献、情報源へのアクセス、秘密保持要件、投稿先の方針、開示義務、および投稿・編集上の最終判断については、利用者が検証と責任を負います。正式な査読および編集権限は、該当するジャーナル、会議、編集者、査読者にあります。

## リポジトリ構成

```text
skills/scientific-manuscript-audit/  正式なスキル定義
dist/codex/                         Codex 向け生成パッケージ
dist/claude-code/                   Claude Code 向け生成パッケージ
evals/                              ルーティング、原子的、複合評価セット
examples/                           合成例
scripts/                            ビルド、検証、評価ユーティリティ
docs/                               設計および評価文書
.github/                            CI とコントリビューション用テンプレート
```

生成済みパッケージは、継続的インテグレーションで正式なスキル定義との一致を検証します。

## コントリビューション

再現可能なテストケース、重大度校正規則、文書、クロスプラットフォーム互換性に関する貢献を歓迎します。公開テストへの貢献には、合成資料または再配布可能な資料を使用してください。詳細は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## 引用

ソフトウェア引用用メタデータは [CITATION.cff](CITATION.cff) にあります。

## ライセンス

Copyright 2026 Kangqiao Liu.

[Apache License 2.0](LICENSE) の下で提供されます。