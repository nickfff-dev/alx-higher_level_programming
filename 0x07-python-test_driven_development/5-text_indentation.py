#!/usr/bin/python3
"""

This module contains a function that indents texts

"""


def text_indentation(text):
    """
    Add indentation to the given text.

    Args:
        text (str): The original text.

    Raises:
        TypeError: If 'text' is not a string.

    Returns:
        None: Prints the indented text.
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    special_chars = ['.', ':', '?', '!']
    indented_text = text

    for char in special_chars:
        indented_text = indented_text.replace(char, char + '\n\n')

    print('\n'.join(line.strip() for line in indented_text.split('\n')
                    if line.strip()))
