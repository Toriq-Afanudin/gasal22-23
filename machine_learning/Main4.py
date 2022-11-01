import numpy as np
import matplotlib.pyplot as plt

data_x = np.random.randn(1000)
data_x.sort()
data_y = []


def fungsi(nilai_x):
    nilai_y = (nilai_x**2) - nilai_x - 6
    data_y.append(nilai_y)


for i in data_x:
    fungsi(i)

plt.plot(data_x, data_y)
plt.show()
