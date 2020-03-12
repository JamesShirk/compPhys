import numpy as np
from math import floor
import matplotlib.pyplot as plt

class walker:
    def __init__(self, size):
        self.grid = np.zeros((size,size))
        self.grid[size//2][size//2] = 1
        self.size = size
        self.output = []
    def currentPosition(self):
        x,y = np.where(self.grid == 1)
        x, y = int(x), int(y)
        return x, y
    def move(self, n):
        for i in range(n):
            self.__move()
            self.output.append(self.__distanceFromOrigin())
        return self.output, self.grid
    def __move(self):
        possibleSteps = [-2, -1, 1, 2]
        step = possibleSteps[floor(np.random.random_sample() * 4)]
        direction = floor(np.random.random_sample() * 4)
        if direction == 0:
            self.__moveLeft(step)
        if direction == 1:
            self.__moveRight(step)
        if direction == 2:
            self.__moveUp(step)
        else:
            self.__moveDown(step)
    def __moveLeft(self, d):
        x, y = self.currentPosition()
        try:
            self.grid[x - d][y] = 1
            self.grid[x][y] = .25 if d != 0 else 1
        except:
            self.__move()
    def __moveRight(self, d):
        x, y = self.currentPosition()
        try:
            self.grid[x + d][y] = 1
            self.grid[x][y] = .25 if d != 0 else 1
        except:
            self.__move()
    def __moveUp(self, d):
        x, y = self.currentPosition()
        try:
            self.grid[x][y - d] = 1
            self.grid[x][y] = .25 if d != 0 else 1
        except:
            self.__move()
    def __moveDown(self, d):
        x, y = self.currentPosition()
        try:
            self.grid[x][y + d] = 1
            self.grid[x][y] = .25 if d != 0 else 1
        except:
            self.__move()
    def __distanceFromOrigin(self):
        x, y = self.currentPosition()
        origin = self.size // 2
        return np.sqrt((x - origin)**2 + (y - origin)**2)

def averageDistance(outputs):
    distanceLastStep = []
    for i in outputs:
        distanceLastStep.append(i[-1])
    sumDistances = sum(distanceLastStep)
    #distanceLastStep = [i / sumDistances for i in distanceLastStep]
    n, bins, _ = plt.hist(distanceLastStep, density = True)
    plt.xlabel("Distance from origin")
    plt.ylabel("Probability")
    plt.savefig("distance.png")
    plt.close()
    bin_width = bins[1] - bins[0]
    # If it's a PDF it should integrate to 1 over the whole range, so this checkes that.
    integral = bin_width * sum(n)
    print("The histogram integrates to " + str(integral))

if __name__ == "__main__":
    nWalkers = 1000
    outputs = []
    for i in range(nWalkers):
        walky = walker(101)
        output, grid = walky.move(10)
        outputs.append(output)
    averageDistance(outputs)
    plt.imshow(grid, cmap='hot', interpolation='nearest')
    plt.show()
    plt.title("Path of the Walker")
    plt.savefig("path.png")
    plt.close()