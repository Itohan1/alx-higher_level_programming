#!/usr/bin/python3
""""""

def text_indentation(text):

    """"""

    if not(isinstance(text, str) or text == ''):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if (text[i] in [':', '.', '?']):
            print(text[i])
            print()
        else:
            print(text[i], end='')
        i += 1
