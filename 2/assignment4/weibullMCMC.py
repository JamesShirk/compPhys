from numpy.random import random_sample
from math import exp
import matplotlib.pyplot as plt

def weibull(x, n = 1, a = 2):
    #result = (k/l) * ((x / l) ** (k - 1))
    #result *= exp(-((x/l)**k))
    return (a / n) * (x / n)**(a - 1) * exp(-(x / n)**a)

def mhmc(n, x0 = 1):
    output, k = [], 0
    while(k < n):
        # Appends data to an output for returning
        output.append(x0)
        # Takes the two random samples needed
        u1, u2 = random_sample(), random_sample()
        # Determines y based on the value of u1
        y = (x0 + .01) if (u1 > .5) else (x0 - .01)
        # Computes r = p(y) / p(x0) where p is a weibull distribution
        r = weibull(y) / weibull(x0)
        # Determines the next value of x0
        x0 = y if (u2 <= r) else x0
        k += 1
    return output

if __name__ == "__main__":
    nRuns = 100000
    x = range(nRuns)
    y = mhmc(nRuns, 5)
    plt.plot(x, y, "-")
    plt.ylabel("x")
    plt.xlabel("t")
    plt.title("Random Process Sampled Using MCMC pulled from a Weibull Distribution")
    plt.savefig("output.png")
    plt.close()
    # x = range(10)
    # y = [weibull(i) for i in x]
    # print(y)