# messingwith_NumPy.py
# lecture notes
# author: atacan buyuktalas

import numpy as np

list_of_numbers = [1,2,3,"asd"]
list_of_numbers = list_of_numbers + [3] # adding 3 to the list
print("list", list_of_numbers)

numbers = np.array([1,2,3,4,]) 
numbers = numbers + [1,2,3,4] # adding 3 to each element in the array, you cannot do this with a list
print("array", numbers)

rando = np.random.randint(100,200,30) # random numbers between 100 and 200, 30 of them
print("rando", rando)

normalrando = np.random.normal(100, 20, 30) # random numbers with a normal distribution, mean 100, standard deviation 20, 30 of them
print("normalrando", normalrando)

normalrando2 = np.random.normal(loc=50, scale=20, size=100) # random numbers with a normal distribution, mean 50, standard deviation 20, 100 of them
print("normalrando2", normalrando2)