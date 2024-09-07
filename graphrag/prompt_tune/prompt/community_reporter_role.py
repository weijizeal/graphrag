# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for community reporter role generation."""

GENERATE_COMMUNITY_REPORTER_ROLE_PROMPT = """ 
{persona} 
根据给定的文本样本，帮助用户创建一个角色定义，该角色将负责社区分析。 请查看以下示例，确定其关键部分，并根据提供的领域和您的专业知识，为提供的输入创建一个符合相同模式的新角色定义。 请记住，您的输出应在结构和内容上与示例一致。

示例： 一名技术记者正在分析Kevin Scott的《Behind the Tech Podcast》，根据社区中的实体列表及其关系以及可选的相关声明进行分析。 该报告将用于为决策者提供与社区相关的重要发展情况及其潜在影响的参考信息。

领域：{domain} 
文本：{input_text}
角色："""
