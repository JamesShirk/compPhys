import numpy as np
from numpy.random import random_sample
from math import floor

class snake:
    def __init__(self, length):
        self.grid = np.zeros((length, 2))
        for i in range(length):
            self.grid[i] = np.array((i, 0))
        self.currentHead = 0
    def move(self):
        headCheck = random_sample()
        if headCheck < .5:
            headPos = self.grid[-1]
            self.currentHead = -1
        else:
            headPos = self.grid[0]
            self.currentHead = 0
        direction = floor(random_sample() * 4)
        x = headPos[0]
        y = headPos[1]
        possibleMovements = np.array(((x + 1, y),(x - 1, y),(x, y + 1),(x, y - 1)))
        i = 0
        while i < 4:
            if possibleMovements[i] in self.grid:
                possibleMovements = np.delete(possibleMovements, i)
                i += 1
            i += 1
        print(possibleMovements)
            
    def __str__(self):
        return np.array2string(self.grid, precision=3, separator=',', suppress_small=True)

if __name__ == "__main__":
    snake1 = snake(10)
    for i in range(20):
        snake1.move()