# program input buku
buku_list = []
while True:
    judul = input('Masukan judul buku\t:')
    penulis = input('Masukan nama penulis\t:')
    buku = [judul, penulis]
    buku_list.append(buku)
    print('---------------------------')
    for index, buku in enumerate(buku_list):
        print(f'{index+1}. {buku[0]}\t{buku[1]}')
    print('\n')
    selesai = input('Apakah akan lanjut?(y/n)\t:')
    if selesai == 'n':
        break
    print('\n')
print('Program selesai')
