# Tugas kemarin

nama = input("Masukan nama\t:")
nilai = int(input("Masukan nilai\t:"))
if nilai <= 60:
    print(f"{nama} mendapat nilai = C")
    print(nama, "mendapat nilai C")
elif nilai <= 80:
    print(f"{nama} mendapat nilai = B")
elif nilai <= 100:
    print(f"{nama} mendapat nilai = A")
