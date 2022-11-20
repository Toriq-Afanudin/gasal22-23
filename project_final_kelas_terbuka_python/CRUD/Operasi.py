from . import Database
from . import Util
from . import View


def delete(index):
    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(550 * index)
            data_hapus = file.readline()
            data_break = data_hapus.split(",")

            print(f"\nPenulis\t: {data_break[2][0:20]}")
            print(f"Judul\t: {data_break[3][0:20]}")
            print(f"Tahun\t: {data_break[4]}")
            hapus_data = input(
                "apakah anda yakin akan menghapus data tersebut (y/n) ? "
            )

            if hapus_data == "y" or hapus_data == "Y":

                pass
    except:
        print("error")
    pass


def update(nomer_data, pk, date_add, penulis, judul, tahun):
    data = Database.TEMPLATE.copy()
    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(550 * (nomer_data - 1))
            file.write(data_str)
        View.read_console()
    except:
        print("error")


def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = Util.random_string(6)
    data["date_add"] = Util.waktu()
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = tahun

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("dahlah, kalo gagaaaal")


def create_firts_data():
    penulis = input("penulis: ")
    judul = input("judul: ")

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

    data = Database.TEMPLATE.copy()

    data["pk"] = Util.random_string(6)
    data["date_add"] = Util.waktu()
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = tahun_str

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("dahlah, kalo gagaaaal")


def read():
    with open(Database.DB_NAME, "r") as file:
        content = file.readlines()
        return content
