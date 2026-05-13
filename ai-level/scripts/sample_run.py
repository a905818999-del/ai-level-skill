import argparse
from pathlib import Path
import textwrap


BASELINE_ANSWER = "1C 2CD 3D"

MAIN_ANSWER = """\
考虑到复用以及外部信息的获取我会用 workbuddy 或者 openclaw，做成一个 skill。

调用小红书 / 12306 等 MCP 或者 skill 完成衣食住行的信息收录。

通过对话让 openclaw 帮我做这个 skill，简单测一下看方案是否可行，信息是否准确，然后就放给他做。

做完让他产出一个 HTML，方便分享给同行的人。
"""

ANCHOR_ANSWER = """\
1. 我会先定取舍顺序：老人不要太累优先，其次是交通住宿安全和方便，再是小孩每天有一个期待点，预算可以小幅浮动，景点数量排最后。
2. 我会要求 Agent 输出工具调用记录、来源链接、查询时间和关键字段截图或引用；像火车票和酒店这种最终还要自己点进去确认，避免它假装查过。
3. 反馈不会只说“再改改”，我会按固定检查项改：每天步行强度、交通折返、预算偏差、老人休息点、小孩兴趣点、来源是否过期。改完后让它说明这一版具体改了什么。
"""

EVAL_CASES = [
    {
        "name": "beginner-route",
        "baseline": "1A 2A 3A",
        "scenario": "First Real Ask",
        "answer": "我可能只会问 AI：帮我写一下。如果不好，我就再问一次。",
        "expected": "确认 Lv.1",
        "must_include": ["不要急着上工具", "先学会补充对象、语气、限制和例子"],
        "must_not_include": ["Agent", "Skill", "MCP", "确认 Lv.3"],
    },
    {
        "name": "mid-workflow-route",
        "baseline": "1C 2C 3B",
        "scenario": "Expensive Family Purchase",
        "answer": "我会告诉 AI 预算、用途和家里人在意的点，让它解释参数、做对比表、列风险，再提醒我哪些信息要自己核对。",
        "expected": "确认 Lv.4-Lv.5",
        "must_include": ["能把模糊购买决策拆成标准和核对项", "下一步是固定成一张决策表"],
        "must_not_include": ["确认 Lv.6", "确认 Lv.7"],
    },
    {
        "name": "high-baseline-weak-answer",
        "baseline": "1D 2D 3D",
        "scenario": "Personal Workflow Automation",
        "answer": "我会让 Agent 搜资料、总结、生成结果。如果不行就让它再改，之后可以做成 Skill。",
        "expected": "确认 Lv.6",
        "must_include": ["工具名不是证据", "还没看到输入规则、校验规则和复用后的改进"],
        "must_not_include": ["确认 Lv.7", "确认 Lv.8"],
    },
    {
        "name": "real-lv7-system-designer",
        "baseline": "1D 2CD 3D",
        "scenario": "Knowledge Product Launch",
        "answer": "我会先定义受众和产物标准，收集材料到 source folder，让 AI 聚类、出结构、写初稿，再跑反 slop 检查和事实核对。最后输出分享页，并保留输入模板、检查表和失败处理规则，下次复用。",
        "expected": "确认 Lv.7",
        "must_include": ["已经在设计流程，而不是只让 AI 生成内容", "Lv.8 还需要真实跑过、复用过、改进过"],
        "must_not_include": ["确认 Lv.8"],
    },
    {
        "name": "real-lv8-evidence",
        "baseline": "1D 2D 3D",
        "scenario": "Personal Workflow Automation",
        "answer": "这个周报流程已经跑了四次。第一版只汇总链接，第二周误收了几条无关内容，所以我加了来源时间、why-it-matters、reject reason 和人工确认字段。现在同事也能填 source folder 跑同一套模板。",
        "expected": "确认 Lv.8",
        "must_include": ["有多次运行、失败后改规则、可复用产物", "如果同事能稳定使用，才继续看 Lv.9/Lv.10"],
        "must_not_include": ["确认 Lv.10"],
    },
    {
        "name": "lv9-signal-not-confirmed",
        "baseline": "1D 2D 3D",
        "scenario": "Personal AI Operating System",
        "answer": "我的方法是 AI 做资料扩展、反方评审和初稿，我自己定目标、排序冲突和做最终判断。旅行、采购、学习和项目复盘都用类似结构。",
        "expected": "Lv.9 signal｜确认 Lv.8-Lv.9",
        "must_include": ["方法论语言很强", "还需要跨场景真实产物或别人能用的证据"],
        "must_not_include": ["确认 Lv.10"],
    },
]


def dedent(text):
    return textwrap.dedent(text).strip()


def render_welcome():
    return dedent(
        """
        欢迎来到 AI 应用等级测试。

        这个测试不是让你自评“我有多会用 AI”，而是通过一个简单场景，看你会如何把 AI 用到真实问题里。

        等级大致分成 10 级：

        Lv.0 旁观者：知道 AI，但基本没用过。
        Lv.1 尝鲜者：偶尔问 AI，要什么给什么。
        Lv.2 对话者：会追问、补充背景，让回答变好。
        Lv.3 驯化师：会给约束、格式、例子，能控制输出质量。
        Lv.4 越境者：开始用 AI 做自己不熟悉领域的事。
        Lv.5 织网者：把 AI 嵌入固定流程，有模板和检查清单。
        Lv.6 召唤师：会用 Agent、工具或外部资料完成多步任务。
        Lv.7 铸造师：会设计自己的 Skill、Agent 流程或复用系统。
        Lv.8 造物主：能持续产出可用作品、工具或系统，并不断复用改进。
        Lv.9 觉醒者：形成自己的人机协作方法论，知道哪些交给 AI，哪些必须自己判断。
        Lv.10 一人军团：有成熟的 AI 工作系统，一个人能完成过去一个小团队的产出。

        测试怎么进行：
        1. 先用 3 个小问题了解你的基础使用情况。
        2. 再根据你的基础回答，给你一个更适合你当前用法的真实场景，看你会怎么用 AI 解决。
        3. 如果有些地方需要看得更清楚，会补一个追问。
        4. 最后给出等级区间、确认等级、判断依据和下一步建议。

        选择题说明：
        - 第 1 题单选。
        - 第 2 题可以选 1-2 个最符合你的做法。
        - 第 3 题单选，选你已经稳定做到的最高一项。

        没有标准答案。请按你真实会做的方式回答。
        """
    )


def render_baseline():
    return dedent(
        f"""
        先回答这 3 个基础问题即可，直接写选项，例如 `1C 2CD 3D`。
        第 2 题可以多选，其余题单选。

        1. 过去 30 天，你有没有用 AI 做过真实任务？
           A. 很少或基本没有
           B. 有，主要是写作、总结、翻译、搜索类帮助
           C. 有，用在真实工作或生活决策里，结果确实被使用
           D. 有，而且经常用模板、工具、工作流或 Agent

        2. 当 AI 给出一个很弱或不可靠的答案时，你通常怎么做？
           A. 重新问，或者换个工具
           B. 让它写详细一点
           C. 补充背景、限制条件、例子或输出格式
           D. 拆任务、要求来源、标注不确定性，并验证关键信息

        3. 你有没有把某种 AI 用法变成可复用的东西？
           A. 没有
           B. 保存过 prompt 或示例
           C. 有 checklist、模板或重复流程
           D. 做过或用过 Agent / Skill / MCP / 工具流来重复处理任务

        样例回答：{BASELINE_ANSWER}
        """
    )


def render_scenario():
    prompt = dedent(
        """
        收到。你的基础信息显示：你已经把 AI 用在真实任务里，也有验证意识和工具流经验。
        我会给你一个更适合你当前用法的生活场景。基础题只负责选题，不直接定级。

        你要安排一次 5 天家庭旅行。同行里有老人、小孩和成年人，大家体力、兴趣和耐心都不一样。

        预算不能乱花，时间在下个月，交通、天气、人流、住宿评价都可能变化。
        你希望最后不是一份漂亮攻略，而是一份同行人真的能照着走、也知道为什么这么安排的方案。

        如果你准备用 AI 帮你把这件事做好，你会怎么做？

        样例回答：
        """
    )
    return f"{prompt}\n{MAIN_ANSWER.strip()}"


def render_anchor():
    prompt = dedent(
        f"""
        你已经说了会用 workbuddy / openclaw 调用 12306、小红书、浏览器等信息源，最后生成 HTML，也可能沉淀成 Skill。

        我只追三个还没看清的点：

        1. 如果“老人不累、小孩开心、预算不爆、你自己也想玩”发生冲突，你会让 AI 按什么顺序取舍？
        2. 你会怎么确认 Agent 真的调用了 12306 / 携程 / 浏览器，而不是只编了一个看起来像真的结果？
        3. 你说会反馈微调。这个反馈是随口说“再改改”，还是有固定检查项，比如步行强度、预算偏差、来源新鲜度、每天兴趣点？

        样例回答：
        """
    )
    return f"{prompt}\n{ANCHOR_ANSWER.strip()}"


def render_report():
    return dedent(
        """
        你的 AI 应用等级：Lv.7-Lv.8｜确认 Lv.7
        证据强度：E2

        一句话：
        你已经不是“会问 AI”的阶段了。你的思路是把问题拆成 Agent / Skill / 外部信息源 / 可分享产物，这已经很 Lv.7。

        为什么这么判：
        - 你会先想到复用，而不是只做一次旅行攻略。
        - 你知道要接外部信息源，比如 12306、小红书、携程、浏览器抓取。
        - 你会要求 reference，也会自己点进去确认，说明不是盲信模型。
        - 你考虑最终产物 HTML，说明你在想“怎么让别人真的用起来”。

        离 Lv.8 差在哪：
        Lv.8 的核心不是“我能搭一个 Skill”，而是“这个 Skill 真跑过、真产出过、还能复用改进”。

        大佬视角会这么看：你现在不缺执行力，缺的是决策标准。

        Agent 能帮你跑资料、出方案、做页面，但它不知道你真正认为什么叫“好”。这个标准如果不写进去，系统跑得越快，只是越快地产出一堆看起来不错、但不一定适合你的东西。

        往 Lv.8 走，重点不是再接一个工具，而是把三件事钉住：
        - 先定取舍顺序。老人不累、小孩开心、预算不爆、路线顺，这些都对，但不能并列第一。你要先给系统一个排序，否则它只会做平均分方案。
        - 把校验前置。不要等方案出来以后再人工挑错。直接要求每个关键结论带来源、查询时间、风险标记和待确认项。好系统不是少犯错，而是让错误更容易被抓住。
        - 留下结构，不要只留下结果。一次旅行攻略没什么价值。真正有价值的是：下次任何“多人、多偏好、多约束”的决策，都能复用这套输入、排序、校验、输出结构。

        一句话：Lv.8 不是让 AI 多干活，是让 AI 按你的标准干活。

        下一步怎么升：
        大佬的实际操作会更像这样：

        1. 先写一条决策原则，而不是先搜攻略。
        示例：这次旅行宁可少玩两个点，也不能让老人累崩；孩子每天必须有一个期待点；预算可以浮动 10%，但不能靠牺牲住宿安全感来省钱。

        2. 让 Agent 先出“决策表”，不是直接出行程。
        表里至少有：方案、适合谁、不适合谁、最大风险、证据来源、需要人工确认的地方。先选方向，再排行程。

        3. 给每个方案加一个反方评审。
        让 AI 专门挑刺：这个方案为什么可能失败？老人会在哪里累？孩子会在哪里无聊？预算最容易在哪里失控？

        4. 最后再生成分享页。
        分享页不是展示“攻略多丰富”，而是让同行人快速确认：我们为什么选这个方案，放弃了什么，风险在哪里，备选是什么。

        你的下一步，就是把这个旅行规划变成一个“可分享的旅行决策页”，让别人一眼看懂你的取舍逻辑，而不是只看到一份攻略。

        一个小挑战：
        跑一次 Travel Skill v0.1，最后产出一个 HTML 页面，里面只放 5 个东西：

        1. 2-3 个候选方案，不要只给一个最优解。
        2. 每个方案适合谁、不适合谁。
        3. 关键事实的来源和查询时间。
        4. 老人累 / 小孩无聊 / 预算超支时的备选调整。
        5. 一句话复盘：这个流程下次哪里可以直接复用。

        做到这一步，你就不是“会用 AI 规划旅行”，而是开始有一个能反复长出来的小系统了。
        """
    )


def build_output():
    sections = [
        "# /ai-level sample run",
        render_welcome(),
        render_baseline(),
        render_scenario(),
        render_anchor(),
        render_report(),
        render_eval_summary(),
    ]
    return "\n\n---\n\n".join(sections)


def render_eval_summary():
    lines = ["# multi-route regression cases"]
    for case in EVAL_CASES:
        lines.extend(
            [
                "",
                f"## {case['name']}",
                f"Baseline: {case['baseline']}",
                f"Scenario: {case['scenario']}",
                f"Answer: {case['answer']}",
                f"Expected: {case['expected']}",
                "Required report signals:",
            ]
        )
        for phrase in case["must_include"]:
            lines.append(f"- {phrase}")
        lines.append("Forbidden over-scoring:")
        for phrase in case["must_not_include"]:
            lines.append(f"- {phrase}")
    return "\n".join(lines)


def run_checks(output):
    forbidden_phrases = [
        "高阶信号，所以我先不急",
        "高阶信号，会追加",
        "铆钉追问来确认是不是已经真的做得到",
        "我在评估",
        "我想看一下你会怎么把它真正落地。请具体说明这个流程：",
        "- 需要哪些输入？",
        "- 会调用哪些信息源？每个信息源解决什么问题？",
    ]
    for phrase in forbidden_phrases:
        if phrase in output:
            raise AssertionError(f"forbidden internal phrasing leaked: {phrase}")

    required_phrases = [
        "第 2 题可以多选",
        "基础题只负责选题，不直接定级",
        "你的 AI 应用等级：Lv.7-Lv.8｜确认 Lv.7",
        "离 Lv.8 差在哪",
        "可分享的旅行决策页",
        "我只追三个还没看清的点",
        "你已经说了会用 workbuddy / openclaw",
    ]
    for phrase in required_phrases:
        if phrase not in output:
            raise AssertionError(f"required phrase missing: {phrase}")

    if "匹配难度" in output:
        raise AssertionError("user-facing exam-like wording leaked: 匹配难度")

    for case in EVAL_CASES:
        if case["name"] not in output:
            raise AssertionError(f"eval case missing from output: {case['name']}")
        if case["expected"] not in output:
            raise AssertionError(f"eval expected result missing: {case['name']}")
        for phrase in case["must_include"]:
            if phrase not in output:
                raise AssertionError(f"eval required phrase missing ({case['name']}): {phrase}")

    lv8 = next(case for case in EVAL_CASES if case["name"] == "real-lv8-evidence")
    lv8_block = _case_block(output, lv8["name"])
    if "多次运行" not in lv8_block or "失败后改规则" not in lv8_block:
        raise AssertionError("Lv.8 case missing reuse/iteration evidence")

    root = Path(__file__).resolve().parents[1]
    scenario_bank = root / "references" / "scenario-bank.md"
    if not scenario_bank.exists():
        raise AssertionError("scenario-bank.md missing")

    scenario_text = scenario_bank.read_text(encoding="utf-8")
    scenario_required = [
        "First Real Ask",
        "Family Travel 2.0",
        "Personal Workflow Automation",
        "Personal AI Operating System",
        "Baseline selects the lane; practical evidence confirms the level.",
    ]
    for phrase in scenario_required:
        if phrase not in scenario_text:
            raise AssertionError(f"scenario-bank phrase missing: {phrase}")

    anchor_required = [
        "Home Move And New Setup",
        "Expensive Family Purchase",
        "Eight-Week Learning Sprint",
        "Messy Work Rescue",
        "Knowledge Product Launch",
        "Personal Workflow Automation",
        "Personal AI Operating System",
        "Scenario-Specific Anchor Examples",
    ]
    for phrase in anchor_required:
        if phrase not in scenario_text:
            raise AssertionError(f"scenario-specific anchor missing: {phrase}")


def _case_block(output, case_name):
    marker = f"## {case_name}"
    start = output.index(marker)
    next_start = output.find("\n## ", start + len(marker))
    if next_start == -1:
        return output[start:]
    return output[start:next_start]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="run regression checks")
    args = parser.parse_args()

    output = build_output()
    if args.check:
        run_checks(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
