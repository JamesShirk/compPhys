from numpy.linalg import det, eig
from numpy import empty
import numpy as np
import eigenValue as eV
import matplotlib.pyplot as plt
from math import sqrt, cos, pi

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

def vibration(nMasses, numPoints):
    
    n = nMasses
    
    T = 10 * np.random.random_sample()
    masses = 10 * np.random.random_sample(n)
    x0 = np.random.random_sample(n) - .5

    print("The initial values are:", x0)
    A = np.zeros(shape=(n,n))
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
    

    output, dummy = eV.eigenValues(A, 1000, 1e-8)
    eigenvals, eigenvecs = eig(A)
    
    gamma = np.dot(np.linalg.inv(eigenvecs), x0)
    
    frequency = np.zeros(shape=(1,n))
    
    for i in range(0, n):
        frequency[0][i] = sqrt(-1*eigenvals[i])

    #g = np.diag(gamma)

    time = np.linspace(0, 720, num = numPoints, endpoint=False)

    endgame = np.zeros(shape = (n, numPoints))

    for i in range(0, n):
        for j in range(0, numPoints):
            for k in range(0, n):
                endgame[i][j] += eigenvecs[i][k]*cos(frequency[0][k] * time[j] * (pi / 180))
    
    endgame = endgame.tolist()

    legend = []
    for i in range(0, n):
        plt.plot(time, endgame[i], "-")
        legend.append("Mass " + str(i + 1))
    plt.xlabel("Time")
    plt.ylabel("$\Delta X$")
    plt.legend(legend, loc="best")
    plt.savefig("motionEquation.png", dpi = 300)
    

if __name__ == "__main__":
    #A = NonSing(8)

    A = np.array(((
        (7, 1),
        (-4, 3)
    )))

    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=3)
    print(A)

    output, junk = eV.eigenValues(A, 10000, 1e-10)
    

    # output, eigenvectors = eV.eigenValues(A, 1000, 1e-10)

    print("output:\n", output.round(5))
    # print("eigenvectors:\n", junk.round(5))

    eigenvals, eigenvecs = eig(A)
    print("eigenvals: \n", eigenvals)
    # print("eigenvectors: \n", eigenvecs)

    # vibration(100, 720)
    