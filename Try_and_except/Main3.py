while True:
    try:
        with open("data.txt", "r") as file:
            print("Membaca isi data.txt")
            print(file.read())
        break
    except:
        print("file data.txt tidak ditemukan, membuat file baru")
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write("file baru")
        break

print("akhir dari program")
