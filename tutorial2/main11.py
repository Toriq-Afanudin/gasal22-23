# membuat barisan fibonacci
a_1 = 0
a_2 = 1
batas_bawah = 0
batas_atas = int(input('Berapa bilangan = '))
list_bil = []
while batas_bawah < batas_atas:
    a_3 = a_1+a_2
    list_bil.append(a_3)
    a_1 = a_2
    a_2 = a_3
    batas_bawah += 1
print(f'Barisan Fibonacci = {list_bil}')
