# --- LIST ---

# Kumpulan data numbers
data_angka = [2, 3, 5, 7, 3, 1, 0, 9, 4]
print(data_angka)

# Kumpulan data floats
data_float = [2.3, 4.5, 1.1, 0.9, 5.2]
print(data_float)

# Kumpulan data strings
data_string = ["Ucup", "Otong", "Dadang", "Dudung"]
print(data_string)

# Kumpulan data booleans
data_boolean = [True, False, False, False, True]
print(data_boolean)

# Kumpulan data campuan
data_campuran = [2, "Ucup", 4.8, False, "Otong", True]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0, 10, 2)  # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list pake for loop, list comprehention
list_pake_for = [i for i in range(1, 11)]
print(list_pake_for)
list_pake_for_2 = [i**2 for i in range(1, 11)]
print(list_pake_for_2)

# Membuat list pake for pake if
list_pake_for_if = [i for i in range(1, 11) if i % 2 == 0]
print(list_pake_for_if)
list_pake_for_if = [i for i in range(1, 11) if i % 2 == 1]
print(list_pake_for_if)
