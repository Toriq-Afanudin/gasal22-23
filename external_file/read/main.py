# Tutorial membaca text external


print("=" * 3, "Membaca file txt", "=" * 3)

file = open("data.txt", mode="r")

print(f"Status read : {file.readable()}")
print(f"Status write : {file.writable()}")

# Baca seluruh baris
# print(file.read())

# Baca perbaris
print(file.readline(), end="")
print(file.readline(), end="")

# Baca semua baris sebagai list
# print(file.readlines())

# Menutup file
print(f"Apakah file sudah di close : {file.closed}")
file.close()
print(f"Apakah file sudah di close : {file.closed}")

# Membaca file dengan with
print("=" * 3, "Membaca file dengan with", "=" * 3)

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"Apakah file sudah di close : {file.closed}")

print(f"Apakah file sudah di close : {file.closed}")
