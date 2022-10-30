import numpy as np
import os

os.system("cls")

dtipe = [("nama", "S10"), ("tinggi", int)]
data = [("Ucup", 170), ("Otong", 150), ("Mario", 180)]
a = np.array(data, dtype=dtipe)
print(a)
print(np.sort(a, order="nama"))
print(np.sort(a, order="tinggi"))
