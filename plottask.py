# plottask.py
# author: Joseph Benkanoun
# write a program that displays:
# a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, and
# a plot of the function h(x)=x3 in the range 0 to 10
# on the one set of axes.

# TBD - look here for two different scales
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html

# import numpy for distribution generation
# import matplotlib for plotting
import numpy as np
import matplotlib.pyplot as plt

# including a clear function at the start to clear existing plot each time I iterate over the code
plt.clf()

# define the histogram using normal distribution
# used documentation at https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
values = np.random.normal(loc=5, scale=2, size=1000)
plt.hist(values)

# define the function
def h(x):
    return x**3

# generate x values and use them to generate y values
# generate 300 points in the range 0 to 10 to create the plot
# documentation at https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
x_values = np.linspace(0, 10, 300) 
y_values = h(x_values)


# generate the plot
plt.plot(x_values, y_values, label='$h(x) = x^3$')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.title('Plot of h(x) = x^3')
plt.grid(True)
plt.legend(['h(x)=x3'])
plt.xlim([0, 10])
plt.show()