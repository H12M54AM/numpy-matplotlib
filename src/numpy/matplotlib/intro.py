import matplotlib.pyplot as plt
import numpy as np
import random

num1 = random.randint(0, 100)
num2 = random.randint(100, 200)
num3 = random.randint(0, 100)
num4 = random.randint(100, 200)
# yrand = random.randint(0, 100)

xpoints = np.array([0, num1, num2])
ypoints = np.array([0, num3, num4])

plt.plot(xpoints, ypoints)
plt.show()