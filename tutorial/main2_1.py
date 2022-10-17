# membandingkan angka
input_1 = input('\ninput 1 = ')
input_2 = input('input 2 = ')
print('\nKesimpulan:')
if input_1 > input_2:
    print(f'input 1 ({input_1}) > input 2 ({input_2})')
elif input_2 > input_1:
    print(f'input 2 ({input_2}) > input 1 ({input_1})')
elif input_1 == input_2:
    print(f'input 1 ({input_1}) = input 2 ({input_2})\n')
print('Program selesai\n')
