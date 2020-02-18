import numpy as np                          # For numpy arrays and associated methods
from random import randint                  # To generate a random direction for the particle to walk
import matplotlib.pyplot as plt             # Plotting
import imageio                              # Saving the gif of the motion
from math import sqrt                       # Sqrt function

# Getting to use OOP :))
# This class represents the particle undergoing the 'brownian' motion
class walker:
    # Constructor, sets an empty grid of size = size, and the center equal to zero
    def __init__ (self, size, Apersistence = None):
        self.grid = np.zeros((size, size))
        self.grid[size//2][size//2] = 1
        self.halfSize = 51
        self.directionLastMoved = 0
        self.persistence = Apersistence
        self.output = []
    # Public Methods
    # Moves the particle in a random direction
    def move(self, memory = None, dont = None):
        if self.directionLastMoved == 0:
            direction = randint(1,4) if memory is None else memory
            if dont is not None:
                while(direction == dont):
                    direction = randint(1,4)
            if(direction == 1):
                self.__moveLeft()
            elif (direction == 2):
                self.__moveRight()
            elif (direction == 3):
                self.__moveUp()
            elif (direction == 4):
                self.__moveDown()
        else:
            persistanceCheck = randint(1,5)
            if persistanceCheck == 1 or persistanceCheck == 2 or persistanceCheck == 3:
                lastMovement = self.directionLastMoved
                self.directionLastMoved = 0
                self.move(lastMovement)
            else:
                lastMovement = self.directionLastMoved
                self.directionLastMoved = 0
                self.move(None, lastMovement)
    # Returns x, y location in the grid the particle currently occupies by finding where in the grid is 1
    def currentLocation(self):
        x, y = np.where(self.grid == 1)
        return int(x), int(y)
    def returnGrid(self):
        return self.grid
    def getOutput(self):
        return self.output
    # Private Methods
    # Each method has the same format, finding current location by finding the 1 value, setting a value one shifted of that to 1 and the current to .25.
    # If it's at a wall it will just recursively moves until it randomly gets a valid direction.
    def __moveLeft(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        if (x == 0 or y == 0):
            self.move()
        else:
            try:
                self.directionLastMoved = 1 if self.persistence is not None else 0
                self.__output(x, y)
                self.grid[x - 1][y] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    def __moveRight(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        try:
            self.directionLastMoved = 2 if self.persistence is not None else 0
            self.__output(x, y)
            self.grid[x + 1][y] = 1
            self.grid[x][y] = 0.25
        except:
            self.move()
    def __moveUp(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        if (x == 0 or y == 0):
            self.move()
        else:
            try:
                self.directionLastMoved = 3 if self.persistence is not None else 0
                self.__output(x, y)
                self.grid[x][y + 1] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    def __moveDown(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        try:
            self.directionLastMoved = 4 if self.persistence is not None else 0
            self.__output(x, y)
            self.grid[x][y - 1] = 1
            self.grid[x][y] = 0.25
        except:
            self.move()
    def __output(self, x, y):
        dx = sqrt((x - self.halfSize)**2 + (y - self.halfSize)**2)
        self.output.append(dx)

def run(nParticles, nSteps, persistence):
    allMovement = []
    for i in range(nParticles):
        walk = walker(101, True)
        for j in range(nSteps):
            walk.move()
        allMovement.append(walk.getOutput())
    rootMeanSquared = RMS(nParticles, nSteps, allMovement)
    x = np.arange(1, nSteps + 1)
    plot(x, rootMeanSquared)

def RMS(nParticles, nSteps, movement):
    squaredSums = []
    for i in range(nSteps):
        sum = 0
        for j in range(nParticles):
            sum += (movement[j][i] ** 2)
        sum /= nParticles
        squaredSums.append(sum)
    return squaredSums

def plot(x, rootMeanSquared):
    plt.plot(x, rootMeanSquared, "--")
    plt.ylabel("mean \Delta x(t)^{2}")
    plt.xlabel("t")
    plt.title("Diffusion distance over time with persistence")
    plt.savefig("inClass/rmsWith.png")
    plt.close()

if __name__ == "__main__":
    run(150, 1000, None)