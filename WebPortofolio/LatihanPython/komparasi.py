#OPERASI KOMPARASI

print('===KOMPARASI===')
a = 6
b = 9
c = a is b

print(a, '>', b,'  = ', a > b)
print(a, '<', b,'  = ', a < b)
print(a, '>=', b,' = ', a >= b)
print(a, '<=', b,' = ', a <= b)
print(a, '!=', b,' = ', a != b)
print(a, '==', b,' = ', a == b)
print(a, 'is', b,' = ', c)

#NOT, OR, AND, XOR
#DLM BENTUK BOOLEAN

print('===NOT==-')
a = True
b = not a
print('b not a = ', b)

# OR jika ada true maka akan memilih true

print('===OR===')
a = True
b = True
c = a or b
print(a, 'or', b,'   = ', c )
a = True
b = False
c = a or b
print(a, 'or', b,'  = ', c )
a = False
b = True
c = a or b
print(a, 'or', b,'  = ', c )
a = False
b = False
c = a or b
print(a, 'or', b,' = ', c )

#AND jika ada false maka akan memilih false

print('===AND===')
a = True
b = True
c = a and b
print(a, 'and', b,'   = ', c )
a = True
b = False
c = a and b
print(a, 'and', b,'  = ', c)
a = False
b = True
c = a and b
print(a, 'and', b,'  = ', c)
a = False
b = False
c = a and b
print(a, 'and', b,' = ', c)

print('===XOR===')
a = True
b = True
c = a ^ b
print(a, 'XOR', b,'   = ', c )
a = True
b = False
c = a ^ b
print(a, 'XOR', b,'  = ', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b,'  = ', c)
a = False
b = False
c = a ^ b
print(a, 'XOR', b,' = ', c)
a = False
b = True
d = False
e = True
c = a ^ b ^ d ^ e
print(a, 'XOR', b, 'XOR', d, 'XOR', e,' = ', c)

x = 65
print('id untuk x = ',id(x))
print('hex id untuk x = ', hex(id(x)))