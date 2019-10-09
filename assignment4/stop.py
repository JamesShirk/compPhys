from math import sqrt, exp, pi
import matplotlib.pyplot as plt
from numpy import arange, fft, linspace
import pywt
import scipy
from astroML.fourier import\
    FT_continuous, IFT_continuous, sinegauss, sinegauss_FT, wavelet_PSD

def function(x, a):
    return ((2/((pi ** .25)*sqrt(3*a)))*(1 - (x**2/a**2))*exp((-x**2)/(2*(a**2))))


def main():
    x = arange(-5, 5, .01)
    #yFamily = [function(i, 1) for i in x]
    y = [function(i, .5) for i in x]
    freq = fft.fftfreq(x.shape[-1])

    W = sinegauss(x, 0, 1.5, Q=1.0)
    f0 = linspace(0.5, 7.5, 100)
    wPSD = wavelet_PSD(x, y, f0, Q=1.0)

    fig = plt.figure(figsize=(5, 5))
    fig.subplots_adjust(hspace=0.05, left=0.12, right=0.95, bottom=0.08, top=0.95)

    # First Panel

    ax = fig.add_subplot(311)
    ax.plot(x, y, '-k', lw=1)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-2.9, 2.9)
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.set_ylabel('$\psi(t)$')

    ax = fig.add_subplot(312)
    ax.plot(x, W.real, '-k', label='real part', lw=1)
    ax.plot(x, W.imag, '--k', label='imag part', lw=1)


    ax.text(0.02, 0.95, ("Example Wavelet\n"
                     "$t_0 = 0$, $f_0=1.5$, $Q=1.0$"),
        ha='left', va='top', transform=ax.transAxes)
    
    ax.legend(loc=1)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_ylabel('Example Wavelet')
    ax.xaxis.set_major_formatter(plt.NullFormatter())

    ax = plt.subplot(313)
    ax.imshow(wPSD, origin='lower', aspect='auto',
          extent=[x[0], x[-1], f0[0], f0[-1]])

    ax.text(0.02, 0.95, ("Wavelet PSD"), color='w',
        ha='left', va='top', transform=ax.transAxes)

    ax.set_xlim(-4, 4)
    ax.set_ylim(0.5, 7.5)

    ax.set_xlabel('$t$')
    ax.set_ylabel('$f_0$')

    plt.savefig("Test.png", dpi=300)

if __name__ == "__main__":
    main()