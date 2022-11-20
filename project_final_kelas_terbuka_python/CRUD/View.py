from . import Operasi


def delete_console():
    data_file = Operasi.read()
    read_console()
    while True:
        nomer_data = int(input("Masukan nomer data yang akan anda hapus: "))
        panjang_data = len(data_file)
        if nomer_data < 1 or nomer_data > panjang_data:
            print("nomer yang anda masukan tidak ditemukan, silakan masukan ulang")
        else:
            break
    Operasi.delete(nomer_data - 1)


def update_console():
    data_file = Operasi.read()
    read_console()
    while True:
        nomer_data = int(input("Masukan nomer data yang akan di update: "))
        panjang_data = len(data_file)
        if nomer_data < 1 or nomer_data > panjang_data:
            print("nomer yang anda masukan tidak ditemukan, silakan masukan ulang")
        else:
            break

    data_break = data_file[nomer_data - 1].split(",")

    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][0:4]

    while True:
        print("\n" + "=" * 63)
        print("silahkan pilih data apa yang ingin anda rubah")
        print(f"1. Penulis\t: {penulis:.20}")
        print(f"2. Judul\t: {judul:.20}")
        print(f"3. Tahun\t: {tahun:4}")

        user_option = input("pilih data [1, 2, 3]: ")
        if user_option == "1":
            ubah = input("ubah penulis: ")
            penulis = ubah
        elif user_option == "2":
            ubah = input("ubah judul: ")
            judul = ubah
        elif user_option == "1":
            ubah = input("ubah tahun: ")
            tahun = ubah
        else:
            print("data yang anda masukan salah")

        selesai = input("apakah ada yang ingin diubah lagi (y/n)?")
        if selesai == "n":
            break

    Operasi.update(nomer_data, pk, date_add, penulis, judul, tahun)


def create_console():
    print("\n" + "=" * 63)
    print("\nsilahkan isi data buku baru:")
    penulis = input("penulis\t: ")
    judul = input("judul\t: ")
    while True:
        try:
            tahun = int(input("tahun\t: "))
            if len(str(tahun)) == 4:
                tahun_str = f"{tahun}"
                break
            else:
                print("tahun harus 4 digit")
        except:
            print("tahun harus berisi angka, silahkan masukan tahun lagi (yyyy)")

    Operasi.create(tahun_str, judul, penulis)
    print("berikut data baru anda:")
    read_console()


def read_console():
    data_file = Operasi.read()
    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"

    # Header
    print("\n" + "=" * 63)
    print(f"{index:4} | {penulis:15} | {judul:30} | {tahun:5}")
    print("-" * 63)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        print(
            f"{index+1:4} | {data_break[2]:.15} | {data_break[3]:.30} | {data_break[4]:5}",
            end="",
        )

    # Footer
    print("=" * 63 + "\n")
