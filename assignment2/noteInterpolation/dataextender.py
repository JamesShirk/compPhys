import numpy as np

with open("dataextended.txt", "w+") as f:
    x = np.arange(-4, 5.1, .1)
    print(x)
    y = []
    for i in x:
        if ( i >= -1 and i <= 1):
            y.append(1)
        else:
            y.append(0)
    for i in range(0, len(x)):
        f.write(str(x[i]) + "," + str(y[i]) + "\n")