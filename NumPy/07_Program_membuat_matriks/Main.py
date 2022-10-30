import numpy as np
import os

os.system("cls")

jumlah_baris = int(input("Jumlah baris: "))
jumlah_kolom = int(input("Jumlah kolom: "))
satu_matriks = []
for i in range(jumlah_baris):
    satu_baris = []
    for j in range(jumlah_kolom):
        inputan = int(input(f"Masukan nilai baris ke-{i+1} kolom ke-{j+1}: "))
        satu_baris.append(inputan)
    satu_matriks.append(satu_baris)
print(satu_matriks)
hasil_matriks = np.vstack(satu_matriks)
print(f"Hasil Matriks =\n{hasil_matriks}")
