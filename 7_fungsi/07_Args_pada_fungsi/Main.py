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
