mahasiswa1 = {
    'nama': 'Ucup Surucup',
    'nim': '1900006105',
    'sks': 140,
    'beasiswa': False,
}

mahasiswa2 = {
    'nama': 'Otong Surotong',
    'nim': '1900006106',
    'sks': 144,
    'beasiswa': True,
}

mahasiswa3 = {
    'nama': 'Asep Sikasyep',
    'nim': '1900006107',
    'sks': 130,
    'beasiswa': False,
}

mahasiswa4 = {
    'nama': 'Dudung Durudung',
    'nim': '1900006108',
    'sks': 132,
    'beasiswa': False,
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
    'MAH004': mahasiswa4,
}

print(f"{'KEY':<7}{'NAMA':<17}{'NIM':<12}{'SKS':<4}{'BEASISWA':<8}")
print("-"*50)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    print(f"{KEY:<7}{NAMA:<17}{NIM:<12}{SKS:<4}{BEASISWA:<8}")
