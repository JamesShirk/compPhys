from math import pi, sin, exp, cos
from numpy import linspace
import matplotlib.pyplot as plt

def function(x):
    return ((sin(30*pi*x)+(.6*sin(70*pi*x)))*(exp(-1*(x**2)) / x))

def derivative(x):
    numerator = -1*((exp(-(x**2))) * (((6*(x**2) + 3)*sin(70*pi*x)) - (210*pi*x*cos(70*pi*x) + ((10*(x**2) + 5)*sin(30*pi*x)) - ((150*pi*x) * cos(30*pi*x)))))
    return (numerator / (5*(x**2)))

def functionPlot(nPoints):
    # X cannot be 0 with this sampling
    x = linspace(-3, 3, nPoints)
    y = [function(i) for i in x]
    plt.plot(x, y, "--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Plot of the Function with 200 Samples")
    plt.savefig("function" + str(nPoints) + ".png", dpi = 300)
    plt.close()

def derivativePlot(nPoints):
    # X cannot be 0 with this sampling
    x = linspace(-3, 3, nPoints)
    y = [derivative(i) for i in x]
    plt.plot(x, y, "--")
    plt.xlabel("x")
    plt.ylabel("$\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    axes.set_ylim([-1200, 1200])
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Analytical Derivative with " + str(nPoints) + " Samples")
    plt.savefig("derivative" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()

def forwardEuler(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [function(i) for i in x]
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
    plt.savefig("derivativeForward" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()

def backwardEuler(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [function(i) for i in x]
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
    plt.savefig("derivativeBackward" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()

def centralDifference(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [function(i) for i in x]
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
    plt.savefig("derivativeCentral" + str(nPoints) + "_1200.png", dpi = 300)
    plt.close()


if __name__ == "__main__":
    functionPlot(200)
    derivativePlot(200)
    forwardEuler(200)
    backwardEuler(200)
    centralDifference(200)