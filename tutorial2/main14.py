data_angka = [i for i in range(1, 11)]
print(f"data angka\t= {data_angka}")
data_kuadrat = [i**2 for i in range(1, 11)]
print(f"data kuadrat\t= {data_kuadrat}")
data_kubik = [i**3 for i in range(1, 11)]
print(f"data kubik\t= {data_kubik}")
print("-"*65)
print(f"{'BILANGAN BERPANGKAT':^34}")
print("-"*65)
print(f'{"Pangkat 1":<10}| {"Pangkat 2":<10}| {"Pangkat 3":<10}')
for j in range(10):
    print(f"{data_angka[j]:<10}| {data_kuadrat[j]:<10}| {data_kubik[j]:<10}")
