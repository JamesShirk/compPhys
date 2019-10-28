from numpy.fft import fft, fftfreq, ifft
from numpy import linspace
from math import pi, sin, exp, cos, sqrt      
import matplotlib.pyplot as plt

def function(x):
    return ((sin(30*pi*x)+(.6*sin(70*pi*x)))*(exp(-1*(x**2)) / x))

def fourierTransform(nPoints):
    t = linspace(-3, 3, nPoints)
    y = [function(i) for i in t]

    freq = fftfreq(t.shape[-1])
    transform = fft(y)
    magnitude = [sqrt(transform.real[i]**2 + transform.imag[i]**2) for i in range(0, len(transform))]

    freqNew = orderFreq(nPoints, magnitude, freq)[1]
    magnitudeNew = orderFreq(nPoints, magnitude, freq)[0]

    plt.plot(freq, transform.real, '--', freq, transform.imag, "--")
    plt.legend(["Real", "Imaginary"], loc = "best")
    plt.xlabel('Frequency')
    plt.ylabel('FT(f)')
    plt.title('Fourier Transform of Function')
    plt.savefig('fourierTransformRealImag.png', dpi = 300)
    plt.close()

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
    return outMag, outFreq;

def spectralMethod(nPoints):
    t = linspace(-3, 3, nPoints)
    y = [function(i) for i in t]

    freq = fftfreq(t.shape[-1])
    transform = fft(y)
    magnitude = [sqrt(transform.real[i]**2 + transform.imag[i]**2) for i in range(0, len(transform))]

    freqNew = orderFreq(nPoints, magnitude, freq)[1]
    magnitudeNew = orderFreq(nPoints, magnitude, freq)[0]

    dx = []
    # Central Euler
    for i in range(1, (nPoints) - 1):
        j = i - 1
        k = i + 1
        # performs the forward euler method. 
        # x[j] - x[i] is a constant but left in to generalize
        dx.append((magnitudeNew[k] - magnitudeNew[j]) / (freqNew[k] - freqNew[j]))

    plt.plot(freqNew[1:(nPoints) - 1], dx, '--')
    plt.xlabel('Frequency')
    plt.ylabel('"$\\frac{d}{dx}FT(f)$"')
    plt.title('Fourier Transform of Function')
    plt.savefig('derivativeFT.png', dpi = 300)
    plt.close()

    # IFFT module requires the points to be the old order
    dxStart = dx[(nPoints // 2): nPoints]
    dxEnd = dx[0:(nPoints // 2)]
    outDx = dxStart + dxEnd
    outDx.insert(0, 0)
    outDx.append(0)

    derivative = ifft(outDx)
    magnitudeDerivative = [sqrt(derivative.real[i]**2 + derivative.imag[i]**2) for i in range(0, len(derivative))]

    #plt.plot(freq, derivative.real, '--', freq, derivative.imag, "--")
    plt.plot(freq, derivative.real, "--")
    plt.legend(["Real", "Imaginary"], loc = "best")
    plt.xlabel('time')
    plt.ylabel('"$\\frac{d}{dx}f(t)$"')
    plt.title('IFT of FT derivative')
    plt.savefig('derivativeIFT.png', dpi = 300)
    plt.close()


if __name__ == "__main__":
    fourierTransform(400)
    #spectralMethod(1, [1, 2, 3])
    spectralMethod(400)