from math import sqrt, exp, pi
import matplotlib.pyplot as plt
from numpy import arange
import pywt
import scipy

def function(x, a):
    return ((2/((pi ** .25)*sqrt(3*a)))*(1 - (x**2/a**2))*exp((-x**2)/(2*(a**2))))

def main():
    x = arange(-5, 5, .1)
    yFamily = [function(i, 1) for i in x]
    y = [function(i, .5) for i in x]

    coef, freqs = pywt.cwt(y, 1,'mexh')

    print(len(coef[0]))

    plt.matshow(coef)
    plt.savefig("test.png", dpi = 300)
    plt.close()

    plt.plot(x, coef[0], "-")
    plt.savefig("wavelettransform.png", dpi = 300)
    plt.close()

    plt.plot(x, y, "--")
    plt.axhline(y=0, color='black', linestyle='-')
    plt.savefig("function.png", dpi = 300)
    plt.close()

    plt.plot(x, yFamily, "--")
    plt.axhline(y=0, color='black', linestyle='-')
    plt.savefig("mexicanHat.png", dpi = 300)
    plt.close()

if __name__ == "__main__":
    main()