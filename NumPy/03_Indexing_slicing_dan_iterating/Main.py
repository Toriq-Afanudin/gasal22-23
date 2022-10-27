import numpy as np

a = np.arange(10) ** 2
print(a)

# Mengambil nilai
print(f"Elemen ke 1 dari a adalah {a[0]}")
print(f"Elemen ke 7 dari a adalah {a[6]}")
print(f"Elemen terakhir dari a adalah {a[-1]}")

# Slicing
print(f"Elemen dari 1-6 adalah {a[0:6]}")
print(f"Elemen dari 4 sampai akhir {a[3:]}")
print(f"Elemen dari awal sampai 5 adalah {a[:5]}")

# Iterasi
for i in a:
    print(f"Value = {i}")