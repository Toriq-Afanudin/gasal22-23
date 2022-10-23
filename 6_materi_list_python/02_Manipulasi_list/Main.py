# Operasi

# Index  0 (-3)   1 (-2)   2 (-1)
data = ["Ucup", "Otong", "Dudung", "Asep"]

# Mengambil data dari list ini
data_0 = data[0]
print(f"Data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_otong = data[1]
print(f"data otong adalah {data_otong}")

# Mengambil info jumlah data pada list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi data list

# Menambahkan item pada list sesuai posisi
print(f"Data sebelum ditembah = {data}")
data.insert(2, "Dadang")
print(f"Data ditambah ditengah = {data}")

# Menambahkan item pada list diakhir
data.append("Jono")
print(f"Data ditambah diakhir = {data}")

# Menambahkan list dengan list
data_baru = ["Ujang", "Bela", "Rifa"]
print(f"data baru = {data_baru}")
data.extend(data_baru)
print(f"data gabungan = {data}")

# Merubah data
# Kita ubah data 2 menjadi Micheal
data[2] = "Micheal"
print(f"Ubah data[2] = {data}")

# Meremove data
data.remove("Bela")  # Nanti dicontohkan yang error
print(f"Data remove = {data}")

# Meremove data paling belakang
data.pop()
print(f"remove paling belakang = {data}")

# Mengambil data akhir
data_akhir = data.pop()
print(f"ambil data akhir = {data_akhir}")
