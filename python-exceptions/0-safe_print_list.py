#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0

    while i < x:
        try:
            print(f"{my_list[i]}", end='')
            count += 1
        except IndexError:
            pass
        i += 1

    print()
    return count
