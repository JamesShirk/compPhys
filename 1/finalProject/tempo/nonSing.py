
from numpy.linalg import det, eig
from numpy import empty
import numpy as np
import eigenValue as eV
import matplotlib.pyplot as plt
from math import sqrt, cos, pi
import time

# Generates a random nonsingular matrix by checking the determinent 
def NonSing(n):
    while(True):
        A = generate(n)
        if(det(A) != 0):
            return(A)

# generates a random nxn matrix with random values -10 to 10
def generate(n):
    A = np.random.rand(n, n)
    A *= 10
    return(A)

# Main Problem
def vibration(nMasses, numPoints):
    
    n = nMasses
    
    T = 10 * np.random.random_sample()
    masses = 10 * np.random.random_sample(n)
    x0 = np.random.random_sample(n) - .5
    print("The masses are:", masses)
    print("The initial values are:", x0)
    print("The tension is :", T)
    A = np.zeros(shape=(n,n))
    # Generates the matrix which represents the system
    for i in range(0, n):
        if (i == 0):
            A[0][0] = (-2 * T) / masses[i]
            A[0][1] = T / masses[i]
        elif (i == (n - 1)):
            A[n-1][n-2] = T / masses[i]
            A[n-1][n-1] = (-2 * T) / masses[i]
        else:
            A[i][i - 1] = T / masses[i]
            A[i][i] = (-2 * T)/ masses[i]
            A[i][i + 1] = T / masses[i]
    
    # Used numpy for eigenvectors as I could not calculate them
    # eigenvals, dummy = eV.eigenValues(A, 1000, 1e-8)
    eigenvals, eigenvecs = eig(A)
    
    gamma = np.dot(np.linalg.inv(eigenvecs), x0)
    
    frequency = np.zeros(shape=(1,n))
    
    for i in range(0, n):
        frequency[0][i] = sqrt(-1*eigenvals[i])


    time = np.linspace(0, 720, num = numPoints, endpoint=False)

    endgame = np.zeros(shape = (n, numPoints))

    # Generates an array containing the values over time for each equation.
    for i in range(0, n):
        for j in range(0, numPoints):
            for k in range(0, n):
                endgame[i][j] += gamma[k]*eigenvecs[i][k]*cos(frequency[0][k] * time[j] * (pi / 180))
    
    average = np.average(endgame, axis = 0)

    endgame = endgame.tolist()

    legend = []

    #Plots 
    for i in range(0, n):
        plt.plot(time, endgame[i], "-")
        #legend.append("Mass " + str(i + 1))
    plt.xlabel("Time")
    plt.ylabel("$\Delta X$")
    plt.title("Equations of Motion for " + str(n) + " Masses Connected in Series.")
    #plt.legend(legend, loc="best")
    plt.savefig("motionEquation" + str(n) +".png", dpi = 300)
    plt.close()

    plt.plot(time, average)
    plt.xlabel("Time")
    plt.ylabel("$\Delta\\bar{X}$")
    plt.title("Mean Position from Axis for " + str(n) + " masses")
    plt.legend(legend, loc="best")
    plt.savefig("average" + str(n) +".png", dpi = 300)
    plt.close()


    

if __name__ == "__main__":
    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=3)


    start = time.time()
    vibration(250, 720)
    end = time.time()
    print("The program took ", end - start, " seconds.")
    