from math import sqrt, exp, pi
import matplotlib.pyplot as plt
from numpy import arange, fft, linspace
import pywt
import scipy

def function(x, a):
    return ((2/((pi ** .25)*sqrt(3*a)))*(1 - (x**2/a**2))*exp((-x**2)/(2*(a**2))))

def main():
    x = arange(-5, 5, .1)
    yFamily = [function(i, 1) for i in x]
    y = [function(i, .5) for i in x]

    coef, freqs = pywt.cwt(y, 2,'mexh')
    coef2, freqs2 = pywt.cwt(y, 10,'morl')

    freq = fft.fftfreq(x.shape[-1])
    coefSum = [sum(i) for i in zip(*coef)]
    coef2Sum = [sum (i) for i in zip(*coef2)]

    #plt.plot(x, y, "--", x, coef[0], "--", x, coef[1], "--",x, coef[2], "--",x, coef[3], "--",coef[3], "--",coef[4], "--",coef[5], "--",coef[6], "--")
    plt.plot(x, y, "--", x, coefSum, "--", x, coef2Sum, "--")
    plt.xlabel("time")
    plt.ylabel("psi(t)")
    plt.title("Mexican Hat order and Function")
    #plt.legend(["Original", "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"], loc="best")
    plt.legend(["psi(t)", "Mexican Hat 2 Freqs", "Morlet 10 Freqs"], loc = "best")
    plt.savefig("allFunctions.png", dpi = 300)
    plt.close()

if __name__ == "__main__":
    main()