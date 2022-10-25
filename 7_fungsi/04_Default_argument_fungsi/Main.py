'''Default argument'''
# def fungsi(argument)
# def fungsi(argument = nilai defaultnya):


def say_hello(nama="Ganteng"):
    print(f"Hallo {nama}")


say_hello("Ucup")
say_hello()

# Fungsi dengan satu input, dan satu default argument


def sapa_dia(nama, pesan="Apa kabar?"):
    print(f"Hai {nama}, {pesan}")


sapa_dia("Dudung")


def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil


print(hitung_pangkat(2, 3))
# Mencantumkan argument saat menggunakan fungsi
hasil_perhitungan = hitung_pangkat(pangkat=8, angka=2)
print(hasil_perhitungan)


def perhitungan(input1=1, input2=2, input3=3, input4=4):
    hasil = input1+input2+input3+input4
    return hasil


print(perhitungan())
print(perhitungan(input3=10))
