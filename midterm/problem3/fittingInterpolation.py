

from numpy import log as ln      # Natural Log 
from numpy import exp, linspace  # Expontial and taking data
import itertools                 # Iterate over two variables
import matplotlib.pyplot as plt  # Plot data
from scipy import interpolate    # Interpolation package

# Calculates the parameters for F(x) = Ae^Bx
def fitting():
    x = [1.2, 2.8, 4.3, 5.4, 6.8, 7.9]
    y = [7.5, 16.03, 38.9, 67.0, 151.8, 250.1]

    sumLnY = 0
    sumX2 = 0
    sumX = 0
    sumXLnY = 0

    # Summing quantities that will be needed
    for i, j in zip(x, y):
        sumLnY += ln(j)
        sumX2 += i**2
        sumX += i
        sumXLnY += (i*ln(j))

    
    # You may solve for these functions by taking the given fit y = Aexp(Bx) and taking the natural log
    # ln(y) = ln(A) +  Bx and then use the formula to find ln(A) and B

    a = (((sumLnY * sumX2) - (sumX * sumXLnY)) / ((len(x) * sumX2) - (sumX ** 2)))
    b = (((len(x) * sumXLnY) - (sumX * sumLnY)) / ((len(x) * sumX2) - (sumX ** 2)))

    # a is really ln(A) so you must take the exponential before returning it
    return exp(a), b;

# Calculates R2 Value
def rSquared():

    x = [1.2, 2.8, 4.3, 5.4, 6.8, 7.9]
    y = [7.5, 16.03, 38.9, 67.0, 151.8, 250.1]

    sumYYMean2 = 0
    residualSum = 0

    for i, j in zip(x, y):
        sumYYMean2 += ((j - ((sum(y)) / len(y))) ** 2)
        residualSum += ((j - fitFunction(i)) ** 2)

    print("Rsquared = ", (1 - (residualSum / sumYYMean2)))

# Uses the a and b from fitting() and turns it into a function
def fitFunction(x):
    a, b = fitting()
    return (a*exp(b*x))

# Makes the plot of the fitting
def plotFit():
    x = [1.2, 2.8, 4.3, 5.4, 6.8, 7.9]
    y = [7.5, 16.03, 38.9, 67.0, 151.8, 250.1]
    xFit = linspace(1, 8, 500)
    yFit = [fitFunction(i) for i in xFit]
    plt.plot(x, y, "o", xFit, yFit, "--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Data and Least Squares Fit")
    plt.legend(["Data", "Least Squares Fit"], loc="best")
    plt.savefig("leastSquaresFit.png", dpi = 300)
    plt.close()

# Makes the plot of the interpolation
def interpolation():
    x = [1.2, 2.8, 4.3, 5.4, 6.8, 7.9]
    y = [7.5, 16.03, 38.9, 67.0, 151.8, 250.1]
    cubic = interpolate.interp1d(x, y, kind = "cubic")
    xNew = linspace(1.2, 7.9, 200)
    yNew = [cubic(i) for i in xNew]
    xInter = [2.7, 4.2, 5.3, 6.7, 7.8]
    yInter = [cubic(i) for i in xInter]
    plt.plot(x, y, "o", xInter, yInter, "o", xNew, yNew, "--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Data and Cubic Spline Interpolation")
    plt.legend(["Data", "Interpolated Points", "Interpolation function"], loc="best")
    plt.savefig("interpolation.png", dpi = 1000)
    plt.close()

# Plots both on the same graph
def fittingInterpolation():

    # Interpolation Calculation
    x = [1.2, 2.8, 4.3, 5.4, 6.8, 7.9]
    y = [7.5, 16.03, 38.9, 67.0, 151.8, 250.1]
    cubic = interpolate.interp1d(x, y, kind = "cubic")

    xNew = linspace(1.2, 7.9, 500)
    yInterpolation = [cubic(i) for i in xNew]
    yFitting = [fitFunction(i) for i in xNew]
    plt.plot(x, y, "o", xNew, yInterpolation, "--", xNew, yFitting, "--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Data interpolated and fitted")
    plt.legend(["Data", "Interpolated Points", "Exponential Fit"], loc="best")
    plt.savefig("allSamePlot.png", dpi = 1000)
    plt.close()


    # Calculates interpolation and fit value at each x 
    xCompare = [2.7, 4.2, 5.3, 6.7, 7.8]
    yInter = [cubic(i) for i in xCompare]
    yFit = [fitFunction(i) for i in xCompare]


    # Relative difference
    relDif = [abs(yInter[i] - yFit[i]) / ((yInter[i] + yFit[i]) / 2) for i in range(0, len(yFit))]
    plt.plot(xCompare, relDif, "-o")
    plt.xlabel("x")
    plt.ylabel("relative difference")
    plt.title("Relative Difference Interpolation and Fit")
    plt.savefig("relativeDifference.png", dpi = 1000)
    plt.close()


    # Percent difference
    perDif = [abs(yInter[i] - yFit[i]) / ((yInter[i] + yFit[i]) / 2) * 100 for i in range(0, len(yFit))]
    plt.plot(xCompare, perDif, "-o")
    plt.xlabel("x")
    plt.ylabel("Percent difference")
    plt.title("Percent Difference Interpolation and Fit")
    plt.savefig("percentDifference.png", dpi = 1000)
    plt.close()


if __name__ == "__main__":
    plotFit()
    interpolation()
    fittingInterpolation()
    fitting()
    rSquared()