import os
os.system("cls")
print("="*30)
print("SELAMAT DATANG DI PROGRAM")
print("PENDAFTARAN LES BIMBEL")
print("="*30)
print("Jenis Les")
print("1. Private\n2. Klasikal\n")
opsiLes=input("Opsi les: ")
print("="*30)
if opsiLes=="2":
    jumlahSiswa=int(input("Jumlah siswa: "))
else:
    jumlahSiswa=1
dataSiswa=[]
for i in range(jumlahSiswa):
    namaSiswa=input(f"Nama siswa {i+1}: ")
    dataSiswa.append(namaSiswa)
print("="*30)
jumlahHari=int(input("Jumlah hari: "))
print("="*30)
print("Daftar hari\n1. Senin\n2. Selasa\n3. Rabu\n4. Kamis\n5. Jumat\n6. Sabtu\n7. Minggu\n")
dataHari=[]
dataBiaya=[]
for i in range(jumlahHari):
    opsiHari=input(f"Pilih hari {i+1}: ")
    if opsiHari=="1":
        hari="Senin"
        biaya=50000
    elif opsiHari=="2":
        hari="Selasa"
        biaya=50000
    elif opsiHari=="3":
        hari="Rabu"
        biaya=50000
    elif opsiHari=="4":
        hari="kamis"
        biaya=60000
    elif opsiHari=="5":
        hari="Jumat"
        biaya=60000
    elif opsiHari=="6":
        hari="Sabtu"
        biaya=70000
    else:
        hari="Minggu"
        biaya=70000
    dataHari.append(hari)
    dataBiaya.append(biaya)
print("="*30)
print("NOTA PEMBAYARAN")
print("="*30)
if opsiLes=="2":
    jenisLes="Klasikal"
else:
    jenisLes="Private"
print(f"Jenis Les\t: {jenisLes}")
print(f"Daftar siswa\t: {dataSiswa}")
print(f"Daftar hari\t: {dataHari}")
print(f"Daftar biaya\t: {dataBiaya}")
totalBiaya=sum(dataBiaya)*jumlahSiswa*jumlahHari
print(f"Total biaya\t: Rp. {totalBiaya}")
if jumlahSiswa==3:
    diskon=0.03
elif jumlahSiswa>=4:
    diskon=0.07
dapetDiskon=totalBiaya*diskon
totalPembayaran=totalBiaya-dapetDiskon
print(f"Diskon\t\t: Rp. {int(dapetDiskon)}")
print(f"Pembayaran\t: Rp. {int(totalPembayaran)}")
print("="*30)