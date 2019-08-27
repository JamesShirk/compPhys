

def stDev(*args):
    sum = 0
    sumsq = 0
    for x in args:
        sum += x
        sumsq += x**2
    N = len(args)
    mean = sum / N
    return ((sumsq - N*mean**2)/(N-1))

if __name__ == "__main__":
    stDev(*args):
