import numpy as np
import os

os.system("cls")

a = np.floor(np.random.randn(2, 2))
print(f"a = {a}")
print(f"Nilai max dari a = {a.max()}")
print(f"Posisi max dari a = {a.argmax()}")
print(f"Nilai min dari a = {a.min()}")
print(f"Posisi min dari a = {a.argmin()}")
print(f"Mengurutkan nilai a = {np.sort(a)}")
print(f"Mengurutkan a berdasarkan arg = {np.argsort(a)}")
