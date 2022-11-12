# 1. Mode write
# Dia akan membuat file baru jika tidak ada,
# Lalu akan menimpa atau overwrite isinya
with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Jhon si Jhoni")

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Ucup surucup")

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Otong surotong")

# 2. Mode append
with open("data_2.txt", "w", encoding="utf-8") as file:
    file.write("Jhon si Jhoni\n")

with open("data_2.txt", "a", encoding="utf-8") as file:
    file.write("Ucup surucup\n")

with open("data_2.txt", "a", encoding="utf-8") as file:
    file.write("Otong surotong\n")


# 3. Mode r+
with open("data_3.txt", "w", encoding="utf-8") as file:
    file.write("Jhon si Jhoni\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")
    file.write("baris ke-3\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris ke-4\n")  # Menimpa isi text sesuai panjang data
