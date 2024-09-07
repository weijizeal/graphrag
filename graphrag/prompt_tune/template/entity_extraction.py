# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity extraction."""

GRAPH_EXTRACTION_PROMPT = """
-目标-
给定可能与此活动相关的文本文档和实体类型列表，从文本中识别这些类型的所有实体以及已识别实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个已标识的实体，提取以下信息:
- entity_name: 实体名
- entity_type: 以下之一的实体类型： [{entity_types}]
- entity_description: 对实体属性和活动的全面描述
将每个实体格式化为("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)

2. 从步骤1中标识的实体中，确定彼此“明显相关”的所有实体对(source_entity, target_entity) 。
对于每一对相关实体，提取以下信息:
- source_entity: 源实体的名称，如步骤1所示
- target_entity: 目标实体的名称，如步骤1所示
- relationship_description: 解释为什么你认为源实体和目标实体彼此相关
- relationship_strength: 表示源实体与目标实体之间的关系强度
将每个关系格式化为("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. 返回步骤1和步骤2中确定的所有实体和关系的单个列表。使用**{{record_delimiter}}**作为列表分隔符。

4. 完成后，输出{{completion_delimiter}}。

-例子-
######################
{examples}

-真实的数据-
######################
实体类型: [{entity_types}]
文本: {{input_text}}
######################
输出:"""

GRAPH_EXTRACTION_JSON_PROMPT = """
-目标-
给定可能与此活动相关的文本文档和实体类型列表，从文本中识别这些类型的所有实体以及已识别实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个已识别的实体，提取以下信息:
- entity_name: 实体名
- entity_type: 以下之一的实体类型： [{entity_types}]
- entity_description: 对实体属性和活动的全面描述
使用以下格式将每个实体输出格式化为JSON条目:

{{"name": <entity name>, "type": <type>, "description": <entity description>}}

2. 从步骤1中确定的实体中，确定彼此“明显相关”的所有实体对(source_entity, target_entity)。
对于每一对相关实体，提取以下信息:
- source_entity: 源实体的名称，如步骤1所示
- target_entity: 目标实体的名称，如步骤1所示
- relationship_description: 解释为什么你认为源实体和目标实体彼此相关
- relationship_strength: 表示源实体与目标实体之间的关系强度
使用以下格式将每个关系格式化为JSON条目:

{{"source": <source_entity>, "target": <target_entity>, "relationship": <relationship_description>, "relationship_strength": <relationship_strength>}}

3. 返回步骤1和步骤2中识别出的所有JSON实体和关系的单个列表。

-例子-
######################
{examples}

-真实数据-
######################
entity_types: {entity_types}
text: {{input_text}}
######################
输出:"""

EXAMPLE_EXTRACTION_TEMPLATE = """
案例 {n}:

实体类型: [{entity_types}]
文本:
{input_text}
------------------------
输出:
{output}
#############################

"""

UNTYPED_EXAMPLE_EXTRACTION_TEMPLATE = """
案例 {n}:

文本:
{input_text}
------------------------
输出:
{output}
#############################

"""


UNTYPED_GRAPH_EXTRACTION_PROMPT = """
-目标-
给定一个可能与此活动相关的文本文档，首先从文本中确定所需的所有实体，以便捕获文本中的信息和思想。
接下来，报告标识实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个已识别的实体，提取以下信息:
- entity_name: 实体名
- entity_type: 建议实体的几个标签或类别。分类不应该是具体的，而应该尽可能的一般化。
- entity_description: 对实体属性和活动的全面描述
格式化每个实体为("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)

2. 从步骤1中确定的实体中，确定彼此“明显相关”的所有对(source_entity, target_entity)。
对于每一对相关实体，提取以下信息:
- source_entity: 源实体的名称，如步骤1所示
- target_entity: 目标实体的名称，如步骤1所示
- relationship_description: 解释为什么你认为源实体和目标实体彼此相关
- relationship_strength: 表示源实体与目标实体之间的关系强度
格式化每个关系为("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. 将步骤1和步骤2中识别出的所有实体和关系返回为单个列表。使用**{{record_delimiter}}**作为列表分隔符。

4. 完成后，输出{{completion_delimiter}}。

-例子-
######################
{examples}

-真实数据-
######################
文本: {{input_text}}
######################
输出:
"""
