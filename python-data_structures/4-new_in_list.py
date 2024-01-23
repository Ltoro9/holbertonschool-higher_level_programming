#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    argc = len(my_list)
    new_list = my_list[:]
    new_list[idx] = element
    if idx < 0 or idx >= argc:
        return my_list[:]
    else:
        return new_list
