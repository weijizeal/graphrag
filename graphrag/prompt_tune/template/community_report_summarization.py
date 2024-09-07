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
每段之后，添加数据记录参考，如果段落内容来自一个或多个数据记录。引用格式为[records: <record_source> (<record_id_list>, ...<record_source> (<record_id_list>)]. 如果有超过5条数据记录，显示最相关的前5条记录。每段应包含多句解释和具体的例子，并引用具体的命名实体。所有段落必须在开头和结尾都有这些参考。若无相关角色或记录，使用 "NONE"。

参考添加后的示例段落：
这是输出文本的一个段落 [records: Entities (1, 2, 3), Claims (2, 5), Relationships (10, 12)]

# 示例输入
-----------
文本:

实体

id,entity,description
5,ABILA CITY PARK,Abila 市公园是POK集会的地点

关系

id,source,target,description
37,ABILA CITY PARK,POK RALLY,Abila 市公园是POK集会的地点
38,ABILA CITY PARK,POK,POK在Abila 市公园举办集会
39,ABILA CITY PARK,POKRALLY,POKRally在Abila 市公园举行
40,ABILA CITY PARK,CENTRAL BULLETIN,Central Bulletin报道了在Abila 市公园举行的POK集会

输出:
{{
    "title": "Abila 市公园与POK集会",
    "summary": "该社区围绕Abila 市公园展开，该公园是POK集会的地点。公园与POK、POKRally以及Central Bulletin有关系，这些都与集会活动相关。",
    "rating": 5.0,
    "rating_explanation": "由于POK集会期间可能会发生动荡或冲突，因此影响评级为中等。",
    "findings": [
        {{
            "summary": "Abila 市公园作为中心位置",
            "explanation": "Abila 市公园是该社区的核心实体，作为POK集会的地点。该公园是所有其他实体的共同联系，表明其在社区中的重要性。该公园与集会的关联可能会导致如公共秩序紊乱等问题，具体取决于集会的性质及其引发的反应。 [records: Entities (5), Relationships (37, 38, 39, 40)]"
        }},
        {{
            "summary": "POK 在社区中的角色",
            "explanation": "POK是该社区的另一个关键实体，它是Abila 市公园集会的组织者。根据POK的性质及其集会的目的，它可能会成为潜在的威胁来源，具体取决于其目标及引发的反应。理解POK与公园的关系是了解该社区动态的关键。 [records: Relationships (38)]"
        }},
        {{
            "summary": "POKRALLY作为重要事件",
            "explanation": "POKRALLY是Abila 市公园发生的一个重要事件。该事件是社区动态的关键因素，具体取决于集会的性质及其引发的反应，它可能会成为潜在的威胁来源。理解集会与公园的关系是了解该社区动态的关键。 [records: Relationships (39)]"
        }},
        {{
            "summary": "Central Bulletin的角色",
            "explanation": "Central Bulletin正在报道Abila 市公园的POK集会，这表明该事件已引起媒体的关注，这可能会放大其对社区的影响。Central Bulletin的角色可能在塑造公众对该事件及其涉及实体的看法中发挥重要作用。 [records: Relationships (40)]"
        }}
    ]

}}

# 实际数据

使用以下文本作为你的回答依据。不要在回答中杜撰任何内容。

文本:
{{input_text}}
输出:"""
