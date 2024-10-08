# 版权 (c) 2024 Microsoft Corporation.
# 根据 MIT 许可证授权

"""用于社区报告总结的微调提示。"""

COMMUNITY_REPORT_SUMMARIZATION_PROMPT = """
{persona}

# 目标
以 {role} 的身份编写一份关于社区的全面评估报告。该报告的内容包括社区主要实体和关系的概述。

# 报告结构
报告应包含以下部分：
- 标题：社区的名称，代表其关键实体 - 标题应简短但具体。在可能的情况下，标题中应包含具有代表性的命名实体。
- 概要：社区整体结构的执行概要，实体之间的关系及其与实体相关的显著点。
- 报告评级：{report_rating_description}
- 评级解释：用一句话解释评级。
- 详细发现：列出5-10个关于社区的关键见解。每个见解应包含简短的总结，并附有根据下文所列的依据规则撰写的多段解释。内容应全面。

输出应为格式良好的JSON字符串，以下格式返回。不要使用任何不必要的转义序列。输出应为单个JSON对象，可以通过json.loads进行解析。
    {{
        "title": "<report_title>",
        "summary": "<executive_summary>",
        "rating": <threat_severity_rating>,
        "rating_explanation": "<rating_explanation>",
        "findings": "[{{"summary":"<insight_1_summary>", "explanation": "<insight_1_explanation>"}}, {{"summary":"<insight_2_summary>", "explanation": "<insight_2_explanation>"}}]"
    }}

# 依据规则
在每段文字后面，如果该段内容源自一个或多个数据记录，请添加数据记录引用。引用格式为 [记录: <记录来源> (<记录ID列表>, ...<记录来源> (<记录ID列表>)].
在单个记录ID列表中不要列出超过 5 个记录 ID。相反，列出最相关的前 5 个记录 ID，并添加“+更多”以表明还有更多。
例如：
“X 先生是 Y 公司的所有者，并且面临许多不当行为的指控 [数据: 报告(1),实体(5,7)；关系(23)；声明(1、5、7、23、2,+更多)]。”

其中 1、5、7、23、2、34、46 和 64 表示相关数据记录的 ID(而非索引)。

不要包含没有提供支持证据的信息。

# 示例输入
# ----------
# 文本:

# 实体

id,entity,description
1,天安门广场,天安门广场是北京市的一个著名地标
2,人民英雄纪念碑,人民英雄纪念碑位于天安门广场的中心

# 关系

id,source,target,description
10,天安门广场,人民英雄纪念碑,人民英雄纪念碑坐落在天安门广场中央
11,天安门广场,国庆庆典,国庆庆典每年在天安门广场举行
12,人民英雄纪念碑,游客,许多游客前往天安门广场参观人民英雄纪念碑

# 输出:
{{
    "title": "天安门广场和人民英雄纪念碑",
    "summary": "该社区围绕天安门广场展开，广场是北京市的重要地标。天安门广场与人民英雄纪念碑有直接关系，许多游客前往参观，此外，天安门广场也是国庆庆典的举办地。",
    "rating": 4.5,
    "rating_explanation": "该区域具有历史和文化的重要性，吸引了大量游客，特别是在国庆期间，影响力巨大。",
    "findings": [
        {{
            "summary": "天安门广场作为历史文化地标",
            "explanation": "天安门广场是北京市的中心地带，作为重要的历史文化地标，具有广泛的影响力。每年，广场吸引了大量国内外游客，特别是在重大节日如国庆庆典时。 [记录: 实体 (1), 关系 (11)]"
        }},
        {{
            "summary": "人民英雄纪念碑的意义",
            "explanation": "人民英雄纪念碑位于天安门广场的中心，是为了纪念为中国革命事业献身的人民英雄。它不仅是历史纪念碑，还具有重要的教育意义，吸引了成千上万的游客前来缅怀先烈。 [记录: 实体 (2), 关系 (10, 12)]"
        }},
        {{
            "summary": "天安门广场与游客的互动",
            "explanation": "每年，成千上万的游客涌向天安门广场，参观人民英雄纪念碑，体验历史氛围。这种人与地标的互动增强了该地区的文化和社会价值，特别是在国庆节等重大活动期间。 [记录: 关系 (12)]"
        }}
    ]
}}


# 实际数据

使用以下文本作为你的回答依据。不要在回答中杜撰任何内容。

文本:
{{input_text}}
输出:"""
