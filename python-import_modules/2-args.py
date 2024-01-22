#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argc = len(sys.argv)
count = 1
if argc == 1:
    print("0 arguments.")
elif argc == 2:
    print("1 argument:")
    print("1: {}".format(str(sys.argv[1])))
else:
    print("{} arguments:".format(argc - 1))
    for my_arg in range(1, argc):
        print("{}: {}".format(my_arg, str(sys.argv[my_arg])))
