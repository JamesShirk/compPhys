import numpy as np              # For PRNG
from math import floor          # Floor function
import matplotlib.pyplot as plt # Plotting
import time

# Creates an array of dimention nValues, multplies it by the max, and then gets ints by flooring
def numberGenerator(nValues, max, plusOne = None):
    sample = np.random.random_sample((nValues,))
    sample *= max
    output = [floor(i) for i in sample]
    output = np.array(output)
    if(plusOne):
        output = output + 1
    return output

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
    #print("------fixed------")
    #countOutput(output)
    #print("The variance is ", centralMoment(output, 2))
    #print("The skewness is ", skewness(output))
    #print("The kurtosis is ", kurtosis(output))
    return output

def correctDie(nRolls):
    # Generates 1000 values from 0 to 5, then adds 1 and returns, should already be evenly distibuted
    x = numberGenerator(nRolls, 6, plusOne = True)
    # Converts type back to list
    output = [i for i in x]
    # System IO
    #print("------fair------")
    #countOutput(output)
    #print("The variance is ", centralMoment(output, 2))
    #print("The skewness is ", skewness(output))
    #print("The kurtosis is ", kurtosis(output))
    return output

# Counts the number of sixes or the number of rolls for each value
def countOutput(input, n = 1000, six = None):
    if six == True:
        count = 0
        for i in range(0, n):
            if input[0][i] == input[1][i] and input[0][i] == 6:
                count += 1
        #print("The number of 6 + 6 rolls was: ", count)
        return count
    for i in range(0, 6):
        print("The number for roll " + str(i + 1) + " " ,input.count(i + 1), ". Proportion of total: ",input.count(i + 1) / n)

def run():
    nRolls = 1000
    fairDie = correctDie(nRolls)
    fixedDie = weightedDie(nRolls)
    dieRolls = [fairDie, fixedDie]
    dieRolls.append([i + j for i, j in zip(dieRolls[0],dieRolls[1])])
    return countOutput(dieRolls, nRolls, six = True)

if __name__ == "__main__":
    sixes = []
    for i in range(0, 100000):
        sixes.append(run())
    
    # 1D PDF
    plt.hist(sixes, bins = 30, density = True)
    plt.ylabel("Probability")
    plt.xlabel("NSixes")
    plt.title("PDF for number of six pairs")
    plt.savefig("1DHistoSixesPackage.png", dpi = 100)
    plt.close()