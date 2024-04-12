# floor.py
# this program prompts a float number, rounds it down to the nearest integer and prints out the result
# author: atacan buyuktalas

import math

number_to_floor = float(input("Enter a float number: "))
floored_number = math.floor(number_to_floor)
print(f'{number_to_floor} floored is {floored_number}')

