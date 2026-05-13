# AI Level Skill

一个短测 AI 应用等级的 Codex Skill。

它不是让用户自评“我会不会用 AI”，而是用 3 个基础问题做软分流，再给一个更适合当前用法的真实场景和必要追问，判断用户大概处在哪一段，并给出下一步建议。

## 适合谁

- 想快速了解自己 AI 应用水平的同事。
- 想判断团队成员是不是只会“问 AI”，还是已经能设计流程、工具和复用系统。
- 想把 AI 能力讨论从口号拉回真实操作的人。

## 怎么用

安装后，在 Codex 里输入：

```text
/ai-level
```

或直接说：

```text
AI-level，帮我测一下 AI 应用等级
```

测试一般包括：

1. 三个基础选择题。
2. 根据基础回答选择一个生活、工作、创作或系统设计场景。
3. 如果回答里出现 Agent、Skill、MCP、自动化或复用系统，会追加一个落地追问。
4. 输出等级区间、确认等级、判断依据和下一步建议。

基础题只负责选题，不直接定级。最终等级仍然看实操回答、追问证据和是否有真实产物/复用/迭代。

## 一键安装

### 推荐：用 Codex Skill Installer

把下面这句话发给 Codex：

```text
请用 skill-installer 安装这个 skill：
https://github.com/a905818999-del/ai-level-skill/tree/v0.1.2/ai-level
```

也可以直接运行系统自带安装脚本：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo a905818999-del/ai-level-skill --ref v0.1.2 --path ai-level
```

安装后重启 Codex，让新 skill 生效。

### 本地安装

如果你已经下载或克隆了这个仓库，在当前目录运行：

```powershell
.\install.ps1
```

如果本地已经安装过，想覆盖：

```powershell
.\install.ps1 -Force
```

## 同事群分享文案

可以直接发这一段：

```text
我做了一个 AI 应用等级小测试，不是那种很长的问卷。

它会先用 3 个小问题判断大概测试区间，再给你一个真实场景，看你到底是“会问 AI”，还是已经能把 AI 做成流程、工具或可复用系统。

安装链接：
https://github.com/a905818999-del/ai-level-skill/tree/v0.1.2/ai-level

安装后在 Codex 里输入 /ai-level 就能开始。
大概 3-5 分钟，最后会给你一个等级区间、确认等级和下一步建议。
```

## 发布前验证

当前版本已经跑过：

- `npm test`
- `python ai-level\scripts\sample_run.py --check`
- `quick_validate.py ai-level`
- `quick_validate.py C:\Users\zhen.qian\.codex\skills\ai-level`
- `python -m py_compile ai-level\scripts\sample_run.py`
- 模拟同事样本试跑：`release/simulated-colleague-trials-20260512.md`
- 全场景矩阵 QA：`release/qa-all-scenarios-all-levels-ceo-review-20260513.md`
- 场景库严格评审：`release/scenario-bank-full-review-20260513.md`

## 目录

```text
ai-level/
  SKILL.md
  agents/openai.yaml
  references/
    scenario-bank.md
  scripts/sample_run.py
release/
  simulated-colleague-trials-20260512.md
install.ps1
package.json
README.md
```
