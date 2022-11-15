from . import Operasi


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
