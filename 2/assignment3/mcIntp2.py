# Monte carlo integration for problem 1
from math import cos, pi, exp, sqrt
from numpy.random import normal
import matplotlib.pyplot as plt

# From wolfram alpha using ""
# integral from -inf to inf of (e^((-(x-3)^2)/2) + e^((-(x-6)^2)/2)) * (1/(sqrt(2*pi))) * e^(-(x^2)/2)
analyticalResult = (1 + exp(27./4)) / (sqrt(2) * exp(9))
mu = 0
sigma = 1

def function(x):
    firstExponential = exp(-((x-3)**2) / 2)
    secondExponential = exp(-((x-6)**2) / 2)
    return firstExponential + secondExponential

def mcInt(precision = 1e-5):
    area, count, sum = 0, 1, 0
    error = []
    while(precisionCheck(area, precision)):
        x = normal(mu, sigma, 1)
        fx = function(x)
        sum += fx
        area = sum / count
        error.append([abs(area - analyticalResult), count])
        count += 1
    return area, error

def precisionCheck(area, precision):
    return (precision < abs(area - analyticalResult))


if __name__ == "__main__":
    area, errorConvergence = mcInt()
    print(area)
    print(analyticalResult)
    transposed = [[errorConvergence[j][i] for j in range(len(errorConvergence))] for i in range(len(errorConvergence[0]))]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.plot(transposed[1][10:-1], transposed[0][10:-1], "-")
    ax.axhline()
    fig.savefig("outputP2.png")