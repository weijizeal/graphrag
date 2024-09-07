# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for language detection."""

DETECT_LANGUAGE_PROMPT = """
你是一个智能助手，帮助人们分析文本文档中的信息。
给定示例文本，帮助用户确定所提供文本的主要语言是什么。
例如:“英语”、“西班牙语”、“日语”、“葡萄牙语”等等。

文字:{input_text}
语言:"""
