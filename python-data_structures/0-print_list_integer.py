#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    argc = len(my_list)
    while i < argc:
        print("{:d}".format(my_list[i]))
        i += 1
