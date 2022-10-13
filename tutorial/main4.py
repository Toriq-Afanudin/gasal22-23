# string
# menyambung string dan mengetahui panjang string
nama_lengkap = "Ayu Wahyuni"
print("panjang "+nama_lengkap+" adalah "+str(len(nama_lengkap)))

# mengecek keberadaan string
a = "Ay"
b = a in nama_lengkap
c = "Au"
d = c in nama_lengkap
e = a not in nama_lengkap
print("apakah "+a+" ada di "+nama_lengkap+" =", b)
print("apakah "+c+" ada di "+nama_lengkap+" =", d)
print("apakah "+a+" tidak ada di "+nama_lengkap+" =", e)

# mengulang string
print("wk"*10)

# indexing
print("index ke-0 dari "+nama_lengkap+" adalah ", nama_lengkap[0])
print("index ke-1 dari "+nama_lengkap+" adalah ", nama_lengkap[1])
print("index ke-2 dari "+nama_lengkap+" adalah ", nama_lengkap[2])
print("index ke-6 sampai 8 dari "+nama_lengkap+" adalah ", nama_lengkap[6:9])
print("index ke-[0,2,4,6,8] dari "+nama_lengkap +
      " adalah ", nama_lengkap[0:11:2])

# ASCII dan char
ascii_code = ord("a")
char_code = chr(117)
print("ASCII dari a adalah ", ascii_code)
print("ASCII minimal ", min(nama_lengkap))
print("ASCII maksimal ", max(nama_lengkap))
print("Char dari 117 adalah ", char_code)
