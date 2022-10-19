# list --> array (mengakses dengan indeks)
data_list = ['ucup', 'otong', 'dudung']
print(data_list[0])

# dictionary (dict) --> associative array
# identifier --> key
data_dict = {
    'key': 'value',
    'cp': 'ucup',
    'tg': 'otong',
    'dg': 'dadang',
    'number': 100,
    'list': data_list
}
print(f'data dict = {data_dict}')
print(data_dict['tg'])
print(data_dict['number'])
print(data_dict['list'])
