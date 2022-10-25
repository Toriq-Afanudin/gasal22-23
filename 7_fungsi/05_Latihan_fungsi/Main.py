'''Latihan Fungsi'''
import os
# Program menghitung luas dan keliling
os.system("cls")
while True:
    # Membuat header program
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

    # Mengambil input user
    PANJANG = int(input("Masukan panjang\t= "))
    LEBAR = int(input("Masukan lebar\t= "))
    LUAS = PANJANG*LEBAR
    KELILING = 2*(PANJANG+LEBAR)
    print(f"Hasil perhitungan luas\t\t= {LUAS}")
    print(f"Hasil perhitungan keliling\t= {KELILING}")
    lanjut = input("Apakah program akan dilanjutkan? (y/n)")
    if lanjut == "n":
        break
print("Program selesai.")
