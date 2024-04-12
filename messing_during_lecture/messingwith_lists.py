# messingwith_lists.py
# code examples from the lecture
# author: atacan buyuktalas
'''
ages = [12,21,23,34, 'asdasd']

sum = 0

for age in ages:
    sum += age
print(sum)
'''

ages = [12,21,23,34, 'asdasd']

sum = 0

length_of_list = len(ages)
for i in range (0, length_of_list):
    sum += ages[i]