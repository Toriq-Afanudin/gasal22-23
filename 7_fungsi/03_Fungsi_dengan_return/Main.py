'''Fungsi dengan kembalian'''
# Template fungsi dengan kembalian
# daf nama_fungsi(argument):
#       badan_fungsi
#       return output

# fungsi kuadrat


def kuadrat(angka):
    output = angka**2
    return output


y = kuadrat(3)
print(f"y = {y}")

# Fungsi dengan banyak return


def operasi_matematika(angka_1, angka_2):
    jumlah = angka_1+angka_2
    kurang = angka_1-angka_2
    kali = angka_1*angka_2
    bagi = angka_1/angka_2
    return jumlah, kurang, kali, bagi


bilangan_1 = int(input("Bilangan_1 = "))
bilangan_2 = int(input("Bilangan_2 = "))
k, l, m, n = operasi_matematika(bilangan_1, bilangan_2)
print(f"{bilangan_1} + {bilangan_2} = {k}")
print(f"{bilangan_1} - {bilangan_2} = {l}")
print(f"{bilangan_1} * {bilangan_2} = {m}")
print(f"{bilangan_1} / {bilangan_2} = {n}")
