# James Shirk Computational Physics Assignment 1 Problem 1
# Using Numpy generated values

import numpy as np              # For PRNG
from math import floor          # Floor function
import matplotlib.pyplot as plt # Plotting
import time


# Calculates the central moment of order x
def centralMoment(input, order):
    moment = 0
    mean = sum(input)/len(input)
    for i in input:
        moment += (i - mean) ** order
    return moment / len(input)

# Calculates the skewness using the central moments
def skewness(input):
    return centralMoment(input, 3) / (centralMoment(input, 2)**(1.5))

# Calculates the kurtosis using the central moments
def kurtosis(input):
    return centralMoment(input, 4) / (centralMoment(input, 2)**(2))

# Creates an array of dimention nValues, multplies it by the max, and then gets ints by flooring
def numberGenerator(nValues, max, plusOne = None):
    sample = np.random.random_sample((nValues,))
    sample *= max
    output = [floor(i) for i in sample]
    output = np.array(output)
    if(plusOne):
        output = output + 1
    return output

# For uncorrelated random numbers within the interval [0,1], the following relation should hold true
# Mean(x^k) = 1/(k + 1)
# This checks that
def randomness(k):
    x = numberGenerator(1000, 100)
    y = [i / 100. for i in x]
    num = []
    for i in y:
        num.append(i ** k)
    mean = sum(num)/len(num)
    expected = 1/(1+k)
    print("For a k of", k, "Random numbers should return", expected, "They did return", mean, "a difference of ", (abs(expected - mean)/expected)*100,"%")
    print("Mean squared is", (sum(y)/len(y))**2,"It should equal .25")

# Fixed Die
def weightedDie(nRolls):
    x = numberGenerator(nRolls, 100, plusOne = True)
    # Converts type back to list
    output = [i for i in x]
    # If a output is above 75 (25% of the values), it sets the output to 6, else it mods it by 5 which should evenly distribute the remaining rolls
    # 15% each
    for i in range(0, len(output)):
        if (output[i]) > 74:
            output[i] = 6
        else:
            output[i] = (output[i] % 5) + 1
    # System IO
    print("------fixed------")
    countOutput(output)
    print("The variance is ", centralMoment(output, 2))
    print("The skewness is ", skewness(output))
    print("The kurtosis is ", kurtosis(output))
    return output

def correctDie(nRolls):
    # Generates 1000 values from 0 to 5, then adds 1 and returns, should already be evenly distibuted
    x = numberGenerator(nRolls, 6, plusOne = True)
    # Converts type back to list
    output = [i for i in x]
    # System IO
    print("------fair------")
    countOutput(output)
    print("The variance is ", centralMoment(output, 2))
    print("The skewness is ", skewness(output))
    print("The kurtosis is ", kurtosis(output))
    return output

# Counts the number of sixes or the number of rolls for each value
def countOutput(input, n = 1000, six = None):
    if six == True:
        count = 0
        for i in range(0, n):
            if input[0][i] == input[1][i] and input[0][i] == 6:
                count += 1
        print("The number of 6 + 6 rolls was: ", count)
        return 0
    for i in range(0, 6):
        print("The number for roll " + str(i + 1) + " " ,input.count(i + 1), ". Proportion of total: ",input.count(i + 1) / n)

if __name__ == "__main__":
    nRolls = 1000
    fairDie = correctDie(nRolls)
    fixedDie = weightedDie(nRolls)
    dieRolls = [fairDie, fixedDie]
    dieRolls.append([i + j for i, j in zip(dieRolls[0],dieRolls[1])])
    countOutput(dieRolls, nRolls, six = True)

    # 2D PDF
    plt.hist2d(dieRolls[0], dieRolls[1], bins = [6,6], range = [[.5, 6.5], [.5, 6.5]], density = True)
    plt.ylabel("Fixed Die")
    plt.xlabel("Fair Die")
    plt.title("PDF for die rolls")
    plt.colorbar()
    plt.savefig("2DHistoPackage.png", dpi = 100)
    plt.close()

    # 1D PDF
    plt.hist(dieRolls[2], bins = 12, range = (.5, 12.5), density = True)
    plt.ylabel("Probability")
    plt.xlabel("Sum of Die Rolls")
    plt.title("PDF for sum of Die Rolls")
    plt.savefig("1DHistoPackage.png", dpi = 100)
    plt.close()

    # System IO
    print("------sum------")
    print("The variance is ", centralMoment(dieRolls[2], 2))
    print("The skewness is ", skewness(dieRolls[2]))
    print("The kurtosis is ", kurtosis(dieRolls[2]))

    for i in range(3, 10):
        randomness(i)