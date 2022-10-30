import numpy as np
import os

os.system("cls")
a1 = np.array([1, -1, 2])
b1 = np.array([2, -3, 1])

# Perkalian dot
c1 = np.dot(a1, b1)
c2 = np.cross(a1, b1)
c3 = np.cross(b1, a1)

# Display
print(c1)
print(c2)
print(c3)
