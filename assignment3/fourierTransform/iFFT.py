from numpy.fft import ifft
from numpy import arange
from math import sin
import matplotlib.pyplot as plt

def function(x):
    if (x == 0):
        return 1
    else:
        return (sin(x)/x)

def main():
    values = arange(-10, 10, .1)
    x = [function(i) for i in values]
    output = ifft(x)
    plt.plot(values, output.real, 'b-', values, output.imag, 'r--')
    plt.legend(('real', 'imaginary'))
    plt.savefig('iFFT.png')



if __name__ == "__main__":
    main()