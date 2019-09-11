import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
from statistics import mean 

def Interpolation():
    types = ["lin","quad", "cub"]
    data = pd.read_csv("data.txt")
    dataExtended = pd.read_csv("dataextended.txt")
    flin = interpolate.interp1d(data["x"], data["y"], kind = "linear")
    fquad = interpolate.interp1d(data["x"], data["y"], kind = "quadratic")
    fcub = interpolate.interp1d(data["x"], data["y"], kind = "cubic")
    xnew = np.linspace(-4, 5, endpoint = True)
    plt.plot(data["x"], data["y"], "o", xnew, flin(xnew), "-", xnew, fquad(xnew), "-.", xnew, fcub(xnew), "--")
    plt.legend(["data", "linear", "quadratic", "cubic spline"], loc="best")
    plt.savefig("noteInterpolation.png", dpi = 1000)
    plt.close()
    # -----------------------------------------------------------------------------
    # Plots to calculater error
    # List comprehensions are used on a more robust data file to find f at each point
    # -----------------------------------------------------------------------------
    resultLin = [abs((flin(round(i,1)) - j)) for i, j in zip(dataExtended["x"], dataExtended["y"])]
    resultQuad = [abs((fquad(round(i,1)) - j)) for i, j in zip(dataExtended["x"], dataExtended["y"])]
    resultCub = [abs((fcub(round(i,1)) - j)) for i, j in zip(dataExtended["x"], dataExtended["y"])]
    plt.plot(dataExtended["x"], resultLin, "-", dataExtended["x"], resultQuad, "--", dataExtended["x"], resultCub, "-.",)
    plt.legend(["linear", "quadratic", "cubic spline"], loc="best")
    plt.savefig("error.png")
    plt.close()
    

if __name__ == "__main__":
    Interpolation()
