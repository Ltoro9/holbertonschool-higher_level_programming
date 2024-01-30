#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    for i in roman_string:
        value = roman_numbers[i]
        if value == 0:
            return 0
        if value > prev_value:
            prev_value = value - prev_value
        else:
            prev_value += value
    return prev_value
