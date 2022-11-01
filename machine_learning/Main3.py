import numpy as np
import os

os.system("cls")

matrix_A = np.array([(1, 1, -1), (-2, 0, 3)])
matrix_B = np.array([(1, 1), (3, 4), (0, -1)])
matrix_C = np.dot(matrix_A, matrix_B)
matrix_D = np.dot(matrix_B, matrix_A)


# Display
print(matrix_A)
print(matrix_B)
print(matrix_C)
print(matrix_D)
