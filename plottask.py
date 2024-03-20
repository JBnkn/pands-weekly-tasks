# plottask.py
# author: Joseph Benkanoun
# write a program that displays:
# a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, and
# a plot of the function h(x)=x3 in the range 0 to 10
# on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

values = np.random.normal(loc=5, scale=2, size=1000)

plt.hist(values)
plt.show()