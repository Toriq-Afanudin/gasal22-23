# Operaasi list
data_angka = [2, 3, 1, 0, 5, 6, 7, 3, 3, 2, 4, 5, 2, 1, 6, 0, 2, 3, 4, 3, 1]
print(f"data angka = {data_angka}")

# Count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# Ambil posisi data
data_nama = ["Ucup", "Otong", "Dudung", "Dadang", "Asep"]
print(data_nama)
index_dudung = data_nama.index("Dudung")
print(f"index si Dudung = {index_dudung}")
index_otong = data_nama.index("Otong")
print(f"index si Otong = {index_otong}")

# Mengurutkan data
print(f"data sebelum sorted = {data_angka}")
data_angka.sort()
print(f"data setelah sorted = {data_angka}")
print(f"data sebelum sorted = {data_nama}")
data_nama.sort()
print(f"data setelah sorted = {data_nama}")

# Balik listnya
data_angka.reverse()
print(f"data setelah reverse = {data_angka}")
data_nama.reverse()
print(f"data setelah reverse = {data_nama}")
