nama = []
nilai = []
program = True
while program:
    input_nama = input("Masukan nama\t: ")
    input_nilai = int(input("Masukan nilai\t: "))
    nama.append(input_nama)
    nilai.append(input_nilai)
    print(f"\n{'Nama':<10}| {'Nilai':<5}")
    print("-"*17)
    panjang = len(nama)
    for i in range(panjang):
        print(f"{nama[i]:<10}| {nilai[i]:<5}")
    print("\n")
    hentikan_program = input("Lanjutkan (y/n): ")
    if hentikan_program == "n":
        program = False
print("Program selesai")
