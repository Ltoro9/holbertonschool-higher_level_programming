#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argc = len(sys.argv)
count = 1
if argc == 1:
    print("{} arguments.".format(argc))
elif argc == 2:
    print("{} argument:".format(argc))
    print("{}: {}".format(argc, argv[argc]))
else:
    print("{} arguments:".format(argc - 1))
    my_arg = 1
    while my_arg < argc:
        print("{}: {}".format(my_arg, str(sys.argv[my_arg])))
        my_arg += 1
