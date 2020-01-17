import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
nMasses = [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40]
print(len(nMasses))
timeTaken = [.01170206069946289, 0.017492055892944336, 0.05964016914367676, 0.09692502021789551, 0.16785430908203125, 0.16312503814697266, 0.24422049522399902, 0.2961282730102539, 0.21789836883544922, 0.8810455799102783, 1.221785306930542, 5.307999610900879, 8.564101934432983, 7.5314106941223145, 16.072021007537842]
z = np.polyfit(nMasses, timeTaken, 3)
p = np.poly1d(z)
x = np.linspace(2, 40, 1000)
y = [p(i) for i in x]
plt.plot(nMasses, timeTaken, "o", x, y)
chi_squared = 0
for i in range(0, len(nMasses)):
    chi_squared += ((timeTaken[i] - p(nMasses[i])) ** 2) / p(nMasses[i])
print("Chi squared is ", chi_squared)
plt.xlabel("Number of Masses")
plt.ylabel("Time Taken (seconds)")
plt.text(6, 10, "$\chi^2$ = " + str(round(chi_squared, 5)))
plt.title("Number of Masses versus Time Taken")
plt.savefig("timecomplexity.png", dpi = 300)
plt.close()