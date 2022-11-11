from numbers import Number

# input_1 = input("Masukan sembarang: ")
# input_2 = int(input("Masukan angka: "))
# print(f"{input_1} = {isinstance(input_1,Number)}")
# print(f"{input_2} = {isinstance(input_2,Number)}")


def penjumlahan(a, b):
    if isinstance(a, Number):
        print("inputan sudah benar:")
        hasil = a + b
        return hasil
    else:
        print("\ninputan harus berupa number:")
        hasil = None
        return hasil


print(f"hasil 1 = {penjumlahan(2,3)}")
print(f"hasil 2 = {penjumlahan('aku','kamu')}")
