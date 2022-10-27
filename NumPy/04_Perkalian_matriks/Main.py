import numpy as np

a = np.array([(1, 2), (3, 4), (2, 1)])
b = np.array([(1, 1, 1), (1, 2, 0)])
print(f"Matriks a =\n{a}")
print(f"Matriks b =\n{b}")
c_1 = np.dot(a, b)  # Cara 1
c_2 = a.dot(b)  # Cara 2
print(f"a dot b =\n{c_1}\n{c_2}")
