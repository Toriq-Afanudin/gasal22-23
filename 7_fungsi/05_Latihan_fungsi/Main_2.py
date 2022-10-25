import os


def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")


def input_user():
    panjang = int(input("Masukan panjang\t= "))
    lebar = int(input("Masukan lebar\t= "))
    luas = panjang*lebar
    keliling = 2*(panjang+lebar)
    print(f"{'-'*40:^40}")
    print(f"{'Luas persegi panjang':<25} = {luas}")
    print(f"{'Keliling persegi panjang':<25} = {keliling}")
    print(f"{'-'*40:^40}")


while True:
    header()
    input_user()
    lanjutkan = input("Apakah program akan dilanjutkan? (y/n)")
    if lanjutkan == "n":
        break
