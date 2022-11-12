"""lambda function"""


def f_kuadrat(angka):
    return angka**2


print(f"fungsi kuadrat biasa = {f_kuadrat(3)}")
kuadrat = lambda angka: angka**2
print(f"fungsi kuadrat lambda = {kuadrat(5)}")
# pangkat = lambda num, pow: num**pow
# print(f"hasil lambda pangkat = {pangkat(4,3)}")

data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(data_genap)

data_ganjil = list(filter(lambda x: (x % 2 != 0), data_angka))
print(data_ganjil)

data_3 = list(filter(lambda x: (x % 3 == 0), data_angka))
print(data_3)


def pangkat(n):
    return lambda angka: angka**n


pangkat_2 = pangkat(2)
print(f"pangkat 2 dari 5 = {pangkat_2(5)}")
pangkat_3 = pangkat(3)
print(f"pangkat 3 dari 6 = {pangkat_3(6)}")
print(f"pangkat sembarang = {pangkat(4)(5)}")
