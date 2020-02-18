# Monte carlo integration for problem 1
from math import cos, pi
from numpy.random import random_sample
import matplotlib.pyplot as plt

def function(x):
    return (x * (cos(pi * x ) ** 2))

def mcInt(precision = 1e-3):
    area, count, sum = 0, 1, 0
    error = []
    while(precisionCheck(area, precision)):
        x = random_sample()
        fx = function(x)
        sum += fx
        area = sum / count
        error.append([abs(area - .25), count])
        count += 1
    return area, error

def precisionCheck(area, precision):
    return (precision < abs(area - .25))


if __name__ == "__main__":
    area, errorConvergence = mcInt(1e-4)
    transposed = [[errorConvergence[j][i] for j in range(len(errorConvergence))] for i in range(len(errorConvergence[0]))]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.plot(transposed[1][10:-1], transposed[0][10:-1], "-")
    ax.axhline()
    fig.savefig("output.png")