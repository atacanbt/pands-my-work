# randomfruit.py
# this program prints out rondom fruit 
# author: atacan buyuktalas

import random

fruits = ['Apple', 'Banana', 'Grape', 'Watermelon', 'Melon', 'Pineapple', 'Plum', 'Orange', 'Grapefruit', 'Pear', 'Kiwi']
# solution 1
# random_fruit = random.choice(fruits)
# print('A random fruit is {}'.format(random_fruit))

# solution 2
# print('A random fruit is ' + random.choice(fruits))

# solution 3
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}".format(fruit))
