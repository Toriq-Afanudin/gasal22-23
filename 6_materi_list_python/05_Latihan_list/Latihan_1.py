# Latihan list

# Nilai siswa
nama_siswa = ["Nafis", "Hafis", "Bela", "Rifa",
              "Dira", "Adel", "Alfika", "Ardan", "Risza", "Tito"]
nilai_ulangan = [80, 70, 77, 90, 76, 64, 100, 95, 50, 85]
nilai_UTS = [55, 60, 80, 82, 70, 77, 90, 99, 100, 90]
nilai_UAS = [96, 80, 80, 80, 100, 100, 60, 70, 89, 79]


print("\n")
print(f"{'Daftar Nilai Siswa':^29}")
print("-"*29)
print(f"{'Nama':<10}| {'NU':<4}| {'UTS':<4}| {'UAS':<4}|")
print("-"*29)
panjang = len(nama_siswa)
for i in range(panjang):
    print(
        f"{nama_siswa[i]:<10}| {nilai_ulangan[i]:<4}| {nilai_UTS[i]:<4}| {nilai_UAS[i]:<4}|")
print("\n")
