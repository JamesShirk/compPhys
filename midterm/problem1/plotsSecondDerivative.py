from math import pi, sin, exp, cos
from numpy import linspace
import matplotlib.pyplot as plt

def function(x):
    return ((sin(30*pi*x)+(.6*sin(70*pi*x)))*(exp(-1*(x**2)) / x))

def derivative(x):
    numerator = -1*((exp(-(x**2))) * (((6*(x**2) + 3)*sin(70*pi*x)) - (210*pi*x*cos(70*pi*x) + ((10*(x**2) + 5)*sin(30*pi*x)) - ((150*pi*x) * cos(30*pi*x)))))
    return (numerator / (5*(x**2)))

# Defo messed up in here somewhere
def secondDerivative(x):
    numerator = (exp(-(x**2)) * ((((12*(x**4)) + ((6 - 14700*(pi**2))*(x**2)) + 6) * sin(70*pi*x)) + ((-840 * pi *(x**3) - 420*pi*x)*cos(70*pi*x))+((20*(x**4)+((10 - (4500*pi*2))*(x**2))+10)*sin(30*pi*x)) + (((-600*pi*(x**3) - 300*pi*x)*cos(30*pi*x)))))
    return (numerator / (5*(x**3)))

def secondDerivativePlot(nPoints):
    # X cannot be 0 with this sampling
    x = linspace(-3, 3, nPoints)
    y = [secondDerivative(i) for i in x]
    plt.plot(x, y, "--")
    axes = plt.gca()
    axes.set_ylim([-5000, 5000])
    plt.xlabel("x")
    plt.ylabel("$\\frac{d^2}{dx^2}f(x)$")
    plt.title("Plot of the Second Derivative with" + str(nPoints) + " Samples")
    plt.savefig("secondDerivative" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()

def forwardEuler(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [derivative(i) for i in x]
    dx = []

    for i in range(0, (nPoints) - 1):
        j = i + 1
        # performs the forward euler method. 
        # x[j] - x[i] is a constant but left in to generalize
        dx.append((y[j] - y[i]) / (x[j] - x[i]))

    plt.plot(x[0:(nPoints - 1)], dx, "--")
    plt.xlabel("x")
    plt.ylabel("$\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    axes.set_ylim([-1200, 1200])
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Forward Euler Derivative with " + str(nPoints) + " Samples")
    plt.savefig("secondDerivativeForward" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()

def backwardEuler(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [derivative(i) for i in x]
    dx = []

    for i in range(1, (nPoints)):
        j = i - 1
        # performs the forward euler method. 
        # x[j] - x[i] is a constant but left in to generalize
        dx.append((y[i] - y[j]) / (x[i] - x[j]))

    plt.plot(x[1:(nPoints)], dx, "--")
    plt.xlabel("x")
    plt.ylabel("$\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    axes.set_ylim([-1200, 1200])
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Backward Euler Derivative with " + str(nPoints) + " Samples")
    plt.savefig("secondDerivativeBackward" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()

def centralDifference(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [derivative(i) for i in x]
    dx = []

    for i in range(1, (nPoints) - 1):
        j = i - 1
        k = i + 1
        # performs the forward euler method. 
        # x[j] - x[i] is a constant but left in to generalize
        dx.append((y[k] - y[j]) / (x[k] - x[j]))

    plt.plot(x[1:(nPoints) - 1], dx, "--")
    plt.xlabel("x")
    plt.ylabel("$\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    axes.set_ylim([-1200, 1200])
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Backward Euler Derivative with " + str(nPoints) + " Samples")
    plt.savefig("secondDerivativeCentral" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()

if __name__ == "__main__":
    secondDerivativePlot(400)
    # forwardEuler(400)
    # backwardEuler(400)
    # centralDifference(400)