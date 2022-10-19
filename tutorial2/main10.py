# copy dictionary
teman_teman = {
    "cup": "ucup surucup",
    "tong": "otong surotong",
    "dung": "dudung surudung",
    "sep": "asep sukasep"
}
friends = teman_teman.copy()
print(f'\nteman_teman\t= {teman_teman}\n')
print(f'friends\t\t= {friends}\n')
teman_teman["cup"] = "ucup si keren"
print(f'\nteman_teman\t= {teman_teman}\n')
print(f'friends\t\t= {friends}\n')

# pop() --> mengambil berdasarkan key
data_ucup = teman_teman.pop("cup")
print(f'\nteman_teman\t= {teman_teman}\n')
print(f'data ucup\t= {data_ucup}')

# popitem() --> mengambil data terakhir
data_terakhir = teman_teman.popitem()
print(f'\nteman_teman\t= {teman_teman}\n')
print(f'data_terakhir\t= {data_terakhir}')
