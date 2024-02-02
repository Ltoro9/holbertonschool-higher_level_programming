#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py
Description: prints a text with 2 new lines after each'., ? and :'
Author: Alfre, Antonio, Louis, Date: Feb 01 2024
"""
def text_indentation(text):
    """Description: prints a text with 2 new lines after each'., ? and :'
    - text is a string"""
    err = "unsupported operand type(s) for +: 'NoneType' and 'int'"
    if text is None:
        raise TypeError(err)
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    while c < len(text):
        print(text[c], end='')
        if text[c] == '.' or text[c] =='?' or text[c] == ':':
            print('\n')
            if c + 1 < len(text) and text[c + 1] == ' ':
                c += 1
        c += 1
