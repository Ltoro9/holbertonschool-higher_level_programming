#!/usr/bin/python3
def text_indentation(text):
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

