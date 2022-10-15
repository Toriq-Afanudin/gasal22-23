# list didalam list
list_0 = [0, 1, 2]
list_1 = [2, 3, 4]
list_gabungan = [list_0, list_1]
print(f'list_0 = {list_0}')
print(f'list_1 = {list_1}')
print(f'list_gabungan = {list_gabungan}')
list_gabungan = [list_0, list_1, 6, 7, 9]
print(f'list gabung dg angka = {list_gabungan}')

# contoh penggunaan
peserta_0 = ['Ucup', 24, 'Laki-laki']
peserta_1 = ['Otong', 35, 'Laki-laki']
peserta_2 = ['Dedeh', 55, 'Perempuan']
list_peserta = [peserta_0, peserta_1, peserta_2]
print(f'daftar peserta = {list_peserta}\n')

for i in list_peserta:
    print(f'nama\t: {i[0]}')
    print(f'umur\t: {i[1]}')
    print(f'gender\t: {i[2]}\n')
