while True:
    angka = int(input("Masukan angka: "))
    try:
        hasil = 10 / angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n":
            break
    except:
        print("Pembagi nol, silakan masukan input lagi.")

print("Akhir dari program")
