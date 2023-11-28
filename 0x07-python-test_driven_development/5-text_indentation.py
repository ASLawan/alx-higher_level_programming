#!/usr/bin/python3
"""
    Module with function that prints two newlines
    after the following characters: ., ?, :

"""


def text_indentation(text):
    """Function that prints text with 2 newlines
        after given characters
    """
    t_msg = "text must be a string"
    target = [".", "?", ":"]

    if not text or not isinstance(text, str):
        raise TypeError(t_msg)

    text = text.replace('. ', '.\n')
    text = text.replace('? ', '?\n')
    text = text.replace(': ', ':\n')
    text = text.strip()

    for i in range(len(text)):
        if text[i] in target:
            print(text[i], end="")
            print()
        else:
            print(text[i], end="")
