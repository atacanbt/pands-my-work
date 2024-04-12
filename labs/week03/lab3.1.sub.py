# sub.py
# this program prompts 2 numbers, substracts the second one from the first one and prints the answer
# author: Atacan Buyuktalas

fnum = int(input('Enter the first number: '))
snum = int(input('Enter the second number: '))
# when we input something else than integer program gives value error as we set the entry value as "int" 
answer = fnum - snum

# print(f'{fnum} minus {snum} is {answer}')
print('{} minus {} is {}'.format(fnum, snum, answer))
