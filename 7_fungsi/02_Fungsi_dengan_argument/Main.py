def hello(nama):
    print(f"Hello word {nama}, selamat datang")


hello("Ucup")
hello("Otong")
hello("Asep")


def tambah(angka_1, angka_2):
    hasil = angka_1+angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")


tambah(1, 5)
tambah(7, 11)


def say_hi(list_peserta):
    for nama in list_peserta:
        print(f"Yang terhormat {nama}")


boyband = ["Ucup", "Otong", "Asep", "Dudung"]
say_hi(boyband)
mahasiswa = ["ardan", "alfika", "risza", "junaedi"]
say_hi(mahasiswa)
