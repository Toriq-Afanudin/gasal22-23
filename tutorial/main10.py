# Operasi
# index
data = ['ucup', 'otong', 'dudung']
print(f'list data = {data}\n')

# mengambil data dari list
data_0 = data[0]
print(f'data pertama adalah {data_0}\n')

# mengambil data terakhir
data_terakhir = data[-1]
print(f'data terakhir adalah {data_terakhir}\n')

# insert data
print(f'data sebelum ditambah {data}')
data.insert(1, 'asep')
print(f'data setelah ditambah {data}')

# menambahkan data di akhir
data.append('ujang')
print(f'data ditambahkan diakhir {data}')

# menggabungkan dua buah list
data_baru = ['nobita', 'naruto', 'sasuke']
data.extend(data_baru)
print(f'data gabungan {data}')

# meremove data
data.remove('nobita')
print(f'data remove {data}')

# meremove data paling akhir
data.pop()
print(f'menghilangkan data paling akhir {data}')
data_akhir = data.pop()
print(f'mengambil data akhir {data_akhir}')
