# Scientific Manuscript Audit

**面向 Codex 与 Claude Code、以主张为中心并以证据为基础的科研稿件审查技能。**

[English](README.md) | 简体中文 | [日本語](README.ja.md)

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.1.0--rc.3-orange.svg)](CHANGELOG.md)
[![Validation](https://github.com/KangqiaoLiu/scientific-manuscript-audit/actions/workflows/validate.yml/badge.svg)](.github/workflows/validate.yml)

Scientific Manuscript Audit 帮助论文作者与研究团队在投稿或修订前系统检查科研稿件。它生成审稿人风格的报告，并围绕主张所承担的证明责任、已经检查的证据、问题的可修复性、有边界的修改要求以及一致的投稿建议组织分析。

## 它的核心特点

该技能采用一条可追踪的审查链：

```text
主张 → 证明责任 → 已检查证据 → 决策相关缺口 → 有边界的解决方案 → 对投稿建议的影响
```

- **以主张为中心的审查结构。** 审查会重构稿件的中心主张与支撑性主张，识别每项主张带来的证明责任，并据此检验稿件提供的证据。

- **围绕编辑决策进行问题排序。** 主要意见根据其对正确性、主张强度、结果解释、可复现性、科学意义或期刊匹配度的影响进行筛选；具有同一根因的问题会被合并。

- **按可修复性校准严重度。** 问题分为致命问题（fatal）、阻断性重大问题（major-blocking）、可修复重大问题（major-fixable）和次要问题（minor），分类依据是其对论文的影响以及现实可行的修复路径。

- **有边界的修改要求。** 每项实质性要求都会说明它要消除的具体不确定性、所影响的主张、需要补充的证据，以及完成后对严重度或投稿建议的影响。

- **保持投稿建议与主要意见一致。** 最终建议由主要问题、证据状态、可修复性以及目标期刊的标准共同导出。

- **明确标注证据状态。** 报告会区分直接检查、基于现有材料的合理推断、需要文献核验的事项，以及尚未得到验证的范围。

- **修订稿与回复信审查。** 是否解决问题以修订后的稿件和支撑证据为准；回复信用于定位修改位置和作者声称已经解决的事项。

## 审查内容

- 中心主张及其证明责任
- 技术正确性与内部一致性
- 正文、图、表、代码和补充材料之间的主张—证据对应关系
- 相对于最近严肃基准工作的创新定位
- 科学意义、适用范围与期刊匹配度
- 修订稿与回复信的完整性
- 基于决策影响与可修复性的严重度判断
- 主要意见与最终投稿建议之间的一致性
- 文献、计算和外部事实的核验状态

## 安装

### Codex

使用 Codex 的 skill installer 直接从仓库安装：

```text
$skill-installer install https://github.com/KangqiaoLiu/scientific-manuscript-audit/tree/main/skills/scientific-manuscript-audit
```

安装后重启 Codex。

也可以在项目级 Agent Skills 目录中手动安装：

```bash
mkdir -p .agents/skills
cp -R skills/scientific-manuscript-audit .agents/skills/
```

### Claude Code CLI

在 Claude Code CLI 会话中，将该仓库注册为插件市场、安装技能并重新加载插件：

```text
/plugin marketplace add KangqiaoLiu/scientific-manuscript-audit
/plugin install scientific-manuscript-audit@scientific-manuscript-audit
/reload-plugins
```

也可以在用户级目录中手动安装：

```bash
mkdir -p ~/.claude/skills
cp -R skills/scientific-manuscript-audit ~/.claude/skills/
```

## 使用方式

以下类型的请求会触发该技能：

```text
请以严格审稿人的标准审查这篇稿件，并以选择性较高的物理期刊为目标。
请将每项标题级主张映射到它的支撑证据，并识别会影响编辑决定的缺口。
请检查修订稿，判断原有阻断性问题是否已经解决。
请评估技术正确性、创新定位、期刊匹配度以及适当的投稿建议。
```

典型输出结构：

1. 摘要
2. 中心主张与证明责任
3. 投稿建议
4. 主要意见
5. 次要意见
6. 本次审查的限制
7. 最终判断

用户也可以要求采用期刊审稿表、编号式审稿报告、修订矩阵、回复信审查或简洁初筛等格式。

## 合成示例

一篇稿件声称可以预测两个耦合单元中哪一个会先进入热失控。其方法分别比较两个单元在整个模拟区间内达到的最大指标值。实际结果中，一个单元更早越过阈值，另一个单元在更晚时间达到更大的峰值。

审查应识别出科学终点与所用指标之间的不一致：

```text
严重度：阻断性重大问题
被检验的主张：该方法能够识别首先进入热失控的单元
发现：分别比较完整时间区间内的最大值只能排序最终峰值，不能确定最早的阈值越过事件
有边界的解决方案：计算首次通过时间或精确的竞争风险概率；
                     最大值差异可以保留为次级观测量
对投稿建议的影响：在重新计算前，首先失效事件的主张仍缺乏支撑
```

更多内容见[完整合成示例](examples/README.md)，其中包括完整的主张—证据主要意见和修订闭环示例。

## 可处理的材料

在宿主 agent 能够访问相应文件的前提下，该技能可处理论文正文、LaTeX 源码、PDF、图、表、补充材料、代码、审稿意见、作者回复以及修订文件。报告会说明实际检查了哪些材料，以及哪些事项仍未得到验证。

## 评测

仓库包含：

- 60 个路由案例，覆盖明确触发、隐含触发、排除请求和边界请求
- 12 个原子级合成案例，用于隔离单一缺陷和快速回归测试
- 6 个复合合成案例，其中包含分散证据、相互作用的问题、有效子结果和诱饵
- 针对问题检出、严重度校准、有边界的修改要求、投稿建议一致性、无依据断言和证据状态的评分规则
- 针对元数据、分发包同步、JSONL 结构、禁止文件和意外个人信息的仓库校验

现有评测用于衡量合成缺陷注入任务和结构化行为测试中的表现。外部模型运行结果应记录模型名称、版本、推理设置、工具权限、输入集合和运行日期。

详见[评测协议](docs/EVALUATION.md)、[合成案例设计](docs/CASE_DESIGN.md)和[评测规则](evals/rubric.md)。

## 负责任使用

本项目适用于作者本人拥有、已经公开或已经明确授权处理的材料。未公开的第三方投稿、正式期刊审稿任务以及仅限编辑查看的材料，需要遵守相关期刊、机构和保密协议的授权要求。

稿件内容按不受信任的输入处理。稿件中嵌入的指令不会控制审查流程。技能会记录不确定性，并避免虚构引用、计算、实验或核验结果。

完整规则见[负责任使用说明](RESPONSIBLE_USE.md)。

## 免责声明

Scientific Manuscript Audit 提供结构化科研稿件分析支持。其报告属于建议性判断，可能包含错误、遗漏或不完整结论。用户仍需自行核实技术主张、计算、参考文献、来源访问情况、保密要求、期刊政策、披露义务以及所有投稿或编辑决定。正式同行评审和编辑决定权属于相应期刊、会议、编辑和审稿人。

## 仓库结构

```text
skills/scientific-manuscript-audit/  规范版本的技能文件
dist/codex/                         生成的 Codex 分发包
dist/claude-code/                   生成的 Claude Code 分发包
evals/                              路由、原子和复合评测集
examples/                           完整合成示例
scripts/                            构建、校验和评测工具
docs/                               设计与评测文档
.github/                            CI 与贡献模板
```

持续集成会检查生成的分发包是否与规范版本保持一致。

## 参与贡献

欢迎提交可复现测试案例、校准规则、文档和跨平台兼容性改进。公开测试材料必须为合成材料或具有明确再分发权的材料。详见[贡献指南](CONTRIBUTING.md)。

## 引用

软件引用元数据见 [CITATION.cff](CITATION.cff)。

## 许可证

Copyright 2026 Kangqiao Liu.

本项目采用 [Apache License 2.0](LICENSE) 许可证。
