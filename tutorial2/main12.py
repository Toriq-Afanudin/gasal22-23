# menentukan sebuah bilangan prima atau bukan
bilangan = int(input("Masukan sembarang = "))
pembagi = 2
for i in range(pembagi, bilangan):
    if bilangan % pembagi == 0:
        print(f'{bilangan} bukan prima')
        break
    else:
        pembagi += 1
        if pembagi == bilangan:
            print(f'{bilangan} adalah prima')
