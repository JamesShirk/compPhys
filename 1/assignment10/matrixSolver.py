import itertools
from numpy import linspace
# Where matrix is in form Ax = b, x0 is best guess,
def matrixSolver(A, b, nIterations, tolerance, relaxation, x0 = [0,0,0]):
    k = 1
    out = x0
    tolCounter = 0
    while(k <= nIterations):
        for i in range(0, len(A)):
            sigma = 0
            for j in range(0, len(A)):
                if( j != i ):
                    sigma += relaxation*A[i][j]*out[j]
            out[i] = (1/A[i][i])*(b[i] - sigma)

        # Tolerance checker
        tolCheck = [0,0,0]
        #print(tolCheck)
        for i in range(0, len(A)):
             for j in range(0, len(A)):
                tolCheck[i] += out[j]*A[i][j]
        #print(tolCheck)
        for i in range(0, len(A)):
            if (abs(b[i] - tolCheck[i]) < tolerance):
                tolCounter += 1
        if(tolCounter == 3):
            print("The problem took " + str(k) + " iterations.")
            break
        else:
            tolCounter = 0
        k += 1
    print(out)
    return(k)

if __name__ == "__main__":
    matrix = [[3, -1 , 1],[3, 6, 2],[3, 3, 7]]
    b = [1, 0, 4]
    x = linspace(.1,2, 200, endpoint = False)
    #iterations = [matrixSolver(matrix, b, 10000, 1e-15, i) for i in x]
    #print(iterations)
    matrixSolver(matrix, b, 10000, 1e-15, 1)