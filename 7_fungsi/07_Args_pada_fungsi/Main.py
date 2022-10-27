'''*args'''

# Memasukan data/argument


def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("Ucup", 170, 40)


def fungsi_2(data_list):
    nama = data_list[0]
    tinggi = data_list[1]
    berat = data_list[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi_2(["Otong", 160, 50])


def fungsi_3(*data_list):
    nama = data_list[0]
    tinggi = data_list[1]
    berat = data_list[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi_3("Asep", 165, 55)


def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    print(f"Hasil penjumlahan = {output}")


tambah(1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7, 4, 3)
tambah(2, 4, 3, 5, 3, 2, 1, 2, 3, 2, 3, 2, 3, 2,
       2, 1, 2, 3, 6, 5, 3, 2, 3, 4, 5, 3, 2, 2)
masukan = list(input("Masukan : "))
data_int = []
for i in masukan:
    data = int(i)
    data_int.append(data)
print(data_int)
tambah(data_int)
