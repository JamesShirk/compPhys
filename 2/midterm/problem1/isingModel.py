from numpy.random import random_sample
from math import floor, exp
import matplotlib.pyplot as plt

def isingModel(L, T, J, nIterations):
    lattice = [[-1 for i in range(L)] for i in range(L)]
    for _ in range(nIterations):
        x, y = floor(random_sample() * L), floor(random_sample() * L)
        r = random_sample()
        if r < exp(-deltaE(lattice, J, x, y)/T):
            lattice[x][y] *= -1
    return lattice


def deltaE(lattice, J, x, y):
    L = len(lattice)
    Nparallel, Nopposite = 0, 0
    neighbors = [(x - 1, y),(x, y - 1),(x + 1, y),(x, y - 1)]
    neighbors = [i for i in neighbors if ((i[0] != -1) and (i[0] != L) and (i[1] != -1) and (i[1] != L))]
    for i in neighbors:
        if lattice[i[0]][i[1]] == lattice[x][y]:
            Nparallel += 1
        else:
            Nopposite += 1
    return 2 * J * (Nparallel - Nopposite)
    

if __name__ == "__main__":
    J = 1
    lattice = isingModel(30, 1, J, 150000)
    plt.imshow(lattice)
    netMagnetization = 0
    for i in lattice:
        for j in lattice:
            netMagnetization += 1
    plt.show()