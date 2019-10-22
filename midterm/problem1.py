from math import pi, sin, exp, cos
from numpy import linspace
import matplotlib.pyplot as plt

def function(x):
    return ((sin(30*pi*x)+(.6*sin(70*pi*x)))*(exp(-1*(x**2)) / x))

def derivative(x):
    firstTerm = ((-2*exp(-1 * (x**2))) - ((1/(x**2))*exp(-1*(x**2))*(sin(30*pi*x)+.6*sin(70*pi*x))))
    secondTerm = 6*pi*(exp(-1* (x**2))*(1/x))*(5*cos(30*pi*x)+7*cos(70*pi*x))
    return (firstTerm + secondTerm)

def functionPlot():
    # X cannot be 0 with this sampling
    x = linspace(-3, 3, 200)
    y = [function(i) for i in x]
    plt.plot(x, y, "--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    # axes = plt.gca()
    # axes.set_ylim([-10, 10])
    plt.title("Plot of the Function with 200 Samples")
    plt.savefig("function200.png", dpi = 300)
    plt.close()

def derivativePlot():
    # X cannot be 0 with this sampling
    x = linspace(-3, 3, 200)
    y = [derivative(i) for i in x]
    plt.plot(x, y, "--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    axes = plt.gca()
    axes.set_ylim([-800, 800])
    plt.title("Plot of the Function with 800 Samples")
    plt.savefig("derivative200_800.png", dpi = 300)
    plt.close()

if __name__ == "__main__":
    functionPlot()
    derivativePlot()