import numpy as np
from random import randint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import matplotlib.animation as animation
import imageio

class walker:
    # Constructors 
    def __init__ (self, size):
        self.grid = np.zeros((size, size))
        self.grid[size//2][size//2] = 1
    # Public Methods
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
    def currentLocation(self):
        x, y = np.nonzero(self.grid)
        print("Walker is at (" + str(int(x)) + "," + str(int(y)) + ")")
    def returnGrid(self):
        return self.grid
    # Private Methods
    def __moveRight(self):
        x, y = np.nonzero(self.grid)
        x = int(x)
        y = int(y)
        try:
            self.grid[x][y + 1] = 1
            self.grid[x][y] = .25
        except:
            self.move()
    def __moveLeft(self):
        x, y = np.nonzero(self.grid)
        x = int(x)
        y = int(y)
        try:
            self.grid[x][y - 1] = 1
            self.grid[x][y] = .25
        except:
            self.move()
    def __moveUp(self):
        x, y = np.nonzero(self.grid)
        x = int(x)
        y = int(y)
        try:
            self.grid[x + 1][y] = 1
            self.grid[x][y] = .25
        except:
            self.move()
    def __moveDown(self):
        x, y = np.nonzero(self.grid)
        x = int(x)
        y = int(y)
        try:
            self.grid[x - 1][y] = 1
            self.grid[x][y] = .25
        except:
            self.move()

def test():
    fig, ax = plt.subplots(figsize=(5,5))
    walk1.move()
    ax.spy(walk1.returnGrid())
    ax.set(xlabel="X Position", ylabel="Y Position",title="Current Walker Position")
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return image



if __name__ == "__main__":
    walk1 = walker(101)
    kwargs_write = {'fps':1.0, 'quantizer':'nq'}
    imageio.mimsave('./movement.gif', [test() for i in range(100)], fps=5)