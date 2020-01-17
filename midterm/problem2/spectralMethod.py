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

# Calculates the spectral method and mkaes plots
def spectralMethod(nPoints):
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
    plt.gcf().subplots_adjust(left=0.15)
    plt.legend(["Spectral Method", "Analytical"], loc = "best")
    plt.savefig('specDer.png', dpi = 300)
    plt.close()

    perError = []

    for i, k in zip(inverse, dx):
        perError.append(((i-k)/k * 100))

    plt.plot(t, perError, "--")
    plt.xlabel("x")
    plt.ylabel("Percent Error from $\\frac{d}{dx}f(x)$")
    plt.gcf().subplots_adjust(left=0.15)
    plt.title("Plot of the Percent Errors from Spectral Method")
    plt.savefig("specPerError" + str(nPoints) + ".png", dpi = 300)
    plt.close()

if __name__ == "__main__":
    spectralMethod(400)