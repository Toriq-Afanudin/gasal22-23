# perulangan (loop)

# menggunakan list
angka2 = [0, 3, 2, 5, 10]
for i in angka2:
    print("i sekarang --> ", i)
print("akhir dari program\n")

# menggunakan range
for i in range(5):
    print("i sekarang --> ", i)
print("akhir dari program\n")

# range menggunakan batas tidak = 0
for i in range(1, 5):
    print("i sekarang --> ", i)
print("akhir dari program\n")

# menggunakan string
huruf = "saya suka makan"
for i in huruf:
    print("i sekarang --> ", i)
print("akhir dari program\n")

# while loop
angka = 0
while angka < 5:
    print('Thoriq kece')
    print(f'angka sekarang --> {angka}')
    angka += 1
print('cukup')
