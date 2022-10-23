bilangan_1 = [i for i in range(1, 101)]
bilangan_2 = [i for i in range(1, 101)]
batas_bawah = 0
j = 0
k = 0
list_1 = []
list_2 = []
list_3 = []
inputan = int(input("Inputan yang di inginkan: "))
while batas_bawah < inputan**2:
    while j < inputan:
        bilangan_3 = bilangan_1[k]**2+bilangan_2[j]**2
        bilangan_4 = bilangan_3**(1/2)
        if bilangan_4-int(bilangan_4) == 0.0:
            bilangan_5 = int(bilangan_4)
            list_1.append(bilangan_1[k])
            list_2.append(bilangan_2[j])
            list_3.append(bilangan_5)
        j += 1
        batas_bawah += 1
    k += 1
    j = 0
list_4 = []
for i in range(len(list_3)):
    data_sementara = [list_1[i], list_2[i], list_3[i]]
    data_sementara.sort()
    keberadaan_data = list_4.count(data_sementara)
    if keberadaan_data == 0:
        list_4.append(data_sementara)
print(
    f"Daftar Bilangan Triple Pythagoras [a, b, c] dengan a, b kurang dari samadengan {inputan}:\n{list_4}")
