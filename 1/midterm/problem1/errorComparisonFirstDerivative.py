from math import pi, sin, exp, cos, sqrt
from numpy import linspace
import matplotlib.pyplot as plt

# James Shirk October 29 for Comp Phys Midterm Problem 1 
import numpy as np
from numpy import sin, pi, exp, cos, linspace, arange, real
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt
import itertools


def function(x):
    return ((sin(30*pi*x)+(.6*sin(70*pi*x)))*(exp(-1*(x**2)) / x))

def derivative(x):
    numerator = -1*((exp(-(x**2))) * (((6*(x**2) + 3)*sin(70*pi*x)) - (210*pi*x*cos(70*pi*x) + ((10*(x**2) + 5)*sin(30*pi*x)) - ((150*pi*x) * cos(30*pi*x)))))
    return (numerator / (5*(x**2)))

def errorComparison(nPoints):
    x = linspace(-3, 3, nPoints)
    y = [function(i) for i in x]

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
        dx = (y[j] - y[i]) / (x[j] - x[i]) - derivative(x[i])
        dxForwardErr.append(dx)
        dxForwardPerErr.append((dx - derivative(x[i])) / derivative(x[i]))
    # Backward
    for i in range(1, (nPoints)):
        j = i - 1
        dx = (y[i] - y[j]) / (x[i] - x[j]) - derivative(x[i])
        dxBackwardErr.append(dx)
        dxBackwardPerErr.append((dx - derivative(x[i])) / derivative(x[i]))
    # Central
    for i in range(1, (nPoints) - 1):
        j = i - 1
        k = i + 1
        dx = (y[k] - y[j]) / (x[k] - x[j]) - derivative(x[i])
        dxCentralErr.append(dx)
        dxCentralPerErr.append((dx - derivative(x[i])) / derivative(x[i]))
    
    # Plot of the absolute errors
    plt.plot(x, dxAnalyticalErr, "-", x[0:(nPoints - 1)], dxForwardErr, "--", x[1:(nPoints)], dxBackwardErr, "--", x[1:(nPoints) - 1], dxCentralErr, "--")
    plt.xlabel("x")
    plt.ylabel("Absolute error from $\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Absolute Errors of Methods with " + str(nPoints) + " Samples")
    plt.legend(["Analytical", "Forward", "Backward", "Central"], loc="best")
    plt.savefig("derivativeAbsError" + str(nPoints) + ".png", dpi = 300)
    plt.close()

    
    


    t = linspace(-3, 3, nPoints)
    y = [function(i) for i in t]
    transform = fft(y)
    dx = [derivative(i) for i in t]

    # Mkaes a new array and multiplies by i of the original data
    spectralMethod = 1j*np.zeros(nPoints)
    spectralMethod[0:nPoints//2] = 1j*arange(0, nPoints//2, 1)
    spectralMethod[nPoints//2+1:] = 1j*arange(-nPoints//2 + 1, 0, 1)
    spectralMethod = spectralMethod*transform
    inverse = real(ifft(spectralMethod))

    plt.plot(t, inverse, '--', t, dx, "--")
    plt.xlabel('Time')
    plt.ylabel('f(t)')
    plt.title('Derivative Calculated Through Spectral Methods')
    plt.savefig('specDer.png', dpi = 300)
    plt.close()

    perError = []

    for i, k in zip(inverse, dx):
        perError.append(((i-k)/k + 1.5))

    plt.plot(t, perError, "--")
    plt.xlabel("x")
    plt.ylabel("Percent Error from $\\frac{d}{dx}f(x)$")
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Percent Errors from Spectral Method")
    plt.savefig("specPerError" + str(nPoints) + ".png", dpi = 300)
    plt.close()




# Plot the percent errors
    plt.plot(x, dxAnalyticalErr, "-", x[0:(nPoints - 1)], dxForwardPerErr, "--", x[1:(nPoints)], dxBackwardPerErr, "--", x[1:(nPoints) - 1], dxCentralPerErr, "--", t, perError, "--")
    plt.xlabel("x")
    plt.ylabel("Percent Error from $\\frac{d}{dx}f(x)$")
    axes = plt.gca()
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Percent Errors of Methods with " + str(nPoints) + " Samples")
    plt.legend(["Analytical", "Forward", "Backward", "Central", "Spectral"], loc="best")
    plt.savefig("derivativePerError" + str(nPoints) + ".png", dpi = 300)
    plt.close()

if __name__ == "__main__":
    errorComparison(400)