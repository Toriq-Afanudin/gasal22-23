input_user = int(input("Masukana angka: "))
try:
    hasil = 10 / input_user
    print(f"hasil = {hasil}")
except Exception as error_message:
    print(f"Error: {error_message}")

input_user = int(input("Masukana angka: "))
try:
    hasil = 10 / input_user
    print(f"hasil = {hasil}")
except ZeroDivisionError as error_message:
    print(f"Error: {error_message}")
