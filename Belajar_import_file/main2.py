import numpy as np
import matplotlib.pyplot as plt

# Generate data
jumlah_data = 100
y = [i * 0.1 + np.random.randn() for i in range(jumlah_data)]
x = [i * 0.1 for i in range(jumlah_data)]

# prediksi
def persamaan_linear(x, gradien):
    y = gradien * x
    return y


x_prediksi = np.array([0, 100])
m_awal = 5
m_prediksi = m_awal
m_list = []
y_list = []
x_list = []

for i in range(1, jumlah_data):
    y_prediksi = persamaan_linear(x[i], m_prediksi)
    y_actual = y[i]
    error = y_actual - y_prediksi
    delta_m = error / x[i]
    m_prediksi += delta_m
    m_list.append(m_prediksi)
    y_list.append(m_prediksi)
    x_list.append(x[i])

# Plot data
plt.plot(x_list, y_list, "r")
plt.scatter(x, y)
plt.show()
