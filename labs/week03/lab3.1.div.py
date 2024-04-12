# div.py
# this program prompts two number, divides the first one by the second one and prints the integer and remainder results
# author: atacan buyuktalas

fnum = int(input('Enter the first number: '))
snum = int(input('Enter the second number: '))

answer_integer = fnum // snum
answer_remainder = fnum % snum

print("{} divided by {} is {} with the remainder {}".format(fnum, snum, answer_integer, answer_remainder))
