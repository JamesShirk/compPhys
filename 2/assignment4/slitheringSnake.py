import numpy as np
from numpy.random import random_sample
from math import floor, sqrt
import itertools
import matplotlib.pyplot as plt

class snake:
    def __init__(self, length):
        self.grid = np.zeros((length, 2))
        for i in range(length):
            self.grid[i] = np.array((i, 0))
        self.grid = self.grid.tolist()
        self.currentHead = 0
        self.nMoveIterations = 0
        self.output = []
    def move(self, head = None):
        if head is None:
            headCheck = random_sample()
            self.currentHead = -1 if headCheck < .5 else 0
        headPos = self.grid[self.currentHead]
        x = headPos[0]
        y = headPos[1]
        possibleMovements = [[x + 1, y],[x - 1, y],[x, y + 1],[x, y - 1]]
        i = 3
        while i >= 0:
            if possibleMovements[i] in self.grid:
                del possibleMovements[i]
            i -= 1
        if len(possibleMovements) == 0:
            self.nMoveIterations += 1
            self.currentHead = -1 if self.currentHead == 0 else 0
            if self.nMoveIterations == 2:
                return -1
            self.move()
        else:
            direction = floor(random_sample() * len(possibleMovements))
            self.grid.append(possibleMovements[direction]) if self.currentHead == -1 else self.grid.insert(0, possibleMovements[direction])
            if self.currentHead == 0:
                del self.grid[-1]
            else:
                del self.grid[0]
            self.output.append(self.__getDistance__())
            return 0

    def printGrid(self):
        print(self.grid)

    def getOutput(self):
        return self.output

    def __getDistance__(self):
        xEnd, yEnd = self.grid[-1][0], self.grid[-1][1]
        xStart, yStart = self.grid[0][0], self.grid[0][1]
        return sqrt((xEnd - xStart)**2 + (yEnd - yStart)**2)

def sumLists(total):
    longest = 0
    for i in total:
        longest = len(i) if len(i) > longest else longest
    sums = []
    n = []
    for i in range(longest):
        sums.append(0)
        n.append(0)
    for i in total:
        for j in range(len(i)):
            sums[j] += i[j]
            n[j] += 1
    aveSum = [i / j for i, j in zip(sums, n)]
    return aveSum, n

if __name__ == "__main__":
    output = []
    for i in range(1000):
        snakey = snake(10)
        i = 0
        #n = 0
        while(i == 0):
            i = snakey.move()
        output.append(snakey.getOutput())
        #    n += 1
        #print(snake1)
        #print(n)
    averages, n = sumLists(output)
    x = range(len(averages))
    plt.plot(x, averages, "-")
    plt.ylabel("Average Distance Between Heads")
    plt.xlabel("N Steps")
    plt.savefig("distance.png")
    plt.close()

    plt.plot(x, n, "-")
    plt.ylabel("Number Not Stuck")
    plt.xlabel("N Steps")
    plt.savefig("stuck.png")