# Module matematika dengan import
from Matematika import tambah, pangkat
from Matematika import kali as k


hasil_tambah = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = k(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"hasil tambah = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"pangkat 3 dari 3 = {pangkat_3(3)}")
