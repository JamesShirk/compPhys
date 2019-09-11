import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
import math


def dataInterpolation():
    data = pd.read_csv("data.txt")
    x = data.loc[: ,"Voltage"]
    y = data.loc[: ,"Current"]
    f = interpolate.interp1d(x, y, kind = "cubic")
    xnew = np.linspace(-1.5, 0, endpoint = True)
    plt.plot(x, y, "o", xnew, f(xnew), "-")
    plt.legend(["data", "cubic spline"], loc="best")
    plt.savefig("data.png", dpi = 1000)

def dataInterpolationExtended():
    data = pd.read_csv("dataExtended.txt")
    x = data.loc[: ,"Voltage"]
    y = data.loc[: ,"Current"]
    f = interpolate.interp1d(x, y, kind = "cubic")
    xnew = np.linspace(-1.5, 4.5, endpoint = True)
    plt.plot(x, y, "o", xnew, f(xnew), "-")
    plt.legend(["data", "cubic spline"], loc="best")
    plt.savefig("dataExtended.png", dpi = 1000)


if __name__ == "__main__":
    dataInterpolation()
    dataInterpolationExtended()

    