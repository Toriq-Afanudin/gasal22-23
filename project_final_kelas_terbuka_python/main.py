import os
import CRUD as CRUD

if __name__ == "__main__":

    # Check database itu ada atau tidak

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
        print("\n=========================\n")

        # CRUD.init_console()

        if user_option == "1":
            print("Read Data")
        elif user_option == "2":
            print("Create Data")
        elif user_option == "3":
            print("Update Data")
        elif user_option == "4":
            print("Delete Data")
        else:
            print("Opsi tidak ditemukan")

        print("\n=========================\n")
        is_done = input("Apakah program selesai (y/n)? ")
        if is_done == "y":
            break
