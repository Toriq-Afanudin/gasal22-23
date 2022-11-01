import numpy as np
import matplotlib.pyplot as plt
import os

os.system("cls")

data_x = np.random.randn(1000)

data_x.sort()
data_y = []
data_y2 = []
data_y3 = []


def fungsi_kuadrat(nilai_x):
    nilai_y = nilai_x**2
    nilai_y2 = nilai_x**2 + 5
    nilai_y3 = nilai_x**3
    data_y.append(nilai_y)
    data_y2.append(nilai_y2)
    data_y3.append(nilai_y3)


for i in data_x:
    fungsi_kuadrat(i)
plt.plot(data_x, data_y, "y--")
plt.plot(data_x, data_y2, "r-.")
plt.plot(data_x, data_y3, "g")
plt.show()
