# strategies/separator.py
# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A module containing run method definition for separator strategy.verb: text_chunk
"""

from collections.abc import Iterable
from typing import Any
from datashaper import ProgressTicker
from graphrag.index.verbs.text.chunk.typing import TextChunk


def run(
    input: list[str], args: dict[str, Any], tick: ProgressTicker
) -> Iterable[TextChunk]:
    """
    Chunks text into multiple parts based on a separator. A pipeline verb.

    Args:
        input: list of text strings to be chunked.
        args: a dictionary containing the chunking strategy arguments, such as separator.
        tick: progress ticker for reporting progress.

    Returns:
        An iterable of TextChunk objects, where each chunk is a part of the input text.
    """
    # Get separator from the args, default to space if not provided
    separator = args.get("separator", " ")

    for doc_idx, text in enumerate(input):
        # Split the text using the provided separator
        chunks = text.split(separator)

        # Yield each chunk as a TextChunk object
        for chunk in chunks:
            if chunk.strip():  # Ignore empty or whitespace chunks
                yield TextChunk(
                    text_chunk=chunk,
                    source_doc_indices=[doc_idx],
                )
        tick(1)
