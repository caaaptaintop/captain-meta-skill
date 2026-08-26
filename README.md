# Captain Meta Skill

## 中文

`captain-meta-skill` 是一个独立的 Agent Skill 元工程，用于把可重复的工作设计成可维护、可评估、可演化的技能包。它聚焦问题边界、接口契约、生成质量和迭代证据，保持最小可用结构。

Captain 使用自己的名称、版本和发布节奏。它不声称包含 Yao 的全套 Skill OS 引擎、CLI、报告系统或完整工作树。

## 六种模式

六种模式覆盖一个技能从定位到演化的最小闭环：

| 模式 | 作用 | 主要产出 |
| --- | --- | --- |
| **A Root** | 找到真实问题，确定边界，判断是否适合做成 Skill | 问题定义与排除项 |
| **B Design** | 定义触发条件、输入、输出、约束和质量标准 | 技能设计契约 |
| **C Generate** | 按契约生成最小入口和必要资源 | 可运行的技能包 |
| **D Evaluate** | 用代表性案例和结构检查验证触发与结果 | 评测结果与失败样本 |
| **E Reflect** | 根据失败、反馈和证据定位缺口 | 反思记录与改进判断 |
| **F Evolve** | 只将有证据支持的改动纳入下一版 | 受控演化版本 |

首次使用通常按 `A Root → B Design → C Generate → D Evaluate → E Reflect → F Evolve` 推进，之后从实际缺口回到对应模式。

## 最小工作流

1. 记录一项反复出现的工作，写清目标和预期结果。
2. 用 **A Root** 确认它值得复用，并划定不处理的相邻问题。
3. 用 **B Design** 写出触发、输入、输出、约束和验收标准。
4. 用 **C Generate** 只创建必要的 `SKILL.md`、接口和资源。
5. 用 **D Evaluate** 运行正例、反例和代表性输出检查。
6. 用 **E Reflect** 记录失败原因，再用 **F Evolve** 做最小修改并重新评测。

## 适用场景

- 把重复的个人或团队工作沉淀为可复用技能。
- 设计新技能，或维护已有技能的边界、接口和评测。
- 在小型技能库中建立清晰的资源结构与演化记录。
- 需要先判断“该不该做成 Skill”，再决定如何实现。

## 不适用场景

- 一次性问答、一次性提示词或不需要复用的临时任务。
- 只需要解释概念、翻译文本或撰写普通文档的请求。
- 需要完整应用、后端服务、生产部署或独立 CI 平台的项目。
- 没有明确边界，也没有可观察结果或反馈来源的想法。

## 项目最小结构

```text
captain-meta-skill/
├── README.md
├── SKILL.md
├── agents/
│   └── interface.yaml
├── references/
├── evals/
├── tests/
├── upstream.lock.json
└── THIRD_PARTY_NOTICES.md
```

目录只在实际需要时增加内容。`upstream.lock.json` 记录来源锁定，`THIRD_PARTY_NOTICES.md` 记录第三方来源与许可证说明。

## 安装

面向 Codex 的全局安装：

```bash
npx -y skills add caaaptaintop/captain-meta-skill -a codex -g -y
```

## 上游参考与维护者同步

- **Yao Meta Skill**（[yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill)）：Captain 的核心工程基础与历史来源，锁定 commit `f5d8f681372edae1915991e2de0c23dc306dd30f`。维护者按需审阅并同步适合 Captain 边界的工程经验与修复，不自动带入 Yao 的全套 Skill OS 引擎、CLI、报告系统或完整工作树。
- **Dao Skill**（[gnipbao/dao-skill](https://github.com/gnipbao/dao-skill)）：机制参考，锁定 commit `1cae835995c0ff4d9a33a6fec82cca0a54b7cd05`，用于参考任务意图路由、根问题诊断和证据驱动演化。Captain 未合并 Dao 的 Git 历史。

精确来源见 [`upstream.lock.json`](upstream.lock.json)，第三方声明见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。Captain 的维护与发布以本仓库为准。

## 许可证

MIT

---

## English

`captain-meta-skill` is an independently released Agent Skill meta-engineering project for turning repeatable work into maintainable, evaluable, and evolvable skill packages. It focuses on problem boundaries, interface contracts, generation quality, and iteration evidence while keeping the package small.

Captain uses its own name, version, and release cadence. It does not claim to contain Yao's full Skill OS engine, CLI, report system, or complete work tree.

## Six Modes

The six modes form the smallest loop from positioning a skill to evolving it:

| Mode | Purpose | Main output |
| --- | --- | --- |
| **A Root** | Find the real problem, set the boundary, and decide whether it belongs in a Skill | Problem definition and exclusions |
| **B Design** | Define triggers, inputs, outputs, constraints, and quality standards | Skill design contract |
| **C Generate** | Generate the minimum entrypoint and required resources from the contract | Runnable skill package |
| **D Evaluate** | Check triggering and results with representative cases and structure checks | Evaluation results and failures |
| **E Reflect** | Use failures, feedback, and evidence to locate gaps | Reflection record and improvement decision |
| **F Evolve** | Carry only evidence-supported changes into the next version | Controlled evolution |

The first pass usually follows `A Root → B Design → C Generate → D Evaluate → E Reflect → F Evolve`. Later passes return to the mode where the next gap is visible.

## Minimal Workflow

1. Capture a recurring piece of work, including its goal and expected result.
2. Use **A Root** to confirm reuse is worthwhile and exclude neighboring problems.
3. Use **B Design** to define triggers, inputs, outputs, constraints, and acceptance checks.
4. Use **C Generate** to create only the required `SKILL.md`, interface, and resources.
5. Use **D Evaluate** with positive cases, negative cases, and representative output checks.
6. Use **E Reflect** to record failure causes, then use **F Evolve** for the smallest change and rerun the evaluation.

## Good Fit

- Turning repeated personal or team work into reusable skills.
- Designing a new skill or maintaining the boundaries, interface, and evaluations of an existing one.
- Keeping resource structure and evolution records clear in a small skill library.
- Deciding whether work should become a Skill before deciding how to implement it.

## Not a Fit

- One-off answers, one-off prompts, or temporary work with no reuse value.
- Requests that only need concept explanations, translation, or ordinary documentation.
- Projects requiring a complete application, backend service, production deployment, or standalone CI platform.
- Ideas without a clear boundary, observable result, or feedback source.

## Minimum Project Structure

```text
captain-meta-skill/
├── README.md
├── SKILL.md
├── agents/
│   └── interface.yaml
├── references/
├── evals/
├── tests/
├── upstream.lock.json
└── THIRD_PARTY_NOTICES.md
```

Add content to a directory only when the skill needs it. `upstream.lock.json` records source pins, and `THIRD_PARTY_NOTICES.md` records third-party attribution and license details.

## Installation

Install globally for Codex:

```bash
npx -y skills add caaaptaintop/captain-meta-skill -a codex -g -y
```

## Upstream References and Maintainer Sync

- **Yao Meta Skill** ([yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill)): Captain's core engineering foundation and historical source, pinned to commit `f5d8f681372edae1915991e2de0c23dc306dd30f`. Maintainers review and sync engineering practices and fixes that fit Captain's boundary as needed. Yao's full Skill OS engine, CLI, report system, and complete work tree are not brought in automatically.
- **Dao Skill** ([gnipbao/dao-skill](https://github.com/gnipbao/dao-skill)): a mechanism reference, pinned to commit `1cae835995c0ff4d9a33a6fec82cca0a54b7cd05`, for task-intent routing, root-problem diagnosis, and evidence-driven evolution. Captain has not merged Dao's Git history.

See [`upstream.lock.json`](upstream.lock.json) for exact source pins and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for third-party notices. This repository is the source of truth for Captain's maintenance and releases.

## License

MIT
