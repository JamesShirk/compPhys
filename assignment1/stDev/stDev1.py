# James Shirk, August 27, 2019 for Dr. Pratt Computational Physics class assignment 1

# Imports the square root function from the math module
from math import sqrt
import statistics

# Open the 'samples.txt' file and append each entry to a list.
with open("samples.txt","r") as f:
    samples = []
    for line in f:
        # Take each line, remove the newline character, convert it to an int and append it to a list
        samples.append(int(line.strip()))

# The first method of standard deviation implementation
def stDev1(samps):
    sum = 0
    sumsq = 0
    N = len(samps)
    # iterate over each element in the list and sum each element and each element squared
    for i in samps:
        sum += i
        sumsq += i**2
    # Calculate the mean and standard deviation
    mean = sum / N
    stDev = sqrt((sumsq - N * (mean**2))/(N-1))
    # Rather than returning the mean and the stdev, I print them to the console
    # This simplifies the code by removing the need to return two variables
    print("From the first method: The mean is " + str(mean) + ", the standard deviation is " + str(stDev))

# The second implementation of standard deviation implementation
def stDev2(samps):
    mean = 0
    stDev = 0
    N = len(samps)
    # iterate over each element, the second argument of range is exclusive so you must add one
    # Find the mean by calculating the mean and then changing the mean up or down due to the impact from each element 
    for i in range(1, (N + 1)):
        j = samps[(i-1)]
        oldMean = mean
        mean += (j-mean)/i
        stDev += (j-mean)*(j-oldMean)
    # finalize calculation of stDev by dividing it by the elements and taking the square root
    stDev /= (N - 1)
    stDev = sqrt(stDev)
    # Rather than returning the mean and the stdev, I print them to the console
    # This simplifies the code by removing the need to return two variables
    print("From the second method: The mean is " + str(mean) + ", the standard deviation is " + str(stDev))

# Execute the functions
if __name__ == "__main__":
    stDev1(samples)
    stDev2(samples)  
