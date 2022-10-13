# operator bitwise
a = 5
b = 8
c = a | b
# operator |
print(a, '=', format(a, '08b'))
print(b, '=', format(b, '08b'))
print('---------------(|)')
print(c, '=', format(c, '08b'))
print('\n')

# operator &
c = a & b
print(a, '=', format(a, '08b'))
print(b, '=', format(b, '08b'))
print('---------------(&)')
print(c, '=', format(c, '08b'))
print('\n')

# operator ^
c = a ^ b
print(a, '=', format(a, '08b'))
print(b, '=', format(b, '08b'))
print('---------------(^)')
print(c, '=', format(c, '08b'))
print('\n')

# operator ~
c = ~a+1
print(a, '=', format(a, '08b'))
print('---------------(~)')
print(c, '=', format(c, '08b'))
print('\n')

# shift right >> and shift left <<
c = a >> 2
d = a << 2
print(a, '=', format(a, '08b'))
print(a, 'geser kanan 2 kali =', c, format(c, '08b'))
print(a, 'geser kiri 2 kali =', d, format(d, '08b'))
