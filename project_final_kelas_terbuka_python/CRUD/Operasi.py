from . import Database
from . import Util


def create_firts_data():
    penulis = input("penulis: ")
    judul = input("judul: ")
    tahun = input("tahun: ")

    data = Database.TEMPLATE.copy()

    data["pk"] = Util.random_string(6)
    data["date_add"] = Util.waktu()
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = tahun

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
