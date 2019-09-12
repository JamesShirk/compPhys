# James Shirk, September 12,  2019 for Dr. Pratt Computational Physics class assignment 1, problem 1
import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
import math

# function for first table
def dataInterpolation():
    # Takes in the data and stores it in a pandas dataframe, then creates two single column dataframes
    # Containing x and y values for readability
    data = pd.read_csv("data.txt")
    x = data.loc[: ,"Voltage"]
    y = data.loc[: ,"Current"]
    # Interpolates the function using a cubic spline
    f = interpolate.interp1d(x, y, kind = "cubic")
    xnew = np.linspace(-1.5, 0, endpoint = True)
    # Plots the original function as points and the interpolation as a line
    plt.plot(x, y, "o", xnew, f(xnew), "-")
    plt.legend(["data", "cubic spline"], loc="best")
    plt.savefig("data.png", dpi = 1000)

# function for extended table
def dataInterpolationExtended():
    # Takes in the extended dataframe and stores it in a pandas dataframe, then creates two single column dataframes
    # Containing x and y values for readability
    data = pd.read_csv("dataExtended.txt")
    x = data.loc[: ,"Voltage"]
    y = data.loc[: ,"Current"]
    # Interpolates the function using a cubic spline
    f = interpolate.interp1d(x, y, kind = "cubic")
    xnew = np.linspace(-1.5, 4.5, endpoint = True)
    # Plots the original function as points and the interpolation as a line
    plt.plot(x, y, "o", xnew, f(xnew), "-")
    plt.legend(["data", "cubic spline"], loc="best")
    plt.savefig("dataExtended.png", dpi = 1000)

# Runs the functions on running the script
if __name__ == "__main__":
    dataInterpolation()
    dataInterpolationExtended()

    