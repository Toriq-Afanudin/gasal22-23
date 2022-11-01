import numpy as np
import matplotlib.pyplot as plt
import os

os.system("cls")

data_x = np.random.randn(100)
data_x.sort()
data_y = []
data_y_min = []


def fungsi_lingkaran(nilai_x):
    nilai_y = (4 - nilai_x**2) ** (1 / 2)
    data_y.append(nilai_y)
    data_y_min.append(nilai_y * (-1))


for i in data_x:
    fungsi_lingkaran(i)

"""plt.plot(data_x, data_y)
plt.plot(data_x, data_y_min)"""
plot_3 = plt.scatter(data_x, data_y)
plot_4 = plt.scatter(data_x, data_y_min)

plt.setp(plot_3, color="r", linewidth=0.025)
plt.setp(plot_4, color="b", linewidth=2)

plt.axis([-2, 2, -2, 2])
plt.show()
