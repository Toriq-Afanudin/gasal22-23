# ---LIST---
# list numbers
list_angka = [0, 2, 3, 4, 5, 6, 54, 3, 9]
print(list_angka, "\n")

# list string
list_string = ['ucup', 'otong', 'abdul', 'khadir']
print(list_string, "\n")

# list float
list_float = [5.5, 2.4, 0.1, 9.2]
print(list_float, "\n")

# list boolean
list_boolean = [True, False, False, True]
print(list_boolean, "\n")

# list campuran
list_campuran = [9, 'ucup', True, 80, 'otong', False]
print(list_campuran, "\n")

# range
data_range = range(0, 10)
print(data_range, "\n")
data_list = list(data_range)
print(data_list, "\n")

# membuat list dengan for loop
list_pake_for = [i**2 for i in range(1, 11)]
print(list_pake_for, "\n")

# list pake for pake if
list_pake_for_if = [i for i in range(1, 11) if i % 2 == 1]
print(list_pake_for_if, "\n")
