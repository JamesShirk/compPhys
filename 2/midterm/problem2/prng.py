import time
from readAudio import getSeed

# Main PRNG uses xorshift method
class rng:
    def __init__(self):
        # Instantiate seeds
        self.seeds = getSeed(3)
        self.x = self.seeds[5]
        self.y = self.seeds[15]
        self.z = self.seeds[20]
        self.w = self.seeds[25]
    def __xorshift(self):
        # Generates the random numbers
        t = self.x ^ (self.x  << 11)
        self.x = self.y
        self.y = self.z
        self.z = self.w
        self.w = self.w ^ (self.w >> 19) ^ t ^ (t >> 8)
    def getRandom(self, n):
        self.__xorshift()
        return (self.w % n)
