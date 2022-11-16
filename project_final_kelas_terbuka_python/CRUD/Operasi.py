from . import Database
from . import Util


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
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            return content
    except:
        print("gagal membaca data")
        list_kosong = []
        return list_kosong
