[![CI](https://github.com/caaaptaintop/captain-meta-skill/actions/workflows/test.yml/badge.svg)](https://github.com/caaaptaintop/captain-meta-skill/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Captain Meta Skill

## 一句话定位

Captain 是一个把重复工作变成可复用、可评测、可打包、可维护 Agent Skill 的元工程，公开身份、版本和发布节奏独立于它继承的工程实现。

## Captain 0.3

Captain 0.3 恢复了基于 Yao Engine 的完整工程路径，同时把 Captain 的边界和来源说明放在公开入口：

- 用统一 CLI 初始化和自动生成 Skill 包。
- 对触发条件与输出结果执行可重复评测。
- 生成平台无关的 Skill IR，再编译为多平台契约。
- 生成兼容性包、归档文件和目标适配器。
- 在临时 Skill 根目录执行安装模拟。
- 检查脚本、依赖、网络、权限和来源摘要的 trust。
- 检查目标包的 runtime conformance 和降级说明。
- 维护 registry 元数据、校验和与升级差异。
- 用 Review Studio 聚合闸门、阻断项、警告和审阅动作。
- 在发布前执行可核对的 release gates。

这些能力描述的是仓库中已经存在的 CLI、脚本、契约和检查入口。实际通过等级以当前运行结果为准。

## 为什么用 Captain

- 把是否值得做成 Skill 的判断放在实现之前，减少一次性提示词和无效包。
- 把触发边界、输入、输出、资源和失败处理写成可检查的契约。
- 用同一份 Skill IR 连接源包、平台编译和分发包，降低平台差异带来的漂移。
- 让评测、信任、安装、注册和发布状态有可追踪的证据位置。

## 三层归属

| 层 | Captain 中的角色 | 清晰边界 |
| --- | --- | --- |
| Yao Engine | Captain 继承的工程实现和 Git 历史 | 提供 CLI、自动生成、评测、编译、打包、信任、安装和发布检查；工程来源锁在 upstream.lock.json。 |
| Dao | 机制参考 | 提供根问题诊断、A-F 模式和证据驱动演化的启发；Dao 的 Git 历史和代码没有合并进 Captain。 |
| Captain | 公开身份与维护者策略 | 负责名称、版本、六模式融合、来源锁、公开文档、下游维护和 Captain 发布。 |

当前来源锁定在 upstream.lock.json：

- Yao Meta Skill：yaojingang/yao-meta-skill，版本 2.1.0，commit f5d8f681372edae1915991e2de0c23dc306dd30f，整合类型为 engine-source-and-history；Dao Skill：gnipbao/dao-skill，commit 1cae835995c0ff4d9a33a6fec82cca0a54b7cd05，整合类型为 mechanisms-only。

## A-F 六模式

Captain 保留 Dao 启发的六模式，并把它们接到 Captain 自己的工程路径上：

| 模式 | 处理的问题 | 主要结果 |
| --- | --- | --- |
| A Root | 这项工作是否有稳定的重复问题，边界在哪里 | 表层需求、根问题、第一性原理、成功标准、核心张力、关键约束与假设、最小下一步 |
| B Design | Skill 应该响应什么，接收什么，交付什么 | 触发、输入、输出、约束和验收契约 |
| C Generate | 如何把契约落成最小可运行包 | SKILL.md、接口元数据和所需资源 |
| D Evaluate | 触发和输出是否在代表性案例上成立 | 触发评测、输出评测和失败样本 |
| E Reflect | 失败和反馈说明了哪个缺口 | 脱敏证据包、缺口判断和改进方向 |
| F Evolve | 哪个经过批准的改动值得进入下一版 | 最小变更、回归结果和独立的部署状态 |

复合任务选择最高需要的模式：F > E > D > C > B > A。高模式可以包含低模式工作，但不能跳过边界和证据要求。

A-F 只负责识别当前任务。Captain 把诊断整理成统一契约，D Evaluate、E Reflect 和 F Evolve 都交给同一套 Yao 证据、Trust、适配与验证链执行，不存在独立的 Dao 诊断器。F Evolve 中的修改者是当前获得明确授权的 Agent；它只修改锁定目标，不允许后台 Agent 自动改写。

## 两类使用者

### 使用者

使用者可以直接加载已发布的 Captain Skill，用 A Root 和 B Design 判断一个重复工作是否适合沉淀，再按需要查看评测、适配和安装证据。

### 创建者与维护者

创建者负责锁定目标目录、描述触发边界、补充真实案例、运行检查并选择发布范围。维护者负责审阅来源变化、更新来源锁、保持 Captain 归属清楚，并让每个发布闸门对应到实际证据。

## 5 分钟 Quick Start

在 Captain 仓库根目录执行。示例把 my-skill 放入临时目录，避免把新包写进 Captain 源树。

    cd /path/to/captain-meta-skill
    WORKDIR="$(mktemp -d)"
    python3 scripts/yao.py init my-skill \
      --description "把重复工作整理成可复用的 Agent Skill。" \
      --intent-job "把已验证的重复工作整理成可路由的 Agent Skill。" \
      --intent-real-input "一份包含步骤、边界和失败案例的工作流说明" \
      --intent-primary-output "包含 SKILL.md、接口元数据和评测案例的可验证 Skill 包" \
      --intent-exclusion "一次性问答、翻译和普通文档写作" \
      --intent-constraint "保持入口精简，生成报告不进入公开源码" \
      --intent-standard "通过结构验证，并用本 Skill 自己的案例验证触发和输出" \
      --output-dir "$WORKDIR"
    python3 scripts/yao.py validate "$WORKDIR/my-skill"
    python3 scripts/yao.py skill-ir "$WORKDIR/my-skill"
    python3 scripts/yao.py compile-skill "$WORKDIR/my-skill" \
      --target openai \
      --target claude \
      --target generic \
      --target agent-skills-compatible \
      --target vscode
    mkdir -p "$WORKDIR/my-skill/evals/output"
    sed -n '1,4p' evals/output/cases.jsonl > "$WORKDIR/my-skill/evals/output/cases.jsonl"
    python3 scripts/yao.py output-eval \
      --cases "$WORKDIR/my-skill/evals/output/cases.jsonl" \
      --output-json "$WORKDIR/my-skill/reports/output_quality_scorecard.json" \
      --output-md "$WORKDIR/my-skill/reports/output_quality_scorecard.md" \
      --blind-pack-json "$WORKDIR/my-skill/reports/output_blind_review_pack.json" \
      --blind-pack-md "$WORKDIR/my-skill/reports/output_blind_review_pack.md" \
      --blind-answer-key-json "$WORKDIR/my-skill/reports/output_blind_answer_key.json" \
      --self
    python3 scripts/yao.py package "$WORKDIR/my-skill" \
      --platform openai \
      --platform claude \
      --platform generic \
      --platform vscode \
      --output-dir "$WORKDIR/my-skill/dist" \
      --zip
    python3 scripts/yao.py install-simulate "$WORKDIR/my-skill" \
      --package-dir "$WORKDIR/my-skill/dist" \
      --install-root "$WORKDIR/install-simulation"

init 会生成首个 Skill 包和初始报告；这里取仓库中四个无外部 fixture 的示例案例，只用于验证评测链可运行，不能证明 my-skill 的真实质量。正式项目必须换成 my-skill 自己的案例和真实输出。

output-eval 是全局评测入口，使用显式案例文件和输出路径，不接收 my-skill 位置参数；--self 是授权该入口运行的必要标记。upgrade 检查的实际命令名是 upgrade-check。

## 完整工作流

1. 用 A Root 写下表层需求、根问题、第一性原理、成功标准、核心张力、关键约束与假设、最小下一步。
2. 用 B Design 固定 Skill 名称、触发描述、输入输出、资源边界和验收方式。
3. 用 C Generate 创建最小包，或只编辑已经明确授权的目标目录。
4. 运行 validate，检查 frontmatter、资源边界、治理字段和可加载结构。
5. 运行触发评测与 output-eval，分别检查路由精度和交付结果；记录正例、反例、近邻和边界案例。
6. 对需要共享或跨平台的包导出 Skill IR，编译目标契约，再生成适配器和归档包。
7. 运行 trust、conformance、registry audit、package verification 和 install simulation。
8. 打开 Review Studio，处理 block 和 warn，确认发布闸门、版本差异和回滚边界。
9. 发布 Captain 版本，独立记录源状态、已安装状态和部署状态；用 E Reflect 处理失败证据，再经 F Evolve 做一个可归因的改动并重新检查。

## 能力导航

| 能力 | Captain 0.3 提供的行为 | 主要入口 |
| --- | --- | --- |
| CLI 与自动生成 | 初始化最小 Skill 包，填充接口、manifest 和初始工程报告 | scripts/yao.py init |
| 触发与输出评测 | 用案例检查应该触发、应该拒绝和输出断言 | scripts/trigger_eval.py；scripts/yao.py output-eval |
| Skill IR | 先保存平台无关的任务、触发、工作流、资源、风险和治理契约 | scripts/yao.py skill-ir |
| 多平台编译 | 将 Skill IR 编译成 OpenAI、Claude、generic、Agent Skills 和 VS Code 契约 | scripts/yao.py compile-skill |
| 打包 | 生成目标适配器、兼容性文件和可选 ZIP 归档 | scripts/yao.py package |
| 安装模拟 | 在临时本地 Skill 根目录解包并加载入口、manifest、接口和适配器 | scripts/yao.py install-simulate |
| Trust 与 runtime conformance | 检查秘密、脚本、网络、权限、目标元数据、资源路径和降级说明 | scripts/yao.py trust；scripts/yao.py conformance |
| Registry 与升级 | 写入包元数据、兼容性、校验和，并比较前后版本差异 | scripts/yao.py registry-audit；scripts/yao.py upgrade-check |
| Review Studio | 把闸门、阻断项、警告、证据链接和审阅动作放在一个审阅面 | scripts/yao.py review-studio |
| Release gates | 按风险选择治理、评测、信任、安装和发布检查 | references/gate-selection.md；scripts/yao.py promote-check |

## 证据等级

| 等级 | 含义 | 可以支持的判断 |
| --- | --- | --- |
| E1 Static | 读取源码、元数据、契约、链接和规则 | 结构是否存在，边界是否写清 |
| E2 Simulated | 运行确定性案例、dry run、打包校验或安装模拟 | 受控输入下的流程和包结构是否成立 |
| E3 Runtime | 在目标宿主或 Provider 中执行，并保存结果 | 指定运行环境中的真实行为 |
| E4 Operational | 多次真实使用，有审阅过的结果和反馈 | 长期使用中的稳定性和漂移 |

Captain 不把生成报告、计划中的检查或单次静态读取得出的结论自动提升到更高等级。每个发布判断都应标出证据等级和未覆盖的边界。

### 世界级证据收集

只有确实要核验 E3/E4 证据时才运行这组命令；它会准备提交包并验证来源、哈希、审阅状态和总账，不会把模板或计划当作完成证据。

    SUBMISSIONS_DIR="${SUBMISSIONS_DIR:-evidence/world_class/submissions}"
    python3 scripts/yao.py world-class-preflight . --submissions-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-submission-kit . --output-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-submission-kit . --output-dir "$SUBMISSIONS_DIR" --prefill-artifacts --self
    python3 scripts/yao.py world-class-intake . --submissions-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-submission-review . --submissions-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-ledger . --submissions-dir "$SUBMISSIONS_DIR" --self

## 适用范围

Captain 适合：

- 个人或团队反复执行、且有可观察交付物的工作。
- 需要明确触发边界、输入输出和失败处理的 Agent Skill。
- 需要跨平台分发、来源锁、评测或可回滚维护的 Skill 包。
- 需要把失败反馈转成受控改动的持续维护工作。

Captain 不适合：

- 一次性问答、一次性提示词、普通翻译或普通文档写作。
- 只有想法，没有稳定输入、输出或成功条件的工作。
- 需要完整应用、后端服务、生产部署或独立账户操作的项目。

## 源码结构

以下只列 Captain 维护的源契约与实现目录。运行报告、打包产物、预览文件和历史首页副本不属于这棵跟踪源码树。

    captain-meta-skill/
    ├── README.md
    ├── SKILL.md
    ├── agents/interface.yaml
    ├── references/
    ├── scripts/
    ├── evals/
    ├── tests/
    ├── skill-ir/
    ├── runtime/
    ├── security/
    ├── registry/
    ├── templates/
    ├── manifest.json
    ├── upstream.lock.json
    ├── THIRD_PARTY_NOTICES.md
    ├── LICENSE
    └── .github/workflows/test.yml

- SKILL.md 是运行时入口，保持短小，只承载触发面、路由和必要闸门。
- references/ 放稳定方法、边界、评测、分发和维护说明。
- scripts/ 放 CLI、编译器、检查器、报告生成器和闸门逻辑。
- evals/ 与 tests/ 放可重复的触发、输出、分发和回归输入。
- skill-ir/、runtime/、security/ 和 registry/ 承载中立契约、运行一致性、安全策略和包登记。

## 安装

面向 Codex 的全局安装：

    npx -y skills add caaaptaintop/captain-meta-skill -a codex -g -y

安装后，加载 Captain Meta Skill，并把具体 Skill 目标路径交给 CLI。Captain 本身需要作为目标时，才对相应维护命令显式使用 --self。

创建者也可以直接克隆仓库，在仓库根目录运行 scripts/yao.py；发布或同步前，先构建并验证归档，再执行安装模拟。

本地开发默认同步到停用镜像 `~/.agents/skills.disabled/captain-meta-skill`：先完成打包与校验，再运行 `make sync-local-install`。只有明确要替换当前启用版本时才运行 `make sync-active-install`；两个入口都只接受已验证归档。

## 维护与同步

Captain 的 origin 是公开发布源，Yao 是只读的工程上游，Dao 是只读的机制参考。Captain 用户从 Captain 发布更新，不使用 Yao 的自更新通道覆盖 Captain。

维护 Yao Engine 时：

1. 获取 upstream，并从 upstream.lock.json 中的 Yao commit 开始查看变化。
2. 只选择适合 Captain 边界的工程实现或修复，保留 Captain 的公开身份、README、来源锁和维护策略。
3. 运行受影响的检查，再运行 make ci-test。
4. 所有源改动和证据通过审阅后，更新 Yao 版本与 commit 锁，再更新 Captain 自己的版本和发布说明，记录回滚边界。

维护 Dao 参考时，只更新机制说明、来源许可和必要的归因。不要合并 Dao Git 历史，也不要把 Dao 代码当作 Captain 的实现来源。

日常生成报告、临时预览、原始本地遥测、Provider 原始输出和临时安装目录不应成为公开包的隐含源码。

## 来源与许可

- Captain Meta Skill 由本仓库公开身份维护，版本、发布和下游策略以本仓库为准，许可证为 [MIT](LICENSE)。
- Yao Meta Skill 的工程实现和 Git 历史来源于 [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill)，具体 commit 见 [upstream.lock.json](upstream.lock.json)。
- Dao Skill 仅作为机制参考，来源为 [gnipbao/dao-skill](https://github.com/gnipbao/dao-skill)，具体 commit 和归因见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

---

# Captain Meta Skill

## One-line Positioning

Captain is a meta-engineering project that turns recurring work into reusable, evaluable, packageable, and maintainable Agent Skills, with its own public identity, versioning, and release cadence independent from the engineering implementation it inherits.

## Captain 0.3

Captain 0.3 restores the complete Yao Engine based engineering path while putting Captain's boundaries and source record in the public entrypoint:

- Initialize and auto-generate Skill packages through one CLI.
- Evaluate trigger behavior and output results with repeatable cases.
- Produce platform-neutral Skill IR, then compile target-specific contracts.
- Generate compatibility packages, archives, and target adapters.
- Simulate installation into a temporary Skill root.
- Run trust checks for scripts, dependencies, network, permissions, and source summaries.
- Check runtime conformance and degradation notes for packaged targets.
- Maintain registry metadata, checksums, and upgrade diffs.
- Use Review Studio to bring gates, blockers, warnings, and review actions together.
- Apply reviewable release gates before publishing.

These are capabilities backed by the repository's existing CLI, scripts, contracts, and checks. The actual passing level comes from the current run.

## Why Captain

- Decide whether work deserves a Skill before adding implementation.
- Turn trigger boundaries, inputs, outputs, resources, and failure handling into checkable contracts.
- Connect source packages, platform compilation, and distribution through one Skill IR to reduce drift.
- Give evaluation, trust, installation, registry, and release status traceable evidence locations.

## Three Ownership Layers

| Layer | Role in Captain | Boundary |
| --- | --- | --- |
| Yao Engine | Inherited engineering implementation and Git history | Supplies the CLI, auto-generation, evaluation, compilation, packaging, trust, installation, and release checks; its source is pinned in upstream.lock.json. |
| Dao | Mechanism reference | Informs root-problem diagnosis, the A-F modes, and evidence-led evolution; Dao Git history and code are not merged into Captain. |
| Captain | Public identity and maintenance policy | Owns the name, version, six-mode integration, source locks, public documentation, downstream maintenance, and Captain releases. |

The current source pins are recorded in upstream.lock.json:

- Yao Meta Skill: yaojingang/yao-meta-skill, version 2.1.0, commit f5d8f681372edae1915991e2de0c23dc306dd30f, integration engine-source-and-history; Dao Skill: gnipbao/dao-skill, commit 1cae835995c0ff4d9a33a6fec82cca0a54b7cd05, integration mechanisms-only.

## Six A-F Modes

Captain retains the Dao-inspired six modes and connects them to Captain's own engineering path:

| Mode | Question it handles | Main result |
| --- | --- | --- |
| A Root | Is there a stable recurring problem, and where is the boundary? | Surface request, root problem, first principle, success condition, core tension, material constraints and assumptions, and smallest next step |
| B Design | What should the Skill respond to, accept, and deliver? | Trigger, input, output, constraint, and acceptance contract |
| C Generate | How does the contract become the smallest runnable package? | SKILL.md, interface metadata, and required resources |
| D Evaluate | Do triggering and output hold on representative cases? | Trigger evaluation, output evaluation, and failures |
| E Reflect | What gap is revealed by failure or feedback? | Redacted evidence packet, gap judgment, and direction |
| F Evolve | Which approved change belongs in the next version? | Attributable change, regression result, and separate deployment status |

For a compound task, choose the highest required mode: F > E > D > C > B > A. A higher mode may include lower-mode work, but it keeps every boundary and evidence requirement.

A-F only classifies the current task. Captain normalizes diagnosis into one contract, and D Evaluate, E Reflect, and F Evolve all use the same Yao evidence, trust, adaptation, and verification chain; there is no separate Dao diagnostic engine. In F Evolve, the modifier is the currently authorized agent, operating only on the locked target; no background agent may mutate files.

## Two User Roles

### Users

Users can load a released Captain Skill, use A Root and B Design to decide whether recurring work should be captured, and inspect evaluation, compatibility, and installation evidence when needed.

### Authors and Maintainers

Authors lock the target directory, define the trigger boundary, add real cases, run checks, and choose the release scope. Maintainers review source changes, update source pins, keep Captain ownership explicit, and connect every release gate to concrete evidence.

## 5-minute Quick Start

Run this from the Captain repository root. The example puts my-skill in a temporary directory so the Captain source tree stays unchanged.

    cd /path/to/captain-meta-skill
    WORKDIR="$(mktemp -d)"
    python3 scripts/yao.py init my-skill \
      --description "Turn recurring work into a reusable Agent Skill." \
      --intent-job "Turn a verified recurring workflow into a routeable Agent Skill." \
      --intent-real-input "A workflow brief with steps, boundaries, and failure cases" \
      --intent-primary-output "A verifiable Skill package with SKILL.md, interface metadata, and eval cases" \
      --intent-exclusion "One-off answers, translation, and ordinary documentation" \
      --intent-constraint "Keep the entrypoint lean and generated reports out of public source" \
      --intent-standard "Pass structural validation and use the Skill's own cases for trigger and output checks" \
      --output-dir "$WORKDIR"
    python3 scripts/yao.py validate "$WORKDIR/my-skill"
    python3 scripts/yao.py skill-ir "$WORKDIR/my-skill"
    python3 scripts/yao.py compile-skill "$WORKDIR/my-skill" \
      --target openai \
      --target claude \
      --target generic \
      --target agent-skills-compatible \
      --target vscode
    mkdir -p "$WORKDIR/my-skill/evals/output"
    sed -n '1,4p' evals/output/cases.jsonl > "$WORKDIR/my-skill/evals/output/cases.jsonl"
    python3 scripts/yao.py output-eval \
      --cases "$WORKDIR/my-skill/evals/output/cases.jsonl" \
      --output-json "$WORKDIR/my-skill/reports/output_quality_scorecard.json" \
      --output-md "$WORKDIR/my-skill/reports/output_quality_scorecard.md" \
      --blind-pack-json "$WORKDIR/my-skill/reports/output_blind_review_pack.json" \
      --blind-pack-md "$WORKDIR/my-skill/reports/output_blind_review_pack.md" \
      --blind-answer-key-json "$WORKDIR/my-skill/reports/output_blind_answer_key.json" \
      --self
    python3 scripts/yao.py package "$WORKDIR/my-skill" \
      --platform openai \
      --platform claude \
      --platform generic \
      --platform vscode \
      --output-dir "$WORKDIR/my-skill/dist" \
      --zip
    python3 scripts/yao.py install-simulate "$WORKDIR/my-skill" \
      --package-dir "$WORKDIR/my-skill/dist" \
      --install-root "$WORKDIR/install-simulation"

init generates the first Skill package and initial reports. This example takes four cases with no external fixtures only to prove the evaluation chain runs; it does not prove my-skill's real quality. A real project must replace them with its own cases and actual outputs.

output-eval is a global evaluation entrypoint. It takes an explicit case file and output paths instead of a positional my-skill directory, and --self authorizes this entrypoint to run. The actual upgrade command is upgrade-check.

## Complete Workflow

1. Use A Root to record the surface request, root problem, first principle, success condition, core tension, material constraints and assumptions, and smallest next step.
2. Use B Design to lock the Skill name, trigger description, inputs, outputs, resource boundary, and acceptance method.
3. Use C Generate to create the smallest package, or edit only an explicitly authorized target.
4. Run validate for frontmatter, resource boundaries, governance fields, and loadable structure.
5. Run trigger evaluation and output-eval separately for routing precision and delivered results; keep positive, negative, near-neighbor, and boundary cases.
6. For shared or multi-platform packages, export Skill IR, compile target contracts, and generate adapters and archives.
7. Run trust, conformance, registry audit, package verification, and install simulation.
8. Open Review Studio, resolve block and warn states, and confirm release gates, version diffs, and the rollback boundary.
9. Publish a Captain version while recording source, installed, and deployment status separately; use E Reflect for failure evidence, then make one attributable F Evolve change and rerun the checks.

## Capability Map

| Capability | What Captain 0.3 does | Main entrypoint |
| --- | --- | --- |
| CLI and auto-generation | Initializes a minimal Skill package and fills interface, manifest, and initial engineering reports | scripts/yao.py init |
| Trigger and output evaluation | Checks should-trigger, should-not-trigger, and output assertions with cases | scripts/trigger_eval.py; scripts/yao.py output-eval |
| Skill IR | Stores platform-neutral job, trigger, workflow, resource, risk, and governance contracts first | scripts/yao.py skill-ir |
| Multi-platform compilation | Compiles Skill IR into OpenAI, Claude, generic, Agent Skills, and VS Code contracts | scripts/yao.py compile-skill |
| Packaging | Generates target adapters, compatibility files, and optional ZIP archives | scripts/yao.py package |
| Install simulation | Extracts into a temporary local Skill root and loads the entrypoint, manifest, interface, and adapters | scripts/yao.py install-simulate |
| Trust and runtime conformance | Checks secrets, scripts, network, permissions, target metadata, resource paths, and degradation notes | scripts/yao.py trust; scripts/yao.py conformance |
| Registry and upgrade | Writes package metadata, compatibility, and checksums, then compares version differences | scripts/yao.py registry-audit; scripts/yao.py upgrade-check |
| Review Studio | Puts gates, blockers, warnings, evidence links, and review actions on one review surface | scripts/yao.py review-studio |
| Release gates | Selects governance, evaluation, trust, installation, and release checks by risk | references/gate-selection.md; scripts/yao.py promote-check |

## Evidence Levels

| Level | Meaning | Judgment it can support |
| --- | --- | --- |
| E1 Static | Source, metadata, contracts, links, and rules were inspected | Whether structure exists and boundaries are written |
| E2 Simulated | Deterministic cases, dry runs, package checks, or install simulations passed | Whether the controlled flow and package structure work |
| E3 Runtime | Execution happened in the intended host or Provider with recorded results | Behavior in the specified runtime |
| E4 Operational | Repeated real use produced reviewed outcomes and feedback | Long-term stability and drift under use |

Captain does not automatically promote generated reports, planned checks, or one static read into a stronger level. Each release decision should name its evidence level and uncovered boundary.

### World-class evidence collection

Run this only when E3/E4 evidence must be reviewed. It prepares submissions and validates provenance, hashes, review state, and the ledger without treating templates or planned work as completion evidence.

    SUBMISSIONS_DIR="${SUBMISSIONS_DIR:-evidence/world_class/submissions}"
    python3 scripts/yao.py world-class-preflight . --submissions-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-submission-kit . --output-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-submission-kit . --output-dir "$SUBMISSIONS_DIR" --prefill-artifacts --self
    python3 scripts/yao.py world-class-intake . --submissions-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-submission-review . --submissions-dir "$SUBMISSIONS_DIR" --self
    python3 scripts/yao.py world-class-ledger . --submissions-dir "$SUBMISSIONS_DIR" --self

## Good Fit

Captain fits:

- Personal or team work that repeats and produces an observable deliverable.
- Agent Skills that need explicit trigger boundaries, inputs, outputs, and failure handling.
- Skill packages that need cross-platform distribution, source pins, evaluation, or rollback-aware maintenance.
- Maintenance work that turns failure feedback into controlled changes.

Captain does not fit:

- One-off answers, one-off prompts, ordinary translation, or ordinary document writing.
- Ideas without stable inputs, outputs, or a success condition.
- Projects that require a complete application, backend service, production deployment, or independent account operations.

## Source Structure

The tree below lists Captain-maintained source contracts and implementation directories. Runtime reports, package artifacts, preview files, and historical homepage copies are outside this tracked source tree.

    captain-meta-skill/
    ├── README.md
    ├── SKILL.md
    ├── agents/interface.yaml
    ├── references/
    ├── scripts/
    ├── evals/
    ├── tests/
    ├── skill-ir/
    ├── runtime/
    ├── security/
    ├── registry/
    ├── templates/
    ├── manifest.json
    ├── upstream.lock.json
    ├── THIRD_PARTY_NOTICES.md
    ├── LICENSE
    └── .github/workflows/test.yml

- SKILL.md is the runtime entrypoint. It stays compact and carries the trigger surface, routing, and essential gates.
- references/ contains stable method, boundary, evaluation, distribution, and maintenance guidance.
- scripts/ contains the CLI, compiler, checkers, report generators, and gate logic.
- evals/ and tests/ contain repeatable trigger, output, distribution, and regression inputs.
- skill-ir/, runtime/, security/, and registry/ hold neutral contracts, runtime conformance, security policy, and package records.

## Installation

Global installation for Codex:

    npx -y skills add caaaptaintop/captain-meta-skill -a codex -g -y

After installation, load Captain Meta Skill and pass a concrete Skill target path to the CLI. Use --self only when the corresponding maintenance command explicitly targets Captain itself.

Authors can also clone the repository and run scripts/yao.py from its root; before release or synchronization, build and verify the archive, then run install simulation.

Development source sync defaults to the disabled mirror `~/.agents/skills.disabled/captain-meta-skill`: build and verify the archive, then run `make sync-local-install`. Use `make sync-active-install` only for an explicit active replacement; both paths require a verified archive.

## Maintenance and Sync

Captain's origin is the public release source, Yao is the read-only engineering upstream, and Dao is the read-only mechanism reference. Captain users update from Captain releases rather than letting Yao's self-update channel overwrite Captain.

When maintaining the Yao Engine:

1. Fetch upstream and inspect changes from the Yao commit recorded in upstream.lock.json.
2. Select only engineering implementation or fixes that fit Captain's boundary, preserving Captain's public identity, README, source lock, and maintenance policy.
3. Run affected checks, then run make ci-test.
4. Update the Yao version and commit pin only after source and evidence pass review, then bump Captain's own version and release notes and record the rollback boundary.

When maintaining the Dao reference, update only mechanism notes, source licensing, and required attribution. Do not merge Dao Git history or treat Dao code as Captain's implementation source.

Routine generated reports, temporary previews, raw local telemetry, raw Provider output, and temporary install directories should not become implicit public package source.

## Sources and License

- Captain Meta Skill is maintained under this repository's public identity, with versioning, releases, and downstream policy governed here, and is licensed under [MIT](LICENSE).
- The Yao Meta Skill engineering implementation and Git history come from [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill); the exact commit is in [upstream.lock.json](upstream.lock.json).
- Dao Skill is a mechanism reference only, from [gnipbao/dao-skill](https://github.com/gnipbao/dao-skill); its exact commit and attribution are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
