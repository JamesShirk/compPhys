# November 21, 2019 James Shirk Computational Physics Bonus Homework

import itertools
from numpy import linspace
import matplotlib.pyplot as plt

# Where matrix is in form Ax = b, x0 is best guess and defaults to 0,0,0
def matrixSolver(A, b, nIterations, tolerance, relaxation, x0 = [0,0,0]):
    k = 1
    out = x0
    tolCounter = 0
    while(k <= nIterations):
        
        # Main iterative method 

        for i in range(0, len(A)):
            sigma = 0
            for j in range(0, len(A)):
                if (j != i):
                    sigma += A[i][j]*out[j]
            out[i] = out[i] + relaxation*(((b[i] - sigma)/(A[i][i])) - out[i])


        # Tolerance checker
        tolCheck = [0,0,0]
        
        # Makes a new matrix with dimensions equal to b and then compares, if all three are within the tolerance from b, it breaks the loop
        for i in range(0, len(A)):
             for j in range(0, len(A)):
                tolCheck[i] += out[j]*A[i][j]
        for i in range(0, len(A)):
            if (abs(b[i] - tolCheck[i]) < tolerance):
                tolCounter += 1
        if(tolCounter == 3):
            print("The problem took " + str(k) + " iterations.")
            break
        else:
            tolCounter = 0
        k += 1

    # Prints the output
    print(out)
    
    # Returns number of iterations
    return(k)

def plot():
    # Taken manually, looping caused problems for some reason
    # Diverges above 1.4
    relaxation = [.1,.2,.3,.4,.5,.6,.7,.8,.9,.95, .975, .9825, .99, 1.01, 1.02, 1.03, 1.04, 1.05, 1.1, 1.2, 1.3, 1.4]
    nIterations = [308, 154, 100, 72, 55, 43, 35, 28, 23, 20, 19, 19, 18, 17, 17, 16, 17, 18, 24, 41, 85, 666]

    # Plots the relaxation vs the number of iterations on a semilog scale.
    plt.plot(relaxation, nIterations, "-")
    plt.xlabel("Relaxation Parameter")
    plt.ylabel("Number of Iterations(Log Scale)")
    plt.title("Number of Iterations over Relaxation Parameter")
    plt.yscale("log")
    plt.savefig("relaxation.png", dpi = 1000)
    plt.close()

if __name__ == "__main__":
    # Defines the matrix A and vector b, then plugs into iterative method
    matrix = [[3, -1 , 1],[3, 6, 2],[3, 3, 7]]
    b = [1, 0, 4]
    matrixSolver(matrix, b, 10000, 1e-10, 1.04)

    # For making the plot
    plot()