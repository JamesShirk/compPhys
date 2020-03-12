# Discrete form of the sde should be 
# Y(i+1) = Yi + (th1 - th2(Yi))(ti+1 - ti) + (th3 - th4Yi)(Wi+1 - Wi)
from numpy.random import normal
from math import sqrt
import matplotlib.pyplot as plt

th1 = 1
th2 = 13
th3 = 2
th4 = 5

def eulerScheme(xi, N, T):
    dt = T/N
    x = []
    x.append(xi)
    # I found that sigma affects the range e.g. a sigma of 2 ~ a range of +- 2
    # theta impacts how quickly the variance occurs and the range to a lesser degree
    ou = ornsteinUhlenbeck(T, N, 3, 2, 0)
    for i in range(1, N):
        x.append(x[i - 1] + (th1 - th2*x[i-1])*dt + (th3 - th4*x[i-1])*(ou[i] - ou[i - 1]))
        #x.append(x[i - 1] + (th1 - th2*x[i-1])*dt + (th3)*(ou[i] - ou[i - 1]))
    return x


# Ornstein uhlenbeck is defined as the solution to dx = -(th)(xt)(dt) + sigma(dWt)
# Yi+1 = Yi - (th)(Xt)(ti+1-ti) + (sigma)(Wi+1 - Wi)
def ornsteinUhlenbeck(T,N, theta, sigma, initial):
    w = weinerProcess(T, N)
    dt = T/N
    ou = []
    ou.append(initial)
    for i in range(1, N):
        nextValue = (ou[i - 1] - theta*ou[i - 1]*dt + sigma*(w[i] - w[i-1]))
        ou.append(nextValue)
    return ou

def weinerProcess(T,N):
    w = []
    dt = T/N
    w.append(sqrt(dt) * normal())
    for i in range(1,N):
        dw = sqrt(dt) * normal()
        w.append(w[i - 1] + dw)
    return w

# Calculates the autocorrelation of the data
def autocorrelation(x, lag):
    mean = sum(x)/len(x)
    sumTop = 0
    sumBot = 0
    for i in range(len(x) - lag):
        sumTop += (x[i] - mean) * (x[i+lag] - mean)
    for i in range(len(x)):
        sumBot += ((x[i] - mean)**2)
    return sumTop / sumBot

def discard(x,t,n):
    del x[:n]
    del t[:n]
    print("The kurtosis is", kurtosis(x))
    print("The skewness is", skewness(x))
    print("The standard deviation is", stdev(x))
    print("The mean is",sum(x)/len(x))

    plt.plot(t,x)
    plt.xlabel("t (s)")
    plt.ylabel("Y")
    plt.savefig("process.png")
    plt.close()

# Calculates the central moment of order x
def centralMoment(input, order):
    moment = 0
    mean = sum(input)/len(input)
    for i in input:
        moment += (i - mean) ** order
    return moment / len(input)

def stdev(x):
    return sqrt(centralMoment(x, 2))

# Calculates the skewness using the central moments
def skewness(input):
    return centralMoment(input, 3) / (centralMoment(input, 2)**(1.5))

# Calculates the kurtosis using the central moments
def kurtosis(input):
    return centralMoment(input, 4) / (centralMoment(input, 2)**(2))


if __name__ == "__main__":
    T = 20
    N = T * 100
    x = eulerScheme(90, N, T)
    t = range(N)
    t = [i*(T/N) for i in t]
    print(autocorrelation(x, 300))
    autoX = range(N)
    autoY = []
    for i in range(N):
        autoY.append(autocorrelation(x,i))

    plt.plot(t, autoY, "-")
    plt.xlabel("lag (s)")
    plt.ylabel("autocorrelation")
    plt.savefig("autocorrelationfunction.png")
    plt.close()

    discard(x,t,50)