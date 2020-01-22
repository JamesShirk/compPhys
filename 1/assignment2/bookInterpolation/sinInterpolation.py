# James Shirk, September 12,  2019 for Dr. Pratt Computational Physics class assignment 1, problem 1
import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
import math

# Takes in argument n points and plots a interpolation of nPoints of sin
def sinInterpolation(nPoints):
    # Creates x and y arrays where x has nPoints and y is sin of x
    x = np.linspace(0, 2*math.pi, nPoints, endpoint = True)
    y = [math.sin(i) for i in x]
    # interpolates x and y using cubic spline
    f = interpolate.interp1d(x, y, kind = "cubic")
    xnew = np.linspace(0, 2*math.pi, endpoint = True)
    # Ensures that it only plots the base sin function a single time from 0 to 2pi every pi/2 
    # allows for iteration of function
    if nPoints == 5:
        plt.plot(x, y, "o")
    # Plots iteration
    plt.plot(xnew, f(xnew), "--")

# Executes starting script
if __name__ == "__main__":
    # Creates an array of strings to put in legend
    legend = ["sin"]
    # Iterates (upperbound - 1) - 5 times plotting the new iteration each time
    # Appends new value to the legends
    for x in range(5, 10):
        sinInterpolation(x)
        legend.append(str(x) + " terms")
    # Adds the legend, saves the file, and closes the plot
    plt.legend(legend, loc="best")
    plt.savefig("sinInterpolation.png", dpi = 1000)
    plt.close()
