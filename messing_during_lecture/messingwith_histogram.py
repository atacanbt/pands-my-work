# messingwith_histogram.py
# lecture notes
# author: atacan buyuktalas

import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(1) # seed the random number generator
norm_data = np.random.normal(size= 10000) # 10000 random numbers with a normal distribution

plt.hist(norm_data) # histogram of the data
plt.show() # show the plot
