# Looping dari list

# For loop
print("For loop")
kumpulan_angka = [3, 5, 2, 1, 4, 6, 2, 0, 2]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Ucup", "Otong", "Dadang", "Dudung", "Diding"]
for nama in peserta:
    print(f"nama = {nama}")

# For loop dan range
print("\nFor loop dan range")
data_angka = [4, 5, 2, 3, 1, 0, 0, 2, 3, 1]
panjang = len(data_angka)
for i in range(panjang):
    print(f"angka = {data_angka[i]}")

# While loop
print("\nWhile loop")
angka = [2, 1, 3, 0, 4, 3, 5, 2, 1, 2]
panjang = len(angka)
i = 0
while i < panjang:
    print(f"angka = {angka[i]}")
    i += 1

# List komprehension
print("\nList komprehension")
data_sembarang = ["ucup", 1, 2, 3, "otong"]
[print(f"data = {i}") for i in data_sembarang]
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka_kuadrat = [i**2 for i in angka]
print(f"angka kuadrat = {angka_kuadrat}")

# Enumerate
print("\nEnumerate")
data_nama = ["asep", "otong", "dadang", "ucup", "mario", "naruto"]
for index, data in enumerate(data_nama):
    print(f"index = {index}, data = {data}")
