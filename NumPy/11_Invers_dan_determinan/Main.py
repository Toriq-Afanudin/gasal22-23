import numpy as np
import os

os.system("cls")
a = np.array([(1, -1), (-2, 3)])
print(f"a =\n{a}")

# Invers matrix
a_inv = np.linalg.inv(a)
print(f"a_inv =\n{a_inv}")
identity = np.dot(a, a_inv)
print(f"identity =\n{identity}")

# Determinan matrix
det_a = np.linalg.det(a)
print(f"det_a =\n{det_a}")
det_a_inv = np.linalg.det(a_inv)
print(f"det_a_inv =\n{det_a_inv}")
det_i = det_a * det_a_inv
print(det_i)
