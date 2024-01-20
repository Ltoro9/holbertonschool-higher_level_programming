#!/usr/bin/python3
def print_last_digit(number):
    digit = int(str(number)[-1])
    print(f"{digit}", end='')
    return digit
