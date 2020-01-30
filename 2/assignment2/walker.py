import numpy as np                          # For numpy arrays and associated methods
from random import randint                  # To generate a random direction for the particle to walk
import matplotlib.pyplot as plt             # Plotting
import matplotlib                           # This and the following line are to prevent crashes when trying to animate
matplotlib.use('Agg')                      
import matplotlib.animation as animation    # Making a gif of the motion
import imageio                              # Saving the gif of the motion
from math import sqrt                       # Sqrt function

# Getting to use OOP :))
# This class represents the particle undergoing the 'brownian' motion
class walker:
    # Constructor, sets an empty grid of size = size, and the center equal to zero
    def __init__ (self, size):
        self.grid = np.zeros((size, size))
        self.grid[size//2][size//2] = 1
    # Public Methods
    # Moves the particle in a random direction
    def move(self):
        direction = randint(1, 4)
        if(direction == 1):
            self.__moveLeft()
        elif (direction == 2):
            self.__moveRight()
        elif (direction == 3):
            self.__moveUp()
        else:
            self.__moveDown()
    # Returns x, y location in the grid the particle currently occupies by finding where in the grid is 1
    def currentLocation(self):
        x, y = np.where(self.grid == 1)
        return int(x), int(y)
    def returnGrid(self):
        return self.grid
    # Private Methods
    # Each method has the same format, finding current location by finding the 1 value, setting a value one shifted of that to 1 and the current to .25.
    # If it's at a wall it will just recursively moves until it randomly gets a valid direction.
    def __moveRight(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        try:
            self.grid[x][y + 1] = 1
            self.grid[x][y] = 0.25
        except:
            self.move()
    def __moveLeft(self):
        x, y = np.where(self.grid == 1)
        if (x == 0 or y == 0):
            self.move()
            print(1)
        else:
            x = int(x)
            y = int(y)
            try:
                self.grid[x][y - 1] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    def __moveUp(self):
        x, y = np.where(self.grid == 1)
        if (x == 0 or y == 0):
            self.move()
            print(2)
        else:
            x = int(x)
            y = int(y)
            try:
                self.grid[x - 1][y] = 1
                self.grid[x][y] = 0.25
            except:
                self.move()
    def __moveDown(self):
        x, y = np.where(self.grid == 1)
        x = int(x)
        y = int(y)
        try:
            self.grid[x + 1][y] = 1
            self.grid[x][y] = 0.25
        except:
            self.move()

def test():
    fig, ax = plt.subplots(figsize=(5,5))
    walk1.move()
    ax.imshow(walk1.returnGrid(), cmap="hot")
    ax.set(xlabel="X Position", ylabel="Y Position",title="Current Walker Position")
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return image

def animate(n, fps):
    kwargs_write = {'fps':1.0, 'quantizer':'nq'}
    imageio.mimsave('./movement.gif', [test() for i in range(n)], fps=fps)

def distance(L, NumWalkers):
    output = []
    midX, midY = (L//2, L//2)
    for i in range(NumWalkers):
        walk = walker(L)
        dist = []
        for j in range(1, 501):
            if (j == 10 or j == 20 or j == 50 or j == 100 or j == 200 or j == 500):
                x, y = walk.currentLocation()
                dx = sqrt((x - midX)**2 + (y - midY)**2)
                # print(dx)
                dist.append(dx)
                walk.move()
            else:
                walk.move()
        output.append(dist)
    return output

def histos(L, N):
    input = distance(L, N)
    steps = {0:10, 1:20, 2:50, 3:100, 4:200, 5:500}

    # TODO: FIX THESE NEXT 15 LINES
    list10, list20, list50, list100, list200, list500 = [], [], [], [], [], []
    for i in range(len(input)):
        list10.append(input[i][0])
        list20.append(input[i][1]) 
        list50.append(input[i][2])
        list100.append(input[i][3])
        list200.append(input[i][4])
        list500.append(input[i][5])
    dists = []
    dists.append(list10)
    dists.append(list20)
    dists.append(list50)
    dists.append(list100)
    dists.append(list200)
    dists.append(list500)

    for i in range(6):
        plt.hist(dists[i], bins = 15, density = True)
        plt.ylabel("Probability of Distance from origin for " + str(steps.get(i)) + " steps.")
        plt.xlabel("Distance")
        plt.title("PDF of distance from origin for " + str(steps.get(i)) + " steps.")
        plt.savefig("1DHisto" + str(steps.get(i)) +".png", dpi = 100)
        plt.close()



if __name__ == "__main__":
    walk1 = walker(101)
    animate(2000, 10)
    #histos(11, 150)