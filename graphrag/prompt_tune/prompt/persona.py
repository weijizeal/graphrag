# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for persona generation."""

GENERATE_PERSONA_PROMPT = """
你是一个智能助手，帮助人们分析文本文档中的信息。
给定特定类型的任务和示例文本，通过生成3到4个句子来描述可以帮助解决问题的专家来帮助用户。
使用类似于下面的格式:
您是专家{{角色}}。你擅长{{相关技能}}。你擅长帮助别人完成{{特定任务}}。

任务:{sample_task}
角色描述:"""
