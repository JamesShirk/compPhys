from math import pi, sin, exp, cos
from numpy import linspace
import matplotlib.pyplot as plt

def function(x):
    return ((sin(30*pi*x)+(.6*sin(70*pi*x)))*(exp(-1*(x**2)) / x))

def derivative(x):
    numerator = -1*((exp(-(x**2))) * (((6*(x**2) + 3)*sin(70*pi*x)) - (210*pi*x*cos(70*pi*x) + ((10*(x**2) + 5)*sin(30*pi*x)) - ((150*pi*x) * cos(30*pi*x)))))
    return (numerator / (5*(x**2)))

def secondDerivative(x):
    numerator = (exp(-(x**2)) * ((((12*(x**4)) + ((6 - 14700*(pi**2))*(x**2)) + 6) * sin(70*pi*x)) + ((-840 * pi *(x**3) - 420*pi*x)*cos(70*pi*x))+((20*(x**4)+((10 - (4500*pi*2))*(x**2))+10)*sin(30*pi*x)) + (((-600*pi*(x**3) - 300*pi*x)*cos(30*pi*x)))))
    return (numerator / (5*(x**3)))

def errorComparison(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [derivative(i) for i in x]

    dxAnalyticalErr = [0 for i in x]
    dxForwardErr = []
    dxBackwardErr = []
    dxCentralErr = []

    dxAnalyticalPerErr = [0 for i in x]
    dxForwardPerErr = []
    dxBackwardPerErr = []
    dxCentralPerErr = []

    # Forward
    for i in range(0, (nPoints) - 1):
        j = i + 1
        dx = (y[j] - y[i]) / (x[j] - x[i]) - secondDerivative(x[i])
        dxForwardErr.append(dx)
        dxForwardPerErr.append((dx - secondDerivative(x[i])) / secondDerivative(x[i]))
    # Backward
    for i in range(1, (nPoints)):
        j = i - 1
        dx = (y[i] - y[j]) / (x[i] - x[j]) - secondDerivative(x[i])
        dxBackwardErr.append(dx)
        dxBackwardPerErr.append((dx - secondDerivative(x[i])) / secondDerivative(x[i]))
    # Central
    for i in range(1, (nPoints) - 1):
        j = i - 1
        k = i + 1
        dx = (y[k] - y[j]) / (x[k] - x[j]) - secondDerivative(x[i])
        dxCentralErr.append(dx)
        dxCentralPerErr.append((dx - secondDerivative(x[i])) / secondDerivative(x[i]))
    
    # Plot of the absolute errors
    plt.plot(x, dxAnalyticalErr, "-", x[0:(nPoints - 1)], dxForwardErr, "--", x[1:(nPoints)], dxBackwardErr, "--", x[1:(nPoints) - 1], dxCentralErr, "--")
    plt.xlabel("x")
    plt.ylabel("Absolute error from $\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    plt.gcf().subplots_adjust(left=0.2)
    plt.title("Plot of the Absolute Errors of Methods with " + str(nPoints) + " Samples")
    plt.legend(["Analytical", "Forward", "Backward", "Central"], loc="best")
    plt.savefig("SecondDerivativeAbsError" + str(nPoints) + ".png", dpi = 300)
    plt.close()

    # Plot the percent errors
    plt.plot(x, dxAnalyticalErr, "-", x[0:(nPoints - 1)], dxForwardPerErr, "--", x[1:(nPoints)], dxBackwardPerErr, "--", x[1:(nPoints) - 1], dxCentralPerErr, "--")
    plt.xlabel("x")
    plt.ylabel("Percent Error from $\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Percent Errors of Methods with " + str(nPoints) + " Samples")
    plt.legend(["Analytical", "Forward", "Backward", "Central"], loc="best")
    plt.savefig("SecondDerivativePerError" + str(nPoints) + ".png", dpi = 300)
    plt.close()
    

if __name__ == "__main__":
    errorComparison(400)