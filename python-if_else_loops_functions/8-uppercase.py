#!/usr/bin/python3
def uppercase(str):
    my_upper = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            my_upper = my_upper + (chr(ord(letter) - 32))
        else:
            my_upper = my_upper + letter
    print('{}'.format(my_upper))
