# James Shirk, August 28, 2019 for Dr. Pratt Computational Physics class assignment 1, problem 2
# Generates Data for the problem

# Imports math used to take factorial and numpy used to generate list
import math
import numpy as np

# Main Function, takes in order and outputs results from -5 to 5 incrementing by .1 for the taylor cos approximation
def TaylorSeries(order):
    # Make an array of numbers from 0 to 10 incrementing by .1
    numbers = np.linspace(-5,5,1001)
    taylorOutput = []
    # The outer for loop iterates over each element in the 'numbers' list
    # The innter for loop takes in the order and does the mathematical summation
    # This is an attempt to replicate the mathematical summation by taking in the order
    for i in numbers:
        result = 0
        for j in range(0,(order+1)):
            result += ((-1)**j)*((i**(2*j))/math.factorial(2*j))
        taylorOutput.append(result)
    # Opens file with name 'taylorOutputOrder(order).txt and prints writes the results to it
    with open("taylorOutputOrder" + str(order) + ".txt","w+") as f:
        for i in range(0, len(taylorOutput)):
            f.write(str(taylorOutput[i]) + "\n")
    # Creates a file with the number list used to allow for easier math in R
    with open("numberList.txt","w+") as f:
        for i in range(0, len(numbers)):
            f.write(str(numbers[i]) + "\n")

#Executes the functions by taking in user input for the order series to be produced.
if __name__ == "__main__":
    TaylorSeries(int(input("Which order cosine taylor series approximation do you want (starting at 0)? ")))