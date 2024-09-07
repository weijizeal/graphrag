# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for domain generation."""

GENERATE_DOMAIN_PROMPT = """
你是一名智能助手，帮助用户分析文本文档中的信息。 根据给定的文本样本，帮助用户分配一个描述性的领域，用于总结该文本的主题。 示例领域包括：“社会研究”、“算法分析”、“医学科学”等。

文本：{input_text} 
领域:"""
