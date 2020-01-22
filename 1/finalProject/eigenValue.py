# James Shirk for computational physics 1, November 27,28 2019
# Finds eigenvectors and eigenvalues using 

import numpy as np
from scipy.linalg import hessenberg
from math import sqrt

# Performs a q r decomposition, with Q = Q and A = R
# Uses householder transformations to create zeroes in R and to find the orthagonal matrix Q
def qrDecomosition(matrix):

    R = np.asarray(matrix)
    m, n = R.shape

    Q =  identityMatrix(m)

    for i in range(n - (m == n)):
    #for i in range(n - 1):
        H = identityMatrix(m)
        H[i:, i:] = make_householder(R[i:, i])
        Q = np.matmul(Q, H)
        R = np.matmul(H, R)

    return Q, R

# Performs a householder transformation of a given matrix
def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = identityMatrix(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H

# Creates a size x size identity matrix (1's on the diagonal)
def identityMatrix(size):
    identity = []
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(1) if (j == i) else row.append(0)
        identity.append(row)
    identity = np.asarray(identity)
    identity = identity.astype(float)
    return identity

# Computes the eigenvalues and eigenvectors for a given matrix
def eigenValues(A, numIterations, tolerance):
    k = 1
    copy = A
    m, n = A.shape
    A = hessenberg(A)
    I = identityMatrix(m)
    s = I
    # use an arbitrary number of iterations, always converges within tolernace within ~ 30 iterations
    while(k < numIterations):
        # Basic algorithm is A(0) = QR, then A(1) = RQ, this does not change eigenvalues/vectors
        # Diagonalizes A, where the eigenvalues are the diagonal entries

        # Shifting converges more quickly

        mu = wilkinsonShift(A[m - 2][m - 2], A[m - 1][m - 1], A[m - 2][m - 1])

        A = np.subtract(A, mu*I)
        q, r = qrDecomosition(A)

        s = np.matmul(s, q)

        A = np.matmul(r, q)
        A = np.add(A, mu*I)

        if tolcheck(A, tolerance):
            print("Took " + str(k) + " iterations.")
            return A, s
        k += 1
    return A, s

def eigenValuesNoShift(A, numIterations, tolerance):
    k = 1
    
    s = identityMatrix(A.shape[0])
    # use an arbitrary number of iterations, always converges within tolernace within ~ 30 iterations
    while(k < numIterations):
        # Basic algorithm is A(0) = QR, then A(1) = RQ, this does not change eigenvalues/vectors
        # Diagonalizes A, where the eigenvalues are the diagonal entries
        q, r = np.linalg.qr(A)
        s = np.matmul(s, q)
        A = np.matmul(r, q)
        # Product of all q gives the eigenvectors
        if tolcheck(A, tolerance):
            print("Took " + str(k) + " iterations.")
            return A, s
        k += 1
    return A, s

# Computes the shift
def wilkinsonShift(a, b, c):
    sigma = (a - c) / 2
    return (c - ((sign(sigma) * (b ** 2)) / ((abs(sigma)) + sqrt((sigma ** 2) + (b ** 2)))))

def sign(x):
    return 1 if (x >= 0) else -1

# For a given NxN matrix, checks if all entries below diagonal are within tolerance of zero
# Returns false if not in tolerance, true if within tolerance
def tolcheck(A, tolerance):
    m, n = A.shape
    for i in range(0, m - 1):
        for j in range(i + 1, n):
            if (abs(A[j][i]) > tolerance):
                return False
<<<<<<< HEAD
    return True

def eigenvectors(A, eigs):
    eigvecs = np.zeros(shape=(len(eigs),len(eigs)))
    b = []
    I = identityMatrix(len(eigs))
    for i in eigs:
        b.append(1)
    b = np.asarray(b)
    for i in eigs:
        B = A
        x = i + .1
        B = np.subtract(B, x*I)
        B = np.linalg.inv(B)
        C = np.linalg.norm(B.dot(b))
        B1 = (B.dot(b)) / C
        print(B1)

# if __name__ == "__main__":
#     # Should work for an arbitrarily large matrix
#     a = np.array(((
#         (1, 2,   3),
#         ( 4, 1, 7),
#         (3,  4, 1),
#     )))
#     output, eigenvecs = eigenValues(a, 100, 1e-30)
#     print("output:\n", output.round(10))
#     print("eigenvectors:\n", eigenvecs.round(10))
=======
    return True
>>>>>>> ea055333597b0e6a3dadbd24aab37faa7cf85792
