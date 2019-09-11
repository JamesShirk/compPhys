import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
import math

def sinInterpolation(nPoints):
    x = np.linspace(0, 2*math.pi, nPoints, endpoint = True)
    y = [math.sin(i) for i in x]
    f = interpolate.interp1d(x, y, kind = "cubic")
    xnew = np.linspace(0, 2*math.pi, endpoint = True)
    plt.plot(x, y, "o", xnew, f(xnew), "-")
    plt.legend(["sin", "cubic interpolation"], loc="best")
    plt.savefig("sinInterpolation.png", dpi = 1000)

 if __name__ == "__main__":
    sinInterpolation(int(input("How many data points for sin interpolation (min is 4): ")))