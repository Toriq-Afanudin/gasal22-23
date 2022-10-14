# continue, pass, break
# pass
angka = 0
while angka < 5:
    print(f'thoriq ganteng {angka}')
    if angka == 3:
        pass
    else:
        print('maksimal')
    angka += 1
print('program selesai\n')

# continue
angka2 = 0
while angka2 < 5:
    angka2 += 1
    print(f'whatsappp --> {angka2}')
    if angka2 == 3:
        print('skippp')
        continue  # program dibawahnya akan di skipp
    print('lanjut')
print('program selesai\n')

# break
angka3 = 0
while angka3 < 5:
    print(f'looping ke-{angka3}')
    angka3 += 1
    if angka3 == 3:
        print('looping sudah mencapai 3')
        break
    print(f'looping belum mencapai 3')
print('program selesai')
