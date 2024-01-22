#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argc = len(sys.argv)
count = 1
if argc == 1:
    print("0 arguments.")
elif argc == 2:
    print("1 argument:")
    print("{}: {}".format(count, str(sys.argv[1])))
else:
    print("{} arguments:".format(argc - 1))
    my_arg = 1
    while my_arg < argc:
        print("{}: {}".format(my_arg, str(sys.argv[my_arg])))
        my_arg += 1
