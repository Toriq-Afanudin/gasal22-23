from . import Operasi

DB_NAME = "data.txt"

TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "penulis": 255 * " ",
    "judul": 255 * " ",
    "tahun": "yyyy",
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("database tersedia, init done!")
    except:
        print("database tidak tersedia, silahkan membuat database baru!")
        with open(DB_NAME, "w", encoding="utf-8") as file:
            Operasi.create_firts_data()
