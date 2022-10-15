from copy import deepcopy
data_0 = [1, 2]
data_1 = [3, 4]
data = [data_0, data_1]
print(f'data\t\t= {data}')
print(f'data [0]\t= {data[0]}')
print(f'data [0][0]\t= {data[0][0]}')
print(f'data [0][1]\t= {data[0][1]}')
print(f'data [1][0]\t= {data[1][0]}\n')
data_copy = data.copy()
print(f'data copy = {data_copy}')
data_copy[0][0] = 5  # data asli juga ikut berubah
print(f'data asli = {data}')
print(f'data copy = {data_copy}\n')

data_deepcopy = deepcopy(data)
print(f'data asli\t= {data}')
print(f'data deepcopy\t= {data_deepcopy}\n')

data[0][0] = 10
print(f'data asli\t= {data}')
print(f'data deepcopy\t= {data_deepcopy}\n')
