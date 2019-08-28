import math
import numpy as np

# Make an array of numbers from 0 to 10 incrementing by .1
numbers = np.linspace(-5,5,101)

def TaylorSeries(order):
    taylorOutput = []
    for i in numbers:
        result = 0
        for j in range(0,(order+1)):
            result += ((-1)**j)*((i**(2*j))/math.factorial(2*j))
        taylorOutput.append(result)
    with open("taylorOutputOrder" + str(order) + ".txt","w+") as f:
        for i in range(0, len(taylorOutput)):
            f.write(str(taylorOutput[i]) + "\n")

if __name__ == "__main__":
    TaylorSeries(0)
    TaylorSeries(4)
    TaylorSeries(10)