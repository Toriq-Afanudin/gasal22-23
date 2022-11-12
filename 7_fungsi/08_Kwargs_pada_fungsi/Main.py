"""**kwargs"""


def fungsi(nama, tinggi, berat):
    """fungsi biasa"""
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("ucup", 183, 79)


def fungsi_2(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi_2(nama="ucup", tinggi="183", berat="56")


def fungsi_3(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    if kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    return output


hasil_tambah = fungsi_3(1, 2, 3, 4, 5, 6, 7, 8, 9, option="tambah")
hasil_kali = fungsi_3(1, 2, 3, 4, 5, 6, 7, 8, 9, option="kali")
print(hasil_tambah)
print(hasil_kali)
