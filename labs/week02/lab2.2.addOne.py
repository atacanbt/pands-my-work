# addOne.py
# program reads the number given and adds 1 to tha total value
# author: Atacan Buyuktalas

number = int(input('please enter a number '))
newNumber = number + 1
# print(newNumber)
# print(f'{number} plus one is {newNumber}')
txt = "{0} plus 1 is {1}"
print(txt.format(number, newNumber))
