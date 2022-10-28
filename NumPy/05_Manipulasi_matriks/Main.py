import numpy as np
import os

os.system("cls")

a = np.array([(1, 2, 3), (1, -1, 0)])
print(f"Matiks a =\n{a}")
b = a.transpose()  # --> Cara 1
# np.transpose(a) --> Cara 2
print(f"\nTranspose matriks a =\n{b}")
# print(f"\nTranspose matriks a =\n{a.T}") --> Cara 3

# Flatten array, vector baris
print(f"Flatten matriks a = {a.ravel()}")
print(f"Flatten matriks a = {np.ravel(a)}")

# Reshape matriks
print(f"Reshape matriks a =\n{a.reshape(3,2)}")
print(f"Matriks a =\n{a}")
a.resize(3, 2)
print(f"Resize matriks a =\n{a}")
