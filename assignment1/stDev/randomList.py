# James Shirk, August 27, 2019 for Dr. Pratt Computational Physics class assignment 1, problem 3

# Random Module used to generate random numbers
# The default random seed is based on the time since none is provided
import random

def randomList():
    # Opens a file called samples.txt and then iterates one million times writing a random 
    # number between 0 and 1000 on a seperate line
    with open("samples.txt","w+") as f:
        for i in range(0,1000000):
            f.write(str(random.randint(0,1001))+"\n")

# Executes the function
if __name__ == "__main__":
    randomList()