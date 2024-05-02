# messingwith_matplotlib.py
# lecture notes
# author: atacan buyuktalas

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101)) # 1 to 100
ypoints = xpoints * xpoints # x squared

plt.plot(xpoints, ypoints, label= "xsquared") # plot x squared
plt.plot(xpoints, xpoints, label= "straight", color='blue') # plot x
plt.legend() # show the label

randompoints = np.random.randint(1, 1000, 100) # 100 random numbers between 1 and 1000
plt.scatter(xpoints, randompoints, label="random", color='red') # scatter plot

plt.show() # show the plot

