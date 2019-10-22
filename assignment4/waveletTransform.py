# James Shirk October 10 2019, wavelet transform

from math import sqrt, exp, pi
import matplotlib.pyplot as plt
from numpy import arange, fft, linspace
import pywt         #package fro computing wavelet transforms
import scipy

# Creates a function of x and a of the given function
def function(x, a):
    return ((2/((pi ** .25)*sqrt(3*a)))*(1 - (x**2/a**2))*exp((-x**2)/(2*(a**2))))

def main():

    x = arange(-5, 5, .1)
    yFamily = [function(i, 1) for i in x]
    y = [function(i, .5) for i in x]

    # Main code that performs the cwt, requires a scales, put a list from 1 to 128. 'mexh' is mexicna hat
    coef, freqs = pywt.cwt(y, arange(1,129),'mexh')

    # Computes normalized frequency from time (x)
    freq = fft.fftfreq(x.shape[-1])

    # sums the coefficients of the cwt 
    coefSum = [sum(i) for i in zip(*coef)]

    # plots the sums of the coefficients as a function of the frequency
    plt.plot(freq, coefSum, "o")
    plt.xlabel("frequency")
    plt.ylabel("Sum of Coefficients")
    plt.title("Mexican Hat Wavelet Transform")
    plt.savefig("wavelettransformMexh.png", dpi = 300)
    plt.close()


    # plt.plot(x, y, "-", x, yFamily, "--")
    # plt.xlabel("time")
    # plt.ylabel("\psi(t)")
    # plt.title("Mexican Hat Mother Wavelets")
    # plt.savefig("function.png", dpi = 300)
    # plt.close()

    # Matrix visualizer
    plt.imshow(coef, origin='lower', aspect='auto', extent=[x[0], x[-1], freqs[0], freqs[-1]])
    plt.xlabel("t")
    plt.ylabel("f")
    plt.title("Coefficient matrix visualization")
    plt.savefig("CoefMatrixMexh.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    main()
