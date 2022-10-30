import numpy as np
import os

os.system("cls")

# Membuat matrix dengan type data tertentu
a = np.array(([1, 2, 3], [4, 5, 6]), dtype=float)

# Membuat array dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2


def jumlah(baris, kolom):
    return baris + kolom


c = np.fromfunction(kuadrat, (1, 10), dtype=int)
b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
d = np.fromfunction(jumlah, (4, 4), dtype=float)

# Membuat array atau matrix dengan menggunakan iterable
iterable = (i * i for i in range(5))
e = np.fromiter(iterable, dtype=int)

# Multitype array
data = [("ucup", 150), ("otong", 160), ("mario", 180)]
dtipe = [("nama", "S255"), ("tinggi", int)]
f = np.array(data, dtype=dtipe)

# Display
print(f"float a = {a}")
print(f"b = {b}")
print(f"b**2 = {b**2}")
print(f"c = {c}")
print(f"d =\n{d}")
print(f"e = {e}")
print(f"data = {data}")
print(f"f = {f}")
