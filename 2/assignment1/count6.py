import numpy as np              # For PRNG
from math import floor          # Floor function
import matplotlib.pyplot as plt # Plotting
import time

# Main PRNG
def psuedoRanXOR(seed, m1, p, q, n, upperLimit, m2 = None):
    # Allows for the use of two m values (mod value for the Fibbonacci generator)
    m2 = m1 if not isinstance(m2, int) else m2
    # Generates the intial random data using the simple Fibbonacci generator
    nInitial = p + 1 if p > q else q + 1
    initial = psuedoRanSum(seed, m1, nInitial, p, q)
    # Appends values to the end of the list equal to (Xp XOR Xq mod m2)
    for _ in range(0, n):
        initial.append((initial[len(initial) - p] ^ initial[len(initial) - q]) % m2)
    # generates even distribution by modding the output by some upperlimit
    output = [i % upperLimit for i in initial]
    # Returns only the XOR generated values
    return(output[nInitial:n + nInitial])

# Generates Fibbonacci values using a seed as x0 and seed mod p as x1 then just x2 = x1 + x0 mod m
def psuedoRanSum(seed, m, n, p, q):
    x0 = seed
    x1 =  seed % p if seed % 2 == 0 else seed % q
    x2 = 0
    values = []
    for _ in range(0, n):
        x2 = (x1 + x0) % m
        x1 = x2
        x0 = x1
        values.append(x2)
    return values

# Fixed Die
def weightedDie(nRolls):
    x = psuedoRanXOR(round(time.time()), 2**32 - 1, 250, 103, nRolls, 100)
    output = [i + 1 for i in x]
    # If a output is above 75 (25% of the values), it sets the output to 6, else it mods it by 5 which should evenly distribute the remaining rolls
    # 15% each
    for i in range(0, len(output)):
        if (output[i]) > 74:
            output[i] = 6
        else:
            output[i] = (output[i] % 5) + 1
    # System IO
    # print("------fixed------")
    countOutput(output)
    # print("The variance is ", centralMoment(output, 2))
    # print("The skewness is ", skewness(output))
    # print("The kurtosis is ", kurtosis(output))
    return output

def correctDie(nRolls):
    # Generates 1000 values from 0 to 5, then adds 1 and returns, should already be evenly distibuted
    x = psuedoRanXOR(round(time.time()), 2**32 - 1, 250, 103, nRolls, 6)
    output = [i + 1 for i in x]
    # System IO
    # print("------fair------")
    countOutput(output)
    # print("The variance is ", centralMoment(output, 2))
    # print("The skewness is ", skewness(output))
    # print("The kurtosis is ", kurtosis(output))
    return output

# Counts the number of sixes or the number of rolls for each value
def countOutput(input, n = 1000, six = None):
    if six == True:
        count = 0
        for i in range(0, n):
            if input[0][i] == input[1][i] and input[0][i] == 6:
                count += 1
        # print("The number of 6 + 6 rolls was: ", count)
        return count
    for i in range(0, 6):
        # print("The number for roll " + str(i + 1) + " " ,input.count(i + 1), ". Proportion of total: ",input.count(i + 1) / n)
        x = i

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
    plt.savefig("1DHistoSixesManual.png", dpi = 100)
    plt.close()