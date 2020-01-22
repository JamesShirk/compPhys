from numpy.fft import fft, fftfreq
from numpy import arange, delete
from math import sin, sqrt
import matplotlib.pyplot as plt
import pylab

def function(x):
    if(x >= 0 and x < .5):
        return 1
    elif(x >= .5 and x < 1):
        return -1
    else:
        return 0

def timeShiftingFirst():
    values = arange(-6, 4, .1)
    freq = fftfreq(values.shape[-1])
    x = [function(i) for i in values]
    output = fft(x)
    magnitude = [sqrt(output.real[i]**2 + output.imag[i]**2) for i in range(0, len(output))]
    plt.plot(freq, magnitude, 'o')
    plt.xlim(-.6, .6)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude of Fourier Transform Function')
    plt.title('Time Shifted Fourier Transform')
    plt.savefig('timeShiftedFT.png')
    plt.close()

def timeShiftingAfter():
    values = arange(-5, 5, .1)
    freq = fftfreq(values.shape[-1])
    x = [function(i) for i in values]
    output = fft(x)
    magnitude = [sqrt(output.real[i]**2 + output.imag[i]**2) for i in range(0, len(output))]
    plt.plot(freq, magnitude, 'o')
    plt.xlim(-.6, .6)

    values2 = arange(-5, 5, .1)
    x2 = [function(i) for i in values2]
    freq2 = fftfreq(values2.shape[-1])
    output2 = fft(x2)
    magnitude2 = [sqrt(output2.real[i]**2 + output2.imag[i]**2) for i in range(0, len(output2))]
    plt.plot(freq, magnitude, '^', freq2, magnitude2, 'v')
    plt.legend(["Shifted", "Unshifted"])
    plt.xlim(-.6, .6)

    plt.xlabel('Frequency')
    plt.ylabel('Magnitude of Fourier Transform Function')
    plt.title('Time Shifted Fourier Transform')
    plt.savefig('both.png')
    plt.close()

def functionPlot():
    values = arange(-6, 4, .1)
    x = [function(i) for i in values]
    plt.plot(values, x, "-")
    plt.xlim(-6, 6)
    plt.xlabel('Time')
    plt.ylabel('f(t)')
    plt.title('Starting Function')
    plt.savefig('functionShifted.png')
    plt.close()

if __name__ == "__main__":
    timeShiftingAfter()