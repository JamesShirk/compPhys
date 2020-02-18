import numpy as np                          # For numpy arrays and associated methods
from random import randint                  # To generate a random direction for the particle to walk
import matplotlib.pyplot as plt             # Plotting
import matplotlib                           # This and the following line are to prevent crashes when trying to animate
matplotlib.use('Agg')                      
import matplotlib.animation as animation    # Making a gif of the motion
#import imageio                              # Saving the gif of the motion
from math import sqrt                       # Sqrt function

# Getting to use OOP :))
# This class represents the particle undergoing the 'brownian' motion
class walker:
    # Constructor, sets an empty grid of size = size, and the center equal to zero, the grid represents the walking area of the brownian walker.
    # Initializes a number of other important variables too
    def __init__ (self, size):
        self.grid = np.zeros((size, size))
        self.grid[size//2][size//2] = 1
        self.size = size
        self.increment = 0
        self.steps = 0
        self.stuckToWall = 0
        self.stuckLocations = []
        self.grids = []
    # ------------------------------------ 
    # Public Methods
    # ------------------------------------ 
    # Moves the particle in a random direction
    def move(self):
        self.steps += 1
        direction = randint(1, 4)
        if (direction == 1):
            self.__moveLeft()
        elif (direction == 2):
            self.__moveRight()
        elif (direction == 3):
            self.__moveUp()
        else:
            self.__moveDown()
    # Moves iteratively until the increments are more than n particles. increment incremements when a particle gets stuck
    def moveUntilStuck(self, nParticles):
        k = nParticles
        while (self.increment < nParticles):
            self.move()
        return self.stuckLocations, self.grids, self.stuckToWall
    # Returns x, y location in the grid the particle currently occupies by finding where in the grid is 1
    def currentLocation(self):
        x, y = np.where(self.grid == 1)
        return int(x), int(y)
    def returnGrid(self):
        return self.grid
    # ------------------------------------ 
    # Private Methods
    # ------------------------------------ 
    # Upon a particle being stuck it will call the new particle method which initializes the center to 1 again and increments.
    def __newParticle(self):
        self.steps = 0
        self.grid[self.size//2][self.size//2] = 1
        print("Particle " + str(self.increment) + " has gotten stuck\r", end = "")
        self.increment += 1
    # Each method has the same format, finding current location by finding the 1 value, setting a value one shifted of that to 1 and the current to .25.
    # If it's at a wall it will get stuck i.e., set current location to .75 and then initialize a "new" walker
    # Each step has to check if the particle is at a wall or near another particle, and if not it will move
    # Each of the four methods is the same except the movement direction
    def __moveRight(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        if (self.__checkWall(x, y)):
            self.stuckToWall += 1
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        elif (self.__checkNearby(x, y)):
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        else:
            try:
                self.grid[x][y + 1] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    def __moveLeft(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        if (self.__checkWall(x, y)):
            self.stuckToWall += 1
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        elif (self.__checkNearby(x, y)):
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        else:
            try:
                self.grid[x][y - 1] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    def __moveUp(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        if (self.__checkWall(x, y)):
            self.stuckToWall += 1
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        elif (self.__checkNearby(x, y)):
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        else:
            try:
                self.grid[x - 1][y] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    def __moveDown(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        if (self.__checkWall(x, y)):
            self.stuckToWall += 1
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        elif (self.__checkNearby(x, y)):
            self.grid[x][y] = .75
            self.__output(x, y)
            self.__newParticle()
        else:
            try:
                self.grid[x + 1][y] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    # Called upon a particle being stuck; creates an array with the final location and n steps, then appends this and the grid to a list
    def __output(self, x, y):
        data = []
        data.append(self.steps)
        data.append(x)
        data.append(y)
        self.grids.append(self.grid.tolist())
        self.stuckLocations.append(data)
    # Returns true if a particle is nearby (e.g. one of the directions == .75) and false otherwise
    def __checkNearby(self, x, y):
        return (self.grid[x - 1][y] == .75 or self.grid[x + 1][y] == .75 or self.grid[x][y + 1] == .75 or self.grid[x][y - 1] == .75)
    # Returns true if the particle is next to wall false otherwise
    def __checkWall(self, x, y):
        return (x == self.size - 1  or y == self.size - 1 or x == 0 or y == 0)

# Moves it until stuck, then creates a heatmap of all of the particles before calling the histos functions and returning the grids to be used for animations
def movement(n):
    walk = walker(101)
    stuckLocations, grids, nStuckToWall = walk.moveUntilStuck(n)
    fig, ax = plt.subplots(figsize=(5,5))
    ax.imshow(walk.returnGrid(), cmap="hot")
    ax.set(xlabel="X Position", ylabel="Y Position",title="Current Walker Position")
    plt.savefig("problem2/heatMap.png", dpi = 100)
    print(nStuckToWall)
    print("The proportion that stuck to the wall over those that did not is " + str((nStuckToWall / n) * 100) + "%")
    histos(stuckLocations)
    return grids

# Creates histogram of the finalposition and the number of steps before being stuck
def histos(stuckLocations):
    nSteps, xFinal, yFinal = [], [], []
    for i in range(len(stuckLocations)):
        nSteps.append(stuckLocations[i][0])
        xFinal.append(stuckLocations[i][1])
        yFinal.append(stuckLocations[i][2])
    
    plt.hist2d(xFinal, yFinal, bins = 10, density = True)
    plt.ylabel("Final Y Position")
    plt.xlabel("Final X Position")
    plt.title("PDF for Final position")
    plt.colorbar()
    plt.savefig("problem2/2DHistoPosition.png", dpi = 100)
    plt.close()

    plt.hist(nSteps, bins = 50, density = True)
    plt.ylabel("Probability")
    plt.xlabel("Number of Steps until Stuck")
    plt.title("Probability versus N steps")
    plt.savefig("problem2/nStepsPDF.png", dpi = 100)
    plt.close()

# Update plot function for the animation creation
def updateFig(*args):
    global k
    k = k + 1 if k < 999 else 0
    print(k)
    im.set_array(grids[k])
    return im,

if __name__ == "__main__":
    # Main method
    grids = movement(100)

    # All for animation
    # k = 0
    # fig = plt.figure()
    # im = plt.imshow(grids[0], animated=True, cmap="hot")
    # ani = animation.FuncAnimation(fig, updateFig, frames = 999)
    # ani.save('problem2/change.gif', writer='imagemagick', fps=10)