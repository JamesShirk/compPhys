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

def main():
    values = arange(-5, 5, .1)
    x = [function(i) for i in values]
    freq = fftfreq(values.shape[-1])
    output = fft(x)
    magnitude = [sqrt(output.real[i]**2 + output.imag[i]**2) for i in range(0, len(output))]
    plt.plot(freq, magnitude, 'o')
    plt.xlim(-.6, .6)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude of Fourier Transform Function')
    plt.title('Fourier Transform')
    plt.savefig('magnitudeFFT.png')
    plt.close()

def timeShifting():
    values = arange(-6, 4, .1)
    x = [function(i) for i in values]
    freq = fftfreq(values.shape[-1])
    output = fft(x)
    magnitude = [sqrt(output.real[i]**2 + output.imag[i]**2) for i in range(0, len(output))]
    plt.plot(freq, magnitude, 'o')
    plt.xlim(-.6, .6)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude of Fourier Transform Function')
    plt.title('Time Scaled Fourier Transform')
    plt.savefig('timeShiftedFT.png')
    plt.close()

def functionPlot():
    values = arange(-5, 5, .1)
    x = [function(i) for i in values]
    plt.plot(values, x, "-")
    plt.xlim(-6, 6)
    plt.xlabel('Time')
    plt.ylabel('f(t)')
    plt.title('Starting Function')
    plt.savefig('function.png')
    plt.close()

if __name__ == "__main__":
    main()
    timeShifting()
    functionPlot()


