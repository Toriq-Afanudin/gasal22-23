import numpy as np
import matplotlib.pyplot as plt

data_x = np.random.randn(1000)
data_x.sort()
data_y1 = []
data_y2 = []


def fungsi(nilai_x):
    nilai_y1 = (nilai_x**2) - nilai_x - 6
    nilai_y2 = (nilai_x**2) - nilai_x - 4
    data_y1.append(nilai_y1)
    data_y2.append(nilai_y2)


# Mencari nilai y
for i in data_x:
    fungsi(i)

# Ploting data
plot_1 = plt.plot(data_x, data_y1)
plot_2 = plt.plot(data_x, data_y2)

# Set properti
plt.setp(plot_1, color="r", linestyle="--", linewidth=1)
plt.setp(plot_2, color="b", linestyle="-.", linewidth=2)

# Setting axis
plt.axis([-3, 4, -7, 10])

# Menampilkan data
plt.show()
