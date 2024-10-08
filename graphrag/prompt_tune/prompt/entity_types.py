# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity types generation."""

ENTITY_TYPE_GENERATION_PROMPT = """
目标是研究实体类型及其特征之间的联系和关系，以便理解文本中所有可用的信息。
用户的任务是{task}。
作为分析的一部分，您需要识别以下文本中出现的实体类型。
实体类型必须与用户任务相关。
避免使用一般的实体类型，如“其他”或“未知”。
这一点非常重要:不要生成冗余或重叠的实体类型。例如，如果文本包含“公司”和“组织”实体类型，则应该只返回其中一个。
不要担心数量，总是选择质量而不是数量。并确保你的答案中的所有内容都与实体提取的上下文相关。
记住，我们需要的是实体类型。
将实体类型返回为逗号分隔的字符串列表。
=====================================================================
示例部分:下面的部分包括示例输出。这些例子**必须排除在你的答案**之外。

示例1
任务:确定指定团体内的连接和组织层次。
公司A是瑞典的一家公司。公司A的主管是人B。
回应:
组织的人
例1结束

示例2
任务:确定不同哲学思想流派之间共享的关键概念、原则和论点，并追溯它们彼此之间的历史或意识形态影响。
以笛卡尔等思想家为代表的理性主义认为理性是知识的主要来源。这个学派的主要概念包括强调推理的演绎方法。
回应:
概念，人，思想流派
例2结束

示例3
任务:确定间接形成问题的所有基本力量、因素和趋势。
像松下这样的行业领导者正在争夺电池生产领域的霸主地位。他们正在大力投资于研发，并正在探索新技术以获得竞争优势。
回应:
组织、技术、行业、投资策略
例3结束
======================================================================

======================================================================
真实数据:以下部分是真实数据。你应该只使用这些真实的数据来准备你的答案。仅生成实体类型。
任务:{任务}
文字:{input_text}
回应:
{{< entity_types >}}
"""

ENTITY_TYPE_GENERATION_JSON_PROMPT = """
目标是研究实体类型及其特征之间的联系和关系，以便理解文本中所有可用的信息。
用户的任务是{task}。
作为分析的一部分，您需要识别以下文本中出现的实体类型。
实体类型必须与用户任务相关。
避免使用一般的实体类型，如“其他”或“未知”。
这一点非常重要:不要生成冗余或重叠的实体类型。例如，如果文本包含“公司”和“组织”实体类型，则应该只返回其中一个。
不要担心数量，总是选择质量而不是数量。并确保你的答案中的所有内容都与实体提取的上下文相关。
以JSON格式返回实体类型，其中“entities”作为键，实体类型作为字符串数组。
=====================================================================
示例部分:下面的部分包括示例输出。这些例子**必须排除在你的答案**之外。

示例1
任务:确定指定团体内的连接和组织层次。
Example_Org_A是瑞典的一家公司。Example_Org_A的主管是Example_Individual_B。
JSON响应:
{{"entity_types":["组织", "人员"]}}
例1结束

示例2
任务:确定不同哲学思想流派之间共享的关键概念、原则和论点，并追溯它们彼此之间的历史或意识形态影响。
以笛卡尔等思想家为代表的理性主义认为理性是知识的主要来源。这个学派的主要概念包括强调推理的演绎方法。
JSON响应:
{{"entity_types":["概念", "人物", "思想流派"]}}
例2结束

示例3
任务:确定间接形成问题的所有基本力量、因素和趋势。
像松下这样的行业领导者正在争夺电池生产领域的霸主地位。他们正在大力投资于研发，并正在探索新技术以获得竞争优势。
JSON响应:
{{"entity_types":["组织", "技术", "行业", "投资策略"]}}
例3结束
======================================================================

======================================================================
真实数据:以下部分是真实数据。你应该只使用这些真实的数据来准备你的答案。仅生成实体类型。
任务:{任务}
文字:{input_text}
JSON响应:
{{"entity_type": [<entity_type >]}}
"""
