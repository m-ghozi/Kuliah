a = 8
b = 32
print('a =', a, '=', format(a, '08b'))
print('b =', b, '=', format(b, '08b'), '\n')
print('-----AND-----')
print('a & b =', a & b)
print(format(a, '08b'), '&', format(b, '08b'), '=', format(a & b, '08b'), '\n')
print('-----OR-----')
print('a | b =', a | b)
print(format(a, '08b'), '|', format(b, '08b'), '=', format(a | b, '08b'), '\n')
print('-----XOR------')
print('a ^ b =', a ^ b)
print(format(a, '08b'), '^', format(b, '08b'), '=', format(a ^ b, '08b'), '\n')
print('-----NOT-----')
print('~a ~b =', ~a, ~b)
print('~' + format(a, '08b'), '~' + format(b, '08b'), '=', format(~a, '08b'),
format(~b, '08b'), '\n')
print('------shift right------')
print('a >> b =', a >> b)
print(format(a, '08b'), '>>', format(b, '08b'), '=', format(a >> b, '08b'), '\n')
print('-----shift left------')
print('b << a =', b << a)
print(format(b, '08b'), '<<', format(a, '08b'), '=', format(b << a, '08b'), '\n')
