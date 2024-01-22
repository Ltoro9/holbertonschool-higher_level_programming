#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argc = len(sys.argv)
my_arg = 1
number = 0
while my_arg < argc:
    number += int(sys.argv[my_arg])
    my_arg += 1
print(f"{number}")
