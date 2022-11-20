batas = int(input("masukan angka: "))


def faktorial(batas):
    print(f"{batas}!=", end="")
    hasil = 1
    for i in range(batas):
        if batas == 1:
            print(batas, end="")
            break
        print(batas, "x ", end="")
        hasil *= batas
        batas -= 1
    print("=", hasil)


faktorial(batas)
