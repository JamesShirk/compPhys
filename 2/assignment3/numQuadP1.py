from math import cos, pi
import numpy as np

def function(x):
    return (x * (cos(pi * x ) ** 2))

def simpson_nonuniform(x, f):
    N = len(x) - 1
    h = np.diff(x)

    result = 0.0
    for i in range(1, N, 2):
        hph = h[i] + h[i - 1]
        result += f[i] * ( h[i]**3 + h[i - 1]**3 + 3. * h[i] * h[i - 1] * hph ) / ( 6 * h[i] * h[i - 1] )
        result += f[i - 1] * ( 2. * h[i - 1]**3 - h[i]**3 + 3. * h[i] * h[i - 1]**2) / ( 6 * h[i - 1] * hph)
        result += f[i + 1] * ( 2. * h[i]**3 - h[i - 1]**3 + 3. * h[i - 1] * h[i]**2) / ( 6 * h[i] * hph )

    if (N + 1) % 2 == 0:
        result += f[N] * ( 2 * h[N - 1]**2 + 3. * h[N - 2] * h[N - 1]) / ( 6 * ( h[N - 2] + h[N - 1] ) )
        result += f[N - 1] * ( h[N - 1]**2 + 3*h[N - 1]* h[N - 2] ) / ( 6 * h[N - 2] )
        result -= f[N - 2] * h[N - 1]**3 / ( 6 * h[N - 2] * ( h[N - 2] + h[N - 1] ) )
    return result

if __name__ == "__main__":
    x = np.arange(0, 1, .0001)
    y = [function(i) for i in x]
    print(simpson_nonuniform(x, y))