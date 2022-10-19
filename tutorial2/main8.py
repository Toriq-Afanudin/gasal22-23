# operator dictionary
data_dict = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung'
}

# panjang dictionary
LENDICT = len(data_dict)
print(f'Panjang Dict: {LENDICT}')

KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f'{KEY} apakah ada di data: {CHECKKEY}')
KEY = 'kis'
CHECKKEY = KEY in data_dict
print(f'{KEY} apakah ada di data: {CHECKKEY}')
print(data_dict.get('cup'))
print(data_dict.get('kis'))
print(data_dict.get('kis', 'data tidak ditemukan'))
print(data_dict.get('cup', 'data tidak ditemukan'))

# update data
data_dict['cup'] = 'ucup si ganteng'
print(data_dict)
data_dict['sep'] = 'asep sukasep'
print(data_dict)
data_dict.update({'cup': 'ucup surucup'})
print(data_dict)
data_dict.update({'thor': 'thoriq afanudin'})
print(data_dict)

# menghapus data
del data_dict['thor']
print(data_dict)
