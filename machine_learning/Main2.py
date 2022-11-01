import numpy as np
import matplotlib.pyplot as plt
import os

os.system("cls")

data_x = np.random.randn(10000)
data_x.sort()
data_y = []
data_y_min = []


def fungsi_lingkaran(nilai_x):
    nilai_y = (4 - nilai_x**2) ** (1 / 2)
    data_y.append(nilai_y)
    data_y_min.append(nilai_y * (-1))


for i in data_x:
    fungsi_lingkaran(i)

plt.plot(data_x, data_y, "r")
plt.plot(data_x, data_y_min, "y")
plt.show()
