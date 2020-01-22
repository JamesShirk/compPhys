import matplotlib.pyplot as plt
import numpy as np
import time
import random

def psuedoRanXOR(seed, m1, p, q, n, upperLimit, m2 = None):
    m2 = m1 if not isinstance(m2, int) else m2
    nInitial = p + 1 if p > q else q + 1
    initial = psuedoRanSum(seed, m1, nInitial, p)
    for _ in range(0, n):
        initial.append((initial[len(initial) - p] ^ initial[len(initial) - q]) % m2)
    output = [i % upperLimit for i in initial]
    return(output[nInitial:n + nInitial])

def psuedoRanSum(seed, m, n, p):
    x0 = seed
    x1 = seed % p
    x2 = 0
    values = []
    for _ in range(0, n):
        x2 = (x1 + x0) % m
        x1 = x2
        x0 = x1
        values.append(x2)
    return values

def weightedDie(nRolls):
    x = psuedoRanXOR(round(time.time()), 2**32 - 1, 250, 103, nRolls, 100)
    output = [i + 1 for i in x]
    choices = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    for i in range(0, len(output)):
        if (output[i]) > 74:
            output[i] = 6
        else:
            output[i] = choices.get(output[i] % 5)
    print("fixed")
    countOutput(output)
    return output

def correctDie(nRolls):
    x = psuedoRanXOR(round(time.time()), 2**32 - 1, 250, 103, nRolls, 6)
    output = [i + 1 for i in x]
    # print(len(output))
    print("fair")
    countOutput(output)
    return output

def countOutput(input, n = 1000, six = None):
    if six == True:
        count = 0
        for i in range(0, n):
            if input[0][i] == input[1][i] and input[0][i] == 6:
                count += 1
        print("The number of 6 + 6 rolls was: ", count)
        return 0
    for i in range(0, 6):
        print("The number for roll " + str(i + 1) + " " ,input.count(i + 1), " . Proportion of total: ",input.count(i + 1) / n)


if __name__ == "__main__":
    # x = psuedoRanXOR(round(time.time()), 2**32 - 1, 250, 103, 10000, 6)
    x = psuedoRanXOR(8249477275360464591067, 2**32 - 1, 250, 103, 10000, 6)
    nRolls = 1000
    fairDie = correctDie(nRolls)
    fixedDie = weightedDie(nRolls)
    dieRolls = [fairDie, fixedDie]
    countOutput(dieRolls, nRolls, six = True)
    #random.shuffle(fairDie)
    #random.shuffle(fixedDie)
    plt.hist2d(dieRolls[0], dieRolls[1], bins = [6,6], range = [[.5, 6.5], [.5, 6.5]], density = True)
    plt.ylabel("Fixed Die")
    plt.xlabel("Fair Die")
    plt.colorbar()
    plt.savefig("testHisto.png", dpi = 100)
    plt.close()
