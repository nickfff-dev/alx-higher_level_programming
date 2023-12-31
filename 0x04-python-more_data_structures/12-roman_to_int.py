#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    nums = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(roman_string)):
        if (i > 0 and nums[roman_string[i]] > nums[roman_string[i - 1]]):
            integer += \
                nums[roman_string[i]] - 2 * nums[roman_string[i - 1]]
        else:
            integer += nums[roman_string[i]]
    return integer
