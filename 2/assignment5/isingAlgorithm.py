from numpy.random import random_sample
import matplotlib.pyplot as plt
import time

# Queue is an abstract data type with these required functions.
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def isNotEmpty(self):
        return False if self.isEmpty() else True

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def swendsenWangUpdate(L, disc, pAdd):
    output = []
    for i in range(len(L)):
        for j in range(len(L[i])):
            if disc[i][j] != 1:
                findAndFlipCluster(L,disc,(i,j), pAdd)
    # TAKE SYSTEM OBSERVABLES
    print(disc)
    # for i in range(len(L)):
    #     for j in range(len(L[i])):
    #         disc[i][j] = 0
    return L, disc

def findAndFlipCluster(L, disc, root, pAdd):
    r = random_sample()
    flip = True if r < .5 else False
    q = Queue()
    q.enqueue(root)
    disc[root[0]][root[1]] == 1 
    while (q.isNotEmpty()):
        x = q.dequeue()
        for i in range(len(L)):
            for j in range(len(L[i])):
                y = [[i-1, j],[i + 1, j],[i, j - 1],[i, j + 1]]
                LY = []
                for k in y:
                    try:
                        LY.append(disc[k[0]][k[1]])
                    except:
                        LY.append(None)
                for k in y:
                    if disc[i][j] in LY:
                        index = LY.index(disc[i][j])
                        r = random_sample()
                        if r < pAdd:
                            q.enqueue(y[index])
                            disc[y[index][0]][y[index][1]] = 1
        L[x[0]][x[1]] = L[x[0]][x[1]] * (-1 if flip == True else 1)

def initialState(size):
    L = []
    disc = []
    for i in range(size):
        row = []
        discrow = []
        for j in range(size):
            row.append(j + size*i)
            discrow.append(1) if random_sample() > .6 else discrow.append(0)
        L.append(row)
        disc.append(discrow)
    return L, disc

if __name__ == "__main__":
    L, disc = initialState(16)
    L, disc = swendsenWangUpdate(L, disc, 1.0)
    for i in range(len(L)):
        for j in range(len(L)):
            L[i][j] == 0 if L[i][j] < 0 else 1
    plt.spy(disc)
    plt.show()