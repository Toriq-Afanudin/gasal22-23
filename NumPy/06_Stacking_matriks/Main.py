import numpy as np

a = np.array([1, 2, 3])
b = np.array([6, 5, 4])
print(f"a = {a}\nb = {b}")

c = np.hstack((a, b))
d = np.vstack((a, b))
print(f"Horizontal stack =\n{c}")
print(f"Vertikal stack =\n{d}")

matriks_0 = np.zeros((2, 3))
matriks_1 = np.ones((2, 3))
print(f"Matriks 0 =\n{matriks_0}")
print(f"Matriks 1 =\n{matriks_1}")

gabung_horizontal = np.hstack((matriks_0, matriks_1))
gabung_vertikal = np.vstack((matriks_0, matriks_1))
print(f"Gabung vertikal =\n{gabung_vertikal}")
print(f"Gabung horizontal =\n{gabung_horizontal}")

# Saat penggabungan matriks secara vertikal, maka jumlah kolomnya harus sama
# Saat penggabungan matriks secara horizontal, maka jumlah barisnya harus sama
