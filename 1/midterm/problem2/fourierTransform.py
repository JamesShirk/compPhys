# James Shirk October 29 for Comp Phys Midterm Problem 1 
from numpy.fft import fft, fftfreq, ifft, irfft
from numpy import linspace
import numpy as np
from math import pi, sin, exp, cos, sqrt      
import matplotlib.pyplot as plt
import itertools

def function(x):
    return ((sin(30*pi*x)+(.6*sin(70*pi*x)))*(exp(-1*(x**2)) / x))

# Analytical Derivative of given function
def derivative(x):
    numerator = -1*((exp(-(x**2))) * (((6*(x**2) + 3)*sin(70*pi*x)) - (210*pi*x*cos(70*pi*x) + ((10*(x**2) + 5)*sin(30*pi*x)) - ((150*pi*x) * cos(30*pi*x)))))
    return (numerator / (5*(x**2)))

def fourierTransform(nPoints):
    t = linspace(-3, 3, nPoints)
    y = [function(i) for i in t]

    freq = fftfreq(t.shape[-1])
    transform = fft(y)
    magnitude = [sqrt(transform.real[i]**2 + transform.imag[i]**2) for i in range(0, len(transform))]

    freqNew = orderFreq(nPoints, magnitude, freq)[1]
    magnitudeNew = orderFreq(nPoints, magnitude, freq)[0]

    # Plot of real/imag components
    plt.plot(freq, transform.real, '--', freq, transform.imag, "--")
    plt.legend(["Real", "Imaginary"], loc = "best")
    plt.xlabel('Frequency')
    plt.ylabel('FT(f)')
    plt.title('Fourier Transform of Function')
    plt.savefig('fourierTransformRealImag.png', dpi = 300)
    plt.close()

    # Plot of magnitude
    plt.plot(freqNew, magnitudeNew, '--')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.title('Fourier Transform of Function')
    plt.savefig('fourierTransformMagnitude.png', dpi = 300)
    plt.close()
    
# Upon conversion from time to frequency, the positive frequencies come before the negative frequencies
# This converts between the two
def orderFreq(nPoints, magnitude, freq):
    endMag = magnitude[0:(nPoints // 2)]
    startMag = magnitude[(nPoints // 2):nPoints]
    endFreq = freq[0:(nPoints // 2)]
    startFreq = freq[(nPoints // 2):nPoints]
    outFreq = []
    outMag = []
    outFreq.extend(startFreq)
    outFreq.extend(endFreq)
    outMag = (startMag + endMag)
    return (outMag, outFreq)


if __name__ == "__main__":
    fourierTransform(400)