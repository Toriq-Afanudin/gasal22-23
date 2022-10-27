import numpy as np

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

anp = np.array([1, 2, 3, 4, 5])
bnp = np.array([6, 7, 8, 9, 10])

# ELEMENTWISE operation
# Penjumlahan
hasil = a + b
hasil_2 = anp + bnp

# Pengurangan
hasil_3 = anp - bnp

# Perkalian
hasil_4 = anp * bnp

# Pembagian
hasil_5 = anp / bnp

# Multidimensi array numpy
c = np.array([(1, 2, 3), (3, 4, 5)])
d = np.array([(-1, -1, -1), (2, 2, 2)])
hasil_6 = c * d

# Display
print(hasil)
print(hasil_2)
print(hasil_3)
print(hasil_4)
print(hasil_5)
print(hasil_6)
