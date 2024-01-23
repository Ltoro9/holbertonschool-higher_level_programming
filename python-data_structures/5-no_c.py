#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for _ in my_string:
        if _.lower() not in {'c', 'C'}:
            new_string += _
    return new_string
