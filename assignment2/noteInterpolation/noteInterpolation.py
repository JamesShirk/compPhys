# James Shirk, September 12,  2019 for Dr. Pratt Computational Physics class assignment 1, problem 2
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import misc
import pandas as pd
from numpy import linspace, arange

# Main Function
def Interpolation():
    # Read in the data files which were written as csv's and store them in Panda dataframe
    data = pd.read_csv("data.txt")
    # dataExtended = pd.read_csv("dataextended.txt")
    # Performs the three interpolation methods, linear, quadratic spline, and cubic spline using the x and y data that was provided
    # Cannot return functions as printing them gives memory address 
    flin = interpolate.interp1d(data["x"], data["y"], kind = "linear")
    fquad = interpolate.interp1d(data["x"], data["y"], kind = "quadratic")
    fcub = interpolate.interp1d(data["x"], data["y"], kind = "cubic")
    # Must generate an array of new values to plug into the interpolation functions
    xnew = linspace(-4, 5, endpoint = True)
    # Plots the functions and changes config settings, legend etc. Saves as .png
    plt.plot(data["x"], data["y"], "-", xnew, flin(xnew), "-", xnew, fquad(xnew), "-.", xnew, fcub(xnew), "--")
    plt.legend(["data", "linear", "quadratic", "cubic spline"], loc="best")
    plt.savefig("noteInterpolation.png", dpi = 1000)
    plt.close()

    test = []
    print(misc.derivative(flin, 4, n = 2))
    for i in range(-3, 5):
        ii = i
        i = InterpolationError(i)
        i *= misc.derivative(flin, ii, n = 2)
        print(i)
        test.append(i)
    testx = arange(-3, 5, 1)
    plt.plot(data["x"], data["y"], "-", testx, test, "--")
    plt.savefig("test.png")
    plt.close()
    # -----------------------------------------------------------------------------
    # Plots to visualize absolute error
    # List comprehensions are used on a more robust data file to find absolute error of f at each point
    # More file is made assuming that this is a step function subtracted from another
    # -----------------------------------------------------------------------------
    #resultLin = [abs((flin(round(i,1)) - j)) for i, j in zip(dataExtended["x"], dataExtended["y"])]
    #resultQuad = [abs((fquad(round(i,1)) - j)) for i, j in zip(dataExtended["x"], dataExtended["y"])]
    #resultCub = [abs((fcub(round(i,1)) - j)) for i, j in zip(dataExtended["x"], dataExtended["y"])]
    # Plots the absolute error functions all on the same graph and store as a png
    #plt.plot(dataExtended["x"], resultLin, "-", dataExtended["x"], resultQuad, "--", dataExtended["x"], resultCub, "-.",)
    #plt.legend(["linear", "quadratic", "cubic spline"], loc="best")
    #plt.savefig("error.png", dpi = 1000)
    #plt.close()

def InterpolationError(x):
    x = (x + 4) * (x - 5)
    x /= 2
    return x
# Executes functions on running script
if __name__ == "__main__":
    Interpolation()
