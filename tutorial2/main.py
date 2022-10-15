# menghitung jumlah data tertentu
data_angka = [1, 3, 2, 4, 5, 7, 3, 4, 5, 6, 9, 1, 2, 0, 3, 3, 3]
hitung_data_4 = data_angka.count(4)
hitung_data_3 = data_angka.count(3)
print(f'jumlah data 4 = {hitung_data_4}')
print(f'jumlah data 3 = {hitung_data_3}')

# mengetahui index suatu data (posisi)
data = ['Ucup', 'Otong', 'Ujang']
index_data_ucup = data.index('Ucup')
index_data_otong = data.index('Otong')
print(f'index data ucup = {index_data_ucup}')
print(f'index data otong = {index_data_otong}')

# mengurutkan data
print(f'data sebelum diurutkan = {data_angka}')
data_angka.sort()
print(f'data setelah diurutkan = {data_angka}')
data_angka.reverse()
print(f'data setelah direverse = {data_angka}\n')
print(f'data sebelum diurutkan = {data}')
data.sort()
print(f'data setelah diurutkan = {data}')
