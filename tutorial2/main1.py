# fakta saat kita mengkopi data dengan cara a=b
a = ['Ucup', 'Otong', 'Ujang']
print(f'data a = {a}')
b = a
print(f'data b = {b}')
a[1] = 'Yusuf'
print(f'data a[1] diganti menjadi Yusuf =\n{a}')
print(f'data b[1] ikut berubah =\n{b}')
print('hal ini dikarenakan a dan b memiliki alamat yang sama')
print(f'alamat a = {hex(id(a))}')
print(f'alamat b = {hex(id(b))}')


# cara menduplikat data a.copy()
c = a.copy()
print(f'data a = {a} dengan alamat {hex(id(a))}')
print(f'data b = {b} dengan alamat {hex(id(b))}')
print(f'data c = {c} dengan alamat {hex(id(c))}\n')
c[1] = 'Maman'
print(f'data a = {a} dengan alamat {hex(id(a))}')
print(f'data b = {b} dengan alamat {hex(id(b))}')
print(f'data c = {c} dengan alamat {hex(id(c))}')
