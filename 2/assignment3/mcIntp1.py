# Monte carlo integration for problem 1
from math import cos, pi
from numpy.random import random_sample
import matplotlib.pyplot as plt

# Function Definition
def function(x):
    return (x * (cos(pi * x ) ** 2))

# Monte Carlo Intergral with default precision
def mcInt(precision = 1e-3):
    area, count, sum = 0, 1, 0
    error = []
    # Runs until error is within precision
    while(precisionCheck(area, precision)):
        # Pulls x from a uniform distribution on 0,1
        x = random_sample()
        fx = function(x)
        sum += fx
        # Computers the average
        area = sum / count
        # Appends Error
        error.append([abs(area - .25), count])
        count += 1
    return area, error

# Tolerance checking
def precisionCheck(area, precision):
    return (precision < abs(area - .25))


if __name__ == "__main__":
    # Runs the code
    area, errorConvergence = mcInt(1e-4)
    print(area)
    # Transposes the output
    transposed = [[errorConvergence[j][i] for j in range(len(errorConvergence))] for i in range(len(errorConvergence[0]))]
    # Plots
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_yscale('log')
    ax.set_ylabel("Absolute Error")
    ax.set_xlabel("Number of Random Samples")
    ax.set_title("Semilog of Absolute Error over Number of Samples")
    ax.plot(transposed[1][10:-1], transposed[0][10:-1], "-")
    ax.axhline()
    print("test")
    fig.savefig("outputp1.png")