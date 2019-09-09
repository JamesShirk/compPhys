import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
from statistics import mean 

def Interpolation(type):
    types = ["linear","quadratic", "cubic"]
    data = pd.read_csv("data.txt")
    x = data.loc[: ,"x"]
    y = data.loc[: ,"y"]
    f = interpolate.interp1d(x, y, kind = types[type])
    xnew = np.linspace(-4, 5, endpoint = True)
    plt.plot(x, y, "o", xnew, f(xnew), "-")
    plt.legend(["data",  types[type] + " interpolation"], loc="best")
    plt.savefig("data" + types[type] + ".png")
    funcX = f(x)
    # e = []
    # for i in range(0, 10):
    #     z = funcX[i]
    #     l = y[i]
    #     e.append(l - z)
    # print(mean(e))

if __name__ == "__main__":
    Interpolation(int(input("Which type of interpolation do you want (0 for linear, 1 for quadratic, 2 for cubic): ")))

