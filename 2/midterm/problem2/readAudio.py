import wave
import record as rec
import matplotlib.pyplot as plt

def getSeed(n):
    # Generates a sound file (mostly noise) that it reads in as binary (data is 0 - 255)
    rec.generate()
    w = wave.open("output.wav", "rb")
    binary_data = w.readframes(w.getnframes())
    w.close()

    # Takes the product of all the binary data and bitshifts it
    seed = 1
    for i in range(0,len(binary_data)):
        seed *= binary_data[i] + 1
        seed = seed << n
    # due to the number of 10/20/30/40.../100../250 must remove these by doing an approximate floor division
    num = 1
    for i in range(180):
        num *= 1000000000
    seed //= num 

    seedList = []

    # for every 9 numbers it slices the seed (which is ~3000 digits long)
    for i in range(1, len(str(seed)), 9):
        seedList.append(seed % (100000000))
        seed //= (100000000)
    return seedList


if __name__ == "__main__":
    all = []
    for i in range(10):
        all.extend(getSeed(4))
    plt.hist(all, 50)
    plt.xlabel("seed")
    plt.ylabel("N")
    plt.show()