import os
import CRUD as CRUD

if __name__ == "__main__":
    os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    # Check database itu ada atau tidak
    CRUD.init_console()

    while True:
        # Membersihkan cmd saat program dijalankan
        os.system("cls")

        # Judul awal dan opsi
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")

        user_option = input("Masukan opsi: ")

        # CRUD.init_console()

        if user_option == "1":
            CRUD.read_console()
        elif user_option == "2":
            print("Create Data")
        elif user_option == "3":
            print("Update Data")
        elif user_option == "4":
            print("Delete Data")
        else:
            print("Opsi tidak ditemukan")

        is_done = input("Apakah program selesai (y/n)? ")
        if is_done == "y":
            break
