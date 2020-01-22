# James Shirk for computational physics class September 28-30
# computes FT 

from numpy.fft import fft, fftfreq   # For computing Fourier transform
from numpy import arange             # for making lists of equally spaced numbers
from math import sin, sqrt           # for sin and sqrt
import matplotlib.pyplot as plt      # for plotting
from time import time                # Time differences

# Haar function
def function(x):
    if(x >= 0 and x < .5):
        return 1
    elif(x >= .5 and x < 1):
        return -1
    else:
        return 0

# Main fourier transform
def fourierTransform():
    # When computing the time shifting, I changed values = arange(-5, 5, .1) to -6, 4, .1
    values = arange(-5, 5, .1)
    # Computes the value of the function for each element in values
    x = [function(i) for i in values]
    # Computes the frequency using the original values as the time
    freq = fftfreq(values.shape[-1])
    # Function that computes the fourier transform
    output = fft(x)
    # Takes the magnitude
    magnitude = [sqrt(output.real[i]**2 + output.imag[i]**2) for i in range(0, len(output))]
    # Plots
    plt.plot(freq, magnitude, 'o')
    plt.xlim(-.6, .6)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude of Fourier Transform Function')
    plt.title('Fourier Transform')
    plt.savefig('magnitudeFFT.png')
    plt.close()

def functionPlot():
    #Plots the function over the same range
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
    timeTotal = 0
    # Takes the time over 1000 runs
    for x in range(0, 1000):
        t1 = time()
        fourierTransform()
        t2 = time()
        timeTotal += (t2 - t1)
    # Is in milliseconds by default since it's in seconds and i'd divide by 1000 as thats the number of runs and then multiply by 1000 to get ms but they cancel out
    print("The program took " + str(timeTotal) + " milliseconds.")

