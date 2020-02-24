from math import cos, pi
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return (x * (cos(pi * x ) ** 2))

def trapezoidal(x, f):
    result = 0
    for i in range(len(x) - 1):
        dx = abs(x[i] - x[i+1])
        df = abs(f[i+1] - f[i])
        # Triangle part of the trapezoid
        result +=  df * dx * .5
        # Square part of the trapezoid
        result += f[i] * dx if f[i] <= f[i] else f[i + 1] * dx

    return result

if __name__ == "__main__":
    x = np.arange(0, 1, .00002)
    y = [function(i) for i in x]
    print(trapezoidal(x,y))

    convergence = []

    # Runs for a large number of points from 1000 to 100000
    for i in range(1,100):
        data = []
        dx = 1 / (i * 1000)
        samplePoints = 1/dx
        x = np.arange(0, 1, dx)
        y = [function(i) for i in x]
        data.append(samplePoints)
        data.append(abs(trapezoidal(x, y) - .25))
        convergence.append(data)

    # Plotting
    transposed = [[convergence[j][i] for j in range(len(convergence))] for i in range(len(convergence[0]))]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_yscale('log')
    ax.set_ylabel("Absolute Error")
    ax.set_xlabel("Number of X points")
    ax.set_title("Semilog of Absolute Error over Number of Samples")
    ax.plot(transposed[0], transposed[1], "-")
    ax.axhline()
    fig.savefig("outputp1num.png")