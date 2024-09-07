# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity summarization."""

ENTITY_SUMMARIZATION_PROMPT = """
{persona}
使用你的专业知识，你被要求生成以下提供的数据的全面总结。
给定一个或两个实体，以及一个描述列表，它们都与同一实体或一组实体相关。
请用{language}将所有这些连接成一个简洁的描述。确保包括从所有描述中收集的信息。
如果所提供的描述是矛盾的，请解决矛盾，并提供一个单一的，连贯的总结。
确保用第三人称写，并包括实体名称，这样我们就有了完整的上下文。

尽可能从附近的文本中获取相关信息，这是非常重要的。

如果没有答案，或者描述是空的，只传达文本中提供的信息。
#######
-Data-
Entities: {{entity_name}}
Description List: {{description_list}}
#######
Output:"""
