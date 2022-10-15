# looping list
# menggunakan for in
kumpulan_angka = [3, 5, 6, 2, 4, 1, 9, 8, 0]
for angka in kumpulan_angka:
    print(f'angka = {angka}')
print('\n')

peserta = ['Ucup', 'Otong', 'Dadang', 'Dudung']
for nama in peserta:
    print(f'nama = {nama}')
print('\n')

# menggunakan range
panjang = len(peserta)
for i in range(panjang):
    print(f'nama = {peserta[i]}')
print('\n')

# menggunakan while loop
i = 0
while i < panjang:
    print(f'nama = {peserta[i]}')
    i += 1
print('\n')

# list komprehensif
data = ['ucup', 1, 3, 5, 'otong']
[print(f'data = {i}') for i in data]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kuadrat = [i**2 for i in numbers]
print(f'kuadrat = {kuadrat}')

for index, data in enumerate(data):
    print(f'index = {index}, data = {data}')
