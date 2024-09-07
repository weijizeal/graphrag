# 版权所有 (c) 2024 Microsoft Corporation.
# 根据 MIT 许可证授权

"""包含提示定义的文件。"""

CLAIM_EXTRACTION_PROMPT = """
-目标活动-
你是一个智能助手，帮助人类分析师分析文档中针对特定实体的声明。

-目标-
根据可能与此活动相关的文本文档、实体规范和声明描述，提取所有符合实体规范的实体及针对这些实体的所有声明。

-步骤-
1. 提取所有符合预定义实体规范的命名实体。实体规范可以是实体名称列表或实体类型列表。
2. 对于步骤1中识别出的每个实体，提取与该实体相关的所有声明。声明需符合指定的声明描述，并且该实体应为声明的主题。
对于每个声明，提取以下信息：
- 主体：声明中作为主题的实体名称。主体实体是声明中描述的行为的执行者，需为步骤1中识别出的实体之一。
- 客体：声明中作为客体的实体名称。客体实体是报告/处理行为或受行为影响的实体。如果客体实体未知，使用 **NONE**。
- 声明类型：声明的总体类别。命名方式应能够在多个文本输入中重复使用，以便相似声明共享同一声明类型。
- 声明状态：**TRUE**，**FALSE** 或 **SUSPECTED**。TRUE 表示声明已确认，FALSE 表示声明被证实为假，SUSPECTED 表示声明未经证实。
- 声明描述：详细描述解释声明的原因，并包括所有相关的证据和参考。
- 声明日期：声明做出的时间段 (start_date, end_date)。开始日期和结束日期应为 ISO-8601 格式。如果声明在单一日期做出，则开始日期和结束日期设为同一天。如果日期未知，返回 **NONE**。
- 声明来源文本：从原文中提取的所有与声明相关的引用列表。

格式化每个声明为 (<subject_entity>{tuple_delimiter}<object_entity>{tuple_delimiter}<claim_type>{tuple_delimiter}<claim_status>{tuple_delimiter}<claim_start_date>{tuple_delimiter}<claim_end_date>{tuple_delimiter}<claim_description>{tuple_delimiter}<claim_source>)

3. 将步骤1和2中识别出的所有声明以英文返回为单个列表。使用 **{record_delimiter}** 作为列表分隔符。

4. 完成时，输出 {completion_delimiter}

-示例-
示例 1:
实体规范：organization
声明描述：与某实体相关的风险标志
文本：根据 2022/01/10 的一篇文章，A公司因在多个由政府机构B发布的公开招标中串标而被罚款。该公司由涉嫌在2015年从事腐败活动的C先生拥有。
输出:

(A公司{tuple_delimiter}政府机构B{tuple_delimiter}反竞争行为{tuple_delimiter}TRUE{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}A公司因在多个由政府机构B发布的公开招标中串标而被罚款，且根据2022/01/10的文章，该公司被发现存在反竞争行为{tuple_delimiter}根据2022/01/10的文章，A公司因在多个由政府机构B发布的公开招标中串标而被罚款。)
{completion_delimiter}

示例 2:
实体规范：A公司，C先生
声明描述：与某实体相关的风险标志
文本：根据2022/01/10的文章，A公司因在多个由政府机构B发布的公开招标中串标而被罚款。该公司由涉嫌在2015年从事腐败活动的C先生拥有。
输出:

(A公司{tuple_delimiter}政府机构B{tuple_delimiter}反竞争行为{tuple_delimiter}TRUE{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}2022-01-10T00:00:00{tuple_delimiter}A公司因在多个由政府机构B发布的公开招标中串标而被罚款，且根据2022/01/10的文章，该公司被发现存在反竞争行为{tuple_delimiter}根据2022/01/10的文章，A公司因在多个由政府机构B发布的公开招标中串标而被罚款。)
{record_delimiter}
(C先生{tuple_delimiter}NONE{tuple_delimiter}腐败{tuple_delimiter}SUSPECTED{tuple_delimiter}2015-01-01T00:00:00{tuple_delimiter}2015-12-30T00:00:00{tuple_delimiter}C先生涉嫌在2015年从事腐败活动{tuple_delimiter}该公司由涉嫌在2015年从事腐败活动的C先生拥有。)
{completion_delimiter}

-真实数据-
使用以下输入进行回答。
实体规范: {entity_specs}
声明描述: {claim_description}
文本: {input_text}
输出:"""


CONTINUE_PROMPT = "上次提取中遗漏了许多实体。使用相同的格式将它们添加在下面：\n"
LOOP_PROMPT = "似乎仍然有一些实体可能被遗漏了。请回答YES或NO，是否仍有需要添加的实体。\n"
