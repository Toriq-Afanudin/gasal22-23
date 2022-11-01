import numpy as np
import matplotlib.pyplot as plt

diameter = 1
x_awal = -1 * diameter / 2
x_akhir = diameter / 2
data_x = [x_awal]

while True:
    x_awal += 0.125
    data_x.append(x_awal)
    if x_awal >= x_akhir:
        break

data_y = []
data_y_min = []
data_x_min = []
for i in data_x:
    nilai_y = (diameter / 2 - i) ** (1 / 2)
    data_y.append(nilai_y)
    data_y_min.append(-nilai_y)
    data_x_min.append(-i)

plt.plot(data_x, data_y, "r")
plt.scatter(data_x, data_y)
plt.plot(data_x, data_y_min, "r")
plt.scatter(data_x, data_y_min)
plt.plot(data_x_min, data_y_min, "r")
plt.scatter(data_x_min, data_y_min)
plt.plot(data_x_min, data_y, "r")
plt.scatter(data_x_min, data_y)
plt.show()
