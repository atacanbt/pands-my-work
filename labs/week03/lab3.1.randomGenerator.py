# randomGenerator.py
# this program prints out random number between 1 and 10
# authot: atacan buyuktalas
'''
import random

number = random.randint(1,10)
print("Here is a random number {}".format(number))
'''
range_start = int(input('Enter the start of the range: '))
range_end = int(input('Enter the end of the range: '))
import random
number = random.randint(range_start, range_end)
print(number)
