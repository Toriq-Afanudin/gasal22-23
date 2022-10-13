# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# <,>,>=,<=,==,!=,is,is not
a = 4
b = 2
print(a, "apakah lebih besar dari 3?", a > 3)
print(a, "apakah lebih kecil dari 3?", a < 3)
print(b, "apakah lebih besar dari 3?", b > 3)
print(b, "apakah lebih kecil dari 3?", b < 3)

# komparasi dan logika
# ++++++++++3-----------10++++++++++
inputUser = float(input("Masukan angka kurang dari 3\natau\nlebih dari 10\n:"))
print(inputUser, "kurang dari 3?", inputUser < 3)
print(inputUser, "lebih dari 10?", inputUser > 10)
print(inputUser, "angka yang anda masukan", inputUser > 10 or inputUser < 3)

# ----------3+++++++++++10-----------
print(inputUser, "angka lebih dari 3 dan kurang dari 10",
      inputUser > 3 and inputUser < 10)
