# messingwith_piecharts.py
# lecture notes
# author: atacan buyuktalas

import matplotlib.pyplot as plt
import numpy as np

fruit = np.array(["apple", "banana", "cherry", "date", "elderberry"]) # fruit names
numbers = np.array([10, 20, 30, 40, 50]) # number of each fruit

plt.pie(numbers, labels=fruit) # pie chart of the fruit
plt.legend() # show the label
plt.show() # show the plot