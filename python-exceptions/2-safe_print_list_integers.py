#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if str(value).isdigit() or (str(value)[0] == '-' and str(value)[1:].isdigit()):
                print("{:d}".format(int(value)), end='')
                count += 1
    except (IndexError, ValueError, TypeError):
        pass
    print()
    return count
